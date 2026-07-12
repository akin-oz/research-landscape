---
schema_version: 2
entity_type: research-software
id: SW-NOMAD
name: NOMAD
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-NOMAD-REPOSITORY
  - SRC-NOMAD-DOCUMENTATION
  - SRC-NOMAD-ARCHITECTURE
  - SRC-NOMAD-HOWTO
  - SRC-NOMAD-CONTRIBUTION
  - SRC-NOMAD-JOSS-2023
open_source: "yes"
github: https://github.com/nomad-coe/nomad
repository_url: https://github.com/nomad-coe/nomad
website: https://nomad-lab.eu/
license: Apache-2.0
programming_language_ids:
  - PROGRAMMING-LANGUAGE-PYTHON
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-PYTHON
    source_ids: [SRC-NOMAD-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The project-owned repository exposes NOMAD as a Python package and identifies Python as a repository implementation language. This does not assert that every component, plugin, or contributor uses Python.
---

# NOMAD

NOMAD is represented as a distinct research-software artifact. The FAIRmat
ecosystem record supplies its broader, evidence-bounded infrastructure context.

Its public documentation describes a container-oriented application/worker
architecture: the outward-facing application serves the API, graphical user
interface, and documentation, while workers process data. The documentation
also exposes bounded user, plugin, Oasis-hosting, and core-contribution paths;
these are upstream learning and participation surfaces rather than canonical
nodes or promises about access, review, or acceptance.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NOMAD-REPOSITORY` | [FAIRmat-NFDI/nomad](https://github.com/nomad-coe/nomad) describes NOMAD as web-based research-data-management software for materials science, links the official project site, and states the Apache-2.0 license. Accessed 2026-07-12. |
| `SRC-NOMAD-DOCUMENTATION` | [NOMAD Repository and Archive: Introduction](https://nomad-lab.eu/prod/rae/docs/introduction.html) describes NOMAD as storage, processing, management, discovery, and analytics for computational materials-science data, with a web GUI and RESTful API. Accessed 2026-07-12. |
| `SRC-NOMAD-ARCHITECTURE` | [NOMAD documentation: Architecture](https://nomad-lab.eu/prod/v1/docs/explanation/architecture.html) describes the container-oriented application/worker split, API/GUI/documentation, parsing and normalization, and documented supporting services. Accessed 2026-07-12. |
| `SRC-NOMAD-HOWTO` | [NOMAD documentation: How-to overview](https://nomad-lab.eu/docs/howto/overview.html) documents GUI/API data management, upload and publication, plugin entry-point categories, Oasis hosting, and core-development routes. Accessed 2026-07-12. |
| `SRC-NOMAD-CONTRIBUTION` | [NOMAD documentation: How to contribute](https://nomad-lab.eu/prod/v1/docs/howto/develop/contrib.html) documents synchronized GitHub and MPCDF GitLab development projects, public GitHub issues, and contribution guidance. Accessed 2026-07-12. |
| `SRC-NOMAD-JOSS-2023` | [Journal of Open Source Software: NOMAD](https://joss.theoj.org/papers/10.21105/joss.05388) identifies the 15 October 2023 article, DOI `10.21105/joss.05388`, author list including Claudia Draxl, and the distributed materials-data-management platform subject. Accessed 2026-07-12. |

## Boundary and limitations

This record does not claim that all FAIRmat participants maintain NOMAD, that
the listed repository is the only development venue, or that current release
activity proves research quality, availability, or applicant fit. The Python
relation does not make every component, plugin, or contributor Python-based.
Public issues, GitLab access, plugins, Oasis deployment, API, and documentation
routes do not establish contributor status, review rights, acceptance,
mentoring, employment, security posture, or a current governance roster.
