---
schema_version: 2
entity_type: university
id: UNIVERSITY-UMN
name: University of Minnesota
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-UMN-TADMOR-PROFILE
country_id: COUNTRY-US
city: Minneapolis
website: https://twin-cities.umn.edu/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-US
    source_ids: [SRC-UMN-TADMOR-PROFILE]
    confidence: high
    evidence_window: 2026-07
---

# University of Minnesota

The University of Minnesota is the direct University affiliation endpoint for
Ellad Tadmor in the OpenKIM slice. It is represented as an institution, not as
a claim about all programmes, groups, opportunities, or OpenKIM ownership.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-UMN-TADMOR-PROFILE` | [University of Minnesota: Ellad Tadmor](https://cse.umn.edu/dsi/ellad-tadmor) identifies Tadmor as Professor in Aerospace Engineering and Mechanics and gives a Minneapolis, Minnesota, United States address. Accessed 2026-07-13. |

## Boundary and limitations

This record supplies an affiliation and geographic endpoint. It makes no
University-wide claim about rankings, admissions, funding, language, programme
eligibility, research quality, OpenKIM ownership, or applicant fit.
