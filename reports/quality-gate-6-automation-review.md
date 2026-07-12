# Quality Gate 6 review: automation

**Gate status:** complete

**Review date:** 2026-07-12

## Gate outcome

Quality Gate 6 adds one deterministic Python tool,
[`scripts/research_landscape.py`](../scripts/research_landscape.py), plus a
pinned development runtime and CI enforcement. The tool consumes canonical v2
entities and [`views/definitions.yaml`](../views/definitions.yaml), validates
their structural integrity, and produces committed navigation projections and a
repository-health report. It never writes or synthesizes canonical facts.

## Automated coverage

| Required capability | Evidence |
| --- | --- |
| Metadata, schema, and frontmatter validation | v2 frontmatter is parsed with PyYAML and checked against `entity-vnext.schema.json` with JSON Schema format checks. |
| Duplicate detection | Duplicate stable IDs fail validation; same-type normalized-name collisions are health warnings. |
| Reference and relationship integrity | Typed metadata references, predicate/endpoint pairs, record-local relationship sources, and unresolved IDs are checked. |
| Direct-host integrity | Reviewed/published groups must satisfy ADR 0006's exactly-one host field, target type, and matching `belongs_to` assertion. |
| Broken links | Relative Markdown links across repository Markdown are checked. |
| Orphan detection | Entities with no inbound/outbound graph connection are reported as health warnings, excluding controlled roots. |
| Migration validation | v2 records must live in their approved entity-type directory; v2 frontmatter outside `entities/` fails validation. |
| Deterministic view generation | Ten public views are generated from the 13-view manifest; private views intentionally generate no public output. |
| Repository health and quality metrics | The generated health report counts entities, confidence coverage, relationship predicates, migration status, errors, and warnings. |
| CI enforcement | GitHub Actions installs pinned dependencies, validates the graph, and runs generation in `--check` mode. |

## Generated-output boundary

The public projections under [`views/generated/`](../views/generated/README.md)
and the health report under
[`reports/generated/`](generated/repository-health.md) carry a generated-file
banner and content fingerprint. The fingerprint is derived from canonical
entities, the v2 schema, and view definitions, so identical inputs produce
byte-identical output. CI fails if output has drifted.

Generated output shows concise metadata and canonical links only. It does not
copy entity bodies, evidence tables, private shortlist data, subjective scores,
or inferred inverse relationships. Private Current Focus, My Shortlist, and
Waiting List views remain intentionally absent from the public repository.

## Verification record

On 2026-07-12 the following passed:

```text
python3 scripts/research_landscape.py validate
python3 scripts/research_landscape.py generate
python3 scripts/research_landscape.py generate --check
```

The corpus contains 67 v2 entities and 116 typed relationship assertions, with
zero validation errors and zero duplicate-name or orphan warnings. JSON Schema
files also parse in CI.

## Known limitations

- Local link validation checks path existence, not remote URL availability or
  anchor fragments.
- Confidence and freshness metrics reflect declared metadata; they do not judge
  scientific quality, prestige, mentorship, or applicant fit.
- The generator supports the declared current corpus and documented paths. New
  predicates or entity types require an architecture/schema review and test
  coverage before becoming generated-view behavior.
- Source IDs remain record-local citations, not a first-class source graph.

## QG7 handoff

Quality Gate 7 may build explainable recommendation queries only from these
validated canonical records and generated view inputs. It must use declared,
versioned rules; show supporting evidence, confidence, coverage, and
limitations; and never infer prestige or accessibility into a global result.
