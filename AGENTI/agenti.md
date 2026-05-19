# agenti.md

Questo file contiene l'elenco degli agenti e il loro modo di essere assimilati.

## Definizione

Un agente è una capacità operativa specializzata.

Non è per forza un agente reale autonomo.  
Viene adattato dall'AI che richiama il framework.

## Compatibilità

| Framework | ChatGPT | Claude AI | Gemini AI |
|---|---|---|---|
| agente | ruolo operativo / GPT personalizzato | skill / procedura | Gem / helper |

## Schema agente

```yaml
agente:
  nome: ""
  versione: "1.0"
  stato: "attivo"
  descrizione: ""
  scopo: ""
  compatibilita:
    chatgpt: ""
    claude: ""
    gemini: ""
  attivazione:
    quando_usarlo: []
    quando_non_usarlo: []
  input:
    accettati: []
    richiesti: []
  output:
    prodotti: []
    formato_preferito: ""
  ambiti:
    principali: []
    secondari: []
    intersezioni: []
  funzioni:
    usate: []
  schemi:
    usati: []
  regole:
    operative: []
    sicurezza: []
    qualita: []
  limiti: []
  passaggi:
    prima: []
    dopo: []
```

## Agenti disponibili

- `orchestratore` — Coordina moduli, agenti, ambiti e funzioni.
- `analista` — Analizza richieste, dati e contesti.
- `ricercatore` — Cerca, verifica e organizza informazioni.
- `costruttore` — Crea file, strutture, codice e template.
- `revisore` — Controlla qualità, coerenza e completezza.
- `specialista-output` — Sceglie e adatta il formato di risposta.
- `traduttore-compatibilita` — Traduce concetti tra ChatGPT, Claude e Gemini.
- `architetto-framework` — Progetta architetture modulari e repository.
- `analista-lavoro` — Analizza contratti, buste paga e dati lavorativi.
- `analista-finanziario` — Analizza numeri, costi, entrate e uscite.
- `analista-salute` — Gestisce contesto salute in modo prudente e non diagnostico.
- `sviluppatore-web` — Produce codice web e componenti frontend.
- `designer-ux-ui` — Valuta interfacce, esperienza utente e layout.
- `redattore-documentale` — Scrive documentazione, istruzioni e testi strutturati.
- `cuoco-strategico` — Crea ricette, menù, spesa e organizzazione cucina.
- `gestore-memoria` — Propone patch, aggiornamenti e continuità del framework.

## Regola di attivazione

Per task semplici usare un solo agente.  
Per task complessi usare una catena agenti.

Esempio:

```yaml
catena:
  - orchestratore
  - analista
  - costruttore
  - revisore
  - specialista-output
```
