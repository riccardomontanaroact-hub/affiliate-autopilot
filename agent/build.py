import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SITE = ROOT / "site"
PREVIEW = ROOT / "preview" / "vorli-next"
SITE.mkdir(exist_ok=True)
(SITE / "products").mkdir(exist_ok=True)


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def esc(value):
    return html.escape(str(value))


def score(product):
    return round(
        (product.get("commission_rate", 0) * 100) * 25
        + min(product.get("rating", 0), 5) * 8
        + min(product.get("price", 0) / 100, 5) * 2
        + len(product.get("pros", [])) * 2,
        2,
    )


cfg = load("config.json")
products = load("products.json")
for product in products:
    product["score"] = score(product)
products.sort(key=lambda item: item["score"], reverse=True)

# Publish the reviewed mobile-first VORLI design, rather than the old generated shell.
index_source = (PREVIEW / "index.html").read_text(encoding="utf-8")
style_source = (PREVIEW / "style.css").read_text(encoding="utf-8")

# Guard against publishing an outdated homepage without the approved VORLI logo.
if 'class="brand-mark"' not in index_source or 'vorli-gradient' not in index_source or 'SMART E-COMMERCE' not in index_source or 'FOR A BETTER TOMORROW' not in index_source:
    raise SystemExit("Build bloccata: il lockup VORLI approvato manca dalla sorgente preview/index.html.")

(SITE / "index.html").write_text(index_source, encoding="utf-8")
(SITE / "style.css").write_text(style_source, encoding="utf-8")
# Publish the supporting pages linked by the new navigation as well.
for page in ("risorse.html", "guida.html", "usb-c.html"):
    (SITE / page).write_text((PREVIEW / page).read_text(encoding="utf-8"), encoding="utf-8")

# Keep the product catalogue available as a separate page. Placeholder offers are
# explicitly marked as demos and never link visitors to example.com.
cards = []
for product in products:
    demo = (
        product.get("affiliate_url", "").startswith("https://example.com")
        or product.get("merchant", "").strip().upper() in {"INSERISCI NETWORK", "DEMO"}
    )
    if demo:
        action = '<span class="tag demo">Scheda dimostrativa · offerta non disponibile</span>'
    else:
        action = (
            f'<a class="button" href="{esc(product.get("affiliate_url", ""))}" '
            'rel="sponsored nofollow noopener" target="_blank">Vedi offerta</a>'
        )
    price = product.get("price")
    price_html = f'<p class="price">€ {float(price):.2f}</p>' if price is not None and not demo else ""
    cards.append(
        '<article class="card">'
        f'<span class="tag demo">{ "Demo" if demo else "Prodotto" }</span>'
        f'<h2>{esc(product.get("name", "Prodotto"))}</h2>'
        f'<p class="muted">{esc(product.get("category", ""))}'
        f' · {("⭐ " + esc(product.get("rating"))) if product.get("rating") else ""}</p>'
        f'<p>{esc(product.get("description", ""))}</p>'
        f'{price_html}{action}</article>'
    )

catalog = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Catalogo VORLI: schede prodotto e offerte da verificare.">
<title>Catalogo | VORLI</title><link rel="stylesheet" href="style.css?v=vorli-brand-lockup-20261011">
</head>
<body>
<header class="top"><div class="wrap nav">
<a class="brand" href="index.html" aria-label="VORLI — Smart E-commerce"><svg class="brand-mark" viewBox="0 0 88 88" role="img" aria-label="Simbolo VORLI tridimensionale con orbita luminosa" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="vorli-gradient" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8df8ff"/><stop offset=".42" stop-color="#36c8ff"/><stop offset=".72" stop-color="#6284ff"/><stop offset="1" stop-color="#c17aff"/></linearGradient><linearGradient id="vorli-depth" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#10295c"/><stop offset=".5" stop-color="#2457a8"/><stop offset="1" stop-color="#6a3ea2"/></linearGradient><filter id="vorli-glow" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="2.8" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><ellipse class="brand-orbit orbit-back" cx="44" cy="44" rx="36" ry="14" fill="none" stroke="#39d9ff" stroke-width="2" opacity=".8" transform="rotate(-28 44 44)"/><ellipse class="brand-orbit orbit-front" cx="44" cy="44" rx="31" ry="11" fill="none" stroke="#b47cff" stroke-width="1.6" opacity=".75" transform="rotate(27 44 44)"/><path d="M18 17 35 68 67 17" fill="none" stroke="#07132f" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/><path d="M18 15 35 66 67 15" fill="none" stroke="url(#vorli-depth)" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" transform="translate(2 2)"/><path d="M18 14 35 64 67 14" fill="none" stroke="url(#vorli-gradient)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" filter="url(#vorli-glow)"/><path d="M20 17 35 59 63 17" fill="none" stroke="#e1ffff" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" opacity=".8"/><circle cx="74" cy="24" r="4.2" fill="#b9faff" filter="url(#vorli-glow)"/></svg><span class="brand-copy"><span class="brand-name">VORLI</span><span class="brand-subtitle">SMART E-COMMERCE</span><span class="brand-payoff">FOR A BETTER TOMORROW</span></span></a>
<nav class="links" aria-label="Navigazione principale">
<a href="index.html">Home</a><a href="catalogo.html" aria-current="page">Catalogo</a>
<a href="risorse.html">Risorse</a><a href="guida.html">Metodo</a>
</nav></div></header>
<main class="wrap">
<section class="intro"><span class="eyebrow">VORLI Shopping</span>
<h1>Catalogo prodotti</h1>
<p>Le schede dimostrative sono chiaramente indicate. Verifica sempre venditore, prezzo e disponibilità.</p>
<p class="notice">{esc(cfg.get("affiliate_disclosure", "Alcuni link possono essere affiliati."))}</p>
</section>
<div class="grid three">{''.join(cards)}</div>
</main>
<footer class="foot"><div class="wrap"><strong>VORLI</strong>
<p>Prezzi e disponibilità possono cambiare. Le schede demo non sono offerte acquistabili.</p>
<p>© 2026 VORLI · <a href="guida.html">Metodo editoriale</a></p></div></footer>
</body></html>"""
(SITE / "catalogo.html").write_text(catalog, encoding="utf-8")

rows = "".join(
    f"<tr><td>{esc(p.get('name', ''))}</td><td>{esc(p.get('merchant', ''))}</td>"
    f"<td>{float(p.get('commission_rate', 0)) * 100:.2f}%</td><td>{p['score']}</td></tr>"
    for p in products
)
dashboard = f"""<!doctype html><html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dashboard — {esc(cfg['site_name'])}</title><link rel="stylesheet" href="style.css?v=vorli-brand-lockup-20261011">
</head><body><main class="wrap"><h1>Dashboard Autopilot</h1>
<p class="muted">Priorità prodotti calcolata automaticamente. Non contiene credenziali.</p>
<table><thead><tr><th>Prodotto</th><th>Network</th><th>Commissione</th><th>Score</th></tr></thead>
<tbody>{rows}</tbody></table></main></body></html>"""
(SITE / "dashboard.html").write_text(dashboard, encoding="utf-8")
(DATA / "ranked_products.json").write_text(
    json.dumps(products, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(f"Build completata: {len(products)} prodotti; home VORLI Next e catalogo generati.")
