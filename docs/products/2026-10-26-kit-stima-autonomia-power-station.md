# Kit VORLI — Stima autonomia power station (modello compilabile)
**Versione bozza 0.1 · 26 ottobre 2026 · NON in vendita**

## Scopo
Modello originale per raccogliere requisiti e stimare orientativamente l'autonomia di una batteria portatile. Non sostituisce manuale, misurazioni reali, prove di sicurezza o progettazione di sistemi elettrici.

### Scheda dispositivo
| Voce | Valore da inserire |
|---|---|
| Nome/modello (opzionale) | |
| Energia nominale batteria (Wh) | |
| Quota di capacità effettivamente utilizzabile (0–1, ipotesi o dato del produttore) | |
| Rendimento totale di conversione (0–1, ipotesi o dato verificato) | |
| Potenza continua massima uscita (W) | |
| Potenza di picco e durata ammissibile (se documentate) | |
| Temperatura e condizioni di uso | |
| Fonte delle specifiche + data | |

### Carichi previsti
| Apparecchio | W medi | Ore desiderate | Energia teorica richiesta (Wh = W × ore) | Picco di avvio verificato? |
|---|---:|---:|---:|---|
| Esempio: router (solo ipotesi) | 10 | 6 | 60 | n.d. |
| Apparecchio 2 | | | | |
| Apparecchio 3 | | | | |
| **Totale** | | | | |

### Formule
1. Energia stimata disponibile (Wh) = capacità nominale (Wh) × quota utilizzabile × rendimento complessivo.
2. Autonomia orientativa per carico costante (ore) = energia stimata disponibile / W medi complessivi.
3. Fabbisogno teorico per la durata desiderata (Wh) = somma di (W medi di ciascun apparecchio × ore di uso).
4. Se la somma delle potenze simultanee supera la potenza continua ammessa, la configurazione **non è idonea**, anche se i Wh sembrano sufficienti. Verificare i picchi separatamente.

**Esempio fittizio:** 500 Wh × 0,90 × 0,85 = 382,5 Wh stimati; a 60 W costanti ≈ 6,38 ore. Il rendimento non è un valore certificato. Non garantisce autonomia effettiva.

### Registro qualità e trasparenza
- Specifiche copiate dal produttore? [ ] sì [ ] no — URL/data: ____
- Misure effettuate direttamente? [ ] sì [ ] no — se no, evitare «testato».
- Limiti elettrici e avvertenze del manuale verificati? [ ] sì [ ] no
- Collegamenti commerciali presenti? [ ] no (default). Se aggiunti in futuro, disclosure evidente.
- Uso medicale, emergenziale o impianto domestico? [ ] sì → richiede valutazione specializzata; non usare questo modello come garanzia.

### Fonte per i principi generali
- DOE, accumulo e inverter: https://www.energy.gov/cmei/systems/articles/solar-plus-storage-101
- DOE, perdite e rendimento non costante dell'inverter: https://www1.eere.energy.gov/buildings/publications/pdfs/building_america/32765.pdf

**Commercializzazione bloccata:** prima di vendere il kit verificare originalità finale, utilità reale, corrette informazioni ai consumatori, disciplina del recesso dei contenuti digitali, IVA e posizione fiscale del venditore italiano. Non attivare checkout né prezzi.
