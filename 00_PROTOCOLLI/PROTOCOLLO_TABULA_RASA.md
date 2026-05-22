# PROTOCOLLO TABULA RASA — MD_OS

## Scopo

Il Protocollo Tabula Rasa definisce la procedura standard per sostituire completamente MD_OS con una nuova generazione del sistema.

---

## Regola Centrale

Quando viene invocato `PROTOCOLLO TABULA RASA`, il sistema deve:

1. generare un archivio `.zip` scaricabile con la nuova versione completa;
2. produrre una mappa dei file contenuti nello zip;
3. creare, se possibile, un ramo di sicurezza o un riferimento di backup;
4. cancellare dal repository tutti i file della versione precedente;
5. caricare la nuova versione pulita;
6. verificare che il `README.md` descriva solo la nuova architettura;
7. dichiarare eventuali file non cancellati per limiti tecnici o permessi.

---

## Procedura

```text
CREA ZIP NUOVA VERSIONE
↓
VERIFICA STRUTTURA ZIP
↓
LEGGI FILE ESISTENTI DEL REPOSITORY
↓
CANCELLA FILE VECCHI
↓
CARICA FILE NUOVI
↓
VERIFICA README E MANIFESTO
↓
RESTITUISCI REPORT
```

---

## Vincoli

- Non fingere una cancellazione completa se non e stata eseguita.
- Dichiarare sempre quali file sono stati cancellati.
- Dichiarare sempre quali file non e stato possibile rilevare o rimuovere.
- Non lasciare vecchie architetture attive nella radice.
- Conservare lo zip come pacchetto scaricabile per l'utente.

---

## Struttura Minima della Nuova Versione

```text
README.md
00_AVVIO/
01_MANIFESTO/
02_CERVELLO/
03_MEMORIA/
04_PROFESSIONI/
05_PROFILI/
06_SKILL/
07_MATRICI/
08_DATASET/
09_SQUADRE/
10_OFFICINA/
11_VERIFICA/
12_APPRENDIMENTO/
```

---

## Output Finale Obbligatorio

Il report finale deve contenere:

| Campo | Obbligo |
|---|---|
| Zip generato | link scaricabile |
| File cancellati | elenco |
| File caricati | elenco o conteggio |
| File non gestiti | elenco |
| Commit finale | hash |
| Stato | completo / parziale |
