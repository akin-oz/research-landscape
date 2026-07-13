---
schema_version: 2
entity_type: research-ecosystem
id: ECO-GPAW
name: GPAW Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-GPAW-DOCUMENTATION
  - SRC-GPAW-INSTALLATION
  - SRC-GPAW-DEVELOPMENT
  - SRC-DTU-CAMD-RESEARCH
ecosystem_kind: open DFT and electronic-structure software ecosystem
website: https://gpaw.readthedocs.io/
software_ids:
  - SW-GPAW
research_group_ids:
  - RG-DTU-CAMD
relationship_assertions:
  - predicate: includes
    target_id: SW-GPAW
    source_ids: [SRC-GPAW-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: RG-DTU-CAMD
    source_ids: [SRC-DTU-CAMD-RESEARCH]
    confidence: high
    evidence_window: 2026-07
    notes: CAMD publicly identifies GPAW development as group work; this does not assert exclusive development, current individual maintenance, or a complete participating-group roster.
---

# GPAW Ecosystem

The GPAW ecosystem is modeled separately from the GPAW software artifact. It
connects the documented code to CAMD's group-level development evidence and
records public installation, development, testing, issue, and contact routes
without treating them as a complete contributor, governance, funding, or
support graph.

## Contribution and learning surfaces

GPAW publishes source and release installation routes, documentation, a
development workflow, test guidance, a GitLab issue and merge-request route,
and public mailing-list and chat context. The workflow describes a project
membership request for pushing branches to the central repository and the
review/CI process. These are transparent participation routes, not a promise
of membership, review, acceptance, response, support, mentoring, or access.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-GPAW-DOCUMENTATION` | [GPAW documentation](https://gpaw.readthedocs.io/) presents the DFT Python code and its ASE basis. Accessed 2026-07-13. |
| `SRC-GPAW-INSTALLATION` | [GPAW installation](https://gpaw.readthedocs.io/install.html) documents PyPI, source-tarball, and Git installation paths, a command-line tool, tests, mailing-list/chat support routes, and the public GitLab project. Accessed 2026-07-13. |
| `SRC-GPAW-DEVELOPMENT` | [GPAW development workflow](https://gpaw.readthedocs.io/devel/workflow.html) documents development-environment setup, tests, merge requests, CI checks, and reviewer workflow. Accessed 2026-07-13. |
| `SRC-DTU-CAMD-RESEARCH` | [DTU Physics: Atomic-scale Materials Design](https://physics.dtu.dk/research/sections/camd/research/atomic-scale-materials-design) identifies CAMD's development of GPAW. Accessed 2026-07-13. |

## Boundary and limitations

This record does not enumerate every developer, maintainer, reviewer,
contributor, institution, funder, package, method, setup, interface, release,
test, event, or user. It does not infer individual role, review authority,
contribution frequency, employment, support, supervision, mentoring, funding,
admissions, or applicant fit from public project material.
