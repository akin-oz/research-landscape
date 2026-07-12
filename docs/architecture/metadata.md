# vNext entity metadata

This document specifies the proposed vNext YAML frontmatter profile for Markdown-first entity records. It normalizes the fields needed for cross-entity navigation while keeping relationships as stable IDs. It is an architecture contract, not a migration: existing records and the v1 JSON Schemas remain valid and authoritative until versioned vNext schemas are introduced.

## Design rules

- Every entity has one immutable `id`, one controlled `entity_type`, one canonical `name`, lifecycle metadata, and evidence context.
- Relationship fields use stable IDs with `_id` or `_ids` suffixes. Never put a duplicated entity object or a display name in a relationship field.
- Scalar facts belong in the entity that owns them. Views may calculate reverse links but must not duplicate entity metadata.
- Omit an unknown relationship. Use an explicit controlled `unknown` value only where a field's semantics require a reviewed answer.
- Dates use ISO 8601 calendar dates (`YYYY-MM-DD`) quoted in YAML so they remain strings for JSON Schema validation; URLs are canonical public URLs where available, and IDs use the project stable-ID format.

## Required common fields

| Field | Requirement | Semantics and controlled values |
| --- | --- | --- |
| `schema_version` | Required | Integer metadata-contract version. The proposed profile is `2`; use it only for a new `entities/` record validated against the vNext schema, never by silently relabelling a v1 record. |
| `entity_type` | Required | One of the controlled vNext values below. |
| `id` | Required | Immutable, project-issued stable ID; uppercase ASCII segments separated by hyphens. Never derive it from a score, rank, or mutable title. |
| `name` | Required | Canonical public display name. |
| `status` | Required | `draft`, `reviewed`, `published`, or `retired`. |
| `created_at` | Required | Date the repository record was first created. |
| `updated_at` | Required | Date the record's content last changed. |
| `last_review` | Required | Date an editor last evaluated factual freshness and source coverage. Use the creation/review date for a new draft and update it only after a real review. It is not a claim about the entity's real-world activity. |
| `confidence` | Required | `high`, `medium`, `low`, or `unassessed`, describing evidence confidence rather than perceived quality. New drafts normally use `unassessed`. |
| `source_ids` | Required for reviewed/published records; optional for a draft | Stable IDs of source/evidence records when such records are available. The Markdown body retains citations and rationale. |

The distinct `updated_at` and `last_review` fields matter: a formatting edit may update the former, while a freshness review may update the latter without changing a substantive fact.

## Controlled vNext entity types

| vNext `entity_type` | Purpose |
| --- | --- |
| `principal-investigator` | Publicly identified research leader, supervisor, or independent investigator. |
| `research-group` | Named lab, center, or research unit. |
| `university` | Degree-granting or research institution. |
| `department` | Academic or administrative unit within an institution. |
| `country` | National or territorial context used for location and filters. |
| `research-ecosystem` | Evidence-bounded network spanning people, groups, software, institutions, communities, funding, and conferences. |
| `research-software` | Research-relevant software artifact or project. |
| `research-area` | Reusable, controlled subject concept. |
| `conference` | Scholarly conference, meeting series, or event. |
| `funding-program` | Public funding scheme, call, or funding organization programme. |
| `project` | Time-bounded research or software project, including a funded project where evidenced. |
| `publication` | Scholarly publication or research output. |
| `organization` | Non-university organization, consortium, community host, institute, funder, company, or similar accountable body. |

Supporting types such as programming languages, datasets, faculties, and graduate programmes may continue under their versioned v1 contracts until vNext adds an explicit successor. A future type change must be versioned and mapped; it must never silently reinterpret an existing record.

## Canonical entity-specific requirements

This table is the normative source for the vNext entity-specific requirement rules. [`entity-vnext.schema.json`](../../schemas/entity-vnext.schema.json) enforces the structural requirements below; the [entity model](entity-model.md) explains their research meaning. No requirement is applied to a v1 record in this architecture phase.

| `entity_type` | Required vNext metadata | Notes |
| --- | --- | --- |
| `principal-investigator` | `affiliation_ids` | Non-empty documented affiliations; group membership, current acceptance, and career stage remain separately evidenced. |
| `research-group` | For `reviewed` and `published` records, exactly one of `institution_id` or `organization_id` | The sole direct host. `institution_id` resolves to a University; `organization_id` resolves to a non-university Organization. `department_id` is optional administrative context, not a substitute or second host. |
| `university` | `country_id` | Country is a location/filter relationship, not a directory parent. |
| `department` | `university_id` | `faculty_id` is optional because structures vary. |
| `country` | `country_code` | ISO 3166-1 alpha-2; `region` is optional controlled context. |
| `research-ecosystem` | `ecosystem_kind`, `website` | Software, people, funding and community links are added only with evidence. |
| `research-software` | `repository_url` **or** `website` | `license` is included whenever publicly stated; public code without a licence is not automatically open source. |
| `research-area` | `label` | `parent_id` is optional and must follow a documented controlled taxonomy. |
| `conference` | `conference_kind`, `website` | An edition additionally records `event_start_date` when it is represented as a distinct record. |
| `funding-program` | `funder_organization_id`, `funding_program_kind`, `website` | An award belongs in a Project record, not in the programme record. |
| `project` | `title`, `project_status`, `start_date`, and `host_organization_id` **or** non-empty `participant_ids` | `funding_program_ids` is added only when evidenced. |
| `publication` | `title`, `publication_date`, `publication_type` | Author and topic IDs are optional only because public metadata can be incomplete. |
| `organization` | `organization_kind` | Use University instead when that is the appropriate specialized identity. |

## Relationship and classification fields

The names below replace ambiguous text fields such as `country`, `institution`, `department`, `research_group`, `research_areas`, `software`, and `programming_languages` with normalized references. The corresponding display names are resolved from target entity records.

| Field | Applies to | Semantics |
| --- | --- | --- |
| `country_id` | Location-bearing entities | ID of the canonical Country record. A country is a filter and location endpoint, not a parent directory requirement. |
| `country_code`, `region` | Country entities | ISO 3166-1 alpha-2 code and a controlled regional classification. Other entities resolve location through `country_id` or documented relationships. |
| `city` | Location-bearing entities | Human-readable city or locality. Use the public preferred form; omit if unavailable. |
| `institution_id` | Research groups and other applicable single-host entities | ID of an accountable University. For a Research Group, it is the one direct host when the host is a University and is mutually exclusive with `organization_id`. |
| `institution_ids` | Ecosystems, conferences, funding programmes, and other multi-host entities | IDs of participating Universities where the relationship is evidenced. Use `institution_id` only where the entity-specific rule permits a singular direct University host. |
| `organization_id` | Research groups and other entities with one direct non-university host | ID of the accountable non-university Organization. For a Research Group, it is the one direct host when the host is an Organization and is mutually exclusive with `institution_id`. |
| `organization_ids` | Any applicable entity | IDs of additional accountable or collaborating Organizations. They cannot satisfy or restate a Research Group's direct-host field. |
| `department_id` | Principal investigators, groups, programmes, projects | ID of the directly associated Department. For a Research Group, it is optional administrative context and cannot substitute for its direct host. |
| `research_group_ids` | Principal investigators, software, projects, publications | IDs of associated Research Groups. Many-to-many and time-sensitive. |
| `principal_investigator_ids` | Groups, projects, software, funding programmes, publications | IDs of related Principal Investigators, with the role explained in the body or a typed relationship record. |
| `research_area_ids` | Any topical entity | IDs of controlled Research Area records. |
| `software_ids` | Ecosystems, people, groups, projects, publications | IDs of related Research Software records; use a typed relationship to distinguish develops, maintains, uses, or studies. |
| `programming_language_ids` | Software and other evidenced entities | IDs of controlled Programming Language records. |
| `mentorship_process_evidence` | Research Groups, Departments, Universities, Organizations | Bounded public process observations with a controlled category, source IDs, exact scope, evidence window or review date, confidence, and limitation. Never a score, testimonial, capacity, or outcome claim. |
| `ecosystem_ids` | Software, people, groups, organizations, projects | IDs of relevant Research Ecosystem records. |
| `community_ids` | Universities, organizations, ecosystems, software | IDs of community-hosting Organization or Research Ecosystem records. |
| `funding_program_ids` | Ecosystems, projects, groups, organizations | IDs of related Funding Program records. |
| `project_ids` | Funding programmes, ecosystems, groups, software | IDs of related Project records. |
| `conference_ids` | Ecosystems, software, groups, organizations | IDs of relevant Conference records. |
| `publication_ids` | Principal investigators, groups, projects, software | IDs of related Publication records. |
| `maintainer_ids` | Research Software and Research Ecosystems | IDs of Principal Investigators or Organizations with a documented maintenance role. |
| `contributor_ids` | Research Software, Projects, Funding Programs, and Ecosystems | IDs of documented contributors or participants. A contributor role is not inferred from affiliation. |

An `_ids` field is a unique ordered list of IDs; order is not a ranking unless a field explicitly documents that meaning. Relationship fields are omitted when unknown. Empty arrays should be used only for a deliberate, evidence-backed assertion that no currently applicable relation exists.

## Person, accessibility, and web-presence fields

These fields are applicable only where meaningful; they are optional for unrelated entity types. Values must reflect public, attributable evidence and should be accompanied by an evidence source.

| Field | Applies to | Semantics and controlled values |
| --- | --- | --- |
| `career_stage` | Principally a Principal Investigator | `early-career`, `mid-career`, `senior`, `emeritus`, `unknown`, or `not-applicable`. It is a time-bounded editorial classification, not a measure of merit. |
| `open_source` | Software, groups, projects, ecosystems | `yes`, `no`, `mixed`, `unknown`, or `not-applicable`. Use `yes` only when the relevant source code is publicly available under a stated or clearly documented open-source license. Quote these YAML values. |
| `github` | Any applicable entity | Canonical GitHub profile, organization, or repository URL; it is not evidence of employment or maintainership on its own. |
| `repository_url`, `license` | Research Software and projects | Canonical source/repository URL and stated licence. A non-GitHub repository remains first-class; a public URL without a licence is not sufficient for `open_source: "yes"`. |
| `orcid` | Principal Investigators and authors | Canonical ORCID URL, not merely a numeric string. |
| `google_scholar` | Principal Investigators and authors | Canonical public Google Scholar profile URL when it is clearly attributable. |
| `website` | Any applicable entity | Canonical official website or profile URL. |
| `accepting_msc` | Principal Investigators, groups, programmes | `yes`, `no`, `unknown`, or `not-applicable`, based on current public evidence. It does not replace an application decision. Quote these YAML values. |
| `accepting_phd` | Principal Investigators, groups, programmes | `yes`, `no`, `unknown`, or `not-applicable`, with the same evidence rule. Quote these YAML values. |
| `international_students` | Principal Investigators, groups, programmes, universities | `yes`, `no`, `unknown`, or `not-applicable`, meaning whether public information supports eligibility or participation for international students. It is not a visa guarantee. Quote these YAML values. |
| `instruction_language_codes` | Programmes and universities | Sourced BCP 47/ISO-style language codes for formal instruction, such as `en`. Omit when unreviewed. |
| `working_language_codes` | Principal Investigators, groups, projects, and organizations | Sourced language codes for day-to-day research work where explicitly stated. Do not infer from a page’s display language. |
| `remote_collaboration` | Groups, projects, programmes, and organizations | `yes`, `no`, `unknown`, or `not-applicable`, based on explicit policy or documented project practice. |
| `industry_collaboration` | Principal Investigators, groups, projects, organizations, and ecosystems | `yes`, `no`, `unknown`, or `not-applicable`, supported by a named, relevant public collaboration or project—not geography or a generic logo wall. |
| `volatile_assertions` | Any entity with a time-sensitive claim | Dated, sourced assertions for openings, GitHub activity, eligibility, remote practice, or industry collaboration. They support filters without pretending a volatile fact is a timeless entity property. |

For these availability fields, `unknown` means the record was reviewed and reliable public evidence was not found; an omitted field means it has not yet been evaluated. Use a quoted string for YAML 1.1 compatibility so `yes` and `no` cannot be coerced to booleans.

## Volatile assertions

Open positions, current repository activity, current acceptance and opportunity evidence expire. They use `volatile_assertions`, not an unsourced permanent label. Each assertion must include a subject, status, `checked_at`, `review_by`, non-empty `source_ids`, and confidence; it may also include a target entity, URL, threshold, scope, and notes.

```yaml
volatile_assertions:
  - subject: open-position
    status: open
    target_id: PROJECT-EXAMPLE-001
    url: https://example.edu/openings/example
    checked_at: "2026-07-11"
    review_by: "2026-08-11"
    source_ids: [SOURCE-EXAMPLE-OPENING]
    confidence: high
  - subject: github-activity
    status: active
    threshold: "at least one maintainer-authored repository event in the prior 90 days"
    checked_at: "2026-07-11"
    review_by: "2026-08-11"
    source_ids: [SOURCE-EXAMPLE-GITHUB]
    confidence: medium
```

The `github-activity` threshold is a view/profile definition, not a quality score. An expired `review_by` date causes a view to flag or exclude the assertion according to its documented unknown policy.

## Proposed vNext template

This is a forward-looking template for a Principal Investigator record. It intentionally uses relationship IDs, while the Markdown body holds sources, evidence notes, and nuanced explanation. Until vNext JSON Schemas land, do not apply this template to a v1-validated record unchanged.

```yaml
---
schema_version: 2
entity_type: principal-investigator
id: PI-EXAMPLE-001
name: Example Researcher
status: draft
created_at: "2026-07-11"
updated_at: "2026-07-11"
last_review: "2026-07-11"
confidence: unassessed
source_ids: []

country_id: COUNTRY-SE
city: Stockholm
institution_id: UNIVERSITY-EXAMPLE
department_id: DEPARTMENT-EXAMPLE-MATERIALS
affiliation_ids:
  - UNIVERSITY-EXAMPLE
research_group_ids:
  - RESEARCH-GROUP-EXAMPLE-MATERIALS-INFORMATICS
career_stage: mid-career

research_area_ids:
  - RESEARCH-AREA-MATERIALS-INFORMATICS
software_ids:
  - RESEARCH-SOFTWARE-EXAMPLE
programming_language_ids:
  - PROGRAMMING-LANGUAGE-PYTHON

open_source: "yes"
github: https://github.com/example
orcid: https://orcid.org/0000-0000-0000-0000
google_scholar: https://scholar.google.com/citations?user=example
website: https://example.edu/researcher

accepting_msc: "unknown"
accepting_phd: "unknown"
international_students: "unknown"
working_language_codes: [en]
remote_collaboration: "unknown"
industry_collaboration: "unknown"
---
```

## Compatibility with existing v1 schemas

The existing [common schema](../../schemas/common.schema.json) and entity schemas use `schema_version: 1`; they remain the validation contract for all current records. [`entity-vnext.schema.json`](../../schemas/entity-vnext.schema.json) is available as the forward-looking shape contract, but is not yet enforced by CI or applied to any record. The following mapping guides future migration work and does not change any v1 schema or record.

| v1 field or type | vNext equivalent | Compatibility rule |
| --- | --- | --- |
| `schema_version: 1` | `schema_version: 2` | Keep v1 on existing records. Change version only in an approved migration paired with vNext JSON Schema validation. |
| `advisor` | `principal-investigator` | Preserve `advisor` on v1 records; map deliberately in a migration with source and ID continuity checks. |
| `lab` | `research-group` | Preserve `lab` on v1 records; map deliberately. |
| `software` | `research-software` | Preserve `software` on v1 records; map deliberately. |
| `funding-project` | `project` plus `funding-program` relationships | Do not split an existing record without an explicit migration and evidence review. |
| `country_id`, `department_id`, `research_area_ids`, `language_ids` | Same normalized relationship concept | Retain established v1 fields where they exist; map `language_ids` to `programming_language_ids` only with a type-compatible target. |
| `organization_id` on `lab` | `institution_id` **or** `organization_id` | Retain `organization_id` for v1 validation. During an evidence-reviewed vNext migration, select exactly one direct host by canonical target type; use `department_id` or plural fields only for separate documented context. |
| `affiliation_ids`, `group_ids` on `advisor` | `institution_id` / `organization_ids`, `research_group_ids` | Retain v1 plural fields until a migration can preserve role, time, and evidence. |
| `repository_url` | `github` and/or repository-specific metadata | `github` is a web-presence pointer; it must not replace a non-GitHub `repository_url`. |
| `updated_at` and optional `confidence` | Same fields plus `last_review` | Existing v1 values stay valid. Backfill `last_review` only after an actual review. |

No aliases are silently dual-written in canonical data. A migration should either maintain an explicitly documented compatibility projection or update the versioned schema and all affected field references together. This preserves Git-friendly reviewability and avoids records that appear valid while expressing contradictory relationships.

## Validation expectations for vNext

The architecture schema checks YAML shape, controlled values, date formats, and
the reviewed/published Research Group direct-host cardinality. Canonical review
must additionally resolve `institution_id` to a University and
`organization_id` to a non-university Organization; JSON Schema cannot perform
that cross-record check. A later Knowledge Graph Layer should automate target-ID
existence and relation-type compatibility checks in CI. Validation must not make
claims from a missing field, manufacture inverse links, rank entities, or treat
`confidence` as a quality score. Semantic checks that require judgment—including
source reliability, role interpretation, and availability wording—remain
editorial review responsibilities.
