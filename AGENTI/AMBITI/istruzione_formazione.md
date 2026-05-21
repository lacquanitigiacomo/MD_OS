---
id_ambito: ISTRUZIONE_FORMAZIONE
nome: Istruzione Formazione
stato: attivo
versione: 1.0.0
cartella_agenti: AGENTI/AGENTI-SINGOLI/ISTRUZIONE_FORMAZIONE/
trigger: ['didattica', 'tutoring', 'valutazione', 'progettazione_corsi', 'metodo_studio']
tag: ['didattica', 'tutoring', 'valutazione', 'progettazione_corsi', 'metodo_studio']
dataset_collegati:
  - DATASET/ISTRUZIONE_FORMAZIONE/dataset_operativo.md
---

# Ambito — Istruzione Formazione

## Identità ambito
Macro-area operativa per istruzione formazione.

## Sottoaree
- didattica
- tutoring
- valutazione
- progettazione_corsi
- metodo_studio

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
