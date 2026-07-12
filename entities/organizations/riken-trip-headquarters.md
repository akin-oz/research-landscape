---
schema_version: 2
entity_type: organization
id: ORG-RIKEN-TRIP
name: RIKEN TRIP Headquarters
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-RIKEN-TRIP-OVERVIEW
country_id: COUNTRY-JP
city: Wako
organization_kind: research program headquarters
website: https://www.riken.jp/en/research/labs/trip/index.html
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-JP
    source_ids: [SRC-RIKEN-TRIP-OVERVIEW]
    confidence: high
    evidence_window: 2026-07
---

# RIKEN TRIP Headquarters

RIKEN TRIP Headquarters is represented as the non-university direct host for
the Polymeromics Team. Its public organization page presents the team and
Ryo Yoshida within TRIP's research-platform structure.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-RIKEN-TRIP-OVERVIEW` | [RIKEN TRIP Headquarters](https://www.riken.jp/en/research/labs/trip/index.html) lists the Polymeromics Team and Ryo Yoshida in its organization and gives the Wako, Saitama, Japan contact address. Accessed 2026-07-12. |

## Boundary and limitations

This organization record covers the direct team host and geographic endpoint
used by this slice. It does not assert a university affiliation, a degree route,
or that every TRIP unit shares the Polymeromics Team's software and research
scope.
