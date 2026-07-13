---
schema_version: 2
entity_type: research-problem
id: PROBLEM-ATOMISTIC-STRUCTURE-OPTIMIZATION
name: Atomistic Structure Optimization
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-ASE-OPTIMIZATION
  - SRC-DTU-CAMD-ATOMIC-DESIGN
problem_kind: atomistic structure-relaxation and optimization challenge
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE]
relationship_assertions:
  - predicate: addresses
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-DTU-CAMD-ATOMIC-DESIGN]
    confidence: high
    evidence_window: 2026-07
---

# Atomistic Structure Optimization

This record models the bounded computational challenge of optimizing or
relaxing atomistic structures through local or global optimization methods. It
does not claim that an optimizer, calculator, potential, initial structure,
workflow, software package, or research problem is best.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-ASE-OPTIMIZATION` | [ASE documentation: Structure optimization](https://ase-lib.org/ase/optimize.html) documents local and global optimization algorithms, structure-optimization classes that relax `Atoms` objects, and optional cell optimization through filters. Accessed 2026-07-13. |
| `SRC-DTU-CAMD-ATOMIC-DESIGN` | [DTU Physics: Atomic-scale Materials Design](https://physics.dtu.dk/research/sections/camd/research/Atomic-scale-Materials-Design) identifies CAMD's atomistic materials-design work, including ASE/GPAW development and global optimization. It supports only this problem's controlled Computational Materials Science classification. Accessed 2026-07-13. |

## Boundary and limitations

This is a discoverable computational challenge, not a project, benchmark,
convergence guarantee, force-field or calculator comparison, funding call,
importance ranking, or recommendation for a particular researcher, workflow,
or software package.
