---
schema_version: 2
entity_type: research-ecosystem
id: ECO-MATERIALS-PROJECT
name: Materials Project
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-MP-LBNL-PROGRAM
  - SRC-PERSSON-GROUP-RESEARCH
  - SRC-PERSSON-GROUP-SOFTWARE
  - SRC-LBNL-PERSSON-NEWS-2026
ecosystem_kind: materials data and software ecosystem
website: https://materialsproject.org/
software_ids:
  - SW-PYMATGEN
organization_ids:
  - ORG-LBNL
research_group_ids:
  - RG-PERSSON-GROUP
relationship_assertions:
  - predicate: includes
    target_id: SW-PYMATGEN
    source_ids: [SRC-PERSSON-GROUP-SOFTWARE]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: PI-KRISTIN-PERSSON
    role: founder-and-director
    source_ids: [SRC-LBNL-PERSSON-NEWS-2026]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: RG-PERSSON-GROUP
    source_ids: [SRC-PERSSON-GROUP-RESEARCH]
    confidence: high
    evidence_window: 2026-07
    notes: The group describes using and expanding Materials Project database and analysis capabilities.
  - predicate: connects
    target_id: ORG-LBNL
    source_ids: [SRC-MP-LBNL-PROGRAM]
    confidence: high
    evidence_window: 2026-07
    notes: Berkeley Lab presents Materials Project as a Materials Sciences Division research program; this does not assert exclusive ownership.
---

# Materials Project

Materials Project is represented as a research ecosystem rather than as a
single software package. The ecosystem connects its documented public platform,
one distinct software artifact, an evidenced group and leader, and its Berkeley
Lab context without treating that limited set as a complete roster.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-MP-LBNL-PROGRAM` | [Berkeley Lab Materials Sciences Division: Materials Project](https://materialssciences.lbl.gov/research/research-programs/materials-project/) describes Materials Project's goal of accelerating materials discovery through advanced scientific computing and design tools. Accessed 2026-07-12. |
| `SRC-PERSSON-GROUP-RESEARCH` | [Persson Group research](https://perssongroup.lbl.gov/research/) describes Materials Project as a multi-institution, multinational effort and says the group uses and expands its database and analysis capabilities. Accessed 2026-07-12. |
| `SRC-PERSSON-GROUP-SOFTWARE` | [Persson Group software](https://perssongroup.lbl.gov/software.html) lists Pymatgen among code used by Materials Project. Accessed 2026-07-12. |
| `SRC-LBNL-PERSSON-NEWS-2026` | [Berkeley Lab, 8 May 2026: Kristin Persson elected to the American Academy of Arts and Sciences](https://newscenter.lbl.gov/2026/05/08/berkeley-labs-kristin-persson-elected-to-the-american-academy-of-arts-and-sciences/) identifies Persson as Materials Project's founder and director. Accessed 2026-07-12. |

## Boundary and limitations

This record does not claim that Lawrence Berkeley National Laboratory is the
ecosystem's exclusive owner or that the linked entities exhaust Materials
Project's collaborators, software, or host institutions. It distinguishes
[pymatgen](../research-software/pymatgen.md) as a software artifact rather than
equating the full platform with one library.
