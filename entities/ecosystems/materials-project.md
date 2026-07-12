---
schema_version: 2
entity_type: research-ecosystem
id: ECO-MATERIALS-PROJECT
name: Materials Project
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-MP-LBNL-PROGRAM
  - SRC-MP-DOCUMENTATION
  - SRC-MP-DATA-WORKFLOWS
  - SRC-MP-DATA-BUILDERS
  - SRC-MP-API-GETTING-STARTED
  - SRC-PERSSON-GROUP-RESEARCH
  - SRC-PERSSON-GROUP-SOFTWARE
  - SRC-LBNL-PERSSON-NEWS-2026
  - SRC-NUS-ONG-PROFILE
  - SRC-LBNL-JAIN-PROFILE
  - SRC-UC-BERKELEY-CEDER-PROFILE
ecosystem_kind: materials data and software ecosystem
website: https://materialsproject.org/
software_ids:
  - SW-PYMATGEN
organization_ids:
  - ORG-LBNL
research_group_ids:
  - RG-PERSSON-GROUP
relationship_assertions:
  - predicate: includes
    target_id: SW-PYMATGEN
    source_ids: [SRC-PERSSON-GROUP-SOFTWARE]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: PI-KRISTIN-PERSSON
    role: founder-and-director
    source_ids: [SRC-LBNL-PERSSON-NEWS-2026]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: PI-SHYUE-PING-ONG
    role: core-contributor
    source_ids: [SRC-NUS-ONG-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: PI-ANUBHAV-JAIN
    role: associate-director
    source_ids: [SRC-LBNL-JAIN-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: RG-PERSSON-GROUP
    source_ids: [SRC-PERSSON-GROUP-RESEARCH]
    confidence: high
    evidence_window: 2026-07
    notes: The group describes using and expanding Materials Project database and analysis capabilities.
  - predicate: connects
    target_id: RG-CEDER-GROUP
    role: contributor
    source_ids: [SRC-UC-BERKELEY-CEDER-PROFILE]
    confidence: high
    evidence_window: 2026-07
    notes: UC Berkeley describes the CEDER Group as contributing extensively to Materials Project; this does not establish exclusive ownership, a complete contributor roster, or individual software maintenance.
  - predicate: connects
    target_id: ORG-LBNL
    source_ids: [SRC-MP-LBNL-PROGRAM]
    confidence: high
    evidence_window: 2026-07
    notes: Berkeley Lab presents Materials Project as a Materials Sciences Division research program; this does not assert exclusive ownership.
---

# Materials Project

Materials Project is represented as a research ecosystem rather than as a
single software package. The ecosystem connects its documented public platform,
one distinct software artifact, an evidenced group and leader, and its Berkeley
Lab context without treating that limited set as a complete roster.

Its public documentation describes a data-production path in which automated
high-throughput workflows generate task data, builders transform it into
purpose-specific data collections, and the API exposes documented query routes.
This gives the ecosystem a bounded architecture description without turning its
internal packages, databases, workflow definitions, or API endpoints into
unsupported canonical entities.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-MP-LBNL-PROGRAM` | [Berkeley Lab Materials Sciences Division: Materials Project](https://materialssciences.lbl.gov/research/research-programs/materials-project/) describes Materials Project's goal of accelerating materials discovery through advanced scientific computing and design tools. Accessed 2026-07-12. |
| `SRC-MP-DOCUMENTATION` | [Materials Project documentation: Introduction](https://docs.materialsproject.org/) describes the Department of Energy-origin effort to pre-compute material properties and make the data publicly available to accelerate discovery. It also directs documentation improvements through a public forum and GitHub review path. Accessed 2026-07-12. |
| `SRC-MP-DATA-WORKFLOWS` | [Materials Project documentation: Data Workflows](https://docs.materialsproject.org/data-production/data-workflows) describes automated high-throughput `atomate` workflows, standardized pymatgen input sets, task-data parsing, MongoDB storage, and downstream builders. Accessed 2026-07-12. |
| `SRC-MP-DATA-BUILDERS` | [Materials Project documentation: Data Builders](https://docs.materialsproject.org/data-production/data-builders) describes builders that transform input collections into new collections and the documented `emmet` model/API relationship. Accessed 2026-07-12. |
| `SRC-MP-API-GETTING-STARTED` | [Materials Project documentation: API getting started](https://docs.materialsproject.org/downloading-data/using-the-api/getting-started) documents the `mp-api` Python client, account API-key requirement, `MPRester`, and available data endpoints. Accessed 2026-07-12. |
| `SRC-PERSSON-GROUP-RESEARCH` | [Persson Group research](https://perssongroup.lbl.gov/research/) describes Materials Project as a multi-institution, multinational effort and says the group uses and expands its database and analysis capabilities. Accessed 2026-07-12. |
| `SRC-PERSSON-GROUP-SOFTWARE` | [Persson Group software](https://perssongroup.lbl.gov/software.html) lists Pymatgen among code used by Materials Project. Accessed 2026-07-12. |
| `SRC-LBNL-PERSSON-NEWS-2026` | [Berkeley Lab, 8 May 2026: Kristin Persson elected to the American Academy of Arts and Sciences](https://newscenter.lbl.gov/2026/05/08/berkeley-labs-kristin-persson-elected-to-the-american-academy-of-arts-and-sciences/) identifies Persson as Materials Project's founder and director. Accessed 2026-07-12. |
| `SRC-NUS-ONG-PROFILE` | [NUS Materials Science and Engineering: Shyue Ping Ong](https://cde.nus.edu.sg/mse/staff/shyue-ping-ong/) identifies Ong as a core contributor to Materials Project. Accessed 2026-07-12. |
| `SRC-LBNL-JAIN-PROFILE` | [Berkeley Lab Energy Technologies Area: Anubhav Jain](https://eta.lbl.gov/people/anubhav-jain) identifies Jain as Associate Director of Berkeley Lab's Materials Project program. Accessed 2026-07-12. |
| `SRC-UC-BERKELEY-CEDER-PROFILE` | [UC Berkeley Research: Gerbrand Ceder](https://vcresearch.berkeley.edu/faculty/gerbrand-ceder) states that the CEDER Group contributes extensively to Materials Project. It does not identify a complete contributor roster, individual role, software-maintenance responsibility, or ownership. Accessed 2026-07-12. |

## Boundary and limitations

This record does not claim that Lawrence Berkeley National Laboratory is the
ecosystem's exclusive owner or that the linked entities exhaust Materials
Project's collaborators, software, or host institutions. It distinguishes
[pymatgen](../research-software/pymatgen.md) as a software artifact rather than
equating the full platform with one library. The documentation's Department of
Energy origin is not converted into a current funding relationship: no reviewed
funding-programme identity and direct award evidence support one. The public
architecture does not establish the current deployment, availability, ownership,
or governance of every underlying package, workflow, database, or endpoint.
