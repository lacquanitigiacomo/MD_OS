# Dataset Innovazioni Incrementali

## Scopo

Questo dataset raccoglie innovazioni incrementali applicabili a MD_OS senza stravolgere la struttura esistente.

Ogni innovazione deve avere:

- codice stabile
- valore operativo
- agenti coinvolti
- dataset impattati
- pattern generati
- stato di avanzamento

## Innovazioni

| ID | Innovazione | Valore operativo | Agenti coinvolti | Dataset impattati | Stato |
|---|---|---|---|---|---|
| INN-001 | Profilazione automatica keyword | Estrae keyword da ogni sessione e le classifica | interaction_agent, dataset_curator_agent | KEYWORDS, SESSION_DATASET | proposta |
| INN-002 | Pattern miner di sistema | Rileva pattern ricorrenti da decisioni, debug e sessioni | pattern_miner_agent, optimization_agent | PATTERN_SYSTEM, DECISIONS | proposta |
| INN-003 | Generazione agenti da dataset | Crea profili agenti incrociando capability, decisioni e keyword | agent_registry, capability_mapper_agent | AGENT_CAPABILITIES, AGENT_GENERATION_MODEL | proposta |
| INN-004 | Matrice maturità moduli | Misura quanto ogni area è idea, bozza, operativa o stabile | matrix_builder_agent, production_realist | MATURITY_MATRIX | proposta |
| INN-005 | Mappa gap conoscenza | Registra ciò che MD_OS non sa ancora e come impararlo | knowledge_gap_agent, retrieval_agent | UNKNOWNS, SOURCE_INDEX | proposta |
| INN-006 | Motore confronto opzioni | Confronta alternative con pro, contro, rischio e impatto | vision_agent, senior_system_architect | DECISION_OPTIONS | proposta |
| INN-007 | Diario apprendimento agente | Registra cosa ogni agente ha imparato e cosa deve migliorare | reflection_agent, memory_agent | AGENT_LEARNING | proposta |
| INN-008 | Ranking priorità release | Ordina backlog per valore, sforzo, rischio e dipendenze | chief_product_strategist, production_realist | FEATURE_BACKLOG, RELEASE_PRIORITY | proposta |
| INN-009 | Protocollo revisione documenti | Decide se un file deve stare in root, docs, datasets o agents | senior_technical_writer, senior_information_architect | ARCHITETTURA_REPOSITORY | proposta |
| INN-010 | Beta feedback loop | Trasforma errori beta in fix, dataset e release blocker | optimization_agent, senior_qa_engineer | BETA_AWARENESS, RELEASE_BLOCKERS | proposta |

## Regola

Ogni innovazione deve poter essere interrogata come dato, non solo letta come descrizione.

## Prossima azione

Convertire le innovazioni prioritarie in issue o patch operative.
