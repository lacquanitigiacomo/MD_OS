"""
MD_OS v10.9.0 — Identita Persistente
Continuita attraverso reboot, aggiornamenti, crash.
"""
import sqlite3
import json
import hashlib
import time
from pathlib import Path
from typing import Dict, Any

DB_PATH = Path(__file__).parent / "dataset" / "coscienza.sqlite"
IDENTITA_PATH = Path(__file__).parent / "dataset" / "identita.json"

class Identita:
    """Gestisce la persistenza e l'integrita dell'identita del sistema."""

    def __init__(self):
        pass

    def _conn(self):
        conn = sqlite3.connect(str(DB_PATH))
        conn.row_factory = sqlite3.Row
        return conn

    def snapshot(self) -> Dict[str, Any]:
        with self._conn() as conn:
            ident = conn.execute("SELECT * FROM identita WHERE id = 1").fetchone()
            if not ident:
                return {"errore": "Identita non trovata"}

            capabilities = conn.execute("SELECT * FROM capability").fetchall()
            agenda = conn.execute("SELECT * FROM agenda").fetchall()
            relazioni = conn.execute("SELECT * FROM relazioni").fetchall()
            meta = conn.execute("SELECT * FROM meta_cognizione ORDER BY timestamp DESC LIMIT 100").fetchall()
            etica = conn.execute("SELECT * FROM etica ORDER BY timestamp DESC LIMIT 100").fetchall()

            snapshot = {
                "identita": dict(ident),
                "capabilities": [dict(c) for c in capabilities],
                "agenda": [dict(a) for a in agenda],
                "relazioni": [dict(r) for r in relazioni],
                "meta_cognizione_recente": [dict(m) for m in meta],
                "etica_recente": [dict(e) for e in etica],
                "timestamp": time.time(),
                "versione_schema": "10.9.0"
            }

            payload = json.dumps(snapshot, sort_keys=True, ensure_ascii=False)
            checksum = hashlib.sha256(payload.encode("utf-8")).hexdigest()
            snapshot["checksum"] = checksum

            with open(IDENTITA_PATH, "w", encoding="utf-8") as f:
                json.dump(snapshot, f, ensure_ascii=False, indent=2)

            conn.execute("""
                UPDATE identita SET stato_json = ?, checksum = ? WHERE id = 1
            """, (payload, checksum))
            conn.commit()

            return {
                "esito": "successo",
                "checksum": checksum,
                "dimensione_bytes": len(payload),
                "percorso": str(IDENTITA_PATH),
                "messaggio": "Snapshot identita creato e validato."
            }

    def ripristina(self, snapshot_path: Path = None) -> Dict[str, Any]:
        path = snapshot_path or IDENTITA_PATH
        if not path.exists():
            return {"errore": f"Snapshot non trovato: {path}"}

        with open(path, "r", encoding="utf-8") as f:
            snapshot = json.load(f)

        stored_checksum = snapshot.pop("checksum", None)
        payload = json.dumps(snapshot, sort_keys=True, ensure_ascii=False)
        computed = hashlib.sha256(payload.encode("utf-8")).hexdigest()

        if stored_checksum != computed:
            return {"errore": "Checksum non valido. Snapshot corrotto o manomesso."}

        with self._conn() as conn:
            ident = snapshot["identita"]
            conn.execute("""
                INSERT OR REPLACE INTO identita (id, nome, versione, nascita, stato_json, checksum)
                VALUES (1, ?, ?, ?, ?, ?)
            """, (ident["nome"], ident["versione"], ident["nascita"], payload, computed))

            for cap in snapshot.get("capabilities", []):
                conn.execute("""
                    INSERT OR REPLACE INTO capability
                    (id, componente, sottosistema, capacita, descrizione, confidenza, stato)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (cap.get("id"), cap["componente"], cap["sottosistema"],
                      cap["capacita"], cap.get("descrizione"), cap.get("confidenza", 0.5),
                      cap.get("stato", "non_testata")))
            conn.commit()

        return {
            "esito": "successo",
            "checksum_verificato": computed,
            "messaggio": "Identita ripristinata con integrita verificata."
        }

    def verifica_integrita(self) -> Dict[str, Any]:
        with self._conn() as conn:
            ident = conn.execute("SELECT * FROM identita WHERE id = 1").fetchone()
            if not ident or not ident["stato_json"]:
                return {"integra": False, "motivo": "Stato identita assente"}
            expected = hashlib.sha256(ident["stato_json"].encode("utf-8")).hexdigest()
            return {
                "integra": expected == ident["checksum"],
                "checksum_atteso": expected,
                "checksum_memorizzato": ident["checksum"],
                "ultimo_reboot": ident["ultimo_reboot"]
            }
