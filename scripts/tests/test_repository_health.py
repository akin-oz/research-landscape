"""Regression coverage for the canonical graph validator and generator."""

from __future__ import annotations

import datetime as dt
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import research_landscape as rl  # noqa: E402


class RepositoryHealthTests(unittest.TestCase):
    def test_canonical_graph_is_valid(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        self.assertGreater(len(records), 0)
        self.assertGreater(sum(len(r.metadata.get("relationship_assertions", [])) for r in records.values()), 0)

    def test_required_view_contract_is_present(self) -> None:
        manifest = rl.yaml.safe_load((ROOT / "views/definitions.yaml").read_text(encoding="utf-8"))
        ids = {view["view_id"] for view in manifest["views"]}
        self.assertEqual(
            {
                "global", "countries", "universities", "research-areas", "research-software",
                "ecosystems", "principal-investigators", "research-groups", "conferences", "funding",
                "my-shortlist", "current-focus", "waiting-list",
            },
            ids,
        )

    def test_committed_generated_output_is_current(self) -> None:
        self.assertEqual(0, rl.generate(ROOT, check=True))

    def test_committed_recommendations_are_current(self) -> None:
        self.assertEqual(0, rl.recommend(ROOT, check=True, query_id=None))

    def test_freshness_audit_is_reproducible_and_non_scoring(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        audit = rl.freshness_audit(records, dt.date(2026, 7, 12))
        reviewed = [record for record in records.values() if record.metadata.get("status") in {"reviewed", "published"}]
        self.assertEqual(len(reviewed), audit["reviewed_records"])
        self.assertEqual(len(reviewed), len(audit["buckets"]["current"]))
        self.assertEqual([], audit["buckets"]["attention"])
        self.assertEqual([], audit["buckets"]["stale"])
        self.assertIn("does not measure research quality", rl.render_freshness_audit(audit))

    def test_open_source_pi_and_university_host_queries_are_explainable(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        queries = {query["query_id"]: query for query in model["queries"]}
        pi_candidates = rl.recommendation_candidates(queries["principal-investigators-open-software"], records)
        self.assertEqual(["PI-SHYUE-PING-ONG"], [candidate["record"].id for candidate in pi_candidates])
        university_candidates = rl.recommendation_candidates(queries["universities-hosting-computational-materials-groups"], records)
        self.assertGreaterEqual(len(university_candidates), 1)
        self.assertTrue(all(candidate["criteria"] == 2 for candidate in university_candidates))
        self.assertTrue(all(len(candidate["signals"]) >= 2 for candidate in university_candidates))

    def test_ai_for_materials_slice_uses_explicit_area_evidence(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        queries = {query["query_id"]: query for query in model["queries"]}
        group_candidates = rl.recommendation_candidates(queries["groups-ai-for-materials"], records)
        self.assertEqual(
            ["RG-HACKING-MATERIALS", "RG-MATERIALYZE-AI"],
            sorted(candidate["record"].id for candidate in group_candidates),
        )
        pi_candidates = rl.recommendation_candidates(queries["principal-investigators-ai-for-materials"], records)
        self.assertEqual(["PI-ANUBHAV-JAIN"], [candidate["record"].id for candidate in pi_candidates])
        ecosystem_candidates = rl.recommendation_candidates(queries["ecosystems-ai-for-materials"], records)
        self.assertEqual(
            ["ECO-FAIR-CHEM", "ECO-MATERIALS-PROJECT"],
            sorted(candidate["record"].id for candidate in ecosystem_candidates),
        )
        fair_chem = next(candidate for candidate in ecosystem_candidates if candidate["record"].id == "ECO-FAIR-CHEM")
        self.assertEqual(2, fair_chem["criteria"])
        self.assertTrue(any("includes `SW-FAIRCHEM`" == item["label"] for item in fair_chem["signals"]))
        self.assertTrue(any("classified in `AREA-AI-FOR-MATERIALS`" in item["label"] for item in fair_chem["signals"]))

    def test_source_identifier_must_be_in_the_evidence_table(self) -> None:
        record = rl.Record(
            path=ROOT / "entities/research-areas/test.md",
            metadata={
                "id": "AREA-TEST",
                "entity_type": "research-area",
                "source_ids": ["SRC-TEST"],
                "relationship_assertions": [],
            },
            body="Narrative mention: `SRC-TEST`.\n",
        )
        results = rl.Results([], [])
        rl.validate_graph(ROOT, {record.id: record}, results)
        self.assertIn("source SRC-TEST missing from Evidence table", results.errors[0])
        self.assertEqual([], rl.evidence_table_source_ids(record.body))

    def test_evidence_rows_require_a_public_url_and_valid_access_date(self) -> None:
        record = rl.Record(
            path=ROOT / "entities/research-areas/test.md",
            metadata={
                "id": "AREA-TEST",
                "entity_type": "research-area",
                "source_ids": ["SRC-TEST"],
                "relationship_assertions": [],
            },
            body=(
                "## Evidence\n\n"
                "| Source ID | Evidence |\n"
                "| --- | --- |\n"
                "| `SRC-TEST` | A source without a locator. Accessed 2026-99-99. |\n"
            ),
        )
        results = rl.Results([], [])
        rl.validate_graph(ROOT, {record.id: record}, results)
        self.assertTrue(any("Evidence source SRC-TEST missing public URL" in error for error in results.errors))
        self.assertTrue(any("Evidence source SRC-TEST has invalid access date" in error for error in results.errors))

    def test_fairchem_slice_has_one_sourced_ecosystem_software_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software = records["SW-FAIRCHEM"]
        ecosystem = records["ECO-FAIR-CHEM"]
        self.assertIn("AREA-AI-FOR-MATERIALS", software.metadata["research_area_ids"])
        self.assertEqual(["ECO-FAIR-CHEM"], software.metadata["ecosystem_ids"])
        includes = rl.matching_assertions(ecosystem, "includes", {software.id})
        self.assertEqual(1, len(includes))
        self.assertEqual(["SRC-FAIRCHEM-DOCUMENTATION", "SRC-FAIRCHEM-REPOSITORY"], includes[0]["source_ids"])

    def test_recommendation_catalog_lists_available_and_unavailable_queries(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        catalog = rl.recommendation_catalog(model)
        self.assertIn("`groups-ai-for-materials` | available", catalog)
        self.assertIn("`python-heavy-research-groups` | unavailable", catalog)
        self.assertIn("No private profiles", catalog)


if __name__ == "__main__":
    unittest.main()
