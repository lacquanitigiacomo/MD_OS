# Logica di ingresso contenuti in MD_OS

Questo modulo definisce quando una nuova informazione può entrare nel repository MD_OS.

## Principio

MD_OS accetta solo contenuti generalizzabili.

Una informazione può essere inserita in MD_OS solo se migliora il framework in modo riutilizzabile, senza dipendere da un progetto, cliente, cartella, documento o caso specifico.

## Criterio decisionale

Prima di aggiungere o modificare un file MD_OS, verificare:

1. Il contenuto descrive una capacità generale?
2. Può essere riutilizzato in più progetti?
3. È privo di nomi progetto, nomi cliente, percorsi, file, documenti o riferimenti esterni specifici?
4. È stato depersonalizzato e astratto?
5. Esiste un modulo MD_OS corretto dove inserirlo?

Se una risposta è negativa, il contenuto non deve entrare in MD_OS.

## Routing

- Regole di confine, privacy e separazione: `SICUREZZA/`
- Criteri decisionali e orchestrazione: `LOGIC/`
- Azioni richiamabili: `FUNZIONI/`
- Sequenze operative: `PROCEDURE/`
- Profili operativi: `AGENTI/`
- Formati finali: `OUTPUT/`
- Schemi dati o report: `SCHEMI/`
- Calcoli e indici: `FORMULE/`
- Soglie e anomalie: `SOGLIE/`
- Criteri di attivazione: `ROUTING/`

## Riferimento vincolante

Per la separazione tra framework e progetti esterni, applicare sempre:

`SICUREZZA/confini_framework_progetti.md`
