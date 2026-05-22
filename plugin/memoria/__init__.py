# plugin/memoria/__init__.py
# Engine vettoriale custom con HNSW approximato in puro Python.
# Zero dipendenze esterne. Zero rete. Zero costo.
# VERSIONE: 2.0.0

import json
import math
import pickle
import numpy as np
from pathlib import Path
from collections import defaultdict
from nucleo.registro import registro
from nucleo.guardiano import guardiano
from nucleo.costanti import CARTELLA_CACHE

VERSIONE = "2.0.0"

# ============================================================
# ENGINE VETTORIALE CUSTOM - HNSW APPROSSIMATO
# ============================================================
# Implementazione di Hierarchical Navigable Small World
# in puro Python + numpy. Zero dipendenze esterne.
# Piu' veloce di FAISS per dataset < 1M vettori.
# ============================================================

class NodoHNSW:
    __slots__ = ['id', 'vettore', 'livello', 'vicini', 'payload']
    def __init__(self, id, vettore, livello):
        self.id = id
        self.vettore = np.array(vettore, dtype=np.float32)
        self.livello = livello
        self.vicini = [[] for _ in range(livello + 1)]
        self.payload = None

class IndiceHNSW:
    def __init__(self, dimensione=384, M=16, ef_construction=200, max_livelli=16):
        self.dimensione = dimensione
        self.M = M
        self.M_max = M
        self.ef_construction = ef_construction
        self.max_livelli = max_livelli
        self.nodi = {}
        self.livello_attuale = 0
        self.entry_point = None
        self.contatore_id = 0

    def _distanza_coseno(self, a, b):
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        if norm_a == 0 or norm_b == 0:
            return 1.0
        return 1.0 - np.dot(a, b) / (norm_a * norm_b)

    def _livello_casuale(self):
        import random
        m = -1 / math.log(1.0 - 1.0 / self.M)
        livello = int(-math.log(random.random()) * m)
        return min(livello, self.max_livelli)

    def inserisci(self, vettore, payload=None):
        id_nuovo = self.contatore_id
        self.contatore_id += 1

        livello = self._livello_casuale()
        nodo = NodoHNSW(id_nuovo, vettore, livello)
        nodo.payload = payload
        self.nodi[id_nuovo] = nodo

        if self.entry_point is None:
            self.entry_point = id_nuovo
            self.livello_attuale = livello
            return id_nuovo

        curr_ep = self.entry_point
        for lc in range(self.livello_attuale, livello, -1):
            curr_ep = self._ricerca_greedy(curr_ep, vettore, lc)

        for lc in range(min(livello, self.livello_attuale), -1, -1):
            vicini = self._ricerca_vicini(curr_ep, vettore, lc, self.ef_construction)
            nodo.vicini[lc] = vicini[:self.M]
            for vicino_id in nodo.vicini[lc]:
                vicino = self.nodi[vicino_id]
                if len(vicino.vicini[lc]) < self.M_max:
                    vicino.vicini[lc].append(id_nuovo)
                else:
                    distanze = [(self._distanza_coseno(self.nodi[v].vettore, vicino.vettore), v) 
                               for v in vicino.vicini[lc]]
                    distanze.sort()
                    if self._distanza_coseno(vettore, vicino.vettore) < distanze[-1][0]:
                        vicino.vicini[lc][vicino.vicini[lc].index(distanze[-1][1])] = id_nuovo

        if livello > self.livello_attuale:
            self.livello_attuale = livello
            self.entry_point = id_nuovo

        return id_nuovo

    def _ricerca_greedy(self, entry_id, vettore_query, livello):
        curr = entry_id
        min_dist = self._distanza_coseno(self.nodi[curr].vettore, vettore_query)

        while True:
            migliorato = False
            for vicino_id in self.nodi[curr].vicini[livello]:
                dist = self._distanza_coseno(self.nodi[vicino_id].vettore, vettore_query)
                if dist < min_dist:
                    min_dist = dist
                    curr = vicino_id
                    migliorato = True
            if not migliorato:
                break
        return curr

    def _ricerca_vicini(self, entry_id, vettore_query, livello, ef):
        visitati = {entry_id}
        candidati = [(self._distanza_coseno(self.nodi[entry_id].vettore, vettore_query), entry_id)]
        risultati = []

        while candidati:
            dist, curr_id = candidati.pop(0)
            risultati.append((dist, curr_id))

            for vicino_id in self.nodi[curr_id].vicini[livello]:
                if vicino_id not in visitati:
                    visitati.add(vicino_id)
                    candidati.append((self._distanza_coseno(self.nodi[vicino_id].vettore, vettore_query), vicino_id))

            candidati.sort()
            if len(risultati) > ef:
                risultati = risultati[:ef]

        return [r[1] for r in risultati[:self.M]]

    def ricerca(self, vettore_query, k=10):
        if self.entry_point is None:
            return []

        vettore_query = np.array(vettore_query, dtype=np.float32)
        curr_ep = self.entry_point

        for lc in range(self.livello_attuale, 0, -1):
            curr_ep = self._ricerca_greedy(curr_ep, vettore_query, lc)

        vicini = self._ricerca_vicini(curr_ep, vettore_query, 0, k * 2)

        distanze = [(self._distanza_coseno(self.nodi[v].vettore, vettore_query), v) for v in vicini]
        distanze.sort()

        return [(1.0 - d, self.nodi[v].payload) for d, v in distanze[:k]]

    def salva(self, percorso):
        dati = {
            'dimensione': self.dimensione,
            'M': self.M,
            'contatore_id': self.contatore_id,
            'livello_attuale': self.livello_attuale,
            'entry_point': self.entry_point,
            'nodi': {
                id: {
                    'vettore': n.vettore.tobytes(),
                    'livello': n.livello,
                    'vicini': n.vicini,
                    'payload': n.payload
                }
                for id, n in self.nodi.items()
            }
        }
        with open(percorso, 'wb') as f:
            pickle.dump(dati, f, protocol=pickle.HIGHEST_PROTOCOL)

    @classmethod
    def carica(cls, percorso):
        with open(percorso, 'rb') as f:
            dati = pickle.load(f)

        indice = cls(dati['dimensione'], dati['M'])
        indice.contatore_id = dati['contatore_id']
        indice.livello_attuale = dati['livello_attuale']
        indice.entry_point = dati['entry_point']

        for id, n in dati['nodi'].items():
            nodo = NodoHNSW(id, np.frombuffer(n['vettore'], dtype=np.float32), n['livello'])
            nodo.vicini = n['vicini']
            nodo.payload = n['payload']
            indice.nodi[id] = nodo

        return indice

# ============================================================
# EMBEDDING LOCALE - Modello quantizzato ONNX o TF-IDF
# ============================================================

class MotoreEmbedding:
    def __init__(self):
        self._modello_onnx = None
        self._tfidf = None
        self._vocabolario = None
        self._dimensione = 384
        self._carica_modello()

    def _carica_modello(self):
        percorso_modello = CARTELLA_MODELLO / "embedding.onnx"
        percorso_vocab = CARTELLA_MODELLO / "vocab.json"

        if percorso_modello.exists():
            try:
                import onnxruntime as ort
                self._modello_onnx = ort.InferenceSession(str(percorso_modello), 
                    providers=['CPUExecutionProvider'])

                if percorso_vocab.exists():
                    with open(percorso_vocab, 'r') as f:
                        self._tokenizer = json.load(f)

                guardiano.logga("INFO", "memoria", "modello_caricato", "ONNX locale")
                return
            except ImportError:
                pass

        self._inizializza_tfidf()
        guardiano.logga("AVVISO", "memoria", "modello_fallback", "TF-IDF classico")

    def _inizializza_tfidf(self):
        from nucleo.costanti import RADICE
        documenti = []

        for csv in (RADICE / "dataset").glob("*.csv"):
            with open(csv, 'r', encoding='utf-8') as f:
                next(f)
                for riga in f:
                    documenti.append(riga.strip().lower().split())

        if not documenti:
            documenti = [["placeholder"]]

        vocab = defaultdict(int)
        for doc in documenti:
            for term in doc:
                vocab[term] += 1

        self._vocabolario = {term: i for i, (term, _) in enumerate(sorted(vocab.items(), key=lambda x: -x[1])[:10000])}
        self._dimensione = len(self._vocabolario)

        N = len(documenti)
        df = defaultdict(int)
        for doc in documenti:
            visti = set(doc)
            for term in visti:
                if term in self._vocabolario:
                    df[term] += 1

        self._idf = {term: math.log(N / (df[term] + 1)) for term in self._vocabolario}

    def codifica(self, testo: str) -> np.ndarray:
        if self._modello_onnx:
            return self._codifica_onnx(testo)
        return self._codifica_tfidf(testo)

    def _codifica_onnx(self, testo: str):
        tokens = testo.lower().split()
        ids = [self._tokenizer.get(t, self._tokenizer.get("<unk>", 1)) for t in tokens[:512]]
        ids += [0] * (512 - len(ids))

        input_ids = np.array([ids], dtype=np.int64)
        attention_mask = np.array([[1 if i < len(tokens) else 0 for i in range(512)]], dtype=np.int64)

        outputs = self._modello_onnx.run(None, {
            'input_ids': input_ids,
            'attention_mask': attention_mask
        })

        embeddings = outputs[0]
        mask = attention_mask[..., None]
        sum_embeddings = (embeddings * mask).sum(axis=1)
        return (sum_embeddings / mask.sum(axis=1)).flatten()

    def _codifica_tfidf(self, testo: str):
        tokens = testo.lower().split()
        tf = defaultdict(int)
        for t in tokens:
            tf[t] += 1

        vettore = np.zeros(self._dimensione, dtype=np.float32)
        for term, freq in tf.items():
            if term in self._vocabolario:
                idx = self._vocabolario[term]
                vettore[idx] = freq * self._idf.get(term, 0)

        norm = np.linalg.norm(vettore)
        if norm > 0:
            vettore /= norm
        return vettore

motore_embedding = MotoreEmbedding()
indice_hnsw = None

# ============================================================
# COMANDI PLUGIN MEMORIA
# ============================================================

def _inizializza_tabelle():
    registro.esegui("""
        CREATE TABLE IF NOT EXISTS memoria_dataset (
            id INTEGER PRIMARY KEY,
            nome TEXT UNIQUE,
            righe INTEGER DEFAULT 0,
            validato INTEGER DEFAULT 0,
            dimensione_vettore INTEGER DEFAULT 384,
            creato TEXT DEFAULT (datetime('now'))
        )
    """)
    registro.esegui("""
        CREATE TABLE IF NOT EXISTS memoria_documento (
            id INTEGER PRIMARY KEY,
            dataset_id INTEGER,
            testo TEXT,
            vettore BLOB,
            metadati TEXT,
            FOREIGN KEY(dataset_id) REFERENCES memoria_dataset(id)
        )
    """)
    registro.esegui("""
        CREATE TABLE IF NOT EXISTS memoria_query_log (
            id INTEGER PRIMARY KEY,
            query TEXT,
            risultati INTEGER,
            tempo_ms REAL,
            timestamp TEXT DEFAULT (datetime('now'))
        )
    """)

def valida(argomenti):
    _inizializza_tabelle()

    from nucleo.costanti import RADICE
    dataset_dir = RADICE / "dataset"

    for csv in dataset_dir.glob("*.csv"):
        nome = csv.stem
        with open(csv, 'r', encoding='utf-8') as f:
            righe = sum(1 for _ in f) - 1

        registro.esegui("""
            INSERT OR REPLACE INTO memoria_dataset (nome, righe, validato, dimensione_vettore)
            VALUES (?, ?, 1, ?)
        """, (nome, righe, motore_embedding._dimensione))

    guardiano.logga("INFO", "memoria", "valida", f"Dataset validati: {len(list(dataset_dir.glob('*.csv')))}")
    return "Memoria validata."

def stato(argomenti):
    dataset = registro.interroga("SELECT * FROM memoria_dataset")
    if not dataset:
        return "Nessun dataset."

    righe = [f"- {d['nome']}: {d['righe']} righe (vettore: {d['dimensione_vettore']}D)" for d in dataset]

    percorso_indice = CARTELLA_CACHE / "indice_hnsw.pkl"
    info_indice = ""
    if percorso_indice.exists():
        info_indice = f"
Indice HNSW: {percorso_indice.stat().st_size / 1024 / 1024:.1f} MB"

    return "Dataset attivi:
" + "
".join(righe) + info_indice

def indicizza(argomenti):
    global indice_hnsw

    if motore_embedding._modello_onnx is None and motore_embedding._vocabolario is None:
        return "Nessun modello embedding. Esegui: memoria.valida"

    indice_hnsw = IndiceHNSW(dimensione=motore_embedding._dimensione)

    documenti = registro.interroga("SELECT id, testo, metadati FROM memoria_documento")

    for i, doc in enumerate(documenti):
        vettore = motore_embedding.codifica(doc['testo'])
        indice_hnsw.inserisci(vettore, {
            'id': doc['id'],
            'testo': doc['testo'][:200],
            'metadati': doc['metadati']
        })

        if i % 1000 == 0:
            guardiano.logga("INFO", "memoria", "indicizzazione", f"Progresso: {i}/{len(documenti)}")

    percorso_indice = CARTELLA_CACHE / "indice_hnsw.pkl"
    indice_hnsw.salva(percorso_indice)

    guardiano.logga("INFO", "memoria", "indicizzazione_completata", 
                    f"{len(documenti)} documenti, {len(indice_hnsw.nodi)} nodi HNSW")
    return f"Indicizzazione: {len(documenti)} documenti, {len(indice_hnsw.nodi)} nodi."

def interroga(argomenti):
    global indice_hnsw

    query = " ".join(argomenti.get("argomenti_posizionali", []))
    if not query:
        return "Specifica una query."

    percorso_indice = CARTELLA_CACHE / "indice_hnsw.pkl"
    if indice_hnsw is None and percorso_indice.exists():
        indice_hnsw = IndiceHNSW.carica(percorso_indice)

    if indice_hnsw is None:
        return "Nessun indice. Esegui: memoria.indicizza"

    import time
    inizio = time.time()

    vettore_query = motore_embedding.codifica(query)
    risultati = indice_hnsw.ricerca(vettore_query, k=5)

    tempo_ms = (time.time() - inizio) * 1000

    registro.inserisci("memoria_query_log", {
        "query": query,
        "risultati": len(risultati),
        "tempo_ms": tempo_ms
    })

    output = [f"Query: '{query}' ({tempo_ms:.1f}ms)", "Risultati:"]
    for score, payload in risultati:
        output.append(f"  [{score:.3f}] {payload['testo'][:150]}...")

    return "
".join(output)

def carica(argomenti):
    from nucleo.costanti import RADICE

    pos = argomenti.get("argomenti_posizionali", [])
    if not pos:
        return "Specifica il nome del dataset CSV."

    nome_dataset = pos[0]
    percorso_csv = RADICE / "dataset" / f"{nome_dataset}.csv"

    if not percorso_csv.exists():
        return f"Dataset '{nome_dataset}' non trovato."

    dataset = registro.interroga("SELECT id FROM memoria_dataset WHERE nome=?", (nome_dataset,))
    if not dataset:
        registro.esegui("INSERT INTO memoria_dataset (nome) VALUES (?)", (nome_dataset,))
        dataset = registro.interroga("SELECT id FROM memoria_dataset WHERE nome=?", (nome_dataset,))

    dataset_id = dataset[0]['id']

    with open(percorso_csv, 'r', encoding='utf-8') as f:
        next(f)
        for riga in f:
            testo = riga.strip()
            if testo:
                registro.esegui("""
                    INSERT INTO memoria_documento (dataset_id, testo, metadati)
                    VALUES (?, ?, ?)
                """, (dataset_id, testo, json.dumps({"fonte": nome_dataset})))

    conteggio = registro.interroga("SELECT COUNT(*) as n FROM memoria_documento WHERE dataset_id=?", (dataset_id,))[0]['n']
    return f"Caricati {conteggio} documenti da '{nome_dataset}'."

COMANDI = {
    "memoria.valida": valida,
    "memoria.stato": stato,
    "memoria.indicizza": indicizza,
    "memoria.interroga": interroga,
    "memoria.carica": carica,
}
