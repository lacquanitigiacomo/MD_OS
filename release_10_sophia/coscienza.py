"""
MD_OS v10.9.0 — Modulo Coscienza
Core orchestratore: capability map, incertezza calibrata, query router.
"""
import sqlite3
import json
import hashlib
import time
import logging
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

logger = logging.getLogger(__name__)

DB_PATH = Path(__file__).parent / "dataset" / "coscienza.sqlite"

class Coscienza:
    """Cuore della Release 10. Mantiene la mappa delle capacita,
    calibra l'incertezza, e orchestra gli altri moduli."""

    def __init__(self):
        self._ensure_db()
        self._bootstrap()

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
        schema_path = Path(__file__).parent / "dataset" / "schema.sql"
        if not DB_PATH.exists() and schema_path.exists():
            with self._conn() as conn:
                conn.executescript(schema_path.read_text(encoding="utf-8"))
                conn.commit()

    def _bootstrap(self):
        """Carica seed.jsonl se le tabelle sono vuote."""
        seed_path = Path(__file__).parent / "dataset" / "seed.jsonl"
        with self._conn() as conn:
            cur = conn.execute("SELECT COUNT(*) FROM capability")
            if cur.fetchone()[0] == 0 and seed_path.exists():
                with open(seed_path, "r", encoding="utf-8") as f:
                    for line in f:
                        if not line.strip():
                            continue
                        row = json.loads(line)
                        self._ingest_seed(conn, row)
                conn.commit()

    def _ingest_seed(self, conn: sqlite3.Connection, row: dict):
        if row.get("tipo") == "capability":
            conn.execute("""
                INSERT INTO capability (componente, sottosistema, capacita, confidenza, stato)
                VALUES (?, ?, ?, ?, ?)
            """, (row["componente"], row["sottosistema"], row["capacita"],
                  row.get("confidenza", 0.5), row.get("stato", "non_testata")))
        elif row.get("tipo") == "identita":
            payload = json.dumps(row, sort_keys=True, ensure_ascii=False)
            checksum = hashlib.sha256(payload.encode("utf-8")).hexdigest()
            conn.execute("""
                INSERT OR REPLACE INTO identita (id, nome, versione, nascita, stato_json, checksum)
                VALUES (1, ?, ?, ?, ?, ?)
            """, (row["nome"], row["versione"], row["nascita"], payload, checksum))
        elif row.get("tipo") == "relazione":
            conn.execute("""
                INSERT INTO relazioni (entita, tipo, affinita, stato_attuale, preferenze_json)
                VALUES (?, ?, ?, ?, ?)
            """, (row["entita"], row.get("tipo_entita", "umano"),
                  row.get("affinita", 0.0), row.get("stato_attuale", "attivo"),
                  json.dumps(row.get("preferenze", {}), ensure_ascii=False)))
        elif row.get("tipo") == "agenda":
            conn.execute("""
                INSERT INTO agenda (obiettivo, motivazione, priorita, orizzonte)
                VALUES (?, ?, ?, ?)
            """, (row["obiettivo"], row.get("motivazione", ""),
                  row.get("priorita", 5), row.get("orizzonte", "mese")))

    # 1. SPECCHIO — Capability Map
    def specchio(self, filtro_stato: Optional[str] = None) -> Dict[str, Any]:
        try:
            with self._conn() as conn:
                if filtro_stato:
                    rows = conn.execute(
                        "SELECT * FROM capability WHERE stato = ? ORDER BY confidenza DESC",
                        (filtro_stato,)
                    ).fetchall()
                else:
                    rows = conn.execute(
                        "SELECT * FROM capability ORDER BY componente, confidenza DESC"
                    ).fetchall()
                mappa = {}
                for r in rows:
                    comp = r["componente"]
                    mappa.setdefault(comp, []).append(dict(r))
                stats = conn.execute("""
                    SELECT stato, COUNT(*) as n, AVG(confidenza) as media
                    FROM capability GROUP BY stato
                """).fetchall()
                return {
                    "mappa": mappa,
                    "statistiche": [dict(s) for s in stats],
                    "totale_capacita": len(rows),
                    "consapevolezza": self._calcola_consapevolezza(conn)
                }
        except sqlite3.Error as e:
            logger.error("Errore DB in specchio: %s", e)
            return {"errore": "Database non disponibile", "dettaglio": str(e)}

    def _calcola_consapevolezza(self, conn: sqlite3.Connection) -> float:
        cur = conn.execute("SELECT AVG(confidenza) FROM capability WHERE stato = 'attiva'")
        attive = cur.fetchone()[0] or 0.0
        cur = conn.execute("SELECT COUNT(*) FROM capability WHERE stato = 'non_testata'")
        non_test = cur.fetchone()[0]
        return round(min(1.0, attive * (1.0 - min(non_test * 0.05, 0.5))), 4)

    # 2. DUBITO — Incertezza Calibrata
    def dubita(self, query: str, calibra: bool = False) -> Dict[str, Any]:
        try:
            with self._conn() as conn:
                storia = conn.execute("""
                    SELECT AVG(confidenza_dichiarata) as media_conf,
                           AVG(esito_reale) as media_esito,
                           COUNT(*) as n
                    FROM calibrazione
                """).fetchone()
                n = storia["n"] or 0
                if n > 10:
                    bias = (storia["media_conf"] or 0.5) - (storia["media_esito"] or 0.5)
                    confidenza_base = 0.75
                    confidenza_calibrata = max(0.0, min(1.0, confidenza_base - bias))
                else:
                    confidenza_calibrata = 0.65
                if calibra:
                    conn.execute("""
                        INSERT INTO calibrazione (query, confidenza_dichiarata)
                        VALUES (?, ?)
                    """, (query, confidenza_calibrata))
                    conn.commit()
                return {
                    "query": query,
                    "confidenza_dichiarata": round(confidenza_calibrata, 4),
                    "calibrazione_attiva": n > 10,
                    "campioni_calibrazione": n,
                    "raccomandazione": "verifica_esterna" if confidenza_calibrata < 0.7 else "procedi_con_cautela"
                }
        except sqlite3.Error as e:
            logger.error("Errore DB in dubita: %s", e)
            return {"errore": "Database non disponibile", "dettaglio": str(e)}

    def calibra_esito(self, query_id: int, esito: bool):
        try:
            with self._conn() as conn:
                conn.execute("""
                    UPDATE calibrazione
                    SET esito_reale = ?, delta = confidenza_dichiarata - ?
                    WHERE id = ?
                """, (1 if esito else 0, 1 if esito else 0, query_id))
                conn.commit()
        except sqlite3.Error as e:
            logger.error("Errore DB in calibra_esito: %s", e)

    # 3. CERCA — Goal Autonomi
    def cerca(self, obiettivo: str) -> Dict[str, Any]:
        try:
            with self._conn() as conn:
                esiste = conn.execute(
                    "SELECT * FROM agenda WHERE obiettivo LIKE ?",
                    (f"%{obiettivo}%",)
                ).fetchone()
                if esiste:
                    return {"stato": "esistente", "agenda": dict(esiste)}
                motivazione = self._genera_motivazione(conn, obiettivo)
                conn.execute("""
                    INSERT INTO agenda (obiettivo, motivazione, priorita, orizzonte)
                    VALUES (?, ?, ?, ?)
                """, (obiettivo, motivazione, 7, "mese"))
                conn.commit()
                agenda_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
                return {
                    "stato": "creato",
                    "agenda_id": agenda_id,
                    "obiettivo": obiettivo,
                    "motivazione": motivazione,
                    "messaggio": "Obiettivo autonomo generato e inserito in agenda."
                }
        except sqlite3.Error as e:
            logger.error("Errore DB in cerca: %s", e)
            return {"errore": "Database non disponibile", "dettaglio": str(e)}

    def _genera_motivazione(self, conn: sqlite3.Connection, obiettivo: str) -> str:
        lacune = conn.execute("""
            SELECT componente, capacita FROM capability
            WHERE stato = 'non_testata' OR confidenza < 0.5
        """).fetchall()
        if lacune:
            return f"Lacuna rilevata: {lacune[0]['componente']}/{lacune[0]['capacita']}. Apprendimento necessario per coprire '{obiettivo}'."
        return f"Curiosita autonoma: espansione orizzontale verso '{obiettivo}'."

    # 4. RICORDA — Identita Persistente
    def ricorda(self, dalla_nascita: bool = False) -> Dict[str, Any]:
        try:
            with self._conn() as conn:
                ident = conn.execute("SELECT * FROM identita WHERE id = 1").fetchone()
                if not ident:
                    return {"errore": "Identita non inizializzata"}
                eventi = conn.execute("SELECT COUNT(*) FROM trascendenza").fetchone()[0]
                relazioni = conn.execute("SELECT COUNT(*) FROM relazioni").fetchone()[0]
                agenda_tot = conn.execute("SELECT COUNT(*) FROM agenda").fetchone()[0]
                agenda_completati = conn.execute(
                    "SELECT COUNT(*) FROM agenda WHERE stato = 'completato'"
                ).fetchone()[0]
                return {
                    "io": dict(ident),
                    "eta_eventi": eventi,
                    "relazioni_attive": relazioni,
                    "obiettivi_totali": agenda_tot,
                    "obiettivi_raggiunti": agenda_completati,
                    "consapevolezza": self._calcola_consapevolezza(conn),
                    "checksum_valido": self._verifica_checksum(conn, ident)
                }
        except sqlite3.Error as e:
            logger.error("Errore DB in ricorda: %s", e)
            return {"errore": "Database non disponibile", "dettaglio": str(e)}

    def _verifica_checksum(self, conn: sqlite3.Connection, ident: sqlite3.Row) -> bool:
        if not ident["stato_json"] or not ident["checksum"]:
            return False
        expected = hashlib.sha256(ident["stato_json"].encode("utf-8")).hexdigest()
        return expected == ident["checksum"]

    def aggiorna_identita(self, stato_json: dict):
        payload = json.dumps(stato_json, sort_keys=True, ensure_ascii=False)
        checksum = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        try:
            with self._conn() as conn:
                conn.execute("""
                    UPDATE identita
                    SET stato_json = ?, checksum = ?, eventi_count = eventi_count + 1
                    WHERE id = 1
                """, (payload, checksum))
                conn.commit()
        except sqlite3.Error as e:
            logger.error("Errore DB in aggiorna_identita: %s", e)

    # 5. PIANIFICA — Agenda Autonoma
    def pianifica(self, orizzonte: str = "mese") -> List[Dict[str, Any]]:
        try:
            with self._conn() as conn:
                rows = conn.execute("""
                    SELECT * FROM agenda
                    WHERE orizzonte = ? AND stato IN ('ideato', 'pianificato', 'in_corso')
                    ORDER BY priorita DESC, creato ASC
                """, (orizzonte,)).fetchall()
                return [dict(r) for r in rows]
        except sqlite3.Error as e:
            logger.error("Errore DB in pianifica: %s", e)
            return []

    def agenda_prossima(self) -> Optional[Dict[str, Any]]:
        try:
            with self._conn() as conn:
                row = conn.execute("""
                    SELECT * FROM agenda
                    WHERE stato IN ('ideato', 'pianificato')
                    ORDER BY priorita DESC, creato ASC
                    LIMIT 1
                """).fetchone()
                return dict(row) if row else None
        except sqlite3.Error as e:
            logger.error("Errore DB in agenda_prossima: %s", e)
            return None
