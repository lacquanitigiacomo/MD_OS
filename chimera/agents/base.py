"""Base class for all CHIMERA agents."""
from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseAgent(ABC):
    """Every agent must implement execute()."""

    @abstractmethod
    def execute(self, inputs: Dict[str, Any], config: Dict[str, Any]) -> Any:
        """Run the agent.

        Args:
            inputs: Results from predecessor nodes (node_id -> result).
            config: Node-specific parameters from config.yaml.

        Returns:
            Any serializable result.
        """
        pass
