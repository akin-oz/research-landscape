# Reference implementation review: AiiDA vertical slice

**Review date:** 2026-07-11

**Scope:** the AiiDA vNext reference cluster described in [the reference implementation](../docs/reference-implementation.md).

**Outcome:** the architecture supports a small, evidence-bounded software ecosystem without moving legacy content. The observed gaps should be resolved before scaling to hundreds of entities.

## Unexpected friction

| Finding | Effect in this slice | Treatment |
| --- | --- | --- |
| Unquoted ISO YAML dates parse as date objects, while both entity schemas require JSON strings with `format: date`. | Lifecycle fields looked visually valid but failed direct JSON Schema validation. | Quoted lifecycle and validation-date scalars in the slice and corrected the affected v1/vNext template examples. |
| Source IDs are required on reviewed v2 records and rich relationships, but no source/evidence entity or resolver exists. | A source ID cannot be validated as a graph target. | Every `SRC-*` value is resolved only in the subject record's Evidence table; no source entity or report-owned source store was invented. |
| `programming_language_ids` exists in v2, but programming language is neither a v2 entity type nor an `entities/` namespace. | The source-backed AiiDA → Python link cannot be represented as a complete v2 canonical relationship. | Omitted the field and documented the unresolved view limitation. |
| Views describe query contracts but provide no executable format or generator. | A real generated index cannot be produced or verified for this PR. | Recorded deterministic reachability checks only; no manual result list was added. |
| ID syntax is validated, but allocation and collisions are not. | A readable ID can be schema-valid without being centrally issued. | Used a consistent, scoped ID set and recorded the need for an ID registry. |

## Metadata problems

1. The entity-model narrative says a Research Area needs common `name`, while the normative metadata contract and schema require `label`. The area record contains both; the documents are not changed here.
2. Unquoted date examples in the original v1/vNext templates conflicted with the schemas after ordinary YAML parsing. The examples were corrected to quote date strings; existing records were not mass-rewritten.
3. `source_ids` are structurally valid but cannot be semantically resolved. This blocks a strong assertion that a record is fully provenance-complete even when its body has primary citations.
4. The present metadata cannot express the software's sourced Python relationship without crossing the v1/v2 boundary. Adding a free-text `language` would have bypassed the contract and was rejected.
5. Current roles are source snapshots. `last_review` and relationship `evidence_window` make their review point visible, but v2 has no uniform review-by field for affiliation or group-role assertions.

## Relationship problems

1. `software_ids` is useful as a normalized graph join, while `relationship_assertions` carries the evidence-bearing `develops` predicate. The two representations have to stay coherent, but the contract has no rule or validator that enforces that coherence.
2. Group-level software development was already described by the entity and software-ecosystem documents but missing from the relationship matrix. The matrix is now explicitly aligned; the source still does not support an individual maintainer claim for every group member.
3. The AiiDA ecosystem has multiple documented partners. The slice records only the PSI-connected entities required for the vertical chain; it must not be read as a complete ecosystem roster.

## Naming issues

| Decision | Rationale | Follow-up question |
| --- | --- | --- |
| `aiida-core` for the software record; `AiiDA Ecosystem` for the ecosystem record | The official site presents the engine and surrounding ecosystem as distinct things. | Establish a naming guide for code package, product, and ecosystem display names. |
| `Paul Scherrer Institute` as an `organization` | PSI is a research institute, not a university. | Define controlled organization kinds if automated filtering needs them. |
| `Computational Materials Science` as the one research area | It is the narrow direct wording supported by the PSI article. | Define a governed research-area taxonomy before adding broader or narrower links. |

## Missing contracts

- A canonical, reusable source/evidence record and resolver.
- A vNext successor and canonical home for programming-language records.
- An explicit compatibility policy for a v2 entity to reference an approved v1 supporting entity during the transition.
- A machine-readable subject/object compatibility matrix and checks that field-based joins match rich assertions.
- An identifier registry and duplicate-ID validation.
- A machine-readable view manifest, generator, freshness policy, and deterministic test fixtures.

## Boundary violations

| Boundary | Result | Evidence |
| --- | --- | --- |
| Canonical public facts vs. reports | Preserved | Facts are in `entities/`; reports retain only their existing analysis and a navigation link. |
| Canonical graph vs. applicant workspace | Preserved | No graph edge or public fact was added to `relationships/`. |
| Current facts vs. historic interpretation | Preserved | Current roles use first-party sources and evidence windows; legacy reports keep their stated 2026-07-11 scope. |
| Views vs. copied entity content | Preserved | No generated or manual view result was added. |
| Source register vs. canonical evidence store | Preserved, but fragile | The report-scoped `global-sources.md` was not promoted or altered; source keys are local citations only. |

No boundary violation was found in the implemented slice. The final row is a
scalability risk, not a reason to silently create a parallel source graph.

## Recommended improvements before scale

1. **P0 — specify evidence records.** Define a source/evidence schema, stable IDs, storage location, citation metadata, and a resolver; then migrate local citation keys deliberately.
2. **P0 — close the language bridge.** Define whether Programming Language remains a v1 satellite with an explicit compatibility projection or gains a versioned v2 type and canonical namespace.
3. **P1 — add graph validation.** Validate v2 frontmatter against `entity-vnext.schema.json`, ID uniqueness, relationship targets, predicate subject/object combinations, source-key resolution, and index/assertion consistency.
4. **P1 — define view manifests.** Make the declared view fields machine-readable, implement a deterministic generator, and add fixtures based on this AiiDA slice.
5. **P2 — define review freshness.** Give time-sensitive affiliation, group-role, and ecosystem relations a consistent review-by policy without treating missing data as a negative claim.

## Open questions

1. Should source evidence be first-class entities, a dedicated registry, or a versioned external-citation index?
2. What is the approved path for using a v1 Programming Language record from a v2 Research Software record before a v2 successor exists?
3. Should `software_ids` plus a `develops` assertion be required to be a matched pair, or should one representation become authoritative?
4. Should an AiiDA ecosystem view include all publicly documented partners by default, or only entities that meet a named evidence/freshness threshold?
5. What automated check should prevent a legacy dossier's compatibility link from becoming a second mutable profile?
