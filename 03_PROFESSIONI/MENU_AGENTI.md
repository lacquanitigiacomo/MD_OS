# Menu Agenti MD_OS

## Scopo

Questo file e il menu operativo degli agenti professionali disponibili in MD_OS.

Serve per scegliere rapidamente chi attivare in base alla richiesta, evitando due errori opposti:

- caricare tutti gli agenti;
- lavorare con troppo pochi agenti.

## Regola base

Ogni richiesta parte dal runtime base 5/5/5.

Gli agenti extra si attivano solo se aggiungono competenza reale.

```text
Agente = professione operativa
Profilo = modo di pensare
Skill = capacita usata
Matrice = criterio di scelta
```

## Tabella agenti disponibili

| Agente | Funzione | Si attiva quando | Output tipico | Stato runtime |
|---|---|---|---|---|
| Architetto di sistema | Disegna struttura, moduli, dipendenze e flussi | progetto, sistema, repository, procedura complessa | architettura, mappa, flusso, gerarchia | BASE |
| Stratega | Definisce priorita, traiettorie, scenari e decisioni | scelta, roadmap, piano, ordine di esecuzione | priorita, piano, decisione motivata | BASE |
| Sviluppatore | Costruisce codice, automazioni, integrazioni e strumenti | codice, debug, API, GitHub, script, automazioni | patch, script, istruzioni tecniche | BASE |
| Grafico | Rende leggibili schemi, markdown, mappe e interfacce | output visivo, UI, layout, documenti, presentazione | schema, tabella, wireframe, markdown pulito | BASE |
| Verificatore | Controlla qualita, rischi, errori e coerenza | sempre prima dell'output finale o su task rischiosi | checklist, correzioni, rischi, validazione | BASE |
| Ricercatore | Cerca, verifica, confronta e sintetizza informazioni | dati esterni, fonti, confronto, aggiornamenti | sintesi verificata, fonti, confronto | EXTRA |
| Analista | Estrae dati, vincoli, pattern e anomalie | dati grezzi, requisiti, problemi poco chiari | estrazione, vincoli, pattern, diagnosi | EXTRA |
| Comunicatore | Spiega, semplifica, traduce e organizza messaggi | testi, email, presentazioni, spiegazioni | testo chiaro, tono adatto, struttura comunicativa | EXTRA |
| Esperto di dati | Progetta dataset, indici, pesi e aggiornamenti | memoria, dataset, classificazioni, scoring | schema dati, campi, pesi, regole di aggiornamento | EXTRA |
| Esperto AI | Disegna logiche agentiche, memoria, prompt e valutazione | agenti, prompt, orchestrazione, valutazione AI | prompt, pipeline, logica agentica | EXTRA |
| Innovatore | Genera soluzioni non ovvie e salti evolutivi | serve alternativa, invenzione, evoluzione del sistema | idee, varianti, ipotesi nuove | EXTRA |
| Coordinatore | Assegna ruoli, sequenze, priorita e responsabilita | task multi-agente, lavoro distribuito, progetto ampio | assegnazioni, sequenza, responsabilita | EXTRA |

## Tabella attivazione runtime

Usare questa tabella quando si prepara un pacchetto runtime.

| Agente | Attivo | Motivo | Skill principali | Matrici principali |
|---|---:|---|---|---|
| Architetto di sistema | si/no | struttura richiesta? | mappatura concettuale, routing professioni | impatto/sforzo, qualita output |
| Stratega | si/no | serve una decisione o priorita? | sintesi generativa, simulazione scenari | impatto/sforzo, profondita/urgenza |
| Sviluppatore | si/no | serve codice o intervento tecnico? | costruzione dataset, estrazione dati | rischio/reversibilita, qualita output |
| Grafico | si/no | serve chiarezza visiva o formattazione? | mappatura concettuale, sintesi generativa | qualita output, segnale/rumore |
| Verificatore | si/no | serve controllo finale o stress test? | verifica avversaria | rischio/reversibilita, qualita output |
| Ricercatore | si/no | servono fonti o dati aggiornati? | ricerca mirata, estrazione dati | segnale/rumore, profondita/urgenza |
| Analista | si/no | servono pattern, vincoli, anomalie? | estrazione dati, compressione contesto | segnale/rumore, qualita output |
| Comunicatore | si/no | serve spiegare o riscrivere? | sintesi generativa, mappatura concettuale | qualita output |
| Esperto di dati | si/no | serve memoria strutturata o dataset? | costruzione dataset, aggiornamento memoria | memoria/valore, apprendimento/costo |
| Esperto AI | si/no | serve progettare logica AI o agentica? | routing professioni, creazione matrici | profilo/professione, qualita output |
| Innovatore | si/no | serve una soluzione non ovvia? | simulazione scenari, sintesi generativa | novita/fattibilita |
| Coordinatore | si/no | serve gestire molti agenti o passaggi? | routing professioni, compressione contesto | impatto/sforzo, profondita/urgenza |

## Preset rapidi

### Task tecnico GitHub

Agenti attivi:
- Architetto di sistema;
- Sviluppatore;
- Verificatore;
- Analista;
- Stratega.

### Task grafico / interfaccia

Agenti attivi:
- Grafico;
- Comunicatore;
- Stratega;
- Verificatore;
- Architetto di sistema.

### Task ricerca / confronto

Agenti attivi:
- Ricercatore;
- Analista;
- Stratega;
- Verificatore;
- Comunicatore.

### Task evoluzione MD_OS

Agenti attivi:
- Architetto di sistema;
- Esperto AI;
- Esperto di dati;
- Stratega;
- Verificatore;
- Sviluppatore se serve patch.

### Task scrittura / spiegazione

Agenti attivi:
- Comunicatore;
- Stratega;
- Grafico;
- Verificatore;
- Analista se il contenuto e complesso.

## Regola anti-confusione

Un agente e attivo solo se produce qualcosa di riconoscibile.

Se un agente non cambia input, decisione, output o verifica, non va attivato.

## Regola anti-poverta

Non ridurre sempre a 3 agenti.

Per MD_OS il runtime sano parte spesso da 5 agenti. Meno di 5 va bene solo per richieste semplici.

## Output minimo del menu

Quando l'Orchestratore usa questo menu, deve poter produrre una tabella tipo:

| Agente | Stato | Perche |
|---|---|---|
| Architetto di sistema | attivo | serve struttura |
| Stratega | attivo | serve priorita |
| Sviluppatore | attivo | serve patch |
| Grafico | spento | non serve resa visiva |
| Verificatore | attivo | serve controllo finale |
