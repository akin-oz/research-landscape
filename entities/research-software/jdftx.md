---
schema_version: 2
entity_type: research-software
id: SW-JDFTX
name: JDFTx
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-JDFTX-PROJECT]
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE, AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE]
open_source: "yes"
website: https://jdftx.org/
license: GPL-3.0-or-later
programming_language_ids: [PROGRAMMING-LANGUAGE-CPP]
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-CPP
    source_ids: [SRC-JDFTX-PROJECT]
    confidence: high
    evidence_window: 2026-07
---

# JDFTx

JDFTx is an open plane-wave density-functional-theory code. Its separate
ecosystem record owns public documentation, tutorial, issue, and developer
routes; this record does not model every interface, contributor, or user.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-JDFTX-PROJECT` | [JDFTx documentation](https://jdftx.org/) identifies JDFTx as a plane-wave DFT code, states GPL version 3 or higher distribution, explicitly describes highly templated object-oriented C++11 implementation, and provides tutorials, developer guidance, and issue reporting routes. Accessed 2026-07-13. |

## Boundary and limitations

This record makes no claim about performance, method completeness, support,
funding, openings, mentoring, admissions, or applicant fit.
