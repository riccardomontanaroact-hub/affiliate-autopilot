# VORLI — Piano di preparazione alla vendita

## Stato verificato
Il sito è attualmente un catalogo statico di affiliazione, non un negozio con checkout. `data/products.json` contiene un prodotto dimostrativo con URL example.com. Non pubblicare prezzi, disponibilità, recensioni o commissioni inventate.

## Modalità operative
1. **Affiliazione**: mostrare solo prodotti e link autorizzati dai programmi approvati; acquisto e pagamento sul sito del commerciante.
2. **Vendita diretta**: attivare il pulsante “Acquista” solo dopo la configurazione verificata di venditore, fornitore, gestione ordini, resi, fiscalità, privacy, termini di vendita e provider di pagamento. Mai raccogliere numeri di carta nel repository o in HTML statico.

## Lavori tecnici prioritari
- Filtrare dal catalogo pubblico prodotti `demo-*`, URL `example.com`, link mancanti e offerte non verificate.
- Gestire uno stato esplicito per ogni prodotto: `draft`, `verified_affiliate`, `verified_direct`.
- Validare campi obbligatori, prezzi non negativi, URL HTTPS, date di verifica e provenienza di ogni offerta prima del build.
- Mostrare pulsanti diversi: “Vai al negozio” per affiliazione; “Acquista” solo con checkout reale approvato.
- Aggiungere pagine di contatto, privacy, cookie ove necessari, disclosure affiliazioni, termini, spedizioni e resi secondo il modello commerciale.
- Automatizzare i build con GitHub Actions, controlli qualità e notifiche degli errori; non effettuare pubblicazioni di offerte non verificate.
- Evitare dashboard interne e dati sensibili pubblicati su GitHub Pages.

## Dati e autorizzazioni ancora necessari
- Conferma dell'accettazione Awin e autorizzazione ai singoli inserzionisti.
- Per vendite dirette: soggetto venditore, tipologia di prodotti (fisici/digitali), fornitore, disponibilità, spedizioni, resi e provider checkout.
- Credenziali API soltanto tramite secrets del provider CI/hosting, mai in file pubblici.

## Regole per un agente AI
- Non inventare prezzi, disponibilità, recensioni, sconti o commissioni.
- Non attivare link commerciali o checkout senza conferma delle autorizzazioni.
- Preparare modifiche in branch e pull request con controlli automatici.
- Conservare un log delle fonti, date di aggiornamento e risultati di validazione.
- In caso di errore API, non pubblicare dati vecchi come offerte correnti.
