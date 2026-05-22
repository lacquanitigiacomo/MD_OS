"""
PolicyEngine — Engine policy che sembra enterprise
Regole JSON-based, aggiornabili a caldo, zero costi.
"""
import json
import re
from pathlib import Path
from typing import Dict, List, Any

class PolicyEngine:
    """
    Engine policy semplice ma credibile.
    Le policy sono file JSON che definiscono regole di accesso e comportamento.
    """

    def __init__(self, policy_dir: Path = None):
        self.policy_dir = policy_dir or Path(__file__).parent / "policies"
        self.policy_dir.mkdir(parents=True, exist_ok=True)
        self.policies = {}
        self._load_policies()

    def _load_policies(self):
        """Carica tutte le policy JSON dalla directory."""
        for policy_file in self.policy_dir.glob("*.json"):
            try:
                self.policies[policy_file.stem] = json.loads(policy_file.read_text(encoding="utf-8"))
            except:
                pass

        # Policy di default se vuoto
        if not self.policies:
            self._create_default_policies()

    def _create_default_policies(self):
        defaults = {
            "access_control": {
                "version": "1.0",
                "rules": [
                    {"role": "admin", "allow": ["*"]},
                    {"role": "user", "allow": ["read", "execute"], "deny": ["delete", "config"]},
                    {"role": "guest", "allow": ["read"], "deny": ["execute", "write"]}
                ]
            },
            "rate_limiting": {
                "version": "1.0",
                "limits": [
                    {"role": "user", "requests_per_minute": 60},
                    {"role": "guest", "requests_per_minute": 10}
                ]
            },
            "data_retention": {
                "version": "1.0",
                "rules": [
                    {"data_type": "log", "retention_days": 90},
                    {"data_type": "session", "retention_days": 7},
                    {"data_type": "audit", "retention_days": 365}
                ]
            }
        }
        for name, policy in defaults.items():
            self.set_policy(name, policy)

    def set_policy(self, name: str, policy: Dict[str, Any]):
        """Crea o aggiorna una policy."""
        self.policies[name] = policy
        policy_file = self.policy_dir / f"{name}.json"
        policy_file.write_text(json.dumps(policy, indent=2), encoding="utf-8")

    def check_access(self, role: str, action: str) -> Dict[str, Any]:
        """Verifica se un ruolo puo' eseguire un'azione."""
        policy = self.policies.get("access_control", {})
        rules = policy.get("rules", [])

        for rule in rules:
            if rule.get("role") == role:
                if "*" in rule.get("allow", []):
                    return {"allowed": True, "reason": "Admin wildcard"}
                if action in rule.get("deny", []):
                    return {"allowed": False, "reason": f"Action '{action}' denied for role '{role}'"}
                if action in rule.get("allow", []):
                    return {"allowed": True, "reason": f"Action '{action}' explicitly allowed"}

        return {"allowed": False, "reason": f"No matching policy for role '{role}'"}

    def get_retention(self, data_type: str) -> int:
        """Restituisce giorni di retention per un tipo di dato."""
        policy = self.policies.get("data_retention", {})
        for rule in policy.get("rules", []):
            if rule.get("data_type") == data_type:
                return rule.get("retention_days", 30)
        return 30

    def list_policies(self) -> List[str]:
        """Lista policy disponibili."""
        return list(self.policies.keys())
