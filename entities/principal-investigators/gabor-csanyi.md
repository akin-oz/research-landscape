---
schema_version: 2
entity_type: principal-investigator
id: PI-GABOR-CSANYI
name: Gábor Csányi
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-CAMBRIDGE-CSANYI-PROFILE
  - SRC-MACE-REPOSITORY
affiliation_ids:
  - UNIVERSITY-CAMBRIDGE
research_area_ids:
  - AREA-MACHINE-LEARNED-POTENTIALS
website: https://www.eng.cam.ac.uk/profiles/gc121
relationship_assertions:
  - predicate: affiliated_with
    target_id: UNIVERSITY-CAMBRIDGE
    source_ids: [SRC-CAMBRIDGE-CSANYI-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-MACHINE-LEARNED-POTENTIALS
    source_ids: [SRC-CAMBRIDGE-CSANYI-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: develops
    target_id: SW-MACE
    role: group-attributed-development
    source_ids: [SRC-MACE-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The repository attributes the reference implementation to the group of Gábor Csányi and named contributors; it does not identify an individual coding, maintenance, governance, or release role for Csányi.
---

# Gábor Csányi

Gábor Csányi is represented for the publicly documented University of Cambridge
affiliation, machine-learning interatomic-potential research, and the bounded
group-attributed MACE development connection. The latter is not promoted to an
individual maintainer or sole-author claim.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-CAMBRIDGE-CSANYI-PROFILE` | [University of Cambridge Department of Engineering: Gábor Csányi](https://www.eng.cam.ac.uk/profiles/gc121) identifies him as Professor of Molecular Modelling in the Mechanics, Materials and Design division and describes his work applying machine learning to materials-modelling problems, including deriving force fields (interatomic potentials) from ab initio electronic-structure data. Accessed 2026-07-12. |
| `SRC-MACE-REPOSITORY` | [ACEsuit/mace](https://github.com/ACEsuit/mace) identifies the MACE reference implementation as developed by named contributors and the group of Gábor Csányi. It is used only for a group-attributed development relationship, not to infer individual code authorship or current maintenance. Accessed 2026-07-12. |

## Boundary and limitations

This record does not add a separate research-group identity from a generic
departmental group label, infer a current opening, supervision capacity,
mentoring, funding, admissions, working language, or applicant fit, or
attribute all MACE development to Csányi personally.
