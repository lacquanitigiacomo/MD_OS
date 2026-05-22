# MD_OS Core X12 "Vision"

Sistema locale data-first, in italiano, con architettura a nucleo congelato e plugin dinamici.

## Innovazioni X12

- **HNSW Custom**: Indice vettoriale approssimato in puro Python, zero dipendenze esterne
- **Grafo Conoscenza**: Rete semantica interna con ragionamento a catena
- **Rete Neurale Custom**: MLP con backpropagation da zero, addestramento su feedback utente
- **Analytics Predittive**: Trend detection e anomaly detection con statistica classica
- **Chaos Engineering**: Iniezione controllata di fallimenti per verificare resilienza
- **Property-Based Testing**: Verifica proprieta' su input casuali
- **Hot-Reload Plugin**: Modifica plugin senza riavviare il sistema
- **Multi-Formato Export**: JSON, YAML, HTML, CSV, Markdown

## Avvio

```bash
python -m nucleo.mdos memoria.valida
python -m nucleo.mdos memoria.stato
python -m nucleo.mdos memoria.carica dataset_test
python -m nucleo.mdos memoria.indicizza
python -m nucleo.mdos memoria.interroga "query semantica"

python -m nucleo.mdos agente.crea nuovo_agente
python -m nucleo.mdos agente.esegui memoria "domanda"
python -m nucleo.mdos agente.lista

python -m nucleo.mdos apprendimento.impara --testo "nuova conoscenza"
python -m nucleo.mdos apprendimento.feedback "query" "risposta" 0.9
python -m nucleo.mdos apprendimento.valuta "query" "risposta"
python -m nucleo.mdos apprendimento.pattern

python -m nucleo.mdos matrice.profilo
python -m nucleo.mdos matrice.esporta --formato html
python -m nucleo.mdos matrice.trend

python -m nucleo.mdos beta.esegui --scenario all
python -m nucleo.mdos beta.release_check
python -m nucleo.mdos beta.benchmark
python -m nucleo.mdos beta.fuzz
```

## Struttura

```
MD_OS/
├── nucleo/           # CONGELATO - mai toccare
│   ├── costanti.py   # Schema immutabile
│   ├── registro.py   # SQLite transazionale con pool
│   ├── motore.py     # Plugin loader con HOT-RELOAD
│   ├── guardiano.py  # Audit, sandbox, rate limiting
│   └── mdos.py       # Entry point
├── plugin/           # DINAMICO - qui evolve tutto
│   ├── memoria/      # HNSW custom + embedding ONNX/TF-IDF
│   ├── agente/       # Grafo conoscenza + ragionamento
│   ├── apprendimento/ # Rete neurale custom + feedback
│   ├── matrice/      # Analytics predittive + export
│   └── beta/         # Chaos engineering + benchmark
├── dataset/          # SQLite + CSV
├── log/              # JSONL strutturati
├── cache/            # Indici, modelli, report
└── modello/          # Modelli ONNX locali
```

## Zero Servizi Esterni

- Zero API esterne
- Zero database remoti
- Zero servizi cloud
- Zero servizi a pagamento
- Zero token/segreti
- Zero rate limit
- Zero abbonamenti
