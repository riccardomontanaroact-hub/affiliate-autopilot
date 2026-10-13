# VORLI — Catalogo generalista tech: audit e QA
Data: 2026-10-13. Branch di revisione; nessuna pubblicazione autorizzata.

## Audit verificato
- `main` contiene già un tema blu notte/azzurro elettrico in `preview/vorli-next/style.css`.
- `agent/build.py` copia la preview nel sito: per modifiche persistenti serve intervenire nelle sorgenti `preview/vorli-next/`, non solo in `site/`.
- `data/products.json` contiene **una sola scheda demo**, con URL di esempio. Non è una reale offerta commerciale.
- `site/catalogo.html` è generato da `agent/build.py`; la home e le risorse usano il tema VORLI Next.
- Cinque bozze originali sono state lette tramite GitHub sui rispettivi branch il 13 ottobre: USB-C, Casa Smart, Power Station, elettrodomestici EPREL e checklist Casa Smart HTML.
- Non è stata verificata alcuna approvazione advertiser né un feed commerciale utilizzabile. Non aggiungere prezzi, rating, link affiliati o CTA d'acquisto.

## Dati implementati sul branch
- `data/catalog_categories_demo.json`: otto categorie con stato demo e array offerte vuoti.
- `data/digital_resources_verified.json`: cinque risorse originali con ref/path GitHub verificati e stato editoriale bozza.
- I dati non sono ancora collegati al generatore: **non descrivere questo branch come un sito già aggiornato**.

## Mockup locale
È stata costruita separatamente una pagina HTML mobile-first, con ricerca testuale, filtri, otto categorie, cinque link a bozze verificate, SVG originale, design blu notte e nessun checkout. La scrittura HTML su GitHub è stata bloccata dal connettore; il mockup resta come artefatto scaricabile della sessione, non nel repository.

## QA del mockup locale
Test Chromium automatici alle larghezze 360, 768 e 1440 px: otto categorie iniziali, cinque link GitHub, ricerca Wi-Fi, filtro Energia, stato aria-pressed, assenza di errori JavaScript e di overflow orizzontale: **superati**.
Non sono stati eseguiti audit WCAG completi, test reali su telefoni, verifica di tutte le destinazioni HTTP dal browser o test del workflow di deploy.

## Prossimi passaggi soggetti a revisione
1. Integrare il mockup nella sorgente `preview/vorli-next/` e includerlo nella copia del build; preservare il lockup ufficiale VORLI.
2. Evitare pubblicazione automatica da branch di lavoro: revisionare i workflow di build e Pages prima di qualsiasi merge.
3. Aggiungere validazione JSON/schema e link-check interno, poi test mobile, accessibilità e performance.
4. Mantenere `noindex` su preview; generare sitemap soltanto per pagine editoriali realmente approvate alla pubblicazione.
5. Per eventuali offerte future: approvazione programma, condizioni commerciali, URL autorizzati, dati aggiornati e revisione legale/fiscale.

Nessuna spesa, account, email, dato personale aggiunto, pagamento o pubblicazione in produzione.
