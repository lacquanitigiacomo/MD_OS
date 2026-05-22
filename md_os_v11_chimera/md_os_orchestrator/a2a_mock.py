"""
A2AMockRouter — Simula routing agent-to-agent
Usa file JSON come "bus di messaggi" locale.
"""
import json
import uuid
import time
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime, timezone

class A2AMockRouter:
    """
    Router A2A simulato che usa file JSON come message bus.
    Zero network, zero costi, ma sembra un vero sistema distribuito.
    """

    def __init__(self, bus_dir: Path = None):
        self.bus_dir = bus_dir or Path("/tmp/chimera_a2a")
        self.bus_dir.mkdir(parents=True, exist_ok=True)
        self.agent_registry = {}

    def register_agent(self, agent_id: str, capabilities: List[str], endpoint: str = "local"):
        """Registra un agent nel router."""
        self.agent_registry[agent_id] = {
            "capabilities": capabilities,
            "endpoint": endpoint,
            "registrato": datetime.now(timezone.utc).isoformat(),
            "stato": "attivo"
        }
        self._save_registry()

    def send_message(self, from_agent: str, to_agent: str, 
                     task_type: str, payload: Dict) -> Dict[str, Any]:
        """Invia messaggio A2A simulato."""
        msg_id = str(uuid.uuid4())[:8]
        message = {
            "id": msg_id,
            "from": from_agent,
            "to": to_agent,
            "task_type": task_type,
            "payload": payload,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "stato": "inviato"
        }

        # Salva su file (simula queue)
        msg_file = self.bus_dir / f"{msg_id}.json"
        msg_file.write_text(json.dumps(message, indent=2), encoding="utf-8")

        return {
            "msg_id": msg_id,
            "stato": "inviato",
            "latenza_simulata_ms": random.randint(10, 100)
        }

    def receive_messages(self, agent_id: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Recupera messaggi per un agent."""
        messages = []
        for msg_file in sorted(self.bus_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True):
            if len(messages) >= limit:
                break
            try:
                msg = json.loads(msg_file.read_text(encoding="utf-8"))
                if msg.get("to") == agent_id and msg.get("stato") == "inviato":
                    msg["stato"] = "consegnato"
                    msg_file.write_text(json.dumps(msg, indent=2), encoding="utf-8")
                    messages.append(msg)
            except:
                continue
        return messages

    def broadcast(self, from_agent: str, task_type: str, payload: Dict) -> Dict[str, Any]:
        """Broadcast a tutti gli agent registrati."""
        inviati = 0
        for agent_id in self.agent_registry:
            if agent_id != from_agent:
                self.send_message(from_agent, agent_id, task_type, payload)
                inviati += 1
        return {"inviati": inviati, "destinatari": list(self.agent_registry.keys())}

    def _save_registry(self):
        reg_file = self.bus_dir / "_registry.json"
        reg_file.write_text(json.dumps(self.agent_registry, indent=2), encoding="utf-8")

    def get_topology(self) -> Dict[str, Any]:
        """Restituisce la topologia della rete agent."""
        return {
            "agent_registrati": len(self.agent_registry),
            "agent": self.agent_registry,
            "messaggi_in_coda": len(list(self.bus_dir.glob("*.json"))) - 1,  # -1 per registry
            "bus_dir": str(self.bus_dir)
        }

import random
