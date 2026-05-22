"""Read and write local files relative to project root."""
import json
from pathlib import Path
from .base import BaseAgent


class FileReadAgent(BaseAgent):
    def execute(self, inputs, config):
        path = Path(config.get("path", "data/input.json"))
        if not path.is_absolute():
            path = Path(__file__).parent.parent.parent / path

        if not path.exists():
            return {"error": f"File not found: {path}", "path": str(path)}

        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as exc:
            return {"error": f"Read failed: {exc}", "path": str(path)}

        # Try to parse as JSON
        try:
            data = json.loads(content)
        except Exception:
            data = content

        return {"agent": "file_read", "path": str(path), "content": data}


class FileWriteAgent(BaseAgent):
    def execute(self, inputs, config):
        path = Path(config.get("path", "data/output.json"))
        if not path.is_absolute():
            path = Path(__file__).parent.parent.parent / path

        path.parent.mkdir(parents=True, exist_ok=True)

        # Gather data: from config or from predecessor outputs
        data = config.get("data")
        if data is None and inputs:
            # Use the first predecessor result
            first = list(inputs.values())[0]
            data = first

        if data is None:
            return {"error": "No data to write. Set 'data' in config or connect a predecessor."}

        try:
            text = json.dumps(data, indent=2, ensure_ascii=False, default=str)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        except Exception as exc:
            return {"error": f"Write failed: {exc}", "path": str(path)}

        return {"agent": "file_write", "path": str(path), "bytes_written": len(text)}
