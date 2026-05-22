# MD_OS Stable Core X10

Sistema locale eseguibile, data-first, in italiano, con agenti derivati da dataset, refactor X10, apprendimento incrementale, query interna, matrici e release check.

## Avvio

```bash
python mdos.py validate
python mdos.py status
python mdos.py query memoria retrieval agenti
python mdos.py refactor --goal "migliorare memoria, retrieval e agenti"
python mdos.py learn --text "Nuova decisione: i dataset sono la fonte primaria"
python mdos.py matrix
python mdos.py profile
python mdos.py release-check
python mdos.py beta --scenario memory_failure
```

## Reparto Tecnologia e Innovazione

Il reparto Tecnologia e Innovazione è il nucleo operativo incaricato di trasformare MD_OS in un sistema locale, verificabile e progressivamente migliorabile. Non agisce come semplice area tecnica: governa il ciclo completo che va dalla raccolta dei dati alla loro validazione, dall'esecuzione degli agenti alla misurazione dei risultati.

### Obiettivo costante

Il reparto persegue in modo continuo tre direttrici: **innovazione, efficienza e visione**.

- **Innovazione**: introdurre soluzioni, metodi e strumenti che aumentano le capacità reali di MD_OS senza compromettere stabilità e controllo.
- **Efficienza**: ridurre complessità, sprechi, passaggi manuali e ridondanze, migliorando velocità, chiarezza e affidabilità dei processi.
- **Visione**: mantenere una direzione evolutiva coerente, capace di collegare le scelte tecniche immediate agli obiettivi futuri del sistema.

Ogni aggiornamento tecnologico deve quindi rispondere a una domanda operativa precisa: aumenta l'innovazione, migliora l'efficienza o rafforza la visione di MD_OS?

### Missione

- Consolidare MD_OS come sistema data-first, dove dataset, log, matrici ed export sono la fonte primaria delle decisioni.
- Mantenere un'architettura stabile, evitando modifiche strutturali non necessarie e privilegiando evoluzioni tramite dati, plugin e procedure.
- Sviluppare funzioni di automazione, apprendimento incrementale, interrogazione interna e controllo qualità.
- Rendere ogni avanzamento tracciabile, ripetibile e verificabile prima di essere promosso a componente stabile.

### Ambiti operativi

1. **Core locale**: manutenzione del runtime Python, dei comandi CLI e delle funzioni essenziali di avvio, validazione, stato e diagnostica.
2. **Dataset e memoria**: gestione delle fonti dati, conteggio righe, validazione dei dataset, apprendimento incrementale e recupero delle informazioni.
3. **Agenti**: definizione, lettura e miglioramento degli agenti derivati dai dataset, con attenzione a ruolo, contesto, istruzioni e output atteso.
4. **Retrieval e query interna**: potenziamento delle ricerche locali, del ranking dei risultati e della consultazione semantica dei contenuti disponibili.
5. **Refactor X10**: applicazione della regola secondo cui ogni ciclo di refactor deve produrre almeno 10 avanzamenti concreti, documentabili e utili.
6. **Matrici e profili**: esportazione di matrici operative, valutazione della readiness e misurazione dello stato complessivo del sistema.
7. **Release e beta test**: controllo dei blocker, verifica del rilascio, simulazione di scenari critici e validazione prima della stabilizzazione.

### Principi tecnici

- **Stabilità prima dell'espansione**: ogni nuova funzione deve rafforzare il sistema, non aumentare confusione o fragilità.
- **Dati prima delle opinioni**: le decisioni operative devono essere fondate su dataset, risultati di validazione, log e matrici.
- **Esecuzione locale**: il sistema deve poter funzionare in locale, con dipendenze ridotte e comportamento prevedibile.
- **Tracciabilità**: ogni modifica deve avere uno scopo chiaro, un impatto verificabile e una collocazione coerente.
- **Incrementalità**: gli aggiornamenti devono essere piccoli, controllabili e cumulativi.

### Output attesi

Il reparto produce e mantiene:

- comandi CLI funzionanti;
- dataset validati;
- agenti interrogabili;
- procedure di refactor;
- matrici operative;
- profili di readiness;
- controlli di release;
- scenari beta;
- documentazione tecnica essenziale.

### Criteri di qualità

Un aggiornamento tecnologico è accettabile solo se:

- non rompe l'avvio del sistema;
- non altera inutilmente la struttura congelata;
- migliora almeno un flusso operativo reale;
- può essere validato tramite `python mdos.py validate`, `python mdos.py status` o comandi equivalenti;
- lascia il repository più chiaro, più leggibile o più controllabile rispetto allo stato precedente.

## Regola X10

Ogni `refactor` deve produrre almeno 10 avanzamenti concreti.

## Struttura congelata

L'evoluzione avviene tramite dataset, plugin, log, export e matrici, non cambiando continuamente cartelle.
