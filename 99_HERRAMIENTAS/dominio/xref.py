# -*- coding: utf-8 -*-
import re, json, os, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from dm_data import *
from ev_data import EVENTS
from gl_data import TERMS
import io as _io, contextlib as _cl
with _cl.redirect_stdout(_io.StringIO()):
    from build_f4 import RISKS_F5

import pathlib as _pl
B = str(_pl.Path(__file__).resolve().parents[2])
S = json.load(open(os.path.join(os.path.dirname(__file__), "srs_ids.json"), encoding="utf8"))
docs = {
 "SRS": os.path.join(B, "02_SRS_FASE_3", "SRS_COLBASOFT_v1.3.md"),
 "DM": os.path.join(B, "03_DOMINIO_FASE_4", "DOMAIN_MODEL.md"),
 "EC": os.path.join(B, "03_DOMINIO_FASE_4", "EVENT_CATALOG.md"),
 "GL": os.path.join(B, "03_DOMINIO_FASE_4", "GLOSSARY.md"),
 "CL": os.path.join(B, "CLAUDE.md"),
}
# documentos de control del CP-04 (se verifican si existen)
for _k, _f in [("AU", "04_CP04_AUDITORIA.md"), ("CI", "04_CP04_CIERRE.md"), ("DP", "04_CP04_DECISIONES_PENDIENTES.md")]:
    _p = os.path.join(B, "04_CP04_AUDITORIA", _f)
    if os.path.exists(_p):
        docs[_k] = _p
T = {k: open(v, encoding="utf8").read() for k, v in docs.items()}
spec = open(os.path.join(B, "01_SPEC_FASE_2", "COLBASOFT_SPEC_v1.3.md"), encoding="utf8").read()

valid = {
 "HU": set(S["HU"]), "RF": set(S["RF"]), "RN": set(S["RN"]), "RNF": set(S["RNF"]),
 "KPI": {f"KPI-{i:02d}" for i in range(1, 25)}, "CU": {f"CU-{i:02d}" for i in range(1, 25)},
 "DEC": {f"DEC-{i:02d}" for i in range(1, 10)}, "H": {f"H-{i:02d}" for i in range(1, 21)},
 "RS": {f"R-S{i:02d}" for i in range(1, 11)}, "HD": {h[0] for h in DOMAIN_FINDINGS},
 "EV": {e["id"] for e in EVENTS}, "E": {e["id"] for e in ENTITIES}, "VO": {v[0] for v in VALUE_OBJECTS},
 "AG": {a[0] for a in AGGREGATES}, "IN": {i[0] for i in INVARIANTS}, "SM": {s[0] for s in STATE_MACHINES},
 "SD": {s["id"] for s in SUBDOMAINS}, "RF5": {r[0] for r in RISKS_F5},
 "PN": {f"PN-{i:02d}" for i in range(1, 15)}, "CD": {f"CD-{i:02d}" for i in range(1, 50)},
 "M": {f"M-{i:02d}" for i in range(1, 21)}, "RG": {f"RG-{i:02d}" for i in range(1, 43)},
 "DC": {f"DC-{i:02d}" for i in range(1, 9)}, "PR": {f"PR-{i:02d}" for i in range(1, 7)},
 "GL": {f"GL-{i:03d}" for i in range(1, len(TERMS) + 1)}, "PO": {f"PO-{i:02d}" for i in range(1, 15)},
 "CA": {f"CA-{i:02d}" for i in range(1, 39)}, "OP": {f"OP-{i:02d}" for i in range(1, 13)},
 "D": {f"D-{i:02d}" for i in range(1, 13)},
}
pats = [
 ("HU", r"\bHU-[A-Z]{3}-\d{3}\b"), ("RF", r"\bRF-[A-Z]{3}-\d{3}\b"), ("RNF", r"\bRNF-[A-Z]{3}-\d{3}\b"), ("RN", r"\bRN-[A-Z]{3}-\d{3}\b"),
 ("KPI", r"\bKPI-\d{2}\b"), ("CU", r"\bCU-\d{2}\b"), ("DEC", r"\bDEC-\d{2}\b"), ("H", r"(?<![A-Z-])H-\d{2}\b"), ("RS", r"\bR-S\d{2}\b"),
 ("HD", r"\bHD-\d{2}\b"), ("EV", r"\bEV-[A-Z]{3}-\d{3}\b"), ("E", r"(?<![A-Z-])E-\d{2}\b"), ("VO", r"\bVO-\d{2}\b"), ("AG", r"\bAG-\d{2}\b"),
 ("IN", r"\bIN-\d{2}\b"), ("SM", r"\bSM-\d{2}\b"), ("SD", r"\bSD-\d{2}\b"), ("RF5", r"\bRF5-\d{2}\b"), ("PN", r"\bPN-\d{2}\b"),
 ("CD", r"\bCD-\d{2}\b"), ("M", r"(?<![A-Z-])M-\d{2}\b"), ("RG", r"\bRG-\d{2}\b"), ("DC", r"\bDC-\d{2}\b"), ("PR", r"\bPR-\d{2}\b"),
 ("GL", r"\bGL-\d{3}\b"), ("PO", r"\bPO-\d{2}\b"), ("CA", r"\bCA-\d{2}\b"), ("OP", r"\bOP-\d{2}\b"), ("D", r"(?<![A-Z-])D-\d{2}\b"),
]
bad = defaultdict(Counter)
for dk, txt in T.items():
    for kind, p in pats:
        for m in re.findall(p, txt):
            if m not in valid[kind]:
                bad[dk][f"{kind}:{m}"] += 1
for dk, c in bad.items():
    print(dk, dict(c))
# legacy SPEC ids used in phase-4 docs outside allowed contexts
unpaired = r"(?<![A-Z-])(?:RNF|RN|HU|RF)-\d{3}b?(?![\w-])(?!\s*(?:→|\())"
for dk in ["DM", "EC", "GL"]:
    leg = re.findall(unpaired, T[dk])
    if leg:
        print(dk, "IDs del SPEC sin emparejar con su ID del SRS:", Counter(leg).most_common(12))
# tablas con columnas descuadradas
for dk, txt in T.items():
    L = txt.split("\n"); badrows = 0; i = 0
    while i < len(L):
        if not L[i].startswith("|"):
            i += 1; continue
        j = i
        while j < len(L) and L[j].startswith("|"):
            j += 1
        n0 = re.sub(r"`[^`]*`", "", L[i]).count("|")
        badrows += sum(1 for k in range(i, j) if re.sub(r"`[^`]*`", "", L[k]).count("|") != n0)
        i = j
    if badrows:
        print(dk, "filas de tabla descuadradas:", badrows)
print("Verificación terminada: sin salida adicional = sin errores.")
