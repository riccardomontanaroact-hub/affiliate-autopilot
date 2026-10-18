#!/usr/bin/env python3
"""Offline smoke test for VORLI's A4 blackout workbook.

Prerequisites: Chrome/Chromium, pdfinfo and pdftotext (Poppler).
No network calls, external accounts, payments, or production deployment.
Usage: python3 tools/qa_printable_blackout.py
Exit code 0 = structural print checks pass; manual visual QA still required.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "docs/drafts/printables/passaporto-blackout-tecnologico-A4-2026-10-18.html"
HEADINGS = (
    "Passaporto blackout tecnologico",
    "Quanta energia serve davvero?",
    "Compatibilità della batteria",
    "Test e manutenzione",
)


def require_binary(*names: str) -> str:
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    raise RuntimeError("Missing executable: " + " / ".join(names))


def run(*args: str) -> str:
    p = subprocess.run(args, capture_output=True, text=True, check=False, timeout=90)
    if p.returncode:
        raise RuntimeError(
            f"Command failed ({p.returncode}): {args[0]}\n"
            + (p.stderr or p.stdout)[-1500:]
        )
    return p.stdout


def main() -> int:
    if not HTML.is_file():
        raise RuntimeError(f"Workbook HTML not found: {HTML}")
    browser = require_binary("chromium", "chromium-browser", "google-chrome", "google-chrome-stable")
    pdfinfo = require_binary("pdfinfo")
    pdftotext = require_binary("pdftotext")

    with tempfile.TemporaryDirectory(prefix="vorli-print-qa-") as temp:
        output = Path(temp) / "workbook.pdf"
        profile = Path(temp) / "chrome-profile"
        run(
            browser,
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--no-pdf-header-footer",
            "--print-to-pdf-no-header",
            "--user-data-dir=" + str(profile),
            "--print-to-pdf=" + str(output),
            HTML.resolve().as_uri(),
        )
        if not output.is_file():
            raise RuntimeError("Chromium did not produce a PDF")
        # First determine page count; then request detailed sizes for all pages.
        basic_info = run(pdfinfo, str(output))
        pages_match = re.search(r"^Pages:\s+(\d+)$", basic_info, flags=re.MULTILINE)
        if not pages_match:
            raise RuntimeError("Could not read PDF page count")
        count = int(pages_match.group(1))
        info = run(pdfinfo, "-f", "1", "-l", str(count), str(output))
        text = run(pdftotext, "-layout", str(output), "-")
        pdf_pages = [p for p in text.split("\f") if p.strip()]
        failures = []
        if count != 4:
            failures.append(f"Expected 4 PDF pages, got {count}")
        if len(pdf_pages) != count:
            failures.append(f"PDF text extraction returned {len(pdf_pages)} pages, metadata says {count}")
        for idx, heading in enumerate(HEADINGS):
            if idx >= len(pdf_pages):
                failures.append(f"Missing page {idx + 1}: {heading}")
                continue
            if heading not in pdf_pages[idx]:
                failures.append(f"Page {idx + 1} does not contain expected heading: {heading}")
            if not re.search(rf"\b{idx + 1}\s*/\s*4\b", pdf_pages[idx]):
                failures.append(f"Page {idx + 1} is missing its {idx + 1}/4 footer")
        # Require individual dimensions for each page; never accept a single
        # aggregate "Page size" line as proof for a multi-page document.
        sizes = re.findall(
            r"^Page\s+(\d+)\s+size:\s+([\d.]+)\s+x\s+([\d.]+)\s+pts",
            info, re.MULTILINE,
        )
        found_pages = [int(page) for page, _, _ in sizes]
        expected_pages = list(range(1, count + 1))
        if found_pages != expected_pages:
            failures.append(
                f"Could not verify dimensions of every PDF page: "
                f"expected {expected_pages}, got {found_pages}"
            )
        for page, width, height in sizes:
            if not (594 <= float(width) <= 596 and 841 <= float(height) <= 843):
                failures.append(
                    f"Page {page}: unexpected size {width} x {height} pt (expected A4)"
                )
        print(f"PDF pages: {count}; extracted pages: {len(pdf_pages)}")
        print("A4 check:", "PASS" if found_pages == expected_pages and not any("unexpected size" in f or "dimensions" in f for f in failures) else "UNVERIFIED/FAIL")
        print("Headings and footers:", "PASS" if not failures else "FAIL")
        if failures:
            for failure in failures:
                print("FAIL:", failure)
            print("Release remains BLOCKED. Review PDF visually after fixing issues.")
            return 1
        print("PASS: structural print checks only. Visual, accessibility, safety and legal reviews remain REQUIRED.")
        return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, subprocess.TimeoutExpired) as error:
        print("QA ERROR:", error, file=sys.stderr)
        sys.exit(2)
