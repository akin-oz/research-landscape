---
schema_version: 2
entity_type: project
id: PROJ-NOMAD-LABORATORY-COE
name: The Novel Materials Discovery Laboratory
title: The Novel Materials Discovery Laboratory
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-NOMAD-LABORATORY-CORDIS
  - SRC-NOMAD-COE-STORY
project_status: completed
start_date: "2015-11-01"
end_date: "2018-10-31"
host_organization_id: ORG-MPG
funding_program_ids:
  - FUND-H2020-RESEARCH-INFRASTRUCTURES
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
software_ids:
  - SW-NOMAD
website: https://cordis.europa.eu/project/id/676580
relationship_assertions:
  - predicate: involves
    target_id: ORG-MPG
    role: coordinator
    source_ids: [SRC-NOMAD-LABORATORY-CORDIS]
    confidence: high
    start_date: "2015-11-01"
    end_date: "2018-10-31"
    evidence_window: 2015-11–2018-10
  - predicate: develops
    target_id: SW-NOMAD
    source_ids: [SRC-NOMAD-LABORATORY-CORDIS, SRC-NOMAD-COE-STORY]
    confidence: high
    start_date: "2015-11-01"
    end_date: "2018-10-31"
    evidence_window: 2015-11–2018-10
    notes: Historical project-level development context for NOMAD infrastructure and tools; this does not assert current maintenance or exclusive authorship.
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-NOMAD-LABORATORY-CORDIS]
    confidence: high
    start_date: "2015-11-01"
    end_date: "2018-10-31"
    evidence_window: 2015-11–2018-10
---

# The Novel Materials Discovery Laboratory

The Novel Materials Discovery Laboratory (NoMaD) is represented as a completed
Horizon 2020 Centre of Excellence project. It provides a dated project context
for the historical extension of NOMAD infrastructure and tools, separate from
the current software record and current FAIRmat ecosystem.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NOMAD-LABORATORY-CORDIS` | [European Commission CORDIS: The Novel Materials Discovery Laboratory](https://cordis.europa.eu/project/id/676580) identifies grant agreement 676580 as a completed H2020 Research Infrastructures project, coordinated by Max-Planck-Gesellschaft, with dates 2015-11-01 through 2018-10-31. Its reporting describes NOMAD's computational-materials-science data infrastructure and project-developed tools. Accessed 2026-07-12. |
| `SRC-NOMAD-COE-STORY` | [NOMAD CoE: Our Story](https://www.nomad-coe.eu/nomad-coe/connections-nomad-coe/our-story-nomad-coe) states that NOMAD was substantially extended in the 2015–2018 H2020 NOMAD Laboratory CoE. Accessed 2026-07-12. |

## Boundary and limitations

This is a completed project record, not a current NOMAD governance, funding,
or maintainer record. It does not identify all 13 partners, every work package,
all project outputs, current services, or a continuing relationship with the
current FAIRmat ecosystem.
