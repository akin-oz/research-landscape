#!/usr/bin/env python3
"""Validate and project the Markdown-first Research Landscape knowledge graph.

This tool treats entity Markdown and view definitions as inputs. Generated views
and health reports are reproducible projections, never canonical facts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ENTITY_TYPES = {
    "principal-investigator", "research-group", "university", "department",
    "country", "research-ecosystem", "research-software", "research-area",
    "conference", "funding-program", "project", "publication", "organization",
}

ENTITY_DIRECTORIES = {
    "principal-investigator": "principal-investigators",
    "research-group": "research-groups",
    "university": "universities",
    "department": "departments",
    "country": "countries",
    "research-ecosystem": "ecosystems",
    "research-software": "research-software",
    "research-area": "research-areas",
    "conference": "conferences",
    "funding-program": "funding",
    "project": "projects",
    "publication": "publications",
    "organization": "organizations",
}

RELATION_TARGETS = {
    ("organization", "located_in"): {"country"},
    ("organization", "administers"): {"funding-program"},
    ("university", "located_in"): {"country"},
    ("research-group", "belongs_to"): {"university", "organization", "department"},
    ("research-group", "works_on"): {"research-area"},
    ("research-group", "develops"): {"research-software"},
    ("publication", "authored_by"): {"principal-investigator"},
    ("publication", "describes"): {"project", "research-software"},
    ("project", "involves"): {"principal-investigator", "research-group", "university", "organization"},
    ("project", "develops"): {"research-software"},
    ("project", "uses"): {"research-software"},
    ("project", "works_on"): {"research-area"},
    ("project", "produces"): {"publication"},
    ("principal-investigator", "affiliated_with"): {"university", "department", "organization"},
    ("principal-investigator", "leads"): {"research-group", "project"},
    ("principal-investigator", "works_on"): {"research-area"},
    ("principal-investigator", "develops"): {"research-software"},
    ("principal-investigator", "belongs_to"): {"research-group"},
    ("principal-investigator", "collaborates_with"): {"organization"},
    ("principal-investigator", "speaks_at"): {"conference"},
    ("department", "belongs_to"): {"university"},
    ("department", "works_on"): {"research-area"},
    ("conference", "covers"): {"research-area"},
    ("conference", "hosted_by"): {"organization", "university"},
    ("funding-program", "funds"): {"project"},
    ("research-ecosystem", "includes"): {"research-software"},
    ("research-ecosystem", "connects"): {
        "principal-investigator", "research-group", "research-software",
        "organization", "funding-program", "conference", "project",
    },
    ("research-area", "broader_than"): {"research-area"},
    ("research-software", "used_by"): {"research-group"},
}

REFERENCE_TYPES = {
    "country_id": {"country"}, "institution_id": {"university"},
    "institution_ids": {"university"}, "organization_id": {"organization"},
    "organization_ids": {"organization"}, "department_id": {"department"},
    "research_group_ids": {"research-group"},
    "principal_investigator_ids": {"principal-investigator"},
    "research_area_ids": {"research-area"}, "software_ids": {"research-software"},
    "ecosystem_ids": {"research-ecosystem"},
    "funding_program_ids": {"funding-program"}, "project_ids": {"project"},
    "conference_ids": {"conference"}, "publication_ids": {"publication"},
    "university_id": {"university"}, "host_organization_id": {"organization"},
    "funder_organization_id": {"organization"}, "parent_id": {"research-area"},
    "participant_ids": {"principal-investigator", "research-group", "university", "organization"},
    "affiliation_ids": {"university", "department", "organization"},
}

PUBLIC_VIEW_FILES = {
    "global": "global.md", "countries": "countries.md", "universities": "universities.md",
    "research-areas": "research-areas.md", "research-software": "research-software.md",
    "ecosystems": "ecosystems.md", "principal-investigators": "principal-investigators.md",
    "research-groups": "research-groups.md", "conferences": "conferences.md", "funding": "funding.md",
}

SOURCE_PATTERN = re.compile(r"`(SRC-[A-Z0-9-]+)`")
LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")


@dataclass(frozen=True)
class Record:
    path: Path
    metadata: dict[str, Any]
    body: str

    @property
    def id(self) -> str:
        return self.metadata["id"]

    @property
    def entity_type(self) -> str:
        return self.metadata["entity_type"]


@dataclass
class Results:
    errors: list[str]
    warnings: list[str]

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)


def frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError("unterminated YAML frontmatter")
    metadata = yaml.safe_load(parts[1])
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter must be a mapping")
    return metadata, parts[2]


def load_records(root: Path, results: Results) -> dict[str, Record]:
    records: dict[str, Record] = {}
    for path in sorted((root / "entities").glob("*/*.md")):
        if path.name == "README.md":
            continue
        try:
            metadata, body = frontmatter(path)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            results.error(f"{path.relative_to(root)}: {exc}")
            continue
        identifier = metadata.get("id")
        if not isinstance(identifier, str):
            results.error(f"{path.relative_to(root)}: missing string id")
            continue
        if identifier in records:
            results.error(
                f"{path.relative_to(root)}: duplicate id {identifier}; already owned by "
                f"{records[identifier].path.relative_to(root)}"
            )
            continue
        records[identifier] = Record(path, metadata, body)
    return records


def validate_schema(root: Path, records: dict[str, Record], results: Results) -> None:
    schema = json.loads((root / "schemas/entity-vnext.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for record in records.values():
        for error in validator.iter_errors(record.metadata):
            location = ".".join(str(part) for part in error.path) or "frontmatter"
            results.error(f"{record.path.relative_to(root)}: schema {location}: {error.message}")


def as_ids(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    return []


def validate_graph(root: Path, records: dict[str, Record], results: Results) -> None:
    for record in records.values():
        source_keys = set(SOURCE_PATTERN.findall(record.body))
        for source_id in as_ids(record.metadata.get("source_ids", [])):
            if source_id not in source_keys:
                results.error(f"{record.path.relative_to(root)}: source {source_id} missing from Evidence table")
        for field, expected_types in REFERENCE_TYPES.items():
            for target_id in as_ids(record.metadata.get(field, [])):
                target = records.get(target_id)
                if target is None:
                    results.error(f"{record.path.relative_to(root)}: unresolved {field} target {target_id}")
                elif target.entity_type not in expected_types:
                    results.error(
                        f"{record.path.relative_to(root)}: {field} target {target_id} has type "
                        f"{target.entity_type}, expected {sorted(expected_types)}"
                    )
        for assertion in record.metadata.get("relationship_assertions", []) or []:
            target_id = assertion.get("target_id")
            target = records.get(target_id)
            if target is None:
                results.error(f"{record.path.relative_to(root)}: unresolved relationship target {target_id}")
            else:
                allowed = RELATION_TARGETS.get((record.entity_type, assertion.get("predicate")), set())
                if target.entity_type not in allowed:
                    results.error(
                        f"{record.path.relative_to(root)}: invalid relation "
                        f"{record.entity_type} --{assertion.get('predicate')}--> {target.entity_type}"
                    )
            for source_id in as_ids(assertion.get("source_ids", [])):
                if source_id not in source_keys:
                    results.error(
                        f"{record.path.relative_to(root)}: relationship source {source_id} missing from Evidence table"
                    )
        if record.entity_type == "research-group" and record.metadata.get("status") in {"reviewed", "published"}:
            direct_fields = [field for field in ("institution_id", "organization_id") if field in record.metadata]
            if len(direct_fields) != 1:
                results.error(f"{record.path.relative_to(root)}: reviewed group requires exactly one direct-host field")
                continue
            field = direct_fields[0]
            host_id = record.metadata[field]
            expected_type = "university" if field == "institution_id" else "organization"
            host = records.get(host_id)
            if host is None or host.entity_type != expected_type:
                results.error(f"{record.path.relative_to(root)}: direct host {host_id} must resolve to {expected_type}")
            matches = [
                assertion for assertion in record.metadata.get("relationship_assertions", [])
                if assertion.get("predicate") == "belongs_to" and assertion.get("target_id") == host_id
            ]
            if len(matches) != 1:
                results.error(f"{record.path.relative_to(root)}: direct host {host_id} requires one matching belongs_to assertion")


def validate_migration(root: Path, records: dict[str, Record], results: Results) -> None:
    """Keep v2 canonical records in their one approved entity namespace."""
    for record in records.values():
        expected_directory = ENTITY_DIRECTORIES.get(record.entity_type)
        if expected_directory is None:
            results.error(f"{record.path.relative_to(root)}: unsupported entity type {record.entity_type}")
        elif record.path.parent.name != expected_directory:
            results.error(
                f"{record.path.relative_to(root)}: {record.entity_type} must live in "
                f"entities/{expected_directory}/"
            )
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts or "entities" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        try:
            metadata, _ = frontmatter(path)
        except (ValueError, yaml.YAMLError):
            continue
        if metadata.get("schema_version") == 2:
            results.error(
                f"{path.relative_to(root)}: v2 entity frontmatter must be migrated into entities/"
            )


def validate_links(root: Path, results: Results) -> None:
    skipped = {".git", ".idea"}
    for path in sorted(root.rglob("*.md")):
        if any(part in skipped for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith(("mailto:", "tel:", "data:")):
                continue
            if not (path.parent / target).resolve().exists():
                results.error(f"{path.relative_to(root)}: broken local Markdown link {raw_target}")


def quality_warnings(root: Path, records: dict[str, Record], results: Results) -> None:
    normalized: dict[tuple[str, str], list[Record]] = defaultdict(list)
    inbound = Counter()
    for record in records.values():
        normalized[(record.entity_type, record.metadata.get("name", "").casefold().strip())].append(record)
        for assertion in record.metadata.get("relationship_assertions", []) or []:
            if assertion.get("target_id") in records:
                inbound[assertion["target_id"]] += 1
        for field in REFERENCE_TYPES:
            for target_id in as_ids(record.metadata.get(field, [])):
                if target_id in records:
                    inbound[target_id] += 1
    for (entity_type, name), owners in sorted(normalized.items()):
        if name and len(owners) > 1:
            locations = ", ".join(str(owner.path.relative_to(root)) for owner in owners)
            results.warning(f"possible duplicate {entity_type} name '{name}': {locations}")
    for record in records.values():
        assertions = record.metadata.get("relationship_assertions", []) or []
        if not assertions and not inbound[record.id] and record.entity_type not in {"country", "research-area"}:
            results.warning(f"orphan entity: {record.id} ({record.path.relative_to(root)})")


def validate(root: Path) -> tuple[dict[str, Record], Results]:
    results = Results([], [])
    records = load_records(root, results)
    validate_schema(root, records, results)
    validate_graph(root, records, results)
    validate_migration(root, records, results)
    validate_links(root, results)
    quality_warnings(root, records, results)
    return records, results


def input_fingerprint(root: Path) -> str:
    digest = hashlib.sha256()
    inputs = [root / "views/definitions.yaml", root / "schemas/entity-vnext.schema.json"]
    inputs.extend(sorted((root / "entities").glob("*/*.md")))
    for path in inputs:
        if path.name == "README.md":
            continue
        digest.update(str(path.relative_to(root)).encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def eligible(record: Record) -> bool:
    return record.metadata.get("status") in {"reviewed", "published"} and record.metadata.get("confidence") in {"high", "medium"}


def relation_targets(record: Record, predicate: str | None = None) -> list[str]:
    targets = []
    for assertion in record.metadata.get("relationship_assertions", []) or []:
        if predicate is None or assertion.get("predicate") == predicate:
            targets.append(assertion["target_id"])
    return sorted(set(targets))


def metadata_or_relation_ids(record: Record, field: str, predicate: str, target_type: str, records: dict[str, Record]) -> list[str]:
    values = set(as_ids(record.metadata.get(field, [])))
    for target_id in relation_targets(record, predicate):
        target = records.get(target_id)
        if target and target.entity_type == target_type:
            values.add(target_id)
    return sorted(values)


def resolved_countries(record: Record, records: dict[str, Record], seen: set[str] | None = None) -> list[str]:
    seen = set() if seen is None else seen
    if record.id in seen:
        return []
    seen.add(record.id)
    countries = set(as_ids(record.metadata.get("country_id", [])))
    for assertion in record.metadata.get("relationship_assertions", []) or []:
        target = records.get(assertion.get("target_id"))
        if target and target.entity_type == "country":
            countries.add(target.id)
    for field in ("institution_id", "organization_id", "university_id"):
        for target_id in as_ids(record.metadata.get(field, [])):
            target = records.get(target_id)
            if target:
                countries.update(resolved_countries(target, records, seen))
    if record.entity_type == "principal-investigator":
        for target_id in as_ids(record.metadata.get("affiliation_ids", [])):
            target = records.get(target_id)
            if target:
                countries.update(resolved_countries(target, records, seen))
    return sorted(countries)


def canonical_link(record: Record, output_path: Path) -> str:
    relative = os.path.relpath(record.path, output_path.parent).replace(os.sep, "/")
    return f"[{record.metadata['name']}]({relative})"


def clean(value: Any) -> str:
    if isinstance(value, list):
        return ", ".join(map(str, value)) or "—"
    if value in (None, ""):
        return "—"
    return str(value).replace("|", "\\|")


def rows(records: list[Record], output_path: Path, all_records: dict[str, Record]) -> list[str]:
    result = ["| Entity | ID | Type | Confidence | Last review | Resolved country |", "| --- | --- | --- | --- | --- | --- |"]
    for record in sorted(records, key=lambda item: (item.entity_type, item.metadata["name"].casefold(), item.id)):
        result.append(
            f"| {canonical_link(record, output_path)} | `{record.id}` | {record.entity_type} | "
            f"{clean(record.metadata.get('confidence'))} | {clean(record.metadata.get('last_review'))} | "
            f"{clean(resolved_countries(record, all_records))} |"
        )
    return result


def related_to(target_id: str, records: dict[str, Record]) -> list[Record]:
    related = []
    for record in records.values():
        fields = ("institution_id", "organization_id", "university_id", "research_area_ids", "software_ids", "ecosystem_ids", "funding_program_ids", "project_ids", "conference_ids")
        if any(target_id in as_ids(record.metadata.get(field, [])) for field in fields):
            related.append(record)
            continue
        if target_id in relation_targets(record):
            related.append(record)
    return related


def render_view(view: dict[str, Any], records: dict[str, Record], output_path: Path, fingerprint: str) -> str:
    title = view["view_id"].replace("-", " ").title()
    lines = [
        "<!-- GENERATED FILE: edit entities or views/definitions.yaml, then regenerate. -->",
        f"<!-- input-fingerprint: {fingerprint} -->",
        f"# {title} view",
        "",
        f"**Definition:** `{view['view_id']}`",
        f"**Input fingerprint:** `{fingerprint}`",
        "**Status:** deterministic generated projection; canonical facts and evidence remain in `entities/`.",
        "",
    ]
    selected = [record for record in records.values() if eligible(record) and record.entity_type in set(view["scope"])]
    view_id = view["view_id"]
    if view_id in {"global", "principal-investigators", "research-groups"}:
        lines.extend(rows(selected, output_path, records))
    elif view_id == "countries":
        for country in sorted((r for r in selected if r.entity_type == "country"), key=lambda r: r.metadata["name"].casefold()):
            members = [record for record in selected if country.id in resolved_countries(record, records)]
            lines.extend([f"## {canonical_link(country, output_path)}", ""])
            lines.extend(rows(members, output_path, records))
            lines.append("")
    elif view_id == "research-areas":
        for area in sorted((r for r in selected if r.entity_type == "research-area"), key=lambda r: r.metadata["name"].casefold()):
            members = [record for record in selected if area.id in metadata_or_relation_ids(record, "research_area_ids", "works_on", "research-area", records) or area.id in relation_targets(record, "covers")]
            lines.extend([f"## {canonical_link(area, output_path)}", ""])
            lines.extend(rows(members, output_path, records))
            lines.append("")
    elif view_id in {"universities", "research-software", "ecosystems", "conferences", "funding"}:
        primary_type = {"universities": "university", "research-software": "research-software", "ecosystems": "research-ecosystem", "conferences": "conference", "funding": "funding-program"}[view_id]
        for primary in sorted((r for r in selected if r.entity_type == primary_type), key=lambda r: r.metadata["name"].casefold()):
            members = [primary, *related_to(primary.id, records)]
            unique = {record.id: record for record in members if eligible(record)}
            lines.extend([f"## {canonical_link(primary, output_path)}", ""])
            lines.extend(rows(list(unique.values()), output_path, records))
            lines.append("")
    else:
        raise ValueError(f"unsupported public view {view_id}")
    lines.extend([
        "## Boundary",
        "",
        "Membership and ordering come only from the declared view definition and canonical frontmatter/relationships. A missing connection is unknown; this output does not claim openings, mentorship, funding availability, language, or personal fit.",
        "",
    ])
    return "\n".join(lines)


def health_report(root: Path, records: dict[str, Record], results: Results, fingerprint: str) -> str:
    by_type = Counter(record.entity_type for record in records.values())
    by_confidence = Counter(record.metadata.get("confidence", "unassessed") for record in records.values())
    predicates = Counter(
        assertion.get("predicate") for record in records.values()
        for assertion in record.metadata.get("relationship_assertions", []) or []
    )
    relationships = sum(predicates.values())
    lines = [
        "<!-- GENERATED FILE: edit canonical inputs, then regenerate. -->",
        f"<!-- input-fingerprint: {fingerprint} -->",
        "# Repository health report",
        "",
        f"**Input fingerprint:** `{fingerprint}`",
        "**Status:** deterministic generated projection; this report owns no entity facts.",
        "",
        "## Summary",
        "",
        f"- Canonical v2 entities: **{len(records)}**",
        f"- Typed relationship assertions: **{relationships}**",
        f"- Validation errors: **{len(results.errors)}**",
        f"- Health warnings: **{len(results.warnings)}**",
        "",
        "## Entity types",
        "",
        "| Type | Count |", "| --- | ---: |",
        *[f"| {entity_type} | {count} |" for entity_type, count in sorted(by_type.items())],
        "",
        "## Confidence coverage",
        "",
        "| Confidence | Count |", "| --- | ---: |",
        *[f"| {confidence} | {count} |" for confidence, count in sorted(by_confidence.items())],
        "",
        "## Migration integrity",
        "",
        f"- Canonical v2 records in approved entity directories: **{len(records)}**",
        "- v2 frontmatter outside `entities/`: **0** when validation passes.",
        "",
        "## Relationship predicates",
        "",
        "| Predicate | Count |", "| --- | ---: |",
        *[f"| {predicate} | {count} |" for predicate, count in sorted(predicates.items())],
        "",
        "## Findings",
        "",
    ]
    if results.errors:
        lines.extend([f"- **Error:** {error}" for error in results.errors])
    else:
        lines.append("- No structural validation errors.")
    if results.warnings:
        lines.extend([f"- **Warning:** {warning}" for warning in results.warnings])
    else:
        lines.append("- No duplicate-name or orphan-entity warnings.")
    lines.extend([
        "",
        "## Interpretation boundary",
        "",
        "Counts and warnings are maintenance signals. They are not research-quality, prestige, mentorship, or recommendation scores. Correct facts in canonical entities and rerun this tool; do not edit this generated report.",
        "",
    ])
    return "\n".join(lines)


def write_or_check(path: Path, content: str, check: bool, drift: list[str]) -> None:
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            drift.append(str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def generate(root: Path, check: bool) -> int:
    records, results = validate(root)
    if results.errors:
        print_results(root, records, results)
        return 1
    manifest = yaml.safe_load((root / "views/definitions.yaml").read_text(encoding="utf-8"))
    fingerprint = input_fingerprint(root)
    drift: list[str] = []
    generated = root / "views/generated"
    for view in manifest["views"]:
        if view["visibility"] != "public":
            continue
        output = generated / PUBLIC_VIEW_FILES[view["view_id"]]
        write_or_check(output, render_view(view, records, output, fingerprint), check, drift)
    readme = "\n".join([
        "<!-- GENERATED FILE: edit canonical inputs, then regenerate. -->",
        f"<!-- input-fingerprint: {fingerprint} -->",
        "# Generated views",
        "",
        "These are reproducible public navigation projections from `entities/` and `views/definitions.yaml`. They contain concise metadata and canonical links only. Private views intentionally produce no output.",
        "",
        "Do not edit these files manually. Run `python3 scripts/research_landscape.py generate` after changing canonical inputs, then use `--check` in CI to detect drift.",
        "",
    ])
    write_or_check(generated / "README.md", readme, check, drift)
    write_or_check(root / "reports/generated/repository-health.md", health_report(root, records, results, fingerprint), check, drift)
    if drift:
        print("Generated output is stale or missing:")
        print("\n".join(f"- {Path(path).relative_to(root)}" for path in drift))
        return 1
    print_results(root, records, results)
    print("Generated views and repository health report are in sync." if check else "Generated views and repository health report.")
    return 0


def print_results(root: Path, records: dict[str, Record], results: Results) -> None:
    relationships = sum(len(record.metadata.get("relationship_assertions", []) or []) for record in records.values())
    print(f"Validated {len(records)} v2 entities and {relationships} typed relationship assertions.")
    for error in results.errors:
        print(f"ERROR: {error}")
    for warning in results.warnings:
        print(f"WARNING: {warning}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "generate", "health"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="fail if generated output differs from canonical inputs")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.command == "validate":
        records, results = validate(root)
        print_results(root, records, results)
        return 1 if results.errors else 0
    return generate(root, args.check)


if __name__ == "__main__":
    raise SystemExit(main())
