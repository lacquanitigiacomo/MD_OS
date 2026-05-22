#!/usr/bin/env python3
"""
Test suite MD_OS v11 Chimera
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from md_os_core.nucleo import Nucleo
from md_os_orchestrator.mcp_mock import MCPMockServer
from md_os_orchestrator.a2a_mock import A2AMockRouter
from md_os_orchestrator.bridge import LocalBridge
from md_os_governance.audit import AuditLogger
from md_os_governance.policy import PolicyEngine

def test_nucleo_bootstrap():
    n = Nucleo()
    health = n.health_check()
    assert health["skill_attive"] >= 8, f"Attese >=8 skill, trovate {health['skill_attive']}"
    assert health["versione"] == "11.0.0"
    print("[PASS] nucleo bootstrap")

def test_processa_saluto():
    n = Nucleo()
    r = n.processa("Ciao!")
    assert "output" in r
    assert "Ciao!" in r["output"] or "chimera" in r["output"].lower()
    assert r["confidenza"] > 0.5
    print("[PASS] processa saluto")

def test_processa_calcolo():
    n = Nucleo()
    r = n.processa("calcola somma di 10 20 30")
    assert "60" in r["output"]
    print("[PASS] processa calcolo")

def test_memoria_working():
    n = Nucleo()
    n.memoria.working_set("test_session", "chiave_test", "valore_test")
    v = n.memoria.working_get("test_session", "chiave_test")
    assert v == "valore_test"
    print("[PASS] memoria working")

def test_memoria_episodic():
    n = Nucleo()
    n.memoria.episodic_remember("Evento di test", "utente", 0.8)
    events = n.memoria.episodic_recall("utente", 5)
    assert len(events) >= 1
    print("[PASS] memoria episodic")

def test_mcp_tools():
    n = Nucleo()
    mcp = MCPMockServer(n)
    tools = mcp.handle_request("tools/list")
    assert len(tools["tools"]) >= 4
    print("[PASS] mcp tools list")

def test_mcp_processa():
    n = Nucleo()
    mcp = MCPMockServer(n)
    result = mcp.handle_request("tools/call", {
        "name": "chimera/processa",
        "arguments": {"input": "test"}
    })
    assert "content" in result
    print("[PASS] mcp processa")

def test_a2a_routing():
    a2a = A2AMockRouter()
    a2a.register_agent("agent_test", ["test"])
    msg = a2a.send_message("chimera", "agent_test", "task", {"data": "test"})
    assert "msg_id" in msg
    received = a2a.receive_messages("agent_test")
    assert len(received) >= 1
    print("[PASS] a2a routing")

def test_bridge_full():
    n = Nucleo()
    mcp = MCPMockServer(n)
    a2a = A2AMockRouter()
    bridge = LocalBridge(n, mcp, a2a)
    result = bridge.process_with_protocols("test", use_mcp=True, use_a2a=True)
    assert "core" in result
    assert "mcp" in result
    assert "a2a" in result
    print("[PASS] bridge full stack")

def test_audit_logging():
    audit = AuditLogger()
    audit.log("INFO", "test", "azione_test", "utente_test", "risorsa_test")
    stats = audit.dashboard_stats()
    assert stats["log_totali"] >= 1
    print("[PASS] audit logging")

def test_policy_engine():
    policy = PolicyEngine()
    assert policy.check_access("admin", "delete")["allowed"] is True
    assert policy.check_access("guest", "delete")["allowed"] is False
    assert policy.check_access("user", "read")["allowed"] is True
    print("[PASS] policy engine")

def test_skill_registry():
    n = Nucleo()
    result = n.skill_registry.register("test_skill", "test", ["test_pattern"], "Test: {var}")
    assert result["esito"] == "successo"
    stats = n.skill_registry.stats()
    assert stats["attive"] >= 9  # 8 base + 1 nuova
    print("[PASS] skill registry")

if __name__ == "__main__":
    test_nucleo_bootstrap()
    test_processa_saluto()
    test_processa_calcolo()
    test_memoria_working()
    test_memoria_episodic()
    test_mcp_tools()
    test_mcp_processa()
    test_a2a_routing()
    test_bridge_full()
    test_audit_logging()
    test_policy_engine()
    test_skill_registry()
    print("\n=== TUTTI I TEST SUPERATI ===")
