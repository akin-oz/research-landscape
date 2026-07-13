---
schema_version: 2
entity_type: research-software
id: SW-QBOX
name: Qbox
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-QBOX-REPOSITORY]
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE, AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE]
open_source: "yes"
website: https://qboxcode.org/
repository_url: https://github.com/qboxcode/qbox-public
license: GPL-2.0-or-later
programming_language_ids: [PROGRAMMING-LANGUAGE-CPP]
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-CPP
    source_ids: [SRC-QBOX-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
---

# Qbox

Qbox is an open C++/MPI/OpenMP implementation of first-principles molecular
dynamics and plane-wave density-functional theory. Its separate ecosystem
record owns public source and participation routes.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-QBOX-REPOSITORY` | [qboxcode/qbox-public](https://github.com/qboxcode/qbox-public) identifies Qbox as a C++/MPI/OpenMP first-principles molecular-dynamics implementation with plane-wave DFT electronic-structure calculations, displays GPL-2.0 licensing, states GPL version 2 or later distribution, and exposes issues and pull requests. Accessed 2026-07-13. |

## Boundary and limitations

This record makes no claim about performance, support, funding, mentoring,
admissions, applicant fit, or every Qbox contributor or interface.
