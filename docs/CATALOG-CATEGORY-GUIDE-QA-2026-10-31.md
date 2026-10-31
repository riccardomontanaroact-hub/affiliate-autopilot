# VORLI Lab — guida editoriale per otto categorie (31 ottobre 2026)

## Scopo e perimetro
Nuova pagina originale `preview/vorli-next/guida-scelta-tech-lab.html` con otto checklist di valutazione: computer, software, elettronica, elettrodomestici smart, accessori casa, sport tech, benessere tech, energia portatile. Tre criteri pratici per categoria, senza modelli, prezzi, promesse mediche, offerte o link commerciali. I contenuti sono orientativi: verificare le specifiche del prodotto esatto e la documentazione ufficiale.

## Implementazione
- Pagina HTML semantica in italiano, `noindex,nofollow`, zero JavaScript e zero asset remoti; riusa il CSS blu notte/azzurro elettrico del catalogo.
- Indice navigabile da tastiera e otto sezioni con ancore e link di ritorno. Griglie responsive: due colonne su desktop, una su mobile.
- Otto schede del catalogo demo rimandano alla rispettiva checklist, senza alterare titoli, descrizioni o logica di ricerca/filtri.
- `tests/test_catalogo_lab.py`: link locali con frammenti e verifiche statiche della guida.
- `tests/catalog-progressive.test.cjs`: presenza e isolamento della guida e corrispondenza delle otto ancore.
- `tests/browser_catalog_lab.py`: verifica Chromium su 320/360/768/1440 px, tastiera, navigazione e assenza di overflow; screenshot della guida a 360/1440 px.

## Verifica sorgenti originali
Il 31 ottobre 2026 è stata confermata via repository l'esistenza dei cinque sorgenti già registrati: USB-C, Casa Smart Sicura, Power Station, Elettrodomestici EPREL e Casa Smart compilabile. Sono **bozze** su branch separati, non file finali o prodotti acquistabili. Nessun nuovo collegamento affiliato è stato aggiunto.

## Test da eseguire / limiti
Eseguire:
```sh
python -m unittest discover -s tests -v
node --test tests/catalog-progressive.test.cjs
python tests/browser_catalog_lab.py
```
Una PR o un commit non costituisce prova di test superati: consultare l'esito effettivo del workflow e gli screenshot. Restano da completare revisione visiva umana, screen reader, WCAG 2.2, dispositivi fisici, revisione editoriale e verifiche legali/fiscali.

## Sicurezza
Solo `preview/vorli-next/` e test/documentazione, **nessuna modifica a `site/`**, nessun merge/deploy. Non pubblicare nella sitemap del sito live una pagina Lab `noindex`. Nessuna raccolta dati, immagine di terzi, servizio esterno, prezzo, checkout, provider di pagamento, link affiliato o approvazione Awin presunta.
