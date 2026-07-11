---
template_type: "relationship-email-research-advice-request"
template_version: 1
record_id: "{{relationship_id}}-EMAIL-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
contact_id: "{{relationship_id}}-CNT-{{sequence_3}}"
status: "template"
email_status: "draft"
email_kind: "research_advice_request"
direction: "outbound"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
planned_send_at: "{{timestamp_iso8601_or_empty}}"
---

# Research-advice request — {{relationship_id}}

Use after completing meaningful preparation or when asking one bounded technical question. This is not a disguised request for a thesis place.

## Evidence packet

| reading_id_or_fact_id | direct fact | source_path_or_url | limitation |
| --- | --- | --- | --- |
| "{{relationship_id}}-READ-{{sequence_3}}" | "{{source_supported_fact}}" | "{{source_path_or_url}}" | "{{scope_or_uncertainty}}" |

## Question quality check

| field | value |
| --- | --- |
| question | `{{one_answerable_research_question}}` |
| why_now | `{{connection_to_documented_work}}` |
| work_already_done | `{{reading_reproduction_or_analysis_completed}}` |
| requested_response | `{{brief_advice_or_source_recommendation}}` |
| assumption_to_avoid | `{{unverified_claim}}` |

## Draft

> Dear {{advisor_salutation_and_name}},
>
> I followed up on {{specific_work_or_topic}} by {{specific_preparation_done}}. One point I am trying to understand is {{one_answerable_research_question}}.
>
> My current reading suggests {{source_supported_fact}}, but I do not want to overinterpret it. Would you recommend {{one_preparation_step_or_source}} for understanding this direction more rigorously?
>
> I am asking for advice rather than a decision about admission or supervision. A brief response when convenient would be very helpful.
>
> Kind regards,<br>
> {{owner_name}}

## Linkage

| field | value |
| --- | --- |
| source_event_id | `{{relationship_id}}-EVT-{{sequence_3_or_empty}}` |
| linked_reading_ids | `{{comma_separated_reading_ids}}` |
| actual_sent_at | `{{timestamp_iso8601_or_empty}}` |
| response_contact_id | `{{relationship_id}}-CNT-{{sequence_3_or_empty}}` |
