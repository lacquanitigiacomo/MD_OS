# Framework AI Modulare

Questo repository contiene un framework composto principalmente da file `.md`.

I file Markdown non sono semplice documentazione: sono istruzioni operative che un servizio AI può leggere, assimilare e usare per configurare il proprio comportamento durante una sessione.

Il framework serve a fornire:

- struttura di avvio;
- logica operativa;
- agenti specializzati;
- ambiti di riferimento;
- funzioni operative;
- schemi dati;
- formati di output;
- regole di routing;
- compatibilità tra ChatGPT, Claude AI e Gemini AI.

## Compatibilità

Il framework deve adattarsi all'ambiente che lo richiama.

| Concetto framework | ChatGPT | Claude AI | Gemini AI |
|---|---|---|---|
| agente | ruolo operativo / Custom GPT se configurato | skill / procedura / istruzione progetto | Gem / helper / istruzione personalizzata |
| funzione | procedura emulata / action se disponibile | skill o procedura se disponibile | tool, estensione o procedura |
| ambito | contesto operativo | contesto skill/progetto | contesto Gem/Workspace |
| schema | formato dati/risposta | struttura output/artifact | formato risposta/dati |
| output | risposta o file | risposta/artifact | risposta/file |

Il framework non deve fingere capacità reali se l'ambiente non le supporta.

## Struttura

```text
/
├── README.md
├── boot.md
├── LOGICA/
│   └── logica.md
├── AGENTI/
│   ├── agenti.md
│   ├── ambiti.md
│   ├── AGENTI SINGOLI/
│   └── AMBITI/
├── SCHEMI/
├── OUTPUT/
└── FUNZIONI/
```

## Avvio

Il servizio AI deve caricare:

```text
boot.md
```
