"""
MD_OS v10.9.0 — Comandi CLI
Registrazione dei comandi nel motore del nucleo congelato.
"""
from .coscienza import Coscienza
from .meta_cognizione import MetaCognizione
from .etica import Etica
from .identita import Identita
from .relazioni import Relazioni
from .trascendenza import Trascendenza

class SophiaCommands:
    """Adapter che registra tutti i comandi della Release 10 nel motore MD_OS."""

    def __init__(self):
        self.coscienza = Coscienza()
        self.meta = MetaCognizione()
        self.etica = Etica()
        self.identita = Identita()
        self.relazioni = Relazioni()
        self.trascendenza = Trascendenza(self.coscienza, self.identita)

    def registra(self, motore):
        """Registra tutti i comandi nel motore."""
        comandi = {
            "coscienza.specchio": self.cmd_specchio,
            "coscienza.dubita": self.cmd_dubita,
            "coscienza.cerca": self.cmd_cerca,
            "coscienza.ricorda": self.cmd_ricorda,
            "coscienza.pianifica": self.cmd_pianifica,
            "coscienza.agenda_prossima": self.cmd_agenda_prossima,
            "coscienza.meta": self.cmd_meta,
            "coscienza.storico_bias": self.cmd_storico_bias,
            "coscienza.etica": self.cmd_etica,
            "coscienza.report_etico": self.cmd_report_etico,
            "coscienza.empatia": self.cmd_empatia,
            "coscienza.relazione": self.cmd_relazione,
            "coscienza.relazioni.lista": self.cmd_lista_relazioni,
            "coscienza.snapshot": self.cmd_snapshot,
            "coscienza.ripristina": self.cmd_ripristina,
            "coscienza.verifica": self.cmd_verifica,
            "coscienza.trascendi": self.cmd_trascendi,
            "coscienza.storico_trascendenza": self.cmd_storico_trasc,
        }
        for nome, funzione in comandi.items():
            motore.registra(nome, funzione)

    def cmd_specchio(self, args: dict):
        return self.coscienza.specchio(filtro_stato=args.get("stato"))

    def cmd_dubita(self, args: dict):
        return self.coscienza.dubita(args.get("query", ""), args.get("calibra", False))

    def cmd_cerca(self, args: dict):
        return self.coscienza.cerca(args.get("obiettivo", ""))

    def cmd_ricorda(self, args: dict):
        return self.coscienza.ricorda(args.get("dalla_nascita", False))

    def cmd_pianifica(self, args: dict):
        return self.coscienza.pianifica(args.get("orizzonte", "mese"))

    def cmd_agenda_prossima(self, args: dict):
        return self.coscienza.agenda_prossima()

    def cmd_meta(self, args: dict):
        return self.meta.rifletti(args.get("ragionamento", ""), args.get("ragionamento", ""), args.get("passaggi", []))

    def cmd_storico_bias(self, args: dict):
        return self.meta.storico_bias(int(args.get("limit", 20)))

    def cmd_etica(self, args: dict):
        return self.etica.valuta(args.get("azione", ""), args.get("contesto"), args.get("revisore"))

    def cmd_report_etico(self, args: dict):
        return self.etica.report_etico(int(args.get("limit", 50)))

    def cmd_empatia(self, args: dict):
        return self.relazioni.empatia(args.get("utente", ""))

    def cmd_relazione(self, args: dict):
        return {"storia": self.relazioni.storia(args.get("con", "")), "modello": self.relazioni.empatia(args.get("con", ""))}

    def cmd_lista_relazioni(self, args: dict):
        return self.relazioni.lista_entita()

    def cmd_snapshot(self, args: dict):
        return self.identita.snapshot()

    def cmd_ripristina(self, args: dict):
        from pathlib import Path
        p = args.get("da")
        return self.identita.ripristina(Path(p) if p else None)

    def cmd_verifica(self, args: dict):
        return self.identita.verifica_integrita()

    def cmd_trascendi(self, args: dict):
        return self.trascendenza.trascendi(args.get("operazione", ""), args.get("nodo_destinazione"))

    def cmd_storico_trasc(self, args: dict):
        return self.trascendenza.storico_trascendenza(int(args.get("limit", 20)))
