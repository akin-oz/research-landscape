---
schema_version: 2
entity_type: organization
id: ORG-LBNL
name: Lawrence Berkeley National Laboratory
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-LBNL-PERSSON-NEWS-2026
  - SRC-LBNL-CONTACT
country_id: COUNTRY-US
city: Berkeley
organization_kind: national laboratory
website: https://www.lbl.gov/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-US
    source_ids: [SRC-LBNL-CONTACT]
    confidence: high
    evidence_window: 2026-07
---

# Lawrence Berkeley National Laboratory

Lawrence Berkeley National Laboratory (Berkeley Lab) is represented as a
non-university Organization. It is the accountable direct host for the Persson
Group in this slice; that relationship does not model the full institutional
structure around the Materials Project ecosystem.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-LBNL-PERSSON-NEWS-2026` | [Berkeley Lab, 8 May 2026: Kristin Persson elected to the American Academy of Arts and Sciences](https://newscenter.lbl.gov/2026/05/08/berkeley-labs-kristin-persson-elected-to-the-american-academy-of-arts-and-sciences/) describes Berkeley Lab as a multiprogram national laboratory managed by the University of California for the U.S. Department of Energy Office of Science. Accessed 2026-07-12. |
| `SRC-LBNL-CONTACT` | [Berkeley Lab Intellectual Property Office: Contact Us](https://ipo.lbl.gov/about-us/contact-us/) gives Lawrence Berkeley National Laboratory's mailing address as 1 Cyclotron Road, Berkeley, CA 94720 USA. Accessed 2026-07-12. |

## Boundary and limitations

This organization record covers the public host and location relationships used
by this cohort. It does not claim exclusive ownership or exclusive hosting of
Materials Project, which is publicly described as a broader effort.
