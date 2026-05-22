import csv
import json
from pathlib import Path
from mdos.core.paths import DATASETS, ROOT

ESTENSIONI_DATI = {".jsonl", ".json", ".csv", ".md", ".txt"}


def normalizza_testo(testo):
    return " ".join(str(testo or "").lower().replace("_", " ").replace("-", " ").split())


def estrai_parole_chiave(testo):
    stop = {
        "il", "lo", "la", "i", "gli", "le", "un", "una", "uno", "di", "a", "da", "in", "con", "su", "per",
        "che", "e", "o", "ma", "se", "come", "cosa", "questo", "questa", "ora", "poi", "del", "della",
        "dei", "delle", "dei", "nel", "nella", "sono", "si", "mi", "ti", "ci", "vi", "al", "alla"
    }
    parole = []
    for raw in normalizza_testo(testo).split():
        parola = "".join(c for c in raw if c.isalnum() or c in {"_"})
        if len(parola) >= 3 and parola not in stop and parola not in parole:
            parole.append(parola)
    return parole[:16]


def _record_da_jsonl(path):
    records = []
    for i, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
            testo = json.dumps(obj, ensure_ascii=False)
        except Exception:
            obj = {"testo": line.strip()}
            testo = line.strip()
        records.append({"path": str(path.relative_to(ROOT)), "linea": i, "oggetto": obj, "testo": testo})
    return records


def _record_da_json(path):
    try:
        obj = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        obj = {"testo": path.read_text(encoding="utf-8", errors="ignore")}
    return [{"path": str(path.relative_to(ROOT)), "linea": 1, "oggetto": obj, "testo": json.dumps(obj, ensure_ascii=False)}]


def _record_da_csv(path):
    records = []
    with path.open(encoding="utf-8", newline="", errors="ignore") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            records.append({"path": str(path.relative_to(ROOT)), "linea": i, "oggetto": row, "testo": json.dumps(row, ensure_ascii=False)})
    return records


def _record_da_testo(path):
    testo = path.read_text(encoding="utf-8", errors="ignore")
    return [{"path": str(path.relative_to(ROOT)), "linea": 1, "oggetto": {"testo": testo[:2000]}, "testo": testo}]


def carica_record_dataset():
    records = []
    if not DATASETS.exists():
        return records
    for path in DATASETS.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in ESTENSIONI_DATI:
            continue
        try:
            if path.suffix.lower() == ".jsonl":
                records.extend(_record_da_jsonl(path))
            elif path.suffix.lower() == ".json":
                records.extend(_record_da_json(path))
            elif path.suffix.lower() == ".csv":
                records.extend(_record_da_csv(path))
            else:
                records.extend(_record_da_testo(path))
        except Exception:
            continue
    return records


def cerca_memoria(testo, limite=8):
    parole = estrai_parole_chiave(testo)
    risultati = []
    for record in carica_record_dataset():
        corpo = normalizza_testo(record.get("testo", ""))
        score = sum(corpo.count(p) for p in parole)
        if score <= 0:
            continue
        risultati.append({
            "score": score,
            "path": record["path"],
            "linea": record["linea"],
            "anteprima": record.get("testo", "")[:260].replace("\n", " "),
            "oggetto": record.get("oggetto", {})
        })
    risultati.sort(key=lambda x: (x["score"], x["path"]), reverse=True)
    return risultati[:limite]


def riassumi_memoria(risultati):
    if not risultati:
        return "Nessun dato rilevante trovato nei dataset locali."
    righe = []
    for r in risultati:
        righe.append(f"- {r['path']}:{r['linea']} score={r['score']} :: {r['anteprima']}")
    return "\n".join(righe)
