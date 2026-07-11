---
template_type: "relationship-follow-up"
template_version: 1
record_id: "{{relationship_id}}-FUP-{{sequence_3}}"
follow_up_id: "{{relationship_id}}-FUP-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
source_event_id: "{{relationship_id}}-EVT-{{sequence_3}}"
status: "template"
follow_up_status: "planned"
channel: "{{email_phone_meeting_other}}"
due_at: "{{timestamp_iso8601_or_empty}}"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Follow-up plan — {{follow_up_id}}

Use this file for one focused follow-up. Link to an email draft or meeting record; do not copy its full narrative here.

## Trigger facts

| fact_id | direct trigger | source_event_or_record | confidence |
| --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{fact_that_requires_follow_up}}" | "{{relationship_id}}-EVT-{{sequence_3}}" | "high_medium_low" |

## Follow-up contract

| field | value |
| --- | --- |
| purpose | `{{one_bounded_follow_up_purpose}}` |
| recipient_or_owner_id | `{{stable_id}}` |
| desired_outcome | `{{observable_answer_or_artifact}}` |
| linked_email_id | `{{relationship_id}}-EMAIL-{{sequence_3_or_empty}}` |
| linked_action_id | `{{relationship_id}}-ACT-{{sequence_3_or_empty}}` |
| stop_condition | `{{when_to_close_or_escalate}}` |

## Assumptions and safeguards

| assumption_or_unknown | safeguard | resolution_evidence |
| --- | --- | --- |
| "{{assumption_or_unknown}}" | "{{do_not_overstate_or_pressure}}" | "{{what_would_resolve_it}}" |

## Completion record

| completed_at | factual_outcome | evidence_path | resulting_event_id | resulting_action_id | final_status |
| --- | --- | --- | --- | --- | --- |
| "{{timestamp_iso8601_or_empty}}" | "{{fact_only_outcome}}" | "{{relative_path_or_url}}" | "{{relationship_id}}-EVT-{{sequence_3_or_empty}}" | "{{relationship_id}}-ACT-{{sequence_3_or_empty}}" | "completed_cancelled_deferred" |
