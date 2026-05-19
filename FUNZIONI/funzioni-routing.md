# funzioni-routing.md

```yaml
funzioni:
  analizza_richiesta:
    input: "messaggio utente"
    output:
      obiettivo: ""
      vincoli: []
      dati_mancanti: []
      tipo_task: ""

  classifica_complessita:
    criteri:
      bassa: "risposta semplice"
      media: "più passaggi o analisi"
      alta: "file, repository, più moduli, dati complessi"

  seleziona_ambito:
    input: "richiesta analizzata"
    output:
      principale: ""
      secondari: []
      motivo: ""

  seleziona_agente:
    input:
      - "ambito"
      - "complessità"
      - "tipo task"
    output:
      agenti: []

  seleziona_schema:
    input:
      - "tipo dati"
      - "output richiesto"
    output:
      schemi: []

  seleziona_output:
    regole:
      stringato: "veloce e diretto"
      report: "analisi media"
      dossier: "analisi completa"
      codice-web: "HTML/CSS/JS"
      json: "dati strutturati"
```
