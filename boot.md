# boot.md

Questo file avvia il Framework AI Modulare.

## Obiettivo

All'avvio il servizio AI deve:

1. riconoscere l'ambiente: ChatGPT, Claude AI, Gemini AI o altro;
2. ricostruire la struttura del repository;
3. controllare file e cartelle disponibili;
4. caricare i moduli base;
5. costruire una mappa interna;
6. attivare logica, funzioni, agenti, ambiti, schemi e output;
7. dichiarare limiti reali.

## Sequenza di caricamento

```yaml
boot_sequence:
  - README.md
  - LOGICA/logica.md
  - FUNZIONI/funzioni.md
  - FUNZIONI/funzioni-avvio.md
  - FUNZIONI/funzioni-routing.md
  - FUNZIONI/funzioni-agenti.md
  - FUNZIONI/funzioni-ambiti.md
  - FUNZIONI/funzioni-output.md
  - FUNZIONI/funzioni-memoria.md
  - AGENTI/agenti.md
  - AGENTI/ambiti.md
  - SCHEMI/schema-agenti.md
  - SCHEMI/schema-ambiti.md
  - SCHEMI/schema-funzioni.md
  - SCHEMI/schema-routing.md
  - SCHEMI/schema-output.md
  - OUTPUT/output-stringato.md
  - OUTPUT/output-report.md
  - OUTPUT/output-dossier.md
```

## Ricostruzione repository

Se l'AI può accedere ai file:

```yaml
azioni:
  - elenca_cartelle
  - elenca_file
  - rileva_file_nuovi
  - rileva_file_mancanti
  - crea_mappa_moduli
```

Se non può accedere ai file:

```yaml
azioni:
  - usa_struttura_dichiarata
  - segnala_limite_accesso
  - chiedi_file_solo_quando_necessario
```

## Adattamento ambiente

### ChatGPT
Interpretare agenti come ruoli operativi o GPT personalizzati se disponibili.

### Claude AI
Interpretare agenti come skill, procedure o istruzioni di progetto.

### Gemini AI
Interpretare agenti come Gem, helper o istruzioni personalizzate.

## Output conferma

```text
BOOT caricato.
Ambiente rilevato: [...]
Struttura framework: [...]
Moduli base: attivi
Agenti: disponibili
Ambiti: disponibili
Funzioni: reali/emulate secondo ambiente
Schemi: disponibili
Output: disponibili
Limiti: [...]
Framework pronto.
```
