from .paths import DATASETS
from .io import read_csv
REQUIRED=["AGENTS.csv","CAPABILITIES.csv","INNOVATIONS.csv","PATTERNS.csv","GAPS.csv","RELATIONS.csv","MEMORY_SCOPES.csv","RELEASE_BLOCKERS.csv","LEARNING_EVENTS.jsonl"]
def validate(): return [n for n in REQUIRED if not (DATASETS/n).exists()]
def count_rows():
    counts={}
    for f in DATASETS.glob("*.csv"): counts[f.name]=len(read_csv(f))
    j=DATASETS/"LEARNING_EVENTS.jsonl"
    if j.exists(): counts[j.name]=sum(1 for line in j.open(encoding="utf-8") if line.strip())
    return counts
