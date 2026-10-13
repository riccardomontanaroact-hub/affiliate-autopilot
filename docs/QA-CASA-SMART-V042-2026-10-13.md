# VORLI Casa Smart v0.4.2 — QA (2026-10-13)

The draft calculator adds optional annual electricity use (kWh/year) and electricity price (EUR/kWh) to the 36-month estimate.

Formula: purchase + accessories + 36 * monthly subscription + 3 * annual subscription + 3 * kWh/year * EUR/kWh.

Both energy inputs are required to include energy; otherwise a validation message appears. Empty optional non-energy inputs count as zero.

Nine tests were executed against the saved inline JavaScript using a simulated DOM, all passed: empty purchase price; purchase price only; incomplete energy input in both directions; complete energy inputs; annual subscription; valid zero; negative input; nonnumeric input. No real browser, device, or print tests were performed on this version.

Editorial status: DRAFT, not approved for sale or publication. The HTML includes noindex and a visible draft notice.

Research checked on 2026-10-13:
- eWeki IT, Awin advertiser 19988: consumer electronics, 30-day cookie. Approval and personal commission rate unverified. https://ui.awin.com/merchant-profile/19988
- AliExpress IT, Awin advertiser 12251: published range 2.3%-6.9%, 3-day cookie; individual eligibility and rates unverified. https://ui.awin.com/merchant-profile/12251
- EU energy labels may state consumption per 100 cycles, not per year: https://commission.europa.eu/news-and-media/news/focus-improved-eu-energy-label-paving-way-more-innovative-and-energy-efficient-products-2021-02-16_it

Organic SEO plan: explain total smart-device cost, difference between watts and annual kWh, and how to compare hub and subscription requirements. No spam or affiliate links without approval.

Next: browser and mobile QA; verify affiliate dashboard statuses and legal/tax obligations before commercial launch.
