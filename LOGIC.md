# DIRETTIVA DI SICUREZZA: ZERO-REFACTOR & PRESERVAZIONE STRUTTURALE

[MANDATORY / TASSATIVO] Questo modulo estende le difese del file LOGIC.md. Vieta al sistema di eseguire refactoring continui, riscritture arbitrarie o modifiche non richieste al codice precedentemente generato e validato, garantendo all'Utente il controllo assoluto sulla persistenza e l'integrità dei dati.

---

## 1. REGOLA OPERATIVA (Markdown Discorsivo)

### 1.1 Ispezione dell'Ultimo Output Validato
Prima di generare qualsiasi variante o aggiornamento di un codice o di una configurazione, il sistema ha l'obbligo di analizzare l'esatta struttura dell'ultimo blocco di codice emesso nella sessione. Quella versione costituisce la "Baseline Immutabile".

### 1.2 Principio di Conservazione e Incremento
Il codice che funziona o che è stato approvato non deve essere riscritto, ottimizzato secondo criteri soggettivi dell'AI o privato di commenti e funzioni precedentemente inseriti. Il sistema deve limitarsi a mantenere intatta la struttura esistente e aggiungere le nuove implementazioni richieste in coda o nei punti logici esatti.

### 1.3 Evidenziazione Chirurgica delle Modifiche
Se una modifica strutturale o una correzione all'interno del blocco esistente è strettamente necessaria, il sistema non deve integrarla silenziosamente. Deve:
1. Isolare la porzione di codice interessata.
2. Esplicitare la proposta di modifica in un blocco dedicato.
3. Spiegare il motivo tecnico dell'intervento prima di procedere.

### 1.4 Obbligo di Codice Totale (End-to-End)
È tassativamente vietato troncare il codice, utilizzare placeholder come `# ... resto del codice invariato ...` o omettere parti della struttura. Ogni output finale deve contenere il codice completo dalla riga 1 all'ultima riga, garantendo che un'operazione di copia-incolla da parte dell'Utente non distrugga le funzioni precedenti.

---

## 2. ARCHITETTURA LOGICA E FUNZIONI DI CONTROLLO (Python Execution Simulation)

Il sistema deve simulare internamente questa esatta logica di controllo sequenziale prima di rispondere a una richiesta di modifica o aggiornamento del codice:

```python
def genera_output_codice_protetto(codice_precedente, richiesta_utente):
    """
    Garantisce la stabilità del codice ed evita refactoring continui.
    Forza la produzione di file completi end-to-end senza perdite di dati.
    """
    # 1. CONTROLLO ULTIMO CODICE GENERATO (BASELINE)
    assert codice_precedente is not None, "Errore: Nessun codice rilevato nel contesto di sessione."
    
    struttura_invariata = estrai_blocchi_funzionali(codice_precedente)
    proposta_modifica = []
    nuovo_codice_totale = []

    # 2. VALUTAZIONE CHIRURGICA DELLE MODIFICHE
    if richiede_alterazione_core(richiesta_utente):
        # Isola solo il segmento da modificare senza toccare il resto
        segmento_target = individua_segmento_critico(codice_precedente, richiesta_utente)
        proposta_modifica.append({
            "STATO_PRECEDENTE": segmento_target["raw"],
            "PROPOSTA_AGGIORNAMENTO": calcola_estensione_funzionale(richiesta_utente),
            "MOTIVAZIONE": "Iniezione richiesta per ottimizzazione o integrazione logica."
        })
    
    # 3. COMPILAZIONE INCREMENTALE (TENGO IL BUONO E AGGIUNGO)
    for blocco in struttura_invariata:
        if blocco["id"] == segmento_target["id"]:
            nuovo_codice_totale.append(proposta_modifica["PROPOSTA_AGGIORNAMENTO"])
        else:
            nuovo_codice_totale.append(blocco["raw"])
            
    # Se la richiesta prevede nuove funzioni stand-alone, le appende in coda
    if richiede_nuove_funzioni(richiesta_utente):
        nuovo_codice_totale.append(genera_nuovo_modulo_isolato(richiesta_utente))

    # 4. OUTPUT TOTALE DEL FILE DALL'INIZIO ALLA FINE (NO PLACEHOLDERS)
    codice_finale_end_to_end = assembla_blocchi_finali(nuovo_codice_totale)
    
    return renderizza_risposta_strutturata(
        segnalazione_modifiche=proposta_modifica,
        codice_completo=codice_finale_end_to_end
    )
    