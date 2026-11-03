# VORLI Lab — matrice di verifica pre-rilascio (3 novembre 2026)

> **Documento di lavoro, non autorizzazione al deploy.** La produzione e il branch `main` non devono essere modificati. Le verifiche non eseguite sono esplicitamente **DA FARE**, non superate.

## Inventario verificato nel branch di partenza

- Guida editoriale: `preview/vorli-next/guida-scelta-tech-lab.html`, otto checklist con tre criteri ciascuna.
- Scheda CSV: `preview/vorli-next/scheda-confronto-tech-lab.csv`, descritta nella documentazione del 2 novembre come 24 criteri, da verificare nuovamente sul commit candidato.
- La guida ha `noindex,nofollow`, non mostra offerte né checkout e contiene un collegamento relativo al CSV.
- La guida dichiara l'aggiornamento al 31 ottobre: aggiornare solo dopo revisione effettiva.

## Gate di rilascio — tutti obbligatori

| Area | Prova richiesta | Stato al 3 novembre |
| --- | --- | --- |
| Sicurezza | Risolvere esposizioni documentate nella PR #148, inclusa cronologia e credenziali eventualmente coinvolte, con procedura approvata | **BLOCCANTE / DA FARE** |
| Responsività | Screenshot e ispezione manuale a 320, 360, 768, 1440 px, zoom 200% e 400%; verificare niente contenuti tagliati | **DA FARE** |
| Accessibilità | Tastiera completa, focus visibile, screen reader, contrasto WCAG 2.2, nomi dei link e landmark | **DA FARE** |
| Stampa | Anteprima A4, stampa reale in scala di grigi, sezioni non troncate, link/URL utili | **DA FARE** |
| CSV | Conteggio righe, encoding UTF-8, intestazioni, assenza di formule, apertura in foglio di calcolo senza macro | **DA FARE** |
| Link | Risoluzione di tutti gli href locali nel build candidato; controlli di redirect e link esterni solo se autorizzati | **DA FARE** |
| SEO | Canonical, robots e sitemap coerenti con ambiente Lab; non indicizzare prototipi | **DA FARE** |
| Contenuti | Revisione editoriale e controllo delle affermazioni tecniche con fonti ufficiali datate | **DA FARE** |
| Immagini | Registro origine, licenza, attribuzione, alt e dimensioni; nessuna immagine non autorizzata | **DA FARE** |
| Affiliati | Conferma individuale dell'approvazione di ciascun advertiser e dei termini applicabili | **NON VERIFICATO** |
| Vendite | Approvazione esplicita, provider di pagamento e verifiche legali/fiscali prima di prezzi o checkout | **NON AUTORIZZATO** |

## Procedura riproducibile sul branch candidato

```sh
python -m unittest discover -s tests -v
node --test tests/catalog-progressive.test.cjs
python -m compileall -q agent tests
python tests/browser_catalog_lab.py
```

Registrare per ogni comando: commit SHA, data, ambiente, exit code e log CI. Non riutilizzare come prova test di commit precedenti. Eseguire una revisione visiva degli screenshot oltre ai test automatici.

## Politica contenuti e monetizzazione

- Otto categorie **demo** e bozze digitali originali restano distinte da offerte commerciali.
- Non pubblicare link Awin finché non sono verificati autorizzazione e condizioni del programma. Non assumere che le quattro candidature storiche siano ancora in attesa o approvate.
- Non creare account, non usare dati personali, non inviare spam, non sostenere spese.
- Non integrare questa PR in `main` e non pubblicare la preview senza sblocco esplicito dei gate.
