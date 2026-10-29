# Kit VORLI — Piano backup e test di ripristino per creator

**Versione:** bozza originale 0.2 · 27/10/2026 · Non in vendita · Nessun prezzo, checkout o link affiliato attivo.

## Istruzioni d'uso
Duplica questa scheda per ogni progetto o tipologia di contenuto. Compila con **nomi generici** e non con password, token, codici di recupero o dati di clienti. Esegui le prove su file fittizi.

**Ambiente di prova sicuro:** usa una cartella locale isolata, fuori dalle cartelle sincronizzate automaticamente (cloud drive, backup continuo, cartelle condivise). Rinominare o spostare una cartella sincronizzata può propagare la modifica anche alle copie remote: non usare questa simulazione su dati veri o su una cartella sincronizzata. Per valutare davvero il backup, recupera i file **dalla copia di sicurezza scelta**, non dalla cartella originale rinominata. Non scollegare, eliminare o sovrascrivere dati di lavoro per simulare un guasto.

### Scheda A — Inventario essenziale
| Tipo di file | Importanza (1–3) | Frequenza modifiche | Posizione principale (generica) | Tempo massimo accettabile per recupero | Perdita massima di lavoro accettabile |
| --- | --- | --- | --- | --- | --- |
| Video sorgenti | | | | | |
| Progetti di montaggio | | | | | |
| Audio e immagini | | | | | |
| Esportazioni finali | | | | | |
| Documenti di lavoro | | | | | |

**Come compilare le ultime due colonne:** il *tempo massimo di recupero* è quanto puoi aspettare prima di tornare a lavorare; la *perdita massima di lavoro* è quante ore o giorni di modifiche puoi tollerare di perdere. Questi obiettivi guidano la frequenza dei backup e la prova di ripristino, ma non sono garanzie del servizio.

### Scheda B — Mappa delle copie
| Copia | Supporto / servizio (categoria) | Sempre connessa? | Versioni precedenti? | Protezione accesso | Ultima verifica |
| --- | --- | --- | --- | --- | --- |
| Lavoro | | | | | |
| Backup 1 | | | | | |
| Backup 2 | | | | | |

**Controllo rischio:** se tutte le copie dipendono dallo stesso dispositivo, account o luogo, il piano può fallire per una causa comune. Per i dati critici, valuta una copia offline/non sempre raggiungibile e verifica periodicamente che sia leggibile e ripristinabile. Valuta una copia indipendente e una modalità di recupero in caso di account non accessibile.

### Scheda C — Prova di ripristino
- Data del test: __________
- Set di prova (solo file fittizi): __________
- Evento simulato (es. cancellazione accidentale): __________
- Origine della copia usata: __________
- Tempo di recupero: __________
- File aperti e verificati correttamente? Sì / No
- Progetto ricollegato ai file sorgente e riaperto nell'applicazione prevista? Sì / No / Non applicabile
- Età della versione recuperata rispetto all'ultima modifica: __________
- Il tempo e la perdita di lavoro simulata rispettano gli obiettivi della Scheda A? Sì / No
- Versione recuperata: __________
- Errori riscontrati e correzioni: __________
- Prossimo test: __________

### Esempio compilato — prova di recupero senza dati reali

*Scenario puramente illustrativo, non un test effettuato da VORLI.* Un creator ha tre file fittizi: `clip-demo.txt`, `audio-demo.txt`, `progetto-demo.txt`. L'obiettivo scelto è tornare operativo entro **2 ore** e perdere non più di **1 giorno** di modifiche. Queste sono soglie dell'esempio, non prestazioni garantite.

1. Crea i tre file di prova in una cartella `lavoro-demo` e registra il contenuto atteso di ciascuno (per esempio una frase diversa).
2. Copiali su un supporto o servizio separato, annotando l'ora della copia e se è possibile recuperare versioni precedenti.
3. **Solo nella cartella locale isolata e con file fittizi, senza cancellare gli originali**, simula l'indisponibilità della cartella di lavoro (per esempio rinominandola `lavoro-demo-non-usare`). Non farlo in cartelle cloud sincronizzate: la rinomina potrebbe propagarsi. Mantieni l'originale fuori dal percorso usato per il ripristino.
4. Ripristina i tre file **esclusivamente dal backup separato** in una **nuova** cartella `ripristino-demo`; non usare i file originali e non sovrascriverli. Se il recupero dal backup non riesce, registra l'esito negativo: non sostituirlo con una semplice copia dalla cartella di lavoro.
5. Apri tutti i file, confronta il contenuto atteso, misura il tempo effettivo e annota la data della versione recuperata. Se il progetto richiede applicazioni o media collegati, verifica anche che si apra e che i collegamenti funzionino.
6. Ripristina la situazione iniziale e conserva soltanto un verbale generico del test, senza nomi reali di clienti o percorsi sensibili.

**Esito:** `SUPERATO` soltanto se i file sono integri e utilizzabili, il tempo misurato non supera l'obiettivo e l'età della copia rientra nella perdita massima accettabile. Altrimenti `NON SUPERATO`: registra il problema, correggi il piano e ripeti la prova. Un backup «completato» senza ripristino verificato non basta per dichiarare superato il test.

**Diagnosi rapida in caso di fallimento:** file mancanti → ricontrollare cartelle incluse e filtri; versione troppo vecchia → rivedere frequenza e conservazione; file presenti ma progetto inutilizzabile → verificare dipendenze, software e file collegati; ripristino troppo lento → verificare dimensioni, velocità e disponibilità del supporto. Non effettuare prove distruttive su dati di lavoro.

**Riferimento tecnico:** CISA, *StopRansomware Guide*, v3.1 (2023), raccomanda copie offline protette e prove regolari di disponibilità e integrità: https://www.cisa.gov/sites/default/files/2023-10/StopRansomware-Guide-508C-v3_1.pdf (consultata 27/10/2026).

### Scheda D — Confronto servizi o supporti
Assegna un voto da 0 (non soddisfa) a 3 (soddisfa bene). **Non sommare il punteggio se mancano dati essenziali.**

| Criterio | Soluzione A | Soluzione B | Soluzione C |
| --- | --- | --- | --- |
| Capacità utile verificata | | | |
| Ripristino versioni precedenti | | | |
| Recupero senza dispositivo originale | | | |
| Costo totale nel tempo | | | |
| Accesso e privacy | | | |
| Facilità di esportazione | | | |
| Prova di ripristino riuscita | | | |

### Decisione e prossime azioni
La soluzione scelta è __________ perché __________. Il limite principale è __________. Prima dell'uso su file reali devo __________.

## Scheda prodotto editoriale (non commerciale)
**Titolo proposto:** Kit VORLI — Backup e ripristino per creator  
**Categoria:** organizzazione digitale / produttività  
**Destinatari:** creator, freelance, piccoli team editoriali  
**Contenuto:** inventario, mappa copie, protocollo di prova e tabella comparativa  
**Beneficio concreto:** aiutare a progettare e verificare un recupero di file senza promesse assolute di sicurezza  
**SEO title:** Kit piano backup creator e test di ripristino | VORLI  
**Meta description:** Modelli compilabili per organizzare copie di sicurezza, verificare il recupero e confrontare soluzioni di backup per file creativi.  
**CTA bozza:** «Esplora il modello» — non collegare a pagamento finché non sono completate revisione legale, fiscale e di prodotto.

## Controlli pre-commercializzazione
Revisione di accuratezza, diritti e licenze; disclosure di eventuali link affiliati; condizioni di vendita e recesso digitale; funzione online di recesso quando applicabile; trattamento dei dati; IVA e posizione fiscale italiana da verificare con professionista. Nessun diritto di recesso può essere escluso automaticamente per il solo fatto che il prodotto sia un PDF.

**Riferimenti:** https://www.cisa.gov/stopransomware/ransomware-guide ; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02011L0083-20220528 ; https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en . Consultati il 27/10/2026.
