---
schema_version: 2
entity_type: university
id: UNIVERSITY-DTU
name: Technical University of Denmark
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-DTU-ORGANIZATION
  - SRC-DTU-CONTACT
country_id: COUNTRY-DK
city: Kongens Lyngby
website: https://www.dtu.dk/english
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-DK
    source_ids: [SRC-DTU-CONTACT]
    confidence: high
    evidence_window: 2026-07
---

# Technical University of Denmark

The Technical University of Denmark (DTU) is the direct University host for
Computational Atomic-scale Materials Design (CAMD) in this slice.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-DTU-ORGANIZATION` | [DTU Organization](https://dtu.dk/english/about/organization) identifies DTU as an independent, self-governing university and describes its department-based research structure. Accessed 2026-07-12. |
| `SRC-DTU-CONTACT` | [DTU: Contact](https://www.shop.dtu.dk/en/contact-form/) gives the Technical University of Denmark main address in Kongens Lyngby, Denmark. Accessed 2026-07-12. |

## Boundary and limitations

This record provides the host and geographic endpoint needed by this slice. It
makes no university-wide claim about rankings, admissions, funding, language,
programme eligibility, or research quality.
