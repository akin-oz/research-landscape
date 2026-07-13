---
schema_version: 2
entity_type: research-ecosystem
id: ECO-QBOX
name: Qbox Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-QBOX-REPOSITORY]
ecosystem_kind: open first-principles molecular-dynamics and density-functional-theory software ecosystem
website: https://qboxcode.org/
software_ids: [SW-QBOX]
relationship_assertions:
  - predicate: includes
    target_id: SW-QBOX
    source_ids: [SRC-QBOX-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
---

# Qbox Ecosystem

The Qbox ecosystem records public source, issue, pull-request, documentation,
and download routes without asserting a complete contributor, institution,
funding, maintainer, or support graph.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-QBOX-REPOSITORY` | [qboxcode/qbox-public](https://github.com/qboxcode/qbox-public) is the public Qbox source repository and exposes issues, pull requests, documentation, and project source context. Accessed 2026-07-13. |

## Boundary and limitations

Public routes do not establish access, acceptance, review, response, support,
mentoring, membership, individual role, funding, admissions, or applicant fit.
