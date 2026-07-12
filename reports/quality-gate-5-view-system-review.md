# Quality Gate 5 review: deterministic view system

**Gate status:** complete — definition layer; generated indexes intentionally
deferred to Quality Gate 6 automation.

**Review date:** 2026-07-12

## Gate outcome

Quality Gate 5 establishes one machine-readable source of truth for required
view families: [`views/definitions.yaml`](../views/definitions.yaml). It
declares deterministic membership scope, traversals, facets, ordering,
visibility, evidence boundaries, and unknown handling without adding
hand-maintained entity lists.

The manifest has 13 unique required view IDs: Global, Countries, Universities,
Research Areas, Research Software, Ecosystems, Principal Investigators,
Research Groups, Conferences, Funding, My Shortlist, Current Focus, and
Waiting List.

## Generated-output decision

No populated Markdown index is committed in this gate. Such an index would be
either manually maintained (prohibited) or produced by tooling that does not
yet exist. Every definition declares `generated_output: none` and an
`output_reason`. Quality Gate 6 owns generation, output provenance, freshness,
validation, and repository-health integration.

This is an intentional boundary, not a claim that the current README examples
are generated results.

## Coverage and boundaries

| Requirement | Result |
| --- | --- |
| Views organize; entities own | Passed. Definitions select canonical IDs and declared relationships only. |
| No duplicated facts | Passed. Display is limited to concise frontmatter plus canonical links. |
| Deterministic membership and order | Passed at definition level. Each view has fixed scope and ordering. |
| Public/private separation | Passed. Shortlist, Current Focus, and Waiting List require private inputs and create no public output. |
| Unknown values | Passed. The common contract retains unknown values unless a documented path is required. |
| Country is a filter | Passed. Country resolution is a declared relationship traversal. |
| Time awareness | Passed. Conference/Funding use dates; focus/waiting entries require action or revisit dates. |
| Current-targets compatibility | Passed. The existing guide has no separate result set and is superseded by Current Focus behavior. |

## Validation record

The one-off view-definition validation passed. It checked manifest version, the
exact 13 required IDs, uniqueness, required declaration fields, visibility,
nonempty scope and ordering, membership/facet shape, output reasons, and
navigation READMEs for every new family. Local links and whitespace are checked
before publishing.

## QG6 handoff

Quality Gate 6 must parse entity frontmatter and this manifest, resolve only
declared relationship paths, validate endpoint types, generate clearly marked
indexes with source revision/time, detect generated-output drift, and report
absent or unknown data without creating negative claims. The generator cannot
become a second source of truth or synthesize missing relationships.
