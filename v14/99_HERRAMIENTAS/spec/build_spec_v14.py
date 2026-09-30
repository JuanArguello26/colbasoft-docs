# -*- coding: utf-8 -*-
"""Genera COLBASOFT_SPEC_v1.4.md a partir de COLBASOFT_SPEC_v1.3.md (que no se modifica).

La v1.4 registra las respuestas del Director a H-19, H-20, HD-29 y HD-30 (30 de septiembre de 2026).
Cada cambio es un reemplazo exacto que debe encontrarse una sola vez en la v1.3; si no aparece, falla.

Uso: python build_spec_v14.py [carpeta_de_salida]   (por defecto, 01_SPEC_FASE_2 del proyecto)
"""
import sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "01_SPEC_FASE_2" / "COLBASOFT_SPEC_v1.3.md"
OUT_DIR = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "01_SPEC_FASE_2"
OUT = OUT_DIR / "COLBASOFT_SPEC_v1.4.md"

CAMBIOS = """
## Control de cambios de la versión 1.4

> La versión 1.4 registra las respuestas del Director del Proyecto a **H-19, H-20, HD-29 y HD-30** (30 de septiembre de 2026), todas en la opción recomendada tras verificarla contra las fuentes. Las versiones anteriores se conservan sin cambios.

| Asunto | Respuesta del Director | Qué cambia en el SPEC |
|---|---|---|
| **H-19** (HU-035 depende de HU-024, del Horizonte 2) | **(a)** En el Núcleo la ubicación se propone con una **regla fija** (zona por categoría, agrupación por referencia y mayor capacidad libre, en ese orden; si ninguna aplica, la zona de recepción). Los criterios configurables siguen en el Horizonte 2 | HU-035 (criterio 1), PN-03 (paso 1), RN-020 |
| **H-20** (RF-136 calcula los 24 KPI) | **(a)** Se acota el RF al Núcleo y se crea un RF para el resto | RF-136 (12 KPI del Núcleo: 01, 05, 08, 09, 11, 13, 14, 16, 17, 19, 21 y 24), **RF-185** nuevo en el Horizonte 2 (KPI-02, 03, 04, 06, 07, 10, 12, 15, 18, 20, 22 y 23), §12.3 elemento 15 |
| **HD-29** (corte parcial y movimiento parcial) | **(a)** Una pieza **no se divide**: el movimiento interno mueve la pieza completa y tomar una parte es un corte parcial (salida) | Nueva regla **RN-090*** (§9.18), HU-045 (criterio 2), PN-05 (paso 3), RF-166, CD-49 |
| **HD-30** (alcance del control por pieza) | **(a)** Toda la mercancía se controla por piezas; lo que llega suelto se registra como paquete o bolsa con su cantidad de unidades | RN-084* |

**Limitación conocida (HD-29).** Una parte de un paquete o bolsa de unidades **no puede trasladarse a otra ubicación** como movimiento interno, porque eso exigiría dividir la pieza. Se puede registrar como salida la parte que se toma. El Director puede reabrir la decisión con la información del levantamiento AS-IS (Q-04: frecuencia y forma de los cortes).

**Elementos nuevos.** **1 requisito funcional** (RF-185, Horizonte 2) y **1 regla estructural** (RN-090*). Ninguna historia nueva. El Núcleo no cambia (94 HU y 164 RF); el Completo pasa a 114 HU y 185 RF, y el Horizonte 2, de 20 a 21 RF. Las reglas pasan de 91 a **92**.

**Pendiente que sigue abierto:** HD-28 (identidad física de la pieza, contenedores con mezcla de lotes y reemplazo de QR), la aprobación formal de DEC-08 (acta firmada) y la verificación de campo de KPI-24.
"""

REGLA = """
## 9.18 Regla incorporada en la versión 1.4 (respuesta a HD-29)

> Esta regla **no forma parte de las 82** de §9.2–§9.12 ni de las de §9.15 y §9.16. Se numera a continuación de RN-089* con asterisco. Es estructural: no es parametrizable (DEC-04).

| ID | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-090*** | **Una pieza no se divide.** Un movimiento interno mueve la pieza completa; tomar una parte de una pieza es un corte parcial (RN-086*), que se registra como salida. La división de una pieza en dos no existe en el MVP | Estructural | `[HD-29]` `[F-3]` `[RN-086*]` |
"""

RF_185 = "| RF-185 | El sistema debe calcular los 12 indicadores restantes del Capítulo 10 (KPI-02, 03, 04, 06, 07, 10, 12, 15, 18, 20, 22 y 23), que el backlog ubica en el Horizonte 2 (§12.3, elemento 15) o que requieren el conteo general (KPI-02) | P1 | — | Cap. 10, RF-136 | `[NUEVO]` `[H-20]` |\n"


def block_end(txt, cap_marker, heading):
    c = txt.index(cap_marker)
    h = txt.index(heading, c)
    cands = [p for p in (txt.find("\n## M-", h + 5), txt.find("\n---\n", h + 5)) if p != -1]
    return min(cands)


R = [
 ("# COLBASOFT_SPEC v1.3\n", "# COLBASOFT_SPEC v1.4\n"),
 ("| **Versión** | 1.3 |", "| **Versión** | 1.4 |"),
 ("· 30 de septiembre de 2026 (v1.2 y v1.3) |", "· 30 de septiembre de 2026 (v1.2, v1.3 y v1.4) |"),
 ("| **Estado** | **Borrador v1.3** (30-sep-2026): registra las respuestas a DEC-01…DEC-09. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar (borrador en `05_V13_DECISIONES/`) y pendientes HD-28, HD-29, HD-30, H-19 y H-20 |",
  "| **Estado** | **Borrador v1.4** (30-sep-2026): registra las respuestas a DEC-01…DEC-09, H-19, H-20, HD-29 y HD-30. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar (borrador en `05_V13_DECISIONES/`), HD-28 y la verificación de campo de KPI-24 |"),
 ("| **Versión anterior** | `COLBASOFT_SPEC_v1.2.md` (30-sep-2026), `COLBASOFT_SPEC_v1.1.md` (29-sep-2026) y `COLBASOFT_SPEC_v1.0.md` (5-sep-2026), conservadas sin cambios |",
  "| **Versión anterior** | `COLBASOFT_SPEC_v1.3.md`, `COLBASOFT_SPEC_v1.2.md` (30-sep-2026), `COLBASOFT_SPEC_v1.1.md` (29-sep-2026) y `COLBASOFT_SPEC_v1.0.md` (5-sep-2026), conservadas sin cambios |"),
 ("\n## Control de cambios de la versión 1.3\n", CAMBIOS + "\n## Control de cambios de la versión 1.3\n"),
 ("| **7** | Requisitos Funcionales | 184 requisitos (RF-001 … RF-184) |", "| **7** | Requisitos Funcionales | 185 requisitos (RF-001 … RF-185) |"),
 ("+ 6 incorporadas en la v1.2 (§9.16) |", "+ 6 incorporadas en la v1.2 (§9.16) + 1 incorporada en la v1.4 (§9.18) |"),
 ("| `RF-nnn` | Requisito funcional | RF-001 … RF-184 (corregido en la v1.3, §9.17) |", "| `RF-nnn` | Requisito funcional | RF-001 … RF-185 (corregido en la v1.3, §9.17) |"),
 ("· RN-084* … RN-089* (v1.2) |", "· RN-084* … RN-089* (v1.2) · RN-090* (v1.4) |"),
 # ---- H-19
 ("1. El sistema propone una ubicación destino según criterios configurados: zona por categoría, ubicación con capacidad, agrupación por referencia `[NUEVO]`.",
  "1. El sistema propone una ubicación destino con una regla fija en el Núcleo: zona por categoría, agrupación por referencia y mayor capacidad libre, en ese orden; si ninguna aplica, propone la zona de recepción. Los criterios configurables son del Horizonte 2 (HU-024) `[NUEVO]` `[H-19]`."),
 ("(1) El sistema propone ubicación según los criterios de HU-024.",
  "(1) El sistema propone la ubicación con una regla fija —zona por categoría, agrupación por referencia y mayor capacidad libre, en ese orden—; si ninguna aplica, propone la zona de recepción `[RN-020]` `[H-19]`."),
 ("| **RN-020** | El sistema **propone** la ubicación destino según los criterios configurados; el Auxiliar **confirma o desvía**. La propuesta nunca es una imposición. | Configurable | `[NUEVO]` |",
  "| **RN-020** | El sistema **propone** la ubicación destino según los criterios vigentes —en el Núcleo, una regla fija: zona por categoría, agrupación por referencia y mayor capacidad libre; configurables desde el Horizonte 2 (HU-024)—; el Auxiliar **confirma o desvía**. La propuesta nunca es una imposición. | Configurable | `[NUEVO]` `[H-19]` |"),
 # ---- H-20
 ("| RF-136 | El sistema debe calcular los 24 indicadores definidos en el Capítulo 10 | P1 | — | Cap. 10 | `[MON §8.2]` |",
  "| RF-136 | El sistema debe calcular los 12 indicadores del Núcleo definidos en el Capítulo 10 (KPI-01, 05, 08, 09, 11, 13, 14, 16, 17, 19, 21 y 24); los otros 12 son el RF-185 | P1 | — | Cap. 10 | `[MON §8.2]` `[H-20]` |"),
 ("| 15 | KPIs 03, 04, 06, 07, 10, 12, 15, 18, 20, 22, 23 | M-16 | Los tres KPIs del compromiso ya están en el MVP | `[NUEVO]` |",
  "| 15 | KPIs 02, 03, 04, 06, 07, 10, 12, 15, 18, 20, 22, 23 (RF-185) | M-16 | Los tres KPIs del compromiso ya están en el MVP; KPI-02 requiere el conteo general | `[NUEVO]` `[H-20]` |"),
 ("| M-16 Reportes | 7 | RF-134–140 | 1 | 4 | 2 | 0 |", "| M-16 Reportes | 8 | RF-134–140, RF-185 | 1 | 5 | 2 | 0 |"),
 ("> **184 requisitos funcionales**, numerados RF-001 a RF-184 y agrupados por módulo.", "> **185 requisitos funcionales**, numerados RF-001 a RF-185 y agrupados por módulo."),
 ("| **Total** | **184** | | **80** | **82** | **22** | **0** |", "| **Total** | **185** | | **80** | **83** | **22** | **0** |"),
 ("| 7 | Requisitos funcionales | 184 |", "| 7 | Requisitos funcionales | 185 |"),
 # ---- HD-29
 ("(2) Se puede mover cantidad total o parcial.", "(2) Se mueve la pieza completa: una pieza no se divide, y tomar una parte de ella es un corte parcial que se registra como salida `[RN-090*]` `[HD-29]`."),
 ("El movimiento parcial de una pieza entre ubicaciones es DECISIÓN PENDIENTE (HD-29) `[NUEVO]`.",
  "La pieza se mueve completa: no se divide, y tomar una parte de ella es un corte parcial que se registra como salida (PN-10) `[RN-090*]` `[HD-29]` `[NUEVO]`."),
 ("| RF-072, RF-163 | `[F-4]` `[RN-087*]` |", "| RF-072, RF-163 | `[F-4]` `[RN-087*]` `[RN-090*]` |"),
 ("un corte parcial la reduce y la deja con su remanente `[F-3]`. `[Q-11]` `[RN-084*]` `[RN-085*]`",
  "un corte parcial la reduce y la deja con su remanente `[F-3]`. **No se divide en dos** `[RN-090*]` `[HD-29]`. `[Q-11]` `[RN-084*]` `[RN-085*]`"),
 # ---- HD-30
 ("el QR sigue identificando SKU + Lote | Estructural | `[Q-11]` `[F-1]` `[F-2]` `[F-6]` `[CD-49]` |",
  "el QR sigue identificando SKU + Lote. **Sin excepción**: la mercancía que llega suelta se registra como paquete o bolsa con su cantidad de unidades `[HD-30]` | Estructural | `[Q-11]` `[F-1]` `[F-2]` `[F-6]` `[CD-49]` `[HD-30]` |"),
 # ---- fe de erratas
 ("el total vigente es **91: 69 estructurales y 22 configurables** |", "el total vigente es **91: 69 estructurales y 22 configurables**; con la de §9.18 (v1.4), **92: 70 estructurales y 22 configurables** |"),
 ("Los rangos vigentes son `HU-001…HU-114` y `RF-001…RF-184` (hallazgo H-03 del SRS)", "Los rangos vigentes son `HU-001…HU-114` y `RF-001…RF-185` (hallazgo H-03 del SRS)"),
 ("| **HD-29** | Qué ocurre con el remanente", "| **HD-29** *(resuelto en la v1.4)* | Qué ocurre con el remanente"),
 ("| **HD-30** | Si toda referencia", "| **HD-30** *(resuelto en la v1.4)* | Si toda referencia"),
 ("**Pendientes que siguen abiertos** (no se inventa ninguna respuesta): HD-28, HD-29 y HD-30 del modelo de dominio; los hallazgos H-19 y H-20 del SRS;",
  "**Pendientes que siguen abiertos** (no se inventa ninguna respuesta; HD-29, HD-30, H-19 y H-20 se resolvieron en la v1.4): HD-28 del modelo de dominio;"),
 # ---- cap. 13
 ("| 1.3 | 30 de septiembre de 2026 | Respuestas a DEC-02…DEC-09 (ver «Control de cambios de la versión 1.3»); 4 HU y 13 RF nuevos; fe de erratas de las reglas (§9.17) | Borrador; validación técnica y acta de DEC-08 pendientes |",
  "| 1.3 | 30 de septiembre de 2026 | Respuestas a DEC-02…DEC-09 (ver «Control de cambios de la versión 1.3»); 4 HU y 13 RF nuevos; fe de erratas de las reglas (§9.17) | Borrador; conservada sin cambios |\n"
  "| 1.4 | 30 de septiembre de 2026 | Respuestas a H-19, H-20, HD-29 y HD-30 (ver «Control de cambios de la versión 1.4»); 1 RF y 1 regla nuevos | Borrador; validación técnica y acta de DEC-08 pendientes |"),
 ("| `COLBASOFT_SPEC v1.3` | **Este documento** — Fase 2, con las respuestas a DEC-02…DEC-09 | Borrador; aprobación pendiente |",
  "| `COLBASOFT_SPEC v1.4` | **Este documento** — Fase 2, con las respuestas a H-19, H-20, HD-29 y HD-30 | Borrador; aprobación pendiente |\n| `COLBASOFT_SPEC v1.3` | Versión anterior — respuestas a DEC-02…DEC-09 | Borrador; conservada sin cambios |"),
 ("*COLBASOFT_SPEC v1.3 — Especificación Funcional de Producto*", "*COLBASOFT_SPEC v1.4 — Especificación Funcional de Producto*"),
 ("· 30 de septiembre de 2026 (v1.2 y v1.3)*", "· 30 de septiembre de 2026 (v1.2, v1.3 y v1.4)*"),
]


def main():
    txt = SRC.read_text(encoding="utf8")
    for old, new in R:
        n = txt.count(old)
        assert n == 1, f"se esperaba 1 ocurrencia y hay {n}: {old[:90]!r}"
        txt = txt.replace(old, new)
    anchor = "\n---\n\n# CAPÍTULO 10"
    assert txt.count(anchor) == 1
    txt = txt.replace(anchor, "\n" + REGLA + anchor)
    p = block_end(txt, "# CAPÍTULO 7", "## M-16 · Reportes y Exportación Analítica")
    assert txt[:p].endswith("|\n")
    txt = txt[:p] + RF_185 + txt[p:]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(txt, encoding="utf8", newline="\n")
    print(OUT, len(txt), "chars", txt.count("\n"), "lines")


if __name__ == "__main__":
    main()
