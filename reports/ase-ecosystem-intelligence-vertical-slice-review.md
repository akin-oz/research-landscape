# ASE ecosystem-intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG3 enrichment of the existing ASE, CAMD, DTU, and 2017 ASE
publication cohort described in [the vertical-slice document](../docs/ase-ecosystem-intelligence-vertical-slice.md).

**Outcome:** this fifth Quality Gate 3 slice adds one canonical publication and
one evidence-bearing relationship. It makes the ASE ecosystem more intelligible
through source-backed modular calculator architecture, Python/CLI/GUI user
journey, GitLab contribution workflow, and community/support context, without
making unreviewed people or funding claims.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| ASE purpose and architecture | ASE documentation for the overview, calculators, and command-line tool | Supports Python atomistic-simulation purpose and the bounded `Atoms`/calculator, Python/CLI/GUI workflow. |
| Community and contribution workflow | ASE development and contact documentation; public GitLab repository | Supports GitLab, merge-request, review, testing, documentation, mailing-list, Matrix, forum, and issue routes. |
| Institution and group | Existing DTU CAMD evidence | Preserves the independently reviewed group-level ASE development and direct University host path. |
| Key technical reference | Warwick Research Archive ASE article record | Supports the 21 March 2017 date, DOI, and ASE technical subject. |
| Funding boundary | Published-paper and group evidence reviewed for this slice | No direct current programme identity plus safe ASE award evidence supports a typed funding relationship. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S94` through `S100` remain source-
register keys and are not used as canonical citation identifiers.

## Relationship review

| Check | Result |
| --- | --- |
| Publication software description | `PUB-ASE-2017` records `describes → SW-ASE` using the article's stated technical subject. |
| Author boundary | No `authored_by` relation is asserted because no article author identity has been independently reviewed as a canonical record. |
| Existing ecosystem role | The existing `ECO-ASE → connects → RG-DTU-CAMD` and group-level `develops → SW-ASE` assertions remain one-way and evidence-bearing; no inverse maintenance, employment, or governance edge is added. |
| No unsupported funding edge | No funding relation is fabricated from the historical publication's grant metadata, the DTU group, or source availability. |

## Contract limitations surfaced, not changed

1. `programming_language_ids` cannot be populated until a canonical Programming
   Language entity type and namespace are approved.
2. The schema has no canonical Community, calculator, external-code, API,
   dependency, database, workflow, package, or contributor-role entity type, so
   documented components are not converted into speculative graph nodes.
3. The documented `connects` predicate does not accept a Research Ecosystem
   target. Related ecosystems therefore remain cross-reference candidates rather
   than unsupported typed relations.
4. A paper author list and open contribution surface do not meet the review
   standard for an individual maintainer or contributor identity.

## Deliberate non-claims

1. GitLab, merge requests, source code, support channels, calculator interfaces,
   and CLI/GUI paths do not establish individual review, acceptance, mentorship,
   employment, governance, security posture, result quality, or support
   commitments.
2. The 2017 publication does not establish current versions, capabilities,
   affiliations, maintainer roles, funding, or a complete author graph.
3. CAMD's documented ASE development does not establish exclusive development,
   ownership, governance, or current maintenance.
4. No career placement, opening, supervision, admissions, language, ranking,
   or applicant-fit claim is made.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this cohort
was added. It checked schema shape and date formats, unique IDs, relationship
target/type compatibility (including `describes`), record-local source
resolution, direct-host target type, matching `belongs_to` assertions, exact-one
host cardinality, changed-document local links, whitespace, and the ADR 0006
University/Organization positive and negative branch cases. No persistent
validator, migration utility, generated view, or architecture change is
introduced before Quality Gate 6.
