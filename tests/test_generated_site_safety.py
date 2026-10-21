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

    def test_all_generated_public_pages_remain_noindex(self):
        for name in ("index.html", "risorse.html", "guida.html", "usb-c.html", "catalogo.html", "dashboard.html"):
            with self.subTest(page=name):
                html = (self.site / name).read_text(encoding="utf-8")
                self.assertIn('<meta name="robots" content="noindex,nofollow">', html)

    def test_generated_catalog_and_dashboard_have_skip_navigation(self):
        for name in ("catalogo.html", "dashboard.html"):
            with self.subTest(page=name):
                html = (self.site / name).read_text(encoding="utf-8")
                self.assertIn('<a class="skip" href="#contenuto">Salta al contenuto</a>', html)
                self.assertIn('id="contenuto"', html)

    def test_local_navigation_targets_exist(self):
        import re
        pages = ("index.html", "risorse.html", "guida.html", "usb-c.html", "catalogo.html", "dashboard.html")
        for page in pages:
            html = (self.site / page).read_text(encoding="utf-8")
            for target in re.findall(r"""href=["']([^"']+)["']""", html):
                if target.startswith(("https://", "http://", "mailto:", "tel:", "#", "javascript:")):
                    continue
                local = target.split("#", 1)[0].split("?", 1)[0]
                if local:
                    with self.subTest(page=page, target=target):
                        self.assertTrue((self.site / local).is_file(), f"Missing local target {target}")

    def test_public_ranked_export_excludes_demo_merchant(self):
        data = json.loads((ROOT / "data" / "ranked_products.json").read_text(encoding="utf-8"))
        self.assertTrue(data)
        demo_items = [item for item in data if item.get("id") == "demo-001"]
        self.assertTrue(demo_items, "The demo fixture should remain in the public export")
        self.assertTrue(all(item.get("status") == "unavailable" for item in demo_items))
        self.assertTrue(all(item.get("merchant") != "INSERISCI NETWORK" for item in data))


if __name__ == "__main__":
    unittest.main()
