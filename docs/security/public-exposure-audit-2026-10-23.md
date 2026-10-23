# Audit pubblicazione e riservatezza — 23 ottobre 2026

> Revisione tecnica in bozza. Nessuna autorizzazione alla pubblicazione o al merge.

## Evidenze controllate (23/10/2026)

- Repository GitHub **pubblico**, branch di produzione `main`.
- `data/config.json` in `main` contiene ancora valori identificativi nei campi `owner` e `contact`. **Non riprodurre tali valori in documenti, log o report.**
- Nel branch di questa PR gli stessi campi sono vuoti. La modifica **non** elimina le versioni precedenti dalla cronologia Git e **non** corregge automaticamente il branch `main`.
- `site/dashboard.html` esiste in `main`. Il contenuto letto è una pagina HTML statica con intestazione e tabella vuota; non sono state osservate credenziali in questo singolo file. **L'accessibilità della pagina sul dominio GitHub Pages non è stata confermata**: il tentativo di apertura dal controllo esterno non ha fornito un esito utilizzabile.
- Il file `site/index.html` contiene attualmente `robots=noindex,nofollow`. Questa direttiva **non** è un controllo di accesso né una garanzia di riservatezza.

## Controlli obbligatori prima di un eventuale merge

1. Verificare il workflow di build/deploy e l'elenco completo dei file pubblicati; escludere configurazioni, report interni, dashboard amministrative e file con dati personali dall'artefatto pubblico.
2. Verificare direttamente gli URL effettivamente distribuiti dal sito, con e senza autenticazione, senza presumere che `noindex` protegga i contenuti.
3. Cercare eventuali dati personali o segreti nella cronologia Git e negli artefatti già distribuiti; l'azzeramento nel branch non risolve esposizioni pregresse.
4. In caso di esposizione di token/credenziali, revocarli e ruotarli fuori dal repository; valutare con attenzione gli obblighi di gestione dell'incidente.
5. Tenere questa PR **in bozza** fino a revisione esplicita. Nessun deploy, merge o attivazione di pagamenti autorizzati.

## Limiti della verifica

Controllati tramite connettore GitHub i file indicati e i metadati del repository. Non sono stati eseguiti test autenticati sul sito pubblicato, audit dell'intera cronologia o verifica di tutti gli artefatti di deploy. Nessuna conclusione definitiva sull'assenza di esposizioni.

Fonti interne: `data/config.json` (`main` e branch PR #41), `site/dashboard.html` (`main`), `site/index.html` (`main`), metadati del repository. Data verifica: 2026-10-23.
