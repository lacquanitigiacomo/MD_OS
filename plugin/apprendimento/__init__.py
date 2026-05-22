# plugin/apprendimento/__init__.py
# Rete neurale locale con backpropagation custom.
# Addestramento sui dati del sistema, zero rete, zero API esterne.
# VERSIONE: 2.0.0

import json
import math
import random
import pickle
from pathlib import Path
from collections import defaultdict
from nucleo.registro import registro
from nucleo.guardiano import guardiano
from nucleo.costanti import CARTELLA_CACHE
from plugin.memoria import motore_embedding

VERSIONE = "2.0.0"

# ============================================================
# RETE NEURALE CUSTOM - MLP con backpropagation
# ============================================================
# Implementazione da zero in puro Python. Zero framework ML.
# Addestramento su feedback utente e pattern dai log.
# ============================================================

class ReteNeurale:
    def __init__(self, architettura, tasso_apprendimento=0.01):
        self.architettura = architettura
        self.lr = tasso_apprendimento
        self.pesi = []
        self.bias = []
        self._inizializza()

    def _inizializza(self):
        for i in range(len(self.architettura) - 1):
            n_in, n_out = self.architettura[i], self.architettura[i + 1]
            limite = math.sqrt(6.0 / (n_in + n_out))
            peso = [[random.uniform(-limite, limite) for _ in range(n_out)] for _ in range(n_in)]
            self.pesi.append(peso)
            self.bias.append([0.0] * n_out)

    def _sigmoid(self, x):
        return 1.0 / (1.0 + math.exp(-max(-500, min(500, x))))

    def _sigmoid_derivata(self, x):
        s = self._sigmoid(x)
        return s * (1.0 - s)

    def _relu(self, x):
        return max(0.0, x)

    def _relu_derivata(self, x):
        return 1.0 if x > 0 else 0.0

    def forward(self, input_vettore):
        attivazioni = [input_vettore]
        z_vals = []

        current = input_vettore
        for i, (peso, bias) in enumerate(zip(self.pesi, self.bias)):
            z = []
            for j in range(len(bias)):
                somma = bias[j]
                for k in range(len(current)):
                    somma += current[k] * peso[k][j]
                z.append(somma)

            z_vals.append(z)

            if i == len(self.pesi) - 1:
                current = [self._sigmoid(val) for val in z]
            else:
                current = [self._relu(val) for val in z]

            attivazioni.append(current)

        return current, attivazioni, z_vals

    def backward(self, input_vettore, target):
        output, attivazioni, z_vals = self.forward(input_vettore)

        errore = [output[j] - target[j] for j in range(len(target))]

        delta = [[] for _ in range(len(self.pesi))]

        delta[-1] = [errore[j] * self._sigmoid_derivata(z_vals[-1][j]) 
                     for j in range(len(errore))]

        for l in range(len(self.pesi) - 2, -1, -1):
            delta[l] = []
            for j in range(len(self.bias[l])):
                somma = 0.0
                for k in range(len(delta[l + 1])):
                    somma += delta[l + 1][k] * self.pesi[l + 1][j][k]
                delta[l].append(somma * self._relu_derivata(z_vals[l][j]))

        grad_pesi = []
        grad_bias = []

        for l in range(len(self.pesi)):
            gp = [[0.0] * len(self.pesi[l][0]) for _ in range(len(self.pesi[l]))]
            gb = [0.0] * len(self.bias[l])

            for j in range(len(self.bias[l])):
                gb[j] = delta[l][j]
                for k in range(len(attivazioni[l])):
                    gp[k][j] = delta[l][j] * attivazioni[l][k]

            grad_pesi.append(gp)
            grad_bias.append(gb)

        return grad_pesi, grad_bias

    def addestra(self, input_vettore, target):
        grad_pesi, grad_bias = self.backward(input_vettore, target)

        for l in range(len(self.pesi)):
            for j in range(len(self.pesi[l][0])):
                self.bias[l][j] -= self.lr * grad_bias[l][j]
                for k in range(len(self.pesi[l])):
                    self.pesi[l][k][j] -= self.lr * grad_pesi[l][k][j]

    def predici(self, input_vettore):
        output, _, _ = self.forward(input_vettore)
        return output

    def salva(self, percorso):
        with open(percorso, 'wb') as f:
            pickle.dump({
                'architettura': self.architettura,
                'lr': self.lr,
                'pesi': self.pesi,
                'bias': self.bias
            }, f)

    @classmethod
    def carica(cls, percorso):
        with open(percorso, 'rb') as f:
            dati = pickle.load(f)
        rete = cls(dati['architettura'], dati['lr'])
        rete.pesi = dati['pesi']
        rete.bias = dati['bias']
        return rete

# ============================================================
# ENGINE APPRENDIMENTO
# ============================================================

class EngineApprendimento:
    def __init__(self):
        self.rete_valutazione = None
        self._carica_modello()

    def _carica_modello(self):
        percorso = CARTELLA_CACHE / "rete_valutazione.pkl"
        if percorso.exists():
            self.rete_valutazione = ReteNeurale.carica(percorso)
            guardiano.logga("INFO", "apprendimento", "modello_caricato", "Rete valutazione esistente")
        else:
            self.rete_valutazione = ReteNeurale([384, 128, 64, 16, 1], 0.001)
            guardiano.logga("INFO", "apprendimento", "modello_nuovo", "Rete valutazione inizializzata")

    def valuta_risposta(self, query, risposta, contesto):
        import numpy as np
        vettore_query = motore_embedding.codifica(query)
        vettore_risposta = motore_embedding.codifica(risposta)

        similarita = self._similarita_coseno(vettore_query, vettore_risposta)
        lunghezza_norm = min(len(risposta) / 1000, 1.0)

        input_rete = list(vettore_query[:380]) + [similarita, lunghezza_norm]

        score = self.rete_valutazione.predici(input_rete)[0]
        return score

    def addestra_feedback(self, query, risposta, feedback_utente, contesto):
        import numpy as np
        vettore_query = motore_embedding.codifica(query)
        vettore_risposta = motore_embedding.codifica(risposta)

        similarita = self._similarita_coseno(vettore_query, vettore_risposta)
        lunghezza_norm = min(len(risposta) / 1000, 1.0)

        input_rete = list(vettore_query[:380]) + [similarita, lunghezza_norm]

        for _ in range(10):
            self.rete_valutazione.addestra(input_rete, [feedback_utente])

        self.rete_valutazione.salva(CARTELLA_CACHE / "rete_valutazione.pkl")

        guardiano.logga("INFO", "apprendimento", "addestramento", 
                        f"Feedback {feedback_utente} per query '{query[:50]}...'")

    @staticmethod
    def _similarita_coseno(a, b):
        import numpy as np
        a, b = np.array(a), np.array(b)
        na, nb = np.linalg.norm(a), np.linalg.norm(b)
        if na == 0 or nb == 0:
            return 0.0
        return float(np.dot(a, b) / (na * nb))

engine_apprendimento = EngineApprendimento()

# ============================================================
# COMANDI
# ============================================================

def impara(argomenti):
    testo = argomenti.get("testo")
    if not testo:
        return "Specifica --testo '...'"

    registro.esegui("""
        CREATE TABLE IF NOT EXISTS apprendimento_knowledge (
            id INTEGER PRIMARY KEY,
            testo TEXT,
            vettore BLOB,
            fonte TEXT,
            validato INTEGER DEFAULT 0,
            utilizzi INTEGER DEFAULT 0,
            timestamp TEXT DEFAULT (datetime('now'))
        )
    """)

    vettore = motore_embedding.codifica(testo).tobytes()

    registro.esegui("""
        INSERT INTO apprendimento_knowledge (testo, vettore, fonte) VALUES (?, ?, ?)
    """, (testo, vettore, 'manuale'))

    guardiano.logga("INFO", "apprendimento", "impara", f"Nuova conoscenza: {testo[:50]}...")
    return "Conoscenza registrata e indicizzata."

def feedback(argomenti):
    pos = argomenti.get("argomenti_posizionali", [])
    if len(pos) < 3:
        return "Uso: apprendimento.feedback <query> <risposta> <punteggio_0_1>"

    query = pos[0]
    risposta = pos[1]
    try:
        punteggio = float(pos[2])
        punteggio = max(0.0, min(1.0, punteggio))
    except ValueError:
        return "Punteggio deve essere tra 0.0 e 1.0"

    registro.esegui("""
        CREATE TABLE IF NOT EXISTS apprendimento_feedback (
            id INTEGER PRIMARY KEY,
            query TEXT,
            risposta TEXT,
            punteggio REAL,
            contesto TEXT,
            timestamp TEXT DEFAULT (datetime('now'))
        )
    """)

    registro.esegui("""
        INSERT INTO apprendimento_feedback (query, risposta, punteggio, contesto) 
        VALUES (?, ?, ?, ?)
    """, (query, risposta, punteggio, json.dumps({})))

    engine_apprendimento.addestra_feedback(query, risposta, punteggio, {})

    return f"Feedback registrato: {punteggio}. Rete addestrata."

def valuta(argomenti):
    pos = argomenti.get("argomenti_posizionali", [])
    if len(pos) < 2:
        return "Uso: apprendimento.valuta <query> <risposta>"

    query = pos[0]
    risposta = pos[1]

    score = engine_apprendimento.valuta_risposta(query, risposta, {})

    return f"Valutazione rete neurale: {score:.3f} (0=pessimo, 1=ottimo)"

def pattern(argomenti):
    query_recenti = registro.interroga("""
        SELECT query, COUNT(*) as freq, AVG(punteggio) as avg_score
        FROM apprendimento_feedback
        WHERE timestamp > datetime('now', '-7 days')
        GROUP BY query
        ORDER BY freq DESC
        LIMIT 20
    """)

    if not query_recenti:
        return "Nessun feedback recente."

    output = ["Pattern rilevati (ultimi 7 giorni):"]
    for q in query_recenti:
        output.append(f"  {q['freq']}x | score {q['avg_score']:.2f} | {q['query'][:60]}...")

    return "
".join(output)

COMANDI = {
    "apprendimento.impara": impara,
    "apprendimento.feedback": feedback,
    "apprendimento.valuta": valuta,
    "apprendimento.pattern": pattern,
}
