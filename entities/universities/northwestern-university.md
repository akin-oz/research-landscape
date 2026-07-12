---
schema_version: 2
entity_type: university
id: UNIVERSITY-NORTHWESTERN
name: Northwestern University
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-NU-LOCATION
country_id: COUNTRY-US
city: Evanston
website: https://www.northwestern.edu/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-US
    source_ids: [SRC-NU-LOCATION]
    confidence: high
    evidence_window: 2026-07
---

# Northwestern University

Northwestern University is the University host for the Wolverton Research Group
in this slice. It remains a distinct University identity; no generic
Organization record is created to satisfy the group-host contract.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NU-LOCATION` | [Northwestern University MSES: Contact Us](https://www.northwestern.edu/mses/about/contact-us.html) gives a Northwestern University mailing address in Evanston, Illinois, USA. Accessed 2026-07-12. |

## Boundary and limitations

This record provides the direct host and geographic endpoint needed by the
slice. It makes no university-level claim about rankings, admissions, funding,
programmes, language, or the research activity of units beyond the documented
group relationship.
