# RIKEN Computational Materials Science–Yunoki vertical slice review

**Review date:** 2026-07-12

**Scope:** the reviewed Seiji Yunoki / RIKEN Center for Computational Science
cohort in [the vertical-slice document](../docs/riken-yunoki-vertical-slice.md).

**Outcome:** the slice adds four canonical entities and six evidence-bearing
relationships. It exercises the accepted Organization-host branch of ADR 0006
and keeps documented numerical-methods and software-application statements
separate from unsupported software stewardship claims.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| R-CCS identity, team host, and location | RIKEN Center for Computational Science overview and access page | Supports the non-university host, team listing, Kobe location, and Japan endpoint. |
| Yunoki’s current R-CCS affiliation and team role | RIKEN Yunoki profile and team page | Supports current R-CCS affiliation and Team Principal leadership of the named team. |
| Team research scope | RIKEN Computational Materials Science Research Team page | Supports numerical methods, quantum simulations, materials/condensed-matter scope, and reuse of the Computational Materials Science area. |
| Software boundary | Same team page | The reference to a software application does not name an artifact or establish development/maintenance ownership, so no such node or edge is created. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S36` and `S48`–`S50` remain
source-register keys and are not used as canonical citation identifiers.

## ADR 0006 host review

| Check | Result |
| --- | --- |
| Direct-host cardinality | `RG-RIKEN-COMPUTATIONAL-MATERIALS-SCIENCE` has `organization_id: ORG-RIKEN-CCS` and no `institution_id`. |
| Host type | `ORG-RIKEN-CCS` resolves to one reviewed v2 `organization` record. |
| Evidence-bearing relationship | The team records `belongs_to → ORG-RIKEN-CCS` using current RIKEN organization and team sources. |
| No duplicate University | No University or generic Organization duplicate is created for R-CCS. |

## Deliberate non-claims

1. A generic reference to a software application does not prove a named
   software artifact, individual maintenance, group development, or ownership.
2. The additional RIKEN affiliations in Yunoki’s individual profile are not
   modeled as current canonical affiliations in this slice, because the scope
   is the direct R-CCS host of the named anchor team.
3. R-CCS job, internship, school, or joint-graduate-programme pages are not
   treated as evidence of a current Yunoki-team opening or degree pathway.
4. No current opening, supervision, mentoring, admissions, funding, language,
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
