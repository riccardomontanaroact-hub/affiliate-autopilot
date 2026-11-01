# VORLI Lab — risorse originali: accessibilità e trasparenza (1 novembre 2026)

## Modifiche verificabili

- `preview/vorli-next/risorse-originali-lab.html`: i cinque collegamenti GitHub alle bozze hanno nomi accessibili univoci con titolo della risorsa e avviso «nuova scheda». Il simbolo grafico è nascosto agli screen reader.
- Aggiunta navigazione verso `guida-scelta-tech-lab.html` per raggiungere le otto checklist editoriali.
- Eliminati la data di verifica congelata nel layout e il testo che presumeva uno stato di approvazione Awin. Lo stato delle candidature cambia indipendentemente dal sito e va letto dalle fonti autorizzate.
- Confermata distinzione visibile tra **bozze**, **categorie demo** e **offerte assenti**. Nessun prodotto dichiarato acquistabile.

## Controllo sorgenti, 1 novembre 2026

I cinque percorsi già registrati sono stati letti nuovamente tramite repository GitHub: kit USB-C, Casa Smart Sicura, scheda Power Station, workbook elettrodomestici EPREL e checklist HTML Casa Smart. Le risposte contengono i sorgenti testuali; la presenza non implica approvazione editoriale, pubblicazione commerciale o diritti su contenuti di terzi.

## Regressioni aggiunte

- `tests/test_catalogo_lab.py`: controllo cinque link, nomi accessibili, `noindex`, link locali e assenza di dichiarazioni Awin congelate.
- `tests/catalog-progressive.test.cjs`: verifica indipendente delle cinque destinazioni rispetto al registro locale e dei titoli leggibili.
- `tests/browser_catalog_lab.py`: nuova verifica della pagina risorse a 320/360/768/1440 px, navigazione da tastiera, nomi accessibili, link locali, assenza di overflow e richieste remote; screenshot a 360 e 1440 px.

## Esecuzione e limiti

```sh
python -m unittest discover -s tests -v
node --test tests/catalog-progressive.test.cjs
python -m compileall -q agent tests
python tests/browser_catalog_lab.py
```

La CI della PR deve essere controllata sul commit corrente prima di considerare superati i test. Test automatici e screenshot non sostituiscono revisione visiva, screen reader, audit WCAG 2.2, test su smartphone fisici e revisione editoriale.

**Isolamento:** solo `preview/vorli-next/`, `tests/` e documentazione. Non modificare `site/`, non fare merge o deploy automatici. Nessun checkout, link affiliato, prezzo, tracciamento, dati personali, account o spesa. I contenuti Lab restano `noindex,nofollow`; non inserirli in una sitemap pubblica.
