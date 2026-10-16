"""Offline smoke checks for the VORLI preview landing. Run: python -m unittest tests/test_resource_lab.py"""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREVIEW = ROOT / "preview" / "vorli-next"


class ResourceLabTests(unittest.TestCase):
    def test_preview_metadata(self):
        html = (PREVIEW / "risorse-originali-lab.html").read_text(encoding="utf-8")
        self.assertIn('content="noindex,nofollow"', html)
        self.assertIn('name="viewport"', html)
        self.assertIn('href="#main"', html)
        self.assertNotIn("<form", html)
        self.assertNotIn('type="submit"', html)

    def test_local_dependencies(self):
        for name in ("catalogo-lab.css", "catalogo-lab-data.js", "risorse-originali-lab.js"):
            self.assertTrue((PREVIEW / name).is_file(), name)

    def test_catalog_data(self):
        raw = (PREVIEW / "catalogo-lab-data.js").read_text(encoding="utf-8")
        match = re.search(r"window.VORLI_CATALOG_LAB\s*=\s*(\{.*\});", raw, re.S)
        self.assertIsNotNone(match)
        data = json.loads(match.group(1))
        self.assertEqual(len(data["categories"]), 8)
        self.assertEqual(len(data["resources"]), 5)
        self.assertEqual(data["commercialOffers"], 0)
        self.assertFalse(data["checkoutEnabled"])


if __name__ == "__main__":
    unittest.main()
