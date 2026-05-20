# Confini tra MD_OS e progetti esterni

MD_OS è il framework operativo generale.

MD_OS non deve contenere materiali, nomi, istruzioni operative, percorsi, riferimenti, dati o contenuti specifici di progetti esterni.

I progetti esterni, inclusi quelli conservati su Google Drive o altri archivi, devono restare separati dal repository MD_OS.

MD_OS può contenere solo:
- logiche generali;
- agenti riutilizzabili;
- funzioni astratte;
- procedure non legate a un singolo caso;
- soglie, schemi e formati output generalizzabili;
- regole di routing e sicurezza.

Se durante un progetto esterno emerge una nuova logica utile, questa può essere inserita in MD_OS solo dopo essere stata:
- astratta;
- depersonalizzata;
- privata di riferimenti a clienti, cartelle, file o casi specifici;
- collocata nel modulo corretto del framework.

## Regola operativa

Prima di aggiornare MD_OS sulla base di un progetto esterno, verificare che il contenuto proposto sia una capacità generale del framework e non materiale del progetto.

## Esito atteso

Il repository MD_OS deve restare pulito, modulare e riutilizzabile.

I materiali dei progetti devono restare nei rispettivi archivi esterni.
