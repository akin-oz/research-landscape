---
schema_version: 2
entity_type: principal-investigator
id: PI-CLAUDIA-DRAXL
name: Claudia Draxl
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-HU-DRAXL-PROFILE
  - SRC-SOLGROUP-HOME
  - SRC-FAIRMAT-TEAM
affiliation_ids:
  - UNIVERSITY-HU-BERLIN
research_group_ids:
  - RG-SOLGROUP
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://sol.physik.hu-berlin.de/
relationship_assertions:
  - predicate: affiliated_with
    target_id: UNIVERSITY-HU-BERLIN
    source_ids: [SRC-HU-DRAXL-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: leads
    target_id: RG-SOLGROUP
    role: group-leader
    source_ids: [SRC-SOLGROUP-HOME]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-SOLGROUP-HOME]
    confidence: high
    evidence_window: 2026-07
---

# Claudia Draxl

Claudia Draxl is represented for her current Humboldt-Universität zu Berlin
affiliation, SOLgroup leadership, and computational-materials research
connection. Her FAIRmat spokesperson role is represented by the source
ecosystem’s evidence-bearing relationship rather than duplicated here.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-HU-DRAXL-PROFILE` | [Humboldt-Universität zu Berlin: Claudia Draxl](https://www.hu-berlin.de/personen/prof-dr-dr-hc-claudia-draxl) identifies her as a professor in the Institute of Physics, Theoretical Physics (Solid State Theory), and lists a FAIRmat project through September 2026. Accessed 2026-07-12. |
| `SRC-SOLGROUP-HOME` | [SOLgroup](https://sol.physik.hu-berlin.de/) identifies Prof. Claudia Draxl as the leader of the Humboldt-Universität zu Berlin solid-state theory group and describes its condensed-matter theory and computational-materials-science work. Accessed 2026-07-12. |
| `SRC-FAIRMAT-TEAM` | [FAIRmat Team](https://www.fairmat-nfdi.eu/fairmat/about-fairmat/team-fairmat) lists Prof. Dr. Claudia Draxl as spokesperson and an area leader. Accessed 2026-07-12. |

## Boundary and limitations

This record does not turn the FAIRmat role into a personal claim of exclusive
NOMAD ownership or maintenance, infer a current vacancy, or convert listed
project dates into funding availability. It makes no claim about supervision,
mentoring, admissions, language, or applicant fit.
