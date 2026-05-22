#!/usr/bin/env python3
"""
Generatore evoluzione X10 MD_OS.
Produce 50 versioni successive, ognuna con 10 novita funzionali e innovative.
Output: datasets/evolution_x10_versions.jsonl
"""
import json
from pathlib import Path

VERSIONS = [
    ("V01", "ask-core", "ask CLI, intent detection, answer loop"),
    ("V02", "memory-core", "keyword retrieval, ranking, provenance"),
    ("V03", "agent-orchestrator", "agent selection and local pipeline"),
    ("V04", "quality-loop", "score, blockers, corrective actions"),
    ("V05", "learning-loop", "interactions, feedback, reusable patterns"),
    ("V06", "security-gate", "safe tools, permissions, trusted boundaries"),
    ("V07", "dashboard", "status, metrics, next best action"),
    ("V08", "roadmap-engine", "dynamic priorities and planned evolution"),
    ("V09", "report-engine", "markdown and json operational reports"),
    ("V10", "decision-engine", "planner and next best action intelligence"),
    ("V11", "hybrid-retrieval", "keyword plus metadata retrieval"),
    ("V12", "dataset-governance", "dataset quality, integrity, lifecycle"),
    ("V13", "technical-agents", "CTO, reviewer, strategist refinement"),
    ("V14", "internal-versioning", "versions, regressions, evolution log"),
    ("V15", "beta-lab", "failure scenarios and controlled tests"),
    ("V16", "systems-matrix", "systems, dependencies, leverage points"),
    ("V17", "interactive-session", "continuous interact mode"),
    ("V18", "feedback-weighting", "ranking and agent score from feedback"),
    ("V19", "advanced-provenance", "audit trail for every useful output"),
    ("V20", "local-optimization", "less noise, less latency, more reuse"),
    ("V21", "pattern-intelligence", "recognition of recurring requests"),
    ("V22", "quality-gates", "blocking weak or incoherent changes"),
    ("V23", "department-agents", "agents connected to departments"),
    ("V24", "light-knowledge-graph", "relations without heavy database"),
    ("V25", "cli-composition", "composable and chainable commands"),
    ("V26", "operational-exports", "audit-ready exports"),
    ("V27", "self-diagnosis", "gaps, bottlenecks, missing datasets"),
    ("V28", "decision-memory", "reasoned decision history"),
    ("V29", "ai-emulation-lab", "dataset-first AI capability emulation"),
    ("V30", "external-service-strategy", "paid AI readiness without dependency"),
    ("V31", "adaptive-context", "right context for each task"),
    ("V32", "dataset-compression", "deduplication and information density"),
    ("V33", "agent-scoring", "measured utility of each agent"),
    ("V34", "release-intelligence", "release check informed by quality data"),
    ("V35", "docs-as-system", "documentation usable as operational data"),
    ("V36", "light-semantic-query", "semantic-like matching via patterns"),
    ("V37", "runtime-profiles", "operational modes and profiles"),
    ("V38", "local-audit", "trace significant actions"),
    ("V39", "predictive-maintenance", "predict likely fixes and weak areas"),
    ("V40", "progressive-autonomy", "reduce repeated manual work"),
    ("V41", "multi-output", "plans, patches, reports, checklists"),
    ("V42", "vision-evaluator", "innovation efficiency vision coherence"),
    ("V43", "tool-sandbox", "simulate tools before execution"),
    ("V44", "learning-review", "clean obsolete or weak learning"),
    ("V45", "performance-index", "speed, utility, noise, reuse index"),
    ("V46", "dataset-marketplace", "discover reusable internal datasets"),
    ("V47", "priority-system", "choose best next work by score"),
    ("V48", "dataset-neural-ecosystem", "stronger network of local relations"),
    ("V49", "ai-integration-readiness", "cost benefit gates for external AI"),
    ("V50", "stable-core-x10-evolution", "consolidate into stable core")
]

X10_TYPES = [
    ("dataset", "aggiungere o aggiornare schema dati dedicato"),
    ("cli", "aggiungere hook o comando CLI collegato"),
    ("agent", "definire ruolo agente o responsabilita di sistema"),
    ("metric", "aggiungere metrica verificabile"),
    ("security", "aggiungere controllo sicurezza o confine operativo"),
    ("beta", "aggiungere scenario beta o caso di test"),
    ("report", "aggiungere export, report o vista diagnostica"),
    ("pattern", "aggiungere keyword, pattern o trigger riconoscibile"),
    ("feedback", "aggiungere aggiornamento feedback o score"),
    ("validation", "aggiungere controllo di validazione locale")
]


def build_record(index, version_id, name, goal):
    novita = []
    for n, (kind, action) in enumerate(X10_TYPES, start=1):
        novita.append({
            "n": n,
            "tipo": kind,
            "azione": f"{action} per {name}",
            "criterio_done": f"{version_id}.{n:02d} verificabile tramite dataset, comando, report o test locale"
        })
    return {
        "id": version_id,
        "nome": name,
        "obiettivo": goal,
        "principio_x10": "10 novita funzionali e innovative per ogni versione",
        "novita": novita,
        "score_target": {
            "innovazione": 9,
            "efficienza": 8 + (index % 2),
            "visione": 9
        },
        "dipendenze": [f"V{index-1:02d}"] if index > 1 else [],
        "stato": "pianificato"
    }


def main():
    root = Path(__file__).resolve().parents[1]
    out = root / "datasets" / "evolution_x10_versions.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for index, (version_id, name, goal) in enumerate(VERSIONS, start=1):
            f.write(json.dumps(build_record(index, version_id, name, goal), ensure_ascii=False) + "\n")
    print(f"Generate {len(VERSIONS)} versioni X10 in {out}")
    print(f"Totale novita: {len(VERSIONS) * len(X10_TYPES)}")


if __name__ == "__main__":
    main()
