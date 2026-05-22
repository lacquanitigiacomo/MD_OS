from mdos.core.paths import ROOT
EXT={".md",".csv",".json",".jsonl",".py"}
def query(terms):
    terms=[t.lower() for t in terms]; out=[]
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in EXT and ".git" not in p.parts:
            txt=p.read_text(encoding="utf-8",errors="ignore").lower()
            score=sum(txt.count(t) for t in terms)
            if score: out.append({"path":str(p.relative_to(ROOT)),"score":score})
    return sorted(out,key=lambda x:x["score"],reverse=True)
