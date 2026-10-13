# VORLI — Casa Smart v0.3: rapporto tecnico e piano commerciale
Data: 13 ottobre 2026, ore 07:13 (Europe/Rome). Stato: documentazione interna; nessuna pubblicazione.

## QA svolto
La v0.2 (branch `vorli/product-casa-smart-checklist-20261013-0510`) richiede erroneamente l'abbonamento annuo per il calcolo. Ho preparato in memoria una modifica v0.3 che aggiunge accessori iniziali e abbonamento mensile facoltativi, rende facoltativo il canone annuo e mantiene il prezzo iniziale obbligatorio, zero ammesso. Formula su 36 mesi: prezzo + accessori + 36×mensile + 3×annuo. Avvertenza sul doppio conteggio mensile/annuo. Costi energia, imposte, riparazioni e aumenti non inclusi.

Lo script v0.3 è stato validato sintatticamente e sono stati verificati quattro vettori aritmetici:
- 100, 0, 0, 0 → 100 euro
- 100, 20, 5, 10 → 330 euro
- 0, 0, 0, 0 → 0 euro
- 249,99, 29,90, 3,99, 0 → 423,53 euro

I controlli statici hanno rilevato campi, formula, banner BOZZA e regole di stampa. Nessun uso di fetch, XMLHttpRequest, localStorage, iframe o risorse script esterne nella bozza in memoria. **Non sono stati eseguiti test reali in browser, su mobile, stampa PDF o screen reader.**

## Ostacolo GitHub
La creazione del file HTML v0.3 nel branch separato è stata bloccata dai controlli del connettore. Nessun commit HTML riuscito e nessuna modifica al sito pubblico. La versione 0.3 non è disponibile nel repository come file HTML. Non dichiararla implementata o pronta.

## Scheda commerciale (bozza)
**Casa Smart senza sorprese**: checklist offline per verificare compatibilità, privacy, aggiornamenti, garanzia e costi indicativi di un dispositivo smart su tre anni. Non certifica sicurezza o conformità. Prezzo e checkout non stabiliti; nessun link affiliato attivato.

## SEO organico non-spam
Articolo futuro: «Presa smart: il costo reale in tre anni». Struttura: requisiti Wi-Fi e hub, aggiornamenti, privacy, abbonamenti, esempio ipotetico, checklist. Evitare recensioni inventate, claim di risparmio e link affiliati senza autorizzazione. Pubblicare solo dopo revisione.

## Fonti consultate il 13 ottobre 2026
- Scheda pubblica Awin eWeki IT (advertiser 19988): elettronica di consumo e cookie 30 giorni. Non attesta approvazione VORLI né commissioni effettive. https://ui.awin.com/merchant-profile/19988
- Commissione europea, Cyber Resilience Act: segnalazioni dal 11 settembre 2026; principali obblighi dal 11 dicembre 2027. https://digital-strategy.ec.europa.eu/en/policies/cra-summary

## Prima della vendita
Verificare i requisiti fiscali italiani e IVA, diritto dei consumatori per contenuti digitali, accessibilità e qualità del prodotto. Nessuna spesa, candidatura, email, account, pagamento o pubblicazione.
