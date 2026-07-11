---
template_type: "relationship-email-meeting-request"
template_version: 1
record_id: "{{relationship_id}}-EMAIL-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
contact_id: "{{relationship_id}}-CNT-{{sequence_3}}"
meeting_id: "{{relationship_id}}-MTG-{{sequence_3}}"
status: "template"
email_status: "draft"
email_kind: "meeting_request"
direction: "outbound"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
planned_send_at: "{{timestamp_iso8601_or_empty}}"
---

# Meeting request — {{relationship_id}}

Use only after there is a documented reason to request a conversation. Propose a short, bounded discussion and make declining easy.

## Request constraints

| field | value |
| --- | --- |
| purpose | `{{specific_research_discussion_purpose}}` |
| requested_duration_minutes | `{{small_integer}}` |
| proposed_time_windows | `{{iso8601_time_windows}}` |
| format | `{{in_person_video_phone_or_advisor_preference}}` |
| preparation_artifact | `{{one_page_note_or_link_or_empty}}` |
| linked_preparation_file | `{{relative_path_to_meeting_preparation}}` |

## Facts to state / assumptions to omit

| category | content | supporting_ref |
| --- | --- | --- |
| fact | `{{reason_for_meeting_supported_by_record}}` | `{{contact_or_source_id}}` |
| assumption_to_omit | `{{availability_interest_or_commitment_not_yet_confirmed}}` | `{{why_unknown}}` |

## Draft

> Dear {{advisor_salutation_and_name}},
>
> Thank you for {{specific_prior_interaction_or_response}}. Based on {{documented_context}}, I would value a short {{requested_duration_minutes}}-minute discussion about {{specific_research_discussion_purpose}}.
>
> I can make any of these times work: {{proposed_time_windows}}. I am also happy to follow your preferred format and schedule. I have prepared {{preparation_artifact}} so that the conversation can stay focused.
>
> If a meeting is not convenient, I would still appreciate any suggested reading or preparation step.
>
> Kind regards,<br>
> {{owner_name}}

## Outcome linkage

| field | value |
| --- | --- |
| actual_sent_at | `{{timestamp_iso8601_or_empty}}` |
| scheduling_contact_id | `{{relationship_id}}-CNT-{{sequence_3_or_empty}}` |
| confirmed_meeting_id | `{{relationship_id}}-MTG-{{sequence_3_or_empty}}` |
| no_response_follow_up_id | `{{relationship_id}}-FUP-{{sequence_3_or_empty}}` |
