import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
BUILD_FILE = REPO_ROOT / "agent" / "build.py"
VALIDATION_FILE = REPO_ROOT / "agent" / "offer_validation.py"


def verified_product(product_id, name, affiliate_url):
    return {
        "id": product_id,
        "name": name,
        "category": "Test",
        "price": 29.99,
        "commission_rate": 0.08,
        "merchant": "Venditore verificato",
        "affiliate_url": affiliate_url,
        "rating": None,
        "description": "Descrizione basata su fonte verificata.",
        "pros": [],
        "cons": [],
        "keywords": [],
        "verification": {
            "program": "Awin test",
            "approval_status": "approved",
            "source_url": "https://merchant.example.org/product",
            "source_checked_at": "2026-10-22",
            "price_checked_at": "2026-10-22",
            "commission_source_url": "https://network.example.org/commission",
            "commission_checked_at": "2026-10-22",
            "rating_source_url": "",
            "rating_checked_at": None,
            "checked_by": "revisione manuale",
            "notes": ""
        }
    }


class BuildPublicationGuardTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "agent").mkdir()
        (self.root / "data").mkdir()
        preview = self.root / "preview" / "vorli-next"
        preview.mkdir(parents=True)

        shutil.copy2(BUILD_FILE, self.root / "agent" / "build.py")
        shutil.copy2(VALIDATION_FILE, self.root / "agent" / "offer_validation.py")

        (self.root / "data" / "config.json").write_text(json.dumps({
            "site_name": "VORLI test",
            "affiliate_disclosure": "Disclosure affiliata di test."
        }), encoding="utf-8")

        demo = {
            "id": "demo-001",
            "name": "Prodotto demo",
            "category": "Test",
            "price": 49.90,
            "commission_rate": 0.04,
            "merchant": "INSERISCI NETWORK",
            "affiliate_url": "https://example.com/",
            "rating": 4.5,
            "description": "Scheda dimostrativa.",
            "pros": ["demo"],
            "cons": ["demo"],
            "keywords": ["demo"]
        }
        pending = verified_product(
            "pending-001", "Offerta in attesa",
            "https://track.example.org/pending"
        )
        pending["verification"]["approval_status"] = "pending"
        approved = verified_product(
            "approved-001", "Offerta approvata",
            "https://track.example.org/approved"
        )
        self.products = [demo, pending, approved]
        (self.root / "data" / "products.json").write_text(
            json.dumps(self.products), encoding="utf-8"
        )

        # Build's brand-lockup guard only checks for these required markers.
        (preview / "index.html").write_text(
            '<div class="brand-mark">vorli-gradient SMART E-COMMERCE '
            'FOR A BETTER TOMORROW</div>', encoding="utf-8"
        )
        (preview / "style.css").write_text("body { font-family: sans-serif; }", encoding="utf-8")
        for page in ("risorse.html", "guida.html", "usb-c.html"):
            (preview / page).write_text("<!doctype html><html lang='it'></html>", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def build(self):
        return subprocess.run(
            [sys.executable, str(self.root / "agent" / "build.py")],
            cwd=self.root, capture_output=True, text=True, check=False
        )

    def test_unapproved_offer_has_no_active_affiliate_button(self):
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        catalog = (self.root / "site" / "catalogo.html").read_text(encoding="utf-8")
        self.assertIn("Offerta in attesa", catalog)
        self.assertIn("Offerta non disponibile", catalog)
        self.assertNotIn('href="https://track.example.org/pending"', catalog)
        self.assertIn('href="https://track.example.org/approved"', catalog)

    def test_demo_remains_flagged_and_never_links_to_example_com(self):
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        catalog = (self.root / "site" / "catalogo.html").read_text(encoding="utf-8")
        self.assertIn("Scheda dimostrativa", catalog)
        self.assertNotIn('href="https://example.com/', catalog)

    def test_unverified_commission_blocks_publication(self):
        product = verified_product(
            "no-commission-source", "Commissione senza fonte",
            "https://track.example.org/no-commission-source"
        )
        product["verification"]["commission_source_url"] = ""
        (self.root / "data" / "products.json").write_text(
            json.dumps([product]), encoding="utf-8"
        )
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        catalog = (self.root / "site" / "catalogo.html").read_text(encoding="utf-8")
        self.assertNotIn('href="https://track.example.org/no-commission-source"', catalog)
        self.assertIn("Offerta non disponibile", catalog)

    def test_null_price_is_allowed_when_other_checks_pass(self):
        product = verified_product(
            "price-null", "Offerta senza prezzo pubblicato",
            "https://track.example.org/price-null"
        )
        product["price"] = None
        product["verification"]["price_checked_at"] = None
        (self.root / "data" / "products.json").write_text(
            json.dumps([product]), encoding="utf-8"
        )
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        catalog = (self.root / "site" / "catalogo.html").read_text(encoding="utf-8")
        self.assertIn('href="https://track.example.org/price-null"', catalog)
        self.assertNotIn("€ 29.99", catalog)


if __name__ == "__main__":
    unittest.main()
