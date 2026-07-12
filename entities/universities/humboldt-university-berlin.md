---
schema_version: 2
entity_type: university
id: UNIVERSITY-HU-BERLIN
name: Humboldt-Universität zu Berlin
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-HU-CONTACT
  - SRC-HU-IMPRINT
country_id: COUNTRY-DE
city: Berlin
website: https://www.hu-berlin.de/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-DE
    source_ids: [SRC-HU-CONTACT]
    confidence: high
    evidence_window: 2026-07
---

# Humboldt-Universität zu Berlin

Humboldt-Universität zu Berlin is the direct University host for SOLgroup in
this slice. It is represented as a University rather than duplicated as a
generic Organization.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-HU-CONTACT` | [Humboldt International Campus: Contact](https://hic.hu-berlin.de/en/contact) gives Humboldt-Universität zu Berlin's address in Berlin, Germany. Accessed 2026-07-12. |
| `SRC-HU-IMPRINT` | [Humboldt-Universität zu Berlin: Imprint](https://prod.elsa.agnes.hu-berlin.de/elsa/pages/cs/sys/portal/imprint/imprint.faces?navigationPosition=link_impressum&recordRequest=true) identifies the University as a public-law corporation and gives its Berlin address. Accessed 2026-07-12. |

## Boundary and limitations

This record supplies the University host and geographic endpoint used by this
slice. It makes no University-wide claim about rankings, admissions, funding,
language, programme eligibility, or research quality.
