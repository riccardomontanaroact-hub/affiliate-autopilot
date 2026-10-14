# VORLI Lab — PC energy calculator QA (14 October 2026)

**Draft only. No merge, deploy, payments, sales or affiliate links.**

The calculator source and tests are **not in this branch**. They were tested locally but their upload was blocked. This branch contains only this release note.

Local Python regression result: **9/9 passed** on 14/10/2026.
Local mobile HTML JavaScript regression result: **10/10 passed** on 14/10/2026.
The prototype is offline, responsive, and untested manually on physical devices.

Source editorial workbook remains on branch `vorli/research-pc-energy-eweki-20261014-2014`, file `docs/VORLI-LAB-COSTO-PC-EWEKI-RICERCA-2026-10-14.md`.

Method: use average measured power at the wall, not PSU rated power. Annual kWh = active watts × active hours × days / 1000 + standby watts × standby hours × days / 1000. Hours cannot overlap. Three-year estimated cost = purchase + 3 × annual kWh × EUR/kWh + three-year maintenance. Assumes constant usage and tariff; excludes other unmeasured costs.

Next: upload source after connector permission is restored, review accessibility and mobile layout, review legal/tax/advertiser status, and request approval before any merge or public release.