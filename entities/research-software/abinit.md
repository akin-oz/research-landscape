---
schema_version: 2
entity_type: research-software
id: SW-ABINIT
name: ABINIT
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-ABINIT-PRESENTATION
  - SRC-ABINIT-LICENSE
  - SRC-ABINIT-DEVELOPMENT
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
open_source: "yes"
website: https://www.abinit.org/
repository_url: https://github.com/abinit/abinit
license: GPL-3.0-only
programming_language_ids:
  - PROGRAMMING-LANGUAGE-FORTRAN
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-FORTRAN
    source_ids: [SRC-ABINIT-DEVELOPMENT]
    confidence: high
    evidence_window: 2026-07
    notes: ABINIT's official developer overview identifies Fortran90 among the project's development languages and tools. This is a bounded software implementation relation, not a claim about every auxiliary artifact, group practice, or individual skill.
---

# ABINIT

ABINIT is represented as the distinct public DFT and materials-simulation
software suite. The separate ABINIT ecosystem record owns the public
development, learning, and contribution surfaces; this software record does
not model every utility, pseudopotential, workflow, build dependency, method,
benchmark, contributor, or user.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-ABINIT-PRESENTATION` | [ABINIT: Presentation](https://www.abinit.org/presentation.html) describes an electronic-structure package for molecules and periodic solids using DFT, plane waves, pseudopotentials or PAW data, and related materials properties; it states that ABINIT has been distributed under the GNU General Public License since version 3. Accessed 2026-07-13. |
| `SRC-ABINIT-LICENSE` | [ABINIT: License](https://docs.abinit.org/about/license/) publishes the GNU General Public License, Version 3, for the program. Accessed 2026-07-13. |
| `SRC-ABINIT-DEVELOPMENT` | [ABINIT: development overview](https://docs.abinit.org/developers/overview_development/) describes the worldwide-open development philosophy and names Fortran90, Git, GitLab, testing, and related tools in the developer environment. Accessed 2026-07-13. |

## Boundary and limitations

This record does not establish that every ABINIT component, data table,
auxiliary utility, result, or workflow is covered by the same implementation,
license, maturity, or support conditions. It makes no claim about performance,
correctness, review, support, funding, openings, mentoring, admissions, or
applicant fit.
