#!/usr/bin/env python3
"""
MD_OS v11 "Chimera" — CLI Principale
Interfaccia a riga di comando che sembra un tool enterprise.
"""
import sys
import json
import argparse
from pathlib import Path

# Aggiungi parent al path
sys.path.insert(0, str(Path(__file__).parent))

from md_os_core.nucleo import Nucleo
from md_os_core.memoria import MemoriaGerarchica
from md_os_orchestrator.mcp_mock import MCPMockServer
from md_os_orchestrator.a2a_mock import A2AMockRouter
from md_os_orchestrator.bridge import LocalBridge
from md_os_governance.audit import AuditLogger
from md_os_governance.policy import PolicyEngine

class ChimeraCLI:
    def __init__(self):
        self.nucleo = Nucleo()
        self.mcp = MCPMockServer(self.nucleo)
        self.a2a = A2AMockRouter()
        self.bridge = LocalBridge(self.nucleo, self.mcp, self.a2a)
        self.audit = AuditLogger()
        self.policy = PolicyEngine()

        # Registra chimera come agent A2A
        self.a2a.register_agent("chimera_master", 
                                ["processamento", "memoria", "orchestrazione"])

    def run(self):
        parser = argparse.ArgumentParser(
            description="MD_OS v11 Chimera — Sistema Operativo per Automazione Intelligente",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Esempi:
  %(prog)s chat "Ciao, come stai?"
  %(prog)s health
  %(prog)s skill list
  %(prog)s mcp tools
  %(prog)s memoria query "progetto"
  %(prog)s audit stats
            """
        )
        subparsers = parser.add_subparsers(dest="command", help="Comandi disponibili")

        # Chat
        chat_parser = subparsers.add_parser("chat", help="Chat con Chimera")
        chat_parser.add_argument("input", help="Input utente")
        chat_parser.add_argument("--mcp", action="store_true", help="Usa protocollo MCP")
        chat_parser.add_argument("--a2a", action="store_true", help="Usa protocollo A2A")

        # Health
        subparsers.add_parser("health", help="Health check completo")

        # Skill
        skill_parser = subparsers.add_parser("skill", help="Gestione skill")
        skill_sub = skill_parser.add_subparsers(dest="skill_cmd")
        skill_sub.add_parser("list", help="Lista skill")
        skill_sub.add_parser("stats", help="Statistiche skill")

        # MCP
        mcp_parser = subparsers.add_parser("mcp", help="Protocollo MCP")
        mcp_sub = mcp_parser.add_subparsers(dest="mcp_cmd")
        mcp_sub.add_parser("tools", help="Lista tool MCP")
        mcp_sub.add_parser("init", help="Inizializza MCP")

        # Memoria
        mem_parser = subparsers.add_parser("memoria", help="Gestione memoria")
        mem_sub = mem_parser.add_subparsers(dest="mem_cmd")
        mem_query = mem_sub.add_parser("query", help="Query memoria")
        mem_query.add_argument("query", help="Query string")
        mem_sub.add_parser("status", help="Status memoria")

        # Audit
        audit_parser = subparsers.add_parser("audit", help="Audit e governance")
        audit_sub = audit_parser.add_subparsers(dest="audit_cmd")
        audit_sub.add_parser("stats", help="Statistiche audit")

        # A2A
        a2a_parser = subparsers.add_parser("a2a", help="Protocollo A2A")
        a2a_sub = a2a_parser.add_subparsers(dest="a2a_cmd")
        a2a_sub.add_parser("topology", help="Topologia rete agent")

        args = parser.parse_args()

        if not args.command:
            parser.print_help()
            return

        self._execute(args)

    def _execute(self, args):
        if args.command == "chat":
            result = self.bridge.process_with_protocols(
                args.input, 
                use_mcp=args.mcp, 
                use_a2a=args.a2a
            )
            print(json.dumps(result, indent=2, ensure_ascii=False))

        elif args.command == "health":
            health = self.bridge.health_full()
            print(json.dumps(health, indent=2, ensure_ascii=False))

        elif args.command == "skill":
            if args.skill_cmd == "list":
                skills = self.nucleo.lista_skill()
                for s in skills:
                    print(f"  [{s['categoria']}] {s['nome']} (usi: {s['usi_count']}, conf: {s['confidenza']})")
            elif args.skill_cmd == "stats":
                stats = self.nucleo.skill_registry.stats()
                print(json.dumps(stats, indent=2, ensure_ascii=False))

        elif args.command == "mcp":
            if args.mcp_cmd == "tools":
                tools = self.mcp.handle_request("tools/list")
                for t in tools.get("tools", []):
                    print(f"  {t['name']}: {t['description']}")
            elif args.mcp_cmd == "init":
                init = self.mcp.handle_request("initialize")
                print(json.dumps(init, indent=2, ensure_ascii=False))

        elif args.command == "memoria":
            if args.mem_cmd == "query":
                result = self.nucleo.memoria.ricerca(args.query)
                print(result)
            elif args.mem_cmd == "status":
                print(self.nucleo.memoria.status())

        elif args.command == "audit":
            if args.audit_cmd == "stats":
                stats = self.audit.dashboard_stats()
                print(json.dumps(stats, indent=2, ensure_ascii=False))

        elif args.command == "a2a":
            if args.a2a_cmd == "topology":
                topo = self.a2a.get_topology()
                print(json.dumps(topo, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    cli = ChimeraCLI()
    cli.run()
