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
        self.language = None
        self.main_count = 0
        self.h1_count = 0

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if "id" in data:
            self.ids.append(data["id"])
        if tag == "a":
            self.links.append(data)
        if tag == "h3":
            self.headings.append(tag)
        if tag == "h1":
            self.h1_count += 1
        if tag == "main":
            self.main_count += 1
        if tag == "html":
            self.language = data.get("lang")
        if tag == "img":
            self.images.append(data)
        if tag == "meta" and data.get("name", "").lower() == "robots":
            self.robots.append(data.get("content", "").lower())


def parse_document(path):
    document = Markup()
    document.feed(path.read_text(encoding="utf-8"))
    return document


class GlossaryIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = parse_document(GLOSSARY)
        cls.html = GLOSSARY.read_text(encoding="utf-8")

    def test_twelve_definitions_and_unique_ids(self):
        self.assertEqual(len(self.doc.headings), 12)
        self.assertEqual(len(self.doc.ids), len(set(self.doc.ids)))
        self.assertIn("main", self.doc.ids)
        self.assertIn("termini", self.doc.ids)

    def test_accessible_document_basics(self):
        self.assertEqual(self.doc.language, "it")
        self.assertEqual(self.doc.main_count, 1)
        self.assertEqual(self.doc.h1_count, 1)
        self.assertTrue(any(link.get("href") == "#main" for link in self.doc.links))

    def test_noindex_and_demo_disclosure(self):
        self.assertTrue(any("noindex" in value for value in self.doc.robots))
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
            self.assertFalse(path.startswith("/") or "\\" in path or ".." in Path(path).parts, href)
            target = ROOT / path if path else GLOSSARY
            self.assertTrue(target.is_file(), href)
            if parsed.fragment:
                target_document = self.doc if not path else parse_document(target)
                self.assertIn(unquote(parsed.fragment), target_document.ids, href)

    def test_images_and_external_tab_safety(self):
        for image in self.doc.images:
            self.assertIn("alt", image)
        for link in self.doc.links:
            if link.get("target") == "_blank":
                rel = set(link.get("rel", "").split())
                self.assertTrue({"noopener", "noreferrer"} <= rel)


if __name__ == "__main__":
    unittest.main()
