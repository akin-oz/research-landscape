# NCCR MARVEL funding vertical slice review

**Review date:** 2026-07-12

**Scope:** the reviewed SNSF / NCCR MARVEL / Materials Cloud funding-context
cohort in [the vertical-slice document](../docs/nccr-marvel-funding-vertical-slice.md).

**Outcome:** this first Quality Gate 2 slice adds two canonical entities and
three evidence-bearing relationships. It introduces a funding-program record,
connects it to a distinct funder organization, and adds only a historical,
limited ecosystem connection supported by NCCR MARVEL's public material.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| SNSF identity and location | SNSF About and Contact pages | Supports SNSF as a Swiss research funding organization and its Bern, Switzerland location endpoint. |
| NCCR programme administration | SNSF NCCR programme page | Supports NCCR programme context, SNSF administration, and NCCR MARVEL's place in that programme. |
| NCCR MARVEL time boundary | NCCR MARVEL third-phase award announcement | Supports a final phase scheduled from May 2022 through April 2026 and the 2014–2026 SNSF funding context. |
| Materials Cloud connection | NCCR MARVEL Materials Cloud announcement | Supports a historical 2021 statement that Materials Cloud was developed by NCCR MARVEL, not a current-funding or ownership claim. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S57` through `S60` remain source-
register keys and are not used as canonical citation identifiers.

## Relationship review

| Check | Result |
| --- | --- |
| Funder endpoint | `FUND-NCCR-MARVEL.funder_organization_id` resolves to the reviewed `ORG-SNSF` organization record. |
| Administration assertion | `ORG-SNSF` records `administers → FUND-NCCR-MARVEL` with SNSF programme evidence. |
| Location assertion | `ORG-SNSF` records `located_in → COUNTRY-CH` with SNSF contact evidence. |
| Historical ecosystem assertion | `ECO-MATERIALS-CLOUD` records `connects → FUND-NCCR-MARVEL` with a 2021 evidence window and explicit non-current limitation. |
| One-way storage | No inverse `administers`, `located_in`, or `connects` relationship is added to the target record. |

## Deliberate non-claims

1. This record does not make a current-funding claim for Materials Cloud from
   the cited final NCCR MARVEL phase, which was scheduled through April 2026.
2. It does not establish the complete NCCR MARVEL consortium, every co-funder,
   grant recipient, amount, or allocation.
3. It does not create a project node from an internal MARVEL project label,
   because the required project identity and complete evidence-bearing graph
   edges are not established by this slice's reviewed sources.
4. No current opening, programme eligibility, supervision, admissions,
   mentorship, funding availability, language, ranking, or applicant-fit claim
   is made.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this
cohort was added. It checked schema shape and date formats, unique IDs,
relationship target/type compatibility (including the new `administers`
mapping), record-local source resolution, direct-host target type, matching
`belongs_to` assertions, exact-one host cardinality, changed-document local
links, whitespace, and the ADR 0006 University/Organization positive and
negative branch cases. No persistent validator, migration utility, generated
view, or architecture change is introduced before Quality Gate 6.
