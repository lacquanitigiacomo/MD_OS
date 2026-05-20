# Schema output estrazione dati

Questo schema definisce il formato standard per i dati prodotti dal reparto ESTRAZIONE_DATI.

## Obiettivo

Rendere ogni dato estratto tracciabile, controllabile e riutilizzabile.

## Campi minimi

| Campo | Descrizione |
|---|---|
| ID estrazione | Identificativo progressivo |
| Fonte | Nome file o documento |
| Percorso fonte | Posizione della fonte nel progetto |
| Tipo fonte | PDF, immagine, scansione, documento, tabella, foglio, altro |
| Pagina/sezione | Pagina, sezione o area da cui deriva il dato |
| Campo | Nome del campo estratto |
| Valore estratto | Valore testuale, numerico o descrittivo |
| Tipo dato | Testo, numero, importo, data, periodo, codice, tabella, altro |
| Stato campo | Estratto, parziale, illeggibile, mancante, ambiguo, da verificare |
| Qualità estrazione | Alta, media, bassa, nulla |
| Metodo lettura | Lettura diretta, OCR, visione, tabella, trascrizione manuale, altro |
| Note tecniche | Limiti, dubbi, condizioni di lettura |
| Destinazione | Reparto o procedura che userà il dato |

## Template tabellare

```markdown
| ID | Fonte | Percorso | Tipo fonte | Pagina/sezione | Campo | Valore | Tipo dato | Stato | Qualità | Metodo | Note | Destinazione |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

## Regole

- Un campo dubbio deve restare dubbio.
- Un campo illeggibile deve essere marcato come illeggibile.
- Un valore mancante non deve essere inventato.
- Un dato estratto non deve contenere interpretazioni specialistiche.
- Ogni valore deve mantenere riferimento alla fonte.

## Esempio astratto

```markdown
| E001 | documento.pdf | /cartella/documento.pdf | PDF | pag. 2 | Data documento | 2026-01-15 | DATA | ESTRATTO | ALTA | lettura diretta | nessuna | analisi documentale |
```
