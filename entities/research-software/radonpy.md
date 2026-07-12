---
schema_version: 2
entity_type: research-software
id: SW-RADONPY
name: RadonPy
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-RADONPY-REPOSITORY
  - SRC-RIKEN-POLYMEROMICS-TEAM
  - SRC-RIKEN-POLYMEROMICS-PUBLICATIONS
research_area_ids:
  - AREA-MATERIALS-INFORMATICS
open_source: "yes"
github: https://github.com/RadonPy/RadonPy
repository_url: https://github.com/RadonPy/RadonPy
website: https://github.com/RadonPy/RadonPy
license: BSD-3-Clause
programming_language_ids:
  - PROGRAMMING-LANGUAGE-PYTHON
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-PYTHON
    source_ids: [SRC-RADONPY-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The project-owned repository describes RadonPy as a Python library. This records the software implementation language, not a group-wide language policy or an individual skill.
---

# RadonPy

RadonPy is represented as a distinct research-software artifact for automated
polymer physical-property calculations. The Polymeromics Team connection is
documented at group level, without claiming an exhaustive individual maintainer
roster.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-RADONPY-REPOSITORY` | [RadonPy/RadonPy](https://github.com/RadonPy/RadonPy) describes RadonPy as an open-source Python library for fully automated all-atom classical molecular-dynamics calculation of polymer properties and identifies the BSD-3-Clause license. Accessed 2026-07-12. |
| `SRC-RIKEN-POLYMEROMICS-TEAM` | [RIKEN Polymeromics Team](https://www.riken.jp/en/research/labs/trip/agis/polymeromics/index.html) lists RadonPy as a selected team output and links its GitHub site. Accessed 2026-07-12. |
| `SRC-RIKEN-POLYMEROMICS-PUBLICATIONS` | [RIKEN Polymeromics Team (Japanese): Major Publications](https://www.riken.jp/research/labs/trip/agis/polymeromics/index.html) lists the 2022 RadonPy article as “automated physical property calculation using all-atom classical molecular dynamics simulations for polymer informatics.” This supports the controlled Materials Informatics classification at the software level; it does not assert a broader taxonomy or current project role. Accessed 2026-07-12. |

## Boundary and limitations

This record does not claim that RIKEN or the Polymeromics Team exclusively owns
or maintains RadonPy, that every team member is a maintainer, or that repository
activity establishes a particular opening, mentoring environment, or applicant
fit. The Python relation does not make Python a team-wide requirement or claim
that every team member uses it. The Materials Informatics classification is
bounded to the source's polymer-informatics description; it does not classify
every polymer simulation tool or establish a broader research-area hierarchy.
