"""Static resource landing regression checks; run: python -m unittest discover -s tests."""
import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "preview" / "vorli-next"
REPO = "https://github.com/riccardomontanaroact-hub/affiliate-autopilot/blob/"

class Anchors(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.cards = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "href" in a:
            self.hrefs.append(a["href"])
        if tag == "article" and "resource" in a.get("class", "").split():
            self.cards += 1

class StaticResourceLabTests(unittest.TestCase):
    def test_static_cards_and_source_registry(self):
        page = (LAB / "risorse-originali-lab.html").read_text(encoding="utf-8")
        raw = (LAB / "catalogo-lab-data.js").read_text(encoding="utf-8")
        match = re.search(r"window\.VORLI_CATALOG_LAB\s*=\s*(\{.*\});", raw, re.S)
        self.assertIsNotNone(match)
        data = json.loads(match.group(1))
        parser = Anchors()
        parser.feed(page)
        self.assertEqual(parser.cards, len(data["resources"]))
        self.assertEqual(5, parser.cards)
        actual = sorted(x for x in parser.hrefs if x.startswith(REPO))
        expected = sorted(REPO + item["source"] for item in data["resources"])
        self.assertEqual(expected, actual)
        self.assertNotIn("<script", page.lower())
        self.assertIn('name="robots" content="noindex,nofollow"', page)
        self.assertNotIn("<form", page.lower())
        for href in parser.hrefs:
            if href.startswith(("https://", "http://", "#")):
                continue
            self.assertTrue((LAB / href).is_file(), href)

    def test_catalog_links_to_static_resource_landing(self):
        page = (LAB / "catalogo-lab.html").read_text(encoding="utf-8")
        self.assertIn('href="risorse-originali-lab.html"', page)
        self.assertNotIn('href="risorse.html"', page)
        self.assertIn('name="robots" content="noindex,nofollow"', page)

if __name__ == "__main__":
    unittest.main()
