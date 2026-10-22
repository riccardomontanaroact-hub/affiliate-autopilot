# Registro prodotti digitali — stato lancio

Aggiornato: 2026-10-22

## Regola di pubblicazione

Un file PDF finito non equivale a un prodotto vendibile: per dichiararlo acquistabile occorrono il file finale caricato sulla piattaforma, prezzo e descrizione corretti, copertina, pagamento attivo, consegna automatica configurata e un test del percorso d'acquisto. Non pubblicare file a pagamento in questo repository pubblico.

## Prodotti AZETA Editing / Payhip

### 1. Manuale di scrittura creativa
- File PDF presente nella libreria: `manuale_di_scrittura_creativa_primo_romanzo.pdf`
- Prezzo stabilito: €12,90
- Stato: PDF presente; scheda Payhip risultava salvata con titolo, prezzo e descrizione.
- Da completare: controllare copertina associata, anteprima pubblica, disponibilità del download, collegamento del processore di pagamento e test di acquisto/consegna.
- Non dichiarare checkout attivo finché non testato.

### 2. Metodo: Scrivere un romanzo in 3 mesi
- File PDF presente nella libreria: `metodo_scrivere_un_romanzo_in_3_mesi.pdf`
- Prezzo stabilito: €17,90
- Stato: PDF presente; scheda Payhip risultava salvata con titolo, prezzo e descrizione.
- Da completare: controllare copertina associata, anteprima pubblica, disponibilità del download, collegamento del processore di pagamento e test di acquisto/consegna.
- Non dichiarare checkout attivo finché non testato.

### 3. Guida al preventivo personalizzato
- File PDF presente nella libreria: `Guida al preventivo AZETA Editing.pdf`
- Stato: guida informativa esistente; ruolo commerciale e prezzo non confermati.
- Da completare: decidere se usarla come risorsa gratuita/lead magnet o come prodotto a pagamento, poi impostare la scheda coerentemente. Non assegnare un prezzo automaticamente.

## Prodotto VORLI

### 4. Casa Smart senza sorprese
- Sorgente editoriale: `vault/products/casa-smart-senza-sorprese-bozza-01.md`
- PDF di lavoro generato il 2026-10-22: `VORLI_Casa_Smart_senza_sorprese_v1.pdf` (conservato nella sessione di lavoro, non in questo repository pubblico).
- Stato: prima versione PDF impaginata; revisione finale, test accessibilità/leggibilità e controllo fonti ancora necessari.
- Prezzo: non definito.
- Checkout e consegna: non configurati.
- Da completare: revisione contenuti e fonti, verifica resa su telefono e stampa, copertina finale, decisione prezzo, caricamento su una piattaforma di vendita, termini e informativa applicabili, test di acquisto e consegna.

## Blocco tecnico sul catalogo affiliato

Il segnaposto dimostrativo in `data/products.json` è stato rimosso dal catalogo pubblico. I prodotti digitali sopra elencati sono gestiti separatamente dalle offerte affiliate: non devono essere inseriti in `data/products.json` come se fossero offerte di merchant.

## Ruoli dei cinque agenti

- Coordinatore e Stratega: mantiene l'ordine delle dipendenze e segnala i blocchi.
- Creatore del Sito e Catalogo: controlla pagine e build.
- Monetizzatore: verifica che le schede non vengano presentate come vendibili prima del checkout.
- Designer e SEO: controlla copertine, metadati, accessibilità e presentazione.
- Promotore e Partnership: prepara materiali di lancio; non invia contatti o campagne.

Gli agenti attualmente presenti nel repository eseguono audit deterministici; non possono accedere a Payhip, caricare file su un account esterno, collegare pagamenti o pubblicare schede per conto dell'utente. Le azioni commerciali vanno confermate e verificate sulla piattaforma.
