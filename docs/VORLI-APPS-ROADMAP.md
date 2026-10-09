# VORLI — Piano delle due applicazioni

## Obiettivo
Due applicazioni distinte, collegate a un backend e catalogo condivisi:
1. **VORLI Control**: pannello privato del proprietario, installabile come PWA; non accessibile pubblicamente senza login.
2. **VORLI Shopping**: app Android pubblica per i clienti, da preparare per Google Play dopo la validazione del sito.

## Sicurezza prima di tutto
- GitHub Pages è hosting statico: NON è sufficiente per proteggere un pannello privato. Non pubblicare dati sensibili, credenziali, token, commissioni o comandi amministrativi nel frontend statico.
- Autenticazione gestita da un provider affidabile, MFA, sessioni sicure, autorizzazioni lato server e audit log.
- Nessuna chiave di advertiser, pagamento o API privata nel browser o nel repository.
- Agenti AI: approvazione umana per pubblicazioni, spese, modifiche commerciali e pagamenti; limiti, log e pulsante di arresto.

## VORLI Control — MVP
- Login privato e ruolo admin unico.
- Stato del sito e dei deployment, con errori e link diagnostici.
- Coda di approvazione delle proposte dei due agenti AI.
- Catalogo prodotti: bozze, revisioni, approvazioni, pubblicazioni.
- Dashboard con click, conversioni e commissioni **solo quando arrivano dati reali dalle integrazioni**.
- Notifiche per errori critici e richieste di approvazione.
- UI mobile-first e manifest PWA, dopo l'introduzione del backend sicuro.

## VORLI Shopping — MVP
- Catalogo condiviso con sito, ricerca, filtri e schede prodotto.
- Chiarezza sui link di affiliazione e sul venditore effettivo.
- Preferiti e confronti, con consenso per notifiche.
- Vendita diretta di prodotti digitali solo dopo checkout, adempimenti e integrazione pagamenti verificati.
- Preparazione Android/Play Store: privacy policy, Data Safety, account sviluppatore, test e revisione.

## Sequenza operativa
1. Ripristinare CI/CD: pubblicare solo da main e verificare i branch che falliscono per protezione github-pages.
2. Stabilizzare il catalogo mobile e testare accessibilità, prestazioni e navigazione.
3. Scegliere backend e provider auth, definire modello dati e permessi.
4. Implementare VORLI Control in ambiente protetto; testare accesso negato senza autenticazione.
5. Collegare agenti AI e integrazioni solo con credenziali server-side.
6. Realizzare VORLI Shopping riusando API/catalogo, testare e preparare rilascio Play Store.

## Criteri di completamento
- Control non espone dati amministrativi ad utenti anonimi.
- Nessun agente può eseguire azioni sensibili senza approvazione.
- Pubblicazione del sito verde su main e controlli mobile superati.
- App pubblica e pannello privato condividono dati senza condividere privilegi.

**Stato:** specifica iniziale; nessuna delle due app è ancora dichiarata sviluppata o pubblicata.
