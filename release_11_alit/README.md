# MD_OS Release 11 — ALIT Investigative Intelligence Kernel

## Scopo
Plugin dinamico per ANALISI LAVORO. Non modifica il nucleo congelato di MD_OS. Aggiunge un layer operativo per audit investigativo multidisciplinare 2022-2026 su buste paga, orari, mansioni, salute, sicurezza, diritti e prove documentali.

## Regole madri
1. Ogni analisi copre sempre 2022-2026.
2. Ogni anno ha sempre 12 mesi in tabella, anche se il dato manca.
3. Ogni dato viene classificato: D0 documentale, D1 ricostruito da pattern forte, D2 simulato plausibile, D3 ipotesi debole, ND non disponibile.
4. I dati simulati non sono prove: servono a generare scenari, piste e domande tecniche.
5. Nessuna conclusione senza fonte, formula, classe dato e confidenza.

## Codifica turni
| Codice | Significato esposto | Traduzione reale |
|---|---|---|
| 1 | turno giorno | stesso giorno 08:00-16:00 |
| 2 | turno sera | stesso giorno 16:00-24:00 |
| 3 | notte agganciata al giorno esposto | giorno successivo 00:00-08:00 |
| R | riposo nominale | verificare smonto da 3 del giorno precedente |
| F | ferie nominali | verificare smonto/lavoro da 3 del giorno precedente |

## Regola SHIFT-3-DAY+1
Il codice 3 esposto su data D genera lavoro reale su data D+1 dalle 00:00 alle 08:00. Questa regola si applica a tutti gli anni 2022-2026 e influenza notturni, festivi, domeniche, smonti, ferie, ROL, riposi, cedolino e timeline salute.

## Esempio
Calendario esposto:
- lun = 2
- mar = 2
- mer = 3
- gio = 3
- ven = R

Calendario reale:
- lun 16:00-24:00
- mar 16:00-24:00
- gio 00:00-08:00 derivato da mer=3
- ven 00:00-08:00 derivato da gio=3 + smonto/R nominale

## Agenti ALIT
Vedi `AGENTS.md`.

## Workflow
Vedi `WORKFLOW.md`.

## Schemi dati
Vedi `SCHEMAS.md`.
