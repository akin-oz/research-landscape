# Entity-oriented knowledge model

> **Status:** vNext architecture. This document defines the target model only; it does not move records, rename existing directories, or change the current JSON Schemas.

## Purpose

Research Landscape is a document-backed knowledge graph: one canonical Markdown record per real-world entity, machine-readable YAML frontmatter, stable IDs, and typed, evidence-bounded links between records. It remains Markdown-first, Git-friendly, human-readable, and usable by future automation without requiring a database, Neo4j, or a web application.

The primary unit of organization is an entity, not a location. A country is a useful entity and filter, but it is not the repository's hierarchy root. The same principal investigator, software project, or research ecosystem can therefore appear in a country, university, research-area, software, and personal view without copying its facts.

## Model rules

1. A canonical entity has one Markdown document and one immutable internal `id`.
2. YAML frontmatter holds structured, machine-readable facts; the Markdown body holds context, evidence, limitations, and editorial reasoning.
3. Relationships use stable IDs rather than copied names or embedded profiles. See the [relationship model](relationships.md).
4. A fact that is absent or not public is omitted; absence is not a negative claim. Explicit `unknown` is reserved for a value that was reviewed but could not be established.
5. Source IDs, confidence, evidence windows, and review dates travel with claims so future views can expose uncertainty rather than manufacture precision.
6. Views organize and filter entities. They never become a second source of entity data.

The current [data-model entity contract](../data-model/entity-model.md), [frontmatter specification](../specifications/frontmatter.md), and [stable-ID rules](../data-model/stable-identifiers.md) remain authoritative for records already covered by their schemas.

## Canonical record shape

Every vNext entity uses the common identity, lifecycle, review, and evidence envelope in [vNext entity metadata](metadata.md): `schema_version: 2`, `entity_type`, `id`, `name`, `status`, `created_at`, `updated_at`, `last_review`, and `confidence`. IDs follow the current uppercase, hyphenated stable-ID convention; display names and paths may change without changing an ID.

The vNext metadata contract uses normalized `_id` and `_ids` references as canonical graph joins. The brief's human-readable context names—such as country, institution, department, research group, research area, software, and programming language—are resolved from those target entities in a display or view. They are not duplicate free-text relationship fields in canonical metadata.

```yaml
---
schema_version: 2
id: PI-ANUBHAV-JAIN
entity_type: principal-investigator
name: Anubhav Jain
status: draft
created_at: "2026-07-11"
updated_at: "2026-07-11"
last_review: "2026-07-11"
confidence: unassessed
source_ids: []

# Normalized location and affiliation context.
country_id: COUNTRY-US
city: Berkeley
department_id: DEPARTMENT-LBNL-ETA
affiliation_ids: [ORGANIZATION-LBNL]
organization_ids: [ORGANIZATION-LBNL]
research_group_ids: [RESEARCH-GROUP-MATERIALS-PROJECT]

career_stage: senior
research_area_ids: [RESEARCH-AREA-MATERIALS-INFORMATICS]
software_ids: [RESEARCH-SOFTWARE-PYMATGEN]
programming_language_ids: [PROGRAMMING-LANGUAGE-PYTHON]

github: https://github.com/example
orcid: https://orcid.org/0000-0000-0000-0000
google_scholar: https://scholar.google.com/citations?user=example
website: https://example.org

# Use quoted controlled states only when a review supports the value.
accepting_msc: "unknown"
accepting_phd: "unknown"
international_students: "unknown"
working_language_codes: [en]
remote_collaboration: "unknown"
industry_collaboration: "unknown"

---
```

This example is a target design, not a claim that the shown values are current or that every field applies to every entity. It conforms to the proposed [`entity-vnext.schema.json`](../../schemas/entity-vnext.schema.json) shape, which is not yet CI-enforced. Current v1 schemas intentionally retain earlier names such as `advisor`, `lab`, `group_ids`, and `language_ids`.

### Metadata groups

| Group | Fields | Rule |
| --- | --- | --- |
| Identity, lifecycle, and review | `schema_version`, `id`, `entity_type`, `name`, `status`, `created_at`, `updated_at`, `last_review`, `confidence` | Required on every vNext entity. |
| Location and host context | `country_id`, `city`, `institution_id`, `institution_ids`, `organization_id`, `organization_ids`, `department_id`, `research_group_ids` | Stable IDs are canonical. Views resolve human-readable country, institution, department, and group names from those IDs. |
| Discovery and fit | `career_stage`, `research_area_ids`, `software_ids`, `programming_language_ids`, `open_source`, `accepting_msc`, `accepting_phd`, `international_students`, `working_language_codes`, `remote_collaboration`, `industry_collaboration` | Use controlled values and evidence; do not infer availability, language, or collaboration from a title or website. |
| Public identifiers and links | `github`, `orcid`, `google_scholar`, `website`, plus `external_ids` | Public identifiers aid reconciliation but never replace the internal stable ID. |
| Evidence and relationships | `source_ids`, `relationship_assertions` | `source_ids` are required for reviewed/published records; `relationship_assertions` carries typed, optionally dated assertions. `confidence` measures evidence quality, not an entity's quality or rank. |

## Intended entity locations

The target paths below establish an entity-oriented namespace. They are architecture targets only: existing content remains where it is until a later, incremental migration.

| Entity type | Intended directory | Canonical file example |
| --- | --- | --- |
| Principal Investigator | `entities/principal-investigators/` | `entities/principal-investigators/anubhav-jain.md` |
| Research Group | `entities/research-groups/` | `entities/research-groups/materials-project.md` |
| University | `entities/universities/` | `entities/universities/example-university.md` |
| Department | `entities/departments/` | `entities/departments/materials-science.md` |
| Country | `entities/countries/` | `entities/countries/sweden.md` |
| Research Ecosystem | `entities/ecosystems/` | `entities/ecosystems/materials-project.md` |
| Research Software | `entities/research-software/` | `entities/research-software/pymatgen.md` |
| Programming Language | `entities/programming-languages/` | `entities/programming-languages/python.md` |
| Research Area | `entities/research-areas/` | `entities/research-areas/materials-informatics.md` |
| Conference | `entities/conferences/` | `entities/conferences/materials-research-society.md` |
| Funding Program | `entities/funding/` | `entities/funding/horizon-europe.md` |
| Project | `entities/projects/` | `entities/projects/example-project.md` |
| Publication | `entities/publications/` | `entities/publications/example-publication.md` |
| Organization | `entities/organizations/` | `entities/organizations/lawrence-berkeley-national-laboratory.md` |

## First-class entities

All entries below require the common identity and lifecycle metadata. The [canonical entity-specific requirements](metadata.md#canonical-entity-specific-requirements) are the single normative source for future-schema rules; the summaries below explain their research meaning. Optional fields are recorded only when public evidence supports them.

### Principal Investigator

**Purpose.** A publicly documented research leader responsible for a research direction, group, project, or supervision context. It is not a claim that the person is accepting applicants.

**Required metadata.** At least one of `institution_id` or `organization_ids`, plus `career_stage` when it has been reviewed. Public `orcid`, `website`, `research_area_ids`, and `research_group_ids` are strongly preferred when available.

**Relationships.** Belongs to research groups and/or organizations, develops or maintains research software, works on research areas, collaborates with organizations, speaks at conferences, participates in projects, and authors publications.

**Example.** `PI-ANUBHAV-JAIN` in `entities/principal-investigators/anubhav-jain.md` can reference `GRP-MATERIALS-PROJECT`, `SW-PYMATGEN`, and `AREA-MATERIALS-INFORMATICS` without copying those records.

### Research Group

**Purpose.** A named lab, center, or durable research unit with a public research identity. It can have multiple leaders and members over time.

**Required metadata.** A reviewed or published group has exactly one direct
host: `institution_id` resolving to a University, or `organization_id`
resolving to a non-university Organization. `department_id` may add evidenced
administrative context but cannot replace or duplicate the direct host.
`principal_investigator_ids`, `research_area_ids`, and `website` are included
when evidenced.

**Relationships.** Belongs to its one direct University or Organization host;
may additionally identify an evidenced Department context; includes principal
investigators; uses research software; works on research areas; participates in
ecosystems and projects; and produces publications.

**Example.** `GRP-MATERIALS-PROJECT` in `entities/research-groups/materials-project.md` is one group record even when it appears in several software or country views.

### University

**Purpose.** A degree-granting university or comparable higher-education institution.

**Required metadata.** `country_id`. `ror`, `website`, and city are recorded when known.

**Relationships.** Is located in a country; hosts departments, research groups, principal investigators, projects, conferences, and ecosystem activity; and may administer funding or collaboration programs.

**Example.** `UNI-EXAMPLE` in `entities/universities/example-university.md` can be the host referenced by many department and group records.

### Department

**Purpose.** An academic unit within a university, regardless of whether the institution calls it a school, faculty, institute, or department.

**Required metadata.** `institution_id`, which resolves to the hosting University record. `website` is optional because institutional structures vary.

**Relationships.** Belongs to a university; hosts or administers research groups, principal investigators, projects, and programs; and works on research areas.

**Example.** `UNI-EXAMPLE-MSE-DEPT` in `entities/departments/materials-science.md` points to `UNI-EXAMPLE` rather than repeating the university's country or web address.

### Country

**Purpose.** A normalized national context for geography, policy, and filtering—not the primary owner of all records within its borders.

**Required metadata.** `country_code` using ISO 3166-1 alpha-2. `iso_numeric` and `region` are optional supporting fields.

**Relationships.** Universities, organizations, conferences, funding programs, and people with relevant public location evidence are `located_in` a country. A country can also be a target of geographic views.

**Example.** `SE` in `entities/countries/sweden.md` supports a Sweden view without nesting every Swedish entity below it.

### Research Ecosystem

**Purpose.** A durable research network centered on a shared platform, infrastructure, collaboration, or community, such as Materials Project, AiiDA, Materials Cloud, NOMAD, AFLOW, Open Catalyst Project, ASE, pymatgen, Quantum ESPRESSO, or LAMMPS.

**Required metadata.** `website` and at least one evidenced connection through `software_ids`, `community_ids`, `organization_ids`, or `project_ids`.

**Relationships.** Connects principal investigators, research groups, research software, universities and other organizations, funding programs, projects, communities, and conferences. It is a first-class node rather than a tag applied to unrelated pages.

**Example.** `ECO-MATERIALS-PROJECT` in `entities/ecosystems/materials-project.md` can link a maintainer, a hosted software package, funder, workshop, and contributing group in one evidence-backed network.

### Research Software

**Purpose.** A research-relevant executable package, library, workflow, platform, or codebase with a distinct public identity.

**Required metadata.** At least one of `repository_url` or `website`; `license` when publicly stated. `programming_language_ids` and `ecosystem_ids` are recorded when evidenced.

**Relationships.** Is developed or maintained by principal investigators, organizations, or groups; is used by research groups; is implemented in programming languages; supports research areas; appears in publications and projects; and may anchor a research ecosystem.

**Example.** `SW-PYMATGEN` in `entities/research-software/pymatgen.md` can link maintainers and users separately, avoiding an unsupported assumption that every user is a maintainer.

### Programming Language

**Purpose.** A controlled language concept used only to connect documented
Research Software implementation evidence.

**Required metadata.** `label` and an identity source. A
`programming_language_ids` convenience facet on Research Software is valid
only when a matching sourced `implemented_in` assertion exists.

**Relationships.** Receives `implemented_in` assertions from Research
Software. The inverse is generated for navigation; it must not be stored as a
second assertion.

### Research Area

**Purpose.** A reusable, controlled subject concept used for navigation and comparison rather than a free-form keyword cloud.

**Required metadata.** No domain field beyond common `name`, which is the controlled canonical label. A formal broader/narrower taxonomy is deferred until a versioned field is added to the vNext contract.

**Relationships.** Is worked on by people and groups, supported by software, addressed by projects and publications, and covered by conferences. Areas may be broader or narrower than other areas.

**Example.** `AREA-MATERIALS-INFORMATICS` in `entities/research-areas/materials-informatics.md` can classify records across countries and ecosystems.

### Conference

**Purpose.** A recurring conference series, workshop, or separately identified event relevant to research communities.

**Required metadata.** `website`; use `country_id`, `institution_ids`, and `organization_ids` when a public location or organizer is known. A future event-edition extension can add date and series fields without changing the conference identity.

**Relationships.** Is hosted by an organization, located in a country for a specific edition, covers research areas, features speakers, convenes ecosystems, and may publish proceedings.

**Example.** `CONF-EXAMPLE-SERIES` in `entities/conferences/example-conference.md` may receive dated `speaks_at` links from principal investigators without claiming an ongoing affiliation.

### Funding Program

**Purpose.** A public funder initiative, call family, or structured funding mechanism; it is distinct from an individual awarded project.

**Required metadata.** At least one of `organization_ids` or `institution_id`, plus an official `website` or public program identifier in `external_ids`.

**Relationships.** Is administered by an organization, funds projects, supports ecosystems and communities, and may have geographic or research-area scope.

**Example.** `FUND-EXAMPLE-PROGRAM` in `entities/funding/example-program.md` can fund many projects without duplicating funder details into each project.

### Project

**Purpose.** A time-bounded or otherwise discrete research activity, whether funded, collaborative, software-focused, or infrastructure-focused.

**Required metadata.** The common `name`, at least one `institution_id` or `organization_ids`, and `funding_program_ids` when funding is evidenced. Time-bound project fields require a future versioned extension rather than unvalidated ad hoc keys.

**Relationships.** Is funded by funding programs, involves people, groups, and organizations, works on research areas, develops or uses software, contributes to ecosystems, and produces publications or datasets.

**Example.** `PROJ-EXAMPLE-001` in `entities/projects/example-project.md` can preserve start/end dates and evidence for a collaboration after its participants change affiliation.

### Publication

**Purpose.** A distinct scholarly output, including an article, preprint, conference paper, book, chapter, thesis, dataset, software release, or other citable work.

**Required metadata.** The common `name` as the canonical title, plus `external_ids` for a DOI or other persistent identifier when available. The existing v1 publication schema remains the bibliographic source of truth until vNext adds versioned publication-specific fields.

**Relationships.** Is authored by principal investigators and other recorded contributors, describes projects or software, addresses research areas, and may be associated with a conference or ecosystem.

**Example.** `PUB-EXAMPLE-001` in `entities/publications/example-publication.md` references author IDs rather than embedding biographies or duplicate citation records.

### Organization

**Purpose.** A general-purpose institution, institute, laboratory, company, nonprofit, funder, publisher, or community body that is not better represented by a specialized first-class entity.

**Required metadata.** `country_id` when a location is meaningful. `website` and external identifiers such as ROR are included when available; a controlled organization-kind extension requires a future schema version.

**Relationships.** Is located in a country; hosts or employs people and groups; administers funding programs, projects, and conferences; collaborates with principal investigators; and participates in ecosystems.

**Example.** `ORG-LBNL` in `entities/organizations/lawrence-berkeley-national-laboratory.md` can be the accountable host for groups and the collaborator on projects.

Do not create both a University and a generic Organization record merely to describe the same institution. Use the specialized University record where it is the appropriate identity, and reserve Organization for a distinct legal, operating, or partner entity.

## Entity graph

The graph below shows the central navigation paths. A Research Group has one
direct host: the University and Organization paths are alternatives, not
concurrent direct-host claims. Edge labels are defined precisely in the
[relationship model](relationships.md).

```mermaid
flowchart LR
  PI[Principal Investigator]
  RG[Research Group]
  U[University]
  D[Department]
  C[Country]
  E[Research Ecosystem]
  S[Research Software]
  A[Research Area]
  CON[Conference]
  F[Funding Program]
  P[Project]
  PUB[Publication]
  O[Organization]

  PI -->|belongs_to| RG
  RG -->|belongs_to (direct host)| U
  RG -->|belongs_to (direct host)| O
  RG -->|belongs_to (administrative context)| D
  D -->|belongs_to| U
  U -->|located_in| C
  PI -->|develops| S
  PI -->|works_on| A
  PI -->|collaborates_with| O
  PI -->|speaks_at| CON
  S -->|used_by| RG
  F -->|funds| P
  P -->|produces| PUB
  P -->|involves| RG
  PUB -->|addresses| A
  E -->|connects| PI
  E -->|connects| RG
  E -->|connects| S
  E -->|connects| F
  E -->|connects| CON
```

## Compatibility and migration boundary

This proposal deliberately does not rewrite the current model. The following bridge keeps the architecture legible while a later versioned migration is designed:

| vNext concept | Current schema/model term | Architecture decision now |
| --- | --- | --- |
| Principal Investigator | `advisor` | Treat as the successor concept; do not rename existing `advisor` records in this change. |
| Research Group | `lab` | Treat as the successor concept; preserve v1 fields until an evidence-reviewed migration selects the one vNext direct host by target type. |
| Project and Funding Program | `funding-project` | Split the conceptual program from individual project only when versioned schemas and evidence support it. |
| University, Department, Country, Research Area, Research Software, Publication | Same or closely matching current terms | Reuse current stable-ID and evidence conventions; extend only through a versioned schema proposal. |
| Faculty, graduate program, programming language, dataset | Existing supporting entities | Keep them available as satellites; they are not removed by this 13-entity core. |

No current file is moved, renamed, or silently reclassified. Until a future schema release, current records continue to use only fields accepted by their existing schemas, and new logical views can be documented without duplicating entity content.
