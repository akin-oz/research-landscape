---
schema_version: 2
entity_type: research-group
id: RG-WOLVERTON-GROUP
name: Wolverton Research Group
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-OQMD-OVERVIEW
  - SRC-WOLVERTON-GROUP-MEMBERS
institution_id: UNIVERSITY-NORTHWESTERN
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://www.wolverton.northwestern.edu/
relationship_assertions:
  - predicate: belongs_to
    target_id: UNIVERSITY-NORTHWESTERN
    source_ids: [SRC-OQMD-OVERVIEW]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-WOLVERTON-GROUP-MEMBERS]
    confidence: high
    evidence_window: 2026-07
---

# Wolverton Research Group

The Wolverton Research Group is the university-hosted group in this slice. Its
direct host is Northwestern University under the accepted `institution_id`
branch; its public methods statement supports its link to the existing
Computational Materials Science area.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-OQMD-OVERVIEW` | [OQMD documentation: Overview](https://oqmd.org/documentation/overview) identifies the Wolverton Research Group at Northwestern University as OQMD's developer and maintainer. Accessed 2026-07-12. |
| `SRC-WOLVERTON-GROUP-MEMBERS` | [Wolverton Research Group: Members](https://www.wolverton.northwestern.edu/members) says the group focuses on computational materials science using first-principles simulations and machine learning. Accessed 2026-07-12. |

## Boundary and limitations

No Department record is created merely to make the host more granular, and no
Organization duplicate is created for Northwestern University. The record does
not turn its documented OQMD connection into a claim that every group member
maintains the platform.
