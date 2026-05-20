# Schema rilievo documentale

Questo schema definisce il formato standard per registrare un fatto, un dato o un'anomalia ricavati da una fonte documentale.

È applicabile a qualsiasi progetto basato su documenti, immagini, tabelle, comunicazioni o file strutturati.

## Obiettivo

Ogni rilievo deve essere tracciabile, verificabile e separato dalle interpretazioni.

## Campi minimi

| Campo | Descrizione |
|---|---|
| ID rilievo | Identificativo progressivo |
| Fatto rilevato | Descrizione sintetica del fatto o dato |
| Fonte | Nome del file o documento da cui deriva |
| Percorso fonte | Posizione della fonte nel progetto |
| Tipo fonte | PDF, documento, immagine, foglio, comunicazione, tabella, altro |
| Data fonte | Data del documento, se disponibile |
| Periodo riferito | Periodo a cui il rilievo si riferisce |
| Categoria | Area tematica del rilievo |
| Dato estratto | Valore, testo o elemento osservato |
| Interpretazione | Lettura prudente del dato |
| Impatto possibile | Effetto potenziale sull'analisi |
| Confidenza | Alta, media, bassa, nulla |
| Stato | Da verificare, validato, scartato, duplicato, mancante |
| Collegamenti | Altri rilievi o fonti collegate |
| Note | Limiti, dubbi, condizioni di lettura |

## Separazione obbligatoria

Un rilievo deve distinguere sempre tra:

- dato osservato;
- interpretazione;
- ipotesi;
- conclusione;
- verifica richiesta.

## Stati ammessi

```text
DA_VERIFICARE
VALIDATO
SCARTATO
DUPLICATO
MANCANTE
INCOMPLETO
```

## Livelli di confidenza

Usare il modulo:

```text
SOGLIE/livelli_confidenza_fonti.md
```

## Template tabellare

```markdown
| ID | Fatto rilevato | Fonte | Percorso | Tipo fonte | Data fonte | Periodo | Categoria | Dato estratto | Interpretazione | Impatto possibile | Confidenza | Stato | Collegamenti | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

## Regola di prudenza

Non trasformare un rilievo in una conclusione generale se manca una fonte diretta o un incrocio documentale sufficiente.
