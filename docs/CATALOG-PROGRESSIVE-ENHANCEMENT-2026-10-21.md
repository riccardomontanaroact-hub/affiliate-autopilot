# VORLI Lab — Progressive enhancement (21 ottobre 2026)

**Scope:** `vorli/catalog-progressive-enhancement-20261021`, based on `vorli/catalog-navigation-fallback-fixed-20261020`. Non destinato al deploy.

## Modifiche
- `catalogo-lab.html`: 8 schede editoriali e 5 risorse originali **prerenderizzate in HTML**, visibili anche se JavaScript è disattivato, non disponibile o fallisce prima dell'avvio. Il collegamento al catalogo statico resta presente.
- `catalogo-lab.js`: genera schede in due `DocumentFragment` e sostituisce l'HTML di fallback **solo al termine** della costruzione di entrambe le raccolte. I filtri vengono abilitati solo dopo il completamento del rendering.
- `catalogo-lab.css`: filtri nascosti in assenza di inizializzazione JavaScript; visibili con `.js-ready`.
- `tests/catalog-progressive.test.cjs`: test Node.js standard per schede HTML, coerenza dati, assenza checkout, collegamenti interni, e pattern di enhancement. Esecuzione prevista: `node --test tests/catalog-progressive.test.cjs`.

## Verifiche e limiti
I 5 sorgenti sono stati riletti via connettore GitHub il 21 ottobre 2026 sui branch esplicitati nel catalogo; esistenza verificata, **non** revisione editoriale o idoneità commerciale. Nessun prodotto è in vendita. Le candidature Awin ACEMAGIC, eWeki IT, 2GO Software IT, ALLPOWERS IT non sono trattate come approvate. Il catalogo mantiene `noindex,nofollow`.

La generazione del markup HTML è stata controllata per conteggio (8 + 5), struttura e riferimenti; test statici nel codice allegato. **Non sono stati eseguiti in questa sessione test reali su Chromium a 360/768/1440 px né audit WCAG.** Non dichiarare superati questi test prima dell'esecuzione.

## Verifiche necessarie prima di qualsiasi rilascio
1. Eseguire `node --test tests/catalog-progressive.test.cjs`.
2. Aprire il Lab in browser con JS attivo, disattivato e con script dati bloccato; verificare 8 + 5 schede senza duplicati e ricerca/filtri solo se disponibili.
3. Verificare viewport 360/768/1440, zoom 200%, tastiera, lettore di schermo e contrasto.
4. Revisionare i cinque materiali digitali, i diritti d'uso, le condizioni commerciali, gli adempimenti legali/fiscali e ogni eventuale approvazione Awin prima di pubblicare.

Nessuna modifica a `main` o `site/`; nessuna spesa, vendita, pagamento, link affiliato non autorizzato o dato personale pubblicato.
