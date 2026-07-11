---
report_type: research-relationship-management-index
status: active
updated_at: 2026-07-11
---

# Research Relationship Management (RRM)

This directory defines the repository’s **Research Relationship Management (RRM)** boundary. RRM preserves the minimum decision-relevant context around research-related interactions—such as a request for research advice, a referral, or an exploratory collaboration conversation—without turning the repository into a contact-management system.

RRM is deliberately **not a CRM, networking tool, sales funnel, contact database, reminder system, or engagement-scoring system**. It must never rank people by responsiveness, infer a relationship from silence, collect personal profiles, or optimize outreach volume.

## Purpose

Research Landscape answers questions about public research environments: what entities exist, what public sources support claims about them, and how those observations inform evidence, metrics, and recommendations. See the [entity model](../docs/data-model/entity-model.md), [relationship model](../docs/data-model/relationships.md), and [evidence model](../docs/methodology/evidence-model.md).

RRM answers a narrower procedural question: *when an applicant or contributor chooses to initiate a research-relevant interaction, what context may be preserved so that the next decision is honest, bounded, and reproducible?*

It exists to prevent three failure modes:

- treating a public ranking or advisor dossier as a substitute for a conversation;
- treating a private interaction as proof of a public research claim; and
- losing the context, scope, and consent boundaries of a material interaction.

## Current contents

| File | Purpose |
| --- | --- |
| [philosophy.md](philosophy.md) | Scope, lifecycle, workflow, status semantics, evidence boundary, repository conventions, and automation-readiness principles. |
| [follow-up-strategy.md](follow-up-strategy.md) | Respectful timing, stop rules, and closure discipline for follow-ups. |
| [templates/](templates/README.md) | Reusable Markdown-first trackers, notes, and research-focused email templates. |
| [active/](active/README.md) | Intentionally prepared or ongoing relationship records; a directory is not evidence that contact occurred. |
| [contacts/](contacts/README.md) | Minimal public-contact-route and privacy policy. |
| [archived/](archived/README.md) | Retention and closure policy for intentionally inactive records. |

The module currently contains three **prepared, uncontacted** advisor records. They are structured planning shells linked to existing public due diligence; their contact, meeting, action, follow-up, and application tables are empty. Adding a directory or a status vocabulary never authorizes collecting interaction data.

## Research Landscape vs. RRM

| Concern | Research Landscape | RRM |
| --- | --- | --- |
| Primary object | Publicly documented research entities, relationships, and evidence. | A deliberately recorded research-related interaction and its decision context. |
| Main question | “What does the public evidence support?” | “What happened in this bounded interaction, and what should happen next?” |
| Source of truth | Cited public sources, reviewed observations, and schema-backed entity records. | A minimal interaction record only when a person intentionally creates one. |
| Publication rule | Claims require traceable evidence and review. | Interaction context is not evidence by default and does not update public claims automatically. |
| Output | Evidence-aware reports, knowledge records, and recommendations. | A bounded next step, closure, or a request for more public evidence. |

The two modules may link by stable entity ID, but they must not collapse into one another. A person may be a strong public research fit with no interaction record; an interaction record may exist without changing any research assessment.

## Directory conventions

1. **Markdown first.** Human-readable Markdown is canonical. Future machine-readable metadata must be additive, not a replacement for readable context.
2. **Stable references, not copied profiles.** Future records should refer to existing entity IDs defined in the [stable identifier specification](../docs/data-model/stable-identifiers.md). They must not duplicate an advisor’s biography, contact details, or research record.
3. **Minimal, factual interaction context.** Record only what is necessary to explain a research decision. Do not record sensitive personal data, character judgments, speculative relationship labels, or private information that is not meant to be stored in a repository.
4. **No inference from silence.** No response, delayed response, or a brief reply is never evidence of interest, quality, availability, or relationship status beyond the documented interaction fact.
5. **Evidence is not interaction.** Cite public sources in Research Landscape; use interaction references only to locate a procedural note. The distinction is defined in [philosophy.md](philosophy.md#evidence-links-and-interaction-links).
6. **No automatic promotion.** A private note, advice, or introduction does not prove a fact about an entity, validate a score, or overwrite a public report. Any eligible public claim follows the normal evidence workflow.
7. **No records by default.** A future record begins only with an explicit purpose and an intentional author. It is never generated from search results, an email address, a coauthor list, social media, or an inferred network edge.

## Automation readiness without an application

The module is designed so future tooling can validate structure without deciding human relationships. A future record format may use stable IDs, ISO 8601 dates, a finite status vocabulary, typed links, and append-only event references. Automation may check missing fields, invalid transitions, duplicate IDs, or broken links. It must not:

- infer sentiment, relationship strength, availability, or consent;
- send messages, schedule follow-ups, or create reminders;
- scrape/add contact details or interactions;
- convert an interaction into research evidence; or
- rank people by response behavior.

The templates use lightweight frontmatter compatible with the repository’s Markdown and metadata rules in [frontmatter.md](../docs/specifications/frontmatter.md). A formal JSON schema or automation proposal still requires a separate architectural decision; this module creates neither.

## Relationship status at a glance

RRM statuses describe the state of a **recorded process**, not the value of a person or a relationship. The canonical meanings and allowed transitions are in [philosophy.md](philosophy.md#relationship-status-semantics). In particular, `not_recorded` means no RRM record exists and is never a negative signal; silence never changes a status by itself.

## How to use this module

Before creating or maintaining a record:

1. Start with public evidence and an applicant-specific research question.
2. Confirm that an interaction would serve a legitimate research purpose, not broad networking.
3. State what minimum fact needs to be clarified (for example, project fit, scope, or supervision capacity).
4. Preserve only the minimum procedural context required for the next decision.
5. Keep public evidence updates and interaction notes separate.
6. Close or archive the record when its purpose is complete; do not retain speculative relationship history.

For the full lifecycle and safeguards, read [philosophy.md](philosophy.md).
