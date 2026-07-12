# Quality Gate 1 review: canonical knowledge expansion

**Gate status:** complete
**Review date:** 2026-07-12
**Scope:** the published vNext canonical records under `entities/` and their
eleven reviewed vertical slices.

## Gate outcome

Quality Gate 1 established and exercised a reusable, evidence-first migration
pattern for high-value research-ecosystem knowledge. The reviewed corpus now
contains 52 v2 canonical entities and 87 typed, evidence-bearing relationship
assertions. It preserves legacy dossiers and reports in place while making each
new reusable public fact owned by exactly one record under `entities/`.

This is a completion review for the gate, not a claim that the global graph is
complete. The next gate expands connections into projects, funding,
conferences, and other supported entities without weakening the canonical or
evidence boundaries established here.

## Published migration cohort

| Slice | Canonical path exercised | Review record |
| --- | --- | --- |
| [AiiDA](../docs/reference-implementation.md) | Software → ecosystem → PI → group → organization → country → area | [Reference implementation review](reference-implementation-review.md) |
| [Materials Project](../docs/materials-project-vertical-slice.md) | Software → ecosystem → PI → group → organization → country → area | [Materials Project review](materials-project-vertical-slice-review.md) |
| [OQMD](../docs/oqmd-wolverton-vertical-slice.md) | Ecosystem → PI → group → university → country → area | [OQMD review](oqmd-wolverton-vertical-slice-review.md) |
| [AFLOW](../docs/aflow-curtarolo-vertical-slice.md) | Software → ecosystem → PI → group → university → country → area | [AFLOW review](aflow-curtarolo-vertical-slice-review.md) |
| [Materialyze.AI](../docs/materialyze-ai-vertical-slice.md) | PI → group → university → country → areas → existing software/ecosystem | [Materialyze.AI review](materialyze-ai-vertical-slice-review.md) |
| [Hacking Materials](../docs/hacking-materials-vertical-slice.md) | PI → group → existing organization, country, area, and ecosystem | [Hacking Materials review](hacking-materials-vertical-slice-review.md) |
| [THEOS / Materials Cloud](../docs/theos-vertical-slice.md) | PI → group → university → country → ecosystem → software | [THEOS review](theos-vertical-slice-review.md) |
| [FAIRmat / NOMAD](../docs/fairmat-draxl-vertical-slice.md) | PI → group → university → country → ecosystem → software → area | [FAIRmat review](fairmat-draxl-vertical-slice-review.md) |
| [RIKEN Computational Materials Science](../docs/riken-yunoki-vertical-slice.md) | PI → group → organization → country → area | [RIKEN CMS review](riken-yunoki-vertical-slice-review.md) |
| [RIKEN Polymeromics](../docs/riken-polymeromics-vertical-slice.md) | PI → group → organization → country → area → software | [RIKEN Polymeromics review](riken-polymeromics-vertical-slice-review.md) |
| [ASE / DTU CAMD](../docs/ase-dtu-vertical-slice.md) | Software → ecosystem → group → university → country → area | [ASE–DTU CAMD review](ase-dtu-vertical-slice-review.md) |

## Reusable migration pattern

Every reviewed slice followed the same bounded process:

1. Start from a high-value, first-party evidence trail and define the smallest
   useful canonical graph.
2. Reuse an existing canonical entity where its identity and relationship are
   already supported; create a new record only where it has a distinct owner.
3. Put reusable facts and record-local `SRC-*` citations in the entity record;
   retain applicant-specific analysis and historical interpretations in their
   legacy locations.
4. Add only one-way, typed `relationship_assertions` whose subject, target,
   predicate, and local source are all explicit.
5. For every reviewed research group, resolve exactly one direct host and add
   the matching evidence-bearing `belongs_to` assertion under ADR 0006.
6. Document graph reachability for future views without adding hand-maintained
   view results or copied profiles.
7. Review the slice's deliberate omissions, run the one-off corpus checks,
   and publish the record, slice explanation, and review together.

## Coverage established

| Entity type | Reviewed records | Gate evidence |
| --- | ---: | --- |
| Principal Investigator | 10 | The Anchor Cohort is represented by reviewed PI records with bounded affiliations, leadership, and research-area assertions. |
| Research Group | 11 | Every reviewed group has a direct University or Organization host and a matching `belongs_to` assertion. |
| Research Software | 6 | Software nodes distinguish code artifacts from broader ecosystems where the sources support that distinction. |
| Research Ecosystem | 7 | Ecosystem nodes connect only the reviewed software, groups, people, and organizations supported by their own citations. |
| University | 6 | University records provide direct hosts and country endpoints without becoming duplicated group profiles. |
| Organization | 4 | Research-institute and national-laboratory hosts are represented separately from Universities. |
| Country | 6 | Countries are location/filter endpoints rather than parent directories for graph content. |
| Research Area | 2 | Controlled areas are reused through typed relations; no speculative taxonomy expansion was performed. |

The cohort includes no reviewed `funding-program`, `project`, `conference`,
`department`, or `publication` records. Those types require their own
evidence-bounded QG2 expansions; their absence is unknown coverage, not a
negative conclusion about any existing group or ecosystem.

## Quality and boundary review

| Gate rule | Review result |
| --- | --- |
| Canonical ownership | Passed. New reusable public facts are owned by records under `entities/`; reports, legacy dossiers, and views link rather than duplicate them. |
| Evidence before inference | Passed. Reviewed records carry record-local sources; unsupported individual-maintainer, exclusive-ownership, opportunity, and mentorship claims are omitted. |
| Frozen architecture | Passed. QG1 used the accepted entity, relationship, metadata, and host contracts. No architecture redesign or new parallel system was introduced. |
| Small vertical slices | Passed. Each cohort was independently documented and reviewed; the corpus was not mass-migrated. |
| Documentation and navigation | Passed. Each slice has a canonical graph explanation, limitations, review record, and entity-directory navigation. |
| View boundary | Passed. Future reachability is documented, but no generated or hand-maintained view output was fabricated. |
| Automation boundary | Preserved. One-off QG1 corpus checks were used for review; no persistent validator, migration utility, or generated-view tooling was added before QG6. |

## Exit evidence and QG2 handoff

The last QG1 corpus check passed against the published ASE/DTU cohort with 52
v2 entities and 87 typed assertions. It covered schema/date shape, unique
identifiers, predicate target types, record-local source resolution, direct-
host cardinality and target type, matching `belongs_to` assertions, changed-
document local links, whitespace, schema JSON parsing, and ADR 0006's
University and Organization host branches.

Quality Gate 2 begins from this reviewed graph. The first QG2 work must select
new nodes and edges only where current sources support a precise relationship,
reuse the QG1 migration pattern, and retain the same review/commit/publish
discipline.

## Known limitations carried forward

- Record-local source keys remain an accepted QG1 provenance convention, not a
  first-class source/evidence graph.
- Programming-language records, generated views, and persistent validators are
  deferred by the frozen execution sequence.
- Coverage is intentionally sparse and should not be read as a ranked or
  exhaustive map of computational-materials research.
