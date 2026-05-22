# Dataset Architettura Repository

## Scopo

Questo dataset definisce come deve essere ordinato il repository MD_OS.

## Principio

I file narrativi devono essere ridotti al minimo. Le informazioni operative devono vivere in dataset interrogabili.

## Struttura proposta

| Percorso | Funzione | Regola |
|---|---|---|
| `/` | file rapidi di orientamento | pochi file, sempre sovrascrivibili |
| `/docs` | documenti stabili e protocolli | solo file completi e redatti bene |
| `/datasets` | conoscenza strutturata interrogabile | fonte primaria del sistema |
| `/agents` | profili agenti generati o derivati dai dataset | niente duplicazioni inutili |
| `/beta` | test, debug, scenari e simulazioni | spazio sperimentale |
| `/patches` | proposte di modifica | ingresso prima della release |

## File root ammessi

| File | Scopo |
|---|---|
| `README.md` | panoramica essenziale del progetto |
| `STATUS.md` | stato corrente sintetico |
| `ROADMAP.md` | prossime milestone |
| `RELEASE.md` | release attuale e criteri |
| `INDEX.md` | indice operativo dei file importanti |

## Regola di migrazione

Un file `.md` descrittivo deve diventare dataset quando contiene:

- liste di agenti
- matrici
- stati
- capability
- decisioni
- keyword
- dipendenze
- funzioni
- protocolli ripetibili

Un file resta in `/docs` solo se spiega un comportamento stabile o una regola di sistema.
