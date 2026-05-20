# MD_OS - Framework AI Modulare

MD_OS è un framework operativo basato su file Markdown. I file non sono semplice documentazione: definiscono istruzioni, agenti, funzioni, procedure, formule, schemi, soglie, logiche di routing e formati di output.

## Separazione centrale

- GitHub contiene il framework: regole, agenti, procedure, formule, funzioni, schemi, soglie e output.
- Google Drive contiene i materiali dei progetti: PDF, documenti, immagini, fogli, dataset, dossier e cartelle operative.

## Struttura principale

```txt
README.md
BOOT.md
AGENTI/
FUNZIONI/
PROCEDURE/
FORMULE/
SCHEMI/
SOGLIE/
LOGIC/
OUTPUT/
ROUTING/
SICUREZZA/
PROGETTI/
TEMPLATE/
```

## Regola operativa

Un agente definisce chi lavora, quando lavora, quali moduli carica e quale output produce.
Le competenze riutilizzabili non devono essere duplicate dentro gli agenti: vanno nei moduli dedicati.

```txt
AGENTI   = profili operativi specialistici
FUNZIONI = azioni richiamabili
PROCEDURE = sequenze di lavoro
FORMULE = calcoli e indici
SCHEMI = strutture dati e report
SOGLIE = criteri di rischio e anomalia
OUTPUT = formati finali
LOGIC = regole generali e orchestrazione
ROUTING = criteri di attivazione
SICUREZZA = privacy, limiti, prudenza
```
