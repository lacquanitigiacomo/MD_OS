# plugin/matrice/__init__.py
# Dashboard operativa, export multi-formato, analytics predittive.
# VERSIONE: 2.0.0

import json
import math
from datetime import datetime, timedelta
from pathlib import Path
from nucleo.registro import registro
from nucleo.guardiano import guardiano
from nucleo.costanti import CARTELLA_LOG, RADICE

VERSIONE = "2.0.0"

# ============================================================
# ANALYTICS PREDITTIVE - Trend detection locale
# ============================================================
# Analisi serie temporali sui log per predire problemi.
# Zero ML framework, solo statistica classica.
# ============================================================

class AnaliticaPredittiva:
    def __init__(self):
        self.finestra_giorni = 30

    def trend_errori(self):
        dati = registro.interroga("""
            SELECT 
                date(timestamp) as giorno,
                COUNT(*) as totale,
                SUM(CASE WHEN livello IN ('ERRORE', 'CRITICO') THEN 1 ELSE 0 END) as errori
            FROM nucleo_log
            WHERE timestamp > datetime('now', '-30 days')
            GROUP BY date(timestamp)
            ORDER BY giorno
        """)

        if len(dati) < 3:
            return {"trend": "insufficienti_dati", "previsione": None}

        n = len(dati)
        x = list(range(n))
        y = [d['errori'] for d in dati]

        media_x = sum(x) / n
        media_y = sum(y) / n

        numeratore = sum((xi - media_x) * (yi - media_y) for xi, yi in zip(x, y))
        denominatore = sum((xi - media_x) ** 2 for xi in x)

        pendenza = numeratore / denominatore if denominatore != 0 else 0
        intercetta = media_y - pendenza * media_x

        previsione = intercetta + pendenza * n

        return {
            "trend": "crescente" if pendenza > 0.1 else "decrescente" if pendenza < -0.1 else "stabile",
            "pendenza": round(pendenza, 4),
            "previsione_errori_domani": max(0, round(previsione, 1)),
            "giorni_analizzati": n,
            "alert": previsione > media_y * 1.5
        }

    def health_score(self):
        punteggio = 100

        critici = registro.interroga("""
            SELECT COUNT(*) as n FROM nucleo_log 
            WHERE livello = 'CRITICO' AND timestamp > datetime('now', '-7 days')
        """)[0]['n']
        punteggio -= critici * 10

        errori = registro.interroga("""
            SELECT COUNT(*) as n FROM nucleo_log 
            WHERE livello = 'ERRORE' AND timestamp > datetime('now', '-7 days')
        """)[0]['n']
        punteggio -= min(errori * 2, 30)

        dataset_validi = registro.interroga("""
            SELECT COUNT(*) as n FROM memoria_dataset WHERE validato = 1
        """)[0]['n']
        punteggio += dataset_validi * 5

        agenti = registro.interroga("""
            SELECT COUNT(DISTINCT agente) as n FROM agente_log 
            WHERE timestamp > datetime('now', '-7 days')
        """)[0]['n']
        punteggio += agenti * 10

        return max(0, min(100, punteggio))

    def anomaly_detection(self):
        orarie = registro.interroga("""
            SELECT 
                strftime('%H', timestamp) as ora,
                COUNT(*) as freq
            FROM nucleo_log
            WHERE timestamp > datetime('now', '-7 days')
            GROUP BY strftime('%H', timestamp)
        """)

        if len(orarie) < 5:
            return []

        frequenze = [o['freq'] for o in orarie]
        media = sum(frequenze) / len(frequenze)
        varianza = sum((f - media) ** 2 for f in frequenze) / len(frequenze)
        dev_std = math.sqrt(varianza)

        anomalie = []
        for o in orarie:
            z_score = (o['freq'] - media) / dev_std if dev_std > 0 else 0
            if abs(z_score) > 2:
                anomalie.append({
                    "ora": o['ora'],
                    "frequenza": o['freq'],
                    "z_score": round(z_score, 2),
                    "tipo": "picco" if z_score > 0 else "calo"
                })

        return anomalie

# ============================================================
# EXPORT MULTI-FORMATO
# ============================================================

class Esportatore:
    FORMATI = ["json", "yaml", "html", "csv", "markdown"]

    def esporta(self, formato="json", dati=None):
        if dati is None:
            dati = self._raccogli_dati()

        if formato == "json":
            return json.dumps(dati, indent=2, ensure_ascii=False)
        elif formato == "yaml":
            import yaml
            return yaml.dump(dati, allow_unicode=True, sort_keys=False)
        elif formato == "html":
            return self._to_html(dati)
        elif formato == "csv":
            return self._to_csv(dati)
        elif formato == "markdown":
            return self._to_markdown(dati)
        else:
            return json.dumps(dati, indent=2, ensure_ascii=False)

    def _raccogli_dati(self):
        analitica = AnaliticaPredittiva()

        return {
            "timestamp": datetime.now().isoformat(),
            "versione": "X12",
            "health_score": analitica.health_score(),
            "trend_errori": analitica.trend_errori(),
            "anomalie": analitica.anomaly_detection(),
            "dataset": registro.interroga("SELECT * FROM memoria_dataset"),
            "log_riepilogo": registro.interroga("""
                SELECT livello, COUNT(*) as n 
                FROM nucleo_log 
                WHERE timestamp > datetime('now', '-24 hours')
                GROUP BY livello
            """),
            "agenti_attivi": registro.interroga("""
                SELECT agente, COUNT(*) as esecuzioni, AVG(confidenza) as confidenza_media
                FROM agente_log 
                WHERE timestamp > datetime('now', '-7 days')
                GROUP BY agente
            """),
            "apprendimento": registro.interroga("""
                SELECT COUNT(*) as knowledge_totali,
                       SUM(utilizzi) as utilizzi_totali
                FROM apprendimento_knowledge
            """)
        }

    def _to_html(self, dati):
        health = dati['health_score']
        trend = dati['trend_errori']

        html = f"""<!DOCTYPE html>
<html><head><title>MD_OS Dashboard</title>
<style>
body {{ font-family: system-ui, sans-serif; margin: 40px; background: #0a0a0a; color: #e0e0e0; }}
.card {{ background: #1a1a1a; border-radius: 12px; padding: 20px; margin: 15px 0; border: 1px solid #333; }}
.score {{ font-size: 48px; font-weight: bold; }}
.score.ok {{ color: #4ade80; }} .score.warn {{ color: #fbbf24; }} .score.crit {{ color: #ef4444; }}
h1 {{ color: #60a5fa; }} h2 {{ color: #a78bfa; }}
table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #333; }}
th {{ color: #94a3b8; }}
.alert {{ background: #7f1d1d; color: #fca5a5; padding: 10px; border-radius: 6px; }}
</style></head><body>
<h1>MD_OS Core X12 - Dashboard</h1>
<div class="card">
<h2>Health Score</h2>
<div class="score {'ok' if health > 70 else 'warn' if health > 40 else 'crit'}">
{health}
</div>
</div>
<div class="card"><h2>Trend Errori</h2>
<p>Trend: {trend.get('trend', 'N/A')}</p>
<p>Pendenza: {trend.get('pendenza', 'N/A')}</p>
<p>Previsione domani: {trend.get('previsione_errori_domani', 'N/A')} errori</p>
{'<div class="alert">ALERT: Trend errori in crescita!</div>' if trend.get('alert') else ''}
</div>
<div class="card"><h2>Anomalie</h2><pre>{json.dumps(dati['anomalie'], indent=2)}</pre></div>
<div class="card"><h2>Dataset</h2>
<table><tr><th>Nome</th><th>Righe</th><th>Validato</th></tr>
"""
        for d in dati.get('dataset', []):
            html += f"<tr><td>{d['nome']}</td><td>{d['righe']}</td><td>{'Sì' if d['validato'] else 'No'}</td></tr>"
        html += "</table></div></body></html>"
        return html

    def _to_csv(self, dati):
        righe = ["timestamp,health_score,trend,previsione_errori"]
        trend = dati.get('trend_errori', {})
        righe.append(f"{dati['timestamp']},{dati['health_score']},{trend.get('trend','N/A')},{trend.get('previsione_errori_domani','N/A')}")
        return "
".join(righe)

    def _to_markdown(self, dati):
        md = f"""# MD_OS Dashboard - {dati['timestamp'][:10]}

## Health Score: {dati['health_score']}/100

## Trend Errori
- Direzione: {dati['trend_errori'].get('trend', 'N/A')}
- Previsione domani: {dati['trend_errori'].get('previsione_errori_domani', 'N/A')} errori

## Dataset
"""
        for d in dati.get('dataset', []):
            md += f"- **{d['nome']}**: {d['righe']} righe
"

        md += "
## Agenti Attivi
"
        for a in dati.get('agenti_attivi', []):
            md += f"- **{a['agente']}**: {a['esecuzioni']} esecuzioni (conf: {a.get('confidenza_media', 'N/A')})
"

        return md

esportatore = Esportatore()

# ============================================================
# COMANDI
# ============================================================

def esporta(argomenti):
    formato = argomenti.get("formato", "json")
    if formato not in Esportatore.FORMATI:
        return f"Formati: {', '.join(Esportatore.FORMATI)}"

    risultato = esportatore.esporta(formato)

    percorso = CARTELLA_LOG / f"matrice_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{formato}"
    with open(percorso, 'w', encoding='utf-8') as f:
        f.write(risultato)

    guardiano.logga("INFO", "matrice", "esporta", f"Dashboard esportata in {formato}")
    return f"Dashboard esportata in {percorso}

{risultato[:500]}..."

def profilo(argomenti):
    analitica = AnaliticaPredittiva()

    health = analitica.health_score()
    trend = analitica.trend_errori()
    anomalie = analitica.anomaly_detection()

    output = f"""=======================================
     MD_OS X12 - PROFILO READINESS
=======================================

Health Score:     {health}/100 {'[OK]' if health > 70 else '[WARN]' if health > 40 else '[CRIT]'}
Trend Errori:     {trend['trend']}
Previsione:       {trend.get('previsione_errori_domani', 'N/A')} errori previsti domani
Anomalie:         {len(anomalie)} rilevate
"""

    if anomalie:
        output += "
Anomalie rilevate:
"
        for a in anomalie:
            output += f"  [{a['tipo'].upper()}] Ora {a['ora']}: {a['frequenza']} eventi (z={a['z_score']})
"

    if trend.get('alert'):
        output += "
!!! ALERT: Trend errori in crescita significativa!
"

    return output

def trend(argomenti):
    analitica = AnaliticaPredittiva()
    return json.dumps(analitica.trend_errori(), indent=2, ensure_ascii=False)

COMANDI = {
    "matrice.esporta": esporta,
    "matrice.profilo": profilo,
    "matrice.trend": trend,
}
