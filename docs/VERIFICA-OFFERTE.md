# Procedura per inserire offerte affiliate verificate

Questo progetto non deve pubblicare dati dimostrativi come se fossero offerte acquistabili. Il file `data/products.json` resta il catalogo pubblicato; `data/product_intake_template.json` è soltanto un modello di raccolta dati e non viene importato automaticamente.

## Prima di inserire un prodotto

1. **Approvazione del programma:** verifica nel pannello del network che l'account e il programma dell'inserzionista siano approvati. Nel blocco `verification`, `approval_status` deve essere `approved` prima della pubblicazione.
2. **Nome, venditore e link:** ricava i dati dalla pagina ufficiale del venditore o dal feed autorizzato del network. Usa il link affiliato generato dal network; non costruire o indovinare URL di tracking.
3. **Fonte generale:** registra `verification.source_url`, `verification.source_checked_at` (data ISO, ad esempio `2026-10-22`), `verification.program` e `verification.checked_by`.
4. **Prezzo e disponibilità:** annota la data in `price_checked_at`. Se il prezzo non è verificabile, lascia `price` a `null`; se è valorizzato, la data di controllo è obbligatoria.
5. **Commissione:** usa soltanto la percentuale mostrata dal network per il programma approvato. Registra `commission_source_url` e `commission_checked_at`; senza questi dati l'offerta non viene pubblicata.
6. **Valutazioni:** inserisci una valutazione solo se esiste una fonte verificabile e annotala in `rating_source_url` e `rating_checked_at`. In assenza di fonte, lascia `rating` a `null`.
7. **Descrizione e caratteristiche:** scrivi soltanto affermazioni sostenute dalle fonti. Non inventare pro, contro, specifiche o promesse.
8. **Controllo finale:** verifica manualmente il link HTTPS generato dal network, il mercato di destinazione, la disclosure affiliata e le condizioni del programma prima di copiare i dati nel catalogo pubblicato. Il generatore non attiva pulsanti per offerte prive di approvazione o verifiche obbligatorie.

## Regole di sicurezza

- Non inserire password, token, cookie o dati personali nei file del repository.
- Non pubblicare un'offerta se il programma è in attesa, rifiutato o non verificato.
- Non usare link di esempio come `https://example.com/` per offerte reali.
- Non automatizzare accettazioni di termini, iscrizioni o attivazioni di campagne senza approvazione umana.
- Il modello è una checklist operativa, non una connessione automatica ad Awin o ad altri network.
