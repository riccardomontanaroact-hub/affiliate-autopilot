# VORLI Lab — calcolatore energetico PC (bozza tecnica)

**Revisione:** 15 ottobre 2026, 02:15 CEST. **Stato:** esclusivamente branch di sviluppo; non pubblicare, non vendere, non unire in `main` senza revisione esplicita.

## Obiettivo
Calcolatore locale e offline per stimare consumo annuale di un computer e costo totale di tre anni. Nessuna telemetria, pagamento, iscrizione, prezzo di mercato, promessa di risparmio o link affiliato.

## Formule e ipotesi
- Consumo annuo (kWh) = (W attivi × ore attive/giorno + W standby × ore standby/giorno) × giorni di utilizzo / 1000.
- Spesa energetica annua (€) = consumo annuo × tariffa inserita dall'utente (€/kWh).
- Costo complessivo su tre anni (€) = acquisto + tre volte la spesa annua + manutenzione triennale.
- Ore attive e standby sono disgiunte; tariffa e utilizzo rimangono costanti; giorni esclusi non generano consumo nel modello. Watt da misurare alla presa, non ricavare dalla potenza nominale dell'alimentatore.
- Tutti i valori iniziali sono **esempi ipotetici**, non dati correnti o misure reali.

## QA
Il pacchetto di sviluppo originario, preparato il 15/10/2026, ha superato **10 test Python e 10 test JavaScript** in esecuzione locale il 15/10/2026. Questo dato riguarda la versione archiviata, non costituisce verifica automatica del codice GitHub finché tutti i file non sono stati trasferiti e ritestati. Mancano test visivi e di accessibilità su dispositivi reali.

## Fonti e opportunità commerciali (consultate il 15/10/2026)
- eWeki IT — elettronica di consumo, programma Awin 19988, cookie pubblicizzato di 30 giorni: https://ui.awin.com/merchant-profile/19988. Commissione per VORLI e approvazione **non verificate**.
- EASA — indicazioni di sicurezza per batterie al litio e power bank: https://www.easa.europa.eu/en/light/topics/lithium-batteries-aviation-powering-future-and-managing-risks (pubblicato 01/07/2025, aggiornato 22/07/2025). Non generalizzare la trasportabilità delle power station in aereo.

## Prima di ogni pubblicazione
Verificare gli stati contrattuali direttamente nella dashboard Awin, i diritti del consumatore e la disclosure commerciale; verificare il comportamento mobile, accessibilità e arrotondamenti. Nessun merge/deploy/pagamento automatico. Nessuna informazione personale nel repository pubblico.

## SEO editoriale non-spam
Un'unica pagina utile: “Quanto consuma un PC acceso quattro ore al giorno?” con calcolo replicabile, limiti e FAQ. Nessuna pagina massiva generata per varianti quasi identiche; nessun prezzo o sconto non verificato.
