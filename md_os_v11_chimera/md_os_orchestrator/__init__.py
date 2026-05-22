"""
MD_OS v11 "Chimera" — Orchestrator
Simula MCP e A2A protocolli usando HTTP locale e file.
Zero costi, zero API esterne.
"""
__version__ = "11.0.0"

from .mcp_mock import MCPMockServer
from .a2a_mock import A2AMockRouter
from .bridge import LocalBridge

__all__ = ["MCPMockServer", "A2AMockRouter", "LocalBridge"]
