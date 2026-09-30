from patch_srs_lib import patch

CAMBIOS = """## Control de cambios de la versión 1.3

> La v1.3 se regenera desde las mismas fuentes, tras incorporar al SPEC v1.3 las respuestas del Director a **DEC-02…DEC-09** (30 de septiembre de 2026). La v1.2 se conserva sin cambios en `SRS_COLBASOFT_v1.2.md`. Las historias y requisitos nuevos **no los crea este SRS**: vienen del SPEC v1.3 (son las propuestas PROP-RN, PROP-KPI y PROP-CIE del Anexo C, ahora aprobadas).

| Decisión | Efecto en este SRS |
|---|---|
| **DEC-02** (a) — 20 módulos, dashboard M-17 y exclusión de toda IA | Sin cambios de contenido. Hallazgo H-17 resuelto |
| **DEC-03** (a) — numeración canónica `RN-<DOM>-nnn` y fe de erratas del SPEC | Se adopta formalmente la numeración del Anexo A.4. El SPEC v1.3 §9.17 emite la fe de erratas. Hallazgos H-01 y H-09 resueltos |
| **DEC-04** (a) — toda regla estructural es no configurable; el Jefe lee los parámetros; el Administrador o el Jefe cierran las observaciones de auditoría | RF-PAR-001 (el Jefe consulta los parámetros), HU-AUD-003 (criterio 4) y su escenario Gherkin. Hallazgo H-06 resuelto |
| **DEC-05** (a) — se crean HU y RF del cierre de jornada (PN-14) | HU-TAR-004, HU-TAR-005; RF-TAR-006, RF-TAR-007, RF-TAR-008; CU-19 con requisitos. Hallazgo H-10 resuelto |
| **DEC-06** (a) — se aprueban todas las propuestas de cierre de brechas | RF-BOD-009, RF-MOV-013, RF-NOV-007, RF-CNT-015, RF-SAL-014, RF-NOV-008, RF-KDX-009, RF-QRC-009, RF-ENT-017, RF-PAR-007; HU-MOV-009 y HU-CNT-011; RF-PAR-001 con dos parámetros nuevos. Las 91 reglas tienen requisito (antes, 85 de 91). Hallazgos H-11, H-12 y H-13 resueltos |
| **DEC-07** (a) — se retira la valorización del MVP | HU-REP-001 (criterio 5) y su escenario Gherkin; RF-INV-005 y RF-DSH-003 se conservan como restricción preventiva. Hallazgo H-07 resuelto |
| **DEC-08** (a) — acta y tabla de equivalencia de fases | Solo un **borrador** (`05_V13_DECISIONES/`). H-15 y H-16 siguen abiertos hasta que el acta se firme |
| **DEC-09** (a) — alerta de lote sobre el umbral de antigüedad | Se redefine la condición de la alerta (RN-ALE, PN-11). Hallazgo H-18 resuelto |

Cifras de la v1.3: historias **114** (antes 110), requisitos funcionales **171 → 184**, escenarios Gherkin **498 → 515**. No cambian las 91 reglas, los 47 RNF, los 24 casos de uso, los 24 KPI ni los conceptos de dominio (49). El Núcleo pasa a 94 HU y 152 → 164 RF; el Completo, a 114 HU y 184 RF. Los números del Cap. 0 que siguen describen la reconstrucción de contexto de la v1.0 y se conservan como registro histórico.

"""

patch("cap00.md", [
 ("# SRS_COLBASOFT v1.2\n", "# SRS_COLBASOFT v1.3\n"),
 ("| **Versión** | 1.2 |", "| **Versión** | 1.3 |"),
 ("· 30 de septiembre de 2026 (v1.2) |", "· 30 de septiembre de 2026 (v1.2 y v1.3) |"),
 ("| **Estado** | **Borrador v1.2** (30-sep-2026): incorpora DEC-01 = A con la capa de trazabilidad por pieza. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: DEC-02…DEC-09 sin responder y acta de DEC-08 |",
  "| **Estado** | **Borrador v1.3** (30-sep-2026): registra las respuestas a DEC-01…DEC-09. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar y pendientes HD-28, HD-29, HD-30, H-19 y H-20 |"),
 ("| **Versión anterior** | `SRS_COLBASOFT_v1.1.md` (29-sep-2026) y `SRS_COLBASOFT_v1.0.md` (28-sep-2026), conservadas sin cambios |",
  "| **Versión anterior** | `SRS_COLBASOFT_v1.2.md` (30-sep-2026), `SRS_COLBASOFT_v1.1.md` (29-sep-2026) y `SRS_COLBASOFT_v1.0.md` (28-sep-2026), conservadas sin cambios |"),
 ("COLBASOFT_SPEC v1.2 → **SRS v1.2** |", "COLBASOFT_SPEC v1.3 → **SRS v1.3** |"),
 ("`COLBASOFT_SPEC_v1.2.md` (Fase 2, revisado tras la auditoría de DEC-01) |", "`COLBASOFT_SPEC_v1.3.md` (Fase 2, con las respuestas a DEC-02…DEC-09) |"),
 ("normaliza, reorganiza y hace trazable el contenido del COLBASOFT_SPEC v1.2.", "normaliza, reorganiza y hace trazable el contenido del COLBASOFT_SPEC v1.3."),
 ("## Control de cambios de la versión 1.2\n", CAMBIOS + "## Control de cambios de la versión 1.2\n"),
 ("| **5** | Historias de Usuario Normalizadas | 110 historias · ID estable · MoSCoW · dependencias · Gherkin |", "| **5** | Historias de Usuario Normalizadas | 114 historias · ID estable · MoSCoW · dependencias · Gherkin |"),
 ("| **6** | Requisitos Funcionales Normalizados | 171 RF con ID permanente |", "| **6** | Requisitos Funcionales Normalizados | 184 RF con ID permanente |"),
])
patch("cap01.md", [("`COLBASOFT_SPEC_v1.2.md` (5 sep. 2026; v1.1 del 29 sep. 2026; v1.2 del 30 sep. 2026)", "`COLBASOFT_SPEC_v1.3.md` (5 sep. 2026; v1.1 del 29 sep. 2026; v1.2 y v1.3 del 30 sep. 2026)")])
patch("cap12.md", [
 ("incluida la trazabilidad por pieza (elemento 40, v1.2): 84 HU y 143 RF de la v1.1 más 7 HU y 9 RF de la v1.2 | **91** | **152** |",
  "incluidas la trazabilidad por pieza (elemento 40, v1.2) y el cierre de brechas y de jornada (elemento 41, v1.3): 84 HU y 143 RF de la v1.1, más 7 HU y 9 RF de la v1.2, más 3 HU y 12 RF de la v1.3 | **94** | **164** |"),
 ("| **110** | **171** |\n", "| **114** | **184** |\n"),
 ("| **Must** (P0) | 40 | 38 | 2 | 82 | 81 | 1 |", "| **Must** (P0) | 40 | 38 | 2 | 82 | 81 | 1 |"),
 ("| **Should** (P1) | 55 | 45 | 10 | 71 | 58 | 13 |", "| **Should** (P1) | 59 | 48 | 11 | 83 | 69 | 14 |"),
 ("| **Could** (P2) | 15 | 8 | 7 | 18 | 13 | 5 |", "| **Could** (P2) | 15 | 8 | 7 | 19 | 14 | 5 |"),
 ("| **Total** | **110** | **91** | **19** | **171** | **152** | **19** |", "| **Total** | **114** | **94** | **20** | **184** | **164** | **20** |"),
 ("(498 escenarios en total;", "(515 escenarios en total;"),
 ("incluidos los 19 HU / 19 RF del Horizonte 2", "incluidos los 20 HU / 20 RF del Horizonte 2"),
])
patch("cap11.md", [("(H-08, resuelto por DEC-01 = A en la v1.2:", "(H-08, resuelto por DEC-01 = A en la v1.2:")])

# casos de uso
patch("uc_a.md", [
 ("@RF163 @RF164 @RF165 · RN: @RN002b", "@RF163 @RF164 @RF165 @RF180 · RN: @RN002b"),
 ("RF: @RF040 @RF041 @RF042 @RF043 @RF044 @RF045 @RF046 @RF047 · RN:", "RF: @RF040 @RF041 @RF042 @RF043 @RF044 @RF045 @RF046 @RF047 @RF179 · RN:"),
 ("@RF072 @RF073 @RF076 @RF166 · RN:", "@RF072 @RF073 @RF076 @RF166 @RF172 · RN:"),
 ("RF: @RF152 @RF153 @RF154 @RF155 @RF156 @RF157 · RN:", "RF: @RF152 @RF153 @RF154 @RF155 @RF156 @RF157 @RF181 · RN:"),
])
patch("uc_b.md", [
 ("HU: @HU045 @HU046 @HU106 · RF: @RF072 @RF073 @RF074 @RF075 @RF076 @RF077 @RF166 ·", "HU: @HU045 @HU046 @HU106 @HU111 · RF: @RF072 @RF073 @RF074 @RF075 @RF076 @RF077 @RF166 @RF173 ·"),
 ("HU: @HU063 @HU064 @HU062 @HU065 · RF: @RF103 @RF104 @RF095 @RF096 @RF098 @RF100 @RF101 @RF102 @RF105 ·", "HU: @HU063 @HU064 @HU062 @HU065 @HU112 · RF: @RF103 @RF104 @RF095 @RF096 @RF098 @RF100 @RF101 @RF102 @RF105 @RF175 ·"),
 ("@RF067 @RF068 @RF069 @RF070 @RF071 @RF167 @RF168 ·", "@RF067 @RF068 @RF069 @RF070 @RF071 @RF167 @RF168 @RF176 ·"),
])
patch("uc_c.md", [
 ("HU: @HU067 @HU068 @HU069 @HU070 · RF: @RF106 @RF107 @RF108 @RF109 @RF110 @RF111 ·", "HU: @HU067 @HU068 @HU069 @HU070 · RF: @RF106 @RF107 @RF108 @RF109 @RF110 @RF111 @RF174 @RF177 ·"),
 ("@RF124 @RF125 @RF126 @RF170 ·", "@RF124 @RF125 @RF126 @RF170 @RF178 ·"),
 ("| **Trazabilidad** | HU: **ninguna** · RF: **ninguno** (ver nota) · RN: @RN054 @RN028 ·", "| **Trazabilidad** | HU: @HU113 @HU114 · RF: @RF182 @RF183 @RF184 · RN: @RN054 @RN028 ·"),
 ("> **Nota de trazabilidad — hallazgo H-10.** El SPEC modela PN-14 (§3) y lo incluye en el backlog del MVP (elemento 39, §12.2), pero **no le asigna ninguna historia de usuario ni requisito funcional**; solo la regla @RN054 y el requisito @RNF011 lo afectan indirectamente. Este caso de uso se documenta desde el proceso del SPEC y queda marcado como **requisitos pendientes de definición** hasta que el Director decida (ver Anexo C, decisión DEC-05).",
  "> **Nota de trazabilidad — hallazgo H-10 (resuelto).** El SPEC v1.0 a v1.2 modelaba PN-14 (§3) y lo incluía en el backlog del MVP (elemento 39, §12.2) sin historia ni requisito. El Director resolvió DEC-05 (a) el 30-sep-2026: el SPEC v1.3 crea @HU113, @HU114 y @RF182 a @RF184, que este caso de uso recorre."),
])

# annex C
patch("annex_c.md", [
 ("Se mantiene el SPEC por defecto |", "**RESUELTA el 30-sep-2026: opción (a).** Se mantienen los 20 módulos y la exclusión de toda IA |"),
 ("Persisten dos cifras en circulación (68 y 82) |", "**RESUELTA el 30-sep-2026: opción (a).** Fe de erratas en el SPEC v1.3 §9.17 |"),
 ("Riesgo de que se implementen como configurables reglas que protegen la integridad (R-S08) |", "**RESUELTA el 30-sep-2026: opción (a).** Toda regla estructural es no configurable |"),
 ("CU-19 queda sin requisitos y sin criterio de aceptación |", "**RESUELTA el 30-sep-2026: opción (a).** HU-TAR-004, HU-TAR-005 y RF-TAR-006…008 |"),
 ("El sistema no implementará reglas ni capturará datos que hoy nadie exige |", "**RESUELTA el 30-sep-2026: opción (a).** Se aprueban todas las propuestas (C.2) |"),
 ("Permiso sin dato de origen (RF-INV-005, RF-DSH-003, HU-REP-001 crit. 5) |", "**RESUELTA el 30-sep-2026: opción (a).** La valorización se retira del MVP |"),
 ("Ambigüedad sobre qué versión rige |", "**Respondida el 30-sep-2026: opción (a); acta pendiente de firma** (borrador en `05_V13_DECISIONES/`) |"),
 ("Alerta sin condición de disparo definida |", "**RESUELTA el 30-sep-2026: opción (a).** Umbral de antigüedad del lote |"),
 ("## C.2 Propuestas de cierre de brechas (NO incorporadas al baseline)", "## C.2 Propuestas de cierre de brechas (**APROBADAS por el Director el 30-sep-2026 e incorporadas al baseline en la v1.3**: DEC-05 y DEC-06)\n\n> Correspondencia con los requisitos de la v1.3: PROP-RN-01 → RF-BOD-009 · PROP-RN-02 → RF-MOV-013 (HU-MOV-009) · PROP-RN-03 → RF-NOV-007 · PROP-RN-04 → RF-CNT-015 (HU-CNT-011; Horizonte 2) · PROP-RN-05 → RF-SAL-014 · PROP-RN-06 → RF-NOV-008 · PROP-KPI-01 → RF-KDX-009 · PROP-KPI-02 → RF-QRC-009 · PROP-KPI-03 → RF-BOD-009 · PROP-KPI-04 → RF-ENT-017 · PROP-KPI-05 → RF-PAR-001 (parámetro «días sin movimiento») · PROP-KPI-06 → RF-PAR-007 · PROP-CIE-01…03 → RF-TAR-006…008 (HU-TAR-004, HU-TAR-005)."),
 ("| H-01, H-09 | Abierto | DEC-03 |", "| H-01, H-09 | **Resuelto en la v1.3** | DEC-03 (a) |"),
 ("| H-06 | Abierto | DEC-04 |", "| H-06 | **Resuelto en la v1.3** | DEC-04 (a) |"),
 ("| H-07 | Abierto | DEC-07 |", "| H-07 | **Resuelto en la v1.3** | DEC-07 (a) |"),
 ("| H-10 | Abierto | DEC-05 |", "| H-10 | **Resuelto en la v1.3** | DEC-05 (a) |"),
 ("| H-11, H-12, H-13 | Abierto | DEC-06 |", "| H-11, H-12, H-13 | **Resuelto en la v1.3** | DEC-06 (a) |"),
 ("| H-15, H-16 | Abierto | DEC-08 |", "| H-15, H-16 | Abierto: acta en borrador, sin firmar | DEC-08 (a) |"),
 ("| H-17 | Abierto | DEC-02 |", "| H-17 | **Resuelto en la v1.3** | DEC-02 (a) |"),
 ("| H-18 | Abierto | DEC-09 |", "| H-18 | **Resuelto en la v1.3** | DEC-09 (a) |"),
 ("---\n\n**ESTADO DEL ANEXO C**", """## C.11 Respuestas del Director a DEC-02…DEC-09 (versión 1.3)

> Dadas el 30 de septiembre de 2026, todas en la opción (a) recomendada por el SRS. Con DEC-01 (C.10), las nueve decisiones tienen respuesta; la aprobación formal sigue pendiente del acta de DEC-08.

| ID | Respuesta | Efecto en este SRS |
|---|---|---|
| **DEC-02** | (a) 20 módulos, dashboard M-17 y exclusión de toda IA | Ninguno en cifras |
| **DEC-03** | (a) Numeración canónica `RN-<DOM>-nnn` y fe de erratas del SPEC | SPEC v1.3 §9.17 |
| **DEC-04** | (a) Toda regla estructural no configurable; el Jefe lee parámetros; el Administrador o el Jefe cierran las observaciones de auditoría | RF-PAR-001, HU-AUD-003 |
| **DEC-05** | (a) Se crean HU y RF del cierre de jornada | HU-TAR-004, HU-TAR-005, RF-TAR-006…008 |
| **DEC-06** | (a) Se aprueban todas las propuestas de cierre de brechas | 10 RF nuevos y 2 HU (véase C.2), más 2 parámetros en RF-PAR-001 |
| **DEC-07** | (a) La valorización se retira del MVP | HU-REP-001 (criterio 5); RF-INV-005 y RF-DSH-003 como restricción preventiva |
| **DEC-08** | (a) Acta de aprobación y tabla de equivalencia de fases | Borrador sin firma en `05_V13_DECISIONES/`; H-15 y H-16 siguen abiertos |
| **DEC-09** | (a) La alerta se redefine sobre el umbral de antigüedad | PN-11; RN-LOT-005 |

**Pendientes que siguen abiertos:** el acta firmada de DEC-08; H-19 y H-20; HD-28, HD-29 y HD-30 del modelo de dominio; la verificación de campo de KPI-24 (Fase 3 del roadmap).

---

**ESTADO DEL ANEXO C**"""),
 ("| **Completado** | 9 decisiones · 5 decisiones del cierre del CP-04 (C.9) · decisiones del 30-sep-2026 (C.10)", "| **Completado** | 9 decisiones, todas con respuesta (C.10 y C.11) · 5 decisiones del cierre del CP-04 (C.9)"),
 ("| **Pendiente** | Respuesta del Director a DEC-02…DEC-09 · HD-28, HD-29 y HD-30 |", "| **Pendiente** | Acta firmada de DEC-08 · H-19, H-20 · HD-28, HD-29 y HD-30 |"),
])
print("ok")
