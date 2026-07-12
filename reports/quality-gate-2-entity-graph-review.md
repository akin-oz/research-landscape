# Quality Gate 2 review: entity graph completion

**Gate status:** complete
**Review date:** 2026-07-12
**Scope:** the published vNext canonical graph after the Quality Gate 1 cohort
and the five published Quality Gate 2 vertical slices.

## Gate outcome

Quality Gate 2 extended the canonical graph beyond the first cohort into each
entity category named by the execution brief: Principal Investigators, Research
Groups, Universities, Countries, Research Areas, Research Software, Projects,
Organizations, Funding Programs, and Conferences. The reviewed corpus contains
60 v2 entities and 101 typed, evidence-bearing relationship assertions.

This is a gate-completion review, not an assertion that the world graph or any
individual ecosystem is complete. Every expansion remains bounded to a precise
public source, canonical owner, relationship predicate, and documented
limitation. Unknown participants, funding, current roles, governance, and
opportunities are not converted into negative conclusions or inferred facts.

## Published QG2 migration cohort

| Slice | New graph capability | Review record |
| --- | --- | --- |
| [NCCR MARVEL funding](../docs/nccr-marvel-funding-vertical-slice.md) | Funder organization → funding programme → historical ecosystem connection | [NCCR MARVEL review](nccr-marvel-funding-vertical-slice-review.md) |
| [NoMaD Laboratory project](../docs/nomad-laboratory-project-vertical-slice.md) | Organization coordinator → completed project → historical software and area relations | [NoMaD Laboratory review](nomad-laboratory-project-vertical-slice-review.md) |
| [Northwestern MSE Department](../docs/northwestern-mse-department-vertical-slice.md) | Department → University and area, plus an administrative group context that preserves the direct host | [Northwestern MSE review](northwestern-mse-department-vertical-slice-review.md) |
| [Horizon 2020–NoMaD funding](../docs/horizon-2020-nomad-funding-vertical-slice.md) | European Commission → funding programme → completed project | [Horizon 2020–NoMaD review](horizon-2020-nomad-funding-vertical-slice-review.md) |
| [FAIRmat Users Meeting](../docs/fairmat-users-meeting-vertical-slice.md) | Ecosystem → completed event → research area and country context | [FAIRmat Users Meeting review](fairmat-users-meeting-vertical-slice-review.md) |

## Coverage established

| Entity type | Reviewed records | Relationship contribution |
| --- | ---: | --- |
| Principal Investigator | 10 | Leadership, affiliation, and research-area paths from the QG1 Anchor Cohort. |
| Research Group | 11 | Direct University/Organization hosts, areas, and software-development contexts. |
| University | 6 | Group hosts, Department endpoint, and country context. |
| Country | 6 | Location/filter endpoints for Universities, Organizations, and events. |
| Research Area | 2 | Group, Department, Project, and Conference subject paths. |
| Research Software | 6 | Group and completed-project development contexts, separated from ecosystems. |
| Research Ecosystem | 7 | Software, people, groups, funding-program, and event connections. |
| Organization | 7 | Research-institute, funder, coordinator, and programme-administration contexts. |
| Funding Program | 2 | Bounded programme administration and one dated programme-to-project funding relation. |
| Project | 1 | Completed NoMaD Laboratory record with coordinator, software, area, and funding endpoints. |
| Department | 1 | Administrative context distinct from a group's direct host. |
| Conference | 1 | Completed FAIRmat Users Meeting with ecosystem and research-area connections. |

The gate did not add a Publication record. Publication is not required by the
QG2 execution list, and its future addition must have a distinct citable
identity and source-backed project, software, person, or area relation rather
than being created merely to populate a type.

## Relationship coverage

The reviewed graph uses 12 typed predicates: `administers`,
`affiliated_with`, `belongs_to`, `connects`, `covers`, `develops`, `funds`,
`includes`, `involves`, `leads`, `located_in`, and `works_on`. The QG2 slices
specifically exercised `administers`, `funds`, `involves`, and `covers` in
addition to the established PI/group/software relations.

Every reviewed Research Group continues to satisfy ADR 0006: exactly one
direct University or Organization host and exactly one matching evidence-
bearing `belongs_to` assertion. A Department relation, where present, remains
separate administrative context rather than a second host.

## Quality and boundary review

| Gate rule | Review result |
| --- | --- |
| Canonical ownership | Passed. Each new fact has one owner under `entities/`; reports and indexes link without copying entity profiles. |
| Evidence before inference | Passed. Funding, project, Department, and event claims are tied to record-local sources and explicit time windows where relevant. |
| Direct-host integrity | Passed. Department context did not alter a group's required direct University or Organization host. |
| Time awareness | Passed. Completed 2015–2018 project/funding and 2026 event facts retain their dates and are not presented as current availability. |
| Frozen architecture | Passed. Existing schema fields and documented predicates were exercised; no architecture redesign, new type, or parallel store was introduced. |
| Views boundary | Passed. Records document future reachability only; no manual or generated result view was fabricated. |
| Automation boundary | Preserved. QG2 used one-off review checks only; persistent validation, generation, and health tooling remain deferred to QG6. |

## Exit evidence and QG3 handoff

The final QG2 corpus check passed at 60 v2 entities and 101 typed assertions.
It covered schema/date shape, unique IDs, documented predicate target types,
record-local source resolution, direct-host cardinality and target type,
matching direct `belongs_to` assertions, changed-document local links,
whitespace, schema JSON parsing, and ADR 0006 University/Organization branch
cases.

Quality Gate 3 begins from this graph. It must deepen first-class software
ecosystems with the documented roles in the constitution—purpose, architecture,
scope, programming stack where an approved canonical path exists, maintainers,
contributors, hosts, groups, publications, funding, community, contribution
workflow, user journey, dependencies, and related ecosystems—without filling
unknown fields, creating speculative people, or duplicating current records.

## Known limitations carried forward

- The graph is deliberately sparse; it is neither a coverage map nor a ranking.
- Programming-language entities and relationships remain deferred by the
  existing vNext contract.
- Source IDs remain record-local citation keys rather than a first-class source
  entity graph.
- Persistent graph validation and generated views remain out of scope until
  Quality Gate 6 and Quality Gate 5 respectively.
