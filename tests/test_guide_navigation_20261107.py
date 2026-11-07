"""Static, offline quality gates for VORLI Lab's editorial buying guide.

Run: python -m unittest discover -s tests -p 'test_guide_navigation_20261107.py' -v
No network, external accounts, credentials, or production writes.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import unittest

ROOT = Path(__file__).resolve().parents[1] / "preview" / "vorli-next"
GUIDE = ROOT / "guida-scelta-tech-lab.html"


class GuideParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.images = []
        self.meta = {}
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a":
            self.links.append(a)
        if tag == "img":
            self.images.append(a)
        if tag == "meta" and a.get("name"):
            self.meta[a["name"].lower()] = a.get("content", "")
        if tag == "button":
            self.buttons.append(a)


class GuideIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = GUIDE.read_text(encoding="utf-8")
        cls.parser = GuideParser()
        cls.parser.feed(cls.html)

    def test_fragment_links_exist_and_ids_are_unique(self):
        ids = self.parser.ids
        self.assertEqual(len(ids), len(set(ids)), "Duplicate HTML IDs")
        for link in self.parser.links:
            href = link.get("href", "")
            fragment = urlsplit(href).fragment
            if fragment and not urlsplit(href).path:
                self.assertIn(unquote(fragment), ids, f"Broken fragment: {href}")

    def test_relative_files_exist_without_path_escape(self):
        for link in self.parser.links:
            href = link.get("href", "")
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (ROOT / unquote(parsed.path)).resolve()
            self.assertTrue(target.is_relative_to(ROOT.resolve()), f"Path escape: {href}")
            self.assertTrue(target.is_file(), f"Missing linked file: {href}")

    def test_lab_stays_noncommercial_and_nonindexed(self):
        robots = self.parser.meta.get("robots", "").lower().replace(" ", "")
        self.assertIn("noindex", robots)
        self.assertIn("nofollow", robots)
        lowered = self.html.lower()
        for token in ("checkout", "acquistabile"):
            self.assertIn(token, lowered, f"Missing explicit commercial disclaimer: {token}")
        for link in self.parser.links:
            href = link.get("href", "").lower()
            self.assertNotIn("awin1.com/cread.php", href)
            self.assertNotIn("paypal.com/checkout", href)

    def test_images_have_text_alternatives(self):
        for image in self.parser.images:
            self.assertIn("alt", image, f"Missing alt attribute: {image}")

    def test_new_tab_links_are_protected(self):
        for link in self.parser.links:
            if link.get("target", "").lower() == "_blank":
                rel = set(link.get("rel", "").lower().split())
                self.assertIn("noopener", rel)
                self.assertIn("noreferrer", rel)


if __name__ == "__main__":
    unittest.main()
