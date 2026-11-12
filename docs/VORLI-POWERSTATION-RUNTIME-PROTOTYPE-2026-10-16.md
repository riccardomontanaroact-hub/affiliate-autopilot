# VORLI — Prototipo calcolatore autonomia power station

Data verifica: 16 ottobre 2026. Documento preparatorio, non pubblicato.

Formula indicativa: ore = Wh nominali × rendimento stimato × (1 − riserva) / W medi. Rendimento e riserva sono ipotesi modificabili, non prestazioni garantite. Distinguere la capacità energetica (Wh) dalla potenza di uscita (W); verificare separatamente picchi di avvio e limiti continui. Non usare stime generiche per dispositivi salvavita.

Fonte produttore: https://faq.jackery.com/hc/en-us/articles/52357015569179-How-can-I-estimate-the-runtime-of-my-portable-power-station (FAQ del 2 luglio 2026, stima con fattore 0,8).

Fonte metodologica: https://eu.flashfishtech.com/pages/portable-power-station-runtime-calculator (rendimento e riserva, variabilità dei carichi).

Esempio dimostrativo: 1024 Wh × 0,8 × 0,9 / 120 W = 6,144 ore, non garantite.

Requisiti per prototipo futuro: calcolo offline, input validati, niente tracciamento, nessun link affiliato, nessuna pubblicazione senza revisione.
