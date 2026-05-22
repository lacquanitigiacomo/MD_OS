# MD_OS External Intelligence Radar v30

## Promessa

Questa patch permette a MD_OS di analizzare riferimenti esterni, classificarli, valutarli e trasformarli in pattern integrabili.

Non serve accumulare link.  
Ogni riferimento deve generare una decisione.

## Cosa aggiunge

- `INNOVATION_RADAR`
- `LOCAL_AI_STRATEGY`
- `benchmark_integration_report`
- `benchmark_scorecard`
- `local_ai_plan`
- dataset di scoring e ingestione riferimenti
- agenti curator e analyst

## Fonti benchmark già considerate

| Riferimento | Pattern principale |
|---|---|
| `vercel-labs/agent-skills` | skill operative |
| `Significant-Gravitas/AutoGPT` | autonomous task loop |
| `sindresorhus/awesome-chatgpt` | catalogo curato |
| `nomic-ai/gpt4all` | AI locale e LocalDocs |
| `taishi-i/awesome-ChatGPT-repositories` | radar repository, scoring e ricerca |

## Flusso operativo

```text
link esterno
→ classificazione
→ pattern utili
→ pattern da scartare
→ score
→ adattamento MD_OS
→ patch eventuale
```

## Comandi

- `ANALIZZA GITHUB: <repo>`
- `RADAR INNOVAZIONE: <link>`
- `BENCHMARK REPO: <repo>`
- `INTEGRIAMO QUESTO: <repo>`
- `LOCAL AI STRATEGY: <scenario>`

## Regola

Non copiare sistemi esterni.  
Estrarre pattern, adattarli a MD_OS v30 e integrare solo ciò che aumenta leva, coerenza e velocità.
