---
template_type: "relationship-research-idea-note"
template_version: 1
record_id: "{{relationship_id}}-NOTE-{{sequence_3}}"
note_id: "{{relationship_id}}-NOTE-{{sequence_3}}"
idea_id: "{{relationship_id}}-IDEA-{{sequence_3}}"
relationship_id: "{{relationship_id}}"
advisor_id: "{{advisor_id}}"
owner_id: "{{owner_id}}"
status: "template"
idea_status: "seed"
created_at: "{{date_yyyy_mm_dd}}"
updated_at: "{{date_yyyy_mm_dd}}"
---

# Research-idea note — {{idea_id}}

Use for one testable research hypothesis. A promising implementation task is not enough: specify the scientific question and a way the claim could fail.

## Hypothesis statement

| field | value |
| --- | --- |
| title | `{{short_title}}` |
| problem | `{{specific_problem_to_solve}}` |
| motivation | `{{why_the_problem_matters_now}}` |
| scientific_question | `{{testable_question}}` |
| potential_contribution | `{{testable_contribution_to_knowledge_or_practice}}` |
| software_component | `{{code_package_workflow_dataset_or_automation}}` |
| scientific_component | `{{materials_theory_measurement_or_validation_component}}` |
| proposed_method_or_artifact | `{{software_method_dataset_or_workflow}}` |
| candidate_materials_or_domain | `{{bounded_domain}}` |
| difficulty | `{{low_medium_high_with_specific_reason}}` |
| long_term_value | `{{future_reuse_research_or_career_value}}` |
| linked_register_id | `{{relationship_id}}-IDEAS` |

## Facts supporting the idea

| fact_id | statement | source_path_or_url | confidence | scope_limit |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{source_supported_fact}}" | "{{source_path_or_url}}" | "high_medium_low" | "{{what_it_does_not_prove}}" |

## Assumptions and falsification

| assumption_id | hypothesis_or_assumption | test_that_could_fail_it | required_data_or_access | owner_id |
| --- | --- | --- | --- | --- |
| "{{relationship_id}}-NOTE-{{sequence_3}}" | "{{assumption_or_hypothesis}}" | "{{benchmark_or_validation_test}}" | "{{data_compute_or_collaborator_need}}" | "{{owner_id}}" |

## Validation route

| stage | method | success_metric | failure_signal | evidence_artifact |
| --- | --- | --- | --- | --- |
| baseline | `{{baseline_method}}` | `{{metric}}` | `{{failure_signal}}` | `{{relative_path_or_url}}` |
| validation | `{{benchmark_dft_experiment_literature_or_other}}` | `{{metric}}` | `{{failure_signal}}` | `{{relative_path_or_url}}` |

## Scope and decision

| field | value |
| --- | --- |
| in_scope | `{{bounded_scope}}` |
| out_of_scope | `{{explicit_exclusions}}` |
| first_milestone | `{{observable_30_to_90_day_milestone}}` |
| decision_needed | `{{accept_revise_reject_or_defer}}` |
| decision_by | `{{date_yyyy_mm_dd}}` |

## Open questions

1. `{{question_that_requires_advisor_or_domain_input}}`
2. `{{question_about_validation_or_data_rights}}`
3. `{{question_about_contribution_and_authorship}}`
