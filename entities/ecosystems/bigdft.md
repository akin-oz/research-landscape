---
schema_version: 2
entity_type: research-ecosystem
id: ECO-BIGDFT
name: BigDFT Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-BIGDFT-PROJECT, SRC-BIGDFT-PACKAGE, SRC-BIGDFT-DEVELOPER-GUIDE]
ecosystem_kind: open density-functional-theory software ecosystem
website: https://bigdft.org/
software_ids: [SW-BIGDFT]
relationship_assertions:
  - predicate: includes
    target_id: SW-BIGDFT
    source_ids: [SRC-BIGDFT-PROJECT]
    confidence: high
    evidence_window: 2026-07
---

# BigDFT Ecosystem

The BigDFT ecosystem records public project, documentation, tutorial, GitLab,
and developer routes without asserting a complete community, institution,
funding, maintainer, or support graph.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-BIGDFT-PROJECT` | [BigDFT project site](https://bigdft.org/index.html) links downloads, user/developer resources, tutorials, and a user guide for the public DFT project. Accessed 2026-07-13. |
| `SRC-BIGDFT-PACKAGE` | [BigDFT-suite package documentation](https://bigdft-suite.readthedocs.io/en/latest/overview/package.html) states that suite programs are maintained on its GitLab page. Accessed 2026-07-13. |
| `SRC-BIGDFT-DEVELOPER-GUIDE` | [BigDFT-suite developer guide](https://bigdft-suite.readthedocs.io/en/latest/devel/developers.html) documents Git branching, merge-request, test, and continuous-integration routes. Accessed 2026-07-13. |

## Boundary and limitations

Public routes do not establish access, acceptance, review, response, support,
mentoring, membership, individual role, contributor roster, employment,
supervision, funding, admissions, or applicant fit.
