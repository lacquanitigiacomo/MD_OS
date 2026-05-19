# schema-controllo-file.md

Questo schema definisce i metadati minimi da inserire e controllare nei file del framework.

Serve per mantenere tracciabilità, compatibilità, stato e qualità dei file `.md`, dei file di configurazione e dei file di sviluppo.

---

## Blocco obbligatorio di aggiornamento

Ogni file operativo del framework dovrebbe terminare con questo blocco:

```markdown
---

## Ultimo aggiornamento

- Data: YYYY-MM-DD
- Versione: "1.0"
- Autore: ""
- Tipo modifica: "creazione | aggiornamento | revisione | correzione | deprecazione"
- Stato: "attivo | sperimentale | deprecato | archiviato"
- Compatibilità verificata:
  - ChatGPT: "sì | no | parziale"
  - Claude AI: "sì | no | parziale"
  - Gemini AI: "sì | no | parziale"
- File correlati:
  - ""
- Note: ""
```

---

## Schema YAML equivalente

```yaml
controllo_file:
  data: "YYYY-MM-DD"
  versione: "1.0"
  autore: ""
  tipo_modifica: "creazione | aggiornamento | revisione | correzione | deprecazione"
  stato: "attivo | sperimentale | deprecato | archiviato"
  compatibilita_verificata:
    chatgpt: "sì | no | parziale"
    claude_ai: "sì | no | parziale"
    gemini_ai: "sì | no | parziale"
  file_correlati: []
  note: ""
```

---

## Regole di controllo

Un file è considerato completo quando contiene:

1. titolo chiaro;
2. scopo del file;
3. istruzioni operative o schema;
4. compatibilità quando rilevante;
5. limiti quando rilevante;
6. blocco `Ultimo aggiornamento` finale.

---

## Regole per file di programmazione e sviluppo

Per file tecnici, codice, configurazioni o procedure di sviluppo, aggiungere anche:

```yaml
sviluppo:
  linguaggio_o_formato: "markdown | yaml | json | python | javascript | html | css | altro"
  dipendenze: []
  input_attesi: []
  output_attesi: []
  rischi: []
  test_o_verifiche: []
  rollback: ""
```

---

## Uso nel framework

Gli agenti `revisore`, `architetto-framework`, `gestore-memoria` e `redattore-documentale` devono usare questo schema quando:

- creano nuovi file;
- revisionano file esistenti;
- aggiornano il framework;
- preparano patch;
- verificano compatibilità tra ChatGPT, Claude AI e Gemini AI.

---

## Ultimo aggiornamento

- Data: 2026-05-19
- Versione: "1.0"
- Autore: "ChatGPT"
- Tipo modifica: "creazione"
- Stato: "attivo"
- Compatibilità verificata:
  - ChatGPT: "sì"
  - Claude AI: "sì"
  - Gemini AI: "sì"
- File correlati:
  - "SCHEMI/schema-output.md"
  - "SCHEMI/schema-routing.md"
  - "FUNZIONI/funzioni-controllo.md"
- Note: "Schema creato per standardizzare aggiornamento e controllo dei file del framework."
