# Kit VORLI — Mappa accessi e piano recupero per micro-team
Versione: bozza originale 0.1 — 27 ottobre 2026
Formato progettato: schede compilabili; non in vendita.

## Obiettivo
Aiutare creator e micro-team a individuare chi ha accesso ai sistemi, quale metodo di autenticazione è attivo e quali azioni eseguire quando una persona lascia il gruppo. **Non è un password manager né un archivio di credenziali.**

## Scheda A — Inventario per categorie (senza segreti)
| Categoria servizio | Ruolo responsabile (non nome personale) | Utenti autorizzati (numero) | 2FA disponibile? | Passkey disponibile? | Revisione entro |
|---|---|---:|---|---|---|
| Social media | | | | | |
| Sito e dominio | | | | | |
| Negozio / pagamenti | | | | | |
| Analisi traffico | | | | | |
| Archiviazione | | | | | |

**Non scrivere:** password, chiavi API, codici OTP, backup code, email personali, token, dati di pagamento, link riservati.

## Scheda B — Confronto strumenti (A, B, C)
| Criterio | Strumento A | Strumento B | Strumento C |
|---|---|---|---|
| Prezzo pubblico verificato + data | | | |
| Prezzo per 3 utenti | | | |
| Esportazione supportata | | | |
| 2FA per account principale | | | |
| Passkey disponibili | | | |
| Gestione ruoli e revoca | | | |
| Documentazione recupero | | | |
| Note su prova con dati fittizi | | | |

## Scheda C — Procedura di uscita di un collaboratore
1. Identificare le categorie di sistemi cui il ruolo aveva accesso.
2. Revocare le sessioni e i permessi dal pannello del servizio.
3. Ruotare le credenziali condivise eventualmente esposte (fuori da questo kit).
4. Verificare deleghe, automazioni e integrazioni di terze parti.
5. Testare con account di prova che l'accesso sia stato revocato.
6. Annotare data e ruolo responsabile senza includere dati personali.

## Scheda D — Piano di recupero
- Chi gestisce il ripristino (ruolo, non nome)?
- Quale documentazione ufficiale è stata consultata?
- È stato testato il ripristino con dati fittizi?
- Dove sono custodite **separatamente e in modo sicuro** le credenziali di recupero? (Non annotare la posizione precisa se il kit verrà condiviso.)
- Quando effettuare il prossimo controllo?

## Note commerciali e legali
Nessuna promessa di sicurezza assoluta. Nessun marchio o software è necessario per usare il kit.
Prima di una eventuale vendita digitale: verificare status fiscale del venditore italiano, termini di vendita, disclosure, privacy, recesso e funzione online ove applicabile. Nessun checkout o pagamento attivo.
Fonti di orientamento, consultate il 27/10/2026:
- https://europa.eu/youreurope/business/selling-in-eu/selling-goods-services/ecommerce-distance-selling/index_en.htm
- https://www.gazzettaufficiale.it/eli/id/2026/01/08/26G00002/SG
- https://www.agcm.it/media/comunicati-stampa/2017/7/alias-8853
