---
schema_version: 2
entity_type: research-ecosystem
id: ECO-ABINIT
name: ABINIT Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-ABINIT-HOME
  - SRC-ABINIT-GIT
  - SRC-ABINIT-DEVELOPMENT
ecosystem_kind: open DFT, materials-simulation, and electronic-structure software ecosystem
website: https://www.abinit.org/
software_ids:
  - SW-ABINIT
relationship_assertions:
  - predicate: includes
    target_id: SW-ABINIT
    source_ids: [SRC-ABINIT-HOME]
    confidence: high
    evidence_window: 2026-07
---

# ABINIT Ecosystem

The ABINIT ecosystem is modeled separately from the ABINIT software suite. It
captures documented public learning, discussion, development, source-control,
and testing surfaces without turning a worldwide-open development philosophy
into a complete person, institutional, funding, or governance graph.

## Contribution and learning surfaces

ABINIT's public home provides packages, sources, installation, tutorials,
schools, workshops, mailing-list/forum routes, and a developer corner. Its
documentation describes Git control, a GitHub mirror that welcomes bug fixes
and improvements, and active development hosted on the project's internal
GitLab. The developer overview documents collaboration, Git/GitLab, testing,
and related project tools. These are contribution and learning routes, not a
promise of access, review, acceptance, response, support, mentoring, or
membership.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-ABINIT-HOME` | [ABINIT](https://www.abinit.org/) presents software packages and sources, installation, tutorials, schools/workshops, mailing-list/forum links, and a developer corner around the materials DFT suite. Accessed 2026-07-13. |
| `SRC-ABINIT-GIT` | [ABINIT: Git](https://docs.abinit.org/topics/Git/) documents Gitflow-based development, the official GitHub mirror welcoming bug fixes and improvements, the internal GitLab location of most active development, and links to the ABINIT GitHub organization. Accessed 2026-07-13. |
| `SRC-ABINIT-DEVELOPMENT` | [ABINIT: development overview](https://docs.abinit.org/developers/overview_development/) describes collaboration by groups in different locations, worldwide-open contribution, and a developer environment including Git, GitLab, testing, Fortran90, MPI, and Python. Accessed 2026-07-13. |

## Boundary and limitations

This record does not enumerate every developer, maintainer, reviewer,
contributor, organization, funder, consortium, package, utility, data table,
method, school, workshop, event, or user. It does not infer individual role,
review authority, contribution frequency, employment, support, supervision,
mentoring, funding, admissions, or applicant fit.
