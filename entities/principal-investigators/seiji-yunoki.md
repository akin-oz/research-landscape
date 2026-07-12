---
schema_version: 2
entity_type: principal-investigator
id: PI-SEIJI-YUNOKI
name: Seiji Yunoki
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-RIKEN-CMS-TEAM
  - SRC-RIKEN-YUNOKI-PROFILE
affiliation_ids:
  - ORG-RIKEN-CCS
research_group_ids:
  - RG-RIKEN-COMPUTATIONAL-MATERIALS-SCIENCE
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://www.r-ccs.riken.jp/en/research/labs/cmasrt/
relationship_assertions:
  - predicate: affiliated_with
    target_id: ORG-RIKEN-CCS
    source_ids: [SRC-RIKEN-YUNOKI-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: leads
    target_id: RG-RIKEN-COMPUTATIONAL-MATERIALS-SCIENCE
    role: team-principal
    source_ids: [SRC-RIKEN-CMS-TEAM]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-RIKEN-CMS-TEAM]
    confidence: high
    evidence_window: 2026-07
---

# Seiji Yunoki

Seiji Yunoki is represented for his current RIKEN Center for Computational
Science affiliation, Computational Materials Science Research Team leadership,
and computational-materials research connection. Other current RIKEN roles are
not modeled here because this slice uses the direct host of the named team.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-RIKEN-CMS-TEAM` | [RIKEN Computational Materials Science Research Team](https://www.r-ccs.riken.jp/en/research/labs/cmasrt/) identifies Seiji Yunoki as Team Principal and describes the team's numerical methods and computational materials/quantum-systems research. Accessed 2026-07-12. |
| `SRC-RIKEN-YUNOKI-PROFILE` | [RIKEN: Seiji Yunoki](https://www.r-ccs.riken.jp/labs/cms/people-post-en/seiji-yunoki/) lists his affiliation with the Computational Materials Science Research Team at R-CCS and identifies the R-CCS Team Principal title. Accessed 2026-07-12. |

## Boundary and limitations

This record does not attempt to model Yunoki's additional RIKEN affiliations,
infer that a team-level software application implies individual maintenance, or
treat R-CCS programs or job links as a current opening or degree route. It
makes no claim about mentoring, admissions, funding, language, or applicant fit.
