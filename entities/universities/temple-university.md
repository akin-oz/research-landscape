---
schema_version: 2
entity_type: university
id: UNIVERSITY-TEMPLE
name: Temple University
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-TEMPLE-CONTACT
country_id: COUNTRY-US
city: Philadelphia
website: https://www.temple.edu/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-US
    source_ids: [SRC-TEMPLE-CONTACT]
    confidence: high
    evidence_window: 2026-07
---

# Temple University

Temple University is the direct University affiliation endpoint for Axel
Kohlmeyer in the LAMMPS core-developer slice. It is represented as an
institution, not as a claim about all Temple programmes, groups, opportunities,
or LAMMPS ownership.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-TEMPLE-CONTACT` | [Temple University: Contact](https://www.temple.edu/contact) gives Temple University's address in Philadelphia, Pennsylvania, United States. Accessed 2026-07-13. |

## Boundary and limitations

This record supplies a direct affiliation and geographic endpoint. It makes no
University-wide claim about rankings, admissions, funding, language, programme
eligibility, research quality, LAMMPS ownership, or applicant fit.
