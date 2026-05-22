"""Transform / reshape data between nodes."""
from .base import BaseAgent


class TransformAgent(BaseAgent):
    def execute(self, inputs, config):
        operation = config.get("operation", "pass")

        # Collect all predecessor outputs
        data = list(inputs.values())
        if len(data) == 1:
            data = data[0]

        if operation == "pass":
            return {"agent": "transform", "result": data}

        elif operation == "extract_field":
            field = config.get("field", "results")
            if isinstance(data, dict):
                return {"agent": "transform", "result": data.get(field)}
            return {"agent": "transform", "result": None, "error": "Data is not a dict"}

        elif operation == "count":
            if isinstance(data, list):
                return {"agent": "transform", "result": len(data)}
            return {"agent": "transform", "result": None, "error": "Data is not a list"}

        elif operation == "join_strings":
            sep = config.get("separator", "\n")
            strings = []
            for d in (data if isinstance(data, list) else [data]):
                if isinstance(d, str):
                    strings.append(d)
                elif isinstance(d, dict):
                    strings.append(str(d))
            return {"agent": "transform", "result": sep.join(strings)}

        elif operation == "to_markdown":
            # Handle web_search results
            if isinstance(data, dict) and "results" in data:
                header = "# " + data.get("query", "Results") + "\n"
                lines = [header]
                for r in data["results"]:
                    title = r.get("title", "Untitled")
                    snippet = r.get("snippet", "")
                    url = r.get("url", "")
                    lines.append("## " + title)
                    lines.append(snippet)
                    lines.append("<" + url + ">")
                    lines.append("")
                return {"agent": "transform", "result": "\n".join(lines)}

            # Handle python stdout JSON
            if isinstance(data, dict) and "stdout" in data:
                import json
                try:
                    payload = json.loads(data["stdout"])
                except Exception:
                    payload = data["stdout"]
                if isinstance(payload, dict) and "dataset" in payload:
                    lines = ["# Analysis Report\n"]
                    lines.append(f"- **Count**: {payload.get('count')}")
                    lines.append(f"- **Mean**: {payload.get('mean')}")
                    lines.append(f"- **Max**: {payload.get('max')}")
                    lines.append(f"- **Min**: {payload.get('min')}")
                    lines.append("")
                    lines.append("## Raw Dataset")
                    lines.append("```json")
                    lines.append(json.dumps(payload.get('dataset'), indent=2))
                    lines.append("```")
                    return {"agent": "transform", "result": "\n".join(lines)}
                return {"agent": "transform", "result": str(payload)}

            # Fallback: stringify
            return {"agent": "transform", "result": str(data)}

        else:
            return {"agent": "transform", "result": data, "warning": f"Unknown operation '{operation}'"}
