"""
LocalBridge — Ponte tra core e orchestrator
Gestisce il flusso dati locale senza network.
"""
import json
from pathlib import Path
from typing import Dict, Any

class LocalBridge:
    """
    Bridge che collega Nucleo, MCP e A2A in un unico flusso locale.
    """

    def __init__(self, nucleo=None, mcp=None, a2a=None):
        self.nucleo = nucleo
        self.mcp = mcp
        self.a2a = a2a

    def process_with_protocols(self, input_utente: str, 
                               use_mcp: bool = False,
                               use_a2a: bool = False) -> Dict[str, Any]:
        """
        Processa input opzionalmente attraverso protocolli simulati.
        """
        result = {"input": input_utente, "protocols_used": []}

        # Step 1: Processa con nucleo
        if self.nucleo:
            core_result = self.nucleo.processa(input_utente)
            result["core"] = core_result

        # Step 2: Se richiesto, esponi via MCP
        if use_mcp and self.mcp:
            mcp_result = self.mcp.handle_request("tools/call", {
                "name": "chimera/processa",
                "arguments": {"input": input_utente}
            })
            result["mcp"] = mcp_result
            result["protocols_used"].append("mcp")

        # Step 3: Se richiesto, broadcast via A2A
        if use_a2a and self.a2a:
            a2a_result = self.a2a.broadcast("chimera_master", "task", {
                "input": input_utente,
                "core_result": result.get("core", {})
            })
            result["a2a"] = a2a_result
            result["protocols_used"].append("a2a")

        return result

    def health_full(self) -> Dict[str, Any]:
        """Health check completo di tutto lo stack."""
        health = {
            "bridge": "ok",
            "timestamp": __import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat()
        }
        if self.nucleo:
            health["core"] = self.nucleo.health_check()
        if self.mcp:
            health["mcp"] = {"tools": len(self.mcp.tools), "mock": True}
        if self.a2a:
            health["a2a"] = self.a2a.get_topology()
        return health
