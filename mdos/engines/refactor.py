import datetime
from mdos.core.paths import DATASETS,EXPORTS
from mdos.core.io import append_jsonl,write_text
def run_refactor(goal):
    seeds=[
    ("funzione","scoring priorità su gap e innovazioni"),
    ("dataset","normalizzare relazioni agenti-capability-pattern"),
    ("matrice","generare capability matrix e risk matrix"),
    ("agente","rafforzare refactor_agent"),
    ("pattern","usare architecture freeze"),
    ("memoria","salvare refactor append-only"),
    ("beta","test memory_failure"),
    ("release","calcolare readiness"),
    ("innovazione","plugin senza cambio struttura"),
    ("query","ricerca locale su file testuali")]
    adv=[{"id":f"RX10-{i:02d}","tipo":k,"azione":a,"goal":goal} for i,(k,a) in enumerate(seeds,1)]
    append_jsonl(DATASETS/"LEARNING_EVENTS.jsonl",{"ts":datetime.datetime.now().isoformat(),"type":"refactor_x10","goal":goal,"advances":adv})
    out=EXPORTS/f"refactor_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    lines=["# Report REFACTOR X10","","| ID | Tipo | Azione |","|---|---|---|"]+[f"| {x['id']} | {x['tipo']} | {x['azione']} |" for x in adv]
    write_text(out,"\n".join(lines)+"\n")
    return adv,out
