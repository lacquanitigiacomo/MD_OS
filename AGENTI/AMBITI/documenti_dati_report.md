---
id_ambito: DOCUMENTI_DATI_REPORT
nome: Documenti Dati Report
descrizione_breve: Ambito operativo documenti dati report.
trigger: ['estrazione_dati', 'reportistica', 'revisione_documentale', 'normalizzazione', 'dossier']
tag: ['estrazione_dati', 'reportistica', 'revisione_documentale', 'normalizzazione', 'dossier']
cartella_agenti: AGENTI/AGENTI-SINGOLI/DOCUMENTI_DATI_REPORT/
dataset_collegati:
  - DATASET/DOCUMENTI_DATI_REPORT/dataset_operativo.md
stato: attivo
versione: 1.0.0
---
# Ambito — Documenti Dati Report

## 1. Identità ambito
Ambito dedicato a documenti dati report.

## 2. Scopo
Orientare discovery, selezione agenti, dataset e output per le sottoaree collegate.

## 3. Perimetro operativo
Sottoaree: estrazione_dati, reportistica, revisione_documentale, normalizzazione, dossier.

## 4. Quando attivarlo
Quando la richiesta contiene trigger o tag collegati alle sottoaree dell'ambito.

## 5. Quando non attivarlo
Quando la richiesta è chiaramente coperta da altra macro-area.

## 6. Trigger principali
- estrazione_dati
- reportistica
- revisione_documentale
- normalizzazione
- dossier

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
