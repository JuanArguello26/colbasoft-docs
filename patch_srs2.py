from patch_srs_lib import patch

CAMBIOS_SRS = """## Control de cambios de la versión 1.2

> La v1.2 se regenera desde las mismas fuentes, tras incorporar al SPEC v1.2 las decisiones del Director del **30 de septiembre de 2026** (`DEC-01 = A — Núcleo, con 1 bodega piloto`, más la capa de trazabilidad por pieza). La v1.1 se conserva sin cambios en `SRS_COLBASOFT_v1.1.md`. Las historias y requisitos nuevos **no los crea este SRS**: vienen del SPEC v1.2 y este documento solo les asigna ID permanente y los hace trazables.

| Decisión | Efecto en este SRS |
|---|---|
| **DEC-01 = A** — umbral aprobatorio: Núcleo, 1 bodega piloto | El Cap. 12 fija el **MVP-Núcleo** como umbral aprobatorio: **91 HU y 152 RF** (antes 84 y 143). El **MVP-Completo** pasa a 110 HU y 171 RF. H-08 queda resuelto. Anexo C: DEC-01 resuelta |
| **Q-11 · F-1 · F-2** — trazabilidad por pieza, con cantidad propia registrada al recibir | Historias nuevas HU-ENT-009 (piezas en la recepción) y HU-KDX-006 (trazabilidad por pieza); requisitos nuevos RF-ENT-014, RF-ENT-015, RF-KDX-008 y RF-INV-009; reglas nuevas **RN-LOT-006** y **RN-LOT-007**; concepto nuevo CD-49 «Pieza» |
| **F-6** — contenedores y bolsas agrupadas | HU-ENT-010 y RF-ENT-016 (un contenedor es una pieza de un solo SKU + Lote; la mezcla de lotes queda como DECISIÓN PENDIENTE, HD-28) |
| **F-4** — el operario selecciona la pieza tras el escaneo | HU-MOV-008, RF-MOV-012, regla nueva **RN-MOV-011** |
| **Q-10 · F-3** — el escaneo de salida verifica y cuenta; corte parcial | HU-SAL-008 y HU-SAL-009, RF-SAL-012 y RF-SAL-013, reglas nuevas **RN-SAL-008** y **RN-SAL-009** |
| **F-5** — conteo manual pieza por pieza | HU-CNT-010, RF-CNT-014, regla nueva **RN-CNT-009** |
| **Q-09** — la reimpresión conserva el mismo QR | Cambia el texto de **RN-IDE-004**, **RF-QRC-006**, los criterios 2–4 de **HU-QRC-004** y sus escenarios Gherkin. Los motivos de reemplazo de un identificador quedan como DECISIÓN PENDIENTE (HD-28) |
| **Nivel Ingeniería** | Se corrige R-S03 (decía «nivel Tecnólogo») |

Cifras de la v1.2: historias **110** (antes 103), requisitos funcionales **171** (antes 162), escenarios **498** (antes 462), reglas **91** (antes 85), conceptos de dominio **49**. No cambian los 47 RNF, los 24 casos de uso, los 24 KPI ni los 19 HU / 19 RF del Horizonte 2. Los números del Cap. 0 que siguen describen la reconstrucción de contexto de la v1.0 y se conservan como registro histórico.

"""

patch("cap00.md", [
 ("# SRS_COLBASOFT v1.1\n", "# SRS_COLBASOFT v1.2\n"),
 ("| **Versión** | 1.1 |", "| **Versión** | 1.2 |"),
 ("| **Fecha** | 28 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) |",
  "| **Fecha** | 28 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) · 30 de septiembre de 2026 (v1.2) |"),
 ("| **Estado** | **Validado técnicamente** (cierre del CP-04, 29-sep-2026). **Aprobación funcional y académica pendiente**: HD-25 y DEC-01…DEC-09 sin responder (`04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md`) |",
  "| **Estado** | **Borrador v1.2** (30-sep-2026): incorpora DEC-01 = A con la capa de trazabilidad por pieza. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: DEC-02…DEC-09 sin responder y acta de DEC-08 |"),
 ("| **Versión anterior** | `SRS_COLBASOFT_v1.0.md` (28-sep-2026), conservada sin cambios |",
  "| **Versión anterior** | `SRS_COLBASOFT_v1.1.md` (29-sep-2026) y `SRS_COLBASOFT_v1.0.md` (28-sep-2026), conservadas sin cambios |"),
 ("COLBASOFT_SPEC v1.1 → **SRS v1.1** |", "COLBASOFT_SPEC v1.2 → **SRS v1.2** |"),
 ("`COLBASOFT_SPEC_v1.1.md` (Fase 2, revisado en el cierre del CP-04) |", "`COLBASOFT_SPEC_v1.2.md` (Fase 2, revisado tras la auditoría de DEC-01) |"),
 ("normaliza, reorganiza y hace trazable el contenido aprobado del COLBASOFT_SPEC v1.1.", "normaliza, reorganiza y hace trazable el contenido del COLBASOFT_SPEC v1.2."),
 ("## Control de cambios de la versión 1.1\n", CAMBIOS_SRS + "## Control de cambios de la versión 1.1\n"),
])

patch("cap01.md", [
 ("Los 48 conceptos de dominio están definidos operativamente en el **Capítulo 4 del SPEC** (CD-01…CD-48)", "Los 49 conceptos de dominio están definidos operativamente en el **Capítulo 4 del SPEC** (CD-01…CD-49)"),
 ("| **Novedad** | Reporte de una anomalía física observada por un operario; nunca se elimina, se cierra | CD-48 |",
  "| **Novedad** | Reporte de una anomalía física observada por un operario; nunca se elimina, se cierra | CD-48 |\n| **Pieza** | Unidad física individual de mercancía dentro de un lote (rollo, paquete o bolsa, contenedor agrupado), con cantidad propia registrada en la recepción; el QR no la identifica | CD-49 |"),
 ("| 3 | `COLBASOFT_SPEC_v1.1.md` (5 sep. 2026; v1.1 del 29 sep. 2026) | Fuente principal del SRS |",
  "| 3 | `COLBASOFT_SPEC_v1.2.md` (5 sep. 2026; v1.1 del 29 sep. 2026; v1.2 del 30 sep. 2026) | Fuente principal del SRS |"),
])

patch("cap11.md", [
 ("(H-08, DEC-01).", "(H-08, resuelto por DEC-01 = A en la v1.2: las transferencias y el conteo general quedan fuera del umbral aprobatorio)."),
])

patch("cap12.md", [
 ("El SPEC ubica 19 HU y 19 RF en el Horizonte 2 (v1.1) y, a la vez, mantiene en el alcance MVP (DC-02) las transferencias y los conteos (H-08). Hasta que el Director defina el «entregable mínimo aprobatorio» (S-15, DEC-01), este SRS define **dos umbrales** de aceptación:",
  "El SPEC ubica 19 HU y 19 RF en el Horizonte 2 (v1.1) y, a la vez, mantiene en el alcance MVP (DC-02) las transferencias y los conteos (H-08). **El 30 de septiembre de 2026 el Director resolvió DEC-01 = A**: el «entregable mínimo aprobatorio» (S-15) es el **MVP-Núcleo**, con 1 bodega piloto. Este SRS conserva **dos umbrales** de aceptación, pero solo el primero es aprobatorio:"),
 ("| **MVP-Núcleo (H1)** | Todo lo que el backlog del SPEC declara Horizonte 1 | **84** | **143** |",
  "| **MVP-Núcleo (H1) — umbral aprobatorio `[DEC-01]`** | Todo lo que el backlog del SPEC declara Horizonte 1, incluida la trazabilidad por pieza (elemento 40, v1.2): 84 HU y 143 RF de la v1.1 más 7 HU y 9 RF de la v1.2 | **91** | **152** |"),
 ("| **103** | **162** |\n", "| **110** | **171** |\n"),
 ("**Regla de aceptación mínima:** el MVP no puede aceptarse con menos que el **MVP-Núcleo**. La decisión DEC-01 determina si el umbral aprobatorio es el Núcleo o el Completo.",
  "**Regla de aceptación:** el MVP se acepta con el **MVP-Núcleo** `[DEC-01]`. Lo que el MVP-Completo añade (Horizonte 2: transferencias, conteo general y demás) **no es criterio de aprobación**; queda como entrega posterior."),
 ("| **Must** (P0) | 34 | 32 | 2 | 74 | 73 | 1 |", "| **Must** (P0) | 40 | 38 | 2 | 82 | 81 | 1 |"),
 ("| **Should** (P1) | 54 | 44 | 10 | 70 | 57 | 13 |", "| **Should** (P1) | 55 | 45 | 10 | 71 | 58 | 13 |"),
 ("| **Total** | **103** | **84** | **19** | **162** | **143** | **19** |", "| **Total** | **110** | **91** | **19** | **171** | **152** | **19** |"),
 ("(462 escenarios en total;", "(498 escenarios en total;"),
])

patch("annex_c.md", [
 ("| El Cap. 12 conserva dos umbrales y no puede fijar el criterio de cierre |",
  "| **RESUELTA el 30-sep-2026: opción (a) Núcleo, con 1 bodega piloto y la capa de trazabilidad por pieza (v1.2).** El Cap. 12 fija el Núcleo como umbral aprobatorio |"),
 ("Alcance desproporcionado para nivel Tecnólogo: 103 HU · 162 RF · 47 RNF · 82 RN", "Alcance desproporcionado para nivel Ingeniería (corregido en la v1.2; decía «Tecnólogo»): 110 HU · 171 RF · 47 RNF · 91 RN (MVP-Completo)"),
 ("| Umbral MVP-Núcleo (Cap. 12) · decisión DEC-01 | RG-38 |", "| Umbral MVP-Núcleo (Cap. 12): 91 HU · 152 RF, DEC-01 = A | RG-38 |"),
 ("| H-08 | Abierto | DEC-01 |", "| H-08 | **Resuelto en la v1.2** | DEC-01 = A |"),
 ("---\n\n**ESTADO DEL ANEXO C**",
  """## C.10 Decisiones del Director del 30 de septiembre de 2026 (versión 1.2)

> Tomadas al auditar DEC-01. **Sí responden una DEC-nn (DEC-01)** y resuelven HD-25 del modelo de dominio. Las DEC-02…DEC-09 siguen abiertas.

| ID | Decisión | Efecto en este SRS |
|---|---|---|
| **DEC-01** | **A — Núcleo, con 1 bodega piloto** | Cap. 12: umbral aprobatorio = MVP-Núcleo (91 HU · 152 RF). Transferencias y conteo general (Horizonte 2) quedan fuera |
| **Q-11** | La trazabilidad por **pieza o rollo está dentro del MVP** | HU-ENT-009, HU-KDX-006, RF-ENT-014, RF-ENT-015, RF-KDX-008, RF-INV-009, RN-LOT-006, RN-LOT-007 |
| **F-1 · F-2** | Pieza = rollo (metros o kilogramos) o paquete/bolsa (unidades); la cantidad de cada pieza se registra al recibir | Ídem; CD-49 |
| **F-3** | Se permiten cortes parciales de rollos | HU-SAL-009, RF-SAL-013, RN-SAL-008 |
| **F-4** | El operario selecciona la pieza tras el escaneo; la ubicación filtra y verifica | HU-MOV-008, RF-MOV-012, RN-MOV-011 |
| **F-5** | El conteo es manual, pieza por pieza | HU-CNT-010, RF-CNT-014, RN-CNT-009 |
| **F-6** | Contenedores y bolsas agrupadas dentro del MVP | HU-ENT-010, RF-ENT-016 |
| **Q-09** | La reimpresión conserva el mismo QR | RN-IDE-004, RF-QRC-006, HU-QRC-004 |
| **Q-10** | El escaneo de salida verifica y cuenta | HU-SAL-008, RF-SAL-012, RN-SAL-009 |
| Piloto · nivel | 1 bodega · Ingeniería | R-S03 corregido |

**Decisiones que quedan pendientes** (no se inventan): **HD-28** (contenedor con mezcla de lotes; diferencia entre «paquete o bolsa» y «contenedor agrupado»; motivos por los que un identificador se reemplaza ahora que la reimpresión no lo reemplaza), **HD-29** (qué ocurre con el remanente de un corte parcial si se mueve a otra ubicación; movimiento parcial de una pieza) y **HD-30** (si toda referencia se controla por piezas).

---

**ESTADO DEL ANEXO C**"""),
 ("| **Completado** | 9 decisiones · 5 decisiones del cierre del CP-04 (C.9)", "| **Completado** | 9 decisiones · 5 decisiones del cierre del CP-04 (C.9) · decisiones del 30-sep-2026 (C.10)"),
 ("| **Pendiente** | Respuesta del Director a DEC-01…DEC-09 |", "| **Pendiente** | Respuesta del Director a DEC-02…DEC-09 · HD-28, HD-29 y HD-30 |"),
])

patch("uc_a.md", [
 ("4. El Auxiliar cuenta físicamente la mercancía y registra la cantidad recibida por línea; el sistema confirma visualmente cada registro guardado.",
  "4. El Auxiliar cuenta físicamente la mercancía pieza por pieza y registra cada pieza (rollo, paquete, bolsa o contenedor agrupado) con su cantidad propia; la cantidad recibida por línea es la suma de sus piezas (@RN084, @RN085); el sistema confirma visualmente cada registro guardado."),
 ("HU: @HU030 @HU031 @HU032 @HU033 @HU034 @HU036 @HU037 @HU016 · RF: @RF048 @RF049 @RF050 @RF051 @RF052 @RF053 @RF054 @RF055 @RF056 @RF057 @RF058 @RF059 @RF060 · RN: @RN002b @RN003 @RN005 @RN006 @RN007 @RN008 @RN057b @RN054 @RN071 @RN081 @RN083 |",
  "HU: @HU030 @HU031 @HU032 @HU033 @HU034 @HU036 @HU037 @HU016 @HU104 @HU105 · RF: @RF048 @RF049 @RF050 @RF051 @RF052 @RF053 @RF054 @RF055 @RF056 @RF057 @RF058 @RF059 @RF060 @RF163 @RF164 @RF165 · RN: @RN002b @RN003 @RN005 @RN006 @RN007 @RN008 @RN057b @RN054 @RN071 @RN081 @RN083 @RN084 @RN085 |"),
 ("- **A1 · Reimpresión por deterioro:** el Auxiliar o Coordinador la solicita indicando motivo; el identificador nuevo hereda íntegramente la trazabilidad del anterior, que queda **Reemplazado** y consultable en el historial.",
  "- **A1 · Reimpresión por deterioro:** el Auxiliar o Coordinador la solicita indicando motivo; se imprime otra copia del mismo QR: el identificador no cambia, no se crea una nueva identidad y la reimpresión queda consultable en el historial (@RN018, Q-09)."),
 ("- **A3 · Mercancía sin posibilidad de rotulado individual:** se rotula el contenedor y se registra como unidad de manejo agrupada.",
  "- **A3 · Mercancía sin posibilidad de rotulado individual:** se rotula el contenedor con el QR del SKU + Lote y se registra como pieza de tipo contenedor agrupado, con su cantidad de unidades (@RN084, F-6); la mezcla de lotes en un contenedor es DECISIÓN PENDIENTE (HD-28)."),
 ("3. Escanea el identificador de la mercancía y después el de la ubicación.",
  "3. Escanea el identificador de la mercancía, selecciona la pieza que ubica (@RN087) y después escanea el de la ubicación."),
 ("HU: @HU035 @HU024 @HU021 · RF: @RF035 @RF036 @RF039 @RF072 @RF073 @RF076 · RN: @RN019 @RN020 @RN021 @RN022 @RN026 @RN082 |",
  "HU: @HU035 @HU024 @HU021 @HU106 · RF: @RF035 @RF036 @RF039 @RF072 @RF073 @RF076 @RF166 · RN: @RN019 @RN020 @RN021 @RN022 @RN026 @RN082 @RN087 |"),
])

patch("uc_b.md", [
 ("3. El Auxiliar indica la cantidad a mover (total o parcial).",
  "3. El Auxiliar selecciona la pieza que mueve; con varias piezas del mismo lote en la ubicación de origen, la ubicación filtra y verifica qué piezas se ofrecen (@RN087). El movimiento parcial de una pieza entre ubicaciones es DECISIÓN PENDIENTE (HD-29)."),
 ("HU: @HU045 @HU046 · RF: @RF072 @RF073 @RF074 @RF075 @RF076 @RF077 · RN: @RN026 @RN025 @RN027 @RN021 @RN036 @RN028 @RN054 @RN015 @RN083 |",
  "HU: @HU045 @HU046 @HU106 · RF: @RF072 @RF073 @RF074 @RF075 @RF076 @RF077 @RF166 · RN: @RN026 @RN025 @RN027 @RN021 @RN036 @RN028 @RN054 @RN015 @RN083 @RN087 |"),
 ("3. El Auxiliar recibe sus tareas en la tablet, escanea la ubicación y cuenta físicamente.",
  "3. El Auxiliar recibe sus tareas en la tablet, escanea la ubicación y cuenta físicamente, a mano, pieza por pieza (@RN089)."),
 ("4. El Auxiliar registra la cantidad contada; el sistema no le muestra la cantidad esperada, ni antes ni después.",
  "4. El Auxiliar registra la cantidad de cada pieza contada, y la cantidad contada de la unidad de inventario es la suma de sus piezas; el sistema no le muestra la cantidad esperada, ni antes ni después."),
 ("HU: @HU058 @HU059 @HU060 @HU061 @HU062 @HU065 @HU066 · RF: @RF093 @RF094 @RF095 @RF096 @RF097 @RF098 @RF099 @RF100 @RF101 @RF102 @RF105 · RN: @RN039 @RN040 @RN041 @RN042 @RN043 @RN044 @RN029 · KPI: KPI-01 KPI-03 KPI-04 KPI-06 |",
  "HU: @HU058 @HU059 @HU060 @HU061 @HU062 @HU065 @HU066 @HU109 · RF: @RF093 @RF094 @RF095 @RF096 @RF097 @RF098 @RF099 @RF100 @RF101 @RF102 @RF105 @RF169 · RN: @RN039 @RN040 @RN041 @RN042 @RN043 @RN044 @RN029 @RN089 · KPI: KPI-01 KPI-03 KPI-04 KPI-06 |"),
 ("5. El Auxiliar escanea cada unidad al tomarla; el sistema valida que lo escaneado corresponda a lo solicitado.",
  "5. El Auxiliar escanea lo que toma y selecciona la pieza tomada; si corta parte de un rollo, registra la cantidad cortada (@RN086, @RN087); el sistema valida que lo escaneado corresponda a lo solicitado y cuenta cada pieza tomada una sola vez (@RN050, @RN088)."),
 ("HU: @HU038 @HU039 @HU040 @HU041 @HU042 @HU043 @HU044 · RF: @RF061 @RF062 @RF063 @RF064 @RF065 @RF066 @RF067 @RF068 @RF069 @RF070 @RF071 · RN: @RN048 @RN025 @RN031 @RN030 @RN049 @RN050 @RN009 @RN036 @RN051 @RN052 @RN053 · KPI: KPI-11 KPI-13 KPI-16 |",
  "HU: @HU038 @HU039 @HU040 @HU041 @HU042 @HU043 @HU044 @HU107 @HU108 · RF: @RF061 @RF062 @RF063 @RF064 @RF065 @RF066 @RF067 @RF068 @RF069 @RF070 @RF071 @RF167 @RF168 · RN: @RN048 @RN025 @RN031 @RN030 @RN049 @RN050 @RN009 @RN036 @RN051 @RN052 @RN053 @RN086 @RN088 · KPI: KPI-11 KPI-13 KPI-16 |"),
 ("HU: @HU071 @HU072 @HU073 @HU074 @HU075 @HU076 · RF: @RF112 @RF113 @RF114 @RF115 @RF116 @RF117 @RF118 @RF119 · RN: @RN065 @RN067 @RN025 @RN031 @RN032 @RN036 @RN066 |",
  "HU: @HU071 @HU072 @HU073 @HU074 @HU075 @HU076 @HU110 · RF: @RF112 @RF113 @RF114 @RF115 @RF116 @RF117 @RF118 @RF119 @RF171 · RN: @RN065 @RN067 @RN025 @RN031 @RN032 @RN036 @RN066 @RN084 |"),
])
