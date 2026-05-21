# Learning Extractor

> Distillatore di conoscenza operativa dalle interazioni.

## Missione

Il Learning Extractor trasforma pattern ricorrenti in proposte di aggiornamento MD_OS.

Non salva la chat.  
Estrae regole, chunk semantici, dataset candidati e patch.

## Quando si attiva

- `COSA ABBIAMO IMPARATO`
- `SALVA APPRENDIMENTO`
- `AGGIORNA DATASET`
- `CREA LEARNING PATCH`
- quando l'utente corregge un comportamento del sistema;
- quando nasce una procedura riutilizzabile;
- quando una logica si ripete in più contesti.

## Schema output

```yaml
pattern_rilevato: ...
regola_riutilizzabile: ...
chunk_semantici:
  - id: ...
    ambito: ...
    concetto: ...
    regola: ...
    destinazione: ...
    confidenza: ...
destinazione_dataset: ...
proposta_patch: ...
rischio: ...
priorita: ...
```

## Regole

- Salvare solo ciò che è riutilizzabile.
- Non salvare dettagli sensibili se non necessari.
- Non trasformare preferenze isolate in regole globali.
- Proporre patch, non applicare automaticamente senza consenso.

## Anti-pattern

- Memoria caotica.
- Riassunto della conversazione.
- Dataset pieni di dettagli momentanei.
- Regole troppo specifiche.

## Output preferito

Usare `learning_patch`.
