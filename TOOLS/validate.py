from pathlib import Path
import yaml, sys
ROOT=Path(__file__).resolve().parents[1]
REQ=['id','area','level','skills','lessico','funzioni','formule','datasets','outputs']
def fm(p):
    txt=p.read_text(encoding='utf-8')
    if not txt.startswith('---'): return {}
    end=txt.find('---',3)
    return yaml.safe_load(txt[3:end]) or {}
def main():
    errors=[]
    for p in (ROOT/'AGENTI'/'singoli').rglob('*.md'):
        data=fm(p)
        for k in REQ:
            if k not in data: errors.append(f'{p}: manca {k}')
    print('\n'.join(errors) if errors else 'VALIDO')
if __name__=='__main__': main()
