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
import shutil
from pathlib import Path

LAB = Path(__file__).resolve().parents[1] / "preview" / "vorli-next"
PAGE = (LAB / "catalogo-lab.html").as_uri()
EVIDENCE = Path(__file__).resolve().parents[1] / "artifacts" / "catalog-lab"
WIDTHS = (320, 360, 768, 1440)


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
    page.locator("#category-filter").select_option("sport-tech")
    assert visible(page, "category") == 1
    assert visible(page, "resource") == 0
    page.locator("#reset-filters").click()
    page.locator("#catalog-search").fill("parola-che-non-esiste")
    assert page.locator("#empty-results").is_visible()
    page.locator("#empty-reset").click()
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
                print(f"PASS: {width}px, JS on/off, filters, keyboard, links, no overflow")
        finally:
            browser.close()
    print(f"PASS: actual VORLI Lab smoke test; screenshots in {EVIDENCE}")
    print("NOT VERIFIED: screen readers, WCAG 2.2 audit, real mobile hardware, legal review")


if __name__ == "__main__":
    main()
