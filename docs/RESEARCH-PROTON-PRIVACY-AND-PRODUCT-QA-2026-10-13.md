# VORLI | Proton Partners + revisione prodotto Casa Smart
**Ricerca:** 13 ottobre 2026, Europe/Rome. **Stato:** documento interno; nessuna affiliazione approvata, candidatura, pubblicazione o vendita.

## A. Opportunità internazionale: Proton Partners
**Fonte primaria:** https://proton.me/it/partners/affiliates (consultata il 13/10/2026).

- **Settore:** software per privacy e sicurezza digitale (mail, VPN, cloud e password manager); coerente con la categoria software di VORLI.
- **Destinatari citati dal programma:** YouTuber, blogger, influencer, editori, aziende e organizzazioni. La presenza dei creator non prova che una specifica persona fisica residente in Italia venga approvata.
- **Commissioni PUBBLICIZZATE, non contrattuali VORLI:** la tabella della pagina mostra il 30% su nuove sottoscrizioni e rinnovi per varie linee; per la riga di Proton VPN sono pubblicizzati 100% sui nuovi abbonamenti mensili e 40% sui nuovi abbonamenti annuali/biennali, con 30% sui rinnovi. Le percentuali si riferiscono ai ricavi idonei previsti dai termini, non a guadagni garantiti; non estenderle a ogni prodotto/piano.
- **Pagamento PUBBLICIZZATO:** bonifico il giorno 30 del mese successivo quando il saldo supera **100 USD** secondo la pagina italiana; importi inferiori rinviati. La pagina francese usa una valuta diversa: richiedere conferma della valuta applicabile al contratto.
- **Restrizioni esplicite:** vietati spam, cookie stuffing, traffico artificiale, claim ingannevoli e bidding PPC sui marchi Proton; le promozioni PPC consentite devono puntare prima al proprio sito, non direttamente a Proton. Richiesta disclosure della relazione di affiliazione.
- **Da verificare prima di candidarsi:** gratuità contrattuale effettiva e costi indiretti; cookie e attribuzione; definizione di nuovo cliente/rinnovo e storni; requisiti fiscali e documenti per persona fisica italiana; soglia/valuta; pagamento; paesi e categorie idonee; eventuale necessità di attività economica registrata.
- **Decisione:** candidato da valutare, **non** programma attivo di VORLI. Nessuna candidatura o link affiliato creato.

## B. Prodotto originale da sviluppare: «Privacy digitale senza complicazioni»
**Target:** principianti, famiglie e freelance. **Promessa corretta:** scheda di autovalutazione organizzativa; non promette anonimato, protezione totale o certificazioni.

### Scheda personale, da compilare localmente (non raccogliere segreti)
| Area | Domanda da verificare | Esito Sì/No/Da verificare | Azione non sensibile |
| --- | --- | --- | --- |
| Password | Ogni account importante ha una password distinta? | ___ | ___ |
| Accesso | Dove disponibile, è attivo un secondo fattore? | ___ | ___ |
| Recupero | Esiste un metodo di recupero verificato? | ___ | ___ |
| Dispositivi | Sistema operativo e app ricevono aggiornamenti? | ___ | ___ |
| Backup | È stato provato il recupero di un file di test? | ___ | ___ |
| Cloud | So quali file sincronizzo e con chi li condivido? | ___ | ___ |
| Rete | So distinguere la sicurezza del sito HTTPS da quella della rete? | ___ | ___ |
| VPN | Ho capito cosa una VPN protegge e cosa non protegge? | ___ | ___ |
| Costi | Conosco rinnovi, limiti dei piani e cancellazione? | ___ | ___ |

**Regole:** non scrivere password, codici MFA, chiavi di recupero, indirizzi personali o dati bancari; evitare affermazioni comparative non testate. Una VPN non rende anonimi e non sostituisce aggiornamenti, MFA e buone pratiche.

### Scheda commerciale (bozza, NON in vendita)
- **Titolo:** Privacy digitale senza complicazioni — 9 controlli utili prima di pagare un abbonamento.
- **Formato previsto:** PDF stampabile + versione compilabile localmente; i file finali non sono ancora stati realizzati.
- **Valore:** checklist agnostica rispetto ai marchi; aiuta a decidere se serve davvero un servizio a pagamento.
- **Prezzo:** non determinato. Nessun carrello, checkout, metodo di pagamento o link di affiliazione.
- **Avvertenza:** non è consulenza di cybersecurity né garanzia di sicurezza.

### SEO organico, senza spam
- **Intento principale:** informativo, «come organizzare la privacy digitale in famiglia».
- **Articolo pilastro proposto:** «Privacy digitale: 9 controlli gratuiti prima di comprare una VPN».
- **Sottotemi:** «VPN cosa non protegge», «backup come verificarlo», «password manager come scegliere», «MFA e recupero account».
- **Outline:** obiettivo → checklist → limiti dei singoli strumenti → quando NON acquistare → comparazione costi/abbonamenti → FAQ.
- **Distribuzione:** un articolo approfondito e un video originale dimostrativo; niente pubblicazione massiva, testimonianze inventate, keyword stuffing o link non autorizzati.
- **Disclosure:** se in futuro presenti link di affiliazione, etichetta pubblicitaria chiara e vicina al link, secondo condizioni del programma e norme applicabili.

## C. Audit statico della bozza HTML «Casa Smart senza sorprese»
**Materiale ispezionato:** branch `vorli/producto-casa-smart-layout-20261011`, file `vault/products/casa-smart-senza-sorprese-layout-bozza-02.html` e `docs/QA-MANUALE-CASA-SMART-BOZZA.md` (lettura del 13/10/2026). La PR #31 è aperta e in bozza; nessun test interattivo eseguito in questa iterazione.

**Rilievo 1 — blocco di posizionamento:** l'HTML mostra righe e quadratini stampabili, ma non contiene campi HTML `input` o `textarea` per la compilazione da browser. Non descrivere questa versione come «PDF compilabile» o «form digitale compilabile» fino a implementazione/test; è una scheda **stampabile**.

**Rilievo 2 — avvertenza di bozza:** il pulsante «Nascondi note di bozza» applica `hidden` al nodo `#draft-notes`. La stampa usa lo stato del DOM; occorre testare se, dopo il click, l'avviso «NON PUBBLICARE NÉ VENDERE» sparisce anche dal PDF. Soluzione proposta: rendere il disclaimer sempre visibile nella stampa tramite regola CSS `@media print` e prova automatizzata in entrambi gli stati del toggle.

**Rilievo 3 — validazione:** il workflow PR #31 testa ancore, toggle, fonti consentite, overflow e layout PDF. Il test non dimostra accessibilità PDF/UA, funzionamento della compilazione, correttezza legale o resa su ogni browser. Mantenere la checklist manuale come gate.

**Priorità:** chiudere questi due gap prima di aggiungere nuovi prodotti in vendita; nessun merge/deploy autorizzato.

## D. Gate italiani/UE prima della vendita digitale
- Verificare con un professionista l'inquadramento fiscale italiano e l'eventuale esercizio abituale d'impresa; il piano gratuito di una piattaforma non elimina obblighi fiscali.
- Verificare regole IVA per servizi digitali B2C transfrontalieri e OSS, senza applicare automaticamente soglie a ogni fattispecie: https://europa.eu/youreurope/business/finance-and-tax/vat/one-stop-shop/index_it.htm (consultato 13/10/2026).
- Valutare informazioni precontrattuali, recesso e consenso espresso per fornitura immediata di contenuti digitali, ove applicabile: https://europa.eu/youreurope/citizens/consumers/shopping/returns/index_en.htm (consultato 13/10/2026).
- Trasparenza della natura pubblicitaria: https://agcm.it/media/comunicati-stampa/2025/6/PS12814-PS12815-PS12816-PS12817-PS12818-PS12826 (consultato 13/10/2026).

## E. Prossime verifiche, senza azioni commerciali
1. Controllare stato candidature direttamente nel pannello Awin; un messaggio informativo non equivale ad approvazione.
2. Definire una singola versione realmente testata e accessibile del primo prodotto VORLI.
3. Solo dopo revisione: valutare Proton con condizioni individuali, senza candidatura automatica.
4. Nessuna spesa, account, email, pubblicazione in produzione, link tracciato o dato personale inserito in questo documento.
