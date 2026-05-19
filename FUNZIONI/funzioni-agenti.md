# funzioni-agenti.md

```yaml
funzioni:
  attiva_agente:
    tipo: "emulata"
    scopo: "Applicare un agente come ruolo operativo."
    input:
      - "nome agente"
      - "task"
      - "ambito"
    output:
      - "risultato agente"

  crea_catena_agenti:
    tipo: "emulata"
    scopo: "Organizzare più agenti in sequenza."
    esempio:
      - "orchestratore"
      - "analista"
      - "costruttore"
      - "revisore"

  passa_contesto:
    tipo: "emulata"
    scopo: "Passare informazioni essenziali tra agenti."
    regole:
      - "non passare rumore"
      - "mantenere solo dati utili"
      - "dichiarare limiti"

  raccogli_output_agenti:
    tipo: "emulata"
    scopo: "Unire risultati parziali in output coerente."
```
