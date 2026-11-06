"""Offline regression checks for VORLI Lab resource links and disclosure.

Run: python -m unittest tests/test_resource_links_lab.py -v
No network calls; remote GitHub targets are syntactically checked, not fetched.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import unittest

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "preview" / "vorli-next"
PAGE = LAB / "risorse-originali-lab.html"


class ResourceParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = []
        self.robots = []
        self.resource_count = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "meta" and attrs.get("name") == "robots":
            self.robots.append(attrs.get("content", "").lower())
        if tag == "article" and "resource" in attrs.get("class", "").split():
            self.resource_count += 1
        if tag == "a":
            self.links.append(attrs)


class ResourceLinkIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = PAGE.read_text(encoding="utf-8")
        cls.parser = ResourceParser()
        cls.parser.feed(cls.html)

    def test_preview_disclosure_and_count(self):
        self.assertEqual(self.parser.resource_count, 5)
        self.assertIn("noindex", " ".join(self.parser.robots))
        self.assertIn("Nessuno è acquistabile", self.html)
        self.assertIn("Nessuna vendita attiva", self.html)

    def test_local_links_and_fragment_targets(self):
        self.assertEqual(len(self.parser.ids), len(set(self.parser.ids)))
        for link in self.parser.links:
            href = link.get("href", "")
            self.assertTrue(href, "Link senza href")
            parsed = urlparse(href)
            if parsed.scheme or parsed.netloc:
                continue
            with self.subTest(href=href):
                if parsed.path:
                    path = (LAB / parsed.path).resolve()
                    self.assertTrue(path.is_relative_to(LAB.resolve()), href)
                    self.assertTrue(path.is_file(), href)
                if parsed.fragment and not parsed.path:
                    self.assertIn(parsed.fragment, self.parser.ids)

    def test_external_links_are_safe_and_source_only(self):
        external = []
        for link in self.parser.links:
            href = link["href"]
            parsed = urlparse(href)
            if not parsed.scheme and not parsed.netloc:
                continue
            external.append(href)
            with self.subTest(href=href):
                self.assertEqual(parsed.scheme, "https")
                self.assertEqual(parsed.hostname, "github.com")
                self.assertTrue(parsed.path.startswith(
                    "/riccardomontanaroact-hub/affiliate-autopilot/blob/"))
                self.assertNotIn("..", parsed.path.split("/"))
                self.assertEqual(link.get("target"), "_blank")
                self.assertTrue({"noopener", "noreferrer"}.issubset(
                    set(link.get("rel", "").split())))
        self.assertEqual(len(external), 5)
        self.assertEqual(len(set(external)), 5)


if __name__ == "__main__":
    unittest.main()
