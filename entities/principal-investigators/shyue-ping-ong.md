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
  - SRC-M3GNET-PUBLICATION
affiliation_ids:
  - UNIVERSITY-NUS
research_group_ids:
  - RG-MATERIALYZE-AI
research_area_ids:
  - AREA-MATERIALS-INFORMATICS
  - AREA-MACHINE-LEARNED-POTENTIALS
publication_ids:
  - PUB-M3GNET-2022
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
  - predicate: works_on
    target_id: AREA-MACHINE-LEARNED-POTENTIALS
    source_ids: [SRC-M3GNET-PUBLICATION]
    confidence: high
    evidence_window: 2026-07
    notes: The public M3GNet publication identifies Ong as an author and describes a universal graph deep-learning interatomic potential. It supports a topical relation, not a MatGL maintenance, governance, or individual software-role claim.
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
| `SRC-M3GNET-PUBLICATION` | [Nature Computational Science: A universal graph deep learning interatomic potential for the periodic table](https://www.nature.com/articles/s43588-022-00349-3) identifies Shyue Ping Ong as an author and describes M3GNet as a universal graph-neural-network interatomic potential for materials. The canonical publication record is `PUB-M3GNET-2022`. This source supports a research-topic relation, not a current MatGL maintainer, governance, or individual contribution claim. Accessed 2026-07-12. |

## Boundary and limitations

This record does not treat historical UC San Diego material as a current
affiliation, assert that NUS owns pymatgen or Materials Project, or attribute
all lab work to Ong personally. It makes no claim about current openings,
supervision capacity, mentoring, admissions, funding, language, or applicant
fit.
