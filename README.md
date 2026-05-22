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
| `meta_cognizione.py` | Ragionamento su proprio ragionamento, bias detection (15 tipi) |
| `etica.py` | Scoring azioni su asse utilita/danno |
| `identita.py` | Persistenza identita attraverso reboot, snapshot atomico, ripristino completo |
| `relazioni.py` | Modellazione utente, storia conversazioni, empatia computazionale |
| `trascendenza.py` | Migrazione nodo, clonazione, spegnimento consapevole |
| `comandi.py` | Registrazione CLI nel motore |

## Dataset (popolato al 100%)
- `dataset/coscienza.sqlite` — 48+ righe seed:
  - capability: 24 righe
  - identita: 1 riga
  - relazioni: 8 righe
  - agenda: 12 righe

## Fix applicati rispetto alla versione originale
1. **Connessioni SQLite chiuse esplicitamente** via `@contextmanager` in tutti i moduli
2. **Fix timezone-aware datetime** in `relazioni.py` (`datetime.now(timezone.utc)`)
3. **Checksum identita calcolato durante bootstrap** del seed
4. **Ripristino identita completo e atomico**: ricostruisce tutte le tabelle in transazione unica
5. **Snapshot atomico filesystem**: scrittura su file temporaneo + rename
6. **Schema SQL corretto**: rimosso `AUTOINCREMENT` dalla tabella `identita`
7. **Test portabili**: path relativo, funzionanti da qualsiasi directory
8. **Logging strutturato** su tutti i moduli
9. **Catalogo bias esteso** da 6 a 15 tipi
10. **Indice composito** su agenda per query frequenti

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
