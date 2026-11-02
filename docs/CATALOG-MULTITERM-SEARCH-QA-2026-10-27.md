# VORLI Lab — ricerca multi-parola e landmark accessibile (27 ottobre 2026)

## Ambito
Base `vorli/catalog-empty-state-ux-20261026` (PR #99 in bozza). Nuovo branch separato; nessun intervento in `site/`, su `main` o nei workflow di deploy.

## Problema e correzione
La ricerca precedente richiedeva che l'intera stringa inserita fosse contigua nel testo indicizzato. Per esempio, `casa smart` trovava le risorse con quel titolo ma **non** la categoria «Accessori casa», dove «casa» era nel nome e «smart» nelle parole chiave. La nuova logica normalizza e divide la query in termini separati da spazi; ogni termine deve comparire nella scheda, indipendentemente dall'ordine. Restano invariati il filtro per categoria, il pulsante di reset, lo stato vuoto e il fallback senza JavaScript.

I filtri sono ora un landmark `role="search"` nominato «Ricerca e filtri del catalogo demo». Input e selezione dichiarano con `aria-controls` le due griglie aggiornate. Nessun form, invio, tracking o chiamata esterna.

## Verifiche effettuate in questa sessione
- Lettura diretta dei sorgenti sul branch e parsing JavaScript riuscito.
- Esecuzione del **vero `catalogo-lab.js`** con un DOM di prova in memoria, popolato dai 13 record del file dati: 8 categorie e 5 risorse iniziali; `casa smart` → 1 categoria e 2 risorse; `smart    casa` → 1 e 2; query inesistente → 0 e 0 con stato vuoto visibile; reset → 8 e 5 con focus ripristinato; filtro `sport-tech` → 1 e 0.
- Verifica statica: 8 schede categoria, 5 schede risorsa, `noindex,nofollow`, landmark ricerca, `aria-controls` su due controlli, assenza di chiamate `fetch` o `XMLHttpRequest`.
- Nuove asserzioni aggiunte a `tests/browser_catalog_lab.py` e `tests/catalog-progressive.test.cjs`. **Non ancora eseguite su Chromium/CI**: non attribuire a questa PR il successo delle run precedenti.
- Verifica tramite API GitHub dell'esistenza di tutti e 5 i sorgenti originali (non equivalgono a revisione editoriale):
  - USB-C: `vorli/research-usbc-20261009/vault/products/kit-compatibilita-usbc-2026.md`
  - Casa Smart Sicura: `vorli/monetization-smart-home-20261009/vault/products/checklist-casa-smart-20261009.md`
  - Power Station: `vorli/powerstation-buyer-checklist-20261009-0707/vault/products/scheda-confronto-power-station-20261009.md`
  - Elettrodomestici EPREL: `vorli/monetization-eprel-20261009/vault/products/confronta-elettrodomestici-eprel-workbook-20261009.md`
  - Casa Smart compilabile: `vorli/product-casa-smart-checklist-20261013-0510/drafts/casa-smart-checklist-interattiva-2026-10-13.html`

## Da completare prima di qualsiasi merge/pubblicazione
Eseguire Python, Node e Chromium sul nuovo branch, verificare visivamente gli screenshot, screen reader reali, test fisici mobile/tablet, audit WCAG 2.2 e revisione editoriale/legale. L'attuale workflow browser ha un elenco ristretto di branch di destinazione: la PR contro il branch del 26 ottobre **potrebbe non avviarlo automaticamente**; non interpretare l'assenza di run come esito positivo.

## Guardrail
8 categorie **demo**, 5 sorgenti **bozza**, 0 offerte attive. Nessuna verifica di approvazione privata Awin; nessun link affiliato, checkout, prezzo, pagamento, account, dati personali o spesa. Nessun deploy.
