# FAIRmat Users Meeting vertical slice review

**Review date:** 2026-07-12

**Scope:** the reviewed FAIRmat / Eighth FAIRmat Users Meeting cohort in
[the vertical-slice document](../docs/fairmat-users-meeting-vertical-slice.md).

**Outcome:** this fifth Quality Gate 2 slice adds one canonical Conference
record and two evidence-bearing relationships. It records a completed FAIRmat
event, its bounded ecosystem connection, and its documented computational-
materials workflow scope without turning the event into a people or host roster.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Event identity, dates, and location | FAIRmat Indico event page | Supports the June 16–17, 2026 Berlin meeting identity and published scope. |
| Event completion and FAIRmat/NOMAD relation | FAIRmat event listing | Confirms the Users Meeting as a FAIRmat event focused on FAIRmat/NOMAD practical data-management sessions. |
| Research-area scope | FAIRmat Indico event page | Supports experimental and computational research workflows in physics, chemistry, and materials science. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S69` and `S70` remain source-register
keys and are not used as canonical citation identifiers.

## Relationship review

| Check | Result |
| --- | --- |
| Ecosystem assertion | `ECO-FAIRMAT` records `connects → CONF-FAIRMAT-USERS-MEETING-2026` with a June 2026 historical-event window. |
| Conference index | `ECO-FAIRMAT.conference_ids` resolves to the reviewed Conference record without duplicating its event profile. |
| Area assertion | The Conference records `covers → AREA-COMPUTATIONAL-MATERIALS-SCIENCE` with its official event-scope evidence. |
| Country context | `country_id: COUNTRY-DE` resolves to the existing Germany record; no additional location relationship is inferred. |
| One-way storage | No inverse `connects` or `covers` assertion is stored on the ecosystem or area target. |

## Deliberate non-claims

1. This completed event does not establish a recurring series, a future meeting,
   or a current event opportunity.
2. It does not establish an attendee, speaker, organizer, host, developer, or
   maintainer role for any person or institution named in programme material.
3. It does not establish that all FAIRmat or NOMAD participants attended or
   that participation conveys affiliation, mentorship, funding, or employment.
4. No current opening, supervision, mentoring, admissions, language, ranking,
   or applicant-fit claim is made.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this
cohort was added. It checked schema shape and date formats, unique IDs,
relationship target/type compatibility (including `covers`), record-local
source resolution, direct-host target type, matching `belongs_to` assertions,
exact-one host cardinality, changed-document local links, whitespace, and the
ADR 0006 University/Organization positive and negative branch cases. No
persistent validator, migration utility, generated view, or architecture
change is introduced before Quality Gate 6.
