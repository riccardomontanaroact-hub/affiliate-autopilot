import json, html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
SITE = ROOT / 'site'
SITE.mkdir(exist_ok=True)
(SITE/'products').mkdir(exist_ok=True)

def load(name):
    return json.loads((DATA/name).read_text(encoding='utf-8'))

cfg = load('config.json')
products = load('products.json')

def esc(x): return html.escape(str(x))

def score(p):
    return round((p.get('commission_rate',0)*100)*25 + min(p.get('rating',0),5)*8 + min(p.get('price',0)/100,5)*2 + len(p.get('pros',[]))*2, 2)

for p in products:
    p['score'] = score(p)
products.sort(key=lambda x:x['score'], reverse=True)

css='''body{font-family:system-ui,-apple-system,Segoe UI,sans-serif;margin:0;background:#f6f7f9;color:#18202a}header{background:#111827;color:white;padding:42px 20px}main{max-width:1050px;margin:auto;padding:28px 20px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}.card{background:white;border:1px solid #e5e7eb;border-radius:16px;padding:20px;box-shadow:0 5px 20px #00000008}.price{font-size:1.5rem;font-weight:800}.btn{display:inline-block;background:#facc15;color:#111827;padding:12px 16px;border-radius:10px;text-decoration:none;font-weight:800}.muted{color:#667085;font-size:.9rem}table{width:100%;border-collapse:collapse;background:white}td,th{padding:10px;border-bottom:1px solid #eee;text-align:left}footer{max-width:1050px;margin:auto;padding:30px 20px;color:#667085;font-size:.85rem}'''
(SITE/'style.css').write_text(css, encoding='utf-8')

cards=''.join(f'''<article class="card"><h2>{esc(p['name'])}</h2><p class="muted">{esc(p['category'])} · ⭐ {esc(p.get('rating',''))}</p><p>{esc(p['description'])}</p><p class="price">€ {p['price']:.2f}</p><a class="btn" href="{esc(p['affiliate_url'])}" rel="sponsored nofollow noopener" target="_blank">Vedi offerta</a></article>''' for p in products)

index=f'''<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(cfg['site_name'])}</title><meta name="description" content="{esc(cfg['tagline'])}"><link rel="stylesheet" href="style.css"></head><body><header><main><h1>{esc(cfg['site_name'])}</h1><p>{esc(cfg['tagline'])}</p></main></header><main><p class="muted">{esc(cfg['affiliate_disclosure'])}</p><div class="grid">{cards}</div></main><footer>© {esc(cfg['site_name'])}</footer></body></html>'''
(SITE/'index.html').write_text(index, encoding='utf-8')

rows=''.join(f"<tr><td>{esc(p['name'])}</td><td>{esc(p['merchant'])}</td><td>{p['commission_rate']*100:.2f}%</td><td>{p['score']}</td></tr>" for p in products)
dashboard=f'''<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Dashboard — {esc(cfg['site_name'])}</title><link rel="stylesheet" href="style.css"></head><body><main><h1>Dashboard Autopilot</h1><p class="muted">Priorità prodotti calcolata automaticamente. Non contiene credenziali.</p><table><thead><tr><th>Prodotto</th><th>Network</th><th>Commissione</th><th>Score</th></tr></thead><tbody>{rows}</tbody></table></main></body></html>'''
(SITE/'dashboard.html').write_text(dashboard, encoding='utf-8')
(DATA/'ranked_products.json').write_text(json.dumps(products, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Build completata: {len(products)} prodotti')
