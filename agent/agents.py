#!/usr/bin/env python3
"""Run five deterministic VORLI specialist agents and write an auditable report.

These agents perform repository-based checks; they do not call external LLMs,
contact partners, publish offers, spend money, or change account settings.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports"
REQUIRED_PAGES = ("index.html", "catalogo.html", "risorse.html", "guida.html", "usb-c.html")


def read_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def result(name, role, status, summary, findings=None, next_step=""):
    return {
        "agent": name,
        "role": role,
        "status": status,
        "summary": summary,
        "findings": findings or [],
        "next_step": next_step,
    }


def is_demo(product):
    url = str(product.get("affiliate_url", ""))
    merchant = str(product.get("merchant", "")).strip().upper()
    return url.startswith("https://example.com") or merchant in {"INSERISCI NETWORK", "DEMO"}


def run_agents(root: Path = ROOT):
    data_dir = root / "data"
    site_dir = root / "site"
    products = read_json(data_dir / "products.json", [])
    config = read_json(data_dir / "config.json", {})
    findings = []
    present_pages = [p for p in REQUIRED_PAGES if (site_dir / p).is_file()]
    missing_pages = [p for p in REQUIRED_PAGES if p not in present_pages]
    demo_products = [p for p in products if is_demo(p)]
    real_products = [p for p in products if not is_demo(p)]
    agents = []

    # 1. Coordinator / strategist: inventory and next-step readiness.
    core_missing = [p for p in ("agent/build.py", "data/config.json", "data/products.json") if not (root / p).is_file()]
    status = "ATTENZIONE" if core_missing or missing_pages else "OK"
    agents.append(result(
        "Coordinatore e Stratega",
        "Controlla le basi del progetto, sintetizza i rischi e ordina il prossimo intervento.",
        status,
        f"File fondamentali mancanti: {len(core_missing)}; pagine pubblicate mancanti: {len(missing_pages)}.",
        [*(f"File fondamentale mancante: {p}" for p in core_missing),
         *(f"Pagina attesa non trovata: site/{p}" for p in missing_pages)],
        "Completare prima i blocchi tecnici e mantenere separate le attività che richiedono approvazione umana."
    ))

    # 2. Site creator / developer: verify build inputs and published pages.
    status = "ATTENZIONE" if missing_pages or not (root / "agent/build.py").is_file() else "OK"
    agents.append(result(
        "Creatore del Sito e Catalogo",
        "Verifica il generatore e la presenza delle pagine essenziali del sito.",
        status,
        f"Pagine presenti: {len(present_pages)}/{len(REQUIRED_PAGES)}.",
        [*(f"Manca site/{p}" for p in missing_pages)],
        "Dopo ogni modifica, eseguire la build e verificare il deploy GitHub Pages."
    ))

    # 3. Monetization: readiness audit only; never activates commerce.
    invalid_links = [p for p in products if p.get("affiliate_url") and not str(p["affiliate_url"]).startswith("https://")]
    missing_links = [p for p in real_products if not p.get("affiliate_url")]
    disclosure = bool(config.get("affiliate_disclosure"))
    status = "ATTENZIONE" if demo_products or invalid_links or missing_links or not disclosure else "OK"
    agents.append(result(
        "Monetizzatore",
        "Controlla la preparazione delle schede e la trasparenza affiliata senza attivare vendite.",
        status,
        f"Schede reali candidate: {len(real_products)}; schede demo: {len(demo_products)}; disclosure presente: {'sì' if disclosure else 'no'}.",
        [*(f"Scheda demo da sostituire: {p.get('id', p.get('name', 'senza ID'))}" for p in demo_products),
         *(f"Link non HTTPS: {p.get('id', p.get('name', 'senza ID'))}" for p in invalid_links),
         *(f"Link affiliato mancante: {p.get('id', p.get('name', 'senza ID'))}" for p in missing_links),
         *([] if disclosure else ["Disclosure affiliata mancante"])],
        "Sostituire i dati demo solo con offerte verificate e programmi approvati; checkout e campagne restano disattivati."
    ))

    # 4. Designer / SEO: basic mobile, language and metadata audit.
    seo_findings = []
    inspected = 0
    for page in REQUIRED_PAGES:
        path = site_dir / page
        if not path.is_file():
            continue
        inspected += 1
        content = path.read_text(encoding="utf-8", errors="replace")
        if 'lang="it"' not in content:
            seo_findings.append(f"{page}: attributo lang=\"it\" assente")
        if "name=\"viewport\"" not in content:
            seo_findings.append(f"{page}: meta viewport assente")
        if not re.search(r"<title>\s*.+?\s*</title>", content, re.I | re.S):
            seo_findings.append(f"{page}: titolo pagina assente")
        if not re.search(r'<meta\s+name="description"\s+content="[^"]+?"', content, re.I):
            seo_findings.append(f"{page}: meta description assente")
        if re.search(r'<meta\s+name="robots"\s+content="[^"]*noindex', content, re.I):
            seo_findings.append(f"{page}: noindex presente; verificare prima dell'indicizzazione pubblica")
        for img in re.findall(r"<img\b[^>]*>", content, re.I):
            if not re.search(r'\balt\s*=', img, re.I):
                seo_findings.append(f"{page}: immagine senza attributo alt")
                break
    agents.append(result(
        "Designer e SEO",
        "Controlla i requisiti di base per mobile, accessibilità e metadati SEO.",
        "ATTENZIONE" if seo_findings else "OK",
        f"Pagine controllate: {inspected}; rilievi: {len(seo_findings)}.",
        seo_findings,
        "Rivedere i rilievi SEO e accessibilità prima di investire nella promozione organica."
    ))

    # 5. Promotion / partnerships: assess readiness, never send outreach.
    promo_findings = []
    if not real_products:
        promo_findings.append("Nessuna scheda prodotto reale pronta da promuovere.")
    if not config.get("networks"):
        promo_findings.append("Nessun network affiliato configurato.")
    agents.append(result(
        "Promotore e Partnership",
        "Valuta se catalogo e tracciamento sono pronti per future collaborazioni.",
        "ATTENZIONE" if promo_findings else "OK",
        f"Schede reali candidate alla promozione: {len(real_products)}. Nessun contatto esterno inviato.",
        promo_findings,
        "Preparare proposte e materiali; ogni contatto, accordo o campagna richiede approvazione umana."
    ))

    warning_count = sum(a["status"] != "OK" for a in agents)
    return {
        "project": "VORLI",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "execution_mode": "deterministic_repository_audit",
        "note": "Controlli automatici verificabili; non è un modello LLM autonomo e non esegue azioni commerciali.",
        "summary": {
            "agents_run": len(agents),
            "agents_with_findings": warning_count,
            "products_total": len(products),
            "products_demo": len(demo_products),
            "products_real_candidates": len(real_products),
        },
        "agents": agents,
    }


def render_markdown(report):
    summary = report["summary"]
    lines = [
        "# Rapporto agenti VORLI",
        "",
        f"- Generato (UTC): {report['generated_at_utc']}",
        f"- Modalità: `{report['execution_mode']}`",
        f"- Agenti eseguiti: {summary['agents_run']}",
        f"- Agenti con rilievi: {summary['agents_with_findings']}",
        f"- Prodotti: {summary['products_total']} totali, {summary['products_demo']} demo, {summary['products_real_candidates']} candidati reali",
        "",
        "> I controlli sono automatici e basati sui file del repository. Non sono ancora agenti LLM autonomi; non contattano partner, non spendono denaro e non attivano vendite.",
        "",
    ]
    for agent in report["agents"]:
        lines += [f"## {agent['agent']} — {agent['status']}", "", agent["summary"], "", agent["role"], ""]
        if agent["findings"]:
            lines += ["**Rilievi**", *[f"- {finding}" for finding in agent["findings"]], ""]
        lines += [f"**Prossimo passo:** {agent['next_step']}", ""]
    return "\n".join(lines).rstrip() + "\n"


def main():
    report = run_agents()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "agent-status.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown = render_markdown(report)
    (REPORT_DIR / "agent-status.md").write_text(markdown, encoding="utf-8")
    print(markdown)
    summary_path = __import__("os").environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary_file:
            summary_file.write(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
