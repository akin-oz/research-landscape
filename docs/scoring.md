# Scoring architecture

## Purpose

Scores are derived, versioned interpretations of evidence—not properties that belong permanently to a person, lab, university, country, or ecosystem. This architecture separates public, profile-independent signals from an applicant's compatibility and feasibility. It extends the existing [scoring model](scoring-model.md) and versioned [scoring contracts](../scoring/README.md); it does not change their formulas or calculate new scores.

**Non-negotiable rule:** accessibility must never affect a global score, global ranking, country view, university view, software view, or ecosystem view. Accessibility belongs only in a personal view for a declared applicant profile.

## Three distinct score types

| Score | Purpose | Inputs | Where it may appear |
| --- | --- | --- | --- |
| Global score | A transparent, profile-independent summary of documented public research signals and evidence coverage. It is not a prestige league table. | Public, sourced entity and relationship evidence only. | Public global/entity views, always with model version and coverage. |
| Personal score | Compatibility between one declared applicant profile and an entity or opportunity. | Global evidence plus declared research, software, career, and mentorship preferences. | The owner's shortlist and other explicitly personal views. |
| Accessibility score | Feasibility for one declared applicant at a point in time. | Applicant-specific mobility, language, funding, degree, remote, and timing constraints plus current evidence. | The owner's personal views only. |

The default UI or Markdown rendering should show these as separate columns or dimensions. A user may make a private decision ordering, but any blended calculation must be named `personal_decision_score`, record its weights, and never be copied into a global result.

## Dimension ownership

| Dimension | Global score | Personal score | Accessibility score | Boundary |
| --- | --- | --- | --- | --- |
| Research Fit | No | Yes | No | Fit depends on the applicant's project question and methods. |
| Software Fit | Underlying public software evidence only | Yes | No | A documented AiiDA, Python, or workflow connection is public evidence; its value to an applicant is personal. |
| Career ROI | No | Yes | No | Career goals and trade-offs are individual. |
| Mentorship | Evidence availability only | Yes | No | Public evidence can support a bounded assessment; reputation, awards, or country never prove mentorship fit. |
| Open Source Culture | Yes, from artifact and governance evidence | Optional | No | A GitHub profile alone is not enough evidence. |
| International Mobility | No | Optional preference | Yes | Visa/relocation feasibility is applicant- and time-specific. |
| Language Barrier | No | Optional preference | Yes | Use explicit program/working-language evidence, never a geographic stereotype. |
| Funding | Public funding activity only | Optional preference | Yes, for access to a specific route | A public grant does not prove an applicant is funded or eligible. |
| Current opening / degree eligibility | No | Optional gate | Yes | Must be time-bounded and sourced. |

## Calculation and missing data

All scored dimensions use the evidence rules and scale documented by their named model. The existing computational-materials scorecard, for example, uses 0–5 dimension values and normalizes only over available evidence. The same principle applies to all score types:

```text
score = sum(weight_i * dimension_i for available dimensions)
        / sum(weight_i for available dimensions)

coverage = available_weight / total_weight
```

Unknown is blank or `unavailable`, never zero. Every result must display coverage, the evidence window, the lowest material confidence, and the exact model/profile version. A low-coverage score is a prompt for research, not a precise comparison.

## What a score record must retain

Future score artifacts should be derived files or generated data, never ad hoc frontmatter copied across entities. Each result needs:

```yaml
entity_id: <canonical-entity-id>
score_type: global | personal | accessibility | personal_decision
scoring_model: v<major>/<model>
profile_id: <private-profile-id-or-null>
calculated_at: <ISO-8601-date>
evidence_window: <date-range>
coverage: <0-to-1>
confidence: high | medium | low | unavailable
dimensions:
  - name: <dimension>
    value: <model-scale-or-unavailable>
    weight: <weight>
    source_ids: [<source-id>]
```

`profile_id` is required for personal, accessibility, and decision scores, and must not expose private personal information. A global score has no applicant profile. Any change to a formula, normalization rule, interpretation, or default weight requires a new version under `scoring/v<major>/`, following the repository's existing versioning rule.

## Rendering rules

| View type | May display | Must not use |
| --- | --- | --- |
| Global, country, university, research-area, software, ecosystem | Canonical facts; source coverage; a documented global score if a model authorizes it | Personal weights, accessibility, private constraints, application status. |
| My shortlist | Canonical links; global, personal, and accessibility results shown separately | An unlabeled universal ranking. |
| Current targets | Personal and accessibility results; dated eligibility/action evidence | Stale opportunity claims or a public rank altered by private constraints. |

## Example boundary

For an applicant moving from software engineering toward computational materials, research fit and software fit may receive high personal weights for documented Python, workflow, data, or materials-informatics connections. A current MSc route, funding eligibility, English-language requirement, travel, or remote-collaboration feasibility instead changes that applicant's accessibility result.

If funding or mobility evidence is unavailable, the accessibility dimension stays unavailable and triggers follow-up. It cannot lower the global score of a PI, research group, university, country, software project, or ecosystem. This preserves the repository's central principle: compare compatibility transparently, not people or places by inaccessible personal circumstances.

## Refresh and review

- Recalculate when a sourced input, relationship, score model, or personal profile version changes.
- Expire or flag results that rely on stale roles, openings, admissions, repository activity, or funding evidence.
- Keep the source trail and calculation auditable in Git.
- Never derive a score from prestige, nationality, demographics, unverified anecdotes, or missing data.

The existing [v1 default weights](../scoring/v1/weights.md) and [computational-materials career-fit scorecard](../scoring/v1/computational-materials-career-fit.md) remain intact. This document defines how future global, personal, and accessibility outputs coexist without conflation.
