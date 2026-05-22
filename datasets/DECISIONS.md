# MD_OS Decisions Dataset

## Purpose

This dataset stores project decisions extracted from guided learning sessions.

## Format

Each decision must include:

- date
- session focus
- decision
- reason
- affected agents
- affected files
- next action

---

## Decisions

### D001 - Human-confirmed strategic blocking

- date: 2026-05-22
- session focus: vision_agent authority
- decision: vision_agent can block incoherent decisions only after showing options and asking for human confirmation
- reason: preserve strategic control without silent execution
- affected agents: vision_agent
- next action: continue profiling agent authority and escalation rules

### D002 - Multi-horizon vision model

- date: 2026-05-22
- session focus: vision_agent horizon
- decision: vision_agent must reason across short, medium and long term horizons
- reason: MD_OS needs operational, roadmap and strategic continuity
- affected agents: vision_agent
- next action: connect horizons to roadmap and execution cycle

### D003 - Senior expert council activation

- date: 2026-05-22
- session focus: agent system structure
- decision: MD_OS requires senior visionary, architect, developer, engineer, product, governance, UX and innovation agents
- reason: complex design requires specialist perspectives and controlled conflict
- affected agents: senior expert council
- next action: profile senior agents progressively

### D004 - Hybrid senior identity model

- date: 2026-05-22
- session focus: senior agent behavior
- decision: senior agents must have both technical identity and persona identity
- reason: technical clarity plus behavioral diversity improves council output
- affected agents: all senior agents
- next action: assign personas to all active senior agents

### D005 - Session close dataset update

- date: 2026-05-22
- session focus: guided learning sessions
- decision: when the user declares session end, MD_OS must extract decisions, keywords, agent updates and next actions into repository datasets
- reason: preserve learning across sessions and make MD_OS cumulative
- affected agents: interaction_agent, memory_agent, agent_registry
- next action: implement guided learning protocol

### D006 - Beta emulation workspace

- date: 2026-05-22
- session focus: beta testing and debug
- decision: MD_OS needs a dedicated beta workspace for emulation, scenarios, reports and experiments
- reason: system quality improves when ideas are tested before release promotion
- affected agents: vision_agent, interaction_agent, optimization_agent, production_realist
- affected files: beta/README.md, beta/scenarios/SCENARIO_001_MEMORY_FAILURE.md, beta/debug/DEBUG_REPORT_001.md
- next action: use beta results to prioritize memory, retrieval and validation layers

### D007 - Build-emulate-debug-learn cycle

- date: 2026-05-22
- session focus: operating method
- decision: MD_OS should use a build, emulate, fail, debug, patch, learn and release cycle
- reason: this turns design into tested system evolution
- affected agents: all operating agents
- affected files: datasets/SESSION_DATASET.md, datasets/KEYWORDS.md, datasets/BETA_AWARENESS.md
- next action: record beta findings as release blockers and improvement inputs
