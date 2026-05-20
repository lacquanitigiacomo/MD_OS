# Procedura estrazione dati documentali

Questa procedura definisce come estrarre dati da documenti, immagini, tabelle e fonti testuali.

È applicabile a qualsiasi progetto documentale.

## Obiettivo

Produrre dati grezzi strutturati, tracciabili e riutilizzabili dai reparti specialistici.

## Prerequisito

Prima di estrarre dati, deve esistere almeno un inventario fonti.

Usare:

```text
PROCEDURE/procedura_inventario_fonti.md
```

## Sequenza operativa

1. Identificare la fonte da leggere.
2. Verificare tipo file e qualità apparente.
3. Dichiarare se la fonte è letta integralmente o parzialmente.
4. Estrarre i campi visibili.
5. Separare testo, numeri, date, importi e note.
6. Mantenere il collegamento alla fonte.
7. Non correggere valori incerti per intuizione.
8. Marcare ogni campo con qualità estrazione.
9. Segnalare campi mancanti o illeggibili.
10. Produrre output secondo `SCHEMI/schema_output_estrazione_dati.md`.
11. Inviare a revisione estrazione se i dati sono complessi o critici.

## Tipi di dato

Classificare i dati estratti come:

```text
TESTO
NUMERO
IMPORTO
DATA
PERIODO
CODICE
TABELLA
IMMAGINE
CAMPO_MANCANTE
CAMPO_ILLEGIBILE
CAMPO_AMBIGUO
```

## Stati campo

```text
ESTRATTO
PARZIALE
ILLEGIBILE
MANCANTE
AMBIGUO
DA_VERIFICARE
```

## Regole di qualità

Usare:

```text
SOGLIE/soglie_qualita_estrazione.md
```

## Output minimo

Ogni estrazione deve produrre:

- ID estrazione;
- fonte;
- percorso fonte;
- tipo fonte;
- campo;
- valore estratto;
- tipo dato;
- stato campo;
- qualità estrazione;
- note tecniche.

## Regola finale

L'estrazione dati non è analisi.

L'analisi inizia solo dopo che i dati sono stati estratti, revisionati e consegnati ai reparti competenti.
