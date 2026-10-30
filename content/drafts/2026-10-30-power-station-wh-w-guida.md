---
title: "Power station portatile: Wh e W non sono la stessa cosa"
description: "Guida pratica alla capacità in Wh, alla potenza in W e alle stime prudenti di autonomia prima di acquistare una power station."
status: draft
date: 2026-10-30
category: energia-portatile
robots: noindex
---

# Power station portatile: come leggere Wh, W e autonomia senza farsi ingannare

Una power station portatile può alimentare dispositivi durante un viaggio o in situazioni in cui non è disponibile una presa elettrica. Ma **capacità della batteria** e **potenza erogabile** non sono sinonimi. Per confrontare due modelli, controlla entrambi i dati e le condizioni d'uso.

## 1. I Wh indicano quanta energia è immagazzinata
Una batteria dichiarata da **512 Wh** contiene nominalmente 512 wattora di energia. Non significa che un apparecchio da 512 W funzionerà esattamente un'ora: una parte dell'energia viene persa nella conversione e nell'elettronica, e la capacità utilizzabile può essere inferiore.

## 2. I W indicano quanta potenza può essere erogata
La **potenza continua in W** dell'uscita AC deve essere compatibile con l'assorbimento dell'apparecchio. La potenza di **picco** (o surge) può essere disponibile solo per tempi brevi: non va scambiata con la potenza continua. Alcuni apparecchi, soprattutto con motori e compressori, hanno picchi di avvio.

## 3. Un esempio di autonomia, solo indicativo
Se un dispositivo assorbe in media **60 W** e la power station ha **512 Wh nominali**, il calcolo ideale è 512 ÷ 60 = **8,53 ore**. Ipotizzando **a puro scopo illustrativo** l'85% di energia utile, si ottiene (512 × 0,85) ÷ 60 = **7,25 ore**. L'85% non è una specifica universale né una promessa: inverter, temperatura, stato della batteria, consumo a vuoto e carico reale possono modificare molto il risultato.

Per una stima più seria, usa i dati di capacità *utilizzabile* e rendimento pubblicati dal produttore e, se possibile, una misurazione del dispositivo. Non utilizzare il calcolatore dei consumi domestici VORLI come prova di autonomia di una batteria: il suo scopo è differente.

## 3 bis. Perché l'autoconsumo dell'inverter conta (esempio documentato)
Il semplice rapporto Wh ÷ W può sovrastimare l'autonomia, soprattutto quando il dispositivo collegato assorbe poca potenza. In una [FAQ tecnica ufficiale BLUETTI AC50B](https://www.bluettipower.eu/products/ac50b-camping-power-station), il produttore indica **448 Wh** nominali, profondità di scarica (**DoD**) del **90%**, efficienza dell'inverter (**η**) dell'**85%** e autoconsumo di **10 W**. Per un carico AC **costante di 60 W**, applicando *solo a quel modello* la formula dichiarata:

**Autonomia stimata = 448 × 0,90 × 0,85 ÷ (60 + 10) ≈ 4,90 ore**.

Senza considerare alcuna perdita, 448 ÷ 60 darebbe **7,47 ore**: una differenza significativa. Non significa che ogni power station abbia lo stesso rendimento o autoconsumo. Chiedi al produttore **DoD, efficienza e consumo a vuoto del modello preciso** e controlla se il dato riguarda le uscite AC o DC. Carichi variabili, avvii di motori/compressori e condizioni ambientali richiedono verifiche ulteriori: **questa formula non va usata per promettere l'autonomia di un frigorifero**.

## 4. Controlla le uscite davvero necessarie
Verifica prese AC adatte al mercato di destinazione, porte USB-C con potenza compatibile, uscite DC e numero di apparecchi alimentabili simultaneamente. La presenza di una presa non garantisce che supporti ogni dispositivo.

## 5. Chiedi come viene misurato il tempo di ricarica
Una ricarica dichiarata «rapida» può dipendere da presa AC, pannelli solari, condizioni meteo, potenza di ingresso e intervallo di carica misurato. Verifica se il tempo riguarda 0–80%, 0–100% o un altro intervallo.

## 6. Sicurezza e utilizzo
Segui le istruzioni del produttore per temperatura, ventilazione, conservazione, protezione dall'acqua e trasporto. Non improvvisare collegamenti all'impianto domestico. Controlla la conformità e gli avvisi di sicurezza pertinenti: il marchio CE, quando previsto, è una **dichiarazione di conformità del produttore**, non una garanzia di autonomia.

## 7. Confronta il costo completo
Prima di acquistare, annota capacità nominale e utilizzabile, potenza continua, peso, rumorosità, garanzia, assistenza, eventuali batterie aggiuntive, costo di accessori e spedizione. Non scegliere soltanto in base alla percentuale di sconto.

### Mini-scheda di confronto (da compilare)
| Dato | Modello A | Modello B |
|---|---|---|
| Capacità nominale (Wh) | da verificare | da verificare |
| Capacità utilizzabile documentata | da verificare | da verificare |
| DoD, rendimento inverter e autoconsumo (con fonte) | da verificare | da verificare |
| Potenza continua AC (W) | da verificare | da verificare |
| Picco AC (W e durata) | da verificare | da verificare |
| Porte e limiti per porta | da verificare | da verificare |
| Ricarica e condizioni dichiarate | da verificare | da verificare |
| Peso, garanzia, assistenza | da verificare | da verificare |
| Prezzo totale e data della verifica | da verificare | da verificare |

**Trasparenza:** questa è una bozza editoriale originale senza link affiliati, prezzi, recensioni di prodotti testati o sponsorizzazioni. Prima della pubblicazione aggiornare specifiche e fonti per ogni modello, verificare eventuali autorizzazioni commerciali e aggiungere disclosure evidente se presenti link remunerati.

**Fonti di contesto (consultate il 30/10/2026):** [BLUETTI — AC50B, FAQ su formula di autonomia e autoconsumo](https://www.bluettipower.eu/products/ac50b-camping-power-station); [UE — sicurezza dei prodotti](https://europa.eu/youreurope/citizens/consumers/shopping/product-safety/index_en.htm); [UE — informazioni per acquisti a distanza](https://europa.eu/youreurope/business/selling-in-eu/selling-goods-services/ecommerce-distance-selling/index_en.htm). Le formule sono aritmetiche indicative, non dati di laboratorio.
