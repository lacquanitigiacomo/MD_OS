# Sistema Interattivo Progressivo MD_OS

## Scopo

Questo documento definisce come far evolvere MD_OS da insieme di comandi locali a sistema interattivo performante, capace di apprendere progressivamente dai propri dataset, migliorare la qualita delle risposte e diventare piu intelligente senza dipendere da calcolo continuo o servizi esterni obbligatori.

## Tesi centrale

MD_OS deve funzionare come un ciclo cognitivo locale:

```txt
input utente -> recupero storico -> orchestrazione agenti -> sintesi -> valutazione -> risposta -> apprendimento -> aggiornamento dataset
```

Il sistema non deve generare ogni risposta da zero. Deve usare storico, dataset, pattern, decisioni precedenti, scoring e feedback per migliorare progressivamente.

## Struttura attuale da riutilizzare

MD_OS dispone gia di elementi fondamentali:

- `validate`: verifica dataset e integrita minima;
- `status`: mostra stato e conteggi;
- `query`: recupera informazioni dai dati;
- `learn`: salva nuova conoscenza;
- `refactor`: produce avanzamenti X10;
- `matrix`: esporta matrici;
- `profile`: misura readiness;
- `release-check`: controlla blocker;
- `agent`: legge agenti;
- `beta`: esegue scenari di test.

Questi comandi non vanno sostituiti. Vanno orchestrati.

## Obiettivo operativo

Creare un comando centrale:

```bash
python mdos.py interact
```

Oppure, in forma diretta:

```bash
python mdos.py ask "come miglioriamo il sistema memoria?"
```

Il comando deve:

1. ricevere una richiesta;
2. estrarre termini chiave;
3. interrogare i dataset;
4. selezionare gli agenti utili;
5. generare una risposta strutturata;
6. valutare qualita, coerenza e rischio;
7. proporre una prossima azione;
8. salvare apprendimento, pattern e decisioni utili.

## Architettura proposta

```txt
mdos/
  engines/
    interact.py       # ciclo interattivo principale
    orchestrator.py   # selezione agenti e composizione risultati
    evaluator.py      # scoring qualita, efficienza, visione
    planner.py        # scomposizione obiettivi e next action
    memory.py         # recupero leggero da dataset e storico
    patterns.py       # riconoscimento richieste ricorrenti

datasets/
  ai_capabilities.jsonl
  interactions.jsonl
  decisions.jsonl
  patterns.jsonl
  feedback.jsonl
  agent_scores.jsonl
```

## Ciclo interattivo

### 1. Input

Il sistema riceve una richiesta utente.

Esempio:

```txt
Trova una strategia per rendere MD_OS piu autonomo e performante.
```

### 2. Normalizzazione

Il testo viene pulito e trasformato in elementi semplici:

- intenzione;
- parole chiave;
- area coinvolta;
- urgenza;
- tipo output richiesto;
- sistemi MD_OS pertinenti.

### 3. Recupero storico

Il sistema interroga dataset e storico con logica leggera:

- query testuale;
- matching keyword;
- similarita semplice;
- ranking per frequenza, utilita e coerenza;
- filtro su stato e area.

Non serve calcolo pesante. Serve recupero intelligente.

### 4. Selezione agenti

L'orchestratore sceglie gli agenti/sistemi piu adatti.

Esempio:

- Planner;
- Memory Agent;
- CTO Agent;
- Quality Reviewer;
- Next Action Agent;
- Systems Mapper.

### 5. Produzione risposta

Ogni agente produce una parte:

- diagnosi;
- proposta;
- rischio;
- output atteso;
- azione successiva.

L'orchestratore sintetizza in un'unica risposta leggibile.

### 6. Valutazione

Il sistema valuta la risposta prima di restituirla:

- utilita;
- chiarezza;
- coerenza con MD_OS;
- leggerezza;
- innovazione;
- efficienza;
- visione;
- rischio di deriva.

### 7. Risposta

La risposta deve sempre contenere, quando utile:

- sintesi;
- ragionamento operativo;
- proposta concreta;
- rischio;
- prossima azione.

### 8. Apprendimento progressivo

Dopo la risposta il sistema salva:

- richiesta;
- termini chiave;
- agenti usati;
- dataset consultati;
- output prodotto;
- score;
- eventuale decisione;
- prossima azione consigliata.

Questo alimenta `interactions.jsonl`, `patterns.jsonl`, `decisions.jsonl` e `feedback.jsonl`.

## Come diventa piu intelligente

MD_OS diventa piu intelligente non perche aumenta il calcolo, ma perche aumenta la qualita dello storico.

Ogni interazione produce dati riutilizzabili:

- quali richieste tornano spesso;
- quali agenti aiutano di piu;
- quali risposte vengono accettate;
- quali decisioni portano risultati;
- quali pattern riducono lavoro;
- quali aree generano blocker;
- quali sistemi hanno piu impatto.

Con il tempo il sistema puo:

- suggerire risposte migliori;
- recuperare contesto piu rapidamente;
- evitare ripetizioni;
- riconoscere pattern ricorrenti;
- proporre next action piu precise;
- distinguere innovazione utile da rumore;
- dare priorita a cio che genera valore.

## Dataset fondamentali

### `interactions.jsonl`

Registra ogni scambio utile.

```json
{
  "id": "INT-0001",
  "input": "come rendiamo MD_OS piu autonomo?",
  "intent": "miglioramento_sistema",
  "keywords": ["autonomia", "performance", "dataset"],
  "agents": ["planner", "cto", "quality_reviewer"],
  "output_summary": "proposto ciclo interact",
  "score": 86,
  "learned": true
}
```

### `patterns.jsonl`

Registra schemi ricorrenti.

```json
{
  "id": "PAT-0001",
  "pattern": "richiesta_miglioramento_architettura",
  "trigger": ["migliorare", "sistema", "performante"],
  "agents": ["systems_mapper", "cto", "planner"],
  "output_template": "diagnosi_proposta_next_action"
}
```

### `feedback.jsonl`

Registra valutazioni esplicite o implicite.

```json
{
  "id": "FDB-0001",
  "interaction_id": "INT-0001",
  "rating": 8,
  "note": "proposta utile, serve implementazione CLI",
  "azione": "prioritizzare interact"
}
```

### `agent_scores.jsonl`

Misura utilita degli agenti.

```json
{
  "agent": "cto",
  "task_type": "analisi_tecnica",
  "uses": 12,
  "success_score_avg": 8.4,
  "last_update": "2026-05-22"
}
```

## Primo set di agenti operativi

### Planner

Scompone richieste in passaggi.

### Memory Agent

Recupera storico e dataset rilevanti.

### CTO Agent

Valuta architettura, codice, rischio tecnico e refactor.

### Strategist

Collega scelte tecniche alla visione di medio periodo.

### Quality Reviewer

Controlla utilita, coerenza, completezza e verificabilita.

### Next Action Agent

Propone il prossimo passo piu utile.

### Systems Mapper

Mappa componenti, relazioni, dipendenze e leve di miglioramento.

## Modalita interattive

### Modalita ask

Una richiesta, una risposta.

```bash
python mdos.py ask "trova la prossima azione migliore"
```

### Modalita interact

Sessione continua.

```bash
python mdos.py interact
```

### Modalita learn

Salvataggio mirato di una nuova informazione.

```bash
python mdos.py learn --text "Decisione: interact diventa il centro operativo"
```

### Modalita evaluate

Valuta una proposta o un file.

```bash
python mdos.py evaluate --target docs/sistemi/sistema-interattivo-progressivo.md
```

## Regole di performance

- privilegiare file JSONL append-only;
- evitare database complessi nella prima fase;
- usare ranking semplice e trasparente;
- salvare ogni risultato utile;
- non ricalcolare cio che e gia stato deciso;
- separare memoria, agenti e valutazione;
- mantenere comandi CLI chiari;
- introdurre caching solo dopo aver misurato colli di bottiglia.

## Regole di apprendimento

MD_OS puo apprendere solo cio che viene registrato in modo verificabile.

Ogni apprendimento deve avere:

- origine;
- testo;
- keywords;
- area;
- utilita prevista;
- collegamento a interazione o decisione;
- data;
- stato.

L'apprendimento non deve essere accumulo cieco. Deve essere memoria utile.

## Misura di intelligenza progressiva

L'intelligenza di MD_OS va misurata con indicatori pratici:

- riduzione dei passaggi manuali;
- aumento delle risposte riutilizzabili;
- miglioramento del recupero storico;
- crescita dei pattern riconosciuti;
- diminuzione delle decisioni ripetute;
- aumento della qualita media degli output;
- diminuzione dei blocker ricorrenti;
- miglioramento dello score innovazione/efficienza/visione.

## Roadmap implementativa

### Fase 1: Dataset di apprendimento

- Creare `interactions.jsonl`.
- Creare `patterns.jsonl`.
- Creare `feedback.jsonl`.
- Creare `agent_scores.jsonl`.

### Fase 2: Motore interattivo minimo

- Creare `mdos/engines/interact.py`.
- Aggiungere comando `ask`.
- Collegare `query`, `learn` e `agent`.

### Fase 3: Orchestrazione agenti

- Creare `orchestrator.py`.
- Usare `ai_capabilities.jsonl` per scegliere sistemi e agenti.
- Produrre risposta sintetica con next action.

### Fase 4: Valutazione

- Creare `evaluator.py`.
- Integrare score innovazione, efficienza e visione.
- Salvare score in `interactions.jsonl`.

### Fase 5: Apprendimento progressivo

- Salvare pattern ricorrenti.
- Aggiornare agent_scores.
- Suggerire automaticamente miglioramenti.

### Fase 6: Sistema performante

- Ottimizzare ranking.
- Aggiungere cache locale se necessaria.
- Generare report periodici.
- Collegare release-check ai dataset interattivi.

## Decisione architetturale

Il centro futuro di MD_OS deve essere `interact`/`ask`, non una collezione dispersa di comandi.

I comandi esistenti restano fondamentali, ma diventano sottosistemi richiamati dal ciclo interattivo.

## Formula finale

```txt
memoria + agenti + valutazione + feedback + dataset = intelligenza progressiva locale
```

Questo e il modo piu coerente per far funzionare MD_OS come sistema interattivo performante e progressivamente piu intelligente.
