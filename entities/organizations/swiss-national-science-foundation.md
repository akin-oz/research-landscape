---
schema_version: 2
entity_type: organization
id: ORG-SNSF
name: Swiss National Science Foundation (SNSF)
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-SNSF-ABOUT
  - SRC-SNSF-CONTACT
  - SRC-SNSF-NCCR-PROGRAM
country_id: COUNTRY-CH
city: Bern
organization_kind: research funding organization
website: https://www.snf.ch/en/kPRYnL3xxtTod01R/page/theSNSF
funding_program_ids:
  - FUND-NCCR-MARVEL
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-CH
    source_ids: [SRC-SNSF-CONTACT]
    confidence: high
    evidence_window: 2026-07
  - predicate: administers
    target_id: FUND-NCCR-MARVEL
    source_ids: [SRC-SNSF-NCCR-PROGRAM]
    confidence: high
    evidence_window: 2026-07
    notes: The SNSF's NCCR programme page identifies the NCCR scheme as an SNSF programme and its MARVEL entry; this does not represent every co-funder or programme participant.
---

# Swiss National Science Foundation

The Swiss National Science Foundation (SNSF) is represented as the research
funder for the reviewed NCCR MARVEL funding-program record. It is distinct from
the Universities, research institutes, and research groups that participate in
the resulting research network.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SNSF-ABOUT` | [SNSF: About us](https://www.snf.ch/en/kPRYnL3xxtTod01R/page/theSNSF) identifies the Swiss National Science Foundation as Switzerland's research funding organization, mandated by the federal government to support basic science. Accessed 2026-07-12. |
| `SRC-SNSF-CONTACT` | [SNSF: Contact](https://www.snf.ch/en/X5jbA5udARKhcIk8/page/aboutus/contact) gives the Swiss National Science Foundation postal address in Bern, Switzerland. Accessed 2026-07-12. |
| `SRC-SNSF-NCCR-PROGRAM` | [SNSF: National Centres of Competence in Research](https://www.snf.ch/en/FJBJ8XGQ1tjG8J8w/funding/programmes/national-centres-of-competence-in-research-nccr) describes NCCRs as an SNSF funding programme and lists NCCR MARVEL among the programme's centres. Accessed 2026-07-12. |

## Boundary and limitations

This record identifies the funder and programme-administration context only.
It does not attribute all NCCR funding to SNSF alone, list every NCCR, infer a
grant amount for a specific participant, or establish a relationship with every
Swiss research organization.
