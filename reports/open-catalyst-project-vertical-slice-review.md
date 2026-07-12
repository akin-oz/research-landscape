# Open Catalyst Project vertical slice review

**Review date:** 2026-07-13

**Scope:** promotion of the Open Catalyst Project evidence trail to one
reviewed ecosystem record with a bounded successor-code relation to the
existing FAIRChem software entity.

**Outcome:** the slice adds one canonical entity and one evidence-bearing
relationship. It preserves the legacy project's independently named public
surface while explicitly recording the source's deprecation and code migration.

## Evidence coverage

| Claim family | Primary evidence | Review result |
| --- | --- | --- |
| Project and public surfaces | Official Open Catalyst Project website | Supports the catalyst-AI purpose, OC20/OC22 data, baseline code, leaderboard, and evaluation-server routes. |
| Migration boundary | Open-Catalyst-Project GitHub organization | Supports that the organization is deprecated and code development moved to Fair-Chem, with `ocp` models in `fairchem.core`. |
| Continuing dataset documentation | FAIR Chemistry catalyst-datasets documentation | Supports FAIR Chemistry's current documentation of Open Catalyst datasets for ML heterogeneous-catalysis use. |

## Relationship review

| Check | Result |
| --- | --- |
| Canonical identity | `ECO-OPEN-CATALYST-PROJECT` owns the named project ecosystem, rather than duplicating its context in FAIRChem. |
| Successor software route | `ECO-OPEN-CATALYST-PROJECT → includes → SW-FAIRCHEM` is limited to the OCP organization's stated code migration. |
| Time boundary | The edge uses `historical-to-2026-07`, reflecting a deprecated legacy organization and a current documentation route. |
| Area discovery | Existing sourced FAIRChem classifications expose the path under AI for Materials and Machine-Learned Potentials without creating an OCP-wide area assertion. |
| No duplicated ownership | OCP facts remain in its ecosystem record; FAIRChem keeps software and current AI/atomistic-simulation context. |

## Deliberate non-claims

1. No exhaustiveness claim is made for OCP datasets, models, tools, people,
   institutions, contributors, funders, governance, evaluation, or challenges.
2. The public legacy site and migration notice do not establish current OCP
   maintenance, support, review, employment, membership, or governance roles.
3. The slice makes no claim about accuracy, benchmark standing, access, cost,
   funding, mentoring, openings, admissions, or applicant outcomes.

## Verification record

Acceptance requires clean canonical validation, deterministic view and
recommendation regeneration, and regression coverage for the migration-boundary
path. This slice introduces no schema, scoring, or generator change.
