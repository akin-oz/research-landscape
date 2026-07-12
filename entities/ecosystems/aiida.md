---
schema_version: 2
entity_type: research-ecosystem
id: ECO-AIIDA
name: AiiDA Ecosystem
status: reviewed
created_at: "2026-07-11"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-AIIDA-ECOSYSTEM
  - SRC-AIIDA-TEAM
  - SRC-THEOS-RESEARCH
  - SRC-AIIDA-DOCUMENTATION
  - SRC-AIIDA-PLUGIN-REGISTRY
  - SRC-AIIDA-CONTRIBUTION
  - SRC-AIIDA-ACKNOWLEDGEMENTS
ecosystem_kind: research-software ecosystem
website: https://aiida.net/ecosystem/
software_ids:
  - SW-AIIDA-CORE
organization_ids:
  - ORG-PSI
research_group_ids:
  - RG-PSI-MSD
  - RG-THEOS
funding_program_ids:
  - FUND-NCCR-MARVEL
relationship_assertions:
  - predicate: includes
    target_id: SW-AIIDA-CORE
    source_ids: [SRC-AIIDA-ECOSYSTEM]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: RG-PSI-MSD
    source_ids: [SRC-AIIDA-TEAM]
    confidence: high
    evidence_window: 2026-07
    notes: The team page identifies the Materials Software and Data Group at PSI as a joint-effort partner.
  - predicate: connects
    target_id: ORG-PSI
    source_ids: [SRC-AIIDA-TEAM]
    confidence: high
    evidence_window: 2026-07
    notes: The team page identifies PSI as the host of the Materials Software and Data Group in the joint effort.
  - predicate: connects
    target_id: PI-GIOVANNI-PIZZI
    role: development-team member
    source_ids: [SRC-AIIDA-TEAM]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: RG-THEOS
    source_ids: [SRC-THEOS-RESEARCH]
    confidence: high
    evidence_window: 2026-07
    notes: THEOS describes a shared contribution to AiiDA development and maintenance; this does not assert exclusive development.
  - predicate: connects
    target_id: FUND-NCCR-MARVEL
    source_ids: [SRC-AIIDA-ACKNOWLEDGEMENTS]
    confidence: high
    evidence_window: 2026-07
    notes: AiiDA acknowledges NCCR MARVEL support for AiiDA development. This does not establish current funding, an exclusive funder, or support for every ecosystem component.
---

# AiiDA Ecosystem

This record models the public AiiDA ecosystem, not a generic category for all
workflow software. The ecosystem connects `aiida-core`, the documented PSI
development group and its group leader without claiming that those are the
ecosystem's only participants or hosts.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-AIIDA-ECOSYSTEM` | [The AiiDA ecosystem](https://aiida.net/ecosystem/) describes AiiDA as an ecosystem of tools, platforms and community plugins and calls `aiida-core` the foundation for the surrounding components. Accessed 2026-07-11. |
| `SRC-AIIDA-TEAM` | [AiiDA team](https://aiida.net/team/) identifies the Materials Software and Data Group at PSI as a joint-effort partner and lists Giovanni Pizzi in the AiiDA development team as its group leader. Accessed 2026-07-11. |
| `SRC-THEOS-RESEARCH` | [THEOS: Research overview](https://www.epfl.ch/labs/theos/page-89530-en-html/) says THEOS contributes to the development and maintenance of open-source infrastructure including AiiDA. Accessed 2026-07-12. |
| `SRC-AIIDA-DOCUMENTATION` | [AiiDA documentation: Introduction](https://aiida.readthedocs.io/projects/aiida-core/en/stable/intro/index.html) describes the workflow, provenance, high-throughput, data-query, and reproducibility functions of AiiDA. Accessed 2026-07-12. |
| `SRC-AIIDA-PLUGIN-REGISTRY` | [AiiDA plugin registry](https://aiida.net/plugin-registry/) describes community plugins for simulation codes, data types, schedulers, transports, and workflows. Accessed 2026-07-12. |
| `SRC-AIIDA-CONTRIBUTION` | [aiidateam/aiida-core](https://github.com/aiidateam/aiida-core) provides the public source repository and contributor pathway through issues, pull requests, discussions, and the Contributor wiki. Accessed 2026-07-12. |
| `SRC-AIIDA-ACKNOWLEDGEMENTS` | [AiiDA acknowledgements](https://www.aiida.net/sections/acknowledgements.html) lists NCCR MARVEL among the organizations and projects that support or have supported AiiDA development. Accessed 2026-07-12. |

## Purpose, architecture, and scientific scope

AiiDA is an open-source infrastructure for automating, managing, preserving,
sharing, and reproducing complex computational-science workflows and their
data. Its public architecture centers on `aiida-core`: an event-based workflow
engine, provenance graph, object-relational data layer, plugin interface, and
interfaces to local and remote compute resources. The AiiDA ecosystem extends
that core through code-specific plugins, workflow tools, learning resources,
AiiDAlab, and Materials Cloud data-sharing routes.

## Community and contribution workflow

The public plugin registry makes community extensions discoverable across
simulation codes, data types, schedulers, transports, and workflows. The
project-owned repository provides public issues, pull requests, discussions,
and a Contributor wiki; the official documentation provides tutorials and
plugin-development material. These are contribution and learning surfaces, not
evidence of an individual review, maintainer, employment, or mentorship role.

## Typical user journey

The official ecosystem documentation describes a five-step path: install
`aiida-core`; add code plugins; connect to local or remote compute resources;
run calculations and workflows while recording provenance; then share data and
provenance through Materials Cloud or build browser-facing workflows with
AiiDAlab. This is an upstream product journey, not a claim that every user
follows it or that every plugin supports every workflow.

## Institutional, funding, and publication context

PSI's Materials Software and Data Group and EPFL's THEOS have separate,
evidence-bearing group records. The AiiDA acknowledgements support a bounded
historical/current-support connection to [NCCR MARVEL](../funding/nccr-marvel.md),
but do not establish an exclusive or current award. The reviewed key technical
reference is [AiiDA 1.0](../publications/aiida-1-0.md), kept as a separate
publication record.

## Career-relevant learning surface

For a researcher or software engineer, the documented public entry points are
workflow design, provenance-aware data handling, plugin development, source
contributions, tutorials, and HPC-facing workflow execution. These are
evidence-backed skills surfaces, not a promise of employment, admission,
mentorship, contribution acceptance, or a personalized career outcome.

## Modeling limitations

The current vNext contract has no canonical Programming Language, Community,
or dependency entity type and no typed ecosystem-to-ecosystem predicate.
Consequently, the Python, plugin, Materials Cloud, AiiDAlab, and dependency
contexts are documented with source-backed links rather than manufactured graph
nodes or unsupported relationship assertions.

## Boundary and limitations

The record asserts only the AiiDA-to-PSI, AiiDA-to-THEOS, and NCCR MARVEL
support connections documented above. It does not claim exclusive ownership by
either host or funder, enumerate every plugin or contributor, infer current
funding, or turn a development-team listing into an availability or supervision
claim.
