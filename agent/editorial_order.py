"""Public-safe editorial catalogue helpers for VORLI.

No ranking by affiliate commission or commercial score.
"""
try:
    from .offer_policy import ready_for_publication
except ImportError:
    from offer_policy import ready_for_publication

PUBLIC_FIELDS = ("id", "name", "category", "description")


def editorial_order(products):
    """Preserve the reviewed input order, independent of commercial incentives."""
    return list(products)


def is_public_offer(product):
    """Use the single fail-closed offer policy, never a weaker duplicate gate."""
    return ready_for_publication(product)


def public_catalog(products):
    """Whitelisted public export; never emit tracking links or commission data."""
    return [
        {
            **{key: product[key] for key in PUBLIC_FIELDS if key in product},
            "status": "published" if is_public_offer(product) else "not_published",
        }
        for product in products
    ]
