---
template_type: "relationship-reading-progress"
template_version: 1
record_id: "{{relationship_id}}-READING"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
status: "template"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Reading progress — {{relationship_id}}

This is a reading register, not a bibliography or paper review. Use one detailed [reading note](notes/reading-note.md) per item when a source materially changes a decision, meeting question, or research idea.

## Reading queue and progress

| reading_id | publication_id | source_url | title_or_short_label | relevance | status | started_at | completed_at | note_id | fact_status | key_ideas | questions | materials_atlas_connection | research_landscape_connection | ideas_generated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-READ-{{sequence_3}}" | "{{stable_publication_id_or_doi}}" | "{{source_url}}" | "{{title_or_short_label}}" | "{{why_this_matters_to_relationship}}" | "queued_in_progress_read_deferred" | "{{timestamp_iso8601_or_empty}}" | "{{timestamp_iso8601_or_empty}}" | "{{relationship_id}}-NOTE-{{sequence_3}}" | "not_extracted_facts_checked" | "{{brief_idea_or_link_to_note}}" | "{{question_to_ask_or_investigate}}" | "{{specific_connection_or_not_applicable}}" | "{{specific_connection_or_not_applicable}}" | "{{relationship_id}}-IDEA-{{sequence_3_or_empty}}" |

## Evidence and interpretation separation

| reading_id | direct_fact_to_reuse | linked_source_location | interpretation_or_hypothesis | confidence |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-READ-{{sequence_3}}" | "{{source_supported_fact_or_empty}}" | "{{page_section_or_url_fragment}}" | "{{clearly_labelled_interpretation}}" | "high_medium_low_unassessed" |

## Rules

- `publication_id` should be a DOI, a repository record ID, or another stable identifier—not a title alone.
- Mark `completed_at` only after reading enough to identify the source’s claim, method, limitations, and relevance.
- A paper title, abstract, or citation is not automatically evidence for a conclusion outside its stated scope.
- `key_ideas`, `questions`, and the two project-connection columns must distinguish a source-supported fact from an interpretation. Use `not_applicable` instead of inventing a connection.
- `ideas_generated` should contain only stable idea IDs; the substantive hypothesis belongs in `research-ideas.md` and `notes/research-idea.md`.
