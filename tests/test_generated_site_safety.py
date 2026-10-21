"""Regression checks for the generated VORLI public pages."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestGeneratedSiteSafety(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(
            [sys.executable, "agent/build.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        cls.site = ROOT / "site"

    def test_generated_catalog_is_noindex_and_has_valid_meta_separation(self):
        html = (self.site / "catalogo.html").read_text(encoding="utf-8")
        self.assertIn('<meta name="robots" content="noindex,nofollow">\n<title>Catalogo | VORLI</title>', html)
        self.assertNotIn("\\n<title>Catalogo | VORLI</title>", html)

    def test_demo_catalog_has_no_purchase_links(self):
        html = (self.site / "catalogo.html").read_text(encoding="utf-8")
        self.assertIn("Acquisto non disponibile", html)
        self.assertNotIn('class="button" href=', html)
        self.assertNotIn("https://example.com", html)

    def test_generated_dashboard_is_noindex_and_hides_commercial_fields(self):
        html = (self.site / "dashboard.html").read_text(encoding="utf-8")
        self.assertIn('<meta name="robots" content="noindex,nofollow">', html)
        self.assertNotIn("Commissione", html)
        self.assertNotIn("affiliate_url", html)
        self.assertIn("Non disponibile", html)

    def test_public_ranked_export_excludes_demo_merchant(self):
        data = json.loads((ROOT / "data" / "ranked_products.json").read_text(encoding="utf-8"))
        self.assertTrue(data)
        self.assertTrue(all(item.get("status") == "unavailable" for item in data))
        self.assertTrue(all(item.get("merchant") != "INSERISCI NETWORK" for item in data))


if __name__ == "__main__":
    unittest.main()
