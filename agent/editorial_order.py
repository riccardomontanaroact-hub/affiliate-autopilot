"""Editorial ordering guardrails for VORLI (not yet wired into the build)."""


def editorial_order(products):
    """Preserve the reviewed source order; never rank by affiliate incentives."""
    return list(products)
