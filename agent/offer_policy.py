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
    if merchant.strip().upper() in DEMO_MERCHANTS:
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
        if (parsed.scheme != "https" or not parsed.hostname
                or parsed.username or parsed.password
                or parsed.hostname.lower() in PLACEHOLDER_HOSTS):
            return False
    except (KeyError, TypeError, ValueError):
        return False
    return True


def public_metadata(product: dict) -> dict:
    """Allowlist safe editorial fields; omit tracking URLs and account details."""
    fields = ("id", "name", "category", "merchant", "description", "rating")
    output = {key: product[key] for key in fields if key in product}
    output["status"] = (
        "reviewed" if ready_for_publication(product) else "unavailable"
    )
    return output
