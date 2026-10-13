# VORLI — Piano QA e correzioni Casa Smart v0.3 (13 ottobre 2026)

Stato: documento interno; nessuna pubblicazione o vendita. Base di lavoro: branch `vorli/product-casa-smart-checklist-20261013-0510`, scheda HTML v0.2.

## Miglioramento prioritario individuato
La v0.2 calcola solo `prezzo iniziale + 3 × canone annuale` e richiede la compilazione del campo annuale anche se il dispositivo non ha abbonamento. Un utente potrebbe lasciare vuoto il campo e non ottenere alcuna stima. La scheda non separa accessori una tantum e abbonamenti mensili.

## Specifica proposta per la v0.3
Aggiungere tre campi facoltativi non negativi: accessori iniziali, abbonamento mensile e abbonamento annuo. Il prezzo iniziale resta obbligatorio e può valere zero. Campi facoltativi vuoti valgono zero. Calcolo: `totale indicativo su 36 mesi = prezzo iniziale + accessori iniziali + 36 × canone mensile + 3 × canone annuo`. Avvertire di non duplicare lo stesso canone nei campi mensile e annuale. Escludere e dichiarare costi energetici, aumenti di prezzo, riparazioni, imposte e altre spese non inserite.

## Vettori di test aritmetici
| Prezzo | Accessori | Mensile | Annuale | Totale atteso 36 mesi |
|---:|---:|---:|---:|---:|
| 100 € | 0 € | 0 € | 0 € | 100 € |
| 100 € | 20 € | 5 € | 10 € | 330 € |
| 0 € | 0 € | 0 € | 0 € | 0 € |
| 249,99 € | 29,90 € | 3,99 € | 0 € | 423,53 € |

Questi quattro vettori sono stati verificati aritmeticamente il 13 ottobre 2026. Non equivalgono a un test del browser né a una verifica del PDF stampato.

## QA ancora da svolgere
- Aggiornare l'HTML della scheda sul branch separato; verificare che il calcolo reagisca a ogni campo.
- Verificare campo prezzo vuoto, input negativi, importi molto elevati, decimali e reset.
- Provare con tastiera, lettore schermo, smartphone e stampa PDF A4.
- Mantenere avvertenza BOZZA visibile in stampa; non raccogliere dati e non aggiungere chiamate di rete.

## Contesto commerciale e fonti (consultate 13 ottobre 2026)
- Commissione europea, Cyber Resilience Act: https://digital-strategy.ec.europa.eu/en/policies/cra-summary . Gli obblighi principali si applicano dall'11 dicembre 2027, quelli di segnalazione dall'11 settembre 2026. Non affermare che ogni prodotto in vendita oggi sia già conforme al regime completo.
- Awin, eWeki IT (advertiser 19988): https://ui.awin.com/merchant-profile/19988 . Settore dichiarato: elettronica di consumo; cookie pubblicizzato 30 giorni. Nessuna prova di approvazione VORLI o commissione effettiva.
- Awin, FAQ italiana: https://www.awin.com/it/faq . La durata dei cookie può variare da programma a programma, così come l'attribuzione.

## Piano SEO organico, non-spam
Articolo futuro: «Presa smart: il costo reale in tre anni (e cosa controllare prima dell'acquisto)». Intento informativo: chiarire compatibilità, aggiornamenti e costi ricorrenti, mostrare un esempio ipotetico e offrire la scheda dopo revisione. Niente recensioni o guadagni inventati, né link affiliati non autorizzati. Nessuna pubblicazione prima di autorizzazione.

## Limiti commerciali e fiscali
Nessun account, pagamento, candidatura o vendita attivati. Per vendita diretta a consumatori UE, verificare prima obblighi IVA, diritti dei consumatori, gestione di contenuti digitali e posizione fiscale del venditore individuale italiano con un professionista. Non presumere che un piano gratuito equivalga a zero commissioni.
