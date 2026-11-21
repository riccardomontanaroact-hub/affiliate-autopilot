"""Semantic and commercial-safety checks for the unpublished VORLI decision matrix.

Run: python -m unittest discover -s tests -p 'test_matrix_semantics.py' -v
Uses only the Python standard library. Does not fetch external resources.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

PAGE = Path(__file__).resolve().parents[1] / "preview/vorli-next/matrice-scelta-tech-lab.html"


class MatrixParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.headings = []
        self.definitions = []
        self.meta = {}
        self.forbidden = []
        self.main_count = 0
        self.skip_link = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag in {"script", "iframe", "form", "button"}:
            self.forbidden.append(tag)
        if any(key.lower().startswith("on") for key in attributes):
            self.forbidden.append("event-handler")
        if tag == "main":
            self.main_count += 1
        if tag == "a" and attributes.get("href") == "#main":
            self.skip_link = True
        if tag == "meta" and attributes.get("name"):
            self.meta[attributes["name"].lower()] = attributes.get("content", "")
        if tag in {"h1", "h2", "h3", "dt", "dd"}:
            self.stack.append([tag, []])

    def handle_data(self, data):
        for _, chunks in self.stack:
            chunks.append(data)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1][0] == tag:
            _, chunks = self.stack.pop()
            value = " ".join(" ".join(chunks).split())
            if tag in {"h1", "h2", "h3"}:
                self.headings.append((tag, value))
            elif tag in {"dt", "dd"}:
                self.definitions.append((tag, value))


class MatrixSemantics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = PAGE.read_text(encoding="utf-8")
        cls.page = MatrixParser()
        cls.page.feed(cls.html)

    def test_eight_distinct_categories(self):
        titles = [value for tag, value in self.page.headings if tag == "h3"]
        self.assertEqual(len(titles), 8)
        self.assertEqual(len(set(titles)), 8)
        for name in ("Computer", "Software", "Elettronica", "Elettrodomestici",
                     "Accessori casa", "Sport tech", "Benessere", "Energia"):
            self.assertTrue(any(name.lower() in title.lower() for title in titles), name)

    def test_three_complete_criteria_per_category(self):
        labels = [value for tag, value in self.page.definitions if tag == "dt"]
        values = [value for tag, value in self.page.definitions if tag == "dd"]
        self.assertEqual(labels, ["Priorità", "Controllo critico", "Fonte da consultare"] * 8)
        self.assertEqual(len(values), 24)
        self.assertTrue(all(len(value) >= 12 for value in values))

    def test_accessibility_and_unpublished_metadata(self):
        self.assertEqual(self.page.main_count, 1)
        self.assertTrue(self.page.skip_link)
        self.assertEqual(len([tag for tag, _ in self.page.headings if tag == "h1"]), 1)
        self.assertIn("noindex", self.page.meta.get("robots", "").lower())
        self.assertIn("nofollow", self.page.meta.get("robots", "").lower())
        self.assertIn('lang="it"', self.html.lower())

    def test_no_active_commerce_or_tracking(self):
        self.assertEqual(self.page.forbidden, [])
        self.assertIsNone(re.search(r"(?i)(?:awin1|clickref|add.to.cart|checkout|paypal\.com|stripe\.com)", self.html))
        self.assertIn("nessun prodotto acquistabile", self.html.lower())


if __name__ == "__main__":
    unittest.main()
