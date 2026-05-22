"""Neural Mesh execution engine with pluggable agents."""
import json
import sqlite3
from typing import Dict, List, Any
from .database import get_db_path
from .agents import get_agent


class Node:
    """Single mesh node backed by an agent plugin."""

    def __init__(self, node_id: str, node_type: str, config: Dict[str, Any]):
        self.id = node_id
        self.type = node_type
        self.config = config
        self.inputs: List[str] = []
        self.outputs: List[str] = []
        # Validate agent exists immediately
        try:
            self._agent = get_agent(node_type)
        except ValueError as exc:
            raise ValueError(f"Node '{node_id}': {exc}") from exc

    def execute(self, inputs: Dict[str, Any]) -> Any:
        """Delegate to the registered agent plugin."""
        return self._agent.execute(inputs, self.config)


class NeuralMesh:
    """DAG-based mesh runner with SQLite logging."""

    def __init__(self, config: Dict[str, Any], db_path=None):
        self.config = config
        self.db_path = db_path or get_db_path()
        self.nodes: Dict[str, Node] = {}
        self.graph: Dict[str, List[str]] = {}
        self._build_from_config()

    def _build_from_config(self):
        """Construct node objects and adjacency list from config."""
        nodes_cfg = self.config.get("nodes", {})
        if not isinstance(nodes_cfg, dict):
            raise ValueError("'nodes' section must be a mapping of node_id -> definition.")

        for node_id, definition in nodes_cfg.items():
            if not isinstance(definition, dict):
                raise ValueError(f"Node '{node_id}' definition must be a mapping.")
            node_type = definition.get("type", "unknown")
            node_config = definition.get("config", {})
            self.nodes[node_id] = Node(node_id, node_type, node_config)
            self.graph[node_id] = []

        connections = self.config.get("connections", [])
        if not isinstance(connections, list):
            raise ValueError("'connections' section must be a list.")

        for conn in connections:
            if not isinstance(conn, dict):
                continue
            src = conn.get("from")
            dst = conn.get("to")
            if src not in self.nodes:
                raise ValueError(f"Connection references unknown source node: {src}")
            if dst not in self.nodes:
                raise ValueError(f"Connection references unknown target node: {dst}")
            self.graph[src].append(dst)
            self.nodes[dst].inputs.append(src)
            self.nodes[src].outputs.append(dst)

    def run(self) -> Dict[str, Any]:
        """Execute nodes in topological order (Kahn's algorithm simplification).

        Returns:
            dict: node_id -> execution result.
        """
        executed: set = set()
        results: Dict[str, Any] = {}
        queue = [n for n in self.nodes if not self.nodes[n].inputs]

        if not queue:
            raise RuntimeError("Mesh has no source nodes (nodes with zero inputs).")

        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()

        try:
            while queue:
                current = queue.pop(0)
                node = self.nodes[current]
                node_inputs = {src: results[src] for src in node.inputs}

                try:
                    result = node.execute(node_inputs)
                    results[current] = result
                    executed.add(current)
                    cur.execute(
                        "INSERT INTO execution_log (node_id, status, payload) VALUES (?, ?, ?)",
                        (current, "success", json.dumps(result, default=str)),
                    )
                except Exception as exc:
                    cur.execute(
                        "INSERT INTO execution_log (node_id, status, payload) VALUES (?, ?, ?)",
                        (current, "error", str(exc)),
                    )
                    conn.commit()
                    raise RuntimeError(f"Node '{current}' execution failed: {exc}") from exc

                for child in self.graph[current]:
                    if child in executed:
                        continue
                    if all(pred in executed for pred in self.nodes[child].inputs):
                        queue.append(child)

            if len(executed) != len(self.nodes):
                unexecuted = set(self.nodes.keys()) - executed
                raise RuntimeError(f"Mesh execution stalled. Possible cycle or missing inputs for: {unexecuted}")

            conn.commit()
        finally:
            conn.close()

        return results
