# Research Landscape

An open, evidence-based framework for evaluating the fit between graduate applicants and academic research environments.

> This repository does not rank researchers by prestige. It evaluates compatibility between applicants and research environments.

## Mission

Make advisor, lab, department, program, and university research easier to assess using traceable evidence, explicit uncertainty, and reproducible scoring. The project is designed as a document-backed knowledge graph—not a collection of opinions or promotional profiles.

## Motivation

Applicants often make high-stakes decisions from incomplete information and reputation signals. Evidence is scattered across publications, institutional pages, grants, repositories, and alumni records. This repository provides a common method for collecting that evidence, recording its limits, and comparing environments against an applicant's declared priorities.

## Project philosophy

- **Evidence before assertion.** Claims have sources, access dates, and confidence labels.
- **Compatibility, not prestige.** Scores are profiles that can be reweighted for a use case; they are not league tables.
- **Transparent uncertainty.** Missing or conflicting data is visible and never silently converted into a negative judgment.
- **Reproducible by default.** Inputs, transformations, scoring versions, and report revisions are reviewable in Git.
- **Respectful and fair.** Reports describe public, relevant evidence; they avoid personal speculation and harmful inferences.

## Methodology

The framework connects schema-validated entities and relationships to sourced observations, normalized metrics, dimension scores, and a use-case-specific compatibility calculation. Reports are views over this structured knowledge model and preserve evidence links and confidence at every layer. Read the [entity model](docs/data-model/entity-model.md), [frontmatter specification](docs/specifications/frontmatter.md), [methodology](docs/methodology.md), and [scoring model](docs/scoring-model.md) before contributing.

## Repository structure

| Location | Purpose |
| --- | --- |
| `docs/` | Governance, method, quality, and ethical guidance |
| `framework/` | Reusable entity-report templates with standardized metadata |
| `schemas/` | Versioned JSON Schemas for entity frontmatter |
| `docs/data-model/` | Entity, relationship, and stable-ID contracts |
| `methodology/metrics/` | Definitions and collection rules for each metric |
| `scoring/` | Calculation contracts and default weight guidance |
| `countries/` | Country-specific evidence reports, comparisons, and future geographical coverage |
| `reports/` | Future published reports and comparisons |
| `relationships/` | Markdown-first Research Relationship Management records, templates, and lifecycle guidance |
| `templates/` | Report and comparison starting points |
| `.github/` | Contribution forms and validation automation |

## Scoring principles

Scores are bounded, explainable indicators—not truth claims. A report includes the scoring-model version, evidence window, coverage, confidence, and sensitivity to alternative weights. Default weights express a general research-applicant baseline and are never a universal definition of “best.” See [v1 weights](scoring/v1/weights.md).

## Roadmap

The project begins with repository infrastructure (`v0.0.1`), then the knowledge model (`v0.1.0`), automation, and a clearly labeled Turkey pilot. The complete plan is in [ROADMAP.md](ROADMAP.md).

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md), the [quality guidelines](docs/quality-guidelines.md), and [ethics policy](docs/ethics.md). Contributions should improve evidence, method, or tooling; they must not add unsourced reputational claims.

## Future vision

The long-term goal is a maintained, machine-readable public knowledge base that can support thousands of advisors across hundreds of universities, with human review and automated data-refresh workflows. See [architecture](docs/architecture.md).

## Status

The core knowledge model is published. The repository includes an evidence-bounded Turkey advisor search, an Akdeniz University pilot, and an evidence-first due-diligence comparison of its narrowed three-advisor shortlist; these are compatibility analyses for a declared applicant profile, not university or prestige rankings. The [Research Relationship Management module](relationships/README.md) carries those evidence-backed findings into transparent, applicant-owned relationship records. Start with the [Turkey shortlist](countries/turkey/top-advisors-turkey.md) or the [advisor due-diligence dossiers](advisor-due-diligence/README.md).

## License and citation

Released under the [MIT License](LICENSE). Cite this project using [CITATION.cff](CITATION.cff).
