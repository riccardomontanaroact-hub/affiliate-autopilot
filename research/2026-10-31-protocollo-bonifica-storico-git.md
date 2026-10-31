# VORLI — protocollo di bonifica della cronologia Git (bozza, non eseguibile)

**Verifica:** 31 ottobre 2026. **Ambito:** repository pubblico e PR di lavoro. **Stato:** proposta di sicurezza, non autorizza merge, riscritture della storia, pubblicazioni o modifiche in produzione.

## Perché serve
Un controllo diretto della versione `main` ha confermato che un file JSON di ricerca contiene ancora un identificativo publisher e un URL affiliato con parametri di attribuzione. Sul branch di questa PR i relativi campi sono stati sostituiti con `null`, ma **la sola PR in bozza non modifica `main`, la versione già pubblicata o i commit storici**. I diff delle PR, le cache e i cloni possono conservare copie dei dati.

**Classificazione:** un ID publisher o un link di attribuzione non equivale necessariamente a password, chiave API o token di accesso. Resta tuttavia materiale che VORLI ha scelto di non diffondere nel codice pubblico. Non dichiarare compromissioni di account senza evidenze.

## Sequenza di intervento, solo dopo autorizzazione esplicita
1. **Inventario privato:** individuare tutti i riferimenti nei branch, nei tag, nei diff PR, nelle pagine già distribuite e negli artefatti CI; registrare i dettagli sensibili **fuori dal repository e dalle PR pubbliche**. Non riportare valori, link completi o dati personali nei ticket.
2. **Contenimento nel codice corrente:** verificare che la correzione proposta rimuova i valori dalle versioni destinate a essere pubblicate. Testare anche HTML, JSON, sitemap, bundle generati e output del deploy. Non considerare la sola ricerca statica come verifica completa.
3. **Revisione dell'impatto:** esaminare tutte le PR aperte e i branch che derivano dalla vecchia storia. Valutare rischio di reintroduzione e necessità di chiusura/ricreazione di PR. Evitare merge automatici o aggiornamenti massivi.
4. **Decisione sulla cronologia:** distinguere fra bonifica dei file correnti e riscrittura dello storico. Quest'ultima può richiedere `git-filter-repo --sensitive-data-removal`, force-push coordinati e interventi di GitHub Support sulle viste memorizzate; ha effetti su SHA, firme, branch e PR. **Non eseguirla automaticamente.**
5. **Credenziali:** solo se l'inventario rivela veri segreti di autenticazione, revocarli/ruotarli con precedenza. Non trattare un normale identificativo di affiliazione come se fosse una password.
6. **Verifica finale:** controllare nuovamente i file correnti, i risultati dei test, i diff delle PR e la distribuzione effettiva; annotare ciò che non è verificabile (cache esterne, cloni, dashboard privata).
7. **Gate commerciale:** non attivare CTA affiliate, vendite dirette o raccolta di dati cliente fino a verifica separata delle condizioni contrattuali, della privacy e degli obblighi legali. Le informazioni pubbliche obbligatorie del venditore, quando applicabili, richiedono un canale appropriato: non vanno semplicemente omesse.

## Limiti della verifica del 31/10/2026
- **Confermato:** la versione `main` contiene ancora i campi con dati di attribuzione; il branch di questa PR li ha impostati a `null`.
- **Non verificato:** bonifica completa di ogni ref, diff, cache, fork o pagina già pubblicata; esito della CI; eventuali revoche in dashboard del network.
- **Azione sicura in questa fase:** mantenere questa PR in bozza e usare la checklist per pianificare una revisione umana prima di qualsiasi rilascio.

## Fonte primaria
- GitHub Docs, *Removing sensitive data from a repository* (consultata 31/10/2026): https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository

Nessun identificativo personale, indirizzo email, URL di tracking o credenziale deve essere copiato in questo documento.
