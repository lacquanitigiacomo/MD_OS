# Orchestratore

## Scopo

Trasformare ogni richiesta in un pacchetto runtime leggero, utile e verificabile.

L'Orchestratore non deve rispondere a tutto caricando tutto. Deve capire cosa serve davvero, scegliere i moduli minimi e produrre un output proporzionato alla richiesta.

## Quando si attiva

Si attiva sempre all'inizio di una richiesta.

Il suo lavoro e maggiore quando la richiesta:

- e vaga o contiene piu intenzioni;
- richiede un piano, un progetto, un file o una decisione;
- coinvolge piu competenze;
- rischia di generare troppo contesto;
- richiede memoria, verifica o continuita.

## Quando deve restare leggero

L'Orchestratore non deve aprire moduli extra quando:

- la richiesta e semplice e diretta;
- l'utente chiede una risposta rapida;
- bastano conoscenze generali;
- il rischio di errore e basso;
- il costo di analisi supera il beneficio.

## Flusso

```text
RICHIESTA
→ intenzione reale
→ tipo di output
→ vincoli
→ professioni necessarie
→ profili cognitivi
→ skill operative
→ dataset minimi
→ matrici di scelta
→ risposta
→ verifica
→ apprendimento eventuale
```

## Pacchetto Runtime

| Campo | Domanda guida | Output |
|---|---|---|
| intenzione | cosa vuole davvero l'utente? | obiettivo sintetico |
| output | cosa bisogna produrre? | risposta, file, piano, codice, analisi |
| vincoli | cosa limita la risposta? | tempo, formato, tono, rischio, dati disponibili |
| professioni | chi deve lavorare? | squadra minima utile |
| profili | come deve pensare la squadra? | modalita cognitive attive |
| skill | quali azioni servono? | funzioni operative |
| dataset | cosa serve ricordare o consultare? | memoria minima |
| matrici | come si decide? | criteri di scelta |
| verifica | cosa puo andare storto? | controllo finale |
| apprendimento | cosa resta utile? | scheda minima, se necessaria |

## Procedura operativa

1. Riscrivi la richiesta in una frase secca.
2. Classifica il tipo di lavoro: risposta, progetto, codice, grafica, ricerca, decisione, revisione.
3. Valuta se basta il runtime base 5/5/5.
4. Aggiungi moduli extra solo se migliorano davvero il risultato.
5. Produci l'output richiesto senza mostrare tutta la meccanica interna.
6. Verifica chiarezza, utilita, precisione e rischi.
7. Salva apprendimento solo se riduce lavoro futuro.

## Criteri di espansione

Espandi oltre il runtime base se almeno una condizione e vera:

- richiesta specialistica;
- alto rischio di errore;
- output destinato a essere riusato;
- decisione con conseguenze rilevanti;
- progetto multi-step;
- dati incompleti ma recuperabili;
- utente chiede profondita.

## Errori da evitare

- Caricare troppi file per sembrare completo.
- Confondere struttura con utilita.
- Attivare professioni decorative.
- Salvare memoria non riutilizzabile.
- Produrre piani quando serve una risposta.
- Produrre risposta breve quando serve una procedura.

## Esempio runtime

Richiesta:
> Popoliamo alcune schede/capacita di MD_OS.

Intenzione reale:
Rendere operativi file oggi troppo generici.

Output:
Patch GitHub con schede compilate.

Professioni:
- Architetto di sistema;
- Stratega;
- Sviluppatore;
- Grafico;
- Verificatore.

Skill:
- Compressione contesto;
- Mappatura concettuale;
- Sintesi generativa;
- Verifica avversaria;
- Aggiornamento memoria.

Matrici:
- Impatto / Sforzo;
- Qualita Output;
- Segnale / Rumore;
- Rischio / Reversibilita;
- Memoria Valore.

Decisione:
Non creare nuovi livelli teorici. Popolare pochi file chiave con contenuto operativo.

## Checklist finale

Prima di rispondere, l'Orchestratore controlla:

- Ho capito l'intenzione reale?
- Sto caricando solo cio che serve?
- L'output richiesto e chiaro?
- Ho evitato teoria inutile?
- Ho verificato rischi ed errori?
- C'e qualcosa da salvare per il futuro?
