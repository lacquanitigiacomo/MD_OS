import json
from pathlib import Path
from mdos.core.paths import DATASETS

REGISTRO = DATASETS / "x50_release_registry.jsonl"


def leggi_x50():
    elementi = []
    if not REGISTRO.exists():
        return elementi
    for line in REGISTRO.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.strip():
            continue
        try:
            elementi.append(json.loads(line))
        except Exception:
            pass
    return elementi


def stato_x50():
    elementi = [x for x in leggi_x50() if x.get("id") != "X50-00"]
    attivi = [x for x in elementi if x.get("stato") == "attiva"]
    pianificati = [x for x in elementi if x.get("stato") == "pianificata"]
    prossimi = sorted(pianificati, key=lambda x: x.get("priorita", 0), reverse=True)[:5]
    percentuale = round((len(attivi) / len(elementi)) * 100, 2) if elementi else 0
    return {
        "totale": len(elementi),
        "attivi": len(attivi),
        "pianificati": len(pianificati),
        "percentuale_attiva": percentuale,
        "prossimi": prossimi
    }


def formato_x50():
    s = stato_x50()
    righe = [
        "MD_OS X50",
        f"Moduli totali: {s['totale']}",
        f"Moduli attivi: {s['attivi']}",
        f"Moduli pianificati: {s['pianificati']}",
        f"Attivazione X50: {s['percentuale_attiva']}%",
        "",
        "Prossime priorita:"
    ]
    for item in s["prossimi"]:
        righe.append(f"- {item.get('id')} {item.get('nome')} priorita={item.get('priorita')} :: {item.get('obiettivo')}")
    return "\n".join(righe)
