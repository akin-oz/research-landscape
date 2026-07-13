---
schema_version: 2
entity_type: research-software
id: SW-SIESTA
name: SIESTA
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-SIESTA-REPOSITORY
  - SRC-SIESTA-REFERENCE-MANUAL
  - SRC-SIESTA-INSTALLATION
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
  - AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE
open_source: "yes"
website: https://siesta-project.org/siesta
repository_url: https://gitlab.com/siesta-project/siesta
license: GPL-3.0-only
programming_language_ids:
  - PROGRAMMING-LANGUAGE-FORTRAN
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-FORTRAN
    source_ids: [SRC-SIESTA-REFERENCE-MANUAL]
    confidence: high
    evidence_window: 2026-07
    notes: The official SIESTA reference manual explicitly describes the program as written in Fortran 2003. This is a software implementation relation, not a claim about every auxiliary component, contributor, or user skill.
  - predicate: supports
    target_id: PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION
    source_ids: [SRC-SIESTA-REFERENCE-MANUAL]
    confidence: high
    evidence_window: 2026-07
    notes: SIESTA's reference manual describes Kohn-Sham DFT electronic-structure calculations for molecules and solids; this assertion is limited to support for the named computational challenge.
---

# SIESTA

SIESTA is represented as a distinct public first-principles materials-simulation
code. Its separate ecosystem record owns public installation, documentation,
contribution, and GitLab participation surfaces; this software record does not
model every calculation mode, basis, pseudopotential, module, dependency,
benchmark, contributor, or user.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SIESTA-REPOSITORY` | [siesta-project/siesta](https://gitlab.com/siesta-project/siesta) identifies SIESTA as a first-principles materials-simulation code using DFT and displays GNU GPLv3 licensing for the official source repository. Accessed 2026-07-13. |
| `SRC-SIESTA-REFERENCE-MANUAL` | [SIESTA Reference Manual: Introduction](https://docs.siesta-project.org/projects/siesta/en/5.4/reference/siesta.html) describes electronic-structure calculations and ab initio molecular dynamics for molecules and solids using Kohn-Sham density-functional methods, and states that SIESTA is written in Fortran 2003. Accessed 2026-07-13. |
| `SRC-SIESTA-INSTALLATION` | [SIESTA Quick install](https://docs.siesta-project.org/projects/siesta/en/stable/installation/quick-install.html) documents conda and source installation routes plus build requirements including Fortran/C compilers, CMake, BLAS/LAPACK, and optional parallel libraries. Accessed 2026-07-13. |

## Boundary and limitations

This record does not establish that every SIESTA component, configuration,
extension, dependency, output, benchmark, or workflow has identical methods,
implementation, licensing, or support conditions. It makes no claim about
performance, correctness, review, support, funding, openings, mentoring,
admissions, or applicant fit.
