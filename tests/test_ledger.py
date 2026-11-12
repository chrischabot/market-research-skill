"""Tests for skill/scripts/ledger.py. Run with: python3 -m unittest discover tests"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "skill" / "scripts" / "ledger.py"

HEADER = "# {title}\n\nProduct: Tallyroom. Date: 2026-03-02. Written by: {role}.\nInputs: test.\n\n"
LINKS = "See https://example.com/a and https://example.com/b and https://example.org/c.\n"


def run_ledger(command, workspace):
    return subprocess.run(
        [sys.executable, str(SCRIPT), command, str(workspace)],
        capture_output=True,
        text=True,
    )


class LedgerTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.ws = Path(self.tmp.name)
        self.run_data = {
            "product": "Tallyroom",
            "depth": "standard",
            "budget": None,
            "agents_started": 2,
            "status": "in_progress",
            "started": "2026-03-02",
            "updated": "2026-03-02",
            "units": [
                {"id": "intake", "stage": 1, "role": "lead", "outputs": ["intake.md"], "status": "done"},
                {
                    "id": "area:stock",
                    "stage": 3,
                    "role": "component-analyst",
                    "outputs": ["components/stock.md"],
                    "status": "done",
                },
                {
                    "id": "competitor:shelfwise:feedback",
                    "stage": 6,
                    "role": "feedback-researcher",
                    "outputs": ["competitors/shelfwise-feedback.md"],
                    "status": "planned",
                },
            ],
        }
        self.write("intake.md", HEADER.format(title="Intake", role="lead"))
        self.write(
            "components/stock.md",
            HEADER.format(title="Stock", role="component analyst") + "Intended: rolling counts.\n",
        )

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        path = self.ws / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def save(self):
        self.write("run.json", json.dumps(self.run_data))

    def check(self):
        self.save()
        return run_ledger("check", self.ws)

    def test_consistent_ledger_passes(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("ledger and files agree", result.stdout)

    def test_done_unit_without_file_fails(self):
        self.run_data["units"][2]["status"] = "done"
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("does not exist", result.stdout)

    def test_evidence_document_needs_links(self):
        self.run_data["units"][2]["status"] = "done"
        self.write(
            "competitors/shelfwise-feedback.md",
            HEADER.format(title="Shelfwise", role="feedback researcher") + "People like it.\n",
        )
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("needs at least 3", result.stdout)

    def test_feedback_with_links_and_quotes_passes(self):
        self.run_data["units"][2]["status"] = "done"
        body = LINKS + "".join(
            f'"The stock counts were wrong again this week, number {n}" (https://example.com/t{n})\n'
            for n in range(3)
        )
        self.write(
            "competitors/shelfwise-feedback.md",
            HEADER.format(title="Shelfwise", role="feedback researcher") + body,
        )
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertNotIn("warning:", result.stdout)

    def test_missing_header_fails(self):
        self.write("intake.md", "# Intake\n\nNo header here.\n")
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("no 'Product:' header", result.stdout)

    def test_deferred_needs_a_note(self):
        self.run_data["units"][2]["status"] = "deferred"
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("needs a note", result.stdout)
        self.run_data["units"][2]["note"] = "budget could not fund this competitor"
        self.assertEqual(self.check().returncode, 0)

    def test_complete_run_cannot_have_open_units(self):
        self.run_data["status"] = "complete"
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("still open", result.stdout)

    def test_incomplete_run_needs_a_reason(self):
        self.run_data["status"] = "incomplete"
        self.assertEqual(self.check().returncode, 1)
        self.run_data["incomplete_reason"] = "no web access in this session"
        self.assertEqual(self.check().returncode, 0)

    def test_budget_overrun_fails(self):
        self.run_data["budget"] = 1
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("exceeds the budget", result.stdout)

    def test_output_cannot_escape_the_workspace(self):
        self.run_data["units"][0]["outputs"] = ["../intake.md"]
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("inside the workspace", result.stdout)

    def test_duplicate_ids_and_outputs_fail(self):
        self.run_data["units"].append(dict(self.run_data["units"][0]))
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate unit id", result.stdout)

    def test_broken_link_in_strategy_fails(self):
        self.run_data["units"].append(
            {
                "id": "strategy:pitches",
                "stage": 7,
                "role": "strategy-writer",
                "outputs": ["strategy/pitches.md"],
                "status": "done",
            }
        )
        self.write(
            "strategy/pitches.md",
            HEADER.format(title="Pitches", role="writer")
            + "See [the brief](product-brief.md) and [intake](../intake.md).\n",
        )
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("product-brief.md, which does not exist", result.stdout)
        self.assertNotIn("../intake.md, which", result.stdout)

    def test_unlisted_competitor_file_warns(self):
        self.write("competitors/stray-brief.md", "# Stray\n")
        result = self.check()
        self.assertEqual(result.returncode, 0)
        self.assertIn("no unit in the ledger lists it", result.stdout)

    def test_table_lists_units_and_summary(self):
        self.save()
        result = run_ledger("table", self.ws)
        self.assertEqual(result.returncode, 0)
        self.assertIn("| 3 | area:stock | component-analyst | done |", result.stdout)
        self.assertIn("2 done, 1 planned", result.stdout)
        self.assertIn("Agents started: 2, no budget set", result.stdout)

    def test_missing_ledger_is_reported(self):
        result = run_ledger("check", self.ws)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no run.json", result.stderr)


if __name__ == "__main__":
    unittest.main()
