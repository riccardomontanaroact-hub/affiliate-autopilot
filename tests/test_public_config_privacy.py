"""Prevent personal identifiers in the public repository configuration.

This test intentionally checks patterns, not real addresses or publisher IDs.
Historical commits require a separate, carefully reviewed cleanup.
"""
import json
import re
import unittest
from pathlib import Path


CONFIG = Path(__file__).resolve().parents[1] / "data" / "config.json"
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

    def test_public_disclosure_is_preserved(self):
        config = json.loads(CONFIG.read_text(encoding="utf-8"))
        self.assertIn("affiliazione", config["affiliate_disclosure"].lower())


if __name__ == "__main__":
    unittest.main()
