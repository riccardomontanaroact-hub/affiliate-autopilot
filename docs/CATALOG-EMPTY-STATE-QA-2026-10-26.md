# VORLI Lab — feedback ricerca vicino ai filtri (26 ottobre 2026)

## Ambito e isolamento
- Base: `vorli/catalog-accessibility-regression-20261025` (PR #69 in bozza), **non** `main`.
- Modifiche esclusivamente a `preview/vorli-next/catalogo-lab.html`, test e workflow QA; nessun file in `site/`.
- Catalogo demo: 8 categorie, 5 risorse originali ancora bozze; `noindex,nofollow`; nessun checkout, prezzo, tracking, link affiliato, raccolta dati o deploy.

## Problema osservato nel sorgente
Prima della modifica, il pannello `#empty-results` era collocato **dopo** l'intera griglia delle cinque risorse, lontano dal campo ricerca e dal contatore `#results-count`. In caso di ricerca senza corrispondenze, il messaggio e il pulsante di ripristino potevano apparire molto più in basso rispetto ai filtri, rendendo poco chiaro l'esito.

## Correzione implementata
- Spostato il medesimo pannello `#empty-results` immediatamente dopo `#results-count`, **prima** delle categorie; ID, testo, pulsante e logica JS invariati.
- Aggiunto test Python che blocca il ritorno del pannello in fondo alla pagina.
- Rafforzato test Chromium reale a 320/360/768/1440 px: posizione del pannello, contatore zero, pulsante reset e focus che torna alla ricerca.
- Screenshot aggiuntivo `catalog-360-empty-state.png` nella cartella artefatti QA.
- Esteso il trigger QA per le PR che puntano al branch della PR #69.

## Verifiche e limiti
- Le modifiche e i test sono nel branch di laboratorio; **non dichiarare superati** i test aggiunti prima del risultato effettivo di GitHub Actions.
- Il workflow non esegue deploy; salva screenshot per revisione umana.
- Ancora necessari: revisione screenshot, screen reader reali, dispositivi fisici, audit WCAG 2.2 completo, revisione editoriale delle cinque bozze, approvazioni commerciali, verifiche fiscali e privacy.
- Le candidature Awin ACEMAGIC, eWeki IT, 2GO Software IT e ALLPOWERS IT non vengono considerate approvate; nessuna offerta autorizzata è stata inserita.

**Non effettuare merge o pubblicazione automatica.**
