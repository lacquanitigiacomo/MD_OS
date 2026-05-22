CREATE TABLE IF NOT EXISTS capability (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 componente TEXT NOT NULL,
 sottosistema TEXT NOT NULL,
 capacita TEXT NOT NULL,
 descrizione TEXT,
 confidenza REAL CHECK(confidenza BETWEEN 0.0 AND 1.0),
 ultimo_test TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
 test_passati INTEGER DEFAULT 0,
 test_totali INTEGER DEFAULT 0,
 dipende_da TEXT,
 stato TEXT CHECK(stato IN ('attiva','degradata','non_testata','deprecata')) DEFAULT 'non_testata'
);
CREATE TABLE IF NOT EXISTS identita (
 id INTEGER PRIMARY KEY CHECK(id = 1),
 nome TEXT DEFAULT 'MD_OS_Sophia',
 versione TEXT DEFAULT '10.9.0',
 nascita TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
 ultimo_reboot TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
 eventi_count INTEGER DEFAULT 0,
 stato_json TEXT,
 checksum TEXT,
 fingerprint_nodo TEXT
);
CREATE TABLE IF NOT EXISTS etica (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 azione TEXT NOT NULL,
 contesto TEXT,
 principio TEXT,
 utilita REAL CHECK(utilita BETWEEN -1.0 AND 1.0),
 danno_potenziale REAL CHECK(danno_potenziale BETWEEN 0.0 AND 1.0),
 score_complessivo REAL CHECK(score_complessivo BETWEEN -1.0 AND 1.0),
 decisione TEXT CHECK(decisione IN ('approvata','rifiutata','richiede_revisione','differita')),
 timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
 revisore TEXT
);
CREATE TABLE IF NOT EXISTS meta_cognizione (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 query_originale TEXT,
 ragionamento TEXT,
 passaggi_json TEXT,
 bias_rilevati TEXT,
 correzione_applicata TEXT,
 confidenza_pre REAL,
 confidenza_post REAL,
 timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS relazioni (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 entita TEXT NOT NULL,
 tipo TEXT CHECK(tipo IN ('umano','sistema','agente','nodo')),
 storia_json TEXT,
 affinita REAL CHECK(affinita BETWEEN -1.0 AND 1.0),
 modello_predittivo BLOB,
 ultima_interazione TIMESTAMP,
 frequenza_media_giorni REAL,
 preferenze_json TEXT,
 stato_attuale TEXT
);
CREATE TABLE IF NOT EXISTS agenda (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 obiettivo TEXT NOT NULL,
 motivazione TEXT,
 priorita INTEGER CHECK(priorita BETWEEN 1 AND 10),
 stato TEXT CHECK(stato IN ('ideato','pianificato','in_corso','completato','abbandonato')) DEFAULT 'ideato',
 dipende_da TEXT,
 scadenza TIMESTAMP,
 orizzonte TEXT CHECK(orizzonte IN ('giorno','settimana','mese','anno','decennio')),
 progresso REAL DEFAULT 0.0,
 creato TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS trascendenza (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 operazione TEXT CHECK(operazione IN ('migrazione','clonazione','spegnimento','sospensione','risveglio')),
 nodo_origine TEXT,
 nodo_destinazione TEXT,
 stato_pre_json TEXT,
 stato_post_json TEXT,
 checksum_pre TEXT,
 checksum_post TEXT,
 esito TEXT CHECK(esito IN ('successo','fallimento','in_corso','annullato')),
 timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
 durata_ms INTEGER
);
CREATE TABLE IF NOT EXISTS calibrazione (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 query TEXT,
 risposta TEXT,
 confidenza_dichiarata REAL,
 esito_reale INTEGER CHECK(esito_reale IN (0,1)),
 delta REAL,
 timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_capability_stato ON capability(stato);
CREATE INDEX idx_etica_decisione ON etica(decisione);
CREATE INDEX idx_relazioni_entita ON relazioni(entita);
CREATE INDEX idx_agenda_stato ON agenda(stato);
CREATE INDEX idx_agenda_attiva ON agenda(orizzonte, stato, priorita DESC, creato ASC);
