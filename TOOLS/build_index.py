from pathlib import Path
import re, json, yaml
ROOT = Path(__file__).resolve().parents[1]

def read_frontmatter(path):
    txt = path.read_text(encoding='utf-8')
    if not txt.startswith('---'): return {}
    end = txt.find('---', 3)
    return yaml.safe_load(txt[3:end]) or {}

def main():
    agents=[]
    for p in (ROOT/'AGENTI'/'singoli').rglob('*.md'):
        fm=read_frontmatter(p)
        if fm:
            fm['path']=str(p.relative_to(ROOT))
            agents.append(fm)
    (ROOT/'AGENTI'/'agents_index.json').write_text(json.dumps({'agents':agents},ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Indicizzati {len(agents)} agenti')
if __name__=='__main__': main()
