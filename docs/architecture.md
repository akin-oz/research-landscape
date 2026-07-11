# Architecture

## Purpose

Academic choices deserve inspectable evidence. This repository stores human-readable reports alongside structured conventions so a future toolchain can validate, aggregate, and refresh them without replacing editorial review.

The vNext target is an **entity-oriented knowledge system**: Principal Investigators, research groups, universities, research software, research ecosystems and related entities are canonical records; countries are contextual entities and filters, not the organising root. This remains Markdown-first, Git-friendly and database-free.

## Layers

1. **Canonical entities:** one Markdown record per entity under `entities/`, with stable IDs and standardized YAML frontmatter.
2. **Evidence:** source URL, retrieval date, excerpt or extracted value, scope, and confidence.
3. **Relationships:** typed, evidence-bounded links between entity IDs.
4. **Views:** Markdown indexes under `views/` that organize canonical entities without copying them.
5. **Metrics and scores:** normalized observations and versioned, applicant-specific calculations under `methodology/` and `scoring/`.
6. **Reports:** rendered, versioned assessments that cite entities and evidence rather than becoming a competing source of truth.

Entity relationships and evidence flow upward; a score must be traceable back to its inputs. The vNext design is specified in the [entity model](architecture/entity-model.md), [relationship model](architecture/relationships.md), [metadata contract](architecture/metadata.md), [software-ecosystem model](architecture/software-ecosystems.md), [views](../views/README.md), [personalization model](personalization.md), and [scoring architecture](scoring.md).

The earlier [v1 data model](data-model/entity-model.md), [relationship model](data-model/relationships.md), and [frontmatter specification](specifications/frontmatter.md) remain the compatibility contract for existing records. This architecture phase does not move or rename them.

## Report generation

Today, reports are authored from templates and reviewed in pull requests. Future tooling may parse frontmatter, validate source fields and score ranges, generate Markdown views, cache source metadata, and flag stale evidence. Generated output must retain source links and model versions; automation may propose changes but cannot silently publish conclusions.

## Scale and identifiers

Paths use stable, lowercase kebab-case slugs. Future records should add stable IDs (for example, ROR for organizations and ORCID/OpenAlex identifiers when publicly applicable) rather than relying on display names. Separate entity files prevent repeated prose and support thousands of related records. No database, graph server, or web application is part of this architecture.
