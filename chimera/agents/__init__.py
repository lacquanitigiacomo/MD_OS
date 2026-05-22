"""CHIMERA 2.0 Agent Plugins."""
from .base import BaseAgent
from .echo import EchoAgent
from .web_search import WebSearchAgent
from .python import PythonAgent
from .file_io import FileReadAgent, FileWriteAgent
from .transform import TransformAgent

REGISTRY = {
    "echo": EchoAgent,
    "web_search": WebSearchAgent,
    "python": PythonAgent,
    "file_read": FileReadAgent,
    "file_write": FileWriteAgent,
    "transform": TransformAgent,
}

def get_agent(name: str):
    if name not in REGISTRY:
        raise ValueError(f"Unknown agent type '{name}'. Available: {list(REGISTRY.keys())}")
    return REGISTRY[name]()
