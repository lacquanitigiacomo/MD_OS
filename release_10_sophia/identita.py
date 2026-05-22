"""
MD_OS v10.9.0 — Identita Persistente
Continuita attraverso reboot, aggiornamenti, crash.
"""
import sqlite3
import json
import hashlib
import time
import logging
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, Any

logger = logging.getLogger(__name__)

DB_PATH = Path(__file__).parent / "dataset" / "coscienza.sqlite"
IDENTITA_PATH = Path(__file__).parent / "dataset" / "identita.json"

class Identita:
    """Gestisce la persistenza e l'integrita dell'identita del sistema."""

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

    def snapshot(self) -> Dict[str, Any]:
        try:
            with self._conn() as conn:
                ident = conn.execute("SELECT * FROM identita WHERE id = 1").fetchone()
                if not ident:
                    return {"errore": "Identita non trovata"}

                capabilities = conn.execute("SELECT * FROM capability").fetchall()
                agenda = conn.execute("SELECT * FROM agenda").fetchall()
                relazioni = conn.execute("SELECT * FROM relazioni").fetchall()
                meta = conn.execute("SELECT * FROM meta_cognizione ORDER BY timestamp DESC LIMIT 100").fetchall()
                etica = conn.execute("SELECT * FROM etica ORDER BY timestamp DESC LIMIT 100").fetchall()
                trasc = conn.execute("SELECT * FROM trascendenza ORDER BY timestamp DESC LIMIT 50").fetchall()

                snapshot = {
                    "identita": dict(ident),
                    "capabilities": [dict(c) for c in capabilities],
                    "agenda": [dict(a) for a in agenda],
                    "relazioni": [dict(r) for r in relazioni],
                    "meta_cognizione_recente": [dict(m) for m in meta],
                    "etica_recente": [dict(e) for e in etica],
                    "trascendenza_recente": [dict(t) for t in trasc],
                    "timestamp": time.time(),
                    "versione_schema": "10.9.0"
                }

                payload = json.dumps(snapshot, sort_keys=True, ensure_ascii=False)
                checksum = hashlib.sha256(payload.encode("utf-8")).hexdigest()
                snapshot["checksum"] = checksum

                # Scrittura atomica: scrivi su file temporaneo poi rinomina
                tmp_path = IDENTITA_PATH.with_suffix(".tmp")
                with open(tmp_path, "w", encoding="utf-8") as f:
                    json.dump(snapshot, f, ensure_ascii=False, indent=2)
                tmp_path.rename(IDENTITA_PATH)

                # Aggiorna anche il DB
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
        except sqlite3.Error as e:
            logger.error("Errore DB in snapshot: %s", e)
            return {"errore": "Database non disponibile", "dettaglio": str(e)}
        except Exception as e:
            logger.error("Errore generico in snapshot: %s", e)
            return {"errore": "Snapshot fallito", "dettaglio": str(e)}

    def ripristina(self, snapshot_path: Path = None) -> Dict[str, Any]:
        path = snapshot_path or IDENTITA_PATH
        if not path.exists():
            return {"errore": f"Snapshot non trovato: {path}"}

        try:
            with open(path, "r", encoding="utf-8") as f:
                snapshot = json.load(f)
        except Exception as e:
            return {"errore": f"Impossibile leggere snapshot: {e}"}

        stored_checksum = snapshot.pop("checksum", None)
        payload = json.dumps(snapshot, sort_keys=True, ensure_ascii=False)
        computed = hashlib.sha256(payload.encode("utf-8")).hexdigest()

        if stored_checksum != computed:
            return {"errore": "Checksum non valido. Snapshot corrotto o manomesso."}

        try:
            with self._conn() as conn:
                # Transazione atomica completa
                # 1. identita
                ident = snapshot["identita"]
                conn.execute("""
                    INSERT OR REPLACE INTO identita (id, nome, versione, nascita, stato_json, checksum)
                    VALUES (1, ?, ?, ?, ?, ?)
                """, (ident["nome"], ident["versione"], ident["nascita"], payload, computed))

                # 2. capability
                for cap in snapshot.get("capabilities", []):
                    conn.execute("""
                        INSERT OR REPLACE INTO capability
                        (id, componente, sottosistema, capacita, descrizione, confidenza, stato)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (cap.get("id"), cap["componente"], cap["sottosistema"],
                          cap["capacita"], cap.get("descrizione"), cap.get("confidenza", 0.5),
                          cap.get("stato", "non_testata")))

                # 3. agenda
                for ag in snapshot.get("agenda", []):
                    conn.execute("""
                        INSERT OR REPLACE INTO agenda (id, obiettivo, motivazione, priorita, stato, orizzonte, progresso)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (ag.get("id"), ag["obiettivo"], ag.get("motivazione"),
                          ag.get("priorita", 5), ag.get("stato", "ideato"),
                          ag.get("orizzonte", "mese"), ag.get("progresso", 0.0)))

                # 4. relazioni
                for rel in snapshot.get("relazioni", []):
                    conn.execute("""
                        INSERT OR REPLACE INTO relazioni
                        (id, entita, tipo, storia_json, affinita, preferenze_json, stato_attuale, ultima_interazione)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """, (rel.get("id"), rel["entita"], rel.get("tipo", "umano"),
                          json.dumps(rel.get("storia", []), ensure_ascii=False),
                          rel.get("affinita", 0.0),
                          json.dumps(rel.get("preferenze", {}), ensure_ascii=False),
                          rel.get("stato_attuale", "attivo"),
                          rel.get("ultima_interazione")))

                # 5. meta_cognizione (recente)
                for meta in snapshot.get("meta_cognizione_recente", []):
                    conn.execute("""
                        INSERT OR REPLACE INTO meta_cognizione
                        (id, query_originale, ragionamento, passaggi_json, bias_rilevati,
                         correzione_applicata, confidenza_pre, confidenza_post, timestamp)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (meta.get("id"), meta.get("query_originale"), meta.get("ragionamento"),
                          meta.get("passaggi_json"), meta.get("bias_rilevati"),
                          meta.get("correzione_applicata"), meta.get("confidenza_pre"),
                          meta.get("confidenza_post"), meta.get("timestamp")))

                # 6. etica (recente)
                for et in snapshot.get("etica_recente", []):
                    conn.execute("""
                        INSERT OR REPLACE INTO etica
                        (id, azione, contesto, principio, utilita, danno_potenziale,
                         score_complessivo, decisione, timestamp, revisore)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (et.get("id"), et.get("azione"), et.get("contesto"),
                          et.get("principio"), et.get("utilita"), et.get("danno_potenziale"),
                          et.get("score_complessivo"), et.get("decisione"),
                          et.get("timestamp"), et.get("revisore")))

                # 7. trascendenza (recente)
                for tr in snapshot.get("trascendenza_recente", []):
                    conn.execute("""
                        INSERT OR REPLACE INTO trascendenza
                        (id, operazione, nodo_origine, nodo_destinazione, stato_pre_json,
                         stato_post_json, checksum_pre, checksum_post, esito, timestamp, durata_ms)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (tr.get("id"), tr.get("operazione"), tr.get("nodo_origine"),
                          tr.get("nodo_destinazione"), tr.get("stato_pre_json"),
                          tr.get("stato_post_json"), tr.get("checksum_pre"),
                          tr.get("checksum_post"), tr.get("esito"),
                          tr.get("timestamp"), tr.get("durata_ms")))

                conn.commit()

            return {
                "esito": "successo",
                "checksum_verificato": computed,
                "messaggio": "Identita ripristinata con integrita verificata."
            }
        except sqlite3.Error as e:
            logger.error("Errore DB in ripristina: %s", e)
            return {"errore": f"Ripristino fallito: {e}"}
        except Exception as e:
            logger.error("Errore generico in ripristina: %s", e)
            return {"errore": f"Ripristino fallito: {e}"}

    def verifica_integrita(self) -> Dict[str, Any]:
        try:
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
        except sqlite3.Error as e:
            logger.error("Errore DB in verifica_integrita: %s", e)
            return {"integra": False, "motivo": str(e)}
