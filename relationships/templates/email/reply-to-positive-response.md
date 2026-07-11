---
template_type: "relationship-email-reply-to-positive-response"
template_version: 1
record_id: "{{relationship_id}}-EMAIL-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
contact_id: "{{relationship_id}}-CNT-{{sequence_3}}"
status: "template"
email_status: "draft"
email_kind: "reply_to_positive_response"
direction: "outbound"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
planned_send_at: "{{timestamp_iso8601_or_empty}}"
---

# Reply to a positive response — {{relationship_id}}

Use after a concrete response, not after interpreting politeness as interest. Mirror only what was actually offered and confirm the next bounded step.

## Incoming response facts

| source_contact_id | direct offer_or_statement | received_at | evidence_path |
| --- | --- | --- | --- |
| "{{relationship_id}}-CNT-{{sequence_3}}" | "{{verbatim_or_precise_paraphrase}}" | "{{timestamp_iso8601}}" | "{{message_artifact_path}}" |

## Draft

> Dear {{advisor_salutation_and_name}},
>
> Thank you for your response and for offering {{direct_offer_or_next_step}}.
>
> I confirm that {{specific_logistical_or_research_response}}. To keep the discussion focused, I will prepare {{one_bounded_preparation_artifact}} and will come ready to discuss {{one_research_question}}.
>
> I appreciate your time and look forward to {{confirmed_next_step}}.
>
> Kind regards,<br>
> {{owner_name}}

## Confirmed versus assumed

| category | statement | evidence_ref |
| --- | --- | --- |
| confirmed_fact | `{{only_what_the_reply_confirmed}}` | `{{source_contact_id}}` |
| not_yet_confirmed | `{{anything_not_offered_or_not_agreed}}` | `{{keep_out_of_draft}}` |

## Linkage

| field | value |
| --- | --- |
| actual_sent_at | `{{timestamp_iso8601_or_empty}}` |
| resulting_event_id | `{{relationship_id}}-EVT-{{sequence_3_or_empty}}` |
| resulting_meeting_id | `{{relationship_id}}-MTG-{{sequence_3_or_empty}}` |
