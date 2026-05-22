from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
def read(name):
    with (ROOT/'datasets'/name).open(encoding='utf-8') as f:
        return list(csv.DictReader(f))
print('# REFACTOR report')
print('\n## Innovazioni attive')
for r in read('INNOVATIONS.csv')[:10]:
    print(f"- {r['id']}: {r['innovazione']} ({r['stato']})")
print('\n## Gap principali')
for r in read('GAPS.csv'):
    print(f"- {r['id']}: {r['gap']} [{r['priorita']}]")
print('\n## Pattern critici')
for r in read('PATTERNS.csv'):
    if r['impatto'] in ('critico','alto'):
        print(f"- {r['id']}: {r['pattern']} -> {r['azione']}")
