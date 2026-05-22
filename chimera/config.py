"""Robust YAML configuration loader."""
import os
from pathlib import Path

try:
    import yaml
except ImportError as e:  # pragma: no cover
    raise ImportError("PyYAML is required. Install: pip install pyyaml") from e


class ConfigError(Exception):
    """Raised when configuration is missing or invalid."""
    pass


def load_config(path=None):
    """Load and validate config.yaml safely.

    Args:
        path: Path to YAML file. Defaults to CHIMERA_CONFIG env var or config.yaml
              in the project root (one level above this file).

    Returns:
        dict: Parsed configuration mapping.
    """
    if path is None:
        env_path = os.getenv("CHIMERA_CONFIG")
        if env_path:
            path = Path(env_path)
        else:
            # Resolve relative to this file: chimera/config.py -> ../config.yaml
            path = Path(__file__).parent.parent / "config.yaml"
    else:
        path = Path(path)

    if not path.exists():
        raise ConfigError(f"Config file not found: {path.resolve()}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        raise ConfigError(f"YAML parse error in {path}: {exc}") from exc
    except Exception as exc:
        raise ConfigError(f"Cannot read config file {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ConfigError("Configuration root must be a YAML mapping (key/value).")

    return data
