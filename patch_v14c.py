from patch_srs_lib import patch

S011 = """
## 0.11 Control de cambios de la versión 1.4 (respuestas a H-19, H-20, HD-29 y HD-30, 30 de septiembre de 2026)

El Director respondió H-19, H-20, HD-29 y HD-30 en la opción (a), tras verificarla contra las fuentes. El SPEC v1.4 y el SRS v1.4 las recogen antes.

| Asunto | Respuesta | Cambios en el modelo |
|---|---|---|
| **H-19** | Regla fija de propuesta de ubicación en el Núcleo | Ninguno en entidades; cambia el texto de RN-MOV-001 (vía el SRS) |
| **H-20** | RF-REP-003 acotado a 12 KPI; RF-REP-008 para los otros 12 | Ninguno en el dominio |
| **HD-29** | Una pieza no se divide | Regla RN-MOV-012 → **IN-79**; AG-22, E-27, EV-MOV-001, EV-INV-001; **HD-29 resuelto** |
| **HD-30** | Toda la mercancía se controla por piezas | IN-73 (texto); **HD-30 resuelto** |

**Limitación conocida (HD-29).** Una parte de un paquete o bolsa de unidades no puede trasladarse a otra ubicación como movimiento interno, porque exigiría dividir la pieza. Se puede reabrir con el levantamiento AS-IS (Q-04).

**Ningún ID se renumeró ni se reutilizó.** Elemento nuevo: IN-79. Las reglas del SRS pasan de 91 a 92; la nueva es una invariante. Pendiente solo **HD-28**.
"""

patch("dm_data.py", [
 ('"No se decide. El modelo solo admite el corte como salida (RN-SAL-008) y el movimiento interno de la pieza completa (RN-MOV-011); no define la división de una pieza en dos.",\n  "Director — decidir · **Información requerida:** Q-04 (frecuencia y forma de los cortes). Decidir antes del detalle de movimientos de la Fase 5"),',
  '"**Resuelto (opción a, v1.4):** una pieza no se divide. El movimiento interno mueve la pieza completa y tomar una parte de ella es un corte parcial, que se registra como salida (RN-SAL-008, RN-MOV-012 → IN-79). **Limitación conocida:** una parte de un paquete o bolsa de unidades no puede trasladarse a otra ubicación como movimiento interno. Se puede reabrir con el AS-IS (Q-04).",\n  "**Resuelto — HD-29 (a), v1.4**"),'),
 ('"No se decide. El modelo aplica la regla a toda la mercancía (RN-LOT-006) y registra un paquete, bolsa o contenedor agrupado como una pieza con su cantidad de unidades.",\n  "Director — decidir · **Información requerida:** AS-IS (qué mercancía llega suelta). No bloquea la Fase 5 por sí mismo"),',
  '"**Resuelto (opción a, v1.4):** toda la mercancía se controla por piezas, sin excepción (RN-LOT-006, IN-73); lo que llega suelto se registra como paquete o bolsa con su cantidad de unidades.",\n  "**Resuelto — HD-30 (a), v1.4**"),'),
 ('es una invariante entre agregados (RF5-15).", ["IN-73", "IN-74", "IN-75", "IN-76", "IN-77", "IN-78"],', 'es una invariante entre agregados (RF5-15).", ["IN-73", "IN-74", "IN-75", "IN-76", "IN-77", "IN-78", "IN-79"],'),
 ('el QR no la identifica, tiene identidad interna.", ["RN-LOT-006"], "AG-22 / AG-08", "Estructural"),', 'el QR no la identifica, tiene identidad interna. Sin excepción: lo que llega suelto se registra como paquete o bolsa con su cantidad de unidades (HD-30).", ["RN-LOT-006"], "AG-22 / AG-08", "Estructural"),'),
 ('y la cantidad contada de la unidad de inventario es la suma de sus piezas.", ["RN-CNT-009"], "AG-12 / AG-22", "Estructural"),\n]',
  'y la cantidad contada de la unidad de inventario es la suma de sus piezas.", ["RN-CNT-009"], "AG-12 / AG-22", "Estructural"),\n # --- v1.4: respuesta a HD-29 (regla nueva del SPEC v1.4 §9.18)\n ("IN-79", "Una pieza no se divide: un movimiento interno mueve la pieza completa y tomar una parte de ella es un corte parcial, que se registra como salida; la división de una pieza en dos no existe.", ["RN-MOV-012"], "AG-22 / AG-06", "Estructural"),\n]'),
 ('El movimiento parcial de una pieza entre ubicaciones y el destino del remanente de un corte parcial están pendientes (HD-29)."', 'Una pieza no se divide: el movimiento interno la mueve completa y el remanente de un corte sigue siendo la misma pieza (HD-29, RN-MOV-012)."'),
 ('rn=["RN-LOT-006", "RN-LOT-007", "RN-SAL-008", "RN-MOV-011", "RN-SAL-009", "RN-CNT-009", "RN-MAE-007"]),', 'rn=["RN-LOT-006", "RN-LOT-007", "RN-SAL-008", "RN-MOV-011", "RN-MOV-012", "RN-SAL-009", "RN-CNT-009", "RN-MAE-007"]),'),
])
patch("ev_data.py", [
 ('rn="RN-MOV-004, RN-MOV-005, RN-INT-002, RN-EXI-003, RN-MOV-011"', 'rn="RN-MOV-004, RN-MOV-005, RN-INT-002, RN-EXI-003, RN-MOV-011, RN-MOV-012"'),
 ('rn="RN-MOV-010, RN-MOV-004, RN-EXI-002, RN-MOV-002, RN-MOV-001, RN-MOV-011"', 'rn="RN-MOV-010, RN-MOV-004, RN-EXI-002, RN-MOV-002, RN-MOV-001, RN-MOV-011, RN-MOV-012"'),
])
patch("build_f4.py", [
 ('(v1.2 y v1.3)"', '(v1.2, v1.3 y v1.4)"'),
 ('| **Versión** | 1.3 |', '| **Versión** | 1.4 |'),
 ('| **Estado** | **Borrador v1.3** (30-sep-2026): incorpora la trazabilidad por pieza (v1.2) y las respuestas a DEC-02…DEC-09.', '| **Estado** | **Borrador v1.4** (30-sep-2026): incorpora la trazabilidad por pieza (v1.2), las respuestas a DEC-02…DEC-09 (v1.3) y las de H-19, H-20, HD-29 y HD-30.'),
 ('COLBASOFT_SPEC v1.3 → SRS_COLBASOFT v1.3 → **Modelo de Dominio v1.3**', 'COLBASOFT_SPEC v1.4 → SRS_COLBASOFT v1.4 → **Modelo de Dominio v1.4**'),
 ('El detalle está en DOMAIN_MODEL §0.10.\n"""', 'El detalle está en DOMAIN_MODEL §0.10.\n\n> **Versión 1.4.** Incorpora las respuestas a H-19, H-20, HD-29 y HD-30. El detalle está en DOMAIN_MODEL §0.11.\n"""'),
 ('114 HU, 184 RF, 91 RN en la v1.3)', '114 HU, 185 RF, 92 RN en la v1.4)'),
 ('nuevo HD-29 |', 'HD-29 (resuelto en la v1.4) |'),
 ('(82 + 3 de la v1.1 + 6 de la v1.2: IN-70…IN-78)', '(82 + 3 de la v1.1 + 6 de la v1.2 + 1 de la v1.4: IN-70…IN-79)'),
 ('"HD-25 y HD-22 resueltos en la v1.2; HD-28, HD-29 y HD-30 pendientes, sin bloquear la arquitectura por sí mismos"', '"HD-25 y HD-22 resueltos en la v1.2; HD-29 y HD-30 en la v1.4; HD-28 pendiente, sin bloquear la arquitectura por sí mismo"'),
 ('(cierre del CP-04 y decisiones del 30-sep-2026, v1.2 y v1.3):', '(cierre del CP-04 y decisiones del 30-sep-2026, v1.2, v1.3 y v1.4):'),
 ('*Fin de DOMAIN_MODEL v1.3.', '*Fin de DOMAIN_MODEL v1.4.'),
 ('*Fin de EVENT_CATALOG v1.3.*', '*Fin de EVENT_CATALOG v1.4.*'),
 ('*Fin de GLOSSARY v1.3.', '*Fin de GLOSSARY v1.4.'),
 ('| V-5 | Las {len(S["RN"])} reglas del SRS (82 + 3 de la v1.1 + 6 de la v1.2) quedan', '| V-5 | Las {len(S["RN"])} reglas del SRS (82 + 3 de la v1.1 + 6 de la v1.2 + 1 de la v1.4) quedan'),
 ('| V-8 | RF con evento | 🟡 {rf_cov}/184 (', '| V-8 | RF con evento | 🟡 {rf_cov}/185 ('),
 ('**Estado frente a la Fase 5 (v1.3).**', '**Estado frente a la Fase 5 (v1.4).**'),
 ('**HD-28, HD-29 y HD-30** quedan pendientes, junto con HD-17', '**HD-29 y HD-30** se resolvieron en la v1.4; **HD-28** queda pendiente, junto con HD-17'),
])
s = open("build_f4.py", encoding="utf8").read()
i = s.index("\n## 0.10 Control de cambios de la versión 1.3")
j = s.index("\n**ESTADO: CONTEXTO RECONSTRUIDO.**", i)
s = s[:j] + "\n" + S011 + s[j:]
s = s.replace("el **0.10** los de la v1.3.", "el **0.10** los de la v1.3 y el **0.11** los de la v1.4.")
open("build_f4.py", "w", encoding="utf8", newline="\n").write(s)
patch("xref.py", [('"SRS_COLBASOFT_v1.3.md"', '"SRS_COLBASOFT_v1.4.md"'), ('"COLBASOFT_SPEC_v1.3.md"', '"COLBASOFT_SPEC_v1.4.md"')])
print("ok")
