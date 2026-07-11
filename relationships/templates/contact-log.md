---
template_type: "relationship-contact-log"
template_version: 1
record_id: "{{relationship_id}}-CONTACTS"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
status: "template"
timezone: "{{iana_timezone}}"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Contact log — {{relationship_id}}

Use one row for each material contact: an email sent/received, scheduled call, in-person conversation, or explicit no-response follow-up. This is an index, not a transcript. Store a draft in `email/` and meeting detail in `meeting/`.

## Contact entries

| contact_id | event_id | occurred_at | channel | direction | correspondent_id | purpose | fact_only_outcome | confidence | notes | linked_artifact_id | next_action_id | follow_up_id | privacy_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| "{{relationship_id}}-CNT-{{sequence_3}}" | "{{relationship_id}}-EVT-{{sequence_3}}" | "{{timestamp_iso8601}}" | "{{channel}}" | "outbound_inbound" | "{{correspondent_id}}" | "{{purpose}}" | "{{observable_outcome_or_empty}}" | "high_medium_low_unassessed" | "{{brief_non_sensitive_fact_or_link_to_note}}" | "{{relationship_id}}-EMAIL-{{sequence_3}}" | "{{relationship_id}}-ACT-{{sequence_3}}" | "{{relationship_id}}-FUP-{{sequence_3}}" | "{{do_not_store_sensitive_data}}" |

## Fact versus assumption check

| contact_id | facts_supported_by_artifact | assumptions_or_interpretations | unknowns_to_resolve |
| --- | --- | --- | --- |
| "{{relationship_id}}-CNT-{{sequence_3}}" | "{{directly_observed_or_quoted_fact}}" | "{{inference_clearly_labelled}}" | "{{unanswered_question}}" |

## Status vocabulary

- `channel`: `email`, `phone`, `meeting`, `video`, `in_person`, `conference`, `other`.
- `direction`: `outbound`, `inbound`, `mutual`.
- `confidence`: use `high`, `medium`, `low`, or `unassessed` for the recorded outcome; it describes evidence quality, not the relationship quality.
- `notes`: use a short, non-sensitive factual note or link to a detailed meeting/email artifact; do not repeat the transcript.
- Do not use this file to infer interest from response speed. Record response timing as a fact and any interpretation separately.
