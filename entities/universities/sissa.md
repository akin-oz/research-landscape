---
schema_version: 2
entity_type: university
id: UNIVERSITY-SISSA
name: Scuola Internazionale Superiore di Studi Avanzati (SISSA)
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-SISSA-ABOUT
country_id: COUNTRY-IT
city: Trieste
website: https://www.sissa.it/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-IT
    source_ids: [SRC-SISSA-ABOUT]
    confidence: high
    evidence_window: 2026-07
---

# Scuola Internazionale Superiore di Studi Avanzati (SISSA)

SISSA is the direct university affiliation endpoint for Stefano Baroni in the
Quantum ESPRESSO vertical slice. It is modeled as an institution, not a claim
about every SISSA programme, group, opportunity, or project.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SISSA-ABOUT` | [SISSA: About us](https://www.sissa.it/about) describes SISSA as a public higher-education institution and scientific centre located in Trieste, Italy. Accessed 2026-07-12. |

## Boundary and limitations

This record supplies a direct affiliation and geographic endpoint. It makes no
institution-wide claim about rankings, admissions, funding, language,
programme eligibility, research quality, Quantum ESPRESSO ownership, or
applicant fit.
