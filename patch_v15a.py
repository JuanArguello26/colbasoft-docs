from patch_srs_lib import patch

patch("trace.py", [
 ("111:[45,82],112:[63,98],113:[101],114:[113],\n}", "111:[45,82],112:[63,98],113:[101],114:[113],\n}\n# v1.5 (H-19 resuelto en el SPEC v1.4): HU-035 ya no depende de HU-024 (criterios configurables, Horizonte 2)\n_HU_DEPS[35] = [20, 21, 25]"),
])
s = open("trace.py", encoding="utf8").read()
s += '''

# ---------------- Corte de entrega C1 (noviembre de 2026), SPEC v1.5 §12.7 ----------------
C1_BLOQUES = [
 ("C1-1", "Fundación", [1, 2, 5, 6, 10, 11, 20, 21, 98, 99, 94]),
 ("C1-2", "Identificación y lotes", [25, 26, 16]),
 ("C1-3", "Entradas, piezas y ubicación", [30, 31, 32, 33, 35, 104]),
 ("C1-4", "Kardex y consulta de existencia", [77, 78, 110, 71, 72, 73]),
 ("C1-5", "Movimientos internos", [45, 46, 106]),
 ("C1-6", "Salidas y corte parcial", [38, 39, 40, 41, 107, 108]),
]
C1_HU = {hu(n) for _, _, ns in C1_BLOQUES for n in ns}

def _c1_calculado():
    """Criterio del SPEC §12.7: P0 del Horizonte 1 de M-01…M-09, M-13, M-14 y M-19, sus dependencias y HU-094."""
    mods = {"M-01", "M-02", "M-03", "M-04", "M-05", "M-06", "M-07", "M-08", "M-09", "M-13", "M-14", "M-19"}
    sel = {h["id"] for h in D["hu"] if h["mod"] in mods and h["id"] not in H2_HU and h["prio"] == "P0"} | {"HU-094"}
    cambio = True
    while cambio:
        cambio = False
        for h in list(sel):
            for dep in HU_DEPS.get(h, []):
                if dep not in sel:
                    sel.add(dep); cambio = True
    return sel

assert C1_HU == _c1_calculado(), sorted(C1_HU ^ _c1_calculado())
C1_RF = sorted({r for h in C1_HU for r in HU_RF.get(h, []) if r not in H2_RF})
assert len(C1_HU) == 35 and len(C1_RF) == 83, (len(C1_HU), len(C1_RF))
'''
open("trace.py", "w", encoding="utf8", newline="\n").write(s)

patch("build_srs.py", [
 ('OUT = os.path.join(OUT_DIR, "SRS_COLBASOFT_v1.4.md")', 'OUT = os.path.join(OUT_DIR, "SRS_COLBASOFT_v1.5.md")'),
 ('    parts.append(conv(rd("cap12.md")))', '    parts.append(conv(rd("cap12.md").replace("{{TABLA_C1}}", tabla_c1())))'),
 ("def is_mod_rf(mod):", '''def tabla_c1():
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
    return "\\n".join(o)

def is_mod_rf(mod):'''),
])

CAMBIOS = """## Control de cambios de la versión 1.5

> La v1.5 se regenera desde las mismas fuentes, tras incorporar al SPEC v1.5 las decisiones del Director del **30 de septiembre de 2026** sobre la validación del proyecto de grado y la entrega de noviembre. La v1.4 se conserva sin cambios en `SRS_COLBASOFT_v1.4.md`.

| Decisión | Efecto en este SRS |
|---|---|
| **Sin empresa piloto; validación solo con datos ficticios** (el asesor lo aceptó) | Nueva convención **§1.4.8** (cómo se leen «empresa piloto», «piloto» y «verificación de campo»); supuestos **S-1, S-2 y S-7** (Cap. 2); criterios **CA-04, CA-05 y CA-17** y §12.7 (Cap. 12); Anexo C (C.13). Los requisitos **no cambian** |
| **Corte de entrega C1 (noviembre de 2026)** | Nuevo **§12.8** del Cap. 12: 35 historias y 83 requisitos, generados desde la trazabilidad, con bloques, orden y regla de recorte |
| **Corrección de trazabilidad (H-19)** | HU-ENT-006 ya no depende de HU-BOD-005 en la tabla de dependencias entre historias |

Cifras: sin cambios (114 HU, 185 RF, 515 escenarios, 92 reglas). **Limitación que este SRS ahora declara:** sin AS-IS ni línea base el proyecto no demuestra impacto medido en campo; demuestra viabilidad funcional con datos ficticios.

"""
patch("cap00.md", [
 ("# SRS_COLBASOFT v1.4\n", "# SRS_COLBASOFT v1.5\n"),
 ("| **Versión** | 1.4 |", "| **Versión** | 1.5 |"),
 ("· 30 de septiembre de 2026 (v1.2, v1.3 y v1.4) |", "· 30 de septiembre de 2026 (v1.2 a v1.5) |"),
 ("| **Estado** | **Borrador v1.4** (30-sep-2026): registra las respuestas a DEC-01…DEC-09, H-19, H-20, HD-29 y HD-30. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar y pendiente HD-28 |",
  "| **Estado** | **Borrador v1.5** (30-sep-2026): registra la validación con datos ficticios y el corte de entrega C1. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar y pendiente HD-28 |"),
 ("| **Versión anterior** | `SRS_COLBASOFT_v1.3.md`,", "| **Versión anterior** | `SRS_COLBASOFT_v1.4.md`, `SRS_COLBASOFT_v1.3.md`,"),
 ("COLBASOFT_SPEC v1.4 → **SRS v1.4** |", "COLBASOFT_SPEC v1.5 → **SRS v1.5** |"),
 ("`COLBASOFT_SPEC_v1.4.md` (Fase 2, con las respuestas a H-19, H-20, HD-29 y HD-30) |", "`COLBASOFT_SPEC_v1.5.md` (Fase 2, con la validación con datos ficticios y el corte C1) |"),
 ("del COLBASOFT_SPEC v1.4.", "del COLBASOFT_SPEC v1.5."),
 ("## Control de cambios de la versión 1.4\n", CAMBIOS + "## Control de cambios de la versión 1.4\n"),
])
patch("cap01.md", [
 ("`COLBASOFT_SPEC_v1.4.md` (5 sep. 2026; v1.1 del 29 sep. 2026; v1.2, v1.3 y v1.4 del 30 sep. 2026)", "`COLBASOFT_SPEC_v1.5.md` (5 sep. 2026; v1.1 del 29 sep. 2026; v1.2 a v1.5 del 30 sep. 2026)"),
 ("\n## 1.5 Definiciones, acrónimos y abreviaturas\n", """
### 1.4.8 Validación con datos ficticios `[v1.5]`

El 30 de septiembre de 2026 el Director decidió que **no habrá empresa piloto** en el proyecto de grado y que la validación se hará con **datos ficticios** (el asesor lo aceptó). Mientras no exista una empresa real, toda referencia de este documento a «empresa piloto», «piloto», «período de prueba», «verificación de campo» o «línea base de la empresa» se lee como **conjunto de datos ficticios de prueba (DS-1)**: datos aleatorios y verosímiles, preparados en una hoja de Excel y **cargados en una base de datos real** (el Excel no es la base de datos del sistema). DS-1 no contiene precios, clientes ni proveedores (DC-03) ni nombra empresa alguna (DC-01).

**Alcance de lo que se puede afirmar.** El sistema cumple sus requisitos, reglas y criterios de aceptación ejecutables con DS-1. **No se puede afirmar** reducción de errores, ganancia de trazabilidad o de productividad medidas en operación real, ni que los procesos TO-BE coincidan con los de una empresa (S-2, R-S01). Ver SPEC §12.8.

## 1.5 Definiciones, acrónimos y abreviaturas
"""),
])
patch("cap02.md", [
 ("| S-1 | Existe una **empresa de estudio** dispuesta a participar en levantamiento, piloto y medición `[DC-01]` | 🔴 Abierto (V-01) | RG-37 |",
  "| S-1 | ~~Existe una empresa de estudio dispuesta a participar en levantamiento, piloto y medición~~ `[DC-01]` | ⚪ **No aplica (v1.5):** no hay empresa piloto; se valida con datos ficticios (§1.4.8) | RG-37 |"),
 ("| S-2 | Los procesos del Cap. 4 (TO-BE) son compatibles con la operación real de la empresa | 🔴 No verificado: AS-IS sin levantar | R-S01 |",
  "| S-2 | Los procesos del Cap. 4 (TO-BE) son compatibles con la operación real de la empresa | 🔴 **No verificable en el proyecto de grado (v1.5): se declara como limitación.** El kit `06_ASIS_KIT` queda para si aparece una empresa | R-S01 |"),
 ("| S-7 | La **línea base** de KPI-01, KPI-05 y KPI-08 se levantará antes del piloto | 🔴 Abierto (V-03) | RG-36 |",
  "| S-7 | ~~La línea base de KPI-01, KPI-05 y KPI-08 se levantará antes del piloto~~ | ⚪ **No aplica (v1.5):** no se levantará; el impacto no se mide en campo | RG-36 |"),
 ("| **Pendiente** | Confirmar los supuestos S-1…S-4 y S-6 con la empresa de estudio (Fase 3 del roadmap) |", "| **Pendiente** | S-3, S-4 y S-6 se asumen sin verificación de campo (v1.5); S-1 y S-7 no aplican; S-2 se declara como limitación |"),
])
patch("cap12.md", [
 ("| **CA-04** | Los 24 casos de uso del Cap. 4 pueden recorrerse de extremo a extremo con datos de la empresa piloto (CU-19 solo si DEC-05 lo incorpora) |", "| **CA-04** | Los 24 casos de uso del Cap. 4 pueden recorrerse de extremo a extremo con datos ficticios (DS-1, §1.4.8) |"),
 ("operan **sin cuaderno** durante el período de prueba (OP-01) |", "operan **sin cuaderno** durante la prueba con DS-1 (OP-01) |"),
 ("| Cero movimientos registrados fuera del sistema (verificación de campo)", "| Cero movimientos registrados fuera del sistema (comprobado con DS-1; sin verificación de campo)"),
 ("| **CA-17** | **Existe línea base** de los tres KPI antes de iniciar el piloto (V-03) | Documento de línea base (**precondición externa al software**) |", "| **CA-17** | ~~Existe línea base de los tres KPI antes del piloto~~ **No aplica (v1.5)**: los KPI son calculables con DS-1, pero no hay línea base real (V-03 no aplica) | Cálculo de KPI-01, KPI-05 y KPI-08 sobre DS-1 |"),
 ("| Autorización de contacto con empresas reales | V-01 | 🔴 Abierta |", "| Autorización de contacto con empresas reales | V-01 | ⚪ No aplica en el proyecto de grado (v1.5) |"),
 ("| Levantamiento de la línea base de KPI-01, KPI-05, KPI-08 | V-03 | 🔴 Abierta |", "| Levantamiento de la línea base de KPI-01, KPI-05, KPI-08 | V-03 | ⚪ No se levantará (v1.5) |"),
 ("| Criterio si el piloto no alcanza las cifras citadas | V-06 | 🔴 Abierta |", "| Criterio si el piloto no alcanza las cifras citadas | V-06 | ⚪ No aplica: no hay piloto (v1.5) |"),
 ("| Entregable mínimo aprobatorio | S-15 | 🔴 Abierta (DEC-01) |", "| Entregable mínimo aprobatorio | S-15 | 🟢 Resuelta (DEC-01 = A, v1.2) |"),
 ("| Levantamiento de la infraestructura real (tablets, cámara, impresión, conectividad) | C.2.7 | 🟡 Por hacer |", "| Levantamiento de la infraestructura real (tablets, cámara, impresión, conectividad) | C.2.7 | 🟡 Se asume (S-3, S-4) sin verificación de campo (v1.5) |"),
 ("\n---\n\n**ESTADO DEL CAPÍTULO 12**", """
## 12.8 Corte de entrega C1 (noviembre de 2026) y validación con datos ficticios `[v1.5]`

Es un **corte de entrega dentro del Horizonte 1**: no cambia el Núcleo (94 HU y 164 RF), que sigue siendo el umbral aprobatorio `[DEC-01]`. Criterio: historias Must (P0) del Horizonte 1 de los módulos M-01 a M-09, M-13, M-14 y M-19, más sus dependencias y la bitácora (HU-AUD-001). Se construye en el orden C1-1 a C1-6; **si el tiempo no alcanza, se recorta desde el último bloque hacia atrás**, y cada bloque completo entrega un ciclo verificable.

{{TABLA_C1}}

**Fuera del corte C1** (siguen en el Núcleo): ajustes, conteos, novedades, alertas, reportes e indicadores, dashboard, tareas, registro de contenedores agrupados (HU-ENT-010), movimiento en tránsito (HU-MOV-009) y cierre de jornada (HU-TAR-004, HU-TAR-005).

**Validación.** Sin empresa piloto, el MVP se valida con datos ficticios (§1.4.8): se demuestra **viabilidad funcional**, no impacto medido en campo. Esta limitación debe figurar en el informe final.

---

**ESTADO DEL CAPÍTULO 12**"""),
 ("| **Pendiente** | Decisión DEC-01 (umbral aprobatorio) · calibración de valores numéricos de RNF (pendiente #12) · línea base (V-03) |", "| **Pendiente** | Calibración de valores numéricos de RNF (pendiente #12; sin línea base real, se fijan con DS-1) |"),
])
patch("annex_c.md", [
 ("---\n\n**ESTADO DEL ANEXO C**", """## C.13 Decisiones sobre validación y entrega (versión 1.5)

> Tomadas el 30 de septiembre de 2026.

| Decisión | Efecto en este SRS |
|---|---|
| **Sin empresa piloto; validación solo con datos ficticios** (el asesor lo aceptó). El Excel es solo una carga de datos de prueba a una base de datos real | §1.4.8; S-1 y S-7 no aplican; S-2 y R-S01 pasan a **limitación declarada**; CA-04, CA-05 y CA-17 |
| **Corte de entrega C1 (noviembre de 2026)** | §12.8: 35 HU y 83 RF con orden y regla de recorte |

**Riesgos que se mantienen:** RG-35 y RG-36 (sin línea base no hay demostración de impacto) ya no son un pendiente del proyecto sino una **limitación declarada**. R-S01 sigue vigente.

---

**ESTADO DEL ANEXO C**"""),
])
print("ok")
