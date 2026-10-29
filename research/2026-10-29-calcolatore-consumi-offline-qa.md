# Preflight VORLI — Calcolatore offline consumi elettrici
**Verifica e fonti:** 29 ottobre 2026. **Stato:** prototipo originale, non venduto né distribuito in produzione.

## Obiettivo
Trasformare il modello testuale di monitoraggio consumi in uno strumento realmente utilizzabile offline, senza dipendenze esterne, raccolta dati o pagamenti. Non è una simulazione della bolletta.

## Formule e casi di test riproducibili
- Energia annua = (potenza media W / 1000) × ore al giorno × giorni all'anno.
- Spesa variabile annua = energia annua × prezzo €/kWh **fornito dall'utente**.
- Spesa media mensile = spesa annua / 12 (media aritmetica, non bolletta mensile).
- Test A: 100 W, 8 h, 365 giorni, 0,25 €/kWh => 292 kWh/anno, 73 €/anno, 6,08 €/mese (arrotondato).
- Test B: 50 W, 4 h, 200 giorni, 0,25 €/kWh => 40 kWh/anno, 10 €/anno, 0,83 €/mese (arrotondato).
- Test C: prezzo scritto con virgola 0,25 accettato; prezzo vuoto, negativo, testo o oltre 10 rifiutato.
- Test D: ore > 24, giorni > 366, giorni frazionari, watt non numerici rifiutati.
- Test E: un dispositivo vuoto viene ignorato; senza dispositivi appare errore; CSV disponibile solo dopo un calcolo riuscito.
- Test F: nessun fetch, analytics, localStorage, cookie, form action, link affiliato, pagamento o PII nel file.

## Limiti da mostrare
La quota fissa, la quota potenza, gli oneri e le imposte non compresi nel prezzo scelto non vengono calcolati. Le etichette UE possono riportare consumi per unità diverse, non necessariamente W medi. Non proporre come risparmio certo la differenza fra due scenari teorici.

## Requisiti prima di qualsiasi commercializzazione
Revisione di accessibilità e prove manuali su browser mobile/desktop; verifica delle formule con dati reali; eventuali condizioni d'uso e supporto; valutazione fiscale/IVA e diritto di recesso digitale da parte di professionista competente; informazioni legali e disclosure commerciale appropriate. Nessuna conclusione fiscale o di conformità implicita.

## Fonti ufficiali verificate il 29/10/2026
- ARERA: https://www.arera.it/en/consumatori/valori-della-materia-energia-per-il-servizio-di-maggior-tutela
- UE: https://europa.eu/youreurope/citizens/consumers/shopping/energy-labels/

Nessun collegamento a un advertiser o programma non autorizzato. Non effettuare merge, deploy, pubblicazione SEO o vendita senza revisione.
