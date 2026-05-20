# Procedura inventario fonti

Questa procedura serve a ricostruire l'elenco ordinato delle fonti disponibili in un progetto.

È applicabile a qualsiasi progetto documentale.

## Obiettivo

Creare una mappa verificabile dei materiali disponibili, distinguendo sempre tra:

- file rilevati;
- file effettivamente letti;
- file non letti;
- file non accessibili;
- file duplicati;
- file ambigui;
- file mancanti ma necessari.

## Principi

Non dichiarare letto un file solo perché è stato trovato.

Non dedurre il contenuto di un file dal nome.

Non mescolare file simili senza indicare quale fonte è stata usata.

Non produrre conclusioni prima di avere classificato le fonti principali.

## Campi minimi inventario

| Campo | Descrizione |
|---|---|
| ID fonte | Identificativo progressivo |
| Nome file/cartella | Nome visibile della fonte |
| Percorso | Posizione nel progetto |
| Tipo | PDF, immagine, documento, foglio, cartella, archivio, altro |
| Categoria | Contratto, comunicazione, dato economico, salute, foto, nota, tabella, altro |
| Periodo coperto | Data, mese, anno o intervallo |
| Stato lettura | Rilevato, letto, parzialmente letto, non letto, non accessibile |
| Priorità | Alta, media, bassa |
| Uso previsto | A cosa serve nell'analisi |
| Criticità | Limiti, ambiguità, duplicati, qualità bassa |
| Note | Annotazioni operative |

## Stati ammessi

```text
RILEVATO
LETTO
PARZIALMENTE_LETTO
NON_LETTO
NON_ACCESSIBILE
DUPLICATO
AMBIGUO
MANCANTE
SCARTATO
```

## Priorità

```text
ALTA = fonte necessaria per rispondere al task
MEDIA = fonte utile per verifica o contesto
BASSA = fonte accessoria o da leggere solo se serve
```

## Sequenza operativa

1. Identificare la cartella o il perimetro del progetto.
2. Elencare gli elementi nella root.
3. Scendere nelle sottocartelle rilevanti.
4. Separare cartelle, file e note locali.
5. Classificare ogni fonte per tipo e categoria.
6. Segnare lo stato di lettura reale.
7. Evidenziare duplicati o file simili.
8. Identificare fonti mancanti rispetto al task.
9. Produrre una tabella inventario.
10. Prima dell'analisi, dichiarare quali fonti saranno lette.

## Output minimo

```markdown
# Inventario fonti

| ID | Nome | Percorso | Tipo | Categoria | Periodo | Stato lettura | Priorità | Uso previsto | Criticità | Note |
|---|---|---|---|---|---|---|---|---|---|---|
```

## Regola finale

L'inventario fonti è una fase preliminare.

Non sostituisce l'analisi dei contenuti.
