"""Fail-closed publication policy for affiliate offers.

This is a technical gate, not independent verification of advertiser approval.
Only an operator who checked the network dashboard may set approval_status
and approval_verified_on. Never store approval emails or tracking credentials.
"""
from datetime import date
from ipaddress import ip_address
from urllib.parse import urlsplit

DEMO_MERCHANTS = {"INSERISCI NETWORK", "DEMO"}


def is_approved_offer(product):
    if product.get("approval_status") != "approved":
        return False
    checked_on = product.get("approval_verified_on")
    if not isinstance(checked_on, str):
        return False
    try:
        checked_date = date.fromisoformat(checked_on)
    except ValueError:
        return False
    if checked_date > date.today():
        return False
    merchant = str(product.get("merchant") or "").strip()
    if not merchant or merchant.upper() in DEMO_MERCHANTS:
        return False
    url = product.get("affiliate_url")
    if not isinstance(url, str) or not url or any(ch.isspace() for ch in url):
        return False
    try:
        parsed = urlsplit(url)
        host = parsed.hostname
        if parsed.scheme != "https" or not host or parsed.username or parsed.password:
            return False
        if parsed.port not in (None, 443):
            return False
        if host in {"localhost", "example.com"} or host.endswith(".example.com"):
            return False
        if "." not in host:
            return False
        try:
            ip_address(host)
            return False
        except ValueError:
            pass
        return True
    except ValueError:
        return False
