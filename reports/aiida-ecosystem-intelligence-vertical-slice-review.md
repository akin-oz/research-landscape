# AiiDA ecosystem-intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG3 enrichment of the existing AiiDA ecosystem, aiida-core,
PSI/MSD, THEOS, NCCR MARVEL, Giovanni Pizzi, and AiiDA 1.0 cohort described in
[the vertical-slice document](../docs/aiida-ecosystem-intelligence-vertical-slice.md).

**Outcome:** this first Quality Gate 3 slice adds one canonical publication and
three evidence-bearing relationships. It makes the AiiDA software ecosystem
more intelligible through source-backed architecture, funding, community,
contribution, user-journey, and technical-publication context, while preserving
strict boundaries around unverified current roles and missing entity types.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| AiiDA purpose and architecture | AiiDA documentation and official ecosystem page | Supports Python workflow infrastructure, provenance, workflow engine, plugin architecture, compute interfaces, and upstream user journey. |
| Community and contribution workflow | Project-owned aiida-core repository and plugin registry | Supports public source, issue/PR/discussion/contributor surfaces and community extension categories. |
| Institutions and groups | AiiDA team page, PSI MSD page, THEOS research page | Supports bounded PSI/MSD, THEOS, and Pizzi connections without an exhaustive roster. |
| Funding context | AiiDA acknowledgements | Supports a bounded AiiDA-to-NCCR MARVEL support relationship. |
| Key technical reference | Scientific Data AiiDA 1.0 publication | Supports the DOI, 2020 date, Pizzi authorship, and AiiDA software description. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S71` through `S76` remain source-
register keys and are not used as canonical citation identifiers.

## Relationship review

| Check | Result |
| --- | --- |
| Funding connection | `ECO-AIIDA` records `connects → FUND-NCCR-MARVEL` with official acknowledgement evidence and a limitation against current/exclusive-funding inference. |
| Publication authorship | `PUB-AIIDA-1-0` records `authored_by → PI-GIOVANNI-PIZZI` using the publication author list. |
| Publication software description | `PUB-AIIDA-1-0` records `describes → SW-AIIDA-CORE` using the article’s technical subject. |
| Existing ecosystem roles | The PSI/MSD, THEOS, and Pizzi connections remain one-way, evidence-bearing source relations; no inverse maintenance relation is added. |
| No unsupported ecosystem edge | Materials Cloud remains a source-backed cross-reference rather than a fabricated `ECO-AIIDA → ECO-MATERIALS-CLOUD` graph assertion. |

## Contract limitations surfaced, not changed

1. `programming_language_ids` cannot be populated until a canonical Programming
   Language entity type and namespace are approved.
2. The schema has no canonical Community or dependency entity type, so plugins,
   learning assets, schedulers, Materials Cloud, and AiiDAlab are not converted
   into speculative graph nodes.
3. The documented `connects` predicate does not accept a Research Ecosystem
   target. Related ecosystems are therefore cross-referenced in canonical prose
   rather than assigned an unsupported typed relation.
4. The AiiDA team and publication author list do not prove a complete current
   maintainer or contributor roster. Only Pizzi's already-reviewed identity is
   linked to the publication, and no maintainer field is populated.

## Deliberate non-claims

1. Public repository contribution channels do not establish individual
   review, acceptance, mentorship, employment, or project governance.
2. NCCR MARVEL acknowledgement does not prove a current award, exclusive
   funding, or support for every AiiDA component.
3. The 2020 publication does not establish current versions, capabilities,
   affiliations, maintainer roles, or a complete author graph.
4. No career placement, opening, supervision, admissions, language, ranking,
   or applicant-fit claim is made.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this
cohort was added. It checked schema shape and date formats, unique IDs,
relationship target/type compatibility (including `authored_by` and
`describes`), record-local source resolution, direct-host target type, matching
`belongs_to` assertions, exact-one host cardinality, changed-document local
links, whitespace, and the ADR 0006 University/Organization positive and
negative branch cases. No persistent validator, migration utility, generated
view, or architecture change is introduced before Quality Gate 6.
