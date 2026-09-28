# -*- coding: utf-8 -*-
import re
from ids import *

def hu(n): return f"HU-{n:03d}"
def rf(n): return f"RF-{n:03d}"

# ---------------- RF -> HU (legacy numbers)  [SRS] derivación de esta fase ----------------
_RF_HU = {
1:[1],2:[1],3:[1,94],4:[1],5:[2],6:[3],7:[4],
8:[5],9:[5],10:[5],11:[6],12:[6],13:[9,7],14:[8],15:[7],
16:[10],17:[10],18:[10],19:[10],20:[11],21:[12],22:[13],23:[13],24:[14],25:[15],
26:[16],27:[16],28:[16],29:[17],30:[18],31:[19],
32:[20],33:[20],34:[20],35:[20,35],36:[21,35],37:[22],38:[23],39:[24,35],
40:[25],41:[25],42:[26],43:[27],44:[25],45:[28],46:[28],47:[29],
48:[30],49:[30],50:[36],51:[30],52:[31],53:[31],54:[33],55:[33],56:[33],57:[32],58:[32],59:[34],60:[37],
61:[38],62:[38],63:[38],64:[41],65:[39],66:[44],67:[40],68:[40],69:[40,38],70:[42],71:[43],
72:[45],73:[45],74:[46],75:[46],76:[46,35],77:[46],78:[47],79:[48],80:[48],81:[49],82:[50,51],
83:[52],84:[52],85:[52],86:[54,102],87:[53],88:[55],89:[52,53],90:[53,102],91:[56],92:[57],
93:[58],94:[58],95:[58,60],96:[60],97:[58],98:[59],99:[61,62],100:[61],101:[61],102:[62],103:[63],104:[64],105:[65],
106:[67],107:[67],108:[67],109:[68,69],110:[68],111:[68],
112:[71,72,73,74],113:[71],114:[71],115:[73],116:[72],117:[75],118:[76],119:[72],
120:[77],121:[77],122:[78],123:[78],124:[77,80],125:[79],126:[81],
127:[82,83],128:[82],129:[82],130:[82,83],131:[84],132:[86],133:[85],
134:[87,88],135:[87],136:[65],137:[89],138:[89],139:[88,89],140:[90],
141:[91],142:[91],143:[93],144:[92],
145:[94],146:[94],147:[94],148:[95],149:[95],150:[96],151:[97],
152:[98],153:[98],154:[98],155:[98],156:[99],157:[100],
158:[101],159:[101,92],160:[101,92],161:[103,66],162:[101],
}
RF_HU = {rf(k): [hu(x) for x in v] for k, v in _RF_HU.items()}
HU_RF = {}
for r, hs in RF_HU.items():
    for h in hs:
        HU_RF.setdefault(h, []).append(r)
HU_COV_NOTE = {
 "HU-069": "Cobertura parcial: se apoya en RF-133 (escalamiento genérico) y RF-109; no existe un RF dedicado al escalamiento de novedades vencidas (RN-059).",
 "HU-070": "Cobertura parcial: se compone de RF-083, RF-084, RF-040 y RF-035; no existe un RF dedicado a la regla de mercancía sin registro (RN-043).",
}
HU_RF["HU-069"] = ["RF-133", "RF-109"]
HU_RF["HU-070"] = ["RF-083", "RF-084", "RF-040", "RF-035"]

# ---------------- RN referenciadas por token (legacy key) ----------------
def rn_key(tok):
    if tok in RN_NEW:
        return tok
    if tok + "*" in RN_NEW:
        return tok + "*"
    return None

def rn_tokens(text):
    out = []
    for t in re.findall(r"RN-\d{3}b?", text):
        k = rn_key(t)
        if k and k not in out:
            out.append(k)
    return out

_RF_RN_EXTRA = {
1:["RN-001"],2:["RN-001"],3:["RN-061"],8:["RN-001","RN-014"],12:["RN-063","RN-076"],15:["RN-061"],
16:["RN-002"],20:["RN-068"],26:["RN-071"],27:["RN-071"],29:["RN-072"],31:["RN-074"],
32:["RN-014","RN-019"],38:["RN-075"],39:["RN-020"],40:["RN-015","RN-016"],42:["RN-015"],43:["RN-016"],
50:["RN-002b"],52:["RN-054"],57:["RN-057b"],58:["RN-065","RN-012"],62:["RN-048"],69:["RN-031","RN-065"],
72:["RN-026","RN-021"],73:["RN-026"],78:["RN-031","RN-025"],79:["RN-032"],
83:["RN-029","RN-009"],89:["RN-065","RN-012"],95:["RN-039"],99:["RN-039"],
112:["RN-065","RN-067"],113:["RN-025","RN-031","RN-032","RN-036"],115:["RN-066"],117:["RN-065"],119:["RN-067"],
120:["RN-001","RN-012"],121:["RN-001"],123:["RN-012","RN-070"],125:["RN-065","RN-080"],
129:["RN-075"],130:["RN-021","RN-034","RN-037","RN-038","RN-044"],
139:["RN-078"],145:["RN-061"],147:["RN-061"],
152:["RN-024","RN-030","RN-034","RN-041"],154:["RN-079"],155:["RN-079"],
157:["RN-001","RN-009","RN-012","RN-023","RN-029","RN-040","RN-041","RN-061","RN-063","RN-065"],
30:["RN-036b","RN-073"],11:["RN-076","RN-077"],
}
RF_RN = {}
for r in D["rf"]:
    toks = rn_tokens(r["text"] + " " + r["dep"] + " " + r["origin"])
    for k in _RF_RN_EXTRA.get(int(r["id"][3:]), []):
        kk = rn_key(k)
        assert kk, k
        if kk not in toks:
            toks.append(kk)
    RF_RN[r["id"]] = toks

HU_RN = {}
for h in D["hu"]:
    toks = rn_tokens(h["tags"] + " " + h["crit_raw"] + " " + h["story"])
    for rr in HU_RF.get(h["id"], []):
        for k in RF_RN.get(rr, []):
            if k not in toks:
                toks.append(k)
    HU_RN[h["id"]] = toks

# ---------------- KPI <-> RF ----------------
_KPI_RF = {
"KPI-01":[99,105,136,141], "KPI-02":[103,105,136], "KPI-03":[93,104,136], "KPI-04":[99,136],
"KPI-05":[58,69,72,120,136], "KPI-06":[100,136], "KPI-07":[42,136], "KPI-08":[83,99,123,136],
"KPI-09":[114,125,136,151], "KPI-10":[39,136], "KPI-11":[58,69,72,136], "KPI-12":[48,58,136],
"KPI-13":[70,136], "KPI-14":[83,92,136], "KPI-15":[79,81,136], "KPI-16":[69,136],
"KPI-17":[120,136], "KPI-18":[36,115,136], "KPI-19":[127,130,131,136], "KPI-20":[131,133,136],
"KPI-21":[130,136], "KPI-22":[66,86,90,136], "KPI-23":[106,109,111,136], "KPI-24":[120,136],
}
KPI_RF = {k: [rf(x) for x in v] for k, v in _KPI_RF.items()}
RF_KPI = {}
for k, v in KPI_RF.items():
    for r in v:
        RF_KPI.setdefault(r, []).append(k)
HU_KPI = {}
for r, ks in RF_KPI.items():
    if r == "RF-136":
        continue
    for h in RF_HU.get(r, []):
        HU_KPI.setdefault(h, set()).update(ks)
HU_KPI.setdefault("HU-065", set()).update(["KPI-01", "KPI-02"])
for h in D["hu"]:
    for k in re.findall(r"KPI-\d\d", h["story"] + h["crit_raw"]):
        HU_KPI.setdefault(h["id"], set()).add(k)

# ---------------- RF -> CD / PR / DC ----------------
_RF_CD = {
1:"PR-05",2:"PR-05",3:"CD-47",4:"CD-47",5:"PR-05",6:"PR-05",7:"PR-05",
8:"DC-04",9:"DC-04",10:"DC-04",11:"DC-04",12:"CD-28",13:"DC-04",14:"CD-12, CD-13",15:"CD-47",
16:"CD-01, CD-02, CD-10",17:"CD-02",18:"CD-03, CD-04",19:"CD-05",20:"CD-11",21:"CD-02, CD-18",22:"CD-05, CD-46",23:"CD-05, CD-46",24:"CD-02",25:"CD-10, CD-13",
26:"CD-06",27:"CD-06, CD-07",28:"CD-06",29:"CD-06, CD-14",30:"CD-06, CD-22",31:"CD-06",
32:"CD-12, CD-13, CD-14",33:"CD-14",34:"CD-16",35:"CD-14, CD-19",36:"CD-15",37:"CD-14",38:"CD-13",39:"CD-13, CD-14",
40:"CD-07, CD-08",41:"CD-08",42:"CD-08",43:"CD-08, CD-14",44:"CD-08",45:"CD-08",46:"CD-08",47:"CD-09",
48:"CD-35",49:"CD-35",50:"CD-02, CD-35",51:"CD-35",52:"CD-16, CD-35",53:"CD-35",54:"CD-35",55:"CD-35",56:"CD-35",57:"CD-29, CD-35",58:"CD-29, CD-37",59:"CD-17, CD-22",60:"CD-35",
61:"CD-30, CD-36",62:"CD-30",63:"CD-19",64:"CD-18",65:"CD-20",66:"CD-30, CD-46",67:"CD-30",68:"CD-08",69:"CD-20, CD-30",70:"CD-30, CD-36",71:"CD-29, CD-30",
72:"CD-31",73:"CD-18, CD-31",74:"CD-31",75:"CD-31",76:"CD-14, CD-15",77:"CD-22",78:"CD-20, CD-32",79:"CD-32",80:"CD-23",81:"CD-32",82:"CD-23, CD-32, CD-45",
83:"CD-27, CD-33",84:"CD-33, CD-36",85:"CD-33",86:"CD-33, CD-46",87:"CD-33",88:"CD-18, CD-33",89:"CD-24, CD-33, CD-37",90:"CD-33",91:"CD-33, CD-45",92:"CD-33",
93:"CD-39",94:"CD-39",95:"CD-25",96:"CD-25",97:"CD-41",98:"CD-26",99:"CD-27",100:"CD-42",101:"CD-42",102:"CD-38",103:"CD-40",104:"CD-40",105:"CD-43",
106:"CD-48",107:"CD-08, CD-48",108:"CD-48",109:"CD-48",110:"CD-48",111:"CD-48",
112:"CD-18",113:"CD-44",114:"CD-18, CD-37",115:"CD-14, CD-18",116:"CD-18",117:"CD-18, CD-37",118:"CD-02",119:"CD-18",
120:"CD-21, CD-28, CD-37",121:"CD-28",122:"CD-37",123:"CD-34",124:"CD-21, CD-37",125:"CD-18, CD-37",126:"CD-37",
127:"CD-45",128:"CD-45",129:"CD-45",130:"CD-45",131:"CD-45",132:"CD-45",133:"CD-45",
134:"CD-18, CD-28",135:"CD-43",136:"CD-43",137:"DC-06",138:"DC-06",139:"CD-47",140:"DC-06",
141:"CD-19, CD-45",142:"CD-18",143:"CD-13",144:"PR-06",
145:"CD-47",146:"CD-47",147:"CD-47",148:"ROL-05",149:"ROL-05",150:"ROL-05",151:"CD-47",
152:"CD-46",153:"CD-46",154:"CD-47",155:"CD-46",156:"CD-36",157:"CD-46",
158:"CD-41",159:"CD-41",160:"CD-28",161:"CD-41, CD-42",162:"DC-05",
}
RF_CD = {rf(k): v for k, v in _RF_CD.items()}
assert len(RF_CD) == 162

# ---------------- Objetivos de la monografía por módulo (derivación) ----------------
OBJ = {
 "OG": "Objetivo General (§5): modelo conceptual de automatización de la gestión de inventarios para mejorar eficiencia y competitividad",
 "OE-1": "OE-1 (§5.5): conceptos de automatización, gestión de inventarios y eficiencia operativa",
 "OE-2": "OE-2 (§5.5): modelos de adopción tecnológica y su aplicabilidad (resistencia a la automatización)",
 "OE-3": "OE-3 (§5.5): síntesis en modelo conceptual — trazabilidad, reducción de errores, competitividad",
}
MOD_OBJ = {
 "M-01": ("OE-3", "Atribución personal de toda acción: base de la trazabilidad [MON §7.1]"),
 "M-02": ("OE-3", "Segregación de funciones y control: reducción de errores [MON §6]"),
 "M-03": ("OE-1", "Gestión de inventarios: maestro de lo que puede existir [MON §7.1]"),
 "M-04": ("OE-3", "Trazabilidad de origen por lote [MON §7.1]"),
 "M-05": ("OE-1", "Gestión de inventarios: dónde está la existencia [MON §7.1]"),
 "M-06": ("OE-3", "Sustitución de digitación por escaneo: reduce errores humanos [MON §7.2]"),
 "M-07": ("OE-1", "Registro digital de entradas [MON §8.2]"),
 "M-08": ("OE-1", "Registro digital de salidas [MON §8.2]"),
 "M-09": ("OE-1", "Registro digital de movimientos [MON §8.2]"),
 "M-10": ("OE-3", "Corrección controlada del registro: reducción de errores [MON §6, §8.2]"),
 "M-11": ("OE-3", "Medición de exactitud del inventario [MON §8.2]"),
 "M-12": ("OE-2", "Vía de reporte sin imputación: mitiga resistencia cultural [MON §4]"),
 "M-13": ("OE-3", "Visibilidad de la existencia en el momento [MON §6, §7.2]"),
 "M-14": ("OE-3", "Kardex: materialización de la trazabilidad [MON §7.1]"),
 "M-15": ("OE-3", "Automatización basada en reglas: anticipar rupturas y sobre stock [MON §3, §7.1]"),
 "M-16": ("OE-3", "Evaluación del impacto con indicadores [MON §8.2]"),
 "M-17": ("OE-3", "Visibilidad operativa para la toma de decisiones [MON §6]"),
 "M-18": ("OE-3", "Verificación independiente de la trazabilidad [MON §7.1]"),
 "M-19": ("OE-2", "Adaptación escalonada a la operación real [MON §8.2]"),
 "M-20": ("OE-2", "Guía al operario: reduce la barrera de capacitación [MON §3, §8.2]"),
}

# ---------------- Horizonte de entrega SPEC §12 ----------------
_H2_HU = [14,18,19,24,29,47,48,49,50,51,56,63,64,75,85,89,90,93,103]
_H2_RF = [24,30,31,39,47,78,79,80,81,82,91,103,104,117,133,137,140,143,161]
H2_HU = {hu(x) for x in _H2_HU}
H2_RF = {rf(x) for x in _H2_RF}
H2_RNF = {"RNF-028"}

MOSCOW = {"P0": "Must", "P1": "Should", "P2": "Could", "P3": "Won't (esta versión)"}

# ---------------- Dependencias entre historias (legacy) ----------------
_HU_DEPS = {
1:[],2:[1],3:[1],4:[1,5],5:[1],6:[5],7:[5],8:[5,20],9:[5],
10:[5],11:[10],12:[10],13:[10],14:[10],15:[10],
16:[10],17:[16,71],18:[16,17],19:[16],
20:[5],21:[20],22:[20],23:[20,5],24:[15,20,21],
25:[10,16],26:[25],27:[20],28:[25],29:[25],
30:[10,5],31:[30],32:[31,16],33:[30,31],34:[31,67],35:[20,21,24,25],36:[10,30],37:[32],
38:[10,20,99],39:[38],40:[39,26],41:[38],42:[38,99],43:[32,38],44:[38,98],
45:[26,20],46:[45],47:[20,71],48:[47,26,101],49:[48],50:[48,98],51:[47,48],
52:[71,99],53:[52,5],54:[52,98],55:[52],56:[52,84],57:[52],
58:[20,10,101],59:[58,26],60:[58],61:[58,98],62:[58,59,61,52],63:[58],64:[63],65:[62],66:[58,101],
67:[26,1],68:[67],69:[67,98],70:[67,52,25,35],
71:[32,77],72:[26,71],73:[71],74:[71,20],75:[77],76:[71],
77:[32],78:[77],79:[77],80:[77,16],81:[77],
82:[13,71],83:[13],84:[82],85:[82,98],86:[82],
87:[71],88:[77],89:[87,88],90:[87],
91:[71,82],92:[101],93:[91,20],
94:[1],95:[5],96:[94],97:[53,94],
98:[1,5],99:[5],100:[98],
101:[1],102:[53,101],103:[101],
}
HU_DEPS = {hu(k): [hu(x) for x in v] for k, v in _HU_DEPS.items()}
assert len(HU_DEPS) == 103

def check():
    hu_wo_rf = [h["id"] for h in D["hu"] if h["id"] not in HU_RF]
    rf_wo_hu = [r["id"] for r in D["rf"] if r["id"] not in RF_HU]
    print("HU sin RF:", hu_wo_rf, "| RF sin HU:", rf_wo_hu)
    rn_real = [r["id"] for r in D["rn"] if r["tipo"] != "—"]
    rn_rf = {}
    for r, ks in RF_RN.items():
        for k in ks:
            rn_rf.setdefault(k, []).append(r)
    rn_hu = {}
    for h, ks in HU_RN.items():
        for k in ks:
            rn_hu.setdefault(k, []).append(h)
    print("RN sin RF:", [RN_NEW[k] + "(" + k + ")" for k in rn_real if k not in rn_rf])
    print("RN sin HU:", [RN_NEW[k] + "(" + k + ")" for k in rn_real if k not in rn_hu])
    print("RF sin RN:", sum(1 for r in RF_RN if not RF_RN[r]), " RF sin KPI:", sum(1 for r in RF_HU if r not in RF_KPI))
    print("KPI sin RF:", [k for k in ["KPI-%02d" % i for i in range(1, 25)] if k not in KPI_RF])

if __name__ == "__main__":
    check()
