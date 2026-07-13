---
schema_version: 2
entity_type: research-software
id: SW-FLEUR
name: FLEUR
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-FLEUR-HOME
  - SRC-FLEUR-REPOSITORY
  - SRC-FLEUR-INSTALLATION
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
  - AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE
open_source: "yes"
website: https://www.flapw.de/
repository_url: https://iffgit.fz-juelich.de/fleur/fleur
license: MIT
programming_language_ids:
  - PROGRAMMING-LANGUAGE-FORTRAN
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-FORTRAN
    source_ids: [SRC-FLEUR-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The official FLEUR GitLab project identifies FLEUR as a Fortran DFT code. This is a software implementation relation, not a claim about every auxiliary component, contributor, or user skill.
---

# FLEUR

FLEUR is represented as a distinct open all-electron DFT simulation tool for
materials properties. Its ecosystem record owns public download, documentation,
forum, development, and contribution context; this record does not model every
method, workflow, plugin, library, developer, institution, or user.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-FLEUR-HOME` | [FLEUR](https://www.flapw.de/) describes an open-source simulation tool for materials properties using density-functional theory and related methods, links MIT licensing, source, documentation, tutorial, forum, and development context. Accessed 2026-07-13. |
| `SRC-FLEUR-REPOSITORY` | [fleur/fleur](https://iffgit.fz-juelich.de/fleur/fleur) identifies the official project as an all-electron FLAPW DFT Fortran code. Accessed 2026-07-13. |
| `SRC-FLEUR-INSTALLATION` | [FLEUR installation](https://www.flapw.de/master/documentation/installation/) documents Git source access, Fortran/C compiler requirements, build configuration, tests, and optional parallel/library context. Accessed 2026-07-13. |

## Boundary and limitations

This record does not establish that every FLEUR method, workflow, plugin,
dependency, configuration, output, benchmark, or environment shares identical
scope or support conditions. It makes no claim about performance, correctness,
review, support, funding, openings, mentoring, admissions, or applicant fit.
