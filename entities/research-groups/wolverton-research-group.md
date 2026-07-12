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
  - SRC-NU-WOLVERTON-FACULTY
institution_id: UNIVERSITY-NORTHWESTERN
department_id: DEPARTMENT-NORTHWESTERN-MSE
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://www.wolverton.northwestern.edu/
relationship_assertions:
  - predicate: belongs_to
    target_id: UNIVERSITY-NORTHWESTERN
    source_ids: [SRC-OQMD-OVERVIEW]
    confidence: high
    evidence_window: 2026-07
  - predicate: belongs_to
    target_id: DEPARTMENT-NORTHWESTERN-MSE
    source_ids: [SRC-NU-WOLVERTON-FACULTY]
    confidence: high
    evidence_window: 2026-07
    notes: Administrative context through the documented group leader's Materials Science and Engineering department appointment; Northwestern University remains the group's sole direct host.
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-WOLVERTON-GROUP-MEMBERS]
    confidence: high
    evidence_window: 2026-07
---

# Wolverton Research Group

The Wolverton Research Group is the university-hosted group in this slice. Its
direct host is Northwestern University under the accepted `institution_id`
branch; the Department of Materials Science and Engineering supplies separate,
evidence-bounded administrative context. Its public methods statement supports
its link to the existing Computational Materials Science area.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-OQMD-OVERVIEW` | [OQMD documentation: Overview](https://oqmd.org/documentation/overview) identifies the Wolverton Research Group at Northwestern University as OQMD's developer and maintainer. Accessed 2026-07-12. |
| `SRC-WOLVERTON-GROUP-MEMBERS` | [Wolverton Research Group: Members](https://www.wolverton.northwestern.edu/members) says the group focuses on computational materials science using first-principles simulations and machine learning. Accessed 2026-07-12. |
| `SRC-NU-WOLVERTON-FACULTY` | [Northwestern Engineering: Chris Wolverton](https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/wolverton-chris.html) identifies him as a Materials Science and Engineering faculty member, names the Wolverton Research Group website, and describes the group's research. This supports bounded administrative context, not a second direct host. Accessed 2026-07-12. |

## Boundary and limitations

The Department record is used only as documented administrative context; it
does not replace or duplicate the University direct host. No Organization
duplicate is created for Northwestern University, and the documented OQMD
connection does not establish that every group member maintains the platform.
