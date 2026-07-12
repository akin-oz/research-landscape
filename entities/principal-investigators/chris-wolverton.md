---
schema_version: 2
entity_type: principal-investigator
id: PI-CHRIS-WOLVERTON
name: Chris Wolverton
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-NU-WOLVERTON-FACULTY
  - SRC-WOLVERTON-GROUP-MEMBERS
affiliation_ids:
  - UNIVERSITY-NORTHWESTERN
research_group_ids:
  - RG-WOLVERTON-GROUP
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://www.wolverton.northwestern.edu/
relationship_assertions:
  - predicate: affiliated_with
    target_id: UNIVERSITY-NORTHWESTERN
    source_ids: [SRC-NU-WOLVERTON-FACULTY]
    confidence: high
    evidence_window: 2026-07
  - predicate: leads
    target_id: RG-WOLVERTON-GROUP
    role: group-leader
    source_ids: [SRC-WOLVERTON-GROUP-MEMBERS]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-NU-WOLVERTON-FACULTY]
    confidence: high
    evidence_window: 2026-07
---

# Chris Wolverton

Chris Wolverton is represented for the public Northwestern University
affiliation, Wolverton Research Group leadership, and computational-materials
research connection that are needed by this OQMD vertical slice.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NU-WOLVERTON-FACULTY` | [Northwestern Engineering faculty profile: Chris Wolverton](https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/wolverton-chris.html) identifies him as Frank C. Engelhart Professor of Materials Science and Engineering at Northwestern University and describes his group's research as centered on computational materials science and first-principles simulation tools. Accessed 2026-07-12. |
| `SRC-WOLVERTON-GROUP-MEMBERS` | [Wolverton Research Group: Members](https://www.wolverton.northwestern.edu/members) explicitly identifies Prof. Chris Wolverton as the group leader. Accessed 2026-07-12. |

## Boundary and limitations

This record does not attribute individual OQMD development or maintenance to
Chris Wolverton. It makes no claim about current openings, supervision
capacity, mentoring, admissions, working language, or personal fit.
