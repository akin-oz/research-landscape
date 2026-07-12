# NOMAD ecosystem-intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG3 enrichment of the existing FAIRmat, NOMAD, Claudia Draxl,
SOLgroup, historic NoMaD Laboratory CoE, Horizon 2020, and FAIRmat Users Meeting
cohort described in [the vertical-slice document](../docs/nomad-ecosystem-intelligence-vertical-slice.md).

**Outcome:** this third Quality Gate 3 slice adds one canonical publication and
two evidence-bearing relationships. It makes the FAIRmat–NOMAD ecosystem more
intelligible through source-backed platform architecture, data-management and
extension journeys, public contribution context, and a citable technical
reference, while preserving strict boundaries around current funding and people
claims.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| NOMAD purpose and architecture | NOMAD documentation introduction, architecture, and how-to guides | Supports materials-science data-management purpose and the bounded app/worker, API/GUI, processing, extension, and deployment context. |
| Community, contribution, and user journey | Official NOMAD how-to and contribution guides; existing FAIRmat Users Meeting record | Supports GUI/API use, upload/publication, plugins, Oasis hosting, core-development routes, public GitHub issues, and dated training/community context. |
| FAIRmat relationship and funding boundary | FAIRmat consortium, overview, and story pages | Supports FAIRmat operation and further development of the NOMAD Laboratory plus an NFDI consortium statement, without inventing a typed current-funding edge. |
| Key technical reference | JOSS NOMAD article | Supports the 15 October 2023 date, DOI, Claudia Draxl authorship, and NOMAD technical subject. |
| Historical project funding | Existing CORDIS and NOMAD CoE evidence | Preserves the separately reviewed, dated Horizon 2020 → NoMaD Laboratory CoE → NOMAD route. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S83` through `S88` remain source-
register keys and are not used as canonical citation identifiers.

## Relationship review

| Check | Result |
| --- | --- |
| Publication authorship | `PUB-NOMAD-JOSS-2023` records `authored_by → PI-CLAUDIA-DRAXL` using the JOSS author list. |
| Publication software description | `PUB-NOMAD-JOSS-2023` records `describes → SW-NOMAD` using the article's stated technical subject. |
| Existing ecosystem roles | FAIRmat's existing `includes → SW-NOMAD`, spokesperson, and Users Meeting connections remain one-way and evidence-bearing; no inverse maintenance, employment, or governance edge is added. |
| No unsupported NFDI funding edge | The FAIRmat consortium’s NFDI funding statement remains source-backed context because the graph lacks a reviewed NFDI funder/programme pair and direct edge contract. |

## Contract limitations surfaced, not changed

1. `programming_language_ids` cannot be populated until a canonical Programming
   Language entity type and namespace are approved.
2. The schema has no canonical Community, dependency, API endpoint, service,
   database, workflow, package, parser, plugin, or Oasis entity type, so these
   documented components are not converted into speculative graph nodes.
3. The documented `connects` predicate does not accept a Research Ecosystem
   target. Related ecosystems therefore remain cross-reference candidates rather
   than unsupported typed relations.
4. A statement that FAIRmat is funded as an NFDI consortium is not sufficient
   for a Funding Programme edge without reviewed funder/programme identities and
   direct support evidence.

## Deliberate non-claims

1. Public GitHub issues, synchronized GitLab development, plugins, Oasis setup,
   and technical guides do not establish individual review, acceptance,
   mentorship, employment, project governance, or a security posture.
2. The 2023 publication does not establish current versions, capabilities,
   affiliations, maintainer roles, or a complete author graph.
3. The historical H2020 project does not prove current NOMAD or FAIRmat funding.
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
