"""Pre-publication checks for VORLI offers.

Metadata is supplied by an editor, not authenticated against Awin.
Never treat this module as a substitute for dashboard verification.
"""
from datetime import date, datetime, timezone
from urllib.parse import urlsplit


DEMO_MERCHANTS = {"INSERISCI NETWORK", "DEMO", "TEST", "PLACEHOLDER"}
PLACEHOLDER_HOSTS = {
    "example.com", "example.org", "example.net",
    "www.example.com", "www.example.org", "www.example.net",
}


def ready_for_publication(product: dict, today: date | None = None) -> bool:
    """Default deny unless a human explicitly reviewed an approved offer."""
    if product.get("publication_approved") is not True:
        return False
    if product.get("affiliate_status") != "approved":
        return False
    if product.get("approval_source") != "awin_dashboard":
        return False

    merchant = product.get("merchant")
    if not isinstance(merchant, str) or not merchant.strip():
        return False
    normalized_merchant = " ".join(merchant.upper().split())
    if (normalized_merchant in DEMO_MERCHANTS
            or any(marker in normalized_merchant
                   for marker in ("INSERISCI", "PLACEHOLDER", "DEMO"))):
        return False

    try:
        reviewed = date.fromisoformat(product["approval_verified_at"])
        days = ((today or datetime.now(timezone.utc).date()) - reviewed).days
        if not 0 <= days <= 30:
            return False
        url = product["affiliate_url"]
        if not isinstance(url, str):
            return False
        parsed = urlsplit(url)
        hostname = parsed.hostname.lower().rstrip(".") if parsed.hostname else ""
        confusing_placeholder_host = any(
            hostname.startswith(host + ".") for host in PLACEHOLDER_HOSTS
        )
        if (parsed.scheme != "https" or not hostname
                or parsed.username or parsed.password
                or hostname in PLACEHOLDER_HOSTS
                or confusing_placeholder_host):
            return False
    except (KeyError, TypeError, ValueError):
        return False
    return True


def public_metadata(product: dict) -> dict:
    """Allowlist safe editorial fields; omit merchant until offer is approved."""
    fields = ("id", "name", "category", "description", "rating")
    output = {key: product[key] for key in fields if key in product}
    approved = ready_for_publication(product)
    if approved and isinstance(product.get("merchant"), str):
        output["merchant"] = product["merchant"]
    output["status"] = "reviewed" if approved else "unavailable"
    return output
