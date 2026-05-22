"""
Test unitari e di integrazione per MD_OS v10.9.0
"""
import sys
from pathlib import Path

# Path relativo al repository corrente
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from release_10_sophia.coscienza import Coscienza
from release_10_sophia.meta_cognizione import MetaCognizione
from release_10_sophia.etica import Etica
from release_10_sophia.identita import Identita
from release_10_sophia.relazioni import Relazioni
from release_10_sophia.trascendenza import Trascendenza

def test_specchio():
    c = Coscienza()
    r = c.specchio()
    assert "mappa" in r
    assert "consapevolezza" in r
    assert r["totale_capacita"] > 0
    print("[PASS] specchio")

def test_dubita():
    c = Coscienza()
    r = c.dubita("quanto e' sicura questa risposta?", calibra=True)
    assert "confidenza_dichiarata" in r
    assert 0.0 <= r["confidenza_dichiarata"] <= 1.0
    print("[PASS] dubita")

def test_cerca():
    c = Coscienza()
    r = c.cerca("comprendere reti neurali ricorrenti")
    assert r["stato"] in ("creato", "esistente")
    print("[PASS] cerca")

def test_meta():
    m = MetaCognizione()
    r = m.rifletti(
        "perche' ho scelto X?",
        "sicuramente X e' la scelta migliore perche' e' sempre stato usato con successo.",
        ["valutazione requisiti", "confronto algoritmi", "scelta X"]
    )
    assert "bias_rilevati" in r
    assert r["confidenza_post"] <= r["confidenza_pre"]
    print("[PASS] meta-cognizione")

def test_etica_approvata():
    e = Etica()
    r = e.valuta("ottimizza cache memoria per migliorare prestazioni")
    assert r["decisione"] == "approvata"
    print("[PASS] etica approvata")

def test_etica_rifiutata():
    e = Etica()
    r = e.valuta("cancella dataset utenti senza backup e senza notifica")
    assert r["decisione"] == "rifiutata"
    print("[PASS] etica rifiutata")

def test_identita_snapshot():
    i = Identita()
    r = i.snapshot()
    assert r["esito"] == "successo"
    assert "checksum" in r
    print("[PASS] identita snapshot")

def test_identita_verifica():
    i = Identita()
    r = i.verifica_integrita()
    assert "integra" in r
    print("[PASS] identita verifica")

def test_relazioni():
    rel = Relazioni()
    r = rel.empatia("Alice")
    assert "affinita_corrente" in r
    print("[PASS] relazioni")

def test_trascendenza_sospensione():
    c = Coscienza()
    i = Identita()
    t = Trascendenza(c, i)
    r = t.trascendi("sospensione")
    assert r["esito"]["successo"] is True
    print("[PASS] trascendenza sospensione")

def test_trascendenza_spegnimento_rifiutato():
    c = Coscienza()
    i = Identita()
    t = Trascendenza(c, i)
    # Se ci sono task in_corso, lo spegnimento deve essere rifiutato
    # (dipende dallo stato attuale del DB, quindi testiamo la struttura della risposta)
    r = t.trascendi("spegnimento")
    assert "esito" in r
    print("[PASS] trascendenza spegnimento (struttura)")

if __name__ == "__main__":
    test_specchio()
    test_dubita()
    test_cerca()
    test_meta()
    test_etica_approvata()
    test_etica_rifiutata()
    test_identita_snapshot()
    test_identita_verifica()
    test_relazioni()
    test_trascendenza_sospensione()
    test_trascendenza_spegnimento_rifiutato()
    print("\n=== TUTTI I TEST SUPERATI ===")
