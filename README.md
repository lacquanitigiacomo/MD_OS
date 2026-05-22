# MD_OS Stable Core X10

Sistema locale eseguibile, data-first, in italiano, con agenti derivati da dataset, refactor X10, apprendimento incrementale, query interna, matrici e release check.

## Avvio

```bash
python mdos.py validate
python mdos.py status
python mdos.py query memoria retrieval agenti
python mdos.py refactor --goal "migliorare memoria, retrieval e agenti"
python mdos.py learn --text "Nuova decisione: i dataset sono la fonte primaria"
python mdos.py matrix
python mdos.py profile
python mdos.py release-check
python mdos.py beta --scenario memory_failure
```

## Regola X10

Ogni `refactor` deve produrre almeno 10 avanzamenti concreti.

## Struttura congelata

L'evoluzione avviene tramite dataset, plugin, log, export e matrici, non cambiando continuamente cartelle.
