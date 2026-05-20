# Livelli di confidenza delle fonti

Questo modulo definisce soglie standard per valutare l'affidabilità di dati, rilievi e interpretazioni basati su fonti documentali.

È applicabile a qualsiasi progetto.

## Scopo

Evitare che dati deboli, incompleti o inferiti vengano presentati come certi.

## Livelli

| Livello | Definizione |
|---|---|
| ALTA | Fonte diretta, leggibile, coerente e sufficiente rispetto al dato rilevato |
| MEDIA | Fonte presente, ma da interpretare, integrare o incrociare |
| BASSA | Indizio utile, ma non sufficiente per una conclusione |
| NULLA | Dato assente, illeggibile, non verificabile o non supportato |

## Criteri ALTA

Usare `ALTA` solo quando:

- la fonte è stata effettivamente letta;
- il dato è visibile o estratto direttamente;
- il documento è coerente con il periodo analizzato;
- non emergono contraddizioni rilevanti;
- il dato basta a sostenere il rilievo.

## Criteri MEDIA

Usare `MEDIA` quando:

- la fonte esiste ma richiede interpretazione;
- il dato è parziale;
- serve un confronto con altre fonti;
- il documento è chiaro ma non completamente sufficiente;
- il periodo è probabile ma non certo.

## Criteri BASSA

Usare `BASSA` quando:

- il dato è solo un indizio;
- la fonte è indiretta;
- mancano conferme;
- il contenuto è ambiguo;
- il documento non basta a sostenere una conclusione.

## Criteri NULLA

Usare `NULLA` quando:

- la fonte manca;
- il file non è accessibile;
- il dato non è presente;
- il contenuto è illeggibile;
- il rilievo non può essere verificato.

## Regola di escalation

Un rilievo può salire di confidenza solo se viene supportato da:

- fonte diretta più chiara;
- seconda fonte coerente;
- dato strutturato verificabile;
- conferma documentale indipendente.

## Regola di prudenza

Quando la confidenza è `MEDIA`, `BASSA` o `NULLA`, usare formule prudenti:

```text
il dato suggerisce
la fonte indica parzialmente
il punto richiede verifica
non risultano elementi sufficienti
la ricostruzione è incompleta
```

Evitare formule definitive:

```text
è certo
è dimostrato
prova definitiva
violazione automatica
errore sicuro
```

## Output consigliato

Ogni analisi deve dichiarare il livello di confidenza dei rilievi principali.
