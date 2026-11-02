# VORLI Lab — messaggi commerciali e guida alla ricerca (29 ottobre 2026)

## Problema osservato
La pagina Lab del 28 ottobre riportava che ACEMAGIC, eWeki IT, 2GO Software IT e ALLPOWERS IT non erano considerati approvati. Una frase statica sulle approvazioni può diventare falsa senza modifiche al catalogo, perché lo stato delle candidature cambia fuori dal repository. In parallelo, la ricerca supportava più parole in qualsiasi ordine, ma l'interfaccia non lo spiegava.

## Modifiche
- In `preview/vorli-next/catalogo-lab.html` il riquadro di trasparenza **non presume né nega** lo stato attuale dei singoli programmi Awin. Indica che anche una futura approvazione non autorizza automaticamente la pubblicazione di offerte: sono necessari verifica dei termini individuali, conformità e autorizzazione alla pubblicazione.
- Aggiunta una spiegazione visibile della ricerca multi-parola collegata al campo tramite `aria-describedby`.
- In `catalogo-lab.css` la guida usa un testo leggibile su mobile, coerente con la palette blu notte.
- In `tests/test_catalogo_lab.py` aggiunte due regressioni per testo commerciale e associazione accessibile della guida.

## Ambito e sicurezza
Solo anteprima Lab `noindex,nofollow`. Otto categorie demo e cinque link a sorgenti editoriali in bozza; nessun prodotto acquistabile. Nessuna nuova offerta, link affiliato, checkout, prezzo, account, dato personale, tracciamento, spesa, invio email, modifica a `site/`, merge o deploy.

## Verifiche
Modifiche puntuali applicate dopo lettura dei file del branch `vorli/catalog-editorial-sync-qa-20261028`. La creazione dei commit non prova il superamento dei test: eseguire `python -m unittest discover -s tests -v`, `node --test tests/catalog-progressive.test.cjs` e `python tests/browser_catalog_lab.py` sul nuovo branch; verificare risultati GitHub Actions, screenshot e accessibilità con screen reader. La nuova PR resta in bozza e non va integrata automaticamente.

## Prima della produzione
Verificare individualmente nel pannello Awin eventuali approvazioni e condizioni del programma, diritti dei contenuti, disclosure, cookie/privacy, aspetti fiscali e di recesso per vendite dirette. L'approvazione di un advertiser non equivale a un checkout autorizzato.
