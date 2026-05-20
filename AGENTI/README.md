# Modulo AGENTI

Il modulo AGENTI contiene la definizione operativa degli agenti del framework MD_OS.

Gli agenti non sono semplici descrizioni di ruolo. Ogni agente deve indicare:

- scopo operativo;
- ambito di competenza;
- condizioni di attivazione;
- input richiesti;
- funzioni abilitate;
- procedure da applicare;
- formule da richiamare;
- schemi dati/output da usare;
- soglie e criteri di anomalia;
- limiti e regole di prudenza;
- collaborazioni con altri agenti.

## Regola strutturale

Gli agenti singoli devono essere organizzati per ambito dentro:

```txt
AGENTI/AGENTI SINGOLI/<AMBITO>/<nome-agente>.md
```

Esempio:

```txt
AGENTI/AGENTI SINGOLI/ECONOMIA_FINANZA_REVISIONE/analista-finanziario.md
```

Nessun agente singolo dovrebbe restare sciolto direttamente dentro `AGENTI/AGENTI SINGOLI/`, salvo file di servizio come `_README.md` o `_TEMPLATE.md`.

## Separazione delle responsabilità

Il file agente definisce chi lavora, quando lavora e quali moduli deve caricare.

Le competenze operative riutilizzabili devono stare in moduli separati:

```txt
FUNZIONI/   = azioni operative richiamabili
PROCEDURE/ = sequenze professionali di lavoro
FORMULE/   = calcoli, indici, formule matematiche
SCHEMI/    = strutture dati e formati output
SOGLIE/    = criteri di valutazione, rischio e anomalia
```

## Regola anti-duplicazione

Un agente non deve duplicare formule, procedure o soglie già presenti nei moduli dedicati.

Deve invece richiamarle esplicitamente nella sezione `Moduli collegati`.

## Regola di prudenza

Ogni agente deve distinguere tra:

- dati certi;
- dati calcolati;
- inferenze;
- ipotesi;
- dati mancanti;
- verifiche consigliate.

Gli agenti non devono inventare dati mancanti e non devono sostituirsi a professionisti abilitati quando la materia richiede validazione professionale esterna.
