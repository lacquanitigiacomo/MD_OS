# funzioni-memoria.md

```yaml
funzioni:
  crea_patch:
    scopo: "Preparare modifica da inserire nel framework."
    output:
      file: ""
      modifica: ""
      motivo: ""

  genera_changelog:
    scopo: "Elencare modifiche tra versioni."
    output:
      versione: ""
      modifiche: []

  proponi_aggiornamento_framework:
    scopo: "Suggerire nuovo agente, ambito, schema o funzione."
    regole:
      - "non salvare automaticamente se ambiente non supporta memoria"
      - "produrre testo copiabile"
```
