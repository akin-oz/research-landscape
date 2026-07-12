# Quality Gate 4 review: research group intelligence

**Gate status:** complete

**Review date:** 2026-07-12

**Scope:** all 11 reviewed canonical `research-group` records, their direct
hosts, and their corresponding Research Group Intelligence vertical slices.

## Gate outcome

Quality Gate 4 deepened every currently canonical Research Group record without
converting public web surfaces into speculative people, projects, software,
funding, opportunities, mentorship, or career outcomes. The corpus remains 67
v2 entities and 116 typed, evidence-bearing relationship assertions. It is not
a claim of global group coverage or a ranking.

## Reviewed cohort

| Research group | Intelligence slice |
| --- | --- |
| Persson Group | [Slice](../docs/persson-group-intelligence-vertical-slice.md) |
| Wolverton Research Group | [Slice](../docs/wolverton-group-intelligence-vertical-slice.md) |
| Curtarolo Group | [Slice](../docs/curtarolo-group-intelligence-vertical-slice.md) |
| Hacking Materials | [Slice](../docs/hacking-materials-intelligence-vertical-slice.md) |
| THEOS | [Slice](../docs/theos-intelligence-vertical-slice.md) |
| SOLgroup | [Slice](../docs/solgroup-intelligence-vertical-slice.md) |
| DTU CAMD | [Slice](../docs/dtu-camd-intelligence-vertical-slice.md) |
| Materialyze.AI Lab | [Slice](../docs/materialyze-ai-intelligence-vertical-slice.md) |
| Polymeromics Team | [Slice](../docs/riken-polymeromics-intelligence-vertical-slice.md) |
| RIKEN Computational Materials Science Team | [Slice](../docs/riken-computational-materials-science-intelligence-vertical-slice.md) |
| PSI Materials Software and Data Group | [Slice](../docs/psi-msd-intelligence-vertical-slice.md) |

## Coverage and boundaries

Every slice includes an explicit Quality Gate 4 matrix for research themes,
software/programming evidence, ecosystem and open-source participation, people,
funding, infrastructure, projects, collaborations, publication surfaces,
mentorship evidence, and career outcomes. Insufficient evidence remains
unknown rather than being inferred as a negative or a fact.

The cohort gives future views evidence-backed group paths to documented
software and ecosystems, but it does not elevate a paper, repository, group
website, or PI connection into individual maintenance, ownership, service
quality, or current opportunity claims.

## Quality and integrity review

| Gate rule | Result |
| --- | --- |
| Canonical ownership | Passed. Reusable facts remain in `entities/`; slices and reports link rather than duplicate profiles, rosters, or catalogs. |
| Evidence before inference | Passed. Missing funding, collaboration, mentoring, opportunity, and outcome evidence remains explicit. |
| Direct-host integrity | Passed. Every reviewed group has exactly one direct University/Organization host and matching evidence-bearing `belongs_to` assertion under ADR 0006. |
| Software boundary | Passed. Only directly evidenced group-to-software relations are stored as edges. |
| Time awareness | Passed. Dated public process material is not represented as durable live-opening, capacity, or funding facts. |
| Frozen architecture | Passed. No new type, predicate, parallel store, or architecture change was introduced. |
| Documentation/navigation | Passed. Every group has a slice, review record, entity-directory entry, and explicit future-view reachability. |
| Automation boundary | Preserved. One-off corpus checks were used; persistent validation and generated views remain deferred. |

## Exit evidence and QG5 handoff

The final complete-v2-corpus check passed at 67 entities and 116 relationships.
It covered schema/date shape, unique IDs, relationship endpoint types,
record-local source resolution, direct-host cardinality/type, matching
`belongs_to` assertions, changed-document links, whitespace, JSON Schema
parsing, and both ADR 0006 host branches.

Quality Gate 5 can now implement deterministic views from canonical entities
and these paths. It must not copy group prose, turn omission into a negative
fact, or hand-maintain search/ranking results.

## Known limitations

- The cohort is intentionally small and not a global survey.
- Source IDs remain record-local citations rather than source entities.
- Programming-language, project/funding, and comprehensive people/publication
  records need separate evidence-bounded work.
- Deterministic view generation and persistent validation remain deliberate
  next-gate work.
