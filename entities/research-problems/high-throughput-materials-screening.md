---
schema_version: 2
entity_type: research-problem
id: PROBLEM-HIGH-THROUGHPUT-MATERIALS-SCREENING
name: High-Throughput Materials Screening
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-AFLOW-DOCUMENTATION]
problem_kind: computational materials screening challenge
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE]
relationship_assertions:
  - predicate: addresses
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-AFLOW-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
---

# High-Throughput Materials Screening

This record models the bounded computational challenge of screening materials
with high-throughput workflows using first-principles calculations and data
informatics. It does not claim that a screening strategy, property target,
database, dataset, workflow, or software package is best.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-AFLOW-DOCUMENTATION` | [AFLOW documentation](https://aflow.org/aflow-documentation/index.html) describes software tools for high-throughput materials discovery using DFT and data informatics as a screening strategy. Accessed 2026-07-13. |

## Boundary and limitations

This is a discoverable computational challenge, not a project, benchmark,
dataset, database comparison, funding call, importance ranking, or
recommendation for a particular researcher, workflow, or software package.
