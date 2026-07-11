---
template_type: "relationship-template-catalog"
template_version: 1
record_id: "{{template_catalog_id}}"
status: "template"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Relationship research management templates

These templates manage an evidence-aware relationship with a prospective advisor or research contact. They are intentionally Markdown-first: a person can read, edit, review, and archive them without a database or an app; a script can still locate stable IDs, ISO dates, links, and status fields.

They are **operational records**, not advisor entities and not replacements for due-diligence reports. Do not duplicate a public advisor profile, rankings, or research assessment here. Link to a source or an existing due-diligence record instead.

## Template map

| Purpose | Template | Record level |
| --- | --- | --- |
| Relationship context and boundaries | [advisor/relationship-profile.md](advisor/relationship-profile.md) | One per advisor–candidate relationship |
| Chronological milestones | [timeline.md](timeline.md) | One per relationship |
| Every outbound/inbound interaction | [contact-log.md](contact-log.md) | One per relationship |
| Meeting plan | [meeting/meeting-preparation.md](meeting/meeting-preparation.md) | One per meeting |
| Meeting record | [meeting/meeting-notes.md](meeting/meeting-notes.md) | One per meeting |
| Open commitments | [action-items.md](action-items.md) | One per relationship |
| Follow-up plan | [follow-up/follow-up.md](follow-up/follow-up.md) | One per follow-up |
| Reading register | [reading-progress.md](reading-progress.md) | One per relationship |
| Detailed reading note | [notes/reading-note.md](notes/reading-note.md) | One per reading item |
| Research-idea register | [research-ideas.md](research-ideas.md) | One per relationship |
| Detailed idea note | [notes/research-idea.md](notes/research-idea.md) | One per idea |
| Application milestones and evidence | [application-plan.md](application-plan.md) | One per relationship or target programme |
| Email drafts | [email/README.md](email/README.md) | One per draft/send event |

## Placeholder and identifier rules

Replace every quoted `{{placeholder}}` before treating a copy as a record. Quoting keeps a copied template valid YAML even before replacement.

| Placeholder | Meaning | Example shape, not a real record |
| --- | --- | --- |
| `{{relationship_id}}` | Stable relationship key reused by all related files. | `REL-{{owner_slug}}-{{advisor_slug}}` |
| `{{advisor_id}}` / `{{owner_id}}` | Stable IDs for the advisor and candidate/maintainer. | Do not place private email addresses here. |
| `{{sequence_3}}` | Zero-padded sequence within a relationship. | `001`, `002` |
| `{{timestamp_iso8601}}` | A point in time with offset. | `YYYY-MM-DDThh:mm:ss±hh:mm` |
| `{{date_yyyy_mm_dd}}` | A date with no time-of-day claim. | `YYYY-MM-DD` |
| `{{source_path_or_url}}` | Local relative path or stable public URL supporting a fact. | Keep it specific and durable where possible. |

Use these ID patterns consistently:

```text
{{relationship_id}}-EVT-{{sequence_3}}      timeline event
{{relationship_id}}-CNT-{{sequence_3}}      contact-log entry
{{relationship_id}}-MTG-{{sequence_3}}      meeting
{{relationship_id}}-ACT-{{sequence_3}}      action item
{{relationship_id}}-FUP-{{sequence_3}}      follow-up
{{relationship_id}}-READ-{{sequence_3}}     reading item
{{relationship_id}}-IDEA-{{sequence_3}}     research idea
{{relationship_id}}-APP-{{sequence_3}}      application plan
{{relationship_id}}-EMAIL-{{sequence_3}}    email draft/send record
{{relationship_id}}-NOTE-{{sequence_3}}     detailed note
```

## Fact, assumption, and decision discipline

- **Fact:** a directly observed or source-supported statement. Add a source path/URL or an event ID.
- **Assumption / interpretation:** a working belief, hypothesis, preference, or inferred implication. Never present it as a fact.
- **Unknown:** an unanswered question. Keep it visible; do not fill it with a guess.
- **Decision:** a dated choice with owner, rationale, and reversal condition. Link it to the facts and assumptions that informed it.

Use the canonical tracker for each concern. For example, an email belongs in the contact log; a promise made in that email becomes an action item; a detailed email draft belongs in `email/`; the follow-up template only references the draft rather than copying it.

## Dates, privacy, and automation

- Use ISO 8601: `YYYY-MM-DD` for dates and `YYYY-MM-DDThh:mm:ss±hh:mm` for timed events. Store timezone in frontmatter when a file contains timed events.
- Prefer stable IDs and relative repository paths over names or email addresses. Keep sensitive personal details out of the repository.
- Keep frontmatter keys scalar or simple lists so lightweight scripts can index them. Keep the Markdown body human-readable and link rows via IDs.
- Never invent a contact, meeting outcome, availability, commitment, advisor preference, or application status. Empty fields are better than fictional records.

## Copying workflow

1. Copy `advisor/relationship-profile.md` and assign a `relationship_id`.
2. Create the root trackers with that same relationship ID.
3. Create event-level meeting/email/follow-up/note files only when the event or artifact exists or is explicitly planned.
4. Link IDs across records instead of repeating narratives.
5. Update `updated_at` whenever the factual or decision state changes.
