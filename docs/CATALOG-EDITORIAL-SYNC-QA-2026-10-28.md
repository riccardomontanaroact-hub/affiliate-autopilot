# VORLI Lab — controllo coerenza schede/dati (28 ottobre 2026)

## Obiettivo e problema
La ricerca del catalogo usa descrizioni e parole chiave del registro `catalogo-lab-data.js` per filtrare schede HTML statiche. Il controllo precedente confrontava titolo, categoria e URL dei file, ma **non** le descrizioni: una descrizione cambiata nell'HTML poteva non corrispondere al testo effettivamente indicizzato dalla ricerca, pur mantenendo attivi i filtri.

## Correzione non distruttiva
- `preview/vorli-next/catalogo-lab.js`: `categorySync` e `resourceSync` verificano ora anche il testo delle descrizioni delle schede rispetto al registro editoriale, prima di aggiungere opzioni ai filtri.
- Se manca una descrizione o non corrisponde, il codice utilizza il fallback già presente: tutte le schede statiche restano leggibili, ma ricerca e filtri non vengono attivati. Nessun contenuto viene cancellato o ricostruito.
- `tests/test_catalog_lab_hydration.py`: il parser HTML verifica la corrispondenza delle descrizioni di 8 categorie e 5 risorse.
- `tests/catalog-progressive.test.cjs`: aggiunte asserzioni per testo editoriale e guardia JavaScript.

## Verifiche del 28 ottobre
- Letti i file effettivi sul branch del 27 ottobre, da cui deriva questa modifica.
- Analisi sintattica JavaScript riuscita nel runtime JS del connettore di lavoro.
- Ricontrollata tramite API GitHub l'esistenza dei cinque sorgenti originali nei rispettivi branch: USB-C, Casa Smart Sicura, Power Station, Elettrodomestici EPREL e Casa Smart compilabile. L'esistenza non implica revisione completa, pubblicabilità o disponibilità come PDF.
- Le pagine Lab rimangono `noindex,nofollow`; nessun checkout, prezzo, link affiliato o modifica a `site/`.

## QA ancora richiesto
Eseguire sul branch aggiornato `python -m unittest discover -s tests -v`, `node --test tests/catalog-progressive.test.cjs` e `python tests/browser_catalog_lab.py` con Playwright/Chromium; verificare screenshot, screen reader e dispositivi fisici. I test Chromium dei giorni precedenti non certificano questo codice. Il workflow `vorli-lab-browser.yml` ascolta solo PR verso alcuni branch Lab: per consentire l'avvio dei controlli si propone una PR **in bozza** verso `vorli/catalog-accessibility-regression-20261025`, che include cumulativamente le modifiche del 26–28 ottobre; non verso `main`.

## Vincoli editoriali e commerciali
Otto categorie sono **demo**, cinque risorse sono **bozze originali**, nessuna è vendibile. Nessuna verifica di approvazioni individuali Awin è stata eseguita; non considerare autorizzati ACEMAGIC, eWeki IT, 2GO Software IT o ALLPOWERS IT. Nessuna spesa, nuovo account, invio email, dati personali, tracking, pagamento o deploy. Prima di qualsiasi rilascio: revisione editoriale e accessibilità WCAG, controlli legali/fiscali e autorizzazioni commerciali, approvazione umana.
