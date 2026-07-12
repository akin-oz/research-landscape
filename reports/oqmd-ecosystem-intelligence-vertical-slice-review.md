# OQMD ecosystem-intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG3 enrichment of the existing OQMD, Wolverton Research Group,
Chris Wolverton, Northwestern, and 2015 OQMD-publication cohort described in
[the vertical-slice document](../docs/oqmd-ecosystem-intelligence-vertical-slice.md).

**Outcome:** this sixth Quality Gate 3 slice adds one canonical publication and
one evidence-bearing relationship. It makes the OQMD data ecosystem more
intelligible through source-backed public data access, download, provenance,
and citation context, while preserving its ecosystem-only classification and
the absence of an evidenced public code-contribution route.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| OQMD purpose and data-access architecture | OQMD overview, API, download, and structure-source documentation | Supports high-throughput DFT database purpose, public REST/OPTIMADE query path, full download route, and documented data-source context. |
| Public user and citation journey | OQMD API, download, and publications pages | Supports query/filter/download, optional query package, full snapshots, CC-BY data context, and cited-reference route. |
| Institution and group | Existing OQMD and Wolverton evidence | Preserves the independently reviewed developer-and-maintainer group relation and Northwestern/PI routes. |
| Key technical reference | Nature npj Computational Materials OQMD article | Supports the 11 December 2015 date, DOI, Chris Wolverton authorship, and database subject. |
| Contribution and funding boundary | Official pages reviewed for this slice | Does not support a public code-contribution workflow, individual maintainer roster, or safe current funding relationship. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S101` through `S106` remain source-
register keys and are not used as canonical citation identifiers.

## Relationship review

| Check | Result |
| --- | --- |
| Publication authorship | `PUB-OQMD-2015` records `authored_by → PI-CHRIS-WOLVERTON` using the article author list. |
| Publication subject boundary | The source identifies OQMD as the article subject, but no `describes` edge is added: its target contract excludes Research Ecosystem. |
| Existing ecosystem role | The existing `ECO-OQMD → connects → RG-WOLVERTON-GROUP` developer-and-maintainer assertion remains one-way and evidence-bearing; no individual maintenance or inverse edge is added. |
| No unsupported contribution/funding edge | REST, download, and contact routes are not turned into contribution, review, funding, governance, or support commitments. |

## Contract limitations surfaced, not changed

1. `programming_language_ids` cannot be populated until a canonical Programming
   Language entity type and namespace are approved.
2. The schema has no canonical Community, backend software, API endpoint,
   database, query package, dependency, workflow, or contributor-role entity
   type, so documented components are not converted into speculative graph
   nodes.
3. The `describes` predicate allows Project and Research Software targets, not a
   Research Ecosystem target. The OQMD publication's subject stays in evidence-
   backed prose rather than an unsupported typed edge.
4. Public data access and an email contact route do not prove a source-
   contribution, code-review, or acceptance process.

## Deliberate non-claims

1. REST/OPTIMADE endpoints, downloads, an optional query package, and public
   data license do not establish a backend software implementation, API
   stability, result quality, support commitment, security posture, governance,
   or individual maintenance role.
2. The 2015 publication does not establish current database content, versions,
   capabilities, affiliations, funding, maintainer roles, or a complete author
   graph.
3. Wolverton Group development and maintenance does not establish exclusive
   ownership or maintenance by each group member or its PI.
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
