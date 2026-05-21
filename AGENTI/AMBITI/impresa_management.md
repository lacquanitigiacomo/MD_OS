---
id_ambito: IMPRESA_MANAGEMENT
nome: Impresa Management
stato: attivo
versione: 1.0.0
cartella_agenti: AGENTI/AGENTI-SINGOLI/IMPRESA_MANAGEMENT/
trigger: ['strategia', 'project_management', 'operations', 'vendite', 'processi']
tag: ['strategia', 'project_management', 'operations', 'vendite', 'processi', 'leadership']
dataset_collegati:
  - DATASET/IMPRESA_MANAGEMENT/dataset_operativo.md
---

# Ambito — Impresa Management

## Identità ambito
Macro-area operativa per impresa management.

## Sottoaree
- strategia
- project_management
- operations
- vendite
- processi
- leadership

## Funzioni comuni di ambito
- classificare richieste;
- selezionare agenti pertinenti;
- applicare dataset di ambito;
- produrre output specifici;
- proporre patch di miglioramento.

## Logiche comuni di ambito
1. Identificare sottoarea.
2. Selezionare agente principale.
3. Selezionare supporti minimi.
4. Caricare dataset operativo.
5. Produrre risultato verificabile.

## Schemi comuni di ambito
| Campo | Uso |
|---|---|
| richiesta | input utente |
| sottoarea | contesto raffinato |
| agente_principale | responsabile |
| supporti | agenti secondari |
| dataset | fonti interne |
| output | formato finale |

## Output tipici
- analisi strutturata;
- tabella decisionale;
- report breve;
- patch MD_OS;
- checklist operativa.

## Regole di selezione agenti
Usare `TASSONOMIA/albero_ambiti.yaml` e i frontmatter degli agenti.

## Metriche di efficacia
- pochi agenti caricati;
- risposta precisa;
- output riutilizzabile;
- limiti dichiarati.
