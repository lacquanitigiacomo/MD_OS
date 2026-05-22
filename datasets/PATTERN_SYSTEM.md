# Dataset Pattern di Sistema

## Scopo

Registrare pattern ricorrenti rilevati durante progettazione, debug, release e apprendimento.

## Pattern rilevati

| ID | Pattern | Descrizione | Impatto |
|---|---|---|---|
| PAT-001 | Troppi file statici | La conoscenza tende a disperdersi in markdown ridondanti | alta |
| PAT-002 | Dataset come cervello | I dataset diventano il layer cognitivo centrale | critica |
| PAT-003 | Agenti emergenti | Gli agenti funzionano meglio se derivati dai dataset | alta |
| PAT-004 | Conflitto utile | I conflitti controllati migliorano decisioni e qualità | alta |
| PAT-005 | Memoria mancante | Senza retrieval e memoria il sistema perde continuità | critica |
| PAT-006 | Runtime incompleto | Esiste governance ma manca esecuzione runtime reale | critica |
| PAT-007 | Beta loop efficace | Build, emulate, debug e learn produce miglioramenti reali | alta |
| PAT-008 | Root troppo rumorosa | Troppi file nella root riducono leggibilità | media |
| PAT-009 | Documentazione duplicata | Profili agenti duplicano dati già presenti nei dataset | alta |
| PAT-010 | AI knowledge velocity | Le novità AI richiedono apprendimento continuo | critica |

## Regola

I pattern ad alto o critico impatto devono generare:

- patch
- task
- protocolli
- release blocker
- miglioramenti architetturali
