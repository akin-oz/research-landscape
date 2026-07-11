---
template_type: "relationship-email-initial-contact"
template_version: 1
record_id: "{{relationship_id}}-EMAIL-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
contact_id: "{{relationship_id}}-CNT-{{sequence_3}}"
status: "template"
email_status: "draft"
email_kind: "initial_contact"
direction: "outbound"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
planned_send_at: "{{timestamp_iso8601_or_empty}}"
---

# Initial-contact email — {{relationship_id}}

Use for a concise first introduction. It requests advice or a short research conversation; it does not claim admission, funding, supervision, availability, or a prior relationship.

## Source-supported facts safe to mention

| fact_id | statement | source_path_or_url | verified_at |
| --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{specific_fact_about_research_or_publication}}" | "{{source_path_or_url}}" | "{{date_yyyy_mm_dd}}" |

## Assumptions to exclude from the draft

| item_id | assumption_or_unknown | why_not_to_state_as_fact |
| --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{assumption}}" | "{{missing_evidence}}" |

## Draft metadata

| field | value |
| --- | --- |
| recipient_id | `{{advisor_id}}` |
| subject | `{{short_research_advice_subject}}` |
| linked_contact_id | `{{relationship_id}}-CNT-{{sequence_3}}` |
| linked_follow_up_id | `{{relationship_id}}-FUP-{{sequence_3_or_empty}}` |

## Draft

> Dear {{advisor_salutation_and_name}},
>
> I am {{owner_name_or_role}}, with a background in {{relevant_background}}. I am preparing to deepen my work in {{specific_research_intersection}}.
>
> I recently studied {{specific_source_or_work}} and was particularly interested in {{source_supported_observation}}. I am exploring how {{bounded_skill_or_project}} could contribute to a real research question in this area.
>
> I am not writing to ask about admission or funding at this stage. If you are open to it, I would be grateful for your advice on {{one_precise_question}} or for a short conversation about useful preparation steps.
>
> Thank you for your time.
>
> Kind regards,<br>
> {{owner_name}}<br>
> {{one_or_two_relevant_links}}

## Send and outcome record

| field | value |
| --- | --- |
| actual_sent_at | `{{timestamp_iso8601_or_empty}}` |
| delivery_evidence | `{{sent_message_artifact_path_or_empty}}` |
| resulting_contact_id | `{{relationship_id}}-CNT-{{sequence_3}}` |
| next_step | `{{relationship_id}}-FUP-{{sequence_3_or_empty}}` |

Do not infer interest from non-response. Record a fact only when an actual reply, scheduling action, or explicit decision exists.
