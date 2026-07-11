---
template_type: "relationship-email-paper-discussion"
template_version: 1
record_id: "{{relationship_id}}-EMAIL-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
contact_id: "{{relationship_id}}-CNT-{{sequence_3}}"
reading_id: "{{relationship_id}}-READ-{{sequence_3}}"
note_id: "{{relationship_id}}-NOTE-{{sequence_3}}"
status: "template"
email_status: "draft"
email_kind: "paper_discussion"
direction: "outbound"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
planned_send_at: "{{timestamp_iso8601_or_empty}}"
---

# Paper-discussion email — {{relationship_id}}

Use this to discuss one specific paper, method, result, or limitation after actually reading it. The intent is intellectual exchange and learning—not a performance of expertise or a disguised admissions request.

## Source evidence

| reading_id | publication_id | direct fact from the source | source location | limitation |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-READ-{{sequence_3}}" | "{{stable_publication_id_or_doi}}" | "{{precise_source_supported_fact}}" | "{{page_section_figure_or_anchor}}" | "{{what_the_source_does_not_establish}}" |

## Discussion target

| field | value |
| --- | --- |
| specific_question | `{{one_answerable_question_about_method_or_result}}` |
| candidate_interpretation | `{{clearly_labelled_interpretation}}` |
| why_the_question_matters | `{{bounded_connection_to_research_direction}}` |
| requested_response | `{{brief_correction_source_or_discussion}}` |
| linked_reading_note | `{{relative_path_to_reading_note}}` |

## Assumptions to exclude from the email

| assumption_or_unknown | why_not_safe_to_state | resolution |
| --- | --- | --- |
| "{{assumption_or_unknown}}" | "{{missing_evidence}}" | "{{specific_question_or_source}}" |

## Draft

> Dear {{advisor_salutation_and_name}},
>
> I recently read {{paper_title_or_short_label}} and focused on {{specific_method_result_or_limit}}. My reading is that {{precise_source_supported_fact}}.
>
> I am trying to understand {{one_answerable_question_about_method_or_result}}. My tentative interpretation is {{clearly_labelled_interpretation}}, but I would value correction if that misses an important assumption or limitation.
>
> I am asking to improve my understanding of the research direction, not to request an admissions decision. If you have a short suggestion for what to read or test next, I would be grateful.
>
> Kind regards,<br>
> {{owner_name}}

## Linkage

| field | value |
| --- | --- |
| actual_sent_at | `{{timestamp_iso8601_or_empty}}` |
| linked_contact_id | `{{relationship_id}}-CNT-{{sequence_3}}` |
| resulting_action_id | `{{relationship_id}}-ACT-{{sequence_3_or_empty}}` |
| resulting_follow_up_id | `{{relationship_id}}-FUP-{{sequence_3_or_empty}}` |
