# VORLI — Preflight recensioni e minimizzazione dati
Data verifica: 29 ottobre 2026. Stato: ricerca e proposta, **non** pubblicato in produzione.

## Novità verificata
Il 13 ottobre 2026 l'AGCM ha adottato le Linee guida sulle recensioni online (delibera 32067), pubblicate il 19 ottobre. Il mandato della legge 34/2026 riguarda in modo specifico ristorazione e turismo; l'AGCM precisa tuttavia ai paragrafi 5 e 10 che i principi del Codice del consumo offrono indicazioni interpretative anche per altri ambiti merceologici. Non applicare automaticamente al commercio tech la regola settoriale dei 30 giorni.

Per VORLI, che propone guide, confronti e in prospettiva schede affiliate, l'assenza di una prova di acquisto significa che non si deve chiamare una testimonianza “recensione verificata”. Evitare rating sintetici non documentati, stelline fittizie, testimonianze inventate e markup Review/AggregateRating non sostenuto da recensioni reali.

## Controlli operativi per future recensioni
1. **Fonte e tipo**: distinguere valutazione redazionale, prova diretta, specifica del produttore e recensione di un consumatore; non confonderle.
2. **Autenticità**: se si pubblicano recensioni dei clienti, documentare misure ragionevoli e proporzionate di verifica dell'esperienza, senza proclamare “acquisto verificato” in assenza di evidenza.
3. **Trasparenza**: rendere accessibili, accanto alle recensioni, criteri di raccolta, moderazione, selezione, calcolo dei punteggi e presenza di incentivi.
4. **Equilibrio**: non selezionare soltanto giudizi positivi, non indurre la rimozione di quelli negativi e non fornire modelli precompilati positivi.
5. **Incentivi**: non subordinare un vantaggio a un giudizio favorevole; quando pertinente, segnalare in modo evidente l'incentivo anche se non influenza il contenuto.
6. **Reclami**: predisporre gestione motivata delle contestazioni e registro delle decisioni, senza pubblicare dati personali.
7. **Privacy**: minimizzare le informazioni trattate per verificare un acquisto; evitare di conservare documenti fiscali, indirizzi IP o ricevute senza una base giuridica, policy e adeguate misure.
8. **Obsolescenza**: definire criteri oggettivi per recensioni superate, identici per positive e negative.
9. **Affiliazione**: disclosure visibile vicino a raccomandazioni monetizzate; non presentare l'affiliazione come test indipendente o esperienza d'uso.

## Rilievo tecnico sul repository (solo audit, non pubblicazione)
Alla verifica del 29 ottobre, il branch principale conteneva recapiti e un nominativo in file di configurazione e collegamenti di contatto nel footer di più pagine sorgente e generate. Questa proposta elimina i riferimenti diretti nei file interessati **solo nel branch di lavoro**, sostituendoli con una dicitura che richiede la definizione di un canale conforme prima di vendere. Non affermare che le informazioni siano state eliminate dalla cronologia Git o da copie già pubblicate: la rimozione da branch/PR non cancella la storia, né aggiorna il sito pubblico.

La rimozione dei recapiti non è una soluzione definitiva di compliance: prima di avviare vendite occorre verificare e pubblicare le informazioni obbligatorie sul professionista e un contatto adeguato, senza usare dati privati nel codice o nei report. Anche l'eventuale vendita da persona fisica italiana, partita IVA e IVA sui digitali richiedono una valutazione qualificata sul caso concreto.

## Stato e decisioni
- Nessuna recensione cliente verificata acquisita con questa ricerca; non inserire stelle o punteggi.
- Nessuna conclusione fiscale o autorizzazione a vendere.
- Le modifiche restano in PR **draft**, senza merge o deploy.
- Verificare separatamente eventuali ulteriori copie di recapiti e la storia pubblica; non assumere che l'elenco di file esaminati sia esaustivo.
- Non memorizzare in repository pubblico messaggi Awin, credenziali, tracking link, dati cliente.

## Fonti ufficiali consultate il 29/10/2026
- AGCM, linee guida delibera 32067, 13/10/2026: https://www.agcm.it/dotcmsdoc/normativa/consumatore/LLGG_Recensioni_online_Ott2026.pdf (parr. 4–5, 10–11, 17–30, 32).
- AGCM, comunicato del 19/10/2026: https://www.agcm.it/media/comunicati-stampa/2026/10/Pubblicate-le-Linee-Guida-per-le-recensioni-online
- AGCM, trasparenza delle promozioni commerciali: https://agcm.it/media/comunicati-stampa/2025/6/PS12814-PS12815-PS12816-PS12817-PS12818-PS12826

Documento informativo e di controllo editoriale, non consulenza legale o fiscale.
