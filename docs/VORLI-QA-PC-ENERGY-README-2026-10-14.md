# VORLI Lab — PC energy estimator QA (14 October 2026)

**Draft only. No merge, deploy, payments, sales, affiliate links or user data.**

Source editorial document on branch `vorli/research-pc-energy-eweki-20261014-2014`: `docs/VORLI-LAB-COSTO-PC-EWEKI-RICERCA-2026-10-14.md`.

Offline Python calculator and tests in `tools/pc_energy_estimator.py` and `tests/test_pc_energy_estimator.py`. Input: average watts measured at wall, hours active and standby per day (non-overlapping), days per year, electricity EUR/kWh, purchase cost and maintenance over 3 years. Annual kWh = watts × hours × days / 1000, summed for active and standby. Three-year cost = purchase + 3 × annual electricity cost + maintenance. Assumes constant electricity price and usage; not a guarantee of savings. Excludes peripherals not included in measured watts, usage on excluded days, future changes.

Run tests: `python3 -m unittest discover -s tests -p 'test_pc_energy_estimator.py' -v`. Local result 14/10/2026: **9/9 passed**. Smartphone interface and accessibility review still pending. Do not merge or publish without review.