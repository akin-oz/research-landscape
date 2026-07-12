# Materials Project vertical slice review

**Review date:** 2026-07-12

**Scope:** the reviewed Materials Project–LBNL vNext cohort described in
[the vertical-slice document](../docs/materials-project-vertical-slice.md).

**Outcome:** the slice adds six canonical entities and nine evidence-bearing
relationships without moving legacy material. It exercises the accepted
Organization-host branch of ADR 0006 and keeps the ecosystem, software, group,
and PI boundaries distinct.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Materials Project identity and Berkeley Lab connection | Berkeley Lab Materials Sciences Division programme page | Supports an ecosystem record and LBNL connection; does not support exclusivity. |
| Pymatgen identity, repository, and licence | Official pymatgen site and project-owned GitHub repository | Supports a distinct software record, public repository, and MIT licence. |
| Persson PI and LBNL affiliation | Persson Group people page and 2026 Berkeley Lab news | Supports PI leadership of the named group and LBNL affiliation. |
| Persson Group methods and host | Persson Group research and software pages | Supports Computational Materials Science and LBNL host links. |
| United States country endpoint | Berkeley Lab contact page and ISO 3166 `US` reference | Supports location normalization and the country code. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. The report-scoped `S01`, `S02`, `S03`, and `S25` keys
were not reused as canonical evidence IDs.

## ADR 0006 host review

| Check | Result |
| --- | --- |
| Direct-host cardinality | `RG-PERSSON-GROUP` has `organization_id: ORG-LBNL` and no `institution_id`. |
| Host type | `ORG-LBNL` resolves to exactly one reviewed v2 `organization` record. |
| Evidence-bearing relationship | The group has one direct `belongs_to` assertion to `ORG-LBNL`, sourced from its public LBNL location statement. |
| No duplicate University | No duplicate University or generic Organization record is introduced for the same host. |

## Deliberate non-claims

1. The slice does not claim that the Materials Project ecosystem has only the
   recorded host, group, leader, or software.
2. It does not attribute Pymatgen development, maintenance, or use to Kristin
   Persson or the Persson Group. The reviewed group software source identifies
   Shyue Ping Ong as the maintainer.
3. It does not turn public software, platform, or group evidence into claims
   about hiring, supervision, mentoring, funding, language, or personal fit.
4. It does not introduce a Programming Language entity merely to encode the
   sourced Python fact.

## Verification record

The slice review ran the following checks over the entire v2 corpus after this
cohort was added:

- JSON syntax for every schema;
- YAML frontmatter validation against `entity-vnext.schema.json` with date
  format checks;
- unique v2 IDs and relationship target resolution/type compatibility;
- exact-one direct-host cardinality and target type for reviewed/published
  research groups, including organization-only and university-only positive
  schema cases and both/neither negative cases;
- record-local source-key resolution, modified-document local-link checks, and
  whitespace validation.

No architecture change, migration, or new automation is introduced by this
review. Cross-record validation remains a bounded QG1 review procedure until a
later Quality Gate adds repository automation.
