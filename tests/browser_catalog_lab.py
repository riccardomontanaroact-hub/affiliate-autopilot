#!/usr/bin/env python3
"""Manual Chromium smoke test for the *real* VORLI Lab files, not a reduced fixture.

Optional dependency: pip install playwright
Browser: CHROMIUM_PATH=/usr/bin/chromium python tests/browser_catalog_lab.py
No network, payments, production deploy or new accounts are required.
This script is intentionally not part of the default CI until its browser
dependency and execution budget have been explicitly reviewed.
"""
from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

LAB = Path(__file__).resolve().parents[1] / "preview" / "vorli-next"
PAGE = (LAB / "catalogo-lab.html").as_uri()
WIDTHS = (360, 768, 1440)


def count_visible(page, kind):
    return page.locator(f"#{kind}-cards article:visible").count()


def verify_viewport(browser, width):
    context = browser.new_context(viewport={"width": width, "height": 800})
    page = context.new_page()
    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    page.goto(PAGE, wait_until="load")
    assert page.title().startswith("Catalogo tech"), (width, page.title())
    assert count_visible(page, "category") == 8, (width, "categories missing")
    assert count_visible(page, "resource") == 5, (width, "drafts missing")
    assert page.locator(".filters").is_visible(), (width, "JS filters unavailable")
    overflow = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
    assert overflow <= 1, (width, f"horizontal overflow: {overflow}px")
    assert not errors, (width, errors)

    page.locator("#catalog-search").fill("energia")
    assert count_visible(page, "category") == 2, (width, "search category count")
    assert count_visible(page, "resource") == 1, (width, "search draft count")
    page.locator("#reset-filters").click()
    assert count_visible(page, "category") == 8
    assert count_visible(page, "resource") == 5
    page.locator("#category-filter").select_option("sport-tech")
    assert count_visible(page, "category") == 1
    assert count_visible(page, "resource") == 0
    page.locator("#reset-filters").click()
    page.locator("#catalog-search").fill("parola-che-non-esiste")
    assert page.locator("#empty-results").is_visible()
    page.locator("#empty-reset").click()
    assert count_visible(page, "category") == 8
    assert count_visible(page, "resource") == 5
    context.close()

    no_js = browser.new_context(viewport={"width": width, "height": 800}, java_script_enabled=False)
    static = no_js.new_page()
    static.goto(PAGE, wait_until="load")
    assert count_visible(static, "category") == 8, (width, "no-JS categories")
    assert count_visible(static, "resource") == 5, (width, "no-JS drafts")
    assert not static.locator(".filters").is_visible(), (width, "hidden filters exposed")
    assert static.locator('a[href="catalogo-statico-lab.html"]').count() > 0
    assert static.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth") <= 1
    no_js.close()


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise SystemExit("Playwright not installed: pip install playwright") from exc

    chromium = os.environ.get("CHROMIUM_PATH") or shutil.which("chromium") or shutil.which("chromium-browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, **({"executable_path": chromium} if chromium else {}))
        try:
            for width in WIDTHS:
                verify_viewport(browser, width)
                print(f"PASS: {width}px, JS on/off, no overflow, filters and search")
        finally:
            browser.close()
    print("PASS: full VORLI Lab browser smoke test (not a WCAG audit)")


if __name__ == "__main__":
    main()
