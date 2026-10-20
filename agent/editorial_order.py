"""Public-safe editorial catalogue helpers for VORLI.

Reviewed 2026-10-20. No ranking by affiliate commission or commercial score.
"""

PUBLIC_FIELDS = ("id", "name", "category", "description")


def editorial_order(products):
    """Preserve the reviewed input order, independent of commercial incentives."""
    return list(products)


def is_public_offer(product):
    """Only explicitly reviewed HTTPS offers may produce an outbound link."""
    url = product.get("affiliate_url", "")
    merchant = product.get("merchant", "")
    return (
        product.get("approved_for_publication") is True
        and isinstance(url, str)
        and url.startswith("https://")
        and not url.startswith("https://example.com")
        and isinstance(merchant, str)
        and merchant.strip().upper() not in {"INSERISCI NETWORK", "DEMO"}
    )


def public_catalog(products):
    """Whitelisted public export; never emit tracking links or commission data."""
    return [
        {
            **{key: product[key] for key in PUBLIC_FIELDS if key in product},
            "status": "published" if is_public_offer(product) else "not_published",
        }
        for product in products
    ]
