# VORLI catalog publication gate — integration review (2026-10-20)

Status: **NOT DEPLOYED**. Review only. No advertiser approvals are inferred from this document.

## Confirmed gap
The generator at `agent/build.py` does not import or call `agent/offer_policy.py`. The generated `data/ranked_products.json` serializes complete product records rather than a public allowlist. The catalog renders an outbound link whenever a record is not classified as a demo. This is insufficient evidence of advertiser approval.

## Safe implementation criteria
1. Use `ready_for_publication` for a default-deny editorial gate. Dashboard evidence must still be verified outside the repository.
2. Export only `public_metadata` to publicly tracked JSON. Do not export tracking parameters, account identifiers, private approval evidence or internal commission figures.
3. Do not place outbound tracking URLs in generated repository artifacts. Keep links disabled until a separate reviewed publishing mechanism exists.
4. Add tests for unknown fields, missing approval, expired review, demo records and sensitive-field exclusion.
5. Validate the generated HTML and JSON locally before proposing a merge.

## Limits
The current policy uses editor-supplied flags and does not query the affiliate network. It must not be presented as proof of live commercial authorization. No changes to the production branch are authorized.

Source: repository code on `main` and the two unmerged files in `vorli/offer-data-safety-20261019-2313`, inspected 2026-10-20.
