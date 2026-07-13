---
schema_version: 2
entity_type: principal-investigator
id: PI-NICOLA-MARZARI
name: Nicola Marzari
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-EPFL-MARZARI-PROFILE
  - SRC-MATERIALS-CLOUD-TEAM
  - SRC-PSI-LMS-GROUPS
  - SRC-THEOS-RESEARCH
  - SRC-EPFL-MARZARI-2026-TRANSITION
  - SRC-AIIDA-DEVELOPMENT-TEAM
  - SRC-WANNIER90-REPOSITORY
affiliation_ids:
  - UNIVERSITY-EPFL
  - ORG-PSI
research_group_ids:
  - RG-THEOS
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://theos.epfl.ch/
relationship_assertions:
  - predicate: affiliated_with
    target_id: UNIVERSITY-EPFL
    source_ids: [SRC-EPFL-MARZARI-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: affiliated_with
    target_id: ORG-PSI
    source_ids: [SRC-MATERIALS-CLOUD-TEAM, SRC-PSI-LMS-GROUPS]
    confidence: high
    evidence_window: 2026-07
  - predicate: leads
    target_id: RG-THEOS
    role: laboratory-head
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
    role: development-team-member
    source_ids: [SRC-AIIDA-DEVELOPMENT-TEAM]
    confidence: high
    evidence_window: 2026-07
    notes: The official AiiDA Team page lists Marzari in the AiiDA Development team. This does not establish exclusive ownership, a current maintainer assignment, code-review authority, or a guarantee of ongoing contribution.
  - predicate: develops
    target_id: SW-WANNIER90
    role: developer-group-member
    source_ids: [SRC-WANNIER90-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The official Wannier90 repository lists Marzari in the Wannier90 Developer Group. This does not establish exclusive ownership, a current maintainer assignment, code-review authority, or a guarantee of ongoing contribution.
---

# Nicola Marzari

Nicola Marzari is represented for his current EPFL and PSI affiliations,
THEOS leadership, and computational-materials research connection. A public
EPFL announcement identifies a Cambridge appointment beginning in September
2026; that future appointment is deliberately not modeled as current fact.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-EPFL-MARZARI-PROFILE` | [EPFL: Nicola Marzari](https://people.epfl.ch/nicola.marzari/?lang=en) identifies him as Full Professor in the Laboratory of Theory and Simulation of Materials (THEOS) and Director of NCCR MARVEL at EPFL. Accessed 2026-07-12. |
| `SRC-MATERIALS-CLOUD-TEAM` | [Materials Cloud: Team & Contact](https://www.materialscloud.org/team) lists Nicola Marzari as Chair of Theory and Simulation of Materials at EPFL and Laboratory Head of the Laboratory for Materials Simulations at PSI. Accessed 2026-07-12. |
| `SRC-PSI-LMS-GROUPS` | [PSI Laboratory for Materials Simulations: Research Groups](https://www.psi.ch/en/lms/groups) identifies Prof. Nicola Marzari as head of the Laboratory for Materials Simulations. Accessed 2026-07-12. |
| `SRC-THEOS-RESEARCH` | [THEOS: Research overview](https://www.epfl.ch/labs/theos/page-89530-en-html/) describes the laboratory's computational modelling, first-principles simulation, and high-throughput materials design work. Accessed 2026-07-12. |
| `SRC-EPFL-MARZARI-2026-TRANSITION` | [EPFL, 6 November 2025: Nicola Marzari receives David Adler Award](https://actu.epfl.ch/news/nicola-marzari-receives-david-adler-award) identifies a Cambridge professorship that will begin full time in September 2026. It is used only to define the current-state boundary of this July 2026 record. Accessed 2026-07-12. |
| `SRC-AIIDA-DEVELOPMENT-TEAM` | [AiiDA Team](https://aiida.net/team/) lists Nicola Marzari in “The AiiDA Development team” as Chair of Theory and Simulation of Materials at EPFL, Director of NCCR MARVEL, and Head of LMS at PSI. It supports a bounded software-development-team role, not an exhaustive maintainer roster or current contribution-frequency claim. Accessed 2026-07-12. |
| `SRC-WANNIER90-REPOSITORY` | [wannier-developers/wannier90](https://github.com/wannier-developers/wannier90) lists Nicola Marzari in the Wannier90 Developer Group. It supports only the bounded developer-group relation, not exclusive ownership, current maintenance, review authority, or contribution frequency. Accessed 2026-07-13. |

## Boundary and limitations

This record does not model a future Cambridge appointment as current
affiliation, create an NCCR MARVEL funding/programme node from the listed
directorship, or infer individual ownership, maintenance assignment, or
contribution frequency for every THEOS infrastructure contribution. It makes no
claim about openings, supervision, mentoring, admissions, funding, language, or
applicant fit.
