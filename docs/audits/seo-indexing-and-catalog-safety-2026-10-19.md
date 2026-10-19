# VORLI — SEO readiness audit (19 October 2026)

Status: internal draft; source-code review only; no publication authorized.

## Findings on main
- `site/index.html`, `site/guida.html`, `site/risorse.html` and `site/usb-c.html` contain `noindex,nofollow`. Organic discovery of these pages is deliberately disabled for crawlers respecting the directive.
- `site/catalogo.html` and `site/dashboard.html` have no explicit robots meta directive. Both show demonstration content. This does not establish actual search indexing.
- `agent/build.py` rewrites several `site/` pages from `preview/vorli-next/` and generates catalog and dashboard. Permanent fixes belong in the source or generator, not only in generated HTML.
- Catalog generation classifies a product as non-demo from its URL and merchant placeholder alone; it does not explicitly check verified program eligibility before producing an offer link.
- The product scoring formula uses commission and rating inputs without provenance validation. Do not present demonstration data as real product reviews or commercial performance.
- None of seven inspected HTML pages has a canonical tag. Confirm production URL structure before deciding whether canonical annotations are necessary.

## Proposed release gates
1. Keep preview pages unindexed. Review the catalog and dashboard robots policy.
2. Before enabling commercial offers, require confirmed advertiser eligibility, checked terms, valid non-personalized destination, verified product facts, and clear per-link affiliate disclosure.
3. Add build tests for demo indexing, unverified offers, and unverifiable ratings or prices.
4. Only after privacy and compliance review, approve useful original pages for indexing and create internal links and a sitemap with eligible URLs.
5. Do not modify production or enable payments as part of this audit.

## Sources checked 2026-10-19
- Repository main: `site/*.html`, `data/products.json`, `agent/build.py`.
- Google robots directives: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
- Google canonical guidance: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls?hl=it

Limitations: no live HTTP-header inspection, no Search Console access, no evidence of actual indexing.
