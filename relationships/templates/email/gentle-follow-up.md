---
template_type: "relationship-email-gentle-follow-up"
template_version: 1
record_id: "{{relationship_id}}-EMAIL-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
contact_id: "{{relationship_id}}-CNT-{{sequence_3}}"
follow_up_id: "{{relationship_id}}-FUP-{{sequence_3}}"
status: "template"
email_status: "draft"
email_kind: "gentle_follow_up"
direction: "outbound"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
planned_send_at: "{{timestamp_iso8601_or_empty}}"
---

# Gentle follow-up — {{relationship_id}}

Use once after a documented reasonable waiting period. The purpose is to reduce inbox ambiguity, not to create pressure. Do not infer a negative decision from silence.

## Follow-up basis

| field | value |
| --- | --- |
| prior_email_id | `{{relationship_id}}-EMAIL-{{sequence_3}}` |
| prior_sent_at | `{{timestamp_iso8601}}` |
| reason_for_follow_up | `{{brief_fact_based_reason}}` |
| wait_period_days | `{{integer}}` |
| requested_reply_scope | `{{brief_advice_or_yes_no_to_meeting}}` |
| stop_condition | `{{when_no_more_follow_up_will_be_sent}}` |

## Draft

> Dear {{advisor_salutation_and_name}},
>
> I am following up on my note of {{prior_sent_date}} about {{prior_topic}}. I understand that you may be busy; there is no urgency.
>
> If a conversation is not feasible, I would still be grateful for one suggested paper, preparation step, or direction to investigate. If now is not a good time, please do not feel obliged to reply.
>
> Thank you again for your time.
>
> Kind regards,<br>
> {{owner_name}}

## Fact and assumption log

| category | statement | linked_record_id |
| --- | --- | --- |
| fact | `{{prior_email_was_sent_on_date}}` | `{{relationship_id}}-EMAIL-{{sequence_3}}` |
| unknown | `{{reason_for_no_response}}` | `{{do_not_infer}}` |

## Linkage

| field | value |
| --- | --- |
| actual_sent_at | `{{timestamp_iso8601_or_empty}}` |
| resulting_contact_id | `{{relationship_id}}-CNT-{{sequence_3_or_empty}}` |
| completion_status | `{{sent_closed_cancelled}}` |
