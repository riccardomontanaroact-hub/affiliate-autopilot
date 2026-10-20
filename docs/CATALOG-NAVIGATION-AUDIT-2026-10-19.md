# VORLI Lab — audit navigazione e collegamenti (19 ottobre 2026)

**Ambito:** branch di laboratorio `vorli/catalog-static-fallback-20261018`, nessuna modifica a `main` o `site/`.

## Verifiche effettuate tramite GitHub
- La pagina `preview/vorli-next/catalogo-statico-lab.html` contiene otto schede editoriali, `noindex,nofollow`, nessun elemento `script` e nessun modulo d'ordine.
- La pagina `catalogo-lab.html` carica categorie e risorse tramite JavaScript; se JavaScript è disabilitato, `#category-cards` resta vuoto. Il messaggio `noscript` attuale rimanda soltanto alle risorse, **non** al catalogo statico. È un problema di accessibilità e scopribilità da correggere.
- Cinque file sorgente dei prodotti editoriali risultano raggiungibili sui branch indicati nei dati. La loro esistenza **non** ne certifica la revisione editoriale o l'idoneità commerciale.
- `catalogo-lab-data.js` dichiara otto categorie, cinque risorse, `commercialOffers: 0`, `checkoutEnabled: false` e `publicationApproved: false`.

## Intervento consigliato (non applicato)
1. Inserire un collegamento HTML visibile a `catalogo-statico-lab.html` nell'intestazione o nell'area introduttiva di `catalogo-lab.html`.
2. Nel blocco `noscript`, rimandare esplicitamente al catalogo statico, oltre alla pagina delle risorse.
3. Mantenere la navigazione bidirezionale e verificare in browser con JavaScript disattivato, tastiera e viewport 360/768/1440 px.
4. Aggiungere un test automatico che controlli l'esistenza dei target locali e la presenza del collegamento di fallback.

## Limiti del controllo
Questa sessione ha effettuato letture GitHub e controlli strutturali; **nessun test su browser reale** o audit WCAG completo. Un tentativo di aggiornare la pagina interattiva è stato bloccato dal connettore, quindi **non dichiarare implementata la correzione**. Non aprire una PR di rilascio fino al completamento dell'intervento.

Nessun link affiliato, checkout, prezzo, dato personale, deploy o pagamento aggiunto.

## Aggiornamento del 20 ottobre 2026
Correzione applicata sul branch `vorli/catalog-navigation-fallback-fixed-20261020`: il catalogo interattivo ora collega la pagina statica nella navigazione visibile e nel blocco `noscript`; la pagina statica offre navigazione bidirezionale completa. Verificati mediante lettura GitHub: otto schede statiche, cinque sorgenti editoriali esistenti, link locali delle tre pagine Lab, `noindex` e assenza di checkout. Test reali in browser e audit WCAG ancora da eseguire. Nessuna modifica alla produzione.
