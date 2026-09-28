# -*- coding: utf-8 -*-
import json, re
import pathlib as _pl
D = json.load(open(_pl.Path(__file__).resolve().parent / "spec.json", encoding="utf8"))

MOD = {  # code, nombre, grupo, prioridad SPEC
 "M-01": ("ACC", "Acceso y Autenticación"),
 "M-02": ("USR", "Usuarios y Roles"),
 "M-03": ("CAT", "Catálogo de Referencias"),
 "M-04": ("LOT", "Gestión de Lotes"),
 "M-05": ("BOD", "Estructura de Bodega"),
 "M-06": ("QRC", "Identificación QR"),
 "M-07": ("ENT", "Entradas y Recepción"),
 "M-08": ("SAL", "Salidas"),
 "M-09": ("MOV", "Movimientos y Transferencias"),
 "M-10": ("AJU", "Ajustes de Inventario"),
 "M-11": ("CNT", "Conteos"),
 "M-12": ("NOV", "Novedades de Mercancía"),
 "M-13": ("INV", "Consulta de Existencia"),
 "M-14": ("KDX", "Kardex y Trazabilidad"),
 "M-15": ("ALE", "Alertas y Reglas"),
 "M-16": ("REP", "Reportes y Exportación Analítica"),
 "M-17": ("DSH", "Dashboard Operativo"),
 "M-18": ("AUD", "Auditoría y Bitácora"),
 "M-19": ("PAR", "Parámetros y Configuración"),
 "M-20": ("TAR", "Notificaciones y Tareas"),
}
DOM2MOD = {v[0]: k for k, v in MOD.items()}

def seq_ids(items, prefix):
    cnt = {}
    m = {}
    for it in items:
        dom = MOD[it["mod"]][0]
        cnt[dom] = cnt.get(dom, 0) + 1
        m[it["id"]] = f"{prefix}-{dom}-{cnt[dom]:03d}"
    return m

HU_NEW = seq_ids(D["hu"], "HU")
RF_NEW = seq_ids(D["rf"], "RF")

RNF_CAT = {"Seguridad": "SEG", "Disponibilidad": "DSP", "Rendimiento": "REN", "Escalabilidad": "ESC",
           "Accesibilidad": "ACS", "Auditoría": "AUD", "Usabilidad": "USA",
           "Compatibilidad Tablet": "TAB", "Compatibilidad Navegador": "NAV"}
RNF_NEW = {}
cnt = {}
for r in D["rnf"]:
    c = RNF_CAT[r["cat"]]
    cnt[c] = cnt.get(c, 0) + 1
    RNF_NEW[r["id"]] = f"RNF-{c}-{cnt[c]:03d}"

RN_DOM = {
 "INT": ("Integridad y atribución del registro", ["RN-001","RN-012","RN-054","RN-065","RN-066","RN-067","RN-068"]),
 "EXI": ("Existencia, disponibilidad y estados", ["RN-009","RN-019","RN-025","RN-031","RN-032","RN-036"]),
 "MAE": ("Maestros, unicidad y eliminación lógica", ["RN-002","RN-004","RN-010","RN-011","RN-013","RN-014","RN-063","RN-076*","RN-077*"]),
 "IDE": ("Identificación por QR", ["RN-015","RN-016","RN-017","RN-018"]),
 "LOT": ("Lotes", ["RN-071*","RN-072*","RN-036b*","RN-073*","RN-074*"]),
 "ENT": ("Entradas y recepción", ["RN-002b*","RN-003","RN-005","RN-006","RN-007","RN-008","RN-057b*"]),
 "SAL": ("Salidas", ["RN-030","RN-048","RN-049","RN-050","RN-051","RN-052","RN-053"]),
 "MOV": ("Movimientos, ubicación y transferencias", ["RN-020","RN-021","RN-022","RN-026","RN-027","RN-028","RN-033","RN-034","RN-035"]),
 "AJU": ("Ajustes y aprobaciones", ["RN-023","RN-024","RN-029","RN-037","RN-038","RN-062","RN-070*"]),
 "CNT": ("Conteos", ["RN-039","RN-040","RN-041","RN-042","RN-044","RN-045","RN-046","RN-047"]),
 "NOV": ("Novedades y mercancía sin registro", ["RN-043","RN-059","RN-060"]),
 "ALE": ("Alertas", ["RN-055","RN-056","RN-057","RN-058","RN-075*"]),
 "AUD": ("Auditoría, bitácora y exportación", ["RN-061","RN-064","RN-078*","RN-079*","RN-080*"]),
}
RN_NEW = {}
RN_DOMOF = {}
for dom, (name, lst) in RN_DOM.items():
    for k, legacy in enumerate(lst, 1):
        assert legacy not in RN_NEW, legacy
        RN_NEW[legacy] = f"RN-{dom}-{k:03d}"
        RN_DOMOF[legacy] = dom

def norm_rn(tok):
    """RN-057b -> RN-057b*, RN-069 etc. Map textual token to spec id key."""
    return tok

if __name__ == "__main__":
    real = {r["id"] for r in D["rn"] if r["tipo"] != "—"}
    print("RN real:", len(real), "mapped:", len(RN_NEW))
    print("unmapped:", sorted(real - set(RN_NEW)))
    print("extra:", sorted(set(RN_NEW) - real))
    print(len(HU_NEW), len(RF_NEW), len(RNF_NEW))
    print(HU_NEW["HU-030"], RF_NEW["RF-120"], RNF_NEW["RNF-014"], RN_NEW["RN-009"])
