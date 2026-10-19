# VORLI: affiliate offer publication gate

Date: 2026-10-19. Status: proposal only, not deployed.

Before rendering an outbound offer, require a manually confirmed active advertiser relationship, a dated review no older than 30 days, a non-demo merchant, and a valid HTTPS destination. If any condition fails, display a clearly marked unavailable/demo card with no outbound link and no estimated commission.

Do not infer approval from a promotional email or a welcome message without verifying current network status. This is a code-level safety gate, not independent network verification. Never commit tracking URLs, customer data, approval emails, or account identifiers.

Acceptance checks: missing status; expired or future verification; empty URL; example URL; non-HTTPS URL; URL containing credentials; valid-looking URL without approval; demo merchant. All must be non-clickable. Test a recently verified approved entry separately using a harmless synthetic URL, not a real tracking link.

Source: review of agent/build.py on main, 2026-10-19. Existing rendering uses a demo URL/merchant check, not an approval check.
