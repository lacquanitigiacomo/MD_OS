from mdos.core.datasets import count_rows, validate
from mdos.engines.x50 import stato_x50


def stato_cruscotto():
    dataset = count_rows()
    mancanti = validate()
    x50 = stato_x50()
    totale_record = sum(dataset.values()) if dataset else 0
    return {
        "dataset": dataset,
        "mancanti": mancanti,
        "totale_record": totale_record,
        "x50": x50,
        "prossima_azione": scegli_prossima_azione(mancanti, x50)
    }


def scegli_prossima_azione(mancanti, x50):
    if mancanti:
        return "Completare i dataset richiesti mancanti."
    if x50.get("attivi", 0) < 15:
        return "Attivare nuovi moduli X50 con codice, dataset o report verificabile."
    return "Consolidare i comandi CLI e i report automatici."


def formato_cruscotto():
    s = stato_cruscotto()
    righe = [
        "MD_OS Cruscotto",
        f"Record dataset contati: {s['totale_record']}",
        f"Dataset mancanti: {len(s['mancanti'])}",
        f"X50 attivi: {s['x50']['attivi']}/{s['x50']['totale']}",
        "",
        "Dataset:"
    ]
    for nome, valore in sorted(s["dataset"].items()):
        righe.append(f"- {nome}: {valore}")
    if s["mancanti"]:
        righe.append("")
        righe.append("Mancanti:")
        righe.extend(f"- {x}" for x in s["mancanti"])
    righe.append("")
    righe.append("Prossima azione:")
    righe.append(s["prossima_azione"])
    return "\n".join(righe)
