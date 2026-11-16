# VORLI — Piano tecnico di pre-lancio 24 ore

Aggiornato: 2026-11-06  
Stato: preparazione; nessuna vendita o offerta affiliata è attiva.

## Obiettivo del rilascio iniziale

Rilasciare una prima versione pubblica di VORLI con:
- una sola offerta digitale diretta, Casa Smart senza sorprese, solo dopo revisione e checkout verificato;
- catalogo affiliate limitato a offerte effettivamente approvate e tracciate;
- nessuna scheda demo presentata come acquistabile;
- sito mobile-first, contatti e informative essenziali, disclosure visibile;
- percorso di acquisto testato dall'apertura pagina fino alla consegna del file.

## Stato tecnico verificato il 2026-11-06

- Preparata fuori dal repository una nuova bozza commerciale 0.1 di 14 pagine A4, in PDF e DOCX. È un avanzamento editoriale, non un file finale: non è tagged/accessibile certificato e richiede revisione tecnica indipendente, controllo fonti, diritti e correzione editoriale. Il file commerciale non è stato caricato nel repository pubblico.

- Repository: `riccardomontanaroact-hub/affiliate-autopilot`, branch predefinito `main`, pubblico.
- `data/products.json` è vuoto: non esistono offerte affiliate pubblicabili.
- `site/index.html` contiene ancora `noindex,nofollow`, presenta il catalogo come demo e non è una homepage di vendita.
- `data/config.json` contiene una disclosure affiliate generica anche se il catalogo è vuoto; il testo va mostrato solo quando esistono link affiliati effettivi e va rivisto per chiarezza.
- Il generatore `agent/build.py` pubblica le pagine di `preview/vorli-next`, quindi le modifiche alla sola cartella `site` possono essere sovrascritte alla build. La sorgente corretta del sito va modificata in preview e poi ricostruita.
- I cinque agenti in `agent/agents.py` sono controlli deterministici sul repository; non accedono a Payhip, Awin, Amazon, account, pagamenti o partner.
- Le PR #74, #75 e #76 sono ancora draft e non unite.
- Nessun account checkout è collegato e nessun acquisto/consegna è stato testato.

## Piano operativo entro 24 ore

### Blocco A — Prodotto digitale
1. Completare la nuova edizione commerciale, distinta dalla bozza pubblica.
2. Revisione tecnica indipendente: affermazioni su Wi-Fi, Matter, privacy, aggiornamenti e sicurezza; rimuovere o qualificare ogni consiglio non verificato.
3. Verificare tutti i link e registrare data di consultazione.
4. Controllare diritti, originalità, copertina, leggibilità mobile e accessibilità/tag PDF.
5. Definire prezzo, identità e condizioni del venditore, assistenza, rimborsi e trattamento dei dati.
6. Configurare la piattaforma scelta, collegare un metodo di pagamento del titolare e caricare il file finale.
7. Eseguire un test reale autorizzato del checkout e del download; controllare ricevuta, e-mail, accesso al file e rimborsi.

### Blocco B — Sito
1. Preparare una landing page VORLI con descrizione chiara del prodotto e prezzo approvato.
2. Aggiungere pagine di contatto, privacy, cookie/strumenti di tracciamento se presenti, termini e informazioni precontrattuali.
3. Aggiungere disclosure affiliate solo in prossimità delle offerte affiliate e nella pagina informativa.
4. Mantenere `noindex` fino a quando pagine, condizioni e checkout non sono pronti; rimuoverlo solo con approvazione al rilascio.
5. Ricostruire con `python agent/build.py`, eseguire `python -m unittest discover -s tests` e controllare l'output generato.
6. Verificare GitHub Actions, artifact e sito Pages dopo un deploy autorizzato.

### Blocco C — Affiliazioni
1. Verificare nel pannello Awin lo stato effettivo di VORLI e di ALLPOWERS IT.
2. Usare solo link generati dall'account approvato e secondo i termini del singolo advertiser.
3. Verificare prodotto, prezzo, disponibilità, condizioni e link nel giorno di pubblicazione.
4. Inserire nel catalogo solo dopo approvazione e controllo manuale; non simulare ordini.
5. Valutare Amazon.it solo dopo aver verificato ammissione, canali registrati, requisiti e disclosure.

## Gate che impediscono il rilascio

- [ ] Edizione commerciale revisionata e distinta dal materiale pubblico.
- [ ] Fonti, link, diritti e affermazioni tecniche verificati.
- [ ] PDF accessibile e leggibile su mobile e desktop.
- [ ] Prezzo e condizioni approvati dal titolare.
- [ ] Idoneità del venditore e obblighi fiscali verificati con professionista competente.
- [ ] Account checkout creato dal titolare e metodo di pagamento collegato.
- [ ] Checkout e consegna digitale testati realmente.
- [ ] Pagine informative e disclosure complete.
- [ ] Build e test automatici superati.
- [ ] Deploy Pages verificato.
- [ ] Approvazione finale del titolare.

## Dipendenze esterne non automatizzabili da questo repository

La creazione e verifica di account, il collegamento di Stripe/PayPal, la verifica dell'identità, l'accettazione di condizioni contrattuali, la valutazione fiscale, l'approvazione Awin/Amazon e l'esecuzione di pagamenti richiedono il titolare e i rispettivi provider. Non dichiarare completati questi passaggi sulla base di una pagina pubblica o di un redirect.

## Decisione di rilascio

La scadenza di 24 ore è un obiettivo operativo, non una garanzia: se uno dei gate sopra resta aperto, VORLI può essere presentato come sito in pre-lancio, ma non come negozio con checkout funzionante o prodotti acquistabili.
