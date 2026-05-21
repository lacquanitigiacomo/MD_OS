# Placeholder esecutore: le funzioni sono dichiarate in CORE/functions.yaml.
# Integrazioni future possono implementare calcoli reali senza appesantire la chat.
import yaml, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
functions=yaml.safe_load((ROOT/'CORE'/'functions.yaml').read_text(encoding='utf-8'))['functions']
name=sys.argv[1] if len(sys.argv)>1 else None
print(functions.get(name, {'errore':'funzione non trovata'}))
