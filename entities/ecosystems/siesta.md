---
schema_version: 2
entity_type: research-ecosystem
id: ECO-SIESTA
name: SIESTA Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-SIESTA-REPOSITORY
  - SRC-SIESTA-INSTALLATION
  - SRC-SIESTA-CONTRIBUTING
ecosystem_kind: open first-principles and electronic-structure software ecosystem
website: https://siesta-project.org/siesta
software_ids:
  - SW-SIESTA
relationship_assertions:
  - predicate: includes
    target_id: SW-SIESTA
    source_ids: [SRC-SIESTA-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
---

# SIESTA Ecosystem

The SIESTA ecosystem is modeled separately from the SIESTA code. It captures
the documented public source, installation, documentation, GitLab, and
contribution routes without treating those routes as a complete contributor,
maintainer, institution, funding, or governance graph.

## Contribution and learning surfaces

SIESTA publishes source, documentation, tutorials, installation guidance, and
GitLab issue and merge-request routes. Its contribution guidance describes
forking the official repository into a personal namespace, synchronizing an
upstream remote, and opening a merge request for a completed change. These are
transparent participation routes, not a promise of account access, acceptance,
review, response, support, mentoring, or membership.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SIESTA-REPOSITORY` | [siesta-project/siesta](https://gitlab.com/siesta-project/siesta) is the public official source repository and links project documentation, installation, tutorials, issues, and release surfaces. Accessed 2026-07-13. |
| `SRC-SIESTA-INSTALLATION` | [SIESTA Quick install](https://docs.siesta-project.org/projects/siesta/en/stable/installation/quick-install.html) documents conda and source-installation routes plus serial and parallel build context. Accessed 2026-07-13. |
| `SRC-SIESTA-CONTRIBUTING` | [Contributing code to SIESTA](https://siesta-project.org/siesta/Developers/Contributing-to-SIESTA.html) documents forking the official GitLab repository, maintaining an upstream remote, and creating a merge request. Accessed 2026-07-13. |

## Boundary and limitations

This record does not enumerate every developer, maintainer, reviewer,
contributor, institution, funder, package, method, extension, dependency,
release, test, event, or user. It does not infer individual role, review
authority, contribution frequency, employment, support, supervision,
mentoring, funding, admissions, or applicant fit from public project material.
