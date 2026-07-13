#!/usr/bin/env python3
"""Validate and project the Markdown-first Research Landscape knowledge graph.

This tool treats entity Markdown and view definitions as inputs. Generated views
and health reports are reproducible projections, never canonical facts.
"""

from __future__ import annotations

import argparse
import datetime as dt
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
    "conference", "funding-program", "project", "publication", "organization", "programming-language",
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
    "programming-language": "programming-languages",
}

RELATION_TARGETS = {
    ("organization", "located_in"): {"country"},
    ("organization", "administers"): {"funding-program"},
    ("university", "located_in"): {"country"},
    ("research-group", "belongs_to"): {"university", "organization", "department"},
    ("research-group", "works_on"): {"research-area"},
    ("research-group", "develops"): {"research-software"},
    ("publication", "authored_by"): {"principal-investigator"},
    ("publication", "addresses"): {"research-area"},
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
    ("research-software", "implemented_in"): {"programming-language"},
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
    "programming_language_ids": {"programming-language"},
}

PUBLIC_VIEW_FILES = {
    "global": "global.md", "countries": "countries.md", "universities": "universities.md",
    "research-areas": "research-areas.md", "research-software": "research-software.md",
    "ecosystems": "ecosystems.md", "principal-investigators": "principal-investigators.md",
    "research-groups": "research-groups.md", "conferences": "conferences.md", "funding": "funding.md",
}

RECOMMENDATION_KINDS = {
    "groups-with-software", "groups-by-area", "groups-with-open-source-software",
    "groups-with-software-and-area", "ecosystems-connected-to-area",
    "principal-investigators-by-area", "principal-investigators-with-open-source-software",
    "universities-hosting-groups-by-area",
    "groups-with-software-language", "entities-with-mentorship-process-evidence",
}
RECOMMENDATION_REQUIRED_FILTERS = {
    "groups-by-area": ("area_id",),
    "ecosystems-connected-to-area": ("area_id",),
    "principal-investigators-by-area": ("area_id",),
    "universities-hosting-groups-by-area": ("area_id",),
    "groups-with-software-and-area": ("area_ids",),
    "groups-with-software-language": ("language_id",),
}

MENTORSHIP_PROCESS_CATEGORIES = {
    "written-expectations", "onboarding-training", "supervision-process",
    "professional-development", "aggregate-outcomes",
}
MENTORSHIP_PROCESS_ENTITY_TYPES = {"research-group", "department", "university", "organization"}
MENTORSHIP_PROCESS_CONFIDENCES = {"high", "medium", "low"}

LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")
EVIDENCE_SECTION_PATTERN = re.compile(r"^## Evidence\s*$([\s\S]*?)(?=^## |\Z)", re.MULTILINE)
EVIDENCE_SOURCE_ROW_PATTERN = re.compile(r"^\|\s*`(SRC-[A-Z0-9-]+)`\s*\|\s*(.*?)\s*\|\s*$", re.MULTILINE)
PUBLIC_LOCATOR_PATTERN = re.compile(r"https?://")
ACCESS_DATE_PATTERN = re.compile(r"\bAccessed\s+(\d{4}-\d{2}-\d{2})\b", re.IGNORECASE)

# These intervals implement docs/freshness-policy.md. They classify maintenance
# attention only; they do not downgrade source quality or entity confidence.
REVIEW_CURRENT_DAYS = 180
REVIEW_STALE_DAYS = 365
VOLATILE_DUE_SOON_DAYS = 30
OPEN_SOURCE_FILTER_VALUES = {"yes", "no", "mixed", "unknown", "not-applicable"}


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


def evidence_table_sources(body: str) -> list[tuple[str, str]]:
    """Return source IDs and evidence text from dedicated Evidence-table rows.

    Source identifiers mentioned in narrative, limitations, or code examples do
    not resolve a claim. The table is the canonical local citation registry.
    """
    section = EVIDENCE_SECTION_PATTERN.search(body)
    if section is None:
        return []
    return EVIDENCE_SOURCE_ROW_PATTERN.findall(section.group(1))


def evidence_table_source_ids(body: str) -> list[str]:
    return [source_id for source_id, _ in evidence_table_sources(body)]


def validate_graph(root: Path, records: dict[str, Record], results: Results) -> None:
    for record in records.values():
        evidence_sources = evidence_table_sources(record.body)
        evidence_source_ids = [source_id for source_id, _ in evidence_sources]
        source_keys = set(evidence_source_ids)
        if len(evidence_source_ids) != len(source_keys):
            results.error(f"{record.path.relative_to(root)}: duplicate source ID in Evidence table")
        for source_id, evidence in evidence_sources:
            if not PUBLIC_LOCATOR_PATTERN.search(evidence):
                results.error(
                    f"{record.path.relative_to(root)}: Evidence source {source_id} missing public URL"
                )
            access_date = ACCESS_DATE_PATTERN.search(evidence)
            if access_date is None:
                results.error(
                    f"{record.path.relative_to(root)}: Evidence source {source_id} missing access date"
                )
            else:
                try:
                    dt.date.fromisoformat(access_date.group(1))
                except ValueError:
                    results.error(
                        f"{record.path.relative_to(root)}: Evidence source {source_id} has invalid access date"
                    )
        for source_id in as_ids(record.metadata.get("source_ids", [])):
            if source_id not in source_keys:
                results.error(f"{record.path.relative_to(root)}: source {source_id} missing from Evidence table")
        for source_id in as_ids(record.metadata.get("lifecycle_source_ids", [])):
            if source_id not in source_keys:
                results.error(
                    f"{record.path.relative_to(root)}: lifecycle source {source_id} missing from Evidence table"
                )
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
        if record.entity_type == "research-software":
            asserted_languages = {
                assertion.get("target_id")
                for assertion in record.metadata.get("relationship_assertions", []) or []
                if assertion.get("predicate") == "implemented_in"
            }
            for language_id in as_ids(record.metadata.get("programming_language_ids", [])):
                if language_id not in asserted_languages:
                    results.error(
                        f"{record.path.relative_to(root)}: programming_language_ids target {language_id} requires matching implemented_in assertion"
                    )
        observations = record.metadata.get("mentorship_process_evidence", []) or []
        if observations and record.entity_type not in MENTORSHIP_PROCESS_ENTITY_TYPES:
            results.error(f"{record.path.relative_to(root)}: mentorship_process_evidence is not permitted for {record.entity_type}")
        for observation in observations:
            if not isinstance(observation, dict):
                results.error(f"{record.path.relative_to(root)}: mentorship-process observation must be a mapping")
                continue
            category = observation.get("category")
            if category not in MENTORSHIP_PROCESS_CATEGORIES:
                results.error(f"{record.path.relative_to(root)}: mentorship-process category must be controlled: {category}")
            if not as_ids(observation.get("source_ids", [])):
                results.error(f"{record.path.relative_to(root)}: mentorship-process observation requires source_ids")
            for field in ("scope", "limitation"):
                if not isinstance(observation.get(field), str) or not observation[field].strip():
                    results.error(f"{record.path.relative_to(root)}: mentorship-process observation requires non-empty {field}")
            if not any(isinstance(observation.get(field), str) and observation[field].strip() for field in ("evidence_window", "review_date")):
                results.error(f"{record.path.relative_to(root)}: mentorship-process observation requires evidence_window or review_date")
            if observation.get("confidence") not in MENTORSHIP_PROCESS_CONFIDENCES:
                results.error(f"{record.path.relative_to(root)}: mentorship-process confidence must be high, medium, or low")
            for source_id in as_ids(observation.get("source_ids", [])):
                if source_id not in source_keys:
                    results.error(
                        f"{record.path.relative_to(root)}: mentorship-process source {source_id} missing from Evidence table"
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


def recommendation_fingerprint(root: Path) -> str:
    digest = hashlib.sha256()
    inputs = [
        root / "scoring/v1/evidence-recommendations.yaml",
        root / "schemas/entity-vnext.schema.json",
    ]
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
            members = [
                record for record in selected
                if area.id in metadata_or_relation_ids(record, "research_area_ids", "works_on", "research-area", records)
                or area.id in relation_targets(record, "covers")
                or area.id in relation_targets(record, "addresses")
            ]
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
    reviewed = [record for record in records.values() if record.metadata.get("status") in {"reviewed", "published"}]
    records_with_sources = sum(bool(record.metadata.get("source_ids")) for record in reviewed)
    records_with_last_review = sum(bool(record.metadata.get("last_review")) for record in reviewed)
    sourced_relationships = sum(
        bool(assertion.get("source_ids"))
        for record in records.values()
        for assertion in record.metadata.get("relationship_assertions", []) or []
    )
    reviewed_groups = [record for record in reviewed if record.entity_type == "research-group"]
    valid_host_groups = sum(
        len([field for field in ("institution_id", "organization_id") if field in record.metadata]) == 1
        for record in reviewed_groups
    )
    incoming = Counter()
    for record in records.values():
        for target_id in relation_targets(record):
            incoming[target_id] += 1
        for field in REFERENCE_TYPES:
            for target_id in as_ids(record.metadata.get(field, [])):
                incoming[target_id] += 1
    connected = sum(
        bool(record.metadata.get("relationship_assertions")) or incoming[record.id] > 0
        for record in records.values()
    )
    view_manifest = yaml.safe_load((root / "views/definitions.yaml").read_text(encoding="utf-8"))
    view_definitions = view_manifest.get("views", [])
    public_views = [view for view in view_definitions if view.get("visibility") == "public"]
    private_views = [view for view in view_definitions if view.get("visibility") == "private"]
    recommendation_model, recommendation_errors = validate_recommendation_model(root, records)
    recommendation_queries = recommendation_model.get("queries", []) if not recommendation_errors else []
    available_queries = [query for query in recommendation_queries if query.get("status") != "unavailable"]
    unavailable_queries = [query for query in recommendation_queries if query.get("status") == "unavailable"]
    area_coverage = research_area_coverage(records)
    language_coverage = programming_language_coverage(records)
    broken_links = sum("broken local Markdown link" in error for error in results.errors)
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
        "## Quality coverage",
        "",
        "| Metric | Result |",
        "| --- | ---: |",
        f"| Reviewed/published records with source IDs | {records_with_sources}/{len(reviewed)} |",
        f"| Reviewed/published records with last-review dates | {records_with_last_review}/{len(reviewed)} |",
        f"| Typed relationships with source IDs | {sourced_relationships}/{relationships} |",
        f"| Reviewed groups with exactly one direct-host field | {valid_host_groups}/{len(reviewed_groups)} |",
        f"| Entities with an inbound or outbound graph connection | {connected}/{len(records)} |",
        f"| Broken local Markdown links | {broken_links} |",
        f"| Canonical view definitions (public/private) | {len(view_definitions)} ({len(public_views)}/{len(private_views)}) |",
        f"| Generated public views | {len(PUBLIC_VIEW_FILES)}/{len(public_views)} |",
        f"| Recommendation queries (available/unavailable) | {len(recommendation_queries)} ({len(available_queries)}/{len(unavailable_queries)}) |",
        "",
        "## Research-area discovery coverage",
        "",
        "These are counts of direct, documented graph paths. They measure current corpus coverage, not research quality, prominence, or priority.",
        "",
        "| Research area | Groups | Principal Investigators | Research Software | Direct-host Universities | Ecosystems |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
        *[
            f"| {canonical_link(item['area'], root / 'reports/generated/repository-health.md')} | "
            f"{item['groups']} | {item['principal_investigators']} | {item['software']} | "
            f"{item['universities']} | {item['ecosystems']} |"
            for item in area_coverage
        ],
        "",
        "## Programming-language discovery coverage",
        "",
        "These are counts of direct, documented implementation paths. They measure corpus coverage, not software quality, adoption, a group's universal language, an individual's skill, or a recommendation.",
        "",
        "| Programming language | Research Software | Research Groups | Principal Investigators | Direct-host Universities | Ecosystems |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
        *[
            f"| {canonical_link(item['language'], root / 'reports/generated/repository-health.md')} | "
            f"{item['software']} | {item['groups']} | {item['principal_investigators']} | "
            f"{item['universities']} | {item['ecosystems']} |"
            for item in language_coverage
        ],
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


def confidence_value(value: str | None) -> int:
    return {"high": 3, "medium": 2, "low": 1, "unassessed": 0, "unavailable": 0}.get(value or "unassessed", 0)


def lowest_confidence(values: list[str]) -> str:
    labels = [value for value in values if value]
    if not labels:
        return "unavailable"
    return min(labels, key=confidence_value)


def matching_assertions(record: Record, predicate: str, target_ids: set[str] | None = None) -> list[dict[str, Any]]:
    matches = []
    for assertion in record.metadata.get("relationship_assertions", []) or []:
        if assertion.get("predicate") != predicate:
            continue
        if target_ids is not None and assertion.get("target_id") not in target_ids:
            continue
        matches.append(assertion)
    return matches


def research_area_coverage(records: dict[str, Record]) -> list[dict[str, Any]]:
    """Summarize current direct discovery paths by controlled research area.

    The counts intentionally distinguish canonical relation types instead of
    collapsing them into a score. A zero is a coverage gap, not a negative
    statement about the area or its research environments.
    """
    coverage = []
    for area in sorted(
        (record for record in records.values() if record.entity_type == "research-area" and eligible(record)),
        key=lambda record: (record.metadata["name"].casefold(), record.id),
    ):
        groups = [
            record for record in records.values()
            if record.entity_type == "research-group" and eligible(record)
            and matching_assertions(record, "works_on", {area.id})
        ]
        principal_investigators = [
            record for record in records.values()
            if record.entity_type == "principal-investigator" and eligible(record)
            and matching_assertions(record, "works_on", {area.id})
        ]
        software = [
            record for record in records.values()
            if record.entity_type == "research-software" and eligible(record)
            and area.id in as_ids(record.metadata.get("research_area_ids", []))
        ]
        universities = [
            university for university in records.values()
            if university.entity_type == "university" and eligible(university)
            and any(
                group.metadata.get("institution_id") == university.id
                and matching_assertions(group, "works_on", {area.id})
                for group in groups
            )
        ]
        ecosystems = []
        for ecosystem in records.values():
            if ecosystem.entity_type != "research-ecosystem" or not eligible(ecosystem):
                continue
            connected_to_area = any(
                (target := records.get(assertion.get("target_id"))) is not None
                and bool(matching_assertions(target, "works_on", {area.id}))
                for assertion in matching_assertions(ecosystem, "connects")
            )
            includes_area_software = any(
                (software_record := records.get(assertion.get("target_id"))) is not None
                and software_record.entity_type == "research-software"
                and area.id in as_ids(software_record.metadata.get("research_area_ids", []))
                for assertion in matching_assertions(ecosystem, "includes")
            )
            if connected_to_area or includes_area_software:
                ecosystems.append(ecosystem)
        coverage.append({
            "area": area,
            "groups": len(groups),
            "principal_investigators": len(principal_investigators),
            "software": len(software),
            "universities": len(universities),
            "ecosystems": len(ecosystems),
        })
    return coverage


def programming_language_coverage(records: dict[str, Record]) -> list[dict[str, Any]]:
    """Summarize direct, documented implementation-language discovery paths.

    The table is a corpus-maintenance signal. It intentionally uses only
    software `implemented_in` assertions and the source-bearing paths that
    traverse those software records; it does not infer a person's skill or a
    group's universal working language.
    """
    coverage = []
    for language in sorted(
        (record for record in records.values() if record.entity_type == "programming-language" and eligible(record)),
        key=lambda record: (record.metadata["name"].casefold(), record.id),
    ):
        software = [
            record for record in records.values()
            if record.entity_type == "research-software" and eligible(record)
            and matching_assertions(record, "implemented_in", {language.id})
        ]
        software_ids = {record.id for record in software}
        groups = [
            record for record in records.values()
            if record.entity_type == "research-group" and eligible(record)
            and matching_assertions(record, "develops", software_ids)
        ]
        principal_investigators = [
            record for record in records.values()
            if record.entity_type == "principal-investigator" and eligible(record)
            and matching_assertions(record, "develops", software_ids)
        ]
        universities = [
            university for university in records.values()
            if university.entity_type == "university" and eligible(university)
            and any(
                group.metadata.get("institution_id") == university.id
                and matching_assertions(group, "develops", software_ids)
                for group in groups
            )
        ]
        ecosystems = [
            ecosystem for ecosystem in records.values()
            if ecosystem.entity_type == "research-ecosystem" and eligible(ecosystem)
            and matching_assertions(ecosystem, "includes", software_ids)
        ]
        coverage.append({
            "language": language,
            "software": len(software),
            "groups": len(groups),
            "principal_investigators": len(principal_investigators),
            "universities": len(universities),
            "ecosystems": len(ecosystems),
        })
    return coverage


def signal(label: str, assertion: dict[str, Any], owner: Record) -> dict[str, Any]:
    sources = ", ".join(assertion.get("source_ids", [])) or "no-source-id"
    return {
        "label": label,
        "sources": sources,
        "confidence": lowest_confidence([owner.metadata.get("confidence"), assertion.get("confidence")]),
    }


def metadata_signal(label: str, owner: Record) -> dict[str, Any]:
    """Render record-level metadata evidence without inventing an edge."""
    sources = ", ".join(as_ids(owner.metadata.get("source_ids", []))) or "no-source-id"
    return {
        "label": label,
        "sources": sources,
        "confidence": owner.metadata.get("confidence", "unassessed"),
    }


def recommendation_candidates(query: dict[str, Any], records: dict[str, Record]) -> list[dict[str, Any]]:
    kind = query.get("kind")
    candidates: list[dict[str, Any]] = []
    if kind == "groups-with-software":
        for record in records.values():
            if record.entity_type != "research-group" or not eligible(record):
                continue
            signals = [signal(f"develops `{a['target_id']}`", a, record) for a in matching_assertions(record, "develops")]
            if signals:
                candidates.append({"record": record, "signals": signals, "criteria": 1})
    elif kind == "groups-by-area":
        area_ids = {query["area_id"]}
        for record in records.values():
            if record.entity_type != "research-group" or not eligible(record):
                continue
            signals = [signal(f"works on `{a['target_id']}`", a, record) for a in matching_assertions(record, "works_on", area_ids)]
            if signals:
                candidates.append({"record": record, "signals": signals, "criteria": 1})
    elif kind == "groups-with-open-source-software":
        for record in records.values():
            if record.entity_type != "research-group" or not eligible(record):
                continue
            signals = []
            for assertion in matching_assertions(record, "develops"):
                software = records.get(assertion["target_id"])
                if software and software.metadata.get("open_source") == "yes" and software.metadata.get("license"):
                    signals.append(signal(f"develops licensed open-source `{software.id}`", assertion, record))
            if signals:
                candidates.append({"record": record, "signals": signals, "criteria": 1})
    elif kind == "groups-with-software-and-area":
        area_ids = set(query["area_ids"])
        for record in records.values():
            if record.entity_type != "research-group" or not eligible(record):
                continue
            software_signals = [signal(f"develops `{a['target_id']}`", a, record) for a in matching_assertions(record, "develops")]
            area_signals = [signal(f"works on `{a['target_id']}`", a, record) for a in matching_assertions(record, "works_on", area_ids)]
            if software_signals and area_signals:
                candidates.append({"record": record, "signals": software_signals + area_signals, "criteria": 2})
    elif kind == "groups-with-software-language":
        language_id = query["language_id"]
        for record in records.values():
            if record.entity_type != "research-group" or not eligible(record):
                continue
            signals = []
            for development in matching_assertions(record, "develops"):
                software = records.get(development["target_id"])
                if software is None or software.entity_type != "research-software":
                    continue
                for implementation in matching_assertions(software, "implemented_in", {language_id}):
                    signals.append(signal(f"develops `{software.id}`", development, record))
                    signals.append(signal(f"`{software.id}` is implemented in `{language_id}`", implementation, software))
            if signals:
                candidates.append({"record": record, "signals": signals, "criteria": 2})
    elif kind == "entities-with-mentorship-process-evidence":
        for record in records.values():
            if record.entity_type not in {"research-group", "department", "university", "organization"} or not eligible(record):
                continue
            signals = []
            for observation in record.metadata.get("mentorship_process_evidence", []) or []:
                sources = ", ".join(as_ids(observation.get("source_ids", [])))
                signals.append({
                    "label": f"documents `{observation['category']}` for {observation['scope']}",
                    "sources": sources,
                    "confidence": lowest_confidence([record.metadata.get("confidence"), observation.get("confidence")]),
                })
            if signals:
                candidates.append({"record": record, "signals": signals, "criteria": 1})
    elif kind == "principal-investigators-by-area":
        area_ids = {query["area_id"]}
        for record in records.values():
            if record.entity_type != "principal-investigator" or not eligible(record):
                continue
            signals = [signal(f"works on `{a['target_id']}`", a, record) for a in matching_assertions(record, "works_on", area_ids)]
            if signals:
                candidates.append({"record": record, "signals": signals, "criteria": 1})
    elif kind == "principal-investigators-with-open-source-software":
        for record in records.values():
            if record.entity_type != "principal-investigator" or not eligible(record):
                continue
            signals = []
            for assertion in matching_assertions(record, "develops"):
                software = records.get(assertion["target_id"])
                if software and software.metadata.get("open_source") == "yes" and software.metadata.get("license"):
                    signals.append(signal(f"develops licensed open-source `{software.id}`", assertion, record))
            if signals:
                candidates.append({"record": record, "signals": signals, "criteria": 1})
    elif kind == "universities-hosting-groups-by-area":
        area_ids = {query["area_id"]}
        for university in records.values():
            if university.entity_type != "university" or not eligible(university):
                continue
            signals = []
            for group in records.values():
                if group.entity_type != "research-group" or not eligible(group):
                    continue
                host_assertions = matching_assertions(group, "belongs_to", {university.id})
                area_assertions = matching_assertions(group, "works_on", area_ids)
                for host_assertion in host_assertions:
                    for area_assertion in area_assertions:
                        signals.append(signal(f"hosts `{group.id}`", host_assertion, group))
                        signals.append(signal(f"`{group.id}` works on `{area_assertion['target_id']}`", area_assertion, group))
            if signals:
                candidates.append({"record": university, "signals": signals, "criteria": 2})
    elif kind == "ecosystems-connected-to-area":
        area_ids = {query["area_id"]}
        for ecosystem in records.values():
            if ecosystem.entity_type != "research-ecosystem" or not eligible(ecosystem):
                continue
            signals = []
            for connection in matching_assertions(ecosystem, "connects"):
                target = records.get(connection["target_id"])
                if not target:
                    continue
                for area_assertion in matching_assertions(target, "works_on", area_ids):
                    signals.append(signal(f"connects `{target.id}`", connection, ecosystem))
                    signals.append(signal(f"`{target.id}` works on `{area_assertion['target_id']}`", area_assertion, target))
            for inclusion in matching_assertions(ecosystem, "includes"):
                software = records.get(inclusion["target_id"])
                if not software or software.entity_type != "research-software":
                    continue
                matched_areas = set(as_ids(software.metadata.get("research_area_ids", []))) & area_ids
                for area_id in sorted(matched_areas):
                    signals.append(signal(f"includes `{software.id}`", inclusion, ecosystem))
                    signals.append(metadata_signal(f"`{software.id}` is classified in `{area_id}`", software))
            if signals:
                candidates.append({"record": ecosystem, "signals": signals, "criteria": 2})
    else:
        raise ValueError(f"unsupported recommendation kind {kind}")
    return sorted(
        candidates,
        key=lambda item: (-len(item["signals"]), item["record"].metadata["name"].casefold(), item["record"].id),
    )


def validate_recommendation_model(root: Path, records: dict[str, Record]) -> tuple[dict[str, Any], list[str]]:
    model = yaml.safe_load((root / "scoring/v1/evidence-recommendations.yaml").read_text(encoding="utf-8"))
    errors = []
    if model.get("version") != 1:
        errors.append("recommendation model version must be 1")
    query_ids = []
    aliases = set()
    for query in model.get("queries", []):
        query_id = query.get("query_id")
        query_ids.append(query_id)
        if not query_id or not query.get("title"):
            errors.append(f"recommendation query missing query_id or title: {query}")
        if query.get("status") == "unavailable":
            if not query.get("reason") or not query.get("required_evidence"):
                errors.append(f"unavailable query {query_id} requires reason and required_evidence")
            continue
        if query.get("kind") not in RECOMMENDATION_KINDS:
            errors.append(f"query {query_id} has unsupported kind {query.get('kind')}")
        for field in RECOMMENDATION_REQUIRED_FILTERS.get(query.get("kind"), ()):
            value = query.get(field)
            if not as_ids(value):
                errors.append(f"query {query_id} of kind {query.get('kind')} requires {field}")
        for area_id in as_ids(query.get("area_id", [])) + as_ids(query.get("area_ids", [])):
            target = records.get(area_id)
            if target is None or target.entity_type != "research-area":
                errors.append(f"query {query_id} has invalid research-area ID {area_id}")
        for language_id in as_ids(query.get("language_id", [])):
            target = records.get(language_id)
            if target is None or target.entity_type != "programming-language":
                errors.append(f"query {query_id} has invalid programming-language ID {language_id}")
        if query.get("kind") == "entities-with-mentorship-process-evidence":
            reviewed_observations = {
                (record.id, observation.get("category"))
                for record in records.values()
                if record.entity_type in {"research-group", "department", "university", "organization"}
                and eligible(record)
                for observation in record.metadata.get("mentorship_process_evidence", []) or []
            }
            if len({record_id for record_id, _ in reviewed_observations}) < 2 or len(
                {category for _, category in reviewed_observations}
            ) < 2:
                errors.append(
                    f"query {query_id} requires two independently reviewed entities with evidence in at least two mentorship-process categories"
                )
        for alias in query.get("aliases", []):
            if alias in aliases:
                errors.append(f"recommendation alias is duplicated: {alias}")
            aliases.add(alias)
    if len(query_ids) != len(set(query_ids)):
        errors.append("recommendation query IDs must be unique")
    return model, errors


def render_recommendation_query(query: dict[str, Any], records: dict[str, Record], output_path: Path) -> list[str]:
    lines = [f"## {query['title']}", "", f"**Query ID:** `{query['query_id']}`", ""]
    if query.get("status") == "unavailable":
        lines.extend([
            "**Status:** unavailable — no recommendation is emitted.", "",
            f"**Why:** {query['reason']}", "",
            f"**Required before enabling:** {query['required_evidence']}", "",
        ])
        return lines
    candidates = recommendation_candidates(query, records)
    lines.extend([
        "**Status:** available — evidence-discovery result, not a ranking.", "",
        "| Candidate | Documented matching evidence | Confidence | Coverage |",
        "| --- | --- | --- | --- |",
    ])
    for candidate in candidates:
        record = candidate["record"]
        signals = candidate["signals"]
        rendered_signals = "; ".join(f"{item['label']} (sources: {item['sources']})" for item in signals)
        confidence = lowest_confidence([item["confidence"] for item in signals])
        coverage = f"{candidate['criteria']}/{candidate['criteria']} documented criteria"
        lines.append(
            f"| {canonical_link(record, output_path)} (`{record.id}`) | {rendered_signals} | {confidence} | {coverage} |"
        )
    if not candidates:
        lines.append("| — | No reviewed canonical entity currently matches the direct query criteria. | unavailable | 0 criteria |")
    lines.extend(["", f"**Limitations:** {query['limitations']}", ""])
    return lines


def recommendation_report(root: Path, records: dict[str, Record], model: dict[str, Any], fingerprint: str) -> str:
    output_path = root / "reports/generated/evidence-recommendations.md"
    lines = [
        "<!-- GENERATED FILE: edit canonical inputs or scoring/v1/evidence-recommendations.yaml, then regenerate. -->",
        f"<!-- input-fingerprint: {fingerprint} -->",
        "# Evidence recommendations",
        "",
        f"**Model:** `{model['model_id']}`",
        f"**Input fingerprint:** `{fingerprint}`",
        "**Status:** deterministic evidence-discovery projection; not a prestige, quality, or availability ranking.",
        "",
        "## Ordering and boundary",
        "",
        f"Results use `{model['ordering']['primary']}` then `{', '.join(model['ordering']['tie_breakers'])}`. {model['ordering']['interpretation']}",
        "Each row exposes only source-backed matching signals; any traversal is displayed explicitly. Unknown, private, volatile, or unsupported dimensions remain unavailable.",
        "",
    ]
    for query in model["queries"]:
        lines.extend(render_recommendation_query(query, records, output_path))
    lines.extend([
        "## Repair workflow",
        "",
        "Correct evidence and relationships in canonical entities, rerun the generator, and review the diff. Do not edit this report manually or use it to infer admissions, funding, mentorship, language, immigration, or personal fit.",
        "",
    ])
    return "\n".join(lines)


def recommendation_catalog(model: dict[str, Any]) -> str:
    """Render a deterministic index of public evidence-discovery questions."""
    lines = [
        "# Evidence recommendation query catalog", "",
        "Use `python3 scripts/research_landscape.py recommend --query <query-id-or-alias>` to render one query. Available results are evidence-discovery outputs, not rankings; unavailable queries name their missing evidence contract.",
        "",
        "| Query ID | Status | Title | Aliases |",
        "| --- | --- | --- | --- |",
    ]
    for query in model["queries"]:
        status = "unavailable" if query.get("status") == "unavailable" else "available"
        aliases = ", ".join(f"`{alias}`" for alias in query.get("aliases", [])) or "—"
        lines.append(f"| `{query['query_id']}` | {status} | {query['title']} | {aliases} |")
    lines.extend(["", "No private profiles, preferences, or shortlist data are read by this command.", ""])
    return "\n".join(lines)


DISCOVERY_FILTER_TYPES = {
    "area": "research-area",
    "country": "country",
    "software": "research-software",
    "language": "programming-language",
    "ecosystem": "research-ecosystem",
}


def direct_host_country_signals(group: Record, country_id: str, records: dict[str, Record]) -> list[dict[str, Any]]:
    """Return the documented group-to-country path required for a group filter.

    The country filter deliberately follows the ADR 0006 direct host. It does
    not guess a group's location from a name, nearby institution, or topic.
    """
    signals = []
    direct_host_ids = set(as_ids(group.metadata.get("institution_id", []))) | set(
        as_ids(group.metadata.get("organization_id", []))
    )
    for host_assertion in matching_assertions(group, "belongs_to"):
        host = records.get(host_assertion.get("target_id"))
        if host is None or host.id not in direct_host_ids or country_id not in resolved_countries(host, records):
            continue
        signals.append(signal(f"belongs to direct host `{host.id}`", host_assertion, group))
        location_assertions = matching_assertions(host, "located_in", {country_id})
        if location_assertions:
            signals.extend(
                signal(f"`{host.id}` is located in `{country_id}`", assertion, host)
                for assertion in location_assertions
            )
        elif country_id in as_ids(host.metadata.get("country_id", [])):
            signals.append(metadata_signal(f"`{host.id}` is classified in `{country_id}`", host))
    return signals


def deduplicate_signals(signals: list[dict[str, Any]]) -> list[dict[str, Any]]:
    unique = {}
    for item in signals:
        unique[(item["label"], item["sources"], item["confidence"])] = item
    return list(unique.values())


def development_ecosystem_signals(
    developer: Record, ecosystem_id: str, records: dict[str, Record], verb: str,
) -> list[dict[str, Any]]:
    """Return a developer-to-ecosystem path through reviewed software.

    The function intentionally displays both source-bearing assertions instead
    of claiming that the developer is itself an ecosystem member.
    """
    ecosystem = records.get(ecosystem_id)
    if ecosystem is None or ecosystem.entity_type != "research-ecosystem":
        return []
    signals = []
    for development in matching_assertions(developer, "develops"):
        software = records.get(development.get("target_id"))
        if software is None or software.entity_type != "research-software":
            continue
        inclusions = matching_assertions(ecosystem, "includes", {software.id})
        for inclusion in inclusions:
            signals.append(signal(f"{verb} `{software.id}`", development, developer))
            signals.append(signal(f"`{ecosystem_id}` includes `{software.id}`", inclusion, ecosystem))
    return deduplicate_signals(signals)


def discovery_group_candidates(
    records: dict[str, Record],
    area_id: str | None,
    country_id: str | None,
    software_id: str | None,
    language_id: str | None,
    ecosystem_id: str | None = None,
) -> list[dict[str, Any]]:
    """Apply ANDed, source-explainable filters to reviewed research groups."""
    candidates = []
    for group in records.values():
        if group.entity_type != "research-group" or not eligible(group):
            continue
        signals = []
        criteria = 0
        developments = matching_assertions(group, "develops")
        if area_id:
            area_signals = [signal(f"works on `{area_id}`", assertion, group) for assertion in matching_assertions(group, "works_on", {area_id})]
            if not area_signals:
                continue
            signals.extend(area_signals)
            criteria += 1
        if country_id:
            country_signals = direct_host_country_signals(group, country_id, records)
            if not country_signals:
                continue
            signals.extend(country_signals)
            criteria += 1
        if software_id:
            developments = [assertion for assertion in developments if assertion.get("target_id") == software_id]
            if not developments:
                continue
            signals.extend(signal(f"develops `{software_id}`", assertion, group) for assertion in developments)
            criteria += 1
        if language_id:
            language_signals = []
            for development in developments:
                software = records.get(development.get("target_id"))
                if software is None or software.entity_type != "research-software":
                    continue
                for implementation in matching_assertions(software, "implemented_in", {language_id}):
                    language_signals.append(signal(f"develops `{software.id}`", development, group))
                    language_signals.append(signal(f"`{software.id}` is implemented in `{language_id}`", implementation, software))
            if not language_signals:
                continue
            signals.extend(language_signals)
            criteria += 1
        if ecosystem_id:
            ecosystem_signals = development_ecosystem_signals(group, ecosystem_id, records, "develops")
            if not ecosystem_signals:
                continue
            signals.extend(ecosystem_signals)
            criteria += 1
        candidates.append({"record": group, "signals": deduplicate_signals(signals), "criteria": criteria})
    return sorted(candidates, key=lambda item: (item["record"].metadata["name"].casefold(), item["record"].id))


def render_group_discovery(
    records: dict[str, Record],
    area_id: str | None,
    country_id: str | None,
    software_id: str | None,
    language_id: str | None,
    ecosystem_id: str | None,
    output_path: Path,
) -> str:
    filters = [(name, value) for name, value in (
        ("research area", area_id), ("country", country_id), ("research software", software_id), ("programming language", language_id), ("research ecosystem", ecosystem_id),
    ) if value]
    if not filters:
        raise ValueError("provide at least one of --area, --country, --software, --language, or --ecosystem")
    candidates = discovery_group_candidates(records, area_id, country_id, software_id, language_id, ecosystem_id)
    lines = [
        "# Research-group discovery", "",
        "**Status:** deterministic evidence-discovery result, not a ranking.", "",
        "**AND filters:** " + "; ".join(f"{name} `{value}`" for name, value in filters) + ".", "",
        "| Research group | Documented matching evidence | Confidence | Coverage |",
        "| --- | --- | --- | --- |",
    ]
    total_criteria = len(filters)
    for candidate in candidates:
        signals = candidate["signals"]
        rendered_signals = "; ".join(f"{item['label']} (sources: {item['sources']})" for item in signals)
        confidence = lowest_confidence([item["confidence"] for item in signals])
        lines.append(
            f"| {canonical_link(candidate['record'], output_path)} (`{candidate['record'].id}`) | {rendered_signals} | {confidence} | {candidate['criteria']}/{total_criteria} documented criteria |"
        )
    if not candidates:
        lines.append("| — | No reviewed canonical research group matches every requested evidence criterion. | unavailable | 0 criteria |")
    lines.extend([
        "", "## Boundary", "",
        "Results are alphabetically ordered and contain only reviewed groups with every requested source-backed criterion. A country match follows the group’s documented direct host; language and ecosystem matches follow a documented group-development edge through software `implemented_in` or ecosystem `includes` assertions. This does not assert that a group is an ecosystem member or establish openings, group-wide working language, individual skill, mentorship quality, funding, admissions, or applicant fit.", "",
    ])
    return "\n".join(lines)


def discover_groups(
    root: Path,
    area_id: str | None,
    country_id: str | None,
    software_id: str | None,
    language_id: str | None,
    ecosystem_id: str | None,
    check: bool,
    query_id: str | None,
    list_queries: bool,
    as_of: str | None,
) -> int:
    if check or query_id or list_queries or as_of:
        print("ERROR: discover-groups accepts only --area, --country, --software, --language, and --ecosystem")
        return 2
    records, results = validate(root)
    if results.errors:
        print_results(root, records, results)
        return 1
    filters = {"area": area_id, "country": country_id, "software": software_id, "language": language_id, "ecosystem": ecosystem_id}
    for name, value in filters.items():
        if not value:
            continue
        target = records.get(value)
        if target is None or target.entity_type != DISCOVERY_FILTER_TYPES[name]:
            print(f"ERROR: --{name} must reference a canonical {DISCOVERY_FILTER_TYPES[name]} ID, got {value!r}")
            return 2
    try:
        print(render_group_discovery(
            records, area_id, country_id, software_id, language_id, ecosystem_id,
            root / "reports/generated/evidence-recommendations.md",
        ))
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2
    return 0


def affiliation_country_signals(pi: Record, country_id: str, records: dict[str, Record]) -> list[dict[str, Any]]:
    """Return an explicit PI affiliation-to-country path without inferring employment."""
    signals = []
    for affiliation_assertion in matching_assertions(pi, "affiliated_with"):
        affiliation = records.get(affiliation_assertion.get("target_id"))
        if affiliation is None or country_id not in resolved_countries(affiliation, records):
            continue
        signals.append(signal(f"is affiliated with `{affiliation.id}`", affiliation_assertion, pi))
        location_assertions = matching_assertions(affiliation, "located_in", {country_id})
        if location_assertions:
            signals.extend(
                signal(f"`{affiliation.id}` is located in `{country_id}`", assertion, affiliation)
                for assertion in location_assertions
            )
        elif country_id in as_ids(affiliation.metadata.get("country_id", [])):
            signals.append(metadata_signal(f"`{affiliation.id}` is classified in `{country_id}`", affiliation))
    return signals


def discovery_pi_candidates(
    records: dict[str, Record],
    area_id: str | None,
    country_id: str | None,
    software_id: str | None,
    language_id: str | None,
    ecosystem_id: str | None = None,
) -> list[dict[str, Any]]:
    """Apply ANDed, source-explainable filters to reviewed PIs."""
    candidates = []
    for pi in records.values():
        if pi.entity_type != "principal-investigator" or not eligible(pi):
            continue
        signals = []
        criteria = 0
        developments = matching_assertions(pi, "develops")
        if area_id:
            area_signals = [signal(f"works on `{area_id}`", assertion, pi) for assertion in matching_assertions(pi, "works_on", {area_id})]
            if not area_signals:
                continue
            signals.extend(area_signals)
            criteria += 1
        if country_id:
            country_signals = affiliation_country_signals(pi, country_id, records)
            if not country_signals:
                continue
            signals.extend(country_signals)
            criteria += 1
        if software_id:
            developments = [assertion for assertion in developments if assertion.get("target_id") == software_id]
            if not developments:
                continue
            signals.extend(signal(f"develops `{software_id}`", assertion, pi) for assertion in developments)
            criteria += 1
        if language_id:
            language_signals = []
            for development in developments:
                software = records.get(development.get("target_id"))
                if software is None or software.entity_type != "research-software":
                    continue
                for implementation in matching_assertions(software, "implemented_in", {language_id}):
                    language_signals.append(signal(f"develops `{software.id}`", development, pi))
                    language_signals.append(signal(f"`{software.id}` is implemented in `{language_id}`", implementation, software))
            if not language_signals:
                continue
            signals.extend(language_signals)
            criteria += 1
        if ecosystem_id:
            ecosystem_signals = development_ecosystem_signals(pi, ecosystem_id, records, "develops")
            if not ecosystem_signals:
                continue
            signals.extend(ecosystem_signals)
            criteria += 1
        candidates.append({"record": pi, "signals": deduplicate_signals(signals), "criteria": criteria})
    return sorted(candidates, key=lambda item: (item["record"].metadata["name"].casefold(), item["record"].id))


def render_pi_discovery(
    records: dict[str, Record],
    area_id: str | None,
    country_id: str | None,
    software_id: str | None,
    language_id: str | None,
    ecosystem_id: str | None,
    output_path: Path,
) -> str:
    filters = [(name, value) for name, value in (
        ("research area", area_id), ("country", country_id), ("research software", software_id), ("programming language", language_id), ("research ecosystem", ecosystem_id),
    ) if value]
    if not filters:
        raise ValueError("provide at least one of --area, --country, --software, --language, or --ecosystem")
    candidates = discovery_pi_candidates(records, area_id, country_id, software_id, language_id, ecosystem_id)
    lines = [
        "# Principal-investigator discovery", "",
        "**Status:** deterministic evidence-discovery result, not a ranking or availability finding.", "",
        "**AND filters:** " + "; ".join(f"{name} `{value}`" for name, value in filters) + ".", "",
        "| Principal investigator | Documented matching evidence | Confidence | Coverage |",
        "| --- | --- | --- | --- |",
    ]
    total_criteria = len(filters)
    for candidate in candidates:
        signals = candidate["signals"]
        rendered_signals = "; ".join(f"{item['label']} (sources: {item['sources']})" for item in signals)
        confidence = lowest_confidence([item["confidence"] for item in signals])
        lines.append(
            f"| {canonical_link(candidate['record'], output_path)} (`{candidate['record'].id}`) | {rendered_signals} | {confidence} | {candidate['criteria']}/{total_criteria} documented criteria |"
        )
    if not candidates:
        lines.append("| — | No reviewed canonical PI matches every requested evidence criterion. | unavailable | 0 criteria |")
    lines.extend([
        "", "## Boundary", "",
        "Results are alphabetically ordered and contain only PIs with every requested source-backed criterion. A country match follows a documented public affiliation and its documented location; language and ecosystem matches follow a documented PI-development edge through software `implemented_in` or ecosystem `includes` assertions. This does not assert that a PI is an ecosystem member or establish current openings, supervision capacity, mentorship quality, funding, admissions, or applicant fit.", "",
    ])
    return "\n".join(lines)


def discover_pis(
    root: Path,
    area_id: str | None,
    country_id: str | None,
    software_id: str | None,
    language_id: str | None,
    ecosystem_id: str | None,
    check: bool,
    query_id: str | None,
    list_queries: bool,
    as_of: str | None,
) -> int:
    if check or query_id or list_queries or as_of:
        print("ERROR: discover-pis accepts only --area, --country, --software, --language, and --ecosystem")
        return 2
    records, results = validate(root)
    if results.errors:
        print_results(root, records, results)
        return 1
    filters = {"area": area_id, "country": country_id, "software": software_id, "language": language_id, "ecosystem": ecosystem_id}
    for name, value in filters.items():
        if not value:
            continue
        target = records.get(value)
        if target is None or target.entity_type != DISCOVERY_FILTER_TYPES[name]:
            print(f"ERROR: --{name} must reference a canonical {DISCOVERY_FILTER_TYPES[name]} ID, got {value!r}")
            return 2
    try:
        print(render_pi_discovery(
            records, area_id, country_id, software_id, language_id, ecosystem_id,
            root / "reports/generated/evidence-recommendations.md",
        ))
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2
    return 0


def university_country_signals(university: Record, country_id: str) -> list[dict[str, Any]]:
    """Return direct University-to-Country evidence; no inferred geography."""
    location_assertions = matching_assertions(university, "located_in", {country_id})
    if location_assertions:
        return [
            signal(f"is located in `{country_id}`", assertion, university)
            for assertion in location_assertions
        ]
    if country_id in as_ids(university.metadata.get("country_id", [])):
        return [metadata_signal(f"is classified in `{country_id}`", university)]
    return []


def directly_hosted_group_signals(group: Record, university_id: str) -> list[dict[str, Any]]:
    """Return only the group edge that satisfies the reviewed direct-host field."""
    if group.metadata.get("institution_id") != university_id:
        return []
    return [
        signal(f"directly hosts `{group.id}`", assertion, group)
        for assertion in matching_assertions(group, "belongs_to", {university_id})
    ]


def discovery_university_candidates(
    records: dict[str, Record],
    area_id: str | None,
    country_id: str | None,
    software_id: str | None,
    language_id: str | None,
    ecosystem_id: str | None = None,
) -> list[dict[str, Any]]:
    """Find universities through explicit, direct-host group evidence paths."""
    group_filters_present = any((area_id, software_id, language_id, ecosystem_id))
    eligible_groups = discovery_group_candidates(records, area_id, None, software_id, language_id, ecosystem_id)
    if not group_filters_present:
        eligible_groups = [
            {"record": group, "signals": [], "criteria": 0}
            for group in records.values()
            if group.entity_type == "research-group" and eligible(group)
        ]
    candidates = []
    for university in records.values():
        if university.entity_type != "university" or not eligible(university):
            continue
        signals = []
        criteria = 0
        if country_id:
            country_signals = university_country_signals(university, country_id)
            if not country_signals:
                continue
            signals.extend(country_signals)
            criteria += 1
        hosted = []
        for group_candidate in eligible_groups:
            group = group_candidate["record"]
            host_signals = directly_hosted_group_signals(group, university.id)
            if not host_signals:
                continue
            hosted.append((group, host_signals, group_candidate["signals"]))
        if not hosted:
            continue
        if group_filters_present:
            criteria += sum(bool(value) for value in (area_id, software_id, language_id, ecosystem_id))
        for group, host_signals, group_signals in hosted:
            signals.extend(host_signals)
            for item in group_signals:
                signals.append({**item, "label": f"`{group.id}`: {item['label']}"})
        candidates.append({"record": university, "signals": deduplicate_signals(signals), "criteria": criteria})
    return sorted(candidates, key=lambda item: (item["record"].metadata["name"].casefold(), item["record"].id))


def render_university_discovery(
    records: dict[str, Record],
    area_id: str | None,
    country_id: str | None,
    software_id: str | None,
    language_id: str | None,
    ecosystem_id: str | None,
    output_path: Path,
) -> str:
    filters = [(name, value) for name, value in (
        ("research area", area_id), ("country", country_id), ("research software", software_id), ("programming language", language_id), ("research ecosystem", ecosystem_id),
    ) if value]
    if not filters:
        raise ValueError("provide at least one of --area, --country, --software, --language, or --ecosystem")
    candidates = discovery_university_candidates(records, area_id, country_id, software_id, language_id, ecosystem_id)
    lines = [
        "# University environment discovery", "",
        "**Status:** deterministic evidence-discovery result, not a ranking or university-strength assessment.", "",
        "**AND filters:** " + "; ".join(f"{name} `{value}`" for name, value in filters) + ".", "",
        "| University | Documented matching evidence | Confidence | Coverage |",
        "| --- | --- | --- | --- |",
    ]
    total_criteria = len(filters)
    for candidate in candidates:
        signals = candidate["signals"]
        rendered_signals = "; ".join(f"{item['label']} (sources: {item['sources']})" for item in signals)
        confidence = lowest_confidence([item["confidence"] for item in signals])
        lines.append(
            f"| {canonical_link(candidate['record'], output_path)} (`{candidate['record'].id}`) | {rendered_signals} | {confidence} | {candidate['criteria']}/{total_criteria} documented criteria |"
        )
    if not candidates:
        lines.append("| — | No reviewed canonical University has a directly hosted group path matching every requested criterion. | unavailable | 0 criteria |")
    lines.extend([
        "", "## Boundary", "",
        "Results are alphabetically ordered and use only a University's documented country and the ADR 0006 direct-host paths of reviewed groups. Signals name the hosted group that supplied area, software, language, or ecosystem traversal evidence; different signals may come from different directly hosted groups. This does not assert that a university is an ecosystem member or rank universities, establish ecosystem completeness, degree quality, funding, admissions, mentorship, or applicant fit.", "",
    ])
    return "\n".join(lines)


def discover_universities(
    root: Path,
    area_id: str | None,
    country_id: str | None,
    software_id: str | None,
    language_id: str | None,
    ecosystem_id: str | None,
    check: bool,
    query_id: str | None,
    list_queries: bool,
    as_of: str | None,
) -> int:
    if check or query_id or list_queries or as_of:
        print("ERROR: discover-universities accepts only --area, --country, --software, --language, and --ecosystem")
        return 2
    records, results = validate(root)
    if results.errors:
        print_results(root, records, results)
        return 1
    filters = {"area": area_id, "country": country_id, "software": software_id, "language": language_id, "ecosystem": ecosystem_id}
    for name, value in filters.items():
        if not value:
            continue
        target = records.get(value)
        if target is None or target.entity_type != DISCOVERY_FILTER_TYPES[name]:
            print(f"ERROR: --{name} must reference a canonical {DISCOVERY_FILTER_TYPES[name]} ID, got {value!r}")
            return 2
    try:
        print(render_university_discovery(
            records, area_id, country_id, software_id, language_id, ecosystem_id,
            root / "reports/generated/evidence-recommendations.md",
        ))
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2
    return 0


def ecosystem_area_signals(ecosystem: Record, area_id: str, records: dict[str, Record]) -> list[dict[str, Any]]:
    """Return explicit ecosystem paths to a controlled research area."""
    signals = []
    for connection in matching_assertions(ecosystem, "connects"):
        target = records.get(connection.get("target_id"))
        if target is None:
            continue
        for area_assertion in matching_assertions(target, "works_on", {area_id}):
            signals.append(signal(f"connects `{target.id}`", connection, ecosystem))
            signals.append(signal(f"`{target.id}` works on `{area_id}`", area_assertion, target))
    for inclusion in matching_assertions(ecosystem, "includes"):
        software = records.get(inclusion.get("target_id"))
        if software is None or software.entity_type != "research-software":
            continue
        if area_id in as_ids(software.metadata.get("research_area_ids", [])):
            signals.append(signal(f"includes `{software.id}`", inclusion, ecosystem))
            signals.append(metadata_signal(f"`{software.id}` is classified in `{area_id}`", software))
    return deduplicate_signals(signals)


def discovery_ecosystem_candidates(
    records: dict[str, Record], area_id: str | None, software_id: str | None
) -> list[dict[str, Any]]:
    """Apply ANDed, source-explainable filters to reviewed research ecosystems."""
    candidates = []
    for ecosystem in records.values():
        if ecosystem.entity_type != "research-ecosystem" or not eligible(ecosystem):
            continue
        signals = []
        criteria = 0
        if area_id:
            area_signals = ecosystem_area_signals(ecosystem, area_id, records)
            if not area_signals:
                continue
            signals.extend(area_signals)
            criteria += 1
        if software_id:
            software_signals = [
                signal(f"includes `{software_id}`", assertion, ecosystem)
                for assertion in matching_assertions(ecosystem, "includes", {software_id})
            ]
            if not software_signals:
                continue
            signals.extend(software_signals)
            criteria += 1
        candidates.append({"record": ecosystem, "signals": deduplicate_signals(signals), "criteria": criteria})
    return sorted(candidates, key=lambda item: (item["record"].metadata["name"].casefold(), item["record"].id))


def render_ecosystem_discovery(
    records: dict[str, Record], area_id: str | None, software_id: str | None, output_path: Path
) -> str:
    filters = [(name, value) for name, value in (("research area", area_id), ("research software", software_id)) if value]
    if not filters:
        raise ValueError("provide at least one of --area or --software")
    candidates = discovery_ecosystem_candidates(records, area_id, software_id)
    lines = [
        "# Research-ecosystem discovery", "",
        "**Status:** deterministic evidence-discovery result, not a ranking or ecosystem-dominance assessment.", "",
        "**AND filters:** " + "; ".join(f"{name} `{value}`" for name, value in filters) + ".", "",
        "| Research ecosystem | Documented matching evidence | Confidence | Coverage |",
        "| --- | --- | --- | --- |",
    ]
    total_criteria = len(filters)
    for candidate in candidates:
        signals = candidate["signals"]
        rendered_signals = "; ".join(f"{item['label']} (sources: {item['sources']})" for item in signals)
        confidence = lowest_confidence([item["confidence"] for item in signals])
        lines.append(
            f"| {canonical_link(candidate['record'], output_path)} (`{candidate['record'].id}`) | {rendered_signals} | {confidence} | {candidate['criteria']}/{total_criteria} documented criteria |"
        )
    if not candidates:
        lines.append("| — | No reviewed canonical ecosystem matches every requested evidence criterion. | unavailable | 0 criteria |")
    lines.extend([
        "", "## Boundary", "",
        "Results are alphabetically ordered and include only source-backed `connects` or `includes` paths. An area match may arise through a connected group or PI, or through included research software with a documented area classification; each path is displayed. This does not establish field dominance, ecosystem completeness, model performance, funding, hiring, support, or applicant fit.", "",
    ])
    return "\n".join(lines)


def discover_ecosystems(
    root: Path,
    area_id: str | None,
    software_id: str | None,
    country_id: str | None,
    language_id: str | None,
    check: bool,
    query_id: str | None,
    list_queries: bool,
    as_of: str | None,
) -> int:
    if country_id or language_id or check or query_id or list_queries or as_of:
        print("ERROR: discover-ecosystems accepts only --area and --software")
        return 2
    records, results = validate(root)
    if results.errors:
        print_results(root, records, results)
        return 1
    filters = {"area": area_id, "software": software_id}
    for name, value in filters.items():
        if not value:
            continue
        target = records.get(value)
        if target is None or target.entity_type != DISCOVERY_FILTER_TYPES[name]:
            print(f"ERROR: --{name} must reference a canonical {DISCOVERY_FILTER_TYPES[name]} ID, got {value!r}")
            return 2
    try:
        print(render_ecosystem_discovery(
            records, area_id, software_id, root / "reports/generated/evidence-recommendations.md"
        ))
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2
    return 0


def discovery_software_candidates(
    records: dict[str, Record], area_id: str | None, language_id: str | None, ecosystem_id: str | None,
    open_source: str | None = None,
) -> list[dict[str, Any]]:
    """Apply ANDed, source-explainable filters to reviewed research software.

    Area classification is record metadata with the software record's local
    sources; language and ecosystem membership require their own typed,
    source-bearing relationship paths.
    """
    candidates = []
    for software in records.values():
        if software.entity_type != "research-software" or not eligible(software):
            continue
        signals = []
        criteria = 0
        if area_id:
            if area_id not in as_ids(software.metadata.get("research_area_ids", [])):
                continue
            signals.append(metadata_signal(f"is classified in `{area_id}`", software))
            criteria += 1
        if language_id:
            implementations = matching_assertions(software, "implemented_in", {language_id})
            if not implementations:
                continue
            signals.extend(
                signal(f"is implemented in `{language_id}`", assertion, software)
                for assertion in implementations
            )
            criteria += 1
        if ecosystem_id:
            ecosystem = records.get(ecosystem_id)
            inclusions = matching_assertions(ecosystem, "includes", {software.id}) if ecosystem else []
            if not inclusions:
                continue
            signals.extend(
                signal(f"is included by `{ecosystem_id}`", assertion, ecosystem)
                for assertion in inclusions
            )
            criteria += 1
        if open_source:
            if software.metadata.get("open_source") != open_source:
                continue
            signals.append(metadata_signal(f"has documented open-source state `{open_source}`", software))
            criteria += 1
        candidates.append({"record": software, "signals": deduplicate_signals(signals), "criteria": criteria})
    return sorted(candidates, key=lambda item: (item["record"].metadata["name"].casefold(), item["record"].id))


def render_software_discovery(
    records: dict[str, Record], area_id: str | None, language_id: str | None,
    ecosystem_id: str | None, output_path: Path, open_source: str | None = None,
) -> str:
    filters = [(name, value) for name, value in (
        ("research area", area_id), ("programming language", language_id), ("research ecosystem", ecosystem_id),
        ("open-source state", open_source),
    ) if value]
    if not filters:
        raise ValueError("provide at least one of --area, --language, --ecosystem, or --open-source")
    candidates = discovery_software_candidates(records, area_id, language_id, ecosystem_id, open_source)
    lines = [
        "# Research-software discovery", "",
        "**Status:** deterministic evidence-discovery result, not a ranking or software-quality assessment.", "",
        "**AND filters:** " + "; ".join(f"{name} `{value}`" for name, value in filters) + ".", "",
        "| Research software | Lifecycle observation | Documented matching evidence | Confidence | Coverage |",
        "| --- | --- | --- | --- | --- |",
    ]
    total_criteria = len(filters)
    for candidate in candidates:
        signals = candidate["signals"]
        rendered_signals = "; ".join(f"{item['label']} (sources: {item['sources']})" for item in signals)
        confidence = lowest_confidence([item["confidence"] for item in signals])
        lifecycle = candidate["record"].metadata.get("software_lifecycle")
        lifecycle_sources = ", ".join(as_ids(candidate["record"].metadata.get("lifecycle_source_ids", [])))
        lifecycle_observation = f"{lifecycle} (sources: {lifecycle_sources})" if lifecycle else "not documented"
        lines.append(
            f"| {canonical_link(candidate['record'], output_path)} (`{candidate['record'].id}`) | {lifecycle_observation} | {rendered_signals} | {confidence} | {candidate['criteria']}/{total_criteria} documented criteria |"
        )
    if not candidates:
        lines.append("| — | — | No reviewed canonical research software matches every requested evidence criterion. | unavailable | 0 criteria |")
    lines.extend([
        "", "## Boundary", "",
        "Results are alphabetically ordered and contain only reviewed software with every requested evidence criterion. Lifecycle is shown only when the software record has its own cited lifecycle observation; “not documented” does not mean active or inactive. Area classification and an open-source state are backed by the software record's local evidence; language and ecosystem matches use sourced `implemented_in` and `includes` assertions. An open-source state is not a software-quality, activity, governance, support, or individual-value claim. This does not rank software, establish technical superiority, maintenance activity, adoption, funding, openings, mentorship, or applicant fit.", "",
    ])
    return "\n".join(lines)


def discover_software(
    root: Path,
    area_id: str | None,
    language_id: str | None,
    ecosystem_id: str | None,
    open_source: str | None,
    country_id: str | None,
    software_id: str | None,
    check: bool,
    query_id: str | None,
    list_queries: bool,
    as_of: str | None,
) -> int:
    if country_id or software_id or check or query_id or list_queries or as_of:
        print("ERROR: discover-software accepts only --area, --language, --ecosystem, and --open-source")
        return 2
    if open_source and open_source not in OPEN_SOURCE_FILTER_VALUES:
        print("ERROR: --open-source must be one of yes, no, mixed, unknown, or not-applicable")
        return 2
    records, results = validate(root)
    if results.errors:
        print_results(root, records, results)
        return 1
    filters = {"area": area_id, "language": language_id, "ecosystem": ecosystem_id}
    for name, value in filters.items():
        if not value:
            continue
        target = records.get(value)
        if target is None or target.entity_type != DISCOVERY_FILTER_TYPES[name]:
            print(f"ERROR: --{name} must reference a canonical {DISCOVERY_FILTER_TYPES[name]} ID, got {value!r}")
            return 2
    try:
        print(render_software_discovery(
            records, area_id, language_id, ecosystem_id,
            root / "reports/generated/evidence-recommendations.md", open_source,
        ))
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2
    return 0


DISCOVERY_CATALOG_TYPES = (
    ("Research areas", "research-area"),
    ("Countries", "country"),
    ("Research software", "research-software"),
    ("Programming languages", "programming-language"),
    ("Research ecosystems", "research-ecosystem"),
)


def discovery_catalog(records: dict[str, Record]) -> str:
    """Render public, reviewed IDs accepted by the discovery commands."""
    lines = [
        "# Discovery filter catalog", "",
        "Use these reviewed canonical IDs with `discover-groups`, `discover-pis`, `discover-universities`, `discover-ecosystems`, and `discover-software`. The catalog contains no private profile, score, ranking, availability, or fit data.",
        "",
    ]
    for title, entity_type in DISCOVERY_CATALOG_TYPES:
        records_for_type = sorted(
            (record for record in records.values() if record.entity_type == entity_type and eligible(record)),
            key=lambda record: (record.metadata["name"].casefold(), record.id),
        )
        lines.extend([f"## {title}", "", "| Name | Canonical ID |", "| --- | --- |"])
        for record in records_for_type:
            lines.append(f"| {record.metadata['name']} | `{record.id}` |")
        if not records_for_type:
            lines.append("| — | No reviewed canonical records currently available. |")
        lines.append("")
    lines.extend([
        "## Boundary", "",
        "An ID identifies an evidence-backed graph node. Its presence in this catalog does not establish quality, prominence, openness beyond its own documented metadata, current availability, admissions, funding, mentorship, or applicant fit.", "",
    ])
    return "\n".join(lines)


def catalog(
    root: Path,
    check: bool,
    query_id: str | None,
    list_queries: bool,
    area_id: str | None,
    country_id: str | None,
    software_id: str | None,
    language_id: str | None,
    as_of: str | None,
) -> int:
    if check or query_id or list_queries or area_id or country_id or software_id or language_id or as_of:
        print("ERROR: catalog accepts no options")
        return 2
    records, results = validate(root)
    if results.errors:
        print_results(root, records, results)
        return 1
    print(discovery_catalog(records))
    return 0


def render_area_discovery(records: dict[str, Record], output_path: Path) -> str:
    """Render reviewed topic nodes and their bounded direct discovery reach."""
    coverage = {item["area"].id: item for item in research_area_coverage(records)}
    areas = sorted(
        (record for record in records.values() if record.entity_type == "research-area" and eligible(record)),
        key=lambda record: (record.metadata["name"].casefold(), record.id),
    )
    lines = [
        "# Research-area discovery", "",
        "**Status:** deterministic evidence-discovery result, not a research-problem ranking.", "",
        "Each row is a reviewed controlled topic. Reach counts reflect direct documented graph paths only; they are not measures of importance, opportunity, maturity, or quality.", "",
        "| Research area | Canonical ID | Direct discovery reach | Area evidence | Confidence |",
        "| --- | --- | --- | --- | --- |",
    ]
    for area in areas:
        item = coverage[area.id]
        reach = "; ".join(
            f"{key.replace('_', ' ')}: {item[key]}"
            for key in ("groups", "principal_investigators", "software", "universities", "ecosystems")
        )
        lines.append(
            f"| {canonical_link(area, output_path)} | `{area.id}` | {reach} | "
            f"sources: {', '.join(as_ids(area.metadata.get('source_ids', [])))} | {area.metadata['confidence']} |"
        )
    if not areas:
        lines.append("| — | — | No reviewed canonical research areas currently available. | — | unavailable |")
    lines.extend([
        "", "## Boundary", "",
        "This catalog does not select or compare research problems. A larger reach count can reflect only the current evidence coverage. Use an area ID with `discover-groups`, `discover-pis`, `discover-universities`, `discover-ecosystems`, or `discover-software` to inspect the underlying sourced paths. It does not establish problem importance, scientific novelty, funding, admissions, mentoring, availability, or applicant fit.", "",
    ])
    return "\n".join(lines)


def discover_areas(
    root: Path,
    check: bool,
    query_id: str | None,
    list_queries: bool,
    area_id: str | None,
    country_id: str | None,
    software_id: str | None,
    language_id: str | None,
    ecosystem_id: str | None,
    open_source: str | None,
    as_of: str | None,
) -> int:
    if any((check, query_id, list_queries, area_id, country_id, software_id, language_id, ecosystem_id, open_source, as_of)):
        print("ERROR: discover-areas accepts no options")
        return 2
    records, results = validate(root)
    if results.errors:
        print_results(root, records, results)
        return 1
    print(render_area_discovery(records, root / "reports/generated/evidence-recommendations.md"))
    return 0


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


def recommend(root: Path, check: bool, query_id: str | None, list_queries: bool = False) -> int:
    records, results = validate(root)
    if results.errors:
        print_results(root, records, results)
        return 1
    model, model_errors = validate_recommendation_model(root, records)
    if model_errors:
        for error in model_errors:
            print(f"ERROR: {error}")
        return 1
    if list_queries:
        if check or query_id:
            print("ERROR: --list cannot be combined with --check or --query")
            return 1
        print(recommendation_catalog(model))
        return 0
    fingerprint = recommendation_fingerprint(root)
    if query_id:
        matching = [query for query in model["queries"] if query["query_id"] == query_id or query_id in query.get("aliases", [])]
        if len(matching) != 1:
            print(f"ERROR: unknown or ambiguous recommendation query '{query_id}'")
            return 1
        if check:
            print("ERROR: --check is only valid for the full generated recommendation report")
            return 1
        output_path = root / "reports/generated/evidence-recommendations.md"
        print("\n".join(render_recommendation_query(matching[0], records, output_path)))
        return 0
    drift: list[str] = []
    output = root / "reports/generated/evidence-recommendations.md"
    write_or_check(output, recommendation_report(root, records, model, fingerprint), check, drift)
    if drift:
        print("Generated recommendation output is stale or missing:")
        print("\n".join(f"- {Path(path).relative_to(root)}" for path in drift))
        return 1
    print_results(root, records, results)
    print("Generated recommendations are in sync." if check else "Generated recommendations.")
    return 0


def print_results(root: Path, records: dict[str, Record], results: Results) -> None:
    relationships = sum(len(record.metadata.get("relationship_assertions", []) or []) for record in records.values())
    print(f"Validated {len(records)} v2 entities and {relationships} typed relationship assertions.")
    for error in results.errors:
        print(f"ERROR: {error}")
    for warning in results.warnings:
        print(f"WARNING: {warning}")


def parse_date(value: Any, field: str, record: Record) -> dt.date:
    """Parse a schema-validated ISO date with context for standalone audits."""
    try:
        return dt.date.fromisoformat(str(value))
    except ValueError as exc:
        raise ValueError(f"{record.path}: invalid {field} date {value!r}") from exc


def freshness_audit(records: dict[str, Record], as_of: dt.date) -> dict[str, Any]:
    """Classify review currency without mutating canonical facts.

    The audit is intentionally parameterized by an explicit date so an issue,
    CI job, or maintainer can reproduce a result. It is not a generated report:
    freshness changes with time even when canonical inputs do not.
    """
    buckets: dict[str, list[dict[str, Any]]] = {
        "current": [], "attention": [], "stale": [], "future_review_date": [],
        "volatile_overdue": [], "volatile_due_soon": [],
    }
    reviewed = [
        record for record in records.values()
        if record.metadata.get("status") in {"reviewed", "published"}
    ]
    for record in sorted(reviewed, key=lambda item: (item.metadata["last_review"], item.id)):
        review_date = parse_date(record.metadata["last_review"], "last_review", record)
        age = (as_of - review_date).days
        item = {"id": record.id, "name": record.metadata["name"], "last_review": review_date.isoformat(), "age_days": age}
        if age < 0:
            buckets["future_review_date"].append(item)
        elif age <= REVIEW_CURRENT_DAYS:
            buckets["current"].append(item)
        elif age <= REVIEW_STALE_DAYS:
            buckets["attention"].append(item)
        else:
            buckets["stale"].append(item)
        for assertion in record.metadata.get("volatile_assertions", []) or []:
            review_by = parse_date(assertion["review_by"], "volatile_assertions.review_by", record)
            volatile_item = {
                "id": record.id,
                "name": record.metadata["name"],
                "subject": assertion["subject"],
                "review_by": review_by.isoformat(),
                "days_until_review": (review_by - as_of).days,
            }
            if review_by < as_of:
                buckets["volatile_overdue"].append(volatile_item)
            elif review_by <= as_of + dt.timedelta(days=VOLATILE_DUE_SOON_DAYS):
                buckets["volatile_due_soon"].append(volatile_item)
    return {"as_of": as_of.isoformat(), "reviewed_records": len(reviewed), "buckets": buckets}


def render_freshness_audit(audit: dict[str, Any]) -> str:
    """Render a concise, copyable maintenance audit rather than a score."""
    buckets = audit["buckets"]
    lines = [
        "# Review freshness audit", "",
        f"**As of:** `{audit['as_of']}`", "",
        "This is a maintenance signal based on human review dates and declared volatile-assertion review deadlines. It does not measure research quality, source truth, prestige, or fit.",
        "",
        "## Reviewed-record currency", "",
        "| Status | Rule | Records |",
        "| --- | --- | ---: |",
        f"| Current | reviewed within {REVIEW_CURRENT_DAYS} days | {len(buckets['current'])} |",
        f"| Attention | reviewed {REVIEW_CURRENT_DAYS + 1}–{REVIEW_STALE_DAYS} days ago | {len(buckets['attention'])} |",
        f"| Stale | reviewed more than {REVIEW_STALE_DAYS} days ago | {len(buckets['stale'])} |",
        f"| Invalid future date | `last_review` is after the audit date | {len(buckets['future_review_date'])} |",
        "",
        "## Volatile assertions", "",
        "| Status | Rule | Assertions |",
        "| --- | --- | ---: |",
        f"| Overdue | `review_by` before audit date | {len(buckets['volatile_overdue'])} |",
        f"| Due soon | `review_by` within {VOLATILE_DUE_SOON_DAYS} days | {len(buckets['volatile_due_soon'])} |",
        "",
    ]
    sections = [
        ("Records needing attention", "attention", "id", "last_review", "age_days"),
        ("Stale records", "stale", "id", "last_review", "age_days"),
        ("Records with future review dates", "future_review_date", "id", "last_review", "age_days"),
        ("Overdue volatile assertions", "volatile_overdue", "id", "subject", "review_by"),
        ("Volatile assertions due soon", "volatile_due_soon", "id", "subject", "review_by"),
    ]
    for title, bucket, first, second, third in sections:
        items = buckets[bucket]
        if not items:
            continue
        lines.extend([f"## {title}", "", f"| Entity | {second.replace('_', ' ')} | {third.replace('_', ' ')} |", "| --- | --- | --- |"])
        for item in items:
            lines.append(f"| `{item[first]}` | {item[second]} | {item[third]} |")
        lines.append("")
    lines.extend([
        "## Action boundary", "",
        "Review the cited public sources and update only evidence that can be verified. Do not treat age alone as disproof, delete a claim automatically, or infer a negative conclusion from a missing update.",
        "",
    ])
    return "\n".join(lines)


def freshness(root: Path, as_of: dt.date) -> int:
    records, results = validate(root)
    if results.errors:
        print_results(root, records, results)
        return 1
    print(render_freshness_audit(freshness_audit(records, as_of)))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "generate", "health", "recommend", "catalog", "discover-areas", "discover-groups", "discover-pis", "discover-universities", "discover-ecosystems", "discover-software", "freshness"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="fail if generated output differs from canonical inputs")
    parser.add_argument("--query", help="print one recommendation query by stable ID or alias")
    parser.add_argument("--list", action="store_true", dest="list_queries", help="list public recommendation query IDs and aliases")
    parser.add_argument("--area", help="canonical Research Area ID for compatible discovery commands")
    parser.add_argument("--country", help="canonical Country ID for compatible discovery commands")
    parser.add_argument("--software", help="canonical Research Software ID for compatible discovery commands")
    parser.add_argument("--language", help="canonical Programming Language ID for compatible discovery commands")
    parser.add_argument("--ecosystem", help="canonical Research Ecosystem ID for compatible discovery commands")
    parser.add_argument("--open-source", help="documented open-source state for discover-software")
    parser.add_argument("--as-of", help="ISO date for a reproducible freshness audit (defaults to today)")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.ecosystem and args.command not in {"discover-groups", "discover-pis", "discover-universities", "discover-software"}:
        print("ERROR: --ecosystem is accepted only by discover-groups, discover-pis, discover-universities, and discover-software")
        return 2
    if args.open_source and args.command != "discover-software":
        print("ERROR: --open-source is accepted only by discover-software")
        return 2
    if args.command == "validate":
        records, results = validate(root)
        print_results(root, records, results)
        return 1 if results.errors else 0
    if args.command == "recommend":
        return recommend(root, args.check, args.query, args.list_queries)
    if args.command == "catalog":
        return catalog(
            root, args.check, args.query, args.list_queries,
            args.area, args.country, args.software, args.language, args.as_of,
        )
    if args.command == "discover-areas":
        return discover_areas(
            root, args.check, args.query, args.list_queries, args.area, args.country,
            args.software, args.language, args.ecosystem, args.open_source, args.as_of,
        )
    if args.command == "discover-groups":
        return discover_groups(
            root, args.area, args.country, args.software, args.language, args.ecosystem,
            args.check, args.query, args.list_queries, args.as_of,
        )
    if args.command == "discover-pis":
        return discover_pis(
            root, args.area, args.country, args.software, args.language, args.ecosystem,
            args.check, args.query, args.list_queries, args.as_of,
        )
    if args.command == "discover-universities":
        return discover_universities(
            root, args.area, args.country, args.software, args.language, args.ecosystem,
            args.check, args.query, args.list_queries, args.as_of,
        )
    if args.command == "discover-ecosystems":
        return discover_ecosystems(
            root, args.area, args.software, args.country, args.language,
            args.check, args.query, args.list_queries, args.as_of,
        )
    if args.command == "discover-software":
        return discover_software(
            root, args.area, args.language, args.ecosystem, args.open_source, args.country, args.software,
            args.check, args.query, args.list_queries, args.as_of,
        )
    if args.command == "freshness":
        try:
            as_of = dt.date.fromisoformat(args.as_of) if args.as_of else dt.date.today()
        except ValueError:
            print(f"ERROR: --as-of must be an ISO date (YYYY-MM-DD), got {args.as_of!r}")
            return 2
        return freshness(root, as_of)
    return generate(root, args.check)


if __name__ == "__main__":
    raise SystemExit(main())
