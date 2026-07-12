---
schema_version: 2
entity_type: university
id: UNIVERSITY-EPFL
name: EPFL
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-EPFL-ACCREDITATION
  - SRC-EPFL-CONTACT
country_id: COUNTRY-CH
city: Lausanne
website: https://www.epfl.ch/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-CH
    source_ids: [SRC-EPFL-ACCREDITATION, SRC-EPFL-CONTACT]
    confidence: high
    evidence_window: 2026-07
---

# EPFL

EPFL is the direct University host for THEOS in this slice. It is represented
as a University rather than duplicated as a generic Organization.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-EPFL-ACCREDITATION` | [EPFL institutional accreditation self-assessment](https://www.epfl.ch/about/presidency/wp-content/uploads/2022/05/EPFL-Self-assessment-report-2021-22-11.pdf) identifies EPFL (École polytechnique fédérale de Lausanne) as a Swiss federal public university. Accessed 2026-07-12. |
| `SRC-EPFL-CONTACT` | [EPFL: Contact information](https://www.epfl.ch/about/overview/regulations-and-guidelines/epfl-privacy-policy/contact/) gives École Polytechnique Fédérale de Lausanne's mailing address in Lausanne, Switzerland. Accessed 2026-07-12. |

## Boundary and limitations

This record supplies the University host and geographic endpoint used by this
slice. It makes no University-wide claim about rankings, admissions, funding,
language, programme eligibility, or research quality.
