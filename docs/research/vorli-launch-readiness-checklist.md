# VORLI — checklist di prontezza al lancio

Ultimo controllo documentato: 21 ottobre 2026. Questo documento è una checklist operativa, non una dichiarazione di lancio completato.

## Dieci gate prima di attivare il progetto

1. **Validazione tecnica** — confermare che GitHub Actions passi sul commit più recente, inclusi test e build.
2. **Politica offerte** — mantenere il comportamento fail-closed: una scheda è esclusa se manca approvazione umana recente e verificabile.
3. **Merchant demo** — rifiutare nomi segnaposto e varianti comuni; nessun prodotto demo deve diventare acquistabile.
4. **URL affiliati** — accettare solo URL HTTPS validi, senza credenziali incorporate e senza domini segnaposto.
5. **Esportazione pubblica** — verificare che prezzi interni, commissioni, score, link di tracking e identificativi privati non vengano esportati nei metadati pubblici.
6. **Build e pagine** — ricostruire il sito e verificare navigazione, pagine collegate, catalogo, versione mobile e assenza di collegamenti rotti.
7. **SEO** — mantenere `noindex,nofollow` durante la fase prototipo. Rimuoverlo solo dopo approvazione esplicita del lancio e controllo delle pagine.
8. **Privacy e trasparenza** — verificare strumenti effettivamente presenti, cookie/consensi, informativa privacy, disclosure affiliata e dati di contatto prima di rendere il sito commerciale.
9. **Programmi affiliati** — verificare manualmente nella dashboard di ciascun network l'accettazione, i termini, il paese, le categorie consentite e i link ufficiali. Un invito non equivale ad approvazione.
10. **Rilascio controllato** — prima del merge e del deploy, fare revisione finale e ottenere approvazione umana; controllare il sito pubblico dopo il rilascio e conservare un piano di rollback.

## Stato verificato — 21 ottobre 2026

- La run GitHub Actions [39608979873](https://github.com/riccardomontanaroact-hub/affiliate-autopilot/actions/runs/39608979873) è riuscita sul commit `0a81cb0df7c3c93cf331fb7230084e91c0614e54`: compilazione Python, test runner dei cinque agenti, build del sito/catalogo e controllo whitespace superati. È una validazione CI della PR, non un deploy Pages.
- La PR #47 resta aperta in bozza e non è stata unita.
- La configurazione della bozza contiene il titolare `Riccardo Montanaro` e il contatto `vorli.notifications@gmail.com`; la loro presenza nei file non sostituisce una revisione finale prima del lancio.
- Il catalogo contiene ancora una scheda dimostrativa e non deve essere trattato come catalogo commerciale.
- Le pagine generate mantengono `noindex,nofollow` finché il prototipo non viene approvato per il lancio.
- Non è stata verificata nella dashboard Awin un'approvazione attiva sufficiente a rendere acquistabile una scheda.
- La configurazione effettiva di GitHub Pages e la versione restituita dal dominio pubblico non sono state verificate; `site/privacy.html` non è presente su `main` e la modifica è ancora limitata alla PR.

## Regole di sicurezza

- Non inserire credenziali, token o dati personali nel repository.
- Non inventare prezzi, recensioni, approvazioni, link o disponibilità.
- Non attivare checkout, offerte, merge, deploy o contatti con terzi senza autorizzazione.
- Gli agenti automatici forniscono controlli deterministici; non sostituiscono la verifica delle dashboard affiliate né la revisione umana.
