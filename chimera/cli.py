#!/usr/bin/env python3
"""CHIMERA 2.0 CLI entry point."""
import argparse
import sys
from .config import load_config, ConfigError
from .database import init_db, get_db_path
from .mesh import NeuralMesh


def main():
    parser = argparse.ArgumentParser(
        prog="chimera",
        description="CHIMERA 2.0 Neural Mesh — Local-first automation platform",
    )
    sub = parser.add_subparsers(dest="cmd")

    # init
    p_init = sub.add_parser("init", help="Initialize local database")

    # run
    p_run = sub.add_parser("run", help="Execute the mesh defined in config.yaml")

    # status
    p_status = sub.add_parser("status", help="Show project status and paths")

    args = parser.parse_args()

    if args.cmd == "init":
        try:
            db = init_db()
            print(f"[OK] Database initialized: {db}")
        except Exception as exc:
            print(f"[ERR] Init failed: {exc}", file=sys.stderr)
            sys.exit(1)

    elif args.cmd == "run":
        try:
            cfg = load_config()
        except ConfigError as exc:
            print(f"[ERR] {exc}", file=sys.stderr)
            sys.exit(1)

        db = init_db()
        mesh = NeuralMesh(cfg)
        nodes_cfg = cfg.get("nodes", {})
        conns = cfg.get("connections", [])
        print(f"[OK] Mesh loaded: {len(mesh.nodes)} nodes, {len(conns)} connections")
        print(f"[OK] Database: {db}")
        results = mesh.run()
        print("[OK] Execution complete.")
        for node_id, res in results.items():
            agent = "unknown"
            if isinstance(res, dict):
                agent = res.get("agent", "unknown")
                if "output" in res:
                    summary = res["output"]
                elif "result" in res:
                    summary = res["result"]
                elif "count" in res:
                    summary = f"count={res['count']}"
                elif "bytes_written" in res:
                    summary = f"written {res['bytes_written']} bytes"
                elif "content" in res:
                    summary = f"read {len(str(res['content']))} chars"
                elif "stdout" in res:
                    summary = f"rc={res.get('returncode')} stdout={len(res['stdout'])} chars"
                else:
                    summary = str(res)[:80]
            else:
                summary = str(res)[:80]
            print(f"  -> {node_id} ({agent}): {summary}")

    elif args.cmd == "status":
        print(f"Database path : {get_db_path()}")
        try:
            cfg = load_config()
            nodes = cfg.get("nodes", {})
            conns = cfg.get("connections", [])
            print(f"Config path   : resolved automatically")
            print(f"Nodes defined : {len(nodes)}")
            print(f"Connections   : {len(conns)}")
        except ConfigError:
            print("Config path   : not found or invalid")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
