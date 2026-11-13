"""Structural regression checks for the unpublished VORLI decision matrix.

Run from repository root: python -m unittest discover -s tests -p 'test_decision_matrix_lab.py'
These checks do not replace browser, accessibility or legal reviews.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / "preview" / "vorli-next"
PAGE = ROOT / "matrice-scelta-tech-lab.html"
EXPECTED = (
    "Computer", "Software", "Elettronica", "Elettrodomestici smart",
    "Accessori casa", "Sport tech", "Benessere tecnologico", "Energia portatile",
)

class MatrixParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.articles = 0
        self.headers = []
        self.in_h3 = False
        self.in_dt = False
        self.terms = []
        self.text = []
        self.meta = []
        self.images = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "a":
            self.links.append(a)
        if tag == "article":
            self.articles += 1
        if tag == "h3":
            self.in_h3 = True
        if tag == "dt":
            self.in_dt = True
        if tag == "meta":
            self.meta.append(a)
        if tag == "img":
            self.images.append(a)
    def handle_endtag(self, tag):
        if tag == "h3":
            self.in_h3 = False
        if tag == "dt":
            self.in_dt = False
    def handle_data(self, data):
        s = data.strip()
        if s:
            self.text.append(s)
            if self.in_h3:
                self.headers.append(s)
            if self.in_dt:
                self.terms.append(s)

class DecisionMatrixLabTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = PAGE.read_text(encoding="utf-8")
        cls.doc = MatrixParser()
        cls.doc.feed(cls.html)

    def test_eight_categories_with_three_criteria_each(self):
        self.assertEqual(self.doc.articles, 8)
        self.assertEqual(self.doc.headers, [f"{i}. {name}" for i, name in enumerate(EXPECTED, 1)])
        self.assertEqual(self.doc.terms, ["Priorità", "Controllo critico", "Fonte da consultare"] * 8)

    def test_local_links_and_unique_anchors(self):
        self.assertEqual(len(self.doc.ids), len(set(self.doc.ids)))
        self.assertIn("main", self.doc.ids)
        self.assertTrue(self.doc.links)
        for link in self.doc.links:
            href = link.get("href", "")
            parsed = urlsplit(href)
            self.assertFalse(parsed.scheme or parsed.netloc, href)
            self.assertFalse(href.startswith("//"), href)
            target = unquote(parsed.path)
            if target:
                resolved = (ROOT / target).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT.resolve()), href)
                self.assertTrue(resolved.is_file(), href)
            if parsed.fragment and not target:
                self.assertIn(unquote(parsed.fragment), self.doc.ids)
            if link.get("target") == "_blank":
                self.assertIn("noopener", link.get("rel", "").split())

    def test_editorial_only_and_noindex(self):
        self.assertTrue(any(m.get("name") == "robots" and
                            "noindex" in m.get("content", "").lower()
                            for m in self.doc.meta))
        visible = " ".join(self.doc.text).lower()
        self.assertIn("nessun prodotto acquistabile", visible)
        self.assertIn("non negozio attivo", visible)
        self.assertNotRegex(self.html.lower(), r"<(?:form|script|iframe)\\b")
        self.assertNotRegex(self.html.lower(), r"https?://|awin1|add.to.cart|checkout")

    def test_accessibility_and_mobile_layout_basics(self):
        self.assertIn('lang="it"', self.html)
        self.assertIn('name="viewport"', self.html)
        self.assertIn('href="#main"', self.html)
        self.assertIn("focus-visible", self.html)
        self.assertIn("@media(max-width:700px)", self.html)
        self.assertIn("grid-template-columns:1fr", self.html)
        for img in self.doc.images:
            self.assertIn("alt", img)

if __name__ == "__main__":
    unittest.main()
