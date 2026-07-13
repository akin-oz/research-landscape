---
schema_version: 2
entity_type: research-ecosystem
id: ECO-SPGLIB
name: Spglib Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-SPGLIB-DOCUMENTATION, SRC-SPGLIB-REPOSITORY]
ecosystem_kind: open crystal-symmetry software ecosystem
website: https://spglib.readthedocs.io/en/stable/
software_ids: [SW-SPGLIB]
principal_investigator_ids: [PI-ATSUSHI-TOGO]
relationship_assertions:
  - predicate: includes
    target_id: SW-SPGLIB
    source_ids: [SRC-SPGLIB-DOCUMENTATION, SRC-SPGLIB-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: PI-ATSUSHI-TOGO
    role: main-developer
    source_ids: [SRC-SPGLIB-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
    notes: Spglib documentation names Atsushi Togo among current main developers. This does not establish exclusive ownership, a complete maintainer roster, governance, review authority, or contribution frequency beyond that stated role.
---

# Spglib Ecosystem

The Spglib ecosystem records public documentation, source, issue, discussion,
and pull-request routes around the distinct `SW-SPGLIB` software artifact, plus
a bounded current-main-developer connection.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SPGLIB-DOCUMENTATION` | [Spglib documentation](https://spglib.readthedocs.io/en/stable/) documents project features, public repository, BSD-3-Clause license, contributors, and current main developers including Atsushi Togo at NIMS. Accessed 2026-07-13. |
| `SRC-SPGLIB-REPOSITORY` | [spglib/spglib](https://github.com/spglib/spglib) is the public source repository and exposes issues, pull requests, and discussions. Accessed 2026-07-13. |

## Boundary and limitations

Public routes do not establish contributor acceptance, review response,
support, mentoring, funding, admissions, applicant fit, or a complete project
community. Project interfaces do not create dependency relations.
