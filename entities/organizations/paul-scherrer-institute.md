---
schema_version: 2
entity_type: organization
id: ORG-PSI
name: Paul Scherrer Institute
status: reviewed
created_at: "2026-07-11"
updated_at: "2026-07-11"
last_review: "2026-07-11"
confidence: high
source_ids:
  - SRC-PSI-ORGANISATION
  - SRC-PSI-ABOUT
country_id: COUNTRY-CH
city: Villigen
organization_kind: research institute
website: https://www.psi.ch/en/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-CH
    source_ids: [SRC-PSI-ORGANISATION]
    confidence: high
    evidence_window: 2026-07
---

# Paul Scherrer Institute

Paul Scherrer Institute (PSI) is represented as an Organization rather than a
University. This is the accountable host for the Materials Software and Data
Group in the reference slice.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PSI-ORGANISATION` | [PSI organisational page](https://www.psi.ch/en/about/organisation) gives PSI's address in Villigen, Switzerland. Accessed 2026-07-11. |
| `SRC-PSI-ABOUT` | [PSI home page](https://www.psi.ch/en/) identifies PSI as a research institute for natural and engineering sciences in Switzerland. Accessed 2026-07-11. |

## Boundary and limitations

This record covers the public host relationship only. It does not claim that
all PSI units work on AiiDA or that every ecosystem participant is employed by
PSI.
