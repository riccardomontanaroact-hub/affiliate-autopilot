"""Fail-closed checks for VORLI commerce readiness. No credentials or payment processing."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
config = json.loads((ROOT / "data/commerce.json").read_text(encoding="utf-8"))
products = json.loads((ROOT / "data/products.json").read_text(encoding="utf-8"))
errors = []
if config.get("checkout_enabled") or config.get("checkout_mode") != "disabled":
    errors.append("Direct checkout must remain disabled pending provider, legal and seller verification.")
if not config.get("legal_review_required") or not config.get("verified_supplier_required"):
    errors.append("Commercial safety gates cannot be disabled.")
for item in products:
    url = item.get("affiliate_url", "")
    if item.get("id", "").startswith("demo-") or "example.com" in url:
        print(f"DEMO ONLY: {item.get('id', 'unknown')} must not be presented as a purchasable offer.")
    elif not url.startswith("https://"):
        errors.append(f"Invalid HTTPS affiliate URL for {item.get('id', 'unknown')}")
if errors:
    raise SystemExit("\n".join(errors))
print("Commerce configuration validated; checkout is disabled.")
