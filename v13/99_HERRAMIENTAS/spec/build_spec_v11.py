# -*- coding: utf-8 -*-
"""Genera COLBASOFT_SPEC_v1.1.md a partir de COLBASOFT_SPEC_v1.0.md (que no se modifica).

La v1.1 incorpora las decisiones del cierre del CP-04 (DF5-01, DF5-02, DF5-03, DF5-05),
registradas en 04_CP04_AUDITORIA/04_CP04_CIERRE.md. Cada cambio es un reemplazo exacto que
debe encontrarse una sola vez en la v1.0; si el texto de origen no aparece, el script falla.

Uso: python build_spec_v11.py [carpeta_de_salida]   (por defecto, 01_SPEC_FASE_2 del proyecto)
"""
import sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "01_SPEC_FASE_2" / "COLBASOFT_SPEC_v1.0.md"
OUT_DIR = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "01_SPEC_FASE_2"
OUT = OUT_DIR / "COLBASOFT_SPEC_v1.1.md"

CAMBIOS = """
## Control de cambios de la versión 1.1

> La versión 1.1 incorpora las decisiones del **cierre del Checkpoint CP-04** (29 de septiembre de 2026), registradas en `04_CP04_AUDITORIA/04_CP04_CIERRE.md`. La versión 1.0 se conserva sin cambios en `COLBASOFT_SPEC_v1.0.md`. Todo pasaje modificado lleva la etiqueta de la decisión que lo origina (`[DF5-nn]`); el resto del documento es idéntico a la v1.0.

| # | Decisión | Qué cambia | Dónde | Texto de la v1.0 |
|---|---|---|---|---|
| 1 | **DF5-01** | El QR de mercancía identifica **SKU + Lote**, no la unidad de inventario. La unidad de inventario sigue siendo SKU + Lote + Ubicación (RN-066, sin cambios) y se determina con el QR de mercancía más la ubicación | CD-07, CD-08, CD-09, PN-02 (paso 1 y resultado), PN-05 (pasos 1–2), M-06, HU-025, HU-026, HU-028, HU-029, RF-040, RF-042, RN-015, RN-017 | «un identificador QR único por unidad de inventario» (PN-02, RF-040, HU-025); «asociado a una unidad de inventario» (CD-08, CD-09); «resolverlos a su unidad de inventario» (RF-042); «Un mismo identificador secundario de código de barras no puede asociarse a dos unidades de inventario distintas» (RN-017) |
| 2 | **DF5-02** | La entrada confirmada deja la existencia **En recepción**; pasa a Disponible al ubicarse. Toda zona de recepción tiene al menos una ubicación | PN-01 (paso 10 y resultado), nueva regla RN-081* | «El sistema incrementa la existencia disponible de cada unidad de inventario» (PN-01 paso 10); «La existencia disponible refleja exactamente la mercancía físicamente presente» (PN-01, resultado) |
| 3 | **DF5-03** | La primera ubicación de la mercancía en recepción es un **movimiento interno** registrado en el kardex | PN-03 (pasos 6–7 y E-04), nueva regla RN-082* | «El sistema registra la asignación de ubicación. / El sistema actualiza la existencia por ubicación» (PN-03 pasos 6–7) |
| 4 | **DF5-05** | Un registro retenido sin conectividad se **valida de nuevo** al sincronizarse; si ya no cumple las reglas, no se aplica, se rechaza con constancia y, si describe un hecho físico, abre una novedad | PN-01 E-07, PN-05 E-06, nueva regla RN-083* | «El registro se retiene localmente y se sincroniza al restablecerse» (PN-01 E-07, PN-05 E-06) |
| 5 | **DF5-06** (revisada) | Estado del documento: validado técnicamente; la aprobación funcional y académica sigue pendiente de HD-25 y DEC-01…DEC-09 | Portada, §13.7 | «Emitido para revisión del Director» |

**Lo que la v1.1 no cambia.** No se agregan historias, requisitos funcionales, requisitos no funcionales, KPI, procesos ni módulos; no cambia ningún horizonte del backlog (§12). Las reglas pasan de 82 a **85** (las tres nuevas, estructurales, están separadas en §9.15). La discrepancia entre las 68 reglas declaradas y las 82 de las tablas **sigue abierta** (H-01 del SRS, DEC-03): esta versión no la corrige.
"""

REGLAS_V11 = """
## 9.15 Reglas incorporadas en la versión 1.1 (cierre del CP-04)

> Estas tres reglas **no forman parte de las 82** de §9.2–§9.12: se incorporan en la v1.1 por las decisiones DF5-02, DF5-03 y DF5-05 del cierre del CP-04. Se numeran a continuación de RN-080 con asterisco, como las demás reglas incorporadas después de la numeración original (§9.13).

| ID | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-081*** | **La existencia que ingresa por una entrada confirmada queda en recepción**, en una ubicación de una zona de recepción de la bodega: ya está en el inventario pero **no está disponible**, por lo que no se reserva, no sale ni se transfiere hasta ubicarse. Toda zona de recepción tiene al menos una ubicación. Se exceptúa la cantidad dañada, que ingresa inmovilizada en cuarentena (RN-008). | Estructural | `[DF5-02]` `[CD-16]` `[CD-44]` |
| **RN-082*** | **La primera ubicación de la existencia en recepción es un movimiento interno** desde la ubicación de recepción hacia la ubicación destino, y queda en el kardex con qué, cuánto, origen, destino, quién, cuándo y el documento de entrada que la origina. Cumple las reglas del movimiento interno (RN-021, RN-026, RN-027): la existencia total no cambia y el descuento en origen y el incremento en destino son indivisibles. Al confirmarse, la cantidad movida queda **disponible** en el destino, salvo que el destino pertenezca a una zona de recepción, donde sigue en recepción. | Estructural | `[DF5-03]` `[PN-03]` `[RN-026]` |
| **RN-083*** | **Un registro retenido sin conectividad no se aplica sin validarse de nuevo.** Al sincronizarse se valida contra el estado vigente y contra todas las reglas aplicables. Si las cumple, se confirma conservando la fecha y hora en que ocurrió el hecho; si no, **no se aplica**: se rechaza dejando constancia del registro original, de su autor, del motivo del rechazo y del instante. Cuando el registro rechazado describe un hecho físico ya realizado (mercancía recibida o trasladada), se abre una novedad para su resolución. Cada registro retenido se confirma o se rechaza una sola vez: la sincronización nunca produce existencia negativa, movimientos inválidos, estados imposibles, duplicados ni pérdida de trazabilidad. | Estructural | `[DF5-05]` `[RN-054]` |
"""

R = [
 # ---------------------------------------------------------------- portada
 ("# COLBASOFT_SPEC v1.0\n", "# COLBASOFT_SPEC v1.1\n"),
 ("| **Versión** | 1.0 |", "| **Versión** | 1.1 |"),
 ("| **Fecha** | 5 de septiembre de 2026 |", "| **Fecha** | 5 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) |"),
 ("| **Estado** | Emitido para revisión del Director |",
  "| **Estado** | **Validado técnicamente** (cierre del CP-04, 29-sep-2026). **Aprobación funcional y académica pendiente**: HD-25 y DEC-01…DEC-09 sin responder (`04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md`) |\n"
  "| **Versión anterior** | `COLBASOFT_SPEC_v1.0.md` (5-sep-2026), conservada sin cambios |"),
 ("Las decisiones constitucionales recibidas del Director cierran, total o parcialmente, 19 de las 24 preguntas bloqueantes del banco de la Fase F.\n",
  "Las decisiones constitucionales recibidas del Director cierran, total o parcialmente, 19 de las 24 preguntas bloqueantes del banco de la Fase F.\n" + CAMBIOS),
 ("| **9** | Reglas de Negocio | 68 reglas (RN-001 … RN-068) |",
  "| **9** | Reglas de Negocio | 68 reglas declaradas en la v1.0 (RN-001 … RN-068; las tablas contienen 82: H-01 del SRS, DEC-03) + 3 incorporadas en la v1.1 (§9.15) |"),
 ("| `RN-nnn` | Regla de negocio | RN-001 … RN-068 |",
  "| `RN-nnn` | Regla de negocio | RN-001 … RN-068 (v1.0) · RN-081* … RN-083* (v1.1) |"),
 # ---------------------------------------------------------------- PN-01 (DF5-02, DF5-05)
 ("10. El sistema incrementa la existencia disponible de cada unidad de inventario `[MON §6]`.",
  "10. El sistema incrementa la existencia **en recepción** de cada unidad de inventario, en la ubicación de la zona de recepción; todavía no está disponible `[MON §6]` `[CD-16]` `[RN-081*]` `[DF5-02]`."),
 ("| E-07 | Sin conectividad durante la recepción | El registro se retiene localmente y se sincroniza al restablecerse; el documento no se confirma hasta sincronizar `[RN-054]`",
  "| E-07 | Sin conectividad durante la recepción | El registro se retiene localmente y se sincroniza al restablecerse, validándose de nuevo contra el estado vigente `[RN-083*]` `[DF5-05]`; el documento no se confirma hasta sincronizar `[RN-054]`"),
 ("La existencia disponible refleja exactamente la mercancía físicamente presente; existe un movimiento de entrada en el kardex",
  "La existencia **en recepción** refleja exactamente la mercancía físicamente recibida, y pasa a disponible al ubicarse (PN-03) `[DF5-02]`; existe un movimiento de entrada en el kardex"),
 # ---------------------------------------------------------------- PN-02 (DF5-01)
 ("1. El sistema genera un identificador QR único por unidad de inventario `[DC-08]` `[RN-015]`.",
  "1. El sistema genera un identificador QR único por **SKU + Lote** (la combinación referencia + talla + color + lote), no por ubicación `[DC-08]` `[RN-015]` `[DF5-01]`."),
 ("Toda unidad de inventario en bodega es identificable mediante escaneo. Ninguna existencia carece de identificador `[RN-015]`.",
  "Toda unidad de inventario en bodega es identificable mediante escaneo: el QR de su SKU + Lote más el identificador de su ubicación. Ninguna existencia carece de identificador `[RN-015]` `[DF5-01]`."),
 # ---------------------------------------------------------------- PN-03 (DF5-03)
 ("6. El sistema registra la asignación de ubicación.\n7. El sistema actualiza la existencia por ubicación.",
  "6. El sistema registra la primera ubicación como **movimiento interno** en el kardex, desde la ubicación de recepción hacia la ubicación destino, con qué, cuánto, quién, cuándo y el documento de entrada que la origina `[RN-082*]` `[DF5-03]`.\n"
  "7. La cantidad ubicada pasa de **en recepción** a **disponible** en la ubicación destino; la existencia total no cambia `[RN-026]` `[RN-082*]`."),
 ("| E-04 | Mercancía que se reparte en varias ubicaciones | Se registran asignaciones parciales hasta completar la cantidad `[NUEVO]` |",
  "| E-04 | Mercancía que se reparte en varias ubicaciones | Se registran asignaciones parciales —un movimiento interno por cada una— hasta completar la cantidad; el QR del SKU + Lote no cambia `[NUEVO]` `[DF5-01]` `[DF5-03]` |"),
 # ---------------------------------------------------------------- PN-05 (DF5-01, DF5-05)
 ("1. El Auxiliar escanea el identificador de la mercancía `[DC-08]`.\n2. El sistema muestra su ubicación actual y su existencia.",
  "1. El Auxiliar escanea el identificador de la mercancía `[DC-08]`, que identifica su SKU + Lote `[DF5-01]`.\n"
  "2. El sistema muestra las ubicaciones donde ese SKU + Lote tiene existencia; si hay más de una, el Auxiliar indica la de origen escaneando su identificador o seleccionándola, y la selección queda registrada `[RN-015]` `[DF5-01]`."),
 ("| E-06 | Sin conectividad | Se retiene localmente y sincroniza al restablecerse `[RN-054]` |",
  "| E-06 | Sin conectividad | Se retiene localmente y sincroniza al restablecerse `[RN-054]`; al sincronizar se valida de nuevo y, si ya no es válido, se rechaza y abre novedad `[RN-083*]` `[DF5-05]` |"),
 # ---------------------------------------------------------------- Catálogo (DF5-01)
 ("Es el nivel al que se registra existencia, se genera identificador QR, se ejecutan movimientos y se lleva kardex.",
  "Es el nivel al que se registra existencia, se ejecutan movimientos y se lleva kardex. **Se identifica por el QR de su SKU + Lote más su ubicación**: el QR no incluye la ubicación, de modo que un mismo SKU + Lote puede estar en varias ubicaciones sin generar otro QR `[DF5-01]`."),
 ("**Definición operativa:** código único, generado por el sistema, asociado a una unidad de inventario o a una ubicación.",
  "**Definición operativa:** código único, generado por el sistema, asociado a un **SKU + Lote** (QR de mercancía) o a una ubicación (QR de ubicación). El QR de mercancía **no identifica** ubicación, bodega ni cantidad `[DF5-01]`."),
 ("típicamente del proveedor, asociado a una unidad de inventario. Es admitido para lectura",
  "típicamente del proveedor, asociado al identificador QR de un SKU + Lote `[DF5-01]`. Es admitido para lectura"),
 # ---------------------------------------------------------------- M-06 (DF5-01)
 ("**Funciones:** generar identificador QR único para unidad de inventario ·",
  "**Funciones:** generar identificador QR único por SKU + Lote `[DF5-01]` ·"),
 ("consultar el historial de identificadores de una unidad.",
  "consultar el historial de identificadores de un SKU + Lote."),
 ("un identificador reemplazado conserva su vínculo histórico con la unidad `[RN-018]`",
  "un identificador reemplazado conserva su vínculo histórico con su SKU + Lote `[RN-018]`"),
 # ---------------------------------------------------------------- HU (DF5-01)
 ("*Criterios:* (1) El sistema genera un identificador único por unidad de inventario `[RN-016]`.",
  "*Criterios:* (1) El sistema genera un identificador único por SKU + Lote `[RN-016]` `[DF5-01]`."),
 ("(2) El sistema resuelve el identificador y muestra la unidad de inventario correspondiente.",
  "(2) El sistema resuelve el identificador y muestra el SKU + Lote y las ubicaciones donde tiene existencia `[DF5-01]`."),
 ("(4) El historial de identificadores de la unidad es consultable.",
  "(4) El historial de identificadores del SKU + Lote es consultable."),
 ("asociar el código de barras del proveedor a nuestra unidad de inventario **PARA**",
  "asociar el código de barras del proveedor a nuestro identificador QR de SKU + Lote **PARA**"),
 ("(2) Su lectura permite **consultar** la unidad.",
  "(2) Su lectura permite **consultar** el SKU + Lote."),
 ("(4) Un mismo código de barras no puede asociarse a dos unidades distintas.",
  "(4) Un mismo código de barras no puede asociarse a dos identificadores QR distintos `[DF5-01]`."),
 # ---------------------------------------------------------------- RF (DF5-01)
 ("| RF-040 | El sistema debe generar un identificador QR único por unidad de inventario | P0 | Coordinador | M-07 | `[DC-08]` |",
  "| RF-040 | El sistema debe generar un identificador QR único por SKU + Lote (no por ubicación) | P0 | Coordinador | M-07 | `[DC-08]` `[DF5-01]` |"),
 ("| RF-042 | El sistema debe permitir el escaneo de identificadores desde tablet y resolverlos a su unidad de inventario | P0 | Auxiliar | `[DC-05]` | `[DC-08]` |",
  "| RF-042 | El sistema debe permitir el escaneo de identificadores desde tablet y resolverlos a su SKU + Lote y, junto con la ubicación, a la unidad de inventario | P0 | Auxiliar | `[DC-05]` | `[DC-08]` `[DF5-01]` |"),
 # ---------------------------------------------------------------- RN (DF5-01)
 ("| **RN-015** | **Toda unidad de inventario debe tener un identificador activo.** No existe existencia sin identificador. | Estructural | `[DC-08]` |",
  "| **RN-015** | **Toda unidad de inventario debe tener un identificador activo.** No existe existencia sin identificador. El identificador de mercancía es el QR de su **SKU + Lote**; la unidad de inventario se determina con ese QR más su ubicación, obtenida por escaneo del QR de ubicación o por selección registrada. Si el SKU + Lote está en más de una ubicación y no se indica cuál, la operación no se registra. | Estructural | `[DC-08]` `[DF5-01]` |"),
 ("| **RN-017** | Un mismo identificador secundario de código de barras no puede asociarse a dos unidades de inventario distintas. | Estructural | `[DC-08]` |",
  "| **RN-017** | Un mismo identificador secundario de código de barras no puede asociarse a dos identificadores QR de mercancía distintos (es decir, a dos SKU + Lote distintos). | Estructural | `[DC-08]` `[DF5-01]` |"),
 # ---------------------------------------------------------------- Cap. 9 (numeración y nuevas reglas)
 ("La renumeración canónica es tarea de la primera revisión formal del documento con el Director, y debe hacerse en un solo acto para no fragmentar las referencias.\n",
  "La renumeración canónica es tarea de la primera revisión formal del documento con el Director, y debe hacerse en un solo acto para no fragmentar las referencias.\n\n"
  "**Versión 1.1.** Las reglas RN-081* a RN-083* (§9.15) se incorporan por el cierre del CP-04 y se numeran a continuación de RN-080 con el mismo criterio. El «total efectivo» de este apartado es el declarado en la v1.0; el recuento real de las tablas es 82 (H-01 del SRS, DEC-03 abierta) y, con la v1.1, **85**.\n"),
 ("> **Lectura del balance.** El 75 % de las reglas son estructurales e inviolables.",
  "> **Versión 1.1.** A esta tabla, que reproduce las cifras declaradas en la v1.0, se suman las 3 reglas estructurales de §9.15.\n\n"
  "> **Lectura del balance.** El 75 % de las reglas son estructurales e inviolables."),
 # ---------------------------------------------------------------- §13.7
 ("| 1.0 | 5 de septiembre de 2026 | Emisión inicial. Cubre los doce capítulos exigidos y el marco normativo. | Emitido para revisión del Director |",
  "| 1.0 | 5 de septiembre de 2026 | Emisión inicial. Cubre los doce capítulos exigidos y el marco normativo. | Emitido para revisión del Director |\n"
  "| 1.1 | 29 de septiembre de 2026 | Cierre del CP-04: decisiones DF5-01, DF5-02, DF5-03 y DF5-05 (ver «Control de cambios de la versión 1.1»); 3 reglas nuevas (§9.15) | Validado técnicamente; aprobación pendiente (DEC-01…DEC-09, HD-25) |"),
 ("| `COLBASOFT_SPEC v1.0` | **Este documento** — Fase 2 | Emitido |",
  "| `COLBASOFT_SPEC v1.1` | **Este documento** — Fase 2, revisado en el cierre del CP-04 | Validado técnicamente; aprobación pendiente |\n"
  "| `04_CP04_AUDITORIA/04_CP04_CIERRE.md` | Registro de las decisiones DF5 que originan la v1.1 | Emitido |"),
 ("*COLBASOFT_SPEC v1.0 — Especificación Funcional de Producto*\n*5 de septiembre de 2026*",
  "*COLBASOFT_SPEC v1.1 — Especificación Funcional de Producto*\n*5 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1)*"),
]

def main():
    txt = SRC.read_text(encoding="utf8")
    for old, new in R:
        n = txt.count(old)
        assert n == 1, f"se esperaba 1 ocurrencia y hay {n}: {old[:80]!r}"
        txt = txt.replace(old, new)
    # §9.15 va inmediatamente antes del Capítulo 10
    anchor = "\n---\n\n# CAPÍTULO 10"
    assert txt.count(anchor) == 1
    txt = txt.replace(anchor, "\n" + REGLAS_V11 + anchor)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(txt, encoding="utf8", newline="\n")
    print(OUT, len(txt), "chars", txt.count("\n"), "lines")

if __name__ == "__main__":
    main()
