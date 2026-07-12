---
schema_version: 2
entity_type: research-group
id: RG-DTU-CAMD
name: Computational Atomic-scale Materials Design (CAMD)
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-DTU-CAMD-RESEARCH
  - SRC-DTU-CAMD-OVERVIEW
institution_id: UNIVERSITY-DTU
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
software_ids:
  - SW-ASE
website: https://physics.dtu.dk/research/sections/camd
relationship_assertions:
  - predicate: belongs_to
    target_id: UNIVERSITY-DTU
    source_ids: [SRC-DTU-CAMD-OVERVIEW]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-DTU-CAMD-RESEARCH]
    confidence: high
    evidence_window: 2026-07
  - predicate: develops
    target_id: SW-ASE
    source_ids: [SRC-DTU-CAMD-RESEARCH]
    confidence: high
    evidence_window: 2026-07
    notes: CAMD publicly identifies ASE development as group work; this does not assert exclusive development or an individual maintainer roster.
---

# Computational Atomic-scale Materials Design (CAMD)

CAMD is the DTU-hosted research-group node in this slice. Its public research
description supports the Computational Materials Science connection and a
shared, group-level ASE development relationship.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-DTU-CAMD-RESEARCH` | [DTU Physics: Atomic-scale Materials Design](https://physics.dtu.dk/research/sections/camd/research/atomic-scale-materials-design) describes CAMD's development of electronic-structure methods and atomistic simulation techniques, including development of ASE and GPAW. Accessed 2026-07-12. |
| `SRC-DTU-CAMD-OVERVIEW` | [DTU Physics: CAMD](https://physics.dtu.dk/research/sections/camd) identifies CAMD as Computational Atomic-scale Materials Design at DTU Physics. Accessed 2026-07-12. |

## Boundary and limitations

This record does not attribute all ASE development or maintenance to CAMD,
enumerate personnel, or create records for every linked code, database, or
method. It makes no claim about openings, mentoring, admissions, funding,
language, or applicant fit.
