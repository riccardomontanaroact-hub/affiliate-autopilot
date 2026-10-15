# VORLI Lab — verifica numerica, 15 ottobre 2026

Stato: ricerca tecnica in bozza, nessuna pubblicazione.

## Problema riproducibile dal codice

Il calcolatore `tools/pc_energy_mobile.html` verifica che gli input siano numeri finiti, ma non verifica i risultati delle moltiplicazioni. Un input estremo come `active_watts=1e308`, `active_hours_per_day=24`, `standby_hours_per_day=0` e `days_per_year=366` può produrre `Infinity` nel consumo annuale. Un prezzo elettrico enorme può far debordare il costo; la conversione in centesimi può debordare anche per un importo ancora finito.

## Correzione proposta, non ancora implementata

Verificare con `Number.isFinite` i risultati intermedi di consumo e costo e la moltiplicazione per 100 prima dell'arrotondamento. Aggiungere test Node.js per overflow del consumo, del costo annuo e dell'importo di acquisto. Non introdurre limiti commerciali arbitrari senza motivazione.

## Release gate

Non commercializzare il calcolatore finché la correzione non è implementata, i test CI non sono verdi e i controlli manuali su smartphone non sono completati. Nessun dato personale, link affiliato, candidatura o pagamento incluso.

Fonte: codice e suite test nel branch `vorli/qa-pc-energy-js-suite-20261015-0613`, letti il 15/10/2026.