---
schema_version: 2
entity_type: university
id: UNIVERSITY-NUS
name: National University of Singapore
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-NUS-CONTACT
country_id: COUNTRY-SG
city: Singapore
website: https://www.nus.edu.sg/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-SG
    source_ids: [SRC-NUS-CONTACT]
    confidence: high
    evidence_window: 2026-07
---

# National University of Singapore

The National University of Singapore is the direct University host for the
Materialyze.AI Lab in this slice. It remains a specialized University identity;
this record does not create a duplicate Organization solely for group hosting.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NUS-CONTACT` | [National University of Singapore: Contact us](https://www.nus.edu.sg/contact) gives the University's address in Singapore. Accessed 2026-07-12. |

## Boundary and limitations

This record provides only the host and geographic endpoint needed by this
slice. It makes no university-level claim about rankings, admissions, funding,
programmes, language, or research activity beyond the documented group link.
