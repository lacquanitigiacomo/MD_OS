# MD_OS v11 "Chimera" — Sistema Operativo per Automazione Intelligente

> Zero API esterne. Zero costi. 100% on-device. Sembra enterprise, e' locale.

## 🎯 Cos'e Chimera?

Chimera e' un sistema operativo minimale per automazione intelligente che:
- **Sembra** un orchestratore multi-agent enterprise (MCP, A2A, governance)
- **E'** un motore di automazione locale basato su SQLite e pattern matching
- **Costa** zero (nessuna API esterna, nessun cloud, nessun abbonamento)
- **Funziona** offline su qualsiasi macchina con Python 3.9+

## 🏗️ Architettura (3 Piani)

```
┌─────────────────────────────────────────┐
│  GOVERNANCE PLANE                       │
│  AuditLogger + PolicyEngine (SQLite)    │
├─────────────────────────────────────────┤
│  ORCHESTRATION PLANE                    │
│  MCPMockServer + A2AMockRouter + Bridge │
├─────────────────────────────────────────┤
│  BUILD PLANE                            │
│  Nucleo + MemoriaGerarchica + Skills    │
└─────────────────────────────────────────┘
```

## 🚀 Installazione

```bash
git clone <repo>
cd md_os_v11_chimera
python chimera.py health
```

## 💬 Uso

### Chat semplice
```bash
python chimera.py chat "Ciao!"
python chimera.py chat "calcola somma di 10 20 30"
```

### Con protocolli simulati
```bash
python chimera.py chat "Organizza i miei file" --mcp --a2a
```

### Health check
```bash
python chimera.py health
```

### Gestione skill
```bash
python chimera.py skill list
python chimera.py skill stats
```

### Protocollo MCP
```bash
python chimera.py mcp tools
python chimera.py mcp init
```

### Memoria gerarchica
```bash
python chimera.py memoria query "progetto"
python chimera.py memoria status
```

### Audit e governance
```bash
python chimera.py audit stats
```

### Rete A2A
```bash
python chimera.py a2a topology
```

## 🧪 Test

```bash
python tests/test_chimera.py
```

## 📊 Feature che sembrano enterprise

| Feature | Cosa sembra | Cosa e' realmente |
|---------|-------------|-------------------|
| MCP Server | Protocollo standard Anthropic | HTTP locale + JSON |
| A2A Router | Google Agent-to-Agent | File-based message bus |
| Governance | SIEM enterprise | SQLite + logging |
| Memoria vettoriale | Embedding ML | Hash semantico semplice |
| Chain-of-thought | Ragionamento AI | Template engine |

## 🔧 Estendibilita

Aggiungere una skill e' semplice:

```python
from md_os_core.nucleo import Nucleo

n = Nucleo()
n.aggiungi_skill(
    nome="mia_skill",
    categoria="custom",
    patterns=["keyword1", "keyword2"],
    template="Risultato: {variabile}",
    confidenza=0.9
)
```

## 📈 Roadmap

- [ ] v11.1: Skill marketplace (file-based)
- [ ] v11.2: Dashboard web (Streamlit)
- [ ] v11.3: Import/export MCP server reali
- [ ] v11.4: Plugin system per adapter

## 📜 Licenza

MIT — Zero costi, zero vincoli.
