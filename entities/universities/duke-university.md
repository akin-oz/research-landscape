---
schema_version: 2
entity_type: university
id: UNIVERSITY-DUKE
name: Duke University
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-DUKE-CONTACT
  - SRC-DUKE-GRADUATE-LOCATION
country_id: COUNTRY-US
city: Durham
website: https://www.duke.edu/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-US
    source_ids: [SRC-DUKE-CONTACT, SRC-DUKE-GRADUATE-LOCATION]
    confidence: high
    evidence_window: 2026-07
---

# Duke University

Duke University is the direct University host for the Curtarolo Group in this
slice. It remains a specialized University identity; this
record does not create a duplicate Organization solely for group hosting.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-DUKE-CONTACT` | [Duke University: Contact](https://www.duke.edu/contact/) gives Duke University's Durham, North Carolina address. Accessed 2026-07-12. |
| `SRC-DUKE-GRADUATE-LOCATION` | [Duke Graduate School: Admissions FAQs](https://gradschool.duke.edu/admissions/admissions-faqs/) gives the Duke University Graduate School mailing address in Durham, North Carolina, USA. Accessed 2026-07-12. |

## Boundary and limitations

This record provides only the host and geographic endpoint needed by this
slice. It makes no university-level claim about rankings, admissions, funding,
programmes, language, or research activity beyond the documented Curtarolo Group link.
