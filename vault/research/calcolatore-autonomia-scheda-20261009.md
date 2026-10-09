# VORLI Lab — Calcolatore autonomia: scheda editoriale e test
Data: 9 ottobre 2026. Stato: bozza non pubblicata.

## Prodotto
Percorso: `vault/tools/calcolatore-autonomia-power-station-v01.html`.
Uno strumento didattico HTML e JavaScript, fruibile offline, senza librerie esterne, tracciamento, raccolta dati o link commerciali.

## Metodo
- Energia richiesta: somma di potenza media (W) per ore di funzionamento.
- Capacità nominale teorica: Wh richiesti diviso (rendimento ipotizzato × quota utilizzabile).
- Potenza contemporanea: somma dei watt inseriti, assumendo tutti i carichi attivi nello stesso momento.
- Esempio: 45 W × 3 h + 10 W × 3 h + 8 W × 3 h = 189 Wh; rendimento 80% e margine 15% producono 277,94 Wh di capacità teorica. Somma potenze 63 W.
- I dati sono ipotetici: non costituiscono test, certificazione o garanzia di autonomia.
- Non usare il risultato per dispositivi medici critici, impianti elettrici domestici o per equiparare power station e UPS.

## QA da completare prima dell'uso pubblico
1. Test con browser mobile e desktop; verificare tabulazione, etichette e leggibilità.
2. Controllare l'esempio iniziale: 189 Wh, 277,9 Wh e 63 W.
3. Controllare che input vuoti, negativi e valori fuori intervallo mostrino un errore.
4. Testare stampa/salvataggio PDF e assenza di chiamate di rete.
5. Revisione umana di formule, disclaimer e impaginazione.

## Posizionamento organico
Titolo: «Calcolatore power station: quanti Wh servono per notebook e router?»
Slug suggerito: `/strumenti/calcolatore-autonomia-power-station/`
Meta: «Stima wattora, capacità teorica e potenza per notebook, router e luci. Strumento gratuito con ipotesi chiare.»
Distribuzione: pagina informativa originale, FAQ W vs Wh, link interno da guida all'autonomia, post social didattico. Niente spam o affermazioni commerciali non dimostrate.

## Pubblicità e conformità
Non sono inclusi link di affiliazione. Prima di inserirli: verificare condizioni e stato del programma direttamente nella piattaforma, generare link tracciabili con gli strumenti ufficiali e mostrare un'informativa pubblicitaria evidente. Verificare gli obblighi italiani fiscali e di tutela dei consumatori per l'attività commerciale.

## Fonti consultate il 9 ottobre 2026
- Awin, creazione deep link: https://success.awin.com/articles/en_US/Knowledge/How-can-I-use-Link-Builder-to-create-Deep-Links
- Awin, Link Builder API: https://www.awin.com/gb/how-to-use-awin/link-builder-api
- Commissione europea, Influencer Legal Hub: https://commission.europa.eu/topics/consumers/consumer-rights-and-complaints/influencer-legal-hub_en
- Awin, eWeki IT: https://ui.awin.com/merchant-profile/19988 — elettronica di consumo, finestra di attribuzione pubblicata 30 giorni; nessuna commissione individuale verificata.

Nessun file è stato pubblicato in produzione, nessuna spesa o attivazione pagamenti.
