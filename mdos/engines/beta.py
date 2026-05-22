import json,datetime
from mdos.core.paths import BETA,EXPORTS
from mdos.core.io import write_text,append_jsonl
def run(name):
    p=BETA/"scenarios"/f"{name}.json"
    if not p.exists(): return None
    data=json.loads(p.read_text(encoding="utf-8"))
    result={"ts":datetime.datetime.now().isoformat(),"scenario":name,"status":"passed_basic"}
    append_jsonl(BETA/"reports"/"beta_events.jsonl",result)
    out=EXPORTS/f"beta_{name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    write_text(out,f"# Beta Report\n\nScenario: {name}\nStato: passed_basic\n")
    return result,out
