import unittest
from datetime import date
from agent.offer_policy import ready_for_publication, public_metadata
from agent.editorial_order import public_catalog


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

    def test_demo_merchant_variants_are_rejected(self):
        for merchant in ("Demo Merchant", "INSERISCI NETWORK  ", "Shop Placeholder"):
            with self.subTest(merchant=merchant):
                item = dict(
                    publication_approved=True,
                    affiliate_status="approved",
                    approval_source="awin_dashboard",
                    approval_verified_at="2026-10-21",
                    merchant=merchant,
                    affiliate_url="https://merchant.test/product",
                )
                self.assertFalse(ready_for_publication(item, date(2026, 10, 21)))

    def test_http_affiliate_url_is_rejected(self):
        item = dict(
            publication_approved=True,
            affiliate_status="approved",
            approval_source="awin_dashboard",
            approval_verified_at="2026-10-21",
            merchant="Real Merchant",
            affiliate_url="http://merchant.test/product",
        )
        self.assertFalse(ready_for_publication(item, date(2026, 10, 21)))

    def test_url_with_embedded_credentials_is_rejected(self):
        item = dict(
            publication_approved=True,
            affiliate_status="approved",
            approval_source="awin_dashboard",
            approval_verified_at="2026-10-21",
            merchant="Real Merchant",
            affiliate_url="https://user:password@merchant.test/product",
        )
        self.assertFalse(ready_for_publication(item, date(2026, 10, 21)))

    def test_public_export_is_allowlisted(self):
        item = {"name": "Test", "unknown_field": "Do not export"}
        self.assertEqual(public_metadata(item), {"name": "Test", "status": "unavailable"})

    def test_public_catalog_is_allowlisted_and_keeps_order(self):
        products = [
            {
                "id": "first",
                "name": "First",
                "category": "Tech",
                "description": "Public description",
                "merchant": "Private merchant metadata",
                "affiliate_url": "https://tracking.example/secret",
                "commission_rate": 0.20,
            },
            {
                "id": "second",
                "name": "Second",
                "category": "Casa",
                "description": "Second description",
                "score": 999,
            },
        ]
        self.assertEqual(
            public_catalog(products),
            [
                {
                    "id": "first",
                    "name": "First",
                    "category": "Tech",
                    "description": "Public description",
                    "status": "not_published",
                },
                {
                    "id": "second",
                    "name": "Second",
                    "category": "Casa",
                    "description": "Second description",
                    "status": "not_published",
                },
            ],
        )

    def test_public_export_includes_merchant_only_after_approval(self):
        item = {
            "id": "approved-1",
            "name": "Approved item",
            "category": "Tech",
            "description": "Reviewed offer",
            "rating": 4.8,
            "merchant": "Real Merchant",
            "publication_approved": True,
            "affiliate_status": "approved",
            "approval_source": "awin_dashboard",
            "approval_verified_at": "2026-10-21",
            "affiliate_url": "https://merchant.test/product",
        }
        result = public_metadata(item)
        self.assertEqual(result["merchant"], "Real Merchant")
        self.assertEqual(result["status"], "reviewed")

    def test_public_export_excludes_commercial_and_tracking_fields(self):
        item = {
            "id": "product-1",
            "name": "Test",
            "category": "Tech",
            "merchant": "Merchant",
            "description": "Public description",
            "rating": 4.5,
            "price": 99.90,
            "commission_rate": 0.10,
            "affiliate_url": "https://tracking.example/secret",
            "score": 999,
            "private_account_id": "private",
        }
        result = public_metadata(item)
        self.assertEqual(
            set(result),
            {"id", "name", "category", "description", "rating", "status"},
        )
        self.assertNotIn("merchant", result)
        self.assertNotIn("price", result)
        self.assertNotIn("commission_rate", result)
        self.assertNotIn("affiliate_url", result)
        self.assertNotIn("score", result)
        self.assertNotIn("private_account_id", result)


if __name__ == "__main__":
    unittest.main()
