# VORLI - QA avvisi permanenti (12 ottobre 2026)

Stato: proposta di correzione, non applicata. Nessuna autorizzazione alla vendita o alla pubblicazione.

## Problema verificato
Nel file HTML della guida Casa Smart senza sorprese, il pulsante di gestione delle note di bozza nasconde sia l'avviso in copertina sia quello nel piè di pagina. La verifica automatica attuale considera valido che l'avviso finale sparisca.

## Modifica minima proposta
1. Eliminare il pulsante che permette di nascondere gli avvisi e il relativo gestore JavaScript, oppure limitarlo a note editoriali non obbligatorie.
2. Mantenere visibili gli avvisi di bozza, non vendita e non pubblicazione in HTML e nella stampa PDF.
3. Aggiornare il test browser affinché controlli la presenza e la visibilità degli avvisi, invece della loro scomparsa.
4. Dopo la generazione del PDF, verificare che il testo di avvertenza sia effettivamente presente anche nel PDF.

## Gate di rilascio
Questa è una bozza. Prima di distribuire o vendere la guida servono revisione umana, controllo delle fonti, verifica tecnica del PDF e approvazione esplicita. Nessun prezzo o pagamento autorizzato.

## Fonti interne
- PR #31: https://github.com/riccardomontanaroact-hub/affiliate-autopilot/pull/31
- File HTML: vault/products/casa-smart-senza-sorprese-layout-bozza-02.html
- Workflow: .github/workflows/validate.yml

Verifica statica del codice effettuata il 12 ottobre 2026. Nessun test browser o PDF eseguito in questo intervento.
