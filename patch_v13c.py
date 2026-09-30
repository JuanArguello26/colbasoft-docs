import re
from patch_srs_lib import patch

# ---------------------------------------------------------------- dm_data.py
patch("dm_data.py", [
 ("**Sin requisitos funcionales en el SRS** (hallazgo H-10, decisión DEC-05 pendiente): se modela para no perder el concepto, marcado como pendiente.",
  "**Con requisitos funcionales desde la v1.3** (HU-TAR-004, HU-TAR-005, RF-TAR-006…008; hallazgo H-10 resuelto por DEC-05)."),
 ("⚠️ **Sin HU ni RF en el SRS** (H-10, DEC-05).", "Con HU y RF desde la v1.3 (DEC-05)."),
 ('"⚠️ Pendiente DEC-05. Consolidación de una bodega', '"Consolidación de una bodega'),
 ('"Quién responde no está definido en el SPEC (DEC-04)."', '"Responde y cierra el Administrador o el Jefe (DEC-04, v1.3)."'),
 ('bloqueada mientras haya registros sin sincronizar. ⚠️ DEC-05."', 'bloqueada mientras haya registros sin sincronizar."'),
 ('("Abierta", "Cerrada", "EV-AUD-002", "Por definir (DEC-04)", "Respuesta registrada")', '("Abierta", "Cerrada", "EV-AUD-002", "Administrador / Jefe", "Respuesta registrada (DEC-04)")'),
 ('"SPEC PN-14 (sin RF: DEC-05)"', '"SPEC PN-14 (HU-TAR-004, HU-TAR-005; DEC-05)"'),
 ("Si DEC-07 decide una política de costeo, se abrirá un subdominio nuevo.\",\n  \"DEC-07\"),",
  "**Resuelto (DEC-07 a, v1.3):** el permiso «consultar valorización» se retira del MVP y queda como restricción preventiva; si más adelante se define una política de costeo (Horizonte 3), se abrirá un subdominio nuevo.\",\n  \"**Resuelto — DEC-07 (a), v1.3**\"),"),
 ("Se modela solo la condición definida: antigüedad del lote sobre el umbral (RN-LOT-005 → EV-LOT-004). El tipo de alerta queda como en el SPEC, sin condición propia.\",\n  \"DEC-09\"),",
  "**Resuelto (DEC-09 a, v1.3):** la alerta se redefine sobre el umbral de antigüedad del lote (RN-LOT-005 → EV-LOT-004); el lote no tiene «fecha límite».\",\n  \"**Resuelto — DEC-09 (a), v1.3**\"),"),
 ("\"PN-14 está en el MVP (backlog, elemento 39) pero no tiene HU ni RF.\",\n  \"Se modelan la entidad E-26, el agregado AG-21, la máquina SM-21 y los eventos EV-JOR-*, todos marcados ⚠️ pendientes.\",\n  \"DEC-05\"),",
  "\"Hasta la v1.2, PN-14 estaba en el MVP (backlog, elemento 39) pero no tenía HU ni RF.\",\n  \"**Resuelto (DEC-05 a, v1.3):** PN-14 tiene HU-TAR-004, HU-TAR-005 y RF-TAR-006…008; la entidad E-26, el agregado AG-21, la máquina SM-21 y los eventos EV-JOR-* dejan de estar pendientes.\",\n  \"**Resuelto — DEC-05 (a), v1.3**\"),"),
 ("la aprobación funcional y académica sigue pendiente de DEC-01…DEC-09 y HD-25.\",\n  \"Director — aprobación pendiente (DEC-01…DEC-09)\"),",
  "la aprobación funcional y académica sigue pendiente solo del acta de DEC-08 y de HD-28…HD-30 (las nueve decisiones DEC ya tienen respuesta, v1.3).\",\n  \"Director — aprobación pendiente (acta de DEC-08)\"),"),
])

# ---------------------------------------------------------------- ev_data.py
s = open("ev_data.py", encoding="utf8").read()
def addlinks(eid, **kw):
    global s
    L = s.split("\n")
    i = [k for k, l in enumerate(L) if l.startswith(f'E("{eid}"')]
    assert len(i) == 1, eid
    line = L[i[0]]
    for key, val in kw.items():
        m = re.search(rf'\b{key}="([^"]*)"', line)
        if m:
            line = line[:m.end(1)] + ", " + val + line[m.end(1):]
        else:
            j = line.index(', crit=')
            line = line[:j] + f', {key}="{val}"' + line[j:]
    L[i[0]] = line
    s = "\n".join(L)
addlinks("EV-INV-002", rf="RF-BOD-009")
addlinks("EV-INV-005", rf="RF-SAL-014")
addlinks("EV-MOV-003", hu="HU-MOV-009", rf="RF-MOV-013")
addlinks("EV-MOV-004", hu="HU-MOV-009", rf="RF-MOV-013")
addlinks("EV-CNT-013", hu="HU-CNT-011", rf="RF-CNT-015")
addlinks("EV-NOV-006", rf="RF-NOV-008")
addlinks("EV-NOV-007", rf="RF-NOV-007")
addlinks("EV-JOR-001", hu="HU-TAR-004", rf="RF-TAR-006")
addlinks("EV-JOR-002", hu="HU-TAR-004", rf="RF-TAR-007")
addlinks("EV-JOR-003", hu="HU-TAR-004", rf="RF-TAR-007")
addlinks("EV-JOR-004", hu="HU-TAR-005", rf="RF-TAR-008")
addlinks("EV-JOR-005", hu="HU-TAR-005", rf="RF-TAR-008")
addlinks("EV-ENT-003", rf="RF-ENT-017")
addlinks("EV-TRZ-001", rf="RF-QRC-009")
s = s.replace('E("EV-AUD-002", "Observación de auditoría cerrada", "Por definir (DEC-04)"', 'E("EV-AUD-002", "Observación de auditoría cerrada", "Administrador / Jefe"')
s = s.replace('nota="Actor que responde no definido (DEC-04)"', 'nota="Responde y cierra el Administrador o el Jefe (DEC-04, v1.3)"')
open("ev_data.py", "w", encoding="utf8", newline="\n").write(s)

# ---------------------------------------------------------------- gl_data.py
patch("gl_data.py", [
 (" ⚠️ Sin requisitos funcionales en el SRS (DEC-05).", ""),
 ('"No se configura (HD, DEC-04)."', '"No se configura (DEC-04: toda regla estructural es no configurable)."'),
])

S010 = """
## 0.10 Control de cambios de la versión 1.3 (respuestas a DEC-02…DEC-09, 30 de septiembre de 2026)

El Director respondió DEC-02…DEC-09, todas en la opción (a) recomendada por el SRS. El SPEC v1.3 y el SRS v1.3 las recogen antes; esta versión las incorpora editando los datos fuente y regenerando los tres documentos.

| Decisión | Respuesta | Cambios en el modelo |
|---|---|---|
| **DEC-02** | 20 módulos, dashboard M-17 y exclusión de toda IA | Ninguno |
| **DEC-03** | Numeración canónica `RN-<DOM>-nnn` | Ninguno: el modelo ya usaba esos IDs |
| **DEC-04** | Toda regla estructural es no configurable; el Jefe lee parámetros; el Administrador o el Jefe cierran las observaciones de auditoría | E-22, SM-18 y **EV-AUD-002**: el actor «por definir» pasa a «Administrador / Jefe»; término «Regla estructural»; IN-67 deja de ser provisional |
| **DEC-05** | Se crean HU y RF del cierre de jornada | E-26, AG-21, SM-21 y EV-JOR-001…005 dejan de estar marcados como pendientes y se vinculan a HU-TAR-004, HU-TAR-005 y RF-TAR-006…008; **HD-11 resuelto**; término «Cierre de jornada» |
| **DEC-06** | Se aprueban todas las propuestas de cierre de brechas | Vínculos de eventos con los requisitos nuevos: EV-INV-002, EV-INV-005, EV-MOV-003, EV-MOV-004, EV-CNT-013, EV-NOV-006, EV-NOV-007, EV-ENT-003, EV-TRZ-001. Ninguna regla, entidad ni evento nuevos |
| **DEC-07** | La valorización se retira del MVP | **HD-09 resuelto** |
| **DEC-08** | Acta y tabla de equivalencia | Sin efecto en el modelo; **HD-21** queda pendiente solo del acta firmada |
| **DEC-09** | Alerta sobre el umbral de antigüedad del lote | **HD-10 resuelto** |

**Ningún ID se renumeró ni se reutilizó.** No se agregaron entidades, agregados, invariantes, eventos ni términos nuevos; se actualizaron vínculos y textos. Las cifras del SRS pasan a 114 HU y 184 RF.
"""

# ---------------------------------------------------------------- build_f4.py
patch("build_f4.py", [
 ('FECHA = "28 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) · 30 de septiembre de 2026 (v1.2)"', 'FECHA = "28 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) · 30 de septiembre de 2026 (v1.2 y v1.3)"'),
 ('| **Versión** | 1.2 |', '| **Versión** | 1.3 |'),
 ('| **Estado** | **Borrador v1.2** (30-sep-2026): incorpora la trazabilidad por pieza y resuelve HD-25. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: DEC-02…DEC-09 sin responder y acta de DEC-08 |',
  '| **Estado** | **Borrador v1.3** (30-sep-2026): incorpora la trazabilidad por pieza (v1.2) y las respuestas a DEC-02…DEC-09. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar y pendientes HD-28, HD-29 y HD-30 |'),
 ('COLBASOFT_SPEC v1.2 → SRS_COLBASOFT v1.2 → **Modelo de Dominio v1.2**', 'COLBASOFT_SPEC v1.3 → SRS_COLBASOFT v1.3 → **Modelo de Dominio v1.3**'),
 ('El detalle está en DOMAIN_MODEL §0.9.\n"""', 'El detalle está en DOMAIN_MODEL §0.9.\n\n> **Versión 1.3.** Incorpora las respuestas del Director a DEC-02…DEC-09. El detalle está en DOMAIN_MODEL §0.10.\n"""'),
 ('el **0.8** registra los cambios de la v1.1 y el **0.9** los de la v1.2.', 'el **0.8** registra los cambios de la v1.1, el **0.9** los de la v1.2 y el **0.10** los de la v1.3.'),
 ('110 HU, 171 RF, 91 RN en la v1.2)', '114 HU, 184 RF, 91 RN en la v1.3)'),
 ('y los términos GL-206…GL-210). Las reglas del SRS pasan de 85 a 91;', 'y los términos GL-206…GL-210). Las reglas del SRS pasan de 85 a 91;'),
 ('| R-S05 | Reglas y KPI sin requisito de captura; PN-14 sin requisitos | 🟠 | Eventos marcados «sin RF» (Cap. 2 del EVENT_CATALOG) |', '| R-S05 | Reglas y KPI sin requisito de captura; PN-14 sin requisitos | ✅ | Resuelto en la v1.3 (DEC-05, DEC-06) |'),
 ('| R-S08 | Ambigüedad «estructural / configurable» (DEC-04) | 🟠 | IN-67 adopta la interpretación del SRS |', '| R-S08 | Ambigüedad «estructural / configurable» (DEC-04) | ✅ | Resuelto en la v1.3: toda regla estructural es no configurable (IN-67) |'),
 ('**Decisiones del Director aún abiertas (SRS, Anexo C):** DEC-01 umbral aprobatorio', '**Decisiones del Director (SRS, Anexo C) — todas con respuesta en la v1.2 y la v1.3:** DEC-01 umbral aprobatorio'),
 ('· DEC-09 fecha límite de lote. Cada una que toca el dominio se marca ⚠️ donde aplica.', '· DEC-09 fecha límite de lote. Queda pendiente solo el acta firmada de DEC-08.'),
 ('"IN-67 depende de DEC-04; IN-46 depende de HD-13; IN-23 actualizada por DF5-01"', '"IN-67 confirmada por DEC-04; IN-46 depende de HD-13; IN-23 actualizada por DF5-01"'),
 ('"Matriz C depende de datos que ningún RF exige capturar (KPI-05, 07, 10, 12, 17, 24; H-12 del SRS)",\n                    "Cap. 3, EVENT_CATALOG", "H-12 del SRS (heredado)", "9"))',
  '"Matriz C: los datos de origen de KPI-05, 07, 10, 12, 17 y 24 se capturan desde la v1.3 (DEC-06); KPI-24 requiere además verificación de campo",\n                    "Cap. 3, EVENT_CATALOG", "H-12 del SRS (resuelto en la v1.3)", "9"))'),
 ('"PN-14 sin requisitos (DEC-05); PN-04 sin eventos por diseño (solo lectura)"', '"PN-04 sin eventos por diseño (solo lectura); PN-14 con requisitos desde la v1.3 (DEC-05)"'),
 ("Provienen de procesos del SPEC sin historia propia (H-10, H-11 del SRS; HD-11, HD-19).", "Provienen de procesos del SPEC sin historia propia (HD-19; H-10 y H-11 del SRS, resueltos en la v1.3)."),
 ("Son la traducción al dominio de las brechas del SRS: reglas sin RF (H-11), cierre de jornada (H-10) y funciones de módulo sin requisito (HD-19). Implementarlos exige que el Director apruebe las propuestas del Anexo C del SRS (DEC-05, DEC-06).",
  "Son la traducción al dominio de las brechas del SRS que siguen abiertas: funciones de módulo sin requisito (HD-19). Las de reglas sin RF (H-11) y cierre de jornada (H-10) se cerraron en la v1.3 (DEC-05, DEC-06)."),
 ('"H-10, H-11 del SRS · HD-11, HD-19", "6"))', '"HD-19 · H-10 y H-11 del SRS (resueltos en la v1.3)", "6"))'),
 ('"HD-11, HD-17, HD-19 · H-10, H-11, H-12 del SRS", "2"))', '"HD-17, HD-19 · H-10, H-11, H-12 del SRS (resueltos en la v1.3)", "2"))'),
 (' ("RF5-08", "Decisiones del Director abiertas que cambian el modelo", "DEC-01, DEC-04, DEC-05, DEC-07, DEC-09 · HD-21", "🟠", "Entidades y eventos ⚠️ pueden cambiar o desaparecer"),',
  ' ("RF5-08", "Aprobación formal pendiente: el acta de DEC-08 no está firmada; las nueve decisiones DEC ya tienen respuesta (v1.3)", "DEC-08 · HD-21", "🟡", "El documento puede cambiar si la aprobación formal introduce correcciones"),'),
 ('| V-7 | Historias con evento | 🟡 {hu_cov}/110 (el resto son de consulta) |', '| V-7 | Historias con evento | 🟡 {hu_cov}/114 (el resto son de consulta) |'),
 ('| V-8 | RF con evento | 🟡 {rf_cov}/171 (el resto son de consulta, restricción o presentación) |', '| V-8 | RF con evento | 🟡 {rf_cov}/184 (el resto son de consulta, restricción o presentación) |'),
 ('**Estado frente a la Fase 5 (v1.2).**', '**Estado frente a la Fase 5 (v1.3).**'),
 ('y DEC-01…DEC-09 siguen abiertas, sin bloquear la arquitectura (ver `04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md`).', 'sin bloquear la arquitectura. Las nueve decisiones DEC tienen respuesta (DEC-01 en la v1.2; DEC-02…DEC-09 en la v1.3); queda pendiente el acta firmada de DEC-08 (ver `05_V13_DECISIONES/`).'),
 ('| **Dependencias** | Decisiones del Director DEC-01…DEC-09 y hallazgos pendientes (DOMAIN_MODEL Cap. 10) |', '| **Dependencias** | Acta de DEC-08 y hallazgos pendientes (DOMAIN_MODEL Cap. 10) |'),
 ('*Fin de DOMAIN_MODEL v1.2.', '*Fin de DOMAIN_MODEL v1.3.'),
 ('*Fin de EVENT_CATALOG v1.2.*', '*Fin de EVENT_CATALOG v1.3.*'),
 ('*Fin de GLOSSARY v1.2.', '*Fin de GLOSSARY v1.3.'),
])
s = open("build_f4.py", encoding="utf8").read()
anchor = "\n**Ningún ID se renumeró ni se reutilizó.** Los elementos nuevos continúan la numeración (E-27, VO-43, AG-22"
i = s.index(anchor)
# 0.10 va al final del bloque 0.9 (antes de «**ESTADO: CONTEXTO RECONSTRUIDO.**»)
j = s.index("\n**ESTADO: CONTEXTO RECONSTRUIDO.**", i)
s = s[:j] + "\n" + S010 + s[j:]
open("build_f4.py", "w", encoding="utf8", newline="\n").write(s)
patch("xref.py", [('"SRS_COLBASOFT_v1.2.md"', '"SRS_COLBASOFT_v1.3.md"'), ('"COLBASOFT_SPEC_v1.2.md"', '"COLBASOFT_SPEC_v1.3.md"')])
print("ok")
