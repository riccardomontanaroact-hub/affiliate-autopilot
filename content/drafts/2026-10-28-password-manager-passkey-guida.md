---
title: "Password manager e passkey: 8 controlli prima di scegliere"
description: "Guida indipendente per creator e piccoli progetti digitali: password uniche, passkey, MFA, recupero account, esportazione e costi da verificare."
slug: "password-manager-passkey-controlli-scelta"
status: "draft"
language: "it"
last_reviewed: "2026-10-28"
intent: "informational"
review_required: true
---

# Password manager e passkey: 8 controlli prima di scegliere

Un creator può gestire email, hosting, social, piattaforme di vendita e strumenti di lavoro da più dispositivi. Riutilizzare la stessa password su questi servizi è rischioso: una credenziale sottratta in un incidente può essere provata anche altrove. Un **password manager** aiuta a creare e conservare password differenti; una **passkey**, dove supportata, permette un accesso basato su chiavi crittografiche legate al servizio. Non sono sinonimi e possono coesistere.

**Nota editoriale:** questa è una guida informativa originale, non un test comparativo di prodotti. Nessun software è stato provato per conto di VORLI; non ci sono prezzi, punteggi, link affiliati o affermazioni di sicurezza assoluta. La bozza richiede revisione prima della pubblicazione.

## 1. Le password sono davvero uniche?

Controlla che lo strumento possa generare password lunghe e diverse per ciascun account. ENISA raccomanda password o passphrase robuste e uniche, preferibilmente gestite da un password manager. NIST indica la lunghezza come fattore fondamentale e raccomanda di consentire password manager e compilazione automatica nei servizi che richiedono password.

**Verifica pratica:** scegli tre account non sensibili di prova e controlla se il gestore propone credenziali differenti senza copiarle manualmente tra applicazioni. Non inserire credenziali reali in fogli condivisi o screenshot.

## 2. Supporta MFA e come protegge il caveau?

La password principale, se prevista, protegge molte credenziali: chiedi se il gestore offre autenticazione a più fattori (MFA) per il proprio account e quali metodi supporta. NIST raccomanda di scegliere un gestore che supporti MFA. Verifica anche i requisiti del dispositivo e le modalità di sblocco: comodità e protezione devono essere valutate insieme.

**Domanda da annotare:** quali controlli restano disponibili se perdi il telefono principale?

## 3. Che differenza c'è tra passkey e codice temporaneo?

Una passkey conforme a FIDO2/WebAuthn può essere resistente al phishing grazie al legame crittografico con il dominio del servizio. Un codice OTP digitato manualmente, pur utile come secondo fattore, non offre la stessa proprietà di resistenza al phishing secondo NIST. **Non significa che una passkey renda impossibile ogni frode**: restano importanti sicurezza del dispositivo, recupero account e attenzione ai messaggi ingannevoli.

Verifica quali servizi supportano effettivamente passkey e se puoi usare un dispositivo alternativo.

## 4. Posso recuperare l'accesso senza indebolire la sicurezza?

Prima di migrare tutte le credenziali, leggi le procedure ufficiali per recupero, perdita di dispositivo, codici di emergenza e account bloccato. Conserva i codici di recupero secondo le istruzioni del servizio, separatamente dal dispositivo che potresti perdere. Non pubblicare né condividere chiavi, codici o schermate di configurazione.

**Mini-esercizio:** descrivi su carta la procedura per accedere ai servizi essenziali se il tuo smartphone non fosse disponibile. Non includere password o codici reali nella scheda.

## 5. Funziona sui miei dispositivi e browser?

Controlla compatibilità dichiarata con smartphone, computer e browser effettivamente utilizzati. Verifica eventuali limiti del piano gratuito: numero di dispositivi, sincronizzazione, accesso offline e assistenza. Non dedurre queste caratteristiche dal solo nome del piano; leggi condizioni e documentazione aggiornate.

## 6. Come posso esportare o trasferire i dati?

Un gestore non dovrebbe diventare una dipendenza irreversibile. Verifica le opzioni di esportazione, importazione, cancellazione e chiusura dell'account. Un'esportazione può contenere segreti in chiaro: eseguila solo quando necessario, su un dispositivo affidabile, e proteggi o elimina il file secondo le istruzioni del produttore. Non caricare esportazioni su repository pubblici o servizi non destinati a custodire credenziali.

## 7. Quanto costa davvero dopo il periodo iniziale?

Confronta piano gratuito, rinnovo, eventuali limiti funzionali e costi per più utenti o dispositivi. Registra prezzo e data direttamente dalla pagina ufficiale del fornitore, senza assumere che un'offerta temporanea rimanga valida. Per un progetto individuale, la priorità non è il piano più costoso, ma una soluzione sostenibile e recuperabile.

## 8. Cosa succede in caso di incidente?

Verifica se il fornitore pubblica procedure per incidenti, aggiornamenti di sicurezza e segnalazione di vulnerabilità. Mantieni aggiornati sistema operativo e app; usa MFA dove disponibile. Se una password risulta compromessa, cambiala sul servizio interessato e controlla gli accessi recenti, seguendo le indicazioni ufficiali.

## Scheda di confronto compilabile (senza dati sensibili)

| Criterio | Soluzione A | Soluzione B |
| --- | --- | --- |
| Password uniche e generatore | Da verificare | Da verificare |
| MFA per accesso al gestore | Da verificare | Da verificare |
| Passkey e compatibilità | Da verificare | Da verificare |
| Recupero account documentato | Da verificare | Da verificare |
| Dispositivi/browser supportati | Da verificare | Da verificare |
| Esportazione e cancellazione | Da verificare | Da verificare |
| Costi e rinnovo (con data) | Da verificare | Da verificare |
| Aggiornamenti e assistenza | Da verificare | Da verificare |

Non inserire nella tabella credenziali, codici di recupero, indirizzi personali o identificativi degli account.

## Domande frequenti

**Basta una password lunga?** No. La lunghezza conta, ma riutilizzare la stessa password su servizi diversi aumenta il rischio. Quando possibile, usa credenziali uniche e MFA.

**Passkey e password manager sono alternative?** Non necessariamente: alcuni gestori possono supportare anche passkey, ma disponibilità e modalità di sincronizzazione dipendono dal prodotto e dal servizio.

**Devo cambiare tutte le password ogni mese?** Non esiste una regola universale che imponga cambi periodici indiscriminati. È prioritario sostituire password compromesse e seguire le indicazioni di sicurezza del servizio.

## Trasparenza commerciale e pubblicazione

Se in futuro questa guida conterrà collegamenti remunerati, indicare in modo evidente la natura pubblicitaria/di affiliazione prima dei collegamenti pertinenti; non presentare consigli sponsorizzati come test indipendenti. Le condizioni economiche e l'idoneità del programma vanno verificate separatamente nella piattaforma di affiliazione. Nessun collegamento tracciato è inserito in questa bozza.

## Fonti primarie e verifica — 28 ottobre 2026

- ENISA, **Cyber Hygiene**, pratiche consigliate su password, passkey e MFA: https://www.enisa.europa.eu/topics/cyber-hygiene
- NIST, **How Do I Create a Good Password?**, password manager, MFA e lunghezza: https://www.nist.gov/cybersecurity-and-privacy/how-do-i-create-good-password
- NIST, **SP 800-63B, Authenticators**, requisiti e differenza tra OTP e autenticazione resistente al phishing: https://pages.nist.gov/800-63-4/sp800-63b/authenticators/
- AGCM, comunicato 11 giugno 2025, riconoscibilità della pubblicità: https://www.agcm.it/media/comunicati-stampa/2025/6/PS12814-PS12815-PS12816-PS12817-PS12818-PS12826

**Stato editoriale:** bozza, nessun test eseguito, nessuna affiliazione attribuita, nessun prezzo o commissione inventata, nessuna pubblicazione autorizzata.
