---
schema_version: 2
entity_type: research-software
id: SW-AIIDA-CORE
name: aiida-core
status: reviewed
created_at: "2026-07-11"
updated_at: "2026-07-11"
last_review: "2026-07-11"
confidence: high
source_ids:
  - SRC-AIIDA-REGISTRY
  - SRC-AIIDA-REPOSITORY
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
| `SRC-AIIDA-REPOSITORY` | [aiidateam/aiida-core](https://github.com/aiidateam/aiida-core) is the project-owned source repository and states the MIT licence. Accessed 2026-07-11. |

## Boundary and limitations

The official ecosystem material describes `aiida-core` as a Python framework,
but this record deliberately has no `programming_language_ids` value. The vNext
metadata contract has no `programming-language` entity type or canonical
namespace yet. See the reference implementation for the documented
compatibility gap rather than treating prose as a substitute for a controlled
language entity.
