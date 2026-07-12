# Hacking Materials–Berkeley Lab vertical slice review

**Review date:** 2026-07-12

**Scope:** the reviewed Hacking Materials–Berkeley Lab cohort in
[the vertical-slice document](../docs/hacking-materials-vertical-slice.md).

**Outcome:** the slice adds two canonical entities and six evidence-bearing
relationships, including one narrowly sourced extension of the existing
Materials Project ecosystem. It exercises the accepted Organization-host branch
of ADR 0006 without introducing a duplicate host, project, or software record.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Jain's Berkeley Lab affiliation and Materials Project role | Berkeley Lab Energy Technologies Area profile | Supports the PI’s Berkeley Lab affiliation, research-methods description, and associate-director connection to Materials Project. |
| Hacking Materials identity, leadership, host, and methods | Hacking Materials Berkeley Lab group page | Supports the named research group, Jain's leadership, Berkeley Lab host, and computational-materials/theory/HPC/AI scope. |
| Country and controlled area endpoints | Existing LBNL, United States, and Computational Materials Science records | Reuses already reviewed endpoints; this slice adds no duplicate country, host, or topical entity. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S29` and `S38` remain source-register
keys and are not used as canonical citation identifiers.

## ADR 0006 host review

| Check | Result |
| --- | --- |
| Direct-host cardinality | `RG-HACKING-MATERIALS` has `organization_id: ORG-LBNL` and no `institution_id`. |
| Host type | `ORG-LBNL` resolves to one reviewed v2 `organization` record. |
| Evidence-bearing relationship | The group records `belongs_to → ORG-LBNL` with its public Berkeley Lab group-page evidence. |
| No duplicate University | No University or generic Organization duplicate is created for Berkeley Lab. |

## Deliberate non-claims

1. Jain’s associate-director role does not establish group-wide Materials
   Project governance, ownership, software development, or maintenance.
2. FORUM-AI is mentioned by the Berkeley Lab profile but is not modeled as a
   project or funding programme until its identity and required relationships
   receive their own review.
3. Theory, high-performance computing, and AI methods do not imply a complete
   inventory of software, datasets, collaborators, applications, or personnel.
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
