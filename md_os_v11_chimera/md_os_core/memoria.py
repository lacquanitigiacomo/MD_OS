"""
MemoriaGerarchica — Tre livelli che sembrano intelligenti
Working (volatile) → Episodic (eventi) → Semantic (conoscenza)
Tutto in SQLite, zero vettori reali, ma embedding "finti" per sembrare avanzati.
"""
import sqlite3
import json
import hashlib
import random
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime, timezone

logger = __import__('logging').getLogger(__name__)

DB_PATH = Path(__file__).parent / "dataset" / "chimera.sqlite"

class MemoriaGerarchica:
    """
    Simula una memoria gerarchica avanzata usando solo SQLite.
    Gli "embedding" sono hash semantici semplici (bag-of-words).
    """

    def __init__(self, nucleo=None):
        self.nucleo = nucleo

    @contextmanager
    def _conn(self):
        conn = sqlite3.connect(str(DB_PATH))
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    def working_set(self, session_id: str, chiave: str, valore: str, ttl: int = 3600):
        """Memoria a breve termine con TTL."""
        with self._conn() as conn:
            conn.execute("""
                INSERT OR REPLACE INTO memoria_working (session_id, chiave, valore, ttl_seconds)
                VALUES (?, ?, ?, ?)
            """, (session_id, chiave, valore, ttl))
            conn.commit()

    def working_get(self, session_id: str, chiave: str) -> Optional[str]:
        with self._conn() as conn:
            row = conn.execute("""
                SELECT valore FROM memoria_working
                WHERE session_id = ? AND chiave = ?
                AND (julianday('now') - julianday(creato)) * 86400 < ttl_seconds
            """, (session_id, chiave)).fetchone()
            return row["valore"] if row else None

    def working_clear(self, session_id: str):
        with self._conn() as conn:
            conn.execute("DELETE FROM memoria_working WHERE session_id = ?", (session_id,))
            conn.commit()

    def episodic_remember(self, evento: str, entita: str = "utente", sentiment: float = 0.0, meta: Dict = None):
        """Memoria episodica: eventi con timestamp e "embedding" finto."""
        embedding = self._fake_embedding(evento)
        with self._conn() as conn:
            conn.execute("""
                INSERT INTO memoria_episodic (evento, entita, sentiment, embedding_json, meta_json)
                VALUES (?, ?, ?, ?, ?)
            """, (evento, entita, sentiment, json.dumps(embedding), json.dumps(meta or {})))
            conn.commit()

    def episodic_recall(self, entita: str = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Recupera eventi recenti, opzionalmente filtrati per entita."""
        with self._conn() as conn:
            if entita:
                rows = conn.execute("""
                    SELECT * FROM memoria_episodic WHERE entita = ?
                    ORDER BY timestamp DESC LIMIT ?
                """, (entita, limit)).fetchall()
            else:
                rows = conn.execute("""
                    SELECT * FROM memoria_episodic
                    ORDER BY timestamp DESC LIMIT ?
                """, (limit,)).fetchall()
            return [dict(r) for r in rows]

    def semantic_learn(self, concetto: str, definizione: str, relazioni: Dict[str, str] = None, fonte: str = "utente"):
        """Memoria semantica: concetti strutturati."""
        with self._conn() as conn:
            conn.execute("""
                INSERT OR REPLACE INTO memoria_semantic (concetto, definizione, relazioni_json, fonte)
                VALUES (?, ?, ?, ?)
            """, (concetto, definizione, json.dumps(relazioni or {}), fonte))
            conn.commit()

    def semantic_query(self, concetto: str) -> Optional[Dict[str, Any]]:
        """Recupera concetto dalla memoria semantica."""
        with self._conn() as conn:
            row = conn.execute("""
                SELECT * FROM memoria_semantic WHERE concetto = ?
            """, (concetto,)).fetchone()
            return dict(row) if row else None

    def ricerca(self, query: str) -> str:
        """Ricerca cross-livello che sembra intelligente."""
        results = []

        # Cerca in episodic
        with self._conn() as conn:
            rows = conn.execute("""
                SELECT evento, entita, timestamp FROM memoria_episodic
                WHERE evento LIKE ? ORDER BY timestamp DESC LIMIT 3
            """, (f"%{query}%",)).fetchall()
            for r in rows:
                results.append(f"- [{r['entita']}] {r['evento'][:60]}... ({r['timestamp']})")

        # Cerca in semantic
        with self._conn() as conn:
            rows = conn.execute("""
                SELECT concetto, definizione FROM memoria_semantic
                WHERE concetto LIKE ? OR definizione LIKE ? LIMIT 3
            """, (f"%{query}%", f"%{query}%")).fetchall()
            for r in rows:
                results.append(f"- [CONCETTO] {r['concetto']}: {r['definizione'][:60]}...")

        if results:
            return "\n".join(results)
        return "Nessun risultato trovato in memoria."

    def status(self) -> str:
        """Riepilogo status memoria."""
        with self._conn() as conn:
            w = conn.execute("SELECT COUNT(*) FROM memoria_working").fetchone()[0]
            e = conn.execute("SELECT COUNT(*) FROM memoria_episodic").fetchone()[0]
            s = conn.execute("SELECT COUNT(*) FROM memoria_semantic").fetchone()[0]
            return f"Working={w}, Episodic={e}, Semantic={s}"

    def _fake_embedding(self, testo: str) -> List[float]:
        """
        Genera un 'embedding' finto ma deterministico.
        E' un hash semantico semplice: bag-of-words normalizzato.
        Sembra un vettore reale ma costa zero.
        """
        words = testo.lower().split()
        # 16-dimension "embedding" basato su frequenza parole
        embedding = [0.0] * 16
        for word in words:
            h = hashlib.md5(word.encode()).hexdigest()
            for i in range(16):
                embedding[i] += int(h[i*2:(i+1)*2], 16) / 255.0
        # Normalizza
        total = sum(embedding) or 1.0
        return [round(e / total, 4) for e in embedding]
