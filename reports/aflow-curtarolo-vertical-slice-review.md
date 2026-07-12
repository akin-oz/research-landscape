# AFLOW–Curtarolo vertical slice review

**Review date:** 2026-07-12

**Scope:** the AFLOW–Curtarolo–Duke cohort in
[the vertical-slice document](../docs/aflow-curtarolo-vertical-slice.md).

**Outcome:** the slice adds five canonical entities and eight evidence-bearing
relationships. It distinguishes AFLOW's framework from the public web/data
ecosystem and uses the documented Curtarolo Group as the Duke research-unit
node for framework development.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| AFLOW framework and web/data ecosystem | AFLOW documentation and official source repository | Supports separate software and ecosystem records; GPL-3.0 is recorded only for the source repository. |
| Curtarolo Group and AFLOW development context | Curtarolo Materials Lab AFLOW, people, and group pages | Supports the Curtarolo Group identity, its Duke host, and group-level AFLOW framework development without an exclusivity claim. |
| Curtarolo leadership, affiliation, and research area | Duke faculty profile and Curtarolo Group pages | Supports current Duke affiliation, group-leadership context, and computational-materials normalization; it does not support an individual maintenance claim. |
| Duke location | Duke contact and Graduate School location pages | Supports normalized Durham, United States location. |

The canonical records use record-local `SRC-*` keys. Report-scoped `S06`,
`S07`, and `S32` identifiers remain in their existing reports and dossier and
were not reused as canonical evidence IDs.

## Classification and host review

| Check | Result |
| --- | --- |
| Framework vs. ecosystem | `SW-AFLOW` is the executable framework/source repository; `ECO-AFLOW` is the public web/data ecosystem. The GPL-3.0 value is not applied to the ecosystem. |
| Group identity | `RG-CURTAROLO-GROUP` uses the named group documented by the Duke materials pages; the Center remains contextual evidence rather than a duplicate group record. |
| Direct-host cardinality | `RG-CURTAROLO-GROUP` has only `institution_id: UNIVERSITY-DUKE`. |
| Host target type | `UNIVERSITY-DUKE` resolves to one reviewed v2 `university` record, with no duplicate Organization. |
| Evidence-bearing host relationship | The group records `belongs_to → UNIVERSITY-DUKE` with direct Duke-site evidence. |

## Deliberate non-claims

1. The evidence does not establish individual AFLOW development or maintenance
   by Stefano Curtarolo, so none is asserted.
2. The group-to-AFLOW relationship does not establish exclusive development,
   ownership, governance, or current maintenance.
3. The public AFLOW ecosystem is not reduced to one source repository, nor is
   its GPL-3.0 software license applied to databases or interfaces.
4. No opening, mentoring, admissions, funding, language, ranking, or applicant
   fit conclusion is drawn from the group materials.
5. AFLOW consortium members, projects, grants, publications, and additional
   people remain out of scope until their own identities and relationships are
   reviewed.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed with 22 entities
and 34 typed relationship assertions. It checked schema shape and date formats,
unique IDs, relationship target/type compatibility, record-local source
resolution, direct-host target type, matching `belongs_to` assertions,
exact-one host cardinality, changed-document local links, whitespace, and the
ADR 0006 University/Organization positive and negative branch cases. No generic
validator or architecture change is introduced in this Quality Gate 1 slice.
