# VORLI — verifica tecnica pre-lancio
**Data verifica:** 26 ottobre 2026  
**Stato complessivo:** preparazione in corso; non pronto per un lancio commerciale.

Questo registro documenta controlli effettuati sul repository pubblico e separa i risultati verificati dalle attività ancora da svolgere. Non equivale a un collaudo indipendente o a un’approvazione legale/fiscale.

## Controlli verificati

- [x] Repository raggiungibile e branch predefinito `main`; repository pubblico.
- [x] `data/products.json` contiene `[]`: nessuna offerta è caricata nel catalogo.
- [x] `agent/offer_validation.py` richiede URL HTTPS non dimostrativo, merchant e programma identificati, stato esplicito di approvazione, fonte e date di verifica, tasso commissionale valido e dati prezzo/rating corredati da fonti quando presenti.
- [x] `agent/build.py` usa il lockup VORLI approvato come controllo bloccante e applica regole per non presentare offerte dimostrative come acquistabili.
- [x] Le pagine sorgente `site/index.html`, `site/catalogo.html`, `site/risorse.html`, `site/guida.html` e `site/usb-c.html` includono `noindex,nofollow` al momento del controllo.
- [x] La pagina catalogo descrive chiaramente che non ci sono offerte verificate e indirizza alle risorse VORLI, non a prodotti demo.
- [x] La nuova edizione commerciale di Casa Smart è preparata fuori dal repository pubblico; non inserire il PDF commerciale in questo repository.
- [x] Le PR #74, #75 e #76 restano bozze separate e non sono state unite da questa verifica.

## Risultati e limiti

### Catalogo e affiliazioni
Il catalogo vuoto è corretto finché non sono disponibili offerte reali. Prima di aggiungere un’offerta occorre verificare nel pannello della rete l’approvazione del programma, il link personale generato, la destinazione, le condizioni, prezzo/disponibilità e disclosure. Un redirect che apre la pagina del merchant non prova da solo l’attribuzione di una commissione.

### Indicizzazione e contenuti pubblici
Il meta tag `noindex,nofollow` è un segnale per i motori di ricerca, non un controllo di accesso: il repository è pubblico e i file possono essere consultati direttamente. Non caricare materiali commerciali riservati, segreti, credenziali o dati personali. Non rimuovere `noindex` finché catalogo, pagine legali, contatti e percorso commerciale non sono pronti.

### Checkout e vendita diretta
Non risulta configurato un checkout né una consegna digitale. Mancano una scelta finale della piattaforma, il prezzo approvato, le informazioni del venditore, i termini, le informazioni precontrattuali, la procedura per recesso/rimborsi, l’assistenza, la verifica fiscale della situazione concreta e il test del percorso di acquisto/consegna. La piattaforma non è stata collegata e non è stata sostenuta alcuna spesa.

### Prodotto digitale
La guida commerciale è una bozza di lavoro, non una versione pronta alla vendita. Richiede revisione editoriale umana, verifica tecnica indipendente, controllo dei collegamenti e dei diritti, accessibilità, test su telefono/desktop/stampa e approvazione finale. Non dichiarare che sia accessibile o validata da esperti finché non esiste evidenza.

## Gate di rilascio — tutti obbligatori

- [ ] Revisione umana finale e revisione tecnica indipendente del prodotto.
- [ ] Verifica puntuale di ogni fonte e link, con data e risultato registrati.
- [ ] Controllo dei diritti di testi, immagini, font e materiali.
- [ ] PDF finale impaginato e testato su telefono, desktop e stampa; accessibilità valutata.
- [ ] Decisione del proprietario su prezzo, piattaforma e condizioni commerciali.
- [ ] Verifica fiscale/contabile con professionista per la situazione concreta del venditore.
- [ ] Informazioni precontrattuali, privacy, assistenza, recesso/rimborsi e gestione dei dati controllati.
- [ ] Account della piattaforma creato dal titolare e metodi di incasso verificati.
- [ ] Checkout e consegna configurati; prova end-to-end eseguita senza dati reali di clienti.
- [ ] Approvazione esplicita del proprietario prima di qualsiasi pubblicazione.
- [ ] Solo dopo l’approvazione: decidere se rimuovere `noindex`, aggiornare sitemap e controllare l’indicizzazione.
- [ ] Per ogni offerta affiliata: approvazione, link tracciato personale e condizioni verificati prima di inserirla nel catalogo.

## Decisioni ancora riservate al proprietario

1. Prezzo e condizioni di vendita.
2. Piattaforma finale di vendita e autorizzazione a creare/configurare l’account.
3. Approvazione del prodotto finale e della sua pubblicazione.
4. Approvazione a rimuovere `noindex` e rendere il sito ricercabile.
5. Eventuali candidature a programmi affiliati o inserimento di offerte.

## Regola di sicurezza del rilascio

Questa checklist è documentazione preparatoria. Non attiva pubblicazioni, pagamenti, candidature, email o acquisti. Non dichiarare VORLI “pronto” finché tutti i gate pertinenti non sono completati e verificati.
