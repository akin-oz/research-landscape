# Wolverton Research Group intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG4 enrichment of the existing Wolverton Research Group, Chris
Wolverton, Northwestern, OQMD, and computational-materials cohort described in
[the vertical-slice document](../docs/wolverton-group-intelligence-vertical-slice.md).

**Outcome:** this second Quality Gate 4 slice adds no new entity or relationship
because the group, PI, direct host, Department context, research area, and OQMD
connection are already canonical. It improves evidence quality and
discoverability with three new first-party group sources for current research,
OQMD stewardship, publication/news activity, visible role categories, and
selected public alumni outcomes.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Research and technical methods | Wolverton Group home and research pages | Supports energy/sustainability, DFT/ML/high-throughput/multiscale themes and OQMD stewardship. |
| People roles and alumni | Wolverton Group members page | Supports current postdoctoral/graduate/master/undergraduate/alumni categories, role summaries, and selected stated alumni destinations. |
| Publication, qualification, and award surface | Wolverton Group news page | Supports dated paper, joining, qualification, thesis, fellowship, hiring, and award announcements. |
| Software and infrastructure boundary | OQMD and group pages | Supports group-level OQMD development/maintenance plus computational methods, not backend-software, code governance, or hardware claims. |
| Funding, collaboration, and mentorship limits | All reviewed group sources | Does not establish a group funding ledger, partner roster, industry collaboration inventory, or mentoring-process evidence. |

All `SRC-*` values are record-local citations resolved in the Wolverton Group
record’s Evidence table. Report-scoped `S116` through `S118` remain source-
register keys and are not used as canonical citation identifiers.

## Integrity review

| Check | Result |
| --- | --- |
| Canonical ownership | Group evidence remains in `RG-WOLVERTON-GROUP`; no duplicate lab profile, people registry, or alumni entities are created. |
| Direct-host rule | Existing `institution_id: UNIVERSITY-NORTHWESTERN` and matching `belongs_to` assertion remain unchanged and valid. |
| Department boundary | Existing Northwestern MSE link remains administrative context, not a second direct host. |
| OQMD boundary | Group-level OQMD stewardship does not establish a backend-software entity, individual maintenance, or ownership claim. |
| Mentorship and opportunity boundary | Student milestones and the welcome statement are not generalized into mentorship quality, admissions, hiring, or supervision-capacity claims. |
| Career-outcome boundary | Selected alumni positions are examples of publicly stated outcomes, not a rate, causal claim, or guarantee. |

## Deliberate non-claims

1. The public people page is not treated as a complete current roster,
   employment record, or basis for bulk person-entity creation.
2. Research methods and OQMD stewardship do not establish full software
   governance, open-source activity, individual code roles, hardware capacity,
   or service availability.
3. A single student project mentioning a MURI does not establish group funding
   or justify a funding-program relationship.
4. News, qualifications, awards, and alumni outcomes do not establish group
   mentorship quality, placement success, applicant fit, or current openings.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this group
enrichment. It checked schema shape and date formats, unique IDs, relationship
target/type compatibility, record-local source resolution, direct-host target
type, matching `belongs_to` assertions, exact-one host cardinality,
changed-document local links, whitespace, and the ADR 0006 University/
Organization positive and negative branch cases. No persistent validator,
migration utility, generated view, or architecture change is introduced before
Quality Gate 6.
