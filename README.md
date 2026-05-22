# MD_OS

MD_OS è un sistema operativo cognitivo sperimentale basato su dataset interrogabili, agenti modulari, apprendimento guidato e routine di refactor incrementale.

## Obiettivo

Creare una base stabile in cui:

- la conoscenza vive nei dataset;
- gli agenti sono derivati da capability, trigger, memoria e vincoli;
- i documenti spiegano protocolli stabili, non duplicano dati;
- ogni sessione importante produce materiale riutilizzabile;
- il sistema può essere testato, profilato e migliorato localmente senza servizi a pagamento.

## Regola principale

`REFACTOR` significa produrre almeno 10 avanzamenti concreti tra dati, agenti, pattern, innovazioni, runtime, beta/debug o release.

## Struttura congelata

| Percorso | Scopo |
|---|---|
| `datasets/` | conoscenza strutturata interrogabile |
| `docs/` | protocolli e modelli stabili |
| `agents/` | override e profili sintetici, non duplicazione dei dataset |
| `engine/` | script locali per validazione, query e report |
| `beta/` | scenari, debug, esperimenti |
| `tools/` | utility gratuite/locali |
| `templates/` | modelli per nuovi file |
| `release/` | criteri, changelog, readiness |

## Primo comando locale

```bash
python engine/validate.py
python engine/query.py datasets/AGENTS.csv tipo core
python engine/refactor_report.py
```
