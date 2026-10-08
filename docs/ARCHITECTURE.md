# Architettura v1

## Gratis oggi
- GitHub Free + GitHub Pages per il sito.
- GitHub Actions per rebuild automatici su repository pubblico.
- Python standard library per ranking e generazione.
- JSON come archivio semplice.

## AI
L'accesso a un modello generativo remoto non è incluso gratuitamente in modo affidabile: GitHub Models è stato ritirato il 30 luglio 2026. Per questo il progetto non finge di avere una API AI gratuita. Il modulo `content_engine.py` usa template deterministici finché non viene collegato un modello che l'utente è autorizzato a usare senza costi.

## Evoluzione
1. Feed/API dei network autorizzati.
2. Import prodotti con timestamp e fonte.
3. Ranking automatico.
4. Generazione contenuti con modello disponibile gratuitamente.
5. Pubblicazione automatica.
6. Analytics e feedback loop.
