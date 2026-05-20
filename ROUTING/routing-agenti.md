# ROUTING: Attivazione Agenti

## Criterio generale

L'agente viene attivato quando la richiesta dell'utente contiene dati, obiettivi o documenti coerenti con il suo ambito.

Prima di attivare o creare agenti, consultare:

```txt
LOGIC/schema-canonico-repository.md
ROUTING/routing-ambiti.md
AGENTI/REGISTRO-AGENTI.md
```

---

## Regola anti-cartelle-duplicate

Non creare nuovi ambiti o cartelle se esiste già un ambito canonico adatto.

Esempio:

```txt
NO: TECNOLOGIA
SI: TECNOLOGIA_SVILUPPO
```

---

## Multi-agente

Se una richiesta coinvolge più ambiti, attivare:

1. agente principale;
2. agenti secondari di supporto;
3. eventuale agente di output/report;
4. eventuale agente di controllo prudenza/sicurezza.

---

## Priorità di routing

1. Sicurezza, privacy e limiti professionali.
2. Comprensione del dominio.
3. Estrazione dei dati.
4. Verifica e controllo.
5. Analisi specialistica.
6. Output tabellare o report finale.

---

## Esempi di routing

| Richiesta | Ambito | Agenti tipici |
|---|---|---|
| Revisione codice | `TECNOLOGIA_SVILUPPO` | code-reviewer, senior-web-developer, security-engineer |
| Audit web app | `TECNOLOGIA_SVILUPPO` | senior-web-developer, performance-engineer, security-engineer |
| Analisi buste paga | `ECONOMIA_FINANZA_REVISIONE` | revisore-cedolini, consulente-lavoro, commercialista |
| Revisione contratto | `LEGALE_NORMATIVO` | analista-contratti, compliance |
| Dossier documentale | `DOCUMENTI_DATI_REPORT` | estrattore-dati, revisore-documentale, redattore-report |
| Analisi UI/UX | `DESIGN_COMUNICAZIONE` | web-designer, ux-reviewer, grafico |

---

## Regola di aggiornamento

Ogni volta che viene aggiunto un nuovo agente:

1. aggiornare `AGENTI/REGISTRO-AGENTI.md`;
2. verificare che i moduli richiamati esistano;
3. aggiornare il routing se l'agente introduce un caso nuovo;
4. mantenere path canonici.
