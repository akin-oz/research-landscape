---
schema_version: 2
entity_type: organization
id: ORG-SANDIA-NATIONAL-LABORATORIES
name: Sandia National Laboratories
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-SANDIA-ABOUT
country_id: COUNTRY-US
city: Albuquerque
organization_kind: federally funded research and development center
website: https://www.sandia.gov/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-US
    source_ids: [SRC-SANDIA-ABOUT]
    confidence: high
    evidence_window: 2026-07
---

# Sandia National Laboratories

Sandia National Laboratories is the directly documented institutional context
for LAMMPS's original development. It is represented as an Organization rather
than as a University, and it is not treated as the exclusive current owner,
host, funder, or employer of the broader LAMMPS community.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SANDIA-ABOUT` | [Sandia National Laboratories: About](https://www.sandia.gov/about/) identifies Sandia as a federally funded research and development center with headquarters in Albuquerque, New Mexico, United States. Accessed 2026-07-12. |

## Boundary and limitations

This record supplies an institutional and geographic endpoint. It does not
establish a current LAMMPS staffing roster, ownership, governance, funding,
support commitment, opening, mentoring, admissions, or applicant-fit claim.
