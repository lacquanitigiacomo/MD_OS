import json
from datetime import datetime
from mdos.core.paths import DATASETS
from mdos.core.io import append_jsonl
from mdos.engines.memoria import estrai_parole_chiave, cerca_memoria, riassumi_memoria


def punteggi_base(testo, fonti):
    parole = set(estrai_parole_chiave(testo))
    innovazione = min(10, 2 + 2 * len(parole & {"innovazione", "nuovo", "evoluzione", "agente", "sistema", "x10", "genio"}))
    efficienza = min(10, 2 + 2 * len(parole & {"efficienza", "leggero", "dataset", "memoria", "ranking", "riuso"}))
    visione = min(10, 2 + 2 * len(parole & {"visione", "strategia", "roadmap", "futuro", "direzione", "sistemico"}))
    traccia = min(10, len(fonti) * 2)
    totale = round((innovazione + efficienza + visione + traccia) / 4, 2)
    return {"innovazione": innovazione, "efficienza": efficienza, "visione": visione, "traccia": traccia, "totale": totale}


def prossima_azione(testo, risultati):
    parole = set(estrai_parole_chiave(testo))
    if "patch" in parole or "release" in parole:
        return "Preparare una patch piccola, verificabile e collegata ai dataset."
    if "dataset" in parole or "memoria" in parole:
        return "Aggiornare i dataset e rigenerare le matrici di relazione."
    if "comando" in parole or "cli" in parole:
        return "Aggiungere un comando italiano alla CLI e collegarlo a un motore locale."
    if risultati:
        return "Usare le fonti locali trovate per produrre una decisione o una funzione minima."
    return "Registrare la richiesta come nuovo apprendimento e creare un pattern operativo."


def chiedi(testo, limite=6, salva=True):
    risultati = cerca_memoria(testo, limite=limite)
    fonti = [f"{r['path']}:{r['linea']}" for r in risultati]
    score = punteggi_base(testo, fonti)
    azione = prossima_azione(testo, risultati)
    parole = estrai_parole_chiave(testo)
    risposta = {
        "richiesta": testo,
        "parole_chiave": parole,
        "fonti_locali": fonti,
        "score": score,
        "prossima_azione": azione,
        "memoria": risultati
    }
    if salva:
        append_jsonl(DATASETS / "interazioni_genio.jsonl", {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "richiesta": testo,
            "parole_chiave": parole,
            "fonti_locali": fonti,
            "score": score,
            "prossima_azione": azione
        })
    return risposta


def formato_risposta(obj):
    righe = []
    righe.append("MD_OS - Genio Locale")
    righe.append("")
    righe.append("Parole chiave: " + ", ".join(obj["parole_chiave"]))
    righe.append("")
    righe.append("Fonti locali:")
    if obj["fonti_locali"]:
        righe.extend(f"- {f}" for f in obj["fonti_locali"])
    else:
        righe.append("- nessuna fonte locale trovata")
    righe.append("")
    righe.append("Valutazione:")
    for k, v in obj["score"].items():
        righe.append(f"- {k}: {v}/10")
    righe.append("")
    righe.append("Prossima azione:")
    righe.append(obj["prossima_azione"])
    righe.append("")
    righe.append("Memoria rilevante:")
    righe.append(riassumi_memoria(obj["memoria"]))
    return "\n".join(righe)
