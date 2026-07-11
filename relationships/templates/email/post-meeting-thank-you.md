---
template_type: "relationship-email-post-meeting-thank-you"
template_version: 1
record_id: "{{relationship_id}}-EMAIL-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
contact_id: "{{relationship_id}}-CNT-{{sequence_3}}"
meeting_id: "{{relationship_id}}-MTG-{{sequence_3}}"
status: "template"
email_status: "draft"
email_kind: "post_meeting_thank_you"
direction: "outbound"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
planned_send_at: "{{timestamp_iso8601_or_empty}}"
---

# Post-meeting thank-you — {{relationship_id}}

Use within one or two business days after a meeting. It confirms only decisions and actions that were actually discussed; the authoritative detailed record remains the meeting notes.

## Meeting facts to confirm

| meeting_id | fact_or_decision | evidence_section | action_id | owner_id |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-MTG-{{sequence_3}}" | "{{directly_discussed_item}}" | "{{meeting_notes_heading_or_anchor}}" | "{{relationship_id}}-ACT-{{sequence_3_or_empty}}" | "{{owner_id}}" |

## Assumptions to exclude

| assumption | why_not_confirmed | resolution_path |
| --- | --- | --- |
| "{{assumption}}" | "{{not_explicitly_agreed}}" | "{{question_or_follow_up_id}}" |

## Draft

> Dear {{advisor_salutation_and_name}},
>
> Thank you again for taking the time to discuss {{meeting_topic}}. I found your point about {{specific_discussed_point}} especially useful.
>
> My understanding is that I will {{candidate_action}} by {{date_or_condition}}, and that {{only_confirmed_counterpart_action_or_empty}}. I will keep the work focused on {{agreed_research_boundary}} and will send {{agreed_artifact}} when it is ready.
>
> Please let me know if I have misunderstood any of the points above. Thank you again for the guidance.
>
> Kind regards,<br>
> {{owner_name}}

## Linkage

| field | value |
| --- | --- |
| actual_sent_at | `{{timestamp_iso8601_or_empty}}` |
| meeting_notes_path | `{{relative_path_to_meeting_notes}}` |
| created_action_ids | `{{comma_separated_action_ids}}` |
| follow_up_id | `{{relationship_id}}-FUP-{{sequence_3_or_empty}}` |
