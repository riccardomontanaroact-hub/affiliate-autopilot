"""Offline HTML attribute safety regression for the unpublished VORLI matrix.

Run: python -m unittest discover -s tests -p 'test_matrix_attribute_safety.py' -v
This is a static gate, not a browser or comprehensive security audit.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import unittest

PAGE = Path(__file__).resolve().parents[1] / "preview/vorli-next/matrice-scelta-tech-lab.html"
URL_ATTRS = {"href", "src", "action", "formaction", "poster", "data", "srcset"}
DANGEROUS_SCHEMES = {"javascript", "vbscript", "data", "file"}


class AttributeAudit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.findings = []

    def handle_starttag(self, tag, attrs):
        self.check(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        self.check(tag, attrs)

    def check(self, tag, attrs):
        for name, value in attrs:
            name = name.lower()
            value = value or ""
            if name.startswith("on"):
                self.findings.append((tag, name, "event handler"))
            if name == "style" and re.search(r"@import|url\s*\(|expression\s*\(", value, re.I):
                self.findings.append((tag, name, "dynamic CSS"))
            if name in URL_ATTRS:
                # This unpublished editorial page only needs relative local resources.
                # Reject absolute paths, protocol-relative URLs, remote URLs and
                # dangerous schemes even if HTML entities or percent encoding are used.
                decoded = unquote(value).strip().replace("\\", "/")
                parsed = urlsplit(decoded)
                if (parsed.scheme or parsed.netloc or decoded.startswith(("/", "\\")) or
                    re.search(r"[\x00-\x1f]", decoded)):
                    self.findings.append((tag, name, "nonlocal/unsafe URL"))
                if name == "srcset" and ("," in decoded or any(c.isspace() for c in decoded)):
                    self.findings.append((tag, name, "srcset needs explicit review"))


def audit(markup):
    parser = AttributeAudit()
    parser.feed(markup)
    return parser.findings


class MatrixAttributeSafetyTests(unittest.TestCase):
    def test_actual_matrix_has_no_unsafe_attributes(self):
        self.assertEqual(audit(PAGE.read_text(encoding="utf-8")), [])

    def test_event_handler_and_dynamic_style_fixtures(self):
        for sample in (
            '<a onclick="alert(1)" href="guida.html">test</a>',
            '<img onerror="alert(1)" src="image.svg">',
            '<div style="background:url(https://example.org/pixel)">test</div>',
            '<div style="@import url(remote.css)">test</div>',
        ):
            with self.subTest(sample=sample):
                self.assertTrue(audit(sample))

    def test_unsafe_url_fixtures(self):
        for sample in (
            '<a href="javascript:alert(1)">bad</a>',
            '<a href="&#106;avascript:alert(1)">bad</a>',
            '<a href="%6aavascript:alert(1)">bad</a>',
            '<a href="//example.org">bad</a>',
            '<img src="/private.png">',
            '<img srcset="a.png 1x, b.png 2x">',
        ):
            with self.subTest(sample=sample):
                self.assertTrue(audit(sample))

    def test_local_links_remain_allowed(self):
        self.assertEqual(audit('<a href="guida.html">Guida</a><a href="#main">Salta</a>'), [])


if __name__ == "__main__":
    unittest.main()
