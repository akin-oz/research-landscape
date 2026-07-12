---
schema_version: 2
entity_type: principal-investigator
id: PI-ELLAD-TADMOR
name: Ellad Tadmor
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-UMN-TADMOR-PROFILE
  - SRC-UMN-TADMOR-CV
affiliation_ids:
  - UNIVERSITY-UMN
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://cse.umn.edu/dsi/ellad-tadmor
relationship_assertions:
  - predicate: affiliated_with
    target_id: UNIVERSITY-UMN
    source_ids: [SRC-UMN-TADMOR-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-UMN-TADMOR-PROFILE]
    confidence: high
    evidence_window: 2026-07
    notes: The University of Minnesota profile describes atomic-scale materials modelling and the KIM online infrastructure for assessing interatomic-potential transferability. This is a bounded Computational Materials Science connection, not a complete research profile.
---

# Ellad Tadmor

Ellad Tadmor is represented for his current University of Minnesota professor
affiliation, atomic-scale materials-modelling research connection, and
separately documented historical founding-director context for OpenKIM. The
OpenKIM ecosystem owns the latter relationship to avoid asserting a current
maintenance or governance assignment on this PI record.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-UMN-TADMOR-PROFILE` | [University of Minnesota: Ellad Tadmor](https://cse.umn.edu/dsi/ellad-tadmor) identifies him as a Professor of Aerospace Engineering and Mechanics, describes atomic-scale modelling research, and identifies development of the Knowledgebase of Interatomic Models (KIM) as online infrastructure for assessing interatomic-potential transferability. Accessed 2026-07-13. |
| `SRC-UMN-TADMOR-CV` | [University of Minnesota: Ellad Tadmor curriculum vitae](https://dept.aem.umn.edu/~tadmor/Biography/tadmor-cv.pdf) identifies Tadmor as Founding Director of OpenKIM and describes the project as NSF cyberinfrastructure that develops and maintains a curated interatomic-model repository, API, and testing/curation workflow. Accessed 2026-07-13. |

## Boundary and limitations

This record does not treat founding-director history as a current coding,
maintenance, review, governance, contribution-frequency, employment,
supervision, mentoring, funding, admissions, or applicant-fit claim.
