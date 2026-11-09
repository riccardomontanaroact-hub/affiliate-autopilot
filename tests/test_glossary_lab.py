"""Static integrity checks for the VORLI Lab editorial glossary.

Run: python -m unittest tests/test_glossary_lab.py -v
No network, third-party dependencies or production changes.
"""
from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / "preview" / "vorli-next"
GLOSSARY = ROOT / "glossario-tech-lab.html"


class Markup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.headings = []
        self.robots = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if "id" in data:
            self.ids.append(data["id"])
        if tag == "a":
            self.links.append(data)
        if tag == "h3":
            self.headings.append(tag)
        if tag == "img":
            self.images.append(data)
        if tag == "meta" and data.get("name", "").lower() == "robots":
            self.robots.append(data.get("content", "").lower())


class GlossaryIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = GLOSSARY.read_text(encoding="utf-8")
        cls.doc = Markup()
        cls.doc.feed(cls.html)

    def test_twelve_definitions_and_unique_ids(self):
        self.assertEqual(len(self.doc.headings), 12)
        self.assertEqual(len(self.doc.ids), len(set(self.doc.ids)))
        self.assertIn("main", self.doc.ids)
        self.assertIn("termini", self.doc.ids)

    def test_noindex_and_demo_disclosure(self):
        self.assertTrue(any("noindex" in x for x in self.doc.robots))
        self.assertIn("nessun prodotto acquistabile", self.html.lower())
        self.assertNotIn("<form", self.html.lower())
        self.assertNotIn("awin1.com", self.html.lower())

    def test_local_links_and_fragments(self):
        for link in self.doc.links:
            href = link.get("href", "")
            self.assertTrue(href, "Anchor missing href")
            parsed = urlsplit(href)
            self.assertFalse(parsed.scheme or parsed.netloc, href)
            path = unquote(parsed.path)
            self.assertFalse(path.startswith("/") or ".." in Path(path).parts, href)
            target = ROOT / path if path else GLOSSARY
            self.assertTrue(target.is_file(), href)
            if parsed.fragment and not path:
                self.assertIn(unquote(parsed.fragment), self.doc.ids, href)

    def test_images_and_external_tab_safety(self):
        for img in self.doc.images:
            self.assertIn("alt", img)
        for link in self.doc.links:
            if link.get("target") == "_blank":
                rel = set(link.get("rel", "").split())
                self.assertTrue({"noopener", "noreferrer"} <= rel)


if __name__ == "__main__":
    unittest.main()
