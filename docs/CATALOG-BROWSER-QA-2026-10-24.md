# VORLI Lab — test browser reale e prove visive (24 ottobre 2026)

## Isolamento
Branch: `vorli/catalog-browser-ci-20261024`; PR in bozza #65 verso `vorli/catalog-qa-regression-20261023`, **non** verso `main`. Modificati solo lo script di QA e un workflow CI dedicato. `site/`, checkout, offerte, affiliazioni e GitHub Pages restano invariati.

## Esecuzione confermata
- Workflow: [VORLI Lab browser evidence — run 40075902184](https://github.com/riccardomontanaroact-hub/affiliate-autopilot/actions/runs/40075902184)
- Data: 2026-10-24; conclusione GitHub Actions: **success**.
- Test Python `python -m unittest discover -s tests -v`: **25/25 superati**.
- Test Node `node --test tests/catalog-progressive.test.cjs`: **5/5 superati**.
- `python -m compileall -q agent tests`: **superato**.
- Chromium + Playwright sulla pagina completa `preview/vorli-next/catalogo-lab.html`: **superato** a **320, 360, 768, 1440 px**, con JavaScript attivo e disattivato.
- Verificati: 8 categorie demo e 5 bozze visibili, ricerca `energia`, filtro `sport-tech`, reset, nessun risultato, skip link da tastiera, etichette dei filtri, noindex, collegamenti locali, assenza di errori JavaScript e richieste di rete esterne, assenza di overflow orizzontale (soglia 1 px).
- Artefatto: [8 screenshot Chromium (JS on/off, quattro larghezze)](https://github.com/riccardomontanaroact-hub/affiliate-autopilot/actions/runs/40075902184/artifacts/12553720405). Conservazione GitHub: **fino al 31 ottobre 2026**.

## Cosa NON prova il test
Non è un audit WCAG 2.2 completo, non include lettori di schermo, dispositivi fisici, zoom browser al 200%, navigazione completa da tastiera o revisione umana degli screenshot. I link esterni ai cinque sorgenti non sono stati ricontrollati in rete in questo run: il test verifica solo che il catalogo non effettui richieste remote e che i collegamenti locali esistano. Le cinque risorse rimangono **bozze editoriali** sui rispettivi branch, non prodotti scaricabili definitivi né offerte commerciali.

## Prima di qualsiasi rilascio
Revisionare manualmente gli otto screenshot, effettuare audit WCAG e test con screen reader e dispositivi fisici, revisionare le cinque bozze e stabilizzarne i file, verificare SEO e sitemap di una futura versione pubblicabile, diritti immagini e aspetti legali/fiscali. Attendere approvazioni Awin verificabili; **nessun link affiliato, prezzo, checkout o provider pagamenti attivo**. Richiedere approvazione esplicita prima di qualunque merge verso produzione.

Nessuna spesa o servizio a pagamento richiesto; nessun account nuovo, dato personale o spam.
