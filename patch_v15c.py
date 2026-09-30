from patch_srs_lib import patch
S012 = """
## 0.12 Control de cambios de la versión 1.5 (validación con datos ficticios y corte C1, 30 de septiembre de 2026)

El Director decidió que **no habrá empresa piloto** y que el proyecto de grado se valida **solo con datos ficticios**; el asesor lo aceptó. También fijó el **corte de entrega C1** de noviembre de 2026. El SPEC v1.5 y el SRS v1.5 lo recogen antes.

| Decisión | Cambios en el modelo |
|---|---|
| Sin empresa piloto; validación con datos ficticios | **Ninguno** en entidades, agregados, invariantes, eventos ni términos. El riesgo **R-S01** (modelo TO-BE sin contraste con la operación real) deja de ser un pendiente y pasa a **limitación declarada** |
| Corte de entrega C1 (35 HU, 83 RF) | Ninguno en el modelo. El corte construye, entre otros, los agregados de unidad de inventario, movimiento, lote, documento de entrada, solicitud de salida, pieza y QR |

**Lo que el modelo sigue garantizando con datos ficticios:** kardex inmutable, existencia derivada, no-negativo y las invariantes IN-01…IN-79. No se modificó ningún ID.
"""
patch("build_f4.py", [
 ('(v1.2, v1.3 y v1.4)"', '(v1.2 a v1.5)"'),
 ('| **Versión** | 1.4 |', '| **Versión** | 1.5 |'),
 ('| **Estado** | **Borrador v1.4** (30-sep-2026): incorpora la trazabilidad por pieza (v1.2), las respuestas a DEC-02…DEC-09 (v1.3) y las de H-19, H-20, HD-29 y HD-30.', '| **Estado** | **Borrador v1.5** (30-sep-2026): incorpora la trazabilidad por pieza (v1.2), las respuestas a DEC-02…DEC-09 (v1.3), las de H-19, H-20, HD-29 y HD-30 (v1.4) y la validación con datos ficticios (v1.5).'),
 ('COLBASOFT_SPEC v1.4 → SRS_COLBASOFT v1.4 → **Modelo de Dominio v1.4**', 'COLBASOFT_SPEC v1.5 → SRS_COLBASOFT v1.5 → **Modelo de Dominio v1.5**'),
 ('El detalle está en DOMAIN_MODEL §0.11.\n"""', 'El detalle está en DOMAIN_MODEL §0.11.\n\n> **Versión 1.5.** Registra la validación con datos ficticios y el corte de entrega C1; sin cambios de contenido en el modelo. El detalle está en DOMAIN_MODEL §0.12.\n"""'),
 ('y el **0.11** los de la v1.4.', 'el **0.11** los de la v1.4 y el **0.12** los de la v1.5.'),
 ('| R-S01 |', '| R-S01 |') if False else ('*Fin de DOMAIN_MODEL v1.4.', '*Fin de DOMAIN_MODEL v1.5.'),
 ('*Fin de EVENT_CATALOG v1.4.*', '*Fin de EVENT_CATALOG v1.5.*'),
 ('*Fin de GLOSSARY v1.4.', '*Fin de GLOSSARY v1.5.'),
 ('**Estado frente a la Fase 5 (v1.4).**', '**Estado frente a la Fase 5 (v1.5).**'),
])
s = open("build_f4.py", encoding="utf8").read()
i = s.index("\n## 0.11 Control de cambios de la versión 1.4")
j = s.index("\n**ESTADO: CONTEXTO RECONSTRUIDO.**", i)
s = s[:j] + "\n" + S012 + s[j:]
open("build_f4.py", "w", encoding="utf8", newline="\n").write(s)
patch("xref.py", [('"SRS_COLBASOFT_v1.4.md"', '"SRS_COLBASOFT_v1.5.md"'), ('"COLBASOFT_SPEC_v1.4.md"', '"COLBASOFT_SPEC_v1.5.md"')])
