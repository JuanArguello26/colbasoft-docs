import re, sys
def patch(path, pairs, exact1=True):
    s = open(path, encoding="utf8").read()
    for old, new in pairs:
        n = s.count(old)
        assert n >= 1, (path, old[:80])
        if exact1: assert n == 1, (path, n, old[:80])
        s = s.replace(old, new)
    open(path, "w", encoding="utf8", newline="\n").write(s)

# ------------------------------------------------ build_srs.py
patch("build_srs.py", [
 ('OUT = os.path.join(OUT_DIR, "SRS_COLBASOFT_v1.1.md")', 'OUT = os.path.join(OUT_DIR, "SRS_COLBASOFT_v1.2.md")'),
 ("Reorganización de las **103 historias** del SPEC (Cap. 6)", "Reorganización de las **110 historias** del SPEC (Cap. 6)"),
 ("(462 criterios → 462 escenarios)", "(498 criterios → 498 escenarios)"),
 ("HU-001–HU-103 |", "HU-001–HU-110 |"),
 ("| **Completado** | 103 historias con ID `HU-<DOM>-nnn`, MoSCoW, horizonte, dependencias, RF/RN/KPI relacionados y 462 escenarios Gherkin",
  "| **Completado** | 110 historias con ID `HU-<DOM>-nnn`, MoSCoW, horizonte, dependencias, RF/RN/KPI relacionados y 498 escenarios Gherkin"),
 ("Reorganización de los **162 RF** del SPEC", "Reorganización de los **171 RF** del SPEC"),
 ("RF-001–RF-162 |", "RF-001–RF-171 |"),
 ("| **Completado** | 162 RF con ID", "| **Completado** | 171 RF con ID"),
 ("Total del SRS v1.1: **85 reglas**. La discrepancia 68/82 del SPEC sigue abierta (H-01, DEC-03).",
  "Total del SRS v1.1: **85 reglas**. La discrepancia 68/82 del SPEC sigue abierta (H-01, DEC-03).\n>\n> **Versión 1.2 — decisiones del 30-sep-2026.** Se incorporan **6 reglas estructurales nuevas**, separadas de las 85: RN-LOT-006 (toda mercancía se registra por piezas), RN-LOT-007 (la existencia de una unidad de inventario es la suma de sus piezas), RN-SAL-008 (el corte parcial), RN-MOV-011 (selección de la pieza tras el escaneo), RN-SAL-009 (el escaneo de salida verifica y cuenta) y RN-CNT-009 (el conteo es pieza por pieza); vienen de SPEC v1.2 §9.16. Además cambia el texto de **RN-IDE-004** (Q-09: la reimpresión conserva el mismo QR). Total del SRS v1.2: **91 reglas**."),
 ("| **Completado** | 85 reglas en 13 dominios (82 del SPEC v1.0 + 3 de la v1.1)", "| **Completado** | 91 reglas en 13 dominios (82 del SPEC v1.0 + 3 de la v1.1 + 6 de la v1.2)"),
 ("Una fila por cada uno de los 162 RF.", "Una fila por cada uno de los 171 RF."),
 ("## 9.5 Cobertura por regla de negocio (85)", "## 9.5 Cobertura por regla de negocio (91)"),
 ("La cadena está completa para 162 de 162 RF y 103 de 103 HU.", "La cadena está completa para 171 de 171 RF y 110 de 110 HU."),
 ("matriz de 162 RF · cobertura de 82 reglas", "matriz de 171 RF · cobertura de 91 reglas"),
 ("## A.1 Historias de usuario (103)", "## A.1 Historias de usuario (110)"),
 ("## A.2 Requisitos funcionales (162)", "## A.2 Requisitos funcionales (171)"),
 ("## A.4 Reglas de negocio (85)", "## A.4 Reglas de negocio (91)"),
 ("`CD-01…CD-48`", "`CD-01…CD-49`"),
 ("| **Historias de usuario** | 103 | 103 |", "| **Historias de usuario** | 110 | 110 |"),
 ("| **Requisitos funcionales** | 162 | 162 |", "| **Requisitos funcionales** | 171 | 171 |"),
 ("| **82** (v1.0) + **3** (v1.1) |", "| **82** (v1.0) + **3** (v1.1) + **6** (v1.2) |"),
 ("| Conceptos de dominio (CD) | 48 | 48 | 48 (referenciados", "| Conceptos de dominio (CD) | 48 (v1.0) | 49 | 49 (referenciados"),
 ("Todas las HU del SPEC (103) están en el SRS con ID permanente | ✅ {len(HU_NEW)}/103", "Todas las HU del SPEC (110) están en el SRS con ID permanente | ✅ {len(HU_NEW)}/110"),
 ("Todos los RF del SPEC (162) están en el SRS | ✅ {len(RF_NEW)}/162", "Todos los RF del SPEC (171) están en el SRS | ✅ {len(RF_NEW)}/171"),
 ("(85: 82 de la v1.0 + 3 de la v1.1) están en el SRS; los 2 marcadores vacíos quedan documentados | ✅ {len(RN_NEW)}/85",
  "(91: 82 de la v1.0 + 3 de la v1.1 + 6 de la v1.2) están en el SRS; los 2 marcadores vacíos quedan documentados | ✅ {len(RN_NEW)}/91"),
 ("Toda HU tiene al menos un RF | ✅ {sum(1 for h in HU if HU_RF.get(h))}/103", "Toda HU tiene al menos un RF | ✅ {sum(1 for h in HU if HU_RF.get(h))}/110"),
 ("Todo RF tiene al menos una HU | ✅ {sum(1 for r in RF if RF_HU.get(r))}/162", "Todo RF tiene al menos una HU | ✅ {sum(1 for r in RF if RF_HU.get(r))}/171"),
 ("Todo concepto de dominio (48) es referenciado por algún RF | {'✅' if not cd_unused else '🟡'} {len(cd_used)}/48",
  "Todo concepto de dominio (49) es referenciado por algún RF | {'✅' if not cd_unused else '🟡'} {len(cd_used)}/49"),
 ("| Se conservan 82 (+3 incorporadas en la v1.1) |", "| Se conservan 82 (+3 incorporadas en la v1.1, +6 en la v1.2) |"),
 ("| Rangos HU-001…096 y RF-001…138 (§0.4) | HU-001…103 y RF-001…162 |", "| Rangos HU-001…096 y RF-001…138 (§0.4) | HU-001…110 y RF-001…171 |"),
])
print("build_srs ok")
