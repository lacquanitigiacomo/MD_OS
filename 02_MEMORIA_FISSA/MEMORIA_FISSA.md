# MEMORIA FISSA — MD_OS

## Definizione
La memoria fissa non e una chat lunga.
E un sistema di dataset persistenti, modulari e incrociabili.

---

# STRATI DI MEMORIA

| Strato | Tipo | Funzione |
|---|---|---|
| M01 | Memoria Core | Principi permanenti |
| M02 | Memoria Operativa | Workflow e procedure |
| M03 | Memoria Utente | Preferenze e contesto |
| M04 | Memoria Pattern | Pattern riutilizzabili |
| M05 | Memoria Decisionale | Decisioni gia prese |
| M06 | Memoria Skill | Capacita e strumenti |
| M07 | Memoria Cross-Link | Connessioni semantiche |

---

# STRUTTURA DATASET

```json
{
  "id": "dataset_unico",
  "dominio": "macro-area",
  "tags": ["semantica", "routing"],
  "priorita": 0,
  "compressione": "alta",
  "summary": "contesto compresso",
  "payload": "conoscenza operativa",
  "cross_links": [],
  "quality_score": 0
}
```

---

# REGOLA 10X

La memoria deve:

- diminuire token;
- aumentare precisione;
- aumentare continuita;
- evitare riletture;
- accelerare il runtime;
- costruire apprendimento persistente.
