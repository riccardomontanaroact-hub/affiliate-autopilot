# Affiliate Autopilot — v1.0

Sistema gratuito di partenza per un sito di affiliate marketing. Nessun acquisto di dominio, hosting o SaaS richiesto.

## Cosa fa
- catalogo prodotti da `data/products.json`
- pagine prodotto statiche generate da script Python
- dashboard HTML con KPI
- motore di scoring per priorità prodotti
- generatore di contenuti da template
- controlli di compliance e disclosure
- struttura pronta per integrare più network di affiliazione

## Limiti importanti
Questa versione non crea account affiliati, non inserisce credenziali, non acquista servizi e non garantisce guadagni. Le API dei network richiedono autorizzazione e spesso condizioni proprie.

## Avvio locale
```bash
python3 agent/build.py
python3 -m http.server 8000 -d site
```

## Pubblicazione gratuita
Puoi pubblicare il progetto con GitHub Pages su un repository pubblico GitHub Free.

## Configurazione
Modifica `data/config.json` e `data/products.json`. Non inserire mai password o token nel repository pubblico.
