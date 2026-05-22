import datetime
from mdos.core.paths import DATASETS,EXPORTS
from mdos.core.io import read_csv,write_text
def export_all():
    agents=read_csv(DATASETS/"AGENTS.csv"); caps=read_csv(DATASETS/"CAPABILITIES.csv"); gaps=read_csv(DATASETS/"GAPS.csv")
    lines=["# Matrici","","## Capability Matrix","","| Agente | Area | Capability |","|---|---|---|"]
    for a in agents:
        owned="; ".join(c["nome"] for c in caps if c["owner_agent"]==a["agent_id"])
        lines.append(f"| {a['agent_id']} | {a['area']} | {owned} |")
    lines+=["","## Gap Matrix","","| ID | Gap | Priorità |","|---|---|---|"]
    for g in gaps: lines.append(f"| {g['id']} | {g['gap']} | {g['priorita']} |")
    out=EXPORTS/f"matrices_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"; write_text(out,"\n".join(lines)+"\n"); return out
