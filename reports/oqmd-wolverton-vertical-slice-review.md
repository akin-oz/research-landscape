# OQMD–Wolverton vertical slice review

**Review date:** 2026-07-12

**Scope:** the OQMD–Wolverton–Northwestern cohort in
[the vertical-slice document](../docs/oqmd-wolverton-vertical-slice.md).

**Outcome:** the slice adds four canonical entities and seven evidence-bearing
relationships. It validates the accepted University-host branch of ADR 0006
against real reviewed records without creating a duplicate Organization or
collapsing OQMD into an unsupported software entity.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| OQMD and Wolverton Group connection | OQMD documentation overview and group overview | Supports an ecosystem-to-group developer/maintainer connection. |
| Wolverton leadership and computational scope | Group members page and Northwestern faculty profile | Supports PI leadership, University affiliation, and computational-materials area links. |
| Northwestern location | Northwestern University contact page | Supports University location normalization to the existing United States country record. |

The canonical records use record-local `SRC-*` keys. Report-scoped `S04`,
`S05`, and `S31` identifiers remain in their existing reports and dossiers and
were not reused as canonical evidence IDs.

## ADR 0006 University-host review

| Check | Result |
| --- | --- |
| Direct-host cardinality | `RG-WOLVERTON-GROUP` has only `institution_id: UNIVERSITY-NORTHWESTERN`. |
| Host type | The referenced record is one reviewed v2 `university`, not an Organization. |
| Evidence-bearing relationship | The group records `belongs_to → UNIVERSITY-NORTHWESTERN` with direct OQMD documentation evidence. |
| No duplicate identity | No `ORG-NORTHWESTERN` record or redundant Department is added. |

## Deliberate non-claims

1. The group-level OQMD development and maintenance evidence is not attributed
   to Chris Wolverton individually.
2. No direct OQMD-to-PI relationship is manufactured from the group path.
3. OQMD implementation, contributor-roster, data-volume, and interface details
   remain out of scope until separately reviewed.
4. No mentoring, opportunity, admissions, funding, language, or ranking claim
   is derived from the documented research relationship.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed with 17 entities
and 26 typed relationship assertions. It checked schema shape and date formats,
unique IDs, relationship target/type compatibility, record-local source
resolution, direct-host target type, matching `belongs_to` assertions,
exact-one host cardinality, changed-document local links, and whitespace. The
check also exercised both direct-host branches and negative cases for
both/neither reviewed host fields.

No generic validator or architecture change is introduced: these are bounded
QG1 review checks pending a later automation quality gate.
