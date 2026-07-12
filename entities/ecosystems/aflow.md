---
schema_version: 2
entity_type: research-ecosystem
id: ECO-AFLOW
name: AFLOW
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-AFLOW-REPOSITORY
ecosystem_kind: materials data and software ecosystem
website: https://aflow.org/
software_ids:
  - SW-AFLOW
relationship_assertions:
  - predicate: includes
    target_id: SW-AFLOW
    source_ids: [SRC-AFLOW-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The repository describes the AFLOW framework and aflow.org web ecosystem in tandem; this relation models their documented public identity without treating them as one artifact.
---

# AFLOW

AFLOW is represented as the public materials-data and software ecosystem around
`aflow.org`, distinct from the executable AFLOW framework in
[`SW-AFLOW`](../research-software/aflow.md). The source repository describes
the framework and web ecosystem in tandem, but they remain separate canonical
identities.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-AFLOW-REPOSITORY` | [aflow-org/aflow](https://github.com/aflow-org/aflow) describes AFLOW as a high-throughput materials-discovery framework and separately identifies `aflow.org` as a web ecosystem of applications and databases. Accessed 2026-07-12. |

## Boundary and limitations

This record does not treat the AFLOW framework, website, databases, API, or
distributed consortium as a single software artifact. Group-level development
is recorded only on the distinct research-group record for the framework.
