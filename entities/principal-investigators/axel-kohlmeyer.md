---
schema_version: 2
entity_type: principal-investigator
id: PI-AXEL-KOHLMEYER
name: Axel Kohlmeyer
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-TEMPLE-KOHLMEYER
  - SRC-LAMMPS-AUTHORS
affiliation_ids:
  - UNIVERSITY-TEMPLE
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://cst.temple.edu/directory/axel-kohlmeyer
relationship_assertions:
  - predicate: affiliated_with
    target_id: UNIVERSITY-TEMPLE
    source_ids: [SRC-TEMPLE-KOHLMEYER]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-TEMPLE-KOHLMEYER, SRC-LAMMPS-AUTHORS]
    confidence: high
    evidence_window: 2026-07
    notes: Temple documents scientific-software and molecular-dynamics simulation research; the LAMMPS authors page documents materials-science expertise. This is a bounded Computational Materials Science connection, not a complete research profile.
  - predicate: develops
    target_id: SW-LAMMPS
    role: core-developer-and-co-maintainer
    source_ids: [SRC-TEMPLE-KOHLMEYER, SRC-LAMMPS-AUTHORS]
    confidence: high
    evidence_window: 2026-07
    notes: Temple describes Kohlmeyer as a LAMMPS core developer and co-maintainer, and LAMMPS lists him among current core developers. This does not establish sole ownership, every release role, review assignment, contribution frequency, employment by the project, or support availability.
---

# Axel Kohlmeyer

Axel Kohlmeyer is represented for his current Temple University research
faculty affiliation, documented Computational Materials Science connection, and
current LAMMPS core-developer/co-maintainer role. The record does not infer a
student group, supervision capacity, or complete contribution roster.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-TEMPLE-KOHLMEYER` | [Temple University: Axel Kohlmeyer](https://cst.temple.edu/directory/axel-kohlmeyer) identifies him as Full Professor of Research, Associate Director of the Institute for Computational Molecular Science, and leader of Temple's HPC Team. It describes scientific-software engineering and molecular-dynamics simulation research, and calls him a core developer and co-maintainer of LAMMPS. Accessed 2026-07-13. |
| `SRC-LAMMPS-AUTHORS` | [LAMMPS: Authors](https://docs.lammps.org/latest/Intro_authors.html) lists Axel Kohlmeyer at Temple University among current core LAMMPS developers, with expertise including library interfaces, GitHub, code maintenance, testing, and releases. Accessed 2026-07-13. |

## Boundary and limitations

This record does not turn the research-faculty or HPC-team-leadership titles
into a claim about student supervision, current openings, admissions, funding,
working language, mentorship, or applicant fit. Core-developer/co-maintainer
evidence does not establish exclusive ownership, every review or release role,
contribution frequency, support commitment, or employment by the LAMMPS project.
