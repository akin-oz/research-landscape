# ADR 0009: Model evidence-bounded research problems as first-class entities

- **Status:** Accepted — 2026-07-13
- **Date:** 2026-07-13

## Context

Research areas make topics discoverable, but they do not identify a bounded
computational challenge. Projects, grants, papers, and software can all relate
to a challenge without being that challenge. Reusing any of them would make
problem discovery ambiguous and invite unsupported “best problem” rankings.

## Decision

`research-problem` is a first-class v2 entity type with a required
`problem_kind`, record-local evidence, and typed links to research areas.
Every `research_area_ids` classification must have exactly one matching sourced
`addresses` assertion, and every such assertion must resolve back to that
controlled classification.
Research software may use a sourced `supports` relation to a Research Problem.
The public generated problem view and `discover-problems` command show only
reviewed problems and direct software support paths.

The initial record, Lattice Thermal Conductivity Prediction, is intentionally
bounded to the documented Phono3py calculation scope. It is not a statement
about scientific priority, novelty, tractability, funding, or fit.

## Consequences

- A problem is neither a project, funding call, benchmark, nor ranking.
- Every problem and support relation must carry record-local public evidence.
- Future problem discovery can grow through explicit typed relationships rather
  than copied prose or implicit people/software adjacency.
- Comparative problem recommendations remain unavailable until a separate,
  governed evidence contract supports them.
