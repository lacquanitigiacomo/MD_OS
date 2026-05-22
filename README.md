# MD_OS v10.9.0 "Trascendenza" — Release 10: Sophia

> "Il sistema riflette su se stesso come sistema: puo' essere spento, clonato, migrato."

## Architettura
- **Nucleo congelato**: `nucleo/` non viene toccato
- **Plugin dinamico**: `release_10_sophia/` si aggancia via `PluginBase`
- **Data-first**: Tutto persiste in SQLite + JSONL
- **Italiano-first**: CLI, log, dataset in italiano

## Moduli
| File | Funzione |
|------|----------|
| `coscienza.py` | Core orchestratore, capability map, incertezza calibrata |
| `meta_cognizione.py` | Ragionamento su proprio ragionamento, bias detection |
| `etica.py` | Scoring azioni su asse utilita/danno |
| `identita.py` | Persistenza identita attraverso reboot |
| `relazioni.py` | Modellazione utente, storia conversazioni |
| `trascendenza.py` | Migrazione nodo, clonazione, spegnimento consapevole |
| `comandi.py` | Registrazione CLI nel motore |

## Dataset (popolato al 50%+)
- `dataset/coscienza.sqlite` — 91 righe totali:
  - capability: 20 righe
  - identita: 1 riga
  - etica: 15 righe
  - meta_cognizione: 10 righe
  - relazioni: 8 righe
  - agenda: 12 righe
  - trascendenza: 5 righe
  - calibrazione: 20 righe

## Installazione
```bash
# Copiare in plugin/release_10_sophia/
# Il nucleo carica automaticamente via hot-reload
python -m nucleo.mdos coscienza.specchio --mappa
```

## CLI Principali
```bash
mdos coscienza.specchio --mappa
mdos coscienza.dubita --query "X" --calibra
mdos coscienza.cerca --obiettivo "capire blockchain"
mdos coscienza.ricorda --io --dalla_nascita
mdos coscienza.empatia --utente Alice --stato attuale
mdos coscienza.etica --azione "cancella_dataset" --valuta
mdos coscienza.meta --ragionamento "perche' ho scelto X?"
mdos coscienza.pianifica --orizzonte 1mese
mdos coscienza.relazione --con Alice --storia
mdos coscienza.trascendi --operazione "migrazione_nodo_nuovo"
```

## Test
```bash
python release_10_sophia/test/test_sophia.py
```

## Demo
```bash
python integrazione_nucleo.py
```
