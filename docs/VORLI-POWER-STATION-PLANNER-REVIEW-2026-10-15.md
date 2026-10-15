# VORLI Lab — Power Station Planner: revisione del 15 ottobre 2026

Stato: prototipo locale **non pubblicato**, non in vendita. Questa scheda non è prova di un caricamento del codice nel repository.

## Artefatto locale e test

Archivio locale aggiornato: `VORLI_Power_Station_Planner_QA_2026-10-15_0914.zip`. Contiene `tools/power_station_planner.html`, `tests/test_power_station_planner.cjs`, README e piano SEO. Verifica ripetuta il 15 ottobre 2026 con `node --test`: 19 test superati su 19, nessuna verifica su smartphone fisici.

## Modello e limiti

Energia AC stimata (Wh) = capacità nominale × percentuale utilizzabile × efficienza AC. Consumo giornaliero (Wh) = somma di W medi × ore/giorno. Giorni teorici = energia AC / consumo giornaliero. Non garantisce l'autonomia reale, che dipende da temperatura, carico, degrado e consumi propri dell'inverter.

La somma dei W medi dei dispositivi con ore/giorno maggiori di zero è uno scenario conservativo di uso simultaneo, non la misura dei picchi reali. Se un picco di avvio non è noto, la compatibilità resta **non verificata**. Non utilizzare per apparecchiature mediche o decisioni sul trasporto aereo.

## Verifiche prima di qualunque PR e pubblicazione

1. Trasferire HTML, test e documentazione in un branch isolato, senza modificare `main`.
2. Eseguire i test su checkout del branch e aggiungerli alla CI; la CI esistente non certifica automaticamente i test JavaScript.
3. Verificare usabilità/accessibilità mobile, limiti numerici, campi vuoti e comunicazione delle incertezze.
4. Verificare le fonti e la correttezza commerciale prima di eventuali offerte; nessun link affiliato o pagamento nel prototipo.
5. Aprire solo PR **in bozza**; non eseguire merge o deploy automatico.

## Fonti da ricontrollare

- EASA, Dangerous goods when flying: https://www.easa.europa.eu/en/light/topics/dangerous-goods-when-flying
- Regolamento (UE) 2023/1542, batterie: https://eur-lex.europa.eu/eli/reg/2023/1542/oj
- Your Europe, resi e contenuti digitali: https://europa.eu/youreurope/citizens/consumers/shopping/returns/index_it.htm

Nota: i collegamenti sono riferimenti normativi/editoriali, non conferme di approvazione affiliata. Nessun dato personale o link di tracking incluso.

## Correzione QA del 15/10/2026, ore 09:14

Tre nuovi test di regressione: i dispositivi impostati a zero ore/giorno non contribuiscono più al carico simultaneo né al controllo di picco; il calcolo rifiuta l'overflow numerico. **19/19 test Node.js superati localmente**. Il codice aggiornato resta nel pacchetto locale; il commit di questa scheda non costituisce trasferimento del codice HTML o dei test. Nessuna pubblicazione o modifica al branch principale.
