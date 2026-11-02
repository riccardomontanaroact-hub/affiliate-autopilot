"""Keep account-specific affiliate tracking data out of public research JSON."""
import re
import unittest
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
TRACKING = re.compile(
    r"(?i)(?:awinmid\s*=|awinaffid\s*=|awin1\.com/cread\.php|"
    r"publisher[_-]?id|affiliate[_-]?id|clickref|subid)"
)


class PublicResearchPrivacyTests(unittest.TestCase):
    def test_public_data_json_contains_no_account_tracking_identifiers(self):
        files = sorted(DATA_DIR.glob("*.json"))
        self.assertTrue(files, "No public data JSON files found")
        for path in files:
            with self.subTest(file=path.name):
                raw = path.read_text(encoding="utf-8")
                self.assertIsNone(TRACKING.search(raw))
                self.assertNotIn("affiliate_homepage_link_already_tested", raw)


if __name__ == "__main__":
    unittest.main()
