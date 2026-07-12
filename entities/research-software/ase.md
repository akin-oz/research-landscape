---
schema_version: 2
entity_type: research-software
id: SW-ASE
name: Atomic Simulation Environment (ASE)
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-ASE-DOCUMENTATION
  - SRC-ASE-ABOUT
  - SRC-ASE-REPOSITORY
  - SRC-ASE-CALCULATORS
  - SRC-ASE-COMMAND-LINE
  - SRC-ASE-DEVELOPMENT
  - SRC-ASE-CONTACT
  - SRC-ASE-PUBLICATION
open_source: "yes"
website: https://wiki.fysik.dtu.dk/ase/
repository_url: https://gitlab.com/ase/ase
license: LGPL-2.1-or-later
---

# Atomic Simulation Environment (ASE)

ASE is represented as a distinct research-software artifact for atomistic
simulation workflows. Its ecosystem and CAMD group connection are recorded in
separate, evidence-bounded records.

The upstream documentation presents ASE as a modular workflow layer: users
construct `Atoms` objects, attach a calculator for energies and forces, then
run atomistic methods through Python, a command-line interface, or a graphical
interface. The documented GitLab, merge-request, mailing-list, chat, and forum
paths are contribution and learning surfaces; they do not promise review,
acceptance, support, or a personal mentoring relationship.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-ASE-DOCUMENTATION` | [Atomic Simulation Environment documentation](https://wiki.fysik.dtu.dk/ase/index.html) describes ASE as tools and Python modules for setting up, manipulating, running, visualizing, and analyzing atomistic simulations, available under the GNU LGPL. Accessed 2026-07-12. |
| `SRC-ASE-ABOUT` | [ASE: About](https://wiki.fysik.dtu.dk/ase/about.html) describes ASE as a Python environment for atomistic simulations and states the GNU LGPL version 2.1 or later licensing. Accessed 2026-07-12. |
| `SRC-ASE-REPOSITORY` | [ase/ase](https://gitlab.com/ase/ase) is the public GitLab source repository; its README identifies ASE as Python tools and modules for atomistic simulations and documents installation. Accessed 2026-07-12. |
| `SRC-ASE-CALCULATORS` | [ASE documentation: Calculators](https://wiki.fysik.dtu.dk/ase/ase/calculators/calculators.html) describes attaching calculators to `Atoms` objects to calculate energies, forces, and stresses, including external-code configuration. Accessed 2026-07-12. |
| `SRC-ASE-COMMAND-LINE` | [ASE documentation: Command line tool](https://wiki.fysik.dtu.dk/ase/cmdline.html) documents the `ase` CLI for building structures, running calculations, querying databases, conversion, testing, and GUI access. Accessed 2026-07-12. |
| `SRC-ASE-DEVELOPMENT` | [ASE documentation: Development](https://wiki.fysik.dtu.dk/ase/development/development.html) describes contribution, GitLab, code review, coding conventions, documentation, testing, and release-development guidance. Accessed 2026-07-12. |
| `SRC-ASE-CONTACT` | [ASE documentation: Contact](https://wiki.fysik.dtu.dk/ase/contact.html) documents the mailing list, Matrix chat, community forum, and public GitLab issues/merge requests. Accessed 2026-07-12. |
| `SRC-ASE-PUBLICATION` | [Warwick Research Archive: The Atomic Simulation Environment](https://wrap.warwick.ac.uk/id/eprint/87141/) identifies the 21 March 2017 article, DOI `10.1088/1361-648X/aa680e`, and ASE's Python-library subject. Accessed 2026-07-12. |

## Boundary and limitations

This record does not identify an exhaustive maintainer roster, infer current
employment or supervision from a contribution, or treat public source code as a
claim about openings, mentoring, admissions, or applicant fit. Public
repositories, merge requests, support channels, and calculator interfaces do
not establish a contributor role, review right, acceptance, security posture,
or governance roster.
