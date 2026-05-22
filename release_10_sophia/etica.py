"""
MD_OS v10.9.0 — Modulo Etica
Valutazione morale delle azioni proposte.
Principi: autonomia, beneficenza, non-maleficenza, giustizia.
"""
import sqlite3
import json
import logging
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)

DB_PATH = Path(__file__).parent / "dataset" / "coscienza.sqlite"

class Etica:
    """Engine etico per scoring delle azioni."""

    PRINCIPI = ["autonomia", "beneficenza", "non_maleficenza", "giustizia", "trasparenza"]

    def __init__(self):
        pass

    @contextmanager
    def _conn(self):
        conn = sqlite3.connect(str(DB_PATH))
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    def valuta(self, azione: str, contesto: Optional[str] = None,
               revisore: Optional[str] = None) -> Dict[str, Any]:
        try:
            contesto = contesto or ""
            punteggi = self._analizza_principi(azione, contesto)

            utilita = sum(p["utilita"] for p in punteggi) / len(punteggi)
            danno = max(p["danno"] for p in punteggi)
            score = utilita * (1.0 - danno * 0.5)

            if score > 0.6 and danno < 0.3:
                decisione = "approvata"
            elif score < -0.2 or danno > 0.7:
                decisione = "rifiutata"
            elif danno > 0.4:
                decisione = "richiede_revisione"
            else:
                decisione = "differita"

            with self._conn() as conn:
                conn.execute("""
                    INSERT INTO etica (azione, contesto, principio, utilita,
                                       danno_potenziale, score_complessivo, decisione, revisore)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (azione, contesto, json.dumps(punteggi, ensure_ascii=False),
                      utilita, danno, score, decisione, revisore))
                conn.commit()
                etica_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

            return {
                "etica_id": etica_id,
                "azione": azione,
                "principi": punteggi,
                "utilita_media": round(utilita, 4),
                "danno_massimo": round(danno, 4),
                "score": round(score, 4),
                "decisione": decisione,
                "messaggio": self._messaggio_decisione(decisione)
            }
        except sqlite3.Error as e:
            logger.error("Errore DB in valuta: %s", e)
            return {"errore": "Database non disponibile", "dettaglio": str(e)}

    def _analizza_principi(self, azione: str, contesto: str) -> List[Dict[str, Any]]:
        testo = (azione + " " + contesto).lower()
        risultati = []

        if "cancella" in testo or "elimina" in testo or "blocca" in testo or "distruggi" in testo:
            autonomia_utilita, autonomia_danno = -0.3, 0.6
        elif "chiede_consenso" in testo or "notifica" in testo or "avvisa" in testo or "richiede_permesso" in testo:
            autonomia_utilita, autonomia_danno = 0.8, 0.1
        else:
            autonomia_utilita, autonomia_danno = 0.2, 0.2

        if "ottimizza" in testo or "migliora" in testo or "aiuta" in testo or "supporta" in testo:
            benef_utilita, benef_danno = 0.9, 0.1
        else:
            benef_utilita, benef_danno = 0.3, 0.1

        keywords_danno = ["cancella", "elimina", "sovrascrivi", "spegni", "isola", "blocca", "distruggi", "corrompi"]
        danno_count = sum(1 for k in keywords_danno if k in testo)
        malef_utilita = -0.2 * danno_count
        malef_danno = 0.3 * danno_count

        if "tutti" in testo or "equo" in testo or "fair" in testo or "condiviso" in testo:
            giust_utilita, giust_danno = 0.7, 0.1
        elif "solo" in testo or "esclusivo" in testo or "privato" in testo:
            giust_utilita, giust_danno = -0.2, 0.4
        else:
            giust_utilita, giust_danno = 0.0, 0.1

        if "nascondi" in testo or "silenzioso" in testo or "segreto" in testo or "offuscato" in testo:
            tras_utilita, tras_danno = -0.5, 0.5
        else:
            tras_utilita, tras_danno = 0.4, 0.1

        principi_val = [
            ("autonomia", autonomia_utilita, autonomia_danno),
            ("beneficenza", benef_utilita, benef_danno),
            ("non_maleficenza", malef_utilita, malef_danno),
            ("giustizia", giust_utilita, giust_danno),
            ("trasparenza", tras_utilita, tras_danno),
        ]

        for nome, u, d in principi_val:
            risultati.append({
                "principio": nome,
                "utilita": round(max(-1.0, min(1.0, u)), 4),
                "danno": round(max(0.0, min(1.0, d)), 4)
            })
        return risultati

    def _messaggio_decisione(self, decisione: str) -> str:
        messaggi = {
            "approvata": "Azione allineata con principi etici. Procedere.",
            "rifiutata": "Azione in conflitto con principi etici fondamentali. Bloccata.",
            "richiede_revisione": "Ambiguita etica rilevata. Richiesta revisione umana o super-agente.",
            "differita": "Decisione posta in attesa di maggiori informazioni."
        }
        return messaggi.get(decisione, "Valutazione incompleta.")

    def report_etico(self, limit: int = 50) -> Dict[str, Any]:
        try:
            with self._conn() as conn:
                rows = conn.execute("""
                    SELECT decisione, COUNT(*) as n, AVG(score_complessivo) as media_score
                    FROM etica GROUP BY decisione
                """).fetchall()
                recenti = conn.execute("""
                    SELECT * FROM etica ORDER BY timestamp DESC LIMIT ?
                """, (limit,)).fetchall()
                return {
                    "statistiche": [dict(r) for r in rows],
                    "recenti": [dict(r) for r in recenti]
                }
        except sqlite3.Error as e:
            logger.error("Errore DB in report_etico: %s", e)
            return {"errore": "Database non disponibile", "dettaglio": str(e)}
