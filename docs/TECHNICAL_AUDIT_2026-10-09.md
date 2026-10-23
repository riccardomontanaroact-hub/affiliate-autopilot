# VORLI — Audit tecnico iniziale
Data: 2026-10-09

## Ambito
Lettura dei file su `main`: `agent/awin_importer.py`, `agent/build.py`, `agent/content_engine.py`, `data/products.json`, `.github/workflows/build.yml` e README. È un audit iniziale statico, non una suite completa di test né una verifica di sicurezza professionale.

## Risultati

### 1. Importatore Awin — non implementato
`agent/awin_importer.py` stampa che è in attesa dell'approvazione Awin e che non modifica prodotti. Non è collegato a un flusso API o feed reale. Prima dell'implementazione servono approvazione, documentazione tecnica, credenziali conservate in GitHub Secrets e test con dati autorizzati.

### 2. Catalogo — solo demo
`data/products.json` contiene una sola scheda demo, con merchant `INSERISCI NETWORK` e URL `https://example.com/`. Prezzo, commissione, valutazione e pro/contro sono dimostrativi e non devono essere interpretati come dati commerciali verificati. Non aggiungere offerte reali senza fonte, data di verifica e link autorizzato.

### 3. Generatore sito — protezione delle offerte demo
`agent/build.py` riconosce le offerte demo e non mostra loro un pulsante d'acquisto. Questo comportamento va mantenuto. Il punteggio usa campi commissione, rating, prezzo e pro; finché sono dati demo, il ranking non è una valutazione commerciale significativa.

### 4. Motore contenuti — template semplice
`agent/content_engine.py` stampa contenuti derivati direttamente dai campi del catalogo; non effettua ricerca, verifica delle fonti o controlli indipendenti. Ogni contenuto commerciale futuro richiede fonti verificate, revisione e disclosure appropriate.

### 5. GitHub Actions — rischio di pubblicazione da branch di lavoro
Il workflow è attivato da ogni push e contiene un job di deploy Pages senza condizione sul branch. I log più recenti indicano fallimento del deploy dopo build riuscito; le regole di protezione dell'ambiente possono impedire il deploy da branch diversi da `main`. È stata aperta la PR #10 per limitare il deploy a `main`; la modifica non è ancora unita né verificata in produzione.

Il job build contiene inoltre un passaggio che esegue `git push` dopo la rigenerazione. Prima di ampliare le automazioni, va verificato che il token e le regole di branch protection permettano solo scritture previste e che una build di PR non alteri involontariamente dati o file.

### 6. App e agenti
Le richieste di modifica per logo, coordinatore e catalogo sono bozze documentali/codice, non prove di app o agenti autonomi in esecuzione. Il progetto di app resta una specifica, non un'app pubblicata.

## Ordine di lavoro consigliato
1. Rivedere e unire in modo controllato la correzione del deploy solo da `main`; verificare una nuova esecuzione dopo il merge.
2. Portare il logo nel sorgente effettivo usato da `agent/build.py` (cartella `preview/vorli-next`) e testare mobile/desktop, perché il build copia quei file in `site/`.
3. Aggiungere test automatici per schema e validazione catalogo, blocco di link demo e output del generatore.
4. Implementare Awin solo dopo approvazione e disponibilità documentata di feed/API; mai committare token.
5. Importare prodotti con fonti e data di verifica, quindi revisionare pagine e disclosure.
6. Procedere con roadmap app e promozione esterna, senza contatti o spese automatiche fino all'approvazione.

## Fuori ambito
Non sono state create credenziali, effettuate spese, contattate reti o aziende, pubblicati banner o attivati agenti autonomi.
