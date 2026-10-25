# VORLI Lab — accessibilità, nomi link e QA browser (25 ottobre 2026)

## Isolamento e sicurezza
- Branch: `vorli/catalog-accessibility-regression-20261025`; PR in bozza [#69](https://github.com/riccardomontanaroact-hub/affiliate-autopilot/pull/69), verso `vorli/catalog-browser-ci-20261024`, non `main`.
- Nessun file in `site/`, nessun deploy, checkout, prezzo, link affiliato o pagamento introdotto. La pagina resta `noindex,nofollow`.
- 8 categorie demo, 5 risorse digitali ancora bozze. Nessun prodotto dichiarato acquistabile.
- Nessuna immagine esterna o licenza di immagini da verificare per le modifiche odierne: la grafica esistente è CSS.

## Modifiche
1. Ogni collegamento esterno alle cinque bozze GitHub include ora il titolo specifico della risorsa e l'avviso di apertura in una nuova scheda nel nome accessibile. L'icona ↗ è nascosta agli screen reader.
2. Classe CSS `.sr-only` per testo leggibile da tecnologie assistive, non visibile nel layout.
3. Regressione Python per nomi distinti, apertura in nuova scheda e rel sicuro; regressione Playwright sul nome accessibile effettivo.
4. Test Chromium per `forced-colors: active` e `prefers-reduced-motion: reduce` a 360 e 1440 px, visibilità del testo in gradiente, focus tastiera e overflow.
5. Il workflow QA è esteso alle PR sul branch di laboratorio del 24 ottobre, senza deploy.

## Esecuzione verificata
- [GitHub Actions — run 40175433433](https://github.com/riccardomontanaroact-hub/affiliate-autopilot/actions/runs/40175433433): **success** (25 ottobre 2026).
- Python unittest: **26/26** superati.
- Node: **5/5** superati.
- Chromium sulla pagina reale: **320, 360, 768, 1440 px** con JS attivo e disattivato; filtri, reset, navigazione locale, nomi accessibili dei cinque link, assenza di overflow orizzontale.
- Chromium in modalità alto contrasto forzato + movimento ridotto: **360 e 1440 px**, superati i controlli programmati.
- Artefatto: [10 screenshot QA](https://github.com/riccardomontanaroact-hub/affiliate-autopilot/actions/runs/40175433433/artifacts/12591484135) (8 ordinari + 2 forced-colors). Conservazione indicata da GitHub fino al **1 novembre 2026**.
- La prima esecuzione [40175357251](https://github.com/riccardomontanaroact-hub/affiliate-autopilot/actions/runs/40175357251) è fallita per un'asserzione eccessivamente rigida sugli spazi nel nome accessibile; il test è stato corretto e la seconda esecuzione è verde.

## Fonti digitali ricontrollate
Il 25 ottobre sono stati letti da GitHub i cinque sorgenti originali nei rispettivi branch: kit USB-C, checklist Casa Smart Sicura, confronto Power Station, workbook Elettrodomestici/EPREL e scheda HTML Casa Smart compilabile. Esistenza confermata; revisione editoriale, licenze, stabilizzazione e approvazione alla pubblicazione **non** completate.

## Limitazioni prima di un rilascio
I test automatizzati non equivalgono a certificazione WCAG 2.2: mancano prove con screen reader reali, zoom/testo ingrandito approfondito, audit manuale dei contrasti e degli screenshot, dispositivi fisici e revisione editoriale/legale/fiscale. Nessuna verifica aggiornata dell'approvazione Awin (ACEMAGIC, eWeki IT, 2GO Software IT, ALLPOWERS IT); nessun link affiliato pubblicabile finché non autorizzato. SEO e sitemap di produzione restano sospese, coerentemente con `noindex` del laboratorio.

**Non unire né pubblicare automaticamente:** occorre approvazione esplicita.
