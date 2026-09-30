# -*- coding: utf-8 -*-
"""Genera COLBASOFT_SPEC_v1.2.md a partir de COLBASOFT_SPEC_v1.1.md (que no se modifica).

La v1.2 incorpora las decisiones del Director del 30 de septiembre de 2026 (DEC-01 = A con la capa
pieza/rollo; Q-11, F-1…F-6, Q-09, Q-10; piloto de 1 bodega; nivel Ingeniería). Cada cambio es un
reemplazo exacto que debe encontrarse una sola vez en la v1.1, o una inserción en un ancla única;
si el texto de origen no aparece, el script falla.

Uso: python build_spec_v12.py [carpeta_de_salida]   (por defecto, 01_SPEC_FASE_2 del proyecto)
"""
import sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "01_SPEC_FASE_2" / "COLBASOFT_SPEC_v1.1.md"
OUT_DIR = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "01_SPEC_FASE_2"
OUT = OUT_DIR / "COLBASOFT_SPEC_v1.2.md"

CAMBIOS = """
## Control de cambios de la versión 1.2

> La versión 1.2 incorpora las decisiones que el Director del Proyecto tomó el **30 de septiembre de 2026** al auditar DEC-01 (`DEC-01 = A — Núcleo, con 1 bodega piloto`, más la capa de trazabilidad por pieza). La versión 1.1 se conserva sin cambios en `COLBASOFT_SPEC_v1.1.md`. Todo pasaje modificado o nuevo lleva la etiqueta de la decisión que lo origina.

| Etiqueta | Decisión del Director |
|---|---|
| `[DEC-01]` | Alcance aprobatorio = **A, Núcleo (Horizonte 1)**, con **1 bodega piloto**. Transferencias, conteo general y el resto del Horizonte 2 quedan **fuera** del umbral aprobatorio |
| `[Q-11]` | La trazabilidad por **pieza o rollo está dentro del MVP** (antes: Horizonte 3, §12.4 elemento 6) |
| `[F-1]` | **Pieza** = rollo para referencias en metros o kilogramos; paquete o bolsa para referencias en unidades |
| `[F-2]` | La **cantidad de cada rollo o pieza se registra al recibir** |
| `[F-3]` | Se permiten **cortes parciales** de rollos |
| `[F-4]` | Con varias piezas del mismo lote en una ubicación, el operario **selecciona la pieza después del escaneo**; la ubicación funciona como filtro de verificación |
| `[F-5]` | El conteo es **manual, pieza por pieza** |
| `[F-6]` | Los **contenedores y bolsas agrupadas** también entran al MVP |
| `[Q-09]` | Una reimpresión **conserva el mismo QR**; no crea una nueva identidad |
| `[Q-10]` | El escaneo de salida **verifica y cuenta** |
| Otras | Piloto de **1 bodega**; nivel académico **Ingeniería** (la v1.1 y el SRS v1.1 decían «nivel Tecnólogo» en RG-38 y R-S03) |

| # | Decisión | Qué cambia | Dónde | Texto de la v1.1 |
|---|---|---|---|---|
| 1 | **Q-11 · F-1 · F-2** | Aparece el concepto **Pieza** (CD-49): cada rollo, paquete o bolsa tiene identidad interna, tipo y cantidad propia registrada en la recepción. **El QR sigue identificando SKU + Lote** (DF5-01 no se toca) y la unidad de inventario sigue siendo SKU + Lote + Ubicación (RN-066 no se toca) | CD-49, PN-01 (pasos 4–5), HU-104, RF-163, RF-164, RN-084*, RN-085* | «El Auxiliar registra la cantidad recibida por referencia, talla, color y lote» (PN-01 paso 5) |
| 2 | **F-6** | El contenedor o bolsa agrupada se registra como una pieza de tipo «contenedor agrupado» con su cantidad de unidades; pertenece a **un solo SKU + Lote**. La mezcla de lotes en un contenedor queda como DECISIÓN PENDIENTE (HD-28) | PN-02 E-03, HU-105, RF-165 | «Se rotula el contenedor y se registra como unidad de manejo agrupada» (PN-02 E-03) |
| 3 | **F-4** | Tras escanear el QR del SKU + Lote, el operario **selecciona la pieza**; la ubicación filtra y verifica. Aplica a la primera ubicación y al movimiento interno | PN-03 (pasos 3 y 6), PN-05 (pasos 2–3), HU-106, RF-166, RN-087* | PN-03 paso 3; PN-05 pasos 2 y 3 |
| 4 | **Q-10 · F-3** | En la preparación de una salida el escaneo **verifica y cuenta**; cada pieza se cuenta una vez. El **corte parcial** de una pieza descuenta lo cortado y deja el remanente en la misma pieza | PN-10 (pasos 7–8), HU-107, HU-108, RF-167, RF-168, RN-086*, RN-088* | «El Auxiliar escanea cada unidad al tomarla» (PN-10 paso 7) |
| 5 | **F-5** | El conteo se hace **manualmente, pieza por pieza**; la cantidad contada de la unidad de inventario es la suma de sus piezas. La cantidad esperada sigue oculta (RN-040) | PN-08 (pasos 5–6), HU-109, RF-169, RN-089* | «El Auxiliar escanea la ubicación y cuenta físicamente» (PN-08 paso 5) |
| 6 | **Q-11** | Trazabilidad por pieza: kardex y consulta por pieza | HU-110, RF-170, RF-171 | — |
| 7 | **Q-09** | La reimpresión **conserva el mismo QR**: deja de emitir un identificador nuevo y de marcar el anterior como reemplazado. Los demás motivos de reemplazo de un identificador quedan como DECISIÓN PENDIENTE (HD-28) | RN-018, RF-045, HU-028 (criterios 2–4), PN-02 E-01 y E-02, M-06, RG-25 | «El identificador nuevo hereda íntegramente la trazabilidad del anterior, que queda marcado como reemplazado» (RN-018) |
| 8 | **DEC-01** | El Núcleo (Horizonte 1) es el umbral aprobatorio. Se incorpora al Horizonte 1 el elemento 40 «Trazabilidad por pieza» (§12.2). El Horizonte 2 no cambia | §12.2, §12.3, §12.4 (elemento 6), §12.6, §13.6 (asunto 10) | «Hasta que el Director defina el entregable mínimo aprobatorio» |
| 9 | **Nivel Ingeniería** | Se corrige «nivel Tecnólogo» | RG-38 | «un proyecto de nivel Tecnólogo» |
| 10 | **Estado** | Borrador de la v1.2: validación técnica pendiente; aprobación funcional y académica pendiente (DEC-02…DEC-09) | Portada, §13.7 | «Validado técnicamente» |

**Lo que la v1.2 no cambia.** El QR de mercancía (DF5-01), la unidad de inventario (RN-066), las cinco reglas DF5 de la v1.1, los horizontes del Horizonte 2 (19 HU y 19 RF), los KPI, los RNF, los módulos y los procesos (14) no cambian de número. Se agregan **7 historias** (HU-104…HU-110), **9 requisitos funcionales** (RF-163…RF-171), **6 reglas estructurales** (RN-084*…RN-089*, §9.16) y **1 concepto** (CD-49). Las historias y requisitos agregados pertenecen al **Horizonte 1**: el Núcleo pasa de 84 HU y 143 RF a **91 HU y 152 RF**; el Completo, de 103 HU y 162 RF a **110 HU y 171 RF**. Las reglas pasan de 85 a **91**. La discrepancia entre las 68 reglas declaradas y las tablas (H-01 del SRS, DEC-03) **sigue abierta**.

**Decisiones que la v1.2 deja pendientes** (marcadas `DECISIÓN PENDIENTE`; no se inventa ninguna respuesta):

| ID | Pendiente | Por qué |
|---|---|---|
| **HD-28** | Si un contenedor agrupado puede mezclar lotes o SKU (Q-08); cómo se distinguen «paquete o bolsa» (F-1) y «contenedor o bolsa agrupada» (F-6); los motivos por los que un identificador QR se reemplaza ahora que la reimpresión ya no lo reemplaza | Las decisiones del Director no los cubren |
| **HD-29** | Qué ocurre con el remanente de un corte parcial si se mueve a otra ubicación (¿se divide la pieza?); si el movimiento parcial de una pieza entre ubicaciones es posible (HU-045 criterio 2 habla de cantidad parcial) | F-3 habla de cortes; no de divisiones entre ubicaciones |
| **HD-30** | Si toda referencia se controla por piezas o solo las que tienen una pieza física distinguible | F-1 define la pieza para metros, kilogramos y unidades, sin excepciones declaradas |
"""

REGLAS_V12 = """
## 9.16 Reglas incorporadas en la versión 1.2 (decisiones del 30 de septiembre de 2026)

> Estas seis reglas **no forman parte de las 82** de §9.2–§9.12 ni de las tres de §9.15: se incorporan en la v1.2 por las decisiones Q-11, F-1…F-6, Q-09 y Q-10. Se numeran a continuación de RN-083* con asterisco. **Todas son estructurales**: ninguna es parametrizable (DEC-04, interpretación a).

| ID | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-084*** | **Toda mercancía recibida se registra por piezas.** Cada pieza pertenece a un solo SKU + Lote, tiene un tipo —rollo, paquete o bolsa, o contenedor agrupado— y una **cantidad propia registrada en la recepción**. El QR no identifica la pieza: la pieza tiene identidad interna en el sistema y el QR sigue identificando SKU + Lote | Estructural | `[Q-11]` `[F-1]` `[F-2]` `[F-6]` `[CD-49]` |
| **RN-085*** | **La existencia de una unidad de inventario es la suma de las cantidades de sus piezas en esa ubicación.** La cantidad de una pieza solo cambia por un movimiento del kardex (entrada, salida, movimiento interno, ajuste); la cantidad recibida de una línea de entrada es la suma de las cantidades de sus piezas | Estructural | `[Q-11]` `[F-2]` `[RN-065]` `[RN-066]` |
| **RN-086*** | **Un corte parcial descuenta de la pieza solo la cantidad cortada** y deja la pieza con su remanente, con la misma identidad. La cantidad cortada no puede superar la cantidad de la pieza (RN-009). El corte es una salida y cumple las reglas de salida | Estructural | `[F-3]` `[RN-009]` `[RN-048]` |
| **RN-087*** | **Toda operación que mueve, toma o cuenta mercancía identifica la pieza afectada.** Después de escanear el QR del SKU + Lote el operario selecciona la pieza; si hay varias del mismo lote en la ubicación, la ubicación (escaneada o seleccionada) filtra y verifica qué piezas se ofrecen. No se confirma la operación sin pieza seleccionada | Estructural | `[F-4]` `[RN-015]` |
| **RN-088*** | **En la preparación de una salida el escaneo verifica y cuenta.** Cada pieza tomada se cuenta una sola vez: seleccionar de nuevo la misma pieza no suma. La preparación no se confirma completa mientras falten piezas o cantidad solicitada, salvo salida parcial autorizada | Estructural | `[Q-10]` `[RN-050]` `[RN-025]` |
| **RN-089*** | **El conteo se hace manualmente, pieza por pieza.** El contador registra la cantidad de cada pieza sin ver la cantidad esperada (RN-040); la cantidad contada de la unidad de inventario es la suma de sus piezas | Estructural | `[F-5]` `[RN-040]` |
"""

HU_NUEVAS = {
"M-07": """
**HU-104** · P0 · Auxiliar · `[Q-11]` `[F-1]` `[F-2]`
**COMO** Auxiliar de Bodega **QUIERO** registrar cada rollo, paquete o bolsa que recibo con su cantidad **PARA** saber después cuál pieza es cuál y cuánto trae cada una sin tener que medirla otra vez.
*Criterios:* (1) Cada pieza se registra con su tipo —rollo para referencias en metros o kilogramos; paquete o bolsa para referencias en unidades— y con su cantidad propia `[F-1]` `[F-2]`. (2) Cada pieza pertenece a un solo SKU + Lote `[RN-084*]`. (3) La cantidad recibida de la línea es la suma de las cantidades de sus piezas y se compara contra la esperada `[RN-085*]` `[RN-005]`. (4) La pieza conserva su identidad en el sistema desde la recepción; el QR de mercancía sigue identificando solo el SKU + Lote `[DF5-01]`. (5) El sistema confirma visualmente cada pieza registrada.

**HU-105** · P1 · Auxiliar · `[F-6]`
**COMO** Auxiliar de Bodega **QUIERO** registrar como una sola pieza el contenedor o la bolsa agrupada en que llega mercancía sin rotulado individual **PARA** poder ubicarla, moverla y contarla sin rotular cada prenda.
*Criterios:* (1) El contenedor o bolsa agrupada se registra como una pieza de tipo contenedor agrupado, con su cantidad de unidades `[F-6]`. (2) El contenedor pertenece a un solo SKU + Lote; registrar un contenedor con mezcla de lotes o de SKU no se admite hasta que el Director lo decida `[DECISIÓN PENDIENTE — HD-28]`. (3) Se ubica, mueve, cuenta y sale como cualquier otra pieza. (4) Lleva la etiqueta QR del SKU + Lote `[PN-02 E-03]`.
""",
"M-08": """
**HU-107** · P0 · Auxiliar · `[Q-10]` `[RN-088*]`
**COMO** Auxiliar de Bodega **QUIERO** que, al preparar una salida, el escaneo me confirme que tomo lo correcto y cuente las piezas que tomo **PARA** no dejar la salida incompleta ni contar dos veces lo mismo.
*Criterios:* (1) El escaneo verifica que lo tomado corresponde a lo solicitado `[RN-050]` y cuenta las piezas tomadas `[Q-10]`. (2) Después de escanear, el Auxiliar selecciona la pieza; cada pieza se cuenta una sola vez y seleccionar de nuevo la misma no suma `[RN-088*]`. (3) El progreso muestra las piezas y la cantidad tomadas frente a lo solicitado. (4) La preparación no se confirma completa mientras falten piezas o cantidad, salvo salida parcial autorizada `[RN-025]`. (5) Cada pieza tomada queda en el kardex.

**HU-108** · P0 · Auxiliar · `[F-3]` `[RN-086*]`
**COMO** Auxiliar de Bodega **QUIERO** registrar que corté solo una parte de un rollo **PARA** que el resto siga en el inventario con la cantidad correcta.
*Criterios:* (1) Se selecciona la pieza y se indica la cantidad cortada `[F-3]`. (2) La cantidad cortada no puede superar la cantidad de la pieza `[RN-009]` `[RN-086*]`. (3) El sistema descuenta lo cortado de la pieza, que conserva su identidad con el remanente `[RN-086*]`. (4) El corte se registra como una salida, con motivo tipificado, autorización y atribución personal `[RN-048]`. (5) El kardex registra qué pieza, cuánto, quién, cuándo y por qué. (6) La cantidad restante de la pieza queda visible de inmediato.
""",
"M-09": """
**HU-106** · P0 · Auxiliar · `[F-4]` `[RN-087*]`
**COMO** Auxiliar de Bodega **QUIERO** elegir en pantalla la pieza que estoy ubicando o moviendo, después de escanear **PARA** que el sistema sepa exactamente qué pieza cambió de lugar aunque haya varias del mismo lote en el mismo estante.
*Criterios:* (1) Tras escanear el QR del SKU + Lote, el sistema muestra las piezas de ese lote y el Auxiliar selecciona la que mueve `[F-4]`. (2) Con varias piezas del mismo lote en la ubicación de origen, la ubicación actúa como filtro de verificación: solo se ofrecen las piezas que el sistema registra allí. (3) No se confirma un movimiento sin pieza seleccionada `[RN-087*]`. (4) Aplica al movimiento interno y a la primera ubicación desde recepción `[RN-082*]`. (5) El movimiento queda en el kardex con la pieza. (6) La existencia total no cambia `[RN-026]`.
""",
"M-11": """
**HU-109** · P0 · Auxiliar · `[F-5]` `[RN-089*]`
**COMO** Auxiliar de Bodega **QUIERO** contar a mano cada pieza de una ubicación y registrar su cantidad **PARA** que el conteo verifique la realidad pieza por pieza.
*Criterios:* (1) El conteo se hace manualmente, pieza por pieza `[F-5]`. (2) El Auxiliar registra la cantidad de cada pieza contada. (3) `[RN-040]` **La cantidad esperada no se muestra antes ni después de registrar.** (4) La cantidad contada de la unidad de inventario es la suma de sus piezas `[RN-089*]`. (5) El sistema compara lo contado con la existencia congelada y clasifica cada línea como conforme, sobrante o faltante `[RN-039]`.
""",
"M-14": """
**HU-110** · P0 · Jefe / Auditor · `[Q-11]` `[CD-21]`
**COMO** Jefe de Bodega **QUIERO** consultar dónde está y qué ha pasado con cada pieza de un lote **PARA** rastrear un rollo o un paquete concreto y no solo el lote completo.
*Criterios:* (1) La consulta de un lote muestra sus piezas con tipo, cantidad actual, ubicación y estado `[Q-11]`. (2) El kardex de una pieza muestra todos sus movimientos en orden cronológico. (3) `[CD-21]` **Permite responder las seis preguntas de trazabilidad: qué, cuánto, dónde, quién, cuándo y por qué.** (4) La trazabilidad por pieza no requiere un QR propio `[DF5-01]`. (5) Responde dentro del tiempo de RNF-012.
""",
}

RF_NUEVOS = {
"M-07": """| RF-163 | El sistema debe permitir registrar cada pieza recibida —rollo, paquete o bolsa— con su tipo y su cantidad propia, dentro de una línea de entrada | P0 | Auxiliar | RF-052, CD-49 | `[Q-11]` `[F-1]` `[F-2]` |
| RF-164 | El sistema debe derivar la cantidad recibida de cada línea como la suma de las cantidades de sus piezas y compararla contra la esperada | P0 | — | RF-163, RF-054 | `[RN-085*]` |
| RF-165 | El sistema debe permitir registrar un contenedor o bolsa agrupada como una pieza con su cantidad de unidades, perteneciente a un solo SKU + Lote | P1 | Auxiliar | RF-163 | `[F-6]` |
""",
"M-08": """| RF-167 | El sistema debe, en la preparación de una salida, verificar lo escaneado y **contar cada pieza seleccionada una sola vez** | P0 | Auxiliar | RF-068, RF-163 | `[Q-10]` `[RN-088*]` |
| RF-168 | El sistema debe permitir registrar el corte parcial de una pieza, descontando la cantidad cortada y **conservando la pieza con su remanente**, sin superar la cantidad de la pieza | P0 | Auxiliar | RF-167, RF-069 | `[F-3]` `[RN-086*]` |
""",
"M-09": """| RF-166 | El sistema debe **exigir la selección de la pieza** en todo movimiento interno y en la primera ubicación, usando la ubicación como filtro de verificación cuando haya varias piezas del mismo lote | P0 | Auxiliar | RF-072, RF-163 | `[F-4]` `[RN-087*]` |
""",
"M-11": """| RF-169 | El sistema debe permitir contar manualmente pieza por pieza, registrando la cantidad de cada pieza **sin mostrar la esperada** | P0 | Auxiliar | RF-098, RF-163 | `[F-5]` `[RN-089*]` |
""",
"M-13": """| RF-171 | El sistema debe permitir consultar las piezas de un lote con su tipo, cantidad actual, ubicación y estado | P0 | Todos | RF-112, RF-163 | `[Q-11]` |
""",
"M-14": """| RF-170 | El sistema debe registrar en el kardex la pieza afectada por cada movimiento que la toque | P0 | — | RF-120, RF-163 | `[Q-11]` `[RN-085*]` |
""",
}

FUNC_V12 = {  # módulo -> texto añadido al capítulo 5
"M-06": "**Funciones modificadas en la v1.2:** la reimpresión produce otra copia del mismo QR y **no** marca el identificador como reemplazado `[Q-09]`; los demás motivos de reemplazo de un identificador quedan como DECISIÓN PENDIENTE (HD-28).",
"M-07": "**Funciones incorporadas en la v1.2:** registrar cada pieza recibida con su tipo y cantidad propia `[Q-11]` `[F-1]` `[F-2]` · registrar contenedores y bolsas agrupadas como pieza `[F-6]`. **Restricción:** la cantidad recibida de una línea es la suma de sus piezas `[RN-085*]`.",
"M-08": "**Funciones incorporadas en la v1.2:** el escaneo de preparación verifica y cuenta piezas `[Q-10]` · registrar el corte parcial de una pieza `[F-3]`. **Restricciones:** cada pieza se cuenta una sola vez `[RN-088*]` · el corte no supera la cantidad de la pieza `[RN-086*]`.",
"M-09": "**Funciones incorporadas en la v1.2:** seleccionar la pieza tras el escaneo, en el movimiento interno y en la primera ubicación, con la ubicación como filtro de verificación `[F-4]` `[RN-087*]`. Las **transferencias** siguen en el Horizonte 2 y quedan fuera del umbral aprobatorio `[DEC-01]`.",
"M-11": "**Funciones incorporadas en la v1.2:** conteo manual pieza por pieza `[F-5]` `[RN-089*]`. El **conteo general** sigue en el Horizonte 2 y queda fuera del umbral aprobatorio `[DEC-01]`; la granularidad pieza por pieza y el alcance del conteo (cíclico o general) son ejes independientes.",
"M-13": "**Funciones incorporadas en la v1.2:** consultar las piezas de un lote con tipo, cantidad actual, ubicación y estado `[Q-11]`.",
"M-14": "**Funciones incorporadas en la v1.2:** registrar la pieza afectada en cada movimiento y consultar el kardex de una pieza `[Q-11]`.",
}

CD49 = """
### CD-49 · Pieza
**Definición operativa:** unidad física individual de mercancía dentro de un lote, con **cantidad propia registrada en la recepción** `[F-2]` e identidad interna en el sistema. Tipos: **rollo** (referencias medidas en metros o kilogramos), **paquete o bolsa** (referencias contadas en unidades) `[F-1]` y **contenedor agrupado** (contenedor rotulado que agrupa mercancía sin rotulado individual) `[F-6]`. Pertenece a un solo SKU + Lote y se ubica en una sola ubicación. **El QR no identifica la pieza**: identifica el SKU + Lote `[DF5-01]`; el operario selecciona la pieza después del escaneo `[F-4]`. Su cantidad solo cambia por movimientos del kardex; un corte parcial la reduce y la deja con su remanente `[F-3]`. `[Q-11]` `[RN-084*]` `[RN-085*]`
"""

BLOQUE7 = """
### Bloque 7 — Trazabilidad por pieza *(incorporado en la v1.2)*

> `[Q-11]` El Director declaró la trazabilidad por pieza o rollo dentro del MVP: el elemento 6 del Horizonte 3 («Gestión de unidades de manejo y contenedores») se incorpora en lo que exigen Q-11 y F-1…F-6.

| Orden | Elemento | Módulos | RF principales | Origen |
|:--:|---|---|---|---|
| 40 | Piezas (rollo, paquete o bolsa, contenedor agrupado) con cantidad propia, selección tras el escaneo, corte parcial, escaneo de salida que verifica y cuenta, conteo pieza por pieza y trazabilidad por pieza | M-07, M-08, M-09, M-11, M-13, M-14 | RF-163 a RF-171 | `[Q-11]` `[F-1]` `[F-2]` `[F-3]` `[F-4]` `[F-5]` `[F-6]` `[Q-10]` |
"""


def ins_in_block(txt, cap_marker, heading, anchor, new, before=True):
    """Inserta `new` dentro del bloque `heading` del capítulo `cap_marker`, antes (o después) de `anchor`."""
    c = txt.index(cap_marker)
    h = txt.index(heading, c)
    a = txt.index(anchor, h)
    nxt = txt.find("\n## ", h + 5)
    assert nxt == -1 or a < nxt, (heading, anchor)
    return txt[:a] + new + txt[a:] if before else txt[:a + len(anchor)] + new + txt[a + len(anchor):]


def block_end(txt, cap_marker, heading):
    """Posición justo antes del siguiente encabezado '## ' o '---' del bloque de un módulo."""
    c = txt.index(cap_marker)
    h = txt.index(heading, c)
    cands = [p for p in (txt.find("\n## M-", h + 5), txt.find("\n---\n", h + 5)) if p != -1]
    return min(cands)


R = [
 # ---------------------------------------------------------------- portada
 ("# COLBASOFT_SPEC v1.1\n", "# COLBASOFT_SPEC v1.2\n"),
 ("| **Versión** | 1.1 |", "| **Versión** | 1.2 |"),
 ("| **Fecha** | 5 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) |",
  "| **Fecha** | 5 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) · 30 de septiembre de 2026 (v1.2) |"),
 ("| **Estado** | **Validado técnicamente** (cierre del CP-04, 29-sep-2026). **Aprobación funcional y académica pendiente**: HD-25 y DEC-01…DEC-09 sin responder (`04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md`) |",
  "| **Estado** | **Borrador v1.2** (30-sep-2026): incorpora DEC-01 = A con la capa de trazabilidad por pieza y resuelve HD-25. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: DEC-02…DEC-09 sin responder y acta de DEC-08 |"),
 ("| **Versión anterior** | `COLBASOFT_SPEC_v1.0.md` (5-sep-2026), conservada sin cambios |",
  "| **Versión anterior** | `COLBASOFT_SPEC_v1.1.md` (29-sep-2026) y `COLBASOFT_SPEC_v1.0.md` (5-sep-2026), conservadas sin cambios |"),
 ("banco de la Fase F.\n\n## Control de cambios de la versión 1.1\n",
  "banco de la Fase F.\n" + CAMBIOS + "\n## Control de cambios de la versión 1.1\n"),
 # índice y convenciones
 ("| **4** | Catálogo del Producto | 48 conceptos de dominio con definición operativa |",
  "| **4** | Catálogo del Producto | 49 conceptos de dominio con definición operativa (CD-49 «Pieza» desde la v1.2) |"),
 ("| **6** | Historias de Usuario | 103 historias con criterios de aceptación |",
  "| **6** | Historias de Usuario | 110 historias con criterios de aceptación (HU-104…HU-110 desde la v1.2) |"),
 ("| **7** | Requisitos Funcionales | 162 requisitos (RF-001 … RF-162) |",
  "| **7** | Requisitos Funcionales | 171 requisitos (RF-001 … RF-171) |"),
 ("+ 3 incorporadas en la v1.1 (§9.15) |", "+ 3 incorporadas en la v1.1 (§9.15) + 6 incorporadas en la v1.2 (§9.16) |"),
 ("| `CD-nn` | Concepto de dominio | CD-01 … CD-48 |", "| `CD-nn` | Concepto de dominio | CD-01 … CD-49 |"),
 ("| `RN-nnn` | Regla de negocio | RN-001 … RN-068 (v1.0) · RN-081* … RN-083* (v1.1) |",
  "| `RN-nnn` | Regla de negocio | RN-001 … RN-068 (v1.0) · RN-081* … RN-083* (v1.1) · RN-084* … RN-089* (v1.2) |"),
 # ---------------------------------------------------------------- Cap. 3 (procesos)
 ("4. El Auxiliar cuenta físicamente la mercancía recibida.\n5. El Auxiliar registra la cantidad recibida por referencia, talla, color y lote `[NUEVO]`.",
  "4. El Auxiliar cuenta físicamente la mercancía recibida, pieza por pieza `[Q-11]`.\n5. El Auxiliar registra cada pieza —rollo, paquete, bolsa o contenedor agrupado— con su **cantidad propia**; la cantidad recibida por referencia, talla, color y lote es la suma de sus piezas `[RN-084*]` `[RN-085*]` `[F-1]` `[F-2]`."),
 ("| E-01 | La impresión sale ilegible | Se reimprime; el identificador anterior se marca **Reemplazado** y queda en el historial `[RN-018]` |",
  "| E-01 | La impresión sale ilegible | Se reimprime la misma etiqueta: el QR no cambia y no se crea una nueva identidad `[RN-018]` `[Q-09]` |"),
 ("| El Auxiliar solicita reimpresión indicando motivo; el nuevo hereda la trazabilidad del anterior `[RN-018]` |",
  "| El Auxiliar solicita reimpresión indicando motivo; se imprime otra copia del mismo QR `[RN-018]` `[Q-09]` |"),
 ("| Se rotula el contenedor y se registra como unidad de manejo agrupada `[NUEVO]` |",
  "| Se rotula el contenedor con el QR del SKU + Lote y se registra como **pieza de tipo contenedor agrupado**, con su cantidad de unidades `[RN-084*]` `[F-6]`; el contenedor pertenece a un solo SKU + Lote (mezcla de lotes: DECISIÓN PENDIENTE, HD-28) |"),
 ("3. El Auxiliar escanea el identificador de la mercancía `[DC-08]`.\n4. El Auxiliar escanea el identificador de la ubicación `[NUEVO]`.",
  "3. El Auxiliar escanea el identificador de la mercancía `[DC-08]` y selecciona la pieza que ubica `[RN-087*]` `[F-4]`.\n4. El Auxiliar escanea el identificador de la ubicación `[NUEVO]`."),
 ("con qué, cuánto, quién, cuándo y el documento de entrada que la origina `[RN-082*]` `[DF5-03]`.",
  "con qué, cuánto, qué pieza, quién, cuándo y el documento de entrada que la origina `[RN-082*]` `[DF5-03]`."),
 ("2. El sistema muestra las ubicaciones donde ese SKU + Lote tiene existencia; si hay más de una, el Auxiliar indica la de origen escaneando su identificador o seleccionándola, y la selección queda registrada `[RN-015]` `[DF5-01]`.\n3. El Auxiliar indica la cantidad a mover (total o parcial) `[NUEVO]`.",
  "2. El sistema muestra las ubicaciones donde ese SKU + Lote tiene existencia; si hay más de una, el Auxiliar indica la de origen escaneando su identificador o seleccionándola, y la selección queda registrada `[RN-015]` `[DF5-01]`.\n3. El Auxiliar selecciona la pieza que mueve; con varias piezas del mismo lote en la ubicación de origen, la ubicación filtra y verifica qué piezas se ofrecen `[RN-087*]` `[F-4]`. El movimiento parcial de una pieza entre ubicaciones es DECISIÓN PENDIENTE (HD-29) `[NUEVO]`."),
 ("5. El Auxiliar escanea la ubicación y cuenta físicamente `[DC-08]`.\n6. El Auxiliar registra la cantidad contada.",
  "5. El Auxiliar escanea la ubicación y cuenta físicamente, a mano, pieza por pieza `[DC-08]` `[F-5]`.\n6. El Auxiliar registra la cantidad de cada pieza contada; la cantidad contada de la unidad de inventario es la suma de sus piezas `[RN-089*]`."),
 ("7. El Auxiliar escanea cada unidad al tomarla `[DC-08]`.\n8. El sistema valida que lo escaneado corresponda a lo solicitado `[RN-050]`.",
  "7. El Auxiliar escanea el identificador de lo que toma `[DC-08]` y selecciona la pieza tomada; si corta parte de un rollo, registra la cantidad cortada `[RN-086*]` `[RN-087*]` `[F-3]`.\n8. El sistema valida que lo escaneado corresponda a lo solicitado `[RN-050]` y cuenta cada pieza tomada una sola vez `[RN-088*]` `[Q-10]`."),
 # ---------------------------------------------------------------- Cap. 4 (CD-49)
 ("\n## 4.7 Mapa de relaciones del vocabulario\n", CD49 + "\n## 4.7 Mapa de relaciones del vocabulario\n"),
 # ---------------------------------------------------------------- Cap. 6 y 7 (cabeceras y resúmenes)
 ("> **103 historias**, agrupadas por módulo.", "> **110 historias**, agrupadas por módulo."),
 ("| M-07 Entradas | 8 | HU-030 – HU-037 |", "| M-07 Entradas | 10 | HU-030 – HU-037, HU-104, HU-105 |"),
 ("| M-08 Salidas | 7 | HU-038 – HU-044 |", "| M-08 Salidas | 9 | HU-038 – HU-044, HU-107, HU-108 |"),
 ("| M-09 Movimientos y Transferencias | 7 | HU-045 – HU-051 |", "| M-09 Movimientos y Transferencias | 8 | HU-045 – HU-051, HU-106 |"),
 ("| M-11 Conteos | 9 | HU-058 – HU-066 |", "| M-11 Conteos | 10 | HU-058 – HU-066, HU-109 |"),
 ("| M-14 Kardex y Trazabilidad | 5 | HU-077 – HU-081 |", "| M-14 Kardex y Trazabilidad | 6 | HU-077 – HU-081, HU-110 |"),
 ("| **Total** | **103** | |", "| **Total** | **110** | |"),
 ("> **162 requisitos funcionales**, numerados RF-001 a RF-162 y agrupados por módulo.",
  "> **171 requisitos funcionales**, numerados RF-001 a RF-171 y agrupados por módulo."),
 ("| M-07 Entradas | 13 | RF-048–060 | 7 | 4 | 2 | 0 |", "| M-07 Entradas | 16 | RF-048–060, RF-163–165 | 9 | 5 | 2 | 0 |"),
 ("| M-08 Salidas | 11 | RF-061–071 | 6 | 4 | 1 | 0 |", "| M-08 Salidas | 13 | RF-061–071, RF-167–168 | 8 | 4 | 1 | 0 |"),
 ("| M-09 Movimientos y Transferencias | 11 | RF-072–082 | 5 | 5 | 1 | 0 |", "| M-09 Movimientos y Transferencias | 12 | RF-072–082, RF-166 | 6 | 5 | 1 | 0 |"),
 ("| M-11 Conteos | 13 | RF-093–105 | 3 | 8 | 2 | 0 |", "| M-11 Conteos | 14 | RF-093–105, RF-169 | 4 | 8 | 2 | 0 |"),
 ("| M-13 Consulta de Existencia | 8 | RF-112–119 | 5 | 2 | 1 | 0 |", "| M-13 Consulta de Existencia | 9 | RF-112–119, RF-171 | 6 | 2 | 1 | 0 |"),
 ("| M-14 Kardex | 7 | RF-120–126 | 5 | 2 | 0 | 0 |", "| M-14 Kardex | 8 | RF-120–126, RF-170 | 6 | 2 | 0 | 0 |"),
 ("| **Total** | **162** | | **72** | **69** | **21** | **0** |", "| **Total** | **171** | | **80** | **70** | **21** | **0** |"),
 # ---------------------------------------------------------------- Q-09 (reimpresión) y Nivel Ingeniería
 ("| RF-045 | El sistema debe permitir la reimpresión con motivo obligatorio, **heredando el nuevo identificador la trazabilidad del anterior** | P1 | Coord. / Aux. | M-14 | `[RN-018]` |",
  "| RF-045 | El sistema debe permitir la reimpresión con motivo obligatorio, **conservando el mismo QR y sin crear una nueva identidad** | P1 | Coord. / Aux. | M-14 | `[RN-018]` `[Q-09]` |"),
 ("(2) **El identificador nuevo hereda toda la trazabilidad del anterior** `[RN-018]`. (3) El anterior queda marcado como reemplazado, no eliminado. (4) El historial de identificadores del SKU + Lote es consultable.",
  "(2) **La reimpresión produce otra copia del mismo QR: el identificador no cambia y no se crea una nueva identidad** `[RN-018]` `[Q-09]`. (3) Reimprimir no marca el identificador como reemplazado. (4) El historial de reimpresiones del SKU + Lote es consultable."),
 ("| **RN-018** | La reimpresión de un identificador exige motivo. **El identificador nuevo hereda íntegramente la trazabilidad del anterior**, que queda marcado como reemplazado y consultable en el historial. | Estructural | `[DC-08]` `[MON §7.1]` |",
  "| **RN-018** | La reimpresión de un identificador exige motivo. **La reimpresión conserva el mismo QR: produce otra copia del mismo identificador y no crea una nueva identidad**, por lo que el identificador no cambia de estado ni pierde su trazabilidad. La reimpresión queda consultable en el historial del SKU + Lote. Los motivos por los que un identificador se reemplaza o se anula son DECISIÓN PENDIENTE (HD-28) | Estructural | `[DC-08]` `[MON §7.1]` `[Q-09]` |"),
 ("Reimpresión con herencia de trazabilidad `[RN-018]`", "Reimpresión que conserva el mismo QR `[RN-018]` `[Q-09]`"),
 ("**El alcance del MVP resulta desproporcionado** para un proyecto de nivel Tecnólogo.",
  "**El alcance del MVP resulta desproporcionado** para un proyecto de nivel Ingeniería (corregido en la v1.2; la v1.1 decía «Tecnólogo»)."),
 # ---------------------------------------------------------------- Cap. 12
 ("\n**Alcance del MVP:** 39 elementos · 72 requisitos P0 y los P1 indispensables · 20 módulos con funcionalidad parcial en M-11, M-15, M-16 y M-17.",
  BLOQUE7 + "\n**Alcance del MVP:** 40 elementos · 72 requisitos P0 declarados en la v1.1 más 8 de la v1.2, y los P1 indispensables · 20 módulos con funcionalidad parcial en M-11, M-15, M-16 y M-17. **Umbral aprobatorio `[DEC-01]`: Núcleo (Horizonte 1), 91 HU y 152 RF, con 1 bodega piloto.**"),
 ("| 6 | Gestión de unidades de manejo y contenedores | Necesidad operativa demostrada | Dentro de `[DC-02]` |",
  "| 6 | Gestión avanzada de unidades de manejo y contenedores (lo que excede lo incorporado al MVP por Q-11 y F-1…F-6; ver HD-28 y HD-29) | Necesidad operativa demostrada · autorización expresa del Director | Dentro de `[DC-02]`. La pieza, el paquete o bolsa y el contenedor agrupado pasaron al MVP en la v1.2 `[Q-11]` `[F-6]` |"),
 ("| **MVP** | 39 | Operación completa, trazable y medible | ❌ |", "| **MVP** | 40 | Operación completa, trazable y medible | ❌ |"),
 ("| 10 | Entregable mínimo aprobatorio | S-15 | Alcance de construcción |",
  "| 10 | Entregable mínimo aprobatorio | S-15 | **Resuelto en la v1.2 (`[DEC-01]`): Núcleo, con 1 bodega piloto** |"),
 # ---------------------------------------------------------------- Cap. 13
 ("| 4 | Conceptos de dominio definidos | 48 |", "| 4 | Conceptos de dominio definidos | 49 |"),
 ("| 6 | Historias de usuario | 103 |", "| 6 | Historias de usuario | 110 |"),
 ("| 7 | Requisitos funcionales | 162 |", "| 7 | Requisitos funcionales | 171 |"),
 ("| 12 | Elementos de backlog | 73 |", "| 12 | Elementos de backlog | 74 |"),
 ("Los 48 conceptos de dominio están definidos operativamente en el **Capítulo 4**.",
  "Los 49 conceptos de dominio están definidos operativamente en el **Capítulo 4**."),
 ("| 1.1 | 29 de septiembre de 2026 | Cierre del CP-04: decisiones DF5-01, DF5-02, DF5-03 y DF5-05 (ver «Control de cambios de la versión 1.1»); 3 reglas nuevas (§9.15) | Validado técnicamente; aprobación pendiente (DEC-01…DEC-09, HD-25) |",
  "| 1.1 | 29 de septiembre de 2026 | Cierre del CP-04: decisiones DF5-01, DF5-02, DF5-03 y DF5-05 (ver «Control de cambios de la versión 1.1»); 3 reglas nuevas (§9.15) | Validado técnicamente; aprobación pendiente (DEC-01…DEC-09, HD-25) |\n"
  "| 1.2 | 30 de septiembre de 2026 | DEC-01 = A (Núcleo, 1 bodega) con la capa de trazabilidad por pieza: Q-11, F-1…F-6, Q-09, Q-10 (ver «Control de cambios de la versión 1.2»); 7 HU, 9 RF, 6 reglas y 1 concepto nuevos | Borrador; validación técnica y aprobación pendientes (DEC-02…DEC-09) |"),
 ("| `COLBASOFT_SPEC v1.1` | **Este documento** — Fase 2, revisado en el cierre del CP-04 | Validado técnicamente; aprobación pendiente |",
  "| `COLBASOFT_SPEC v1.2` | **Este documento** — Fase 2, revisado tras la auditoría de DEC-01 | Borrador; aprobación pendiente |\n"
  "| `COLBASOFT_SPEC v1.1` | Versión anterior — cierre del CP-04 | Validado técnicamente; conservada sin cambios |"),
 ("*COLBASOFT_SPEC v1.1 — Especificación Funcional de Producto*\n*5 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1)*",
  "*COLBASOFT_SPEC v1.2 — Especificación Funcional de Producto*\n*5 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) · 30 de septiembre de 2026 (v1.2)*"),
]


def main():
    txt = SRC.read_text(encoding="utf8")
    for old, new in R:
        n = txt.count(old)
        assert n == 1, f"se esperaba 1 ocurrencia y hay {n}: {old[:90]!r}"
        txt = txt.replace(old, new)
    # §9.16 va inmediatamente antes del Capítulo 10
    anchor = "\n---\n\n# CAPÍTULO 10"
    assert txt.count(anchor) == 1
    txt = txt.replace(anchor, "\n" + REGLAS_V12 + anchor)
    # Capítulo 5: funciones
    for mod, nuevo in FUNC_V12.items():
        head = {"M-06": "## M-06 · Identificación QR", "M-07": "## M-07 · Entradas y Recepción", "M-08": "## M-08 · Salidas",
                "M-09": "## M-09 · Movimientos y Transferencias", "M-11": "## M-11 · Conteos",
                "M-13": "## M-13 · Consulta de Existencia", "M-14": "## M-14 · Kardex y Trazabilidad"}[mod]
        txt = ins_in_block(txt, "# CAPÍTULO 5", head, "**Dependencias funcionales:**", nuevo + "\n\n")
    # Capítulo 6: historias (al final del bloque de cada módulo)
    for mod, bloque in HU_NUEVAS.items():
        head = {"M-07": "## M-07 · Entradas y Recepción", "M-08": "## M-08 · Salidas",
                "M-09": "## M-09 · Movimientos y Transferencias", "M-11": "## M-11 · Conteos",
                "M-14": "## M-14 · Kardex y Trazabilidad"}[mod]
        p = block_end(txt, "# CAPÍTULO 6", head)
        txt = txt[:p] + "\n" + bloque.strip("\n") + "\n" + txt[p:]
    # Capítulo 7: requisitos (al final de la tabla del módulo)
    for mod, filas in RF_NUEVOS.items():
        head = {"M-07": "## M-07 · Entradas y Recepción", "M-08": "## M-08 · Salidas",
                "M-09": "## M-09 · Movimientos y Transferencias", "M-11": "## M-11 · Conteos",
                "M-13": "## M-13 · Consulta de Existencia", "M-14": "## M-14 · Kardex y Trazabilidad"}[mod]
        p = block_end(txt, "# CAPÍTULO 7", head)
        assert txt[:p].endswith("|\n"), (mod, txt[p - 40:p])
        txt = txt[:p] + filas.strip("\n") + "\n" + txt[p:]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(txt, encoding="utf8", newline="\n")
    print(OUT, len(txt), "chars", txt.count("\n"), "lines")


if __name__ == "__main__":
    main()
