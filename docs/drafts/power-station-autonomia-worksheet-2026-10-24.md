# VORLI — Quanto dura una power station? Scheda di calcolo autonoma (BOZZA)
**Ricerca e revisione fonti:** 24 ottobre 2026. **Stato:** contenuto originale in preparazione, non pubblicato, non venduto. Nessun link affiliato e nessuna raccomandazione commerciale individuale.

## Metadati SEO (bozza, non pubblicare)
- **Titolo SEO:** Quanto dura una power station? Calcolo Wh, watt e autonomia reale
- **Slug proposto:** /guide/calcolare-autonomia-power-station/
- **Meta description:** Una scheda pratica per stimare l'autonomia di una power station: watt, Wh, perdite di conversione, carichi variabili e verifiche prima dell'acquisto.
- **Intento:** informativo, non transazionale. Non inserire prezzi, ranking o recensioni non provate.

## 1. Capire le due misure
- **W (watt):** potenza assorbita da un dispositivo in un certo istante. Il valore effettivo può variare rispetto all'etichetta.
- **Wh (wattora):** quantità di energia. Una batteria da 1.000 Wh non promette automaticamente dieci ore di funzionamento con un carico da 100 W.
- **Potenza massima in uscita (W):** vincolo diverso dalla capacità (Wh). Se il carico o il suo picco di avvio supera i limiti della stazione, l'apparecchio potrebbe non partire anche con batteria piena.

## 2. Formula per una stima iniziale
Per un carico **approssimativamente costante** alimentato in AC:

**Autonomia stimata (ore) = capacità nominale (Wh) × fattore di energia utilizzabile ÷ potenza media assorbita (W)**

Il fattore tiene conto in modo *semplificato* delle perdite e dell'energia non utilizzabile; per una stima più precisa, separare profondità di scarica, efficienza inverter e autoconsumo. **Non sommare due volte le stesse perdite.** Se si conosce l'autoconsumo dell'inverter, aggiungerlo alla potenza assorbita prima della divisione.

### Esempio didattico, con numeri inventati (non caratteristiche di prodotti reali)
- Capacità ipotetica: **768 Wh**.
- Carico costante ipotetico: **80 W**.
- Fattore prudenziale **assunto**, non misurato: **0,80**.
- Energia stimata disponibile: 768 × 0,80 = **614,4 Wh**.
- Autonomia indicativa: 614,4 ÷ 80 = **7,68 ore** (circa 7 h 41 min).

**Limiti:** la durata reale cambia con temperatura, età della batteria, potenza variabile, gestione elettronica, uscite DC/AC, spegnimento automatico e assorbimento a vuoto. L'ipotesi 0,80 è un esempio, non un dato garantito per qualunque modello.

## 3. Scheda compilabile prima di scegliere
| Campo | Valore da inserire | Come verificarlo |
| --- | --- | --- |
| Modello e fonte della scheda tecnica | ______ | Sito/manuale ufficiale, data consultazione |
| Capacità nominale (Wh) | ______ | Specifiche del produttore |
| Potenza AC continua massima (W) | ______ | Manuale ufficiale |
| Potenza di picco ammessa (W e durata) | ______ | Manuale; attenzione ai carichi con motore |
| Dispositivo da alimentare | ______ | Etichetta o manuale |
| Assorbimento medio reale (W) | ______ | Misuratore, se disponibile |
| Ore desiderate | ______ | Scenario d'uso |
| Fattore energia utilizzabile ipotizzato | ______ | Dato testato o assunzione esplicita |
| Autoconsumo dell'inverter (W), se noto | ______ | Test indipendente o specifica |
| Autonomia stimata (h) | ______ | Formula sopra |
| Condizioni ambientali / limiti | ______ | Manuale e scenario |
| Fonte e data | ______ | URL pubblico senza tracking |

## 4. Tre errori da evitare
1. **Confondere Wh con W:** 1.000 Wh di capacità non significano 1.000 W di uscita continua.
2. **Usare solo la potenza nominale dell'elettrodomestico:** frigoriferi e apparecchi con compressore o motore hanno cicli e picchi di avvio; una semplice divisione può risultare inaffidabile.
3. **Ignorare perdite e autoconsumo:** l'inverter e l'elettronica consumano parte dell'energia; una stima deve dichiarare le ipotesi.

## 5. Mini-esercizio senza marchi
Un router da 12 W e una lampada LED da 8 W funzionano contemporaneamente per 5 ore.
- Potenza complessiva ipotetica: 12 + 8 = **20 W**.
- Energia richiesta ideale: 20 × 5 = **100 Wh**.
- Con fattore disponibile ipotetico di 0,80, capacità nominale teorica minima: 100 ÷ 0,80 = **125 Wh**.
- Questo valore è **solo una base di calcolo**, non una raccomandazione di acquisto: occorre verificare compatibilità, limiti d'uscita, autoconsumo e margine operativo.

## 6. Note editoriali e di sicurezza
- Non usare questa scheda per garantire autonomia a dispositivi medici, di sicurezza o ad altre applicazioni critiche. Fare riferimento a manuali, professionisti e sistemi certificati.
- Non attribuire a un modello specifico prestazioni mai misurate. Non inserire recensioni fittizie, prezzi non verificati o claim di sicurezza non documentati.
- Un'eventuale pagina commerciale futura deve mostrare disclosure affiliazioni immediatamente riconoscibile, solo dopo adesione verificata e revisione legale/fiscale.
- Se trasformata in PDF venduto direttamente, prima del checkout vanno verificati venditore, IVA, condizioni contrattuali e diritto di recesso per contenuti digitali: non assumere che il download annulli automaticamente il recesso.
- **Gate:** non pubblicare, non vendere, non generare tracking, non attivare pagamenti senza autorizzazione esplicita e revisione.

## Fonti primarie (consultate il 24/10/2026)
1. Jackery, FAQ ufficiale «How can I estimate the runtime of my portable power station?» (pagina con formula approssimativa e limiti per carichi variabili): https://faq.jackery.com/hc/en-us/articles/52357015569179-How-can-I-estimate-the-runtime-of-my-portable-power-station
2. BLUETTI, guida tecnica «What Is Inverter Efficiency?» (capacità, profondità di scarica, efficienza, autoconsumo): https://www.bluettipower.com/blogs/knowledge/what-is-inverter-efficiency
3. Normattiva, Codice del consumo art. 52 (recesso generale): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206;~art52!vig=
4. Normattiva, Codice del consumo art. 59, comma 1, lett. o (contenuti digitali non su supporto materiale): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206;~art59!vig=

**Nota metodologica:** le due guide tecniche sono fonti dei produttori, non test indipendenti dei singoli modelli. La scheda è originale e i numeri degli esempi sono ipotetici. 
