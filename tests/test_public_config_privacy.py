"""Prevent personal identifiers in the public repository configuration.

This test intentionally checks patterns, not real addresses or publisher IDs.
Historical commits require a separate, carefully reviewed cleanup.
"""
import json
import re
import unittest
from pathlib import Path


CONFIG = Path(__file__).resolve().parents[1] / "data" / "config.json"
SITE = Path(__file__).resolve().parents[1] / "site" / "index.html"
EMAIL = re.compile(r"(?i)\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b")
TRACKING_FIELD = re.compile(
    r"(?i)\b(?:awinaffid|publisher[_-]?id|affiliate[_-]?id|clickref|subid)\b"
)


class PublicConfigPrivacyTests(unittest.TestCase):
    def test_config_contains_no_personal_contact_or_owner(self):
        config = json.loads(CONFIG.read_text(encoding="utf-8"))
        self.assertNotIn("owner", config)
        self.assertNotIn("contact", config)
        self.assertNotIn("email", config)

    def test_config_contains_no_email_or_affiliate_tracking_id(self):
        raw = CONFIG.read_text(encoding="utf-8")
        self.assertIsNone(EMAIL.search(raw))
        self.assertIsNone(TRACKING_FIELD.search(raw))

    def test_public_site_has_no_email_or_links_to_unreleased_drafts(self):
        raw = SITE.read_text(encoding="utf-8")
        self.assertIsNone(EMAIL.search(raw))
        self.assertNotIn("mailto:", raw.lower())
        self.assertNotIn("github.com/", raw.lower())
        self.assertIn("In revisione", raw)

    def test_all_site_and_preview_html_pages_have_no_email(self):
        """Check public HTML and review previews before merging to main."""
        preview = SITE.parents[1] / "preview" / "vorli-next"
        for root in (SITE.parent, preview):
            self.assertTrue(root.is_dir(), f"Missing public HTML directory: {root}")
            html_files = sorted(root.rglob("*.html"))
            self.assertTrue(html_files, f"No HTML files found in {root}")
            for path in html_files:
                with self.subTest(file=str(path.relative_to(SITE.parents[1]))):
                    raw = path.read_text(encoding="utf-8")
                    self.assertIsNone(EMAIL.search(raw))
                    self.assertIsNone(TRACKING_FIELD.search(raw))
                    self.assertNotIn("mailto:", raw.lower())
                    self.assertNotIn("awin1.com/cread.php", raw.lower())

    def test_public_scripts_and_styles_have_no_personal_tracking(self):
        """Prevent identifiers or tracked links in assets shipped with public pages."""
        preview = SITE.parents[1] / "preview" / "vorli-next"
        for root in (SITE.parent, preview):
            for pattern in ("*.js", "*.css", "*.svg"):
                for path in sorted(root.rglob(pattern)):
                    with self.subTest(file=str(path.relative_to(SITE.parents[1]))):
                        raw = path.read_text(encoding="utf-8")
                        self.assertIsNone(EMAIL.search(raw))
                        self.assertIsNone(TRACKING_FIELD.search(raw))
                        self.assertNotIn("awin1.com/cread.php", raw.lower())


    def test_public_disclosure_is_preserved(self):
        config = json.loads(CONFIG.read_text(encoding="utf-8"))
        self.assertIn("affiliazione", config["affiliate_disclosure"].lower())


    def test_public_research_data_has_no_tracking_identifiers(self):
        """Public data files must not include publisher identifiers or tracked URLs."""
        data_dir = CONFIG.parent
        for path in sorted(data_dir.glob("*.json")):
            with self.subTest(file=path.name):
                raw = path.read_text(encoding="utf-8")
                self.assertIsNone(EMAIL.search(raw))
                self.assertIsNone(TRACKING_FIELD.search(raw))
                self.assertNotIn("awin1.com/cread.php", raw.lower())
                self.assertNotIn("membership-invitation/accept", raw.lower())
                self.assertNotIn("affiliate_homepage_link_already_tested", raw)


if __name__ == "__main__":
    unittest.main()
