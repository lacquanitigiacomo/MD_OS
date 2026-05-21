# README AGENTI — MD_OS v8

## Scopo
La cartella `AGENTI/` è il modulo auto-descrittivo di competenze. Definisce tassonomia, schema agente, schema ambito, discovery, selezione e caricamento progressivo.

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

## Funzione DISCOVERY_AGENTI
1. Leggere `TASSONOMIA/albero_ambiti.yaml`.
2. Identificare macro-area, sottoarea e modalità trasversale dalla richiesta.
3. Leggere gli ambiti pertinenti.
4. Scansionare `AGENTI-SINGOLI/<MACRO_AREA>/`.
5. Leggere frontmatter e sezioni Trigger/Tag/Output degli agenti.
6. Selezionare agenti con punteggio maggiore.
7. Caricare integralmente solo agenti selezionati.

## Algoritmo di selezione
```txt
punteggio = trigger_match*3 + tag_match*2 + sottoarea_match*4 + output_match*2 + modalita_match*5 - peso_token_penalty
```

## Regola token
Non leggere tutti gli agenti. Leggere tutto il file agente solo se selezionato come principale o supporto essenziale.

## Regola miglioramento
Ogni nuova logica stabile emersa dall'uso deve produrre una patch a: tassonomia, agente, ambito o dataset.
