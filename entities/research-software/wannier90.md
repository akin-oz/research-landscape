---
schema_version: 2
entity_type: research-software
id: SW-WANNIER90
name: Wannier90
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-WANNIER90-REPOSITORY
  - SRC-WANNIER90-FEATURES
  - SRC-WANNIER90-LIBRARY
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
  - AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE
open_source: "yes"
website: https://wannier.org/
repository_url: https://github.com/wannier-developers/wannier90
license: LGPL-2.1-or-later
programming_language_ids:
  - PROGRAMMING-LANGUAGE-FORTRAN
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-FORTRAN
    source_ids: [SRC-WANNIER90-LIBRARY]
    confidence: high
    evidence_window: 2026-07
    notes: Official documentation describes Wannier90's library interface as a Fortran library. This is a bounded software implementation relation, not a claim about every wrapper, interface, contributor, or user skill.
---

# Wannier90

Wannier90 is represented as a distinct open-source code for generating
maximally-localized Wannier functions and calculating electronic properties of
materials. Its separate ecosystem record owns the public developer-community,
source, contribution, documentation, tutorial, and support context; this
software record does not model every interfacing code, workflow, property,
library, developer, or user.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-WANNIER90-REPOSITORY` | [wannier-developers/wannier90](https://github.com/wannier-developers/wannier90) is the official repository, identifies LGPL-2.1-or-later licensing, links contribution/issue guidance, and lists the Wannier90 Developer Group. Accessed 2026-07-13. |
| `SRC-WANNIER90-FEATURES` | [Wannier90 features](https://wannier.org/features/) describes Wannier90 as an open-source code for generating maximally-localized Wannier functions and computing electronic properties of materials, with development managed on GitHub. Accessed 2026-07-13. |
| `SRC-WANNIER90-LIBRARY` | [Wannier90 library mode](https://wannier90.readthedocs.io/en/latest/user_guide/wannier90/library_mode/) describes a Fortran library interface, serial/MPI libraries, and a C interface through Fortran 2003 interoperability. Accessed 2026-07-13. |

## Boundary and limitations

This record does not establish that every interfacing electronic-structure
code, post-processing tool, property, library, wrapper, output, benchmark, or
workflow is part of Wannier90. It makes no claim about performance,
correctness, review, support, funding, openings, mentoring, admissions, or
applicant fit.
