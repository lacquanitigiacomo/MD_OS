from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
def count(name):
    with (ROOT/'datasets'/name).open(encoding='utf-8') as f:
        return len(list(csv.DictReader(f)))
print('# Profilo sistema')
for name in ['AGENTS.csv','CAPABILITIES.csv','INNOVATIONS.csv','PATTERNS.csv','GAPS.csv','RELATIONS.csv']:
    print(f'- {name}: {count(name)} righe')
