from patch_srs_lib import patch

patch("ids.py", [('"RN-035","RN-082*","RN-087*"])', '"RN-035","RN-082*","RN-087*","RN-090*"])')])
patch("trace.py", [
 ("172:[35],173:[111],", "172:[35],173:[111],"),
 ("182:[113],183:[113],184:[114],\n}", "182:[113],183:[113],184:[114],185:[65],\n}"),
 ('"KPI-02":[103,105,136,175],', '"KPI-02":[103,105,185,175],'),
 ('"KPI-03":[93,104,136],', '"KPI-03":[93,104,185],'),
 ('"KPI-04":[99,136],', '"KPI-04":[99,185],'),
 ('"KPI-06":[100,136],', '"KPI-06":[100,185],'),
 ('"KPI-07":[42,136,179],', '"KPI-07":[42,185,179],'),
 ('"KPI-10":[39,136,172],', '"KPI-10":[39,185,172],'),
 ('"KPI-12":[48,58,136,180],', '"KPI-12":[48,58,185,180],'),
 ('"KPI-15":[79,81,136],', '"KPI-15":[79,81,185],'),
 ('"KPI-18":[36,115,136],', '"KPI-18":[36,115,185],'),
 ('"KPI-20":[131,133,136],', '"KPI-20":[131,133,185],'),
 ('"KPI-22":[66,86,90,136],', '"KPI-22":[66,86,90,185],'),
 ('"KPI-23":[106,109,111,136],', '"KPI-23":[106,109,111,185],'),
 ('    if r == "RF-136":', '    if r in ("RF-136", "RF-185"):'),
 ("171:\"CD-49, CD-18\",\n172:", "171:\"CD-49, CD-18\",\n172:"),
 ('182:"PN-14",183:"PN-14",184:"PN-14",\n}', '182:"PN-14",183:"PN-14",184:"PN-14",185:"CD-43",\n}'),
 ("assert len(RF_CD) == 184", "assert len(RF_CD) == 185"),
 ("_H2_RF = [24,30,31,39,47,78,79,80,81,82,91,103,104,117,133,137,140,143,161,175]", "_H2_RF = [24,30,31,39,47,78,79,80,81,82,91,103,104,117,133,137,140,143,161,175,185]"),
])
patch("build_srs.py", [
 ('rfs = ", ".join(RF_NEW[x] for x in sorted(KPI_RF[k["id"]]) if x != "RF-136") + (", RF-REP-003" if True else "")',
  'rfs = ", ".join(RF_NEW[x] for x in sorted(KPI_RF[k["id"]]) if x not in ("RF-136", "RF-185")) + ", " + (RF_NEW["RF-185"] if "RF-185" in KPI_RF[k["id"]] else RF_NEW["RF-136"])'),
 ('rfs = sorted(x for x in KPI_RF[kid] if x != "RF-136")', 'rfs = sorted(x for x in KPI_RF[kid] if x not in ("RF-136", "RF-185"))'),
 ("{', '.join(RF_NEW[x] for x in rfs)}, RF-REP-003 |", "{', '.join(RF_NEW[x] for x in rfs)}, {RF_NEW['RF-185'] if 'RF-185' in KPI_RF[kid] else RF_NEW['RF-136']} |"),
 ('OUT = os.path.join(OUT_DIR, "SRS_COLBASOFT_v1.3.md")', 'OUT = os.path.join(OUT_DIR, "SRS_COLBASOFT_v1.4.md")'),
 ("Reorganización de los **184 RF** del SPEC", "Reorganización de los **185 RF** del SPEC"),
 ("RF-001–RF-184 |", "RF-001–RF-185 |"),
 ("| **Completado** | 184 RF con ID", "| **Completado** | 185 RF con ID"),
 ("Una fila por cada uno de los 184 RF.", "Una fila por cada uno de los 185 RF."),
 ("## 9.5 Cobertura por regla de negocio (91)", "## 9.5 Cobertura por regla de negocio (92)"),
 ("La cadena está completa para 184 de 184 RF", "La cadena está completa para 185 de 185 RF"),
 ("matriz de 184 RF · cobertura de 91 reglas", "matriz de 185 RF · cobertura de 92 reglas"),
 ("## A.2 Requisitos funcionales (184)", "## A.2 Requisitos funcionales (185)"),
 ("## A.4 Reglas de negocio (91)", "## A.4 Reglas de negocio (92)"),
 ("| **Requisitos funcionales** | 184 | 184 |", "| **Requisitos funcionales** | 185 | 185 |"),
 ("| **82** (v1.0) + **3** (v1.1) + **6** (v1.2) |", "| **82** (v1.0) + **3** (v1.1) + **6** (v1.2) + **1** (v1.4) |"),
 ("Todos los RF del SPEC (184) están en el SRS | ✅ {len(RF_NEW)}/184", "Todos los RF del SPEC (185) están en el SRS | ✅ {len(RF_NEW)}/185"),
 ("(91: 82 de la v1.0 + 3 de la v1.1 + 6 de la v1.2) están en el SRS; los 2 marcadores vacíos quedan documentados | ✅ {len(RN_NEW)}/91",
  "(92: 82 de la v1.0 + 3 de la v1.1 + 6 de la v1.2 + 1 de la v1.4) están en el SRS; los 2 marcadores vacíos quedan documentados | ✅ {len(RN_NEW)}/92"),
 ("Todo RF tiene al menos una HU | ✅ {sum(1 for r in RF if RF_HU.get(r))}/184", "Todo RF tiene al menos una HU | ✅ {sum(1 for r in RF if RF_HU.get(r))}/185"),
 ("HU-001…114 y RF-001…184 (corregido en la v1.3)", "HU-001…114 y RF-001…185 (corregido en la v1.3)"),
 ("Total del SRS v1.2: **91 reglas**.", "Total del SRS v1.2: **91 reglas**.\n>\n> **Versión 1.4 — respuesta a HD-29.** Se incorpora **1 regla estructural nueva**, separada de las 91: RN-MOV-012 (una pieza no se divide: el movimiento interno mueve la pieza completa y tomar una parte es un corte parcial). Viene de SPEC v1.4 §9.18. Además cambian los textos de **RN-MOV-001** (propuesta de ubicación con regla fija en el Núcleo, H-19) y **RN-LOT-006** (sin excepción: lo suelto es un paquete o bolsa, HD-30). Total del SRS v1.4: **92 reglas**."),
 ("| **Completado** | 91 reglas en 13 dominios (82 del SPEC v1.0 + 3 de la v1.1 + 6 de la v1.2)", "| **Completado** | 92 reglas en 13 dominios (82 del SPEC v1.0 + 3 de la v1.1 + 6 de la v1.2 + 1 de la v1.4)"),
 ("`RN-081` a `RN-083` se incorporaron en la v1.1 del SPEC (§9.15, cierre del CP-04) y `RN-084` a `RN-089` en la v1.2 (§9.16, decisiones del 30-sep-2026);", "`RN-081` a `RN-083` se incorporaron en la v1.1 del SPEC (§9.15, cierre del CP-04), `RN-084` a `RN-089` en la v1.2 (§9.16) y `RN-090` en la v1.4 (§9.18);"),
])

CAMBIOS = """## Control de cambios de la versión 1.4

> La v1.4 se regenera desde las mismas fuentes, tras incorporar al SPEC v1.4 las respuestas del Director a **H-19, H-20, HD-29 y HD-30** (30 de septiembre de 2026). La v1.3 se conserva sin cambios en `SRS_COLBASOFT_v1.3.md`.

| Asunto | Respuesta (a) | Efecto en este SRS |
|---|---|---|
| **H-19** | La ubicación se propone con una regla fija en el Núcleo | HU-ENT-006 (criterio 1) y su escenario, RN-MOV-001, CU-08. El hallazgo queda resuelto |
| **H-20** | RF-REP-003 se acota a los 12 KPI del Núcleo; los otros 12 pasan a un RF nuevo | **RF-REP-008** (Horizonte 2); RF-REP-003 (texto); los KPI-02, 03, 04, 06, 07, 10, 12, 15, 18, 20, 22 y 23 se asocian a RF-REP-008. El hallazgo queda resuelto |
| **HD-29** | Una pieza no se divide | Regla nueva **RN-MOV-012**; HU-MOV-002 (criterio 2) y su escenario; RF-MOV-012; CU-10 |
| **HD-30** | Toda la mercancía se controla por piezas | RN-LOT-006 (texto) |

Cifras de la v1.4: requisitos funcionales **184 → 185**, reglas **91 → 92**. No cambian las historias (114), los escenarios (515), los RNF, los KPI ni el Núcleo (94 HU · 164 RF). El Horizonte 2 pasa de 20 a 21 RF.

**Limitación conocida (HD-29).** Una parte de un paquete o bolsa de unidades no puede trasladarse a otra ubicación como movimiento interno, porque exigiría dividir la pieza; la parte que se toma se registra como salida.

"""
patch("cap00.md", [
 ("# SRS_COLBASOFT v1.3\n", "# SRS_COLBASOFT v1.4\n"),
 ("| **Versión** | 1.3 |", "| **Versión** | 1.4 |"),
 ("· 30 de septiembre de 2026 (v1.2 y v1.3) |", "· 30 de septiembre de 2026 (v1.2, v1.3 y v1.4) |"),
 ("| **Estado** | **Borrador v1.3** (30-sep-2026): registra las respuestas a DEC-01…DEC-09. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar y pendientes HD-28, HD-29, HD-30, H-19 y H-20 |",
  "| **Estado** | **Borrador v1.4** (30-sep-2026): registra las respuestas a DEC-01…DEC-09, H-19, H-20, HD-29 y HD-30. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar y pendiente HD-28 |"),
 ("| **Versión anterior** | `SRS_COLBASOFT_v1.2.md` (30-sep-2026), `SRS_COLBASOFT_v1.1.md`", "| **Versión anterior** | `SRS_COLBASOFT_v1.3.md`, `SRS_COLBASOFT_v1.2.md` (30-sep-2026), `SRS_COLBASOFT_v1.1.md`"),
 ("COLBASOFT_SPEC v1.3 → **SRS v1.3** |", "COLBASOFT_SPEC v1.4 → **SRS v1.4** |"),
 ("`COLBASOFT_SPEC_v1.3.md` (Fase 2, con las respuestas a DEC-02…DEC-09) |", "`COLBASOFT_SPEC_v1.4.md` (Fase 2, con las respuestas a H-19, H-20, HD-29 y HD-30) |"),
 ("del COLBASOFT_SPEC v1.3.", "del COLBASOFT_SPEC v1.4."),
 ("## Control de cambios de la versión 1.3\n", CAMBIOS + "## Control de cambios de la versión 1.3\n"),
 ("| **6** | Requisitos Funcionales Normalizados | 184 RF con ID permanente |", "| **6** | Requisitos Funcionales Normalizados | 185 RF con ID permanente |"),
 ("| **H-19** | *(v1.2, detectado al auditar DEC-01)* ", "| **H-19** | **(Resuelto en la v1.4, opción a)** *(v1.2, detectado al auditar DEC-01)* "),
 ("| **H-20** | *(v1.2, detectado al auditar DEC-01)* ", "| **H-20** | **(Resuelto en la v1.4, opción a)** *(v1.2, detectado al auditar DEC-01)* "),
])
patch("cap01.md", [("`COLBASOFT_SPEC_v1.3.md` (5 sep. 2026; v1.1 del 29 sep. 2026; v1.2 y v1.3 del 30 sep. 2026)", "`COLBASOFT_SPEC_v1.4.md` (5 sep. 2026; v1.1 del 29 sep. 2026; v1.2, v1.3 y v1.4 del 30 sep. 2026)")])
patch("cap12.md", [
 ("incluidos los 20 HU / 20 RF del Horizonte 2", "incluidos los 20 HU / 21 RF del Horizonte 2"),
 ("| **Should** (P1) | 59 | 48 | 11 | 83 | 69 | 14 |", "| **Should** (P1) | 59 | 48 | 11 | 84 | 69 | 15 |"),
 ("| **Total** | **114** | **94** | **20** | **184** | **164** | **20** |", "| **Total** | **114** | **94** | **20** | **185** | **164** | **21** |"),
 ("| **114** | **184** |\n", "| **114** | **185** |\n"),
])
patch("annex_c.md", [
 ("| H-19, H-20 | Abierto (nuevos en la v1.2) | Director: aceptar por escrito como limitación o acotar, junto con DEC-01 = A |", "| H-19, H-20 | **Resuelto en la v1.4** | Respuestas (a) del 30-sep-2026 (C.12) |"),
 ("---\n\n**ESTADO DEL ANEXO C**", """## C.12 Respuestas del Director a H-19, H-20, HD-29 y HD-30 (versión 1.4)

> Dadas el 30 de septiembre de 2026, en la opción (a) propuesta, tras verificarla contra las fuentes.

| Asunto | Respuesta | Efecto en este SRS |
|---|---|---|
| **H-19** | (a) Regla fija de propuesta de ubicación en el Núcleo | HU-ENT-006, RN-MOV-001; HU-BOD-005 sigue en el Horizonte 2 |
| **H-20** | (a) RF-REP-003 acotado a 12 KPI; RF nuevo para los otros 12 | RF-REP-003 · RF-REP-008 (Horizonte 2) |
| **HD-29** | (a) Una pieza no se divide | Regla nueva RN-MOV-012; HU-MOV-002 |
| **HD-30** | (a) Toda la mercancía se controla por piezas | RN-LOT-006 |

**Limitación conocida:** una parte de un paquete o bolsa no puede trasladarse a otra ubicación como movimiento interno. Se puede reabrir con el levantamiento AS-IS (Q-04).

---

**ESTADO DEL ANEXO C**"""),
 ("| **Pendiente** | Acta firmada de DEC-08 · H-19, H-20 · HD-28, HD-29 y HD-30 |", "| **Pendiente** | Acta firmada de DEC-08 · HD-28 |"),
])
patch("uc_c.md", [("@RF134 @RF135 @RF136 @RF137 @RF138 @RF139 @RF140 ·", "@RF134 @RF135 @RF136 @RF137 @RF138 @RF139 @RF140 @RF185 ·")])
