# ASE–DTU CAMD vertical slice review

**Review date:** 2026-07-12

**Scope:** the reviewed ASE / DTU CAMD cohort in
[the vertical-slice document](../docs/ase-dtu-vertical-slice.md).

**Outcome:** the slice adds five canonical entities and six evidence-bearing
relationships. It exercises the accepted University-host branch of ADR 0006,
separates ASE software from its ecosystem node, and records only the public,
group-level CAMD ASE-development connection.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| ASE identity and license | ASE documentation and About page | Supports ASE as Python tools and modules for atomistic simulations and GNU LGPL version 2.1 or later licensing. |
| CAMD identity, research scope, and ASE connection | DTU Physics CAMD and Atomic-scale Materials Design pages | Supports CAMD's DTU Physics identity, Computational Materials Science context, and public group-level development of ASE. |
| DTU identity and location | DTU Organization and Contact pages | Supports DTU as a self-governing university and its Kongens Lyngby, Denmark location endpoint. |
| ASE ecosystem link | ASE documentation and CAMD research page | Supports an ASE ecosystem page and the bounded connection to a group that publicly identifies ASE development. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S53` through `S56` remain source-
register keys and are not used as canonical citation identifiers.

## ADR 0006 host review

| Check | Result |
| --- | --- |
| Direct-host cardinality | `RG-DTU-CAMD` has `institution_id: UNIVERSITY-DTU` and no `organization_id`. |
| Host type | `UNIVERSITY-DTU` resolves to one reviewed v2 `university` record. |
| Evidence-bearing relationship | CAMD records `belongs_to → UNIVERSITY-DTU` with its public DTU group-overview evidence. |
| No duplicate Organization | No generic Organization duplicate is created for DTU. |

## Deliberate non-claims

1. The group-level ASE development relation does not establish exclusive
   ownership, governance, maintenance, or an exhaustive CAMD contributor list.
2. The ASE ecosystem node does not establish the full ecosystem membership,
   governance, funding, or every linked software component.
3. GPAW and other projects named alongside ASE are not added merely because
   they are linked in a CAMD research description.
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
