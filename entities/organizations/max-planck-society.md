---
schema_version: 2
entity_type: organization
id: ORG-MPG
name: Max Planck Society for the Advancement of Science
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-MPG-ORGANIZATION
  - SRC-MPG-NOMAD-COORDINATION
country_id: COUNTRY-DE
organization_kind: research organization
website: https://www.mpg.de/183267/organisation
project_ids:
  - PROJ-NOMAD-LABORATORY-COE
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-DE
    source_ids: [SRC-MPG-NOMAD-COORDINATION]
    confidence: high
    evidence_window: 2015-11–2018-10
    notes: This location assertion is bounded to the reviewed NOMAD project context; it does not enumerate all Max Planck Society locations.
---

# Max Planck Society for the Advancement of Science

The Max Planck Society (MPG) is represented as the coordinating research
organization for the completed NoMaD Laboratory Centre of Excellence project.
It is not conflated with the project, the NOMAD software artifact, or every
independent Max Planck institute.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-MPG-ORGANIZATION` | [Max Planck Society: Organisational structure](https://www.mpg.de/183267/organisation) identifies the Max Planck Society for the Advancement of Science as an independent, non-profit research organization and describes its registered seat in Berlin. Accessed 2026-07-12. |
| `SRC-MPG-NOMAD-COORDINATION` | [European Commission CORDIS: The Novel Materials Discovery Laboratory](https://cordis.europa.eu/project/id/676580) identifies Max-Planck-Gesellschaft zur Förderung der Wissenschaften e.V. in Germany as coordinator of the completed NoMaD project. Accessed 2026-07-12. |

## Boundary and limitations

This record establishes only the organization-level project coordination and
bounded Germany location needed by this slice. It does not make a claim about
every MPG institute, employee, current NOMAD maintainer, project participant,
or research area.
