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
                "ecosystems", "principal-investigators", "research-groups", "research-problems", "conferences", "funding",
                "my-shortlist", "current-focus", "waiting-list",
            },
            ids,
        )

    def test_canonical_entity_indexes_link_every_record(self) -> None:
        for index_path in sorted((ROOT / "entities").glob("*/README.md")):
            directory = index_path.parent
            index = index_path.read_text(encoding="utf-8")
            records = sorted(directory.glob("*.md"))
            missing = [path.name for path in records if path.name != "README.md" and f"]({path.name})" not in index]
            self.assertEqual([], missing, f"{directory.relative_to(ROOT)}/README.md omits canonical records: {missing}")

    def test_committed_generated_output_is_current(self) -> None:
        self.assertEqual(0, rl.generate(ROOT, check=True))

    def test_committed_recommendations_are_current(self) -> None:
        self.assertEqual(0, rl.recommend(ROOT, check=True, query_id=None))

    def test_freshness_audit_is_reproducible_and_non_scoring(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        audit = rl.freshness_audit(records, dt.date(2026, 7, 13))
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
            {"groups": 2, "principal_investigators": 2, "software": 2, "problems": 1, "universities": 1, "ecosystems": 1},
            {key: coverage["AREA-MATERIALS-INFORMATICS"][key] for key in (
                "groups", "principal_investigators", "software", "problems", "universities", "ecosystems"
            )},
        )
        self.assertEqual(
            {"groups": 2, "principal_investigators": 2, "software": 7, "problems": 1, "universities": 2, "ecosystems": 6},
            {key: coverage["AREA-MACHINE-LEARNED-POTENTIALS"][key] for key in (
                "groups", "principal_investigators", "software", "problems", "universities", "ecosystems"
            )},
        )
        self.assertEqual(
            {"groups": 5, "principal_investigators": 1, "software": 12, "problems": 1, "universities": 4, "ecosystems": 15},
            {key: coverage["AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE"][key] for key in (
                "groups", "principal_investigators", "software", "problems", "universities", "ecosystems"
            )},
        )
        self.assertEqual(
            {"groups": 1, "principal_investigators": 1, "software": 2, "problems": 1, "universities": 0, "ecosystems": 2},
            {key: coverage["AREA-COMPUTATIONAL-PHONON-CALCULATIONS"][key] for key in (
                "groups", "principal_investigators", "software", "problems", "universities", "ecosystems"
            )},
        )
        self.assertEqual(
            {"groups": 0, "principal_investigators": 1, "software": 1, "problems": 1, "universities": 0, "ecosystems": 1},
            {key: coverage["AREA-CRYSTAL-SYMMETRY-ANALYSIS"][key] for key in (
                "groups", "principal_investigators", "software", "problems", "universities", "ecosystems"
            )},
        )
        report = rl.health_report(ROOT, records, results, rl.input_fingerprint(ROOT))
        self.assertIn("## Research-area discovery coverage", report)
        self.assertIn("These are counts of direct, documented graph paths.", report)

    def test_health_report_makes_programming_language_coverage_explicit(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        coverage = {item["language"].id: item for item in rl.programming_language_coverage(records)}
        self.assertEqual(
            {"software": 6, "groups": 1, "principal_investigators": 1, "universities": 1, "ecosystems": 6},
            {key: coverage["PROGRAMMING-LANGUAGE-CPP"][key] for key in (
                "software", "groups", "principal_investigators", "universities", "ecosystems"
            )},
        )
        self.assertEqual(
            {"software": 16, "groups": 6, "principal_investigators": 5, "universities": 4, "ecosystems": 14},
            {key: coverage["PROGRAMMING-LANGUAGE-PYTHON"][key] for key in (
                "software", "groups", "principal_investigators", "universities", "ecosystems"
            )},
        )
        self.assertEqual(
            {"software": 6, "groups": 0, "principal_investigators": 2, "universities": 0, "ecosystems": 6},
            {key: coverage["PROGRAMMING-LANGUAGE-FORTRAN"][key] for key in (
                "software", "groups", "principal_investigators", "universities", "ecosystems"
            )},
        )
        self.assertEqual(
            {"software": 1, "groups": 0, "principal_investigators": 1, "universities": 0, "ecosystems": 1},
            {key: coverage["PROGRAMMING-LANGUAGE-C"][key] for key in (
                "software", "groups", "principal_investigators", "universities", "ecosystems"
            )},
        )
        report = rl.health_report(ROOT, records, results, rl.input_fingerprint(ROOT))
        self.assertIn("## Programming-language discovery coverage", report)
        self.assertIn("These are counts of direct, documented implementation paths.", report)

    def test_open_source_pi_and_university_host_queries_are_explainable(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        queries = {query["query_id"]: query for query in model["queries"]}
        pi_candidates = rl.recommendation_candidates(queries["principal-investigators-open-software"], records)
        self.assertEqual(
            ["PI-ATSUSHI-TOGO", "PI-AXEL-KOHLMEYER", "PI-GABOR-CSANYI", "PI-GIOVANNI-PIZZI", "PI-NICOLA-MARZARI", "PI-SHYUE-PING-ONG"],
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
            ["ECO-DEEPMD-KIT", "ECO-FAIR-CHEM", "ECO-MATERIALS-PROJECT", "ECO-MATML", "ECO-NEQUIP", "ECO-OPEN-CATALYST-PROJECT"],
            sorted(candidate["record"].id for candidate in ecosystem_candidates),
        )
        fair_chem = next(candidate for candidate in ecosystem_candidates if candidate["record"].id == "ECO-FAIR-CHEM")
        self.assertEqual(2, fair_chem["criteria"])
        self.assertTrue(any("includes `SW-FAIRCHEM`" == item["label"] for item in fair_chem["signals"]))
        self.assertTrue(any("classified in `AREA-AI-FOR-MATERIALS`" in item["label"] for item in fair_chem["signals"]))
        materials_project = next(candidate for candidate in ecosystem_candidates if candidate["record"].id == "ECO-MATERIALS-PROJECT")
        self.assertTrue(any("connects `RG-CEDER-GROUP`" == item["label"] for item in materials_project["signals"]))
        open_catalyst = next(candidate for candidate in ecosystem_candidates if candidate["record"].id == "ECO-OPEN-CATALYST-PROJECT")
        self.assertEqual(2, open_catalyst["criteria"])
        self.assertTrue(any("includes `SW-FAIRCHEM`" == item["label"] for item in open_catalyst["signals"]))

    def test_scientific_software_engineering_area_is_directly_queryable(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        queries = {query["query_id"]: query for query in model["queries"]}
        group_candidates = rl.recommendation_candidates(queries["groups-scientific-software-engineering"], records)
        self.assertEqual(
            ["RG-HACKING-MATERIALS", "RG-PSI-MSD", "RG-THEOS"],
            sorted(candidate["record"].id for candidate in group_candidates),
        )
        pi_candidates = rl.recommendation_candidates(
            queries["principal-investigators-scientific-software-engineering"], records
        )
        self.assertEqual(["PI-AXEL-KOHLMEYER"], [candidate["record"].id for candidate in pi_candidates])
        ecosystem_candidates = rl.recommendation_candidates(
            queries["ecosystems-scientific-software-engineering"], records
        )
        self.assertEqual(
            ["ECO-AIIDA", "ECO-LAMMPS", "ECO-MATERIALS-CLOUD"],
            sorted(candidate["record"].id for candidate in ecosystem_candidates),
        )
        university_candidates = rl.recommendation_candidates(
            queries["universities-hosting-scientific-software-engineering-groups"], records
        )
        self.assertEqual(["UNIVERSITY-EPFL"], [candidate["record"].id for candidate in university_candidates])

    def test_density_functional_theory_area_is_software_and_ecosystem_queryable(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        queries = {query["query_id"]: query for query in model["queries"]}
        ecosystem_candidates = rl.recommendation_candidates(
            queries["ecosystems-density-functional-theory-and-electronic-structure"], records
        )
        self.assertEqual(
            ["ECO-ABINIT", "ECO-ASE", "ECO-BIGDFT", "ECO-CP2K", "ECO-DFTK", "ECO-FLEUR", "ECO-GPAW", "ECO-JDFTX", "ECO-MATERIALS-PROJECT", "ECO-OQMD", "ECO-QBOX", "ECO-QUANTUM-ESPRESSO", "ECO-SIESTA", "ECO-SISL", "ECO-WANNIER90"],
            sorted(candidate["record"].id for candidate in ecosystem_candidates),
        )
        software_candidates = rl.discovery_software_candidates(
            records,
            "AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE",
            None,
            None,
            "yes",
        )
        self.assertEqual(
            ["SW-ABINIT", "SW-BIGDFT", "SW-CP2K", "SW-DFTK", "SW-FLEUR", "SW-GPAW", "SW-JDFTX", "SW-QBOX", "SW-QUANTUM-ESPRESSO", "SW-SIESTA", "SW-SISL", "SW-WANNIER90"],
            [candidate["record"].id for candidate in software_candidates],
        )
        self.assertTrue(all(candidate["criteria"] == 2 for candidate in software_candidates))
        group_candidates = rl.recommendation_candidates(
            queries["groups-density-functional-theory-and-electronic-structure"], records
        )
        self.assertEqual(
            ["RG-CURTAROLO-GROUP", "RG-DTU-CAMD", "RG-PERSSON-GROUP", "RG-SOLGROUP", "RG-WOLVERTON-GROUP"],
            sorted(candidate["record"].id for candidate in group_candidates),
        )
        pi_candidates = rl.recommendation_candidates(
            queries["principal-investigators-density-functional-theory-and-electronic-structure"], records
        )
        self.assertEqual(["PI-STEFANO-BARONI"], [candidate["record"].id for candidate in pi_candidates])
        self.assertTrue(all(candidate["criteria"] == 1 for candidate in pi_candidates))
        university_candidates = rl.recommendation_candidates(
            queries["universities-hosting-density-functional-theory-and-electronic-structure-groups"], records
        )
        self.assertEqual(
            ["UNIVERSITY-DTU", "UNIVERSITY-DUKE", "UNIVERSITY-HU-BERLIN", "UNIVERSITY-NORTHWESTERN"],
            sorted(candidate["record"].id for candidate in university_candidates),
        )
        self.assertTrue(all(candidate["criteria"] == 2 for candidate in university_candidates))

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

    def test_mentorship_process_observations_require_the_adr_contract(self) -> None:
        record = rl.Record(
            path=ROOT / "entities/research-groups/test.md",
            metadata={
                "id": "RG-TEST", "entity_type": "research-group", "source_ids": ["SRC-TEST"],
                "relationship_assertions": [],
                "mentorship_process_evidence": [{
                    "category": "unbounded-category", "source_ids": [], "scope": "", "confidence": "unassessed",
                }],
            },
            body="## Evidence\n\n| Source ID | Evidence |\n| --- | --- |\n| `SRC-TEST` | https://example.org. Accessed 2026-07-13. |\n",
        )
        results = rl.Results([], [])
        rl.validate_graph(ROOT, {record.id: record}, results)
        self.assertTrue(any("category must be controlled" in error for error in results.errors))
        self.assertTrue(any("requires source_ids" in error for error in results.errors))
        self.assertTrue(any("requires non-empty scope" in error for error in results.errors))
        self.assertTrue(any("evidence_window or review_date" in error for error in results.errors))
        self.assertTrue(any("confidence must be high, medium, or low" in error for error in results.errors))

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

    def test_quantum_espresso_slice_keeps_foundation_and_historical_roles_bounded(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        ecosystem = records["ECO-QUANTUM-ESPRESSO"]
        software = records["SW-QUANTUM-ESPRESSO"]
        baroni = records["PI-STEFANO-BARONI"]
        self.assertEqual("yes", software.metadata["open_source"])
        self.assertEqual("GPL-2.0-or-later", software.metadata["license"])
        self.assertEqual(
            [
                "AREA-COMPUTATIONAL-MATERIALS-SCIENCE",
                "AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE",
            ],
            software.metadata["research_area_ids"],
        )
        self.assertEqual(["ORG-QUANTUM-ESPRESSO-FOUNDATION"], ecosystem.metadata["organization_ids"])
        self.assertEqual(
            ["SW-QUANTUM-ESPRESSO"],
            [assertion["target_id"] for assertion in rl.matching_assertions(ecosystem, "includes")],
        )
        self.assertEqual(["UNIVERSITY-SISSA"], baroni.metadata["affiliation_ids"])
        self.assertEqual([], rl.matching_assertions(baroni, "develops"))
        candidates = rl.discovery_ecosystem_candidates(records, None, "SW-QUANTUM-ESPRESSO")
        self.assertEqual(["ECO-QUANTUM-ESPRESSO"], [candidate["record"].id for candidate in candidates])

    def test_lammps_slice_exposes_cplusplus_with_one_bounded_person_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software = records["SW-LAMMPS"]
        ecosystem = records["ECO-LAMMPS"]
        self.assertEqual("yes", software.metadata["open_source"])
        self.assertEqual("GPL-2.0-only", software.metadata["license"])
        self.assertEqual(["PROGRAMMING-LANGUAGE-CPP"], software.metadata["programming_language_ids"])
        self.assertEqual(["ORG-SANDIA-NATIONAL-LABORATORIES"], ecosystem.metadata["organization_ids"])
        self.assertEqual(["PI-AXEL-KOHLMEYER"], ecosystem.metadata["principal_investigator_ids"])
        candidates = rl.discovery_software_candidates(
            records, "AREA-COMPUTATIONAL-MATERIALS-SCIENCE", "PROGRAMMING-LANGUAGE-CPP", "ECO-LAMMPS", "yes"
        )
        self.assertEqual(["SW-LAMMPS"], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])
        self.assertTrue(any("open-source state `yes`" in item["label"] for item in candidates[0]["signals"]))
        rendered = rl.render_software_discovery(
            records,
            "AREA-COMPUTATIONAL-MATERIALS-SCIENCE",
            "PROGRAMMING-LANGUAGE-CPP",
            "ECO-LAMMPS",
            ROOT / "reports/generated/evidence-recommendations.md",
            "yes",
        )
        self.assertIn("open-source state `yes`", rendered)
        self.assertIn("4/4 documented criteria", rendered)

    def test_openkim_slice_keeps_historical_director_context_bounded(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software = records["SW-KIM-API"]
        ecosystem = records["ECO-OPENKIM"]
        tadmor = records["PI-ELLAD-TADMOR"]
        self.assertEqual("yes", software.metadata["open_source"])
        self.assertEqual("LGPL-2.1-or-later", software.metadata["license"])
        self.assertEqual(["PROGRAMMING-LANGUAGE-CPP"], software.metadata["programming_language_ids"])
        self.assertEqual(["UNIVERSITY-UMN"], tadmor.metadata["affiliation_ids"])
        self.assertEqual([], rl.matching_assertions(tadmor, "develops"))
        director = rl.matching_assertions(ecosystem, "connects", {tadmor.id})
        self.assertEqual(1, len(director))
        self.assertEqual("founding-director", director[0]["role"])
        ecosystem_candidates = rl.discovery_ecosystem_candidates(records, None, software.id)
        self.assertEqual(["ECO-OPENKIM"], [candidate["record"].id for candidate in ecosystem_candidates])
        software_candidates = rl.discovery_software_candidates(
            records,
            "AREA-COMPUTATIONAL-MATERIALS-SCIENCE",
            "PROGRAMMING-LANGUAGE-CPP",
            "ECO-OPENKIM",
            "yes",
        )
        self.assertEqual(["SW-KIM-API"], [candidate["record"].id for candidate in software_candidates])
        self.assertEqual(4, software_candidates[0]["criteria"])

    def test_open_catalyst_project_slice_keeps_migration_path_bounded(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        ecosystem = records["ECO-OPEN-CATALYST-PROJECT"]
        fairchem = records["SW-FAIRCHEM"]
        includes = rl.matching_assertions(ecosystem, "includes", {fairchem.id})
        self.assertEqual(1, len(includes))
        self.assertEqual(["SRC-OCP-MIGRATION"], includes[0]["source_ids"])
        self.assertEqual("historical-to-2026-07", includes[0]["evidence_window"])
        candidates = rl.discovery_ecosystem_candidates(
            records, "AREA-MACHINE-LEARNED-POTENTIALS", fairchem.id
        )
        self.assertEqual(
            ["ECO-FAIR-CHEM", "ECO-OPEN-CATALYST-PROJECT"],
            [candidate["record"].id for candidate in candidates],
        )
        open_catalyst = next(candidate for candidate in candidates if candidate["record"].id == ecosystem.id)
        self.assertEqual(2, open_catalyst["criteria"])
        self.assertTrue(any("SRC-OCP-MIGRATION" in signal["sources"] for signal in open_catalyst["signals"]))

    def test_cp2k_slice_exposes_fortran_without_person_claims(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software = records["SW-CP2K"]
        ecosystem = records["ECO-CP2K"]
        self.assertEqual("yes", software.metadata["open_source"])
        self.assertEqual("GPL-2.0-only", software.metadata["license"])
        self.assertEqual(["PROGRAMMING-LANGUAGE-FORTRAN"], software.metadata["programming_language_ids"])
        self.assertEqual(
            ["SW-CP2K"],
            [assertion["target_id"] for assertion in rl.matching_assertions(ecosystem, "includes")],
        )
        candidates = rl.discovery_software_candidates(
            records,
            "AREA-COMPUTATIONAL-MATERIALS-SCIENCE",
            "PROGRAMMING-LANGUAGE-FORTRAN",
            ecosystem.id,
            "yes",
        )
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_gpaw_slice_preserves_distinct_ecosystem_and_camd_development_paths(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software = records["SW-GPAW"]
        ecosystem = records["ECO-GPAW"]
        camd = records["RG-DTU-CAMD"]
        self.assertEqual("yes", software.metadata["open_source"])
        self.assertEqual("GPL-3.0-or-later", software.metadata["license"])
        self.assertEqual(["PROGRAMMING-LANGUAGE-PYTHON"], software.metadata["programming_language_ids"])
        self.assertEqual(["SW-GPAW"], [assertion["target_id"] for assertion in rl.matching_assertions(ecosystem, "includes")])
        self.assertEqual(["RG-DTU-CAMD"], [assertion["target_id"] for assertion in rl.matching_assertions(ecosystem, "connects")])
        self.assertEqual(["SW-ASE", "SW-GPAW"], [assertion["target_id"] for assertion in rl.matching_assertions(camd, "develops")])
        candidates = rl.discovery_software_candidates(
            records,
            "AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE",
            "PROGRAMMING-LANGUAGE-PYTHON",
            ecosystem.id,
            "yes",
        )
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_siesta_slice_exposes_fortran_without_person_claims(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software = records["SW-SIESTA"]
        ecosystem = records["ECO-SIESTA"]
        self.assertEqual("yes", software.metadata["open_source"])
        self.assertEqual("GPL-3.0-only", software.metadata["license"])
        self.assertEqual(["PROGRAMMING-LANGUAGE-FORTRAN"], software.metadata["programming_language_ids"])
        self.assertEqual(
            ["SW-SIESTA"],
            [assertion["target_id"] for assertion in rl.matching_assertions(ecosystem, "includes")],
        )
        candidates = rl.discovery_software_candidates(
            records,
            "AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE",
            "PROGRAMMING-LANGUAGE-FORTRAN",
            ecosystem.id,
            "yes",
        )
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_wannier90_slice_has_bounded_developer_group_paths(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software = records["SW-WANNIER90"]
        ecosystem = records["ECO-WANNIER90"]
        self.assertEqual("yes", software.metadata["open_source"])
        self.assertEqual("LGPL-2.1-or-later", software.metadata["license"])
        self.assertEqual(["PROGRAMMING-LANGUAGE-FORTRAN"], software.metadata["programming_language_ids"])
        self.assertEqual(["SW-WANNIER90"], [item["target_id"] for item in rl.matching_assertions(ecosystem, "includes")])
        self.assertEqual(
            ["PI-GIOVANNI-PIZZI", "PI-NICOLA-MARZARI"],
            [item["target_id"] for item in rl.matching_assertions(ecosystem, "connects")],
        )
        for pi_id in ("PI-GIOVANNI-PIZZI", "PI-NICOLA-MARZARI"):
            develops = rl.matching_assertions(records[pi_id], "develops", {software.id})
            self.assertEqual(1, len(develops))
            self.assertEqual("developer-group-member", develops[0]["role"])
        candidates = rl.discovery_software_candidates(
            records,
            "AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE",
            "PROGRAMMING-LANGUAGE-FORTRAN",
            ecosystem.id,
            "yes",
        )
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_fleur_slice_exposes_fortran_without_person_claims(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software, ecosystem = records["SW-FLEUR"], records["ECO-FLEUR"]
        self.assertEqual(("yes", "MIT"), (software.metadata["open_source"], software.metadata["license"]))
        self.assertEqual(["PROGRAMMING-LANGUAGE-FORTRAN"], software.metadata["programming_language_ids"])
        candidates = rl.discovery_software_candidates(records, "AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE", "PROGRAMMING-LANGUAGE-FORTRAN", ecosystem.id, "yes")
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_dftk_slice_exposes_dft_julia_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software, ecosystem = records["SW-DFTK"], records["ECO-DFTK"]
        self.assertEqual(("yes", "MIT"), (software.metadata["open_source"], software.metadata["license"]))
        self.assertEqual(["PROGRAMMING-LANGUAGE-JULIA"], software.metadata["programming_language_ids"])
        candidates = rl.discovery_software_candidates(
            records, "AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE",
            "PROGRAMMING-LANGUAGE-JULIA", ecosystem.id, "yes",
        )
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_jdftx_slice_exposes_dft_cpp_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software, ecosystem = records["SW-JDFTX"], records["ECO-JDFTX"]
        self.assertEqual(("yes", "GPL-3.0-or-later"), (software.metadata["open_source"], software.metadata["license"]))
        self.assertEqual(["PROGRAMMING-LANGUAGE-CPP"], software.metadata["programming_language_ids"])
        candidates = rl.discovery_software_candidates(
            records, "AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE",
            "PROGRAMMING-LANGUAGE-CPP", ecosystem.id, "yes",
        )
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_qbox_slice_exposes_dft_cpp_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software, ecosystem = records["SW-QBOX"], records["ECO-QBOX"]
        self.assertEqual(("yes", "GPL-2.0-or-later"), (software.metadata["open_source"], software.metadata["license"]))
        candidates = rl.discovery_software_candidates(records, "AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE", "PROGRAMMING-LANGUAGE-CPP", ecosystem.id, "yes")
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_phonopy_slice_exposes_computational_materials_python_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software, ecosystem = records["SW-PHONOPY"], records["ECO-PHONOPY"]
        self.assertEqual(("yes", "BSD-3-Clause"), (software.metadata["open_source"], software.metadata["license"]))
        self.assertEqual(["PROGRAMMING-LANGUAGE-PYTHON"], software.metadata["programming_language_ids"])
        candidates = rl.discovery_software_candidates(records, "AREA-COMPUTATIONAL-MATERIALS-SCIENCE", "PROGRAMMING-LANGUAGE-PYTHON", ecosystem.id, "yes")
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_phono3py_slice_exposes_computational_phonon_python_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software, ecosystem = records["SW-PHONO3PY"], records["ECO-PHONO3PY"]
        self.assertEqual(("yes", "BSD-3-Clause"), (software.metadata["open_source"], software.metadata["license"]))
        self.assertEqual(["PROGRAMMING-LANGUAGE-PYTHON"], software.metadata["programming_language_ids"])
        candidates = rl.discovery_software_candidates(records, "AREA-COMPUTATIONAL-PHONON-CALCULATIONS", "PROGRAMMING-LANGUAGE-PYTHON", ecosystem.id, "yes")
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_spglib_slice_exposes_computational_materials_c_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software, ecosystem = records["SW-SPGLIB"], records["ECO-SPGLIB"]
        self.assertEqual(("yes", "BSD-3-Clause"), (software.metadata["open_source"], software.metadata["license"]))
        self.assertEqual(["PROGRAMMING-LANGUAGE-C"], software.metadata["programming_language_ids"])
        candidates = rl.discovery_software_candidates(records, "AREA-COMPUTATIONAL-MATERIALS-SCIENCE", "PROGRAMMING-LANGUAGE-C", ecosystem.id, "yes")
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_crystal_symmetry_analysis_is_discoverable_without_group_inference(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        area_id = "AREA-CRYSTAL-SYMMETRY-ANALYSIS"
        self.assertEqual([], rl.discovery_group_candidates(records, area_id, None, None, None))
        self.assertEqual(["PI-ATSUSHI-TOGO"], [
            candidate["record"].id
            for candidate in rl.discovery_pi_candidates(records, area_id, None, None, None)
        ])
        self.assertEqual(["SW-SPGLIB"], [
            candidate["record"].id
            for candidate in rl.discovery_software_candidates(records, area_id, None, None, "yes")
        ])

    def test_computational_phonon_calculations_are_discoverable_by_topic(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        area_id = "AREA-COMPUTATIONAL-PHONON-CALCULATIONS"
        self.assertEqual(["RG-NIMS-COMPUTATIONAL-MATERIALS-SCIENCE"], [
            candidate["record"].id
            for candidate in rl.discovery_group_candidates(records, area_id, None, None, None)
        ])
        self.assertEqual(["PI-ATSUSHI-TOGO"], [
            candidate["record"].id
            for candidate in rl.discovery_pi_candidates(records, area_id, None, None, None)
        ])
        self.assertEqual(["SW-PHONO3PY", "SW-PHONOPY"], [
            candidate["record"].id
            for candidate in rl.discovery_software_candidates(records, area_id, None, None, "yes")
        ])

    def test_deepmd_kit_slice_exposes_ai_and_mlp_paths(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software, ecosystem = records["SW-DEEPMD-KIT"], records["ECO-DEEPMD-KIT"]
        self.assertEqual("LGPL-3.0-only", software.metadata["license"])
        self.assertEqual(["PROGRAMMING-LANGUAGE-PYTHON", "PROGRAMMING-LANGUAGE-CPP"], software.metadata["programming_language_ids"])
        candidates = rl.discovery_software_candidates(records, "AREA-MACHINE-LEARNED-POTENTIALS", "PROGRAMMING-LANGUAGE-PYTHON", ecosystem.id, "yes")
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_nequip_slice_exposes_ai_and_mlp_paths(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software, ecosystem = records["SW-NEQUIP"], records["ECO-NEQUIP"]
        self.assertEqual("MIT", software.metadata["license"])
        self.assertEqual(["PROGRAMMING-LANGUAGE-PYTHON"], software.metadata["programming_language_ids"])
        candidates = rl.discovery_software_candidates(records, "AREA-MACHINE-LEARNED-POTENTIALS", "PROGRAMMING-LANGUAGE-PYTHON", ecosystem.id, "yes")
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

    def test_abinit_slice_reuses_fortran_with_one_bounded_ecosystem_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        software = records["SW-ABINIT"]
        ecosystem = records["ECO-ABINIT"]
        self.assertEqual("yes", software.metadata["open_source"])
        self.assertEqual("GPL-3.0-only", software.metadata["license"])
        self.assertEqual(["PROGRAMMING-LANGUAGE-FORTRAN"], software.metadata["programming_language_ids"])
        self.assertEqual(
            ["SW-ABINIT"],
            [assertion["target_id"] for assertion in rl.matching_assertions(ecosystem, "includes")],
        )
        candidates = rl.discovery_software_candidates(
            records,
            "AREA-COMPUTATIONAL-MATERIALS-SCIENCE",
            "PROGRAMMING-LANGUAGE-FORTRAN",
            ecosystem.id,
            "yes",
        )
        self.assertEqual([software.id], [candidate["record"].id for candidate in candidates])
        self.assertEqual(4, candidates[0]["criteria"])

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
            ["RG-CEDER-GROUP", "RG-DTU-CAMD", "RG-MATERIALYZE-AI", "RG-PSI-MSD", "RG-RIKEN-POLYMEROMICS", "RG-THEOS"],
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

    def test_cplusplus_and_python_software_paths_are_explicit(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        self.assertEqual(
            ["PROGRAMMING-LANGUAGE-CPP"],
            records["SW-AFLOW"].metadata["programming_language_ids"],
        )
        self.assertEqual(
            ["PROGRAMMING-LANGUAGE-PYTHON"],
            records["SW-NOMAD"].metadata["programming_language_ids"],
        )
        self.assertEqual(
            ["PROGRAMMING-LANGUAGE-PYTHON"],
            records["SW-RADONPY"].metadata["programming_language_ids"],
        )
        cplusplus_groups = rl.discovery_group_candidates(
            records, None, None, None, "PROGRAMMING-LANGUAGE-CPP"
        )
        self.assertEqual(["RG-CURTAROLO-GROUP"], [candidate["record"].id for candidate in cplusplus_groups])
        self.assertTrue(any("SW-AFLOW" in signal["label"] for signal in cplusplus_groups[0]["signals"]))

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
            ["RG-CEDER-GROUP", "RG-DTU-CAMD", "RG-MATERIALYZE-AI", "RG-PSI-MSD", "RG-RIKEN-POLYMEROMICS", "RG-THEOS"],
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
        aiida_developer = rl.discovery_pi_candidates(
            records, None, None, "SW-AIIDA-CORE", "PROGRAMMING-LANGUAGE-PYTHON"
        )
        self.assertEqual(
            ["PI-GIOVANNI-PIZZI", "PI-NICOLA-MARZARI"],
            sorted(candidate["record"].id for candidate in aiida_developer),
        )
        self.assertTrue(all(candidate["criteria"] == 2 for candidate in aiida_developer))
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
            ["ECO-DEEPMD-KIT", "ECO-FAIR-CHEM", "ECO-MATERIALS-PROJECT", "ECO-MATML", "ECO-NEQUIP", "ECO-OPEN-CATALYST-PROJECT"],
            sorted(candidate["record"].id for candidate in area_candidates),
        )
        fair_chem = next(candidate for candidate in area_candidates if candidate["record"].id == "ECO-FAIR-CHEM")
        self.assertTrue(any("includes `SW-FAIRCHEM`" in signal["label"] for signal in fair_chem["signals"]))
        software_candidates = rl.discovery_ecosystem_candidates(
            records, "AREA-MACHINE-LEARNED-POTENTIALS", "SW-FAIRCHEM"
        )
        self.assertEqual(
            ["ECO-FAIR-CHEM", "ECO-OPEN-CATALYST-PROJECT"],
            [candidate["record"].id for candidate in software_candidates],
        )
        self.assertEqual(2, software_candidates[0]["criteria"])

    def test_ecosystem_area_discovery_does_not_inherit_a_pi_topic_portfolio(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        phonon_ecosystems = rl.discovery_ecosystem_candidates(
            records, "AREA-COMPUTATIONAL-PHONON-CALCULATIONS", None
        )
        self.assertEqual(["ECO-PHONO3PY", "ECO-PHONOPY"], [
            candidate["record"].id for candidate in phonon_ecosystems
        ])

    def test_dynamic_ecosystem_filters_trace_software_paths_without_membership_claims(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        group_candidates = rl.discovery_group_candidates(
            records, None, None, None, None, "ECO-MATML"
        )
        self.assertEqual(["RG-MATERIALYZE-AI"], [candidate["record"].id for candidate in group_candidates])
        self.assertTrue(any("ECO-MATML` includes `SW-MATGL" in signal["label"] for signal in group_candidates[0]["signals"]))
        pi_candidates = rl.discovery_pi_candidates(
            records, None, None, None, None, "ECO-MATERIALS-PROJECT"
        )
        self.assertEqual(["PI-SHYUE-PING-ONG"], [candidate["record"].id for candidate in pi_candidates])
        self.assertTrue(any("ECO-MATERIALS-PROJECT` includes `SW-PYMATGEN" in signal["label"] for signal in pi_candidates[0]["signals"]))
        university_candidates = rl.discovery_university_candidates(
            records, "AREA-MACHINE-LEARNED-POTENTIALS", None, None, None, "ECO-MATML"
        )
        self.assertEqual(["UNIVERSITY-NUS"], [candidate["record"].id for candidate in university_candidates])
        self.assertEqual(2, university_candidates[0]["criteria"])
        self.assertTrue(any("`RG-MATERIALYZE-AI`: `ECO-MATML` includes `SW-MATGL" in signal["label"] for signal in university_candidates[0]["signals"]))

    def test_dynamic_software_discovery_is_path_explainable_and_anded(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        candidates = rl.discovery_software_candidates(
            records,
            "AREA-MACHINE-LEARNED-POTENTIALS",
            "PROGRAMMING-LANGUAGE-PYTHON",
            "ECO-MATML",
        )
        self.assertEqual(["SW-MATGL"], [candidate["record"].id for candidate in candidates])
        self.assertEqual(3, candidates[0]["criteria"])
        signals = candidates[0]["signals"]
        self.assertTrue(any("classified in `AREA-MACHINE-LEARNED-POTENTIALS`" in signal["label"] for signal in signals))
        self.assertTrue(any("implemented in `PROGRAMMING-LANGUAGE-PYTHON`" in signal["label"] for signal in signals))
        self.assertTrue(any("included by `ECO-MATML`" in signal["label"] for signal in signals))
        rendered = rl.render_software_discovery(
            records,
            "AREA-MACHINE-LEARNED-POTENTIALS",
            "PROGRAMMING-LANGUAGE-PYTHON",
            "ECO-MATML",
            ROOT / "reports/generated/evidence-recommendations.md",
        )
        self.assertIn("# Research-software discovery", rendered)
        self.assertIn("not documented", rendered)
        self.assertIn("3/3 documented criteria", rendered)
        ml_python_candidates = rl.discovery_software_candidates(
            records, "AREA-MACHINE-LEARNED-POTENTIALS", "PROGRAMMING-LANGUAGE-PYTHON", None
        )
        self.assertEqual(
            ["SW-CHGNET", "SW-DEEPMD-KIT", "SW-FAIRCHEM", "SW-M3GNET", "SW-MACE", "SW-MATGL", "SW-NEQUIP"],
            sorted(candidate["record"].id for candidate in ml_python_candidates),
        )
        ml_python_rendered = rl.render_software_discovery(
            records, "AREA-MACHINE-LEARNED-POTENTIALS", "PROGRAMMING-LANGUAGE-PYTHON", None,
            ROOT / "reports/generated/evidence-recommendations.md",
        )
        self.assertIn("archived (sources: SRC-M3GNET-REPOSITORY)", ml_python_rendered)
        self.assertIn("not documented", ml_python_rendered)

    def test_discovery_catalog_lists_public_filter_ids(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        catalog = rl.discovery_catalog(records)
        self.assertIn("## Research areas", catalog)
        self.assertIn("## Research problems", catalog)
        self.assertIn("`AREA-MACHINE-LEARNED-POTENTIALS`", catalog)
        self.assertIn("`PROBLEM-MATERIALS-PROPERTY-PREDICTION`", catalog)
        self.assertIn("`COUNTRY-GB`", catalog)
        self.assertIn("`SW-MATGL`", catalog)
        self.assertIn("`PROGRAMMING-LANGUAGE-PYTHON`", catalog)
        self.assertIn("`PROGRAMMING-LANGUAGE-CPP`", catalog)
        self.assertIn("`ECO-MATML`", catalog)
        self.assertIn("contains no private profile", catalog)

    def test_problem_discovery_is_noncomparative_and_exposes_direct_support_paths(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        rendered = rl.render_problem_discovery(records, ROOT / "reports/generated/evidence-recommendations.md")
        self.assertIn("not a problem-importance ranking", rendered)
        self.assertIn("`PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION`", rendered)
        self.assertIn("`SW-PHONO3PY` supports this problem", rendered)
        self.assertIn("`PROBLEM-CRYSTAL-SYMMETRY-DETERMINATION`", rendered)
        self.assertIn("`SW-SPGLIB` supports this problem", rendered)
        self.assertIn("`PROBLEM-MACHINE-LEARNED-INTERATOMIC-POTENTIAL-MODELING`", rendered)
        self.assertIn("`SW-MACE` supports this problem (sources: SRC-MACE-DOCUMENTATION)", rendered)
        self.assertIn("`SW-NEQUIP` supports this problem (sources: SRC-NEQUIP-DOCUMENTATION)", rendered)
        self.assertIn("`SW-DEEPMD-KIT` supports this problem (sources: SRC-DEEPMD-DOCUMENTATION)", rendered)
        self.assertIn("`PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION`", rendered)
        self.assertIn("`SW-ABINIT` supports this problem (sources: SRC-ABINIT-PRESENTATION)", rendered)
        self.assertIn("`SW-QUANTUM-ESPRESSO` supports this problem (sources: SRC-QE-HOME)", rendered)
        self.assertIn("`SW-GPAW` supports this problem (sources: SRC-GPAW-DOCUMENTATION)", rendered)
        self.assertIn("`SW-SIESTA` supports this problem (sources: SRC-SIESTA-REFERENCE-MANUAL)", rendered)

    def test_problem_discovery_area_filter_uses_only_problem_area_evidence(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        rendered = rl.render_problem_discovery(
            records, ROOT / "reports/generated/evidence-recommendations.md",
            "AREA-MACHINE-LEARNED-POTENTIALS",
        )
        self.assertIn("**AND filters:** research area `AREA-MACHINE-LEARNED-POTENTIALS`.", rendered)
        self.assertIn("`PROBLEM-MACHINE-LEARNED-INTERATOMIC-POTENTIAL-MODELING`", rendered)
        self.assertIn("is classified in `AREA-MACHINE-LEARNED-POTENTIALS` (sources: SRC-MACE-DOCUMENTATION, SRC-NEQUIP-DOCUMENTATION, SRC-DEEPMD-DOCUMENTATION)", rendered)
        self.assertNotIn("PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION", rendered)
        self.assertIn("problem record's own source-backed controlled-area classification", rendered)

    def test_problem_discovery_software_filter_requires_direct_support(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        rendered = rl.render_problem_discovery(
            records, ROOT / "reports/generated/evidence-recommendations.md",
            software_id="SW-MACE",
        )
        self.assertIn("**AND filters:** research software `SW-MACE`.", rendered)
        self.assertIn("`PROBLEM-MACHINE-LEARNED-INTERATOMIC-POTENTIAL-MODELING`", rendered)
        self.assertIn("`SW-MACE` supports this problem (sources: SRC-MACE-DOCUMENTATION)", rendered)
        self.assertNotIn("PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION", rendered)
        self.assertIn("software record's direct sourced `supports` assertion", rendered)

        combined = rl.render_problem_discovery(
            records, ROOT / "reports/generated/evidence-recommendations.md",
            "AREA-MACHINE-LEARNED-POTENTIALS", "SW-MACE",
        )
        self.assertIn("**AND filters:** research area `AREA-MACHINE-LEARNED-POTENTIALS`; research software `SW-MACE`.", combined)
        self.assertIn("`PROBLEM-MACHINE-LEARNED-INTERATOMIC-POTENTIAL-MODELING`", combined)

    def test_problem_discovery_ecosystem_filter_requires_inclusion_and_support_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        rendered = rl.render_problem_discovery(
            records, ROOT / "reports/generated/evidence-recommendations.md",
            ecosystem_id="ECO-PHONO3PY",
        )
        self.assertIn("**AND filters:** research ecosystem `ECO-PHONO3PY`.", rendered)
        self.assertIn("`PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION`", rendered)
        self.assertIn("`ECO-PHONO3PY` includes `SW-PHONO3PY` (sources: SRC-PHONO3PY-DOCUMENTATION, SRC-PHONO3PY-REPOSITORY)", rendered)
        self.assertIn("`SW-PHONO3PY` supports this problem (sources: SRC-PHONO3PY-DOCUMENTATION)", rendered)
        self.assertNotIn("PROBLEM-CRYSTAL-SYMMETRY-DETERMINATION", rendered)
        self.assertIn("ecosystem `includes` → software `supports` → problem path", rendered)

    def test_problem_discovery_language_filter_requires_implementation_and_support_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        rendered = rl.render_problem_discovery(
            records, ROOT / "reports/generated/evidence-recommendations.md",
            language_id="PROGRAMMING-LANGUAGE-C",
        )
        self.assertIn("**AND filters:** programming language `PROGRAMMING-LANGUAGE-C`.", rendered)
        self.assertIn("`PROBLEM-CRYSTAL-SYMMETRY-DETERMINATION`", rendered)
        self.assertIn("`SW-SPGLIB` is implemented in `PROGRAMMING-LANGUAGE-C` (sources: SRC-SPGLIB-DOCUMENTATION)", rendered)
        self.assertIn("`SW-SPGLIB` supports this problem (sources: SRC-SPGLIB-DOCUMENTATION)", rendered)
        self.assertNotIn("PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION", rendered)
        self.assertIn("software `implemented_in` → `supports` → problem path", rendered)

    def test_group_problem_filter_requires_development_and_direct_support_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        rendered = rl.render_group_discovery(
            records, None, None, None, None, None,
            ROOT / "reports/generated/evidence-recommendations.md",
            "PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION",
        )
        self.assertIn("**AND filters:** research problem `PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION`.", rendered)
        self.assertIn("`RG-DTU-CAMD`", rendered)
        self.assertIn("develops `SW-GPAW` (sources: SRC-DTU-CAMD-RESEARCH)", rendered)
        self.assertIn("`SW-GPAW` supports `PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION` (sources: SRC-GPAW-DOCUMENTATION)", rendered)
        self.assertIn("does not assert that the group works on the problem itself", rendered)

    def test_pi_problem_filter_requires_development_and_direct_support_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        rendered = rl.render_pi_discovery(
            records, None, None, None, None, None,
            ROOT / "reports/generated/evidence-recommendations.md",
            "PROBLEM-MACHINE-LEARNED-INTERATOMIC-POTENTIAL-MODELING",
        )
        self.assertIn("**AND filters:** research problem `PROBLEM-MACHINE-LEARNED-INTERATOMIC-POTENTIAL-MODELING`.", rendered)
        self.assertIn("`PI-GABOR-CSANYI`", rendered)
        self.assertIn("develops `SW-MACE` (sources: SRC-MACE-REPOSITORY)", rendered)
        self.assertIn("`SW-MACE` supports `PROBLEM-MACHINE-LEARNED-INTERATOMIC-POTENTIAL-MODELING` (sources: SRC-MACE-DOCUMENTATION)", rendered)
        self.assertIn("does not assert that the PI works on, endorses, or supervises the problem", rendered)

    def test_university_problem_filter_requires_direct_host_development_and_support_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        rendered = rl.render_university_discovery(
            records, None, None, None, None, None,
            ROOT / "reports/generated/evidence-recommendations.md",
            "PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION",
        )
        self.assertIn("**AND filters:** research problem `PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION`.", rendered)
        self.assertIn("`UNIVERSITY-DTU`", rendered)
        self.assertIn("directly hosts `RG-DTU-CAMD`", rendered)
        self.assertIn("`RG-DTU-CAMD`: develops `SW-GPAW` (sources: SRC-DTU-CAMD-RESEARCH)", rendered)
        self.assertIn("`RG-DTU-CAMD`: `SW-GPAW` supports `PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION` (sources: SRC-GPAW-DOCUMENTATION)", rendered)
        self.assertIn("does not assert that the University works on, owns, or endorses the problem", rendered)

    def test_ecosystem_problem_filter_requires_inclusion_and_support_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        rendered = rl.render_ecosystem_discovery(
            records, None, None,
            ROOT / "reports/generated/evidence-recommendations.md",
            "PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION",
        )
        self.assertIn("**AND filters:** research problem `PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION`.", rendered)
        self.assertIn("`ECO-PHONO3PY`", rendered)
        self.assertIn("`ECO-PHONO3PY` includes `SW-PHONO3PY` (sources: SRC-PHONO3PY-DOCUMENTATION, SRC-PHONO3PY-REPOSITORY)", rendered)
        self.assertIn("`SW-PHONO3PY` supports this problem (sources: SRC-PHONO3PY-DOCUMENTATION)", rendered)
        self.assertIn("ecosystem `includes` → software `supports` → problem", rendered)

    def test_software_problem_filter_requires_direct_support_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        rendered = rl.render_software_discovery(
            records, None, None, None,
            ROOT / "reports/generated/evidence-recommendations.md",
            problem_id="PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION",
        )
        self.assertIn("**AND filters:** research problem `PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION`.", rendered)
        self.assertIn("`SW-PHONO3PY`", rendered)
        self.assertIn("supports `PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION` (sources: SRC-PHONO3PY-DOCUMENTATION)", rendered)
        self.assertNotIn("`SW-SPGLIB`", rendered)
        self.assertIn("software record's direct sourced `supports` assertion", rendered)

    def test_research_problem_view_and_typed_support_path_are_present(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        problem = records["PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION"]
        support = rl.matching_assertions(records["SW-PHONO3PY"], "supports", {problem.id})
        self.assertEqual(1, len(support))
        self.assertEqual(["SRC-PHONO3PY-DOCUMENTATION"], support[0]["source_ids"])
        generated = (ROOT / "views/generated/research-problems.md").read_text(encoding="utf-8")
        self.assertIn(problem.id, generated)
        self.assertIn("SW-PHONO3PY", generated)
        symmetry_problem = records["PROBLEM-CRYSTAL-SYMMETRY-DETERMINATION"]
        symmetry_support = rl.matching_assertions(records["SW-SPGLIB"], "supports", {symmetry_problem.id})
        self.assertEqual(1, len(symmetry_support))
        self.assertEqual(["SRC-SPGLIB-DOCUMENTATION"], symmetry_support[0]["source_ids"])
        self.assertIn(symmetry_problem.id, generated)
        self.assertIn("SW-SPGLIB", generated)
        mlip_problem = records["PROBLEM-MACHINE-LEARNED-INTERATOMIC-POTENTIAL-MODELING"]
        for software_id, source_id in {
            "SW-MACE": "SRC-MACE-DOCUMENTATION",
            "SW-NEQUIP": "SRC-NEQUIP-DOCUMENTATION",
            "SW-DEEPMD-KIT": "SRC-DEEPMD-DOCUMENTATION",
        }.items():
            support = rl.matching_assertions(records[software_id], "supports", {mlip_problem.id})
            self.assertEqual(1, len(support))
            self.assertEqual([source_id], support[0]["source_ids"])
        self.assertIn(mlip_problem.id, generated)
        self.assertIn("SW-MACE", generated)
        self.assertIn("SW-NEQUIP", generated)
        self.assertIn("SW-DEEPMD-KIT", generated)
        dft_problem = records["PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION"]
        for software_id, source_id in {
            "SW-ABINIT": "SRC-ABINIT-PRESENTATION",
            "SW-QUANTUM-ESPRESSO": "SRC-QE-HOME",
            "SW-GPAW": "SRC-GPAW-DOCUMENTATION",
            "SW-SIESTA": "SRC-SIESTA-REFERENCE-MANUAL",
        }.items():
            support = rl.matching_assertions(records[software_id], "supports", {dft_problem.id})
            self.assertEqual(1, len(support))
            self.assertEqual([source_id], support[0]["source_ids"])
        self.assertIn(dft_problem.id, generated)
        self.assertIn("SW-ABINIT", generated)
        self.assertIn("SW-QUANTUM-ESPRESSO", generated)
        self.assertIn("SW-GPAW", generated)
        self.assertIn("SW-SIESTA", generated)

    def test_research_problem_requires_a_controlled_area_link(self) -> None:
        metadata = {
            "schema_version": 2, "entity_type": "research-problem", "id": "PROBLEM-TEST",
            "name": "Test Problem", "status": "reviewed", "created_at": "2026-07-13",
            "updated_at": "2026-07-13", "last_review": "2026-07-13", "confidence": "high",
            "source_ids": ["SRC-TEST"], "problem_kind": "test challenge",
        }
        record = rl.Record(ROOT / "entities/research-problems/test.md", metadata, "")
        results = rl.Results([], [])
        rl.validate_schema(ROOT, {record.id: record}, results)
        self.assertTrue(any("research_area_ids" in error for error in results.errors))

    def test_area_discovery_exposes_topic_coverage_without_ranking(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        rendered = rl.render_area_discovery(records, ROOT / "reports/generated/evidence-recommendations.md")
        self.assertIn("# Research-area discovery", rendered)
        self.assertIn("not a research-problem ranking", rendered)
        self.assertIn("`AREA-COMPUTATIONAL-PHONON-CALCULATIONS`", rendered)
        self.assertIn("groups: 1; principal investigators: 1; software: 2; problems: 1; universities: 0; ecosystems: 2", rendered)
        self.assertIn("sources: SRC-PHONOPY-DOCUMENTATION", rendered)

    def test_area_discovery_filters_on_a_problem_own_sourced_classification(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        rendered = rl.render_area_discovery(
            records,
            ROOT / "reports/generated/evidence-recommendations.md",
            "PROBLEM-MATERIALS-PROPERTY-PREDICTION",
        )
        self.assertIn("**Problem filter:** research problem `PROBLEM-MATERIALS-PROPERTY-PREDICTION`.", rendered)
        self.assertIn("`AREA-AI-FOR-MATERIALS`", rendered)
        self.assertIn("`AREA-MATERIALS-INFORMATICS`", rendered)
        self.assertNotIn("`AREA-MACHINE-LEARNED-POTENTIALS`", rendered)
        self.assertIn("SRC-CHGNET-HOME, SRC-MATGL-DOCUMENTATION", rendered)
        self.assertIn("does not infer a topic from software, people, institutions, or graph adjacency", rendered)

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
            ["ECO-DEEPMD-KIT", "ECO-FAIR-CHEM", "ECO-MATERIALS-PROJECT", "ECO-MATML", "ECO-NEQUIP", "ECO-OPEN-CATALYST-PROJECT"],
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

    def test_m3gnet_publication_is_a_sourced_author_and_area_path(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        publication = records["PUB-M3GNET-2022"]
        self.assertEqual("2022-11-28", publication.metadata["publication_date"])
        self.assertEqual(
            ["PI-SHYUE-PING-ONG"],
            [assertion["target_id"] for assertion in rl.matching_assertions(publication, "authored_by")],
        )
        self.assertEqual(
            ["AREA-MACHINE-LEARNED-POTENTIALS"],
            [assertion["target_id"] for assertion in rl.matching_assertions(publication, "addresses")],
        )
        self.assertEqual(
            ["SW-M3GNET"],
            [assertion["target_id"] for assertion in rl.matching_assertions(publication, "describes")],
        )
        self.assertEqual("archived", records["SW-M3GNET"].metadata["software_lifecycle"])
        self.assertEqual(["SRC-M3GNET-REPOSITORY"], records["SW-M3GNET"].metadata["lifecycle_source_ids"])
        self.assertIn("PUB-M3GNET-2022", records["PI-SHYUE-PING-ONG"].metadata["publication_ids"])
        research_area_view = rl.render_view(
            next(view for view in rl.yaml.safe_load((ROOT / "views/definitions.yaml").read_text(encoding="utf-8"))["views"] if view["view_id"] == "research-areas"),
            records,
            ROOT / "reports/generated/views/research-areas.md",
            "test-fingerprint",
        )
        self.assertIn("PUB-M3GNET-2022", research_area_view)

    def test_recommendation_catalog_lists_available_and_unavailable_queries(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        catalog = rl.recommendation_catalog(model)
        self.assertIn("`groups-ai-for-materials` | available", catalog)
        self.assertIn("`python-heavy-research-groups` | available", catalog)
        self.assertIn("`high-mentorship-environments` | unavailable", catalog)
        self.assertIn("`dominant-research-ecosystems` | unavailable", catalog)
        self.assertIn("`strongest-academic-environments` | unavailable", catalog)
        self.assertIn("`best-research-problems` | unavailable", catalog)
        self.assertIn("`best-research-advisors` | unavailable", catalog)
        self.assertIn("No private profiles", catalog)

    def test_problem_comparison_remains_gated_by_an_explicit_evidence_contract(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        query = next(item for item in model["queries"] if item["query_id"] == "best-research-problems")
        self.assertEqual("unavailable", query["status"])

        adr = (ROOT / "docs/adr/0010-problem-evaluation-evidence-contract.md").read_text(encoding="utf-8")
        self.assertIn("stakeholder scope and decision purpose", adr)
        self.assertIn("missing-data handling, and uncertainty representation", adr)
        self.assertIn("Versioned aggregation and sensitivity rules", adr)
        self.assertIn("Ethics review", adr)

        recommendations = (ROOT / "docs/recommendations.md").read_text(encoding="utf-8")
        self.assertIn("adr/0010-problem-evaluation-evidence-contract.md", recommendations)

    def test_public_status_documents_match_the_current_graph_contract(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        assertion_count = sum(
            len(record.metadata.get("relationship_assertions", []) or [])
            for record in records.values()
        )

        roadmap = (ROOT / "ROADMAP_STATUS.md").read_text(encoding="utf-8")
        self.assertIn(f"{len(records)} canonical entities", roadmap)
        self.assertIn(f"{assertion_count} evidence-bearing typed relationships", roadmap)
        self.assertIn("comparative\nproblem-evaluation evidence contracts", roadmap)

        architecture = (ROOT / "docs/ARCHITECTURE_STATUS.md").read_text(encoding="utf-8")
        self.assertIn("Accepted ADR 0009", architecture)
        self.assertIn("Accepted ADR 0010", architecture)

    def test_ai_materials_software_environment_query_is_explainable(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        query = next(item for item in model["queries"] if item["query_id"] == "environments-for-ai-materials-software-engineers")
        candidates = rl.recommendation_candidates(query, records)
        self.assertEqual(["RG-CEDER-GROUP", "RG-MATERIALYZE-AI"], sorted(candidate["record"].id for candidate in candidates))
        self.assertTrue(all(candidate["criteria"] == 2 for candidate in candidates))
        self.assertTrue(all(any("develops `SW-" in signal["label"] for signal in candidate["signals"]) for candidate in candidates))

    def test_recommendation_kind_filter_contract_is_satisfied(self) -> None:
        records, results = rl.validate(ROOT)
        self.assertEqual([], results.errors)
        model, model_errors = rl.validate_recommendation_model(ROOT, records)
        self.assertEqual([], model_errors)
        for query in model["queries"]:
            if query.get("status") == "unavailable":
                continue
            for field in rl.RECOMMENDATION_REQUIRED_FILTERS.get(query["kind"], ()):
                self.assertTrue(rl.as_ids(query.get(field)), f"{query['query_id']} requires {field}")


if __name__ == "__main__":
    unittest.main()
