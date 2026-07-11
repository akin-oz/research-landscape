---
template_type: "relationship-meeting-notes"
template_version: 1
record_id: "{{relationship_id}}-MTG-{{sequence_3}}"
meeting_id: "{{relationship_id}}-MTG-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
status: "template"
meeting_status: "held"
meeting_type: "{{in_person_video_phone_other}}"
started_at: "{{timestamp_iso8601}}"
ended_at: "{{timestamp_iso8601_or_empty}}"
timezone: "{{iana_timezone}}"
participant_ids: []
source_artifact_path: "{{relative_path_to_private_or_public_meeting_artifact_or_empty}}"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Meeting notes — {{meeting_id}}

Write factual notes promptly after the meeting. Attribute statements where useful. Do not convert a tentative comment, polite response, or unrecorded implication into a commitment.

## Metadata completion

| field | value |
| --- | --- |
| participant_ids | `{{comma_separated_stable_ids}}` |
| linked_preparation_path | `{{relative_path_to_meeting_preparation}}` |
| linked_contact_id | `{{relationship_id}}-CNT-{{sequence_3_or_empty}}` |
| note_taker_id | `{{owner_id}}` |
| review_status | `draft_reviewed_shared_if_appropriate` |

## Atmosphere

Record observable conditions only (for example, meeting duration, interruptions, or whether a question was answered). Do not infer mood, interest, personality, or commitment from demeanor.

| observation_id | observable fact | source_basis | confidence | interpretation_to_avoid |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{observable_meeting_condition}}" | "direct_observation" | "high_medium_low" | "{{unfounded_mood_or_interest_inference}}" |

## Research discussion

| fact_id | topic | direct statement_or_observation | speaker_or_source | confidence | linked_source_or_event |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{research_topic}}" | "{{precise_fact_or_position}}" | "{{speaker_id_or_source}}" | "high_medium_low" | "{{source_path_or_event_id}}" |

## Advice received

| fact_id | advice | source_or_speaker | scope_or_condition | resulting_action_id |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{directly_given_advice}}" | "{{speaker_id}}" | "{{condition_or_limit}}" | "{{relationship_id}}-ACT-{{sequence_3_or_empty}}" |

## Interesting observations

| observation_id | observation | evidence_basis | why_it_may_matter | confidence |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{fact_or_clearly_labelled_interpretation}}" | "{{source_or_fact_ids}}" | "{{possible_relevance}}" | "high_medium_low_unassessed" |

## Potential opportunities

Potential is not a commitment. Record the source and the next confirmation step.

| opportunity_id | opportunity | source_fact_or_statement | confirmation_needed | next_action_id | status |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{possible_opportunity}}" | "{{direct_statement_or_evidence}}" | "{{what_must_be_confirmed}}" | "{{relationship_id}}-ACT-{{sequence_3_or_empty}}" | "unconfirmed" |

## Concerns

| concern_id | concern | fact_assumption_or_unknown | supporting_record_ids | mitigation_or_question | confidence |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{concern}}" | "fact_assumption_unknown" | "{{comma_separated_ids}}" | "{{mitigation_or_question}}" | "high_medium_low_unassessed" |

## Facts stated or directly observed

| fact_id | speaker_or_source | statement | evidence_basis | confidence | linked_source_or_event |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{speaker_id_or_direct_observation}}" | "{{precise_fact_or_agreed_statement}}" | "direct_statement_observation_artifact" | "high_medium_low" | "{{source_path_or_event_id}}" |

## Assumptions, interpretations, and unknowns

| item_id | category | statement | reason | follow_up_question | owner_id |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "assumption_interpretation_unknown" | "{{statement}}" | "{{why_not_confirmed}}" | "{{question}}" | "{{owner_id}}" |

## Decisions and commitments

| event_id | decision_or_commitment | owner_id | due_at | confirmation_basis | reversal_condition |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-EVT-{{sequence_3}}" | "{{explicit_decision_or_commitment}}" | "{{owner_id}}" | "{{timestamp_iso8601_or_empty}}" | "{{direct_statement_or_written_confirmation}}" | "{{what_would_reopen_it}}" |

## Follow-up actions

| action_id | title | owner_id | due_at | success_condition | linked_follow_up_id |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-ACT-{{sequence_3}}" | "{{action}}" | "{{owner_id}}" | "{{timestamp_iso8601_or_empty}}" | "{{observable_completion}}" | "{{relationship_id}}-FUP-{{sequence_3_or_empty}}" |

## Follow-up needed

| follow_up_id | purpose | due_at | channel | source_fact_ids | status |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-FUP-{{sequence_3}}" | "{{follow_up_purpose}}" | "{{timestamp_iso8601_or_empty}}" | "email_phone_meeting_other" | "{{comma_separated_fact_ids}}" | "planned" |

## One-sentence factual summary

`{{fact_only_summary_with_no_unconfirmed_implications}}`

## Overall impression

Keep the impression separate from facts. It is a decision aid, not evidence of an advisor’s intent or quality.

| impression_id | evidence-linked impression | fact_ids_considered | assumptions_or_unknowns | confidence | review_by |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{clearly_labelled_impression}}" | "{{comma_separated_fact_ids}}" | "{{comma_separated_assumption_or_unknown_ids}}" | "high_medium_low_unassessed" | "{{date_yyyy_mm_dd}}" |
