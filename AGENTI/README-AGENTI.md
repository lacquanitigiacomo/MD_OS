# README AGENTI — MD_OS

## Scopo
La cartella `AGENTI/` è un modulo auto-descrittivo. Definisce tassonomia, schema agente, schema ambito e funzioni di caricamento.

## Struttura
```txt
AGENTI/
├── README-AGENTI.md
├── INDICE-AGENTI.md
├── TASSONOMIA/
├── AMBITI/
└── AGENTI-SINGOLI/
```

## Schema agente singolo
Ogni agente è un singolo file `.md` con frontmatter YAML e sezioni operative:
1. Nome e professione
2. Identità operativa
3. Ambito principale
4. Ambiti secondari
5. Scopo
6. Quando attivarlo
7. Quando non attivarlo
8. Skills
9. Funzioni specifiche
10. Logiche specifiche
11. Schemi specifici
12. Matrici operative
13. Algoritmi operativi
14. Dataset interno
15. Tag operativi
16. Checklist operative
17. Output specifici
18. Fonti di apprendimento specifiche
19. Dataset collegati
20. Agenti collegati
21. Regole di caricamento
22. Modalità di interazione
23. Criteri di qualità
24. Criteri di rischio
25. Limiti
26. Esempi di attivazione
27. Patch e miglioramento continuo
28. Metriche di efficacia

## Schema ambito
Ogni ambito dichiara perimetro, sottoaree, trigger, agenti preferiti, dataset, funzioni comuni, logiche, schemi, output, metriche e regole di discovery.

## Funzione DISCOVERY_AGENTI
1. Leggere `TASSONOMIA/albero_ambiti.yaml`.
2. Identificare macro-area e sottoarea dalla richiesta.
3. Leggere gli ambiti pertinenti.
4. Scansionare `AGENTI-SINGOLI/<MACRO_AREA>/`.
5. Leggere frontmatter e sezioni Trigger/Tag/Output degli agenti.
6. Selezionare agenti con punteggio maggiore.
7. Caricare integralmente solo agenti selezionati.

## Algoritmo di selezione
Punteggio = trigger_match*3 + tag_match*2 + sottoarea_match*4 + output_match*2 - peso_token_penalty.

## Regola token
Non leggere tutti gli agenti. Leggere tutto il file agente solo se selezionato.
