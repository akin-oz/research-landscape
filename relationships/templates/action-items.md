---
template_type: "relationship-action-register"
template_version: 1
record_id: "{{relationship_id}}-ACTIONS"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
status: "template"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Action items — {{relationship_id}}

Use this register for explicit commitments and deliberate self-directed next steps. A task is not evidence that someone agreed to it; connect externally requested tasks to the source event.

## Open actions

| action_id | title | owner_id | assignee_id | status | priority | created_at | due_at | source_event_id | dependency_action_ids | success_condition | evidence_path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-ACT-{{sequence_3}}" | "{{action_title}}" | "{{owner_id}}" | "{{assignee_id}}" | "planned" | "low_medium_high" | "{{timestamp_iso8601}}" | "{{timestamp_iso8601_or_empty}}" | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{comma_separated_action_ids_or_empty}}" | "{{observable_done_definition}}" | "{{relative_path_or_url}}" |

## Completed or cancelled actions

| action_id | final_status | completed_at | outcome_fact | evidence_path | follow_on_action_id |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-ACT-{{sequence_3}}" | "completed_cancelled_deferred" | "{{timestamp_iso8601}}" | "{{fact_only_outcome}}" | "{{relative_path_or_url}}" | "{{relationship_id}}-ACT-{{sequence_3_or_empty}}" |

## Assumptions that need review before work begins

| action_id | assumption | evidence_needed | review_by |
| --- | --- | --- | --- |
| "{{relationship_id}}-ACT-{{sequence_3}}" | "{{working_assumption}}" | "{{source_or_confirmation_needed}}" | "{{date_yyyy_mm_dd}}" |

## Status vocabulary

Use only `planned`, `in_progress`, `blocked`, `completed`, `cancelled`, or `deferred`. A blocked action must name the blocker in a linked note or evidence path.
