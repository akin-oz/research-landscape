# Materials Cloud ecosystem-intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG3 enrichment of the existing Materials Cloud, aiida-core,
THEOS, Nicola Marzari, Giovanni Pizzi, NCCR MARVEL, and 2020 platform-
publication cohort described in [the vertical-slice document](../docs/materials-cloud-ecosystem-intelligence-vertical-slice.md).

**Outcome:** this seventh Quality Gate 3 slice adds one canonical publication
and two evidence-bearing relationships. It makes the Materials Cloud ecosystem
more intelligible through source-backed research-cycle, moderated data-
contribution, Archive-architecture, and technical-publication context, while
retaining the existing historical funding limit.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Materials Cloud purpose and journey | Current Materials Cloud landing page and Archive pages | Supports Learn/Work/Discover/Explore/Archive journey, data sharing, research services, and DOI-based archival workflow. |
| Archive architecture and contribution | Archive about and submission pages | Supports current InvenioRDM context, account-based upload, moderation, DOI publication, record versioning, and integration routes. |
| Institutions, people, and software | Existing Materials Cloud, THEOS, AiiDA, and PI evidence | Preserves separately reviewed AiiDA, THEOS, project-leader, and group contribution facts without expanding to a maintenance roster. |
| Key technical reference | Scientific Data Materials Cloud article | Supports the 8 September 2020 date, DOI, Nicola Marzari/Giovanni Pizzi authorship, and platform scope. |
| Funding boundary | Existing NCCR MARVEL connection and funding record | Preserves historical 2021 development context and rejects any current funding inference after the cited phase. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S107` through `S111` remain source-
register keys and are not used as canonical citation identifiers.

## Relationship review

| Check | Result |
| --- | --- |
| Publication authorship | `PUB-MATERIALS-CLOUD-2020` records `authored_by → PI-NICOLA-MARZARI` and `authored_by → PI-GIOVANNI-PIZZI` using the article author list. |
| Publication subject boundary | The paper describes Materials Cloud, but no `describes` edge is added because its target contract excludes Research Ecosystem. |
| Existing ecosystem roles | Materials Cloud’s existing AiiDA, THEOS, PI, and historical NCCR MARVEL links remain one-way and evidence-bearing; no inverse maintenance, employment, or governance edge is added. |
| Bounded data contribution | Archive upload/moderation/DOI routes are represented in canonical prose, not falsely converted into individual contributor, review-right, or software-development relations. |

## Contract limitations surfaced, not changed

1. `programming_language_ids` cannot be populated until a canonical Programming
   Language entity type and namespace are approved.
2. The schema has no canonical Community, archive component, moderator,
   application, API endpoint, dependency, database, workflow, or package entity
   type, so documented components are not converted into speculative graph
   nodes.
3. The `describes` predicate allows Project and Research Software targets, not
   a Research Ecosystem target. The platform publication's subject stays in
   evidence-backed prose rather than an unsupported typed edge.
4. A moderated data-deposition workflow is not a code-contribution, review,
   employment, or mentoring contract.

## Deliberate non-claims

1. Archive implementation, moderation, DOI, and hosted-resource information do
   not establish individual review, acceptance, mentorship, employment,
   governance, security posture, result quality, or support commitments.
2. The 2020 publication does not establish current versions, capabilities,
   affiliations, maintainer roles, or a complete author graph.
3. The historical NCCR MARVEL relation does not prove current funding or
   eligibility.
4. No career placement, opening, supervision, admissions, language, ranking,
   or applicant-fit claim is made.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this cohort
was added. It checked schema shape and date formats, unique IDs, relationship
target/type compatibility (including `authored_by`), record-local source
resolution, direct-host target type, matching `belongs_to` assertions, exact-one
host cardinality, changed-document local links, whitespace, and the ADR 0006
University/Organization positive and negative branch cases. No persistent
validator, migration utility, generated view, or architecture change is
introduced before Quality Gate 6.
