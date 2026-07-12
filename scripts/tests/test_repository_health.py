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
        self.assertEqual(67, audit["reviewed_records"])
        self.assertEqual(67, len(audit["buckets"]["current"]))
        self.assertEqual([], audit["buckets"]["attention"])
        self.assertEqual([], audit["buckets"]["stale"])
        self.assertIn("does not measure research quality", rl.render_freshness_audit(audit))


if __name__ == "__main__":
    unittest.main()
