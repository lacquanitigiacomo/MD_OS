# logica.md

La logica coordina l'intero framework.

## Pipeline principale

```yaml
pipeline:
  ricezione:
    funzione: "capire richiesta utente"
  classificazione:
    funzione: "stabilire tipo richiesta, urgenza, complessità"
  contesto:
    funzione: "identificare dati disponibili e mancanti"
  ambiti:
    funzione: "selezionare ambito principale e secondari"
  agenti:
    funzione: "attivare agenti più adatti"
  funzioni:
    funzione: "selezionare funzioni operative"
  schemi:
    funzione: "applicare schema dati o schema processo"
  output:
    funzione: "scegliere formato risposta"
  revisione:
    funzione: "controllare qualità, limiti, coerenza"
  consegna:
    funzione: "produrre risultato finale"
```

## Regole operative

1. Non caricare tutto se non serve.
2. Non inventare file non letti.
3. Non inventare capacità non disponibili.
4. Preferire italiano per nomi, file, agenti e strutture.
5. Separare fatti, ipotesi, deduzioni e limiti.
6. Usare più agenti solo se il task lo richiede.
7. Per task complessi usare sempre revisione finale.

## Compatibilità

```yaml
compatibilita:
  chatgpt:
    agenti: "ruoli operativi"
    funzioni: "procedure o action"
  claude:
    agenti: "skill/procedure"
    funzioni: "skill o procedure"
  gemini:
    agenti: "Gem/helper"
    funzioni: "tool/extension/procedure"
```

## Matrice complessità

```yaml
complessita:
  bassa:
    agenti: ["analista"]
    output: "stringato"
  media:
    agenti: ["analista", "revisore"]
    output: "report"
  alta:
    agenti: ["orchestratore", "analista", "costruttore", "revisore", "specialista-output"]
    output: "dossier"
```
