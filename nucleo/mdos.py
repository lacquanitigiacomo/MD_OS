#!/usr/bin/env python3
# nucleo/mdos.py
# Entry point MD_OS Core X12 Vision.

import argparse
import sys
from .costanti import VERSIONE_NUCLEO
from .registro import registro
from .motore import motore
from .guardiano import guardiano

def principale():
    parser = argparse.ArgumentParser(description="MD_OS Core X12 Vision")
    parser.add_argument("comando", help="Comando (es: memoria.valida)")
    parser.add_argument("argomenti", nargs="*", help="Argomenti")
    parser.add_argument("--obiettivo", "-o", help="Obiettivo")
    parser.add_argument("--testo", "-t", help="Testo")
    parser.add_argument("--scenario", "-s", help="Scenario")
    parser.add_argument("--formato", "-f", choices=["json", "yaml", "text", "html"], default="text", help="Formato output")

    args = parser.parse_args()

    guardiano.logga("INFO", "nucleo", "avvio", f"MD_OS v{VERSIONE_NUCLEO} - {args.comando}")

    motore.esplora_plugin()

    parametri = {
        "obiettivo": args.obiettivo,
        "testo": args.testo,
        "scenario": args.scenario,
        "formato": args.formato,
        "argomenti_posizionali": args.argomenti
    }

    try:
        risultato = guardiano.sandbox(motore.esegui, args.comando, parametri)

        if args.formato == "json":
            import json
            print(json.dumps({"risultato": risultato}, indent=2, ensure_ascii=False))
        elif args.formato == "yaml":
            import yaml
            print(yaml.dump({"risultato": risultato}, allow_unicode=True))
        elif args.formato == "html":
            print(f"<pre>{risultato}</pre>")
        else:
            print(risultato)

        guardiano.logga("INFO", "nucleo", "completato", args.comando)
    except Exception as e:
        guardiano.logga("ERRORE", "nucleo", "fallito", str(e))
        raise SystemExit(1)
    finally:
        motore.arresta()

if __name__ == "__main__":
    principale()
