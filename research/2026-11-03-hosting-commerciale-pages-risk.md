# VORLI — rischio hosting GitHub Pages per uso commerciale

**Verifica documentale: 2026-11-03. Priorità: alta. Nessuna modifica a produzione.**

## Fonte primaria
GitHub Docs, *GitHub Pages limits*: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits

La sezione 'Usage limits' esclude l'uso di GitHub Pages come hosting gratuito per un business online, e-commerce o siti principalmente diretti a facilitare transazioni commerciali. Sconsiglia inoltre transazioni sensibili come password e carte di pagamento.

## Conseguenze operative
- Un sito dimostrativo o informativo non è automaticamente equiparabile a un e-commerce: valutare **scopo prevalente** e flussi reali.
- **Non** attivare carrello, checkout, raccolta di carte o vendita diretta su GitHub Pages.
- Prima di un rilascio commerciale, verificare i termini del provider scelto e individuare un hosting che autorizzi esplicitamente il caso d'uso, senza assumere che 'gratuito' significhi 'utilizzabile per e-commerce'.
- Audit dei dati identificativi pubblici e della cronologia Git ancora aperto: non inserire segreti, email, ID publisher o URL di tracciamento.
- Non eseguire deploy o migrazioni senza revisione e consenso.

## Stato
Rischio di policy **documentato**, compatibilità del sito attuale da accertare. Nessuna conclusione di violazione già accertata. Nessuna spesa o modifica di configurazione.
