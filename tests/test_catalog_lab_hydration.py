"""Dependency-free regression checks for VORLI Lab static-first catalog.
Run from a repository checkout: python -m unittest discover -s tests -p 'test_catalog_lab_hydration.py'
"""
import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "preview" / "vorli-next"


class Cards(HTMLParser):
    def __init__(self):
        super().__init__()
        self.container = None
        self.current = None
        self.heading = False
        self.cards = {"category-cards": [], "resource-cards": []}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id") in self.cards:
            self.container = attrs["id"]
        if self.container and tag == "article":
            self.current = {"category": attrs.get("data-category"), "title": "", "link": None}
            self.cards[self.container].append(self.current)
        if self.current and tag == "h3":
            self.heading = True
        if self.current and tag == "a":
            self.current["link"] = attrs.get("href")

    def handle_endtag(self, tag):
        if tag == "h3":
            self.heading = False
        if tag == "article":
            self.current = None

    def handle_data(self, data):
        if self.current and self.heading:
            self.current["title"] += data


class CatalogHydrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (LAB / "catalogo-lab.html").read_text(encoding="utf-8")
        cls.js = (LAB / "catalogo-lab.js").read_text(encoding="utf-8")
        raw = (LAB / "catalogo-lab-data.js").read_text(encoding="utf-8")
        match = re.search(r"window\.VORLI_CATALOG_LAB\s*=\s*(\{.*\})\s*;", raw, re.S)
        assert match, "Catalog data must be a JSON object assigned to VORLI_CATALOG_LAB"
        cls.data = json.loads(match.group(1))
        cls.cards = Cards()
        cls.cards.feed(cls.html)

    def test_eight_categories_and_five_resources_match_data(self):
        categories = self.cards.cards["category-cards"]
        resources = self.cards.cards["resource-cards"]
        self.assertEqual(len(categories), 8)
        self.assertEqual(len(resources), 5)
        self.assertEqual([(c["category"], c["title"].strip()) for c in categories],
                         [(c["id"], c["name"]) for c in self.data["categories"]])
        self.assertEqual([(r["category"], r["title"].strip()) for r in resources],
                         [(r["category"], r["title"]) for r in self.data["resources"]])

    def test_resource_links_are_exactly_editorial_sources(self):
        for card, item in zip(self.cards.cards["resource-cards"], self.data["resources"]):
            self.assertRegex(item["source"], r"^vorli/[a-z0-9-]+/(?:vault/products|drafts)/[a-zA-Z0-9._-]+\.(?:md|html)$")
            self.assertEqual(card["link"],
                "https://github.com/riccardomontanaroact-hub/affiliate-autopilot/blob/" + item["source"])

    def test_script_never_replaces_static_cards(self):
        self.assertNotIn("replaceChildren(", self.js)
        self.assertNotIn("innerHTML", self.js)
        self.assertIn("categorySync", self.js)
        self.assertIn("resourceSync", self.js)
        self.assertIn('document.documentElement.classList.add("js-ready")', self.js)

    def test_no_commerce_in_preview(self):
        self.assertNotRegex(self.html.lower(), r"<form\b|<iframe\b")
        self.assertIn("noindex,nofollow", self.html)
        self.assertNotIn("checkoutEnabled: true", self.js)


if __name__ == "__main__":
    unittest.main()
