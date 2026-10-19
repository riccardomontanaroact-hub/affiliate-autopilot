# VORLI — checklist pre-lancio: affiliazioni e prodotti digitali

**Verifica documentale:** 19 ottobre 2026 (Europe/Rome).  
**Stato:** bozza interna di lavoro; **NON** è autorizzazione a pubblicare, attivare checkout o iniziare vendite.  
**Ambito:** sito editoriale tech, link affiliati, PDF originali; attività di venditore individuale stabilito in Italia.  
**Privacy:** nessun dato personale, identificativo publisher, credenziale o URL di tracking deve essere copiato in questo documento o in un repository pubblico.

## Decisione operativa: due percorsi distinti

| Controllo | Articoli con affiliazioni | Vendita diretta di PDF |
|---|---|---|
| Titolo e utilità | Testo originale, prove e fonti; niente schede ingannevoli | Prodotto originale, licenze/diritti e file collaudato |
| Rapporti commerciali | Programma effettivamente approvato e termini individuali verificati nella dashboard | Identità del venditore e inquadramento fiscale/contrattuale chiariti |
| Disclosure | Avvertenza pubblicitaria ben visibile vicino a ogni link o codice | Informazioni precontrattuali, venditore, prezzo totale, modalità di fornitura |
| Recesso | Il merchant resta venditore del bene; evitare promesse proprie su resi | Informativa sul recesso; eccezione per download immediato solo se tutti i requisiti applicabili sono soddisfatti |
| Pagamenti | Non necessari sul sito VORLI per semplice rinvio al merchant | Checkout, conferma contrattuale, IVA e gestione rimborsi da verificare **prima** di attivare |
| Privacy | Non incorporare parametri personali, email o link di tracking nei commit | Verificare raccolta dati, fornitori, informative e conservazione |
| Stato al 19/10 | **NO-GO per link commerciali non verificati** | **NO-GO per vendita diretta** |

## Gate A — contenuti editoriali e affiliazioni

- [ ] Per ogni merchant registrare **privatamente** lo stato reale in dashboard (approvato/in attesa/rifiutato), la data del controllo, le categorie ammesse, la commissione **individuale** e il cookie **specifico**. Un invito, un messaggio informativo, una promozione e un'email di benvenuto non sono automaticamente equivalenti a una decisione contrattuale attuale.
- [ ] Non assumere che il cookie standard Awin di 30 giorni sia quello di ogni programma. Verificare le condizioni di ciascun advertiser; cancellazione cookie e limiti tecnici possono impedire l'attribuzione.
- [ ] Non mostrare prezzi, sconti, disponibilità, commissioni o recensioni come aggiornati se non verificati con fonte e data.
- [ ] Inserire disclosure immediatamente visibile nei contenuti con link o codici affiliati, ad esempio «Pubblicità — link affiliato [marchio]»; valutare l'applicabilità puntuale delle formule IAP, senza limitarsi a una nota nel footer.
- [ ] SEO: rispondere a una domanda reale, spiegare metodologia, limiti e casi d'uso; non creare pagine doorway, recensioni inventate o duplicazioni di catalogo.
- [ ] Non aggiungere link tracciati al codice pubblico finché non è risolta la bonifica privacy e autorizzata la pubblicazione.

## Gate B — PDF originali (preparazione senza vendite)

- [ ] Revisione umana del contenuto, verifica fonti, titolarità di testi/immagini e assenza di marchi usati impropriamente.
- [ ] Validazione del PDF reale: numero pagine, dimensioni di **ogni** pagina, testo selezionabile, link, leggibilità mobile, indice e accessibilità di base.
- [ ] Definire esattamente chi sia il venditore, chi emetta il documento fiscale, chi riscuota il pagamento e chi gestisca rimborsi/assistenza; verificare anche eventuale ruolo di piattaforma o marketplace.
- [ ] Predisporre informazioni precontrattuali, prezzo totale e caratteristiche del prodotto; conservare prova delle informazioni fornite e della conferma su supporto durevole.
- [ ] **Recesso:** per contenuti digitali non forniti su supporto materiale, non dichiarare «nessun rimborso» in modo automatico. Se si intende iniziare la fornitura prima del termine ordinario, verificare consenso espresso preventivo, presa d'atto della perdita del diritto e conferma contrattuale conforme; il download/streaming e il momento d'inizio della prestazione contano. Verificare anche le regole italiane applicabili.
- [ ] **IVA e fiscalità:** valutare con professionista italiano l'inquadramento del venditore individuale, la necessità di partita IVA, fatturazione, qualificazione della prestazione, eventuale IVA transfrontaliera e OSS. La soglia UE di 10.000 euro per alcune operazioni transfrontaliere non equivale a un'esenzione generale dall'IVA o dall'apertura di partita IVA.
- [ ] Checkout e pagamenti **disabilitati** fino alla chiusura documentata di tutti i gate.

## Gate C — sicurezza del repository pubblico

- [ ] Individuare dati personali e segreti nei file correnti, nella cronologia dei commit, nelle PR e nei diff; rimuovere dal file corrente non significa eliminarli dalla cronologia.
- [ ] Separare configurazione pubblica da segreti e dati personali; non pubblicare email, ID di publisher, URL affiliati personalizzati, token, ordini o dati clienti.
- [ ] Usare solo branch separati e PR in bozza; nessun merge, deploy, cambio di produzione o attivazione pagamento automatica.
- [ ] Eseguire test dei contenuti e verificare il diff prima di proporre una PR.

## Registro fonti primarie (consultate 19/10/2026)

1. **IAP, Regolamento Digital Chart**, versione approvata 30/10/2024, in particolare art. 4 su codici sconto/affiliate marketing: https://www.iap.it/codice-e-altre-fonti/regolamenti-autodisciplinari/regolamento-digital-chart/
2. **Commissione europea, Your Europe**, vendite B2C a distanza, obblighi informativi, conferma e recesso: https://europa.eu/youreurope/business/selling-in-eu/selling-goods-services/ecommerce-distance-selling/index_en.htm
3. **Commissione europea, orientamenti 2021/C 525/01** sulla direttiva 2011/83/UE, incluso il momento d'inizio del download e il consenso al recesso: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52021XC1229%2804%29
4. **EUR-Lex, direttiva 2011/83/UE consolidata**, artt. 8, 14 e 16: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A02011L0083-20220528
5. **Commissione europea, Your Europe**, IVA transfrontaliera (pagina verificata 13/07/2026): https://europa.eu/youreurope/business/finance-and-tax/vat/cross-border-vat/index_en.htm
6. **Commissione europea, Your Europe**, OSS (pagina verificata 13/05/2026): https://europa.eu/youreurope/business/finance-and-tax/vat/one-stop-shop/indexamp_en.htm
7. **Awin, FAQ Italia**, durata cookie variabile per advertiser: https://www.awin.com/it/faq

**Nota metodologica:** fonti generali pubbliche, non sostituiscono termini del singolo advertiser, verifica della dashboard né consulenza legale/fiscale italiana. Ricontrollare le norme e le condizioni alla data di un eventuale lancio.
