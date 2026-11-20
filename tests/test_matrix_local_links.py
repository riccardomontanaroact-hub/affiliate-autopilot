"""Offline link integrity checks for unpublished VORLI editorial matrix.

Run: python -m unittest discover -s tests -p 'test_matrix_local_links.py' -v
No network calls, third-party dependencies or production writes.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "preview" / "vorli-next" / "matrice-scelta-tech-lab.html"


class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag in {"a", "link", "script", "img", "source"}:
            key = {"a": "href", "link": "href", "script": "src",
                   "img": "src", "source": "srcset"}[tag]
            if attrs.get(key):
                self.links.append((tag, attrs[key]))
        if tag == "img":
            self.images.append(attrs)


class MatrixLocalLinks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Links()
        cls.parser.feed(PAGE.read_text(encoding="utf-8"))

    def test_all_referenced_files_exist(self):
        for tag, url in self.parser.links:
            with self.subTest(tag=tag, url=url):
                parsed = urlsplit(url)
                self.assertFalse(parsed.scheme or parsed.netloc,
                                 "External reference in unpublished Lab")
                self.assertFalse(url.startswith("//"))
                self.assertFalse(parsed.path.startswith("/"),
                                 "Root-relative URL breaks GitHub Pages project paths")
                if parsed.path:
                    path = unquote(parsed.path)
                    self.assertNotIn("..", Path(path).parts, "Path traversal")
                    target = PAGE.parent / path
                    self.assertTrue(target.is_file(), f"Missing local file: {url}")

    def test_fragment_targets_exist(self):
        ids = set(self.parser.ids)
        for tag, url in self.parser.links:
            fragment = unquote(urlsplit(url).fragment)
            if fragment and not urlsplit(url).path:
                with self.subTest(url=url):
                    self.assertIn(fragment, ids)

    def test_ids_are_unique(self):
        self.assertEqual(len(self.parser.ids), len(set(self.parser.ids)))

    def test_images_have_alt_text(self):
        for attrs in self.parser.images:
            with self.subTest(src=attrs.get("src")):
                self.assertIn("alt", attrs)


if __name__ == "__main__":
    unittest.main()
