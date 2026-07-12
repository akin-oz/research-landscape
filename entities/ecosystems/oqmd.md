---
schema_version: 2
entity_type: research-ecosystem
id: ECO-OQMD
name: Open Quantum Materials Database
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-OQMD-OVERVIEW
  - SRC-WOLVERTON-GROUP-OVERVIEW
  - SRC-OQMD-API
  - SRC-OQMD-DOWNLOAD
  - SRC-OQMD-STRUCTURES
  - SRC-OQMD-PUBLICATIONS
ecosystem_kind: research data and software ecosystem
website: https://oqmd.org/
research_group_ids:
  - RG-WOLVERTON-GROUP
relationship_assertions:
  - predicate: connects
    target_id: RG-WOLVERTON-GROUP
    role: developer-and-maintainer
    source_ids: [SRC-OQMD-OVERVIEW]
    confidence: high
    evidence_window: 2026-07
    notes: OQMD documentation identifies the Wolverton Research Group at Northwestern University as its developer and maintainer.
---

# Open Quantum Materials Database

The Open Quantum Materials Database (OQMD) is represented as a research-data
and software ecosystem rather than as a single software artifact. The reviewed
connection is limited to its documented Wolverton Research Group development
and maintenance context.

The official service exposes a data-ecosystem path rather than a reviewed
backend-software artifact: its REST and OPTIMADE APIs support search, filtering,
and download without user credentials, while database snapshots are separately
available for download. This captures OQMD's public data-access architecture
without inventing a duplicated software entity, component graph, or public
contributor workflow that the reviewed sources do not establish.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-OQMD-OVERVIEW` | [OQMD documentation: Overview](https://oqmd.org/documentation/overview) states that OQMD is developed and maintained by members of the Wolverton Research Group at Northwestern University. Accessed 2026-07-12. |
| `SRC-WOLVERTON-GROUP-OVERVIEW` | [Wolverton Research Group](https://www.wolverton.northwestern.edu/) says the group develops and maintains OQMD, describing it as a large-scale materials database for big-data-driven research, screening, and discovery. Accessed 2026-07-12. |
| `SRC-OQMD-API` | [OQMD API](https://oqmd.org/api/) documents REST and OPTIMADE query routes for searching, filtering, and downloading data without user credentials, including an optional query package. Accessed 2026-07-12. |
| `SRC-OQMD-DOWNLOAD` | [OQMD download](https://www.oqmd.org/download/) documents full database downloads as MySQL dumps, versioned release context, and the qmpy API codebase route. Accessed 2026-07-12. |
| `SRC-OQMD-STRUCTURES` | [OQMD documentation: Structure sources](https://oqmd.org/documentation/structures) describes the documented ICSD and prototype-iteration sources of calculated structures and identifies the CC-BY 4.0 data license. Accessed 2026-07-12. |
| `SRC-OQMD-PUBLICATIONS` | [OQMD documentation: Publications](https://oqmd.org/documentation/publications) identifies the project-recommended 2013 and 2015 OQMD references and states the CC-BY 4.0 data license. Accessed 2026-07-12. |

## Boundary and limitations

This record does not imply exclusive Northwestern ownership, a complete
contributor roster, or an individual maintenance role for Chris Wolverton. A
separate research-software record for OQMD's backend is intentionally deferred
until its own scope is reviewed. Public API and download access do not establish
a public code-contribution, review, acceptance, support, governance, security,
or maintenance process.
