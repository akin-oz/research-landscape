# Quality Gate 8 review: knowledge quality

**Gate status:** complete

**Review date:** 2026-07-12

## Scope and method

This audit covers the complete repository's local Markdown-link surface and the
entire current canonical v2 graph under `entities/`. It uses the deterministic
validator, generated health report, view definition checks, recommendation-model
checks, generated-output drift checks, regression tests, and JSON Schema syntax
validation. It does not claim that an automated check can determine scientific
truth, source quality, or semantic duplication in prose.

The generated maintenance artifact is
[`repository-health.md`](generated/repository-health.md). It is a projection
from canonical inputs, not another source of facts.

## Measured results

| Quality dimension | Result | Interpretation |
| --- | ---: | --- |
| Canonical v2 entities | 67 | A reviewed, bounded graph cohort; not global coverage. |
| Metadata/source coverage | 67/67 reviewed records have source IDs and last-review dates | Required metadata is complete for the current canonical cohort. |
| Relationship evidence coverage | 116/116 typed assertions have source IDs | Every stored edge has record-local provenance. |
| Direct host integrity | 11/11 reviewed groups | Each group passes ADR 0006 host cardinality/type and matching-edge validation. |
| Graph connectivity | 67/67 entities have inbound or outbound graph connections | No structural orphans in the current cohort. |
| Broken local Markdown links | 0 | All repository-local Markdown targets resolve. Remote availability is not checked. |
| Duplicate signals | 0 stable-ID duplicates; 0 same-type normalized-name warnings | Structural duplicate detection passes; semantic prose duplication still needs human review. |
| Schema and migration compliance | 67/67 in approved entity directories; 0 v2 records outside `entities/` | Canonical ownership/migration placement passes. |
| View coverage | 13 definitions: 10 public generated, 3 private intentionally absent | Every required family has a deterministic contract. |
| Recommendation coverage | 11 queries: 9 available, 2 unavailable | Unavailable Python/mentorship queries expose missing contracts rather than fake results. |
| Automation coverage | Validator, generator, health report, recommendation engine, regression tests, and CI drift checks | Automation consumes canonical data and does not write facts back. |

## Quality findings

The current canonical graph is structurally healthy: all records and stored
relationships are source-bearing, all reviewed groups have direct hosts, no
canonical entity is structurally disconnected, and generated public views and
recommendations reproduce without drift. The health report's confidence
distribution is entirely `high`; that means the current cohort's declared
confidence values are complete, not that all global research claims are known
with high certainty.

The audit also makes coverage limits visible. Only two controlled research-area
entities exist, and the graph is deliberately a small cohort. Programming
language relations, comprehensive project/funding coverage, first-class source
records, and comparable mentorship/outcome evidence remain absent. The
recommendation engine correctly treats Python-heavy and high-mentorship queries
as unavailable.

## Recommended improvements

1. Add a governed programming-language entity contract and evidence-backed
   software-to-language relations before enabling Python-related queries.
2. Define an ethical, aggregate mentorship evidence contract before comparing
   mentoring environments or advisor outcomes.
3. Expand controlled research-area, project, funding, and organization records
   through small evidence-bounded slices, not bulk inference.
4. Consider a first-class source/evidence graph only through an ADR, because
   record-local citation keys limit cross-record provenance analysis.
5. Add remote link checking only with an explicit freshness, rate-limit, and
   archival policy; local-path validation alone must not be mistaken for source
   availability monitoring.

## Audit boundary

This gate proves the integrity and coverage of the current canonical cohort and
automation inputs. It does not prove that legacy reports have no semantic
overlap, that every public webpage remains live, that all research ecosystems
are represented, or that a recommendation is complete. Those are ongoing
editorial and expansion responsibilities governed by the architecture,
evidence, and review contracts.
