---
schema_version: 2
entity_type: research-software
id: SW-PYMATGEN
name: pymatgen
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-PYMATGEN-WEBSITE
  - SRC-PYMATGEN-REPOSITORY
  - SRC-PERSSON-GROUP-SOFTWARE
repository_url: https://github.com/materialsproject/pymatgen
website: https://pymatgen.org/
license: MIT
open_source: "yes"
---

# pymatgen

`pymatgen` is the distinct research-software artifact in the Materials Project
slice. Its ecosystem relationship is recorded from the Materials Project node;
the PI-level lead-developer relation is recorded on the canonical PI record
without copying ecosystem group or host relationships here.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PYMATGEN-WEBSITE` | [pymatgen](https://pymatgen.org/) describes pymatgen as open software used in Materials Project and states that it is released under the MIT License. Accessed 2026-07-12. |
| `SRC-PYMATGEN-REPOSITORY` | [materialsproject/pymatgen](https://github.com/materialsproject/pymatgen) is the public project repository; its README describes the materials-analysis code as powering Materials Project and states the MIT License. Accessed 2026-07-12. |
| `SRC-PERSSON-GROUP-SOFTWARE` | [Persson Group software](https://perssongroup.lbl.gov/software.html) lists Pymatgen among code used by Materials Project and identifies Prof. Shyue Ping Ong as its maintainer. Accessed 2026-07-12. |

## Boundary and limitations

The sources describe pymatgen as Python software, but no
`programming_language_ids` value is added because vNext has no canonical
Programming Language entity type or namespace. This record does not attribute
current maintenance, development, or use to the Persson Group or Kristin
Persson. The PI-level lead-developer relation does not establish NUS or
Materialyze.AI ownership, governance, or group-wide stewardship, and does not
enumerate all pymatgen maintainers.
