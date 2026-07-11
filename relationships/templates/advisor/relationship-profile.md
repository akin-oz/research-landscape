---
template_type: "advisor-relationship-profile"
template_version: 1
record_id: "{{relationship_id}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
relationship_status: "prepared"
status: "template"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Advisor relationship profile — {{relationship_id}}

This template stores relationship intent, evidence links, boundaries, and open questions. It is not an advisor biography, ranking, or due-diligence report. Keep substantive research findings in their original source/due-diligence file and reference them here by ID/path.

## Relationship intent

| field | value |
| --- | --- |
| relationship_status | `prepared_contacted_in_conversation_advice_received_collaboration_exploring_closed_archived` |
| lifecycle_milestone | `discovery_research_first_contact_meeting_follow_up_application_admission_long_term_mentorship` |
| intended_outcome | `{{advice_meeting_application_or_other}}` |
| candidate_research_intersection | `{{bounded_research_intersection}}` |
| relationship_boundary | `{{what_this_relationship_is_not}}` |
| next_decision | `{{specific_decision_to_make}}` |
| next_review_at | `{{date_yyyy_mm_dd}}` |

## Facts linked from source records

| fact_id | concise source-supported statement | source_path_or_url | verified_at | confidence | relevant_to |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{fact_only_statement}}" | "{{source_path_or_url}}" | "{{date_yyyy_mm_dd}}" | "high_medium_low" | "{{meeting_question_or_decision}}" |

## Assumptions, interpretations, and unknowns

| item_id | category | statement | why_not_a_fact | evidence_needed | review_by |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "assumption_interpretation_unknown" | "{{statement}}" | "{{basis_or_missing_evidence}}" | "{{source_or_conversation_needed}}" | "{{date_yyyy_mm_dd}}" |

## Relationship boundaries and consent

| boundary_id | boundary_or_preference | source_event_id | status | review_condition |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{e.g._keep_contact_research_focused}}" | "{{relationship_id}}-EVT-{{sequence_3_or_empty}}" | "active" | "{{what_would_change_it}}" |

## Linked operating records

| record_type | record_id | relative_path | purpose |
| --- | --- | --- | --- |
| timeline | `{{relationship_id}}-TIMELINE` | `{{relative_path}}` | `chronology` |
| contacts | `{{relationship_id}}-CONTACTS` | `{{relative_path}}` | `contact index` |
| actions | `{{relationship_id}}-ACTIONS` | `{{relative_path}}` | `commitments` |
| reading | `{{relationship_id}}-READING` | `{{relative_path}}` | `reading register` |
| ideas | `{{relationship_id}}-IDEAS` | `{{relative_path}}` | `idea register` |

## Decision record

| event_id | decided_at | decision | facts_considered | assumptions_considered | reversal_condition |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-EVT-{{sequence_3}}" | "{{timestamp_iso8601}}" | "{{decision}}" | "{{fact_ids}}" | "{{assumption_ids}}" | "{{what_would_change_the_decision}}" |
