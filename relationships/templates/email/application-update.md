---
template_type: "relationship-email-application-update"
template_version: 1
record_id: "{{relationship_id}}-EMAIL-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
contact_id: "{{relationship_id}}-CNT-{{sequence_3}}"
application_id: "{{relationship_id}}-APP-{{sequence_3}}"
status: "template"
email_status: "draft"
email_kind: "application_update"
direction: "outbound"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
planned_send_at: "{{timestamp_iso8601_or_empty}}"
---

# Application-update email — {{relationship_id}}

Use only to share a material, verified application milestone that is relevant to an existing relationship. It must not imply endorsement, funding, supervision, or a decision before those facts exist.

## Verified update

| fact_id | application_id | factual milestone | verified_at | evidence_path | relevance |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{relationship_id}}-APP-{{sequence_3}}" | "{{prepared_submitted_received_decision_or_other}}" | "{{timestamp_iso8601}}" | "{{receipt_or_plan_path}}" | "{{why_this_update_is_relevant}}" |

## Assumptions to exclude

| assumption_or_unknown | why_not_confirmed | appropriate_next_step |
| --- | --- | --- |
| "{{assumption_or_unknown}}" | "{{missing_confirmation}}" | "{{do_not_request_or_claim}}" |

## Draft

> Dear {{advisor_salutation_and_name}},
>
> I wanted to share a brief update following our discussion of {{documented_context}}. On {{verified_date}}, I {{verified_application_milestone}}.
>
> I remain focused on {{research_preparation_or_project_boundary}} and appreciated your earlier guidance on {{specific_guidance_or_source_event}}. I am sharing this only as an update; I do not want to assume any outcome or commitment beyond what has been explicitly discussed.
>
> Thank you again for your time and guidance.
>
> Kind regards,<br>
> {{owner_name}}

## Linkage

| field | value |
| --- | --- |
| actual_sent_at | `{{timestamp_iso8601_or_empty}}` |
| application_plan_path | `{{relative_path_to_application_plan}}` |
| linked_contact_id | `{{relationship_id}}-CNT-{{sequence_3}}` |
| resulting_follow_up_id | `{{relationship_id}}-FUP-{{sequence_3_or_empty}}` |
