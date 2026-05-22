"""
MD_OS v10.9.0 — Meta-Cognizione
Ragiona sul proprio ragionamento. Rileva bias interni.
"""
import sqlite3
import json
from pathlib import Path
from typing import Dict, List, Any

DB_PATH = Path(__file__).parent / "dataset" / "coscienza.sqlite"

class MetaCognizione:
    """Modulo di riflessione sui processi cognitivi interni."""

    BIAS_CATALOG = {
        "overconfidence": "Tendenza a sovrastimare la propria confidenza",
        "recency": "Dare troppo peso agli eventi recenti",
        "confirmation": "Cercare conferme a pregiudizi esistenti",
        "anchoring": "Dipendenza eccessiva dalla prima informazione ricevuta",
        "availability": "Giudicare probabilita basandosi su esempi facilmente ricordabili",
        "sunk_cost": "Continuare un'azione per investimenti passati irrecuperabili"
    }

    def __init__(self):
        pass

    def _conn(self):
        conn = sqlite3.connect(str(DB_PATH))
        conn.row_factory = sqlite3.Row
        return conn

    def rifletti(self, query: str, ragionamento: str, passaggi: List[str]) -> Dict[str, Any]:
        bias_rilevati = self._rileva_bias(ragionamento, passaggi)
        confidenza_pre = self._stima_confidenza_raw(ragionamento)
        confidenza_post = self._ricalibra_confidenza(confidenza_pre, bias_rilevati)
        correzione = self._genera_correzione(bias_rilevati)

        with self._conn() as conn:
            conn.execute("""
                INSERT INTO meta_cognizione
                (query_originale, ragionamento, passaggi_json, bias_rilevati,
                 correzione_applicata, confidenza_pre, confidenza_post)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                query, ragionamento, json.dumps(passaggi, ensure_ascii=False),
                json.dumps(bias_rilevati, ensure_ascii=False),
                correzione, confidenza_pre, confidenza_post
            ))
            conn.commit()
            meta_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

        return {
            "meta_id": meta_id,
            "query": query,
            "confidenza_pre": round(confidenza_pre, 4),
            "confidenza_post": round(confidenza_post, 4),
            "bias_rilevati": bias_rilevati,
            "correzione": correzione,
            "raccomandazione": "revisione_umana" if any(b["severita"] == "alta" for b in bias_rilevati) else "procedi"
        }

    def _rileva_bias(self, ragionamento: str, passaggi: List[str]) -> List[Dict[str, Any]]:
        testo_completo = (ragionamento + " " + " ".join(passaggi)).lower()
        rilevati = []
        if "sicuramente" in testo_completo or "certamente" in testo_completo:
            rilevati.append({"tipo": "overconfidence", "severita": "media",
                             "descrizione": self.BIAS_CATALOG["overconfidence"]})
        if "sempre" in testo_completo or "mai" in testo_completo:
            rilevati.append({"tipo": "availability", "severita": "bassa",
                             "descrizione": self.BIAS_CATALOG["availability"]})
        if "proprio come l'ultima volta" in testo_completo or "recentemente" in testo_completo:
            rilevati.append({"tipo": "recency", "severita": "media",
                             "descrizione": self.BIAS_CATALOG["recency"]})
        if "dato che ho gia" in testo_completo or "investito troppo" in testo_completo:
            rilevati.append({"tipo": "sunk_cost", "severita": "alta",
                             "descrizione": self.BIAS_CATALOG["sunk_cost"]})
        if len(passaggi) > 0 and all(p.lower().startswith(passaggi[0][:20].lower()) for p in passaggi):
            rilevati.append({"tipo": "anchoring", "severita": "media",
                             "descrizione": self.BIAS_CATALOG["anchoring"]})
        return rilevati

    def _stima_confidenza_raw(self, ragionamento: str) -> float:
        lunghezza = len(ragionamento.split())
        base = min(0.95, 0.5 + lunghezza * 0.01)
        return base

    def _ricalibra_confidenza(self, confidenza: float, bias: List[Dict]) -> float:
        penalita = sum({"bassa": 0.05, "media": 0.15, "alta": 0.30}.get(b["severita"], 0.1) for b in bias)
        return max(0.1, confidenza - penalita)

    def _genera_correzione(self, bias: List[Dict]) -> str:
        if not bias:
            return "Nessun bias rilevato. Procedere con cautela standard."
        suggerimenti = []
        for b in bias:
            if b["tipo"] == "overconfidence":
                suggerimenti.append("Riformulare evitando 'sicuramente'; sostituire con probabilita.")
            elif b["tipo"] == "recency":
                suggerimenti.append("Ampliare la finestra temporale dei dati considerati.")
            elif b["tipo"] == "sunk_cost":
                suggerimenti.append("Valutare solo costi/futuri benefici, ignorare investimenti passati.")
            elif b["tipo"] == "anchoring":
                suggerimenti.append("Ricalibrare partendo da un punto di riferimento diverso.")
            else:
                suggerimenti.append(f"Verificare presenza di {b['tipo']}.")
        return " ".join(suggerimenti)

    def storico_bias(self, limit: int = 20) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            rows = conn.execute("""
                SELECT * FROM meta_cognizione
                ORDER BY timestamp DESC LIMIT ?
            """, (limit,)).fetchall()
            return [dict(r) for r in rows]
