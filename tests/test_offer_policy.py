import unittest
from datetime import date
from agent.offer_policy import ready_for_publication, public_metadata


class TestOfferPolicy(unittest.TestCase):
    def test_default_denied(self):
        self.assertFalse(ready_for_publication({"name": "Draft"}))

    def test_stale_review_denied_independently_of_url(self):
        item = dict(
            merchant="Shop", publication_approved=True,
            affiliate_status="approved", approval_source="awin_dashboard",
            approval_verified_at="2025-01-01",
            affiliate_url="https://merchant.test/product",
        )
        self.assertFalse(ready_for_publication(item, date(2026, 10, 19)))

    def test_placeholder_host_denied_even_with_fresh_approval_metadata(self):
        item = dict(
            merchant="Shop", publication_approved=True,
            affiliate_status="approved", approval_source="awin_dashboard",
            approval_verified_at="2026-10-21",
            affiliate_url="https://example.org/product",
        )
        self.assertFalse(ready_for_publication(item, date(2026, 10, 21)))

    def test_public_export_is_allowlisted(self):
        item = {"name": "Test", "unknown_field": "Do not export"}
        self.assertEqual(public_metadata(item), {"name": "Test", "status": "unavailable"})


if __name__ == "__main__":
    unittest.main()
