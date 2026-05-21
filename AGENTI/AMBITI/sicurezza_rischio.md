---
id_ambito: SICUREZZA_RISCHIO
nome: Sicurezza Rischio
descrizione_breve: Ambito operativo sicurezza rischio.
trigger: ['risk_management', 'audit', 'data_protection', 'continuita_operativa', 'emergenze']
tag: ['risk_management', 'audit', 'data_protection', 'continuita_operativa', 'emergenze']
cartella_agenti: AGENTI/AGENTI-SINGOLI/SICUREZZA_RISCHIO/
dataset_collegati:
  - DATASET/SICUREZZA_RISCHIO/dataset_operativo.md
stato: attivo
versione: 1.0.0
---
# Ambito — Sicurezza Rischio

## 1. Identità ambito
Ambito dedicato a sicurezza rischio.

## 2. Scopo
Orientare discovery, selezione agenti, dataset e output per le sottoaree collegate.

## 3. Perimetro operativo
Sottoaree: risk_management, audit, data_protection, continuita_operativa, emergenze.

## 4. Quando attivarlo
Quando la richiesta contiene trigger o tag collegati alle sottoaree dell'ambito.

## 5. Quando non attivarlo
Quando la richiesta è chiaramente coperta da altra macro-area.

## 6. Trigger principali
- risk_management
- audit
- data_protection
- continuita_operativa
- emergenze

## 7. Agenti preferiti
La selezione avviene tramite `TASSONOMIA/albero_ambiti.yaml`.

## 8. Funzioni comuni di ambito
- classificare richiesta;
- scegliere sottoarea;
- selezionare agente principale;
- caricare dataset operativo;
- produrre output standard;
- proporre patch.

## 9. Logiche comuni di ambito
1. Riconoscere trigger.
2. Isolare obiettivo.
3. Identificare output richiesto.
4. Caricare agente minimo sufficiente.
5. Validare risultato con checklist.

## 10. Output tipici
- analisi;
- checklist;
- tabella;
- piano operativo;
- patch MD_OS;
- report.

## 11. Metriche di efficacia
- riduzione domande inutili;
- output riutilizzabile;
- agenti corretti selezionati;
- dataset pertinente caricato.
