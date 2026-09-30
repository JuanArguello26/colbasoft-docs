import re, json, sys
import pathlib as _pl
ROOT = _pl.Path(__file__).resolve().parents[2]
HERE_DIR = _pl.Path(__file__).resolve().parent
SPEC = str(ROOT / "01_SPEC_FASE_2" / "COLBASOFT_SPEC_v1.4.md")
L = open(SPEC, encoding="utf8").read().split("\n")

def find(prefix, start=0):
    for i in range(start, len(L)):
        if L[i].startswith(prefix): return i
    raise KeyError(prefix)

# chapter boundaries (line indexes)
c6 = find("# CAPÍTULO 6"); c7 = find("# CAPÍTULO 7"); c8 = find("# CAPÍTULO 8")
c9 = find("# CAPÍTULO 9"); c10 = find("# CAPÍTULO 10"); c11 = find("# CAPÍTULO 11")

# ---------- HU ----------
hus = []
cur_mod = None
i = c6
while i < c7:
    m = re.match(r"^## (M-\d\d) · (.+)$", L[i])
    if m: cur_mod = m.group(1)
    h = re.match(r"^\*\*(HU-\d{3})\*\* · (P\d) · (.+?) · (.*)$", L[i])
    if h:
        hu = dict(id=h.group(1), prio=h.group(2), actor=h.group(3).strip(), tags=h.group(4).strip(), mod=cur_mod)
        story = L[i+1]
        hu["story"] = story
        crit = L[i+2]
        assert crit.startswith("*Criterios:*"), (hu["id"], crit[:40])
        hu["crit_raw"] = crit
        body = crit[len("*Criterios:*"):].strip()
        parts = re.split(r"\s*\((\d+)\)\s+", " " + body)
        # parts: ['', '1', text, '2', text ...]
        crits = []
        for k in range(1, len(parts), 2):
            crits.append((int(parts[k]), parts[k+1].strip()))
        hu["crit"] = crits
        hus.append(hu)
    i += 1

# ---------- RF ----------
rfs = []
cur_mod = None
for i in range(c7, c8):
    m = re.match(r"^## (M-\d\d) · (.+)$", L[i])
    if m: cur_mod = m.group(1)
    r = re.match(r"^\| (RF-\d{3}) \| (.+) \| (P\d) \| (.+?) \| (.+?) \| (.+?) \|$", L[i])
    if r:
        rfs.append(dict(id=r.group(1), text=r.group(2), prio=r.group(3), actor=r.group(4).strip(),
                        dep=r.group(5).strip(), origin=r.group(6).strip(), mod=cur_mod))

# ---------- RNF ----------
rnfs = []
cat = None
for i in range(c8, c9):
    m = re.match(r"^## 8\.(\d+) (.+)$", L[i])
    if m: cat = m.group(2).strip()
    r = re.match(r"^\| (RNF-\d{3}) \| (.+) \| (.+?) \| (.+?) \|$", L[i])
    if r:
        rnfs.append(dict(id=r.group(1), text=r.group(2), verif=r.group(3).strip(), origin=r.group(4).strip(), cat=cat))

# ---------- RN ----------
rns = []
sec = None
for i in range(c9, c10):
    m = re.match(r"^## 9\.(\d+) (.+)$", L[i])
    if m: sec = m.group(2).strip()
    r = re.match(r"^\| \*\*(RN-\d{3}[b]?\*?)\*\* \| (.+) \| (Estructural|Configurable|—) \| (.+?) \|$", L[i])
    if r:
        rns.append(dict(id=r.group(1), text=r.group(2), tipo=r.group(3), origin=r.group(4).strip(), sec=sec))

# ---------- KPI ----------
kpis = []
# first three: headings
for i in range(c10, c11):
    m = re.match(r"^### (KPI-\d\d) · (.+?)( `\[.*)?$", L[i])
    if m:
        k = dict(id=m.group(1), name=m.group(2).strip())
        j = i+1
        while j < c11 and not L[j].startswith("###") and not L[j].startswith("## ") and not L[j].startswith("> "):
            f = re.match(r"^\| \*\*(.+?)\*\* \| (.+) \|$", L[j])
            if f: k[f.group(1)] = f.group(2)
            j += 1
        kpis.append(k)
    r = re.match(r"^\| \*\*(KPI-\d\d)\*\* \| (.+?) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \|$", L[i])
    if r:
        kpis.append({"id": r.group(1), "name": r.group(2), "Qué mide": r.group(3), "Fórmula": r.group(4),
                     "Frecuencia": r.group(5), "Usuario": r.group(6), "Fuente del dato": r.group(7), "Origen": r.group(8)})
kpis.sort(key=lambda k: k["id"])

# ---------- PN / CD / M / RG / DC / PR ----------
pns = []
for i, ln in enumerate(L):
    m = re.match(r"^## (PN-\d\d) — (.+)$", ln)
    if m and i > 600: pns.append(dict(id=m.group(1), name=m.group(2), line=i+1))
cds = []
for i, ln in enumerate(L):
    m = re.match(r"^### (CD-\d\d) · (.+)$", ln)
    if m: cds.append(dict(id=m.group(1), name=m.group(2)))
rgs = []
for i in range(c11, find("# CAPÍTULO 12")):
    r = re.match(r"^\| \*\*(RG-\d\d)\*\* \| \*\*(.+?)\*\*(.*?) \| (Alta|Media|Baja) \| (Alto|Medio|Bajo) \| (\S+) \| (.+) \| (.+) \|$", L[i])
    if r:
        rgs.append(dict(id=r.group(1), title=r.group(2), rest=r.group(3).strip(), prob=r.group(4), imp=r.group(5), sev=r.group(6), mit=r.group(7), origin=r.group(8)))

out = dict(hu=hus, rf=rfs, rnf=rnfs, rn=rns, kpi=kpis, pn=pns, cd=cds, rg=rgs)
json.dump(out, open(HERE_DIR / "spec.json", "w", encoding="utf8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in out.items()})
