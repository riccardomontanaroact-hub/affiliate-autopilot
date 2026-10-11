# Procedura per inserire offerte affiliate verificate

Questo progetto non deve pubblicare dati dimostrativi come se fossero offerte acquistabili. Il file `data/products.json` resta il catalogo pubblicato; `data/product_intake_template.json` è soltanto un modello di raccolta dati e non viene importato automaticamente.

## Prima di inserire un prodotto

1. **Approvazione del programma:** verifica nel pannello del network che l'account e il programma dell'inserzionista siano approvati. `approval_status` deve essere `approved` prima della pubblicazione.
2. **Nome, venditore e link:** ricava i dati dalla pagina ufficiale del venditore o dal feed autorizzato del network. Usa il link affiliato generato dal network; non costruire o indovinare URL di tracking.
3. **Prezzo e disponibilità:** annota la fonte e la data del controllo. Se non sono verificabili, lascia il prezzo a `null`.
4. **Commissione:** usa soltanto la percentuale e le condizioni mostrate dal network per il programma approvato. Registra la fonte e la data; non dedurre la commissione da valori di esempio.
5. **Valutazioni:** inserisci una valutazione solo se esiste una fonte verificabile e annotala. In assenza di fonte, lascia `rating` a `null`.
6. **Descrizione e caratteristiche:** scrivi soltanto affermazioni sostenute dalle fonti. Non inventare pro, contro, specifiche o promesse.
7. **Controllo finale:** verifica manualmente il link, il mercato di destinazione, la disclosure affiliate e le condizioni del programma prima di copiare i dati nel catalogo pubblicato.

## Regole di sicurezza

- Non inserire password, token, cookie o dati personali nei file del repository.
- Non pubblicare un'offerta se il programma è in attesa, rifiutato o non verificato.
- Non usare link di esempio come `https://example.com/` per offerte reali.
- Non automatizzare accettazioni di termini, iscrizioni o attivazioni di campagne senza approvazione umana.
- Il modello è una checklist operativa, non una connessione automatica ad Awin o ad altri network.
