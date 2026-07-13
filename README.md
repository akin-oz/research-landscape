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

## Start here

- Explore the current canonical graph through the generated [global view](views/generated/global.md), [software view](views/generated/research-software.md), [ecosystem view](views/generated/ecosystems.md), and [evidence recommendations](reports/generated/evidence-recommendations.md).
- Run `python3 scripts/research_landscape.py discover-areas` to explore reviewed research topics, their evidence sources, and direct discovery coverage before selecting a canonical area ID; this is not a research-problem ranking.
- Run `python3 scripts/research_landscape.py discover-areas --problem PROBLEM-MATERIALS-PROPERTY-PREDICTION` to inspect only the controlled topics directly classified on a reviewed problem record, with its source IDs; this is not a comparison of topics or problems.
- Run `python3 scripts/research_landscape.py discover-areas --software SW-MATGL` to inspect only the controlled topics directly classified on a reviewed software record; combine it with `--problem` to intersect those two cited classifications.
- Run `python3 scripts/research_landscape.py discover-problems --area AREA-MACHINE-LEARNED-POTENTIALS` to inspect reviewed computational challenges in one controlled topic and their direct supporting-software evidence; this is not an importance or tractability ranking.
- Run `python3 scripts/research_landscape.py discover-problems --software SW-PHONO3PY` to find problems with a direct, sourced support assertion from a specific reviewed software record.
- Run `python3 scripts/research_landscape.py discover-problems --ecosystem ECO-PHONO3PY` to find problems through a documented ecosystem-inclusion and software-support path.
- Run `python3 scripts/research_landscape.py discover-problems --language PROGRAMMING-LANGUAGE-C` to inspect problems through a documented implementation-language and direct-software-support path.
- Run `python3 scripts/research_landscape.py catalog` to list reviewed public IDs for interactive discovery filters without reading canonical frontmatter.
- Run `python3 scripts/research_landscape.py inspect --entity SW-MACE` to inspect one reviewed canonical record's direct typed relationships and record-local evidence register without a ranking or profile inference.
- Use `python3 scripts/research_landscape.py discover-groups --area AREA-AI-FOR-MATERIALS --country COUNTRY-US` for an interactive, source-explainable group filter; see [automation](docs/automation.md) for the supported IDs and evidence paths.
- Use `python3 scripts/research_landscape.py discover-groups --language PROGRAMMING-LANGUAGE-CPP` to find documented group-to-software C++ paths; this is not a claim about a group's universal programming practice.
- Use `python3 scripts/research_landscape.py discover-groups --problem PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION` to find groups with a documented development path to software that directly supports a reviewed problem; this does not claim the group itself works on that problem.
- Use `python3 scripts/research_landscape.py discover-pis --software SW-PYMATGEN --language PROGRAMMING-LANGUAGE-PYTHON` for the corresponding source-explainable PI filter; it is discovery, not an availability or mentorship claim.
- Use `python3 scripts/research_landscape.py discover-pis --problem PROBLEM-MACHINE-LEARNED-INTERATOMIC-POTENTIAL-MODELING` to find PIs with a documented development path to software that directly supports a reviewed problem; it does not claim they work on, endorse, or supervise that problem.
- Use `python3 scripts/research_landscape.py discover-universities --area AREA-AI-FOR-MATERIALS --country COUNTRY-US` to inspect direct-host university paths without treating them as a ranking.
- Use `python3 scripts/research_landscape.py discover-universities --problem PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION` to inspect direct-host university paths to group-developed software that supports a reviewed problem; this does not claim the university works on or endorses the problem.
- Use `python3 scripts/research_landscape.py discover-universities --area AREA-MACHINE-LEARNED-POTENTIALS --ecosystem ECO-MATML` to inspect the displayed university → group → software → ecosystem path without implying university membership or ecosystem strength.
- Use `python3 scripts/research_landscape.py discover-ecosystems --area AREA-MACHINE-LEARNED-POTENTIALS` to inspect sourced ecosystem paths without treating coverage as dominance.
- Use `python3 scripts/research_landscape.py discover-ecosystems --problem PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION` to inspect ecosystems through explicit software-support paths without treating any ecosystem as dominant or complete.
- Use `python3 scripts/research_landscape.py discover-ecosystems --area AREA-MACHINE-LEARNED-POTENTIALS --software SW-FAIRCHEM` to inspect the documented Open Catalyst Project-to-FAIRChem migration route; this is not a current-ecosystem or ownership assertion.
- Use `python3 scripts/research_landscape.py discover-software --area AREA-MACHINE-LEARNED-POTENTIALS --language PROGRAMMING-LANGUAGE-PYTHON --ecosystem ECO-MATML --open-source yes` to find software through explicit topic, implementation-language, ecosystem, and documented license-backed openness paths.
- Use `python3 scripts/research_landscape.py discover-software --problem PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION` to find software with a direct, sourced support assertion for a reviewed problem.
- Use `python3 scripts/research_landscape.py discover-software --area AREA-COMPUTATIONAL-MATERIALS-SCIENCE --language PROGRAMMING-LANGUAGE-CPP --ecosystem ECO-OPENKIM --open-source yes` to inspect the bounded KIM API route; it does not imply an OpenKIM maintainer roster or support commitment.
- Use `python3 scripts/research_landscape.py discover-software --area AREA-COMPUTATIONAL-MATERIALS-SCIENCE --language PROGRAMMING-LANGUAGE-FORTRAN --ecosystem ECO-CP2K --open-source yes` to inspect CP2K's sourced implementation and ecosystem route without inferring individual programming skill or project support.
- Use `python3 scripts/research_landscape.py discover-software --area AREA-COMPUTATIONAL-MATERIALS-SCIENCE --language PROGRAMMING-LANGUAGE-FORTRAN --ecosystem ECO-ABINIT --open-source yes` for the same bounded ABINIT path; it is not a current-maintainer, review, or institutional-access claim.
- Use `python3 scripts/research_landscape.py recommend --query ecosystems-density-functional-theory-and-electronic-structure` to inspect exact ABINIT, CP2K, and Quantum ESPRESSO DFT/electronic-structure paths without treating them as comparable or complete.
- Use `python3 scripts/research_landscape.py recommend --query groups-density-functional-theory-and-electronic-structure` to find directly evidenced lab paths; use the matching University query to inspect direct hosts without ranking institutions.
- Read [onboarding](docs/onboarding.md) to contribute, [entity authoring](docs/entity-authoring.md) before changing canonical knowledge, and [review process](docs/review-process.md) before opening a pull request.
- Inspect the generated [repository-health report](reports/generated/repository-health.md) for current coverage and structural limits.

## Methodology

The framework connects schema-validated entities and relationships to sourced observations, normalized metrics, dimension scores, and a use-case-specific compatibility calculation. Reports are views over this structured knowledge model and preserve evidence links and confidence at every layer. Read the [entity model](docs/data-model/entity-model.md), [frontmatter specification](docs/specifications/frontmatter.md), [methodology](docs/methodology.md), and [scoring model](docs/scoring-model.md) before contributing.

## Repository structure

| Location | Purpose |
| --- | --- |
| `docs/` | Governance, method, quality, and ethical guidance |
| `entities/` | Canonical, sourced public facts and typed relationships |
| `views/` | Declarative view definitions and reproducible public navigation projections |
| `framework/` | Reusable entity-report templates with standardized metadata |
| `schemas/` | Versioned JSON Schemas for entity frontmatter |
| `docs/data-model/` | Entity, relationship, and stable-ID contracts |
| `methodology/metrics/` | Definitions and collection rules for each metric |
| `scoring/` | Calculation contracts and default weight guidance |
| `countries/` | Country-specific evidence reports, comparisons, and future geographical coverage |
| `reports/` | Dated analyses, quality reviews, and generated health/recommendation projections |
| `ecosystems/` | Ecosystem-level records; avoids treating countries as research-quality proxies |
| `research-groups/` | Group-level dossiers and discovery queue |
| `principal-investigators/` and `research-leaders/` | PI index and evidence-backed leader dossiers |
| `relationships/` | Markdown-first Research Relationship Management records, templates, and lifecycle guidance |
| `templates/` | Report and comparison starting points |
| `scripts/` | Validation, generation, health, and recommendation automation |
| `.github/` | Contribution forms and validation automation |

## Scoring principles

Scores are bounded, explainable indicators—not truth claims. A report includes the scoring-model version, evidence window, coverage, confidence, and sensitivity to alternative weights. Default weights express a general research-applicant baseline and are never a universal definition of “best.” See [v1 weights](scoring/v1/weights.md).

## Roadmap

The v0.3.0 knowledge-graph execution release is complete for its reviewed canonical cohort. Read the [final implementation review](FINAL_IMPLEMENTATION_REVIEW.md), [roadmap status](ROADMAP_STATUS.md), and the continuing [ROADMAP.md](ROADMAP.md) for its evidence and limits.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md), [onboarding](docs/onboarding.md), the [entity authoring guide](docs/entity-authoring.md), the [review process](docs/review-process.md), the [quality guidelines](docs/quality-guidelines.md), and [ethics policy](docs/ethics.md). Contributions should improve evidence, method, or tooling; they must not add unsourced reputational claims.

## Future vision

The long-term goal is a maintained, machine-readable public knowledge base that can support thousands of advisors across hundreds of universities, with human review and automated data-refresh workflows. See [architecture](docs/architecture.md).

## Global computational-materials intelligence

The repository now includes an evidence-bounded global starting point for a senior software engineer moving into computational materials science: [ecosystem comparison](reports/global-ecosystems.md), [100-person non-ranked discovery slate](reports/top-100-principal-investigators.md), [anchor dossiers](principal-investigators/README.md), [special shortlists](reports/special-reports.md), [source register](reports/global-sources.md), [career roadmap](reports/personal-roadmap.md), and a profile-specific [scorecard](scoring/v1/computational-materials-career-fit.md). The discovery slate is explicitly separated from verified dossiers so that current roles and openings are never fabricated.

## Status

The v0.3.0 execution phase has passed its current-cohort integrity review: the core knowledge model, deterministic views, validation tooling, and explainable evidence recommendations are published. The canonical cohort is intentionally bounded; generated reports display coverage and limitations rather than claiming a complete global map. The repository also includes an evidence-bounded Turkey advisor search, an Akdeniz University pilot, and an evidence-first due-diligence comparison of its narrowed three-advisor shortlist; these are compatibility analyses for a declared applicant profile, not university or prestige rankings. The [Research Relationship Management module](relationships/README.md) carries those evidence-backed findings into transparent, applicant-owned relationship records. Start with the [Turkey shortlist](countries/turkey/top-advisors-turkey.md) or the [advisor due-diligence dossiers](advisor-due-diligence/README.md).

## License and citation

Released under the [MIT License](LICENSE). Cite this project using [CITATION.cff](CITATION.cff).
