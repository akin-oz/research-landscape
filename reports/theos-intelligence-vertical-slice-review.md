# THEOS intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG4 enrichment of the existing THEOS, Nicola Marzari, EPFL,
AiiDA, Materials Cloud, and computational-materials cohort described in [the
vertical-slice document](../docs/theos-intelligence-vertical-slice.md).

**Outcome:** this fifth Quality Gate 4 slice adds no new entity or relationship
because the group, PI, direct host, research area, shared AiiDA development,
and ecosystem connections are already canonical. It improves evidence quality
and discoverability with first-party teaching and project-discovery sources,
alongside an expanded reading of the existing first-party research source.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Research programs and methods | THEOS research overview | Supports first-principles/high-throughput scope, energy and information/communication materials, methodological work, and experimental-validation context. |
| Open-source ecosystem participation | THEOS research overview | Supports shared open-source infrastructure contribution, including existing AiiDA and Materials Cloud connections. |
| Education and mentorship boundary | THEOS research and teaching pages | Supports classes, schools, workshops, online materials, and a course with hands-on computational labs; does not establish individual supervision or mentoring quality. |
| Student-project discovery | THEOS bachelor/master project pages | Supports publicly linked discovery routes, not a specific current project, opening, eligibility, funding, or capacity. |
| People, funding, publication, and outcomes limits | All reviewed THEOS sources | Does not provide a stable accessible roster, group funding ledger, current publication inventory, or alumni-outcome evidence. |

All `SRC-*` values are record-local citations resolved in the THEOS record’s
Evidence table. Report-scoped `S124` and `S125` remain source-register keys and
are not used as canonical citation identifiers.

## Integrity review

| Check | Result |
| --- | --- |
| Canonical ownership | Group evidence remains in `RG-THEOS`; no duplicate lab profile, people registry, project catalog, or software catalog is created. |
| Direct-host rule | Existing `institution_id: UNIVERSITY-EPFL` and matching `belongs_to` assertion remain unchanged and valid. |
| Ecosystem boundary | Shared group contribution continues to support existing AiiDA and Materials Cloud connections without exclusive ownership, governance, or individual-maintainer claims. |
| Student-project boundary | Public discovery routes do not establish a live project, opening, eligibility, funding, or supervision capacity. |
| Education boundary | Courses and outreach show public learning activity, not an individual mentorship guarantee or measured outcome. |
| Missing-evidence boundary | Roster, funding, publication, collaborator, and alumni-outcome gaps remain explicit rather than inferred. |

## Deliberate non-claims

1. Additional named open-source infrastructures are not modeled as entities or
   group relations without distinct canonical identity and relationship review.
2. Methods, high-throughput calculation, and experimental-validation context do
   not establish hardware, allocation, service availability, named partners, or
   a complete collaboration graph.
3. Project pages do not establish a current vacancy, student eligibility,
   funding, admission, supervision capacity, or a project record.
4. Classes, workshops, schools, and online materials do not establish mentoring
   quality, placement success, applicant fit, or career outcomes.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation is required after this
group enrichment. It must check schema shape and date formats, unique IDs,
relationship target/type compatibility, record-local source resolution,
direct-host target type, matching `belongs_to` assertions, exact-one host
cardinality, changed-document local links, whitespace, and the ADR 0006
University/Organization positive and negative branch cases. No persistent
validator, migration utility, generated view, or architecture change is
introduced before Quality Gate 6.
