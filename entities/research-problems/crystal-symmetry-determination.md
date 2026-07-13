---
schema_version: 2
entity_type: research-problem
id: PROBLEM-CRYSTAL-SYMMETRY-DETERMINATION
name: Crystal Symmetry Determination
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-SPGLIB-DOCUMENTATION]
problem_kind: computational crystal-structure analysis challenge
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE, AREA-CRYSTAL-SYMMETRY-ANALYSIS]
relationship_assertions:
  - predicate: addresses
    target_id: AREA-CRYSTAL-SYMMETRY-ANALYSIS
    source_ids: [SRC-SPGLIB-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
---

# Crystal Symmetry Determination

This record models the bounded computational challenge of determining a
crystal structure's symmetry operations and space group. It is not a claim
that one symmetry representation, method, or software implementation is best.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SPGLIB-DOCUMENTATION` | [Spglib documentation](https://spglib.readthedocs.io/en/stable/) documents functions for finding symmetry operations and identifying a space group from a crystal structure. Accessed 2026-07-13. |

## Boundary and limitations

This is a discoverable computational challenge, not a project, funding call,
benchmark, statement of novelty, importance ranking, method-quality comparison,
or recommendation for a particular researcher.
