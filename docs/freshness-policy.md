# Review freshness policy

Research Landscape records when a maintainer last reviewed a canonical record;
it does not silently promise that a public web page or a research relationship
is current. This policy turns that review metadata into a reproducible
maintenance queue while preserving the evidence-first rule: a date is a prompt
to verify a claim, not proof that the claim is wrong.

## Scope

This policy applies to reviewed and published v2 entities and to any declared
`volatile_assertions` in their frontmatter. It does not rank entities, reduce
confidence automatically, scrape remote sources, or convert missing updates
into negative facts.

## Review intervals

The `freshness` audit classifies a reviewed record relative to its explicit
`--as-of` date:

| Signal | Rule | Maintainer action |
| --- | --- | --- |
| Current | `last_review` is at most 180 days old | No routine action solely from the date. |
| Attention | 181–365 days old | Add the record to a source-review batch when practical. |
| Stale | More than 365 days old | Prioritize source verification before using volatile claims in new analysis. |
| Future date | `last_review` falls after the audit date | Correct the review metadata; do not treat it as evidence. |

For a `volatile_assertions` entry, its record-specific `review_by` date wins:
the audit flags it as due soon within 30 days and overdue after that date. This
is appropriate for claims such as openings or GitHub activity, not for stable
historical facts.

## Workflow

Run a reproducible audit before a review batch or release:

```bash
python3 scripts/research_landscape.py freshness --as-of 2026-07-12
```

Review the cited primary sources, preserve the existing claim if still
supported, narrow or retire it if the evidence no longer supports it, then
update `last_review` and affected relationship evidence. Run the normal
validator and regenerate derived outputs afterwards. The audit is intentionally
not committed as a generated report because its result changes as time passes
without a canonical-input change.

## Boundaries

- `last_review` confirms a human review event, not universal source freshness.
- A stale record remains discoverable with its explicit evidence; its age is a
  maintenance signal, never a negative recommendation.
- Remote checks require source-specific, lawful automation and human review
  before they can change canonical facts.
- A record may have a newer source than its review date, but contributors must
  not update a date without reviewing whether the claimed scope still holds.
