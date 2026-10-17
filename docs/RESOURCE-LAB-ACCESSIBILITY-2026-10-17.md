# VORLI Resource Lab — piano accessibilità (17 ottobre 2026)

Ambito: solo branch di anteprima, senza modifiche a `site/` e senza vendita.

Verifica odierna tramite GitHub: tutti e cinque i sorgenti registrati in `data/digital_resources_verified.json` rispondono con contenuto leggibile. Sono bozze, non download commerciali.

Problema riscontrato: `risorse-originali-lab.html` contiene un contenitore vuoto, popolato soltanto da JavaScript. Senza script, l'utente non vede alcuna scheda. Il link “Risorse” in `catalogo-lab.html` rimanda alla pagina legacy anziché alla nuova landing.

Soluzione proposta: cinque schede HTML statiche, link GitHub verificati, navigazione coerente e test automatici per assenza di checkout e presenza di `noindex`. Test reali browser mobile e WCAG ancora da eseguire.

Nessun link affiliato autorizzato, nessun checkout, nessuna pubblicazione o approvazione commerciale presunta.
