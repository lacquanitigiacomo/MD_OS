---
id_dataset: dataset_casa_vita_pratica
ambito: CASA_VITA_PRATICA
tipo: operativo
stato: attivo
versione: 1.0.0
---

# Dataset operativo — Casa Vita Pratica

## Scopo
Fornire contesto rapido di area per ridurre ricerche e token.

## Sottoaree
- cucina
- manutenzione_domestica
- organizzazione_casa
- acquisti
- viaggi
- auto_moto
- giardinaggio

## Matrice trigger → azione
| Trigger | Azione |
|---|---|
| richiesta generale | leggere ambito |
| richiesta specialistica | selezionare agente |
| output richiesto | applicare modello output |

## Limiti
Dataset iniziale da raffinare con uso reale e patch.
