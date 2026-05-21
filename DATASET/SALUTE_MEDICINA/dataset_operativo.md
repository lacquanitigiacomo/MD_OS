---
id_dataset: dataset_salute_medicina
ambito: SALUTE_MEDICINA
tipo: operativo
stato: attivo
versione: 1.0.0
---

# Dataset operativo — Salute Medicina

## Scopo
Fornire contesto rapido di area per ridurre ricerche e token.

## Sottoaree
- medicina_generale
- nutrizione
- psicologia
- prevenzione
- ergonomia
- salute_lavoro

## Matrice trigger → azione
| Trigger | Azione |
|---|---|
| richiesta generale | leggere ambito |
| richiesta specialistica | selezionare agente |
| output richiesto | applicare modello output |

## Limiti
Dataset iniziale da raffinare con uso reale e patch.
