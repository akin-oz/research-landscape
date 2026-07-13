---
schema_version: 2
entity_type: research-group
id: RG-NIMS-COMPUTATIONAL-MATERIALS-SCIENCE
name: Computational Materials Science Group
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-NIMS-TOGO-PROFILE, SRC-NIMS-PHONOPY-FEATURE]
organization_id: ORG-NIMS
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE, AREA-COMPUTATIONAL-PHONON-CALCULATIONS]
website: https://samurai.nims.go.jp/profiles/togo_atsushi?locale=en
relationship_assertions:
  - predicate: belongs_to
    target_id: ORG-NIMS
    source_ids: [SRC-NIMS-TOGO-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-NIMS-TOGO-PROFILE, SRC-NIMS-PHONOPY-FEATURE]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-PHONON-CALCULATIONS
    source_ids: [SRC-NIMS-TOGO-PROFILE, SRC-NIMS-PHONOPY-FEATURE]
    confidence: high
    evidence_window: 2026-07
---

# Computational Materials Science Group at NIMS

This record represents the named NIMS Computational Materials Science Group
led by Atsushi Togo. Its public profile and NIMS feature support its narrowly
modeled computational-materials and phonon-calculation context.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NIMS-TOGO-PROFILE` | [NIMS Researchers Directory: Atsushi Togo](https://samurai.nims.go.jp/profiles/togo_atsushi?locale=en) identifies Atsushi Togo as Group Leader of the Computational Materials Science Group in NIMS's Center for Basic Research on Materials, and lists his research title as phonon-calculation research and scientific-computing software development. Accessed 2026-07-13. |
| `SRC-NIMS-PHONOPY-FEATURE` | [NIMS NOW: Phonopy](https://nimsnow.nims.go.jp/en/research/2026no2_r01/) identifies Togo as Group Leader of NIMS's Computational Materials Science Group and describes Phonopy's material-property phonon calculations. Accessed 2026-07-13. |

## Boundary and limitations

The named group and its public Phonopy context do not establish a complete
roster, group-wide software-development roles, a degree programme, current
openings, funding, mentoring quality, admissions, or applicant fit.
