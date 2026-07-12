---
schema_version: 2
entity_type: research-ecosystem
id: ECO-MATML
name: MatML Ecosystem
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-MATGL-REPOSITORY
ecosystem_kind: materials graph-learning and potential-software ecosystem
website: https://github.com/materialyzeai/matgl
software_ids:
  - SW-MATGL
relationship_assertions:
  - predicate: includes
    target_id: SW-MATGL
    source_ids: [SRC-MATGL-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: MatGL describes itself as part of the named MatML ecosystem. Other named ecosystem components are not added until separately reviewed as canonical entities.
---

# MatML Ecosystem

MatML is the named ecosystem context publicly described by the MatGL project.
This canonical node currently records only the verified MatGL inclusion. Other
named components—such as MAML, MatPES, and MatCalc—remain absent until their
own identities and relationships are independently reviewed.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-MATGL-REPOSITORY` | [materialyzeai/matgl](https://github.com/materialyzeai/matgl) describes MatGL as part of the MatML ecosystem and names MAML, MatPES, and MatCalc as other ecosystem components. It supports the named ecosystem context and MatGL inclusion, not a complete component, contributor, funding, or governance graph. Accessed 2026-07-12. |

## Boundary and limitations

This record does not create canonical records for every named component,
model, dataset, contributor, organization, or user. It does not imply common
ownership, equal licensing, active support, performance, employment,
mentorship, admissions, or applicant fit.
