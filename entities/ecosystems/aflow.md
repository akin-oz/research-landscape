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
  - SRC-AFLOW-DOCUMENTATION
  - SRC-AFLOW-API
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
  - predicate: connects
    target_id: PI-STEFANO-CURTAROLO
    role: contributor
    source_ids: [SRC-AFLOW-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
    notes: The AFLOW framework documentation lists Curtarolo among contributors. This is not a maintenance, exclusive-development, governance, or employment assertion beyond the documented contributor listing.
---

# AFLOW

AFLOW is represented as the public materials-data and software ecosystem around
`aflow.org`, distinct from the executable AFLOW framework in
[`SW-AFLOW`](../research-software/aflow.md). The source repository describes
the framework and web ecosystem in tandem, but they remain separate canonical
identities.

Its public documentation describes the web ecosystem as a discovery surface for
materials data and applications, including REST and AFLUX query APIs. The
ecosystem's contributor connection to Stefano Curtarolo is intentionally bounded
to the framework documentation's contributor listing; group-level framework
development remains on the Curtarolo Group record.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-AFLOW-REPOSITORY` | [aflow-org/aflow](https://github.com/aflow-org/aflow) describes AFLOW as a high-throughput materials-discovery framework and separately identifies `aflow.org` as a web ecosystem of applications and databases. Accessed 2026-07-12. |
| `SRC-AFLOW-DOCUMENTATION` | [AFLOW documentation: Overview](https://aflow.org/aflow-documentation/index.html) describes the Automatic-Flow framework's high-throughput DFT and data-informatics purpose, identifies its source code, and lists Stefano Curtarolo among contributors. Accessed 2026-07-12. |
| `SRC-AFLOW-API` | [AFLOW documentation: AFLUX Search API](https://aflow.org/documentation/) documents searching and downloading AFLOW database results through property-based queries and JSON responses. Accessed 2026-07-12. |

## Boundary and limitations

This record does not treat the AFLOW framework, website, databases, API, or
distributed consortium as a single software artifact. Group-level development
is recorded only on the distinct research-group record for the framework. The
public contributor list does not establish a complete current maintainer roster,
review authority, governance, individual employment relationship, or an
exclusive contribution claim.
