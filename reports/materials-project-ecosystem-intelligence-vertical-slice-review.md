# Materials Project ecosystem-intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG3 enrichment of the existing Materials Project, pymatgen,
Persson Group, LBNL, Kristin Persson, Shyue Ping Ong, Anubhav Jain, and 2013
pymatgen-publication cohort described in [the vertical-slice document](../docs/materials-project-ecosystem-intelligence-vertical-slice.md).

**Outcome:** this second Quality Gate 3 slice adds one canonical publication and
three evidence-bearing relationships. It makes the Materials Project software
ecosystem more intelligible through source-backed data-production architecture,
API user journey, public contribution context, and a citable technical
reference, while keeping current funding and stewardship claims bounded.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Materials Project purpose and architecture | Materials Project documentation for its introduction, workflows, builders, and API client | Supports the public discovery purpose and the bounded workflow → task data → builder → API architecture. |
| Community, contribution, and user journey | Materials Project documentation and project-owned pymatgen site/repository | Supports public documentation edits, API client/account path, install/examples, issues, pull requests, forums, and discussions. |
| Institutions, group, and people | Existing LBNL, Persson Group, NUS, and Berkeley Lab evidence | Preserves the separately reviewed LBNL, group, founder/director, core-contributor, associate-director, and lead-developer facts without broadening their scope. |
| Key technical reference | UC Berkeley eScholarship publication record | Supports the 1 February 2013 date, DOI, two already reviewed authors, and pymatgen description. |
| Funding boundary | Materials Project documentation introduction | DOE origin is documented, but no reviewed funding-programme identity plus direct award evidence supports a typed funding relationship. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S77` through `S82` remain source-
register keys and are not used as canonical citation identifiers.

## Relationship review

| Check | Result |
| --- | --- |
| Publication authorship | `PUB-PYMATGEN-2013` records `authored_by → PI-SHYUE-PING-ONG` and `authored_by → PI-ANUBHAV-JAIN` using the paper author list. |
| Publication software description | `PUB-PYMATGEN-2013` records `describes → SW-PYMATGEN` using the article's stated technical subject. |
| Existing ecosystem roles | Materials Project's existing group, organization, and PI connections remain one-way, evidence-bearing source relations; no inverse maintenance, employment, or governance relation is added. |
| No unsupported funding edge | The DOE-origin statement remains source-backed context rather than a fabricated current or historical funding-programme relationship. |

## Contract limitations surfaced, not changed

1. `programming_language_ids` cannot be populated until a canonical Programming
   Language entity type and namespace are approved.
2. The schema has no canonical Community, API endpoint, data product,
   dependency, workflow, or package entity type, so those documented components
   are not converted into speculative graph nodes.
3. The documented `connects` predicate does not accept a Research Ecosystem
   target. Related ecosystems therefore remain cross-reference candidates rather
   than unsupported typed relations.
4. A DOE-origin statement is insufficient for a Funding Programme edge without
   a reviewed programme identity and direct support evidence.

## Deliberate non-claims

1. Public repository and documentation channels do not establish individual
   review, acceptance, mentorship, employment, or project governance.
2. The 2013 publication does not establish current versions, capabilities,
   affiliations, maintainer roles, or a complete author graph.
3. Documentation of an account/API-key route does not promise universal access,
   stable endpoints, or particular data availability.
4. No career placement, opening, supervision, admissions, language, ranking,
   or applicant-fit claim is made.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this cohort
was added. It checked schema shape and date formats, unique IDs, relationship
target/type compatibility (including `authored_by` and `describes`), record-
local source resolution, direct-host target type, matching `belongs_to`
assertions, exact-one host cardinality, changed-document local links,
whitespace, and the ADR 0006 University/Organization positive and negative
branch cases. No persistent validator, migration utility, generated view, or
architecture change is introduced before Quality Gate 6.
