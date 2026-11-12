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


## Revisione qualità del 29/10/2026, ore 19:15 CET

Correzioni applicate al prototipo della stessa PR:
- Il campo **prezzo €/kWh** è stato spostato all'interno del modulo HTML. Prima era esterno al `<form>`: l'invio da tastiera direttamente dal campo tariffa non seguiva il normale comportamento del modulo.
- L'esportazione CSV usa ora un prefisso testuale costante `Nome: ` per ogni etichetta, rimuovendo anche i caratteri di controllo dal nome. Il prefisso impedisce che un'etichetta scelta dall'utente cominci come formula di foglio di calcolo, anche se inizia con spazi, segni `=`, `+`, `-`, `@`, tab o ritorni a capo. I campi rimangono racchiusi fra doppi apici e i doppi apici interni sono raddoppiati.
- Il JavaScript incorporato è stato sottoposto a controllo di sintassi; sono stati controllati staticamente otto casi di etichette CSV potenzialmente problematiche. **Non** equivalgono a prove di apertura in Excel, LibreOffice o browser mobili.

**Rischio residuo:** OWASP osserva che non esiste una sanificazione CSV universale valida per tutti i fogli di calcolo. Verificare manualmente l'apertura, il salvataggio e la riapertura del CSV nei software target prima di distribuire il prodotto. Il prefisso `Nome: ` è intenzionale e modifica la rappresentazione della sola etichetta nel CSV, non i calcoli.

**Fonti pubbliche consultate il 29/10/2026:**
- OWASP, CSV Injection: https://community.owasp.org/attacks/CSV_Injection
- ARERA, guida alle voci della bolletta: https://www.arera.it/fileadmin/bolletta/allegati/guidaele.pdf

**Nessuna pubblicazione, vendita, attivazione di pagamenti o modifica al branch principale.**


## Revisione qualità del 29/10/2026, ore 20:14 CET — risultati non aggiornati

**Difetto individuato:** dopo un calcolo riuscito, modificare potenza, ore, giorni, tariffa o nome lasciava visibili i risultati precedenti e manteneva attivo `Esporta CSV`. Il file esportato poteva quindi riferirsi ai valori vecchi, non ai dati attualmente presenti nel modulo.

**Correzione applicata:** l'evento `input` del modulo invalida i risultati non appena cambia un campo dopo un calcolo: svuota la tabella, disabilita l'esportazione CSV e chiede di ricalcolare. Dopo un errore di validazione, la modifica di un campo cancella il messaggio di errore precedente. Non cambia le formule né aggiunge rete, analytics o raccolta dati.

**Verifiche statiche:** codice aggiornato sul branch di bozza; controllata presenza del listener `input`, del reset della tabella e della disabilitazione CSV. **Non ancora verificato in un browser reale**: provare manualmente calcolo → modifica tariffa → CSV disabilitato e tabella svuotata → ricalcolo → CSV riabilitato, anche su mobile. Verificare stampa dopo modifica e utilizzo da tastiera. Nessun merge o deploy.


## Smoke test ripetibile del 29/10/2026, ore 23:09 CET

Aggiunto `tests/calcolatore-consumi-smoke.js` alla **stessa PR in bozza**. Comando locale: `node tests/calcolatore-consumi-smoke.js` (Node.js standard, senza dipendenze esterne). Sono stati eseguiti **16 controlli con DOM simulato in JavaScript**, tutti superati, sullo script HTML presente nel branch: formule (292 kWh, 73 €, media 6,08 €), virgola decimale, ricalcolo a tariffa modificata (87,60 €), invalidazione della tabella e del CSV, protezione della cella nome nel CSV, input non validi, confronto di due dispositivi, stampa e reset.

**Ambito preciso:** sono smoke test della logica e degli eventi, non una verifica del rendering/accessibilità in Chrome, Safari, Firefox, né un'apertura reale del CSV in Excel/LibreOffice. Rimangono obbligatori i test manuali cross-browser e del CSV prima di distribuire il prodotto. Nessuna pubblicazione, vendita, attivazione di pagamenti o modifica al branch principale.
