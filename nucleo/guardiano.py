# nucleo/guardiano.py
# Guardiano: audit, validazione, sandbox, rate limiting.

import json
import hashlib
import time
from datetime import datetime
from collections import defaultdict
from .registro import registro
from .costanti import CARTELLA_LOG

class Guardiano:
    LIVELLI = {"DEBUG": 10, "INFO": 20, "AVVISO": 30, "ERRORE": 40, "CRITICO": 50}

    def __init__(self):
        self._rate_limit = defaultdict(list)
        self._soglia_rate = 100

    def _verifica_rate_limit(self, modulo: str):
        ora = time.time()
        self._rate_limit[modulo] = [t for t in self._rate_limit[modulo] if ora - t < 60]
        if len(self._rate_limit[modulo]) >= self._soglia_rate:
            raise RuntimeError(f"Rate limit superato per modulo '{modulo}'")
        self._rate_limit[modulo].append(ora)

    def logga(self, livello: str, modulo: str, azione: str, dettaglio: str, traccia: str = ""):
        self._verifica_rate_limit(modulo)

        if livello not in self.LIVELLI:
            livello = "INFO"

        hash_integrita = hashlib.sha256(f"{modulo}:{azione}:{dettaglio}:{datetime.now().isoformat()}".encode()).hexdigest()[:16]

        registro.inserisci("nucleo_log", {
            "livello": livello,
            "modulo": modulo,
            "azione": azione,
            "dettaglio": dettaglio,
            "traccia": traccia
        })

        import os
        os.makedirs(CARTELLA_LOG, exist_ok=True)
        percorso = CARTELLA_LOG / f"{datetime.now().strftime('%Y-%m')}.jsonl"
        with open(percorso, "a", encoding="utf-8") as f:
            f.write(json.dumps({
                "timestamp": datetime.now().isoformat(),
                "livello": livello,
                "modulo": modulo,
                "azione": azione,
                "dettaglio": dettaglio,
                "hash": hash_integrita
            }, ensure_ascii=False) + "\n")

    def valida(self, condizione: bool, messaggio: str, modulo: str = "guardiano"):
        if not condizione:
            self.logga("ERRORE", modulo, "validazione_fallita", messaggio)
            raise ValueError(messaggio)
        self.logga("INFO", modulo, "validazione_passata", messaggio)
        return True

    def sandbox(self, funzione, *args, **kwargs):
        import signal

        def handler(signum, frame):
            raise TimeoutError("Sandbox timeout")

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(30)

        try:
            risultato = funzione(*args, **kwargs)
            signal.alarm(0)
            return risultato
        except Exception as e:
            signal.alarm(0)
            self.logga("ERRORE", "sandbox", "esecuzione_fallita", str(e))
            raise

guardiano = Guardiano()
