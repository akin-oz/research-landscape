---
schema_version: 2
entity_type: research-ecosystem
id: ECO-NEQUIP
name: NequIP Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-NEQUIP-REPOSITORY, SRC-NEQUIP-DOCUMENTATION]
ecosystem_kind: open equivariant machine-learned-potential software ecosystem
website: https://nequip.readthedocs.io/en/latest/
software_ids: [SW-NEQUIP]
relationship_assertions:
  - predicate: includes
    target_id: SW-NEQUIP
    source_ids: [SRC-NEQUIP-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
---

# NequIP Ecosystem

The NequIP ecosystem records public GitHub source, issues, discussions,
tutorials, documentation, and contribution routes without asserting a complete
community, institution, funding, maintainer, or support graph.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NEQUIP-REPOSITORY` | [mir-group/nequip](https://github.com/mir-group/nequip) is the public source repository and exposes issues, pull requests, discussions, releases, tutorial, and contribution context. Accessed 2026-07-13. |
| `SRC-NEQUIP-DOCUMENTATION` | [NequIP documentation](https://nequip.readthedocs.io/en/latest/introduction/intro.html) exposes user, Python API, integration, and developer-guide paths. Accessed 2026-07-13. |

## Boundary and limitations

Public routes do not establish access, acceptance, review, response, support,
mentoring, membership, individual role, contributor roster, employment,
supervision, funding, admissions, or applicant fit.
