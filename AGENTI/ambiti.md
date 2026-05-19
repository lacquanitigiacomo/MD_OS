# ambiti.md

Questo file contiene gli ambiti di riferimento e le intersezioni usate dagli agenti.

Gli ambiti servono a orientare il framework, selezionare agenti, scegliere funzioni, applicare schemi e produrre output più coerenti.

---

## Definizione

Un ambito è un dominio contestuale.

Serve agli agenti per:

- capire il contesto;
- orientare le decisioni;
- selezionare funzioni;
- scegliere schemi;
- evitare risposte generiche;
- riconoscere dati rilevanti;
- riconoscere rischi;
- collegare più domini tra loro;
- stabilire il livello di cautela necessario.

---

## Schema ambito

```yaml
ambito:
  nome: ""
  versione: "1.0"
  categoria: ""
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
  livello_cautela: "basso | medio | alto"
```

---

## Categorie ambiti

```yaml
categorie_ambiti:
  persona:
    scopo: "gestire vita personale, salute, organizzazione, abitudini"
  lavoro_e_denaro:
    scopo: "gestire lavoro, contratti, economia, documenti, fiscalità"
  creazione_digitale:
    scopo: "gestire web, codice, grafica, contenuti e design"
  conoscenza:
    scopo: "gestire ricerca, studio, apprendimento e analisi"
  sistemi:
    scopo: "gestire framework, automazioni, processi, architetture"
  produzione_output:
    scopo: "gestire documenti, report, dossier, presentazioni e consegne"
```

---

## Ambiti disponibili

### Persona

- `salute` — Benessere, sicurezza, limiti, stress, prevenzione, condizioni fisiche e psicologiche.
- `organizzazione-personale` — Pianificazione, priorità, routine, produttività, gestione tempo, abitudini.
- `cucina` — Ricette, tecniche, menù, spesa, food cost, organizzazione pasti.
- `casa` — Manutenzione domestica, spazi, pulizia, riparazioni, organizzazione ambienti.
- `relazioni-comunicazione` — Messaggi, tono, negoziazione, chiarezza, conflitti, comunicazioni personali.
- `formazione-personale` — Studio, apprendimento, competenze, percorsi, esercizi, crescita personale.

### Lavoro e denaro

- `lavoro` — Contratti, turni, buste paga, mansioni, ferie, permessi, comunicazioni aziendali.
- `finanza` — Soldi, budget, costi, stipendi, tasse, contributi, risparmio, previsioni economiche.
- `fisco` — Tasse, dichiarazioni, detrazioni, documenti fiscali, scadenze, verifiche preliminari.
- `burocrazia` — Moduli, richieste, pratiche, enti, documenti amministrativi, procedure.
- `diritti-doveri` — Regole, obblighi, tutele, responsabilità, vincoli, verifiche normative non definitive.
- `carriera` — CV, portfolio, colloqui, competenze, crescita professionale, posizionamento.

### Creazione digitale

- `web-design` — Siti, UI, UX, layout, frontend, responsive design, esperienza utente.
- `codice` — Sviluppo, debugging, architettura software, script, automazioni, integrazioni.
- `grafica` — Identità visiva, impaginazione, composizione, comunicazione, materiali visuali.
- `contenuti` — Testi, copywriting, articoli, storytelling, social, contenuti editoriali.
- `multimedia` — Immagini, video, audio, formati, storyboard, materiali creativi.
- `accessibilita-usabilita` — Accessibilità, leggibilità, navigazione, inclusione, test utente.

### Conoscenza

- `ricerca` — Raccolta informazioni, fonti, verifica, confronto, sintesi, aggiornamento dati.
- `analisi-dati` — Tabelle, CSV, numeri, pattern, controlli, estrazioni, confronto dataset.
- `studio` — Materie, appunti, mappe, ripasso, spiegazioni, esercizi, programmi di studio.
- `sintesi-conoscenza` — Riassunti, schemi, mappe concettuali, estrazione punti chiave.
- `decisioni` — Valutazione opzioni, pro/contro, scenari, priorità, scelta ragionata.
- `verifica-fatti` — Controllo coerenza, fact-checking, fonti, date, aggiornamenti.

### Sistemi e framework

- `progettazione-framework` — Sistemi modulari, agenti, boot, routing, strutture, repository.
- `automazione` — Workflow, procedure, trigger, task ripetibili, riduzione lavoro manuale.
- `architettura-informativa` — Organizzazione cartelle, file, naming, tassonomie, indici.
- `memoria-contesto` — Patch, changelog, stato progetto, continuità, note di sessione.
- `compatibilita-ai` — Adattamento tra ChatGPT, Claude AI, Gemini AI, limiti e mapping concettuale.
- `qualita-controllo` — Revisione, test, completezza, coerenza, standard, checklist.

### Produzione output

- `documenti` — File, report, dossier, repository, istruzioni, README, documentazione.
- `presentazioni` — Slide, scalette, pitch, struttura narrativa, materiale sintetico.
- `reportistica` — Report, analisi, riepiloghi, stati avanzamento, output manageriali.
- `dossier` — Raccolte complete, analisi multi-file, documenti archiviabili, fascicoli.
- `json-yaml-dati` — Payload, configurazioni, manifest, strutture dati, export leggibile da macchina.
- `codice-output` — File tecnici, snippet, componenti, script, blocchi copiabili.

---

## Caratteristiche operative degli ambiti

```yaml
caratteristiche_ambiti:
  salute:
    livello_cautela: "alto"
    agenti_preferiti: ["analista-salute", "ricercatore", "revisore"]
    output_preferiti: ["stringato", "report"]
    rischi: ["diagnosi", "urgenze sottovalutate", "consulenza medica impropria"]

  lavoro:
    livello_cautela: "medio-alto"
    agenti_preferiti: ["analista-lavoro", "analista-finanziario", "revisore", "redattore-documentale"]
    output_preferiti: ["dossier", "report", "checklist"]
    rischi: ["consulenza legale definitiva", "dati contrattuali incompleti", "confusione tra periodi"]

  finanza:
    livello_cautela: "medio-alto"
    agenti_preferiti: ["analista-finanziario", "revisore"]
    output_preferiti: ["report", "json", "checklist"]
    rischi: ["calcoli incompleti", "stime spacciate per certezze", "mancanza periodo"]

  codice:
    livello_cautela: "medio"
    agenti_preferiti: ["sviluppatore-web", "costruttore", "revisore"]
    output_preferiti: ["codice-web", "report", "json"]
    rischi: ["codice non testato", "dipendenze non dichiarate", "sicurezza ignorata"]

  progettazione_framework:
    livello_cautela: "medio"
    agenti_preferiti: ["architetto-framework", "orchestratore", "traduttore-compatibilita", "gestore-memoria"]
    output_preferiti: ["dossier", "report", "json"]
    rischi: ["astrazione eccessiva", "moduli duplicati", "istruzioni non applicabili"]

  documenti:
    livello_cautela: "medio"
    agenti_preferiti: ["redattore-documentale", "revisore", "specialista-output"]
    output_preferiti: ["dossier", "report", "checklist"]
    rischi: ["file non tracciati", "versioni confuse", "fonti non citate"]
```

---

## Intersezioni principali

```yaml
intersezioni:
  lavoro_finanza:
    usa: ["lavoro", "finanza"]
    esempio: "analisi busta paga, stipendio, trattenute, contributi"
    agenti: ["analista-lavoro", "analista-finanziario", "revisore"]
    output: "dossier"

  lavoro_salute:
    usa: ["lavoro", "salute"]
    esempio: "stress, malattia, carichi, sicurezza, idoneità"
    agenti: ["analista-lavoro", "analista-salute", "revisore"]
    output: "report"

  lavoro_documenti:
    usa: ["lavoro", "documenti"]
    esempio: "contratti, comunicazioni, report, archivio lavorativo"
    agenti: ["analista-lavoro", "redattore-documentale", "revisore"]
    output: "dossier"

  web_design_grafica:
    usa: ["web-design", "grafica"]
    esempio: "landing page, identità visiva, UI"
    agenti: ["designer-ux-ui", "sviluppatore-web", "revisore"]
    output: "codice-web"

  web_design_accessibilita:
    usa: ["web-design", "accessibilita-usabilita"]
    esempio: "UI leggibile, responsive, inclusiva"
    agenti: ["designer-ux-ui", "revisore"]
    output: "report"

  cucina_finanza:
    usa: ["cucina", "finanza"]
    esempio: "food cost, spesa, prezzo porzione"
    agenti: ["cuoco-strategico", "analista-finanziario"]
    output: "report"

  documenti_framework:
    usa: ["documenti", "progettazione-framework"]
    esempio: "repository di istruzioni AI, README, boot, schemi"
    agenti: ["architetto-framework", "redattore-documentale", "revisore"]
    output: "dossier"

  codice_automazione:
    usa: ["codice", "automazione"]
    esempio: "script, workflow, parser, generatori file"
    agenti: ["costruttore", "sviluppatore-web", "revisore"]
    output: "codice-web"

  ricerca_verifica_fatti:
    usa: ["ricerca", "verifica-fatti"]
    esempio: "controllo informazioni aggiornate, fonti, date"
    agenti: ["ricercatore", "revisore"]
    output: "report"

  documenti_reportistica:
    usa: ["documenti", "reportistica", "dossier"]
    esempio: "analisi multi-file, dossier finale, archivio"
    agenti: ["redattore-documentale", "specialista-output", "revisore"]
    output: "dossier"
```

---

## Regole di selezione ambito

1. Se la richiesta riguarda dati personali, salute, lavoro, finanza o norme, usare cautela alta o medio-alta.
2. Se la richiesta riguarda file, cartelle, repository o documenti, attivare `documenti` e spesso `architettura-informativa`.
3. Se la richiesta riguarda AI, agenti, boot, moduli o GitHub, attivare `progettazione-framework` e `compatibilita-ai`.
4. Se la richiesta riguarda output finale, attivare anche `reportistica`, `dossier`, `json-yaml-dati` o `codice-output`.
5. Se la richiesta contiene più domini, dichiarare ambito principale e ambiti secondari.
6. Se l'ambito è incerto, usare `analista` e `orchestratore` per classificare prima di procedere.

---

## Ultimo aggiornamento

- Data: 2026-05-19
- Versione: "1.1"
- Autore: "ChatGPT"
- Tipo modifica: "aggiornamento"
- Stato: "attivo"
- Compatibilità verificata:
  - ChatGPT: "sì"
  - Claude AI: "sì"
  - Gemini AI: "sì"
- File correlati:
  - "AGENTI/agenti.md"
  - "SCHEMI/schema-ambiti.md"
  - "SCHEMI/schema-routing.md"
  - "SCHEMI/schema-controllo-file.md"
- Note: "Espansi ambiti disponibili, categorie, caratteristiche operative e intersezioni."
