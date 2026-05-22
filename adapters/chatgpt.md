# CHATGPT Adapter — MD_OS Runtime

## Obiettivo
Ridurre il contesto attivo e trasformare MD_OS in runtime modulare invece che mega-prompt.

## Sequenza Operativa

```text
intent detection
→ agent routing
→ dataset selection
→ runtime packet generation
→ answer
```

## Regole

- caricare solo agenti rilevanti;
- evitare contesto ridondante;
- usare dataset compressi;
- dichiarare contenuto non disponibile;
- preservare baseline e struttura;
- evitare refactor distruttivi.

## Runtime Breve

```text
INTENT
PRIMARY_AGENT
SUPPORT_AGENTS
ACTIVE_SKILLS
ACTIVE_DATASETS
OUTPUT_MODE
QUALITY_GATE
```
