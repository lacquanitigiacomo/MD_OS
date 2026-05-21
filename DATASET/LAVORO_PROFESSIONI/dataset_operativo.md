---
id_dataset: dataset_lavoro_professioni
ambito: LAVORO_PROFESSIONI
tipo: operativo
stato: attivo
versione: 1.0.0
---

# Dataset operativo — Lavoro Professioni

## Scopo
Fornire contesto rapido di area per ridurre ricerche e token.

## Sottoaree
- buste_paga_payroll
- diritto_lavoro
- ccnl_contratti
- orari_turni
- salute_sicurezza_lavoro
- mansioni_inquadramento
- hr_welfare
- sindacale
- carriera

## Matrice trigger → azione
| Trigger | Azione |
|---|---|
| richiesta generale | leggere ambito |
| richiesta specialistica | selezionare agente |
| output richiesto | applicare modello output |

## Limiti
Dataset iniziale da raffinare con uso reale e patch.
