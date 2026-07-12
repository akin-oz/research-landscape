---
schema_version: 2
entity_type: publication
id: PUB-AIIDA-1-0
name: AiiDA 1.0, a scalable computational infrastructure for automated reproducible workflows and data provenance
title: AiiDA 1.0, a scalable computational infrastructure for automated reproducible workflows and data provenance
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-AIIDA-1-0-PUBLICATION
publication_date: "2020-09-08"
publication_type: article
external_ids:
  doi: 10.1038/s41597-020-00638-4
relationship_assertions:
  - predicate: authored_by
    target_id: PI-GIOVANNI-PIZZI
    source_ids: [SRC-AIIDA-1-0-PUBLICATION]
    confidence: high
    evidence_window: 2020-09
    notes: The canonical record links only the already reviewed Giovanni Pizzi entity; it does not create records for the paper's other authors.
  - predicate: describes
    target_id: SW-AIIDA-CORE
    source_ids: [SRC-AIIDA-1-0-PUBLICATION]
    confidence: high
    evidence_window: 2020-09
    notes: The paper describes AiiDA 1.0's workflow, provenance, plugin, and high-throughput infrastructure; it is not a current-release or maintainer claim.
---

# AiiDA 1.0

This publication is the reviewed key technical reference for the AiiDA software
ecosystem. It is represented separately from the software artifact and its
ecosystem so that a citable historical description does not become a substitute
for current software, funding, maintainer, or group facts.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-AIIDA-1-0-PUBLICATION` | [Scientific Data: AiiDA 1.0](https://www.nature.com/articles/s41597-020-00638-4) identifies the 8 September 2020 article, DOI `10.1038/s41597-020-00638-4`, its author list including Giovanni Pizzi, and its description of AiiDA workflow, provenance, plugin, and high-throughput infrastructure. Accessed 2026-07-12. |

## Boundary and limitations

This record does not claim that every listed author is a current maintainer,
that every current feature existed in 2020, or that the paper proves present
funding, employment, supervision, availability, or applicant fit.
