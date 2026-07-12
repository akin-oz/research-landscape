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

    def test_health_report_makes_research_area_coverage_explicit(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        coverage = {item["area"].id: item for item in rl.research_area_coverage(records)}
        self.assertEqual(
            {"groups": 2, "principal_investigators": 2, "software": 4, "universities": 2, "ecosystems": 2},
            {key: coverage["AREA-MACHINE-LEARNED-POTENTIALS"][key] for key in (
                "groups", "principal_investigators", "software", "universities", "ecosystems"
            )},
        )
        report = rl.health_report(ROOT, records, results, rl.input_fingerprint(ROOT))
        self.assertIn("## Research-area discovery coverage", report)
        self.assertIn("These are counts of direct, documented graph paths.", report)

    def test_open_source_pi_and_university_host_queries_are_explainable(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        queries = {query["query_id"]: query for query in model["queries"]}
        pi_candidates = rl.recommendation_candidates(queries["principal-investigators-open-software"], records)
        self.assertEqual(
            ["PI-GABOR-CSANYI", "PI-SHYUE-PING-ONG"],
            sorted(candidate["record"].id for candidate in pi_candidates),
        )
        university_candidates = rl.recommendation_candidates(queries["universities-hosting-computational-materials-groups"], records)
        self.assertGreaterEqual(len(university_candidates), 1)
        self.assertTrue(all(candidate["criteria"] == 2 for candidate in university_candidates))
        self.assertTrue(all(len(candidate["signals"]) >= 2 for candidate in university_candidates))
        ai_university_candidates = rl.recommendation_candidates(queries["universities-hosting-ai-for-materials-groups"], records)
        self.assertEqual(
            ["UNIVERSITY-NUS", "UNIVERSITY-UC-BERKELEY"],
            sorted(candidate["record"].id for candidate in ai_university_candidates),
        )

    def test_ai_for_materials_slice_uses_explicit_area_evidence(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        queries = {query["query_id"]: query for query in model["queries"]}
        group_candidates = rl.recommendation_candidates(queries["groups-ai-for-materials"], records)
        self.assertEqual(
            ["RG-CEDER-GROUP", "RG-HACKING-MATERIALS", "RG-MATERIALYZE-AI"],
            sorted(candidate["record"].id for candidate in group_candidates),
        )
        pi_candidates = rl.recommendation_candidates(queries["principal-investigators-ai-for-materials"], records)
        self.assertEqual(
            ["PI-ANUBHAV-JAIN", "PI-GERBRAND-CEDER"],
            sorted(candidate["record"].id for candidate in pi_candidates),
        )
        ecosystem_candidates = rl.recommendation_candidates(queries["ecosystems-ai-for-materials"], records)
        self.assertEqual(
            ["ECO-FAIR-CHEM", "ECO-MATERIALS-PROJECT"],
            sorted(candidate["record"].id for candidate in ecosystem_candidates),
        )
        fair_chem = next(candidate for candidate in ecosystem_candidates if candidate["record"].id == "ECO-FAIR-CHEM")
        self.assertEqual(2, fair_chem["criteria"])
        self.assertTrue(any("includes `SW-FAIRCHEM`" == item["label"] for item in fair_chem["signals"]))
        self.assertTrue(any("classified in `AREA-AI-FOR-MATERIALS`" in item["label"] for item in fair_chem["signals"]))
        materials_project = next(candidate for candidate in ecosystem_candidates if candidate["record"].id == "ECO-MATERIALS-PROJECT")
        self.assertTrue(any("connects `RG-CEDER-GROUP`" == item["label"] for item in materials_project["signals"]))

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

    def test_ceder_chgnet_development_path_is_sourced(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        group = records["RG-CEDER-GROUP"]
        software = records["SW-CHGNET"]
        self.assertEqual("yes", software.metadata["open_source"])
        self.assertEqual("BSD-3-Clause", software.metadata["license"])
        self.assertEqual(
            ["SRC-CEDER-GROUP-CHGNET"],
            rl.matching_assertions(group, "develops", {software.id})[0]["source_ids"],
        )

    def test_programming_language_and_mentorship_queries_are_bounded(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        queries = {query["query_id"]: query for query in model["queries"]}
        python_candidates = rl.recommendation_candidates(queries["python-heavy-research-groups"], records)
        self.assertEqual(
            ["RG-CEDER-GROUP", "RG-DTU-CAMD", "RG-MATERIALYZE-AI", "RG-PSI-MSD", "RG-THEOS"],
            sorted(candidate["record"].id for candidate in python_candidates),
        )
        self.assertTrue(all(candidate["criteria"] == 2 for candidate in python_candidates))
        ceder = next(candidate for candidate in python_candidates if candidate["record"].id == "RG-CEDER-GROUP")
        self.assertTrue(any("SW-CHGNET" in item["label"] for item in ceder["signals"]))
        mentorship_candidates = rl.recommendation_candidates(
            queries["entities-with-documented-mentorship-process-evidence"], records
        )
        self.assertEqual(
            ["RG-HACKING-MATERIALS", "RG-MATERIALYZE-AI"],
            sorted(candidate["record"].id for candidate in mentorship_candidates),
        )
        self.assertTrue(all(candidate["criteria"] == 1 for candidate in mentorship_candidates))
        hacking_materials = next(candidate for candidate in mentorship_candidates if candidate["record"].id == "RG-HACKING-MATERIALS")
        self.assertEqual(2, len(hacking_materials["signals"]))
        self.assertTrue(any("`professional-development`" in signal["label"] for signal in hacking_materials["signals"]))
        self.assertEqual("unavailable", queries["high-mentorship-environments"]["status"])

    def test_programming_language_facet_requires_a_matching_relation(self) -> None:
        language = rl.Record(
            path=ROOT / "entities/programming-languages/python.md",
            metadata={"id": "PROGRAMMING-LANGUAGE-PYTHON", "entity_type": "programming-language"},
            body="",
        )
        software = rl.Record(
            path=ROOT / "entities/research-software/test.md",
            metadata={
                "id": "SW-TEST",
                "entity_type": "research-software",
                "programming_language_ids": [language.id],
                "relationship_assertions": [],
            },
            body="",
        )
        results = rl.Results([], [])
        rl.validate_graph(ROOT, {language.id: language, software.id: software}, results)
        self.assertTrue(any("requires matching implemented_in assertion" in error for error in results.errors))

    def test_dynamic_group_discovery_is_explainable_and_anded(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        python_groups = rl.discovery_group_candidates(
            records, None, None, None, "PROGRAMMING-LANGUAGE-PYTHON"
        )
        self.assertEqual(
            ["RG-CEDER-GROUP", "RG-DTU-CAMD", "RG-MATERIALYZE-AI", "RG-PSI-MSD", "RG-THEOS"],
            sorted(candidate["record"].id for candidate in python_groups),
        )
        us_ai_groups = rl.discovery_group_candidates(
            records, "AREA-AI-FOR-MATERIALS", "COUNTRY-US", None, None
        )
        self.assertEqual(
            ["RG-CEDER-GROUP", "RG-HACKING-MATERIALS"],
            sorted(candidate["record"].id for candidate in us_ai_groups),
        )
        self.assertTrue(all(candidate["criteria"] == 2 for candidate in us_ai_groups))
        ceder_signals = next(candidate for candidate in us_ai_groups if candidate["record"].id == "RG-CEDER-GROUP")["signals"]
        self.assertTrue(any("direct host `UNIVERSITY-UC-BERKELEY`" in signal["label"] for signal in ceder_signals))
        self.assertTrue(any("located in `COUNTRY-US`" in signal["label"] for signal in ceder_signals))

    def test_dynamic_pi_discovery_is_explainable_and_anded(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        pymatgen_developer = rl.discovery_pi_candidates(
            records, None, None, "SW-PYMATGEN", "PROGRAMMING-LANGUAGE-PYTHON"
        )
        self.assertEqual(["PI-SHYUE-PING-ONG"], [candidate["record"].id for candidate in pymatgen_developer])
        self.assertEqual(2, pymatgen_developer[0]["criteria"])
        us_ai_pis = rl.discovery_pi_candidates(
            records, "AREA-AI-FOR-MATERIALS", "COUNTRY-US", None, None
        )
        self.assertEqual(
            ["PI-ANUBHAV-JAIN", "PI-GERBRAND-CEDER"],
            sorted(candidate["record"].id for candidate in us_ai_pis),
        )
        self.assertTrue(all(candidate["criteria"] == 2 for candidate in us_ai_pis))
        ceder_signals = next(candidate for candidate in us_ai_pis if candidate["record"].id == "PI-GERBRAND-CEDER")["signals"]
        self.assertTrue(any("affiliated with `UNIVERSITY-UC-BERKELEY`" in signal["label"] for signal in ceder_signals))
        self.assertTrue(any("located in `COUNTRY-US`" in signal["label"] for signal in ceder_signals))

    def test_dynamic_university_discovery_uses_direct_host_paths(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        us_ai_universities = rl.discovery_university_candidates(
            records, "AREA-AI-FOR-MATERIALS", "COUNTRY-US", None, None
        )
        self.assertEqual(["UNIVERSITY-UC-BERKELEY"], [candidate["record"].id for candidate in us_ai_universities])
        self.assertEqual(2, us_ai_universities[0]["criteria"])
        signals = us_ai_universities[0]["signals"]
        self.assertTrue(any("directly hosts `RG-CEDER-GROUP`" in signal["label"] for signal in signals))
        self.assertTrue(any("`RG-CEDER-GROUP`: works on `AREA-AI-FOR-MATERIALS`" in signal["label"] for signal in signals))
        chgnet_universities = rl.discovery_university_candidates(
            records, None, None, "SW-CHGNET", "PROGRAMMING-LANGUAGE-PYTHON"
        )
        self.assertEqual(["UNIVERSITY-UC-BERKELEY"], [candidate["record"].id for candidate in chgnet_universities])

    def test_dynamic_ecosystem_discovery_is_path_explainable(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        area_candidates = rl.discovery_ecosystem_candidates(
            records, "AREA-MACHINE-LEARNED-POTENTIALS", None
        )
        self.assertEqual(
            ["ECO-FAIR-CHEM", "ECO-MATERIALS-PROJECT"],
            sorted(candidate["record"].id for candidate in area_candidates),
        )
        fair_chem = next(candidate for candidate in area_candidates if candidate["record"].id == "ECO-FAIR-CHEM")
        self.assertTrue(any("includes `SW-FAIRCHEM`" in signal["label"] for signal in fair_chem["signals"]))
        software_candidates = rl.discovery_ecosystem_candidates(
            records, "AREA-MACHINE-LEARNED-POTENTIALS", "SW-FAIRCHEM"
        )
        self.assertEqual(["ECO-FAIR-CHEM"], [candidate["record"].id for candidate in software_candidates])
        self.assertEqual(2, software_candidates[0]["criteria"])

    def test_machine_learned_potentials_area_is_explicitly_traversable(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        queries = {query["query_id"]: query for query in model["queries"]}
        group_candidates = rl.recommendation_candidates(queries["groups-machine-learned-potentials"], records)
        self.assertEqual(
            ["RG-CEDER-GROUP", "RG-MATERIALYZE-AI"],
            sorted(candidate["record"].id for candidate in group_candidates),
        )
        ecosystem_candidates = rl.recommendation_candidates(queries["ecosystems-machine-learned-potentials"], records)
        self.assertEqual(
            ["ECO-FAIR-CHEM", "ECO-MATERIALS-PROJECT"],
            sorted(candidate["record"].id for candidate in ecosystem_candidates),
        )
        university_candidates = rl.recommendation_candidates(
            queries["universities-hosting-machine-learned-potential-groups"], records
        )
        self.assertEqual(
            ["UNIVERSITY-NUS", "UNIVERSITY-UC-BERKELEY"],
            sorted(candidate["record"].id for candidate in university_candidates),
        )
        self.assertEqual(
            ["RG-CEDER-GROUP", "RG-MATERIALYZE-AI"],
            sorted(candidate["record"].id for candidate in rl.discovery_group_candidates(
                records, "AREA-MACHINE-LEARNED-POTENTIALS", None, None, None
            )),
        )
        python_groups = rl.discovery_group_candidates(
            records, None, None, None, "PROGRAMMING-LANGUAGE-PYTHON"
        )
        matgl_group = next(candidate for candidate in python_groups if candidate["record"].id == "RG-MATERIALYZE-AI")
        self.assertTrue(any("SW-MATGL" in item["label"] for item in matgl_group["signals"]))
        pi_candidates = rl.recommendation_candidates(
            queries["principal-investigators-machine-learned-potentials"], records
        )
        self.assertEqual(
            ["PI-GABOR-CSANYI", "PI-SHYUE-PING-ONG"],
            sorted(candidate["record"].id for candidate in pi_candidates),
        )
        mace_developer = rl.discovery_pi_candidates(records, None, None, "SW-MACE", None)
        self.assertEqual(["PI-GABOR-CSANYI"], [candidate["record"].id for candidate in mace_developer])
        development = rl.matching_assertions(records["PI-GABOR-CSANYI"], "develops", {"SW-MACE"})
        self.assertEqual("group-attributed-development", development[0]["role"])

    def test_recommendation_catalog_lists_available_and_unavailable_queries(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        catalog = rl.recommendation_catalog(model)
        self.assertIn("`groups-ai-for-materials` | available", catalog)
        self.assertIn("`python-heavy-research-groups` | available", catalog)
        self.assertIn("`high-mentorship-environments` | unavailable", catalog)
        self.assertIn("No private profiles", catalog)


if __name__ == "__main__":
    unittest.main()
