#!/usr/bin/env python3
"""Chromium smoke test for the actual unpublished VORLI catalog (not a fixture).

Run from any working directory:
    python -m pip install playwright
    python -m playwright install chromium
    python tests/browser_catalog_lab.py

Local files only; no network requests, payments, deployments or personal data.
Screenshots are QA evidence, not approved marketing mockups or a WCAG audit.
"""
from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

LAB = Path(__file__).resolve().parents[1] / "preview" / "vorli-next"
PAGE = (LAB / "catalogo-lab.html").as_uri()
EVIDENCE = Path(__file__).resolve().parents[1] / "artifacts" / "catalog-lab"
WIDTHS = (320, 360, 768, 1440)
RESOURCE_TITLES = (
    "Kit compatibilità USB-C",
    "Casa Smart Sicura",
    "Confronta Power Station",
    "Confronta Elettrodomestici",
    "Casa Smart — scheda compilabile",
)


def visible(page, kind):
    return page.locator(f"#{kind}-cards article:visible").count()


def check_no_overflow(page, width, mode):
    overflow = page.evaluate(
        "document.documentElement.scrollWidth - document.documentElement.clientWidth"
    )
    assert overflow <= 1, (width, mode, f"horizontal overflow: {overflow}px")


def check_local_navigation(page):
    # Every local link on the real page must point to a file or a valid anchor.
    for anchor in page.locator("a[href]").all():
        href = anchor.get_attribute("href") or ""
        if href.startswith(("https://", "http://", "mailto:")):
            continue
        path, _, fragment = href.partition("#")
        path = path.split("?", 1)[0]
        if path:
            assert (LAB / path).is_file(), f"Broken local link: {href}"
        if fragment and not path:
            assert page.locator(f'[id="{fragment}"]').count() == 1, (
                f"Missing anchor: {href}"
            )


def verify_viewport(browser, width):
    context = browser.new_context(viewport={"width": width, "height": 800})
    page = context.new_page()
    errors = []
    requests = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    page.on("request", lambda req: requests.append(req.url))
    page.goto(PAGE, wait_until="load")
    assert page.title().startswith("Catalogo tech"), (width, page.title())
    assert visible(page, "category") == 8, (width, "categories missing")
    assert visible(page, "resource") == 5, (width, "drafts missing")
    assert page.locator(".filters").is_visible(), (width, "filters unavailable")
    assert page.locator('meta[name="robots"]').get_attribute("content") == "noindex,nofollow"
    assert page.locator("a.skip").count() == 1
    assert page.locator('nav[aria-label="Navigazione principale"]').count() == 1
    assert page.locator('label[for="catalog-search"]').count() == 1
    assert page.locator('label[for="category-filter"]').count() == 1
    assert page.get_by_role("search", name="Ricerca e filtri del catalogo demo").count() == 1
    for control in ("#catalog-search", "#category-filter"):
        assert page.locator(control).get_attribute("aria-controls") == "category-cards resource-cards"
    # Accessible names must identify the draft, including when links are listed out of context.
    for title in RESOURCE_TITLES:
        link = page.get_by_role("link", name=re.compile(re.escape(title)))
        assert link.count() == 1, (width, "missing unique link name", title)
        accessible = link.aria_snapshot()
        assert "Consulta il sorgente su GitHub" in accessible, (width, accessible)
        assert "nuova scheda" in accessible, (width, accessible)
        assert link.get_attribute("target") == "_blank"
        assert "noopener" in (link.get_attribute("rel") or "")
    check_local_navigation(page)
    check_no_overflow(page, width, "JS")
    assert not errors, (width, errors)
    assert all(url.startswith("file:") for url in requests), (width, requests)

    # Check the keyboard skip link, then exercise actual interactive controls.
    page.keyboard.press("Tab")
    assert page.locator(".skip").evaluate(
        "el => document.activeElement === el"
    ), (width, "skip link not first keyboard focus")
    page.locator("#catalog-search").fill("energia")
    assert visible(page, "category") == 2, (width, "search categories")
    assert visible(page, "resource") == 1, (width, "search resources")
    page.locator("#reset-filters").click()
    assert visible(page, "category") == 8
    assert visible(page, "resource") == 5
    # Multi-word search must match terms across name, description and keywords.
    page.locator("#catalog-search").fill("casa smart")
    assert visible(page, "category") == 1, (width, "multi-word category search")
    assert visible(page, "resource") == 2, (width, "multi-word resource search")
    page.locator("#catalog-search").fill("smart    casa")
    assert visible(page, "category") == 1, (width, "search order / whitespace")
    assert visible(page, "resource") == 2, (width, "search order / whitespace")
    # Different separators must behave like spaces in real Chromium searches.
    page.locator("#catalog-search").fill("power-station")
    assert visible(page, "category") == 1, (width, "hyphenated power-station category")
    assert visible(page, "resource") == 1, (width, "hyphenated power-station resource")
    page.locator("#catalog-search").fill("USB/C")
    assert visible(page, "category") == 2, (width, "slash-separated USB/C categories")
    assert visible(page, "resource") == 1, (width, "slash-separated USB/C resource")
    page.locator("#catalog-search").fill("Wi‑Fi")
    assert visible(page, "category") == 1, (width, "nonbreaking-hyphen Wi-Fi category")
    assert visible(page, "resource") == 0, (width, "nonbreaking-hyphen Wi-Fi resources")
    page.locator("#reset-filters").click()
    page.locator("#category-filter").select_option("sport-tech")
    assert visible(page, "category") == 1
    assert visible(page, "resource") == 0
    page.locator("#reset-filters").click()
    page.locator("#catalog-search").fill("parola-che-non-esiste")
    assert page.locator("#empty-results").is_visible()
    # Feedback must appear beside filters, before the empty category grid,
    # rather than below the entire resources section off-screen.
    empty_box = page.locator("#empty-results").bounding_box()
    cards_box = page.locator("#category-cards").bounding_box()
    assert empty_box and cards_box and empty_box["y"] < cards_box["y"], (
        width, "no-results feedback is too far from search"
    )
    assert "0 categorie demo" in page.locator("#results-count").inner_text()
    if width == 360:
        page.screenshot(path=str(EVIDENCE / "catalog-360-empty-state.png"), full_page=True)
    page.locator("#empty-reset").click()
    assert page.locator("#catalog-search").evaluate("el => document.activeElement === el"), (
        width, "reset must restore keyboard focus to search"
    )
    assert visible(page, "category") == 8
    assert visible(page, "resource") == 5
    check_no_overflow(page, width, "JS after filters")
    page.screenshot(path=str(EVIDENCE / f"catalog-{width}-js.png"), full_page=True)
    context.close()

    no_js = browser.new_context(
        viewport={"width": width, "height": 800}, java_script_enabled=False
    )
    static = no_js.new_page()
    static.goto(PAGE, wait_until="load")
    assert visible(static, "category") == 8, (width, "no-JS categories")
    assert visible(static, "resource") == 5, (width, "no-JS resources")
    assert not static.locator(".filters").is_visible(), (width, "filters exposed without JS")
    assert static.locator('a[href="catalogo-statico-lab.html"]').count() > 0
    check_no_overflow(static, width, "no-JS")
    static.screenshot(path=str(EVIDENCE / f"catalog-{width}-no-js.png"), full_page=True)
    no_js.close()



def verify_accessibility_modes(browser, width):
    """Check forced-colors and reduced-motion modes on the full local page."""
    context = browser.new_context(
        viewport={"width": width, "height": 800},
        forced_colors="active",
        reduced_motion="reduce",
    )
    page = context.new_page()
    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    page.goto(PAGE, wait_until="load")
    assert page.evaluate("matchMedia('(forced-colors: active)').matches")
    assert page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches")
    assert visible(page, "category") == 8
    assert visible(page, "resource") == 5
    # Gradient-clipped headline text must not disappear in forced-colors mode.
    color = page.locator("h1 em").evaluate("el => getComputedStyle(el).color")
    assert color not in ("transparent", "rgba(0, 0, 0, 0)"), (width, color)
    transition = page.locator(".tile").first.evaluate(
        "el => getComputedStyle(el).transitionDuration"
    )
    assert transition == "0s", (width, "reduced-motion transition", transition)
    page.keyboard.press("Tab")
    skip = page.locator("a.skip")
    assert skip.evaluate("el => document.activeElement === el")
    outline = skip.evaluate("el => getComputedStyle(el).outlineStyle")
    assert outline != "none", (width, "keyboard focus invisible")
    check_no_overflow(page, width, "forced colors + reduced motion")
    assert not errors, (width, errors)
    page.screenshot(path=str(EVIDENCE / f"catalog-{width}-forced-colors.png"), full_page=True)
    context.close()



def verify_category_guide(browser, width):
    """Real browser smoke test of the original, unpublished eight-category guide."""
    context = browser.new_context(viewport={"width": width, "height": 800})
    page = context.new_page()
    errors, requests = [], []
    page.on("pageerror", lambda err: errors.append(str(err)))
    page.on("request", lambda req: requests.append(req.url))
    page.goto((LAB / "guida-scelta-tech-lab.html").as_uri(), wait_until="load")
    assert page.title().startswith("Guida alla scelta tecnologica")
    assert page.locator('meta[name="robots"]').get_attribute("content") == "noindex,nofollow"
    assert page.locator(".guide-grid .guide-card").count() == 8
    assert page.get_by_role("navigation", name="Indice delle otto checklist").count() == 1
    for category in (
        "computer", "software", "elettronica", "elettrodomestici-smart",
        "accessori-casa", "sport-tech", "benessere-tech", "energia-portatile",
    ):
        assert page.locator(f'#{category}').count() == 1
        assert page.locator(f'a[href="#{category}"]').count() == 1
        assert page.locator(f'#{category} li').count() == 3
    check_local_navigation(page)
    page.keyboard.press("Tab")
    assert page.locator("a.skip").evaluate("el => document.activeElement === el")
    page.locator('a[href="#energia-portatile"]').click()
    assert page.evaluate("location.hash") == "#energia-portatile"
    check_no_overflow(page, width, "guide")
    assert not errors, (width, errors)
    assert all(url.startswith("file:") for url in requests), (width, requests)
    if width in (360, 1440):
        page.screenshot(path=str(EVIDENCE / f"guide-{width}-editorial.png"), full_page=True)
    context.close()


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise SystemExit("Playwright missing: python -m pip install playwright") from exc

    EVIDENCE.mkdir(parents=True, exist_ok=True)
    chromium = os.environ.get("CHROMIUM_PATH") or shutil.which("chromium") or shutil.which("chromium-browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True, **({"executable_path": chromium} if chromium else {})
        )
        try:
            for width in WIDTHS:
                verify_viewport(browser, width)
                verify_category_guide(browser, width)
                print(f"PASS: {width}px, catalog + eight-topic guide, links, responsive, keyboard")
            for width in (360, 1440):
                verify_accessibility_modes(browser, width)
                print(f"PASS: {width}px, forced-colors, reduced motion, keyboard focus")
        finally:
            browser.close()
    print(f"PASS: actual VORLI Lab smoke test; screenshots in {EVIDENCE}")
    print("NOT VERIFIED: screen readers, WCAG 2.2 audit, real mobile hardware, legal review")


if __name__ == "__main__":
    main()
