---
schema_version: 2
entity_type: principal-investigator
id: PI-RYO-YOSHIDA
name: Ryo Yoshida
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-RIKEN-POLYMEROMICS-TEAM
  - SRC-RIKEN-TRIP-OVERVIEW
affiliation_ids:
  - ORG-RIKEN-TRIP
research_group_ids:
  - RG-RIKEN-POLYMEROMICS
research_area_ids:
  - AREA-MATERIALS-INFORMATICS
website: https://www.riken.jp/en/research/labs/trip/agis/polymeromics/index.html
relationship_assertions:
  - predicate: affiliated_with
    target_id: ORG-RIKEN-TRIP
    source_ids: [SRC-RIKEN-TRIP-OVERVIEW]
    confidence: high
    evidence_window: 2026-07
  - predicate: leads
    target_id: RG-RIKEN-POLYMEROMICS
    role: team-director
    source_ids: [SRC-RIKEN-POLYMEROMICS-TEAM]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-MATERIALS-INFORMATICS
    source_ids: [SRC-RIKEN-POLYMEROMICS-TEAM]
    confidence: high
    evidence_window: 2026-07
---

# Ryo Yoshida

Ryo Yoshida is represented for his current RIKEN TRIP affiliation, Polymeromics
Team leadership, and materials-informatics research connection. RadonPy is
linked at group level, because the reviewed sources do not establish an
individual maintenance role.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-RIKEN-POLYMEROMICS-TEAM` | [RIKEN Polymeromics Team](https://www.riken.jp/en/research/labs/trip/agis/polymeromics/index.html) identifies Ryo Yoshida as Team Director and describes the team's polymer database, automated simulation, machine-learning, and autonomous-discovery work. Accessed 2026-07-12. |
| `SRC-RIKEN-TRIP-OVERVIEW` | [RIKEN TRIP Headquarters](https://www.riken.jp/en/research/labs/trip/index.html) lists the Polymeromics Team and Ryo Yoshida in its organization. Accessed 2026-07-12. |

## Boundary and limitations

This record does not derive an individual RadonPy maintainer or development
role from publication authorship or the group connection, and does not convert
team recruitment notices into a degree route or general availability claim. It
makes no claim about mentoring, admissions, funding, language, or applicant fit.
