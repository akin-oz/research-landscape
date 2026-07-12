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
  - SRC-PYMATGEN-PUBLICATION
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

The project-owned public site and repository describe a user path from
installation and examples to issue reporting, pull requests, forum questions,
or GitHub discussions. Those public channels are useful contribution and
learning surfaces, not evidence that any submission will be accepted or that a
particular person will mentor or review it.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PYMATGEN-WEBSITE` | [pymatgen](https://pymatgen.org/) describes pymatgen as open software used in Materials Project and states that it is released under the MIT License. Accessed 2026-07-12. |
| `SRC-PYMATGEN-REPOSITORY` | [materialsproject/pymatgen](https://github.com/materialsproject/pymatgen) is the public project repository; its README describes the materials-analysis code as powering Materials Project and states the MIT License. Accessed 2026-07-12. |
| `SRC-PERSSON-GROUP-SOFTWARE` | [Persson Group software](https://perssongroup.lbl.gov/software.html) lists Pymatgen among code used by Materials Project and identifies Prof. Shyue Ping Ong as its maintainer. Accessed 2026-07-12. |
| `SRC-PYMATGEN-PUBLICATION` | [LBL ETA Publications: Python Materials Genomics (pymatgen)](https://eta-publications.lbl.gov/publications/python-materials-genomics-pymatgen) identifies the February 2013 article, DOI `10.1016/j.commatsci.2012.10.028`, author list including Shyue Ping Ong and Anubhav Jain, and the library's data-representation and analysis purpose. Accessed 2026-07-12. |

## Boundary and limitations

The sources describe pymatgen as Python software, but no
`programming_language_ids` value is added because vNext has no canonical
Programming Language entity type or namespace. This record does not attribute
current maintenance, development, or use to the Persson Group or Kristin
Persson. The PI-level lead-developer relation does not establish NUS or
Materialyze.AI ownership, governance, or group-wide stewardship, and does not
enumerate all pymatgen maintainers. Public issues, pull requests, forum, and
discussion links do not establish contributor status, review rights, acceptance,
mentoring, employment, or a current project-governance roster.
