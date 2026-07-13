---
schema_version: 2
entity_type: research-problem
id: PROBLEM-MATERIALS-PROPERTY-PREDICTION
name: Materials Property Prediction
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-CHGNET-HOME, SRC-MATGL-DOCUMENTATION]
problem_kind: atomistic materials-property prediction challenge
research_area_ids: [AREA-AI-FOR-MATERIALS, AREA-MATERIALS-INFORMATICS]
relationship_assertions:
  - predicate: addresses
    target_id: AREA-AI-FOR-MATERIALS
    source_ids: [SRC-CHGNET-HOME, SRC-MATGL-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
  - predicate: addresses
    target_id: AREA-MATERIALS-INFORMATICS
    source_ids: [SRC-CHGNET-HOME, SRC-MATGL-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
---

# Materials Property Prediction

This record models the bounded challenge of predicting materials properties
from atomic structures with graph-based machine-learning models. It does not
claim that a particular model, property target, dataset, or workflow is best.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-CHGNET-HOME` | [CHGNet](https://chgnet.lbl.gov/) documents prediction of energy, forces, stress, and magnetic moments from a structure. Accessed 2026-07-13. |
| `SRC-MATGL-DOCUMENTATION` | [MatGL documentation](https://matgl.ai/) describes materials graph deep-learning models as surrogate models for materials-property prediction and documents pretrained property models. Accessed 2026-07-13. |

## Boundary and limitations

This is a discoverable computational challenge, not a project, funding call,
benchmark, importance ranking, performance comparison, or recommendation for a
particular researcher, model, dataset, or software package.
