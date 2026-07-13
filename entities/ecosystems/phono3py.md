---
schema_version: 2
entity_type: research-ecosystem
id: ECO-PHONO3PY
name: Phono3py Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-PHONO3PY-DOCUMENTATION, SRC-PHONO3PY-REPOSITORY]
ecosystem_kind: open phonon–phonon-interaction and thermal-transport software ecosystem
website: https://phonopy.github.io/phono3py/
software_ids: [SW-PHONO3PY]
principal_investigator_ids: [PI-ATSUSHI-TOGO]
relationship_assertions:
  - predicate: includes
    target_id: SW-PHONO3PY
    source_ids: [SRC-PHONO3PY-DOCUMENTATION, SRC-PHONO3PY-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: PI-ATSUSHI-TOGO
    role: contributor
    source_ids: [SRC-PHONO3PY-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
    notes: Phono3py documentation lists Atsushi Togo at NIMS as a contributor. This does not establish current maintenance, governance, review authority, or an exclusive contribution claim.
---

# Phono3py Ecosystem

The Phono3py ecosystem records public documentation, source, issue,
pull-request, and mailing-list routes around the distinct `SW-PHONO3PY`
software artifact, plus a bounded contributor connection.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PHONO3PY-DOCUMENTATION` | [Phono3py documentation](https://phonopy.github.io/phono3py/) publishes installation, workflow, Python API, calculator-interface, mailing-list, license, and contributor information for Phono3py. Accessed 2026-07-13. |
| `SRC-PHONO3PY-REPOSITORY` | [phonopy/phono3py](https://github.com/phonopy/phono3py) is the public Phono3py source repository; its README identifies GitHub issues for issue discussion and pull requests for requests to merge source code. Accessed 2026-07-13. |

## Boundary and limitations

Public routes do not establish contributor roles beyond the stated listing,
acceptance, review, response, support, mentoring, membership, funding,
admissions, or applicant fit. Documented calculator interfaces and dependencies
do not create relations for external software.
