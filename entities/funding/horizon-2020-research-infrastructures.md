---
schema_version: 2
entity_type: funding-program
id: FUND-H2020-RESEARCH-INFRASTRUCTURES
name: Horizon 2020 — Research Infrastructures
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-EC-HORIZON-2020
  - SRC-NOMAD-LABORATORY-CORDIS
funder_organization_id: ORG-EUROPEAN-COMMISSION
funding_program_kind: European Union research infrastructure funding programme
website: https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en
project_ids:
  - PROJ-NOMAD-LABORATORY-COE
relationship_assertions:
  - predicate: funds
    target_id: PROJ-NOMAD-LABORATORY-COE
    source_ids: [SRC-NOMAD-LABORATORY-CORDIS]
    confidence: high
    start_date: "2015-11-01"
    end_date: "2018-10-31"
    evidence_window: 2015-11–2018-10
    notes: CORDIS identifies the NoMaD project as funded under Horizon 2020 Excellent Science — Research Infrastructures. This dated relationship does not establish current funding or an exhaustive award portfolio.
---

# Horizon 2020 — Research Infrastructures

Horizon 2020 — Research Infrastructures is represented as the reviewed funding
programme context for the completed NoMaD Laboratory project. The record is
kept distinct from its funder organization, the project, and the project's
current software descendants.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-EC-HORIZON-2020` | [European Commission: Horizon 2020](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en) identifies Horizon 2020 as the EU research and innovation funding programme for 2014–2020 and states that it has ended. Accessed 2026-07-12. |
| `SRC-NOMAD-LABORATORY-CORDIS` | [European Commission CORDIS: The Novel Materials Discovery Laboratory](https://cordis.europa.eu/project/id/676580) identifies the completed NoMaD project as funded under Horizon 2020 Excellent Science — Research Infrastructures, with dates 2015-11-01 through 2018-10-31. Accessed 2026-07-12. |

## Boundary and limitations

This record captures one evidence-bounded programme-to-project relationship.
It does not establish all Horizon 2020 calls, beneficiaries, agencies, budgets,
or current funding opportunities, and it does not turn the historic award into
a claim about current NOMAD funding.
