---
schema_version: 2
entity_type: research-software
id: SW-AFLOW
name: AFLOW
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-AFLOW-DOCUMENTATION
  - SRC-AFLOW-REPOSITORY
  - SRC-AFLOW-INSTALLATION
  - SRC-AFLOW-API
  - SRC-AFLOW-2023-PUBLICATION
repository_url: https://github.com/aflow-org/aflow
website: https://aflow.org/
license: GPL-3.0
open_source: "yes"
---

# AFLOW framework

`AFLOW` is the distinct research-software framework in this slice. Its
surrounding public data and web interfaces are modeled separately by
[`ECO-AFLOW`](../ecosystems/aflow.md), so the software record does not copy
group, people, or institutional relationships asserted elsewhere in the graph.

The project documentation provides a bounded technical and learning path:
obtain the source, follow installation and generated-code documentation, use
the public data APIs for query/download workflows, and cite the framework's
technical literature. These routes do not establish support, review, or
acceptance guarantees.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-AFLOW-DOCUMENTATION` | [AFLOW documentation](https://aflow.org/aflow-documentation/index.html) describes the Automatic-Flow framework as a collection of software tools for high-throughput materials discovery using DFT and data informatics, and links its source code. Accessed 2026-07-12. |
| `SRC-AFLOW-REPOSITORY` | [aflow-org/aflow](https://github.com/aflow-org/aflow) is the source repository linked by the AFLOW documentation and states that the project is licensed under GNU GPL v3.0. Accessed 2026-07-12. |
| `SRC-AFLOW-INSTALLATION` | [AFLOW: install and documentation](https://aflow.org/install-aflow/) documents source installation, Doxygen-based code documentation, and the project's recommended AFLOW literature including the 2023 `aflow++` paper. Accessed 2026-07-12. |
| `SRC-AFLOW-API` | [AFLOW documentation: AFLUX Search API](https://aflow.org/documentation/) documents property-filtered queries and JSON outputs for searching and downloading AFLOW database results. Accessed 2026-07-12. |
| `SRC-AFLOW-2023-PUBLICATION` | [Duke Scholars: aflow++](https://scholars.duke.edu/individual/pub1557308) identifies the 25 January 2023 article, DOI `10.1016/j.commatsci.2022.111889`, author list including Stefano Curtarolo, and its autonomous-materials-design framework subject. Accessed 2026-07-12. |

## Boundary and limitations

The GPL-3.0 value applies to this software repository, not automatically to
the AFLOW web ecosystem, its databases, interfaces, or every related artifact.
The record makes no current-activity, release-quality, exclusive-maintenance,
or individual-maintainer claim. Installation, documentation, API, and citation
routes do not establish a personal support obligation, contribution acceptance,
review right, mentoring relationship, or current governance roster.
