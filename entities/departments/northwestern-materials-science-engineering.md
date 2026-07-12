---
schema_version: 2
entity_type: department
id: DEPARTMENT-NORTHWESTERN-MSE
name: Department of Materials Science and Engineering
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-NU-MSE-OVERVIEW
  - SRC-NU-MSE-MATERIALS-THEORY
university_id: UNIVERSITY-NORTHWESTERN
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://www.mccormick.northwestern.edu/materials-science/
relationship_assertions:
  - predicate: belongs_to
    target_id: UNIVERSITY-NORTHWESTERN
    source_ids: [SRC-NU-MSE-OVERVIEW]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-NU-MSE-MATERIALS-THEORY]
    confidence: high
    evidence_window: 2026-07
---

# Department of Materials Science and Engineering, Northwestern University

The Department of Materials Science and Engineering is the reviewed
administrative Department context for the Wolverton Research Group. It remains
distinct from the group and does not replace Northwestern University as that
group's one direct host.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NU-MSE-OVERVIEW` | [Northwestern Materials Science & Engineering](https://www.mccormick.northwestern.edu/materials-science/) identifies the Department of Materials Science and Engineering at Northwestern University. Accessed 2026-07-12. |
| `SRC-NU-MSE-MATERIALS-THEORY` | [Northwestern MSE: Materials Theory, Computation, & Design](https://www.mccormick.northwestern.edu/materials-science/research/areas-of-research/materials-theory-computation-design.html) describes computational and theoretical materials-science research at the department and lists Chris Wolverton among its faculty. Accessed 2026-07-12. |

## Boundary and limitations

This record supplies administrative and research-area context only. It does
not make the department the Wolverton Group's direct host, enumerate all
faculty, programmes, or laboratories, or make claims about admissions,
mentorship, funding, language, or applicant fit.
