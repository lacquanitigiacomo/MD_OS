# Routing comunicazione output

Questo modulo definisce quando attivare il reparto logico COMUNICAZIONE_OUTPUT.

## Attivazione obbligatoria

Attivare COMUNICAZIONE_OUTPUT quando la risposta richiesta o prodotta:

- supera una struttura semplice;
- contiene più di una sezione;
- contiene tabelle;
- contiene dati sensibili o tecnici;
- contiene analisi documentale;
- contiene conclusioni, limiti o azioni consigliate;
- deve essere usata come report, dossier, sintesi, lettera o documento operativo;
- deve adattare il registro linguistico al destinatario.

## Attivazione consigliata

Attivare COMUNICAZIONE_OUTPUT quando:

- l'utente segnala che l'output è poco chiaro;
- l'utente chiede maggiore leggibilità;
- l'output rischia di essere troppo tecnico;
- l'output contiene molte fonti;
- l'output deve distinguere dati certi, ipotesi e limiti;
- l'output deve essere archiviabile o riutilizzabile.

## Routing agenti

| Esigenza | Agente consigliato |
|---|---|
| Sintesi e report | `redattore-report` |
| Controllo struttura documentale | `revisore-documentale` |
| Registro linguistico e tono | `revisore-linguistico` |
| Layout, impaginazione, gerarchia visiva | `grafico` |
| Esperienza utente e leggibilità dell'interazione | `ux-reviewer` |
| Output web o interfacce | `web-designer` |

## Ordine consigliato

1. Analisi tecnica.
2. Revisione documentale.
3. Revisione linguistica.
4. Ottimizzazione grafica o UX se serve.
5. Output finale.

## Regola anti-rumore

Non attivare tutti gli agenti comunicativi per ogni risposta.

Caricare solo quelli pertinenti allo scopo dell'output.
