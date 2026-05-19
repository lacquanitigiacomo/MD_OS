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

## Architettura generale

Il framework risiede su GitHub.

GitHub contiene il sistema centrale, cioè:

- file di avvio;
- logica del framework;
- agenti;
- ambiti;
- funzioni;
- schemi;
- formati di output;
- regole comuni;
- compatibilità tra servizi AI.

I progetti operativi e i relativi materiali risiedono invece su Google Drive.

Google Drive contiene i dati reali dei progetti, per esempio:

- documenti;
- file di lavoro;
- PDF;
- immagini;
- fogli di calcolo;
- dossier;
- report;
- cartelle tematiche;
- materiali da analizzare o trasformare.

## Regola di separazione

Il framework su GitHub definisce **come l'AI deve lavorare**.

I progetti su Google Drive definiscono **su cosa l'AI deve lavorare**.

Il servizio AI deve quindi distinguere sempre tra:

- istruzioni generali del framework;
- istruzioni locali del progetto;
- file e dati del progetto;
- strumenti realmente disponibili nell'ambiente;
- funzioni emulate attraverso istruzioni.

## README locale dei progetti

Ogni progetto su Google Drive dovrebbe contenere un proprio `README.md`.

Il `README.md` locale del progetto funziona come manifesto operativo del progetto.

Deve indicare:

- nome del progetto;
- scopo del progetto;
- link al framework GitHub;
- cartelle principali del progetto;
- file importanti;
- ambiti da privilegiare;
- agenti consigliati;
- schemi da usare;
- output preferiti;
- regole specifiche del progetto;
- eventuali limiti o attenzioni.

Flusso consigliato:

```text
1. Il servizio AI entra nella cartella del progetto su Google Drive.
2. Legge il README.md locale del progetto.
3. Dal README.md locale recupera il link al framework GitHub.
4. Carica il file boot.md del framework.
5. Assimila logica, agenti, ambiti, funzioni, schemi e output.
6. Torna al progetto su Google Drive.
7. Ricostruisce cartelle, file e materiali disponibili.
8. Lavora usando framework centrale + istruzioni locali del progetto.
```

Esempio di comando utente:

```text
Entra nella cartella PROGETTI di Google Drive.
Trova ANALISI LAVORO.
Leggi il suo README.md.
Carica il framework GitHub indicato nel README.md.
Poi lavora sui file del progetto seguendo quelle istruzioni.
```

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

---

## Ultimo aggiornamento

- Data: 2026-05-19
- Autore: ChatGPT
- Nota: aggiunta architettura GitHub/Google Drive e ruolo del README locale dei progetti.
