# VORLI Studio — specifica di restyling

Data: 11 ottobre 2026. Proposta in branch separato; non pubblicare.

## Direzione visiva
Palette blu notte #07162D, blu intermedio #0D3357, azzurro elettrico #38CAFF, sfondo #F3F7FB, testo #15283E. Font di sistema e nessuna dipendenza esterna.

## Home mobile-first
Hero con titolo «Tecnologia con criterio», CTA verso catalogo demo e risorse originali. Otto categorie: computer, software, elettronica, elettrodomestici smart, accessori casa, sport tech, benessere tech, energia portatile.

## Catalogo
Griglia responsive 1/2/3 colonne. Schede con categoria, criteri di scelta e badge «Scenario demo». Vietati prezzi, recensioni e pulsanti di acquisto non verificati.

## Accessibilità
HTML semantico, skip link, focus visibile, contrasto WCAG AA da misurare, immagini SVG originali con testo alternativo, riduzione animazioni.

## SEO
Meta title e description univoci. Anteprime noindex. Sitemap solo per URL pubblici autorizzati dopo il rilascio; nessun URL di preview.

## Dipendenze
Il generatore legge preview/vorli-next e copia in site. Il workflow esistente mantiene un git push automatico. Prima di integrare: mettere in sicurezza build e deploy e verificare test su smartphone.
