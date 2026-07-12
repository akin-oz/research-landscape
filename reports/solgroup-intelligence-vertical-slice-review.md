# SOLgroup intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG4 enrichment of existing SOLgroup, Claudia Draxl,
Humboldt-Universität zu Berlin, FAIRmat, NOMAD, and computational-materials
cohort described in [the vertical-slice document](../docs/solgroup-intelligence-vertical-slice.md).

**Outcome:** this sixth Quality Gate 4 slice adds no new entity or relationship
because the group, PI, direct host, research area, FAIRmat, and NOMAD are
already canonical. It improves evidence quality and discoverability with
first-party group and official `exciting` project sources for research scope,
software development/open-source context, people, publications, student topics,
and partnership context.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Research programs and methods | SOLgroup home and code-development pages | Supports condensed-matter/computational-materials scope, spectroscopy, electron-phonon coupling, materials topics, and DFT/beyond-DFT methods. |
| Software development and open-source boundary | SOLgroup code-development page and official `exciting` page | Supports SOLgroup’s core-developer statement plus `exciting`’s GPL/open-source/source-management/test/tutorial surface. |
| People and career boundary | SOLgroup current/former-member surfaces | Supports displayed current people and dated former role categories, not a complete employment record or career outcome. |
| Publication and student-topic surface | SOLgroup publications and job-opportunities pages | Supports chronological current publications and listed student topics, not productivity metrics or a live opening. |
| Partnership/funding/collaboration boundary | SOLgroup GraFOx page | Supports main-partner and oxide-method context, not a full partner, funder, project-governance, or collaboration graph. |

All `SRC-*` values are record-local citations resolved in the SOLgroup record’s
Evidence table. Report-scoped `S126` through `S131` remain source-register keys
and are not used as canonical citation identifiers.

## Integrity review

| Check | Result |
| --- | --- |
| Canonical ownership | Group evidence remains in `RG-SOLGROUP`; no duplicate lab profile, people registry, project catalog, software catalog, or alumni entities are created. |
| Direct-host rule | Existing `institution_id: UNIVERSITY-HU-BERLIN` and matching `belongs_to` assertion remain unchanged and valid. |
| Software boundary | `exciting`/CELL development and `exciting`’s license/process evidence do not establish all individual roles or justify new unreviewed software nodes. |
| FAIRmat/NOMAD boundary | Existing ecosystem/software model and PI-scoped FAIRmat relation remain unchanged; group-context pages do not establish group-wide governance or maintenance. |
| Opportunity boundary | Student topics are discovery material, not a current opening, eligibility, funding, or supervision-capacity claim. |
| Career boundary | Former roles and time spans are not generalized into placement success, mentoring quality, applicant fit, or career outcomes. |

## Deliberate non-claims

1. `exciting`’s GPL license and public software practices do not establish the
   same attributes for CELL or every output associated with SOLgroup.
2. GraFOx and NOMAD/FAIRmat context do not establish a complete partner,
   industry, international-collaboration, grant, funding-programme, or
   governance graph.
3. Current and former public people pages do not establish a complete roster,
   headcount, compensation, or career-outcome record.
4. Student topics, theses, publication lists, and tutorials do not establish a
   current opportunity, individual supervision, mentoring quality, productivity,
   placement success, or applicant fit.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation is required after this
group enrichment. It must check schema shape and date formats, unique IDs,
relationship target/type compatibility, record-local source resolution,
direct-host target type, matching `belongs_to` assertions, exact-one host
cardinality, changed-document local links, whitespace, and the ADR 0006
University/Organization positive and negative branch cases. No persistent
validator, migration utility, generated view, or architecture change is
introduced before Quality Gate 6.
