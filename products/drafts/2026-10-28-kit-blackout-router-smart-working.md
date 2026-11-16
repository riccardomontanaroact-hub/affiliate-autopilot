---
title: "Kit VORLI — Piano blackout per router e postazione di lavoro"
description: "Schede compilabili per stimare consumi, autonomia e priorità dei dispositivi senza confondere una power station con un UPS."
status: "draft"
language: "it"
last_reviewed: "2026-10-28"
review_required: true
product_type: "original-digital-template"
---

# Kit VORLI — Piano blackout per router e postazione di lavoro

**Versione:** bozza originale 0.1 · 28 ottobre 2026. **Non in vendita.** Nessun prezzo, checkout, link affiliato o test reale dichiarato.

## A cosa serve

Un modello compilabile per decidere quali dispositivi **non critici** alimentare temporaneamente durante un'interruzione elettrica, stimare un ordine di grandezza dell'autonomia e predisporre una procedura di arresto ordinato del lavoro. È un esercizio di pianificazione, **non** un progetto elettrico, una certificazione di sicurezza o una garanzia di continuità.

**Limite fondamentale:** una power station non è automaticamente un gruppo di continuità (UPS). Se occorre evitare anche un'interruzione brevissima, verificare la funzione EPS/UPS, i tempi di commutazione dichiarati, i limiti del carico e la compatibilità con l'apparecchio. Gli UPS hanno topologie diverse e non tutti garantiscono tempo di commutazione nullo. Non improvvisare collegamenti a quadri elettrici, prese domestiche, impianti fissi o apparecchi medicali.

## Scheda 1 — Priorità e inventario (valori da misurare)

| Dispositivo | Priorità A/B/C | Alimentazione richiesta (AC/USB-C/DC) | Potenza media misurata (W) | Picco di avvio noto? | Ore desiderate | Note |
| --- | --- | --- | ---: | --- | ---: | --- |
| Router/modem | | | | | | |
| ONT fibra (se presente) | | | | | | |
| Notebook | | | | | | |
| Monitor | | | | | | |
| Lampada | | | | | | |
| Altro dispositivo non critico | | | | | | |

**Priorità A** = indispensabile per concludere un'attività; **B** = utile; **C** = rimandabile. Annotare l'eventuale dipendenza da apparati esterni: anche se il router resta acceso, la connessione può non funzionare durante un guasto della rete dell'operatore. Un'etichetta con potenza massima non equivale sempre al consumo medio: quando possibile misurare con strumenti idonei senza aprire apparecchi o intervenire sui cablaggi.

## Scheda 2 — Calcolo trasparente

1. Sommare le potenze **medie** dei dispositivi che saranno accesi **contemporaneamente**: **P totale (W) = P1 + P2 + ...**.
2. Annotare la capacità nominale della batteria in **Wh**, non confonderla con la potenza di uscita in W.
3. Per un carico relativamente stabile stimare **ore indicative = capacità nominale (Wh) × fattore ipotetico / P totale (W)**. Usare, soltanto come ipotesi di partenza, un fattore **0,80**: non è un rendimento misurato o valido per ogni modello. Per carichi molto piccoli l'autoconsumo dell'inverter può incidere molto.
4. Verificare **separatamente** che il carico sia compatibile con potenza continua, potenza di picco, singole porte, tensione, frequenza, connettori e forma d'onda dichiarati. Una stima in Wh **non** dimostra compatibilità elettrica.
5. Se il carico varia, stimare per intervalli: **energia richiesta (Wh) = somma di (potenza media dell'intervallo in W × durata in ore)**. Evitare di sommare indiscriminatamente le ore di apparecchi accesi in periodi diversi.

| Campo | Scenario A: essenziali | Scenario B: essenziali + comfort |
| --- | --- | --- |
| Dispositivi simultanei | | |
| Potenza totale media (W) | | |
| Capacità nominale (Wh) | | |
| Fattore ipotetico (es. 0,80) | | |
| Ore indicative calcolate | | |
| Potenza continua/picco compatibile? | Da verificare | Da verificare |
| Autonomia reale verificata sul modello? | No / da misurare | No / da misurare |
| Margine di riserva e soglia di spegnimento | | |

### Esempio esclusivamente didattico

Supponiamo **una batteria immaginaria da 512 Wh** e **due dispositivi immaginari** con consumi medi stabili di **12 W** e **28 W**. Totale **40 W**. Con fattore ipotetico **0,80**: 512 × 0,80 / 40 = **10,24 ore teoriche**. Se si aggiunge un terzo carico da **60 W**, totale **100 W**, la stima scende a **4,10 ore teoriche**. Nessuna di queste cifre è una prestazione promessa: le perdite dipendono da modello, modalità AC/DC, temperatura, stato batteria e carico. Non usare la durata calcolata come tempo massimo sicuro per salvare dati o alimentare apparecchi essenziali.

## Scheda 3 — Piano di lavoro durante il blackout

| Momento | Azione non distruttiva | Responsabile | Esito |
| --- | --- | --- | --- |
| Prima di un'interruzione | Salvare lavoro e predisporre copie di sicurezza | | |
| Prima di un'interruzione | Verificare manuali e compatibilità dei soli apparecchi consentiti | | |
| All'interruzione | Controllare se rete dati e apparati esterni sono disponibili | | |
| Durante | Disattivare i carichi C non necessari | | |
| Prima della riserva | Salvare file e spegnere ordinatamente dispositivi | | |
| Dopo | Ricaricare e registrare eventuali problemi, secondo manuale | | |

Non eseguire test di distacco della rete su impianti o carichi critici. Se si vuole verificare un apparecchio in ambiente controllato, farlo **solo** secondo istruzioni del produttore e senza collegamenti improvvisati; non dichiarare «continuità garantita» sulla base di una prova singola.

## Scheda 4 — Confronto neutrale tra soluzioni

| Criterio | Modello A | Modello B | Fonte ufficiale / data |
| --- | --- | --- | --- |
| Capacità nominale (Wh) | | | |
| Potenza AC continua (W) | | | |
| Picco e limiti dichiarati | | | |
| Uscite AC, DC, USB-C compatibili | | | |
| Funzione UPS/EPS e tempo di commutazione dichiarati | | | |
| Consumo a vuoto/autoconsumo dichiarato | | | |
| Temperatura d'esercizio e ventilazione | | | |
| Manuale e garanzia in UE | | | |
| Disponibilità e costo totale aggiornato | | | |
| Stato autorizzazione affiliato | **Non verificato** | **Non verificato** | Dashboard riservata, mai pubblicare dati privati |

**Non compilare prezzi, caratteristiche o autorizzazioni per supposizione.** I valori di un prodotto non si trasferiscono a un altro, anche se hanno capacità Wh simili. Evitare ranking basati su commissioni, recensioni inventate e promesse di risparmio o durata.

## Scheda 5 — Esito della valutazione

- Scenario prioritario: __________
- Potenza media misurata e fonte: __________
- Energia richiesta (Wh) per il periodo: __________
- Compatibilità elettrica e limiti verificati: __________
- Autonomia **stimata**, non garantita: __________
- Durata **misurata**, se esiste una prova lecita e non distruttiva: __________
- Margine per arresto ordinato: __________
- Dati mancanti / domande al produttore: __________
- Decisione provvisoria: __________

## Scheda editoriale VORLI (solo bozza)

**Titolo prodotto:** Kit blackout smart working — piano autonomia e priorità.  
**Destinatari:** creator, freelance, utenti home-office.  
**Contenuto:** inventario dispositivi, formula spiegata, esempio ipotetico, piano di arresto e matrice di confronto.  
**Beneficio verificabile:** rendere espliciti consumi, ipotesi e dati mancanti; **non** garantire autonomia, sicurezza o connessione Internet.  
**SEO title:** Piano blackout router e PC: kit autonomia compilabile | VORLI  
**Meta description:** Schede pratiche per pianificare consumi e priorità di router, notebook e accessori, distinguendo power station e UPS.  
**CTA editoriale non attiva:** «Consulta il modello». Non attivare acquisti o raccolta di dati.

## Fonti e limiti — consultazione 28 ottobre 2026

- Jackery, FAQ aggiornata il **2 luglio 2026**, formula orientativa Wh × 0,8 / W e avvertenze per carichi variabili: https://faq.jackery.com/hc/en-us/articles/52357015569179-How-can-I-estimate-the-runtime-of-my-portable-power-station (fonte commerciale; **non** prova indipendente).
- Eaton, panoramica topologie UPS, continuità e tempi di trasferimento: https://www.eaton.com/sg/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/choosing-the-optimal-ups-topology-.html (fonte di produttore; non specifica un modello VORLI).
- Commissione europea, marcatura CE e significato della dichiarazione del fabbricante: https://single-market-economy.ec.europa.eu/single-market/goods/ce-marking_en
- Commissione europea, sicurezza dei prodotti: https://commission.europa.eu/topics/business-and-industry/product-safety_en
- AGCM, obbligo di rendere riconoscibile la comunicazione promozionale: https://www.agcm.it/media/comunicati-stampa/2017/7/alias-8853
- Direttiva 2011/83/UE, testo consolidato per informazione e recesso dei contenuti digitali: https://eur-lex.europa.eu/eli/dir/2011/83/2022-05-28 (verificare testo vigente e recepimento italiano prima della vendita).

**Gate prima della commercializzazione:** revisione tecnica e di sicurezza; controllo diritti sul testo e sull'impaginazione; disclosure affiliazioni; verifica del recesso digitale e delle condizioni di vendita B2C; verifica IVA e inquadramento fiscale italiano con professionista; privacy e pagamenti; approvazione umana. Il download digitale non elimina automaticamente il diritto di recesso. **Nessuna pubblicazione in produzione.**
