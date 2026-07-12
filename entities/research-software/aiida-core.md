---
schema_version: 2
entity_type: research-software
id: SW-AIIDA-CORE
name: aiida-core
status: reviewed
created_at: "2026-07-11"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-AIIDA-REGISTRY
  - SRC-AIIDA-REPOSITORY
  - SRC-AIIDA-DOCUMENTATION
  - SRC-AIIDA-CONTRIBUTION
repository_url: https://github.com/aiidateam/aiida-core
website: https://aiida.net/
license: MIT
open_source: "yes"
---

# aiida-core

`aiida-core` is the AiiDA workflow manager for computational science. Its
canonical record is intentionally limited to the software artifact; the
surrounding community and platforms are represented by
[AiiDA Ecosystem](../ecosystems/aiida.md).

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-AIIDA-REGISTRY` | [AiiDA plugin registry: aiida-core](https://aiida.net/plugin-registry/aiida-core/) identifies `aiida-core` as the AiiDA workflow manager for computational science and links to its source repository. Accessed 2026-07-11. |
| `SRC-AIIDA-REPOSITORY` | [aiidateam/aiida-core](https://github.com/aiidateam/aiida-core) is the project-owned source repository, describes workflows, provenance, HPC and plugin interfaces, and states the MIT licence. Accessed 2026-07-12. |
| `SRC-AIIDA-DOCUMENTATION` | [AiiDA documentation: Introduction](https://aiida.readthedocs.io/projects/aiida-core/en/stable/intro/index.html) describes an open-source Python infrastructure for automating, managing, persisting, sharing, and reproducing computational-science workflows and data. Accessed 2026-07-12. |
| `SRC-AIIDA-CONTRIBUTION` | [aiidateam/aiida-core](https://github.com/aiidateam/aiida-core) directs prospective contributors to the Contributor wiki and exposes public issues, pull requests, discussions, and source code. Accessed 2026-07-12. |

## Technical profile

The official documentation describes a Python workflow infrastructure that
records workflow and calculation inputs, outputs, and metadata in provenance
graphs. The software supports local and remote compute resources, a plugin
interface, and a command-line workflow interface. The implementation details
of graph nodes, processes, ORM storage, and execution backends remain in the
upstream documentation rather than being copied into this entity.

The project-owned repository provides the public contribution surface: source,
issues, pull requests, discussions, and a contributor guide. This demonstrates
an accessible software-contribution workflow, not a guarantee of review time,
acceptance, mentorship, employment, or a particular maintainer role.

## Boundary and limitations

The official ecosystem material describes `aiida-core` as a Python framework,
but this record deliberately has no `programming_language_ids` value. The vNext
metadata contract has no `programming-language` entity type or canonical
namespace yet. See the reference implementation for the documented
compatibility gap rather than treating prose as a substitute for a controlled
language entity. It also does not name an exhaustive dependency or maintainer
roster because those identities require separately reviewed canonical records.
