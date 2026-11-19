# VORLI Lab — audit delle risorse locali (19 novembre 2026)

## Ambito e metodo
Verifica non distruttiva tramite lettura GitHub Contents API sul branch `vorli/matrix-dom-attribute-safety-20261118`. La pagina di riferimento è `preview/vorli-next/matrice-scelta-tech-lab.html`. Sono stati richiesti e restituiti con successo i contenuti dei seguenti otto file locali, nella stessa directory della matrice:

| Risorsa | Esito lettura |
| --- | --- |
| `index.html` | Presente |
| `catalogo-lab.html` | Presente |
| `risorse-originali-lab.html` | Presente |
| `guida.html` | Presente |
| `guida-scelta-tech-lab.html` | Presente |
| `glossario-tech-lab.html` | Presente |
| `scheda-confronto-tech-lab.csv` | Presente |
| `catalogo-lab.css` | Presente |

La pagina matrice è stata letta: contiene otto articoli editoriali con criteri di scelta, meta robots `noindex,nofollow`, viewport responsive, collegamenti relativi a risorse e dichiarazione esplicita di assenza di prodotti acquistabili. Il CSV originale è presente nel repository: questo **non** certifica ancora la correttezza di ogni cella, il download HTTP o la licenza di distribuzione.

## Limitazioni e release gates
- La lettura tramite API dimostra l'esistenza dei file sul branch, **non** il funzionamento dei link in un sito distribuito.
- Non sono stati eseguiti browser Chromium, test su dispositivi fisici, screen reader, suite unittest o GitHub Actions in questo audit.
- Non sono state verificate licenze di immagini né autorizzazioni commerciali; non aggiungere asset di terzi senza verifica.
- Risolvere il blocco sicurezza segnalato in PR #148; eseguire i test già predisposti nelle PR #196–#205, poi controllare visualizzazione mobile/tablet/desktop, contrasto, navigazione tastiera e download CSV.
- Prima di qualunque pubblicazione verificare autorizzazioni Awin, condizioni legali/fiscali e provider pagamenti. Nessun checkout, prezzo o link affiliato deve essere introdotto in questa fase.

## Confini
Documento di audit per preview sperimentale. Non comporta merge, deploy, modifica a `main`, vendita o spesa.
