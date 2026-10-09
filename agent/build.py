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
    price_html = f'<p class="price">€ {float(price):.2f}</p>' if price is not None else ""
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
<title>Catalogo | VORLI</title><link rel="stylesheet" href="style.css">
</head>
<body>
<header class="top"><div class="wrap nav">
<a class="brand" href="index.html">◆ VORLI</a>
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
<title>Dashboard — {esc(cfg['site_name'])}</title><link rel="stylesheet" href="style.css">
</head><body><main class="wrap"><h1>Dashboard Autopilot</h1>
<p class="muted">Priorità prodotti calcolata automaticamente. Non contiene credenziali.</p>
<table><thead><tr><th>Prodotto</th><th>Network</th><th>Commissione</th><th>Score</th></tr></thead>
<tbody>{rows}</tbody></table></main></body></html>"""
(SITE / "dashboard.html").write_text(dashboard, encoding="utf-8")
(DATA / "ranked_products.json").write_text(
    json.dumps(products, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(f"Build completata: {len(products)} prodotti; home VORLI Next e catalogo generati.")
