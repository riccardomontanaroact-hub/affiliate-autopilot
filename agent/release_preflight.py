"""Fail-closed release preflight for the VORLI draft.

Run with: python agent/release_preflight.py
This reports blockers only; it does not publish, merge, or change settings.
"""
import json
import sys
from pathlib import Path

try:
    from .offer_policy import ready_for_publication
except ImportError:
    from offer_policy import ready_for_publication

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SITE = ROOT / "site"
PREVIEW = ROOT / "preview" / "vorli-next"


def release_blockers():
    blockers = []
    config = json.loads((DATA / "config.json").read_text(encoding="utf-8"))
    owner = str(config.get("owner", "")).strip()
    contact = str(config.get("contact", "")).strip()
    if not owner or any(token in owner.upper() for token in ("INSERISCI", "PLACEHOLDER", "TODO")):
        blockers.append("Identità del titolare/responsabile non compilata.")
    if not contact:
        blockers.append("Contatto ufficiale non compilato.")
    disclosure = str(config.get("affiliate_disclosure", "")).strip()
    if not disclosure:
        blockers.append("Dichiarazione sulle affiliazioni mancante.")

    privacy = (PREVIEW / "privacy.html").read_text(encoding="utf-8").lower()
    if "nota informativa preliminare" in privacy or "non una dichiarazione di conformità legale" in privacy:
        blockers.append("Pagina privacy ancora preliminare: serve revisione prima del lancio.")

    products = json.loads((DATA / "products.json").read_text(encoding="utf-8"))
    ready = [p for p in products if ready_for_publication(p)]
    if not ready:
        blockers.append("Nessuna offerta verificata e approvata pronta per la pubblicazione.")
    for product in products:
        name = str(product.get("name", "")).upper()
        merchant = str(product.get("merchant", "")).upper()
        if any(marker in name + " " + merchant for marker in ("DEMO", "PLACEHOLDER", "INSERISCI", "PRODOTTO DEMO")):
            blockers.append("Il catalogo contiene ancora almeno una scheda dimostrativa.")
            break

    pages = ("index.html", "risorse.html", "guida.html", "usb-c.html", "privacy.html", "catalogo.html", "dashboard.html")
    for page in pages:
        source = PREVIEW / page if page not in ("catalogo.html", "dashboard.html") else None
        generated = SITE / page
        if source is not None and not source.is_file():
            blockers.append(f"Pagina sorgente mancante: {page}.")
        if not generated.is_file():
            blockers.append(f"Pagina generata mancante: {page}.")
        elif '<meta name="robots" content="noindex,nofollow">' not in generated.read_text(encoding="utf-8"):
            blockers.append(f"Pagina generata senza noindex atteso: {page}.")

    return list(dict.fromkeys(blockers))


def main():
    # Build first so checks inspect the current generated output, not stale files.
    import subprocess
    subprocess.run([sys.executable, str(ROOT / "agent" / "build.py")], cwd=ROOT, check=True)
    blockers = release_blockers()
    if blockers:
        print("VORLI — PRE-FLIGHT: BLOCCATO")
        for item in blockers:
            print(f"- {item}")
        print(f"\nTotale blocchi: {len(blockers)}")
        return 1
    print("VORLI — PRE-FLIGHT: controlli automatici superati.")
    print("Serve comunque una revisione umana di privacy, impostazioni Pages e offerte.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
