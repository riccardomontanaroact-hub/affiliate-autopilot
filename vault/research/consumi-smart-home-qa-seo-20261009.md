# VORLI — Consumi smart home: ricerca, scheda editoriale e test
**Data:** 9 ottobre 2026 (Europe/Rome) · **Stato:** bozza tecnica, non pubblicata · **Asset:** `vault/tools/calcolatore-consumi-smart-home-v01.html`

## Perché è utile
Una guida indipendente per stimare energia e spesa variabile dei dispositivi connessi, senza pubblicizzare falsi risparmi. Differenzia potenza (W) ed energia (kWh), distingue modalità attiva, standby e networked standby. Nessuna stima di traffico, ricavi, approvazioni o conversioni.

## Fonti primarie verificate il 9 ottobre 2026
1. ENEA, definizione di kWh: https://www.efficienzaenergetica.enea.it/glossario-efficienza-energetica/lettera-k/kwh-chilowattora.html
2. Commissione europea, standby/networked standby e ambito di applicazione: https://energy-efficient-products.ec.europa.eu/product-list/standby-networked-standby-and-mode_en
3. Regolamento UE 2023/826 (versione consolidata corrente consultabile dal portale): https://eur-lex.europa.eu/eli/reg/2023/826/oj
4. Commissione europea, avvio nuove norme il 9 maggio 2025, applicabili ai nuovi prodotti immessi sul mercato: https://energy.ec.europa.eu/news/eu-consumers-save-energy-new-limits-standby-modes-electrical-appliances-2025-05-08_en
5. Scheda Awin eWeki IT, ID advertiser 19988: https://ui.awin.com/merchant-profile/19988 — **elettronica di consumo**, finestra di attribuzione pubblicata **30 giorni**; commissione individuale non verificata.

Le norme ecodesign non significano che ogni dispositivo esistente consumi la stessa potenza. Non trasferire limiti normativi a stime di consumi reali di specifici prodotti.

## Matematica e casi di prova
Formula: `kWh = W * ore_al_giorno * giorni_all_anno / 1000`; `costo = kWh * tariffa_euro_per_kWh`.
- Caso A: 2 W, 24 h, 365 giorni, 0,28 €/kWh => **17,52 kWh**, **4,9056 €**, visualizzato **4,91 €**.
- Caso B: 10 W, 24 h, 365 giorni, 0,25 €/kWh => **87,6 kWh**, **21,90 €**.
- Caso C: 0 W, 24 h, 365 giorni, tariffa 0 => **0 kWh**, **0 €**.
- Due righe: A + B con tariffa unica 0,25 €/kWh => **105,12 kWh**, **26,28 €**.
- Incompleto, negativo, oltre 24 ore/giorno o 366 giorni/anno: **non deve produrre totale**.
- Nessuna riga: **non deve produrre totale**.

## Verifiche tecniche effettuate / mancanti
- [x] HTML autonomo, senza dipendenze esterne, formati numerici `it-IT`, nessuna credenziale o dato personale.
- [x] Formule verificate con calcolo indipendente dei casi A–C e del totale.
- [x] Markup con etichette accessibili, tabella con intestazioni, focus visibile, contenitore scrollabile per schermi stretti.
- [x] Il codice impedisce totali parziali quando esistono campi invalidi o incompleti.
- [ ] **Test effettivo nel browser mobile e desktop** (Chrome/Safari/Firefox) e audit con screen reader: non eseguiti.
- [ ] Verificare stampa PDF su browser reali e contrasto con strumento automatico.
- [ ] Revisione editoriale e legale prima di pubblicare.

## SEO organico — solo proposta, non URL pubblicati
- Intento: informativo, «consumo router 24 ore», «costo dispositivi smart sempre accesi», «come calcolare kWh standby».
- Title: `Calcolatore consumi smart home: watt, kWh e costo annuo | VORLI`.
- H1: `Quanto consumano i dispositivi smart di casa?`.
- Meta description: `Calcola una stima annuale dei kWh e della spesa variabile per router e dispositivi smart, inserendo watt, ore e tariffa. Nessuna registrazione.`
- Eventuale slug, **non esistente in produzione**: `/lab/consumi-smart-home/`.
- Schema FAQ solo se il contenuto sarà realmente visibile e risponderà alle policy dei motori.
- Non dichiarare test di prodotti o risparmi misurati; non generare pagine doorway né recensioni false.

## Collegamenti commerciali e conformità
L'asset è un **tool informativo gratuito in bozza**, non un prodotto acquistabile. Non contiene affiliazioni. In caso di futuri link verso dispositivi smart, verificare prima approvazione del singolo advertiser nel pannello Awin, URL tracciato completo, policy del programma e disclosure immediatamente visibile. eWeki IT opera nell'elettronica di consumo, ma nessuna approvazione VORLI è qui attestata. Un affiliato individuale italiano deve verificare obblighi fiscali, eventuale continuità dell'attività, pubblicità e privacy con un professionista competente prima di monetizzare. Non abilitare checkout o pagamento.

## Gate di rilascio
Richiedere revisione umana della PR; eseguire test browser, accessibilità e collegamenti; decidere eventuale distribuzione editoriale solo dopo autorizzazione esplicita. Nessun merge automatico e nessun deploy di produzione.
