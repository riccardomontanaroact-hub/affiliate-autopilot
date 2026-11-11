"""Offline regression checks for the VORLI Lab glossary print layout.

Run: python -m unittest discover -s tests -p 'test_glossary_print_lab.py' -v
Static checks only: a browser print preview and physical-device audit remain required.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1] / "preview" / "vorli-next"
HTML = ROOT / "glossario-tech-lab.html"
PRINT = ROOT / "glossario-print.css"


class StylesheetLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.cards = 0

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "link" and attributes.get("rel") == "stylesheet":
            self.links.append(attributes)
        if tag == "article" and "guide-card" in attributes.get("class", "").split():
            self.cards += 1


class GlossaryPrintRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = HTML.read_text(encoding="utf-8")
        cls.css = PRINT.read_text(encoding="utf-8")
        cls.document = StylesheetLinks()
        cls.document.feed(cls.html)

    def test_print_stylesheet_is_local_and_print_only(self):
        matches = [link for link in self.document.links
                   if link.get("href") == PRINT.name]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].get("media"), "print")
        self.assertTrue(PRINT.is_file())
        self.assertNotIn("@import", self.css.lower())
        self.assertNotIn("url(", self.css.lower())

    def test_twelve_printable_definition_cards(self):
        self.assertEqual(self.document.cards, 12)
        self.assertRegex(self.css, r"\\.guide-grid\\s*\\{[^}]*grid-template-columns\\s*:\\s*1fr\\s+1fr")
        self.assertRegex(self.css, r"\\.guide-card\\s*\\{[^}]*break-inside\\s*:\\s*avoid")
        self.assertIn("page-break-inside: avoid", self.css)

    def test_print_readability_and_navigation_exclusion(self):
        self.assertRegex(self.css, r"@media\\s+print\\s*\\{")
        self.assertRegex(self.css, r"@page\\s*\\{[^}]*size\\s*:\\s*A4")
        self.assertRegex(self.css, r"body\\s*\\{[^}]*background\\s*:\\s*#fff")
        self.assertRegex(self.css, r"body\\s*\\{[^}]*color\\s*:\\s*#111827")
        self.assertRegex(self.css, r"header\\s*,\\s*\\.footer[^}]*display\\s*:\\s*none")
        self.assertIn(".guide-card p { font-size: 10pt", self.css)

    def test_no_commercial_or_remote_dependencies_in_print_css(self):
        self.assertNotRegex(self.css.lower(), r"https?://|awin1\\.com|checkout|<script")
        self.assertNotIn("position: fixed", self.css.lower())


if __name__ == "__main__":
    unittest.main()
