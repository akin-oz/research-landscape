---
schema_version: 2
entity_type: research-ecosystem
id: ECO-AIIDA
name: AiiDA Ecosystem
status: reviewed
created_at: "2026-07-11"
updated_at: "2026-07-11"
last_review: "2026-07-11"
confidence: high
source_ids:
  - SRC-AIIDA-ECOSYSTEM
  - SRC-AIIDA-TEAM
ecosystem_kind: research-software ecosystem
website: https://aiida.net/ecosystem/
software_ids:
  - SW-AIIDA-CORE
organization_ids:
  - ORG-PSI
research_group_ids:
  - RG-PSI-MSD
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

## Boundary and limitations

The record asserts only the AiiDA-to-PSI connections documented above. It does
not claim exclusive ownership by PSI, enumerate every plugin, infer funding, or
turn a development-team listing into an availability or supervision claim.
