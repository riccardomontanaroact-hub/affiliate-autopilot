# Kit VORLI — confronto e stima prudente dell'autonomia di power station
**Bozza editoriale v0.2 · 30 ottobre 2026 · Non in vendita · Non pubblicare o distribuire automaticamente**

Questo modello consolida i campi utili delle bozze nelle PR #100, #112 e #130. Non sostituisce manuali, prove di laboratorio, misure elettriche o progettazione di alimentazione di emergenza. Non è un calcolatore certificato.

## A. Definisci l'uso prima di scegliere un prodotto
| Dato | Valore da compilare |
|---|---|
| Scenario (es. campeggio, router) | |
| Uscita necessaria (AC / USB-C / DC), tensione e connettore | |
| Temperatura/ventilazione e condizioni d'uso | |
| Autonomia desiderata e margine di sicurezza | |
| Apparecchi critici o medici? | **Non utilizzare il kit per garantire continuità; rivolgersi a uno specialista** |

## B. Misura o documenta i carichi
| Apparecchio | Uscita | W medi (misurati o stimati?) | Ore desiderate | Wh teorici = W × ore | W di picco all'avvio | Fonte e data |
|---|---|---:|---:|---:|---:|---|
| Dispositivo A | | | | | | |
| Dispositivo B | | | | | | |
| Dispositivo C | | | | | | |

**Importante:** la somma dei Wh richiesti non dimostra che la power station sia compatibile. Verificare **separatamente** la potenza continua simultanea, il picco con durata dichiarata, il limite per singola porta, i protocolli USB-C e i carichi con compressori/motori.

## C. Confronto di tre modelli
| Specifica | Modello A | Modello B | Modello C |
|---|---|---|---|
| Codice esatto / versione / mercato | | | |
| Capacità nominale Wh | | | |
| Capacità utilizzabile, DoD e fonte | | | |
| Efficienza inverter, condizioni e fonte | | | |
| Autoconsumo AC in W e fonte | | | |
| Potenza continua AC W | | | |
| Picco W e durata | | | |
| Porte AC/DC/USB-C e limiti simultanei | | | |
| Peso e dimensioni | | | |
| Ricarica (0–80% o 0–100%?) e condizioni | | | |
| Temperatura, ventilazione e istruzioni | | | |
| Garanzia, venditore e assistenza in Italia | | | |
| Disponibilità e data di verifica | | | |
| Prezzo totale e data (solo dopo verifica) | | | |
| Manuale/scheda tecnica ufficiale | | | |
| Dati discordanti o non confermati | | | |

## D. Calcolo illustrativo per **un carico AC costante**
**Metodo semplificato, solo se i dati sono riferiti allo stesso modello e allo stesso tipo di uscita:**

`Ore stimate ≈ (Wh nominali × DoD × rendimento inverter) / (W medi del carico + W autoconsumo inverter)`

DoD e rendimento sono fattori compresi fra 0 e 1. Se un dato non è documentato, scrivere **non stimabile con affidabilità**: non inventare un valore “tipico”. La formula non descrive carichi variabili, motori, compressori, uscite DC/USB-C o batterie degradate.

**Esempio del produttore, non prova VORLI:** la FAQ BLUETTI AC50B riporta 448 Wh, DoD 0,90, rendimento 0,85 e autoconsumo 10 W. Per 60 W AC costanti: `448 × 0,90 × 0,85 / (60 + 10) = 4,896 ore`. Il calcolo ideale senza perdite darebbe `448 / 60 = 7,47 ore`: non confondere i due risultati. **Non generalizzare questi parametri ad altri prodotti.**

**Controllo qualità aggiuntivo:** il 30/10/2026 la pagina italiana AC50B mostrava nello stesso documento dati contrastanti (268 Wh/600 W nel riquadro iniziale, 448 Wh/700 W in titolo e tabella). Il modello risultava esaurito/non più in produzione. **Bloccare ogni scheda commerciale del modello finché le specifiche non siano chiarite**; l'esempio numerico resta solo didattico e attribuito alla FAQ europea.

## E. Decisione e registro fonti
- Motivo della scelta e vincoli: ______
- Dati non verificati o contraddittori: ______
- Misure dirette eseguite? Sì / No. Se no, non scrivere «testato da VORLI».
- Fonti e data dell'ultimo controllo: ______
- Link affiliati presenti? **No**. Qualsiasi futura monetizzazione richiede verifica privata del programma e disclosure chiara.
- Verifica del manuale, delle limitazioni di trasporto batterie e della sicurezza? ______
- **Blocco vendita digitale:** prima di commercializzare il kit verificare originalità, valore d'uso, obblighi informativi, recesso digitale, IVA e inquadramento dell'attività del venditore italiano; nessun prezzo o checkout.

## Fonti primarie e provenienza — consultate il 30/10/2026
- [BLUETTI EU — FAQ AC50B e formula con autoconsumo](https://www.bluettipower.eu/fi/products/ac50b-camping-power-station-fi)
- [BLUETTI Italia — scheda AC50B con incongruenza interna](https://it.bluettipower.eu/products/ac50b-power-station)
- [EASA — informazioni generali su merci pericolose](https://www.easa.europa.eu/en/domains/air-operations/dangerous-goods) (per il trasporto controllare regole del vettore, senza presumere che la power station sia ammessa).
- Bozze precedenti: [PR #100](https://github.com/riccardomontanaroact-hub/affiliate-autopilot/pull/100), [PR #112](https://github.com/riccardomontanaroact-hub/affiliate-autopilot/pull/112), [PR #130](https://github.com/riccardomontanaroact-hub/affiliate-autopilot/pull/130). Questo è **un candidato unificato**, non una decisione di chiusura o merge delle altre PR.

**Nessun account, candidatura, invio email, spesa, pagamento, deploy o pubblicazione autorizzati.**
