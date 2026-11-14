# VORLI Lab — audit strutturale matrice (14 novembre 2026)

> Documento di verifica per anteprima non pubblicata. Non è un'autorizzazione al rilascio.

## Ambito e metodo

Verificato il contenuto di `preview/vorli-next/matrice-scelta-tech-lab.html` sul branch `vorli/decision-matrix-qa-20261113`, tramite lettura dei file GitHub. I controlli sono stati **eseguiti in modo indipendente con analisi strutturale dei contenuti**, non tramite `python -m unittest` né CI.

## Risultati eseguiti

| Verifica | Esito |
| --- | --- |
| Otto intestazioni di categoria previste, nell'ordine corretto | PASS |
| Tre etichette per categoria (Priorità, Controllo critico, Fonte da consultare), 24 totali | PASS |
| Identificativi HTML senza duplicati | PASS |
| Sette destinazioni locali distinte dei link HTML esistenti sul branch | PASS |
| Meta robots `noindex,nofollow` presente | PASS |
| Nessun form, script, iframe, checkout o token Awin nel file matrice | PASS |
| Regola responsive `@media(max-width:700px)` presente | PASS (presenza codice, non resa visiva) |

Destinazioni verificate: `index.html`, `catalogo-lab.html`, `risorse-originali-lab.html`, `guida.html`, `guida-scelta-tech-lab.html`, `glossario-tech-lab.html`, `scheda-confronto-tech-lab.csv`.

**Limiti:** l'esistenza dei file non dimostra che tutti i collegamenti funzionino in un deploy HTTP. Non sono stati eseguiti i test Python, CI, Chromium, controlli di contrasto misurato, test con screen reader o su dispositivi reali. Nessuna verifica dello stato Awin.

## Gate per il rilascio (ancora aperti)

1. Eseguire `python -m unittest discover -s tests -p 'test_decision_matrix_lab.py' -v` e poi l'intera suite sul branch di integrazione.
2. Risolvere il blocco di sicurezza documentato nella PR #148 prima di qualsiasi merge/deploy.
3. Verificare rendering e navigazione da tastiera su viewport 320, 375, 768 e 1280 px; contrasto, zoom 200%, screen reader e stampa.
4. Verificare tutte le URL su un'anteprima isolata; controllare la sitemap e assicurare che il materiale Lab non sia indicizzato.
5. Rivedere contenuti, diritti delle immagini, compliance legale/fiscale e stato approvazioni advertiser prima di pubblicare prodotti reali.
6. Consolidare con attenzione le PR Lab dipendenti; non fare merge automatico in `main`.

## Confini commerciali

La matrice è un contenuto dimostrativo, non una scheda di vendita. Non aggiungere link affiliati prima dell'autorizzazione advertiser; non attivare checkout, prezzi o acquisti senza consenso esplicito, provider di pagamento e verifiche legali.

Nessuna modifica alla produzione, nessuna spesa e nessun nuovo account per questo audit.
