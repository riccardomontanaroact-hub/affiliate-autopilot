"""Static safety and content checks for the unpublished VORLI catalog lab."""
import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "preview" / "vorli-next"

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.local = []
        self.remote = []
        self.images = []
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "img":
            self.images.append(values.get("src", ""))
        for key in ("href", "src"):
            value = values.get(key)
            if not value:
                continue
            if value.startswith(("https://", "http://")):
                self.remote.append(value)
            elif not value.startswith(("#", "data:")):
                self.local.append(value.split("?", 1)[0])

class CatalogLabTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "catalogo-lab.html").read_text(encoding="utf-8")
        cls.js = (ROOT / "catalogo-lab.js").read_text(encoding="utf-8")
        cls.css = (ROOT / "catalogo-lab.css").read_text(encoding="utf-8")
        source = (ROOT / "catalogo-lab-data.js").read_text(encoding="utf-8")
        match = re.search(r"window\.VORLI_CATALOG_LAB\s*=\s*(\{.*\})\s*;", source, re.S)
        assert match, "Static JSON data not found"
        cls.data = json.loads(match.group(1))

    def test_catalog_is_demo_only(self):
        self.assertEqual(8, len(self.data["categories"]))
        self.assertEqual(5, len(self.data["resources"]))
        self.assertEqual(0, self.data["commercialOffers"])
        self.assertFalse(self.data["checkoutEnabled"])
        self.assertFalse(self.data["publicationApproved"])
        self.assertTrue(all(item["id"] for item in self.data["categories"]))
        self.assertEqual(8, len(set(item["id"] for item in self.data["categories"])))

    def test_all_resources_are_reviewable_sources(self):
        categories = {c["id"] for c in self.data["categories"]}
        for item in self.data["resources"]:
            self.assertIn(item["category"], categories)
            self.assertRegex(item["source"], r"^vorli/[a-z0-9-]+/(vault/products|drafts)/[A-Za-z0-9._-]+\.(md|html)$")
            self.assertIn(item["format"], {"Markdown", "HTML"})

    def test_preview_is_isolated_and_noindex(self):
        self.assertIn('name="robots" content="noindex,nofollow"', self.html)
        self.assertIn('name="viewport"', self.html)
        self.assertIn('href="#main"', self.html)
        self.assertIn('aria-live="polite"', self.html)
        parser = Links()
        parser.feed(self.html)
        self.assertEqual([], parser.images)
        expected_sources = sorted("https://github.com/riccardomontanaroact-hub/affiliate-autopilot/blob/" + item["source"] for item in self.data["resources"])
        self.assertEqual(expected_sources, sorted(parser.remote), "Only the five verified GitHub source links are allowed")
        for path in parser.local:
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertNotIn("checkout", self.js.lower())
        self.assertNotIn("fetch(", self.js)
        self.assertNotIn("XMLHttpRequest", self.js)
        self.assertNotIn("https://example.com", self.html + self.js)

    def test_accessibility_basics(self):
        self.assertIn("prefers-reduced-motion", self.css)
        self.assertIn(":focus-visible", self.css)
        self.assertIn('for="catalog-search"', self.html)
        self.assertIn('for="category-filter"', self.html)
        self.assertIn("aria-current", self.html)

if __name__ == "__main__":
    unittest.main()
