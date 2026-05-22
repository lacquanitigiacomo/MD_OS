import csv,json
from pathlib import Path
def read_csv(path):
    with open(path,encoding="utf-8",newline="") as f: return list(csv.DictReader(f))
def append_jsonl(path,obj):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    with open(path,"a",encoding="utf-8") as f: f.write(json.dumps(obj,ensure_ascii=False)+"\n")
def write_text(path,text):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True); path.write_text(text,encoding="utf-8")
