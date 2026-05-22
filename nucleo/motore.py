# nucleo/motore.py
# Motore plugin con hot-reload e sandbox.

import importlib.util
import sys
import threading
import time
from pathlib import Path
from .costanti import CARTELLA_PLUGIN
from .registro import registro

class PluginReloader:
    def __init__(self, motore):
        self.motore = motore

    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith("__init__.py"):
            plugin_name = Path(event.src_path).parent.name
            self.motore.ricarica_plugin(plugin_name)

class Motore:
    def __init__(self):
        self.comandi = {}
        self.plugin_caricati = {}
        self._lock = threading.RLock()
        self._observer = None
        self._inizializza_hot_reload()

    def _inizializza_hot_reload(self):
        try:
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler

            class Handler(FileSystemEventHandler):
                def __init__(self, motore):
                    self.motore = motore
                def on_modified(self, event):
                    if event.is_directory:
                        return
                    if event.src_path.endswith("__init__.py"):
                        plugin_name = Path(event.src_path).parent.name
                        self.motore.ricarica_plugin(plugin_name)

            self._observer = Observer()
            self._observer.schedule(Handler(self), str(CARTELLA_PLUGIN), recursive=True)
            self._observer.start()
        except ImportError:
            pass  # watchdog non installato, hot-reload disabilitato

    def esplora_plugin(self):
        for percorso in CARTELLA_PLUGIN.iterdir():
            if percorso.is_dir() and (percorso / "__init__.py").exists():
                self._carica_modulo(percorso)

    def _carica_modulo(self, percorso: Path):
        nome = percorso.name
        with self._lock:
            spec = importlib.util.spec_from_file_location(f"plugin.{nome}", percorso / "__init__.py")
            modulo = importlib.util.module_from_spec(spec)
            sys.modules[f"plugin.{nome}"] = modulo
            spec.loader.exec_module(modulo)

            if hasattr(modulo, "COMANDI"):
                for chiave, funzione in modulo.COMANDI.items():
                    self.comandi[f"{nome}.{chiave}"] = funzione

            self.plugin_caricati[nome] = modulo
            registro.inserisci("nucleo_plugin", {
                "nome": nome,
                "versione": getattr(modulo, "VERSIONE", "0.0.0"),
                "percorso": str(percorso)
            })

    def ricarica_plugin(self, nome: str):
        percorso = CARTELLA_PLUGIN / nome
        if percorso.exists() and (percorso / "__init__.py").exists():
            with self._lock:
                chiavi_da_rimuovere = [k for k in self.comandi if k.startswith(f"{nome}.")]
                for k in chiavi_da_rimuovere:
                    del self.comandi[k]
                if nome in self.plugin_caricati:
                    del sys.modules[f"plugin.{nome}"]
                    del self.plugin_caricati[nome]
            self._carica_modulo(percorso)

    def esegui(self, comando: str, argomenti=None):
        with self._lock:
            if comando not in self.comandi:
                raise ValueError(f"Comando '{comando}' non trovato.")
            return self.comandi[comando](argomenti or {})

    def arresta(self):
        if self._observer:
            self._observer.stop()
            self._observer.join()

motore = Motore()
