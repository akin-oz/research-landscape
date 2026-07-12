---
schema_version: 2
entity_type: research-group
id: RG-RIKEN-POLYMEROMICS
name: Polymeromics Team
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-RIKEN-POLYMEROMICS-TEAM
  - SRC-RIKEN-TRIP-OVERVIEW
organization_id: ORG-RIKEN-TRIP
research_area_ids:
  - AREA-MATERIALS-INFORMATICS
software_ids:
  - SW-RADONPY
website: https://www.riken.jp/en/research/labs/trip/agis/polymeromics/index.html
relationship_assertions:
  - predicate: belongs_to
    target_id: ORG-RIKEN-TRIP
    source_ids: [SRC-RIKEN-TRIP-OVERVIEW]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-MATERIALS-INFORMATICS
    source_ids: [SRC-RIKEN-POLYMEROMICS-TEAM]
    confidence: high
    evidence_window: 2026-07
  - predicate: develops
    target_id: SW-RADONPY
    source_ids: [SRC-RIKEN-POLYMEROMICS-TEAM]
    confidence: high
    evidence_window: 2026-07
    notes: The team presents RadonPy as a selected output and related GitHub link; this supports a shared group-level development connection, not exclusive ownership or an individual maintainer roster.
---

# Polymeromics Team

The Polymeromics Team is the TRIP-hosted research-group node in this slice. Its
current public description supports a Materials Informatics connection through
integrated polymer databases, automated molecular-dynamics and first-principles
simulation, and machine-learning research.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-RIKEN-POLYMEROMICS-TEAM` | [RIKEN Polymeromics Team](https://www.riken.jp/en/research/labs/trip/agis/polymeromics/index.html) identifies Ryo Yoshida as Team Director; describes integrated experimental and computational polymer databases, automated molecular-dynamics/first-principles computation, Sim2Real machine learning, and autonomous discovery; and lists RadonPy as a selected output and related GitHub link. Accessed 2026-07-12. |
| `SRC-RIKEN-TRIP-OVERVIEW` | [RIKEN TRIP Headquarters](https://www.riken.jp/en/research/labs/trip/index.html) lists the Polymeromics Team and Ryo Yoshida in its organization. Accessed 2026-07-12. |

## Boundary and limitations

This record does not enumerate all team personnel, claim that every output is
group-maintained software, or infer exclusive ownership or governance of
RadonPy. It makes no claim about openings, mentoring, admissions, funding,
language, or applicant fit.
