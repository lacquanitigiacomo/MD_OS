# CHIMERA 2.0 Neural Mesh — Functional Stable v2.0.1

Local-first automation platform with **pluggable agents**. Every agent is a real, executable module.

## Agents Included

| Agent | Type | Capabilities |
|-------|------|--------------|
| `echo` | Debug | Pass values through, inspect inputs/config |
| `web_search` | Online | DuckDuckGo search (HTML, no API key). Auto-fallback to offline mode if no network |
| `python` | Compute | Execute arbitrary Python in isolated subprocess with full stdlib access |
| `file_read` | I/O | Read local files (JSON/text). Resolves paths relative to project root |
| `file_write` | I/O | Write JSON/text to local files. Auto-creates directories |
| `transform` | Data | `pass`, `extract_field`, `count`, `join_strings`, `to_markdown` |

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Initialize the local SQLite database
python run.py init

# 3. Run the default offline demo (no internet required)
python run.py run

# 4. To run the web search demo (requires internet)
CHIMERA_CONFIG=config_web.yaml python run.py run
```

## Offline Demo (Default)

The default `config.yaml` runs a fully local pipeline:

1. **generate_data** — Python agent creates a random dataset
2. **analyze** — Python agent computes statistics (mean, max, min)
3. **format_report** — Transform agent converts to Markdown
4. **save_report** — FileWrite agent persists `data/report.md`
5. **verify** — FileRead agent reads back and confirms the file

This proves the entire mesh works without any external service.

## Web Search Demo

Use `config_web.yaml` for an online pipeline:

1. **query_input** — Echo agent provides a search query
2. **web_search** — Searches DuckDuckGo and returns structured results
3. **to_markdown** — Formats results as Markdown
4. **save_report** — Writes `data/web_report.md`
5. **verify_file** — Reads back the report

If the network is unavailable, set `offline_mode: true` in the `web_search` node config to receive mock results instead of crashing.

## Architecture

```
chimera/
  agents/
    base.py          — Abstract base class for all agents
    echo.py          — Pass-through / debug
    web_search.py    — DuckDuckGo HTML scraping with offline fallback
    python.py        — Subprocess-based Python execution
    file_io.py       — Local file read/write
    transform.py     — Data reshaping and Markdown formatting
  config.py          — Robust YAML loader with env overrides
  database.py        — SQLite local-first persistence
  mesh.py            — DAG scheduler with per-node logging
  cli.py             — init / run / status commands
```

## Environment Variables

- `CHIMERA_CONFIG` — Override path to config YAML (default: `config.yaml`)
- `CHIMERA_DB_PATH` — Override path to SQLite database (default: `./data/chimera.db`)

## Writing Custom Agents

Create a new file in `chimera/agents/`:

```python
from .base import BaseAgent

class MyAgent(BaseAgent):
    def execute(self, inputs, config):
        # inputs: dict of predecessor node_id -> result
        # config: dict from config.yaml node config section
        return {"agent": "my_agent", "result": "done"}
```

Then register it in `chimera/agents/__init__.py`:

```python
from .my_agent import MyAgent
REGISTRY["my_agent"] = MyAgent
```

## Stability Notes

- **Database path** is always resolved relative to the project root.
- **YAML** uses `safe_load` only; malformed files produce readable errors.
- **Execution** stops on first node failure and logs the error to SQLite.
- **Cycles** in the graph are detected and reported.
- **Python agent** runs in a subprocess with a 10-second timeout to prevent runaway code.
- **Web search** gracefully degrades when offline; never hangs indefinitely.
