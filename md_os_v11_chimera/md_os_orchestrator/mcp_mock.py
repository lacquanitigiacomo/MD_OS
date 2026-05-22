"""
MCPMockServer — Simula un server MCP completo
Risponde a tool/list, tool/call, resources/list come un vero MCP server.
Ma tutto e' locale, in-memory, zero costi.
"""
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime, timezone

class MCPMockServer:
    """
    Mock MCP server che gira su file JSON e SQLite locale.
    Sembra un vero server MCP ma non chiama nessuna API esterna.
    """

    def __init__(self, nucleo=None):
        self.nucleo = nucleo
        self.tools = self._default_tools()
        self.resources = {}

    def _default_tools(self) -> Dict[str, Dict[str, Any]]:
        return {
            "chimera/health": {
                "description": "Health check del sistema Chimera",
                "inputSchema": {"type": "object", "properties": {}},
                "handler": self._tool_health
            },
            "chimera/skill_list": {
                "description": "Lista skill disponibili",
                "inputSchema": {"type": "object", "properties": {"categoria": {"type": "string"}}},
                "handler": self._tool_skill_list
            },
            "chimera/memoria_query": {
                "description": "Query memoria gerarchica",
                "inputSchema": {"type": "object", "properties": {"query": {"type": "string"}}},
                "handler": self._tool_memoria_query
            },
            "chimera/processa": {
                "description": "Processa input utente",
                "inputSchema": {"type": "object", "properties": {"input": {"type": "string"}}},
                "handler": self._tool_processa
            },
            "chimera/log_export": {
                "description": "Esporta log sistema",
                "inputSchema": {"type": "object", "properties": {"limit": {"type": "integer", "default": 100}}},
                "handler": self._tool_log_export
            }
        }

    def handle_request(self, method: str, params: Dict = None) -> Dict[str, Any]:
        """Entry point per richieste MCP simulate."""
        params = params or {}

        if method == "tools/list":
            return {
                "tools": [
                    {"name": name, "description": tool["description"], "inputSchema": tool["inputSchema"]}
                    for name, tool in self.tools.items()
                ]
            }

        elif method == "tools/call":
            tool_name = params.get("name")
            arguments = params.get("arguments", {})
            if tool_name in self.tools:
                try:
                    result = self.tools[tool_name]["handler"](**arguments)
                    return {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]}
                except Exception as e:
                    return {"content": [{"type": "text", "text": f"Errore: {e}"}], "isError": True}
            return {"content": [{"type": "text", "text": f"Tool '{tool_name}' non trovato"}], "isError": True}

        elif method == "resources/list":
            return {"resources": [{"uri": f"chimera://{k}", "name": k} for k in self.resources.keys()]}

        elif method == "initialize":
            return {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}, "resources": {}},
                "serverInfo": {"name": "chimera-mcp", "version": "11.0.0"}
            }

        return {"error": f"Metodo '{method}' non supportato"}

    def _tool_health(self) -> Dict[str, Any]:
        if self.nucleo:
            return self.nucleo.health_check()
        return {"stato": "ok", "mock": True}

    def _tool_skill_list(self, categoria: str = None) -> Dict[str, Any]:
        if self.nucleo:
            return {"skills": self.nucleo.lista_skill()}
        return {"skills": []}

    def _tool_memoria_query(self, query: str) -> Dict[str, Any]:
        if self.nucleo:
            return {"risultato": self.nucleo.memoria.ricerca(query)}
        return {"risultato": "Nucleo non disponibile"}

    def _tool_processa(self, input: str) -> Dict[str, Any]:
        if self.nucleo:
            return self.nucleo.processa(input)
        return {"errore": "Nucleo non disponibile"}

    def _tool_log_export(self, limit: int = 100) -> Dict[str, Any]:
        return {"messaggio": f"Log export simulato: {limit} righe", "formato": "jsonl"}

    def export_openapi(self) -> Dict[str, Any]:
        """Genera spec OpenAPI finta per sembrare enterprise."""
        return {
            "openapi": "3.0.0",
            "info": {"title": "Chimera MCP API", "version": "11.0.0"},
            "paths": {f"/mcp/{tool}": {"post": {"summary": self.tools[tool]["description"]}} 
                     for tool in self.tools}
        }
