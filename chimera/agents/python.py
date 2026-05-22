"""Execute Python code safely in a subprocess."""
import json
import subprocess
import sys
import tempfile
import os
from .base import BaseAgent


class PythonAgent(BaseAgent):
    def execute(self, inputs, config):
        code = config.get("code", "")
        if not code and inputs:
            first = list(inputs.values())[0]
            if isinstance(first, str):
                code = first

        if not code:
            return {"error": "No Python code provided. Set 'code' in node config or pass a string from a predecessor."}

        # Serialize inputs so the script can access them
        inputs_json = json.dumps(inputs, default=str)

        wrapper = (
            "import json, sys, math, random, statistics, datetime, itertools, collections, re, "
            "string, hashlib, fractions, decimal, typing, inspect, textwrap, pprint, csv, "
            "os, pathlib, time, uuid, base64, html\n\n"
            "inputs = json.loads(" + repr(inputs_json) + ")\n\n"
            "# User code starts here\n"
            + code + "\n"
        )

        try:
            with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as f:
                f.write(wrapper)
                tmp = f.name

            proc = subprocess.run(
                [sys.executable, tmp],
                capture_output=True,
                text=True,
                timeout=config.get("timeout", 10),
            )
            os.unlink(tmp)
        except subprocess.TimeoutExpired:
            return {"error": "Python execution timed out.", "code": code}
        except Exception as exc:
            return {"error": f"Execution failed: {exc}", "code": code}

        return {
            "agent": "python",
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "returncode": proc.returncode,
            "code": code,
        }
