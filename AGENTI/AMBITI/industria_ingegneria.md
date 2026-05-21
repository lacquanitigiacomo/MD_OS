---
id_ambito: INDUSTRIA_INGEGNERIA
nome: Industria Ingegneria
stato: attivo
versione: 1.0.0
cartella_agenti: AGENTI/AGENTI-SINGOLI/INDUSTRIA_INGEGNERIA/
trigger: ['meccanica', 'elettrica', 'edilizia', 'impianti', 'produzione']
tag: ['meccanica', 'elettrica', 'edilizia', 'impianti', 'produzione', 'qualita']
dataset_collegati:
  - DATASET/INDUSTRIA_INGEGNERIA/dataset_operativo.md
---

# Ambito — Industria Ingegneria

## Identità ambito
Macro-area operativa per industria ingegneria.

## Sottoaree
- meccanica
- elettrica
- edilizia
- impianti
- produzione
- qualita

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
