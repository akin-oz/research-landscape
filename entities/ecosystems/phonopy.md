---
schema_version: 2
entity_type: research-ecosystem
id: ECO-PHONOPY
name: Phonopy Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-PHONOPY-DOCUMENTATION, SRC-PHONOPY-REPOSITORY]
ecosystem_kind: open phonon-calculation software ecosystem
website: https://phonopy.github.io/phonopy/
software_ids: [SW-PHONOPY]
principal_investigator_ids: [PI-ATSUSHI-TOGO]
relationship_assertions:
  - predicate: includes
    target_id: SW-PHONOPY
    source_ids: [SRC-PHONOPY-DOCUMENTATION, SRC-PHONOPY-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: PI-ATSUSHI-TOGO
    role: contributor
    source_ids: [SRC-PHONOPY-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
    notes: Phonopy documentation lists Atsushi Togo at NIMS as a contributor. This does not establish current maintenance, governance, review authority, or an exclusive contribution claim.
---

# Phonopy Ecosystem

The Phonopy ecosystem records public documentation, source, issue,
pull-request, and mailing-list routes around the distinct `SW-PHONOPY`
software artifact, plus a bounded documented contributor connection.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PHONOPY-DOCUMENTATION` | [Phonopy documentation](https://phonopy.github.io/phonopy/) publishes installation, workflow, Python-API, calculator-interface, mailing-list, license, and contributor information for Phonopy. Accessed 2026-07-13. |
| `SRC-PHONOPY-REPOSITORY` | [phonopy/phonopy](https://github.com/phonopy/phonopy) is the public Phonopy source repository; its README identifies GitHub issues for issue discussion and pull requests for requests to merge source code. Accessed 2026-07-13. |

## Boundary and limitations

Public routes do not establish contributor roles, acceptance, review, response,
support, mentoring, membership, funding, admissions, or applicant fit. The
documented calculator interfaces do not create dependency or ecosystem-member
relations for external software.
