---
schema_version: 2
entity_type: university
id: UNIVERSITY-UC-BERKELEY
name: University of California, Berkeley
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-UC-BERKELEY-HOME
  - SRC-UC-BERKELEY-MAP
country_id: COUNTRY-US
city: Berkeley
website: https://www.berkeley.edu/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-US
    source_ids: [SRC-UC-BERKELEY-HOME, SRC-UC-BERKELEY-MAP]
    confidence: high
    evidence_window: 2026-07
---

# University of California, Berkeley

The University of California, Berkeley is the direct University host for the
CEDER Group in this slice. It is represented only as the canonical institutional
and geographic endpoint needed for that documented group relationship.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-UC-BERKELEY-HOME` | [University of California, Berkeley](https://www.berkeley.edu/) identifies UC Berkeley as a public research university in the U.S. Accessed 2026-07-12. |
| `SRC-UC-BERKELEY-MAP` | [UC Berkeley Campus Map](https://www.berkeley.edu/map/) states that the Berkeley Campus is located in Berkeley, California. Accessed 2026-07-12. |

## Boundary and limitations

This record does not make a university-level claim about rankings, admissions,
funding, programme availability, language, research quality, or access. It
does not treat the CEDER Group as exhaustive evidence of UC Berkeley's research
ecosystem.
