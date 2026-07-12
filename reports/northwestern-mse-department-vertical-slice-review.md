# Northwestern MSE department vertical slice review

**Review date:** 2026-07-12

**Scope:** the reviewed Northwestern MSE / Wolverton Group administrative-
context cohort in [the vertical-slice document](../docs/northwestern-mse-department-vertical-slice.md).

**Outcome:** this third Quality Gate 2 slice adds one canonical entity and
three evidence-bearing relationships. It exercises the Department entity type,
preserves the Wolverton Group's one direct University host, and records a
separate, limited Department context.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Department identity and University endpoint | Northwestern MSE overview | Supports the Department of Materials Science and Engineering at Northwestern University. |
| Department research-area context | Northwestern MSE Materials Theory, Computation, & Design page | Supports computational and theoretical materials-science work at the Department. |
| Group Department context | Northwestern Engineering Chris Wolverton profile | Supports his Materials Science and Engineering appointment, linked Wolverton Research Group site, and group research statement. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S64` through `S66` remain source-
register keys and are not used as canonical citation identifiers.

## ADR 0006 host review

| Check | Result |
| --- | --- |
| Direct-host cardinality | `RG-WOLVERTON-GROUP` retains `institution_id: UNIVERSITY-NORTHWESTERN` and no `organization_id`. |
| Host type | `UNIVERSITY-NORTHWESTERN` resolves to a reviewed v2 `university` record. |
| Direct-host assertion | The existing group `belongs_to → UNIVERSITY-NORTHWESTERN` assertion remains present and is the one matching direct-host assertion. |
| Department context | `department_id: DEPARTMENT-NORTHWESTERN-MSE` and the separate `belongs_to` assertion are administrative context only, as ADR 0006 permits. |
| No duplicate Organization | No generic Organization duplicate is created for Northwestern University or its Department. |

## Deliberate non-claims

1. The Department relation does not make it a second direct host for the group
   or establish that every group member has the same Department affiliation.
2. The Department pages do not establish admissions availability, funding,
   mentor quality, supervision capacity, current openings, or applicant fit.
3. No faculty, programme, degree, laboratory, centre, student, or publication
   roster is created from the Department's navigation or descriptive pages.
4. The Department's computational-materials context does not establish that
   every department group develops OQMD or uses the same software stack.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this
cohort was added. It checked schema shape and date formats, unique IDs,
relationship target/type compatibility, record-local source resolution,
direct-host target type, matching `belongs_to` assertions, exact-one host
cardinality, changed-document local links, whitespace, and the ADR 0006
University/Organization positive and negative branch cases. No persistent
validator, migration utility, generated view, or architecture change is
introduced before Quality Gate 6.
