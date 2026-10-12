# VORLI — Piano catalogo reale e terzo agente AI

## Obiettivo
Sostituire gradualmente le schede dimostrative con offerte reali e verificabili, senza compromettere il sito pubblicato né mostrare come acquistabili prodotti o link non validati.

## Stato verificato
- Il ramo `main` contiene il nuovo design mobile-first.
- `data/products.json` contiene attualmente una sola scheda dimostrativa (`demo-001`) con URL `example.com`; non è un'offerta commerciale utilizzabile.
- Il progetto include già `agent/awin_importer.py`, `agent/build.py`, una dashboard e controlli di compliance. Prima di aggiungere nuove automazioni, verificare ciò che esiste.
- Le approvazioni dei network/inserzionisti possono essere ancora pendenti. Non presumere accesso a programmi, API o link affiliati finché non sono confermati.

## Ruoli dei tre agenti
1. **Creatore/Strategico** — priorità commerciali, categorie, pubblico, confronto delle opportunità e pianificazione.
2. **Monetizzatore** — verifica delle condizioni affiliate, commissioni e disponibilità dei link; segnala le offerte pronte per la pubblicazione. Non inventa link o commissioni.
3. **Graphic Designer professionista / Senior Web Developer** — responsabile della qualità visiva, UX mobile, accessibilità, prestazioni, HTML/CSS, validazione delle pagine e revisione tecnica. Mantiene il design coerente e lavora su un branch separato; non pubblica direttamente su `main`.

Gli agenti collaborano, ma non sono da considerare processi autonomi già installati o in esecuzione: i ruoli devono essere implementati nei flussi di lavoro e supervisionati.

## Regole di ammissione per ogni prodotto
Un prodotto può essere promosso da candidato a pubblicabile solo quando sono documentati:
- nome e modello esatti;
- categoria pertinente (tecnologia, elettrodomestici, accessori, sport con tecnologia);
- prezzo e valuta con fonte e data di verifica, oppure prezzo omesso se non verificabile;
- descrizione e specifiche provenienti da fonti attendibili;
- venditore/network e stato dell'approvazione;
- URL di destinazione reale e funzionante, con link affiliato soltanto se autorizzato;
- disclosure affiliate e conformità alle condizioni del network;
- assenza di duplicati e dati inventati.

Le commissioni, le valutazioni e le recensioni non devono essere stimate o fabricate. Un link di esempio come `example.com` non deve essere presentato come offerta reale.

## Sequenza di lavoro proposta
1. **Audit tecnico**: leggere catalogo, importer Awin, generatore del sito, dashboard e regole di compliance; verificare schema dati e test esistenti.
2. **Separazione demo/reale**: introdurre uno stato esplicito della scheda (ad esempio `demo`, `candidate`, `approved`) e impedire che schede non approvate siano presentate come offerte reali.
3. **Fonti e selezione**: creare un registro delle fonti e una lista di candidati per categoria. Nessun candidato diventa offerta finché prezzo, destinazione e autorizzazione non sono verificati.
4. **UX/catalogo**: il terzo agente verifica etichette demo, filtri, layout mobile, accessibilità e chiarezza dei pulsanti; nessun CTA deve implicare un acquisto disponibile se il link non è valido.
5. **Validazione**: eseguire build e controlli sui dati; provare link e disclosure; esaminare il diff e richiedere revisione umana.
6. **Pubblicazione**: proporre le modifiche tramite pull request. Non unire automaticamente in `main` e non modificare segreti, account o impostazioni di pagamento.

## Criteri minimi di completamento
- Nessuna scheda demo scambiata per prodotto reale.
- Ogni offerta pubblicata ha fonte, data di controllo e destinazione verificata.
- Link non validi o non autorizzati bloccati o chiaramente disabilitati.
- Il sito mobile resta leggibile e navigabile.
- Build/test passano e una persona approva la pull request prima della pubblicazione.

## Limiti e sicurezza
- Non salvare password, token o chiavi API nel repository.
- Non acquistare servizi, non attivare account e non effettuare pagamenti.
- Non dichiarare vendite o guadagni prima che esistano dati reali.
- Le API dei network vanno usate soltanto con accesso autorizzato e nel rispetto dei relativi termini.
