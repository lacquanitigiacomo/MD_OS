"""Debug agent — returns inputs and config."""
from .base import BaseAgent


class EchoAgent(BaseAgent):
    def execute(self, inputs, config):
        # If 'value' is set, pass it through directly (useful for feeding strings to other agents)
        if "value" in config:
            return config["value"]
        return {
            "agent": "echo",
            "received_inputs": inputs,
            "received_config": config,
        }
