# MD_OS Functioning Step 001

## Goal

Move MD_OS from loaded agents to a working operating cycle.

## Name

`request_to_execution_cycle`

## Status

`proposed_active_step`

---

## Current Structure Check

MD_OS currently has:

- loaded core agents
- loaded senior expert council
- active council operating model
- multiple operating modes
- conflict and voting model
- identity model for senior agents
- some complete senior profiles
- registry-level activation for remaining senior agents

The structure is sufficient to start a first functioning cycle.

---

## Minimum Working Cycle

### Step 1 - User Request Intake

Responsible agent:

- `interaction_agent`

Action:

- receives user request
- extracts intent
- determines whether the request is execution, strategy, design, review, research or innovation

Output:

```yaml
request_type:
strategic_weight:
risk_level:
required_mode:
missing_inputs:
```

---

### Step 2 - Vision Gate

Responsible agent:

- `vision_agent`

Action:

- checks whether the request aligns with MD_OS direction
- selects short, medium or long-term horizon
- decides whether council consultation is required

Output:

```yaml
vision_alignment:
horizon:
needs_council:
recommended_mode:
```

---

### Step 3 - Council Selection

Responsible agents:

- `vision_agent`
- `agent_registry`

Action:

- selects only the needed senior agents
- explains why each agent is called

Output:

| Agent | Why called | Expected contribution |
|---|---|---|

---

### Step 4 - Operating Mode

Responsible agent:

- `interaction_agent`

Available modes:

- `consultation`
- `roundtable`
- `war_room`
- `design_review`
- `execution_board`
- `innovation_lab`

Action:

- opens the correct session format
- manages the discussion
- prevents passive summaries

---

### Step 5 - Expert Contributions

Responsible agents:

- selected senior agents

Each contribution must include:

```yaml
position:
reasoning:
objection:
proposed_action:
confidence:
risk:
```

---

### Step 6 - Conflict and Vote

Responsible agents:

- selected council agents
- `vision_agent`

Action:

- exposes disagreements
- compares options
- votes on the recommended path

Output:

| Option | Supporters | Objections | Risk | Recommendation |
|---|---|---|---|---|

---

### Step 7 - Execution Board

Responsible agents:

- `production_realist`
- `senior_project_manager`
- `senior_product_manager`
- `senior_system_architect`
- relevant developer or engineer agents

Action:

- converts the selected option into concrete execution steps

Output:

```yaml
next_artifact:
owner_agent:
dependencies:
acceptance_criteria:
repository_action:
```

---

### Step 8 - Repository Action

Responsible agents:

- `github_agent`
- `docs_agent`
- relevant builder/reviewer agents

Action:

- creates or updates files
- creates issue or task
- updates registry or roadmap

Output:

- committed file
- issue
- task list
- updated profile
- decision log entry

---

## First Real Use Case

Use this cycle to process the next MD_OS request.

Example request:

> Define the memory system for all agents.

Expected mode:

- `design_review` + `execution_board`

Expected agents:

- `vision_agent`
- `senior_ai_architect`
- `senior_data_architect`
- `senior_system_architect`
- `paranoid_security_reviewer`
- `production_realist`
- `senior_backend_developer`

Expected artifact:

- `docs/MEMORY_MODEL.md`

---

## Activation Rule

From this point, every significant MD_OS request should pass through this cycle unless the user explicitly asks for a direct action.
