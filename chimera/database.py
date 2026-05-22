"""Local-first SQLite persistence."""
import os
import sqlite3
from pathlib import Path


def get_db_path():
    """Return absolute Path to SQLite database.

    Priority:
      1. CHIMERA_DB_PATH environment variable.
      2. ./data/chimera.db relative to project root.
    """
    env = os.getenv("CHIMERA_DB_PATH")
    if env:
        return Path(env).resolve()
    # Resolve relative to this file: chimera/database.py -> ../data/chimera.db
    return (Path(__file__).parent.parent / "data" / "chimera.db").resolve()


def init_db(db_path=None):
    """Initialize SQLite schema if not present.

    Args:
        db_path: Override database path. Defaults to get_db_path().
    """
    db_path = db_path or get_db_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.executescript(
        """
        CREATE TABLE IF NOT EXISTS nodes (
            id TEXT PRIMARY KEY,
            type TEXT NOT NULL,
            config TEXT,
            status TEXT DEFAULT 'idle'
        );

        CREATE TABLE IF NOT EXISTS connections (
            from_node TEXT NOT NULL,
            to_node TEXT NOT NULL,
            weight REAL DEFAULT 1.0,
            PRIMARY KEY (from_node, to_node)
        );

        CREATE TABLE IF NOT EXISTS execution_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            node_id TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            status TEXT,
            payload TEXT
        );

        CREATE INDEX IF NOT EXISTS idx_log_node ON execution_log(node_id);
        CREATE INDEX IF NOT EXISTS idx_log_time ON execution_log(timestamp);
        """
    )
    conn.commit()
    conn.close()
    return db_path
