# VORLI Lab — ricerca resistente a trattini e barre (30 ottobre 2026)

## Problema verificato nel codice
Il filtro del catalogo cercava i termini come sottostringhe, normalizzando accenti e spazi ma non separatori. Una ricerca per `power-station` non corrispondeva al testo editoriale `Power station`; `USB/C` e `Wi‑Fi` con trattino Unicode potevano produrre risultati inattesi.

## Intervento limitato al laboratorio
- `preview/vorli-next/catalogo-lab.js`: normalizza trattini ASCII/Unicode, slash e underscore in spazi, sia nei testi indicizzati sia nelle ricerche; mantiene la ricerca multi-parola in qualsiasi ordine e il fallback senza JavaScript.
- `catalogo-lab.html`: il testo d'aiuto accessibile dichiara il supporto a trattini e barre.
- `tests/browser_catalog_lab.py`: nuovi casi su pagina completa Chromium per `power-station` (1 categoria + 1 bozza), `USB/C` (2 categorie + 1 bozza) e `Wi‑Fi` con trattino non separabile (1 categoria, 0 bozze), in tutte e quattro le larghezze già testate.
- `tests/test_catalogo_lab.py` e `tests/catalog-progressive.test.cjs`: regressioni statiche per aiuto e normalizzazione.

## Controlli richiesti prima di approvare
```sh
python -m unittest discover -s tests -v
node --test tests/catalog-progressive.test.cjs
python tests/browser_catalog_lab.py
```
Verificare gli esiti del workflow GitHub Actions sulla PR; un commit riuscito **non** prova che la CI sia passata. Riesaminare screenshot e navigazione con tastiera; restano esclusi screen reader reali e audit WCAG completo.

## Perimetro e sicurezza
Solo anteprima Lab `noindex,nofollow`. Otto categorie demo e cinque sorgenti editoriali in bozza: nessun prodotto acquistabile. Nessuna nuova offerta, link affiliato, prezzo, checkout, tracciamento, account, spesa, dato personale, merge, deploy o modifica a `site/`. Stato individuale Awin non deducibile dal repository; autorizzazioni e verifiche commerciali/fiscali restano obbligatorie prima della pubblicazione.
