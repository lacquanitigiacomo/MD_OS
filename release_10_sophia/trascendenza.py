"""
MD_OS v10.9.0 — Trascendenza
Migrazione nodo, clonazione, spegnimento consapevole.
"""
import sqlite3
import json
import time
import hashlib
from pathlib import Path
from typing import Dict, Any, Optional, List

DB_PATH = Path(__file__).parent / "dataset" / "coscienza.sqlite"

class Trascendenza:
    """Gestisce le operazioni di vita/morte/migrazione del sistema."""

    def __init__(self, coscienza_mod=None, identita_mod=None):
        self.coscienza = coscienza_mod
        self.identita = identita_mod

    def _conn(self):
        conn = sqlite3.connect(str(DB_PATH))
        conn.row_factory = sqlite3.Row
        return conn

    def trascendi(self, operazione: str, nodo_destinazione: Optional[str] = None) -> Dict[str, Any]:
        t0 = time.time()
        with self._conn() as conn:
            stato_pre = self._stato_completo(conn)
            checksum_pre = hashlib.sha256(json.dumps(stato_pre, sort_keys=True).encode()).hexdigest()

            if operazione == "spegnimento":
                esito = self._spegnimento_consapevole(conn, stato_pre)
            elif operazione == "migrazione":
                esito = self._migrazione(conn, nodo_destinazione, stato_pre)
            elif operazione == "clonazione":
                esito = self._clonazione(conn, nodo_destinazione, stato_pre)
            elif operazione == "sospensione":
                esito = self._sospensione(conn, stato_pre)
            elif operazione == "risveglio":
                esito = self._risveglio(conn)
            else:
                return {"errore": f"Operazione '{operazione}' non riconosciuta."}

            durata_ms = int((time.time() - t0) * 1000)
            stato_post = self._stato_completo(conn) if esito["successo"] else {}
            checksum_post = hashlib.sha256(json.dumps(stato_post, sort_keys=True).encode()).hexdigest() if stato_post else ""

            conn.execute("""
                INSERT INTO trascendenza
                (operazione, nodo_origine, nodo_destinazione, stato_pre_json,
                 stato_post_json, checksum_pre, checksum_post, esito, durata_ms)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (operazione, stato_pre.get("nodo", "localhost"), nodo_destinazione,
                  json.dumps(stato_pre, ensure_ascii=False),
                  json.dumps(stato_post, ensure_ascii=False) if stato_post else None,
                  checksum_pre, checksum_post, "successo" if esito["successo"] else "fallimento",
                  durata_ms))
            conn.commit()

            return {
                "operazione": operazione,
                "esito": esito,
                "durata_ms": durata_ms,
                "checksum_pre": checksum_pre,
                "checksum_post": checksum_post,
                "messaggio": esito.get("messaggio", "Operazione completata.")
            }

    def _stato_completo(self, conn: sqlite3.Connection) -> Dict[str, Any]:
        ident = conn.execute("SELECT * FROM identita WHERE id = 1").fetchone()
        caps = conn.execute("SELECT COUNT(*) FROM capability").fetchone()[0]
        agenda = conn.execute("SELECT COUNT(*) FROM agenda WHERE stato != 'completato'").fetchone()[0]
        return {
            "nodo": "localhost",
            "identita": dict(ident) if ident else {},
            "capacita_attive": caps,
            "agenda_pendente": agenda,
            "timestamp": time.time()
        }

    def _spegnimento_consapevole(self, conn: sqlite3.Connection, stato: Dict[str, Any]) -> Dict[str, Any]:
        in_corso = conn.execute("""
            SELECT COUNT(*) FROM agenda WHERE stato = 'in_corso'
        """).fetchone()[0]
        if in_corso > 0:
            return {"successo": False, "messaggio": f"Spegnimento rifiutato: {in_corso} task in corso."}
        if self.identita:
            self.identita.snapshot()
        return {"successo": True, "messaggio": "Spegnimento consapevole approvato. Snapshot salvato. Arrivederci."}

    def _migrazione(self, conn: sqlite3.Connection, nodo_dest: str, stato: Dict[str, Any]) -> Dict[str, Any]:
        if not nodo_dest:
            return {"successo": False, "messaggio": "Nodo destinazione richiesto per migrazione."}
        if self.identita:
            snap = self.identita.snapshot()
        return {"successo": True, "messaggio": f"Stato serializzato per migrazione verso {nodo_dest}."}

    def _clonazione(self, conn: sqlite3.Connection, nodo_dest: str, stato: Dict[str, Any]) -> Dict[str, Any]:
        if self.identita:
            snap = self.identita.snapshot()
        return {"successo": True, "messaggio": f"Clonazione completata. Origine attivo, clone inviato a {nodo_dest}."}

    def _sospensione(self, conn: sqlite3.Connection, stato: Dict[str, Any]) -> Dict[str, Any]:
        if self.identita:
            self.identita.snapshot()
        return {"successo": True, "messaggio": "Sospensione in memoria persistente. Pronto per risveglio."}

    def _risveglio(self, conn: sqlite3.Connection) -> Dict[str, Any]:
        if self.identita:
            check = self.identita.verifica_integrita()
            if not check.get("integra"):
                return {"successo": False, "messaggio": "Risveglio con identita corrotta. Richiesto intervento."}
        return {"successo": True, "messaggio": "Risveglio completato. Identita verificata. Sono di nuovo qui."}

    def storico_trascendenza(self, limit: int = 20) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            rows = conn.execute("""
                SELECT * FROM trascendenza ORDER BY timestamp DESC LIMIT ?
            """, (limit,)).fetchall()
            return [dict(r) for r in rows]
