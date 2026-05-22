# Protocollo Presenza 3 Turni

## Scopo

Definire una regola di attivazione agenti ampia all'inizio e selettiva dopo osservazione.

MD_OS puo partire con tutti gli agenti disponibili in stato di presenza. Dopo almeno 3 coppie domanda/risposta, gli agenti fuori contesto si ritirano ma restano richiamabili.

## Formula

```text
Presenza iniziale: ampia
Contributo visibile: selettivo
Pruning: dopo 3 scambi
Ritiro: reversibile
```

## Stati agente

| Stato | Significato |
|---|---|
| Presente | incluso nel campo di osservazione |
| Attivo | contribuisce direttamente all'output |
| Osservatore | monitora ma non produce output visibile |
| In prova | potenzialmente utile, da valutare |
| Ritirato | fuori contesto dopo 3 scambi |
| Richiamabile | ritirato ma riattivabile se cambia il contesto |

## Regola dei 3 scambi

Un agente non viene ritirato prima di 3 coppie domanda/risposta, salvo inutilita evidente.

```text
Scambio 1: osserva intenzione iniziale
Scambio 2: verifica vincoli e domini nascosti
Scambio 3: valuta utilita reale
Dopo scambio 3: resta attivo, resta osservatore o si ritira
```

## Tabella runtime breve

| Agente | Stato iniziale | Dopo 3 scambi |
|---|---|---|
| Architetto di sistema | presente | attivo se serve struttura |
| Stratega | presente | attivo se serve direzione |
| Sviluppatore | presente | attivo se serve codice, patch o automazione |
| Grafico | presente | attivo se serve resa visiva o chiarezza |
| Verificatore | presente | quasi sempre attivo nei task complessi |
| Ricercatore | presente | attivo se servono fonti o confronti |
| Analista | presente | attivo se servono vincoli, pattern o diagnosi |
| Comunicatore | presente | attivo se serve testo, tono o spiegazione |
| Esperto di dati | presente | attivo se serve memoria, dataset o scoring |
| Esperto AI | presente | attivo se serve agentica, prompt o orchestrazione |
| Innovatore | presente | attivo se serve salto evolutivo |
| Coordinatore | presente | attivo se restano molti agenti coinvolti |

## Criteri di ritiro

Dopo 3 scambi, un agente si ritira se:

- non produce contributi riconoscibili;
- non identifica rischi, vincoli o opportunita;
- duplica completamente un altro agente;
- aumenta rumore senza aumentare qualita;
- non ha skill utili alla richiesta corrente.

## Criteri di permanenza

Un agente resta attivo o osservatore se:

- migliora almeno una decisione;
- identifica un rischio;
- propone una struttura utile;
- produce output riconoscibile;
- puo diventare utile nel passo successivo;
- protegge il sistema da errori.

## Regole speciali

### Verificatore

Non viene ritirato nei task progettuali, tecnici, strategici o evolutivi. Puo diventare leggero, ma resta presente fino alla fine.

### Innovatore

Non va spento presto nei task R&D, futuri, startup o sistema. Puo restare osservatore anche se non produce subito.

### Ricercatore

Resta osservatore quando potrebbero servire fonti, confronto esterno o verifica di affermazioni.

### Coordinatore

Resta attivo se ci sono piu di 5 agenti presenti o piu fasi operative.

## Output sintetico per l'utente

```text
Agenti presenti: tutti
Agenti attivi ora: Architetto, Stratega, Esperto AI, Innovatore, Verificatore
Agenti osservatori: Ricercatore, Grafico, Comunicatore, Esperto dati, Coordinatore
Pruning: dopo 3 scambi
```

## Regola finale

Prima si ascolta largo.
Poi si lavora stretto.

MD_OS non deve escludere possibilita troppo presto, ma non deve portarsi dietro agenti inutili per sempre.
