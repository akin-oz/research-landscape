# Architecture

## Purpose

Academic choices deserve inspectable evidence. This repository stores human-readable reports alongside structured conventions so a future toolchain can validate, aggregate, and refresh them without replacing editorial review.

## Layers

1. **Knowledge model:** entity Markdown documents with schema-validated YAML frontmatter and stable IDs.
2. **Evidence:** source URL, retrieval date, excerpt or extracted value, scope, and confidence.
3. **Metrics:** normalized observations defined in `methodology/metrics/`.
4. **Scores:** versioned dimension calculations and weights under `scoring/`.
5. **Reports:** rendered, versioned assessments under `reports/` or a geographical namespace.

Entity relationships and evidence flow upward; a score must be traceable back to its inputs. See the [entity model](data-model/entity-model.md), [relationship model](data-model/relationships.md), and [frontmatter specification](specifications/frontmatter.md).

## Report generation

Today, reports are authored from templates and reviewed in pull requests. Future Python tooling will parse front matter, validate source fields and score ranges, produce comparison views, cache source metadata, and flag stale evidence. Generated output must retain source links and model versions; automation may propose changes but cannot silently publish conclusions.

## Scale and identifiers

Paths use stable, lowercase kebab-case slugs. Future records should add stable IDs (for example, ROR for organizations and ORCID/OpenAlex identifiers when publicly applicable) rather than relying on display names. Separate entity files prevent repeated prose and support thousands of related records.
