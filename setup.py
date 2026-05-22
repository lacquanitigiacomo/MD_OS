#!/usr/bin/env python3
"""Setup MD_OS Core X12 Vision."""

import subprocess
import sys
from pathlib import Path

def main():
    print("=" * 50)
    print("MD_OS Core X12 Vision - Setup")
    print("=" * 50)

    for d in ["dataset", "log", "cache", "modello"]:
        Path(d).mkdir(exist_ok=True)
        print(f"OK Cartella {d}/ creata")

    print("
Installazione dipendenze opzionali...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("OK Dipendenze installate")
    except subprocess.CalledProcessError:
        print("WARN Installazione manuale: pip install -r requirements.txt")

    print("
Validazione sistema...")
    try:
        subprocess.check_call([sys.executable, "-m", "nucleo.mdos", "memoria.valida"])
        print("OK Sistema validato")
    except Exception as e:
        print(f"WARN Validazione: {e}")

    print("
" + "=" * 50)
    print("Setup completato!")
    print("Esegui: python -m nucleo.mdos memoria.stato")
    print("=" * 50)

if __name__ == "__main__":
    main()
