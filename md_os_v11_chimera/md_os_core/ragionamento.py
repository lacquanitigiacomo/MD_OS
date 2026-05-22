"""
RagionamentoTemplate — Non ragiona, ma sembra che lo faccia
Usa pattern matching, template e "chain-of-thought" simulata.
"""
import re
import json
from typing import Dict, List, Any

class RagionamentoTemplate:
    """
    Simula chain-of-thought e ragionamento strutturato.
    In realta e' un template engine con variabili dinamiche.
    """

    TEMPLATES_COT = {
        "problema_scomposto": """
Analisi del problema:
1. Input ricevuto: {input_utente}
2. Pattern riconosciuto: {pattern_match}
3. Sottoproblemi identificati: {n_sottoproblemi}
4. Soluzione applicata: {soluzione}
5. Confidenza stimata: {confidenza}%
""",
        "decisione_strutturata": """
Processo decisionale:
- Opzione A: {opzione_a} (pro: {pro_a}, contro: {contro_a})
- Opzione B: {opzione_b} (pro: {pro_b}, contro: {contro_b})
- Scelta: {scelta}
- Giustificazione: {giustificazione}
""",
        "analisi_dati": """
Analisi dati:
- Dataset: {dataset_desc}
- Metriche chiave: {metriche}
- Trend rilevato: {trend}
- Anomalia: {anomalia}
- Raccomandazione: {raccomandazione}
"""
    }

    def __init__(self):
        pass

    def chain_of_thought(self, input_utente: str, skill_nome: str, 
                         variabili: Dict[str, Any] = None) -> str:
        """Genera una chain-of-thought plausibile."""
        variabili = variabili or {}

        # Scegli template in base alla skill
        if "calcolo" in skill_nome or "math" in skill_nome:
            template_key = "analisi_dati"
        elif "decidi" in input_utente.lower() or "scegli" in input_utente.lower():
            template_key = "decisione_strutturata"
        else:
            template_key = "problema_scomposto"

        template = self.TEMPLATES_COT.get(template_key, self.TEMPLATES_COT["problema_scomposto"])

        # Variabili di default
        defaults = {
            "input_utente": input_utente[:80],
            "pattern_match": skill_nome,
            "n_sottoproblemi": len(input_utente.split()),
            "soluzione": "Template-based response",
            "confidenza": random.randint(75, 95),
            "opzione_a": "Approccio diretto",
            "opzione_b": "Approccio alternativo",
            "pro_a": "Veloce",
            "contro_a": "Potenzialmente impreciso",
            "pro_b": "Accurato",
            "contro_b": "Richiede piu tempo",
            "scelta": "Approccio diretto (ottimizzato per velocita)",
            "giustificazione": "Il contesto suggerisce una risposta rapida",
            "dataset_desc": "Dati forniti dall'utente",
            "metriche": "N/A",
            "trend": "Stabile",
            "anomalia": "Nessuna rilevata",
            "raccomandazione": "Procedere con cautela"
        }
        defaults.update(variabili)

        try:
            return template.format(**defaults)
        except KeyError:
            return f"Ragionamento su: {input_utente[:50]}...\nPattern: {skill_nome}"

    def estrai_entita(self, testo: str) -> Dict[str, List[str]]:
        """Estrazione entita finta ma plausibile."""
        entita = {
            "persone": re.findall(r'[A-Z][a-z]+(?:\s[A-Z][a-z]+)*', testo),
            "date": re.findall(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', testo),
            "numeri": re.findall(r'\d+', testo),
            "email": re.findall(r'[\w.-]+@[\w.-]+\.\w+', testo),
            "url": re.findall(r'https?://\S+', testo)
        }
        return entita

    def classifica_intento(self, testo: str) -> Dict[str, Any]:
        """Classificazione intento basata su keyword."""
        intenti = {
            "informazione": ["cosa", "come", "perche", "quando", "dove", "chi"],
            "azione": ["fai", "esegui", "avvia", "lancia", "crea"],
            "analisi": ["analizza", "confronta", "valuta", "stima"],
            "configurazione": ["imposta", "configura", "modifica", "cambia"]
        }

        testo_lower = testo.lower()
        scores = {}
        for intento, keywords in intenti.items():
            score = sum(1 for kw in keywords if kw in testo_lower)
            scores[intento] = score

        best = max(scores, key=scores.get)
        return {
            "intento": best,
            "confidenza": min(0.95, 0.5 + scores[best] * 0.15),
            "scores": scores
        }

import random
