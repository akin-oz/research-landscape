# Current targets view

`current-targets` is a time-bounded personal subset of [my shortlist](../my-shortlist/README.md). It is for actionable research and application work, not a public claim that a person is accepting students or that an application is feasible.

## Admission rule

A future target should reference a canonical entity and include, at minimum:

| Field | Purpose |
| --- | --- |
| `entity_id` | Points to the canonical PI, group, program, university, or project. |
| `target_reason` | A concise, personal reason tied to an evidence-backed research question. |
| `evidence_source` | Current primary source for the claimed eligibility, opening, program, or action; it resolves to a canonical `volatile_assertions` source ID where relevant. |
| `checked_at` and `review_by` | Makes volatile facts expire rather than linger as assumptions; canonical entity assertions use the same required fields. |
| `next_action` | A bounded action such as verify eligibility, read a project page, or prepare a question. |
| `personal_score` and `accessibility_score` | Versioned, profile-specific derived results where available. |

An unknown opening, funding route, supervision status, language requirement, or remote-collaboration policy is a research task—not a negative score and not proof of availability. The view must remove or flag stale target assertions when their review date passes.

## Separation from public knowledge

Current targets may be private because they can reveal an applicant's plans. They must never write outreach, private correspondence, personal constraints, or subjective rankings back into canonical entities. A target's accessibility result affects only the owner's personal view and cannot influence a global, country, university, software, or ecosystem result.
