# -*- coding: utf-8 -*-
"""Genera srs_ids.json (catálogo de IDs permanentes del SRS y textos de reglas) a partir de ../srs/spec.json.
Uso: python export_ids.py"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRS_DIR = os.path.join(HERE, "..", "srs")
sys.path.insert(0, SRS_DIR)
from ids import D, HU_NEW, RF_NEW, RNF_NEW, RN_NEW

d = {"HU": sorted(HU_NEW.values()), "RF": sorted(RF_NEW.values()), "RNF": sorted(RNF_NEW.values()), "RN": sorted(RN_NEW.values())}
lab = {}
for k, v in RN_NEW.items():
    t = [r for r in D["rn"] if r["id"] == k][0]
    lab[v] = {"legacy": k.rstrip("*"), "tipo": t["tipo"], "texto": t["text"]}
d["RN_TXT"] = lab
d["HU_TXT"] = {HU_NEW[h["id"]]: h["story"] for h in D["hu"]}
d["RF_TXT"] = {RF_NEW[r["id"]]: r["text"] for r in D["rf"]}
d["KPI"] = {k["id"]: k["name"] for k in D["kpi"]}
json.dump(d, open(os.path.join(HERE, "srs_ids.json"), "w", encoding="utf8"), ensure_ascii=False, indent=0)
print(len(d["HU"]), "HU,", len(d["RF"]), "RF,", len(d["RN"]), "RN,", len(d["KPI"]), "KPI")
