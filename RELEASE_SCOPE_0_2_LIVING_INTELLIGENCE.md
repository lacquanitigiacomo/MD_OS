# MD_OS Release Scope 0.2

## Name

Living Intelligence

## Goal

MD_OS 0.2 must become a learning operating system.

It must know its own internal state, detect missing knowledge, request or search for what is missing, synthesize new information and persist learning in repository datasets.

## Knowledge Zones

| Zone | Meaning |
|---|---|
| Known | already stored in repository files or datasets |
| Unknown | missing from current files and datasets |
| Learned | newly acquired and stored after validation |

## Required Systems

- memory model
- retrieval model
- knowledge gap detector
- learning ingestion protocol
- source validation protocol
- agent learning dataset
- knowledge graph dataset
- unknowns dataset
- source index
- living intelligence test checklist

## Required Agents

- memory_agent
- retrieval_agent
- knowledge_gap_agent
- learning_ingestion_agent
- source_validation_agent
- synthesis_agent
- knowledge_graph_agent
- curriculum_agent
- reflection_agent
- update_planner_agent

## Release Criteria

MD_OS 0.2 is valid only if it can:

1. inspect internal files
2. identify known knowledge
3. identify unknown knowledge
4. request or search missing references
5. synthesize information
6. produce an artifact
7. update datasets
8. update agents when needed
9. record learning for future sessions
10. improve later behavior from stored learning

## Constraint

MD_OS must not pretend to know everything.

It must know what it has, detect what it lacks and learn through validated input.
