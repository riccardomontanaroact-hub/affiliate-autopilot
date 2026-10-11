# Abilitare le revisioni AI di VORLI (facoltativo)

## Stato predefinito

La revisione con modello AI è disattivata. Il workflow continua a eseguire i cinque controlli locali e pubblica il rapporto deterministico. Nessuna richiesta API viene inviata finché non sono impostati entrambi i parametri seguenti.

## Prima di abilitarla

1. Verificare nell'account OpenAI API se è disponibile un progetto API e quali modelli sono abilitati.
2. Verificare tariffe e impostare un limite di spesa e avvisi nel pannello API prima dell'uso. L'API può comportare costi separati dall'abbonamento ChatGPT.
3. In GitHub aprire Settings → Secrets and variables → Actions.
4. In Secrets creare OPENAI_API_KEY con una chiave dedicata. Non inserirla nei file del repository, nei log o nelle chat.
5. In Variables creare VORLI_LLM_ENABLED con valore true.
6. Facoltativamente, in Variables impostare OPENAI_MODEL con un modello disponibile nel progetto API. Se omesso, il codice usa gpt-6-astra; verificarne la disponibilità nel proprio account.
7. Eseguire il workflow manualmente una volta e controllare il rapporto e il consumo API. Per disabilitare, impostare VORLI_LLM_ENABLED a false o rimuovere il secret.

## Limiti e sicurezza

- Una richiesta per ciascuno dei cinque ruoli; il consumo dipende dal modello e dalla lunghezza dei rapporti.
- Il payload invia solo i risultati dei controlli e i rilievi pertinenti, non le chiavi o altre variabili segrete.
- Le richieste usano store=false; verificare comunque le condizioni correnti del servizio prima dell'uso.
- I modelli possono sbagliare: i suggerimenti non sono fatti verificati.
- Gli agenti non possono pubblicare prodotti, modificare il sito, inviare email, contattare partner, spendere denaro o attivare checkout/campagne.
- Le decisioni commerciali e qualsiasi azione esterna restano subordinate all'approvazione umana.
