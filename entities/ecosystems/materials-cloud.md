---
schema_version: 2
entity_type: research-ecosystem
id: ECO-MATERIALS-CLOUD
name: Materials Cloud
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-MATERIALS-CLOUD-OVERVIEW
  - SRC-MATERIALS-CLOUD-TEAM
  - SRC-THEOS-RESEARCH
  - SRC-NCCR-MARVEL-MATERIALS-CLOUD
  - SRC-MATERIALS-CLOUD-ARCHIVE
  - SRC-MATERIALS-CLOUD-SUBMISSION
  - SRC-MATERIALS-CLOUD-PLATFORM-PUBLICATION
ecosystem_kind: computational materials open-science ecosystem
website: https://www.materialscloud.org/
software_ids:
  - SW-AIIDA-CORE
research_group_ids:
  - RG-THEOS
funding_program_ids:
  - FUND-NCCR-MARVEL
relationship_assertions:
  - predicate: includes
    target_id: SW-AIIDA-CORE
    source_ids: [SRC-MATERIALS-CLOUD-OVERVIEW]
    confidence: high
    evidence_window: 2026-07
    notes: Materials Cloud describes itself as powered by AiiDA; this does not equate the two ecosystems.
  - predicate: connects
    target_id: PI-NICOLA-MARZARI
    role: project-leader
    source_ids: [SRC-MATERIALS-CLOUD-TEAM]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: RG-THEOS
    source_ids: [SRC-THEOS-RESEARCH]
    confidence: high
    evidence_window: 2026-07
    notes: THEOS describes a contribution to Materials Cloud infrastructure; this does not assert exclusive ownership or hosting.
  - predicate: connects
    target_id: FUND-NCCR-MARVEL
    source_ids: [SRC-NCCR-MARVEL-MATERIALS-CLOUD]
    confidence: high
    evidence_window: 2021-04
    notes: "Historical programme connection: NCCR MARVEL described Materials Cloud as developed by the NCCR. Its cited final phase was scheduled through April 2026, so this does not assert current funding."
---

# Materials Cloud

Materials Cloud is represented as a research ecosystem distinct from the
underlying AiiDA software. Its public site describes open computational-materials
education, simulation services, data, and provenance-aware dissemination.

Its current public site presents a research-cycle path across Learn, Work,
Discover, Explore, and Archive. The Archive supplies a distinct public
contribution workflow: registered researchers can submit computational-
materials data and metadata for moderation, publication, versioning, and DOI
assignment. This makes contributor participation more concrete without turning
the Archive's implementation components or every hosted resource into
canonical entities.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-MATERIALS-CLOUD-OVERVIEW` | [Materials Cloud](https://www.materialscloud.org/) describes educational, research, and archiving tools; simulation services; curated and raw data; and states that Materials Cloud is powered by AiiDA. Accessed 2026-07-12. |
| `SRC-MATERIALS-CLOUD-TEAM` | [Materials Cloud: Team & Contact](https://www.materialscloud.org/team) lists Nicola Marzari under Project Leaders and gives his EPFL and PSI roles. Accessed 2026-07-12. |
| `SRC-THEOS-RESEARCH` | [THEOS: Research overview](https://www.epfl.ch/labs/theos/page-89530-en-html/) says THEOS contributes to the development and maintenance of Materials Cloud. Accessed 2026-07-12. |
| `SRC-NCCR-MARVEL-MATERIALS-CLOUD` | [NCCR MARVEL: Materials Cloud as an Open Research Europe repository](https://marvel-nccr.ch/news/communication/materials-cloud-open-science-europe) states in 2021 that Materials Cloud was developed by NCCR MARVEL. This is historical programme-context evidence, not proof of current funding. Accessed 2026-07-12. |
| `SRC-MATERIALS-CLOUD-ARCHIVE` | [Materials Cloud Archive: About](https://archive.materialscloud.org/about) describes the open computational-materials data repository, the registration/moderation/publication/DOI process, and its current InvenioRDM-based archive implementation context. Accessed 2026-07-12. |
| `SRC-MATERIALS-CLOUD-SUBMISSION` | [Materials Cloud Archive: Submission instructions](https://archive.materialscloud.org/deposit/information) documents account-based record upload, metadata, moderation, DOI publication, record updates, and integration routes. Accessed 2026-07-12. |
| `SRC-MATERIALS-CLOUD-PLATFORM-PUBLICATION` | [Scientific Data: Materials Cloud](https://www.nature.com/articles/s41597-020-00637-5) identifies the 8 September 2020 platform paper, DOI `10.1038/s41597-020-00637-5`, authors including Giovanni Pizzi and Nicola Marzari, and its archival, modelling, analytics, educational, and provenance scope. Accessed 2026-07-12. |

## Boundary and limitations

This record does not treat Materials Cloud as a single software package or
claim that AiiDA, THEOS, EPFL, PSI, or its listed project leaders are exclusive
owners, hosts, or the complete participant set. Its NCCR MARVEL relation is a
historical development context, not a claim of current funding, programme
eligibility, live-service availability, or applicant fit. Archive submission,
moderation, DOI, and hosted-resource paths do not establish a contribution
acceptance guarantee, personal support obligation, security posture, or a
complete governance or maintainer roster.
