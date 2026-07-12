# RIKEN Polymeromics–Yoshida vertical slice review

**Review date:** 2026-07-12

**Scope:** the reviewed Ryo Yoshida / RIKEN TRIP / Polymeromics cohort in
[the vertical-slice document](../docs/riken-polymeromics-vertical-slice.md).

**Outcome:** the slice adds four canonical entities and seven evidence-bearing
relationships. It exercises the accepted Organization-host branch of ADR 0006,
adds the named RadonPy artifact, and preserves the distinction between a
group-level software connection and an individual maintainer claim.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| TRIP identity, team host, and location | RIKEN TRIP Headquarters page | Supports the non-university host, Polymeromics Team and Yoshida listing, Wako location, and Japan endpoint. |
| Yoshida’s current role and group scope | RIKEN Polymeromics Team page | Supports Team Director leadership and polymer database, automated MD/first-principles, machine-learning, and autonomous-discovery scope. |
| RadonPy identity and license | Project-owned GitHub repository | Supports an open-source Python artifact for automated polymer physical-property calculation and BSD-3-Clause license. |
| Group-to-software connection | RIKEN Polymeromics Team page | Supports a bounded group-level relationship because the page lists RadonPy as a selected team output and related GitHub resource. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S37`, `S51`, and `S52` remain
source-register keys and are not used as canonical citation identifiers.

## ADR 0006 host review

| Check | Result |
| --- | --- |
| Direct-host cardinality | `RG-RIKEN-POLYMEROMICS` has `organization_id: ORG-RIKEN-TRIP` and no `institution_id`. |
| Host type | `ORG-RIKEN-TRIP` resolves to one reviewed v2 `organization` record. |
| Evidence-bearing relationship | The team records `belongs_to → ORG-RIKEN-TRIP` with its public RIKEN organization-page evidence. |
| No duplicate University | No University or generic Organization duplicate is created for TRIP. |

## Deliberate non-claims

1. The group-level RadonPy link does not establish that Yoshida is an
   individual maintainer, owner, or developer, or that every group member is a
   maintainer.
2. The linked repository is not assumed to be the only development venue or an
   exhaustive record of contributors and governance.
3. The team’s database, foundation-model, Sim2Real, autonomous-discovery, and
   recruitment descriptions do not become separate canonical nodes until each
   has a reviewed identity and precise relationship.
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
