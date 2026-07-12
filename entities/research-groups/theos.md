---
schema_version: 2
entity_type: research-group
id: RG-THEOS
name: Laboratory of Theory and Simulation of Materials (THEOS)
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-EPFL-MARZARI-PROFILE
  - SRC-THEOS-RESEARCH
  - SRC-THEOS-TEACHING
  - SRC-THEOS-STUDENT-PROJECTS
institution_id: UNIVERSITY-EPFL
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
  - AREA-SCIENTIFIC-SOFTWARE-ENGINEERING
software_ids:
  - SW-AIIDA-CORE
website: https://www.epfl.ch/labs/theos/
relationship_assertions:
  - predicate: belongs_to
    target_id: UNIVERSITY-EPFL
    source_ids: [SRC-EPFL-MARZARI-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-THEOS-RESEARCH]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-SCIENTIFIC-SOFTWARE-ENGINEERING
    source_ids: [SRC-THEOS-RESEARCH]
    confidence: high
    evidence_window: 2026-07
    notes: THEOS describes a shared contribution to open-source electronic-structure and materials-informatics infrastructure. This supports a research-infrastructure contribution, not exclusive ownership or an individual engineering role.
  - predicate: develops
    target_id: SW-AIIDA-CORE
    source_ids: [SRC-THEOS-RESEARCH]
    confidence: high
    evidence_window: 2026-07
    notes: THEOS describes a shared contribution to the development and maintenance of AiiDA; this does not assert exclusive development or individual maintainer roles.
---

# Laboratory of Theory and Simulation of Materials (THEOS)

THEOS is the EPFL-hosted research-group node in this slice. Its public
description supports a Computational Materials Science connection and a
bounded, explicitly shared contribution to AiiDA infrastructure.

Its current EPFL pages describe first-principles and high-throughput research
on energy and information/communication materials, methodological development,
and shared contribution to several open-source electronic-structure and
materials-informatics infrastructures. The public teaching page identifies
solid-state and atomistic/quantum-simulation courses, including hands-on
computational labs; project pages direct bachelor and master students to the
lab's current project-discovery route. These sources document a public learning
surface, not a current opening, admission decision, individual supervision
practice, or outcome guarantee.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-EPFL-MARZARI-PROFILE` | [EPFL: Nicola Marzari](https://people.epfl.ch/nicola.marzari/?lang=en) identifies him as Full Professor in the Laboratory of Theory and Simulation of Materials, EPFL STI IMX THEOS. Accessed 2026-07-12. |
| `SRC-THEOS-RESEARCH` | [THEOS: Research overview](https://www.epfl.ch/labs/theos/page-89530-en-html/) describes computational modelling and first-principles simulations for materials science, high-throughput design, energy and information/communication materials, methodological work, and the laboratory's shared contribution to open-source infrastructures including AiiDA and Materials Cloud. It also describes classes, schools, workshops, and online-material outreach. Accessed 2026-07-12. |
| `SRC-THEOS-TEACHING` | [THEOS: Teaching](https://www.epfl.ch/labs/theos/page-94168-en-html/) identifies solid-state and atomistic/quantum-simulation courses, including four hands-on computational labs. It supports a public course offering, not individual teaching, supervision, admission, or availability claims. Accessed 2026-07-12. |
| `SRC-THEOS-STUDENT-PROJECTS` | [THEOS: Bachelor projects](https://www.epfl.ch/labs/theos/page-102234-en-html/) and [Master projects](https://www.epfl.ch/labs/theos/page-102235-en-html/) direct students to the laboratory’s project-discovery route. They do not establish a specific currently available project, eligibility, funding, or supervision capacity. Accessed 2026-07-12. |

## Boundary and limitations

This record does not convert each cited infrastructure contribution into
exclusive ownership, enumerate personnel, or create separate project,
publication, funding-programme, application, or software records. It makes no
live-opening, admissions, language, applicant-fit, mentoring-quality, or
career-outcome claim.
