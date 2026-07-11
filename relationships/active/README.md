---
report_type: active-relationship-index-policy
status: active
updated_at: 2026-07-11
---

# Active relationships

Each child directory represents one ongoing or intentionally prepared research relationship. The `active/` path is a storage location, not a lifecycle status. `prepared` means evidence and questions are ready, not that an interaction has happened.

## Directory contract

Use one immutable advisor slug per directory. Every active record contains the same ten files:

- `README.md` — relationship state and evidence links;
- `timeline.md` — lifecycle milestones and dates;
- `contact-log.md` — factual interaction events;
- `meeting-preparation.md` and `meeting-notes.md` — planned versus observed meeting material;
- `action-items.md` and `follow-up.md` — commitments, owners, dates, and message state;
- `reading-progress.md` and `research-ideas.md` — learning and ideas that emerge from the relationship;
- `application-plan.md` — a programme-facing plan, distinct from the relationship itself.

Keep analysis in `advisor-due-diligence/` and interaction facts here. A relationship record may link to evidence, but should not copy an advisor evaluation or assume that public research activity proves availability or interest.

## Status rule

Use the canonical `relationship_status` values from [the RRM philosophy](../philosophy.md#relationship-status-semantics): `prepared`, `contacted`, `in_conversation`, `advice_received`, `collaboration_exploring`, `closed`, or `archived`. Keep meeting, application, admission, and long-term-mentorship progress as dated timeline/application milestones rather than relationship-status values. If contact ends after one unanswered follow-up, use `closed` with a neutral closure reason; do not infer a judgment.

`contact_status` is a narrower factual field. Use `uncontacted` only when no sent or received interaction exists; after an event, update it from the contact log rather than deriving it from elapsed time or silence.
