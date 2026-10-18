# VORLI Lab — QA di prepubblicazione: Passaporto blackout tecnologico
**Revisione statica aggiornata il 18 ottobre 2026 · documento interno alla bozza pubblica · NON approvato per vendita/pubblicazione**

## Oggetto e perimetro
File esaminato: `docs/drafts/printables/passaporto-blackout-tecnologico-A4-2026-10-18.html` (stesso branch).
Questo controllo riguarda esclusivamente il codice HTML/CSS letto nel repository, **non** una prova di stampa, un audit di accessibilità o una verifica legale.

## Controlli statici effettuati
| Verifica | Esito | Evidenza |
|---|---|---|
| Quattro sezioni stampabili | OK nel sorgente | Quattro elementi `section.page`, con footer 1/4–4/4 |
| Impostazione A4 | Presente, non collaudata | `@page { size:A4; margin:0; }` e pagine con `min-height:297mm` |
| Contenuto educativo e prudente | Presente | Avvertenze su combustione in ambienti chiusi, collegamenti improvvisati e dispositivi medici |
| Formule energetiche | Controllo aritmetico | Esempio 20 W × 3 ore = 60 Wh, prima delle perdite |
| Assenza di monetizzazione nel file | OK nel sorgente | Nessun checkout, prezzo, modulo di raccolta dati o link affiliato |
| Dipendenze remote | Nessuna nel sorgente | CSS incorporato, nessuno script, immagine o font esterno |
| Contatti/identificativi privati | Nessuno individuato nel file esaminato | Non equivale a una bonifica dell'intero repository o della sua cronologia |
| Test effettivo di stampa | **NON ESEGUITO** | Le modifiche CSS non dimostrano che il PDF contenga esattamente 4 pagine |
| Accessibilità | **DA COLLAUDARE** | Tabelle, leggibilità e navigazione con tecnologie assistive |
| Conformità commerciale/fiscale | **NON VERIFICATA** | Recesso digitale, IVA, venditore individuale italiano, disclosure |

## Rischi editoriali da risolvere
1. **Impaginazione:** la regola di stampa ora imposta `height:297mm` e `break-inside:avoid` per ciascuna scheda, ma footer assoluto e tabelle potrebbero ancora creare sovrapposizioni o pagine extra. Occorre un collaudo PDF reale.
2. **Leggibilità:** tabelle e footer sono stati aumentati rispettivamente a 9,5 pt e 9 pt; le celle vuote devono comunque essere valutate in stampa reale, soprattutto in bianco e nero.
3. **Uso offline:** controllare che stampa e salvataggio PDF funzionino senza rete e senza perdita di bordi/contrasti.
4. **Sicurezza:** far verificare da una persona competente formulazioni tecniche, limiti dei dispositivi e disclaimer; non sostituire indicazioni di autorità o produttori.
5. **Coerenza editoriale:** le note interne sono state rimosse dalla quarta pagina e sostituite con una checklist per il lettore. La dicitura BOZZA resta intenzionalmente presente, perché il prodotto non è pronto per il pubblico.
6. **Privacy generale:** la pulizia del file `data/config.json` proposta nella PR di bonifica privacy non cancella eventuali informazioni già presenti nella cronologia Git pubblica.

## Modifiche statiche effettuate in questo ciclo
- Rimosso il paragrafo di note editoriali dalla quarta pagina; inserito un promemoria per il lettore.
- Impostata altezza A4 esplicita nella regola CSS di stampa e aggiunte indicazioni per evitare spezzature delle sezioni.
- Aumentata la dimensione delle tabelle e dei footer; le caselle decorative sono marcate `aria-hidden`.
- **Non eseguiti** rendering PDF, verifica della paginazione effettiva, prova in bianco e nero, controllo con lettore di schermo o revisione legale/tecnica.

## Controllo aggiuntivo di accessibilità del sorgente (18/10/2026)
- Le **16 intestazioni** delle quattro tabelle ora usano `<th scope="col">`, così la funzione di intestazione di colonna è esplicita.
- Le **10 caselle decorative** precedentemente prive di `aria-hidden` sono state marcate `aria-hidden="true"`; le altre erano già marcate. Le caselle restano decorative e non sono controlli interattivi.
- Controllo programmatico sul sorgente aggiornato: **4** elementi `section.page`, **4** riferimenti `aria-labelledby` risolti a ID esistenti, nessun ID duplicato, nessun indirizzo email individuato nel file HTML.
- Commit della correzione HTML: `69cad2b8`.
- **Limiti:** questo controllo statico non è una prova con lettore di schermo né una prova di stampa. Non certifica accessibilità, impaginazione o conformità legale.

## Protocollo di collaudo prima di qualsiasi rilascio
- Aprire il file HTML localmente in Chrome desktop; stampare in PDF con A4, scala 100%, intestazioni/piè di pagina del browser disattivati. **Accettazione:** esattamente 4 pagine, nessun contenuto tagliato, footer leggibili.
- Ripetere in bianco e nero e con stampa senza grafica di sfondo. **Accettazione:** avvertenze e celle rimangono distinguibili.
- Verificare il salvataggio PDF da Chrome Android e la visualizzazione su smartphone. **Accettazione:** contenuto completo e testo selezionabile nel PDF.
- Verificare la navigazione con lettore di schermo e le intestazioni di tabella. **Accettazione:** sequenza logica e informazioni comprensibili.
- Rivedere tutte le avvertenze di sicurezza e i riferimenti normativi con fonti ufficiali aggiornate e consulenza appropriata.
- Solo dopo i test, creare una versione finale separata e sottoporla a revisione. **Nessuna pubblicazione automatica, checkout, pagamento o affiliazione.**

## Stato di rilascio
**BLOCCATO — bozza per revisione.** La presenza di un file HTML stampabile non significa che il prodotto sia pronto per essere distribuito o venduto. Nessuna modifica al sito pubblico è autorizzata da questa checklist.

## Fonti pubbliche e perimetro commerciale (consultazione 18/10/2026)
- [AGCM — riconoscibilità della comunicazione pubblicitaria](https://www.agcm.it/media/comunicati-stampa/2018/12/L%27Antitrust-chiude-anche-la-seconda-moral-suasion-su-influencer-e-marchi%2C-ma-avvia-istruttoria-per-possibili-promozioni-occulte/): l'eventuale futura promozione affiliata dovrà essere identificabile; il prototipo non contiene affiliazioni.
- [Awin — FAQ ufficiali italiane](https://www.awin.com/it/faq): l'approvazione di un publisher non equivale all'approvazione di ogni programma advertiser; commissioni e termini individuali richiedono la dashboard.
- [Awin — eWeki IT, profilo pubblico 19988](https://ui.awin.com/merchant-profile/19988): settore elettronica di consumo e cookie pubblico di 30 giorni; commissione individuale e stato contrattuale **non verificati**.
- La revisione del workbook **non** risolve obblighi IVA, recesso sui contenuti digitali o altri requisiti per la vendita diretta da parte di un venditore individuale italiano. Non trarre conclusioni fiscali senza verifica professionale.
