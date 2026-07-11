# Repository audit

> **Audit basis:** the working tree reviewed on 2026-07-11. This is a structural inventory only: no records were moved, renamed, deleted, or reclassified in place.

## Executive finding

The repository has a sound evidence-first method and an explicit v1-to-vNext compatibility boundary. Its main information-architecture problem is not missing structure; it is that the same subject can currently have several plausible homes. In particular, people and groups appear through country paths, global dossiers, indexes, reports, and the planned `entities/` graph. The overlap is often intentional during migration, but the reader is not always told which location owns the underlying fact today.

The current tree contains three different kinds of material:

1. **Current evidence and analysis** — Turkey records, global dossiers, due diligence, and reports.
2. **Reusable platform contracts** — schemas, templates, metric definitions, scoring contracts, and automation scaffolding.
3. **vNext scaffolding** — `entities/` and `views/`, deliberately empty of migrated records.

The audit treats `.git/` as tool-managed Git state. It is listed for completeness but is not a repository-content layer.

## Top-level directory inventory

Each entry has one primary category from the requested taxonomy. “Overlap” identifies either a useful compatibility bridge or a boundary that needs a later migration decision.

| Location | Primary category | Why it exists / current responsibility | Clarity, overlap, and current state |
| --- | --- | --- | --- |
| `.github/` | Automation | Pull-request and issue templates plus the repository validation workflow. | Clear. It is the only CI/workflow home; it depends on the Markdown and JSON-schema corpus. |
| `.git/` | Configuration | Git’s local history, refs, index, and hooks. | Tool-managed and outside the authored IA. No repository documents belong here. |
| `.idea/` | Configuration | Local IDE settings. | Clear as workstation configuration, but it is ignored rather than a collaborative repository layer. |
| `advisor-due-diligence/` | Analysis | Applicant-profile-specific evidence review, comparison, decision gates, reading, and contact preparation for three advisors. | Mostly clear, but overlaps `countries/turkey/` advisor material and `relationships/` preparation records. It must not become the canonical public person profile or a private interaction log. |
| `assets/` | Platform | Reserved visual assets; currently only placeholder files for icons and logos. | Clear but inactive. It should not become a document, evidence, or generated-report store. |
| `countries/` | Knowledge | Legacy geographical navigation containing Turkey evidence, faculty profiles, bibliographies, comparisons, and decision documents; `global/` is contextual only. | Mixed in practice: factual records, analysis, and applicant decisions share country paths. This is the clearest legacy hierarchy that competes with entity-oriented navigation. |
| `docs/` | Documentation | Method, governance, ethics, ADRs, schemas’ usage guidance, release notes, and both v1 and vNext architecture contracts. | Clear as the explanatory layer. `docs/data-model/` (v1) and `docs/architecture/` (vNext) intentionally overlap; their compatibility notes are essential. |
| `ecosystems/` | Knowledge | Intended home for ecosystem-level knowledge. At present it is an index pointing to the global ecosystems report and source register. | Provisional. It overlaps `reports/global-ecosystems.md` and future `entities/ecosystems/`; it owns no ecosystem record yet. |
| `entities/` | Knowledge | Reserved canonical home for vNext entity records, organized by entity type. | Strong target responsibility, but currently all child directories are README-only scaffolds. It intentionally coexists with legacy country paths and dossiers until migration. |
| `framework/` | Platform | v1 entity-report templates with frontmatter and evidence/score sections. | Clear as a legacy authoring contract, but overlaps generic `templates/` and the frontmatter/schema documentation. |
| `methodology/` | Documentation | Metric definitions and collection rules used by evidence and scoring work. | Clear. It complements, rather than owns, the higher-level methodology documentation in `docs/`. |
| `principal-investigators/` | Knowledge | Declared PI index and dossier-pack contract. | Ambiguous in practice: it contains only an index while the ten actual dossier packs live in `research-leaders/`; future canonical PI records are planned under `entities/principal-investigators/`. |
| `relationships/` | Workspace | Markdown-first research relationship-management policy, templates, prepared/active records, and archive rules. | A deliberately separate personal-process boundary, but it combines policy, reusable templates, and applicant-owned records in one module. It must not be treated as public evidence. |
| `reports/` | Analysis | Published global comparative analyses, discovery queues, source register, personal roadmap, and report entry points. | Mixed output types: analysis, an evidence register, and thin aliases to `special-reports.md`. The aliases are intentional navigation aids, but the source register is knowledge-like rather than a conclusion. |
| `research-groups/` | Knowledge | Intended group-level dossier namespace. | Provisional and README-only; the current 50-group queue is in `reports/`. It overlaps future `entities/research-groups/`. |
| `research-leaders/` | Analysis | Ten deep global leader dossiers that combine public evidence with applicant-specific career and contact interpretation. | Rich current corpus, but public factual portions will eventually hand off to canonical entities; it should not become a second canonical entity store. |
| `schemas/` | Platform | JSON Schema contracts for v1 frontmatter and the proposed vNext entity shape. | Clear. It is structurally authoritative for schema validation; vNext is explicitly not yet enforced or applied to existing records. |
| `scoring/` | Platform | Immutable versioned scoring contracts and weights; it also contains the profile-specific computational-materials scorecard. | Model contracts are clear, but the operational profile scorecard is an analysis artifact living beside reusable scoring rules. |
| `scripts/` | Automation | Reserved home for reproducible validation, ingestion, and report generation. | Clear intended role but currently README-only; no generated-output contract is implemented yet. |
| `templates/` | Platform | Generic report and comparison starting templates. | Clear, but overlaps `framework/`’s entity-specific templates and `relationships/templates/`’s workspace templates. |
| `views/` | Generated | Reserved definitions for repeatable entity-graph navigation: global, country, university, area, software, ecosystem, and personal views. | Strong boundary in documentation, but currently no generated views exist; the directory presently acts as vNext documentation/scaffolding. |

## Top-level file inventory

| File | Category | Responsibility and boundary |
| --- | --- | --- |
| `.DS_Store` | Workspace | Finder metadata. It has no project meaning and should not be treated as a repository artifact. |
| `.gitignore` | Configuration | Defines ignored local files; currently ignores `.idea` but not the present `.DS_Store`. |
| `README.md` | Documentation | Primary orientation and navigation page; it should summarize rather than duplicate every detailed contract. |
| `ROADMAP.md` | Documentation | Versioned direction and migration sequencing; it should not become an implementation log. |
| `CHANGELOG.md` | Documentation | Released and unreleased change history; it should reference rather than restate architecture. |
| `CONTRIBUTING.md` | Documentation | Contributor workflow and evidence requirements. |
| `CODE_OF_CONDUCT.md` | Documentation | Community conduct rules. |
| `SECURITY.md` | Documentation | Security reporting boundary. |
| `CITATION.cff` | Documentation | Machine-readable citation metadata. |
| `LICENSE` | Documentation | Legal reuse terms. |

## Cross-cutting ownership observations

### Intentional compatibility, not duplication to remove immediately

- **v1 and vNext contracts:** `docs/data-model/`, `docs/specifications/`, and v1 schemas remain authoritative for existing records; `docs/architecture/`, `entities/`, `views/`, and `entity-vnext.schema.json` define the target. The documentation consistently says no migration has happened.
- **Global discovery versus verified dossiers:** `reports/top-100-principal-investigators.md` is a revalidation-aware queue; `research-leaders/` contains the deeper anchor packs. They should remain visibly different evidence tiers.
- **Report aliases:** the nine short `top-10`, `top-25`, and `top-50` files deliberately direct readers to sections of `reports/special-reports.md`. They are navigation aliases, not competing lists.

### Boundaries that are currently unclear

1. **Canonical PI/group ownership is split three ways.** `countries/` contains legacy person records, `research-leaders/` contains global dossier packs, `principal-investigators/` calls itself the canonical index, and `entities/` is the intended canonical home. Until migration, every index should identify its source-of-truth role explicitly.
2. **Country paths mix knowledge with conclusions.** The Turkey tree includes public faculty evidence alongside recommendations, comparisons, priorities, and decisions. Country is therefore both a navigation facet and a container for applicant-specific analysis.
3. **Dossier packs mix public knowledge and personal interpretation.** `research-leaders/*/profile.md`, `research.md`, and `software.md` are evidence knowledge; `career-value.md` and `contact-strategy.md` are applicant-specific analysis/action planning.
4. **Reusable templates have three homes.** `framework/` owns v1 entity templates, `templates/` owns generic reports, and `relationships/templates/` owns RRM records. The distinction is sensible but is not yet presented as a single authoring decision.
5. **Reports mix conclusions and source material.** `reports/global-sources.md` is a reusable evidence register, while the other report files are analyses or navigation aliases. A later architecture should make the evidence/report relationship unmistakable without moving data in this phase.
6. **Scoring combines contract and instance.** `scoring/v1/*.md` defines reusable rules, whereas `computational-materials-career-fit.md` is a declared-profile application of those rules.
7. **Future-generated concepts are documentation-only today.** `views/` and `scripts/` describe a generation pipeline but contain neither generated output nor an implementation. Readers should not mistake them for populated indexes.

## Audit conclusion

The repository is understandable once a contributor learns the compatibility story, but it is not yet obvious in five minutes because the legacy content layer and vNext target layer are both visible at the top level. The safest next step is to document one ownership map and migration order—not to move records yet. That map should preserve the current evidence while making these distinctions explicit:

- canonical public knowledge versus applicant-specific analysis;
- reusable platform contracts versus authored records;
- personal workspace records versus public evidence; and
- future generated views versus their canonical inputs.
