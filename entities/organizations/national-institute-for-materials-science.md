---
schema_version: 2
entity_type: organization
id: ORG-NIMS
name: National Institute for Materials Science
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-NIMS-TOGO-PROFILE]
country_id: COUNTRY-JP
city: Tsukuba
organization_kind: national research institute
website: https://www.nims.go.jp/eng/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-JP
    source_ids: [SRC-NIMS-TOGO-PROFILE]
    confidence: high
    evidence_window: 2026-07
---

# National Institute for Materials Science

The National Institute for Materials Science (NIMS) is the direct organization
host for the specifically reviewed Computational Materials Science Group in
this slice.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NIMS-TOGO-PROFILE` | [NIMS Researchers Directory: Atsushi Togo](https://samurai.nims.go.jp/profiles/togo_atsushi?locale=en) identifies Atsushi Togo as Group Leader of the Computational Materials Science Group in NIMS's Center for Basic Research on Materials and gives its Tsukuba, Ibaraki, Japan address. Accessed 2026-07-13. |

## Boundary and limitations

This record represents only the direct host and geographic relationship needed
for the reviewed group. It does not claim that every NIMS unit works on
computational materials, or establish a degree route, opening, funding,
mentoring, admissions, or applicant fit.
