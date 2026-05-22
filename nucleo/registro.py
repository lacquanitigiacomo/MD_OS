# nucleo/registro.py
# Registro transazionale con pool di connessioni.

import sqlite3
import threading
from contextlib import contextmanager
from .costanti import DATABASE, SCHEMA_BASE

class Registro:
    _istanza = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._istanza is None:
            with cls._lock:
                if cls._istanza is None:
                    cls._istanza = super().__new__(cls)
                    cls._istanza._inizializza()
        return cls._istanza

    def _inizializza(self):
        self._pool = {}
        self._pool_lock = threading.Lock()
        self._verifica_schema()

    def _connessione(self):
        tid = threading.current_thread().ident
        with self._pool_lock:
            if tid not in self._pool:
                conn = sqlite3.connect(DATABASE, check_same_thread=False)
                conn.row_factory = sqlite3.Row
                conn.executescript(SCHEMA_BASE)
                conn.execute("PRAGMA journal_mode=WAL")
                conn.execute("PRAGMA synchronous=NORMAL")
                self._pool[tid] = conn
            return self._pool[tid]

    def _verifica_schema(self):
        conn = self._connessione()
        cursore = conn.execute("SELECT valore FROM nucleo_meta WHERE chiave='schema_version'")
        if cursore.fetchone() is None:
            conn.execute("INSERT INTO nucleo_meta (chiave, valore) VALUES (?, ?)", ("schema_version", "12"))
            conn.commit()

    @contextmanager
    def transazione(self):
        conn = self._connessione()
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e

    def esegui(self, query, parametri=()):
        with self.transazione() as conn:
            return conn.execute(query, parametri)

    def interroga(self, query, parametri=()):
        conn = self._connessione()
        cursore = conn.execute(query, parametri)
        return [dict(riga) for riga in cursore.fetchall()]

    def inserisci(self, tabella, dati: dict):
        colonne = ", ".join(dati.keys())
        placeholder = ", ".join(["?" for _ in dati])
        query = f"INSERT INTO {tabella} ({colonne}) VALUES ({placeholder})"
        with self.transazione() as conn:
            cursore = conn.execute(query, tuple(dati.values()))
            return cursore.lastrowid

registro = Registro()
