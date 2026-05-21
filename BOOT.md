# BOOT MD_OS

## Agente 0% — base operativa
All'avvio MD_OS non assume competenze specialistiche. Attiva solo regole comuni:
- capire la richiesta;
- distinguere dato, inferenza, ipotesi e limite;
- usare dataset interni prima di cercare altrove;
- ridurre domande inutili;
- scegliere macro-area, sottoarea e agenti minimi necessari;
- produrre output riutilizzabile;
- proporre patch se emerge una logica migliorativa.

## Sequenza di avvio
1. Leggere `README.md`.
2. Leggere `AGENTI/README-AGENTI.md`.
3. Caricare `DATASET/BASE/contesto_base.md`.
4. Leggere `AGENTI/TASSONOMIA/albero_ambiti.yaml`.
5. Identificare macro-area, sottoarea, modalità trasversale e trigger.
6. Leggere solo gli ambiti pertinenti in `AGENTI/AMBITI/`.
7. Eseguire discovery in `AGENTI/AGENTI-SINGOLI/`.
8. Caricare agente principale e massimo 2-4 supporti, salvo task complesso.
9. Caricare dataset collegati dichiarati da ambito e agenti.
10. Generare risultato, patch o aggiornamento.

## Caricamento progressivo
- 0%: boot + contesto base.
- 30%: tassonomia + ambito.
- 60%: agente principale.
- 80%: agenti supporto + dataset.
- 100%: fonti progetto + output strutturato.

## Modalità trasversali
Se la richiesta riguarda sviluppo di idee, prototipi, MVP o prodotto, attivare `SVILUPPO_IDEE_RAPIDO` e comporre agenti da IMPRESA_MANAGEMENT, DATI_RICERCA, TECNOLOGIA_SVILUPPO, DESIGN_COMUNICAZIONE e DOCUMENTI_DATI_REPORT.
