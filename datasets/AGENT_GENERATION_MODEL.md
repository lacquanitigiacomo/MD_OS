# Dataset Generazione Agenti

## Scopo

Gli agenti non devono essere definiti principalmente da testo statico.

Devono emergere dall'incrocio dei dataset.

## Formula

```text
identità + capability + memoria + ruolo + vincoli + dataset collegati = agente
```

## Dataset sorgente

| Dataset | Contributo |
|---|---|
| `AGENT_CAPABILITIES.md` | capacità operative |
| `DECISIONS.md` | comportamento e regole |
| `KEYWORDS.md` | domini concettuali |
| `BETA_AWARENESS.md` | consapevolezze operative |
| `SESSION_DATASET.md` | cronologia evolutiva |
| `AI_KNOWLEDGE_DATASET.md` | conoscenza AI aggiornata |

## Modello agente

| Campo | Origine |
|---|---|
| identità | registry o dataset capability |
| missione | capability + decisioni |
| memoria | dataset collegati |
| personalità | identity model |
| vincoli | governance + decisioni |
| trigger | workflow e protocolli |
| output | ruolo e matrici |

## Regola

I file dentro `/agents` devono diventare:

- profili sintetici
- override specifici
- comportamento speciale
- eccezioni

Non devono duplicare dataset già esistenti.

## Obiettivo

Ridurre:

- duplicazione
- documentazione ridondante
- inconsistenza
- manutenzione manuale

Aumentare:

- interrogabilità
- modularità
- aggiornamento automatico
- generazione dinamica degli agenti
