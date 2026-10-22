"""Additional edge-case checks for VORLI's fail-closed affiliate policy."""
import unittest
from datetime import date

from agent.offer_policy import ready_for_publication


class TestOfferPolicyEdgeCases(unittest.TestCase):
    def candidate(self, **overrides):
        item = {
            "publication_approved": True,
            "affiliate_status": "approved",
            "approval_source": "awin_dashboard",
            "approval_verified_at": "2026-10-21",
            "merchant": "Real Merchant",
            "affiliate_url": "https://merchant.test/product",
        }
        item.update(overrides)
        return item

    def test_future_and_malformed_review_dates_are_denied(self):
        for reviewed_at in ("2026-10-22", "not-a-date", ""):
            with self.subTest(reviewed_at=reviewed_at):
                self.assertFalse(ready_for_publication(
                    self.candidate(approval_verified_at=reviewed_at),
                    date(2026, 10, 21),
                ))

    def test_review_older_than_thirty_days_is_denied(self):
        self.assertFalse(ready_for_publication(
            self.candidate(approval_verified_at="2026-09-20"),
            date(2026, 10, 21),
        ))

    def test_demo_merchant_variants_are_denied(self):
        for merchant in ("  demo  ", "Shop DEMO Outlet", "Placeholder Store", "INSERISCI Network"):
            with self.subTest(merchant=merchant):
                self.assertFalse(ready_for_publication(
                    self.candidate(merchant=merchant), date(2026, 10, 21)
                ))

    def test_placeholder_domain_suffix_is_not_confused_with_placeholder_host(self):
        # The policy blocks exact example hosts, not every hostname containing that text.
        self.assertTrue(ready_for_publication(
            self.candidate(affiliate_url="https://example.com.attacker.test/product"),
            date(2026, 10, 21),
        ))


if __name__ == "__main__":
    unittest.main()
