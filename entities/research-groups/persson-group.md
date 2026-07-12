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
  - SRC-PERSSON-GROUP-PEOPLE
  - SRC-PERSSON-GROUP-PUBLICATIONS
  - SRC-PERSSON-GROUP-POSITIONS
  - SRC-PERSSON-GROUP-NEWS
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

Its first-party pages also provide a bounded Research Group Intelligence view:
they identify public postdoctoral, graduate-student, staff, undergraduate,
visitor, and alumni categories; describe high-throughput computational
materials projects and open-source software practice; publish a chronological
publication list; and include one specific, dated undergraduate-intern role.
These sources are useful evidence about the group’s visible research
environment, but they do not establish a complete roster, funding ledger,
group-wide mentorship quality, hiring status, or career guarantee.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PERSSON-GROUP-RESEARCH` | [Persson Group research](https://perssongroup.lbl.gov/research/) says the group studies the physics and chemistry of materials using atomistic computational methods, high-performance computing, DFT, molecular dynamics, machine learning, and natural-language processing. Accessed 2026-07-12. |
| `SRC-PERSSON-GROUP-SOFTWARE` | [Persson Group software](https://perssongroup.lbl.gov/software.html) states that the group is based in the Energy Sciences Area of Lawrence Berkeley National Laboratory. Accessed 2026-07-12. |
| `SRC-PERSSON-GROUP-PEOPLE` | [Persson Group people](https://perssongroup.lbl.gov/people.html) publicly organizes people into principal-investigator, postdoctoral-fellow, graduate-student, staff, undergraduate-student, visitor, and alumni sections, with individual research descriptions and selected alumni destinations. Accessed 2026-07-12. |
| `SRC-PERSSON-GROUP-PUBLICATIONS` | [Persson Group publications](https://perssongroup.lbl.gov/publications.html) provides a chronological publication list, including 2026 research articles in materials, computation, and data-driven research. Accessed 2026-07-12. |
| `SRC-PERSSON-GROUP-POSITIONS` | [Persson Group open positions and projects](https://perssongroup.lbl.gov/open_positions.html) contains a dated 2024 Materials Project undergraduate-intern description, identifies concrete Python/web/data tasks and one-to-one senior-developer guidance for that role, and displays no postdoctoral or staff openings. It is not used to claim a current opening. Accessed 2026-07-12. |
| `SRC-PERSSON-GROUP-NEWS` | [Persson Group news](https://perssongroup.lbl.gov/blog/) records dated group-member awards and professional recognition, including a 2023 student award report. Accessed 2026-07-12. |

## Boundary and limitations

The group’s Materials Project connection does not establish that it develops,
maintains, or uses pymatgen. No such relationship is asserted here; the cited
software page identifies a maintainer other than the Persson Group or Kristin
Persson. The group site’s public people, opportunity, alumni, publication, and
award material is not a complete roster, funding account, industry-collaboration
inventory, placement statistic, or group-wide mentorship assessment. The dated
intern listing gives role-specific guidance evidence only; it is not a statement
about present availability, admissions, supervision capacity, or outcomes for
other roles.
