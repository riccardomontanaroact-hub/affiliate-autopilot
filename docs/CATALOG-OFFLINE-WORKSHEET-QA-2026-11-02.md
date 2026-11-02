# VORLI Lab — scheda di confronto offline e stampa (2 novembre 2026)

## Contenuto originale proposto

- `preview/vorli-next/scheda-confronto-tech-lab.csv`: modello CSV leggero, senza macro, tracciamenti, prezzi o campi compilati. Otto categorie e **24 criteri** estratti dalla guida editoriale esistente, con colonne vuote per due opzioni, fonte ufficiale e note.
- `preview/vorli-next/guida-scelta-tech-lab.html`: link di download locale e spiegazione esplicita della natura **non commerciale** del modello.
- `preview/vorli-next/catalogo-lab.css`: impaginazione di stampa chiara, a basso consumo di inchiostro, senza navigazione decorativa, con sezioni che evitano spezzature.
- `tests/test_catalogo_lab.py`: confronto riga per riga tra CSV e checklist HTML; intestazioni, campi vuoti, assenza di formule e link esterni.
- `tests/browser_catalog_lab.py`: smoke test del collegamento CSV e dei CSS di stampa in Chromium su 320/360/768/1440 px.

Il nuovo CSV è **un modello editoriale Lab separato** dalle cinque bozze precedentemente registrate: non modificare i contatori 8 categorie / 5 sorgenti verificate, né trattarlo come prodotto in vendita. Non richiede dati personali e può essere compilato localmente dall'utente.

## Comandi di verifica

```sh
python -m unittest discover -s tests -v
node --test tests/catalog-progressive.test.cjs
python -m compileall -q agent tests
python tests/browser_catalog_lab.py
```

La CI deve essere verificata sul commit della PR. Gli screenshot e i test automatici non sostituiscono l'ispezione visiva, le prove di stampa reale, screen reader, audit WCAG 2.2 o verifica legale.

## Blocco di pubblicazione

**Nessun merge/deploy.** Il branch rimane Lab, con pagine `noindex,nofollow` e senza sitemap pubblica. Non sono aggiunti checkout, offerte, link affiliati, prezzi, analytics, immagini esterne, account o spese.

**Gate di sicurezza già noto:** PR #148 segnala dati di contatto/identificativi pubblicati in altre parti del repository e nella cronologia; il lavoro su questo branch non li bonifica. Prima di qualsiasi rilascio pubblico occorre risolvere il rischio separatamente e ottenere approvazioni editoriali/commerciali e verifiche legali/fiscali.
