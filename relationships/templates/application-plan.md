---
template_type: "relationship-application-plan"
template_version: 1
record_id: "{{relationship_id}}-APP-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
status: "template"
application_stage: "exploring"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Application plan — {{relationship_id}}

Use one plan per application or decision path. This file records preparation and evidence, not a claim that an advisor has agreed to supervise or fund anything.

## Application metadata

| field | value |
| --- | --- |
| application_id | `{{relationship_id}}-APP-{{sequence_3}}` |
| target_programme_id | `{{target_programme_id}}` |
| target_term | `{{term_or_cycle}}` |
| formal_deadline_at | `{{timestamp_iso8601_or_empty}}` |
| application_stage | `exploring_preparing_ready_submitted_withdrawn_decided` |
| relationship_status_at_review | `prepared_contacted_in_conversation_advice_received_collaboration_exploring_closed_archived` |

## Eligibility and application-material checklist

Mark an item as `unknown`, `not_started`, `in_progress`, `ready`, `submitted`, `not_required`, or `blocked`. A `ready` status needs an evidence path; an `unknown` requirement is not a completed requirement.

| requirement_id | requirement | status | source_of_requirement | evidence_path | missing_requirement_or_blocker | owner_id | review_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-APP-{{sequence_3}}-REQ-001" | "eligibility" | "unknown" | "{{programme_rules_url_or_path}}" | "{{evidence_path_or_empty}}" | "{{missing_requirement_or_empty}}" | "{{owner_id}}" | "{{date_yyyy_mm_dd}}" |
| "{{relationship_id}}-APP-{{sequence_3}}-REQ-002" | "missing_requirements" | "unknown" | "{{programme_rules_url_or_path}}" | "{{evidence_path_or_empty}}" | "{{specific_missing_requirement}}" | "{{owner_id}}" | "{{date_yyyy_mm_dd}}" |
| "{{relationship_id}}-APP-{{sequence_3}}-REQ-003" | "ALES" | "unknown" | "{{programme_rules_url_or_path}}" | "{{score_report_path_or_empty}}" | "{{missing_requirement_or_empty}}" | "{{owner_id}}" | "{{date_yyyy_mm_dd}}" |
| "{{relationship_id}}-APP-{{sequence_3}}-REQ-004" | "English" | "unknown" | "{{programme_rules_url_or_path}}" | "{{test_score_or_waiver_path_or_empty}}" | "{{missing_requirement_or_empty}}" | "{{owner_id}}" | "{{date_yyyy_mm_dd}}" |
| "{{relationship_id}}-APP-{{sequence_3}}-REQ-005" | "transcript" | "not_started" | "{{programme_rules_url_or_path}}" | "{{official_transcript_path_or_empty}}" | "{{missing_requirement_or_empty}}" | "{{owner_id}}" | "{{date_yyyy_mm_dd}}" |
| "{{relationship_id}}-APP-{{sequence_3}}-REQ-006" | "references" | "not_started" | "{{programme_rules_url_or_path}}" | "{{reference_request_or_submission_path_or_empty}}" | "{{missing_requirement_or_empty}}" | "{{owner_id}}" | "{{date_yyyy_mm_dd}}" |
| "{{relationship_id}}-APP-{{sequence_3}}-REQ-007" | "CV" | "not_started" | "{{programme_rules_url_or_path}}" | "{{cv_path_or_empty}}" | "{{missing_requirement_or_empty}}" | "{{owner_id}}" | "{{date_yyyy_mm_dd}}" |
| "{{relationship_id}}-APP-{{sequence_3}}-REQ-008" | "statement_of_purpose" | "not_started" | "{{programme_rules_url_or_path}}" | "{{statement_path_or_empty}}" | "{{missing_requirement_or_empty}}" | "{{owner_id}}" | "{{date_yyyy_mm_dd}}" |
| "{{relationship_id}}-APP-{{sequence_3}}-REQ-009" | "portfolio" | "unknown" | "{{programme_rules_url_or_path}}" | "{{portfolio_path_or_empty}}" | "{{missing_requirement_or_empty}}" | "{{owner_id}}" | "{{date_yyyy_mm_dd}}" |
| "{{relationship_id}}-APP-{{sequence_3}}-REQ-010" | "GitHub" | "unknown" | "{{programme_rules_url_or_path}}" | "{{github_profile_or_repository_url_or_empty}}" | "{{missing_requirement_or_empty}}" | "{{owner_id}}" | "{{date_yyyy_mm_dd}}" |
| "{{relationship_id}}-APP-{{sequence_3}}-REQ-011" | "timeline" | "not_started" | "{{programme_rules_url_or_path}}" | "{{timeline_path_or_empty}}" | "{{missing_requirement_or_empty}}" | "{{owner_id}}" | "{{date_yyyy_mm_dd}}" |

The `portfolio` and `GitHub` rows are evidence/positioning items unless a programme explicitly requires them. Do not mark them mandatory without a cited programme rule.

## Facts that support the application

| fact_id | statement | source_path_or_url | verified_at | confidence | relevance |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{source_supported_fact}}" | "{{source_path_or_url}}" | "{{date_yyyy_mm_dd}}" | "high_medium_low" | "{{application_relevance}}" |

## Assumptions and unresolved conditions

| item_id | category | statement | evidence_needed | decision_impact | review_by |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "assumption_unknown" | "{{statement}}" | "{{required_confirmation}}" | "{{high_medium_low}}" | "{{date_yyyy_mm_dd}}" |

## Milestones and evidence artifacts

| action_id | milestone | due_at | owner_id | status | success_condition | evidence_path | source_event_id |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-ACT-{{sequence_3}}" | "{{milestone}}" | "{{timestamp_iso8601_or_empty}}" | "{{owner_id}}" | "planned" | "{{observable_completion_condition}}" | "{{relative_path_or_url}}" | "{{relationship_id}}-EVT-{{sequence_3_or_empty}}" |

## Decision record

| event_id | decided_at | decision | facts_considered | assumptions_considered | reversal_condition | linked_note_id |
| --- | --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-EVT-{{sequence_3}}" | "{{timestamp_iso8601}}" | "{{apply_wait_withdraw_or_other}}" | "{{fact_ids}}" | "{{assumption_ids}}" | "{{what_would_change_this}}" | "{{relationship_id}}-NOTE-{{sequence_3}}" |

## Guardrails

- Do not mark `submitted` without a source artifact or submission receipt path.
- Do not record an advisor as committed unless a direct, attributable record says so.
- Keep programme rules, funding, availability, and recommendation claims separate until verified.
