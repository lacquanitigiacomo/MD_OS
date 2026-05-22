from mdos.core.paths import DATASETS
from mdos.core.io import read_csv
def get(agent_id):
    agents=read_csv(DATASETS/"AGENTS.csv"); caps=read_csv(DATASETS/"CAPABILITIES.csv"); rels=read_csv(DATASETS/"RELATIONS.csv")
    a=next((x for x in agents if x["agent_id"]==agent_id),None)
    if not a: return None
    return {"agent":a,"capabilities":[c for c in caps if c["owner_agent"]==agent_id],"relations":[r for r in rels if r["source"]==agent_id or r["target"]==agent_id]}
