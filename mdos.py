#!/usr/bin/env python3
import argparse,json
from mdos.core.datasets import validate,count_rows
from mdos.engines.query import query
from mdos.engines.refactor import run_refactor
from mdos.engines.learning import learn
from mdos.engines.matrix import export_all
from mdos.engines.profile import profile
from mdos.engines.release import check
from mdos.engines.agent import get
from mdos.engines.beta import run as beta_run

def main():
    p=argparse.ArgumentParser()
    s=p.add_subparsers(dest="cmd",required=True)
    s.add_parser("validate")
    s.add_parser("status")
    q=s.add_parser("query"); q.add_argument("terms",nargs="+"); q.add_argument("--limit",type=int,default=20)
    r=s.add_parser("refactor"); r.add_argument("--goal",required=True)
    l=s.add_parser("learn"); l.add_argument("--text",required=True)
    s.add_parser("matrix")
    s.add_parser("profile")
    s.add_parser("release-check")
    a=s.add_parser("agent"); a.add_argument("agent_id")
    b=s.add_parser("beta"); b.add_argument("--scenario",default="memory_failure")
    args=p.parse_args()
    if args.cmd=="validate":
        m=validate()
        print("VALIDAZIONE OK" if not m else "MANCANO: "+", ".join(m))
        for k,v in sorted(count_rows().items()): print(f"{k}: {v}")
        return 0 if not m else 1
    if args.cmd=="status":
        print("MD_OS Stable Core X10")
        for k,v in sorted(count_rows().items()): print(f"{k}: {v}")
    if args.cmd=="query":
        for x in query(args.terms)[:args.limit]: print(f"{x['score']:>4} {x['path']}")
    if args.cmd=="refactor":
        adv,out=run_refactor(args.goal); print(f"REFACTOR completato: {len(adv)} avanzamenti"); print(out)
        for x in adv: print(f"- {x['id']} [{x['tipo']}] {x['azione']}")
    if args.cmd=="learn":
        obj=learn(args.text); print("APPRENDIMENTO SALVATO"); print(", ".join(obj["keywords"]))
    if args.cmd=="matrix":
        print(export_all())
    if args.cmd=="profile":
        prof,out=profile(); print(f"Readiness: {prof['score']}/100"); print(out)
    if args.cmd=="release-check":
        r=check(); print(f"Release: {r['passed']}/{r['total']}"); print(f"Blocker aperti: {len(r['blockers'])}")
    if args.cmd=="agent":
        print(json.dumps(get(args.agent_id),ensure_ascii=False,indent=2))
    if args.cmd=="beta":
        res=beta_run(args.scenario); print(res[1] if res else "Scenario non trovato")
if __name__=="__main__":
    main()
