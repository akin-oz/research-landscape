---
schema_version: 2
entity_type: research-group
id: RG-THEOS
name: Laboratory of Theory and Simulation of Materials (THEOS)
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-EPFL-MARZARI-PROFILE
  - SRC-THEOS-RESEARCH
institution_id: UNIVERSITY-EPFL
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
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

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-EPFL-MARZARI-PROFILE` | [EPFL: Nicola Marzari](https://people.epfl.ch/nicola.marzari/?lang=en) identifies him as Full Professor in the Laboratory of Theory and Simulation of Materials, EPFL STI IMX THEOS. Accessed 2026-07-12. |
| `SRC-THEOS-RESEARCH` | [THEOS: Research overview](https://www.epfl.ch/labs/theos/page-89530-en-html/) describes computational modelling and first-principles simulations for materials science, high-throughput design, and the laboratory's contribution to the development and maintenance of open-source infrastructures including AiiDA and Materials Cloud. Accessed 2026-07-12. |

## Boundary and limitations

This record does not convert each cited infrastructure contribution into
exclusive ownership, enumerate personnel, or create separate project,
publication, funding-programme, application, or software records. It makes no
claim about openings, mentoring, admissions, language, or applicant fit.
