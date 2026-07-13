---
schema_version: 2
entity_type: research-problem
id: PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION
name: Lattice Thermal Conductivity Prediction
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-PHONO3PY-DOCUMENTATION]
problem_kind: computational materials prediction challenge
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE, AREA-COMPUTATIONAL-PHONON-CALCULATIONS]
relationship_assertions:
  - predicate: addresses
    target_id: AREA-COMPUTATIONAL-PHONON-CALCULATIONS
    source_ids: [SRC-PHONO3PY-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
---

# Lattice Thermal Conductivity Prediction

This record models the bounded computational challenge of predicting lattice
thermal conductivity from phonon–phonon interaction calculations. It is not a
claim that this is the most important problem, a complete formulation of the
field, or a comparison of methods.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PHONO3PY-DOCUMENTATION` | [Phono3py documentation](https://phonopy.github.io/phono3py/) describes calculating phonon–phonon interactions and related properties, including lattice thermal conductivity by relaxation-time approximation and direct solution of the phonon Boltzmann equation. Accessed 2026-07-13. |

## Boundary and limitations

This is a discoverable computational challenge, not a project, funding call,
benchmark, claim of novelty, priority ranking, method-quality comparison, or
recommendation for a particular researcher.
