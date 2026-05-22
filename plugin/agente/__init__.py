# plugin/agente/__init__.py
# Engine agenti con grafo di conoscenza, ragionamento a catena,
# orchestrazione multi-agente e competenze specializzate.
# VERSIONE: 2.1.0

import json
import yaml
import re
from pathlib import Path
from collections import defaultdict, deque
from nucleo.registro import registro
from nucleo.guardiano import guardiano
from plugin.memoria import motore_embedding, indice_hnsw

VERSIONE = "2.1.0"
CARTELLA_AGENTI = Path(__file__).parent / "definizioni"

# ============================================================
# GRAFO DI CONOSCENZA - Rete semantica interna
# ============================================================

class GrafoConoscenza:
    def __init__(self):
        self.nodi = {}
        self.archi = defaultdict(list)
        self._indice_inverso = defaultdict(set)

    def aggiungi_nodo(self, id_nodo, testo, vettore, tipo="fatto", metadati=None):
        self.nodi[id_nodo] = {
            'testo': testo,
            'vettore': vettore,
            'tipo': tipo,
            'metadati': metadati or {}
        }
        for term in testo.lower().split():
            self._indice_inverso[term].add(id_nodo)

    def aggiungi_arco(self, da, a, peso=1.0, tipo="correlazione"):
        self.archi[da].append((a, peso, tipo))
        self.archi[a].append((da, peso, tipo))

    def percorso_piu_corto(self, inizio, fine, max_passi=5):
        if inizio not in self.nodi or fine not in self.nodi:
            return None

        visitati = {inizio}
        coda = deque([(inizio, [inizio], 0.0)])

        while coda:
            attuale, percorso, peso_tot = coda.popleft()

            if attuale == fine and len(percorso) > 1:
                return {
                    'percorso': percorso,
                    'passi': len(percorso) - 1,
                    'peso': peso_tot,
                    'spiegazione': [self.nodi[n]['testo'] for n in percorso]
                }

            if len(percorso) >= max_passi:
                continue

            for vicino, peso, tipo in self.archi[attuale]:
                if vicino not in visitati:
                    visitati.add(vicino)
                    coda.append((vicino, percorso + [vicino], peso_tot + peso))

        return None

    def espandi_concetto(self, id_nodo, profondita=2):
        if id_nodo not in self.nodi:
            return []

        visitati = {id_nodo}
        risultato = []
        coda = deque([(id_nodo, 0, 1.0)])

        while coda:
            attuale, distanza, peso = coda.popleft()

            if distanza > 0:
                risultato.append({
                    'id': attuale,
                    'testo': self.nodi[attuale]['testo'],
                    'distanza': distanza,
                    'peso': peso,
                    'tipo': self.nodi[attuale]['tipo']
                })

            if distanza < profondita:
                for vicino, p, tipo in self.archi[attuale]:
                    if vicino not in visitati:
                        visitati.add(vicino)
                        coda.append((vicino, distanza + 1, peso * p))

        return sorted(risultato, key=lambda x: -x['peso'])

    def trova_per_query(self, query, k=5):
        import numpy as np
        vettore_query = motore_embedding.codifica(query)

        risultati = []
        for id_nodo, nodo in self.nodi.items():
            sim = self._similarita_coseno(vettore_query, nodo['vettore'])
            risultati.append((sim, id_nodo))

        risultati.sort(reverse=True)
        return [(s, self.nodi[i]) for s, i in risultati[:k]]

    @staticmethod
    def _similarita_coseno(a, b):
        import numpy as np
        a, b = np.array(a), np.array(b)
        na, nb = np.linalg.norm(a), np.linalg.norm(b)
        if na == 0 or nb == 0:
            return 0.0
        return float(np.dot(a, b) / (na * nb))

grafo = GrafoConoscenza()

# ============================================================
# ORCHESTRATORE MULTI-AGENTE
# ============================================================
# Analizza la query e seleziona l'agente migliore o coordina
# piu agenti per compiti complessi.
# ============================================================

class Orchestratore:
    def __init__(self):
        self._agenti = {}
        self._carica_tutti_agenti()

    def _carica_tutti_agenti(self):
        if not CARTELLA_AGENTI.exists():
            return

        for percorso in CARTELLA_AGENTI.glob("*.yaml"):
            nome = percorso.stem
            with open(percorso, 'r', encoding='utf-8') as f:
                self._agenti[nome] = yaml.safe_load(f)

    def seleziona_agente(self, query):
        """Seleziona l'agente piu adatto per la query."""
        query_lower = query.lower()
        punteggi = {}

        for nome, definizione in self._agenti.items():
            punteggio = 0.0

            # Punteggio per competenze primarie
            for comp in definizione.get('competenze_primarie', []):
                if comp.lower().replace('_', ' ') in query_lower:
                    punteggio += 3.0

            # Punteggio per competenze secondarie
            for comp in definizione.get('competenze_secondarie', []):
                if comp.lower().replace('_', ' ') in query_lower:
                    punteggio += 1.5

            # Punteggio per parole chiave nel ruolo
            ruolo = definizione.get('ruolo', '').lower()
            parole_ruolo = ruolo.split()
            for parola in parole_ruolo:
                if len(parola) > 3 and parola in query_lower:
                    punteggio += 0.5

            # Punteggio per parole chiave nella descrizione
            descrizione = definizione.get('descrizione', '').lower()
            parole_desc = descrizione.split()
            for parola in parole_desc:
                if len(parola) > 3 and parola in query_lower:
                    punteggio += 0.3

            punteggi[nome] = punteggio

        if not punteggi or max(punteggi.values()) == 0:
            return None, punteggi

        migliore = max(punteggi, key=punteggi.get)
        return migliore, punteggi

    def coordina_multi_agente(self, query):
        """Per query complesse, coordina piu agenti."""
        agenti_selezionati = []
        migliore, punteggi = self.seleziona_agente(query)

        if migliore and punteggi[migliore] >= 3.0:
            agenti_selezionati.append(migliore)

        # Aggiungi agenti con punteggio significativo
        for nome, punteggio in sorted(punteggi.items(), key=lambda x: -x[1]):
            if punteggio >= 1.5 and nome not in agenti_selezionati:
                agenti_selezionati.append(nome)
                if len(agenti_selezionati) >= 3:
                    break

        return agenti_selezionati

orchestratore = Orchestratore()

# ============================================================
# ENGINE RAGIONAMENTO
# ============================================================

class MotoreRagionamento:
    def __init__(self):
        self._passaggi = []
        self._confidenza = 1.0

    def ragiona(self, query, agente_def, contesto_iniziale=None):
        self._passaggi = []
        self._confidenza = 1.0

        # Passo 1: Decomposizione
        sotto_domande = self._decomponi(query)
        self._passaggi.append({
            'fase': 'decomposizione',
            'input': query,
            'output': sotto_domande,
            'confidenza': 0.9
        })

        # Passo 2: Recupero contesto
        contesti = []
        for sq in sotto_domande:
            ctx = self._recupera_contesto(sq, agente_def)
            contesti.append(ctx)

        self._passaggi.append({
            'fase': 'recupero',
            'input': sotto_domande,
            'output': [len(c) for c in contesti],
            'confidenza': 0.85
        })

        # Passo 3: Ragionamento a catena
        catena = self._costruisci_catena(sotto_domande, contesti)
        self._passaggi.append({
            'fase': 'ragionamento',
            'input': 'catena logica',
            'output': catena,
            'confidenza': catena.get('confidenza', 0.7)
        })

        # Passo 4: Sintesi
        output = self._sintetizza(catena, agente_def)
        self._passaggi.append({
            'fase': 'sintesi',
            'input': 'catena logica',
            'output': 'strutturato',
            'confidenza': output.get('confidenza', 0.8)
        })

        return output

    def _decomponi(self, query):
        pattern_causale = r'(?:perch[eé]|come mai|qual e la causa)'
        pattern_comparativo = r'(?:differenza|confronto|rispetto a|vs|versus)'
        pattern_procedurale = r'(?:come|passi|procedura|steps)'
        pattern_architetturale = r'(?:architettura|struttura|design|pattern)'
        pattern_sicurezza = r'(?:sicurezza|vulnerabilita|threat|rischio|encrypt)'
        pattern_performance = r'(?:performance|ottimizza|velocizza|bottleneck|lento)'
        pattern_test = r'(?:test|coverage|bug|quality|assurance)'
        pattern_deploy = r'(?:deploy|rilascio|produzione|rollback|monitor)'

        sotto_domande = [query]

        if re.search(pattern_causale, query, re.IGNORECASE):
            sotto_domande.append(f"Fattori causali di: {query}")
            sotto_domande.append(f"Effetti correlati a: {query}")

        if re.search(pattern_comparativo, query, re.IGNORECASE):
            parti = re.split(r'(?:rispetto a|vs|versus|e|vs\.)', query, flags=re.IGNORECASE)
            if len(parti) >= 2:
                sotto_domande.append(f"Caratteristiche di: {parti[0].strip()}")
                sotto_domande.append(f"Caratteristiche di: {parti[1].strip()}")

        if re.search(pattern_procedurale, query, re.IGNORECASE):
            sotto_domande.append(f"Prerequisiti per: {query}")
            sotto_domande.append(f"Passaggi intermedi di: {query}")
            sotto_domande.append(f"Risultato atteso di: {query}")

        if re.search(pattern_architetturale, query, re.IGNORECASE):
            sotto_domande.append(f"Pattern applicabili a: {query}")
            sotto_domande.append(f"Trade-off architetturali per: {query}")

        if re.search(pattern_sicurezza, query, re.IGNORECASE):
            sotto_domande.append(f"Threat model per: {query}")
            sotto_domande.append(f"Contromisure per: {query}")

        if re.search(pattern_performance, query, re.IGNORECASE):
            sotto_domande.append(f"Profilo performance di: {query}")
            sotto_domande.append(f"Ottimizzazioni per: {query}")

        if re.search(pattern_test, query, re.IGNORECASE):
            sotto_domande.append(f"Casi di test per: {query}")
            sotto_domande.append(f"Coverage attesa per: {query}")

        if re.search(pattern_deploy, query, re.IGNORECASE):
            sotto_domande.append(f"Piano deploy per: {query}")
            sotto_domande.append(f"Rollback strategy per: {query}")

        return list(set(sotto_domande))

    def _recupera_contesto(self, query, agente_def):
        contesto = []

        # A. Retrieval vettoriale
        if indice_hnsw:
            vettore = motore_embedding.codifica(query)
            risultati = indice_hnsw.ricerca(vettore, k=3)
            for score, payload in risultati:
                contesto.append({
                    'fonte': 'retrieval_vettoriale',
                    'testo': payload.get('testo', ''),
                    'score': score,
                    'metadati': payload.get('metadati', {})
                })

        # B. Grafo di conoscenza
        nodi = grafo.trova_per_query(query, k=3)
        for score, nodo in nodi:
            contesto.append({
                'fonte': 'grafo_conoscenza',
                'testo': nodo['testo'],
                'score': score,
                'tipo': nodo['tipo'],
                'metadati': nodo['metadati']
            })

            espansi = grafo.espandi_concetto(nodo['metadati'].get('id_grafo'), profondita=1)
            for e in espansi[:2]:
                contesto.append({
                    'fonte': 'grafo_espanso',
                    'testo': e['testo'],
                    'score': e['peso'] * score,
                    'tipo': e['tipo']
                })

        # C. Dataset specifici
        fonti = agente_def.get('fonti_dataset', [])
        for fonte in fonti:
            docs = registro.interroga("""
                SELECT d.testo, d.metadati 
                FROM memoria_documento d
                JOIN memoria_dataset ds ON d.dataset_id = ds.id
                WHERE ds.nome = ?
                LIMIT 3
            """, (fonte,))
            for doc in docs:
                contesto.append({
                    'fonte': f'dataset:{fonte}',
                    'testo': doc['testo'],
                    'metadati': json.loads(doc['metadati'] or '{}')
                })

        return contesto

    def _costruisci_catena(self, domande, contesti):
        catena = {
            'premesse': [],
            'inferenze': [],
            'conclusione': None,
            'confidenza': 1.0
        }

        for ctx_list in contesti:
            for ctx in ctx_list:
                if ctx.get('score', 0) > 0.5:
                    catena['premesse'].append({
                        'testo': ctx['testo'][:200],
                        'fonte': ctx['fonte'],
                        'affidabilita': ctx.get('score', 0.5)
                    })

        for i, premessa in enumerate(catena['premesse']):
            for j, altra in enumerate(catena['premesse'][i+1:], i+1):
                parole_comuni = set(premessa['testo'].lower().split()) & set(altra['testo'].lower().split())
                if len(parole_comuni) >= 2:
                    catena['inferenze'].append({
                        'da': i,
                        'a': j,
                        'tipo': 'correlazione_lessicale',
                        'forza': len(parole_comuni) / max(len(premessa['testo'].split()), len(altra['testo'].split()))
                    })

        if catena['premesse']:
            catena['confidenza'] = sum(p['affidabilita'] for p in catena['premesse']) / len(catena['premesse'])
            catena['confidenza'] *= (1.0 if catena['inferenze'] else 0.7)

        return catena

    def _sintetizza(self, catena, agente_def):
        output_schema = agente_def.get('output_schema', {
            'risposta': 'string',
            'fonti': 'list',
            'confidenza': 'float',
            'ragionamento': 'string'
        })

        premesse_testo = [p['testo'] for p in catena['premesse'][:3]]

        risposta = "Basandomi su "
        if premesse_testo:
            risposta += f"{len(catena['premesse'])} fonti di contesto, "
            risposta += f"ho identificato {len(catena['inferenze'])} correlazioni. "
            risposta += f"Le premesse principali sono: {'; '.join(premesse_testo[:2])}."
        else:
            risposta = "Contesto insufficiente per una risposta affidabile."

        fonti = list(set(p['fonte'] for p in catena['premesse']))

        return {
            'risposta': risposta,
            'fonti_utilizzate': fonti,
            'confidenza': round(catena['confidenza'], 3),
            'ragionamento': {
                'premesse_count': len(catena['premesse']),
                'inferenze_count': len(catena['inferenze']),
                'passaggi': self._passaggi
            },
            'schema': output_schema
        }

# ============================================================
# COMANDI PLUGIN AGENTE
# ============================================================

def _carica_definizione(nome):
    percorso = CARTELLA_AGENTI / f"{nome}.yaml"
    if not percorso.exists():
        return None
    with open(percorso, encoding="utf-8") as f:
        return yaml.safe_load(f)

def esegui(argomenti):
    pos = argomenti.get("argomenti_posizionali", [])
    if len(pos) < 2:
        return "Uso: agente.esegui <nome_agente> <query>"

    nome_agente = pos[0]
    query = " ".join(pos[1:])

    definizione = _carica_definizione(nome_agente)
    if not definizione:
        return f"Agente '{nome_agente}' non trovato. Agenti disponibili: {', '.join(lista_agenti())}"

    _popola_grafo()

    motore = MotoreRagionamento()
    risultato = motore.ragiona(query, definizione)

    registro.esegui("""
        CREATE TABLE IF NOT EXISTS agente_log (
            id INTEGER PRIMARY KEY,
            agente TEXT,
            query TEXT,
            output TEXT,
            confidenza REAL,
            timestamp TEXT DEFAULT (datetime('now'))
        )
    """)
    registro.esegui("""
        INSERT INTO agente_log (agente, query, output, confidenza) VALUES (?, ?, ?, ?)
    """, (nome_agente, query, json.dumps(risultato), risultato.get('confidenza', 0)))

    formato = argomenti.get("formato", "text")
    if formato == "json":
        return json.dumps(risultato, indent=2, ensure_ascii=False)

    competenze = definizione.get('competenze_primarie', [])
    competenze_str = ', '.join(competenze[:3]) if competenze else 'generali'

    return f"""Agente: {nome_agente} ({competenze_str})
Query: {query}
Confidenza: {risultato['confidenza']}

Risposta:
{risultato['risposta']}

Fonti:
{"
".join(['- ' + f for f in risultato['fonti_utilizzate']])}

Ragionamento:
- Premesse: {risultato['ragionamento']['premesse_count']}
- Inferenze: {risultato['ragionamento']['inferenze_count']}
"""

def _popola_grafo():
    if grafo.nodi:
        return

    documenti = registro.interroga("SELECT id, testo, metadati FROM memoria_documento LIMIT 1000")

    for doc in documenti:
        vettore = motore_embedding.codifica(doc['testo'])
        grafo.aggiungi_nodo(
            doc['id'],
            doc['testo'],
            vettore,
            tipo="fatto",
            metadati={"id_grafo": doc['id'], **json.loads(doc['metadati'] or '{}')}
        )

    ids = list(grafo.nodi.keys())
    for i, id_a in enumerate(ids):
        for id_b in ids[i+1:i+50]:
            sim = grafo._similarita_coseno(
                grafo.nodi[id_a]['vettore'],
                grafo.nodi[id_b]['vettore']
            )
            if sim > 0.7:
                grafo.aggiungi_arco(id_a, id_b, peso=sim, tipo="similarita_semantica")

    guardiano.logga("INFO", "agente", "grafo_popolato", 
                    f"{len(grafo.nodi)} nodi, {sum(len(a) for a in grafo.archi.values())} archi")

def lista(argomenti):
    if not CARTELLA_AGENTI.exists():
        return "Nessun agente."

    agenti_info = []
    for p in sorted(CARTELLA_AGENTI.glob("*.yaml")):
        def_agente = _carica_definizione(p.stem)
        if def_agente:
            primarie = def_agente.get('competenze_primarie', [])
            agenti_info.append(f"- {p.stem}: {def_agente.get('ruolo', 'N/A')} [{', '.join(primarie[:2])}]")

    return "Agenti disponibili:
" + "
".join(agenti_info)

def lista_agenti():
    """Versione interna che restituisce lista nomi."""
    if not CARTELLA_AGENTI.exists():
        return []
    return [p.stem for p in CARTELLA_AGENTI.glob("*.yaml")]

def crea(argomenti):
    pos = argomenti.get("argomenti_posizionali", [])
    if not pos:
        return "Uso: agente.crea <nome_agente>"

    nome = pos[0]
    template = {
        'nome': nome,
        'ruolo': f"Esperto in {nome}",
        'descrizione': f"Agente specializzato per {nome}",
        'competenze_primarie': [],
        'competenze_secondarie': [],
        'fonti_dataset': [],
        'istruzioni': [
            "Analizza il contesto prima di rispondere",
            "Cita le fonti utilizzate",
            "Esprimi confidenza nella risposta"
        ],
        'output_schema': {
            'risposta': 'string',
            'fonti_utilizzate': 'list',
            'confidenza': 'float',
            'ragionamento': 'object'
        }
    }

    percorso = CARTELLA_AGENTI / f"{nome}.yaml"
    with open(percorso, 'w', encoding='utf-8') as f:
        yaml.dump(template, f, allow_unicode=True, sort_keys=False)

    return f"Agente '{nome}' creato in {percorso}"

def seleziona(argomenti):
    """Mostra quale agente sarebbe selezionato per una query."""
    pos = argomenti.get("argomenti_posizionali", [])
    if not pos:
        return "Uso: agente.seleziona <query>"

    query = " ".join(pos)
    orchestratore._carica_tutti_agenti()

    migliore, punteggi = orchestratore.seleziona_agente(query)

    output = [f"Query: '{query}'", f"", f"Agente selezionato: {migliore or 'NESSUNO (punteggi troppo bassi)'}", f""]
    output.append("Punteggi per competenze:")

    for nome, punteggio in sorted(punteggi.items(), key=lambda x: -x[1]):
        marker = " <-- SCELTO" if nome == migliore else ""
        output.append(f"  {nome}: {punteggio:.1f}{marker}")

    return "
".join(output)

def coordina(argomenti):
    """Coordina piu agenti per una query complessa."""
    pos = argomenti.get("argomenti_posizionali", [])
    if not pos:
        return "Uso: agente.coordina <query>"

    query = " ".join(pos)
    orchestratore._carica_tutti_agenti()

    agenti = orchestratore.coordina_multi_agente(query)

    if not agenti:
        return f"Nessun agente identificato per '{query}'. Prova con termini piu specifici."

    output = [f"Query complessa: '{query}'", f"", f"Agenti coordinati ({len(agenti)}):"]

    for i, nome in enumerate(agenti, 1):
        def_agente = _carica_definizione(nome)
        if def_agente:
            ruolo = def_agente.get('ruolo', 'N/A')
            primarie = def_agente.get('competenze_primarie', [])
            output.append(f"  {i}. {nome}: {ruolo}")
            output.append(f"     Competenze: {', '.join(primarie)}")

    output.append(f"
Per eseguire: agente.esegui <nome> '{query}'")

    return "
".join(output)

COMANDI = {
    "agente.esegui": esegui,
    "agente.lista": lista,
    "agente.crea": crea,
    "agente.seleziona": seleziona,
    "agente.coordina": coordina,
}
