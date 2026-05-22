import datetime
from .paths import LOGS
from .io import append_jsonl
def event(kind,text,data=None,tags=None):
    obj={"ts":datetime.datetime.now().isoformat(),"kind":kind,"text":text,"data":data or {},"tags":tags or []}
    append_jsonl(LOGS/"events.jsonl",obj); return obj
