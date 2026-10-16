# VORLI — Verifica di sicurezza del calcolatore power station
Data: 16 ottobre 2026. Stato: bozza tecnica; nessuna pubblicazione.

## Problema riscontrato
Il prototipo `tools/powerstation-runtime.html` calcola e mostra un numero di ore anche quando il consumo medio inserito supera la potenza continua massima dichiarata. Compare un avviso, ma il titolo «Autonomia stimata» può essere frainteso come autonomia effettivamente utilizzabile.

## Correzione proposta (non ancora applicata al codice)
Prima del calcolo, se la potenza continua massima è stata inserita e il carico medio la supera, interrompere il calcolo, non mostrare l'autonomia e indicare che il carico non è alimentabile secondo i dati forniti. Continuare a ricordare che i picchi di avvio possono rendere incompatibile anche un carico con consumo medio inferiore alla potenza continua.

## Casi logici controllati (non equivalgono a un collaudo browser)
- 1024 Wh; 120 W; efficienza 80%; riserva 10%; nessun limite indicato: 6,144 ore.
- Stessi dati, limite continuo 120 W: 6,144 ore teoriche, con avviso sui picchi.
- Stessi dati, limite continuo 100 W: configurazione da bloccare, senza indicare ore utilizzabili.
- 1000 Wh; 100 W; efficienza 100%; riserva 99%: 0,1 ore (6 minuti).

## Collaudi ancora necessari
Provare la gestione degli errori nel browser mobile, la navigazione da tastiera, la lettura degli avvisi con screen reader, i valori limite e la visualizzazione su schermi piccoli. Nessun test end-to-end nel browser è stato completato.

## Limitazioni
La formula rappresenta una stima indicativa, non un test di laboratorio. Per apparecchi critici e salvavita non utilizzare questo calcolatore come unica fonte decisionale. Nessun link affiliato, account o dato personale incluso.
