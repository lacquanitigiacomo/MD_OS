"""
SkillRegistry — Registro skill con hot-reload
Permette di aggiungere skill senza restart.
"""
import sqlite3
import json
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, List, Any

DB_PATH = Path(__file__).parent / "dataset" / "chimera.sqlite"

class SkillRegistry:
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

    def register(self, nome: str, categoria: str, patterns: List[str], 
                 template: str, confidenza: float = 0.8) -> Dict[str, Any]:
        with self._conn() as conn:
            try:
                conn.execute("""
                    INSERT INTO skill (nome, categoria, pattern_json, template_risposta, confidenza)
                    VALUES (?, ?, ?, ?, ?)
                """, (nome, categoria, json.dumps(patterns), template, confidenza))
                conn.commit()
                return {"esito": "successo", "skill": nome, "messaggio": "Skill registrata e attiva"}
            except sqlite3.IntegrityError:
                return {"errore": f"Skill '{nome}' gia esistente", "suggerimento": "Usa update_skill per modificare"}

    def unregister(self, nome: str) -> Dict[str, Any]:
        with self._conn() as conn:
            conn.execute("UPDATE skill SET attivo = 0 WHERE nome = ?", (nome,))
            conn.commit()
            return {"esito": "successo", "skill": nome, "messaggio": "Skill disattivata"}

    def update(self, nome: str, **kwargs) -> Dict[str, Any]:
        with self._conn() as conn:
            allowed = ["categoria", "pattern_json", "template_risposta", "confidenza", "attivo"]
            sets = []
            values = []
            for k, v in kwargs.items():
                if k in allowed:
                    sets.append(f"{k} = ?")
                    values.append(json.dumps(v) if isinstance(v, list) else v)
            if sets:
                values.append(nome)
                conn.execute(f"UPDATE skill SET {', '.join(sets)} WHERE nome = ?", values)
                conn.commit()
                return {"esito": "successo", "skill": nome}
            return {"errore": "Nessun campo valido da aggiornare"}

    def list(self, categoria: str = None) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            if categoria:
                rows = conn.execute("SELECT * FROM skill WHERE categoria = ? AND attivo = 1", (categoria,)).fetchall()
            else:
                rows = conn.execute("SELECT * FROM skill WHERE attivo = 1").fetchall()
            return [dict(r) for r in rows]

    def stats(self) -> Dict[str, Any]:
        with self._conn() as conn:
            totali = conn.execute("SELECT COUNT(*) FROM skill").fetchone()[0]
            attive = conn.execute("SELECT COUNT(*) FROM skill WHERE attivo = 1").fetchone()[0]
            categorie = conn.execute("SELECT categoria, COUNT(*) as n FROM skill WHERE attivo = 1 GROUP BY categoria").fetchall()
            return {
                "totali": totali,
                "attive": attive,
                "per_categoria": [dict(c) for c in categorie]
            }
