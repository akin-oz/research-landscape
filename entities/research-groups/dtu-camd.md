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
  - SRC-DTU-CAMD-SOFTWARE
  - SRC-DTU-CAMD-ATOMIC-DESIGN
  - SRC-DTU-CAMD-QUANTUM-MATERIALS
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

The current section page presents four named research-group leaders spanning
atomic-scale design, magnetism/spin-orbit physics, computational quantum
materials, and nanoparticles/electron microscopy. CAMD describes its CAMPOS
software collection as Python-interface programs released under the GNU GPL,
and its Atomic-scale Materials Design page identifies ASE/GPAW, databases,
machine-learning screening, global optimization, and DFT uncertainty work.
One CAMD sub-group page identifies a VILLUM-funded project; it is not a
section-wide funding ledger or a new canonical funding relationship.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-DTU-CAMD-RESEARCH` | [DTU Physics: Atomic-scale Materials Design](https://physics.dtu.dk/research/sections/camd/research/atomic-scale-materials-design) describes CAMD's development of electronic-structure methods and atomistic simulation techniques, including development of ASE and GPAW. Accessed 2026-07-12. |
| `SRC-DTU-CAMD-OVERVIEW` | [DTU Physics: CAMD](https://physics.dtu.dk/research/sections/camd) identifies CAMD as Computational Atomic-scale Materials Design at DTU Physics. Accessed 2026-07-12. |
| `SRC-DTU-CAMD-SOFTWARE` | [DTU Physics: CAMD software](https://physics.dtu.dk/research/sections/camd/about/software) describes the CAMPOS collection for atomic-scale simulations, its Python interfaces, shared ASE tools, GNU GPL licensing, and public invitation to use and develop the code. It does not establish a group-wide language policy or individual maintenance roster. Accessed 2026-07-12. |
| `SRC-DTU-CAMD-ATOMIC-DESIGN` | [DTU Physics: Atomic-scale Materials Design](https://physics.dtu.dk/research/sections/camd/research/Atomic-scale-Materials-Design) identifies ASE/GPAW development, low-dimensional-material databases, ML screening, global optimization, and DFT uncertainty quantification. It is group-scope evidence, not a complete project/software inventory. Accessed 2026-07-12. |
| `SRC-DTU-CAMD-QUANTUM-MATERIALS` | [DTU Physics: Computational Quantum Materials](https://physics.dtu.dk/research/sections/camd/research/Computational-Quantum-Materials) identifies a CAMD sub-group’s research topics, open codes/databases, BSc/MSc project routes, and a VILLUM Foundation grant for its named project. This is sub-group-specific and does not establish CAMD-wide funding, capacity, or a complete project catalog. Accessed 2026-07-12. |

## Boundary and limitations

This record does not attribute all ASE development or maintenance to CAMD,
enumerate personnel, or create records for every linked code, database, or
method. It makes no live-opening, admissions, CAMD-wide funding, group-wide
language, applicant-fit, mentoring-quality, or career-outcome claim.
