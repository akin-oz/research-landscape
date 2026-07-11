---
template_type: "relationship-timeline"
template_version: 1
record_id: "{{relationship_id}}-TIMELINE"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
status: "template"
timezone: "{{iana_timezone}}"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Relationship timeline — {{relationship_id}}

One file per relationship. Record only dated events, commitments, and decision checkpoints. Detailed content belongs in the linked meeting, contact, note, or follow-up record.

## Placeholder fields

- `event_id`: `{{relationship_id}}-EVT-{{sequence_3}}`.
- `occurred_at`: ISO 8601 timestamp for an event that happened; leave blank for an undated fact.
- `planned_for`: ISO 8601 date/timestamp for a future commitment; do not put a plan in `occurred_at`.
- `evidence_ref`: a supporting record ID plus a path/URL where needed.

## Recorded facts and completed events

| event_id | occurred_at | event_type | concise fact | evidence_ref | confidence | linked_record_id |
| --- | --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-EVT-{{sequence_3}}" | "{{timestamp_iso8601}}" | "{{event_type}}" | "{{fact_only_summary}}" | "{{source_path_or_url}}" | "{{high_medium_low}}" | "{{related_record_id}}" |

Allowed `event_type` values: `research_completed`, `message_sent`, `message_received`, `meeting_held`, `decision_made`, `action_completed`, `application_submitted`, `other`.

## Planned events and commitments

| event_id | planned_for | commitment_type | owner_id | success_condition | source_event_id | status | linked_record_id |
| --- | --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_or_timestamp_iso8601}}" | "{{commitment_type}}" | "{{owner_id}}" | "{{observable_completion_condition}}" | "{{relationship_id}}-EVT-{{sequence_3}}" | "planned" | "{{related_record_id}}" |

## Standard milestone checklist

Create a planned event row for each applicable stage. These are placeholders, not claims that any milestone has occurred or will occur.

| milestone | planned_event_id | planned_for | status | completion evidence |
| --- | --- | --- | --- | --- |
| advisor_identified | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{advisor_relationship_profile_path}}" |
| papers_collected | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{reading_progress_path}}" |
| papers_read | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{reading_note_paths}}" |
| questions_prepared | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{meeting_preparation_path}}" |
| research_idea_refined | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{research_idea_note_path}}" |
| research_completed | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{reading_or_due_diligence_record_path}}" |
| initial_contact_sent | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{email_artifact_path}}" |
| response_received | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{contact_log_entry_id}}" |
| meeting_scheduled | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{meeting_preparation_path}}" |
| meeting_held | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{meeting_notes_path}}" |
| follow_up_sent | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{follow_up_or_email_artifact_path}}" |
| application_prepared | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{application_plan_path}}" |
| application_submitted | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{submission_receipt_path}}" |
| decision_received | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "planned" | "{{decision_artifact_path}}" |

## Assumptions and unknowns

| item_id | category | statement | why_it_is_not_a_fact | review_by | linked_record_id |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "assumption_or_unknown" | "{{statement}}" | "{{missing_evidence_or_reason}}" | "{{date_yyyy_mm_dd}}" | "{{related_record_id}}" |

## Decision checkpoints

| event_id | planned_for | decision | required_evidence | reversal_condition | status |
| --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-EVT-{{sequence_3}}" | "{{date_yyyy_mm_dd}}" | "{{decision_to_make}}" | "{{evidence_record_ids}}" | "{{what_would_change_the_decision}}" | "planned" |
