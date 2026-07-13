---
schema_version: 2
entity_type: research-ecosystem
id: ECO-CP2K
name: CP2K Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-CP2K-REPOSITORY
  - SRC-CP2K-DOWNLOAD
  - SRC-CP2K-DEVELOPMENT
ecosystem_kind: open quantum-chemistry, atomistic-simulation, and solid-state-physics software ecosystem
website: https://www.cp2k.org/
software_ids:
  - SW-CP2K
relationship_assertions:
  - predicate: includes
    target_id: SW-CP2K
    source_ids: [SRC-CP2K-REPOSITORY, SRC-CP2K-DOWNLOAD]
    confidence: high
    evidence_window: 2026-07
---

# CP2K Ecosystem

The CP2K ecosystem is represented separately from the CP2K software artifact.
It records the documented public development, installation, manual,
discussion, and testing surfaces around the code without presenting a complete
developer, institution, funding, or governance roster.

## Contribution and learning surfaces

CP2K publishes source, releases, installation paths, a manual, a dashboard,
and a public developer workflow. Its development guidance asks contributors to
work through forks and pull requests, add and run suitable regression tests,
and use the project's CI checks. These are transparent learning and
contribution routes, not a promise of review, acceptance, support, access, or
mentoring.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-CP2K-REPOSITORY` | [cp2k/cp2k](https://github.com/cp2k/cp2k) supplies the public CP2K source, links installation, documentation, a dashboard, and a user-support discussion surface, and identifies GPL-2.0 licensing. Accessed 2026-07-13. |
| `SRC-CP2K-DOWNLOAD` | [CP2K: Downloading CP2K](https://www.cp2k.org/download) identifies open GPL source, released and development versions, public Git access, installation guidance, and developer resources including issue tracking, discussions, testing, and a dashboard. Accessed 2026-07-13. |
| `SRC-CP2K-DEVELOPMENT` | [CP2K: Starting development](https://www.cp2k.org/dev:starting) documents fork-and-pull-request contribution, formatting, compile and regression-test expectations, and CI checks before integration. Accessed 2026-07-13. |

## Boundary and limitations

This record does not enumerate every developer, maintainer, reviewer,
contributor, institution, funder, package, subproject, method, library,
interface, release, test, event, or user. It does not infer individual role,
review authority, contribution frequency, employment, support, supervision,
mentoring, funding, admissions, or applicant fit from public project material.
