from pathlib import Path
import yaml, json, sys
ROOT=Path(__file__).resolve().parents[1]

def load_yaml(p): return yaml.safe_load((ROOT/p).read_text(encoding='utf-8'))
def score(text, terms):
    t=text.lower(); return sum(1 for x in terms if x.lower() in t)
def route_request(text):
    rules=load_yaml('CORE/routing.yaml')['rules']
    best=None
    for r in rules:
        s=score(text,r.get('match',[]))
        if s and (best is None or s>best[0]): best=(s,r)
    return best[1] if best else None
if __name__=='__main__':
    print(json.dumps(route_request(' '.join(sys.argv[1:])) or {},ensure_ascii=False,indent=2))
