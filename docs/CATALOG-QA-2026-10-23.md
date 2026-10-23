# VORLI Lab — QA regressioni e accessibilità (23 ottobre 2026)

## Ambito e isolamento
Branch: `vorli/catalog-qa-regression-20261023`, derivato da `vorli/catalog-static-hydration-20261022`. Modifiche **solo** a CSS dell'anteprima, test e documentazione. Nessuna modifica a `site/`, `main`, checkout, automazioni commerciali o deployment.

## Problemi concreti corretti
1. `tests/catalog-progressive.test.cjs` verificava ancora `createDocumentFragment` e `replaceChildren` della vecchia implementazione: test obsoleto dopo l'hydration statica del 22 ottobre. Ora verifica schede HTML esistenti, sincronizzazione, assenza di sostituzione DOM, filtri, link e sicurezza.
2. `tests/test_catalogo_lab.py` rifiutava **tutti** i link esterni, mentre la pagina mostra cinque sorgenti GitHub reali. Ora accetta **solo** gli esatti cinque URL registrati nei dati editoriali, senza permettere domini pubblicitari.
3. `tests/test_catalog_lab_links_20261019.py` manteneva `@unittest.expectedFailure` per un collegamento di fallback già corretto. Rimosso il marcatore: il collegamento è ora un requisito da verificare normalmente.
4. `catalogo-lab.css`: aggiunto supporto `prefers-contrast: more` e `forced-colors: active`, con testo della hero visibile anche quando il gradiente viene disattivato dal sistema. Il gradiente del CTA primario parte ora da `#046fa9`: contrasto teorico bianco/sfondo circa **5,45:1** su quell'estremo (calcolo sRGB statico, non audit WCAG completo).
5. Aggiunto `tests/browser_catalog_lab.py`, test Chromium **opzionale** sul file HTML completo (non una fixture) a 360/768/1440 px, JavaScript attivo/disattivato, filtri, ricerca, risultati vuoti, overflow orizzontale ed errori JS.

## Controlli effettuati in questa sessione
- Recuperati dal repository HTML, CSS, JS, dati editoriali e test sul nuovo branch.
- Verificata la sintassi JavaScript con il parser V8 (`new Function`), senza esecuzione in browser.
- Verificati staticamente 8 elementi `article.category` e 5 elementi `article.resource` nell'HTML.
- Confrontati esattamente i cinque link GitHub nell'HTML con i cinque `source` in `catalogo-lab-data.js`: corrispondenza.
- Verificati `commercialOffers: 0`, `checkoutEnabled: false`, `publicationApproved: false`, `noindex,nofollow`, fallback statico e assenza di `replaceChildren` nel JS.
- Verificata **via connettore GitHub** l'esistenza dei cinque sorgenti originali, nei rispettivi branch, il 23 ottobre 2026: USB-C, Casa Smart Sicura, Power Station, EPREL, checklist HTML Casa Smart.

## Comandi per verifica su checkout completo
```bash
python -m unittest discover -s tests -v
node --test tests/catalog-progressive.test.cjs
python -m compileall -q agent tests
# Test browser opzionale, NON eseguito qui:
# pip install playwright
# CHROMIUM_PATH=/usr/bin/chromium python tests/browser_catalog_lab.py
```

## Limiti e blocchi prima del rilascio
- **Non** sono stati eseguiti in questa sessione i test Python/Node su checkout completo né il test Chromium sul catalogo reale: il connettore GitHub consente lettura/scrittura, ma non esegue codice del repository.
- Il test Chromium è disponibile come script, ma va eseguito e i risultati registrati. Il suo successo non sostituisce un audit WCAG 2.2, la verifica da tastiera e con screen reader o i test a zoom 200%.
- Non è stato fatto un audit completo di SEO, sitemap, performance o diritti sulle immagini; l'anteprima non carica immagini esterne e rimane `noindex`.
- I cinque sorgenti sono **bozze** verificabili, non PDF definitivi o beni vendibili. Nessuna conferma Awin per ACEMAGIC, eWeki IT, 2GO Software IT, ALLPOWERS IT è stata acquisita.
- Prima di ogni pubblicazione: review editoriale e legale/fiscale, verifica diritti, QA browser e accessibilità, stabilizzazione dei file digitali su un branch approvato, autorizzazioni commerciali e approvazione esplicita del proprietario.

**Sicurezza:** nessuna spesa, account, spam, dati personali, link affiliati, checkout o modifica alla produzione.
