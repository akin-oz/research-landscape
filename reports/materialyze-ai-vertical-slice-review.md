# Materialyze.AI–NUS vertical slice review

**Review date:** 2026-07-12

**Scope:** the current NUS-hosted Materialyze.AI cohort in
[the vertical-slice document](../docs/materialyze-ai-vertical-slice.md).

**Outcome:** the slice adds five canonical entities and connects them to the
existing `pymatgen` and Materials Project records through eight evidence-bearing
relationships. It corrects a stale UCSD-oriented legacy context without
rewriting that dossier as a second canonical profile.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Current affiliation and lab leadership | NUS faculty profile and Materialyze.AI team page | Supports the 2026– NUS appointment and PI leadership of the NUS-hosted Materialyze.AI Lab. |
| Pymatgen stewardship | NUS faculty profile and pymatgen development team | Supports a PI-level founder/lead-developer relationship without asserting an exhaustive maintainer roster. |
| Materials Project connection | NUS faculty profile | Supports a PI-level core-contributor connection without an NUS ownership claim. |
| Materials-informatics focus | NUS faculty profile | Supports normalization to the new Materials Informatics controlled area. |
| NUS and Singapore location | NUS contact page and ISO 3166 | Supports the University and country endpoints. |

The materialyze.ai team page records both the 2026– NUS appointment and
2013–2025 UCSD appointments. The old UCSD-oriented dossier is therefore kept
as dated context, with its current-fact boundary made explicit; no historical
UCSD affiliation is carried into the vNext PI record.

## Classification and host review

| Check | Result |
| --- | --- |
| Direct-host cardinality | `RG-MATERIALYZE-AI` has only `institution_id: UNIVERSITY-NUS`. |
| Host target type | `UNIVERSITY-NUS` resolves to one reviewed v2 `university` record, with no duplicate Organization. |
| Evidence-bearing host relationship | The lab records `belongs_to → UNIVERSITY-NUS` with current NUS and Materialyze.AI evidence. |
| Individual versus group stewardship | Only `PI-SHYUE-PING-ONG` is linked to `SW-PYMATGEN`; the evidence does not establish lab-wide stewardship. |
| Existing ecosystem extension | The Materials Project node is extended by one directly sourced `core-contributor` relation; its existing identities and boundaries remain intact. |

## Deliberate non-claims

1. The NUS evidence does not establish that Materialyze.AI as a group develops,
   maintains, or owns pymatgen, so no group-to-software edge is asserted.
2. The current NUS affiliation does not erase the historical UCSD context; it
   simply prevents that historical context from being repeated as current fact.
3. No NUS ownership, governance, exclusive stewardship, or hosting claim is
   made for pymatgen or Materials Project.
4. No current opening, mentoring, admissions, funding, language, ranking, or
   applicant-fit claim is made.
5. Department, project, funding-programme, publication, and additional-person
   identities remain out of scope until separately reviewed.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed with 27 entities
and 42 typed relationship assertions. It checked schema shape and date formats,
unique IDs, relationship target/type compatibility, record-local source
resolution, direct-host target type, matching `belongs_to` assertions,
exact-one host cardinality, changed-document local links, whitespace, and the
ADR 0006 University/Organization positive and negative branch cases. No generic
validator or architecture change is introduced in this Quality Gate 1 slice.
