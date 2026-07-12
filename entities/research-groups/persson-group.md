---
schema_version: 2
entity_type: research-group
id: RG-PERSSON-GROUP
name: Persson Group
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-PERSSON-GROUP-RESEARCH
  - SRC-PERSSON-GROUP-SOFTWARE
organization_id: ORG-LBNL
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://perssongroup.lbl.gov/
relationship_assertions:
  - predicate: belongs_to
    target_id: ORG-LBNL
    source_ids: [SRC-PERSSON-GROUP-SOFTWARE]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-PERSSON-GROUP-RESEARCH]
    confidence: high
    evidence_window: 2026-07
---

# Persson Group

The Persson Group is the research-group node in this slice. Its direct host is
Lawrence Berkeley National Laboratory, while the group’s public research
description supports its connection to the existing Computational Materials
Science area.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PERSSON-GROUP-RESEARCH` | [Persson Group research](https://perssongroup.lbl.gov/research/) says the group studies the physics and chemistry of materials using atomistic computational methods, high-performance computing, DFT, molecular dynamics, machine learning, and natural-language processing. Accessed 2026-07-12. |
| `SRC-PERSSON-GROUP-SOFTWARE` | [Persson Group software](https://perssongroup.lbl.gov/software.html) states that the group is based in the Energy Sciences Area of Lawrence Berkeley National Laboratory. Accessed 2026-07-12. |

## Boundary and limitations

The group’s Materials Project connection does not establish that it develops,
maintains, or uses pymatgen. No such relationship is asserted here; the cited
software page identifies a maintainer other than the Persson Group or Kristin
Persson.
