# Changelog

All notable changes are documented here. This project follows the principles of [Keep a Changelog](https://keepachangelog.com/) and semantic versioning when releases begin.

## [Unreleased]

### Added

- An AI for Materials controlled research area with direct, evidence-bounded group and PI links, plus FAIR Chemistry/FAIRChem and UC Berkeley/CEDER/Gerbrand Ceder vertical slices.
- New explainable discovery paths for AI-for-Materials groups, PIs, and ecosystems; PIs with licensed open-source software development evidence; and universities directly hosting documented Computational Materials Science groups.
- A `recommend --list` catalog for public query IDs, aliases, titles, and unavailable-dimension status, plus `recommend --query` interactive lookup.
- A reproducible review-freshness audit based on canonical `last_review` dates and declared volatile-assertion deadlines.
- ADR 0007 (Programming Language entity contract) and ADR 0008 (public mentorship-process evidence contract), both proposed and intentionally not implemented pending explicit approval.

### Changed

- Evidence validation now resolves `SRC-*` claims only from unique `## Evidence` table rows and requires a public URL plus a valid ISO access date for each source.
- Ecosystem-by-area recommendations now display both sourced ecosystem-to-entity paths and sourced ecosystem-to-software-to-area paths.

### Notes

- This work is post-v0.3 and is not part of the `v0.3.0` release tag.
- Programming-language and mentorship queries remain unavailable until their proposed architecture contracts are approved and evidence-coverage gates are met.

## [0.3.0] - 2026-07-12

### Added

- The first production-quality knowledge-graph execution cohort: 67 reviewed v2 canonical entities and 116 evidence-bearing typed relationship assertions.
- Software Ecosystem Mapping and Research Group Intelligence coverage for the reviewed cohort, including direct-host integrity checks.
- Declarative deterministic views: 13 definitions, 10 generated public indexes, and 3 deliberately private contracts.
- Repository validation, migration checks, generated health reporting, deterministic recommendation generation, regression tests, and CI drift checks.
- Explainable evidence-discovery queries that expose predicates, targets, source identifiers, confidence, coverage, limitations, and explicitly unavailable dimensions.
- Contributor onboarding, entity-authoring, review-process, automation, recommendation, quality, migration, and architecture-status guidance.
- Final implementation review and release documentation for the complete QG1–QG10 execution phase.

### Changed

- The roadmap now records the completed v0.3.0 execution release and focuses forward work on evidence-bounded expansion, source/freshness governance, and ethical mentorship evidence.

### Notes

- This release is an integrity-reviewed canonical cohort, not a global census, prestige ranking, admissions prediction, or mentorship ranking.
- Language and comparable mentorship dimensions remain unavailable until governed evidence contracts exist.

## [0.2.0] - 2026-07-11

### Added

- Research Relationship Management (RRM): a Markdown-first, Git-based layer for preparing, documenting, and improving research-related interactions without introducing a CRM, database, or web application.
- Reusable relationship templates for timelines, contact logs, meeting preparation and notes, action items, follow-ups, reading progress, research ideas, application plans, and research-focused email drafts.
- Explicit relationship philosophy, privacy boundaries, lifecycle statuses, archive policy, and automation-readiness rules.
- Prepared, uncontacted relationship records for Adem Tekin, Sadettin Yavuz Uğurlu, and Hande Toffoli. The records link to existing due diligence and intentionally contain no fabricated interaction or application facts.
- Deep due-diligence dossiers for the narrowed three-advisor shortlist, including publication audits, reading plans, meeting preparation, risk analysis, decision gates, and first-contact guidance.

### Changed

- The repository README and Turkey index now link the due-diligence and RRM layers.

### Notes

- RRM interaction records are not public research evidence, relationship-quality scores, admissions predictions, or networking profiles.
- Automation may validate structure and dates in the future, but must not infer intent, send messages, scrape contact data, or turn interactions into evidence automatically.

## [0.1.0] - 2026-07-11

### Added

- Core knowledge model: stable identifiers, entity and relationship contracts, evidence pipeline, frontmatter specification, ADRs, and JSON Schemas.
- Versioned scoring-model contracts under `scoring/v1/`.
- Evidence-bounded Akdeniz University compatibility pilot, including current-roster reconciliation, individual advisor dossiers, comparison, ranked shortlist, and decision report.
- Nationwide Turkey advisor search with 20 evidence-backed potential MSc advisors, research-environment comparison, application tiers, and source register.

### Changed

- Country namespaces now surface published pilot and nationwide reports rather than placeholder-only content.

### Notes

- Compatibility tiers are not prestige rankings or admissions recommendations.
- The scoring model remains a design contract; no universal numeric advisor scores are published.

## [0.0.1] - 2026-07-11

### Added

- Initial repository architecture and documentation framework.
- Research methodology, scoring philosophy, and roadmap.
- Community guidelines, contribution documentation, licensing, and open-source infrastructure.

### Notes

This release establishes the project's engineering and methodological foundations. No university data, advisor evaluations, department reports, or scoring results are included.
