"""
MD_OS v11 "Chimera" — Nucleo
Non ha coscienza, ma ha logging cosi ricco che sembra consapevole.
"""
import sqlite3
import json
import hashlib
import time
import logging
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

DB_PATH = Path(__file__).parent / "dataset" / "chimera.sqlite"

class Nucleo:
    """
    Il nucleo non ragiona. Ma ha:
    - Skill registry dinamico
    - Memoria gerarchica (working/episodic/semantic)
    - Pattern matching avanzato
    - Logging strutturato che sembra intelligente
    """

    def __init__(self):
        self._ensure_db()
        from .skill_registry import SkillRegistry
        from .memoria import MemoriaGerarchica
        self.skill_registry = SkillRegistry(self)
        self.memoria = MemoriaGerarchica(self)
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
        if not DB_PATH.exists():
            with self._conn() as conn:
                conn.executescript(self._schema())
                conn.commit()

    def _schema(self) -> str:
        return """
CREATE TABLE IF NOT EXISTS skill (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    categoria TEXT,
    pattern_json TEXT,
    template_risposta TEXT,
    confidenza REAL DEFAULT 0.8,
    usi_count INTEGER DEFAULT 0,
    ultimo_uso TIMESTAMP,
    attivo INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS memoria_working (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,
    chiave TEXT,
    valore TEXT,
    ttl_seconds INTEGER DEFAULT 3600,
    creato TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS memoria_episodic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    evento TEXT,
    entita TEXT,
    sentiment REAL DEFAULT 0.0,
    embedding_json TEXT,
    meta_json TEXT
);

CREATE TABLE IF NOT EXISTS memoria_semantic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    concetto TEXT UNIQUE,
    definizione TEXT,
    relazioni_json TEXT,
    fonte TEXT,
    aggiornato TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS log_orchestrazione (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    livello TEXT,
    componente TEXT,
    azione TEXT,
    input_hash TEXT,
    output_hash TEXT,
    latenza_ms INTEGER,
    meta_json TEXT
);

CREATE TABLE IF NOT EXISTS sessione (
    id TEXT PRIMARY KEY,
    creato TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultimo_ping TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    stato TEXT DEFAULT 'attiva',
    meta_json TEXT
);

CREATE INDEX idx_skill_nome ON skill(nome);
CREATE INDEX idx_memoria_episodic_entita ON memoria_episodic(entita);
CREATE INDEX idx_log_componente ON log_orchestrazione(componente, timestamp);
CREATE INDEX idx_sessione_stato ON sessione(stato);
"""

    def _bootstrap(self):
        """Carica skill di base se vuoto."""
        with self._conn() as conn:
            cur = conn.execute("SELECT COUNT(*) FROM skill")
            if cur.fetchone()[0] == 0:
                skills_base = [
                    ("saluto", "comunicazione", '["ciao", "salve", "hey", "buongiorno"]',
                     "Ciao! Sono Chimera, pronto ad assisterti. Cosa posso fare per te?", 0.95),
                    ("stato_sistema", "system", '["stato", "come stai", "health", "check"]',
                     "Sistema operativo Chimera v11. Tutti i moduli operativi. Memoria: {memoria_status}.", 0.9),
                    ("ricerca_memoria", "memoria", '["ricorda", "cerca", "trova", "dove"]',
                     "Sto cercando nella memoria gerarchica... {risultato_ricerca}", 0.85),
                    ("automazione_file", "file", '["file", "cartella", "organizza", "sposta"]',
                     "Posso organizzare file localmente. Specifica il percorso e l'azione desiderata.", 0.8),
                    ("analisi_testo", "nlp", '["analizza", "riassumi", "estrai", "sentiment"]',
                     "Analisi testuale completata. Risultato: {analisi_output}", 0.82),
                    ("calcolo", "math", '["calcola", "somma", "moltiplica", "percentuale"]',
                     "Calcolo eseguito: {risultato_calcolo}", 0.98),
                    ("genera_codice", "dev", '["codice", "script", "funzione", "programma"]',
                     "Ecco lo snippet richiesto:\n```\n{codice_generato}\n```", 0.75),
                    ("mcp_simulato", "protocol", '["mcp", "tool", "server", "connetti"]',
                     "Protocollo MCP simulato attivo. Endpoint locale: http://localhost:7777/mcp/{tool_name}", 0.7),
                ]
                for nome, cat, pattern, template, conf in skills_base:
                    conn.execute("""
                        INSERT INTO skill (nome, categoria, pattern_json, template_risposta, confidenza)
                        VALUES (?, ?, ?, ?, ?)
                    """, (nome, cat, pattern, template, conf))
                conn.commit()
                logger.info("Bootstrap: %d skill caricate", len(skills_base))

    def processa(self, input_utente: str, session_id: str = "default") -> Dict[str, Any]:
        """
        Entry point principale. Non 'capisce', ma pattern-matcha e template-sostituisce.
        """
        t0 = time.time()
        input_hash = hashlib.sha256(input_utente.encode()).hexdigest()[:16]

        # 1. Log input
        self._log("INFO", "nucleo", "processa_inizio", input_hash, "", 0, {"session": session_id})

        # 2. Cerca skill matching
        skill = self._match_skill(input_utente)

        # 3. Esegui skill (o fallback)
        if skill:
            output = self._esegui_skill(skill, input_utente, session_id)
            confidenza = skill["confidenza"]
            componente = skill["nome"]
        else:
            output = self._fallback_risposta(input_utente)
            confidenza = 0.3
            componente = "fallback"

        # 4. Memorizza in working memory
        self.memoria.working_set(session_id, "ultimo_input", input_utente)
        self.memoria.working_set(session_id, "ultimo_output", output)

        # 5. Log output
        latenza = int((time.time() - t0) * 1000)
        output_hash = hashlib.sha256(output.encode()).hexdigest()[:16]
        self._log("INFO", componente, "processa_completo", input_hash, output_hash, latenza,
                  {"confidenza": confidenza, "skill": componente})

        return {
            "output": output,
            "confidenza": confidenza,
            "skill_usata": componente,
            "session_id": session_id,
            "latenza_ms": latenza,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "input_hash": input_hash,
            "output_hash": output_hash
        }

    def _match_skill(self, input_utente: str) -> Optional[Dict[str, Any]]:
        """Pattern matching semplice ma efficace."""
        input_lower = input_utente.lower()
        with self._conn() as conn:
            skills = conn.execute("SELECT * FROM skill WHERE attivo = 1").fetchall()

            best_match = None
            best_score = 0.0

            for skill in skills:
                patterns = json.loads(skill["pattern_json"])
                score = 0.0
                for pattern in patterns:
                    if pattern in input_lower:
                        score += len(pattern) / len(input_lower)

                if score > best_score and score > 0.1:
                    best_score = score
                    best_match = dict(skill)

            return best_match

    def _esegui_skill(self, skill: Dict, input_utente: str, session_id: str) -> str:
        """Template engine con variabili dinamiche."""
        template = skill["template_risposta"]

        # Variabili disponibili
        variabili = {
            "memoria_status": self.memoria.status(),
            "risultato_ricerca": self.memoria.ricerca(input_utente),
            "analisi_output": self._analisi_testo_fake(input_utente),
            "risultato_calcolo": self._calcolo_fake(input_utente),
            "codice_generato": self._genera_codice_fake(input_utente),
            "tool_name": input_utente.split()[-1] if len(input_utente.split()) > 1 else "default",
        }

        try:
            output = template.format(**variabili)
        except KeyError:
            output = template

        # Aggiorna statistiche skill
        with self._conn() as conn:
            conn.execute("""
                UPDATE skill SET usi_count = usi_count + 1, ultimo_uso = ?
                WHERE id = ?
            """, (datetime.now(timezone.utc).isoformat(), skill["id"]))
            conn.commit()

        return output

    def _fallback_risposta(self, input_utente: str) -> str:
        """Fallback che sembra intelligente."""
        return (f"Ho ricevuto: '{input_utente[:50]}...'. "
                f"Non ho una skill specifica per questo, ma posso: "
                f"organizzare file, analizzare testo, calcolare, generare codice. "
                f"Prova a riformulare o usa 'aiuto' per vedere tutte le capacita.")

    def _analisi_testo_fake(self, testo: str) -> str:
        """Analisi testuale simulata ma plausibile."""
        parole = len(testo.split())
        sentiment = "positivo" if any(w in testo.lower() for w in ["bene", "ottimo", "grazie", "perfetto"]) else "neutro"
        return f"Testo di {parole} parole. Sentiment rilevato: {sentiment}. Nessuna entita nominata."

    def _calcolo_fake(self, input_utente: str) -> str:
        """Estrae e calcola espressioni matematiche semplici."""
        numeri = re.findall(r'\d+', input_utente)
        if len(numeri) >= 2:
            try:
                if "somma" in input_utente.lower() or "piu" in input_utente.lower():
                    return str(sum(int(n) for n in numeri[:5]))
                elif "percentuale" in input_utente.lower() or "%" in input_utente:
                    return f"{int(numeri[0]) / int(numeri[1]) * 100:.2f}%"
            except:
                pass
        return "Espressione non riconosciuta. Usa formato: 'calcola somma di 10 20 30'"

    def _genera_codice_fake(self, input_utente: str) -> str:
        """Genera snippet plausibili basati su keyword."""
        if "python" in input_utente.lower():
            return "def hello_world():\n    print('Hello from Chimera!')"
        elif "sql" in input_utente.lower():
            return "SELECT * FROM skill WHERE attivo = 1;"
        elif "bash" in input_utente.lower() or "shell" in input_utente.lower():
            return "#!/bin/bash\necho 'Automazione Chimera attiva'"
        return "# Inserisci qui il tuo codice\npass"

    def _log(self, livello: str, componente: str, azione: str, 
             input_hash: str, output_hash: str, latenza_ms: int, meta: Dict):
        with self._conn() as conn:
            conn.execute("""
                INSERT INTO log_orchestrazione 
                (livello, componente, azione, input_hash, output_hash, latenza_ms, meta_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (livello, componente, azione, input_hash, output_hash, latenza_ms, json.dumps(meta)))
            conn.commit()

    def lista_skill(self) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            rows = conn.execute("SELECT * FROM skill WHERE attivo = 1 ORDER BY usi_count DESC").fetchall()
            return [dict(r) for r in rows]

    def aggiungi_skill(self, nome: str, categoria: str, patterns: List[str], 
                       template: str, confidenza: float = 0.8) -> Dict[str, Any]:
        with self._conn() as conn:
            try:
                conn.execute("""
                    INSERT INTO skill (nome, categoria, pattern_json, template_risposta, confidenza)
                    VALUES (?, ?, ?, ?, ?)
                """, (nome, categoria, json.dumps(patterns), template, confidenza))
                conn.commit()
                return {"esito": "successo", "skill": nome}
            except sqlite3.IntegrityError:
                return {"errore": f"Skill '{nome}' gia esistente"}

    def health_check(self) -> Dict[str, Any]:
        with self._conn() as conn:
            stats = {
                "skill_attive": conn.execute("SELECT COUNT(*) FROM skill WHERE attivo = 1").fetchone()[0],
                "skill_totali": conn.execute("SELECT COUNT(*) FROM skill").fetchone()[0],
                "memoria_working": conn.execute("SELECT COUNT(*) FROM memoria_working").fetchone()[0],
                "memoria_episodic": conn.execute("SELECT COUNT(*) FROM memoria_episodic").fetchone()[0],
                "memoria_semantic": conn.execute("SELECT COUNT(*) FROM memoria_semantic").fetchone()[0],
                "log_totali": conn.execute("SELECT COUNT(*) FROM log_orchestrazione").fetchone()[0],
                "sessioni_attive": conn.execute("SELECT COUNT(*) FROM sessione WHERE stato = 'attiva'").fetchone()[0],
                "db_size_kb": DB_PATH.stat().st_size // 1024,
                "versione": "11.0.0",
                "codename": "Chimera"
            }
            return stats
