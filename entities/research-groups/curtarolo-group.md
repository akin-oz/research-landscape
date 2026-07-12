---
schema_version: 2
entity_type: research-group
id: RG-CURTAROLO-GROUP
name: Curtarolo Group
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-CURTAROLO-GROUP-JOBS
  - SRC-CURTAROLO-GROUP-AFLOW
  - SRC-CURTAROLO-GROUP-PEOPLE
institution_id: UNIVERSITY-DUKE
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
software_ids:
  - SW-AFLOW
website: https://materials.duke.edu/
relationship_assertions:
  - predicate: belongs_to
    target_id: UNIVERSITY-DUKE
    source_ids: [SRC-CURTAROLO-GROUP-JOBS]
    confidence: high
    evidence_window: 2026-07
  - predicate: develops
    target_id: SW-AFLOW
    source_ids: [SRC-CURTAROLO-GROUP-AFLOW]
    confidence: high
    evidence_window: 2026-07
    notes: The group page says that the AFLOW framework was developed in the group's context; this is not an exclusive-development claim.
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-CURTAROLO-GROUP-JOBS]
    confidence: high
    evidence_window: 2026-07
---

# Curtarolo Group

The Curtarolo Group is the Duke-hosted research-group node for the documented
AFLOW software-development relationship. The group is described in the Duke
materials site as Prof. Curtarolo's group at the Center for Extreme Materials;
the Center is contextual evidence, not a substitute group identity in this
slice.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-CURTAROLO-GROUP-JOBS` | [Curtarolo Materials Lab: Jobs](https://materials.duke.edu/jobs.html) identifies Prof. Curtarolo's group at the Center for Extreme Materials at Duke University and describes computational materials design as its focus. It is used only for group identity, host, and research-scope evidence, not to assert a current opening. Accessed 2026-07-12. |
| `SRC-CURTAROLO-GROUP-AFLOW` | [Curtarolo Materials Lab: AFLOW](https://materials.duke.edu/aflow.html) says AFLOW software is a framework for autonomous DFT and materials-properties calculations developed in the group's context. Accessed 2026-07-12. |
| `SRC-CURTAROLO-GROUP-PEOPLE` | [Curtarolo Group: People](https://materials.duke.edu/people.html) is the group's people page, listing Stefano Curtarolo and identifying him as the research-inquiry contact. Accessed 2026-07-12. |

## Boundary and limitations

The group-to-AFLOW assertion does not establish exclusive development,
ownership, governance, or individual maintenance. This record does not
enumerate personnel, claim that all AFLOW-consortium participants are Duke
members, or convert the public job page into a claim about opportunities.
