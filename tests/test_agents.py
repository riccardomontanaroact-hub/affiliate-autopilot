import json
import tempfile
import unittest
from pathlib import Path

from agent.agents import REQUIRED_PAGES, run_agents, render_markdown


class AgentRunnerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "agent").mkdir()
        (self.root / "data").mkdir()
        (self.root / "site").mkdir()
        (self.root / "agent" / "build.py").write_text("# build", encoding="utf-8")
        (self.root / "data" / "config.json").write_text(json.dumps({
            "affiliate_disclosure": "Disclosure", "networks": ["awin"]
        }), encoding="utf-8")
        (self.root / "data" / "products.json").write_text(json.dumps([{
            "id": "demo", "name": "Demo", "merchant": "DEMO",
            "affiliate_url": "https://example.com/", "price": 12
        }]), encoding="utf-8")
        for page in REQUIRED_PAGES:
            (self.root / "site" / page).write_text(
                '<!doctype html><html lang="it"><head><meta name="viewport" content="width=device-width,initial-scale=1">'
                '<title>Test</title><meta name="description" content="Test page"></head><body></body></html>',
                encoding="utf-8",
            )

    def tearDown(self):
        self.tmp.cleanup()

    def test_runs_five_named_agents(self):
        report = run_agents(self.root)
        self.assertEqual(report["summary"]["agents_run"], 5)
        self.assertEqual(
            [a["agent"] for a in report["agents"]],
            ["Coordinatore e Stratega", "Creatore del Sito e Catalogo", "Monetizzatore",
             "Designer e SEO", "Promotore e Partnership"],
        )

    def test_demo_product_is_flagged_without_commerce_actions(self):
        report = run_agents(self.root)
        monetizer = next(a for a in report["agents"] if a["agent"] == "Monetizzatore")
        promoter = next(a for a in report["agents"] if a["agent"] == "Promotore e Partnership")
        self.assertEqual(monetizer["status"], "ATTENZIONE")
        self.assertIn("Scheda demo da sostituire: demo", monetizer["findings"])
        self.assertIn("Nessun contatto esterno inviato.", promoter["summary"])

    def test_unapproved_real_offer_is_not_counted_as_publishable(self):
        products_path = self.root / "data" / "products.json"
        products = json.loads(products_path.read_text(encoding="utf-8"))
        products.append({
            "id": "pending-001",
            "name": "Offerta in attesa",
            "merchant": "Venditore reale",
            "affiliate_url": "https://track.example.org/pending",
            "commission_rate": 0.05,
            "verification": {
                "program": "Awin",
                "approval_status": "pending",
                "source_url": "https://merchant.example.org/product",
                "source_checked_at": "2026-10-22",
                "commission_source_url": "https://network.example.org/commission",
                "commission_checked_at": "2026-10-22",
                "checked_by": "revisione manuale"
            }
        })
        products_path.write_text(json.dumps(products), encoding="utf-8")

        report = run_agents(self.root)
        monetizer = next(a for a in report["agents"] if a["agent"] == "Monetizzatore")
        self.assertEqual(monetizer["status"], "ATTENZIONE")
        self.assertIn(
            "Offerta non pubblicabile: approvazione o verifiche mancanti: pending-001",
            monetizer["findings"],
        )
        self.assertEqual(report["summary"]["products_publishable"], 0)

    def test_markdown_report_is_auditable(self):
        report = run_agents(self.root)
        markdown = render_markdown(report)
        self.assertIn("# Rapporto agenti VORLI", markdown)
        self.assertIn("Non sono ancora agenti LLM autonomi", markdown)
        self.assertEqual(markdown.count("## "), 5)


if __name__ == "__main__":
    unittest.main()
