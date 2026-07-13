---
schema_version: 2
entity_type: research-ecosystem
id: ECO-FLEUR
name: FLEUR Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-FLEUR-HOME
  - SRC-FLEUR-REPOSITORY
  - SRC-FLEUR-INSTALLATION
  - SRC-FLEUR-DEVELOPERS
ecosystem_kind: open all-electron DFT and electronic-structure software ecosystem
website: https://www.flapw.de/
software_ids:
  - SW-FLEUR
relationship_assertions:
  - predicate: includes
    target_id: SW-FLEUR
    source_ids: [SRC-FLEUR-HOME, SRC-FLEUR-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
---

# FLEUR Ecosystem

The FLEUR ecosystem is modeled separately from the FLEUR code. It records public
source, download, documentation, tutorial, forum, test, and developer routes
without representing a complete community, institution, funding, or governance
graph.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-FLEUR-HOME` | [FLEUR](https://www.flapw.de/) links the public code, GitLab repository, MIT license, documentation, tutorial, and user forum. Accessed 2026-07-13. |
| `SRC-FLEUR-REPOSITORY` | [fleur/fleur](https://iffgit.fz-juelich.de/fleur/fleur) is the official public GitLab source repository. Accessed 2026-07-13. |
| `SRC-FLEUR-INSTALLATION` | [FLEUR installation](https://www.flapw.de/master/documentation/installation/) documents Git retrieval, build requirements, configuration, and automated test guidance. Accessed 2026-07-13. |
| `SRC-FLEUR-DEVELOPERS` | [FLEUR developers guide](https://www.flapw.de/MaX-8.0/develop-main/) states that contributions are welcome and directs contributors to the open-source MIT development model. Accessed 2026-07-13. |

## Boundary and limitations

Public routes do not establish access, acceptance, review, response, support,
mentoring, membership, individual role, contributor roster, funder, employment,
supervision, admissions, or applicant fit.
