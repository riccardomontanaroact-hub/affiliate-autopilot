"""Offline regression checks for the VORLI static fallback. Run: python -m unittest tests.test_catalog_static_fallback"""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
LAB = ROOT / "preview" / "vorli-next"


class StaticCatalogTests(unittest.TestCase):
    def test_categories_match_editorial_data(self):
        html = (LAB / "catalogo-statico-lab.html").read_text(encoding="utf-8")
        raw = (LAB / "catalogo-lab-data.js").read_text(encoding="utf-8")
        match = re.search(r"window.VORLI_CATALOG_LAB\s*=\s*(\{.*\});", raw, re.S)
        self.assertIsNotNone(match)
        data = json.loads(match.group(1))
        self.assertEqual(len(data["categories"]), 8)
        self.assertEqual(html.count('class="tile category"'), 8)
        for item in data["categories"]:
            self.assertIn("<h3>" + item["name"] + "</h3>", html)
        self.assertEqual(data["commercialOffers"], 0)
        self.assertFalse(data["checkoutEnabled"])

    def test_offline_and_no_commerce(self):
        html = (LAB / "catalogo-statico-lab.html").read_text(encoding="utf-8")
        self.assertIn('name="robots" content="noindex,nofollow"', html)
        self.assertIn('href="#main"', html)
        self.assertNotIn("<script", html.lower())
        self.assertNotIn("<form", html.lower())
        self.assertNotIn("checkout", html.lower().replace("nessun checkout", ""))
        self.assertIn('href="risorse-originali-lab.html"', html)
        self.assertTrue((LAB / "risorse-originali-lab.html").is_file())
        self.assertTrue((LAB / "catalogo-lab.css").is_file())


if __name__ == "__main__":
    unittest.main()
