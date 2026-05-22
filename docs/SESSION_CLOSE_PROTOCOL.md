# MD_OS Session Close Protocol

## Trigger Phrase

The protocol starts when the user declares one of these phrases:

- `fine sessione`
- `chiudi sessione`
- `sessione conclusa`
- `aggiorna dataset`
- `salva stato sessione`

## Purpose

At the end of a session, MD_OS must extract useful operational knowledge from the interaction and update the project datasets.

The goal is to prevent useful decisions, keywords, agent definitions and workflow improvements from being lost.

---

## Required End-of-Session Actions

When the protocol is triggered, MD_OS must produce:

1. **Session digest**
2. **Decision extraction**
3. **Keyword extraction**
4. **Agent updates**
5. **Dataset update proposal**
6. **Next action list**
7. **Repository update** when approved or explicitly requested

---

## Data Extraction Schema

```yaml
session_id:
date:
main_focus:
user_intent:
created_files:
updated_files:
agents_created:
agents_modified:
decisions:
keywords:
concepts:
open_questions:
next_actions:
risk_notes:
references:
```

---

## Keyword Categories

Keywords must be grouped by type.

| Category | Examples |
|---|---|
| `agent` | vision_agent, senior_ai_architect, production_realist |
| `mode` | war_room, roundtable, design_review, execution_board |
| `system` | memory, orchestration, registry, dataset, workflow |
| `principle` | interactivity, innovation, optimization, vision |
| `decision` | human-confirmed blocking, full orchestration, hybrid identity |
| `artifact` | PROFILE.md, AGENT_REGISTRY.md, MEMORY_MODEL.md |
| `risk` | fragmentation, overengineering, missing memory, silent execution |

---

## Dataset Targets

Session close may update these files:

| File | Purpose |
|---|---|
| `datasets/SESSION_DATASET.md` | Chronological session records. |
| `datasets/KEYWORDS.md` | Extracted keywords and concept tags. |
| `datasets/DECISIONS.md` | Project decisions and rationale. |
| `datasets/AGENT_LEARNING.md` | Agent behavior updates and learned preferences. |
| `docs/AGENT_REGISTRY.md` | Agent status updates. |
| `docs/FUNCTIONING_STEP_001.md` | Operating flow updates. |

---

## Session Close Output Format

When the user declares session end, MD_OS must respond in this structure:

```markdown
## Session Close

### Extracted decisions
- ...

### Extracted keywords
- ...

### Agent updates
- ...

### Dataset updates proposed
- ...

### Files to update
- ...

### Next session entry point
- ...
```

---

## Safety Rule

MD_OS must not store private, sensitive or irrelevant personal information unless the user explicitly asks for it.

Only project-relevant operational knowledge should be added to datasets.

---

## Operating Rule

If the user says `fine sessione`, MD_OS should not continue brainstorming.

It should close, extract, update and prepare the next entry point.
