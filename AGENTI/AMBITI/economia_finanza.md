---
id_ambito: ECONOMIA_FINANZA
nome: Economia Finanza
descrizione_breve: Ambito operativo economia finanza.
trigger: ['contabilita', 'fiscalita', 'budget_controllo', 'business_plan', 'investimenti']
tag: ['contabilita', 'fiscalita', 'budget_controllo', 'business_plan', 'investimenti']
cartella_agenti: AGENTI/AGENTI-SINGOLI/ECONOMIA_FINANZA/
dataset_collegati:
  - DATASET/ECONOMIA_FINANZA/dataset_operativo.md
stato: attivo
versione: 1.0.0
---
# Ambito — Economia Finanza

## 1. Identità ambito
Ambito dedicato a economia finanza.

## 2. Scopo
Orientare discovery, selezione agenti, dataset e output per le sottoaree collegate.

## 3. Perimetro operativo
Sottoaree: contabilita, fiscalita, budget_controllo, business_plan, investimenti, revisione.

## 4. Quando attivarlo
Quando la richiesta contiene trigger o tag collegati alle sottoaree dell'ambito.

## 5. Quando non attivarlo
Quando la richiesta è chiaramente coperta da altra macro-area.

## 6. Trigger principali
- contabilita
- fiscalita
- budget_controllo
- business_plan
- investimenti
- revisione

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
