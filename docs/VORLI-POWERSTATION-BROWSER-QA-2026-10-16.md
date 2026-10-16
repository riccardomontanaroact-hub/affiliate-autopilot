# VORLI — QA browser del calcolatore power station (16 ottobre 2026)

Stato: bozza, non pubblicare in produzione.

## Test eseguiti in Chromium headless

Sono stati verificati nove scenari sul codice JavaScript del calcolatore, inserito in una pagina HTML locale con gli stessi ID dei campi della bozza GitHub: risultato predefinito 6,14 ore; carico superiore alla potenza massima bloccato; carico uguale alla potenza massima ammesso; potenza non indicata con avviso; consumo zero rifiutato; rendimento 101% rifiutato; riserva 100% rifiutata; potenza negativa rifiutata; risultato precedente nascosto dopo input invalido. Tutti i nove scenari sono passati e non sono emersi errori JavaScript nel browser.

## Limiti

La pagina usata per il test era una ricostruzione locale degli input e dello script letti nel file del branch; non un checkout integrale del documento HTML del repository. Restano da eseguire il test sul file HTML originale, controlli responsive, accessibilità, verifica degli URL delle fonti e revisione umana. Non considerare questo collaudo un'autorizzazione alla pubblicazione.

Nessun dato personale, identificativo affiliato o link di tracciamento incluso. Nessuna vendita, pagamento, spesa o modifica al sito pubblico.
