---
schema_version: 2
entity_type: research-software
id: SW-SPGLIB
name: Spglib
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-SPGLIB-DOCUMENTATION, SRC-SPGLIB-REPOSITORY]
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE, AREA-CRYSTAL-SYMMETRY-ANALYSIS]
open_source: "yes"
website: https://spglib.readthedocs.io/en/stable/
repository_url: https://github.com/spglib/spglib
license: BSD-3-Clause
programming_language_ids: [PROGRAMMING-LANGUAGE-C]
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-C
    source_ids: [SRC-SPGLIB-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
    notes: Spglib documentation describes the library as written in C. Its documented Python, Fortran, Rust, and Ruby interfaces are not treated as implementation-language assertions in this record.
---

# Spglib

Spglib is an open-source C library for finding and handling crystal symmetries.
Its distinct ecosystem record owns public documentation, source, issue,
discussion, and pull-request routes.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SPGLIB-DOCUMENTATION` | [Spglib documentation](https://spglib.readthedocs.io/en/stable/) describes Spglib as a C library for crystal symmetries, documents symmetry operations, space-group identification, Wyckoff assignment, structure refinement, primitive-cell search, C/Python/Fortran/Rust/Ruby interfaces, BSD-3-Clause licensing, and lists Atsushi Togo among current main developers. Accessed 2026-07-13. |
| `SRC-SPGLIB-REPOSITORY` | [spglib/spglib](https://github.com/spglib/spglib) is the public source repository. Its README describes a C library for finding and handling crystal symmetries, exposes issues, pull requests, and discussions, and links its BSD-3-Clause license. Accessed 2026-07-13. |

## Boundary and limitations

This record does not turn documented interfaces into implementation-language
assertions, or make claims about performance, support, funding, mentoring,
admissions, applicant fit, every contributor, or external downstream package.
