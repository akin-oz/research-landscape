# ADR 0010: Gate comparative research-problem outputs behind a governed evidence contract

- **Status:** Accepted — 2026-07-13
- **Date:** 2026-07-13

## Context

The repository can discover bounded computational challenges and their sourced
software, group, PI, University, ecosystem, and implementation-language paths.
Those paths do not establish that one problem is universally better, more
important, more tractable, or a better fit for a particular researcher.

## Decision

`best-research-problems` remains unavailable until a versioned evaluation model
is accepted and has all of the following:

1. A declared stakeholder scope and decision purpose; no universal-value claim.
2. Explicit, separately sourced criteria with definitions, evidence windows,
   missing-data handling, and uncertainty representation.
3. Comparable coverage across the candidate set, with exclusions and conflicts
   visible to users.
4. Versioned aggregation and sensitivity rules, plus reproducible generated
   output that retains every supporting source identifier.
5. Ethics review for incentives and harms, including prestige, hype, extractive
   labor, and gatekeeping risks.

The current public surface remains `discover-problems` and its source-explained
area, software, ecosystem, and programming-language filters. These are
discovery tools, not preliminary scores.

## Consequences

- A future comparative feature must be proposed as a versioned model, not an
  ad hoc frontmatter field or editorial list.
- Missing evidence remains visible and cannot be treated as a negative value.
- The unavailable recommendation query is a concrete implementation gate, not
  permission to infer a ranking from the current graph.
