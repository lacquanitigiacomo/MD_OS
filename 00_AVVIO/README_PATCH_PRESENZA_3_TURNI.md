# Patch MD_OS — Presenza 3 Turni

## Cosa aggiunge

Aggiunge il file:

```text
03_PROFESSIONI/PROTOCOLLO_PRESENZA_3_TURNI.md
```

## Perche serve

Permette a MD_OS di partire con tutti gli agenti presenti, senza escludere troppo presto componenti che potrebbero diventare utili.

Dopo 3 coppie domanda/risposta, gli agenti fuori contesto si ritirano ma restano richiamabili.

## Come applicarla

Copia le cartelle dello ZIP nella root del repository `MD_OS`.

Poi esegui:

```bash
git add 03_PROFESSIONI/PROTOCOLLO_PRESENZA_3_TURNI.md 00_AVVIO/README_PATCH_PRESENZA_3_TURNI.md
git commit -m "Add three-turn agent presence protocol"
git push
```
