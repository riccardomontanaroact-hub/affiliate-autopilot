"""VORLI lab: offline structural regression tests for static catalog.
Run locally from repository root: python -m unittest discover -s tests -p 'test_catalog_lab_links_20261019.py'
"""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "preview" / "vorli-next"

class AnchorReader(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.extend(value for key, value in attrs if key == "href" and value)

class CatalogLinksTests(unittest.TestCase):
    def test_static_catalog_structure(self):
        html = (ROOT / "catalogo-statico-lab.html").read_text(encoding="utf-8")
        self.assertEqual(html.count('class="tile category"'), 8)
        self.assertIn('name="robots" content="noindex,nofollow"', html)
        self.assertNotIn("<script", html.lower())
        self.assertNotIn("<form", html.lower())

    def test_local_page_links_resolve(self):
        for page in ("catalogo-statico-lab.html", "catalogo-lab.html"):
            reader = AnchorReader()
            reader.feed((ROOT / page).read_text(encoding="utf-8"))
            for href in reader.hrefs:
                if href.startswith(("#", "https:", "http:", "mailto:")):
                    continue
                target = href.split("#", 1)[0].split("?", 1)[0]
                if target:
                    with self.subTest(page=page, target=target):
                        self.assertTrue((ROOT / target).is_file())

    @unittest.expectedFailure
    def test_interactive_catalog_exposes_static_fallback(self):
        """Known accessibility gap until interactive HTML can be updated."""
        html = (ROOT / "catalogo-lab.html").read_text(encoding="utf-8")
        self.assertIn('href="catalogo-statico-lab.html"', html)

if __name__ == "__main__":
    unittest.main()
