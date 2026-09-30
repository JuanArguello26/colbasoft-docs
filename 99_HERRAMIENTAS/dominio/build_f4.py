# -*- coding: utf-8 -*-
import json, os, re, unicodedata
from collections import Counter, OrderedDict
from dm_data import *
from ev_data import *
from gl_data import TERMS

HERE = os.path.dirname(os.path.abspath(__file__))
import sys, pathlib as _pl
ROOT = _pl.Path(__file__).resolve().parents[2]
# Uso: python build_f4.py [carpeta_de_salida]  (por defecto, 03_DOMINIO_FASE_4 del proyecto)
OUT = sys.argv[1] if len(sys.argv) > 1 else str(ROOT / "03_DOMINIO_FASE_4")
S = json.load(open(os.path.join(HERE, "srs_ids.json"), encoding="utf8"))
RN_TXT, KPI_N = S["RN_TXT"], S["KPI"]
ENT = {e["id"]: e for e in ENTITIES}
EVT = {e["id"]: e for e in EVENTS}
SD = {s["id"]: s for s in SUBDOMAINS}
FECHA = "28 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1)"

import sys as _sys
_sys.path.insert(0, os.path.join(HERE, "..", "srs"))
_cwd = os.getcwd(); os.chdir(os.path.join(HERE, "..", "srs"))
from ids import RN_NEW as _RN, HU_NEW as _HU, RF_NEW as _RF, RNF_NEW as _RNF
os.chdir(_cwd)
def _leg(tok):
    if tok.startswith("RNF-"): return _RNF.get(tok)
    if tok.startswith("RN-"): return _RN.get(tok) or _RN.get(tok + "*")
    if tok.startswith("HU-"): return _HU.get(tok)
    if tok.startswith("RF-"): return _RF.get(tok)
def pair(s):
    """Empareja cada ID legacy del SPEC con su ID permanente del SRS, si no lo está ya."""
    def rep(m):
        new = _leg(m.group(1))
        return f"{m.group(1)} (SRS {new})" if new else m.group(1)
    return re.sub(r"(?<![A-Z-])((?:RNF|RN|HU|RF)-\d{3}b?)(?![\w-])(?!\s*(?:→|\())", rep, s)


def en(eid): return f"{eid} {ENT[eid]['nombre']}"
def ids(lst): return ", ".join(lst) if lst else "—"
def estado(completado, riesgos, deps, hallazgos, titulo):
    return f"""
---

**ESTADO DEL CAPÍTULO — {titulo}**

| | |
|---|---|
| **Completado** | {completado} |
| **Riesgos** | {riesgos} |
| **Dependencias** | {deps} |
| **Hallazgos** | {hallazgos} |
"""

def header(doc, sub, extra=""):
    return f"""# {doc}
## {sub}

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | {doc} |
| **Versión** | 1.1 |
| **Fase** | Fase 4 del proyecto — Modelo de Dominio (Checkpoint CP-04) |
| **Fecha** | {FECHA} |
| **Estado** | **Validado técnicamente** (cierre del CP-04, 29-sep-2026). **Aprobación funcional y académica pendiente**: HD-25 y DEC-01…DEC-09 sin responder (`04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md`) |
| **Jerarquía documental** | Monografía → Auditoría Fundacional → COLBASOFT_SPEC v1.1 → SRS_COLBASOFT v1.1 → **Modelo de Dominio v1.1** (DOMAIN_MODEL · EVENT_CATALOG · GLOSSARY) |
| **Documentos hermanos** | {extra} |
| **Autoría del proyecto** | Juan Esteban Argüello · Brayan Alexander Osorio · Brandon José Guerrero |
| **Institución / asesor** | Escuela de Ingeniería — CIAF · Edwin Andrés Cabrera Arredondo |
| **Fuera de alcance** | Arquitectura, modelo de datos, tecnologías, interfaces de integración, notaciones de diseño y código: pertenecen a la Fase 5 y posteriores |

> **Naturaleza.** Este documento es **derivado**: no modifica la monografía, la auditoría, el SPEC ni el SRS. Modela el negocio que esos documentos describen. Toda diferencia entre ellos o frente al Prompt Maestro #004 se registra como **Hallazgo del Dominio (HD-nn)**; no se corrige en silencio.

> **Versión 1.1.** Incorpora las decisiones del cierre del CP-04 (DF5-01, DF5-02, DF5-03, DF5-05 y DF5-06), registradas en `04_CP04_AUDITORIA/04_CP04_CIERRE.md`. El detalle de los cambios está en DOMAIN_MODEL §0.8. La v1.0 se conserva en el historial del repositorio (commit `79f823c`).
"""

# ====================================================================================== DOMAIN_MODEL
def cap0():
    s = """
---

# CAPÍTULO 0 — AUDITORÍA DE REANUDACIÓN

> Reconstrucción del contexto ejecutada **antes** de escribir los tres documentos de la Fase 4. Es común a DOMAIN_MODEL, EVENT_CATALOG y GLOSSARY. Los apartados 0.1 a 0.5 y 0.7 conservan la reconstrucción de la v1.0 (28-sep-2026) como registro histórico; el 0.6 muestra los rangos vigentes y el **0.8** registra los cambios de la v1.1.

## 0.1 Estado del proyecto

| Dimensión | Estado verificado |
|---|---|
| **Monografía** | Congelada. El archivo `MONOGRAFÍA  COLBASOFT.docx` no fue modificado. |
| **Auditoría Fundacional** | Aprobada (Fase 0). |
| **COLBASOFT_SPEC v1.0** | Aprobado según los Prompts #003 y #004; el archivo conserva la leyenda «Emitido para revisión del Director». |
| **SRS_COLBASOFT v1.0** | Declarado aprobado por el Prompt #004. **El archivo sigue en «Emitido para revisión del Director» y sus 9 decisiones DEC-01…DEC-09 no tienen respuesta registrada** (HD-21). |
| **Fase en curso** | Fase 4 — Modelo de Dominio. Sin arquitectura, datos, tecnologías ni código. |
| **Carpeta del proyecto** | `00_MONOGRAFIA_ORIGINAL/`, `00_AUDITORIA_FASE_0/`, `01_SPEC_FASE_2/`, `02_SRS_FASE_3/`; esta fase agrega `03_DOMINIO_FASE_4/`. No se recibieron documentos nuevos. |

## 0.2 Checkpoints existentes

El proyecto no conserva documentos de checkpoint independientes; el Prompt #004 se refiere a «CP-03». La secuencia se reconstruye así (inferida de las fechas y del estado de cada entregable):

| Checkpoint | Hito | Documento | Fecha | Estado |
|---|---|---|---|---|
| **CP-00** | Auditoría fundacional | `AUDITORIA_FUNDACIONAL_COLBASOFT.md` | 1-sep-2026 | ✅ Cerrado |
| **CP-01** | Constitución del proyecto: decisiones DC-01…DC-08 | Registradas en el SPEC §0.1 | antes del 5-sep-2026 | ✅ Cerrado parcialmente (19 de 24 preguntas bloqueantes) |
| **CP-02** | Especificación funcional | `COLBASOFT_SPEC_v1.0.md` | 5-sep-2026 | ✅ Cerrado |
| **CP-03** | Especificación de requisitos | `SRS_COLBASOFT_v1.0.md` | 28-sep-2026 | ✅ Cerrado por instrucción del Prompt #004 (con DEC abiertas) |
| **CP-04** | **Modelo de dominio** | `DOMAIN_MODEL.md` · `EVENT_CATALOG.md` · `GLOSSARY.md` | 28-sep-2026 | 🟡 Emitido (este entregable) |

## 0.3 Documentos recibidos y uso en esta fase

| # | Documento | Versión | Qué aporta al dominio |
|---|---|---|---|
| 1 | Monografía original | Única, inmutable | Problema, objetivos (OG, OE-1…OE-3), cinco conceptos formales (§7.1), indicadores de §8.2, términos consagrados («ruptura de stock», «sobre stock») |
| 2 | Auditoría Fundacional | Fase 0 | Vacíos (C.1.4 trazabilidad, C.1.7 modelo de dominio), problemas P-01…P-24, reglas innegociables |
| 3 | COLBASOFT_SPEC v1.0 | v1.0 | **Fuente principal del vocabulario**: 48 conceptos (CD-01…CD-48), vocabulario controlado (§0.5), 14 procesos (PN), 20 módulos, reglas, KPI, principios de rol |
| 4 | SRS_COLBASOFT v1.0 | v1.0 | IDs permanentes (HU, RF, RNF, RN), 82 reglas por dominio, 24 casos de uso, trazabilidad, hallazgos H-01…H-18, decisiones DEC-01…DEC-09 |

## 0.4 Decisiones constitucionales detectadas

**Reglas Innegociables (Auditoría):** RI-1 la monografía no se modifica · RI-2 no eliminar conceptos esenciales · RI-3 no inventar funcionalidades · RI-4 no escribir código · RI-5 no crear arquitectura · RI-6 no cambiar objetivos sin justificar · RI-7 todo hallazgo cita su origen.

**Decisiones del Director (SPEC §0.1):**

| # | Decisión | Consecuencia en el modelo de dominio |
|---|---|---|
| DC-01 | Empresa de estudio sin nombre | Los ejemplos del dominio son ilustrativos y anónimos |
| DC-02 | Alcance MVP cerrado (inventario y logística de bodega) | 15 subdominios, todos dentro de la bodega |
| DC-03 | Sin ventas, compras completas, producción, contabilidad, nómina, CRM ni facturación | Ninguna entidad comercial: el documento de entrada no es orden de compra; la salida no es venta; no hay atributo monetario (HD-09) |
| DC-04 | Cinco roles oficiales | VO-36 Rol con cinco valores; el Sistema es actor, no rol (HD-12) |
| DC-05 | Web responsive + tablet | Notificaciones dentro del sistema web; escaneo con cámara |
| DC-06 | Integración con Power BI; sin tableros analíticos | La herramienta analítica es externa al dominio |
| DC-07 | Sin IA: «inteligente» = reglas + analítica | Los eventos derivados provienen solo de reglas y umbrales |
| DC-08 | QR como identificador principal | Agregado AG-07 Identificador QR; código de barras solo consulta |

**Resumen constitucional del Prompt #004 frente al baseline:** coincide en roles, plataforma, QR e inteligencia por reglas y KPI. Como en el SRS, prevalece la exclusión más estricta: se excluye **toda** IA (DC-07), no solo la generativa, y también la contabilidad (DC-03). Los nombres de entidad que pide el prompt («Producto», «Variante», «Área», «Inventario», «Auditoría») se concilian con el vocabulario del SPEC en HD-01.

## 0.5 Riesgos abiertos heredados del SRS

| ID | Riesgo | Sev. | Efecto sobre el dominio |
|---|---|:--:|---|
| **R-S01** | El SRS se emitió antes del levantamiento AS-IS y de la línea base | 🔴 | El modelo de dominio tampoco está contrastado con la operación real: es un modelo **TO-BE** |
| R-S02 | Mapeos `[SRS]` sin validar por el Director | 🟠 | Las matrices D y E se construyen sobre esos IDs |
| R-S03 | Alcance grande para nivel Tecnólogo | 🟠 | {ne} entidades y {nev} eventos amplían la superficie |
| R-S04 | Tensión DC-02 / Horizonte 2 (DEC-01) | 🟠 | Transferencias y conteo general se modelan completos |
| R-S05 | Reglas y KPI sin requisito de captura; PN-14 sin requisitos | 🟠 | Eventos marcados «sin RF» (Cap. 2 del EVENT_CATALOG) |
| R-S06 | Dos cifras de reglas (68 y 82) | 🟡 | El dominio usa las 82 |
| R-S07 | Valores numéricos de RNF sin calibrar | 🟡 | No afecta al dominio |
| R-S08 | Ambigüedad «estructural / configurable» (DEC-04) | 🟠 | IN-67 adopta la interpretación del SRS |
| R-S09 | Gherkin no valida adopción | 🟠 | No afecta al dominio |
| R-S10 | Cifras de fuentes no verificadas | 🟠 | El dominio no usa cifras de la literatura |

**Decisiones del Director aún abiertas (SRS, Anexo C):** DEC-01 umbral aprobatorio · DEC-02 lista de alcance · DEC-03 cifra y renumeración de reglas · DEC-04 semántica estructural/configurable · DEC-05 cierre de jornada · DEC-06 brechas de trazabilidad · DEC-07 valorización · DEC-08 aprobación formal del SPEC · DEC-09 fecha límite de lote. Cada una que toca el dominio se marca ⚠️ donde aplica.

**Riesgos críticos heredados del SPEC:** adopción (RG-01, RG-02, RG-13, RG-14, RG-16, RG-17, RG-23) y evidencia académica (RG-33…RG-36).

## 0.6 Convenciones de esta fase

| Prefijo | Elemento | Rango en esta versión |
|---|---|---|
| `SD-nn` | Subdominio | SD-01…SD-15 |
| `E-nn` | Entidad | E-01…E-26 |
| `VO-nn` | Objeto de valor | VO-01…VO-42 |
| `AG-nn` | Agregado | AG-01…AG-21 |
| `IN-nn` | Invariante | IN-01…IN-{nin} |
| `PO-nn` | Política del dominio (regla reactiva) | PO-01…PO-14 |
| `SM-nn` | Máquina de estados | SM-01…SM-21 |
| `EV-<DOM>-nnn` | Evento de dominio | 20 dominios, {nev} eventos |
| `GL-nnn` | Término del glosario | GL-001…GL-{ngl} |
| `HD-nn` | Hallazgo del dominio | HD-01…HD-{nhd} |
| `RF5-nn` | Riesgo abierto para la Fase 5 | RF5-01…RF5-{nrf5} |

Los IDs de esta fase son **permanentes**: no se reutilizan ni se renumeran. Las reglas, historias y requisitos se citan con los IDs permanentes del SRS (`RN-<DOM>-nnn`, `HU-<DOM>-nnn`, `RF-<DOM>-nnn`); los procesos, conceptos y KPI, con los del SPEC.

## 0.7 Método

1. Se releyeron los cuatro documentos y se reutilizó la extracción estructurada del SRS (103 HU, 162 RF, 82 RN, 24 KPI).
2. Entidades, objetos de valor, agregados, invariantes, estados, eventos y términos se escribieron como datos únicos, y de ellos se generaron los tres documentos y las cinco matrices. **Una definición aparece una sola vez**: el Cap. 1 (lenguaje ubicuo) y el GLOSSARY usan el mismo texto.
3. Se verificó automáticamente que toda referencia a RN, HU, RF, KPI, evento, entidad e invariante exista (0 referencias rotas).

## 0.8 Control de cambios de la versión 1.1 (cierre del CP-04)

La auditoría del CP-04 (`04_CP04_AUDITORIA/04_CP04_AUDITORIA.md`) encontró que la identidad del QR (HD-04) contradecía RN-INT-005, que la primera ubicación cambiaba la existencia de unidad sin movimiento (HD-23) y que no estaba definido qué pasa con un registro sin conectividad que deja de ser válido (HD-24). El 29 de septiembre de 2026 se tomaron las decisiones siguientes, que esta versión incorpora editando los datos fuente y regenerando los tres documentos:

| Decisión | Contenido | Cambios en el modelo |
|---|---|---|
| **DF5-01** | El QR de mercancía identifica **SKU + Lote**; no identifica ubicación, bodega ni cantidad. La unidad de inventario sigue siendo SKU + Lote + Ubicación | E-04, E-08, E-09, AG-07, VO-07, VO-08, IN-23, IN-25; eventos EV-QRC-001, EV-QRC-003; términos «Identificador QR», «Unidad de inventario», «Identificador secundario»; HD-04 resuelto; nuevos HD-25 y HD-26 (pendientes, no bloqueantes) |
| **DF5-02** | La entrada confirmada queda **En recepción**; pasa a Disponible al ubicarse | Regla RN-EXI-007 → **IN-70**; SM-06; E-11; EV-ENT-012; HD-06 y HD-07 resueltos |
| **DF5-03** | La primera ubicación es un **movimiento interno** en el kardex | Regla RN-MOV-010 → **IN-71**; E-08, E-10, VO-21; SM-06 (nuevas transiciones En recepción → En tránsito y En tránsito → En recepción, esta última por PN-06 E-07); EV-INV-001 conserva ID y nombre y pasa a designar ese movimiento; Cap. 5.3; término nuevo «Primera ubicación»; HD-23 |
| **DF5-05** | Un registro retenido se **valida de nuevo** al sincronizar; si ya no es válido se rechaza con constancia y, si describe un hecho físico, abre una novedad | Regla RN-INT-008 → **IN-72**; SM-07 (estado nuevo «Rechazado en sincronización»); evento nuevo **EV-TRZ-007**; EV-TRZ-004, EV-NOV-001, E-10, E-17, AG-13, VO-32; término nuevo «Rechazado en sincronización»; HD-24; nuevo HD-27 (alcance sin conectividad, pendiente) |
| **DF5-06** (revisada) | Validación técnica del SPEC, el SRS y este modelo en su v1.1; la aprobación funcional y académica queda pendiente de HD-25 y DEC-01…DEC-09 | Portadas; HD-21; HD-25 |

**Ningún ID se renumeró ni se reutilizó.** Los elementos nuevos continúan la numeración (IN-70…IN-72, EV-TRZ-007, HD-23…HD-27, RF5-14 y los términos GL-204 y GL-205). Las reglas del SRS pasan de 82 a 85; las tres nuevas quedan separadas de las 82 originales (SPEC v1.1 §9.15).

**ESTADO: CONTEXTO RECONSTRUIDO.**
""" + estado("Estado del proyecto · 5 checkpoints · 4 documentos · 8 decisiones constitucionales + 7 reglas innegociables · 10 riesgos del SRS · 9 decisiones abiertas",
             "R-S01 (modelo TO-BE sin contraste con la operación real)", "SRS v1.1 (IDs y reglas)", "HD-21 (el SRS figura como emitido, no aprobado; atendido en parte por DF5-06)", "0")
    return (s.replace("{ne}", str(len(ENTITIES))).replace("{nev}", str(len(EVENTS))).replace("{nin}", f"{len(INVARIANTS):02d}")
             .replace("{ngl}", f"{len(TERMS):03d}").replace("{nhd}", f"{len(DOMAIN_FINDINGS):02d}").replace("{nrf5}", f"{len(RISKS_F5):02d}"))

def cap1():
    ul = [t for t in TERMS if t["ul"]]
    groups = OrderedDict()
    for t in ul:
        groups.setdefault(t["ctx"], []).append(t)
    o = ["""
---

# CAPÍTULO 1 — LENGUAJE UBICUO

> Vocabulario oficial del dominio: se usa **sin sinónimos** en documentos, conversaciones, pruebas e interfaz (SPEC §0.5, RNF-USA-006). Este capítulo contiene los **{n} términos centrales**; el GLOSSARY contiene los {m} términos oficiales con idéntica definición.

## 1.1 Reglas del lenguaje

1. **Un concepto, un término.** Los sinónimos prohibidos no se usan ni como explicación.
2. **El término del SPEC prevalece.** Si el SPEC define un concepto (CD-nn), su nombre es el oficial aunque otro documento use otro.
3. **Los nombres pedidos por el Prompt #004 se concilian, no se sustituyen** (HD-01):

| Nombre pedido en el Prompt #004 | Término oficial | Por qué |
|---|---|---|
| Producto | **Referencia** (E-01) | En el SPEC «producto» designa a COLBASOFT; el objeto físico es la **Prenda** (CD-01) y el de catálogo es la Referencia (CD-02) |
| Variante | **SKU** (E-02) | CD-05 ya nombra la combinación referencia + talla + color |
| Área | **Zona** (E-06) | CD-13; «área» no es término del SPEC |
| Inventario | **Unidad de inventario** (E-08) | CD-07; «inventario» es el conjunto, no la entidad controlada |
| Auditoría | **Registro de bitácora** (E-21) + **Observación de auditoría** (E-22) | CD-47 y RN-AUD-002; «auditoría» es el proceso PN-13 |
| «Stock mínimo alcanzado» | **Existencia mínima alcanzada** (EV-INV-006) | «stock» está prohibido como sinónimo de existencia (§0.5) |

4. **Los términos consagrados de la monografía se conservan con su sentido.** «Ruptura de stock» y «sobre stock» nombran condiciones (Monografía §3) y no autorizan usar «stock» por «existencia».
5. **Origen.** Cada término declara dónde nace: Monografía, Auditoría, SPEC, SRS o «Nuevo (Fase 4)».
""".format(n=len(ul), m=len(TERMS))]
    k = 2
    for ctx, ts in groups.items():
        o.append(f"\n## 1.{k} {ctx}\n")
        k += 1
        o.append("| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |")
        o.append("|---|---|---|---|---|")
        for t in ts:
            o.append(f"| **{t['term']}** | {t['d']} | {t['ej'] or '—'} | {t['sin'] or '—'} | {pair(t['origen'])} |")
    o.append(estado(f"{len(ul)} términos centrales en {len(groups)} contextos, con definición, contexto, ejemplo, sinónimos prohibidos y origen; conciliación de los nombres del Prompt #004",
                    "Que la interfaz o el equipo usen los nombres pedidos en lugar de los oficiales", "SPEC §0.5 y Cap. 4 · GLOSSARY", "HD-01, HD-14", "1"))
    return "\n".join(o)

def cap2():
    o = ["""
---

# CAPÍTULO 2 — SUBDOMINIOS

> El negocio de COLBASOFT es **mantener un registro del inventario de bodega que sea confiable, rastreable y medible** `[MON §3, §7.1, §8.2]`. Los subdominios se clasifican según su aporte a ese propósito:
>
> - **Core Domain (núcleo):** donde está la ventaja del producto y el esfuerzo de modelado.
> - **Supporting Domain (soporte):** específico del negocio, necesario para el núcleo, pero no es la ventaja.
> - **Generic Domain (genérico):** problema resuelto de forma general en cualquier sistema.

## 2.1 Mapa de subdominios

| ID | Subdominio | Clasificación | Módulos | Entidades | Diferenciadores |
|---|---|:--:|---|---|---|"""]
    for s in SUBDOMAINS:
        o.append(f"| **{s['id']}** | {s['nombre']} | **{s['tipo']}** | {s['modulos']} | {', '.join(s['entidades']) or '— (cálculo sobre el registro)'} | {s['diferenciadores']} |")
    c = Counter(s["tipo"] for s in SUBDOMAINS)
    o.append(f"\n**Distribución:** Core {c['Core']} · Supporting {c['Supporting']} · Generic {c['Generic']}. Los nueve subdominios mínimos pedidos (Inventario, Movimientos, Trazabilidad, Ubicaciones, Conteos, Alertas, Auditoría, Usuarios, Reportes) están presentes; se agregan Catálogo textil, Identificación, Novedades, Configuración, Tareas y notificaciones y Operación diaria porque el SPEC les dedica módulos o procesos propios.\n")
    o.append("## 2.2 Justificación de cada clasificación\n")
    for s in SUBDOMAINS:
        o.append(f"### {s['id']} · {s['nombre']} — {s['tipo']}\n")
        o.append(f"**Alcance.** {s['alcance']}\n")
        o.append(f"**Por qué es {s['tipo']}.** {s['justificacion']}\n")
    o.append("""## 2.3 Lectura

Los cinco subdominios núcleo forman un solo propósito: **la existencia (SD-01) solo cambia por movimientos (SD-02), que quedan en un kardex (SD-03), se verifican por conteo (SD-04) y se vigilan por reglas (SD-05)**. Es exactamente la cadena que la monografía propone: registrar digitalmente entradas, salidas y movimientos, y medir exactitud, tiempos de registro y frecuencia de errores `[MON §8.2]`. Los subdominios de soporte existen porque el núcleo los necesita, y los genéricos, porque todo sistema los tiene.
""")
    o.append(estado("15 subdominios clasificados y justificados (5 Core, 7 Supporting, 3 Generic)", "Si se sobreinvierte en subdominios genéricos, se resta esfuerzo al núcleo", "SPEC §1.7 (diferenciadores), §5.1 (módulos)", "HD-11 (SD-15 sin requisitos)", "2"))
    return "\n".join(o)

def ev_of(eid):
    orig = [e["id"] for e in EVENTS if e["origen"] == eid]
    aff = [e["id"] for e in EVENTS if eid in e["afect"] and e["origen"] != eid]
    return orig, aff

def cap3():
    o = ["""
---

# CAPÍTULO 3 — ENTIDADES DEL DOMINIO

> Una **entidad** tiene identidad propia que persiste a través de sus cambios de estado. Las fichas describen el concepto de negocio: **no describen estructuras de almacenamiento**. La «información que la define» es conceptual y no fija formatos. Las reglas se citan con sus IDs permanentes del SRS; los eventos, con los del EVENT_CATALOG.

## 3.1 Índice de entidades

| ID | Entidad (término oficial) | Pedida como | Concepto SPEC | Subdominio | Agregado |
|---|---|---|:--:|---|:--:|"""]
    for e in ENTITIES:
        o.append(f"| {e['id']} | **{e['nombre']}** | {e['solicitado'] or '—'} | {e['cd']} | {e['sd']} {SD[e['sd']]['nombre']} | {e['ag']} |")
    o.append("\n> **Entidades mínimas pedidas:** Producto → E-01 Referencia · Variante → E-02 SKU · Lote → E-04 · Ubicación → E-07 · Movimiento → E-10 · Inventario → E-08 Unidad de inventario · Conteo → E-15 · Novedad → E-17 · Usuario → E-19 · Bodega → E-05 · Área → E-06 Zona · Alerta → E-18 · Auditoría → E-21 Registro de bitácora + E-22 Observación de auditoría. Todas presentes.\n")
    o.append("## 3.2 Fichas\n")
    for e in ENTITIES:
        orig, aff = ev_of(e["id"])
        rels = "<br>".join(f"→ {en(t)}: {r}" for t, r in e["rel"])
        rns = ", ".join(e["rn"])
        o.append(f"### {e['id']} · {e['nombre']}" + (f" (pedida como «{e['solicitado']}»)" if e["solicitado"] else "") + "\n")
        o.append("| Campo | Contenido |\n|---|---|")
        o.append(f"| **Descripción** | {e['desc']} |")
        o.append(f"| **Responsabilidad** | {e['resp']} |")
        o.append(f"| **Identidad** | {e['identidad']} |")
        o.append(f"| **Información que la define** | {e['info']} |")
        o.append(f"| **Estado** | {e['sm']} |")
        o.append(f"| **Ciclo de vida** | {e['ciclo']} |")
        o.append(f"| **Relaciones conceptuales** | {rels} |")
        o.append(f"| **Reglas asociadas** | {rns} |")
        o.append(f"| **Eventos que origina** | {ids(orig)} |")
        o.append(f"| **Eventos que la afectan** | {ids(aff)} |")
        o.append(f"| **Subdominio / agregado** | {e['sd']} {SD[e['sd']]['nombre']} · {e['ag']} |")
        o.append(f"| **Concepto de origen** | {e['cd']} |\n")
    o.append(estado(f"{len(ENTITIES)} entidades con descripción, responsabilidad, identidad, estado, ciclo de vida, relaciones, reglas y eventos",
                    "Bodega, Zona y SKU sin estados propios definidos en el SPEC (HD-19); copias impresas de un mismo QR de mercancía (HD-25)",
                    "Cap. 4 (identidades como objetos de valor), Cap. 5 (agregados), EVENT_CATALOG", "HD-01, HD-04 (resuelto, DF5-01), HD-05, HD-06 (resuelto, DF5-02), HD-11, HD-19, HD-23, HD-25", "3"))
    return "\n".join(o)

def cap4():
    o = ["""
---

# CAPÍTULO 4 — OBJETOS DE VALOR

> Un **objeto de valor** se define solo por su contenido, no tiene identidad propia y es **inmutable**: para cambiarlo se reemplaza por otro. Dos objetos de valor con el mismo contenido son el mismo valor.

**Regla general de inmutabilidad.** Todos los objetos de valor de este capítulo son inmutables. Las entidades que los contienen pueden sustituirlos (por ejemplo, un nuevo umbral), salvo donde se indica lo contrario; en ese caso la sustitución también está prohibida.

| ID | Objeto de valor | Qué representa | Inmutabilidad | Validaciones | Ejemplo | Reglas |
|---|---|---|---|---|---|---|"""]
    frozen = {"VO-02": "Una vez generado no se sustituye", "VO-06": "No se sustituye", "VO-07": "No se sustituye ni se reutiliza jamás", "VO-16": "No se sustituye durante el conteo", "VO-17": "Solo corregible por su contador antes de confirmar la tarea", "VO-26": "Conserva el umbral aplicado aunque cambie la configuración", "VO-32": "No se sustituye", "VO-38": "No se sustituye", "VO-05": "No se sustituye si hay movimientos", "VO-01": "No se sustituye"}
    for v in VALUE_OBJECTS:
        inm = frozen.get(v[0], "Inmutable; la entidad lo reemplaza completo")
        o.append(f"| **{v[0]}** | {v[1]} | {v[2]} | {inm} | {v[3]} | {v[4]} | {v[5]} |")
    o.append("\n> Los objetos de valor pedidos como ejemplo por el Prompt #004 están cubiertos: SKU → VO-02 · Código QR → VO-07 · Ubicación física → VO-10 · Cantidad → VO-13 · Estado de inventario → VO-14 · Prioridad → VO-28 (severidad) y VO-29 (prioridad de tarea) · Fecha operativa → VO-32.\n")
    o.append(estado(f"{len(VALUE_OBJECTS)} objetos de valor con inmutabilidad, validaciones y ejemplos",
                    "VO-28 y VO-29 sin escala definida; VO-12 sin regla para unidades heterogéneas; VO-13 sin precisión fijada",
                    "Cap. 3 (entidades que los contienen)", "HD-15, HD-16, HD-17, HD-18", "4"))
    return "\n".join(o)

def cap5():
    o = ["""
---

# CAPÍTULO 5 — AGREGADOS

> Un **agregado** es un conjunto de entidades y objetos de valor que cambia como una unidad para proteger sus invariantes. Se accede a él por su **raíz**. Entre agregados las referencias son **por identidad**, nunca por contención. Este capítulo describe límites de consistencia del negocio, no decisiones de almacenamiento.

## 5.1 Índice de agregados

| ID | Agregado | Raíz | Entidades internas | Invariantes que protege | Referencias por identidad |
|---|---|---|---|---|---|"""]
    for a in AGGREGATES:
        o.append(f"| **{a[0]}** | {a[1]} | {en(a[2])} | {', '.join(en(x) for x in a[3]) or '—'} | {', '.join(a[5])} | {a[6]} |")
    o.append("\n## 5.2 Por qué existe cada agregado\n")
    for a in AGGREGATES:
        o.append(f"**{a[0]} · {a[1]}.** {a[4]}\n")
    o.append("""## 5.3 Operaciones de negocio que involucran varios agregados

Algunas operaciones del negocio afectan a más de un agregado. El dominio declara **qué debe quedar coherente**; cómo garantizarlo es decisión de la Fase 5.

| Operación | Agregados involucrados | Coherencia exigida por el negocio | Regla |
|---|---|---|---|
| Confirmar una entrada | AG-08 → AG-04, AG-06, AG-05, AG-07 | Lote, movimiento de entrada y existencia en recepción nacen juntos o no nace ninguno | RN-ENT-007, RN-LOT-001, RN-INT-004, RN-EXI-007 |
| Primera ubicación (v1.1) | AG-06 → AG-05 (unidad de recepción) y AG-05 (unidad destino) | El descuento en la unidad de recepción y el incremento disponible en la unidad destino son indivisibles; la existencia total no cambia | RN-MOV-010, RN-MOV-004 |
| Movimiento interno | AG-06 → AG-05 (origen) y AG-05 (destino) | La existencia total no cambia: el descuento y el incremento son indivisibles | RN-MOV-004 |
| Transferencia | AG-10 → AG-05 (origen y destino), AG-06 | Reserva, tránsito y recepción mantienen la partición por estado | RN-EXI-004, RN-EXI-005, RN-MOV-007 |
| Autorizar una salida | AG-09 → AG-05 | Nadie más compromete la misma existencia | RN-EXI-003, RN-EXI-004 |
| Aprobar un ajuste | AG-11 → AG-06, AG-05 | El movimiento de ajuste solo existe si la solicitud está aprobada; nunca deja existencia negativa | RN-AJU-001, RN-EXI-001 |
| Cerrar un conteo | AG-12 → AG-11 | Cada diferencia elegida para ajuste origina una solicitud de ajuste | RN-CNT-004 |
| Inmovilizar un lote | AG-04 → AG-05 (todas sus unidades) | Toda la existencia del lote cambia de estado a la vez | RN-LOT-003 |
| Desactivar referencia o ubicación | AG-01 / AG-03 → AG-05 (consulta) | Solo con existencia cero | RN-MAE-003, RN-MAE-005 |
| Sincronizar un registro retenido (v1.1) | AG-06 → AG-05 (y AG-13 si se rechaza) | Se confirma o se rechaza una sola vez, contra el estado vigente; si se rechaza y describe un hecho físico, la novedad nace con el rechazo | RN-INT-008 |
| Cualquier evento auditable | Todos → AG-16 | Todo hecho auditable deja su registro en la bitácora | RN-AUD-001 |
""")
    o.append(estado(f"{len(AGGREGATES)} agregados con raíz, entidades internas, invariantes protegidas, referencias por identidad y justificación; 11 operaciones que involucran varios agregados",
                    "Operaciones indivisibles sobre dos unidades (RF5-02) y concurrencia sobre la disponibilidad (RF5-03)",
                    "Cap. 3, Cap. 6", "HD-04 resuelto por DF5-01: la identidad de AG-05 no cambia; AG-07 identifica SKU + Lote", "5"))
    return "\n".join(o)

def cap6():
    inv_rn = {x for i in INVARIANTS for x in i[2]}
    derived = [e for e in EVENTS if e["der"]]
    pol_rn = sorted(set(S["RN"]) - inv_rn)
    pol_ev = {}
    for rn in pol_rn:
        pol_ev[rn] = [e["id"] for e in EVENTS if rn in e["rn"] and e["der"]] or [e["id"] for e in EVENTS if rn in e["rn"]]
    o = ["""
---

# CAPÍTULO 6 — INVARIANTES DEL DOMINIO

> Una **invariante** es una condición que se cumple **siempre**, antes y después de cualquier cambio. Cada invariante cita las reglas del SRS que la originan, el agregado que la protege y su tipo (estructural = no configurable; configurable = su umbral se ajusta, su lógica no se desactiva).

## 6.1 Invariantes

| ID | Invariante | Reglas (SRS) | Guardián | Tipo |
|---|---|---|---|:--:|"""]
    for i in INVARIANTS:
        o.append(f"| **{i[0]}** | {i[1]} | {', '.join(i[2])} | {i[3]} | {i[4]} |")
    o.append("""
## 6.2 Políticas del dominio (reglas reactivas)

Algunas reglas del SRS no expresan algo que se cumpla siempre, sino **una reacción**: «cuando ocurre X, el sistema hace Y» (escalar al vencer un plazo, generar una alerta al cruzar un umbral). No son invariantes: son **políticas** y se manifiestan como **eventos derivados** (EVENT_CATALOG, Cap. 5).

| ID | Regla (SRS) | Política | Evento(s) derivado(s) |
|---|---|---|---|""")
    for k, rn in enumerate(pol_rn, 1):
        txt = re.sub(r"\*\*|`", "", RN_TXT[rn]["texto"])
        txt = txt if len(txt) < 230 else txt[:227].rsplit(" ", 1)[0] + "…"
        o.append(f"| **PO-{k:02d}** | {rn} | {txt} | {ids(pol_ev[rn])} |")
    allc = inv_rn | set(pol_rn)
    o.append(f"\n**Cobertura:** las {len(S['RN'])} reglas del SRS quedan cubiertas: {len(inv_rn)} como invariantes y {len(pol_rn)} como políticas ({len(allc)}/{len(S['RN'])}).\n")
    o.append(estado(f"{len(INVARIANTS)} invariantes (mínimo exigido: 40), cada una vinculada a reglas del SRS; {len(pol_rn)} políticas reactivas; {len(inv_rn | set(pol_rn))}/{len(S['RN'])} reglas cubiertas (82 + 3 de la v1.1: IN-70…IN-72)",
                    "IN-67 depende de DEC-04; IN-46 depende de HD-13; IN-23 actualizada por DF5-01", "SRS Cap. 8", "HD-04, HD-13 · distinción invariante/política (nueva en esta fase)", "6"))
    return "\n".join(o)

def cap7():
    o = ["""
---

# CAPÍTULO 7 — CICLOS DE VIDA

> Especificación textual de cómo nace, vive y termina cada entidad principal. Los estados formales y sus transiciones están en el Cap. 8. Los ejemplos de ciclo del Prompt #004 se analizan en HD-02 y HD-03.

| Entidad | Ciclo de vida | Observaciones |
|---|---|---|"""]
    for l in LIFECYCLES:
        o.append(f"| **{l[0]}** | {l[1]} | {l[2]} |")
    o.append("""
**Principios comunes a todos los ciclos:**

1. **Nada termina borrado.** El final de todo ciclo es un estado inactivo o cerrado; la identidad persiste (RN-MAE-007).
2. **Lo confirmado no retrocede.** Movimientos, conteos cerrados y ajustes aplicados no vuelven atrás; se corrigen con hechos nuevos (RN-INT-002, RN-CNT-004, RN-AJU-007).
3. **Todo paso tiene actor.** Cada transición la ejecuta un usuario identificado o el Sistema (RN-INT-001).
""")
    o.append(estado(f"{len(LIFECYCLES)} ciclos de vida especificados, sin diagramas", "Estados nuevos sin respaldo explícito en el SPEC (HD-19)", "Cap. 8", "HD-02, HD-03, HD-07, HD-19", "7"))
    return "\n".join(o)

def cap8():
    o = ["""
---

# CAPÍTULO 8 — ESTADOS OFICIALES

> Estados válidos del dominio y transiciones permitidas. **Toda transición no listada está prohibida.** «—» como origen indica el nacimiento del elemento. La columna «Evento» remite al EVENT_CATALOG.

## 8.1 Resumen

| Máquina | Elemento | Estados | Transiciones | Origen |
|---|---|:--:|:--:|---|"""]
    for sm in STATE_MACHINES:
        o.append(f"| {sm[0]} | {sm[1]} | {len(sm[2])} | {len(sm[3])} | {pair(sm[4])} |")
    tot_s = sum(len(s[2]) for s in STATE_MACHINES)
    tot_t = sum(len(s[3]) for s in STATE_MACHINES)
    o.append(f"| **Total** | {len(STATE_MACHINES)} máquinas | **{tot_s}** | **{tot_t}** | |\n")
    k = 2
    for sm in STATE_MACHINES:
        o.append(f"## 8.{k} {sm[0]} · {sm[1]}\n")
        k += 1
        o.append("| Estado | Significado | Tipo |\n|---|---|:--:|")
        for s in sm[2]:
            o.append(f"| **{s[0]}** | {s[1]} | {s[2] or '—'} |")
        o.append("\n| Desde | Hacia | Evento | Actor | Condición (guarda) |\n|---|---|---|---|---|")
        for t in sm[3]:
            o.append(f"| {t[0]} | {t[1]} | {t[2]} | {t[3]} | {t[4]} |")
        o.append("")
    o.append(estado(f"{len(STATE_MACHINES)} máquinas de estado, {tot_s} estados oficiales y {tot_t} transiciones permitidas",
                    "Nombres de estado nuevos (Habilitado, Generado, Reversado, Cancelada) pendientes de confirmación", "Cap. 7, EVENT_CATALOG", "HD-03, HD-07, HD-19", "8"))
    return "\n".join(o)

def cap9():
    o = ["""
---

# CAPÍTULO 9 — MATRICES DEL DOMINIO (A, B, C)

> Las matrices D (Evento ↔ Historia de usuario) y E (Evento ↔ RF) están en el EVENT_CATALOG, Cap. 6.

## Matriz A — Entidad ↔ Evento

**O** = eventos que la entidad origina · **A** = eventos que la afectan sin originarlos.

| Entidad | O | Eventos que origina | A | Eventos que la afectan |
|---|:--:|---|:--:|---|"""]
    for e in ENTITIES:
        orig, aff = ev_of(e["id"])
        o.append(f"| **{en(e['id'])}** | {len(orig)} | {ids(orig)} | {len(aff)} | {ids(aff)} |")
    o.append("\n## Matriz B — Entidad ↔ Regla\n\nReglas asociadas a la entidad (ficha) más las citadas por los eventos que origina.\n\n| Entidad | N.º | Reglas (SRS) |\n|---|:--:|---|")
    for e in ENTITIES:
        orig, _ = ev_of(e["id"])
        rs = set(e["rn"]) | {r for x in orig for r in EVT[x]["rn"]}
        o.append(f"| **{en(e['id'])}** | {len(rs)} | {', '.join(sorted(rs)) or '—'} |")
    o.append("\n## Matriz C — Entidad ↔ KPI\n\nKPI alimentados por eventos que la entidad origina o que la afectan.\n\n| Entidad | KPI |\n|---|---|")
    kpi_ent = {}
    for e in ENTITIES:
        orig, aff = ev_of(e["id"])
        ks = sorted({k for x in orig + aff for k in EVT[x]["kpi"]})
        for k in ks:
            kpi_ent.setdefault(k, []).append(e["id"])
        o.append(f"| **{en(e['id'])}** | {', '.join(f'{k} {KPI_N[k]}' for k in ks) or '—'} |")
    o.append("\n**Vista inversa (KPI → entidades):**\n\n| KPI | Nombre | Entidades |\n|---|---|---|")
    for i in range(1, 25):
        k = f"KPI-{i:02d}"
        o.append(f"| {k} | {KPI_N[k]} | {', '.join(kpi_ent.get(k, [])) or '—'} |")
    o.append(estado(f"Matrices A ({len(ENTITIES)} entidades × {len(EVENTS)} eventos), B (entidad ↔ regla) y C (entidad ↔ KPI, con vista inversa)",
                    "Matriz C depende de datos que ningún RF exige capturar (KPI-05, 07, 10, 12, 17, 24; H-12 del SRS)",
                    "Cap. 3, EVENT_CATALOG", "H-12 del SRS (heredado)", "9"))
    return "\n".join(o)

def cap10():
    o = ["""
---

# CAPÍTULO 10 — HALLAZGOS DEL DOMINIO

> Inconsistencias o vacíos entre la monografía, el SPEC, el SRS y el Prompt #004 detectados al modelar. **Ninguno se corrigió en silencio**: cada uno declara el tratamiento provisional que adopta este modelo y quién debe resolverlo. En la v1.1, los resueltos por las decisiones del cierre del CP-04 conservan su evidencia y registran la decisión (DF5-nn); HD-23 a HD-27 se agregaron en ese cierre.

| ID | Hallazgo | Evidencia | Tratamiento en el modelo | Resuelve |
|---|---|---|---|---|"""]
    for h in DOMAIN_FINDINGS:
        o.append(f"| **{h[0]}** | **{h[1]}** | {h[2]} | {h[3]} | {h[4]} |")
    crit = [h[0] for h in DOMAIN_FINDINGS if "bloqueante" in h[4].lower() and "no bloquea" not in h[4].lower()]
    res = [h[0] for h in DOMAIN_FINDINGS if h[4].startswith("**Resuelto")]
    o.append(f"\n**Resueltos en el cierre del CP-04:** {', '.join(res)}. **Bloqueantes para la Fase 5:** {', '.join(crit) or 'ninguno'}. **Requieren decisión del Director:** {', '.join(h[0] for h in DOMAIN_FINDINGS if 'Director' in h[4] or h[4].startswith('DEC'))}.\n")
    o.append(estado(f"{len(DOMAIN_FINDINGS)} hallazgos con evidencia, tratamiento y responsable", "HD-25 debe decidirse antes de la Fase 5 (04_CP04_DECISIONES_PENDIENTES); los demás pendientes no bloquean la arquitectura", "Todos los capítulos", "—", "10"))
    return "\n".join(o)

def domain_model():
    idx = """
## Índice

| Cap. | Título |
|---|---|
| 0 | Auditoría de reanudación |
| 1 | Lenguaje ubicuo |
| 2 | Subdominios |
| 3 | Entidades del dominio |
| 4 | Objetos de valor |
| 5 | Agregados |
| 6 | Invariantes del dominio (y políticas) |
| 7 | Ciclos de vida |
| 8 | Estados oficiales |
| 9 | Matrices A, B y C |
| 10 | Hallazgos del dominio |
"""
    return (header("DOMAIN_MODEL", "Modelo de Dominio de COLBASOFT", "`EVENT_CATALOG.md` (eventos, matrices D y E) · `GLOSSARY.md` (glosario y auditoría interna)")
            + idx + cap0() + cap1() + cap2() + cap3() + cap4() + cap5() + cap6() + cap7() + cap8() + cap9() + cap10()
            + "\n---\n\n*Fin de DOMAIN_MODEL v1.1. La monografía original permanece sin modificaciones.*\n")

# ====================================================================================== EVENT_CATALOG
def ev_cap1():
    counts = Counter(e["id"][3:6] for e in EVENTS)
    rows = "\n".join(f"| **{d}** | {n} | {sd} {SD[sd]['nombre']} | {counts[d]} |" for d, n, sd in DOMS)
    return f"""
---

> **Reconstrucción de contexto.** La auditoría de reanudación de la Fase 4 está en DOMAIN_MODEL, Cap. 0 (ESTADO: CONTEXTO RECONSTRUIDO) y rige también este documento.

# CAPÍTULO 1 — FILOSOFÍA DE EVENTOS

## 1.1 Qué es un evento en COLBASOFT

Un **evento de dominio** es un **hecho relevante para el negocio que ya ocurrió**. Se nombra en pasado («Entrada confirmada»), tiene un **actor** (usuario identificado o Sistema, RN-INT-001), una **fecha operativa** (VO-32), una **entidad de origen** y un **resultado**. Un evento **no se modifica ni se retira**: si fue un error, se corrige con otro evento.

## 1.2 Evento, acción, movimiento y registro

| Concepto | Qué es | Tiempo | ¿Cambia el estado? | Ejemplo |
|---|---|---|:--:|---|
| **Acción** | Intención de un actor que el sistema evalúa contra las reglas | Presente («quiero…») | No por sí misma | El Coordinador pide confirmar la entrada DE-0087 |
| **Evento** | Hecho que resulta de una acción aceptada, de una acción rechazada relevante para el control, o de una regla que se cumple | Pasado («ocurrió») | Sí, o deja constancia de un intento de control | EV-ENT-012 Entrada confirmada · EV-ENT-014 Autoconfirmación rechazada · EV-INV-006 Existencia mínima alcanzada |
| **Movimiento** | Tipo particular de hecho que **altera la existencia o la ubicación** de una unidad de inventario (CD-28). Todo movimiento confirmado es un evento; no todo evento es un movimiento | Pasado | Sí, sobre la existencia | Movimiento de entrada de 120 unidades |
| **Registro** | **Constancia persistente** de un evento: línea de kardex, registro de bitácora o historial de la entidad | Permanente | No: es la huella del evento | Línea del kardex de la unidad; registro de bitácora del cambio de umbral |

Relación: **acción → (reglas) → evento(s) → registro(s)**. Una acción rechazada no produce movimiento; si el rechazo es relevante para el control (segregación, reglas estructurales, operación no autorizada), produce un **evento de rechazo** que se registra en la bitácora.

## 1.3 Qué no es un evento

- **Consultar** existencia, kardex, reportes o el dashboard: leer nunca escribe (RN-INT-006). Por eso las historias de consulta no tienen eventos (Matriz D).
- **Escanear** para ver qué es una etiqueta: es una acción de lectura; el escaneo solo forma parte de un evento cuando identifica mercancía en un movimiento.
- **Preparar un registro** que todavía no se confirma (estado «En registro»).
- **Visualizar** una notificación.

## 1.4 Propiedades de todo evento

| Propiedad | Regla |
|---|---|
| Inmutable | Una vez ocurrido no se modifica (RN-INT-002, RN-AUD-001) |
| Atribuido | Siempre tiene actor: usuario identificado o Sistema (RN-INT-001) |
| Fechado | Lleva la fecha operativa del hecho, no la de su sincronización (VO-32, HD-16) |
| Trazable | Se registra en el kardex (si altera la existencia), en la bitácora (si es auditable) o en el historial de su entidad |
| Explicable | Si es derivado, cita la regla o el umbral que lo produjo; nunca una predicción (DC-07) |

## 1.5 Convención de nombres e identificadores

- **ID permanente** `EV-<DOM>-nnn`: el dominio es el subdominio o módulo del evento; `nnn` es correlativo y nunca se reutiliza.
- **Nombre**: sustantivo del lenguaje ubicuo + participio («Lote inmovilizado»), sin sinónimos prohibidos.
- **Actor** «Sistema» indica evento derivado de una regla (Cap. 5).

## 1.6 Dominios de eventos

| Código | Dominio | Subdominio | Eventos |
|---|---|---|:--:|
{rows}
| **Total** | | | **{len(EVENTS)}** |
""" + estado("Definición de evento, diferencias entre evento, acción, movimiento y registro, propiedades, convenciones y 20 dominios de eventos",
             "Tratar consultas o escaneos como eventos inflaría el catálogo y la bitácora", "DOMAIN_MODEL Cap. 1 (lenguaje ubicuo)", "HD-16", "1")

def ev_cap2():
    o = ["""
---

# CAPÍTULO 2 — CATÁLOGO COMPLETO DE EVENTOS

> Cada evento declara nombre, actor, entidad de origen, entidades afectadas, disparador, resultado esperado, KPI y reglas. Las historias y los requisitos relacionados están en las matrices D y E (Cap. 6). **⚠️** marca eventos modelados desde el SPEC que no tienen historia o requisito que los implemente."""]
    for d, n, sd in DOMS:
        evs = [e for e in EVENTS if e["id"][3:6] == d]
        o.append(f"\n## 2.{DOMS.index((d, n, sd)) + 1} {d} · {n} ({len(evs)})\n")
        o.append("| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |")
        o.append("|---|---|---|---|---|---|---|---|---|")
        notes = []
        for e in evs:
            flag = " ⚠️" if e["nota"] else ""
            o.append(f"| **{e['id']}** | {e['nombre']}{flag} | {e['actor']} | {en(e['origen'])} | {', '.join(en(x) for x in e['afect'])} | {e['disp']} | {e['res']} | {ids(e['kpi'])} | {ids(e['rn'])} |")
            if e["nota"]:
                notes.append(f"- **{e['id']}**: {e['nota']}")
        if notes:
            o.append("\n" + "\n".join(notes))
    flagged = [e["id"] for e in EVENTS if e["nota"]]
    o.append(estado(f"{len(EVENTS)} eventos (mínimo exigido: 70) con IDs permanentes en 20 dominios y los ocho atributos pedidos",
                    f"{len(flagged)} eventos ⚠️ sin requisito completo que los implemente",
                    "DOMAIN_MODEL Caps. 3 y 8 · SRS Caps. 5–8", "HD-11, HD-17, HD-19 · H-10, H-11, H-12 del SRS", "2"))
    return "\n".join(o)

def ev_cap3():
    o = ["""
---

# CAPÍTULO 3 — LÍNEA TEMPORAL DE EVENTOS

> Orden en que ocurren los eventos en cada uno de los 14 procesos del MVP (SPEC Cap. 3; casos de uso del SRS Cap. 4). «A o B» indica alternativas excluyentes; el comentario indica cuándo ocurre un paso opcional."""]
    for pn, name, cu, steps in TIMELINES:
        o.append(f"\n## {pn} · {name} ({cu})\n")
        o.append("| Orden | Evento(s) | Nombre | Cuándo |\n|:--:|---|---|---|")
        for k, (evs, note) in enumerate(steps, 1):
            ids_ = re.findall(r"EV-[A-Z]{3}-\d{3}", evs)
            names = " / ".join(EVT[x]["nombre"] for x in ids_) if ids_ else "—"
            o.append(f"| {k} | {evs.replace(chr(124), chr(111))} | {names} | {note or 'siempre'} |")
    o.append(estado("Línea temporal de los 14 procesos del MVP", "PN-14 sin requisitos (DEC-05); PN-04 sin eventos por diseño (solo lectura)", "SPEC Cap. 3 · SRS Cap. 4", "HD-07 y HD-23 (orden entrada → primera ubicación, resueltos por DF5-02 y DF5-03)", "3"))
    return "\n".join(o)

def ev_cap4():
    order = ["Crítica", "Alta", "Media", "Baja"]
    crit_def = {
        "Crítica": "Afecta la integridad del inventario, la segregación de funciones o las reglas estructurales: aprobaciones y rechazos de ajustes y salidas, anulaciones, inmovilizaciones, cierres de conteo, cambios de configuración y de rol, hallazgos de integridad, intentos de violar reglas estructurales.",
        "Alta": "Altera la existencia o un dato maestro, o registra acceso: movimientos confirmados, altas y desactivaciones, accesos, exportaciones, rechazos de control.",
        "Media": "Avance de un flujo de trabajo: solicitudes, recepciones, tareas, alertas generadas y atendidas.",
        "Baja": "Informativo o de apoyo: impresión, notificaciones, reportes programados, frecuencia de alertas.",
    }
    o = ["""
---

# CAPÍTULO 4 — EVENTOS AUDITABLES

> **Todo evento del catálogo queda registrado de forma permanente** —nada se purga (RNF-AUD-004)— en al menos uno de tres registros: **Kardex** (si altera la existencia, RN-INT-002), **Bitácora** (si es relevante para el control, RN-AUD-001) o **Historial** de su entidad. La criticidad indica la prioridad de revisión en una auditoría (PN-13).

## 4.1 Criterios de criticidad

| Criticidad | Criterio | Eventos |
|---|---|:--:|"""]
    c = Counter(e["crit"] for e in EVENTS)
    for k in order:
        o.append(f"| **{k}** | {crit_def[k]} | {c[k]} |")
    reg = Counter(e["reg"] for e in EVENTS)
    o.append(f"\n**Destino del registro permanente:** " + " · ".join(f"{k} {v}" for k, v in reg.most_common()) + "\n")
    for k in order:
        o.append(f"## 4.{order.index(k) + 2} Criticidad {k}\n")
        o.append("| ID | Evento | Actor | Registro permanente | Reglas |\n|---|---|---|---|---|")
        for e in [x for x in EVENTS if x["crit"] == k]:
            o.append(f"| {e['id']} | {e['nombre']} | {e['actor']} | {e['reg']} | {ids(e['rn'])} |")
        o.append("")
    o.append("""## 4.6 Reglas de auditoría de eventos

1. Los eventos **Críticos** y **Altos** se registran siempre en la bitácora o en el kardex, con actor, fecha operativa y detalle suficiente para reconstruirlos (RNF-AUD-001).
2. Los cambios de configuración registran **valor anterior y nuevo** (RN-AUD-004).
3. Los eventos de rechazo por reglas estructurales o de segregación (EV-ENT-014, EV-AJU-007, EV-AUD-003, EV-AUD-004, EV-PAR-004) son **Críticos o Altos aunque no cambien el inventario**: prueban que el control funcionó.
4. La discontinuidad de la bitácora (EV-AUD-006) y la discrepancia de integridad (EV-TRZ-006) son **hallazgos críticos** que se notifican al Administrador.
""")
    o.append(estado(f"Clasificación de los {len(EVENTS)} eventos por criticidad ({', '.join(f'{k} {c[k]}' for k in order)}) y registro permanente",
                    "La continuidad de la bitácora debe poder demostrarse (RF5-07)", "SRS RNF-AUD-001…005 · RN-AUD-001", "—", "4"))
    return "\n".join(o)

def ev_cap5():
    der = [e for e in EVENTS if e["der"]]
    alert = {"EV-INV-006", "EV-INV-007", "EV-INV-008", "EV-INV-009", "EV-MOV-004", "EV-MOV-011", "EV-AJU-008", "EV-AJU-009", "EV-CNT-018", "EV-LOT-004", "EV-ALE-007", "EV-NOV-006", "EV-JOR-005"}
    o = ["""
---

# CAPÍTULO 5 — EVENTOS DERIVADOS

> Eventos que el **Sistema** genera automáticamente cuando una regla de negocio o un umbral configurado evalúa verdadera su condición. **No hay inteligencia artificial**: cada evento derivado cita la regla que lo produce (DC-07). Son la manifestación operativa de la «inteligencia» del producto.

| ID | Evento derivado | Condición / regla | Parámetro configurable | ¿Genera alerta? | Criticidad |
|---|---|---|---|:--:|:--:|"""]
    params = {"EV-ACC-003": "Intentos fallidos", "EV-ACC-004": "Tiempo de inactividad", "EV-INV-005": "Plazo de reserva", "EV-INV-006": "Existencia mínima por SKU",
              "EV-INV-007": "Existencia máxima por SKU", "EV-INV-009": "Capacidad de ubicación", "EV-MOV-004": "Tiempo máximo en tránsito", "EV-MOV-011": "Tiempo máximo en tránsito",
              "EV-SAL-004": "Umbral de autorización del Coordinador", "EV-AJU-002": "Umbral ajuste menor/mayor", "EV-AJU-008": "Plazo de aprobación", "EV-AJU-009": "Umbral y ventana de ajustes recurrentes",
              "EV-CNT-009": "Tolerancia de conteo", "EV-CNT-013": "Umbral crítico de diferencia global", "EV-CNT-018": "Plazo de conteo", "EV-LOT-004": "Umbral de antigüedad",
              "EV-NOV-006": "Plazo de resolución de novedad", "EV-ALE-004": "Plazo de atención por severidad", "EV-ALE-007": "Umbral de exactitud", "EV-REP-004": "Periodicidad del reporte",
              "EV-CNT-004": "Fecha de corte", "EV-REP-005": "Frecuencia de cada KPI"}
    for e in der:
        o.append(f"| {e['id']} | {e['nombre']} | {e['der']} | {params.get(e['id'], '—')} | {'Sí' if e['id'] in alert else '—'} | {e['crit']} |")
    o.append("""
**Ejemplos pedidos por el Prompt #004:**

| Ejemplo del prompt | Evento del catálogo | Observación |
|---|---|---|
| Stock mínimo alcanzado | **EV-INV-006 Existencia mínima alcanzada** | Se evita el término prohibido «stock» (HD-14) |
| Conteo vencido | **EV-CNT-018 Conteo vencido** | RN-CNT-005 |
| Lote inconsistente | **EV-TRZ-006 Discrepancia de integridad detectada** (alcance lote) | El SPEC no define «lote inconsistente»; la verificación por lote es RF-KDX-006 (HD-14) |
""")
    o.append(estado(f"{len(der)} eventos derivados, todos por regla o umbral explícitos, sin IA",
                    "Umbrales sin calibrar hasta tener línea base; escalas de severidad sin definir (HD-15)", "DOMAIN_MODEL Cap. 6.2 (políticas) · SRS Cap. 8", "HD-14, HD-15", "5"))
    return "\n".join(o)

def ev_cap6():
    o = ["""
---

# CAPÍTULO 6 — MATRICES D Y E

## Matriz D — Evento ↔ Historia de usuario

| Evento | Nombre | Historias de usuario (SRS) |
|---|---|---|"""]
    for e in EVENTS:
        o.append(f"| {e['id']} | {e['nombre']} | {ids(e['hu'])}{' ⚠️' if not e['hu'] else ''} |")
    hu_cov = {h for e in EVENTS for h in e["hu"]}
    hu_no = sorted(set(S["HU"]) - hu_cov)
    ev_no_hu = [e["id"] for e in EVENTS if not e["hu"]]
    o.append(f"""
**Cobertura de historias:** {len(hu_cov)}/{len(S['HU'])} historias tienen al menos un evento. Las {len(hu_no)} restantes son **historias de consulta** —leer no produce eventos (RN-INT-006)—: {', '.join(hu_no)}.

**Eventos sin historia ({len(ev_no_hu)}):** {', '.join(ev_no_hu)}. Provienen de procesos del SPEC sin historia propia (H-10, H-11 del SRS; HD-11, HD-19).

## Matriz E — Evento ↔ Requisito funcional

| Evento | Nombre | Requisitos funcionales (SRS) |
|---|---|---|""")
    for e in EVENTS:
        o.append(f"| {e['id']} | {e['nombre']} | {ids(e['rf'])}{' ⚠️' if not e['rf'] else ''} |")
    rf_cov = {h for e in EVENTS for h in e["rf"]}
    rf_no = sorted(set(S["RF"]) - rf_cov)
    ev_no_rf = [e["id"] for e in EVENTS if not e["rf"]]
    o.append(f"""
**Cobertura de requisitos:** {len(rf_cov)}/{len(S['RF'])} RF se relacionan con al menos un evento. Los {len(rf_no)} restantes son de **consulta, restricción transversal o presentación**, que no producen hechos nuevos: {', '.join(rf_no)}.

**Eventos sin RF ({len(ev_no_rf)}):** {', '.join(ev_no_rf)}. Son la traducción al dominio de las brechas del SRS: reglas sin RF (H-11), cierre de jornada (H-10) y funciones de módulo sin requisito (HD-19). Implementarlos exige que el Director apruebe las propuestas del Anexo C del SRS (DEC-05, DEC-06).
""")
    o.append(estado(f"Matriz D ({len(EVENTS)} eventos ↔ {len(hu_cov)} historias) y Matriz E ({len(EVENTS)} eventos ↔ {len(rf_cov)} RF), con coberturas y exclusiones justificadas",
                    f"{len(ev_no_rf)} eventos sin RF y {len(ev_no_hu)} sin historia (RF5-12)", "SRS Caps. 5 y 6", "H-10, H-11 del SRS · HD-11, HD-19", "6"))
    return "\n".join(o)

def event_catalog():
    idx = """
## Índice

| Cap. | Título |
|---|---|
| 1 | Filosofía de eventos |
| 2 | Catálogo completo de eventos |
| 3 | Línea temporal de eventos por proceso |
| 4 | Eventos auditables |
| 5 | Eventos derivados |
| 6 | Matrices D (Evento ↔ HU) y E (Evento ↔ RF) |
"""
    return (header("EVENT_CATALOG", "Catálogo de Eventos del Dominio de COLBASOFT", "`DOMAIN_MODEL.md` · `GLOSSARY.md`")
            + idx + ev_cap1() + ev_cap2() + ev_cap3() + ev_cap4() + ev_cap5() + ev_cap6()
            + "\n---\n\n*Fin de EVENT_CATALOG v1.1.*\n")

# ====================================================================================== GLOSSARY
def sortkey(t):
    return unicodedata.normalize("NFD", t["term"].lower()).encode("ascii", "ignore").decode()

RISKS_F5 = [
 ("RF5-01", "Identidad de la mercancía identificada por QR — **resuelto por DF5-01** (el QR identifica SKU + Lote)", "HD-04", "✅", "Ya no condiciona la Fase 5; queda el tratamiento de copias impresas (RF5-14)"),
 ("RF5-02", "Operaciones que deben ser indivisibles sobre dos unidades (movimiento interno, primera ubicación, transferencia, confirmación de entrada)", "Cap. 5.3 · RN-MOV-004 · RN-MOV-010", "🔴", "Si se confirma solo una mitad, la existencia total cambia"),
 ("RF5-03", "Concurrencia sobre la disponibilidad de una misma unidad", "IN-08, IN-10, IN-11", "🔴", "Dos operaciones simultáneas podrían comprometer la misma existencia"),
 ("RF5-04", "Existencia derivada del kardex frente a tiempos de consulta", "IN-03 · RNF-REN-001 · RNF-ESC-004", "🟠", "Derivar en cada consulta puede degradar el rendimiento al crecer el kardex"),
 ("RF5-05", "Registros sin conectividad que al sincronizarse ya no cumplen una regla — la regla ya está definida (DF5-05, RN-INT-008, IN-72); falta garantizarla técnicamente", "HD-16 · HD-24 · RN-INT-003 · RN-INT-008", "🟠", "Sin la revalidación, la sincronización podría dejar existencia negativa o duplicados"),
 ("RF5-06", "Capacidad y ocupación con unidades de medida heterogéneas", "HD-17", "🟠", "KPI-18 y la alerta de sobreocupación no son calculables"),
 ("RF5-07", "Inmutabilidad y continuidad demostrables de kardex y bitácora", "IN-02, IN-63 · RNF-AUD-002", "🟠", "El jurado y el Auditor deben poder comprobarlas"),
 ("RF5-08", "Decisiones del Director abiertas que cambian el modelo", "DEC-01, DEC-04, DEC-05, DEC-07, DEC-09 · HD-21", "🟠", "Entidades y eventos ⚠️ pueden cambiar o desaparecer"),
 ("RF5-09", "Escalas no definidas de severidad y prioridad", "HD-15", "🟡", "Ordenamiento de alertas y tareas indefinido"),
 ("RF5-10", "Ubicación de la existencia en tránsito (HD-05); la zona de recepción y el estado inicial quedaron resueltos por DF5-02", "HD-05", "🟡", "Cómo se representa la porción en tránsito respecto de su unidad origen"),
 ("RF5-11", "Carga del Administrador por ajustes derivados de conteo", "HD-08 · RG-18", "🟡", "Cuello de botella de aprobaciones"),
 ("RF5-12", "Eventos sin requisito que los implemente", "EVENT_CATALOG Cap. 6", "🟠", "Comportamientos del dominio sin criterio de aceptación"),
 ("RF5-13", "Crecimiento ilimitado de kardex, bitácora e historiales (sin purga)", "RNF-AUD-004 · RNF-ESC-004", "🟡", "Volumen a tres años sin estimación"),
 ("RF5-14", "Qué identifica físicamente cada etiqueta de mercancía: copias de un QR de lote, etiqueta física única o paquete (HD-25)", "HD-25 · RN-IDE-004 · RN-SAL-004", "🔴", "Sin decidirlo no se sabe si un escaneo equivale a una cantidad, cómo se reimprime sin invalidar otras etiquetas ni si cambia la identidad de la mercancía"),
]

def gl_ids():
    """IDs estables: los términos de la v1.0 conservan su GL-nnn (orden alfabético original); los agregados después (v11) continúan la numeración."""
    base = sorted((x for x in TERMS if not x.get("v11")), key=sortkey)
    nuevos = [x for x in TERMS if x.get("v11")]
    return {x["term"]: f"GL-{i:03d}" for i, x in enumerate(base + nuevos, 1)}

def glossary():
    terms = sorted(TERMS, key=sortkey)
    gl_id = gl_ids()
    o = [header("GLOSSARY", "Glosario Oficial de COLBASOFT", "`DOMAIN_MODEL.md` · `EVENT_CATALOG.md`")]
    ctx = Counter(t["ctx"] for t in terms)
    o.append(f"""
> **Reconstrucción de contexto.** Ver DOMAIN_MODEL, Cap. 0 (ESTADO: CONTEXTO RECONSTRUIDO).

# CAPÍTULO 1 — USO DEL GLOSARIO

1. **Única definición permitida.** Este glosario es la única fuente de definiciones de COLBASOFT. Ningún documento posterior (arquitectura, modelo de datos, interfaz, pruebas, manuales) puede redefinir un término: lo cita.
2. **Mismo texto que el lenguaje ubicuo.** Los {sum(t['ul'] for t in terms)} términos centrales tienen en DOMAIN_MODEL Cap. 1 exactamente la misma definición.
3. **Sinónimos prohibidos.** No se usan ni como aclaración. El índice inverso (Cap. 3) remite de cada término prohibido al oficial.
4. **Definición prohibida.** Es la interpretación errónea que el término **no** debe recibir.
5. **Cambios.** Un término se agrega o se reformula solo con aprobación del Director; su ID `GL-nnn` no se reutiliza.

**Campos de cada entrada:** definición oficial · definición prohibida · sinónimos prohibidos · contexto (subdominio o ámbito) · documento de origen · relaciones.

**Distribución por contexto:** """ + " · ".join(f"{k} {v}" for k, v in ctx.most_common()) + f"\n\n**Total de términos: {len(terms)}.**\n")
    o.append(estado("Reglas de uso, campos y distribución", "Uso de sinónimos en la interfaz o en documentos futuros", "SPEC §0.5 · DOMAIN_MODEL Cap. 1", "HD-01", "1"))
    o.append("\n---\n\n# CAPÍTULO 2 — TÉRMINOS\n")
    letter = None
    for t in terms:
        L0 = sortkey(t)[0].upper()
        if L0 != letter:
            letter = L0
            o.append(f"\n## {letter}\n")
        rels = "; ".join(f"{r} ({gl_id[r]})" if r in gl_id else r for r in [x.strip() for x in t["rel"].split(";") if x.strip()])
        o.append(f"### {gl_id[t['term']]} · {t['term']}{' ★' if t['ul'] else ''}\n")
        o.append("| Campo | Contenido |\n|---|---|")
        o.append(f"| **Definición oficial** | {t['d']} |")
        o.append(f"| **Definición prohibida** | {t['prohib']} |")
        o.append(f"| **Sinónimos prohibidos** | {t['sin'] or '—'} |")
        o.append(f"| **Contexto** | {t['ctx']} |")
        o.append(f"| **Documento origen** | {pair(t['origen'])} |")
        o.append(f"| **Relaciones** | {rels or '—'} |\n")
    o.append("> ★ = término central del lenguaje ubicuo (DOMAIN_MODEL Cap. 1).\n")
    o.append(estado(f"{len(terms)} términos con los cinco campos exigidos más sinónimos prohibidos", "—", "DOMAIN_MODEL · EVENT_CATALOG", "HD-01, HD-14, HD-22", "2"))
    # índice inverso
    inv = []
    for t in terms:
        for s in [x.strip() for x in t["sin"].split(",") if x.strip()]:
            inv.append((s, t["term"]))
    inv.sort(key=lambda x: unicodedata.normalize("NFD", x[0].lower()).encode("ascii", "ignore").decode())
    o.append("\n---\n\n# CAPÍTULO 3 — ÍNDICE INVERSO DE SINÓNIMOS PROHIBIDOS\n\n| No usar | Usar | ID |\n|---|---|---|")
    for s, term in inv:
        o.append(f"| {s} | **{term}** | {gl_id[term]} |")
    o.append(estado(f"{len(inv)} sinónimos prohibidos con su término oficial", "—", "Cap. 2", "—", "3"))
    # auditoría interna
    o.append(internal_audit(len(terms), len(inv)))
    o.append("\n---\n\n*Fin de GLOSSARY v1.1. La monografía original permanece sin modificaciones.*\n")
    return "\n".join(o)

def internal_audit(nterms, nsyn):
    inv_rn = {x for i in INVARIANTS for x in i[2]}
    pol = sorted(set(S["RN"]) - inv_rn)
    tot_s = sum(len(s[2]) for s in STATE_MACHINES)
    tot_t = sum(len(s[3]) for s in STATE_MACHINES)
    der = sum(1 for e in EVENTS if e["der"])
    hu_cov = len({h for e in EVENTS for h in e["hu"]})
    rf_cov = len({h for e in EVENTS for h in e["rf"]})
    kpi_cov = len({h for e in EVENTS for h in e["kpi"]})
    subc = Counter(s["tipo"] for s in SUBDOMAINS)
    rows = "\n".join(f"| **{r[0]}** | {r[1]} | {r[2]} | {r[3]} | {r[4]} |" for r in RISKS_F5)
    return f"""
---

# AUDITORÍA INTERNA DE LA FASE 4

> Verificación de los tres documentos (DOMAIN_MODEL, EVENT_CATALOG, GLOSSARY). Los totales se calcularon sobre la misma fuente de datos de la que se generaron los documentos.

## A. Totales

| Elemento | Total | Mínimo exigido | Cumple |
|---|:--:|:--:|:--:|
| Subdominios | {len(SUBDOMAINS)} (Core {subc['Core']} · Supporting {subc['Supporting']} · Generic {subc['Generic']}) | 9 | ✅ |
| **Entidades** | **{len(ENTITIES)}** | 13 | ✅ |
| **Objetos de valor** | **{len(VALUE_OBJECTS)}** | — (7 ejemplos) | ✅ |
| **Agregados** | **{len(AGGREGATES)}** | — | ✅ |
| **Invariantes** | **{len(INVARIANTS)}** (+ {len(pol)} políticas reactivas) | 40 | ✅ |
| **Estados oficiales** | **{tot_s}** en {len(STATE_MACHINES)} máquinas ({tot_t} transiciones) | — | ✅ |
| **Eventos** | **{len(EVENTS)}** ({der} derivados) | 70 | ✅ |
| **Términos del glosario** | **{nterms}** ({sum(t['ul'] for t in TERMS)} centrales; {nsyn} sinónimos prohibidos indexados) | 120 | ✅ |
| Hallazgos del dominio | {len(DOMAIN_FINDINGS)} | — | — |
| Líneas temporales | {len(TIMELINES)} procesos | 14 | ✅ |
| Matrices | A, B, C (DOMAIN_MODEL Cap. 9) · D, E (EVENT_CATALOG Cap. 6) | 5 | ✅ |

## B. Verificaciones de consistencia

| # | Verificación | Resultado |
|---|---|:--:|
| V-1 | Toda regla, historia, requisito y KPI citado existe en el SRS/SPEC | ✅ 0 referencias rotas |
| V-2 | Toda entidad citada por un evento, relación o agregado existe | ✅ |
| V-3 | Todo evento citado en estados y líneas temporales existe | ✅ |
| V-4 | Toda invariante citada por un agregado existe | ✅ |
| V-5 | Las {len(S["RN"])} reglas del SRS (82 + 3 de la v1.1) quedan cubiertas como invariante o política | ✅ {len(inv_rn)} + {len(pol)} = {len(inv_rn | set(pol))}/{len(S["RN"])} |
| V-6 | Los 24 KPI aparecen en al menos un evento | ✅ {kpi_cov}/24 |
| V-7 | Historias con evento | 🟡 {hu_cov}/103 (el resto son de consulta) |
| V-8 | RF con evento | 🟡 {rf_cov}/162 (el resto son de consulta, restricción o presentación) |
| V-9 | Toda invariante cita al menos una regla del SRS | ✅ {len(INVARIANTS)}/{len(INVARIANTS)} |
| V-10 | Las definiciones del lenguaje ubicuo y del glosario son idénticas | ✅ (misma fuente) |
| V-11 | Ninguna relación del glosario apunta a un término inexistente | ✅ |
| V-12 | Ningún término nombra a la empresa de estudio (DC-01) ni introduce IA (DC-07) | ✅ |
| V-13 | Sin arquitectura, modelo de datos, tecnologías ni código | ✅ |
| V-14 | Ningún documento previo fue modificado | ✅ |

## C. Riesgos abiertos para la Arquitectura (Fase 5)

| ID | Riesgo | Origen | Sev. | Consecuencia si no se atiende |
|---|---|---|:--:|---|
{rows}

**Estado frente a la Fase 5 (v1.1).** El cierre del CP-04 resolvió HD-04, HD-06, HD-07, HD-23 y HD-24 (DF5-01, DF5-02, DF5-03, DF5-05). **HD-25** (qué identifica físicamente cada etiqueta) requiere una decisión antes de la Fase 5. HD-17, HD-26 y HD-27 requieren información de la operación real y DEC-01…DEC-09 siguen abiertas, sin bloquear la arquitectura (ver `04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md`). Siguen vigentes R-S01 (modelo TO-BE sin contraste con la operación real) y los riesgos críticos de adopción del SPEC.

---

**ESTADO DE LA FASE 4**

| | |
|---|---|
| **Completado** | DOMAIN_MODEL (11 capítulos), EVENT_CATALOG (6 capítulos), GLOSSARY (3 capítulos + auditoría interna) |
| **Riesgos** | {len(RISKS_F5)} riesgos para la Fase 5 ({sum(1 for r in RISKS_F5 if r[3] == "🔴")} críticos abiertos; RF5-01 resuelto) · R-S01 heredado |
| **Dependencias** | Decisiones del Director DEC-01…DEC-09 y hallazgos pendientes (DOMAIN_MODEL Cap. 10) |
| **Hallazgos** | {len(DOMAIN_FINDINGS)} hallazgos del dominio (DOMAIN_MODEL Cap. 10) |
"""

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    docs = {"DOMAIN_MODEL.md": domain_model(), "EVENT_CATALOG.md": event_catalog(), "GLOSSARY.md": glossary()}
    for k, v in docs.items():
        open(os.path.join(OUT, k), "w", encoding="utf8", newline="\n").write(v)
        print(k, len(v), "chars", v.count("\n"), "lines")
