---
schema_version: 2
entity_type: principal-investigator
id: PI-ATSUSHI-TOGO
name: Atsushi Togo
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-NIMS-TOGO-PROFILE, SRC-NIMS-PHONOPY-FEATURE, SRC-PHONOPY-DOCUMENTATION]
affiliation_ids: [ORG-NIMS]
research_group_ids: [RG-NIMS-COMPUTATIONAL-MATERIALS-SCIENCE]
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE]
website: https://samurai.nims.go.jp/profiles/togo_atsushi?locale=en
relationship_assertions:
  - predicate: affiliated_with
    target_id: ORG-NIMS
    source_ids: [SRC-NIMS-TOGO-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: leads
    target_id: RG-NIMS-COMPUTATIONAL-MATERIALS-SCIENCE
    role: group-leader
    source_ids: [SRC-NIMS-TOGO-PROFILE, SRC-NIMS-PHONOPY-FEATURE]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-NIMS-TOGO-PROFILE, SRC-NIMS-PHONOPY-FEATURE]
    confidence: high
    evidence_window: 2026-07
  - predicate: develops
    target_id: SW-PHONOPY
    role: developer-maintainer
    source_ids: [SRC-NIMS-PHONOPY-FEATURE]
    confidence: high
    evidence_window: 2026-03
    notes: NIMS's March 2026 feature identifies Togo as the developer who continues to expand and maintain Phonopy. This does not establish exclusive ownership, a complete maintainer roster, governance, review authority, or contribution frequency beyond that stated role.
---

# Atsushi Togo

Atsushi Togo is represented for current NIMS affiliation, Computational
Materials Science Group leadership, computational-materials research, and the
bounded NIMS-described Phonopy developer-maintainer role.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NIMS-TOGO-PROFILE` | [NIMS Researchers Directory: Atsushi Togo](https://samurai.nims.go.jp/profiles/togo_atsushi?locale=en) identifies Togo as Group Leader of the Computational Materials Science Group at NIMS and lists phonon-calculation research and scientific-computing software development. Accessed 2026-07-13. |
| `SRC-NIMS-PHONOPY-FEATURE` | [NIMS NOW: Phonopy](https://nimsnow.nims.go.jp/en/research/2026no2_r01/) identifies Togo as developer and Group Leader, and states that he continues to expand Phonopy's capabilities and maintain the software. The feature is current as of March 2026. Accessed 2026-07-13. |
| `SRC-PHONOPY-DOCUMENTATION` | [Phonopy documentation](https://phonopy.github.io/phonopy/) lists Atsushi Togo of the National Institute for Materials Science among contributors. Accessed 2026-07-13. |

## Boundary and limitations

This record makes no claim about a complete maintenance or governance roster,
exclusive ownership, review authority, contribution frequency, supervision,
mentoring, admissions, funding, openings, language skill, or applicant fit.
