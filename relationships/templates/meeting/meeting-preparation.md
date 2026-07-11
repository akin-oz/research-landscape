---
template_type: "relationship-meeting-preparation"
template_version: 1
record_id: "{{relationship_id}}-MTG-{{sequence_3}}"
meeting_id: "{{relationship_id}}-MTG-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
status: "template"
meeting_status: "planned"
meeting_type: "{{in_person_video_phone_other}}"
planned_start_at: "{{timestamp_iso8601}}"
planned_end_at: "{{timestamp_iso8601}}"
timezone: "{{iana_timezone}}"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Meeting preparation — {{meeting_id}}

Use one copy per planned meeting. This is a briefing and agenda, not a post hoc account. Transfer only what actually occurred to [meeting-notes.md](meeting-notes.md).

## Meeting contract

| field | value |
| --- | --- |
| purpose | `{{one_bounded_research_or_relationship_purpose}}` |
| requested_decision | `{{decision_or_guidance_sought}}` |
| duration_minutes | `{{integer}}` |
| participant_ids | `{{comma_separated_stable_ids}}` |
| linked_contact_id | `{{relationship_id}}-CNT-{{sequence_3}}` |
| preparation_owner_id | `{{owner_id}}` |

## Advisor summary

Use a short pointer to established evidence; do not reproduce a full advisor profile or make a prestige claim.

| summary_fact_id | concise source-supported summary | source_path_or_url | confidence | relevance_to_meeting |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{one_or_two_sentence_fact_summary}}" | "{{source_path_or_url}}" | "high_medium_low" | "{{why_this_belongs_on_agenda}}" |

## Current projects

| project_id_or_label | source-supported current status | source_path_or_url | relevance | question_to_ask |
| --- | --- | --- | --- | --- |
| "{{stable_project_id_or_label}}" | "{{fact_only_status}}" | "{{source_path_or_url}}" | "{{meeting_relevance}}" | "{{bounded_question}}" |

## Recent papers

| reading_id | publication_id | paper_or_short_label | direct contribution | limitation_or_scope | discussion_question |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-READ-{{sequence_3}}" | "{{stable_publication_id_or_doi}}" | "{{paper_title_or_short_label}}" | "{{source_supported_contribution}}" | "{{scope_limit}}" | "{{specific_question}}" |

## Research interests and shared interests

| category | statement | evidence_ref | fact_or_assumption | confidence |
| --- | --- | --- | --- | --- |
| advisor_research_interest | "{{source_supported_interest}}" | "{{source_path_or_url}}" | "fact" | "high_medium_low" |
| candidate_research_interest | "{{candidate_stated_interest}}" | "{{candidate_artifact_or_statement_path}}" | "fact" | "high_medium_low" |
| shared_interest | "{{bounded_overlap}}" | "{{fact_ids_or_source_paths}}" | "interpretation" | "high_medium_low" |

## Potential thesis ideas

These are prompts for discussion, not commitments or evidence that a position exists.

| idea_id | one-sentence hypothesis | potential software component | potential scientific component | validation route | current status |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-IDEA-{{sequence_3}}" | "{{testable_hypothesis}}" | "{{software_component}}" | "{{scientific_component}}" | "{{benchmark_dft_experiment_literature_or_other}}" | "seed_discussing" |

## Facts to rely on

| fact_id | direct fact | source_path_or_url | confidence | why_relevant |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{source_supported_fact}}" | "{{source_path_or_url}}" | "high_medium_low" | "{{agenda_connection}}" |

## Assumptions and unknowns to test

| item_id | category | statement | question_to_resolve | evidence_needed |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "assumption_unknown" | "{{statement}}" | "{{specific_question}}" | "{{what_would_confirm_or_refute_it}}" |

## Agenda

| agenda_item_id | minutes | topic | desired outcome | supporting_record_ids | owner_id |
| --- | --- | --- | --- | --- | --- |
| "{{meeting_id}}-AGENDA-{{sequence_2}}" | "{{integer}}" | "{{topic}}" | "{{observable_outcome}}" | "{{comma_separated_ids}}" | "{{owner_id}}" |

## Questions and listening prompts

1. `{{open_question_grounded_in_evidence}}`
2. `{{question_about_validation_scope_or_constraints}}`
3. `{{question_about_next_preparation_step}}`

## Topics to avoid

| topic | why_to_avoid_or_defer | safer_alternative |
| --- | --- | --- |
| "{{unsupported_assumption_or_private_question}}" | "{{not_evidence_based_or_too_early}}" | "{{research_focused_question}}" |

Do not turn the meeting into a request for guaranteed admission, funding, recommendation, authorship, or availability. Ask about research direction, preparation, validation, and next steps instead.

## Meeting goals

| goal_id | goal | evidence_of_success | no_assumption_rule |
| --- | --- | --- | --- |
| "{{meeting_id}}-GOAL-{{sequence_2}}" | "{{specific_goal}}" | "{{decision_fact_or_action_record}}" | "{{what_not_to_infer_if_goal_is_not_met}}" |

## Materials to bring or share

| artifact_id | artifact | relative_path_or_url | why_it_is_needed | readiness |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{artifact_name}}" | "{{relative_path_or_url}}" | "{{purpose}}" | "planned_ready_not_needed" |

## Success and stop conditions

| condition_type | condition | evidence_after_meeting |
| --- | --- | --- |
| success | `{{what_a_useful_meeting_produces}}` | `{{decision_or_action_record}}` |
| stop | `{{what_should_not_be_forced_or_assumed}}` | `{{explicitly_recorded_unknown_or_decline}}` |
