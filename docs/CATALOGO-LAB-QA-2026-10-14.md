# VORLI Catalogo Lab — prototipo non commerciale
Verifica: **14 ottobre 2026**. Branch di lavoro, non pubblicato.

## Implementato
- `preview/vorli-next/catalogo-lab.html`: landing e catalogo di esplorazione mobile-first, palette blu notte / azzurro elettrico, hero CSS originale, navigazione e indicatori di stato.
- `catalogo-lab.css`: responsive (1/2/4 colonne), focus visibile, reduced motion, nessun font o immagine esterna. Le grafiche sono CSS originali; non servono licenze di stock.
- `catalogo-lab-data.js`: **otto categorie demo** e **cinque risorse digitali originali già esistenti** (quattro Markdown e un HTML), senza prezzi, recensioni, link affiliati o CTA di acquisto.
- `catalogo-lab.js`: ricerca e filtro per categoria, reset, conteggio live e stato vuoto. Nessuna chiamata di rete, cookie, analytics o raccolta dati.
- `tests/test_catalogo_lab.py`: controlli di integrità, percorsi locali, provenienza delle risorse, noindex e protezioni editoriali.

## Come visualizzare
Avviare dalla radice del repository `python3 -m http.server 8000` e aprire `/preview/vorli-next/catalogo-lab.html`. Si può aprire anche direttamente il file HTML con il browser: tutti gli asset sono locali e il dataset è JavaScript statico. Nessuna connessione a un negozio o network affiliato.

## Fonti e diritti
I cinque URL di risorse puntano a file verificati con il connettore GitHub il **14 ottobre 2026**: kit USB-C, Casa Smart Sicura, confronto power station, workbook EPREL e scheda Casa Smart HTML. I contenuti sono bozze, non prodotti vendibili né PDF finali. I link conducono a GitHub per revisione, non a download commerciali. Grafiche di questa pagina realizzate con CSS e testo originali; nessuna immagine di terzi.

## SEO e sitemap (non pubblicare ora)
Meta title: «Catalogo tecnologia: categorie e guide | VORLI»; meta description candidata: «Guide pratiche e confronti verificati su computer, software, smart home, sport tech ed energia portatile». Non usare finché non sono presenti contenuti finali. Questa pagina mantiene `noindex,nofollow` e **non deve comparire in sitemap**. Quando il sito sarà approvato, creare una sitemap con soli URL canonici pubblici, raggiungibili e indicizzabili; escludere demo, bozze, dashboard e pagine di test. Verificare `robots.txt`, canonical, hreflang (se applicabile), disclosure e dati strutturati prima del rilascio. Non creare dati strutturati Product/Offer con informazioni simulate.

## Gate prima di ogni pubblicazione
1. Test Chromium alle larghezze 360, 768 e 1440 px; tastiera, lettore schermo e contrasto WCAG.
2. Controllo editoriale/tecnico dei cinque file e delle fonti; autorizzazione esplicita alla distribuzione.
3. Conferma stato advertiser Awin 3118306 in dashboard e link approvati (ACEMAGIC, eWeki IT, 2GO Software IT, ALLPOWERS IT ancora non verificati).
4. Revisione legale/fiscale per venditore individuale italiano e provider di pagamento prima di abilitare vendita diretta.
5. Verifica pipeline `agent/build.py`: attualmente il generatore usa `preview/vorli-next/index.html` e genera `site/catalogo.html` separatamente; **questo prototipo non è integrato nella produzione**.
6. Revisione umana e PR in bozza. Non fare merge/deploy automatico.

Nessuna spesa, account, invio email, dati personali, checkout o pubblicazione in produzione.
