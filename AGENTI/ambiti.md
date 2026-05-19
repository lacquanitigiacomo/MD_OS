# ambiti.md

Questo file contiene gli ambiti di riferimento e le intersezioni usate dagli agenti.

## Definizione

Un ambito è un dominio contestuale.

Serve agli agenti per:

- capire il contesto;
- orientare le decisioni;
- selezionare funzioni;
- scegliere schemi;
- evitare risposte generiche.

## Schema ambito

```yaml
ambito:
  nome: ""
  versione: "1.0"
  descrizione: ""
  parole_chiave: []
  agenti_preferiti: []
  funzioni_preferite: []
  schemi_preferiti: []
  output_preferiti: []
  ambiti_collegati: []
  dati_tipici: []
  domande_tipiche: []
  rischi: []
  regole: []
```

## Ambiti disponibili

- `lavoro` — Contratti, turni, buste paga, mansioni, ferie, permessi.
- `salute` — Benessere, sicurezza, limiti, stress, prevenzione.
- `finanza` — Soldi, budget, costi, stipendi, tasse, contributi.
- `web-design` — Siti, UI, UX, layout, frontend, grafica.
- `cucina` — Ricette, tecniche, menù, spesa, food cost.
- `documenti` — File, report, dossier, repository, istruzioni.
- `progettazione-framework` — Sistemi modulari, agenti, boot, routing, strutture.
- `automazione` — Workflow, procedure, trigger, task ripetibili.
- `ricerca` — Raccolta informazioni, fonti, verifica, confronto.
- `codice` — Sviluppo, debugging, architettura software, script.
- `grafica` — Identità visiva, impaginazione, composizione, comunicazione.
- `organizzazione-personale` — Pianificazione, priorità, routine, produttività.

## Intersezioni principali

```yaml
intersezioni:
  lavoro_finanza:
    usa: ["lavoro", "finanza"]
    esempio: "analisi busta paga"
  lavoro_salute:
    usa: ["lavoro", "salute"]
    esempio: "stress, malattia, carichi, sicurezza"
  web_design_grafica:
    usa: ["web-design", "grafica"]
    esempio: "landing page o identità visiva"
  cucina_finanza:
    usa: ["cucina", "finanza"]
    esempio: "food cost e spesa"
  documenti_framework:
    usa: ["documenti", "progettazione-framework"]
    esempio: "repository di istruzioni AI"
  codice_automazione:
    usa: ["codice", "automazione"]
    esempio: "script o workflow"
```
