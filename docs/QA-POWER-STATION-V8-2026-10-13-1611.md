# Power Station QA — 13 ottobre 2026, ore 16:11 Europe/Rome

**Stato: BOZZA. Non pubblicare né vendere.**

Sorgente verificata: `drafts/power-station-autonomia-offline-2026-10-13.html` (blob `532a9e01c7ef9979bc9a27da87e1c1395693b285`).

## Test eseguiti
JavaScript originale estratto dall'HTML ed eseguito in un isolato **V8 con DOM simulato**: **19/19 casi passati**. Casi: campi vuoti; formula Wh/W; fattore 80%; potenza sotto/sopra/uguale al limite; carico variabile; capacità negativa; potenza zero; fattore >100, <0 e 100%; limite negativo; decimali; overflow; ricalcolo; reset; capacità minima positiva; valore non numerico.

**4/4 controlli statici passati:** `noindex,nofollow`, CSS stampa, avviso bozza, nessun pattern evidente di fetch/XHR/iframe/script esterno. Il controllo statico non prova l'assenza assoluta di rete.

**NON eseguiti:** suite Node presente nel repository, browser reale, smartphone, stampa PDF, screen reader, prove su power station fisiche. Nessuna certificazione di sicurezza o autonomia garantita.

## Contenuti commerciali e SEO (solo preparazione)
- Articolo: «Wh e W: differenze e calcolo dell'autonomia», con formula e ipotesi.
- Guida: «Perché i carichi variabili alterano le stime», con avvisi su spunto e inverter.
- Checklist: «Limiti AC/DC, compatibilità, temperatura e manuale da verificare».
- Eventuali future affiliazioni vanno dichiarate chiaramente; **nessun link affiliato inserito**.
- Prima della vendita di contenuti digitali: controllare obblighi precontrattuali, recesso, IVA e posizione del venditore italiano.

## Fonti consultate il 13 ottobre 2026
- Awin, scheda eWeki IT: elettronica di consumo, cookie pubblicizzato 30 giorni; **nessuna commissione o approvazione verificata**: https://ui.awin.com/merchant-profile/19988
- Your Europe, vendita B2C e contenuti digitali: https://europa.eu/youreurope/business/selling-in-eu/selling-goods-services/ecommerce-distance-selling/index_it.htm
- AGCM, trasparenza pubblicitaria: https://agcm.it/media/comunicati-stampa/2025/6/PS12814-PS12815-PS12816-PS12817-PS12818-PS12826

Nessun deploy, pagamento, account o comunicazione effettuati.

## Aggiornamento QA — 14 ottobre 2026, ore 02:13 (Europe/Rome)

Corretto nel branch il formatter delle autonomie positive inferiori a 0,01 ore: ora mostra «meno di 0,01 ore» anziché «0 ore». Le formule e gli avvisi restano invariati. Il JavaScript aggiornato, recuperato dal repository, ha superato **8/8** verifiche in un isolato V8 con DOM simulato: durata teorica breve, durata corretta breve, caso normale, soglia esatta, limite di potenza, capacità negativa, fattore non valido e input mancante. **Non verificati** browser reale, smartphone, stampa PDF e apparecchi fisici. Non pubblicare o vendere prima della revisione completa.
