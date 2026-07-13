---
schema_version: 2
entity_type: research-problem
id: PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION
name: Density-Functional Electronic-Structure Calculation
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-ABINIT-PRESENTATION, SRC-QE-HOME, SRC-GPAW-DOCUMENTATION, SRC-SIESTA-REFERENCE-MANUAL]
problem_kind: first-principles electronic-structure calculation challenge
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE, AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE]
relationship_assertions:
  - predicate: addresses
    target_id: AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE
    source_ids: [SRC-ABINIT-PRESENTATION, SRC-QE-HOME, SRC-GPAW-DOCUMENTATION, SRC-SIESTA-REFERENCE-MANUAL]
    confidence: high
    evidence_window: 2026-07
---

# Density-Functional Electronic-Structure Calculation

This record models the bounded computational challenge of obtaining
electronic-structure quantities for molecules, solids, or materials with
density-functional methods. It does not claim that one functional, basis,
pseudopotential, numerical method, or software package is best.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-ABINIT-PRESENTATION` | [ABINIT presentation](https://www.abinit.org/presentation.html) describes obtaining total energy, charge density, and electronic structure for molecules and periodic solids within DFT. Accessed 2026-07-13. |
| `SRC-QE-HOME` | [Quantum ESPRESSO](https://www.quantum-espresso.org/) describes open-source codes for electronic-structure calculations and nanoscale materials modeling based on density-functional theory. Accessed 2026-07-13. |
| `SRC-GPAW-DOCUMENTATION` | [GPAW documentation](https://gpaw.readthedocs.io/) describes GPAW as a DFT code and documents electronic-structure calculation tutorials. Accessed 2026-07-13. |
| `SRC-SIESTA-REFERENCE-MANUAL` | [SIESTA reference manual](https://docs.siesta-project.org/projects/siesta/en/5.4/reference/siesta.html) describes electronic-structure calculations for molecules and solids using Kohn-Sham density-functional methods. Accessed 2026-07-13. |

## Boundary and limitations

This is a discoverable computational challenge, not a project, funding call,
benchmark, claim of novelty, importance ranking, method-quality comparison, or
recommendation for a particular researcher, approximation, dataset, or tool.
