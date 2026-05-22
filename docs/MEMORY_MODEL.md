# Modello Memoria

## Scopo

Definire come MD_OS conserva conoscenza utile nel tempo.

## Tipi memoria

| Tipo | Dove vive |
|---|---|
| globale | dataset principali |
| ruolo | `MEMORY_SCOPES.csv` e override agente |
| sessione | output temporaneo poi `LEARNING_EVENTS.jsonl` |
| ricerca | `AI_KNOWLEDGE.csv` e `SOURCES.csv` |

## Regola

La memoria non è una biografia. È contesto operativo riutilizzabile.
