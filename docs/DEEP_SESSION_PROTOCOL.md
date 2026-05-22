# MD_OS Deep Session Protocol

## Rule 0 - No Passive Summaries

A deep session must produce at least one concrete artifact:

- agent profile
- architecture file
- issue
- decision log entry
- roadmap update
- configuration file
- prototype spec
- workflow definition

No session ends with only discussion.

---

## Session Loop

Each session follows this loop:

1. **Focus** - choose one system area or one agent.
2. **Interrogation** - ask only the questions needed to define it.
3. **Reference Intake** - collect useful links, examples, repositories, products or patterns.
4. **Profile Draft** - define mission, inputs, outputs, permissions, limits and metrics.
5. **Implementation Target** - decide which file, issue or module must be created.
6. **Commit** - write the artifact to the repository.
7. **Next Step** - select the next agent or system layer.

---

## Session Types

| Code | Session | Output |
|---|---|---|
| S01 | Vision Calibration | `docs/VISION.md` |
| S02 | Agent Profiling | `agents/<agent_id>/PROFILE.md` |
| S03 | Agent Registry Update | `docs/AGENT_REGISTRY.md` |
| S04 | Architecture Design | `docs/ARCHITECTURE.md` |
| S05 | Interaction Design | `docs/INTERACTION_MODEL.md` |
| S06 | Optimization Design | `docs/OPTIMIZATION_MODEL.md` |
| S07 | Innovation Design | `docs/INNOVATION_MODEL.md` |
| S08 | Memory Design | `docs/MEMORY_MODEL.md` |
| S09 | Governance Design | `docs/GOVERNANCE.md` |
| S10 | Build Sprint | concrete files, scripts, configs or issues |

---

## Agent Profiling Template

Each agent profile must contain:

- Agent ID
- Human name
- Mission
- Activation trigger
- Inputs
- Outputs
- Allowed actions
- Forbidden actions
- Required approvals
- Dependencies
- Memory fields
- Failure modes
- Success metrics
- Example prompts
- Links and references
- Open questions

---

## Auto-Update Sessions

MD_OS should run periodic self-update sessions manually triggered by the user.

| Session | Frequency | Purpose |
|---|---:|---|
| System Review | weekly | identify drift, outdated assumptions and broken structure |
| Agent Review | per new agent | refine profile, permissions and outputs |
| Roadmap Review | weekly or after major decision | reorder priorities |
| Repository Review | after structural changes | verify files, docs and workflows |
| Vision Review | monthly | check whether MD_OS still follows its purpose |

---

## Question Discipline

Questions must be direct and bounded.

Bad:

- What do you want MD_OS to be?

Good:

- Should this agent be allowed to modify files directly, or only propose patches?
- Should this agent optimize for speed, quality, cost or autonomy first?
- Which existing product, repo or workflow should this agent learn from?

---

## Current Working Mode

The project enters deep creation mode.

The assistant must:

- avoid long introductions
- avoid passive summaries
- ask targeted questions
- produce repository artifacts
- profile one agent at a time
- keep decision records
- convert answers into files
