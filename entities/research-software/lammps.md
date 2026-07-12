---
schema_version: 2
entity_type: research-software
id: SW-LAMMPS
name: LAMMPS
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-LAMMPS-DOCUMENTATION
  - SRC-LAMMPS-REPOSITORY
  - SRC-LAMMPS-DEVELOPERS
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
open_source: "yes"
website: https://www.lammps.org/
repository_url: https://github.com/lammps/lammps
license: GPL-2.0-only
programming_language_ids:
  - PROGRAMMING-LANGUAGE-CPP
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-CPP
    source_ids: [SRC-LAMMPS-REPOSITORY, SRC-LAMMPS-DEVELOPERS]
    confidence: high
    evidence_window: 2026-07
    notes: The public repository identifies C++ as the primary language and the official developer documentation describes C++ base classes. This is a software implementation relation, not a group-wide language policy or an individual skill claim.
---

# LAMMPS

LAMMPS is represented as a distinct open-source classical molecular-dynamics
code for materials modelling and parallel computation. Its Sandia and broader
community context lives in the separate ecosystem and Organization records; the
software record does not claim an exhaustive developer, package, potential,
funding, or user graph.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-LAMMPS-DOCUMENTATION` | [LAMMPS documentation](https://docs.lammps.org/stable/) describes LAMMPS as a classical molecular-dynamics simulation code focused on materials modelling, designed for parallel computers and extensibility, and distributed under GPLv2. Accessed 2026-07-12. |
| `SRC-LAMMPS-REPOSITORY` | [lammps/lammps](https://github.com/lammps/lammps) is the public development repository. Its README identifies LAMMPS as a classical molecular-dynamics code developed at Sandia, maintained by the LAMMPS development team, and distributed under GPL version 2; GitHub identifies C++ as the repository's primary language. Accessed 2026-07-12. |
| `SRC-LAMMPS-DEVELOPERS` | [LAMMPS Developer documentation](https://docs.lammps.org/Developer.html) documents C++ base classes and developer/maintainer guidance. Accessed 2026-07-12. |

## Boundary and limitations

This record does not model every potential, package, plugin, interface,
dependency, benchmark, release, contributor, institution, or application. It
makes no claim about performance, current support, review rights, acceptance,
funding, openings, mentoring, admissions, or applicant fit.
