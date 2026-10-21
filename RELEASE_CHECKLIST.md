# VORLI — Release readiness checklist

This checklist is intentionally conservative. Passing automated checks does not mean legal compliance, affiliate approval, or production publication.

## Automated preflight
Run from the repository root:

```bash
python agent/release_preflight.py
python -m unittest discover -s tests -v
python agent/build.py
```

The preflight is expected to exit with a non-zero status while any release blocker remains. This is deliberate.

## Required before any public commercial launch

- [x] Owner supplied for the draft: Riccardo Montanaro, natural person (still confirm the final legal presentation before launch).
- [x] Contact address supplied for the draft: vorli.notifications@gmail.com (monitoring and suitability should be confirmed before launch).
- [ ] Review and publish an appropriate privacy notice based on the actual data flows, hosting, providers, cookies, and tracking; obtain professional review where appropriate.
- [ ] Decide whether public pages should remain `noindex,nofollow`; after the owner explicitly approves the strategy, set `indexing_strategy_reviewed` to `true` in `data/config.json`. Keep it `false` until then.
- [ ] Manually verify GitHub Pages source branch/folder and the deployed URL. Only after checking the actual repository settings, set `github_pages_source_verified` to `true` in `data/config.json`; code tests cannot prove the hosting configuration or what a visitor currently sees.
- [ ] Remove the demo product from the public catalogue and add only real offers with evidence of current program approval, terms, price, stock, and destination URL.
- [ ] Verify every affiliate offer in the relevant network dashboard immediately before activation. A record in JSON is not proof of approval.
- [ ] Review affiliate disclosures, price/availability wording, accessibility, mobile layout, and all external destinations.
- [ ] Review the final generated site in a browser before changing visibility or publishing.

## What must not be guessed

The repository does not contain a verified legal owner/contact or a currently approved product offer. These must be supplied or verified from the actual owner/network account; automation must not fabricate them.

## Safe current state

Keep the change in its draft pull request. Do not merge, change GitHub Pages settings, enable indexing, activate affiliate URLs, or make commercial claims until the required items above are complete and explicitly approved.
