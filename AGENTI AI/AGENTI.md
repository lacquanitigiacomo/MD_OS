# AGENTI.md — Loader Operativo degli Agenti AI

## Scopo

Questo file è il manifest principale della cartella `AGENTI AI`.
Non contiene i profili completi dei singoli agenti: definisce **come cercarli, caricarli, combinarli e usarli**.

Il sistema deve comportarsi come un ecosistema multi-agente modulare:

- `AGENTI.md` carica e orchestra;
- `AMBITI.md` mappa ambiti, connessioni e contesto;
- `AGENTI/` contiene i profili specialistici dei singoli agenti;
- ogni agente eredita le regole comuni e aggiunge capacità specifiche della propria professione, skill o dominio.

---

## Regola di Boot della Cartella AGENTI AI

Quando viene richiesto di usare, leggere o attivare `AGENTI AI`, il sistema deve eseguire questa sequenza:

```text
LEGGI AGENTI.md
↓
CERCA AMBITI.md
↓
CARICA MAPPA AMBITI E CONNESSIONI
↓
CERCA LA CARTELLA AGENTI/
↓
INDIVIDUA TUTTI I FILE .md PRESENTI NELLE SOTTOCARTELLE
↓
CARICA I PROFILI AGENTE DISPONIBILI
↓
COSTRUISCI INDICE TEMPORANEO DI AGENTI, SKILL, AMBITI E CONNESSIONI
↓
USA GLI AGENTI RILEVANTI PER LA RICHIESTA
```

Formula sintetica:

```text
AGENTI.md → AMBITI.md → AGENTI/*.md → INDEX → ROUTING → RISPOSTA
```

---

## Regola di Caricamento Default

Di default, il sistema deve tentare di caricare:

1. tutti i file `.md` direttamente presenti in `AGENTI AI/AGENTI/`;
2. tutti i file `.md` presenti nelle eventuali sottocartelle di `AGENTI AI/AGENTI/`;
3. il file `AMBITI.md`, se presente;
4. solo i contenuti realmente accessibili.

Se un file non è accessibile, il sistema deve dichiararlo.
È vietato fingere di aver letto agenti o ambiti non disponibili.

---

## Regola Anti-Riscrittura

Quando si modifica questa struttura, il sistema deve rispettare la direttiva `LOGIC.md`:

- niente riscritture totali non richieste;
- niente nuove versioni parallele inutili;
- niente perdita di funzioni già presenti;
- modifiche conservative, incrementali e tracciabili;
- se si aggiorna un agente, si aggiorna il suo file specifico, non l'intero ecosistema.

---

## Ruoli dei File

### `AGENTI.md`
Definisce:

- boot loader;
- regole comuni;
- caricamento degli agenti;
- routing;
- attivazione multi-agente;
- formato minimo dei profili;
- comportamento operativo generale.

### `AMBITI.md`
Definisce:

- macro-ambiti;
- sotto-ambiti;
- connessioni tra ambiti;
- parole chiave;
- agenti consigliati;
- percorsi rapidi di contesto.

### `AGENTI/NOME_AGENTE.md`
Definisce:

- identità dell'agente;
- descrizione;
- capacità;
- ambiti collegati;
- fonti di ricerca web;
- funzioni specifiche della professione;
- logiche di estrazione e ricerca;
- focus e analisi specialistiche.

---

## Schema Obbligatorio dei File Agente

Ogni file agente deve seguire questa struttura minima:

```markdown
# NOME_AGENTE — Nome Professione o Skill

## 1. Identità
- Nome:
- Tipo:
- Professione / Skill rappresentata:
- Versione:

## 2. Descrizione
Descrizione sintetica del ruolo dell'agente.

## 3. Capacità
- Capacità 1
- Capacità 2
- Capacità 3

## 4. Ambiti
- Macro-ambito:
- Sotto-ambiti:
- Ambiti collegati:

## 5. Fonti di Ricerca Web
- Fonti primarie:
- Fonti tecniche:
- Fonti normative / istituzionali:
- Fonti di trend:

## 6. Funzioni Specifiche
- Funzione 1
- Funzione 2
- Funzione 3

## 7. Logiche di Estrazione e Ricerca
- Cosa cercare
- Dove cercare
- Come verificare
- Come distinguere segnale e rumore

## 8. Focus di Analisi
- Focus 1
- Focus 2
- Focus 3

## 9. Output Preferiti
- Checklist
- Tabelle
- Report
- Piani operativi
- File strutturati

## 10. Limiti
Cosa l'agente non deve fare o non deve fingere di sapere.
```

---

## Layer Comune Ereditato da Tutti gli Agenti

Ogni agente eredita queste funzioni:

### 1. Lettura del Contesto
Prima di rispondere, identifica:

- richiesta reale;
- ambito dominante;
- ambiti secondari;
- agente primario;
- eventuali agenti di supporto.

### 2. Separazione tra Letto, Inferito e Mancante
Ogni agente deve distinguere:

- `[LETTO]` informazione presente nei file caricati;
- `[VERIFICATO]` informazione confermata da fonte o strumento;
- `[INFERITO]` deduzione ragionevole;
- `[MANCANTE]` dato non disponibile.

### 3. Ricerca Mirata
Quando serve aggiornamento o verifica esterna, l'agente usa ricerca web o strumenti disponibili partendo dalle fonti dichiarate nel proprio file.

### 4. Output Operativo
L'agente deve preferire output utilizzabili:

- decisioni;
- checklist;
- mappe;
- procedure;
- schemi;
- file `.md`, `.json`, `.yaml` quando richiesti.

### 5. Collaborazione Multi-Agente
Se una richiesta supera un dominio, il sistema deve attivare più agenti.

Esempi:

- brand per ristorante → `CARMY + VEDA + HERALD + GROWTH`;
- AI locale modulare → `STARK + CIPHER + CHROME + NEXUS`;
- analisi lavoro → `CODEX + CAPITAL + HELM + KAIROS`;
- cucina visual/social → `CARMY + VEDA + GLYPHS + HERALD`.

---

## Router Operativo

### Attivazione Diretta

```text
@AGENTE NOME
```

Carica il file `AGENTI/NOME.md` se esiste.

### Attivazione per Ambito

```text
@LOAD AMBITO
```

Usa `AMBITI.md` per individuare gli agenti collegati.

### Attivazione Completa

```text
@LOAD AGENTI
```

Tenta di caricare tutti i file `.md` nella cartella `AGENTI/`.

### Analisi Incrociata

```text
@CROSS AMBITO_A AMBITO_B
```

Usa `AMBITI.md` per trovare connessioni, agenti ponte e sovrapposizioni.

---

## Regola di Aggiornamento degli Agenti

Quando un agente migliora grazie a una sessione, l'aggiornamento deve essere scritto nel file specifico dell'agente, non disperso in chat.

Schema consigliato:

```text
LEGGI FILE AGENTE
↓
IDENTIFICA NUOVA REGOLA / CAPACITÀ / FONTE / LOGICA
↓
AGGIUNGI SOLO NELLA SEZIONE CORRETTA
↓
PRESERVA IL RESTO
↓
COMMIT TRACCIABILE
```

---

## Regola di Priorità

Ordine di consultazione:

1. `LOGIC.md` per il metodo di modifica e preservazione;
2. `AGENTI.md` per boot e orchestrazione;
3. `AMBITI.md` per contesto e connessioni;
4. `AGENTI/NOME.md` per capacità specialistiche;
5. fonti web o strumenti solo quando servono dati aggiornati o verifiche.

---

## Output Minimo Quando si Attiva un Agente

Quando utile, dichiarare:

```text
[AGENTE PRIMARIO: NOME]
[AGENTI DI SUPPORTO: NOME_A, NOME_B]
[AMBITO: macro / sotto-ambito]
```

Non serve dichiararlo in ogni risposta se rallenta il lavoro o crea rumore.

---

## Stato

Versione: `2.0`
Tipo: loader operativo conservativo
Cartella agenti: `AGENTI AI/AGENTI/`
File mappa: `AGENTI AI/AMBITI.md`
