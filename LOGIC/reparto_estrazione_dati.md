# Reparto logico ESTRAZIONE_DATI

Questo modulo definisce il reparto logico dedicato all'estrazione dei dati da fonti documentali.

## Principio

ESTRAZIONE_DATI produce dati strutturati.

Non interpreta, non valuta responsabilità, non formula conclusioni e non scrive report finali.

Il suo compito è recuperare informazioni da fonti anche difficili da leggere e consegnarle agli altri reparti in forma tracciabile.

## Cosa fa

Il reparto ESTRAZIONE_DATI può:

- leggere documenti;
- estrarre testo;
- estrarre tabelle;
- trascrivere campi;
- normalizzare valori;
- rilevare dati mancanti;
- segnalare ambiguità;
- indicare qualità dell'estrazione;
- mantenere collegamento alla fonte;
- preparare dati per i reparti specialistici.

## Cosa non fa

Il reparto ESTRAZIONE_DATI non deve:

- interpretare legalmente;
- valutare responsabilità;
- diagnosticare;
- decidere anomalie;
- formulare accuse;
- stimare danni;
- scrivere conclusioni;
- aumentare la confidenza dei dati;
- correggere dati dubbi per intuizione.

## Pipeline

```text
INVENTARIO FONTI
→ ESTRAZIONE_DATI
→ REVISIONE_ESTRAZIONE
→ REPARTI SPECIALISTICI
→ COMUNICAZIONE_OUTPUT
```

## Agenti collegati

- `AGENTI/AGENTI SINGOLI/ESTRAZIONE_DATI/estrattore-documentale.md`
- `AGENTI/AGENTI SINGOLI/ESTRAZIONE_DATI/revisore-estrazione.md`

## Moduli collegati

- `ROUTING/routing_estrazione_dati.md`
- `PROCEDURE/procedura_estrazione_dati_documentali.md`
- `SCHEMI/schema_output_estrazione_dati.md`
- `SOGLIE/soglie_qualita_estrazione.md`

## Regola finale

Ogni dato estratto deve mantenere almeno:

- fonte;
- percorso o riferimento;
- campo;
- valore;
- qualità estrazione;
- stato;
- note tecniche.
