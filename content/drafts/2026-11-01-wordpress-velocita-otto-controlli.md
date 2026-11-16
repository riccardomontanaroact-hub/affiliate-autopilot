# Sito WordPress lento? Otto controlli gratuiti prima di comprare un plugin

**Bozza originale VORLI, 1 novembre 2026.** Intento SEO: informativo, per chi gestisce un sito WordPress. Non pubblicata; nessun test su siti terzi, recensione commerciale o collegamento affiliato.

Un sito lento non si risolve sempre installando un plugin a pagamento. Prima di spendere, individua dove si verifica il rallentamento e prova gli interventi a basso rischio.

## Otto controlli pratici
1. **Misura prima di cambiare.** Analizza una pagina rappresentativa con PageSpeed Insights su mobile e desktop. Annota data, URL, dispositivo e risultati; un singolo punteggio non racconta tutta l'esperienza reale.
2. **Distingui dati reali e simulati.** I dati di campo riflettono utenti reali quando disponibili; i test di laboratorio aiutano a individuare problemi, ma non sostituiscono l'esperienza effettiva.
3. **Guarda tre metriche.** LCP riguarda la comparsa del contenuto principale, INP la reattività alle interazioni e CLS la stabilità visiva. Le soglie di riferimento per una buona esperienza sono rispettivamente 2,5 secondi, 200 millisecondi e 0,1, misurate al 75° percentile.
4. **Controlla immagini e video.** Dimensioni e formati non necessari possono appesantire le pagine. Riduci il peso senza sacrificare la leggibilità e verifica che le immagini non cambino improvvisamente dimensione durante il caricamento.
5. **Riduci ciò che non serve.** Rivedi script di terze parti, widget, font e componenti non utilizzati. Ogni intervento va testato: disattivare qualcosa può rompere una funzione importante.
6. **Verifica hosting e cache già disponibili.** Controlla quali ottimizzazioni sono offerte dal provider e quali plugin sono già attivi. Due sistemi di cache sovrapposti possono richiedere configurazioni particolari.
7. **Fai una copia di sicurezza.** Prima di modificare cache, JavaScript, CSS o plugin, prepara un backup e un modo per ripristinare il sito. Prova prima su un ambiente di staging, se disponibile.
8. **Misura di nuovo.** Ripeti i test nelle stesse condizioni per quanto possibile; registra differenze, effetti collaterali e problemi di accessibilità. Se un intervento peggiora l'esperienza, ripristina.

## Tabella di lavoro
| Pagina | Mobile/desktop | LCP | INP (se disponibile) | CLS | Intervento | Data del nuovo test |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |
| | | | | | | |

## Quando valutare un plugin a pagamento
Solo dopo avere individuato un problema specifico e verificato compatibilità con WordPress, hosting, altri plugin, condizioni della licenza, rinnovi, supporto e diritto di rimborso. Non attribuire risultati misurati a prodotti che non hai provato. Un plugin di cache per WordPress **non si applica automaticamente** a un sito statico ospitato su GitHub Pages.

**Nota di trasparenza:** questa guida non contiene link monetizzati. Se in futuro verranno inseriti link commerciali, dovranno essere identificati chiaramente vicino al collegamento.

**Fonti tecniche consultate il 2026-11-01:**
- Google PageSpeed Insights: https://developers.google.com/speed/docs/insights/v5/about
- Core Web Vitals: https://web.dev/articles/vitals
- Pratiche di ottimizzazione: https://web.dev/articles/top-cwv
