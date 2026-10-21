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

    def test_privacy_page_is_linked_from_main_pages(self):
        for name in ("index.html", "risorse.html", "guida.html", "usb-c.html", "catalogo.html"):
            with self.subTest(page=name):
                html = (self.site / name).read_text(encoding="utf-8")
                self.assertIn('href="privacy.html"', html)

    def test_privacy_page_is_cautious_and_noindex(self):
        html = (self.site / "privacy.html").read_text(encoding="utf-8")
        self.assertIn('<meta name="robots" content="noindex,nofollow">', html)
        self.assertIn("nota informativa preliminare", html)
        self.assertIn("informativa privacy di GitHub", html)
        self.assertIn("non integra moduli di contatto", html)

    def test_catalog_disclosure_matches_inactive_affiliate_state(self):
        html = (self.site / "catalogo.html").read_text(encoding="utf-8")
        self.assertIn("In questa anteprima non sono presenti link affiliati attivi.", html)
        self.assertNotIn("Questo sito contiene link di affiliazione", html)

    def test_homepage_and_resources_list_the_same_four_original_guides(self):
        import re
        home = (self.site / "index.html").read_text(encoding="utf-8")
        resources = (self.site / "risorse.html").read_text(encoding="utf-8")
        github_md = r"https://github\\.com/riccardomontanaroact-hub/affiliate-autopilot/blob/[^\\" ]+\\.md"
        self.assertEqual(len(re.findall(github_md, home)), 4)
        self.assertEqual(len(re.findall(github_md, resources)), 4)

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
        for name in ("index.html", "risorse.html", "guida.html", "usb-c.html", "privacy.html", "catalogo.html", "dashboard.html"):
            with self.subTest(page=name):
                html = (self.site / name).read_text(encoding="utf-8")
                self.assertIn('<meta name="robots" content="noindex,nofollow">', html)

    def test_generated_catalog_and_dashboard_have_skip_navigation(self):
        for name in ("catalogo.html", "dashboard.html"):
            with self.subTest(page=name):
                html = (self.site / name).read_text(encoding="utf-8")
                self.assertIn('<a class="skip" href="#contenuto">Salta al contenuto</a>', html)
                self.assertIn('id="contenuto"', html)

    def test_mobile_navigation_has_touch_targets_and_reduced_motion_support(self):
        css = (self.site / "style.css").read_text(encoding="utf-8")
        self.assertIn("min-height:44px", css)
        self.assertIn("@media(prefers-reduced-motion:reduce)", css)

    def test_local_navigation_targets_exist(self):
        import re
        pages = ("index.html", "risorse.html", "guida.html", "usb-c.html", "privacy.html", "catalogo.html", "dashboard.html")
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
