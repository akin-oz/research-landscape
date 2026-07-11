# Contributing

Thank you for improving the evidence base. Start with the [research process](docs/research-process.md), [methodology](docs/methodology.md), and [quality guidelines](docs/quality-guidelines.md).

## Contribution workflow

1. Open an issue for a proposed report, metric change, or evidence correction.
2. Use the applicable template and validate entity frontmatter against `schemas/`; do not write findings directly into an index.
3. Record stable source URLs, publication/access dates, quoted or extracted facts, and a confidence level.
4. Keep observations separate from interpretation and scoring.
5. Submit a focused pull request using the provided template.

## Requirements

- Cite public, lawful, relevant sources; prefer primary sources.
- Use lowercase kebab-case paths and immutable IDs from the [stable identifier specification](docs/data-model/stable-identifiers.md).
- Never infer protected characteristics, private information, intent, or mentoring quality from anecdote.
- Do not treat absence of evidence as evidence of absence.
- Preserve the declared scoring-model version; propose method changes separately from report updates.

Maintainers may request clarification, remove unverifiable claims, or reject content that conflicts with the [ethics policy](docs/ethics.md). See [SECURITY.md](SECURITY.md) for private vulnerability reporting.
