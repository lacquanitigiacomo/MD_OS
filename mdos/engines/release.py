from mdos.core.datasets import count_rows
from mdos.core.paths import DATASETS
from mdos.core.io import read_csv
def check():
    c=count_rows(); blockers=read_csv(DATASETS/"RELEASE_BLOCKERS.csv")
    criteria={"agents":c.get("AGENTS.csv",0)>=20,"caps":c.get("CAPABILITIES.csv",0)>=10,"innovations":c.get("INNOVATIONS.csv",0)>=10,"relations":c.get("RELATIONS.csv",0)>=30,"learning":c.get("LEARNING_EVENTS.jsonl",0)>=1}
    return {"criteria":criteria,"passed":sum(criteria.values()),"total":len(criteria),"blockers":[b for b in blockers if b["stato"]=="aperto"]}
