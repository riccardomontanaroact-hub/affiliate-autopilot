# Quante ore dura una power station? Guida pratica a Wh, W e autonomia
**Bozza editoriale VORLI Lab — 1 novembre 2026.** Nessun test fisico svolto, nessuna affiliazione inserita.

## Risposta breve
La capacità in **wattora (Wh)** indica l'energia immagazzinata; la potenza in **watt (W)** indica quanta energia viene richiesta in un istante. L'autonomia teorica in ore si ottiene dividendo i Wh *utilizzabili* per i W medi assorbiti. Non basta però leggere il numero più grande sulla confezione: conversione AC, riserva della batteria, consumi in standby e picchi di avviamento contano.

## Nove controlli prima di scegliere
1. **Misura il carico reale.** Usa la targhetta o un misuratore adatto; un computer può consumare molto meno del wattaggio massimo dell'alimentatore.
2. **Somma i Wh giornalieri.** Per ogni dispositivo: potenza media W × ore d'uso = Wh. Per carichi ciclici, come frigoriferi, usa il consumo medio misurato.
3. **Distingui capacità da potenza.** 512 Wh non significa 512 W di uscita continua. Controlla entrambe le specifiche.
4. **Controlla la potenza simultanea.** Somma i W degli apparecchi che lavorano insieme e confrontali con la potenza continua dell'inverter.
5. **Considera i picchi.** Compressori e motori possono assorbire più W all'avvio; verifica il dato di spunto sul manuale del dispositivo e della power station.
6. **Tieni conto delle perdite.** L'efficienza AC non è il 100%; i valori di esempio non sostituiscono quelli misurati dal produttore.
7. **Prevedi una riserva.** Non assumere che il 100% dei Wh nominali sia sempre disponibile: temperature, età, limiti di scarica e modalità di utilizzo incidono.
8. **Valuta le uscite.** USB-C, DC e AC hanno limiti e perdite differenti; controlla tensioni, protocolli e compatibilità.
9. **Verifica ricarica, sicurezza e assistenza.** Peso, tempi di ricarica, garanzia, istruzioni e gestione termica possono contare più di uno sconto.

## Esempio trasparente (solo simulazione)
Una power station ipotetica da **512 Wh** alimenta un dispositivo da **60 W medi** tramite presa AC. Se ipotizziamo il **90% di energia utilizzabile**, **85% di rendimento di conversione** e **0 W** di consumo fisso aggiuntivo, otteniamo:

- Energia utilizzabile: 512 × 0,90 = 460,8 Wh.
- Potenza richiesta alla batteria: 60 / 0,85 ≈ 70,59 W.
- Autonomia: 460,8 / 70,59 ≈ **6,53 ore teoriche**.

Se l'elettronica della power station assorbisse anche **5 W costanti dal lato batteria**, la stima scenderebbe a 460,8 / (70,59 + 5) ≈ **6,10 ore**. Entrambe sono simulazioni, non risultati di laboratorio o promesse per un modello reale.

**Formula generale:** ore stimate = (Wh nominali × quota utilizzabile) / (W medi del dispositivo / efficienza di conversione + W fissi dal lato batteria). Con più dispositivi simultanei somma i W medi.

## Scheda di confronto compilabile
| Dato | Modello A | Modello B |
| --- | --- | --- |
| Capacità nominale (Wh) | Da verificare | Da verificare |
| Potenza AC continua (W) | Da verificare | Da verificare |
| Picco AC (W e durata) | Da verificare | Da verificare |
| Rendimento per uscita | Da verificare | Da verificare |
| Uscite USB-C / DC / AC | Da verificare | Da verificare |
| Peso e dimensioni | Da verificare | Da verificare |
| Garanzia e condizioni | Da verificare | Da verificare |
| Prezzo finale verificato alla data | Da verificare | Da verificare |

## Limiti di sicurezza
Il calcolo non certifica compatibilità, durata garantita, continuità di servizio o idoneità a dispositivi medici. Non collegare una power station alla rete domestica tramite cavi improvvisati e non intervenire sul quadro elettrico senza un professionista qualificato. Consulta i manuali dei dispositivi per carichi, ventilazione, temperatura e collegamenti consentiti.

## FAQ
**Una power station da 1.000 Wh dura 10 ore con 100 W?** Solo idealmente, senza perdite e usando tutta l'energia. Nella pratica può durare meno.

**Una batteria grande può alimentare qualsiasi apparecchio?** No. L'uscita continua e il picco di avvio possono impedire l'uso anche se restano Wh disponibili.

**La ricarica solare garantisce un numero fisso di ore?** No: irraggiamento, ombre, meteo, temperatura e compatibilità del pannello cambiano il risultato.

**Posso usare un calcolatore?** È disponibile in bozza un calcolatore VORLI Lab offline: inserisci i dati del tuo scenario e modifica esplicitamente le ipotesi. Nessun dato viene trasmesso.

## Fonti tecniche (consultate il 01/11/2026)
- BLUETTI, guida tecnica su Wh/W e rendimento: https://it.bluettipower.eu/blogs/guida-allacquisto/accumulatore-di-corrente
- Manuale Jackery Explorer 500 (limiti di uscita e uso): https://it.jackery.com/content/dam/jackery/it/user-guide/portable-power-station/Jackery%20Explorer%20500%20Plus%20Portable%20Power%20Station.pdf

**Nota editoriale:** contenuto educativo indipendente, da revisionare prima della pubblicazione; non contiene prezzi, link affiliati o recensioni simulate.
