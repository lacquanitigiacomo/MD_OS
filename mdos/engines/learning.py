import datetime,re
from mdos.core.paths import DATASETS
from mdos.core.io import append_jsonl
def learn(text,tags=None):
    words=re.findall(r"[A-Za-zÀ-ÿ0-9_]{4,}",text.lower())
    kw=sorted(set(words))[:20]
    obj={"ts":datetime.datetime.now().isoformat(),"type":"learning","text":text,"keywords":kw,"tags":tags or []}
    append_jsonl(DATASETS/"LEARNING_EVENTS.jsonl",obj); return obj
