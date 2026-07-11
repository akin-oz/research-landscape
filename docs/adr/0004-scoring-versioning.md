# ADR 0004: Version scoring models as immutable directories

- **Status:** Accepted
- **Date:** 2026-07-11

## Context

Changing score formulas or weights can change historical interpretations and make reports irreproducible.

## Decision

Store each scoring model in `scoring/v<major>/`. A report records its exact scoring-model reference. Existing model files are never edited to change semantics after publication; revisions create a new version.

## Consequences

Scores remain reproducible and comparisons can disclose version differences. Maintainers must support migration and deprecation documentation as models evolve.
