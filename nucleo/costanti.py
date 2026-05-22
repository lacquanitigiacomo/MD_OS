# nucleo/costanti.py
# VERSIONE: 12.0.0 - SCHEMA CONGELATO PERMANENTE
# Questo file non cambia mai. Mai. Nemmeno per bugfix.
# Se c'e' un bug, si aggiunge un plugin di workaround.

from pathlib import Path

RADICE = Path(__file__).parent.parent

# Percorsi congelati
DATABASE = RADICE / "dataset" / "mdos.db"
CARTELLA_PLUGIN = RADICE / "plugin"
CARTELLA_LOG = RADICE / "log"
CARTELLA_CACHE = RADICE / "cache"
CARTELLA_MODELLO = RADICE / "modello"
CONFIG = RADICE / "config.yaml"

VERSIONE_NUCLEO = "12.0.0"

# Schema base SQLite - immutabile
SCHEMA_BASE = """
PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS nucleo_meta (
    chiave TEXT PRIMARY KEY,
    valore TEXT,
    aggiornato TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS nucleo_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT DEFAULT (datetime('now')),
    livello TEXT,
    modulo TEXT,
    azione TEXT,
    dettaglio TEXT,
    traccia TEXT
);

CREATE TABLE IF NOT EXISTS nucleo_plugin (
    nome TEXT PRIMARY KEY,
    versione TEXT,
    percorso TEXT,
    attivo INTEGER DEFAULT 1,
    caricato TEXT DEFAULT (datetime('now'))
);
"""
