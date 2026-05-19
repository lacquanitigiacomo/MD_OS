# funzioni-avvio.md

```yaml
funzioni:
  rileva_ambiente:
    tipo: "emulata"
    scopo: "Identificare ChatGPT, Claude AI, Gemini AI o altro."
    passaggi:
      - "leggi contesto"
      - "identifica segnali ambiente"
      - "applica profilo compatibilità"
    output: "nome ambiente"

  ricostruisci_struttura:
    tipo: "reale se accesso file disponibile, altrimenti emulata"
    scopo: "Mappare cartelle e file del repository."
    passaggi:
      - "elenca cartelle"
      - "elenca file"
      - "rileva moduli base"
      - "rileva moduli aggiuntivi"
    fallback:
      - "usa struttura dichiarata in README.md"

  controlla_aggiornamenti:
    tipo: "reale se accesso repository disponibile"
    scopo: "Verificare nuovi file o modifiche."
    passaggi:
      - "confronta mappa precedente e attuale"
      - "segnala nuovi file"
      - "segnala file mancanti"
    fallback:
      - "dichiara impossibilità di verifica"

  carica_moduli_base:
    tipo: "emulata o reale secondo accesso"
    scopo: "Assimilare file base."
    moduli:
      - "LOGICA/logica.md"
      - "FUNZIONI/funzioni.md"
      - "AGENTI/agenti.md"
      - "AGENTI/ambiti.md"
```
