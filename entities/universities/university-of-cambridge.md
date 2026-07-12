---
schema_version: 2
entity_type: university
id: UNIVERSITY-CAMBRIDGE
name: University of Cambridge
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-CAMBRIDGE-CONTACT
country_id: COUNTRY-GB
city: Cambridge
website: https://www.cam.ac.uk/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-GB
    source_ids: [SRC-CAMBRIDGE-CONTACT]
    confidence: high
    evidence_window: 2026-07
---

# University of Cambridge

The University of Cambridge is the public University affiliation endpoint for
the MACE/Gábor Csányi slice. It is represented as an institution, not as a
claim about all departments, research groups, opportunities, or programme fit.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-CAMBRIDGE-CONTACT` | [University of Cambridge: Contact the University](https://www.cam.ac.uk/about-the-university/contact-the-university) gives the University of Cambridge postal address in Cambridge, United Kingdom. Accessed 2026-07-12. |

## Boundary and limitations

This record supplies an affiliation and geographic endpoint. It makes no
University-wide claim about rankings, admissions, funding, language, programme
eligibility, research quality, or MACE ownership.
