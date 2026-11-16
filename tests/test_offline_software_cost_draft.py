"""Guardrails for the offline, non-published software cost calculator draft."""
from html.parser import HTMLParser
from pathlib import Path
import unittest


FILE = (
    Path(__file__).resolve().parents[1]
    / "products/drafts/2026-11-01-calcolatore-offline-costo-software.html"
)


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.labels = set()
        self.inputs = set()
        self.external_scripts = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "label" and attributes.get("for"):
            self.labels.add(attributes["for"])
        if tag == "input" and attributes.get("id"):
            self.inputs.add(attributes["id"])
        if tag == "script" and attributes.get("src"):
            self.external_scripts.append(attributes["src"])


class OfflineCalculatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = FILE.read_text(encoding="utf-8")
        cls.parsed = FormParser()
        cls.parsed.feed(cls.source)

    def test_every_input_has_label(self):
        self.assertTrue(self.parsed.inputs)
        self.assertEqual(self.parsed.inputs - self.parsed.labels, set())

    def test_offline_no_external_script_or_tracking(self):
        self.assertEqual(self.parsed.external_scripts, [])
        self.assertNotRegex(
            self.source,
            r"https?://|fetch|XMLHttpRequest|localStorage|sessionStorage|utm_|affid=|<iframe",
        )

    def test_draft_has_noindex_and_accessible_results(self):
        self.assertIn('content="noindex,nofollow"', self.source)
        self.assertIn('aria-live="polite"', self.source)
        self.assertIn('event.preventDefault()', self.source)

    def test_renewal_costs_only_after_first_year(self):
        self.assertIn("renew * (years - 1)", self.source)
        # Independent arithmetic reference scenarios, not a browser execution test.
        self.assertAlmostEqual(24.90 + 2 * 59.90, 144.70)
        self.assertAlmostEqual(39.90 + 5 + 3 * 10, 74.90)


if __name__ == "__main__":
    unittest.main()
