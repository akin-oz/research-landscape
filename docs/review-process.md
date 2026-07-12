# Review process

Review protects the graph's long-term integrity. Reviewers assess evidence and
ownership, not the reputation of an institution, research group, or person.

## Author checklist

- The change has one clear artifact owner: canonical entity, report, view
  definition, automation, or private workflow.
- Every new reusable fact has one canonical entity owner and an exact source.
- Every new relationship has a documented predicate, resolvable target, local
  source IDs, confidence, and appropriate direction.
- Unknowns and deliberate non-claims are explicit; no absence becomes a
  negative conclusion.
- Generated files were regenerated rather than hand-edited.
- Validation, recommendation checks where relevant, and tests pass locally.

## Reviewer checklist

1. Verify identity and canonical ownership before reviewing prose.
2. Follow each `SRC-*` key to the record-local Evidence table and confirm the
   stated source scope supports the exact claim.
3. Check relationship direction, target type, dates, and direct-host rules.
4. Separate facts from report interpretation, personal preference, and scores.
5. Check that generated output is a projection of changed canonical inputs or
   versioned definitions, not a manually maintained inventory.
6. Confirm any model/schema/predicate change has an ADR or explicit approved
   architecture decision.
7. Run the documented validation workflow or inspect CI results before merge.

## Review outcomes

- **Approve:** claims, ownership, and automation boundaries are clear.
- **Request changes:** a claim is too broad, missing evidence, duplicated, or
  placed in the wrong layer.
- **Defer:** the evidence is insufficient or an architecture decision is needed.
  Document the gap; do not force a speculative implementation.

## Conflicts of interest

Contributors disclose a material institutional, supervisory, financial, or
personal relationship in the record or pull request. A reviewer with a material
conflict should not be the sole approver. Disagreement is resolved by narrowing
the claim, improving evidence, or preserving an explicit uncertainty—not by
voting on reputation.
