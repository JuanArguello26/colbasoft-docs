# -*- coding: utf-8 -*-
"""Genera COLBASOFT_SPEC_v1.5.md a partir de COLBASOFT_SPEC_v1.4.md (que no se modifica).

La v1.5 registra las decisiones del Director del 30 de septiembre de 2026 sobre la validación del proyecto
de grado (sin empresa piloto; datos ficticios) y el corte de entrega C1 de noviembre de 2026. Cada cambio
es un reemplazo exacto que debe encontrarse una sola vez en la v1.4; si no aparece, el script falla.

Uso: python build_spec_v15.py [carpeta_de_salida]   (por defecto, 01_SPEC_FASE_2 del proyecto)
"""
import sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "01_SPEC_FASE_2" / "COLBASOFT_SPEC_v1.4.md"
OUT_DIR = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "01_SPEC_FASE_2"
OUT = OUT_DIR / "COLBASOFT_SPEC_v1.5.md"

# Corte de entrega C1 (noviembre de 2026): HU y RF con su ID del SPEC, por bloque de construcción.
C1_BLOQUES = [
 ("C1-1", "Fundación", ["HU-001", "HU-002", "HU-005", "HU-006", "HU-010", "HU-011", "HU-020", "HU-021", "HU-098", "HU-099", "HU-094"]),
 ("C1-2", "Identificación y lotes", ["HU-025", "HU-026", "HU-016"]),
 ("C1-3", "Entradas, piezas y ubicación", ["HU-030", "HU-031", "HU-032", "HU-033", "HU-035", "HU-104"]),
 ("C1-4", "Kardex y consulta de existencia", ["HU-077", "HU-078", "HU-110", "HU-071", "HU-072", "HU-073"]),
 ("C1-5", "Movimientos internos", ["HU-045", "HU-046", "HU-106"]),
 ("C1-6", "Salidas y corte parcial", ["HU-038", "HU-039", "HU-040", "HU-041", "HU-107", "HU-108"]),
]
C1_RF = [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 16, 17, 18, 19, 20, 26, 27, 28, 32, 33, 34, 35, 36, 40, 41, 42, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 65, 67, 68, 69, 72, 73, 74, 75, 76, 77, 112, 113, 114, 115, 116, 119, 120, 121, 122, 123, 124, 145, 146, 147, 152, 153, 154, 155, 156, 163, 164, 166, 167, 168, 170, 171, 172, 176, 178, 179, 180, 181]
assert len(C1_RF) == 83 and sum(len(b[2]) for b in C1_BLOQUES) == 35


def _rango(nums):
    """Compacta [1,2,3,5] en 'RF-001–003, RF-005'."""
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(f"RF-{nums[i]:03d}" if i == j else f"RF-{nums[i]:03d}–{nums[j]:03d}")
        i = j + 1
    return ", ".join(out)


SEC_12_7 = """
## 12.7 Corte de entrega C1 — noviembre de 2026

> `[v1.5]` Es un **corte de entrega dentro del Horizonte 1**, no un nuevo horizonte: no cambia el Núcleo (94 HU y 164 RF), que sigue siendo el umbral aprobatorio `[DEC-01]`. Fija qué se construye primero para el MVP de noviembre de 2026 y en qué orden.

**Criterio del corte.** Historias *Must* (P0) del Horizonte 1 de los módulos M-01 a M-09, M-13, M-14 y M-19, más sus dependencias y el registro de bitácora (HU-094, que exige el criterio 3 de HU-001). Resultado: **35 historias (33 P0 y 2 P1) y 83 requisitos funcionales**, sin ningún elemento del Horizonte 2. Ninguna historia del corte depende de otra que esté fuera de él.

| Bloque | Contenido | Historias |
|---|---|---|
"""

SEC_12_7_POST = """
**Requisitos funcionales del corte (83):** {rfs}.

**Orden de construcción y regla de recorte.** Los bloques se construyen en el orden C1-1 a C1-6. Si el tiempo no alcanza, **se recorta desde el último bloque hacia atrás**: C1-6 es el primero en salir, y cada bloque completo entrega un ciclo verificable. Ningún bloque se entrega a medias.

**Queda fuera del corte C1** (sigue en el Núcleo, para después de noviembre): ajustes (M-10), conteos (M-11), novedades (M-12), alertas (M-15), reportes e indicadores (M-16), dashboard (M-17), tareas y notificaciones (M-20), el registro de contenedores y bolsas agrupadas (HU-105), el movimiento interno interrumpido en tránsito (HU-111) y el cierre operativo de jornada (HU-113, HU-114).

## 12.8 Marco de validación del proyecto de grado — datos ficticios

> `[v1.5]` El 30 de septiembre de 2026 el Director decidió que **no habrá empresa piloto** en el proyecto de grado y que la validación se hará **solo con datos ficticios**. El asesor académico lo conoce y lo aceptó.

**Lectura de las referencias a la «empresa piloto».** Mientras no exista una empresa real, toda referencia de este documento a «empresa piloto», «piloto», «período de prueba», «verificación de campo» o «línea base de la empresa» se lee como **conjunto de datos ficticios de prueba (DS-1)**: datos aleatorios y verosímiles, preparados en una hoja de Excel y **cargados en una base de datos real**; el Excel **no** es la base de datos del sistema. DS-1 no contiene precios, clientes ni proveedores `[DC-03]` ni nombra ninguna empresa `[DC-01]`.

| Se puede afirmar | No se puede afirmar |
|---|---|
| Que el sistema cumple sus requisitos funcionales, sus reglas de negocio y los criterios de aceptación ejecutables con DS-1 | Reducción de errores, ganancia de trazabilidad o de productividad **medidas en una operación real** |
| Que conserva la integridad (kardex inmutable, existencia derivada, no-negativo) bajo las pruebas | Que los procesos TO-BE coincidan con los de una empresa concreta (S-2, R-S01) |
| Que puede operarse desde una tablet con los flujos del Núcleo | Que el personal de una empresa lo adopte (KPI-24 sin verificación de campo) |

**Limitación declarada.** Sin AS-IS ni línea base (V-01, V-03 y V-06 no aplican) el proyecto **no demuestra impacto medido**; demuestra **viabilidad funcional**. Esta limitación debe figurar en el informe final. Si más adelante aparece una empresa, se retoma el kit de levantamiento (`06_ASIS_KIT/`) y este marco se revisa.
"""

CAMBIOS = """
## Control de cambios de la versión 1.5

> La versión 1.5 registra las decisiones del Director del **30 de septiembre de 2026** sobre la validación del proyecto de grado y la entrega de noviembre. Las versiones anteriores se conservan sin cambios. El SPEC **no** contiene tecnologías: la pila tecnológica se registra en un documento de la Fase 5 (`07_FASE_5_ARQUITECTURA/ADR-001_PILA_TECNOLOGICA.md`).

| Decisión | Qué cambia en el SPEC |
|---|---|
| **Sin empresa piloto; validación solo con datos ficticios** (el asesor lo aceptó). El Excel con datos aleatorios es solo una **carga de datos de prueba** a una base de datos real | Nuevo §12.8 (marco de validación y regla de lectura de «empresa piloto»); §13.6 asuntos 4, 5 y 6 |
| **Corte de entrega C1 (noviembre de 2026)**: 35 HU y 83 RF, por bloques y con regla de recorte | Nuevo §12.7 |
| **H-19 (corrección de trazabilidad en el SRS)** | La dependencia de HU-035 respecto de HU-024 desaparece en el SRS: ya estaba resuelta en el SPEC v1.4 (H-19) |

**Lo que la v1.5 no cambia.** Las historias (114), los requisitos (185), las reglas (92), los KPI, los horizontes, el Núcleo (umbral aprobatorio) ni el alcance constitucional. **No cambia DC-01**: la empresa sigue sin nombrarse porque no existe.

**Pendientes que siguen abiertos:** acta firmada de DEC-08, HD-28, y el efecto de no tener AS-IS sobre S-2 y R-S01, que ahora se **declaran como limitación** en lugar de pendientes.
"""

R = [
 ("# COLBASOFT_SPEC v1.4\n", "# COLBASOFT_SPEC v1.5\n"),
 ("| **Versión** | 1.4 |", "| **Versión** | 1.5 |"),
 ("· 30 de septiembre de 2026 (v1.2, v1.3 y v1.4) |", "· 30 de septiembre de 2026 (v1.2 a v1.5) |"),
 ("| **Estado** | **Borrador v1.4** (30-sep-2026): registra las respuestas a DEC-01…DEC-09, H-19, H-20, HD-29 y HD-30. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar (borrador en `05_V13_DECISIONES/`), HD-28 y la verificación de campo de KPI-24 |",
  "| **Estado** | **Borrador v1.5** (30-sep-2026): registra la validación con datos ficticios y el corte de entrega C1. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar (borrador en `05_V13_DECISIONES/`) y HD-28 |"),
 ("| **Versión anterior** | `COLBASOFT_SPEC_v1.3.md`,", "| **Versión anterior** | `COLBASOFT_SPEC_v1.4.md`, `COLBASOFT_SPEC_v1.3.md`,"),
 ("\n## Control de cambios de la versión 1.4\n", CAMBIOS + "\n## Control de cambios de la versión 1.4\n"),
 ("| 4 | Autorización de contacto con empresas reales | V-01 | **Fase 3 completa** |", "| 4 | Autorización de contacto con empresas reales | V-01 | **No aplica en el proyecto de grado (v1.5, §12.8)**; se retoma si aparece una empresa |"),
 ("| 5 | Levantamiento de la línea base | V-03 | **Demostración de impacto** |", "| 5 | Levantamiento de la línea base | V-03 | **No se levantará en el proyecto de grado (v1.5, §12.8)**: el impacto no se mide en campo |"),
 ("| 6 | Qué ocurre si el piloto no alcanza las cifras citadas | V-06 | Criterio de aprobación |", "| 6 | Qué ocurre si el piloto no alcanza las cifras citadas | V-06 | **No aplica: no hay piloto (v1.5, §12.8)** |"),
 ("| 1.4 | 30 de septiembre de 2026 | Respuestas a H-19, H-20, HD-29 y HD-30 (ver «Control de cambios de la versión 1.4»); 1 RF y 1 regla nuevos | Borrador; validación técnica y acta de DEC-08 pendientes |",
  "| 1.4 | 30 de septiembre de 2026 | Respuestas a H-19, H-20, HD-29 y HD-30 (ver «Control de cambios de la versión 1.4»); 1 RF y 1 regla nuevos | Borrador; conservada sin cambios |\n"
  "| 1.5 | 30 de septiembre de 2026 | Validación con datos ficticios (§12.8) y corte de entrega C1 de noviembre (§12.7); ver «Control de cambios de la versión 1.5» | Borrador; validación técnica y acta de DEC-08 pendientes |"),
 ("| `COLBASOFT_SPEC v1.4` | **Este documento** — Fase 2, con las respuestas a H-19, H-20, HD-29 y HD-30 | Borrador; aprobación pendiente |",
  "| `COLBASOFT_SPEC v1.5` | **Este documento** — Fase 2, con la validación con datos ficticios y el corte C1 | Borrador; aprobación pendiente |\n| `COLBASOFT_SPEC v1.4` | Versión anterior — respuestas a H-19, H-20, HD-29 y HD-30 | Borrador; conservada sin cambios |"),
 ("*COLBASOFT_SPEC v1.4 — Especificación Funcional de Producto*", "*COLBASOFT_SPEC v1.5 — Especificación Funcional de Producto*"),
 ("· 30 de septiembre de 2026 (v1.2, v1.3 y v1.4)*", "· 30 de septiembre de 2026 (v1.2 a v1.5)*"),
]


def main():
    txt = SRC.read_text(encoding="utf8")
    for old, new in R:
        n = txt.count(old)
        assert n == 1, f"se esperaba 1 ocurrencia y hay {n}: {old[:90]!r}"
        txt = txt.replace(old, new)
    tabla = "\n".join(f"| **{b}** | {n} | {', '.join(h)} |" for b, n, h in C1_BLOQUES)
    sec = SEC_12_7 + tabla + "\n" + SEC_12_7_POST.replace("{rfs}", _rango(C1_RF))
    anchor = "\n---\n\n# CAPÍTULO 13"
    assert txt.count(anchor) == 1
    txt = txt.replace(anchor, "\n" + sec.rstrip("\n") + "\n" + anchor)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(txt, encoding="utf8", newline="\n")
    print(OUT, len(txt), "chars", txt.count("\n"), "lines")


if __name__ == "__main__":
    main()
