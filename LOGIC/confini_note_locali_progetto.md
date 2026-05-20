# Confini delle note locali di progetto

Questo modulo definisce quando un file `.md` può stare dentro una cartella di progetto esterna al repository MD_OS.

## Principio

MD_OS contiene il metodo generale.

Le cartelle progetto contengono dati reali e, solo se necessario, note locali utili a interpretare quei dati.

Una nota locale di progetto non deve sostituire, duplicare o ridefinire il framework MD_OS.

## Cosa può contenere una nota locale

Una nota locale può indicare:

- cosa contiene la cartella;
- quali documenti sono presenti;
- quale periodo coprono i documenti;
- quali file sono prioritari;
- quali elementi cercare nei documenti della cartella;
- collegamenti fattuali ad altre cartelle del progetto;
- limiti, avvertenze o contesto specifico del progetto.

## Cosa non deve contenere una nota locale

Una nota locale non deve indicare:

- quali agenti MD_OS usare;
- quali procedure generali caricare;
- quale routing applicare;
- quali schemi del framework riscrivere;
- istruzioni generali valide per tutti i progetti;
- logiche che dovrebbero stare in MD_OS;
- dati sensibili non necessari alla lettura della cartella.

## Regola decisionale

Se il contenuto serve in più progetti, deve stare in MD_OS.

Se il contenuto serve solo a interpretare una cartella specifica del progetto, può stare in una nota locale.

Se il contenuto è una fonte reale, deve restare come documento del progetto.

## Nome consigliato

Per coerenza, le note locali devono chiamarsi:

```text
_note.md
```

Il prefisso `_` aiuta a distinguerle dai documenti reali e a renderle visibili in alto nella cartella.

## Struttura consigliata

```md
# Note locali cartella

## Contenuto
Descrizione sintetica della cartella.

## Cosa cercare
- Elemento 1
- Elemento 2
- Elemento 3

## Periodo coperto
Periodo o anni dei documenti presenti.

## Collegamenti utili
Riferimenti fattuali ad altre cartelle o documenti del progetto.

## Avvertenze locali
Elementi da leggere con prudenza.

## Limiti
Dati mancanti, ambigui o non ancora verificati.
```

## Regola finale

Le note locali guidano la lettura dei dati del progetto.

Non governano il framework.
