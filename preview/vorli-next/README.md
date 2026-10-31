# VORLI Next — anteprima mobile-first (non pubblicata)

Prototipo iniziato il 9 ottobre 2026; aggiornamento catalogo Lab del 31 ottobre 2026. Tutte le pagine sono in `preview/vorli-next/`, **separate da `site/`** (sito pubblico).

## Avvio e verifiche

Aprire `index.html` localmente oppure eseguire `python3 -m http.server 8000 -d preview/vorli-next`. Il catalogo più recente è `catalogo-lab.html`: 8 categorie editoriali e 5 risorse originali in bozza, già presenti nell'HTML. Ricerca e filtri si attivano con JavaScript locale; senza JavaScript le schede restano visibili. La ricerca supporta più parole anche in ordine diverso (es. `casa smart` e `smart casa`).

Controlli statici: `python -m unittest discover -s tests -v` e `node --test tests/catalog-progressive.test.cjs`. Per Chromium reale: installare Playwright e Chromium e avviare `python tests/browser_catalog_lab.py`. Lo script crea screenshot in `artifacts/catalog-lab/`. Il test browser copre anche la nuova guida per categorie; verificare sempre l'esito della CI sul commit corrente e non dedurlo da esecuzioni precedenti.

## Guida originale per categorie

La pagina `guida-scelta-tech-lab.html` propone otto checklist editoriali originali, una per ogni categoria, raggiungibili direttamente dalle schede del catalogo. È una pagina statica senza JavaScript, con ancore navigabili, CSS locale e `noindex,nofollow`; non contiene prodotti o link commerciali. Il rapporto `docs/CATALOG-CATEGORY-GUIDE-QA-2026-10-31.md` descrive verifiche e limiti.

## Isolamento commerciale e diritti

I 5 link a sorgenti Markdown/HTML sono stati ricontrollati il 31 ottobre 2026 su branch editoriali separati: **non sono PDF finali né prodotti acquistabili**. Le illustrazioni del catalogo sono generate con CSS/testo e non caricano immagini, font o servizi esterni; l'illustrazione SVG della home è incorporata e originale. Gli script del catalogo sono locali e non inviano richieste di rete.

Le pagine Lab hanno `noindex,nofollow`. Nessun link affiliato, prezzo, carrello, checkout, pagamento, tracciamento o dato personale. Non attribuire approvazioni Awin non verificate.

## Prima di un eventuale rilascio

Revisionare visivamente gli screenshot, eseguire screen reader e test su dispositivi fisici, audit WCAG 2.2, verifica SEO/canonical/sitemap della **futura** versione pubblica, revisione editoriale e dei diritti, stabilizzazione dei sorgenti digitali e controlli legali/fiscali e commerciali. Non fare merge o deploy automatici. Il workflow esistente pubblica da `site/`, che qui non viene modificato.
