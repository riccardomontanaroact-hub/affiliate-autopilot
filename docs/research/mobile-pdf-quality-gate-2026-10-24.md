# VORLI — Gate qualità mobile, PDF accessibili e SEO per le due guide (BOZZA INTERNA)

**Data:** 24/10/2026 (Europe/Rome). **Ambito:** le bozze `docs/drafts/power-station-autonomia-worksheet-2026-10-24.md` e `docs/drafts/guida-scegliere-software-privacy-20261024.md`. Nessuna esportazione PDF, test su dispositivi, pubblicazione, prezzo o vendita attestati da questo documento.

## Verifica editoriale già eseguibile sul sorgente

- **Power station:** ricontrollo aritmetico della bozza: 768 Wh × 0,80 ÷ 80 W = **7,68 ore** = **7 h 40 min 48 s**; arrotondamento «circa 7 h 41 min» corretto. Per l'esercizio router + LED: (12 W + 8 W) × 5 h = **100 Wh**; 100 Wh ÷ 0,80 = **125 Wh**, corretto come base *teorica* e non dimensionamento consigliato. I fattori 0,80 e i carichi sono ipotesi, non test di prodotti.
- **Privacy:** controllo aritmetico del costo triennale: 24 + 60 + 60 = **144 €**; 39 × 3 = **117 €**. Il risultato non include variazioni di prezzo, tasse aggiuntive o cambio valuta.
- **Contenuti:** conservare le avvertenze: nessuna autonomia garantita, nessun anonimato totale, nessuna recensione sperimentale, nessun prezzo reale; non sostituire queste cautele con claim promozionali.

## Gate PDF — da eseguire solo dopo l'esportazione

| Test | Criterio di accettazione | Stato |
| --- | --- | --- |
| Struttura | Titolo e sottotitoli riconosciuti come heading, non solo testo ingrandito; elenchi e tabelle semanticamente riconoscibili | NON TESTATO |
| Ordine di lettura | Selezione, lettura assistita e navigazione tastiera seguono ordine logico, comprese tabelle e link | NON TESTATO |
| Lingua e metadati | Lingua italiana impostata, titolo PDF comprensibile, autore/metadata senza informazioni private | NON TESTATO |
| Immagini e grafici | Alternative testuali per grafici informativi; decorazioni ignorabili da lettori di schermo | NON TESTATO |
| Tabelle | Intestazioni distinguibili e celle comprensibili; nessuna tabella tagliata o minuscola su telefono | NON TESTATO |
| Smartphone | Aprire su Android e iOS, a zoom normale e ingrandito; verificare leggibilità, scroll, assenza di sovrapposizioni, tabelle e formule | NON TESTATO |
| Link | Eventuali URL pubblici leggibili e apribili; nessun link di tracking o checkout | NON TESTATO |
| Integrità | Testo selezionabile, nessuna pagina vuota inattesa, font incorporati se necessario, file apribile offline | NON TESTATO |

**Nota tecnica:** un PDF visivamente leggibile non è automaticamente accessibile. I controlli di tag e ordine di lettura devono essere verificati con strumenti adatti e, dove possibile, con tecnologia assistiva. Le tecniche W3C citate sono esempi di conformità WCAG, non un certificato automatico.

## Gate SEO — prima di creare qualunque pagina pubblica

1. **Discrepanza slug risolta editorialmente il 24/10/2026:** le due bozze della guida power station ora usano `/guide/calcolare-autonomia-power-station/` come *percorso proposto*, non URL esistente. Non creare la pagina, duplicati o link interni finché non autorizzati. Se pubblicata in futuro, usare una sola URL preferita e coerenza fra collegamenti interni e segnali canonici.
2. Una sola intenzione di ricerca principale per guida; titolo H1, title e description coerenti con ciò che il file contiene realmente, senza «PDF disponibile» o «acquista» finché non è vero.
3. Inserire data della **revisione effettiva**, fonti consultate e metodo degli esempi ipotetici. Non cambiare date solo per simulare freschezza.
4. Evitare markup `Product`/`Offer` con prezzo, disponibilità, recensioni o rating inventati. Le schede attuali sono **bozze informative**, non offerte acquistabili; qualsiasi markup futuro deve corrispondere ai dati visibili e verificati.
5. Non automatizzare la pubblicazione seriale di pagine quasi identiche; verificare utilità originale e completezza prima dell'indicizzazione.

## Decisione

**NON PRONTO PER LA PUBBLICAZIONE.** I conti didattici sono coerenti, ma i PDF non esistono ancora come output testati; accessibilità, leggibilità mobile, revisione tecnica e aspetti legali/fiscali sono ancora aperti. Questo documento non autorizza merge, vendita, pubblicazione, attivazione pagamenti o email.

## Fonti pubbliche consultate il 24/10/2026

- W3C WAI, PDF3, ordine di lettura e navigazione: https://www.w3.org/WAI/WCAG21/Techniques/pdf/PDF3
- W3C WAI, PDF9, intestazioni nei PDF: https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF9.html
- Google Search Central, contenuti utili e originali: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google Search Central, differenza tra product snippets e merchant listings: https://developers.google.com/search/docs/appearance/structured-data/product
- Google Search Central, consolidamento URL duplicate e link canonici: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
