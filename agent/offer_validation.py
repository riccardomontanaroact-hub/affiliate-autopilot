"""Validation rules shared by the VORLI build and repository audit."""
import math
from datetime import date, datetime
from urllib.parse import urlparse

DEMO_MERCHANTS = {"INSERISCI NETWORK", "DEMO"}


def _https_url(value):
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        parsed = urlparse(value.strip())
        host = (parsed.hostname or "").lower()
        return (
            parsed.scheme.lower() == "https"
            and bool(host)
            and host != "example.com"
            and not host.endswith(".example.com")
        )
    except ValueError:
        return False


def _valid_date(value):
    if not isinstance(value, str) or not value.strip():
        return False
    value = value.strip()
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        try:
            date.fromisoformat(value)
            return True
        except ValueError:
            return False


def is_demo(product):
    if not isinstance(product, dict):
        return True
    merchant = str(product.get("merchant", "")).strip().upper()
    url = product.get("affiliate_url", "")
    try:
        host = (urlparse(url).hostname or "").lower() if isinstance(url, str) else ""
    except ValueError:
        host = ""
    return (
        merchant in DEMO_MERCHANTS
        or host == "example.com"
        or host.endswith(".example.com")
    )


def is_publishable(product):
    """Return True only when an offer has explicit approval and auditable sources."""
    if not isinstance(product, dict) or is_demo(product):
        return False

    if not _https_url(product.get("affiliate_url")):
        return False
    if not str(product.get("merchant", "")).strip():
        return False

    verification = product.get("verification")
    verification = verification if isinstance(verification, dict) else {}
    approval = verification.get("approval_status", product.get("approval_status"))
    program = verification.get("program") or product.get("network") or product.get("program")
    if str(approval or "").strip().lower() != "approved" or not str(program or "").strip():
        return False
    if not _https_url(verification.get("source_url")):
        return False
    if not _valid_date(verification.get("source_checked_at")):
        return False
    if not str(verification.get("checked_by", "")).strip():
        return False

    commission = product.get("commission_rate")
    if isinstance(commission, bool) or not isinstance(commission, (int, float)):
        return False
    if not math.isfinite(commission) or not 0 <= commission <= 1:
        return False
    if not _https_url(verification.get("commission_source_url")):
        return False
    if not _valid_date(verification.get("commission_checked_at")):
        return False

    price = product.get("price")
    if price is not None:
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            return False
        if not math.isfinite(price) or price < 0:
            return False
        if not _valid_date(verification.get("price_checked_at")):
            return False

    rating = product.get("rating")
    if rating is not None:
        if isinstance(rating, bool) or not isinstance(rating, (int, float)):
            return False
        if not math.isfinite(rating) or not 0 <= rating <= 5:
            return False
        if not _https_url(verification.get("rating_source_url")):
            return False
        if not _valid_date(verification.get("rating_checked_at")):
            return False

    return True
