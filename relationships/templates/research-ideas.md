---
template_type: "relationship-research-idea-register"
template_version: 1
record_id: "{{relationship_id}}-IDEAS"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
status: "template"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Research ideas — {{relationship_id}}

This is a lightweight index. Keep each full hypothesis, evidence set, validation plan, and decision in a dedicated [research-idea note](notes/research-idea.md). Do not repeat due-diligence narrative here.

## Idea register

| idea_id | title | origin_event_id | linked_reading_ids | status | problem | motivation | potential_contribution | software_component | scientific_component | difficulty | long_term_value | validation_route | detailed_note_id | next_decision_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-IDEA-{{sequence_3}}" | "{{short_title}}" | "{{relationship_id}}-EVT-{{sequence_3_or_empty}}" | "{{comma_separated_reading_ids}}" | "seed_discussing_accepted_rejected_deferred" | "{{specific_problem}}" | "{{why_now_or_why_it_matters}}" | "{{testable_contribution}}" | "{{software_artifact_or_method}}" | "{{materials_or_scientific_question}}" | "low_medium_high_with_reason" | "{{future_reuse_or_career_value}}" | "{{benchmark_dft_experiment_literature_or_other}}" | "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" |

## Facts and assumptions register

| idea_id | source_supported_facts | assumptions_or_hypotheses | critical_unknown | confidence |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-IDEA-{{sequence_3}}" | "{{fact_ids_or_source_paths}}" | "{{hypothesis_not_a_fact}}" | "{{what_must_be_checked}}" | "high_medium_low_unassessed" |

## Disposition rule

An idea moves to `accepted` only when a named scientific question, validation route, owner, and first milestone exist. An attractive software task with no scientific test remains `seed` or `deferred`.
