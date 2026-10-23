# Public configuration privacy review

Date: 2026-10-17

The public configuration currently contains a contact value that may identify a person. Before any deployment, replace that value with an empty string or a verified business-only contact channel. Do not copy the original value into issues, pull requests, or documentation.

Changing the current file does not remove prior Git history. Assess repository history and cached deployments separately before treating the exposure as remediated. No production changes are authorized.

## Verifica aggiuntiva — 23 ottobre 2026

La configurazione del branch `main` contiene **due campi identificativi** (`owner` e `contact`), non soltanto un recapito. I valori non sono riprodotti qui. Nel branch di questa PR entrambi i campi sono ora stringhe vuote; nessun dato personale viene sostituito con dati inventati.

**Attenzione prima del merge:** il branch di questa PR è stato creato prima di ulteriori modifiche a `main`. Verificare il diff effettivo e l'eventuale conflitto/merge a tre vie per accertare che entrambi i campi siano vuoti nel risultato finale, e controllare i consumer della configurazione per non mostrare etichette vuote o placeholder. L'intervento non cancella la cronologia Git, le copie clonate, i cache o i deployment precedenti.

**Blocco:** nessun merge, deploy o dichiarazione di avvenuta rimozione pubblica senza revisione umana. Valutare separatamente la presenza di `site/dashboard.html` nel repository e nell'artefatto Pages; una dashboard interna non dovrebbe essere esposta al pubblico. Non includere contenuti personali o URL di tracciamento nei documenti di verifica.
