# Soglie qualità estrazione

Questo modulo definisce i livelli di qualità da assegnare ai dati estratti da fonti documentali.

## Scopo

Evitare che dati letti male, incompleti o ambigui vengano trattati come affidabili.

## Livelli

| Livello | Definizione |
|---|---|
| ALTA | Dato leggibile, diretto, completo e coerente nel punto fonte |
| MEDIA | Dato leggibile ma parziale, da controllare o dipendente dal layout |
| BASSA | Dato incerto, ambiguo, incompleto o ricavato da fonte difficile |
| NULLA | Dato assente, illeggibile o non estraibile |

## Qualità ALTA

Usare `ALTA` quando:

- il dato è chiaramente visibile;
- il campo è completo;
- non ci sono ambiguità di lettura;
- la fonte è leggibile;
- il valore non richiede ricostruzione.

## Qualità MEDIA

Usare `MEDIA` quando:

- il dato è leggibile ma il contesto è parziale;
- il layout può creare dubbi;
- serve una seconda verifica;
- il campo è presente ma non perfettamente chiaro;
- il dato è estratto da tabella complessa.

## Qualità BASSA

Usare `BASSA` quando:

- il dato è poco leggibile;
- il valore è incompleto;
- il layout è confuso;
- il dato deriva da immagine o scansione difficile;
- esistono più letture possibili.

## Qualità NULLA

Usare `NULLA` quando:

- il dato non è presente;
- il dato non è leggibile;
- il file non è accessibile;
- il campo non può essere estratto;
- il valore sarebbe solo inventato.

## Regola di conservazione

La qualità di estrazione non coincide con la verità del dato.

Un dato può essere estratto bene ma richiedere comunque verifica specialistica.

## Regola finale

I dati con qualità `BASSA` o `NULLA` non devono essere usati per conclusioni senza ulteriore verifica.
