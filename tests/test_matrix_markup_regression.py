"""Regression checks for forbidden active/commercial markup in the unpublished matrix.

Run: python -m unittest discover -s tests -p 'test_matrix_markup_regression.py'
Static checks are not a substitute for browser, security or accessibility testing.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import unittest

PAGE = Path(__file__).resolve().parents[1] / "preview/vorli-next/matrice-scelta-tech-lab.html"
FORBIDDEN = {"script", "iframe", "form", "object", "embed", "base"}
COMMERCIAL_HOSTS = ("awin1.com", "awin.com")
COMMERCIAL_TERMS = ("checkout", "add-to-cart", "add_to_cart")


class MarkupAudit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.forbidden = []
        self.commercial = []

    def handle_starttag(self, tag, attrs):
        self._check(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        self._check(tag, attrs)

    def _check(self, tag, attrs):
        if tag in FORBIDDEN:
            self.forbidden.append(tag)
        attributes = dict(attrs)
        for key in ("href", "src", "action", "formaction"):
            value = attributes.get(key, "")
            if not value:
                continue
            parsed = urlsplit(value.strip())
            host = (parsed.hostname or "").lower()
            if (parsed.scheme not in ("",) or parsed.netloc or
                any(host == domain or host.endswith("." + domain) for domain in COMMERCIAL_HOSTS) or
                any(term in value.lower() for term in COMMERCIAL_TERMS)):
                self.commercial.append(value)


def audit(html):
    parser = MarkupAudit()
    parser.feed(html)
    return parser


class MatrixMarkupRegressionTests(unittest.TestCase):
    def test_actual_matrix_has_no_active_markup_or_external_commercial_links(self):
        result = audit(PAGE.read_text(encoding="utf-8"))
        self.assertEqual(result.forbidden, [])
        self.assertEqual(result.commercial, [])

    def test_forbidden_markup_regressions(self):
        for sample in (
            "<SCRIPT src='x.js'></SCRIPT>",
            "<form action='/pay'></form>",
            "<iframe src='demo'></iframe>",
            "<object data='x'></object>",
            "<embed src='x'/>",
            "<base href='https://example.org/'>",
            "< script src='x.js'></script>",  # invalid HTML is not parsed as a tag
        )[:-1]:
            with self.subTest(sample=sample):
                self.assertTrue(audit(sample).forbidden)

    def test_commercial_link_regressions(self):
        for sample in (
            '<a href="https://www.awin1.com/cread.php">Affiliate</a>',
            '<a href="//example.org/item">External</a>',
            '<a href="/checkout">Checkout</a>',
            '<a href="javascript:alert(1)">Unsafe</a>',
        ):
            with self.subTest(sample=sample):
                self.assertTrue(audit(sample).commercial)

    def test_safe_local_links_remain_allowed(self):
        result = audit('<a href="guida.html">Guida</a><a href="#main">Vai</a>')
        self.assertEqual(result.forbidden, [])
        self.assertEqual(result.commercial, [])


if __name__ == "__main__":
    unittest.main()
