# ROUTING: Ambiti Canonici MD_OS

## Scopo

Definire gli ambiti canonici da usare nel repository MD_OS e prevenire la creazione di cartelle sinonime.

---

## Ambiti attivi

| Ambito canonico | Uso |
|---|---|
| `DESIGN_COMUNICAZIONE` | grafica, UI, UX, brand, comunicazione visiva |
| `DOCUMENTI_DATI_REPORT` | estrazione dati, revisione documentale, reportistica |
| `ECONOMIA_FINANZA_REVISIONE` | finanza, cedolini, fiscalità, revisione, lavoro amministrativo |
| `LEGALE_NORMATIVO` | contratti, compliance, privacy, norme |
| `SALUTE_BENESSERE` | salute documentale, benessere, dati sanitari non diagnostici |
| `TECNOLOGIA_SVILUPPO` | software, web, dati, devops, cloud, sicurezza applicativa |

---

## Ambiti deprecati

Non usare:

| Alias deprecato | Usare invece |
|---|---|
| `TECNOLOGIA` | `TECNOLOGIA_SVILUPPO` |
| `SVILUPPO` | `TECNOLOGIA_SVILUPPO` |
| `WEB` | `TECNOLOGIA_SVILUPPO` oppure `DESIGN_COMUNICAZIONE` secondo il caso |
| `FINANZA` | `ECONOMIA_FINANZA_REVISIONE` |
| `ECONOMIA` | `ECONOMIA_FINANZA_REVISIONE` |
| `LAVORO` | `ECONOMIA_FINANZA_REVISIONE` oppure nuovo ambito approvato |
| `LEGAL` | `LEGALE_NORMATIVO` |
| `DESIGN` | `DESIGN_COMUNICAZIONE` |
| `DATI` | `DOCUMENTI_DATI_REPORT` o `TECNOLOGIA_SVILUPPO` secondo il caso |

---

## Regola decisionale

Prima di creare un nuovo ambito:

1. verificare se la richiesta rientra in un ambito attivo;
2. se sì, usare l'ambito attivo;
3. se no, proporre un nuovo ambito all'utente;
4. non creare cartelle provvisorie o sinonime.

---

## Ambiti candidati

Questi ambiti sono candidati ma non attivi finché non approvati:

```txt
LAVORO_VERTENZA_SINDACALE
DATI_ANALYTICS_AI
PRODOTTO_STRATEGIA
AI_AUTOMAZIONE
INFRASTRUTTURE_DIGITALI
```
