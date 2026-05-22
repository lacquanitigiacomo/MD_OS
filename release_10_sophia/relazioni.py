"""
MD_OS v10.9.0 — Relazioni Umane
Modellazione utenti, storia conversazioni, empatia computazionale.
"""
import sqlite3
import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime

DB_PATH = Path(__file__).parent / "dataset" / "coscienza.sqlite"

class Relazioni:
    """Gestisce le relazioni con entita umane e sistemi esterni."""

    def __init__(self):
        pass

    def _conn(self):
        conn = sqlite3.connect(str(DB_PATH))
        conn.row_factory = sqlite3.Row
        return conn

    def empatia(self, entita: str, stato_richiesto: str = "attuale") -> Dict[str, Any]:
        with self._conn() as conn:
            row = conn.execute(
                "SELECT * FROM relazioni WHERE entita = ?", (entita,)
            ).fetchone()

            if not row:
                return {"errore": f"Entita '{entita}' non presente in relazioni."}

            storia = json.loads(row["storia_json"] or "[]")
            interazioni_30gg = [s for s in storia
                                if self._entro_giorni(s.get("timestamp"), 30)]
            frequenza = len(interazioni_30gg) / 30.0 if interazioni_30gg else 0.0
            affinita_trend = self._calcola_trend_affinita(storia)

            modello = {
                "entita": entita,
                "tipo": row["tipo"],
                "affinita_corrente": row["affinita"],
                "affinita_trend": affinita_trend,
                "frequenza_interazioni_giornaliera": round(frequenza, 4),
                "preferenze": json.loads(row["preferenze_json"] or "{}"),
                "stato_attuale": row["stato_attuale"],
                "ultima_interazione": row["ultima_interazione"],
                "interazioni_recenti": len(interazioni_30gg),
                "suggerimento_interazione": self._suggerisci(row, frequenza, affinita_trend)
            }
            return modello

    def _entro_giorni(self, timestamp_str: Optional[str], giorni: int) -> bool:
        if not timestamp_str:
            return False
        try:
            t = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
            return (datetime.now() - t).days <= giorni
        except Exception:
            return False

    def _calcola_trend_affinita(self, storia: List[dict]) -> str:
        if len(storia) < 2:
            return "stabile"
        recenti = storia[-5:]
        valori = [s.get("affinita", 0.5) for s in recenti]
        if valori[-1] > valori[0] + 0.1:
            return "crescente"
        elif valori[-1] < valori[0] - 0.1:
            return "decrescente"
        return "stabile"

    def _suggerisci(self, row: sqlite3.Row, freq: float, trend: str) -> str:
        if row["stato_attuale"] == "dormiente" and trend == "decrescente":
            return "Considerare un check-in proattivo per riattivare relazione."
        if freq > 0.8:
            return "Relazione molto attiva. Mantenere supporto costante."
        if row["affinita"] < 0.3:
            return "Attenzione: affinita bassa. Valutare causa e possibile recupero."
        return "Relazione in buono stato. Nessuna azione necessaria."

    def storia(self, entita: str, limit: int = 50) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            row = conn.execute(
                "SELECT storia_json FROM relazioni WHERE entita = ?", (entita,)
            ).fetchone()
            if not row or not row["storia_json"]:
                return []
            storia = json.loads(row["storia_json"])
            return storia[-limit:]

    def aggiorna_relazione(self, entita: str, interazione: Dict[str, Any]):
        with self._conn() as conn:
            row = conn.execute(
                "SELECT storia_json, affinita FROM relazioni WHERE entita = ?", (entita,)
            ).fetchone()
            storia = json.loads(row["storia_json"] or "[]") if row else []
            storia.append(interazione)
            nuova_affinita = self._aggiorna_affinita(row["affinita"] if row else 0.5, interazione)
            conn.execute("""
                INSERT OR REPLACE INTO relazioni (entita, tipo, storia_json, affinita,
                                                 ultima_interazione, stato_attuale)
                VALUES (?, 'umano', ?, ?, ?, 'attivo')
            """, (entita, json.dumps(storia, ensure_ascii=False), nuova_affinita,
                  datetime.now().isoformat()))
            conn.commit()

    def _aggiorna_affinita(self, corrente: float, interazione: Dict[str, Any]) -> float:
        sentiment = interazione.get("sentiment", 0.0)
        importanza = interazione.get("importanza", 0.5)
        delta = sentiment * importanza * 0.1
        return max(-1.0, min(1.0, corrente + delta))

    def lista_entita(self) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            rows = conn.execute("SELECT entita, tipo, affinita, stato_attuale FROM relazioni").fetchall()
            return [dict(r) for r in rows]
