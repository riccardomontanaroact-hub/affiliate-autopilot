#!/usr/bin/env python3
"""Browser QA for the local Power Station HTML draft. No external services required.
Run from repo root: python tests/test_power_station_browser.py
Requirements: pip install playwright; Chromium installed, or playwright install chromium.
Does not publish or alter production files.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "drafts" / "power-station-autonomia-offline-2026-10-13.html"
checks = []

def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS" if ok else "FAIL") + " " + name)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for width in (360, 768, 1280):
        page = browser.new_page(viewport={"width": width, "height": 800})
        errors, network = [], []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("request", lambda req: network.append(req.url) if req.url.startswith(("https://", "http://")) else None)
        page.set_content(SOURCE.read_text(encoding="utf-8"))
        check(f"{width}px no overflow", page.evaluate("document.documentElement.scrollWidth <= innerWidth"))
        check(f"{width}px no JS errors", not errors)
        check(f"{width}px no external requests", not network)
        if width == 360:
            page.locator('[name="capacity"]').fill("1000")
            page.locator('[name="watts"]').fill("100")
            page.locator('[name="usable"]').fill("80")
            page.locator('[name="maxoutput"]').fill("120")
            result = page.locator("#result").inner_text()
            check("10 hours theoretical", "10 ore" in result)
            check("8 hours adjusted", "8 ore" in result)
            check("below continuous limit", "sotto il limite" in result)
            page.locator('[name="watts"]').fill("150")
            check("over-limit warning", "superiore al limite" in page.locator("#result").inner_text())
            page.locator('[name="variable"]').check()
            check("variable load warning", "carico variabile" in page.locator("#result").inner_text())
            page.on("dialog", lambda dialog: dialog.accept())
            page.locator("#reset").click()
            check("reset", page.locator('[name="capacity"]').input_value() == "" and "Inserisci capacità" in page.locator("#result").inner_text())
            page.locator('[name="capacity"]').fill("1000")
            page.locator('[name="watts"]').fill("100")
            with TemporaryDirectory() as tmp:
                dest = Path(tmp) / "power-station.pdf"
                page.pdf(path=str(dest), format="A4", print_background=True)
                check("nonempty PDF", dest.stat().st_size > 5000)
        page.close()
    browser.close()

passed = sum(ok for _, ok in checks)
print(f"{passed}/{len(checks)} checks passed")
if passed != len(checks):
    raise SystemExit(1)
