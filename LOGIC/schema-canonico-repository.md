# SCHEMA CANONICO REPOSITORY MD_OS

## Scopo

Questo file definisce la struttura canonica del repository MD_OS.

Ogni nuova cartella, file, agente, funzione, procedura, formula, schema, soglia, output o logica deve rispettare questa mappa.

L'obiettivo è evitare duplicazioni, ambiguità di naming e cartelle parallele con significato simile.

---

## Regola fondamentale

Prima di creare un nuovo file o una nuova cartella:

1. verificare se esiste già una cartella canonica adatta;
2. usare la cartella esistente;
3. non inventare nuove varianti di naming;
4. se manca davvero un ambito, proporlo prima all'utente;
5. non creare cartelle sinonime.

---

## Root canonica

La root del repository deve contenere solo:

```txt
README.md
BOOT.md
AGENTI/
FUNZIONI/
PROCEDURE/
FORMULE/
SCHEMI/
SOGLIE/
LOGIC/
OUTPUT/
ROUTING/
SICUREZZA/
PROGETTI/
TEMPLATE/
```

Non creare nuove cartelle root senza approvazione esplicita.

---

## Cartelle funzionali canoniche

### AGENTI

Contiene i profili operativi specialistici.

Percorso canonico:

```txt
AGENTI/AGENTI SINGOLI/<AMBITO>/<agente>.md
```

File di servizio ammessi:

```txt
AGENTI/README.md
AGENTI/REGISTRO-AGENTI.md
AGENTI/TEMPLATE-AGENTE.md
```

### FUNZIONI

Contiene azioni operative richiamabili dagli agenti.

Percorso canonico:

```txt
FUNZIONI/<AMBITO>/<funzione>.md
```

### PROCEDURE

Contiene sequenze operative professionali.

Percorso canonico:

```txt
PROCEDURE/<AMBITO>/<procedura>.md
```

### FORMULE

Contiene formule, indici, calcoli e criteri matematici.

Percorso canonico:

```txt
FORMULE/<AMBITO>/<formula>.md
```

### SCHEMI

Contiene strutture dati, tabelle e formati intermedi.

Percorso canonico:

```txt
SCHEMI/<AMBITO>/<schema>.md
```

### SOGLIE

Contiene criteri di rischio, anomalia, priorità e classificazione.

Percorso canonico:

```txt
SOGLIE/<AMBITO>/<soglia>.md
```

### LOGIC

Contiene regole generali, orchestrazione, gestione incertezza, struttura repository e metodo operativo.

Percorso canonico:

```txt
LOGIC/<ambito-o-regola>/<file>.md
```

Sono ammessi anche file generali direttamente in `LOGIC/`.

### OUTPUT

Contiene formati di risposta, report finali, dashboard e modelli di consegna.

Percorso canonico:

```txt
OUTPUT/<AMBITO>/<output>.md
```

### ROUTING

Contiene criteri di attivazione degli agenti e instradamento per ambito.

Percorso canonico:

```txt
ROUTING/<file-routing>.md
```

---

## Ambiti canonici attuali

Gli ambiti attualmente ammessi sono:

```txt
DESIGN_COMUNICAZIONE
DOCUMENTI_DATI_REPORT
ECONOMIA_FINANZA_REVISIONE
LEGALE_NORMATIVO
SALUTE_BENESSERE
TECNOLOGIA_SVILUPPO
```

---

## Ambiti in valutazione

Questi ambiti possono essere aggiunti solo dopo approvazione esplicita:

```txt
LAVORO_VERTENZA_SINDACALE
DATI_ANALYTICS_AI
PRODOTTO_STRATEGIA
AI_AUTOMAZIONE
INFRASTRUTTURE_DIGITALI
```

---

## Alias vietati o deprecati

Non usare come ambiti:

```txt
TECNOLOGIA
SVILUPPO
TECH
WEB
FINANZA
ECONOMIA
LAVORO
LEGAL
SALUTE
DESIGN
DATI
REPORT
```

Usare invece gli ambiti canonici:

```txt
TECNOLOGIA_SVILUPPO
ECONOMIA_FINANZA_REVISIONE
LEGALE_NORMATIVO
SALUTE_BENESSERE
DESIGN_COMUNICAZIONE
DOCUMENTI_DATI_REPORT
```

---

## Regole per nuovi agenti

Ogni nuovo agente deve:

1. stare in `AGENTI/AGENTI SINGOLI/<AMBITO>/`;
2. essere registrato in `AGENTI/REGISTRO-AGENTI.md`;
3. richiamare solo moduli con path canonici;
4. non duplicare formule, procedure o funzioni;
5. avere nome file in minuscolo e kebab-case.

Esempio corretto:

```txt
AGENTI/AGENTI SINGOLI/TECNOLOGIA_SVILUPPO/senior-web-developer.md
```

Esempio errato:

```txt
AGENTI/TECNOLOGIA/WebDeveloperSenior.md
```

---

## Regole per moduli collegati

Se un agente richiama una funzione, lo deve fare così:

```txt
/FUNZIONI/<AMBITO>/<nome-funzione>.md
```

Esempio corretto:

```txt
/FUNZIONI/TECNOLOGIA_SVILUPPO/revisiona_codice.md
```

Esempio errato:

```txt
/FUNZIONI/revisiona_codice.md
```

La stessa regola vale per:

```txt
/PROCEDURE/<AMBITO>/...
/FORMULE/<AMBITO>/...
/SCHEMI/<AMBITO>/...
/SOGLIE/<AMBITO>/...
/OUTPUT/<AMBITO>/...
/LOGIC/<AMBITO>/...
```

---

## Regola anti-duplicazione

Prima di creare un nuovo file verificare:

1. esiste già un file equivalente?
2. esiste già una funzione simile?
3. esiste già uno schema riutilizzabile?
4. il nuovo contenuto è davvero diverso?
5. può essere esteso un modulo esistente invece di crearne uno nuovo?

---

## Regola di aggiornamento

Quando si aggiunge un nuovo ambito o agente, aggiornare sempre:

```txt
AGENTI/REGISTRO-AGENTI.md
ROUTING/routing-agenti.md
LOGIC/schema-canonico-repository.md
```

Se vengono aggiunti moduli tecnici, aggiornare anche schemi, output e funzioni collegate.

---

## Regola di coerenza

Un agente deve richiamare solo file esistenti o dichiarati come da creare nello stesso pacchetto di aggiornamento.

Non lasciare riferimenti rotti.

---

## Regola di migrazione

Se viene trovata una cartella non canonica:

1. non aggiungere nuovi file lì;
2. censire il contenuto;
3. migrare verso cartella canonica;
4. aggiornare i riferimenti;
5. rimuovere o deprecare la cartella vecchia solo dopo conferma.

---

## Decisione canonica attuale

Per l'ambito tecnologia usare sempre:

```txt
TECNOLOGIA_SVILUPPO
```

Non usare:

```txt
TECNOLOGIA
```
