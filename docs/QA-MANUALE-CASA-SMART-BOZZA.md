# QA manuale — Casa Smart senza sorprese (bozza HTML)

**Stato:** checklist di verifica; non equivale a un'approvazione finale. I test automatici aggiornati sono passati; restano da svolgere le verifiche manuali indicate sotto, inclusa la prova con tastiera/lettore di schermo.
**Ultimo controllo automatico HTML/PDF:** GitHub Actions run 68, 17 ottobre 2026, esito positivo sul commit `d7f8ddd88e456058cf9f98eb4150a52819fc24f6`. Chromium ha verificato titolo, ancore interne, testo/stato del toggle dell'avviso di bozza, link esterni previsti e assenza di overflow a 360/390 px; ha generato screenshot mobile/desktop e PDF A4 di 6 pagine. `pdfinfo` riporta `Tagged: yes`. La sezione «Compro o aspetto?», «La mia decisione», le fonti e il piè di pagina risultano nella stessa pagina finale (pagina 6). **Importante:** la presenza dei tag è un controllo automatico preliminare, non dimostra da sola ordine di lettura corretto né piena accessibilità del PDF. Revisione visiva su dispositivo reale, prova con tastiera/lettore di schermo e verifica manuale del PDF restano da completare.
**File da verificare:** `vault/products/casa-smart-senza-sorprese-layout-bozza-02.html`  
**Rilascio:** bloccato finché i controlli richiesti e l'approvazione del proprietario non sono completati.

## Controlli statici
- [ ] HTML valido e struttura semantica corretta.
- [ ] Link «Salta al contenuto principale» raggiungibile da tastiera e destinazione corretta.
- [ ] Tabella con didascalia e intestazioni di colonna esplicite.
- [ ] Ogni collegamento dell'indice punta a un ID esistente.
- [ ] Tutti i pulsanti hanno un'etichetta comprensibile e stato accessibile.
- [ ] La funzione mostra/nascondi aggiorna testo, visibilità e `aria-expanded` in modo coerente.
- [ ] Nessun dato personale, password, token o segreto incluso.
- [ ] I link esterni sono quelli delle fonti istituzionali dichiarate e vengono ricontrollati prima del rilascio.

## Prova su telefono
- [ ] Aprire il file HTML su uno schermo stretto (circa 360 px).
- [ ] Verificare che non compaia scorrimento orizzontale della pagina.
- [ ] Controllare leggibilità, spazi, campi da compilare e tabella.
- [ ] Attivare entrambi i pulsanti e verificare che funzionino.
- [ ] Navigare l'indice e tornare alla sezione precedente.
- [ ] Verificare focus visibile usando tastiera o strumenti di accessibilità disponibili.

## Prova stampa/PDF
- [ ] Aprire la funzione Stampa / salva in PDF.
- [ ] Controllare formato A4, margini, copertina e interruzioni pagina.
- [ ] Verificare che la barra degli strumenti non venga stampata.
- [ ] Controllare che tabelle e campi non siano tagliati o sovrapposti.
- [ ] Controllare leggibilità in scala di grigi e contrasto.
- [ ] Aprire il PDF prodotto su telefono e desktop.

## Revisione contenuti e fonti
- [ ] Ricontrollare le fonti istituzionali e la data di aggiornamento.
- [ ] Verificare la pertinenza per il pubblico italiano/UE; non presentare la guida come consulenza tecnica o legale.
- [ ] Revisione editoriale italiana e controllo refusi.
- [ ] Verificare diritti di testi, immagini e font (la bozza non deve includere materiali non autorizzati).

## Gate di rilascio
- [ ] Tutti i controlli sopra completati e documentati.
- [ ] Verificare separatamente l'accessibilità effettiva del PDF esportato: il PDF automatico risulta tagged, ma ordine di lettura e struttura devono ancora essere controllati manualmente.
- [ ] Eventuali problemi corretti e testati di nuovo.
- [ ] Revisione umana finale e approvazione esplicita.
- [ ] Prezzo, termini, privacy, fiscalità, pagamento e consegna valutati separatamente.
- [ ] Nessuna pubblicazione nel catalogo acquistabile finché i gate non sono soddisfatti.

**Nota:** non dichiarare un controllo superato senza averlo eseguito realmente. Nessun prezzo, pagamento o vendita è autorizzato da questa checklist.
