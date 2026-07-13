---
schema_version: 2
entity_type: research-group
id: RG-CURTAROLO-GROUP
name: Curtarolo Group
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-CURTAROLO-GROUP-JOBS
  - SRC-CURTAROLO-GROUP-AFLOW
  - SRC-CURTAROLO-GROUP-PEOPLE
  - SRC-CURTAROLO-GROUP-HOME
  - SRC-CURTAROLO-GROUP-RESEARCH
  - SRC-CURTAROLO-GROUP-PUBLICATIONS
institution_id: UNIVERSITY-DUKE
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
  - AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE
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
  - predicate: works_on
    target_id: AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE
    source_ids: [SRC-CURTAROLO-GROUP-AFLOW, SRC-CURTAROLO-GROUP-RESEARCH]
    confidence: high
    evidence_window: 2026-07
    notes: The group describes AFLOW's autonomous DFT calculations and its own DFT research. This is a group-scope relation, not an individual software-maintenance or complete methodology claim.
---

# Curtarolo Group

The Curtarolo Group is the Duke-hosted research-group node for the documented
AFLOW software-development relationship. The group is described in the Duke
materials site as Prof. Curtarolo's group at the Center for Extreme Materials;
the Center is contextual evidence, not a substitute group identity in this
slice.

Its public group material identifies research on high-entropy ceramics, phase
stability, symmetry and structure prototyping, autonomous property prediction,
and metallic glasses. It presents AFLOW as an open-source framework developed
in the group, with public source, binary, web-application, API, and workshop
surfaces. The people page displays research-professor, postdoctoral, graduate,
visiting-graduate, adjunct, and scientific-editor roles plus selected alumni
examples; it is not a complete employment or outcomes record. Its
chronological publication page is a public research-output surface, not a
productivity or quality measure.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-CURTAROLO-GROUP-JOBS` | [Curtarolo Materials Lab: Jobs](https://materials.duke.edu/jobs.html) identifies Prof. Curtarolo's group at the Center for Extreme Materials at Duke University and describes computational materials design as its focus. It is used only for group identity, host, and research-scope evidence, not to assert a current opening. Accessed 2026-07-12. |
| `SRC-CURTAROLO-GROUP-AFLOW` | [Curtarolo Materials Lab: AFLOW](https://materials.duke.edu/aflow.html) says AFLOW is an open-source framework for autonomous DFT and materials-properties calculations developed in the group, with public source, binaries, web interfaces, and workshop material. It does not establish individual maintenance, group-wide coding practice, or governance. Accessed 2026-07-12. |
| `SRC-CURTAROLO-GROUP-PEOPLE` | [Curtarolo Group: People](https://materials.duke.edu/people.html) identifies Stefano Curtarolo and public research-professor, postdoctoral, graduate, visiting-graduate, adjunct, and scientific-editor roles, plus selected alumni examples. It is not a complete roster, employment record, or placement statistic. Accessed 2026-07-12. |
| `SRC-CURTAROLO-GROUP-HOME` | [Curtarolo Materials Group](https://materials.duke.edu/) describes AFLOW’s high-throughput DFT and materials-property scope, public database/API surfaces, and virtual seminar series. It does not establish current funding, attendance, instruction, or mentoring outcomes. Accessed 2026-07-12. |
| `SRC-CURTAROLO-GROUP-RESEARCH` | [Curtarolo Group: Research](https://materials.duke.edu/research.html) describes high-entropy ceramics, phase stability, symmetry/prototyping, autonomous property prediction, metallic glasses, DFT, first-principles thermodynamics, and ML methods. It is used for stated group research scope, not hardware or universal member-skill claims. Accessed 2026-07-12. |
| `SRC-CURTAROLO-GROUP-PUBLICATIONS` | [Curtarolo Group: Publications](https://materials.duke.edu/publications.html) is the group’s chronological publication surface, including dated 2026 entries. It supports the existence and topical pattern of a public publication record, not counts, quality, productivity, or attribution metrics. Accessed 2026-07-12. |

## Boundary and limitations

The group-to-AFLOW assertion does not establish exclusive development,
ownership, governance, or individual maintenance. This record does not
enumerate personnel, claim that all AFLOW-consortium participants are Duke
members, or convert the public job page into a claim about opportunities.
