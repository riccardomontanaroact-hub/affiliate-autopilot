# VORLI — triage delle PR e blocchi prima della pubblicazione
Data della verifica: 30 ottobre 2026 (Europe/Rome). Documento interno di progetto, senza dati privati.

## Evidenza verificata
- Ricerca GitHub delle PR aperte nel repository: **117 PR aperte**, tutte contrassegnate **draft** al momento della consultazione. È uno stato del repository, non un conteggio di funzioni operative già pubblicate.
- Il branch predefinito è `main`; la presenza di file in una PR non implica che siano presenti nel sito online.
- Il numero elevato di bozze rende difficile individuare una sequenza sicura di revisione e aumenta il rischio di conflitti e duplicazioni. Non è stata effettuata alcuna fusione o pubblicazione.

## Priorità di revisione (non autorizzazione al merge)
1. **Protezione dei dati — PR #136**: verificare i file pubblici e le pagine già distribuite, rimuovere dati identificativi non necessari, valutare la cronologia Git e le copie già online. I recapiti e gli obblighi informativi legali per un futuro commercio vanno gestiti separatamente: non eliminare informazioni obbligatorie senza sostituzione conforme.
2. **Qualità prodotto digitale — PR #137**: completare prove reali su browser e applicazioni per CSV; confermare accessibilità e assenza di chiamate di rete prima di distribuire il calcolatore offline.
3. **Contenuti editoriali e affiliazioni — PR #135, #138, #139**: verificare fonti e date, approvazioni nella dashboard privata, condizioni economiche individuali e disclosure; non aggiungere collegamenti di tracciamento senza autorizzazione.
4. **Consolidamento backlog**: classificare le altre bozze per tema e duplicazioni; scegliere una sola versione per contenuto e sottoporla a revisione. Evitare nuove PR per variazioni minime quando esiste già una bozza tematicamente pertinente.

## Stato commerciale verificato
- La scheda pubblica eWeki IT Awin (merchant 19988) descrive elettronica di consumo e cookie di 30 giorni. Non attesta né la commissione individuale né l'approvazione di VORLI: https://ui.awin.com/merchant-profile/19988 (consultata il 30/10/2026).
- Le comunicazioni Gmail non sostituiscono lo stato corrente della dashboard privata Awin. Inviti, comunicazioni informative, benvenuti e approvazioni esplicite devono rimanere categorie distinte.
- Non utilizzare numeri di commissione non verificati, prezzi promozionali senza data, vendite o ricavi presunti.

## Gate obbligatori
- Nessun merge, deploy, account, pagamento, candidatura o email da questa checklist.
- Revisione editoriale/tecnica prima di pubblicare; verifica legale/fiscale professionale prima di vendite dirette e pagamenti.
- Per contenuti digitali a pagamento verificare obblighi sul recesso; la soglia UE di 10.000 euro per specifiche vendite transfrontaliere non equivale a una franchigia generale dalla partita IVA.
- Pubblicare dichiarazioni di affiliazione riconoscibili e contenuti originali, evitando SEO spam.

## Fonti pubbliche
- GitHub: elenco PR del repository, consultato il 30/10/2026: https://github.com/riccardomontanaroact-hub/affiliate-autopilot/pulls
- Awin eWeki IT, consultata il 30/10/2026: https://ui.awin.com/merchant-profile/19988
- Direttiva sui diritti dei consumatori (versione consolidata), consultata il 30/10/2026: https://eur-lex.europa.eu/eli/dir/2011/83/2022-05-28

Questa nota è una fotografia del backlog, non una decisione di pubblicazione.

## Verifica regressione privacy del 30/10/2026 (05:08 CET)
- Aggiunto `tests/privacy-public-files-smoke.js` **alla PR #136 già in bozza**: comando previsto `node tests/privacy-public-files-smoke.js`, senza dipendenze o rete.
- Controlla i sei HTML di `site/` e `preview/vorli-next/` più `data/config.json`: niente indirizzi email o `mailto:` nei sei HTML, niente parametri comuni di tracking affiliato nei sei HTML, contatto vuoto e intestazione del progetto generica nel JSON.
- I **sette file del branch** sono stati verificati anche tramite lettura diretta dal repository: nei sei HTML nessuna corrispondenza ai pattern email, `mailto:` o parametri di tracking controllati; nel JSON il campo di contatto è vuoto. Il nuovo script non è stato eseguito in Node in questa sessione: rimane da eseguire in un ambiente che abbia il branch.
- **Limiti:** non copre altri file, dati codificati/obfuscati, dati storici Git, copie esterne o il sito in produzione. Non sostituisce una revisione legale dei contatti obbligatori.
- **Blocco confermato:** il `data/config.json` di `main` conserva ancora recapiti e nome del gestore; la PR non cambia `main` né il sito pubblico. Non confondere il test di un branch con una bonifica già distribuita.

## Verifica di esecuzione isolata — 30/10/2026, 06:12 CET
- Eseguita **la logica JavaScript effettiva** di `tests/privacy-public-files-smoke.js` su copie dei sette file letti dal branch via connettore GitHub, usando un harness JavaScript con filesystem simulato. **Esito: PASS** sui sei HTML e su `data/config.json`.
- Eseguite due prove negative con dati sintetici: inserendo un indirizzo email di esempio in `site/index.html`, il controllo **fallisce correttamente**; inserendo un parametro di tracciamento di esempio, il controllo **fallisce correttamente**. Nessun valore reale o collegamento affiliato è stato salvato.
- **Limite esplicito:** non è un'esecuzione di Node.js nel checkout reale del repository. Il comando Node resta da provare in un ambiente con accesso al branch. Non verifica file non inclusi, dati codificati, cronologia Git o sito pubblico.
- Confronto con `main`: nei sei HTML corrispondenti sono ancora presenti indirizzi email e collegamenti `mailto:`; anche il file di configurazione principale contiene un recapito e un nominativo. I valori non sono riportati qui. **Blocco privacy irrisolto**: la bozza non ha modificato `main` né le copie già distribuite. Non procedere al deploy senza revisione dei recapiti legalmente necessari e del trattamento dei dati preesistenti.
