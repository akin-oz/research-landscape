# Contributing

Thank you for improving the evidence base. Start with [onboarding](docs/onboarding.md), [entity authoring](docs/entity-authoring.md), [review process](docs/review-process.md), [methodology](docs/methodology.md), and [quality guidelines](docs/quality-guidelines.md).

## Contribution workflow

1. Open an issue for a proposed report, metric change, architecture decision, or evidence correction when scope needs agreement.
2. Find the canonical owner before writing. Use the applicable entity/template contract; do not write reusable findings directly into a report, view, or generated index.
3. Record stable source URLs, publication/access dates, exact supported facts, limitations, and a confidence level.
4. Keep observations separate from interpretation, scoring, and personal decision support.
5. Run `validate`, regenerate affected output, run `generate --check` and `recommend --check`, then submit a focused pull request using the provided template.

## Requirements

- Cite public, lawful, relevant sources; prefer primary sources.
- Use lowercase kebab-case paths and immutable IDs from the [stable identifier specification](docs/data-model/stable-identifiers.md).
- Never infer protected characteristics, private information, intent, or mentoring quality from anecdote.
- Do not treat absence of evidence as evidence of absence.
- Preserve the declared scoring-model version; propose method changes separately from report updates.
- Do not edit `views/generated/` or `reports/generated/` by hand; repair canonical inputs or versioned definitions and regenerate.
- Do not add a type, predicate, schema field, or new canonical layer without an ADR/approved architecture decision.

Maintainers may request clarification, remove unverifiable claims, or reject content that conflicts with the [ethics policy](docs/ethics.md). See [SECURITY.md](SECURITY.md) for private vulnerability reporting.
