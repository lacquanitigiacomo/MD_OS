import datetime
from mdos.core.datasets import count_rows
from mdos.core.paths import EXPORTS
from mdos.core.io import write_text
def profile():
    c=count_rows(); score=0
    score+=20 if c.get("AGENTS.csv",0)>=20 else 0
    score+=20 if c.get("CAPABILITIES.csv",0)>=10 else 0
    score+=20 if c.get("INNOVATIONS.csv",0)>=10 else 0
    score+=20 if c.get("RELATIONS.csv",0)>=30 else 0
    score+=20 if c.get("LEARNING_EVENTS.jsonl",0)>=1 else 0
    out=EXPORTS/f"profile_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    write_text(out,"# Profilo Sistema\n\nReadiness: %s/100\n"%score)
    return {"score":score,"counts":c},out
