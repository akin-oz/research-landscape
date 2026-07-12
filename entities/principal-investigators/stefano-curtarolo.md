---
schema_version: 2
entity_type: principal-investigator
id: PI-STEFANO-CURTAROLO
name: Stefano Curtarolo
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-DUKE-CURTAROLO-PROFILE
  - SRC-CURTAROLO-GROUP-JOBS
  - SRC-CURTAROLO-GROUP-PEOPLE
affiliation_ids:
  - UNIVERSITY-DUKE
research_group_ids:
  - RG-CURTAROLO-GROUP
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://mems.duke.edu/people/stefano-curtarolo/
relationship_assertions:
  - predicate: affiliated_with
    target_id: UNIVERSITY-DUKE
    source_ids: [SRC-DUKE-CURTAROLO-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: leads
    target_id: RG-CURTAROLO-GROUP
    role: group-leader
    source_ids: [SRC-CURTAROLO-GROUP-JOBS, SRC-CURTAROLO-GROUP-PEOPLE]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-DUKE-CURTAROLO-PROFILE]
    confidence: high
    evidence_window: 2026-07
---

# Stefano Curtarolo

Stefano Curtarolo is represented for the current public Duke University
affiliation, Curtarolo Group leadership, and computational-materials research
link needed by the AFLOW slice.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-DUKE-CURTAROLO-PROFILE` | [Duke Mechanical Engineering and Materials Science: Stefano Curtarolo](https://mems.duke.edu/people/stefano-curtarolo/) identifies him as a Duke distinguished professor, Director of the Center for Extreme Materials, and lists computational materials science among his research interests. Accessed 2026-07-12. |
| `SRC-CURTAROLO-GROUP-JOBS` | [Curtarolo Materials Lab: Jobs](https://materials.duke.edu/jobs.html) identifies Prof. Curtarolo's group at the Center for Extreme Materials at Duke University. It is used here only for group identity and host evidence, not to assert a current opportunity. Accessed 2026-07-12. |
| `SRC-CURTAROLO-GROUP-PEOPLE` | [Curtarolo Group: People](https://materials.duke.edu/people.html) is the group's people page, listing Stefano Curtarolo and identifying him as the research-inquiry contact. Accessed 2026-07-12. |

## Boundary and limitations

This record does not attribute individual AFLOW development or maintenance to
Stefano Curtarolo. It makes no claim about current openings, supervision
capacity, mentoring, admissions, funding, language, or applicant fit.
