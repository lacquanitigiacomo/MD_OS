---
id_ambito: SCIENZE_NATURALI
nome: Scienze Naturali
descrizione_breve: Ambito operativo scienze naturali.
trigger: ['fisica', 'chimica', 'biologia', 'ambiente', 'geologia']
tag: ['fisica', 'chimica', 'biologia', 'ambiente', 'geologia']
cartella_agenti: AGENTI/AGENTI-SINGOLI/SCIENZE_NATURALI/
dataset_collegati:
  - DATASET/SCIENZE_NATURALI/dataset_operativo.md
stato: attivo
versione: 1.0.0
---
# Ambito — Scienze Naturali

## 1. Identità ambito
Ambito dedicato a scienze naturali.

## 2. Scopo
Orientare discovery, selezione agenti, dataset e output per le sottoaree collegate.

## 3. Perimetro operativo
Sottoaree: fisica, chimica, biologia, ambiente, geologia.

## 4. Quando attivarlo
Quando la richiesta contiene trigger o tag collegati alle sottoaree dell'ambito.

## 5. Quando non attivarlo
Quando la richiesta è chiaramente coperta da altra macro-area.

## 6. Trigger principali
- fisica
- chimica
- biologia
- ambiente
- geologia

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
