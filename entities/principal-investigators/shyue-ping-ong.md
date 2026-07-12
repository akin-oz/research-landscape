---
schema_version: 2
entity_type: principal-investigator
id: PI-SHYUE-PING-ONG
name: Shyue Ping Ong
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-NUS-ONG-PROFILE
  - SRC-MATERIALYZE-TEAM
  - SRC-PYMATGEN-TEAM
affiliation_ids:
  - UNIVERSITY-NUS
research_group_ids:
  - RG-MATERIALYZE-AI
research_area_ids:
  - AREA-MATERIALS-INFORMATICS
website: https://www.materialyze.ai/
relationship_assertions:
  - predicate: affiliated_with
    target_id: UNIVERSITY-NUS
    source_ids: [SRC-NUS-ONG-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: leads
    target_id: RG-MATERIALYZE-AI
    role: principal-investigator
    source_ids: [SRC-NUS-ONG-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: develops
    target_id: SW-PYMATGEN
    role: founder-and-lead-developer
    source_ids: [SRC-NUS-ONG-PROFILE, SRC-PYMATGEN-TEAM]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-MATERIALS-INFORMATICS
    source_ids: [SRC-NUS-ONG-PROFILE]
    confidence: high
    evidence_window: 2026-07
---

# Shyue Ping Ong

Shyue Ping Ong is represented for his current National University of Singapore
affiliation, Materialyze.AI Lab leadership, materials-informatics research
connection, and documented pymatgen stewardship.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NUS-ONG-PROFILE` | [NUS Materials Science and Engineering: Shyue Ping Ong](https://cde.nus.edu.sg/mse/staff/shyue-ping-ong/) identifies him as a Provost's Chair Professor at NUS, leader of Materialyze.AI, founder and lead developer of pymatgen, and a core contributor to Materials Project. Accessed 2026-07-12. |
| `SRC-MATERIALYZE-TEAM` | [Materialyze.AI: Team](https://www.materialyze.ai/team) records his 2026– NUS appointment and 2013–2025 UC San Diego appointments. Accessed 2026-07-12. |
| `SRC-PYMATGEN-TEAM` | [pymatgen: Development Team](https://pymatgen.org/team.html) lists Shyue Ping Ong as a lead developer. The page's UCSD affiliation text is not used for the current affiliation; the NUS sources above supply that evidence. Accessed 2026-07-12. |

## Boundary and limitations

This record does not treat historical UC San Diego material as a current
affiliation, assert that NUS owns pymatgen or Materials Project, or attribute
all lab work to Ong personally. It makes no claim about current openings,
supervision capacity, mentoring, admissions, funding, language, or applicant
fit.
