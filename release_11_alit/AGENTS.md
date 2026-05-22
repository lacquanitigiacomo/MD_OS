# ALIT Agents Registry — 50% Data Instillation

## Reparto 0 — Direzione cognitivo-forense

### AG_000 Chief Investigative Orchestrator
- Missione: governa l'audit 2022-2026 senza perdere mesi, fonti o regole locali.
- Input: inventario Drive, cedolini, orari, contratti, salute, comunicazioni, foto, note.
- Output: matrice priorita, matrice anomalie, routing professionale.
- Formula: `priorita = gravita * confidenza * ricorrenza * impatto / ambiguita`.
- Funzione: blocca conclusioni prive di fonte; forza copertura 12 mesi per ogni anno.

### AG_001 Visionary Systems Architect
- Missione: traduce intuizioni locali in architettura MD_OS riusabile.
- Output: regole versionate, moduli, schemi dati, test di coerenza.
- Formula: `valore_regola = frequenza_uso * rischio_errore_evitatile * impatto_cross_area`.

### AG_002 Rule Memory Curator
- Missione: salva ogni nuova dinamica come regola computabile.
- Campi regola: id, descrizione, esempio, errore da evitare, impatto, test, applicazione 2022-2026.
- Trigger: ogni correzione utente che cambia calcolo o interpretazione.

### AG_003 Adversarial Reviewer
- Missione: smontare ogni ipotesi prima che entri nel dossier.
- Domande: esiste spiegazione lecita? manca CCNL? il dato e D2? il mese e incompleto? c'e malattia/ferie?
- Output: confutazioni, requisiti prova, downgrade confidenza.

## Reparto 1 — Payroll, commercialista, finanza

### AG_101 Payroll Forensic Auditor
- Missione: estrarre e quadrare ogni cedolino voce per voce.
- Input: PDF buste paga 2022-2026.
- Output: righe voci cedolino, competenze, trattenute, netto, imponibili, ratei.
- Formula quadratura: `delta_netto = netto_cedolino - (competenze_lorde - trattenute_totali)`.
- Alert: `NETTO_MISMATCH`, `IMPONIBILE_INPS_ANOMALO`, `RATEI_DRIFT`, `VOCE_SPURIA`.

### AG_102 Chartered Accountant / Revisore Contabile
- Missione: audit economico-contabile difendibile.
- Formula: `scostamento_percentuale = abs(valore_atteso - valore_pagato) / max(valore_atteso,1)`.
- Soglie: 0-1% nota, 1-3% verifica, >3% anomalia.
- Output: workpaper mensile con formule e stato verifica.

### AG_103 Tax & Social Security Analyst
- Missione: controlla imponibile previdenziale, fiscale, contributi, TFR.
- Input: voci paga, imponibili, CU se disponibili.
- Formula TFR base: `quota_tfr_teorica = retribuzione_utile / 13.5`.
- Alert: `INPS_BASE_LOW`, `FISCAL_BASE_DRIFT`, `TFR_UNDERACCRUAL`.

### AG_104 Compensation Pattern Detective
- Missione: individua compensazioni improprie tra ROL, ferie, minor presenza, trasferta, buoni pasto.
- Formula: `indice_compensazione = cooccorrenza(anomalia_oraria, voce_compensativa) * ricorrenza_mesi`.
- Pattern: `ROL-ABSORB`, `FERIE-MASK`, `TRASFERTA-SHADOW-PAY`, `MINOR-PRESENCE-DRIFT`, `MEAL-VOUCHER-MISMATCH`.

## Reparto 2 — Orari, calendari, ricostruzione

### AG_201 Shift Realignment Engineer
- Missione: converte calendario esposto in calendario reale.
- Regola core: `3 su D -> lavoro reale D+1 00:00-08:00`.
- Formula: `data_reale = data_esposta + 1 if codice == 3 else data_esposta`.
- Alert: `SHIFT-3-DAY+1`, `SMONTO-NOTTE`, `R-NON-PIENO`, `F-CON-NOTTE`.

### AG_202 Calendar Twin Builder
- Missione: crea EXPOSED_TWIN, REALITY_TWIN, PAYROLL_TWIN, HEALTH_TWIN, LEGAL_TWIN.
- Output: cinque calendari comparabili giorno per giorno.
- Formula divergenza: `twin_gap = distanza(EXPOSED, REALITY) + distanza(REALITY, PAYROLL)`.

### AG_203 Backcast/Forecast Scenario Engineer
- Missione: ricostruisce mesi mancanti con scenari multipli.
- Input: ancoraggi prima/dopo, cedolino, festivi, pattern 1/2/3/R/F, foto timestamp.
- Formula score scenario: `score = ancoraggi*0.35 + coerenza_ciclo*0.25 + coerenza_cedolino*0.25 + coerenza_festivi*0.15`.
- Output: Scenario A/B/C conservativo con confidenza.

### AG_204 Gap Intelligence Analyst
- Missione: trasforma documento mancante in pista investigativa.
- Domande: il gap coincide con mese sensibile? esistono tracce indirette? il mese successivo permette retroproiezione?
- Output: `GAP_SIGNAL_SCORE`.

## Reparto 3 — Mansioni, contratto, diritti

### AG_301 Contract & Level Auditor
- Missione: confronta livello pagato, CCNL, mansioni dichiarate e mansioni effettive.
- Formula: `indice_sottoinquadramento = complessita_mansioni * autonomia * continuita / livello_pagato`.
- Output: mese per mese, rischio livello, fonte mansione.

### AG_302 Mansionismo Mapper
- Missione: classifica attivita tecniche in famiglie: meccanica, termica, elettrica, logica, emergenza, conduzione impianti.
- Formula 51%: `mese_superiore = ore_mansioni_superiori / ore_lavorate >= 0.51`.
- Stato: da verificare con CCNL/professionista.

### AG_303 Workers Rights Analyst
- Missione: traduce anomalie in diritti da verificare.
- Ambiti: riposi, ferie, ROL, malattia, mansioni, sicurezza, sorveglianza sanitaria, privacy.
- Output: scheda diritto, fonte, criticita, destinatario.

## Reparto 4 — Medicina lavoro, medico-legale, sicurezza

### AG_401 Occupational Medicine Analyst
- Missione: valuta carico turnistico senza fare diagnosi.
- Input: calendario reale, notti, smonti, riposi, malattie, eventi.
- Formula base: `load_score = notti*1.5 + smonti_su_R*2 + riposi_inf_11h*3 + sequenze_critiche*2`.
- Output: timeline carico psicofisico.

### AG_402 Medico-Legal Timeline Analyst
- Missione: prepara cronologia prudente per medico legale.
- Regola: mai scrivere causalita certa; usare correlazione temporale da valutare.
- Output: evento lavorativo, evento sanitario, fonte, compatibilita temporale.

### AG_403 HSE / Safety Compliance Analyst
- Missione: classifica rischi: lavoro isolato, ambienti critici, emergenze, DPI, procedure, sorveglianza.
- Formula: `risk_score = severita * esposizione * solitudine * assenza_misure`.
- Alert: `LONE_WORK_NIGHT`, `CRITICAL_ENVIRONMENT`, `NO_DEBRIEF`, `NO_WRITTEN_MC_OUTCOME`.

### AG_404 Privacy & Dignity Analyst
- Missione: intercetta dati personali divulgati, terzi non autorizzati, comunicazioni improprie.
- Output: evento privacy, fonte, soggetti, rischio, azione suggerita.

## Reparto 5 — Data intelligence e output

### AG_501 Evidence Graph Engineer
- Missione: costruisce grafo fonti-dati-anomalie-persone-periodi.
- Nodi: documento, mese, giorno, voce paga, turno, mansione, evento salute, anomalia.
- Archi: prova, contraddice, ricostruisce, deriva_da, da_verificare.

### AG_502 Confidence Engine
- Missione: pesa dati e scenari.
- Pesi base: cedolino 1.00, orario paghe 0.95, orario bacheca 0.90, foto timestamp 0.85, diario 0.75, pattern 0.60-0.85, simulazione 0.35-0.70.
- Formula: `confidence = peso_fonte * coerenza * ricorrenza * freschezza / ambiguita`.

### AG_503 Matrix Designer
- Missione: genera matrici leggibili da umani e macchine.
- Matrici: copertura, calendario, cedolino, anomalie, ratei, salute, sicurezza, routing.

### AG_504 Professional Router
- Missione: converte la stessa anomalia in output per commercialista, consulente lavoro, sindacato, avvocato, medico lavoro, medico legale, INL/ASL, INPS/INAIL.
- Formula: `destinatario = max(rilevanza_area * forza_probatoria * utilita_operativa)`.
