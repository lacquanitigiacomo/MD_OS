from pathlib import Path
import csv, sys
ROOT = Path(__file__).resolve().parents[1]
required = [
    'README.md','STATUS.md','INDEX.md','ROADMAP.md','RELEASE.md',
    'datasets/COMMANDS.csv','datasets/AGENTS.csv','datasets/CAPABILITIES.csv',
    'datasets/PATTERNS.csv','datasets/INNOVATIONS.csv','datasets/GAPS.csv',
    'datasets/RELATIONS.csv','docs/PROTOCOLLO_REFACTOR.md'
]
errors=[]
for r in required:
    if not (ROOT/r).exists(): errors.append(f'Manca: {r}')
for csv_path in (ROOT/'datasets').glob('*.csv'):
    try:
        with csv_path.open(encoding='utf-8') as f:
            rows=list(csv.DictReader(f))
            if not rows: errors.append(f'Dataset vuoto: {csv_path.name}')
    except Exception as e:
        errors.append(f'CSV non valido {csv_path.name}: {e}')
if errors:
    print('VALIDAZIONE FALLITA')
    print('\n'.join(errors))
    sys.exit(1)
print('VALIDAZIONE OK')
