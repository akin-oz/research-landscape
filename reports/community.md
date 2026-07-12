# Community readiness

Research Landscape is ready for evidence-first public contribution to the
current canonical cohort. This review records the contributor paths and the
limits that maintainers must preserve as the repository grows.

## Readiness review

| Area | Evidence | Result |
| --- | --- | --- |
| Entry point and discoverability | Root README links generated discovery, recommendations, health, onboarding, authoring, and review guidance. | Ready. |
| Contributor onboarding | [`docs/onboarding.md`](../docs/onboarding.md) provides artifact placement, first steps, commands, and help routes. | Ready. |
| Entity authoring | [`docs/entity-authoring.md`](../docs/entity-authoring.md) specifies canonical ownership, frontmatter, local evidence IDs, relationship direction, ADR 0006, unknowns, and validation. | Ready. |
| Evidence and writing guidance | Methodology, quality guidelines, ethics, templates, and contributor policy distinguish facts, interpretation, unknowns, and personal data. | Ready. |
| Review process | [`docs/review-process.md`](../docs/review-process.md) provides author/reviewer checklists, outcomes, conflict handling, and architecture escalation. | Ready. |
| Automation and developer experience | Pinned dependencies, documented commands, regression tests, generated-output boundary, and CI drift checks are published. | Ready. |
| Examples and navigation | Reviewed vertical slices, generated views, recommendations, reports index, and entity-directory indexes provide reference paths. | Ready. |
| Decision records | Accepted ADRs remain the only path for architecture changes; contribution guidance directs schema/type/predicate changes to an ADR. | Ready. |
| Privacy and community safety | Code of Conduct, ethics policy, security reporting, and public/private view boundaries are documented. | Ready. |

## Maintainer commitments

1. Review the canonical owner and evidence before wording or rankings.
2. Keep generated files reproducible and reject manual projection edits.
3. Treat missing evidence as unknown and preserve source scope/limitations.
4. Require ADR review before changing entity types, predicates, schemas, or
   canonical ownership boundaries.
5. Never turn contributor activity, country, prestige, reputation, or private
   information into research-quality, mentoring, or admissions claims.

## Deferred community work

- Remote-source freshness checks require an explicit rate-limit, archive, and
  failure policy.
- A first-class source graph, language entities, and mentorship metrics require
  evidence-contract/ADR work before broad community ingestion.
- Broader international coverage requires the same small-slice review standard,
  not bulk name collection.

The canonical cohort's structural health is documented in the generated
[repository-health report](generated/repository-health.md); this review does
not claim that coverage is globally complete.
