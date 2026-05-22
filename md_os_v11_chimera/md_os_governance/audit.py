"""
AuditLogger — Logging strutturato per compliance
Sembra un SIEM enterprise, ma e' SQLite locale.
"""
import sqlite3
import json
import hashlib
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime, timezone

DB_PATH = Path(__file__).parent / "audit" / "governance.sqlite"

class AuditLogger:
    """
    Logger audit completo per tracciabilita.
    Zero costi, zero servizi esterni.
    """

    def __init__(self):
        self._ensure_db()

    @contextmanager
    def _conn(self):
        conn = sqlite3.connect(str(DB_PATH))
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    def _ensure_db(self):
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        if not DB_PATH.exists():
            with self._conn() as conn:
                conn.executescript("""
CREATE TABLE IF NOT EXISTS audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    livello TEXT CHECK(livello IN ('DEBUG','INFO','WARN','ERROR','CRITICAL')),
    categoria TEXT,
    utente TEXT,
    azione TEXT,
    risorsa TEXT,
    esito TEXT CHECK(esito IN ('successo','fallimento','tentativo')),
    dettaglio TEXT,
    hash_integrita TEXT,
    sessione TEXT,
    ip_client TEXT DEFAULT '127.0.0.1',
    meta_json TEXT
);

CREATE TABLE IF NOT EXISTS metriche (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nome TEXT,
    valore REAL,
    unita TEXT,
    tags_json TEXT
);

CREATE INDEX idx_audit_timestamp ON audit_log(timestamp);
CREATE INDEX idx_audit_utente ON audit_log(utente);
CREATE INDEX idx_audit_sessione ON audit_log(sessione);
""")
                conn.commit()

    def log(self, livello: str, categoria: str, azione: str, 
            utente: str = "system", risorsa: str = "", esito: str = "successo",
            dettaglio: str = "", sessione: str = "", meta: Dict = None):
        """Log strutturato con hash integrita."""
        meta = meta or {}
        payload = f"{livello}:{categoria}:{azione}:{utente}:{risorsa}:{esito}:{dettaglio}:{json.dumps(meta, sort_keys=True)}"
        hash_integrita = hashlib.sha256(payload.encode()).hexdigest()[:32]

        with self._conn() as conn:
            conn.execute("""
                INSERT INTO audit_log 
                (livello, categoria, utente, azione, risorsa, esito, dettaglio, hash_integrita, sessione, meta_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (livello, categoria, utente, azione, risorsa, esito, dettaglio, 
                  hash_integrita, sessione, json.dumps(meta)))
            conn.commit()

    def metric(self, nome: str, valore: float, unita: str = "count", tags: Dict = None):
        """Registra metrica per dashboard."""
        with self._conn() as conn:
            conn.execute("""
                INSERT INTO metriche (nome, valore, unita, tags_json)
                VALUES (?, ?, ?, ?)
            """, (nome, valore, unita, json.dumps(tags or {})))
            conn.commit()

    def query(self, filtri: Dict[str, Any] = None, limit: int = 100) -> List[Dict[str, Any]]:
        """Query audit con filtri."""
        filtri = filtri or {}
        where = []
        params = []

        if "livello" in filtri:
            where.append("livello = ?")
            params.append(filtri["livello"])
        if "utente" in filtri:
            where.append("utente = ?")
            params.append(filtri["utente"])
        if "sessione" in filtri:
            where.append("sessione = ?")
            params.append(filtri["sessione"])
        if "da" in filtri:
            where.append("timestamp >= ?")
            params.append(filtri["da"])
        if "a" in filtri:
            where.append("timestamp <= ?")
            params.append(filtri["a"])

        query_sql = "SELECT * FROM audit_log"
        if where:
            query_sql += " WHERE " + " AND ".join(where)
        query_sql += " ORDER BY timestamp DESC LIMIT ?"
        params.append(limit)

        with self._conn() as conn:
            rows = conn.execute(query_sql, params).fetchall()
            return [dict(r) for r in rows]

    def dashboard_stats(self) -> Dict[str, Any]:
        """Statistiche per dashboard."""
        with self._conn() as conn:
            totali = conn.execute("SELECT COUNT(*) FROM audit_log").fetchone()[0]
            errori = conn.execute("SELECT COUNT(*) FROM audit_log WHERE livello = 'ERROR'").fetchone()[0]
            utenti = conn.execute("SELECT COUNT(DISTINCT utente) FROM audit_log").fetchone()[0]
            sessioni = conn.execute("SELECT COUNT(DISTINCT sessione) FROM audit_log").fetchone()[0]

            # Ultime 24h
            ultime = conn.execute("""
                SELECT COUNT(*) FROM audit_log 
                WHERE timestamp >= datetime('now', '-1 day')
            """).fetchone()[0]

            return {
                "log_totali": totali,
                "errori": errori,
                "utenti_unici": utenti,
                "sessioni": sessioni,
                "ultime_24h": ultime,
                "tasso_errore": round(errori / totali * 100, 2) if totali > 0 else 0
            }
