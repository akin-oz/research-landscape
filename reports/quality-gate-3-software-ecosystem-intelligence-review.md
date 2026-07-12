# Quality Gate 3 review: software ecosystem intelligence

**Gate status:** complete
**Review date:** 2026-07-12
**Scope:** the seven existing reviewed vNext Research Ecosystems and their
canonical software, group, PI, funding, project, event, and publication context.

## Gate outcome

Quality Gate 3 deepened every existing canonical research ecosystem into an
evidence-bounded software or data-ecosystem intelligence slice. The published
vNext corpus now contains 67 entities and 116 typed, evidence-bearing
relationship assertions, including seven canonical technical-publication
records. The gate does not claim global coverage, complete teams, or a complete
software map. It proves that the current canonical ecosystem cohort can expose
purpose, technical architecture, people and institutional context, publication,
funding boundary, contribution path, user journey, and career-relevant learning
surfaces without duplicating facts or inferring unknowns.

## Published QG3 cohort

| Ecosystem | Intelligence scope | Review record |
| --- | --- | --- |
| [AiiDA](../docs/aiida-ecosystem-intelligence-vertical-slice.md) | Workflow/provenance core, plugins, compute, sharing, NCCR MARVEL context, and AiiDA 1.0 paper. | [AiiDA review](aiida-ecosystem-intelligence-vertical-slice-review.md) |
| [Materials Project](../docs/materials-project-ecosystem-intelligence-vertical-slice.md) | High-throughput workflow → data → builders → API context, pymatgen user/contribution path, and pymatgen paper. | [Materials Project review](materials-project-ecosystem-intelligence-vertical-slice-review.md) |
| [NOMAD / FAIRmat](../docs/nomad-ecosystem-intelligence-vertical-slice.md) | App/worker platform, data management, plugins, Oasis, contribution, historic H2020 context, and JOSS paper. | [NOMAD review](nomad-ecosystem-intelligence-vertical-slice-review.md) |
| [AFLOW](../docs/aflow-ecosystem-intelligence-vertical-slice.md) | Framework/web distinction, source/install/API path, bounded contributor context, and aflow++ paper. | [AFLOW review](aflow-ecosystem-intelligence-vertical-slice-review.md) |
| [ASE](../docs/ase-ecosystem-intelligence-vertical-slice.md) | Calculator workflow, Python/CLI/GUI, GitLab contribution/community context, and 2017 paper. | [ASE review](ase-ecosystem-intelligence-vertical-slice-review.md) |
| [OQMD](../docs/oqmd-ecosystem-intelligence-vertical-slice.md) | REST/OPTIMADE and download data paths, provenance/citation context, and 2015 paper. | [OQMD review](oqmd-ecosystem-intelligence-vertical-slice-review.md) |
| [Materials Cloud](../docs/materials-cloud-ecosystem-intelligence-vertical-slice.md) | Research-cycle platform, moderated data deposition, Archive context, historical NCCR boundary, and 2020 paper. | [Materials Cloud review](materials-cloud-ecosystem-intelligence-vertical-slice-review.md) |

## Coverage established

| Required QG3 dimension | Gate evidence | Boundary preserved |
| --- | --- | --- |
| Purpose and scientific scope | Every slice has a source-backed QG3 coverage matrix and canonical entity prose. | A documented platform purpose never becomes an assertion about every result, user, or discipline. |
| Architecture and technical scope | All seven slices record the appropriate bounded architecture: workflows/provenance; data builders/API; app/worker; framework/API; calculators; database/API; and Archive/platform layers. | Infrastructure components remain source-backed prose unless a separate canonical entity/type contract exists. |
| Programming stack | Upstream sources identify Python and/or C++ where relevant. | No Language entity/relationship is created before the approved contract exists. |
| Maintainers, contributors, institutions, and groups | Existing canonical PI/group/organization connections are retained; documented contributor and project-leader roles are added only where a source directly supports them. | A paper author list, public repository, group, or platform connection is not converted into an exhaustive or current maintainer roster. |
| Publications | Seven reviewed publications provide persistent dates/DOIs and ten `authored_by` assertions to already reviewed PI identities where available. | Publication records do not manufacture author entities. Two ecosystem-target papers intentionally omit `describes` because the predicate contract excludes Research Ecosystem targets. |
| Funding | Historical NCCR MARVEL and Horizon 2020/NoMaD project context remains typed and dated. | DOE/NFDI/institutional/paper acknowledgements without the necessary reviewed programme/funder relationship remain documented limitations, not fabricated edges. |
| Repository and contribution paths | AiiDA, pymatgen/Materials Project, NOMAD, AFLOW, ASE, and Materials Cloud expose documented source, issue/PR, plugin, or moderated-data-deposition routes. | OQMD's reviewed sources expose access/download but no public code-contribution path; this absence is explicitly recorded rather than inferred. |
| Community and typical user journey | Every slice maps source-backed routes from learning or setup through use, sharing, querying, extension, or deposition. | No user access, response, support, acceptance, contributor-status, or outcome promise is implied. |
| Career relevance | Each slice identifies technical learning/contribution surfaces tied to real research infrastructure. | No job, admission, mentoring, ranking, supervision, or applicant-fit conclusion is encoded. |
| Dependencies and related ecosystems | Existing direct software/ecosystem/group/funding relationships remain typed; cross-ecosystem context is described in evidence-bearing prose. | The frozen schema lacks safe dependency/community types and an ecosystem-to-ecosystem predicate, so no speculative edges are added. |

## Canonical graph gain

Quality Gate 3 added seven Publication records and fifteen typed assertions:

| New record or relationship family | Count | Evidence discipline |
| --- | ---: | --- |
| Publication records | 7 | Each has a persistent date, DOI, record-local citation, and limitation statement. |
| `authored_by` assertions | 8 | Each target is an already reviewed PI, not a newly fabricated author identity. |
| `describes` assertions | 5 | Added only when the paper's subject is an existing Research Software target. |
| Ecosystem contributor connection | 1 | AFLOW → Stefano Curtarolo, bounded to the official contributor listing. |
| Historical funding-support connection | 1 | AiiDA → NCCR MARVEL, bounded to the official acknowledgement evidence. |

The remaining publication records concern Research Ecosystems rather than
Research Software or Projects. Their technical subject is documented in the
publication and slice prose, but no unsupported `describes` assertion is added.

## Quality and boundary review

| Gate rule | Review result |
| --- | --- |
| Canonical ownership | Passed. Facts continue to live once in `entities/`; slices and reports link to canonical records rather than copy profile data. |
| Evidence before inference | Passed. Every new entity and assertion uses record-local `SRC-*` evidence; gaps are described as limitations. |
| Ecosystem/software distinction | Passed. Materials Project/pymatgen, AFLOW/framework, ASE/software, AiiDA/core, NOMAD/FAIRmat, and Materials Cloud/AiiDA remain distinct. OQMD remains ecosystem-only until an independently scoped backend software record is reviewed. |
| Time awareness | Passed. Historical H2020, NCCR MARVEL, publication, and event context remain dated; no ended programme is presented as current funding. |
| Frozen architecture | Passed. The gate adds no entity type, predicate, ADR, schema redesign, migration, persistent validator, or generated view. |
| Unknowns | Passed. Maintainer rosters, contributors, dependency graphs, programming-language IDs, community nodes, career outcomes, funding gaps, support commitments, and applicant-fit claims remain omitted or explicitly bounded. |
| Discoverability | Passed. Each ecosystem now has a stable canonical entry point, a QG3 coverage matrix, review record, publication record where justified, and traversable links to software, people, groups, funding, and projects. |

## Exit evidence and Quality Gate 4 handoff

The final QG3 corpus check passed at 67 v2 entities and 116 typed assertions.
It covered vNext schema/date shape, unique IDs, legal predicate target types,
record-local source resolution, direct-host cardinality and target type,
matching direct `belongs_to` assertions, changed-document local links,
whitespace, schema JSON parsing, and the ADR 0006 University/Organization
positive and negative branch cases.

Quality Gate 4 can now deepen the global PI and research-group network from
these evidence-bearing ecosystem entry points. It should add one independently
reviewed PI/group/institutional cohort at a time, with direct evidence for
current affiliation, research scope, host identity, software role, funding or
project context where applicable, and explicit mentorship/opportunity
boundaries. It must not turn QG3's public contribution surfaces into claims
about individual supervision, hiring, admissions, or career outcomes.

## Known limitations carried forward

- This is a complete review of the current seven-ecosystem canonical cohort,
  not a global coverage or quality ranking.
- Programming Language, Community, dependency, API endpoint, package,
  workflow, component, and detailed Maintainer entities are still absent from
  the approved vNext contract.
- `describes` intentionally cannot target a Research Ecosystem; this limits
  direct publication-to-ecosystem graph edges without an architecture review.
- Source IDs remain record-local citations rather than first-class Source
  entities.
- Persistent graph validation and generated views remain deferred to QG6 and
  QG5 respectively.
