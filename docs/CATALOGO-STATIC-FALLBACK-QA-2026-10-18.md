# VORLI Catalogo Lab — fallback statico (18 ottobre 2026)

## Obiettivo
Fornire una navigazione consultabile senza JavaScript. Il nuovo file `preview/vorli-next/catalogo-statico-lab.html` eredita la palette blu notte/azzurro elettrico dal CSS esistente e contiene otto categorie editoriali demo. Le cinque risorse digitali rimangono nella landing HTML statica `risorse-originali-lab.html`.

## Verifiche svolte
- Letti dal repository i file del catalogo Lab e della landing risorse del 17 ottobre.
- Verificati nuovamente, tramite lettura GitHub, tutti e cinque i sorgenti delle guide su branch distinti.
- Riletti dal branch i nuovi file: otto schede categoria e otto titoli, metadata noindex, skip link, nessuno script, nessun form.
- Aggiunti controlli di regressione offline in `tests/test_catalog_static_fallback.py`. Non eseguiti su un clone locale in questa sessione: accesso di rete del runner locale non disponibile.
- La pagina statica usa CSS già presente e link relativi a file già presenti nel branch; non usa immagini di terzi.

## Limiti e prossimi passi
Il fallback statico è raggiungibile tramite URL del file sul branch ma non è ancora linkato dal catalogo dinamico: l'aggiornamento del file HTML esistente è stato bloccato dal connettore. Prima del rilascio: collegare `catalogo-statico-lab.html` da `catalogo-lab.html` (anche nel noscript), eseguire i test Python, Playwright/Chromium a 320, 360, 768 e 1440 px, verificare tastiera/zoom/contrasto e correggere eventuali problemi. Non aggiungere il fallback alla sitemap pubblica prima di approvazione.

## Sicurezza commerciale
Le categorie sono demo e le cinque guide sono bozze. Zero offerte, prezzi, link affiliati, checkout e pagamenti. ACEMAGIC, eWeki IT, 2GO Software IT e ALLPOWERS IT non sono considerati approvati. Nessuna modifica a `site/` o al workflow di produzione.
