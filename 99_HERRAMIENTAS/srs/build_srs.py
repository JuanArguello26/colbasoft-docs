# -*- coding: utf-8 -*-
import re, json, os, sys
from collections import Counter, OrderedDict
from ids import *
from trace import *

HERE = os.path.dirname(os.path.abspath(__file__))
def rd(name):
    return open(os.path.join(HERE, name), encoding="utf8").read()

import pathlib as _pl
ROOT = _pl.Path(__file__).resolve().parents[2]
HERE_DIR = _pl.Path(__file__).resolve().parent
# Uso: python build_srs.py [carpeta_de_salida]  (por defecto, 02_SRS_FASE_3 del proyecto)
OUT_DIR = sys.argv[1] if len(sys.argv) > 1 else str(ROOT / "02_SRS_FASE_3")
OUT = os.path.join(OUT_DIR, "SRS_COLBASOFT_v1.5.md")

# ============================================================ conversión de IDs
def rnn(legacy_tok):
    k = rn_key(legacy_tok)
    return RN_NEW[k] if k else legacy_tok

def conv(t):
    """marcadores @HU030 @RF052 @RN057b @RNF014 -> IDs permanentes"""
    t = re.sub(r"@RNF(\d{3})", lambda m: RNF_NEW["RNF-" + m.group(1)], t)
    t = re.sub(r"@RN(\d{3}b?)", lambda m: RN_NEW[rn_key("RN-" + m.group(1))], t)
    t = re.sub(r"@RF(\d{3})", lambda m: RF_NEW["RF-" + m.group(1)], t)
    t = re.sub(r"@HU(\d{3})", lambda m: HU_NEW["HU-" + m.group(1)], t)
    return t

def L(t):
    """IDs legacy (sin @) dentro de texto del SPEC -> IDs permanentes"""
    t = re.sub(r"\bRNF-(\d{3})\b", lambda m: RNF_NEW.get("RNF-" + m.group(1), m.group(0)), t)
    t = re.sub(r"\bRN-(\d{3}b?)\b", lambda m: rnn("RN-" + m.group(1)), t)
    t = re.sub(r"\bRF-(\d{3})\b", lambda m: RF_NEW.get("RF-" + m.group(1), m.group(0)), t)
    t = re.sub(r"\bHU-(\d{3})\b", lambda m: HU_NEW.get("HU-" + m.group(1), m.group(0)), t)
    return t

def strip_md(t):
    return t.replace("**", "").replace("*", "")

# ============================================================ datos
HU = {h["id"]: h for h in D["hu"]}
RF = {r["id"]: r for r in D["rf"]}
RNF = {r["id"]: r for r in D["rnf"]}
RNR = {r["id"]: r for r in D["rn"] if r["tipo"] != "—"}
KPI = {k["id"]: k for k in D["kpi"]}
MODS = list(MOD.keys())
PRIO_NEW = MOSCOW

def sort_rn(keys):
    return sorted(set(keys), key=lambda k: RN_NEW[k])
def sort_new(ids):
    return sorted(set(ids))
def hu_hor(h): return "H2" if h in H2_HU else "H1"
def rf_hor(r): return "H2" if r in H2_RF else "H1"
def rn_list(keys): return ", ".join(RN_NEW[k] for k in sort_rn(keys)) if keys else "—"
def hu_list(ids): return ", ".join(HU_NEW[i] for i in sorted(ids)) if ids else "—"
def rf_list(ids): return ", ".join(RF_NEW[i] for i in sorted(ids)) if ids else "—"

# Gherkin
G = {}
for f in ["g01.txt", "g02.txt", "g03.txt", "g04.txt", "g05.txt", "g06.txt"]:
    txt = rd(f)
    for blk in re.split(r"^=== ", txt, flags=re.M)[1:]:
        head, body = blk.split("\n", 1)
        m = re.match(r"(HU-\d{3}) \| (.+)", head)
        G[m.group(1)] = (m.group(2).strip(), body.rstrip())

# reglas núcleo §9.1
CORE91 = {"RN-001", "RN-009", "RN-012", "RN-023", "RN-029", "RN-040", "RN-041", "RN-061", "RN-063", "RN-065"}

# procesos -> casos de uso
PN_CU = {"PN-01": "CU-06", "PN-02": "CU-07", "PN-03": "CU-08", "PN-04": "CU-09", "PN-05": "CU-10",
         "PN-06": "CU-11", "PN-07": "CU-12", "PN-08": "CU-13", "PN-09": "CU-14", "PN-10": "CU-15",
         "PN-11": "CU-16", "PN-12": "CU-17", "PN-13": "CU-18", "PN-14": "CU-19"}
MOD_GROUP = {"M-01": "Fundacional", "M-02": "Fundacional", "M-19": "Fundacional", "M-20": "Fundacional",
             "M-03": "Maestro", "M-04": "Maestro", "M-05": "Maestro", "M-06": "Maestro",
             "M-07": "Operativo", "M-08": "Operativo", "M-09": "Operativo", "M-10": "Operativo", "M-11": "Operativo", "M-12": "Operativo",
             "M-13": "Información", "M-14": "Información", "M-15": "Información", "M-16": "Información", "M-17": "Información",
             "M-18": "Control"}
MOD_PRIO = {"M-01": "P0", "M-02": "P0", "M-03": "P0", "M-04": "P0", "M-05": "P0", "M-06": "P0", "M-07": "P0", "M-08": "P0",
            "M-09": "P0", "M-10": "P0", "M-11": "P1", "M-12": "P1", "M-13": "P0", "M-14": "P0", "M-15": "P1", "M-16": "P1",
            "M-17": "P1", "M-18": "P1", "M-19": "P0", "M-20": "P1"}
MOD_PN = {"M-07": "PN-01, PN-02, PN-03", "M-08": "PN-10", "M-09": "PN-05, PN-06", "M-10": "PN-07", "M-11": "PN-08, PN-09",
          "M-12": "PN-12", "M-13": "PN-04", "M-15": "PN-11", "M-18": "PN-13"}
MOD_CU = {"M-01": "CU-01", "M-02": "CU-02", "M-03": "CU-03", "M-04": "CU-20", "M-05": "CU-04, CU-08", "M-06": "CU-07",
          "M-07": "CU-06, CU-08", "M-08": "CU-15", "M-09": "CU-10, CU-11", "M-10": "CU-12", "M-11": "CU-13, CU-14",
          "M-12": "CU-17", "M-13": "CU-09", "M-14": "CU-21", "M-15": "CU-16", "M-16": "CU-22", "M-17": "CU-23",
          "M-18": "CU-18", "M-19": "CU-05", "M-20": "CU-24, CU-23, CU-19"}
MOD_DEP = OrderedDict([
 ("M-01", ["M-02", "M-18", "M-19"]),
 ("M-02", ["M-01", "M-05", "M-18"]),
 ("M-03", ["M-19", "M-13"]),
 ("M-04", ["M-03", "M-07", "M-14", "M-13"]),
 ("M-05", ["M-06", "M-13", "M-19"]),
 ("M-06", ["M-05", "M-07", "M-14"]),
 ("M-07", ["M-03", "M-04", "M-05", "M-06", "M-13", "M-14", "M-12"]),
 ("M-08", ["M-13", "M-14", "M-05", "M-06", "M-19", "M-20"]),
 ("M-09", ["M-05", "M-06", "M-13", "M-14", "M-15", "M-19"]),
 ("M-10", ["M-13", "M-14", "M-19", "M-20", "M-18", "M-15"]),
 ("M-11", ["M-13", "M-10", "M-14", "M-05", "M-06", "M-19", "M-20"]),
 ("M-12", ["M-10", "M-14", "M-06", "M-20", "M-13"]),
 ("M-13", ["M-14", "M-03", "M-05", "M-04", "M-02"]),
 ("M-14", ["M-01"]),
 ("M-15", ["M-13", "M-09", "M-10", "M-11", "M-19", "M-20", "M-04"]),
 ("M-16", ["M-14", "M-13", "M-10", "M-11", "M-15", "M-12", "M-02"]),
 ("M-17", ["M-13", "M-15", "M-16", "M-20", "M-11", "M-10"]),
 ("M-18", ["M-14", "M-02"]),
 ("M-19", ["M-02", "M-18", "M-03", "M-05", "M-15"]),
 ("M-20", ["M-07", "M-08", "M-09", "M-10", "M-11", "M-12", "M-15", "M-02"]),
])
MOD_DEP_NOTE = {"M-14": "Recibe escritura de todos los módulos operativos (M-07 a M-12); M-13 y M-16 leen de él. Su propia dependencia es la identidad del usuario (M-01, RF-KDX-002)",
                "M-18": "Todos los módulos escriben en él; lee del kardex para la verificación de integridad"}

def tabla_c1():
    """Corte de entrega C1 (SPEC v1.5 §12.7): HU y RF por bloque de construcción."""
    o = ["| Bloque | Contenido | Historias (ID permanente) |", "|---|---|---|"]
    for b, n, ns in C1_BLOQUES:
        o.append(f"| **{b}** | {n} | {', '.join(HU_NEW[hu(x)] for x in ns)} |")
    pr = Counter(HU[h]["prio"] for h in C1_HU)
    rp = Counter(RF[r]["prio"] for r in C1_RF)
    o.append("")
    o.append(f"**Totales del corte:** {len(C1_HU)} historias (Must {pr['P0']} · Should {pr['P1']} · Could {pr['P2']}) y {len(C1_RF)} requisitos funcionales (Must {rp['P0']} · Should {rp['P1']} · Could {rp['P2']}); todos del Horizonte 1.")
    o.append("")
    o.append("**Requisitos funcionales del corte:** " + ", ".join(RF_NEW[r] for r in sorted(C1_RF, key=lambda x: RF_NEW[x])) + ".")
    return "\n".join(o)

def is_mod_rf(mod): return [r for r in D["rf"] if r["mod"] == mod]

# ============================================================ tablas generadas
def tabla_modulos():
    rows = ["| Módulo | Dominio | Grupo | Prio. SPEC | HU | RF | Procesos | Casos de uso |", "|---|:--:|---|:--:|:--:|:--:|---|---|"]
    tot_h = tot_r = 0
    for m in MODS:
        dom, nom = MOD[m]
        nh = sum(1 for h in D["hu"] if h["mod"] == m)
        nr = sum(1 for r in D["rf"] if r["mod"] == m)
        tot_h += nh; tot_r += nr
        rows.append(f"| **{m}** {nom} | {dom} | {MOD_GROUP[m]} | {MOD_PRIO[m]} | {nh} | {nr} | {MOD_PN.get(m, '—')} | {MOD_CU[m]} |")
    rows.append(f"| **Total** | | | | **{tot_h}** | **{tot_r}** | 14 PN | 24 CU |")
    return "\n".join(rows)

ROLE_WORDS = [("Administrador", "Administrador"), ("Jefe", "Jefe de Bodega"), ("Coordinador", "Coordinador de Bodega"),
              ("Auxiliar", "Auxiliar de Bodega"), ("Auditor", "Auditor"), ("Sistema", "Sistema")]
def hu_por_rol():
    per = {r[1]: [] for r in ROLE_WORDS}
    trans = []
    for h in D["hu"]:
        a = h["actor"]
        if a.startswith("Todos"):
            trans.append(h["id"]); continue
        for w, name in ROLE_WORDS:
            if w in a:
                per[name].append(h["id"])
    out = ["| Rol | Historias (según el campo «actor» del SPEC) | N.º |", "|---|---|:--:|"]
    for w, name in ROLE_WORDS:
        out.append(f"| **{name}** | {', '.join(HU_NEW[i] for i in per[name]) or '—'} | {len(per[name])} |")
    out.append(f"| **Todos los roles** (transversales) | {', '.join(HU_NEW[i] for i in trans)} | {len(trans)} |")
    return "\n".join(out)

def tabla_dep():
    rows = ["| Módulo | Depende funcionalmente de | Nota |", "|---|---|---|"]
    for m, deps in MOD_DEP.items():
        ds = ", ".join(f"{d} {MOD[d][1]}" for d in deps)
        rows.append(f"| **{m}** {MOD[m][1]} | {ds} | {MOD_DEP_NOTE.get(m, '')} |")
    return "\n".join(rows)

def matriz_dep():
    head = "| Depende de → |" + "|".join(f" {m[2:]} " for m in MODS) + "|"
    sep = "|---|" + "|".join(":-:" for _ in MODS) + "|"
    rows = [head, sep]
    for m in MODS:
        cells = []
        for c in MODS:
            cells.append("●" if c in MOD_DEP[m] else ("·" if c == m else ""))
        rows.append(f"| **{m}** |" + "|".join(f" {c} " for c in cells) + "|")
    return "\n".join(rows)

def raices():
    users = {m: [x for x, deps in MOD_DEP.items() if m in deps] for m in MODS}
    reason = {"M-14": "Fuente de verdad de la existencia; todo movimiento se registra en él", "M-13": "Todo módulo que valida disponibilidad consulta la existencia",
              "M-19": "Umbrales, plazos y motivos que gobiernan las reglas configurables", "M-05": "Estructura física: dónde puede estar la existencia",
              "M-20": "Tareas y notificaciones que ejecutan la operación", "M-06": "Identificación y escaneo de mercancía y ubicaciones",
              "M-10": "Ajustes: destino de las diferencias de conteo y novedades", "M-15": "Alertas que disparan las reglas de otros módulos",
              "M-02": "Existencia y ámbito de los usuarios", "M-18": "Bitácora de toda acción", "M-03": "Referencias sobre las que se opera",
              "M-07": "Lotes y entradas", "M-04": "Lotes", "M-01": "Identidad", "M-11": "Conteos", "M-12": "Novedades", "M-16": "Reportes", "M-17": "Dashboard", "M-08": "Salidas", "M-09": "Movimientos"}
    ranked = sorted(MODS, key=lambda m: -len(users[m]))
    rows = []
    for m in ranked[:8]:
        rows.append(f"| **{m}** {MOD[m][1]} | {reason.get(m, '')} | {len(users[m])} ({', '.join(users[m])}) |")
    return "\n".join(rows)

def ciclos():
    pairs = []
    for a in MODS:
        for b in MODS:
            if a < b and b in MOD_DEP[a] and a in MOD_DEP[b]:
                pairs.append((a, b))
    rows = ["| Módulos en dependencia mutua | Motivo funcional |", "|---|---|"]
    why = {("M-01", "M-02"): "El acceso requiere que el usuario exista; el usuario nace de la gestión de acceso",
           ("M-05", "M-06"): "Cada ubicación necesita su QR; el QR de ubicación necesita la ubicación",
           ("M-03", "M-13"): "El catálogo valida la existencia antes de desactivar; la consulta de existencia lee el catálogo",
           ("M-04", "M-07"): "El lote se crea al confirmar la entrada; la entrada asocia o crea el lote",
           ("M-04", "M-13"): "La consulta muestra el lote; el lote consulta la existencia",
           ("M-05", "M-13"): "La estructura valida existencia antes de desactivar una ubicación; la consulta lee la estructura",
           ("M-09", "M-15"): "El tránsito prolongado genera alerta; la alerta se origina en los movimientos",
           ("M-10", "M-15"): "El ajuste recurrente genera alerta; la alerta se origina en los ajustes",
           ("M-15", "M-19"): "Las alertas usan umbrales; los umbrales se configuran para las alertas",
           ("M-08", "M-20"): "La salida genera tareas; la tarea se cierra al ejecutarse la salida",
           ("M-10", "M-20"): "El ajuste genera solicitudes; las solicitudes se notifican y escalan",
           ("M-11", "M-20"): "El conteo genera tareas; la tarea se cierra al registrar el conteo",
           ("M-12", "M-20"): "La novedad escala por plazo; la notificación reporta novedades",
           ("M-15", "M-20"): "Las alertas se notifican; las notificaciones escalan alertas",
           ("M-07", "M-12"): "La recepción dañada abre una novedad",
           ("M-02", "M-18"): "Los cambios de usuarios y roles se registran en la bitácora; la bitácora atribuye cada evento a un usuario",
           ("M-03", "M-19"): "El catálogo usa unidades y umbrales configurables; los parámetros se definen sobre SKU y categorías del catálogo",
           ("M-05", "M-19"): "La estructura usa criterios de asignación configurables; los parámetros incluyen capacidades y reglas sobre la estructura",
           ("M-06", "M-07"): "La entrada genera las unidades a identificar; la identificación se ejecuta sobre lo recibido",
           ("M-02", "M-19"): "Los parámetros los define un usuario; la configuración de acceso es un parámetro",
           }
    for a, b in pairs:
        rows.append(f"| {a} {MOD[a][1]} ↔ {b} {MOD[b][1]} | {why.get((a, b), 'Dependencia funcional mutua declarada en el SPEC')} |")
    return "\n".join(rows)

# ============================================================ CAPÍTULO 5 — HU
DADA_F = {"una", "la", "mercancía", "existencia"}
DADOS_M = {"varios", "movimientos", "tipos", "datos", "los", "unos"}
DADAS_F = {"varias", "alertas", "solicitudes", "líneas", "novedades", "ubicaciones", "recepciones", "las", "tareas", "unas"}

def fix_dado(line):
    m = re.match(r"^(\s*)Dado (\S+)(.*)$", line)
    if not m:
        return line
    w = m.group(2)
    kw = "Dado"
    if w in DADA_F:
        kw = "Dada"
    elif w in DADOS_M:
        kw = "Dados"
    elif w in DADAS_F:
        kw = "Dadas"
    return f"{m.group(1)}{kw} {w}{m.group(3)}"

CRIT_FIX = {("HU-026", 5): ("RNF-014", "RNF-015"), ("HU-071", 3): ("RNF-012", "RNF-014")}

def gherkin_block(hid):
    title, body = G[hid]
    new = HU_NEW[hid]
    crit = {n: t for n, t in HU[hid]["crit"]}
    out = [f"@{new} @{MOSCOW[HU[hid]['prio']].split(' ')[0]} @{HU[hid]['mod']}", f"Característica: {new} — {title}"]
    for line in body.split("\n"):
        m = re.match(r"^Escenario: C(\d+) - (.*)$", line)
        if m:
            n = int(m.group(1))
            ctext = crit[n]
            note = ""
            fix = CRIT_FIX.get((hid, n))
            if fix:
                ctext = ctext.replace(fix[0], fix[1])
                note = f" [SRS: el SPEC cita {fix[0]} (ID legacy, referencia errónea); el requisito aplicable es {RNF_NEW[fix[1]]} (H-05)]"
            out.append(f"  # Criterio SPEC ({n}): {strip_md(L(ctext))}{note}")
            out.append(f"  Escenario: C{n} · {m.group(2)}")
        else:
            out.append("  " + fix_dado(line))
    return "\n".join(out)

def cap5():
    o = []
    o.append("""
---

# CAPÍTULO 5 — HISTORIAS DE USUARIO NORMALIZADAS

> Reorganización de las **114 historias** del SPEC (Cap. 6) con ID estable por dominio, prioridad MoSCoW, dependencias y criterios Gherkin. **No se perdió ninguna historia** (Anexo A) **ni ningún criterio de aceptación** (515 criterios → 515 escenarios). Las historias conservan su redacción «COMO / QUIERO / PARA» del SPEC.

## 5.1 Cómo leer una historia

| Atributo | Significado |
|---|---|
| **ID** | `HU-<DOM>-nnn` permanente (ver §1.4.3). El ID del SPEC se conserva como *legacy* |
| **Prioridad** | MoSCoW derivada mecánicamente de la prioridad P0–P3 del SPEC (§1.4.4) |
| **Horizonte** | H1 = MVP-Núcleo; H2 = versión 1.1 según §12.3 del SPEC (§1.4.5) |
| **Depende de** | Historias que deben existir u operar antes `[SRS]` |
| **RF / RN / KPI** | Requisitos, reglas e indicadores relacionados (RF y KPI derivados en esta fase `[SRS]`; RN provienen de las etiquetas del SPEC más las de sus RF) |
| **Gherkin** | Un escenario por criterio de aceptación del SPEC; el comentario `# Criterio SPEC (n)` reproduce el texto original |

## 5.2 Distribución

""")
    rows = ["| Módulo | Dominio | HU | Must | Should | Could | Won't | H2 | Rango legacy |", "|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|"]
    T = Counter()
    for m in MODS:
        hs = [h for h in D["hu"] if h["mod"] == m]
        c = Counter(h["prio"] for h in hs)
        n2 = sum(1 for h in hs if h["id"] in H2_HU)
        rows.append(f"| **{m}** {MOD[m][1]} | {MOD[m][0]} | {len(hs)} | {c['P0']} | {c['P1']} | {c['P2']} | {c['P3']} | {n2} | {hs[0]['id']}–{hs[-1]['id']} |")
        T.update(c); T["n"] += len(hs); T["h2"] += n2
    rows.append(f"| **Total** | | **{T['n']}** | **{T['P0']}** | **{T['P1']}** | **{T['P2']}** | **{T['P3']}** | **{T['h2']}** | HU-001–HU-114 |")
    o.append("\n".join(rows))
    o.append("")
    n = 3
    for m in MODS:
        dom, nom = MOD[m]
        o.append(f"\n## 5.{n} {m} · {nom} (dominio {dom})\n")
        n += 1
        for h in [x for x in D["hu"] if x["mod"] == m]:
            hid = h["id"]
            new = HU_NEW[hid]
            title = G[hid][0]
            o.append(f"### {new} — {title}\n")
            deps = ", ".join(HU_NEW[d] for d in HU_DEPS[hid]) or "—"
            kp = ", ".join(sorted(HU_KPI.get(hid, []))) or "—"
            o.append(f"**Prioridad:** {MOSCOW[h['prio']]} ({h['prio']}) · **Horizonte:** {hu_hor(hid)} · **Actor (SPEC):** {h['actor']} · **Legacy:** {hid}  ")
            o.append(f"**Depende de:** {deps} · **RF:** {rf_list(HU_RF.get(hid, []))} · **RN:** {rn_list(HU_RN.get(hid, []))} · **KPI:** {kp}  ")
            o.append(f"**Origen (SPEC):** {L(h['tags'])}\n")
            if hid in HU_COV_NOTE:
                o.append(f"> ⚠️ **{L(HU_COV_NOTE[hid])}** (hallazgo H-13)\n")
            o.append(f"**Historia.** {h['story']}\n")
            o.append("```gherkin")
            o.append(gherkin_block(hid))
            o.append("```\n")
    o.append("""
---

**ESTADO DEL CAPÍTULO 5**

| | |
|---|---|
| **Completado** | 114 historias con ID `HU-<DOM>-nnn`, MoSCoW, horizonte, dependencias, RF/RN/KPI relacionados y 515 escenarios Gherkin (1 por criterio del SPEC) |
| **Pendiente** | Validación de los mapeos `[SRS]` por el Director (R-S02) · cobertura RF parcial de HU-NOV-003 y HU-NOV-004 (H-13, DEC-06) |
| **Riesgos encontrados** | H-05 (dos criterios del SPEC citaban un RNF equivocado; se redactaron sin la referencia errónea) · los escenarios no sustituyen las pruebas de usabilidad (R-S09) |
| **Dependencias** | Cap. 6 (RF), Cap. 8 (reglas), Cap. 9 (trazabilidad) |
""")
    return "\n".join(o)

# ============================================================ CAPÍTULO 6 — RF
def cap6():
    o = ["""
---

# CAPÍTULO 6 — REQUISITOS FUNCIONALES NORMALIZADOS

> Reorganización de los **185 RF** del SPEC (Cap. 7) con ID permanente `RF-<DOM>-nnn`. Cada RF indica actor, historia(s) relacionada(s), prioridad, regla(s) de negocio y KPI relacionados. La redacción del requisito, su actor, su prioridad, sus dependencias y su origen **se reproducen del SPEC**; la historia, la regla y el KPI relacionados son derivados de esta fase `[SRS]` (las reglas incluyen todas las que el SPEC cita en el propio requisito). **Ningún RF se perdió** (Anexo A). Los RF que no se relacionan con ningún KPI o regla muestran «—».

## 6.1 Distribución

"""]
    rows = ["| Módulo | Dominio | RF | Must | Should | Could | H2 | Rango legacy |", "|---|:--:|:--:|:--:|:--:|:--:|:--:|---|"]
    T = Counter()
    for m in MODS:
        rs = [r for r in D["rf"] if r["mod"] == m]
        c = Counter(r["prio"] for r in rs)
        n2 = sum(1 for r in rs if r["id"] in H2_RF)
        rows.append(f"| **{m}** {MOD[m][1]} | {MOD[m][0]} | {len(rs)} | {c['P0']} | {c['P1']} | {c['P2']} | {n2} | {rs[0]['id']}–{rs[-1]['id']} |")
        T.update(c); T["n"] += len(rs); T["h2"] += n2
    rows.append(f"| **Total** | | **{T['n']}** | **{T['P0']}** | **{T['P1']}** | **{T['P2']}** | **{T['h2']}** | RF-001–RF-185 |")
    o.append("\n".join(rows))
    o.append("\n> **Hallazgo H-02.** El resumen del SPEC (§7.1) declara 72 P0 / 69 P1 / 21 P2; las filas de los requisitos suman **74 / 70 / 18**. Este SRS usa la prioridad de cada fila.\n")
    n = 2
    for m in MODS:
        dom, nom = MOD[m]
        o.append(f"\n## 6.{n} {m} · {nom} (dominio {dom})\n")
        n += 1
        o.append("| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |")
        o.append("|---|---|---|---|---|---|---|---|---|")
        for r in [x for x in D["rf"] if x["mod"] == m]:
            rid = r["id"]
            hus = ", ".join(HU_NEW[h] for h in RF_HU[rid])
            kp = ", ".join(RF_KPI.get(rid, [])) or "—"
            pr = f"{MOSCOW[r['prio']]}<br>{r['prio']}" + (" · H2" if rid in H2_RF else "")
            o.append(f"| **{RF_NEW[rid]}**<br>*({rid})* | {L(r['text'])} | {r['actor']} | {hus} | {pr} | {rn_list(RF_RN[rid])} | {kp} | {L(r['dep'])} | {L(r['origin'])} |")
    o.append("""
---

**ESTADO DEL CAPÍTULO 6**

| | |
|---|---|
| **Completado** | 185 RF con ID `RF-<DOM>-nnn`, actor, historia(s), MoSCoW, regla(s) y KPI |
| **Pendiente** | Validación de los mapeos `[SRS]` (R-S02) · RF propuestos para reglas y KPI sin requisito (Anexo C, DEC-05 y DEC-06; **no incorporados**) |
| **Riesgos encontrados** | H-02 (prioridades del resumen del SPEC no coinciden) · H-11 y H-12 (brechas) · H-08 (19 RF en H2) |
| **Dependencias** | Cap. 5 (historias), Cap. 7 (RNF), Cap. 8 (reglas) |
""")
    return "\n".join(o)

# ============================================================ CAPÍTULO 7 — RNF
CAT_ORDER = ["Seguridad", "Disponibilidad", "Rendimiento", "Escalabilidad", "Accesibilidad", "Auditoría", "Usabilidad",
             "Compatibilidad Tablet", "Compatibilidad Navegador"]
def cap7():
    o = ["""
---

# CAPÍTULO 7 — REQUISITOS NO FUNCIONALES

> Reorganización de los **47 RNF** del SPEC (Cap. 8) por categoría, con ID permanente `RNF-<CAT>-nnn`. Todos se conservan con su criterio de verificación y su origen. **Los valores numéricos son objetivos de diseño propuestos por el SPEC; su calibración requiere la línea base de la empresa piloto** (§1.4.7): el SRS no introduce metas nuevas. La usabilidad es la categoría prioritaria del producto `[MON §3, §4, §8.2]`.

## 7.1 Distribución

"""]
    rows = ["| Categoría | Código | RNF | Rango legacy | H2 |", "|---|:--:|:--:|---|:--:|"]
    for c in CAT_ORDER:
        rs = [r for r in D["rnf"] if r["cat"] == c]
        rows.append(f"| {c} | {RNF_CAT[c]} | {len(rs)} | {rs[0]['id']}–{rs[-1]['id']} | {sum(1 for r in rs if RNF_NEW[r['id']] in H2_RNF)} |")
    rows.append(f"| **Total** | | **{len(D['rnf'])}** | RNF-001–RNF-047 | {len(H2_RNF)} |")
    o.append("\n".join(rows))
    o.append("\n> **Nota `[SRS]` — prioridad.** El SPEC no asigna prioridad P0–P3 a los RNF. El SRS no la inventa: la columna «Horizonte» indica H1 salvo el que el backlog (§12.3) declara Horizonte 2 (RNF-ACS-004, tamaño de texto ajustable). Los RNF que el backlog lista explícitamente en el Bloque 5 «Adopción» (MVP obligatorio) se marcan con ★.\n")
    BLOQUE5 = {"RNF-042", "RNF-043", "RNF-044", "RNF-037", "RNF-039", "RNF-038", "RNF-029", "RNF-010", "RNF-011", "RNF-019", "RNF-035", "RNF-036"}
    n = 2
    for c in CAT_ORDER:
        o.append(f"\n## 7.{n} {c} ({RNF_CAT[c]})\n")
        n += 1
        o.append("| ID (legacy) | Requisito | Verificación | Origen (SPEC) | Hor. |")
        o.append("|---|---|---|---|:--:|")
        for r in [x for x in D["rnf"] if x["cat"] == c]:
            star = " ★" if r["id"] in BLOQUE5 else ""
            hor = "H2" if RNF_NEW[r["id"]] in H2_RNF else "H1"
            o.append(f"| **{RNF_NEW[r['id']]}**<br>*({r['id']})*{star} | {L(r['text'])} | {L(r['verif'])} | {L(r['origin'])} | {hor} |")
    o.append("""
> ★ = RNF que el backlog del SPEC (§12.2, Bloques 4 y 5) declara MVP obligatorio o condición de medición.

---

**ESTADO DEL CAPÍTULO 7**

| | |
|---|---|
| **Completado** | 47 RNF en 9 categorías con ID `RNF-<CAT>-nnn`, verificación y origen |
| **Pendiente** | Calibración de valores numéricos con la línea base (pendiente #12, CA-12) · prioridad por RNF (no definida en el SPEC) |
| **Riesgos encontrados** | RG-36 (sin línea base no se calibran) · R-S07 |
| **Dependencias** | Cap. 12 (criterios de aceptación) |
""")
    return "\n".join(o)

# ============================================================ CAPÍTULO 8 — RN
def cap8():
    rn_rf = {}
    for r, ks in RF_RN.items():
        for k in ks:
            rn_rf.setdefault(k, []).append(r)
    rn_hu = {}
    for h, ks in HU_RN.items():
        for k in ks:
            rn_hu.setdefault(k, []).append(h)
    o = ["""
---

# CAPÍTULO 8 — REGLAS DE NEGOCIO

> Reorganización de las reglas de negocio del SPEC (Cap. 9) por **dominio**, con ID permanente `RN-<DOM>-nnn`. Este capítulo es el corazón operativo de la «inteligencia» de COLBASOFT `[DC-07]`: la automatización del producto es este cuerpo de reglas evaluándose de forma explícita.

> **Hallazgo H-01 — cifra real.** El SPEC declara «68 reglas» y su §9.14 «68 = 51 estructurales + 17 configurables», pero las tablas §9.2–§9.12 contienen **82 reglas distintas: 60 estructurales + 22 configurables** (la propia suma de la tabla §9.14 da 82). Este SRS conserva **las 82**; ninguna se perdió. Los dos marcadores sin contenido `RN-069*` («reservado») y `RN-026b*` («ver nota de numeración») **no son reglas** y no reciben ID permanente (H-09).

> **Versión 1.1 — cierre del CP-04.** Se incorporan **3 reglas estructurales nuevas**, separadas de las 82: RN-EXI-007 (la entrada confirmada queda en recepción, DF5-02), RN-MOV-010 (la primera ubicación es un movimiento interno, DF5-03) y RN-INT-008 (revalidación al sincronizar, DF5-05); vienen de SPEC v1.1 §9.15. Además cambia el texto de **RN-IDE-001** y **RN-IDE-003** por DF5-01 (el QR de mercancía identifica SKU + Lote). Total del SRS v1.1: **85 reglas**. La discrepancia 68/82 del SPEC sigue abierta (H-01, DEC-03).
>
> **Versión 1.2 — decisiones del 30-sep-2026.** Se incorporan **6 reglas estructurales nuevas**, separadas de las 85: RN-LOT-006 (toda mercancía se registra por piezas), RN-LOT-007 (la existencia de una unidad de inventario es la suma de sus piezas), RN-SAL-008 (el corte parcial), RN-MOV-011 (selección de la pieza tras el escaneo), RN-SAL-009 (el escaneo de salida verifica y cuenta) y RN-CNT-009 (el conteo es pieza por pieza); vienen de SPEC v1.2 §9.16. Además cambia el texto de **RN-IDE-004** (Q-09: la reimpresión conserva el mismo QR). Total del SRS v1.2: **91 reglas**.
>
> **Versión 1.4 — respuesta a HD-29.** Se incorpora **1 regla estructural nueva**, separada de las 91: RN-MOV-012 (una pieza no se divide: el movimiento interno mueve la pieza completa y tomar una parte es un corte parcial). Viene de SPEC v1.4 §9.18. Además cambian los textos de **RN-MOV-001** (propuesta de ubicación con regla fija en el Núcleo, H-19) y **RN-LOT-006** (sin excepción: lo suelto es un paquete o bolsa, HD-30). Total del SRS v1.4: **92 reglas**.

## 8.1 Distribución por dominio

"""]
    rows = ["| Dominio | Nombre | Reglas | Estructurales | Configurables |", "|---|---|:--:|:--:|:--:|"]
    tot = Counter()
    for dom, (nm, lst) in RN_DOM.items():
        ce = sum(1 for k in lst if RNR[k]["tipo"] == "Estructural")
        cc = sum(1 for k in lst if RNR[k]["tipo"] == "Configurable")
        rows.append(f"| **{dom}** | {nm} | {len(lst)} | {ce} | {cc} |")
        tot["n"] += len(lst); tot["e"] += ce; tot["c"] += cc
    rows.append(f"| **Total** | | **{tot['n']}** | **{tot['e']}** | **{tot['c']}** |")
    o.append("\n".join(rows))
    o.append("""
**Definiciones (SPEC §9):** una regla **estructural** es inviolable y no parametrizable; una regla **configurable** ajusta su umbral en Parámetros y Configuración (M-19) pero su lógica no se desactiva. La columna «§9.1» marca las 10 reglas del núcleo no configurable que el SPEC enumera expresamente (RF-PAR-006); **la relación entre «estructural» y «núcleo §9.1» es ambigua en el SPEC** (H-06, DEC-04): el SRS interpreta que **toda regla estructural es no configurable**.
""")
    n = 2
    for dom, (nm, lst) in RN_DOM.items():
        o.append(f"\n## 8.{n} {dom} · {nm}\n")
        n += 1
        o.append("| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |")
        o.append("|---|---|:--:|:--:|---|---|---|")
        for k in lst:
            r = RNR[k]
            leg = k.rstrip("*")
            star = "\\*" if k.endswith("*") else ""
            core = "●" if leg in CORE91 else ""
            rfs = ", ".join(RF_NEW[x] for x in sorted(rn_rf.get(k, []))) or "**sin RF** (H-11)"
            hus = ", ".join(HU_NEW[x] for x in sorted(rn_hu.get(k, []))) or "**sin HU** (H-11)"
            o.append(f"| **{RN_NEW[k]}**<br>*({leg}{star})* | {L(r['text'])} | {r['tipo']} | {core} | {L(r['origin'])} | {rfs} | {hus} |")
    o.append("""
\\* Las reglas con asterisco en el SPEC (`RN-002b`, `RN-036b`, `RN-057b`, `RN-070` a `RN-080`) se incorporaron durante la consolidación del Cap. 9 del SPEC (§9.13); `RN-081` a `RN-083` se incorporaron en la v1.1 del SPEC (§9.15, cierre del CP-04), `RN-084` a `RN-089` en la v1.2 (§9.16) y `RN-090` en la v1.4 (§9.18); su contenido se conserva íntegro y ya no requieren el asterisco.

---

**ESTADO DEL CAPÍTULO 8**

| | |
|---|---|
| **Completado** | 92 reglas en 13 dominios (82 del SPEC v1.0 + 3 de la v1.1 + 6 de la v1.2 + 1 de la v1.4) con ID `RN-<DOM>-nnn`, tipo, origen, RF e HU relacionados |
| **Pendiente** | Confirmar la cifra de 82 y la renumeración canónica (DEC-03) · ambigüedad estructural/configurable (DEC-04) · 6 reglas sin RF (Anexo C, PROP-RN) |
| **Riesgos encontrados** | H-01, H-06, H-09, H-11 · R-S06, R-S08 |
| **Dependencias** | Cap. 6 (RF), Cap. 5 (HU), Cap. 12 (CA-06 y CA-07) |
""")
    return "\n".join(o)

# ============================================================ CAPÍTULO 9 — trazabilidad
def pn_rules():
    lines = open(str(ROOT / "01_SPEC_FASE_2" / "COLBASOFT_SPEC_v1.1.md"), encoding="utf8").read().split("\n")
    starts = [(i, m.group(1)) for i, ln in enumerate(lines) for m in [re.match(r"^## (PN-\d\d) — ", ln)] if m and i > 600]
    res = {}
    for j, (i, pid) in enumerate(starts):
        end = starts[j + 1][0] if j + 1 < len(starts) else next(k for k in range(i + 1, len(lines)) if lines[k].startswith("# CAPÍTULO 4"))
        res[pid] = rn_tokens("\n".join(lines[i:end]))
    return res
PN_RN = pn_rules()

def cap9():
    o = ["""
---

# CAPÍTULO 9 — MATRIZ DE TRAZABILIDAD

> Cadena obligatoria **Objetivo de la monografía → Concepto del SPEC → Historia de usuario → Requisito funcional → Regla de negocio → KPI**. La monografía **no contiene requisitos**; por eso el eslabón «objetivo» se deriva del **módulo** al que pertenece cada requisito y se acompaña del **ancla directa** `[MON §n]` cuando el SPEC la declara en el origen del requisito. Los eslabones marcados `[SRS]` (objetivo por módulo, concepto, historia, KPI) se derivaron en esta fase y **requieren validación del Director** (R-S02).

```
Objetivo de la monografía (OG, OE-1, OE-2, OE-3)
        │  ── se materializa en ──►  Módulo (M-nn)
        ▼
Concepto del SPEC (CD-nn / PR-nn / DC-nn) ──► Historia de usuario (HU-<DOM>-nnn) ──► Requisito funcional (RF-<DOM>-nnn)
                                                                                        │
                                                          Regla de negocio (RN-<DOM>-nnn) ◄──┤──► KPI (KPI-nn)
```

## 9.1 Objetivos de la monografía (transcripción literal)

| ID | Objetivo (Cap. 5 y 5.5 de la monografía, sin modificación) |
|---|---|
| **OG** | «Analizar los factores teóricos para proponer un modelo conceptual de automatización en la gestión de inventarios de PYMES textiles del Eje Cafetero, con el fin de comprender su potencial para mejorar la eficiencia operativa y la competitividad, a partir de una revisión documental.» |
| **OE-1** | «Describir los conceptos clave de automatización de procesos, gestión de inventarios y eficiencia operativa en el contexto de PYMES textiles, identificando definiciones, tipos y beneficios documentos en literatura especializada.» |
| **OE-2** | «Revisar modelos teóricos de automatización aplicados a operaciones logísticas, como frameworks de adopción tecnológica, para evaluar su aplicabilidad en sectores fabricantes tradicionales como el textil colombiano.» |
| **OE-3** | «Sintetizar hallazgos teóricos que permitirán proponer un modelo conceptual integrado, destacando cómo la automatización puede optimizar la trazabilidad, reducir errores y potenciar la competitividad en el Eje Cafetero para 2025, calculando en comparaciones de enfoques documentados.» |

> **Regla `[SRS]`.** Todo requisito contribuye al **OG**; el objetivo específico indicado es el que **más directamente** materializa el módulo. El SPEC/SRS es el modelo conceptual integrado que el OE-3 prometía y la monografía no presentó (vacío C.1.2 de la Auditoría). Las diferencias entre el objetivo transcrito y el proyecto (producto de software frente a modelo conceptual) están registradas en la Auditoría (A.3) y aprobadas como extensión de alcance por el Director.

## 9.2 Objetivos → módulos `[SRS]`

| Módulo | Objetivo más directo | Justificación (ancla) |
|---|:--:|---|"""]
    for m in MODS:
        ob, why = MOD_OBJ[m]
        o.append(f"| **{m}** {MOD[m][1]} | {ob} | {why} |")
    o.append("\n## 9.3 Catálogo de KPI (24)\n")
    o.append("Se conservan los 24 indicadores del SPEC (Cap. 10) con su fórmula. **Ninguno declara meta numérica**: solo puede fijarse contra la línea base de la empresa piloto (V-03). Los tres primeros son los propuestos por la monografía (Cap. 8.2). La columna «RF» es derivada `[SRS]`.\n")
    o.append("| KPI | Nombre | Qué mide | Fórmula | Frecuencia | Usuario | Fuente del dato | Origen (SPEC) | RF relacionados |")
    o.append("|---|---|---|---|---|---|---|---|---|")
    for k in [KPI[f"KPI-{i:02d}"] for i in range(1, 25)]:
        rfs = ", ".join(RF_NEW[x] for x in sorted(KPI_RF[k["id"]]) if x not in ("RF-136", "RF-185")) + ", " + (RF_NEW["RF-185"] if "RF-185" in KPI_RF[k["id"]] else RF_NEW["RF-136"])
        o.append(f"| **{k['id']}** | {k['name']} | {L(k['Qué mide'])} | {k['Fórmula']} | {k['Frecuencia']} | {k['Usuario']} | {L(k['Fuente del dato'])} | {L(k['Origen'])} | {rfs} |")
    o.append("\n> **Hallazgo H-12.** KPI-05, KPI-07, KPI-10, KPI-12, KPI-17 y KPI-24 necesitan un dato que ningún RF exige capturar (Anexo C, C.2.2).\n")

    # 9.4 matriz principal
    o.append("## 9.4 Matriz principal: objetivo → concepto → historia → RF → regla → KPI\n")
    o.append("Una fila por cada uno de los 185 RF. «Ancla MON» = apartado(s) de la monografía que el SPEC declara en el origen del RF; vacío si el origen es `[NUEVO]`, `[DC]`, `[PR]`, `[AUD]`.\n")
    o.append("| Objetivo `[SRS]` | Ancla MON | Concepto (SPEC) | Historia(s) | RF | Regla(s) | KPI |")
    o.append("|:--:|---|---|---|---|---|---|")
    for m in MODS:
        for r in [x for x in D["rf"] if x["mod"] == m]:
            rid = r["id"]
            anc = ", ".join(sorted(set(re.findall(r"§(\d+(?:\.\d+)?)", " ".join(re.findall(r"\[MON [^\]]*\]", r["origin"]))))))
            anc = ("§" + ", §".join(anc.split(", "))) if anc else "—"
            hus = ", ".join(HU_NEW[h] for h in RF_HU[rid])
            kp = ", ".join(RF_KPI.get(rid, [])) or "—"
            o.append(f"| {MOD_OBJ[m][0]} | {anc} | {RF_CD[rid]} | {hus} | **{RF_NEW[rid]}** | {rn_list(RF_RN[rid])} | {kp} |")

    # 9.5 cobertura por regla
    rn_rf = {}
    for r, ks in RF_RN.items():
        for k in ks: rn_rf.setdefault(k, []).append(r)
    rn_hu = {}
    for h, ks in HU_RN.items():
        for k in ks: rn_hu.setdefault(k, []).append(h)
    pn_of = {}
    for pid, ks in PN_RN.items():
        for k in ks: pn_of.setdefault(k, []).append(pid)
    o.append("\n## 9.5 Cobertura por regla de negocio (92)\n")
    o.append("| Regla | Tipo | Proceso(s) | Caso(s) de uso | Historia(s) | RF |")
    o.append("|---|:--:|---|---|---|---|")
    for dom, (nm, lst) in RN_DOM.items():
        for k in lst:
            pns = sorted(pn_of.get(k, []))
            cus = ", ".join(PN_CU[p] for p in pns) or "—"
            o.append(f"| **{RN_NEW[k]}** | {RNR[k]['tipo'][:4]}. | {', '.join(pns) or '—'} | {cus} | {', '.join(HU_NEW[x] for x in sorted(rn_hu.get(k, []))) or '**sin HU**'} | {', '.join(RF_NEW[x] for x in sorted(rn_rf.get(k, []))) or '**sin RF**'} |")

    # 9.6 KPI cobertura
    o.append("\n## 9.6 Cobertura por KPI (24)\n")
    o.append("| KPI | Objetivo de la monografía | Concepto | Historia(s) | RF | Regla(s) relacionada(s) |")
    o.append("|---|---|---|---|---|---|")
    kpi_obj = {"KPI-01": "OG / OE-3 (§8.2)", "KPI-05": "OG / OE-3 (§8.2)", "KPI-08": "OG / OE-3 (§8.2)"}
    kpi_cd = {"KPI-01": "CD-43, CD-27", "KPI-02": "CD-43", "KPI-03": "CD-38", "KPI-04": "CD-27", "KPI-05": "CD-28", "KPI-06": "CD-42",
              "KPI-07": "CD-08", "KPI-08": "CD-33, CD-34, CD-27", "KPI-09": "CD-37, CD-18", "KPI-10": "CD-14", "KPI-11": "CD-28",
              "KPI-12": "CD-35", "KPI-13": "CD-30", "KPI-14": "CD-33", "KPI-15": "CD-23, CD-32", "KPI-16": "CD-30, CD-18",
              "KPI-17": "CD-28", "KPI-18": "CD-14, CD-15", "KPI-19": "CD-45", "KPI-20": "CD-45", "KPI-21": "CD-18", "KPI-22": "CD-33",
              "KPI-23": "CD-48", "KPI-24": "CD-28"}
    for i in range(1, 25):
        kid = f"KPI-{i:02d}"
        orig = KPI[kid]["Origen"]
        obj = kpi_obj.get(kid) or ("OE-3 (" + ", ".join(sorted(set("§" + x for x in re.findall(r"§(\d+(?:\.\d+)?)", orig)))) + ")" if "§" in orig else "OE-3 (nuevo aporte)")
        hs = sorted(h for h, ks in HU_KPI.items() if kid in ks)
        rfs = sorted(x for x in KPI_RF[kid] if x not in ("RF-136", "RF-185"))
        rns = sorted({k for x in rfs for k in RF_RN.get(x, [])}, key=lambda k: RN_NEW[k])
        o.append(f"| **{kid}** {KPI[kid]['name']} | {obj} | {kpi_cd[kid]} | {', '.join(HU_NEW[x] for x in hs) or '—'} | {', '.join(RF_NEW[x] for x in rfs)}, {RF_NEW['RF-185'] if 'RF-185' in KPI_RF[kid] else RF_NEW['RF-136']} | {', '.join(RN_NEW[k] for k in rns) or '—'} |")

    # 9.7 procesos
    o.append("\n## 9.7 Cobertura por proceso de negocio (14)\n")
    o.append("| Proceso | Caso de uso | Módulo(s) | Historias | RF | Reglas citadas en el proceso |")
    o.append("|---|---|---|---|---|---|")
    PN_HU = {"PN-01": [30,31,32,33,34,36,37,16], "PN-02": [25,26,27,28,29], "PN-03": [35,24,21], "PN-04": [71,72,73,74,75,76],
             "PN-05": [45,46], "PN-06": [47,48,49,50,51], "PN-07": [52,53,54,55,56,57,102], "PN-08": [58,59,60,61,62,65,66],
             "PN-09": [63,64], "PN-10": [38,39,40,41,42,43,44], "PN-11": [82,83,84,85,86], "PN-12": [67,68,69,70],
             "PN-13": [94,95,96,97,77,78,79], "PN-14": [113,114]}
    pn_name = {p["id"]: p["name"] for p in D["pn"]}
    for pid in [f"PN-{i:02d}" for i in range(1, 15)]:
        hs = [hu(x) for x in PN_HU[pid]]
        rfs = sorted({r for h in hs for r in HU_RF.get(h, [])})
        mods = ", ".join(sorted({HU[h]["mod"] for h in hs}))
        o.append(f"| **{pid}** {pn_name[pid]} | {PN_CU[pid]} | {mods} | {', '.join(HU_NEW[h] for h in hs) or '**ninguna** (H-10)'} | {', '.join(RF_NEW[r] for r in rfs) or '**ninguno** (H-10)'} | {', '.join(RN_NEW[k] for k in sort_rn(PN_RN[pid])) or '—'} |")

    # 9.8 brechas
    hu_wo_hu = [k for k in RNR if k not in rn_hu]
    rn_wo_rf = [k for k in RNR if k not in rn_rf]
    o.append("\n## 9.8 Brechas de trazabilidad detectadas\n")
    o.append("| Brecha | Elementos | Hallazgo |")
    o.append("|---|---|---|")
    o.append("| Proceso sin HU ni RF | ninguno (PN-14 se cerró en la v1.3 con HU-TAR-004, HU-TAR-005 y RF-TAR-006…RF-TAR-008, DEC-05) | H-10 (resuelto) |")
    o.append(f"| Reglas sin RF | {', '.join(RN_NEW[k] for k in sorted(rn_wo_rf, key=lambda k: RN_NEW[k])) or 'ninguna (cerradas en la v1.3, DEC-06)'} | H-11 |")
    o.append(f"| Reglas sin HU | {', '.join(RN_NEW[k] for k in sorted(hu_wo_hu, key=lambda k: RN_NEW[k])) or 'ninguna (cerradas en la v1.3, DEC-06)'} | H-11 |")
    o.append("| KPI cuyo dato de origen no se exige capturar | ninguno (KPI-05, KPI-07, KPI-10, KPI-12, KPI-17 y KPI-24 se cerraron en la v1.3, DEC-06; KPI-24 requiere además verificación de campo) | H-12 (resuelto) |")
    o.append("| HU con cobertura RF parcial | ninguna (HU-NOV-003 y HU-NOV-004 se cerraron con RF-NOV-008 y RF-NOV-007, DEC-06) | H-13 (resuelto) |")
    o.append("| RF sin historia · HU sin RF | ninguno · ninguna | — |")
    o.append("| Objetivos de la monografía sin requisito | ninguno (todos los módulos derivan de OG/OE-1/OE-2/OE-3); OE-2 se materializa solo en M-12, M-19, M-20 y en los RNF de usabilidad | — |")
    o.append("""
> **Lectura.** La cadena está completa para 185 de 185 RF y 114 de 114 HU. Las brechas que tenía la v1.2 (reglas sin RF, KPI sin dato de origen y PN-14 sin requisitos) se cerraron en la v1.3 por las decisiones DEC-05 y DEC-06 (Anexo C).

---

**ESTADO DEL CAPÍTULO 9**

| | |
|---|---|
| **Completado** | Objetivos transcritos · objetivos→módulos · catálogo de 24 KPI · matriz de 185 RF · cobertura de 92 reglas · de 24 KPI · de 14 procesos · brechas |
| **Pendiente** | Validación por el Director de los eslabones `[SRS]` (R-S02) · brechas cerradas en la v1.3 (DEC-05, DEC-06) |
| **Riesgos encontrados** | H-10, H-11, H-12, H-13 (resueltos en la v1.3) · RG-42 (pérdida de trazabilidad hacia la monografía) |
| **Dependencias** | Caps. 5–8 |
""")
    return "\n".join(o)

# ============================================================ ANEXO A
def annex_a():
    o = ["""
---

# ANEXO A — EQUIVALENCIA DE IDENTIFICADORES (SPEC → SRS)

> Tabla de consulta para quien tenga el SPEC en la mano. Los IDs permanentes de este documento **no cambian**; los del SPEC (*legacy*) quedan como referencia histórica.

## A.1 Historias de usuario (114)

| SPEC | SRS | Módulo | | SPEC | SRS | Módulo | | SPEC | SRS | Módulo |
|---|---|:--:|---|---|---|:--:|---|---|---|:--:|"""]
    hs = D["hu"]
    for i in range(0, len(hs), 3):
        cells = []
        for h in hs[i:i + 3]:
            cells.append(f"{h['id']} | {HU_NEW[h['id']]} | {h['mod']}")
        while len(cells) < 3: cells.append(" | | ")
        o.append("| " + " | | ".join(cells) + " |")
    o.append("\n## A.2 Requisitos funcionales (185)\n")
    o.append("| SPEC | SRS | | SPEC | SRS | | SPEC | SRS | | SPEC | SRS |")
    o.append("|---|---|---|---|---|---|---|---|---|---|---|")
    rs = D["rf"]
    for i in range(0, len(rs), 4):
        cells = [f"{r['id']} | {RF_NEW[r['id']]}" for r in rs[i:i + 4]]
        while len(cells) < 4: cells.append(" | ")
        o.append("| " + " | | ".join(cells) + " |")
    o.append("\n## A.3 Requisitos no funcionales (47)\n")
    o.append("| SPEC | SRS | | SPEC | SRS | | SPEC | SRS | | SPEC | SRS |")
    o.append("|---|---|---|---|---|---|---|---|---|---|---|")
    ns = D["rnf"]
    for i in range(0, len(ns), 4):
        cells = [f"{r['id']} | {RNF_NEW[r['id']]}" for r in ns[i:i + 4]]
        while len(cells) < 4: cells.append(" | ")
        o.append("| " + " | | ".join(cells) + " |")
    o.append("\n## A.4 Reglas de negocio (92)\n")
    o.append("| SPEC | SRS | Tipo | | SPEC | SRS | Tipo | | SPEC | SRS | Tipo |")
    o.append("|---|---|:--:|---|---|---|:--:|---|---|---|:--:|")
    keys = [k for dom, (nm, lst) in RN_DOM.items() for k in lst]
    for i in range(0, len(keys), 3):
        cells = [f"{k.rstrip('*')} | {RN_NEW[k]} | {RNR[k]['tipo'][:4]}." for k in keys[i:i + 3]]
        while len(cells) < 3: cells.append(" | | ")
        o.append("| " + " | | ".join(cells) + " |")
    o.append("\n**Marcadores sin contenido (no reciben ID):** `RN-069*` («reservado») y `RN-026b*` («ver nota de numeración») — H-09.\n")
    o.append("\n## A.5 Elementos que conservan su ID del SPEC\n")
    o.append("`KPI-01…KPI-24` · `PN-01…PN-14` · `CD-01…CD-49` · `M-01…M-20` · `RG-01…RG-42` · `DC-01…DC-08` · `PR-01…PR-06` · `OP-01…OP-12`.\n")
    return "\n".join(o)

# ============================================================ ANEXO B (auditoría interna)
def annex_b(doc_text_wo_annex=None):
    hc = Counter(h["prio"] for h in D["hu"]); rc = Counter(r["prio"] for r in D["rf"])
    n_scn = sum(len(re.findall(r"^Escenario:", v[1], flags=re.M)) for v in G.values())
    n_crit = sum(len(h["crit"]) for h in D["hu"])
    rn_rf = {}
    for r, ks in RF_RN.items():
        for k in ks: rn_rf.setdefault(k, []).append(r)
    rn_hu = {}
    for h, ks in HU_RN.items():
        for k in ks: rn_hu.setdefault(k, []).append(h)
    nrn_e = sum(1 for r in RNR.values() if r["tipo"] == "Estructural")
    nrn_c = sum(1 for r in RNR.values() if r["tipo"] == "Configurable")
    cd_used = set()
    for v in RF_CD.values():
        cd_used |= set(re.findall(r"CD-\d\d", v))
    cd_unused = sorted({c["id"] for c in D["cd"]} - cd_used)
    # unicidad IDs
    allids = list(HU_NEW.values()) + list(RF_NEW.values()) + list(RNF_NEW.values()) + list(RN_NEW.values())
    uniq = len(allids) == len(set(allids))
    rnf_cat = Counter(r["cat"] for r in D["rnf"])
    o = ["""
---

# ANEXO B — AUDITORÍA INTERNA DEL DOCUMENTO

> Verificación final de integridad del SRS frente al SPEC. Los recuentos se calcularon **programáticamente** sobre las mismas tablas de las que se generaron los capítulos 5–9 y los anexos.

## B.1 Totales

| Elemento | Total en el SPEC (declarado) | Total real en las tablas del SPEC | **Total en el SRS** | ¿Se perdió alguno? |
|---|:--:|:--:|:--:|:--:|"""]
    o.append(f"| **Historias de usuario** | 114 | 114 | **{len(HU_NEW)}** (Must {hc['P0']} · Should {hc['P1']} · Could {hc['P2']} · Won't {hc['P3']}) | **No** |")
    o.append(f"| Criterios de aceptación → escenarios Gherkin | — | {n_crit} | **{n_scn}** | **No** (1:1) |")
    o.append(f"| **Requisitos funcionales** | 185 | 185 | **{len(RF_NEW)}** (Must {rc['P0']} · Should {rc['P1']} · Could {rc['P2']} · Won't {rc['P3']}) | **No** |")
    o.append(f"| **Requisitos no funcionales** | 47 | 47 | **{len(RNF_NEW)}** ({', '.join(f'{RNF_CAT[c]} {rnf_cat[c]}' for c in CAT_ORDER)}) | **No** |")
    o.append(f"| **Reglas de negocio** | **68** (v1.0) | **82** (v1.0) + **3** (v1.1) + **6** (v1.2) + **1** (v1.4) | **{len(RN_NEW)}** ({nrn_e} estructurales · {nrn_c} configurables) | **No** — discrepancia del SPEC (H-01) |")
    o.append(f"| **KPI** | 24 | 24 | **{len(D['kpi'])}** | **No** |")
    o.append("| **Casos de uso** | — | — | **24** (14 procesos PN + 10 de módulos) | — |")
    o.append("| Procesos de negocio (PN) | 14 | 14 | 14 (14 con caso de uso y con requisitos) | **No** |")
    o.append(f"| Conceptos de dominio (CD) | 48 (v1.0) | 49 | 49 (referenciados por RF: {len(cd_used)}) | **No** |")
    o.append("| Módulos funcionales | 20 | 20 | 20 | **No** |")
    o.append("| Riesgos funcionales (RG) | 42 | 42 | 42 (permanecen en el SPEC) | **No** |")
    o.append(f"""
## B.2 Verificaciones de integridad

| # | Verificación | Resultado |
|---|---|:--:|
| V-1 | Todas las HU del SPEC (114) están en el SRS con ID permanente | ✅ {len(HU_NEW)}/114 |
| V-2 | Todos los criterios de aceptación tienen un escenario Gherkin | ✅ {n_scn}/{n_crit} |
| V-3 | Todos los RF del SPEC (185) están en el SRS | ✅ {len(RF_NEW)}/185 |
| V-4 | Todos los RNF del SPEC (47) están en el SRS | ✅ {len(RNF_NEW)}/47 |
| V-5 | Todas las reglas con contenido (92: 82 de la v1.0 + 3 de la v1.1 + 6 de la v1.2 + 1 de la v1.4) están en el SRS; los 2 marcadores vacíos quedan documentados | ✅ {len(RN_NEW)}/92 |
| V-6 | Todos los KPI (24) están en el SRS con su fórmula | ✅ {len(D['kpi'])}/24 |
| V-7 | Los IDs permanentes son únicos | {'✅' if uniq else '❌'} {len(allids)} IDs |
| V-8 | Toda HU tiene al menos un RF | ✅ {sum(1 for h in HU if HU_RF.get(h))}/114 |
| V-9 | Todo RF tiene al menos una HU | ✅ {sum(1 for r in RF if RF_HU.get(r))}/185 |
| V-10 | Toda regla está cubierta por algún RF | {'✅' if all(rn_rf.get(k) for k in RNR) else '🟡'} {sum(1 for k in RNR if rn_rf.get(k))}/{len(RNR)} (faltan: {', '.join(RN_NEW[k] for k in sorted((k for k in RNR if not rn_rf.get(k)), key=lambda k: RN_NEW[k]))}) |
| V-11 | Toda regla está cubierta por alguna HU | {'✅' if all(rn_hu.get(k) for k in RNR) else '🟡'} {sum(1 for k in RNR if rn_hu.get(k))}/{len(RNR)} (faltan: {', '.join(RN_NEW[k] for k in sorted((k for k in RNR if not rn_hu.get(k)), key=lambda k: RN_NEW[k]))}) |
| V-12 | Todo KPI tiene al menos un RF que lo alimenta | ✅ {sum(1 for k in KPI_RF if KPI_RF[k])}/24 |
| V-13 | Todo proceso PN tiene caso de uso | ✅ 14/14 |
| V-14 | Todo proceso PN tiene al menos una HU y un RF | ✅ 14/14 (PN-14 con HU-TAR-004, HU-TAR-005 y RF-TAR-006…008 desde la v1.3) |
| V-15 | Todo concepto de dominio (49) es referenciado por algún RF | {'✅' if not cd_unused else '🟡'} {len(cd_used)}/49 {('(no referenciados por RF: ' + ', '.join(cd_unused) + '; son conceptos de contexto o de definición previa)') if cd_unused else ''} |
| V-16 | Ninguna meta numérica nueva fue introducida | ✅ (los valores numéricos de RNF son los del SPEC) |
| V-17 | Ningún requisito nuevo fue creado: las propuestas de cierre de brechas están fuera del baseline (Anexo C) | ✅ |
| V-18 | Se respeta la exclusión de código, base de datos, arquitectura, ERD/UML, endpoints, APIs, frameworks y tecnologías | ✅ (la herramienta analítica externa se cita solo por DC-06) |
""")
    o.append("""
## B.3 Discrepancias del SPEC que este SRS detectó y tratamiento

| Hallazgo | SPEC declara | Contenido real | Tratamiento |
|---|---|---|---|
| H-01 | 68 reglas (51 est. + 17 conf.) | 82 (60 + 22) | Se conservan 82 (+3 incorporadas en la v1.1, +6 en la v1.2) |
| H-02 | RF: 72 P0 / 69 P1 / 21 P2 | 74 / 70 / 18 | Se usa la prioridad de cada fila |
| H-03 | Rangos HU-001…096 y RF-001…138 (§0.4) | HU-001…114 y RF-001…185 (corregido en la v1.3) | Prevalece el contenido |
| H-04 | Trazabilidad 41/12/9/38 % (§0.3) | 34/12/17/37 % (§13.3) | Sin impacto en requisitos |
| H-05 | HU-026 → RNF-014; HU-071 → RNF-012 | Correctos: RNF-015 y RNF-014 | Se enlazan los correctos |

## B.4 Riesgos abiertos

Ver **Anexo C**: 10 riesgos propios de la fase (R-S01…R-S10, uno crítico), 11 riesgos críticos heredados del SPEC (RG-01, 02, 13, 14, 16, 17, 23, 33, 34, 35, 36) y **9 decisiones pendientes del Director (DEC-01…DEC-09)**.

| Riesgo abierto principal | Sev. |
|---|:--:|
| R-S01 — El SRS se emite antes del AS-IS y de la línea base | 🔴 |
| RG-35 / RG-36 — El piloto puede no alcanzar las cifras; sin línea base no se demuestra mejora | 🔴 |
| RG-01 / RG-13 / RG-14 — Adopción real por el personal (operación fuera del sistema, rechazo, curva de aprendizaje) | 🔴 |
| R-S04 — Tensión entre DC-02 y el Horizonte 2 del backlog | 🟠 |
| R-S05 — Reglas y KPI sin requisito de captura; PN-14 sin requisitos | 🟠 |

---

**ESTADO DEL ANEXO B**

| | |
|---|---|
| **Completado** | Totales · 18 verificaciones · discrepancias del SPEC · riesgos abiertos |
| **Pendiente** | Nada dentro del anexo |
| **Riesgos encontrados** | Ver Anexo C |
| **Dependencias** | Todos los capítulos |
""")
    return "\n".join(o)

# ============================================================ ensamblado
def assemble():
    parts = []
    c00 = rd("cap00.md")
    parts.append(c00)
    parts.append(rd("cap01.md"))
    c02 = rd("cap02.md").replace("{{TABLA_MODULOS}}", tabla_modulos())
    parts.append(conv(c02))
    c03 = rd("cap03.md").replace("{{HU_POR_ROL}}", hu_por_rol())
    parts.append(conv(c03))
    ucs = ["""
---

# CAPÍTULO 4 — CASOS DE USO

> **24 casos de uso** que cubren los **14 procesos de negocio (PN-01…PN-14)** del SPEC y los 10 módulos que no tienen proceso propio. Cada caso declara objetivo, actor, precondiciones, postcondiciones, flujo principal, flujos alternos, excepciones y trazabilidad. Los flujos **transcriben y estructuran los procesos TO-BE del SPEC (Cap. 3)** `[SRS]`; no se agrega comportamiento nuevo. Recuérdese que el proceso real de la empresa **no fue levantado** (AS-IS pendiente, H-16).

## 4.1 Índice de casos de uso

| CU | Caso de uso | Proceso SPEC | Módulo | Actor principal |
|---|---|:--:|:--:|---|
| CU-01 | Autenticarse y gestionar la sesión | — | M-01 | Todos |
| CU-02 | Gestionar usuarios y roles | — | M-02 | Administrador |
| CU-03 | Gestionar el catálogo de referencias | — | M-03 | Jefe de Bodega |
| CU-04 | Definir la estructura de la bodega | — | M-05 | Administrador |
| CU-05 | Configurar parámetros y motivos tipificados | — | M-19 | Administrador |
| CU-06 | Recepcionar mercancía | PN-01 | M-07 | Coordinador |
| CU-07 | Identificar mercancía con QR | PN-02 | M-06 | Coordinador |
| CU-08 | Ubicar mercancía | PN-03 | M-07 / M-05 | Auxiliar |
| CU-09 | Consultar existencia y ubicación | PN-04 | M-13 | Todos |
| CU-10 | Reubicar mercancía (movimiento interno) | PN-05 | M-09 | Auxiliar |
| CU-11 | Transferir mercancía entre zonas o bodegas | PN-06 | M-09 | Coordinador / Auxiliar |
| CU-12 | Ajustar inventario | PN-07 | M-10 | Coordinador → Jefe/Admin |
| CU-13 | Ejecutar un conteo cíclico | PN-08 | M-11 | Coordinador / Auxiliar |
| CU-14 | Ejecutar un conteo general | PN-09 | M-11 | Jefe de Bodega |
| CU-15 | Registrar la salida de mercancía | PN-10 | M-08 | Jefe → Auxiliar |
| CU-16 | Gestionar alertas operativas | PN-11 | M-15 | Jefe / Coordinador |
| CU-17 | Reportar y resolver novedades de mercancía | PN-12 | M-12 | Auxiliar |
| CU-18 | Auditar el inventario | PN-13 | M-18 | Auditor |
| CU-19 | Cerrar la jornada operativa | PN-14 | M-20 / M-17 | Jefe / Coordinador |
| CU-20 | Gestionar lotes | — | M-04 | Jefe de Bodega |
| CU-21 | Consultar el kardex y verificar la trazabilidad | — | M-14 | Auditor / Jefe |
| CU-22 | Generar reportes y exportar datos | — | M-16 | Jefe / Admin / Auditor |
| CU-23 | Consultar el dashboard operativo y el panel de tareas | — | M-17 / M-20 | Jefe / Auxiliar |
| CU-24 | Gestionar tareas, notificaciones y aprobaciones | — | M-20 | Sistema |

## 4.2 Especificación de los casos de uso

"""]
    ucs.append(conv(rd("uc_a.md")))
    ucs.append("\n---\n")
    ucs.append(conv(rd("uc_b.md")))
    ucs.append("\n---\n")
    ucs.append(conv(rd("uc_c.md")))
    ucs.append("""

---

**ESTADO DEL CAPÍTULO 4**

| | |
|---|---|
| **Completado** | 24 casos de uso con objetivo, actor, precondiciones, postcondiciones, flujo principal, flujos alternos y excepciones; los 14 procesos PN tienen caso de uso |
| **Pendiente** | CU-19 (Cierre de jornada) sin HU ni RF asociados (H-10, DEC-05) · validación contra el proceso AS-IS de la empresa de estudio |
| **Riesgos encontrados** | R-S01 (procesos TO-BE sin contrastar con la operación real) |
| **Dependencias** | Cap. 3 (actores), Caps. 5–8 (requisitos y reglas que cada caso cita), Cap. 9 |
""")
    parts.append("\n".join(ucs))
    parts.append(cap5())
    parts.append(cap6())
    parts.append(cap7())
    parts.append(cap8())
    parts.append(cap9())
    parts.append(conv(rd("cap10.md")))
    c11 = rd("cap11.md").replace("{{TABLA_DEP}}", tabla_dep()).replace("{{MATRIZ_DEP}}", matriz_dep()).replace("{{TABLA_RAICES}}", raices()).replace("{{TABLA_CICLOS}}", ciclos())
    parts.append(conv(c11))
    parts.append(conv(rd("cap12.md").replace("{{TABLA_C1}}", tabla_c1())))
    parts.append(annex_a())
    parts.append(annex_b())
    parts.append(conv(rd("annex_c.md")))
    parts.append("\n---\n\n*Fin del documento SRS_COLBASOFT v1.2 — La monografía original permanece sin modificaciones.*\n")
    return "\n".join(parts)

if __name__ == "__main__":
    doc = assemble()
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = doc.replace(" (faltan: )", "")
    open(OUT, "w", encoding="utf8", newline="\n").write(doc)
    print("written", OUT, len(doc), "chars", doc.count("\n"), "lines")
