---
template_type: "relationship-reading-note"
template_version: 1
record_id: "{{relationship_id}}-NOTE-{{sequence_3}}"
note_id: "{{relationship_id}}-NOTE-{{sequence_3}}"
reading_id: "{{relationship_id}}-READ-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
status: "template"
source_url: "{{source_url}}"
publication_id: "{{stable_publication_id_or_doi}}"
read_at: "{{timestamp_iso8601_or_empty}}"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Reading note — {{reading_id}}

Use this for a source that materially affects a question, idea, or decision. It is not a copy of the paper abstract.

## Bibliographic facts

| field | value |
| --- | --- |
| publication_id | `{{stable_publication_id_or_doi}}` |
| source_url | `{{source_url}}` |
| source_type | `{{paper_repository_documentation_other}}` |
| section_or_page_read | `{{specific_location}}` |
| reading_status | `completed_partial_revisit` |

## Directly supported facts

| fact_id | statement | source_location | confidence | reusable_in |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{precise_source_supported_fact}}" | "{{page_section_figure_or_anchor}}" | "high_medium_low" | "{{meeting_question_idea_or_decision_id}}" |

## Method and limitation notes

| category | observation | source_location | implication_for_relationship |
| --- | --- | --- | --- |
| method | `{{what_the_source_actually_did}}` | `{{source_location}}` | `{{why_it_matters}}` |
| limitation | `{{scope_or_limit_of_source}}` | `{{source_location}}` | `{{do_not_overgeneralize}}` |

## Interpretation and questions

| item_id | interpretation_or_question | evidence_basis | confidence | next_action_id |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{clearly_labelled_interpretation_or_question}}" | "{{fact_ids}}" | "high_medium_low_unassessed" | "{{relationship_id}}-ACT-{{sequence_3_or_empty}}" |

## One-sentence consequence

`{{what_this_source_changes_or_does_not_change}}`
