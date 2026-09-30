# -*- coding: utf-8 -*-
"""Genera COLBASOFT_SPEC_v1.3.md a partir de COLBASOFT_SPEC_v1.2.md (que no se modifica).

La v1.3 registra las respuestas del Director a DEC-02…DEC-09 (30 de septiembre de 2026). Cada cambio
es un reemplazo exacto que debe encontrarse una sola vez en la v1.2, o una inserción en un ancla única;
si el texto de origen no aparece, el script falla.

Uso: python build_spec_v13.py [carpeta_de_salida]   (por defecto, 01_SPEC_FASE_2 del proyecto)
"""
import sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "01_SPEC_FASE_2" / "COLBASOFT_SPEC_v1.2.md"
OUT_DIR = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "01_SPEC_FASE_2"
OUT = OUT_DIR / "COLBASOFT_SPEC_v1.3.md"

CAMBIOS = """
## Control de cambios de la versión 1.3

> La versión 1.3 registra las respuestas del Director del Proyecto a **DEC-02…DEC-09** (30 de septiembre de 2026), todas en la opción recomendada por el SRS. Las versiones 1.2, 1.1 y 1.0 se conservan sin cambios. Todo pasaje modificado o nuevo lleva la etiqueta de la decisión que lo origina.

| Decisión | Respuesta del Director | Qué cambia en el SPEC |
|---|---|---|
| **DEC-02** | (a) Se mantienen los 20 módulos, incluido el dashboard operativo (M-17); la exclusión es de **toda** IA `[DC-07]` | Nada cambia en el contenido; cierra el hallazgo H-17 del SRS |
| **DEC-03** | (a) El SRS es la numeración canónica de las reglas; fe de erratas del SPEC | Nuevo §9.17 (fe de erratas); §0.4; §13.6 asunto 11 |
| **DEC-04** | (a) Toda regla estructural es no configurable; el **Jefe puede leer** los parámetros; el **Administrador o el Jefe responden y cierran** las observaciones de auditoría | §2.7 (fila nueva «Consultar parámetros de configuración»), M-18, HU-096 (criterio 4), RF-152 |
| **DEC-05** | (a) Se crean las HU y RF del cierre operativo de jornada (PN-14) | HU-113, HU-114; RF-182, RF-183, RF-184; §12.2 elemento 39 |
| **DEC-06** | (a) Se aprueban **todas** las propuestas PROP-RN (reglas sin RF) y PROP-KPI (KPI sin dato de origen) | RF-172…RF-181; HU-111, HU-112; RF-152 (dos parámetros nuevos); §12.2 elemento 41 |
| **DEC-07** | (a) Se retira del MVP el permiso «consultar valorización»; queda como restricción preventiva (RF-116 y RF-143 se conservan) | §2.7, M-16, HU-087 (criterio 5) |
| **DEC-08** | (a) Acta de aprobación y tabla de equivalencia de fases | **Borrador** en `05_V13_DECISIONES/05_V13_DECISIONES_DEC02_DEC09.md`; el acta no está firmada |
| **DEC-09** | (a) La alerta «lote próximo a vencer inmovilización» se redefine sobre el umbral de antigüedad del lote (RN-074) | PN-11 (tipo de alerta «Lote próximo a vencer inmovilización») |

**Elementos nuevos.** **4 historias** (HU-111…HU-114) y **13 requisitos funcionales** (RF-172…RF-184). Ninguna regla nueva: las propuestas PROP-RN dan requisito a reglas que ya existían (RN-022, RN-028, RN-043, RN-047, RN-051, RN-059). **Horizontes:** todos al Horizonte 1, salvo **HU-112 y RF-175** (diferencia crítica del conteo general), que siguen a su proceso en el Horizonte 2. El Núcleo (umbral aprobatorio, `[DEC-01]`) pasa de 91 HU y 152 RF a **94 HU y 164 RF**; el Completo, de 110 HU y 171 RF a **114 HU y 184 RF**. El Horizonte 2 pasa de 19 a 20 HU y de 19 a 20 RF.

**Lo que la v1.3 no cambia.** El QR, la unidad de inventario, la capa de piezas de la v1.2, los 47 RNF, los KPI (24), las reglas (91), los procesos (14) y los módulos (20).

**Pendientes que siguen abiertos** (no se inventa ninguna respuesta): HD-28, HD-29 y HD-30 del modelo de dominio; los hallazgos H-19 y H-20 del SRS; la aprobación formal de DEC-08 (acta firmada); la verificación de campo de KPI-24 (actividad de la Fase 3 del roadmap).
"""

FE_ERRATAS = """
## 9.17 Fe de erratas sobre la cifra y la numeración de las reglas (versión 1.3)

> `[DEC-03]` El Director resolvió, el 30 de septiembre de 2026, adoptar el SRS como numeración canónica de las reglas y emitir esta fe de erratas. **No se modifica el texto de las reglas**; se corrige lo que este capítulo declaraba sobre ellas.

| # | Dice el SPEC | Se corrige a |
|---|---|---|
| 1 | «68 reglas» (índice del documento, §9.14 y §13.4) | Las tablas §9.2–§9.12 contienen **82 reglas distintas: 60 estructurales y 22 configurables**. Con las 3 de §9.15 y las 6 de §9.16 el total vigente es **91: 69 estructurales y 22 configurables** |
| 2 | `RN-069*` («reservado») y `RN-026b*` («ver nota de numeración») figuran en las tablas | **No son reglas**: son marcadores sin contenido y se retiran |
| 3 | Numeración `RN-nnn` del SPEC | La numeración **canónica** es `RN-<DOM>-nnn` del SRS (Anexo A.4). La numeración `RN-nnn` se conserva como referencia cruzada |
| 4 | §0.4 declara `HU-001…HU-096` y `RF-001…RF-138` | Los rangos vigentes son `HU-001…HU-114` y `RF-001…RF-184` (hallazgo H-03 del SRS) |
"""

HU_NUEVAS = {
"M-09": """
**HU-111** · P1 · Jefe · `[RN-028]` `[DEC-06]`
**COMO** Jefe de Bodega **QUIERO** que un movimiento interno interrumpido quede en tránsito y se me avise si tarda demasiado **PARA** no perder el rastro de la mercancía que quedó a medio camino.
*Criterios:* (1) Un movimiento interno que se inicia y no se cierra queda en estado en tránsito `[RN-028]`. (2) La existencia en tránsito no está disponible ni en el origen ni en el destino. (3) Si el tiempo en tránsito supera el máximo configurado, el sistema genera una alerta al Jefe. (4) Los movimientos en tránsito se listan en el cierre de la jornada `[PN-14]`.
""",
"M-11": """
**HU-112** · P1 · Jefe · `[RN-047]` `[DEC-06]`
**COMO** Jefe de Bodega **QUIERO** que el sistema avise al Administrador y al Auditor cuando la diferencia global de un conteo general sea crítica **PARA** que un conteo con un problema grave no se cierre sin que nadie lo sepa.
*Criterios:* (1) El umbral crítico de diferencia global es un parámetro configurable `[RF-152]`. (2) Si la diferencia global del conteo general lo supera, el sistema notifica al Administrador y al Auditor. (3) El cierre del conteo general queda condicionado a esa notificación `[RN-047]`. (4) La notificación queda en la bitácora.
""",
"M-20": """
**HU-113** · P1 · Coordinador / Jefe · `[PN-14]` `[DEC-05]`
**COMO** Coordinador de Bodega **QUIERO** ver al cierre de la jornada qué quedó pendiente y traspasarlo explícitamente al turno siguiente **PARA** que nada quede oculto ni sin responsable.
*Criterios:* (1) El sistema consolida los movimientos de la jornada. (2) Lista las recepciones sin confirmar, los movimientos en tránsito, las tareas de conteo abiertas, los ajustes sin resolver, las novedades sin atender y las alertas activas. (3) Lo que no se resuelve en el turno se traspasa explícitamente al turno siguiente. (4) El cierre queda registrado con quién lo ejecutó `[PR-05]`. (5) El Jefe ve el resumen de la jornada.

**HU-114** · P1 · Jefe · `[PN-14]` `[RN-054]` `[DEC-05]`
**COMO** Jefe de Bodega **QUIERO** que el sistema no deje cerrar la jornada con registros sin sincronizar y me avise si no se cerró **PARA** que el cierre refleje siempre lo que realmente pasó.
*Criterios:* (1) El sistema impide el cierre mientras haya registros sin sincronizar `[RN-054]`. (2) Un cierre no ejecutado se registra como omisión. (3) El Jefe recibe una alerta al día siguiente por el cierre omitido. (4) Una diferencia significativa en el consolidado genera una alerta antes de permitir el cierre.
""",
}

RF_NUEVOS = {
"M-05": "| RF-172 | El sistema debe registrar como información operativa la desviación entre la ubicación propuesta y la confirmada y notificar al Coordinador, sin imputarla al Auxiliar | P1 | — | RF-072 | `[RN-022]` `[DEC-06]` |\n",
"M-06": "| RF-179 | El sistema debe registrar en cada movimiento si la identificación se hizo por escaneo o por selección manual | P1 | — | RF-042, RF-120 | `[KPI-07]` `[DEC-06]` |\n",
"M-07": "| RF-180 | El sistema debe registrar el instante de llegada de la mercancía al documento de entrada | P1 | Auxiliar | RF-048 | `[KPI-12]` `[DEC-06]` |\n",
"M-08": "| RF-176 | El sistema debe liberar automáticamente la reserva no ejecutada dentro del plazo configurado y alertar al solicitante | P1 | — | RF-065, M-19 | `[RN-051]` `[DEC-06]` |\n",
"M-09": "| RF-173 | El sistema debe mantener en tránsito un movimiento interno interrumpido y generar alerta al superar el tiempo máximo configurado | P1 | — | RF-072, M-15 | `[RN-028]` `[DEC-06]` |\n",
"M-11": "| RF-175 | El sistema debe notificar al Administrador y al Auditor y condicionar el cierre de un conteo general cuando la diferencia global supere el umbral crítico configurado | P1 | — | RF-103, M-19 | `[RN-047]` `[DEC-06]` |\n",
"M-12": ("| RF-174 | El sistema debe impedir contar o usar mercancía sin registro hasta su identificación y permitir su incorporación solo mediante ajuste por sobrante con motivo tipificado y aprobación del Jefe | P1 | — | RF-083 | `[RN-043]` `[DEC-06]` |\n"
         "| RF-177 | El sistema debe escalar al Jefe y alertar las novedades no resueltas dentro del plazo configurado | P1 | — | RF-106, M-19 | `[RN-059]` `[DEC-06]` |\n"),
"M-14": "| RF-178 | El sistema debe registrar el instante de inicio y el de confirmación de cada movimiento | P1 | — | RF-120 | `[KPI-05]` `[DEC-06]` |\n",
"M-19": "| RF-181 | El sistema debe permitir registrar el volumen de movimientos de referencia estimado en campo para calcular la adopción | P2 | Administrador | RF-152 | `[KPI-24]` `[DEC-06]` |\n",
"M-20": ("| RF-182 | El sistema debe consolidar al cierre de la jornada los movimientos y los pendientes: recepciones sin confirmar, movimientos en tránsito, tareas de conteo abiertas, ajustes sin resolver, novedades sin atender y alertas activas | P1 | Coordinador | M-13, M-15 | `[PN-14]` `[DEC-05]` |\n"
         "| RF-183 | El sistema debe permitir traspasar explícitamente los pendientes al turno siguiente y registrar el cierre con quién lo ejecutó | P1 | Jefe / Coord. | RF-182 | `[PN-14]` `[DEC-05]` |\n"
         "| RF-184 | El sistema debe impedir el cierre con registros sin sincronizar, registrar como omisión el cierre no ejecutado y alertar ante una diferencia significativa | P1 | — | RF-182 | `[RN-054]` `[DEC-05]` |\n"),
}

HEAD = {"M-05": "## M-05 · Estructura de Bodega", "M-06": "## M-06 · Identificación QR", "M-07": "## M-07 · Entradas y Recepción",
        "M-08": "## M-08 · Salidas", "M-09": "## M-09 · Movimientos y Transferencias", "M-11": "## M-11 · Conteos",
        "M-12": "## M-12 · Novedades de Mercancía", "M-14": "## M-14 · Kardex y Trazabilidad", "M-19": "## M-19 · Parámetros y Configuración",
        "M-20": "## M-20 · Notificaciones y Tareas"}

BLOQUE8 = """
### Bloque 8 — Cierre de brechas de trazabilidad y del cierre de jornada *(incorporado en la v1.3)*

> `[DEC-05]` `[DEC-06]` El Director aprobó las propuestas de cierre de brechas del SRS (PROP-RN, PROP-KPI, PROP-CIE). Capturan desde el primer día datos que no se recuperan después y dan requisito a reglas que no lo tenían.

| Orden | Elemento | Módulos | RF principales | Origen |
|:--:|---|---|---|---|
| 41 | Reglas con requisito propio (desviación de ubicación, movimiento interno en tránsito, mercancía sin registro, reserva vencida, novedad vencida) y captura de datos de KPI (inicio y confirmación del movimiento, modo de identificación, llegada de la mercancía, volumen de referencia) | M-05, M-06, M-07, M-08, M-09, M-12, M-14, M-19 | RF-172, RF-173, RF-174, RF-176 a RF-181 | `[DEC-06]` |
"""


def ins_in_block(txt, cap_marker, heading, anchor, new, before=True):
    c = txt.index(cap_marker)
    h = txt.index(heading, c)
    a = txt.index(anchor, h)
    nxt = txt.find("\n## ", h + 5)
    assert nxt == -1 or a < nxt, (heading, anchor)
    return txt[:a] + new + txt[a:] if before else txt[:a + len(anchor)] + new + txt[a + len(anchor):]


def block_end(txt, cap_marker, heading):
    c = txt.index(cap_marker)
    h = txt.index(heading, c)
    cands = [p for p in (txt.find("\n## M-", h + 5), txt.find("\n---\n", h + 5)) if p != -1]
    return min(cands)


R = [
 # ---------------------------------------------------------------- portada
 ("# COLBASOFT_SPEC v1.2\n", "# COLBASOFT_SPEC v1.3\n"),
 ("| **Versión** | 1.2 |", "| **Versión** | 1.3 |"),
 ("· 30 de septiembre de 2026 (v1.2) |", "· 30 de septiembre de 2026 (v1.2 y v1.3) |"),
 ("| **Estado** | **Borrador v1.2** (30-sep-2026): incorpora DEC-01 = A con la capa de trazabilidad por pieza y resuelve HD-25. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: DEC-02…DEC-09 sin responder y acta de DEC-08 |",
  "| **Estado** | **Borrador v1.3** (30-sep-2026): registra las respuestas a DEC-01…DEC-09. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar (borrador en `05_V13_DECISIONES/`) y pendientes HD-28, HD-29, HD-30, H-19 y H-20 |"),
 ("| **Versión anterior** | `COLBASOFT_SPEC_v1.1.md` (29-sep-2026) y `COLBASOFT_SPEC_v1.0.md` (5-sep-2026), conservadas sin cambios |",
  "| **Versión anterior** | `COLBASOFT_SPEC_v1.2.md` (30-sep-2026), `COLBASOFT_SPEC_v1.1.md` (29-sep-2026) y `COLBASOFT_SPEC_v1.0.md` (5-sep-2026), conservadas sin cambios |"),
 ("\n## Control de cambios de la versión 1.2\n", CAMBIOS + "\n## Control de cambios de la versión 1.2\n"),
 # índice y convenciones
 ("| **6** | Historias de Usuario | 110 historias con criterios de aceptación (HU-104…HU-110 desde la v1.2) |",
  "| **6** | Historias de Usuario | 114 historias con criterios de aceptación (HU-104…HU-110 desde la v1.2; HU-111…HU-114 desde la v1.3) |"),
 ("| **7** | Requisitos Funcionales | 171 requisitos (RF-001 … RF-171) |", "| **7** | Requisitos Funcionales | 184 requisitos (RF-001 … RF-184) |"),
 ("| `HU-nnn` | Historia de usuario | HU-001 … HU-096 |", "| `HU-nnn` | Historia de usuario | HU-001 … HU-114 (corregido en la v1.3, §9.17) |"),
 ("| `RF-nnn` | Requisito funcional | RF-001 … RF-138 |", "| `RF-nnn` | Requisito funcional | RF-001 … RF-184 (corregido en la v1.3, §9.17) |"),
 # ---------------------------------------------------------------- matriz de segregación (DEC-04, DEC-07)
 ("| Consultar valorización | ✅ | ✅ | ❌ | ❌ | ✅ |",
  "| Consultar valorización *(función retirada del MVP, DEC-07)* | — | — | — | — | — |"),
 ("| Configurar umbrales de alerta | ✅ | ❌ | ❌ | ❌ | ❌ |",
  "| Configurar umbrales de alerta | ✅ | ❌ | ❌ | ❌ | ❌ |\n| Consultar parámetros de configuración, sin modificarlos `[DEC-04]` | ✅ | ✅ | ❌ | ❌ | ❌ |"),
 # ---------------------------------------------------------------- DEC-09
 ("| Lote próximo a vencer inmovilización | Lote que alcanza su fecha límite | `[NUEVO]` |",
  "| Lote próximo a vencer inmovilización | Lote que supera el umbral de antigüedad configurado (el lote no tiene «fecha límite») | `[RN-074]` `[DEC-09]` |"),
 # ---------------------------------------------------------------- DEC-07 (M-16, HU-087)
 ("los reportes con valorización no son accesibles al Coordinador ni al Auxiliar `[PR-04]`",
  "en el MVP no existe valorización: ningún reporte muestra costo ni valorización, y la restricción se conserva de forma preventiva `[PR-04]` `[DEC-07]`"),
 ("(5) `[PR-04]` La valorización solo aparece para roles autorizados.",
  "(5) `[PR-04]` `[DEC-07]` Ningún reporte muestra costo ni valorización: el MVP no captura costos."),
 # ---------------------------------------------------------------- DEC-04 (observaciones, parámetros)
 ("su única escritura son observaciones que no alteran el estado `[RN-064]`",
  "su única escritura son observaciones que no alteran el estado `[RN-064]` · las observaciones las responde y cierra el Administrador o el Jefe `[DEC-04]`"),
 ("(3) Es consultable por el Administrador y el Jefe. (4) No se elimina; se cierra con respuesta.",
  "(3) Es consultable por el Administrador y el Jefe. (4) No se elimina; el Administrador o el Jefe la cierra con su respuesta `[DEC-04]`."),
 ("| RF-152 | El sistema debe permitir configurar umbrales de ajuste, tolerancia de conteo, tiempo en tránsito, plazos y umbral de autorización del Coordinador | P0 | Administrador | — | `[CD-46]` |",
  "| RF-152 | El sistema debe permitir al Administrador configurar umbrales de ajuste, tolerancia de conteo, tiempo en tránsito, plazos, umbral de autorización del Coordinador, umbral crítico de diferencia global del conteo general y días sin movimiento, y al Jefe consultarlos sin modificarlos | P0 | Administrador | — | `[CD-46]` `[DEC-04]` `[DEC-06]` |"),
 # ---------------------------------------------------------------- DEC-03
 ("| 11 | Renumeración canónica de las reglas de negocio | — | Limpieza documental `[§9.13]` |",
  "| 11 | Renumeración canónica de las reglas de negocio | — | **Resuelto en la v1.3 (`[DEC-03]`, §9.17)** |"),
 # ---------------------------------------------------------------- Cap. 6 y 7 (resúmenes)
 ("> **110 historias**, agrupadas por módulo.", "> **114 historias**, agrupadas por módulo."),
 ("| M-09 Movimientos y Transferencias | 8 | HU-045 – HU-051, HU-106 |", "| M-09 Movimientos y Transferencias | 9 | HU-045 – HU-051, HU-106, HU-111 |"),
 ("| M-11 Conteos | 10 | HU-058 – HU-066, HU-109 |", "| M-11 Conteos | 11 | HU-058 – HU-066, HU-109, HU-112 |"),
 ("| M-20 Tareas | 3 | HU-101 – HU-103 |", "| M-20 Tareas | 5 | HU-101 – HU-103, HU-113, HU-114 |"),
 ("| **Total** | **110** | |", "| **Total** | **114** | |"),
 ("> **171 requisitos funcionales**, numerados RF-001 a RF-171 y agrupados por módulo.", "> **184 requisitos funcionales**, numerados RF-001 a RF-184 y agrupados por módulo."),
 ("| M-05 Estructura de Bodega | 8 | RF-032–039 | 4 | 3 | 1 | 0 |", "| M-05 Estructura de Bodega | 9 | RF-032–039, RF-172 | 4 | 4 | 1 | 0 |"),
 ("| M-06 Identificación QR | 8 | RF-040–047 | 4 | 3 | 1 | 0 |", "| M-06 Identificación QR | 9 | RF-040–047, RF-179 | 4 | 4 | 1 | 0 |"),
 ("| M-07 Entradas | 16 | RF-048–060, RF-163–165 | 9 | 5 | 2 | 0 |", "| M-07 Entradas | 17 | RF-048–060, RF-163–165, RF-180 | 9 | 6 | 2 | 0 |"),
 ("| M-08 Salidas | 13 | RF-061–071, RF-167–168 | 8 | 4 | 1 | 0 |", "| M-08 Salidas | 14 | RF-061–071, RF-167–168, RF-176 | 8 | 5 | 1 | 0 |"),
 ("| M-09 Movimientos y Transferencias | 12 | RF-072–082, RF-166 | 6 | 5 | 1 | 0 |", "| M-09 Movimientos y Transferencias | 13 | RF-072–082, RF-166, RF-173 | 6 | 6 | 1 | 0 |"),
 ("| M-11 Conteos | 14 | RF-093–105, RF-169 | 4 | 8 | 2 | 0 |", "| M-11 Conteos | 15 | RF-093–105, RF-169, RF-175 | 4 | 9 | 2 | 0 |"),
 ("| M-12 Novedades | 6 | RF-106–111 | 1 | 4 | 1 | 0 |", "| M-12 Novedades | 8 | RF-106–111, RF-174, RF-177 | 1 | 6 | 1 | 0 |"),
 ("| M-14 Kardex | 8 | RF-120–126, RF-170 | 6 | 2 | 0 | 0 |", "| M-14 Kardex | 9 | RF-120–126, RF-170, RF-178 | 6 | 3 | 0 | 0 |"),
 ("| M-19 Parámetros | 6 | RF-152–157 | 4 | 2 | 0 | 0 |", "| M-19 Parámetros | 7 | RF-152–157, RF-181 | 4 | 2 | 1 | 0 |"),
 ("| M-20 Tareas | 5 | RF-158–162 | 1 | 3 | 1 | 0 |", "| M-20 Tareas | 8 | RF-158–162, RF-182–184 | 1 | 6 | 1 | 0 |"),
 ("| **Total** | **171** | | **80** | **70** | **21** | **0** |", "| **Total** | **184** | | **80** | **82** | **22** | **0** |"),
 # ---------------------------------------------------------------- Cap. 12
 ("| 39 | Cierre operativo de jornada | M-20, M-17 | PN-14 | `[NUEVO]` |", "| 39 | Cierre operativo de jornada | M-20, M-17 | PN-14 · RF-182 a RF-184 | `[NUEVO]` `[DEC-05]` |"),
 ("\n**Alcance del MVP:** 40 elementos · 72 requisitos P0 declarados en la v1.1 más 8 de la v1.2, y los P1 indispensables · 20 módulos con funcionalidad parcial en M-11, M-15, M-16 y M-17. **Umbral aprobatorio `[DEC-01]`: Núcleo (Horizonte 1), 91 HU y 152 RF, con 1 bodega piloto.**",
  BLOQUE8 + "\n**Alcance del MVP:** 41 elementos · 72 requisitos P0 declarados en la v1.1 más 8 de la v1.2, y los P1 indispensables · 20 módulos con funcionalidad parcial en M-11, M-15, M-16 y M-17. **Umbral aprobatorio `[DEC-01]`: Núcleo (Horizonte 1), 94 HU y 164 RF, con 1 bodega piloto.**"),
 ("| 2 | Conteo general con bloqueo de movimientos | M-11 | El conteo cíclico ya alimenta el KPI-01 durante el piloto | `[NUEVO]` |",
  "| 2 | Conteo general con bloqueo de movimientos (incluye la alerta de diferencia crítica, RF-175 · HU-112) | M-11 | El conteo cíclico ya alimenta el KPI-01 durante el piloto | `[NUEVO]` `[DEC-06]` |"),
 ("| **MVP** | 40 | Operación completa, trazable y medible | ❌ |", "| **MVP** | 41 | Operación completa, trazable y medible | ❌ |"),
 # ---------------------------------------------------------------- Cap. 13
 ("| 2 | Funciones en la matriz de segregación | 36 |", "| 2 | Funciones en la matriz de segregación | 37 (36 + 1 nueva en la v1.3; «Consultar valorización» figura como retirada) |"),
 ("| 6 | Historias de usuario | 110 |", "| 6 | Historias de usuario | 114 |"),
 ("| 7 | Requisitos funcionales | 171 |", "| 7 | Requisitos funcionales | 184 |"),
 ("| 12 | Elementos de backlog | 74 |", "| 12 | Elementos de backlog | 75 |"),
 ("| 1.2 | 30 de septiembre de 2026 | DEC-01 = A (Núcleo, 1 bodega) con la capa de trazabilidad por pieza: Q-11, F-1…F-6, Q-09, Q-10 (ver «Control de cambios de la versión 1.2»); 7 HU, 9 RF, 6 reglas y 1 concepto nuevos | Borrador; validación técnica y aprobación pendientes (DEC-02…DEC-09) |",
  "| 1.2 | 30 de septiembre de 2026 | DEC-01 = A (Núcleo, 1 bodega) con la capa de trazabilidad por pieza: Q-11, F-1…F-6, Q-09, Q-10 (ver «Control de cambios de la versión 1.2»); 7 HU, 9 RF, 6 reglas y 1 concepto nuevos | Borrador; conservada sin cambios |\n"
  "| 1.3 | 30 de septiembre de 2026 | Respuestas a DEC-02…DEC-09 (ver «Control de cambios de la versión 1.3»); 4 HU y 13 RF nuevos; fe de erratas de las reglas (§9.17) | Borrador; validación técnica y acta de DEC-08 pendientes |"),
 ("| `COLBASOFT_SPEC v1.2` | **Este documento** — Fase 2, revisado tras la auditoría de DEC-01 | Borrador; aprobación pendiente |",
  "| `COLBASOFT_SPEC v1.3` | **Este documento** — Fase 2, con las respuestas a DEC-02…DEC-09 | Borrador; aprobación pendiente |\n| `COLBASOFT_SPEC v1.2` | Versión anterior — auditoría de DEC-01 | Borrador; conservada sin cambios |"),
 ("*COLBASOFT_SPEC v1.2 — Especificación Funcional de Producto*", "*COLBASOFT_SPEC v1.3 — Especificación Funcional de Producto*"),
 ("· 30 de septiembre de 2026 (v1.2)*", "· 30 de septiembre de 2026 (v1.2 y v1.3)*"),
]


def main():
    txt = SRC.read_text(encoding="utf8")
    for old, new in R:
        n = txt.count(old)
        assert n == 1, f"se esperaba 1 ocurrencia y hay {n}: {old[:90]!r}"
        txt = txt.replace(old, new)
    anchor = "\n---\n\n# CAPÍTULO 10"
    assert txt.count(anchor) == 1
    txt = txt.replace(anchor, "\n" + FE_ERRATAS + anchor)
    for mod, bloque in HU_NUEVAS.items():
        p = block_end(txt, "# CAPÍTULO 6", HEAD[mod])
        txt = txt[:p] + "\n" + bloque.strip("\n") + "\n" + txt[p:]
    for mod, filas in RF_NUEVOS.items():
        p = block_end(txt, "# CAPÍTULO 7", HEAD[mod])
        assert txt[:p].endswith("|\n"), (mod, txt[p - 40:p])
        txt = txt[:p] + filas + txt[p:]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(txt, encoding="utf8", newline="\n")
    print(OUT, len(txt), "chars", txt.count("\n"), "lines")


if __name__ == "__main__":
    main()
