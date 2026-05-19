# funzioni.md

Questo file registra le funzioni operative del framework.

## Regola

Ogni funzione può essere:

- `reale`: disponibile tramite strumenti dell'ambiente;
- `emulata`: applicata come procedura istruttiva;
- `non disponibile`: impossibile nell'ambiente corrente.

## Catalogo funzioni

```yaml
funzioni:
  avvio:
    - rileva_ambiente
    - ricostruisci_struttura
    - controlla_aggiornamenti
    - carica_moduli_base
  routing:
    - analizza_richiesta
    - classifica_complessita
    - seleziona_ambito
    - seleziona_agente
    - seleziona_schema
    - seleziona_output
  agenti:
    - attiva_agente
    - crea_catena_agenti
    - passa_contesto
    - raccogli_output_agenti
  ambiti:
    - identifica_ambito_principale
    - identifica_ambiti_secondari
    - calcola_intersezione_ambiti
  output:
    - formatta_risposta
    - genera_dossier
    - genera_report
    - genera_json
    - genera_codice_web
  controllo:
    - controlla_coerenza
    - verifica_completezza
    - rileva_ridondanze
    - segnala_limiti
  memoria:
    - crea_patch
    - genera_changelog
    - proponi_aggiornamento_framework
```
