---
schema_version: 2
entity_type: research-problem
id: PROBLEM-MACHINE-LEARNED-INTERATOMIC-POTENTIAL-MODELING
name: Machine-Learned Interatomic Potential Modeling
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-MACE-DOCUMENTATION, SRC-NEQUIP-DOCUMENTATION, SRC-DEEPMD-DOCUMENTATION]
problem_kind: atomistic machine-learning modeling challenge
research_area_ids: [AREA-AI-FOR-MATERIALS, AREA-MACHINE-LEARNED-POTENTIALS]
relationship_assertions:
  - predicate: addresses
    target_id: AREA-AI-FOR-MATERIALS
    source_ids: [SRC-MACE-DOCUMENTATION, SRC-NEQUIP-DOCUMENTATION, SRC-DEEPMD-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
  - predicate: addresses
    target_id: AREA-MACHINE-LEARNED-POTENTIALS
    source_ids: [SRC-MACE-DOCUMENTATION, SRC-NEQUIP-DOCUMENTATION, SRC-DEEPMD-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
---

# Machine-Learned Interatomic Potential Modeling

This record models the bounded computational challenge of constructing and
using machine-learned interatomic-potential models for atomic systems. It does
not claim that a particular architecture, training procedure, dataset, or
software package is best.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-MACE-DOCUMENTATION` | [MACE introduction](https://mace-docs.readthedocs.io/en/latest/guide/intro.html) describes machine-learning interatomic potentials and provides training documentation. Accessed 2026-07-13. |
| `SRC-NEQUIP-DOCUMENTATION` | [NequIP documentation](https://nequip.readthedocs.io/en/latest/introduction/intro.html) describes E(3)-equivariant interatomic potentials and documents configuration and training techniques. Accessed 2026-07-13. |
| `SRC-DEEPMD-DOCUMENTATION` | [DeePMD-kit documentation](https://deepmd-kit.readthedocs.io/en/stable/) documents preparing data and training a deep-potential model. Accessed 2026-07-13. |

## Boundary and limitations

This is a discoverable computational challenge, not a project, funding call,
benchmark, claim of novelty, importance ranking, performance comparison, or
recommendation for a particular researcher, model, dataset, or software tool.
