# DTU CAMD intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG4 enrichment of the existing DTU CAMD, DTU, ASE, and
computational-materials cohort described in [the vertical-slice
document](../docs/dtu-camd-intelligence-vertical-slice.md).

**Outcome:** this seventh Quality Gate 4 slice adds no new entity or relationship
because the group, direct host, research area, ASE, and ASE ecosystem connection
are already canonical. It improves evidence quality and discoverability with
first-party sources for section leadership, CAMPOS/ASE software, open-source
context, research programs, bounded project routes, and sub-group funding
context.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Section scope and people boundary | DTU CAMD overview | Supports CAMD’s application-oriented atomic-scale scope and four named sub-group leaders, not a full roster. |
| Software and open-source context | DTU CAMD software page | Supports CAMPOS, Python interfaces, shared ASE tools, GNU GPL, and public development-participation statement. |
| Research programs and ASE boundary | Atomic-scale Materials Design page | Supports ASE/GPAW, databases, ML, optimization, and uncertainty context, not a complete software/project inventory. |
| Funding and project-route boundary | Computational Quantum Materials page | Supports one sub-group’s VILLUM project and BSc/MSc project routes, not CAMD-wide funding, availability, or capacity. |
| Publication, mentoring, and career limits | Reviewed CAMD surfaces | Does not yield a stable section publication inventory, individual mentoring evidence, or career outcomes. |

All `SRC-*` values are record-local citations resolved in the DTU CAMD record’s
Evidence table. Report-scoped `S132` through `S134` remain source-register
keys and are not used as canonical citation identifiers.

## Integrity review

| Check | Result |
| --- | --- |
| Canonical ownership | Group evidence remains in `RG-DTU-CAMD`; no duplicate section, people registry, project catalog, or software catalog is created. |
| Direct-host rule | Existing `institution_id: UNIVERSITY-DTU` and matching `belongs_to` assertion remain unchanged and valid. |
| Software boundary | Existing shared ASE-development relation remains unchanged; CAMPOS/GPAW/databases are evidence context, not new unreviewed nodes or individual roles. |
| Funding boundary | The VILLUM statement is attributed only to the named Computational Quantum Materials sub-group and not expanded into a CAMD funding relation. |
| Opportunity boundary | BSc/MSc project routes are discovery material, not current openings, eligibility, funding, or supervision-capacity claims. |
| Missing-evidence boundary | Roster, hardware, full publication, collaboration, mentoring, and career gaps remain explicit rather than inferred. |

## Deliberate non-claims

1. Python-interface and GNU GPL statements about CAMPOS do not establish a
   group-wide language policy, individual coding role, or every resource’s
   license and governance.
2. A named VILLUM project does not establish CAMD-wide funding, an active award
   relation, award amount for the section, or group capacity.
3. Named software, databases, research methods, and project routes do not
   establish canonical software/project entities, a hardware allocation, or a
   complete collaboration graph.
4. Project routes and public leadership information do not establish live
   opportunities, individual supervision, mentoring quality, placement success,
   applicant fit, or career outcomes.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this group
enrichment. It checked schema shape and date formats, unique IDs, relationship
target/type compatibility, record-local source resolution, direct-host target
type, matching `belongs_to` assertions, exact-one host cardinality,
changed-document local links, whitespace, and the ADR 0006
University/Organization positive and negative branch cases. The corpus contains
67 v2 entities and 116 relationship assertions. No persistent validator,
migration utility, generated view, or architecture change is introduced before
Quality Gate 6.
