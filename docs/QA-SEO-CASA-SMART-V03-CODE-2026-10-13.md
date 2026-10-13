# VORLI — Casa Smart v0.3: QA, ricerca e piano SEO
Data verifica: 13 ottobre 2026, ore 08:14 CEST. Documento interno. **Non pubblicare, non vendere, non unire senza revisione.**

## Stato verificato
- Codice aggiornato nel branch `vorli/product-casa-smart-v03-code-20261013-0814`, file `drafts/casa-smart-checklist-interattiva-2026-10-13.html`.
- Calcolo ora implementato: **36 mesi = prezzo iniziale + accessori iniziali + 36 × abbonamento mensile + 3 × abbonamento annuo**.
- Prezzo iniziale obbligatorio (può essere zero); altri campi facoltativi vuoti valgono zero.
- Messaggi espliciti per prezzo mancante, importi negativi/non numerici e totale non finito.
- Nota per evitare doppio conteggio del canone mensile e annuale. Stima non comprende energia, variazioni di prezzo, riparazioni, imposte e costi non inseriti.
- Restano avvertenza di bozza, struttura offline, stampa, reset e layout responsive.

## Test eseguiti e limiti
**Test aritmetici della formula (passati, non test browser):**
| Prezzo | Accessori | Mensile | Annuale | Totale atteso |
| ---: | ---: | ---: | ---: | ---: |
| €100 | €0 | €0 | €0 | €100 |
| €100 | €20 | €5 | €10 | €330 |
| €0 | €0 | €0 | €0 | €0 |
| €249,99 | €29,90 | €3,99 | €0 | €423,53 |

Verifica statica passata: campi presenti, avviso BOZZA presente, `aria-live` presente, nessuna chiamata di rete o persistenza automatica rilevata nel codice esaminato. Codice riletto dal repository dopo il commit.

**Da testare prima di un'eventuale distribuzione:** input nel browser (anche locale italiano con separatore decimale), modifica dinamica di ogni campo, reset, campi vuoti, valori estremi, tastiera/lettore schermo, stampa PDF A4 e visualizzazione smartphone. Non dichiarare il prodotto testato end-to-end.

## Ricerca commerciale verificata
- **eWeki IT**: scheda ufficiale Awin advertiser **19988**: settore dichiarato **elettronica di consumo**, cookie indicato **30 giorni**. Non sono state verificate commissioni contrattuali né approvazione del singolo publisher. Fonte consultata 13 ottobre 2026: https://ui.awin.com/merchant-profile/19988
- **Cyber Resilience Act**: dal **11 settembre 2026** sono applicabili specifici obblighi di segnalazione per i produttori; le principali prescrizioni iniziano **11 dicembre 2027**. La checklist deve suggerire di verificare supporto/aggiornamenti senza dichiarare certificazioni di prodotti specifici. Fonte Commissione europea, pubblicata 11 settembre 2026, consultata 13 ottobre 2026: https://commission.europa.eu/news-and-media/news/safer-and-more-secure-digital-products-2026-09-11_en
- **Vendita diretta digitale UE**: prima di vendere verificare posizione fiscale del venditore individuale in Italia, informativa precontrattuale, recesso/consenso per contenuti digitali e trattamento IVA nelle vendite transfrontaliere. Fonti consultate 13 ottobre 2026: https://europa.eu/youreurope/business/selling-in-eu/selling-goods-services/ecommerce-distance-selling/index_en.htm ; https://europa.eu/youreurope/business/finance-and-tax/vat/cross-border-vat/index_en.htm . Non costituisce consulenza fiscale o legale.
- Nessun nuovo account, domanda di affiliazione o canale a pagamento avviato; nessun link affiliato inserito.

## Scheda commerciale interna (non pubblicata)
**Nome:** Casa Smart senza sorprese — Checklist interattiva v0.3.
**Problema:** chi compra un dispositivo connesso può sottovalutare compatibilità, supporto e abbonamenti.
**Proposta:** checklist originale da compilare localmente, con stima indicativa dei costi su 36 mesi e promemoria delle verifiche.
**Destinatari:** persone che confrontano prese, videocamere, lampadine e altri dispositivi smart domestici.
**Limiti:** non certifica sicurezza/compatibilità; non sostituisce manuale, consulenza tecnica o condizioni del venditore.
**Modello commerciale:** da definire dopo revisione fiscale/contrattuale e test funzionali; nessun prezzo o ricavo dichiarato.

## Piano SEO organico, senza spam
- **Intento:** informativo, confronto pre-acquisto.
- **Articolo pilota (da non pubblicare):** «Quanto costa davvero una presa smart in 3 anni? Checklist e calcolo».
- **Slug proposto:** `/guide/costo-presa-smart-3-anni/`
- **Meta description proposta:** «Prezzo, accessori e abbonamenti: scopri cosa verificare prima di comprare una presa smart e come stimarne il costo su 36 mesi.»
- **Struttura:** (1) costi nascosti (2) compatibilità Wi-Fi/hub (3) aggiornamenti e privacy (4) esempio dichiaratamente ipotetico (5) checklist scaricabile dopo revisione.
- **Link:** solo a fonti ufficiali; eventuali link di affiliazione **solo dopo approvazione verificata**, con disclosure chiara.
- **Distribuzione:** un contenuto originale di qualità e aggiornamenti motivati; niente pagine duplicate, recensioni inventate, outreach automatico o keyword stuffing.
- **Metriche future:** impression organiche, visite qualificate, interazione con guida (senza raccolta dati personali nella checklist), conversioni soltanto se verificate da piattaforme autorizzate.

## Blocchi aperti
1. Test browser e PDF non ancora eseguiti.
2. Conferma delle candidature advertiser da verificare nella dashboard Awin, non deducibile dalle email.
3. Requisiti legali e fiscali per un venditore individuale italiano ancora da chiarire prima della vendita.
4. Nessuna pubblicazione, attivazione di pagamenti o merge autorizzato.
