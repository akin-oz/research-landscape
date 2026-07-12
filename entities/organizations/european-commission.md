---
schema_version: 2
entity_type: organization
id: ORG-EUROPEAN-COMMISSION
name: European Commission
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-EC-ABOUT
  - SRC-EC-HORIZON-2020
organization_kind: European Union executive and funding body
website: https://commission.europa.eu/about_en
funding_program_ids:
  - FUND-H2020-RESEARCH-INFRASTRUCTURES
relationship_assertions:
  - predicate: administers
    target_id: FUND-H2020-RESEARCH-INFRASTRUCTURES
    source_ids: [SRC-EC-ABOUT, SRC-EC-HORIZON-2020]
    confidence: high
    evidence_window: 2014-01–2020-12
    notes: The Commission manages EU funding programmes, and its official Horizon 2020 page identifies Horizon 2020 as the EU research and innovation funding programme for 2014–2020. This does not assert a current programme or an individual award decision.
---

# European Commission

The European Commission is represented as the organization-level funder context
for the completed Horizon 2020 Research Infrastructures programme record. It
is not modeled as a country, a project participant, or a proxy for every EU
institution or funding mechanism.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-EC-ABOUT` | [European Commission: About](https://commission.europa.eu/about_en) identifies the European Commission as the executive body of the European Union and describes its role in managing the EU budget, allocating funding, and managing funding programmes through its departments and executive agencies. Accessed 2026-07-12. |
| `SRC-EC-HORIZON-2020` | [European Commission: Horizon 2020](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en) identifies Horizon 2020 as the EU research and innovation funding programme for 2014–2020 and notes that it has been succeeded by Horizon Europe. Accessed 2026-07-12. |

## Boundary and limitations

This record establishes a programme-administration context only. It does not
claim that the Commission directly managed every grant action, identify a
current Horizon 2020 opportunity, enumerate EU institutions, or establish a
country-level ownership path.
