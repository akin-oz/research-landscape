---
schema_version: 2
entity_type: research-ecosystem
id: ECO-LAMMPS
name: LAMMPS Ecosystem
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-LAMMPS-DOCUMENTATION
  - SRC-LAMMPS-REPOSITORY
  - SRC-LAMMPS-CONTRIBUTIONS
  - SRC-LAMMPS-CONTRIBUTION-REQUIREMENTS
  - SRC-SANDIA-ABOUT
ecosystem_kind: open-source molecular-dynamics software ecosystem
website: https://www.lammps.org/
software_ids:
  - SW-LAMMPS
organization_ids:
  - ORG-SANDIA-NATIONAL-LABORATORIES
relationship_assertions:
  - predicate: includes
    target_id: SW-LAMMPS
    source_ids: [SRC-LAMMPS-DOCUMENTATION, SRC-LAMMPS-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: ORG-SANDIA-NATIONAL-LABORATORIES
    role: original-development-institution
    source_ids: [SRC-LAMMPS-DOCUMENTATION, SRC-LAMMPS-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: Official LAMMPS sources describe original development at Sandia. This does not claim exclusive current ownership, hosting, governance, funding, or employment for the broader project community.
---

# LAMMPS Ecosystem

The LAMMPS ecosystem is represented separately from the LAMMPS software code.
It captures the documented open-source contribution surface and Sandia origin
without reducing a multi-institutional project to one laboratory or promoting
public developer listings into a complete person graph.

## Purpose and contribution surfaces

LAMMPS documentation describes a classical molecular-dynamics code for
materials modelling and a public GitHub development process. The project
documents contribution requirements, integration testing, documentation,
programming standards, GitHub pull requests, automated testing, and core
developer review. These are contribution and learning surfaces, not a promise
of acceptance, review, support, access, or mentoring.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-LAMMPS-DOCUMENTATION` | [LAMMPS documentation](https://docs.lammps.org/stable/) describes materials-modelling scope, parallel and extensible design, original Sandia development, contributions from many groups and institutions, a user forum, and GitHub-coordinated development. Accessed 2026-07-12. |
| `SRC-LAMMPS-REPOSITORY` | [lammps/lammps](https://github.com/lammps/lammps) identifies the public development repository, Sandia/DOE development context, GPLv2 distribution, and the LAMMPS development team contact path. Accessed 2026-07-12. |
| `SRC-LAMMPS-CONTRIBUTIONS` | [LAMMPS: Submitting new features](https://docs.lammps.org/Modify_contribute.html) documents public GitHub development, recommended advance discussion for larger changes, pull-request integration, automated testing, and approving review by a core developer. Accessed 2026-07-12. |
| `SRC-LAMMPS-CONTRIBUTION-REQUIREMENTS` | [LAMMPS: Requirements for contributions](https://docs.lammps.org/latest/Modify_requirements.html) documents contribution requirements including licensing, integration testing, documentation, programming-language standards, build-system requirements, and source-code consistency. Accessed 2026-07-12. |
| `SRC-SANDIA-ABOUT` | [Sandia National Laboratories: About](https://www.sandia.gov/about/) identifies Sandia as a federally funded research and development center headquartered in Albuquerque, New Mexico, United States. Accessed 2026-07-12. |

## Boundary and limitations

This record does not enumerate every developer, maintainer, contributor,
institution, package, potential, plugin, interface, dependency, publication,
funding source, event, or user. It does not infer current maintenance,
code-review authority, contribution frequency, employment, supervision,
mentoring, admissions, funding, language, or applicant fit from public project
material.
