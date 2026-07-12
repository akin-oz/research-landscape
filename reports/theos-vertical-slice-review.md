# THEOS–EPFL / Materials Cloud vertical slice review

**Review date:** 2026-07-12

**Scope:** the reviewed Nicola Marzari / THEOS cohort in
[the vertical-slice document](../docs/theos-vertical-slice.md).

**Outcome:** the slice adds four canonical entities, makes one bounded update
to the existing AiiDA ecosystem, and adds twelve evidence-bearing
relationships. It exercises the accepted University-host branch of ADR 0006,
adds Materials Cloud as a separate ecosystem, and preserves the distinction
between current and future affiliations.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| EPFL and THEOS identity, host, and PI role | EPFL Marzari profile and institutional material | Supports the current Full Professor role, THEOS group identity, EPFL direct host, and Swiss geographic endpoint. |
| THEOS research and infrastructure contribution | THEOS research overview | Supports computational modelling, first-principles/high-throughput research, and shared contributions to AiiDA and Materials Cloud. |
| Current PSI affiliation | Materials Cloud team page and PSI Laboratory for Materials Simulations page | Supports Marzari's current PSI laboratory-head role without creating an overlapping PSI group record. |
| Materials Cloud identity and relation to AiiDA | Materials Cloud overview and team pages | Supports a separate open computational-materials ecosystem, the “powered by AiiDA” relationship, and Marzari's project-leader listing. |
| Future affiliation boundary | 2026 EPFL news announcement | Confirms the Cambridge post begins in September 2026; it is intentionally not a current vNext affiliation on the July review date. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S33` and `S39`–`S42` remain
source-register keys and are not used as canonical citation identifiers.

## ADR 0006 host review

| Check | Result |
| --- | --- |
| Direct-host cardinality | `RG-THEOS` has `institution_id: UNIVERSITY-EPFL` and no `organization_id`. |
| Host type | `UNIVERSITY-EPFL` resolves to one reviewed v2 `university` record. |
| Evidence-bearing relationship | THEOS records `belongs_to → UNIVERSITY-EPFL` using the current EPFL profile. |
| No duplicate Organization | No generic Organization duplicate is created for EPFL. |

## Deliberate non-claims

1. The expected September 2026 Cambridge appointment is not a current
   affiliation, and no future University or group record is added.
2. The THEOS contribution to AiiDA and Materials Cloud is shared; it is not
   evidence of exclusive development, ownership, maintenance, or governance.
3. Marzari's NCCR MARVEL director title does not, by itself, create a project,
   funding-programme, participant, or governance graph node.
4. Materials Cloud's relationship to AiiDA does not reduce either ecosystem to
   the other or establish an exhaustive software inventory.
5. No current opening, supervision, mentoring, admissions, funding, language,
   ranking, or applicant-fit claim is made.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this
cohort was added. It checked schema shape and date formats, unique IDs,
relationship target/type compatibility, record-local source resolution,
direct-host target type, matching `belongs_to` assertions, exact-one host
cardinality, changed-document local links, whitespace, and the ADR 0006
University/Organization positive and negative branch cases. No generic
validator, automation, migration, or architecture change is introduced in
this Quality Gate 1 slice.
