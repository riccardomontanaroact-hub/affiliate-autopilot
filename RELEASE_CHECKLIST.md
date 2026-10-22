# VORLI — Release readiness checklist

This checklist is intentionally conservative. Passing automated checks does not mean legal compliance, affiliate approval, or production publication.

## Automated preflight
Run from the repository root:

```bash
python agent/release_preflight.py
python -m unittest discover -s tests -v
python agent/build.py
```

The preflight is expected to exit with a non-zero status while any release blocker remains. This is deliberate.

## Audit della baseline `main` — 21 ottobre 2026

La revisione del repository ha rilevato che la configurazione attualmente presente su `main` non coincide con quella prudenziale proposta in questa PR:

- `data/config.json` su `main` contiene ancora il segnaposto `INSERISCI IL TUO NOME` e il contatto `riccardomontanaro@etik.com`; la configurazione della PR indica invece il nome fornito per la bozza e `vorli.notifications@gmail.com`.
- `data/products.json` su `main` contiene ancora `Prodotto demo da sostituire`, il merchant segnaposto `INSERISCI NETWORK` e l'URL `https://example.com/`.
- La dichiarazione affiliati presente su `main` afferma che il sito contiene link affiliati, mentre il catalogo esaminato è ancora dimostrativo: verificare e allineare dichiarazione e contenuti prima di una pubblicazione commerciale.
- Il workflow `.github/workflows/build.yml` prevede build/deploy quando cambia `main` e una build pianificata giornaliera. La PR non modifica da sola la produzione; la configurazione effettiva di GitHub Pages e l'aspetto dell'URL pubblico non sono stati verificati da questa audit.
- Verifica comparativa successiva della workflow: su `main` è presente `enablement: true` nel passo `actions/configure-pages@v5`; nella branch della PR è impostato `enablement: false`. Quindi la protezione proposta non è ancora attiva su `main` finché la modifica non viene approvata e integrata. Non ho effettuato il merge né modificato `main`.

Questi riscontri sono blocchi pre-lancio, non autorizzano a fondere la PR né a cambiare impostazioni di pubblicazione. Non è stata confermata la visualizzazione corrente del sito in un browser.

## Verifica repository e interfaccia — 21 ottobre 2026

- La cartella `site/` presente su `main` include le pagine `index.html`, `catalogo.html`, `guida.html`, `risorse.html` e `usb-c.html`; non risulta presente `site/privacy.html`. La pagina privacy è invece nella cartella di anteprima della PR. Prima di una pubblicazione commerciale va aggiunta e verificata nel sito generato, non solo nell'anteprima.
- Il CSS della versione `main` contiene media query per layout desktop e mobile, focus visibile e preferenze di movimento ridotto. Questo è un controllo del codice, non una prova visiva su un dispositivo reale.
- La lettura delle impostazioni GitHub Pages tramite l'integrazione disponibile non è riuscita; quindi sorgente effettiva, stato di pubblicazione e contenuto restituito dal dominio non sono confermati da questa verifica.
- La scansione statica del repository non sostituisce una verifica completa dei flussi dati, dei log del provider, dei link esterni o una revisione legale. Nessuna conformità normativa viene dichiarata.

## Required before any public commercial launch

- [x] Owner supplied for the draft: Riccardo Montanaro, natural person (still confirm the final legal presentation before launch).
- [x] Contact address supplied for the draft: vorli.notifications@gmail.com (monitoring and suitability should be confirmed before launch).
- [ ] Review and publish an appropriate privacy notice based on the actual data flows, hosting, providers, cookies, and tracking; obtain professional review where appropriate.
- [ ] Decide whether public pages should remain `noindex,nofollow`; after the owner explicitly approves the strategy, set `indexing_strategy_reviewed` to `true` in `data/config.json`. Keep it `false` until then.
- [ ] Manually verify GitHub Pages source branch/folder and the deployed URL. Only after checking the actual repository settings, set `github_pages_source_verified` to `true` in `data/config.json`; code tests cannot prove the hosting configuration or what a visitor currently sees.
- [ ] Remove the demo product from the public catalogue and add only real offers with evidence of current program approval, terms, price, stock, and destination URL.
- [ ] Verify every affiliate offer in the relevant network dashboard immediately before activation. A record in JSON is not proof of approval.
- [ ] Review affiliate disclosures, price/availability wording, accessibility, mobile layout, and all external destinations.
- [ ] Review the final generated site in a browser before changing visibility or publishing.

## What must not be guessed

The repository does not contain a verified legal owner/contact or a currently approved product offer. These must be supplied or verified from the actual owner/network account; automation must not fabricate them.

## Safe current state

Keep the change in its draft pull request. Do not merge, change GitHub Pages settings, enable indexing, activate affiliate URLs, or make commercial claims until the required items above are complete and explicitly approved.
