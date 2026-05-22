from pathlib import Path
import csv, sys
if len(sys.argv) < 2:
    print('Uso: python engine/query.py datasets/AGENTS.csv [campo valore]')
    raise SystemExit(1)
ROOT = Path(__file__).resolve().parents[1]
path = ROOT / sys.argv[1]
field = sys.argv[2] if len(sys.argv) > 2 else None
value = sys.argv[3].lower() if len(sys.argv) > 3 else None
with path.open(encoding='utf-8') as f:
    rows=list(csv.DictReader(f))
if field and value:
    rows=[r for r in rows if value in r.get(field,'').lower()]
for r in rows:
    print(r)
