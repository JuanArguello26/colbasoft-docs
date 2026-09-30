# 04_CP04_CIERRE
## Cierre del Checkpoint CP-04 · Dominio v1.1 · Desbloqueo de la Fase 5

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | 04_CP04_CIERRE |
| **Versión** | 1.0 |
| **Fecha** | 29 de septiembre de 2026 |
| **Solicitado por** | Prompt Maestro «Cierre de CP-04 → Dominio v1.1 → Desbloqueo Fase 5» |
| **Parte de** | `04_CP04_AUDITORIA.md` (auditoría que originó este cierre) |
| **Estado** | Emitido: registra las decisiones DF5 y la aprobación DF5-06 |
| **Naturaleza** | Registro de decisiones y de cambios. Sin arquitectura, tecnologías, modelo de datos ni código |

> ⚠️ **Nota de revisión (29-sep-2026, posterior a la emisión).** Este cierre registró «Aprobado para la Fase 5 (DF5-06), con limitaciones conocidas», condicionado a que el Director aceptara tratar DEC-01…DEC-09 como limitaciones (§2). Esa aceptación no se dio. `04_CP04_DECISIONES_PENDIENTES.md` revisa DF5-06: las portadas v1.1 pasan a «**Validado técnicamente** — aprobación funcional y académica pendiente». Además, HD-25 resultó **bloqueante** mientras la alternativa C siga abierta. El estado vigente es el de ese documento: **DECISIONES REQUERIDAS ANTES DE FASE 5**. El resto de este cierre (decisiones DF5-01…DF5-05, cambios y validaciones) sigue vigente.

> **Convenciones.** Se reutilizan los prefijos de la auditoría: `DF5-nn` (decisión del cierre), `HA-nn` (hallazgo de la auditoría), `B-nn` (bloqueo), `AC-nn` (fila de la matriz de auditoría). Los IDs del SPEC se emparejan con los permanentes del SRS («RN-066 → RN-INT-005»).

## Índice

| § | Contenido |
|---|---|
| 1 | Estado anterior |
| 2 | Decisiones DF5-01, DF5-02, DF5-03, DF5-05 y DF5-06 |
| 3 | Contradicciones encontradas |
| 4 | Cambios realizados |
| 5 | Impacto sobre entidades |
| 6 | Impacto sobre agregados |
| 7 | Impacto sobre invariantes |
| 8 | Impacto sobre estados y transiciones |
| 9 | Impacto sobre eventos |
| 10 | Impacto sobre reglas |
| 11 | Impacto sobre trazabilidad |
| 12 | Impacto sobre SRS y SPEC |
| 13 | Pendientes que NO bloquean la Fase 5 |
| 14 | Pendientes que SÍ bloquearían la Fase 5 |
| 15 | Resultado final de validación |

---

# 1. ESTADO ANTERIOR

La auditoría del CP-04 (`04_CP04_AUDITORIA.md`, 29-sep-2026) terminó con **ESTADO: CP-04 CON BLOQUEOS — DECISIONES REQUERIDAS**. Bloqueaban la Fase 5:

| Bloqueo | Hallazgo | Descripción |
|---|---|---|
| B-01 | HD-04 · HA-01 | Si el QR de mercancía identifica la unidad de inventario (SKU + Lote + Ubicación, RN-066 → RN-INT-005), reubicar exige reetiquetar. Eso choca con «mover no cambia el QR» |
| B-02 | HD-07 | PN-01 paso 10 dejaba la entrada «disponible»; CD-16 y CD-44 la dejan «en recepción» |
| B-12 | HA-02 | La primera ubicación cambiaba la existencia de unidad sin movimiento en el kardex, en contra de IN-03 |
| B-11 | HA-04 | No estaba definido qué pasa con un registro sin conectividad que deja de ser válido al sincronizarse |
| B-14 | HA-07 | Ninguna especificación tenía aprobación escrita |

**Corrección a una cifra del Prompt de cierre.** El Prompt cita «invariantes: 68». La v1.0 tenía **69 invariantes** (IN-01…IN-69). El 68 es el número de **reglas** cubiertas por invariantes; las otras 14 las cubren las políticas: 68 + 14 = 82.

**Corrección a la auditoría.** HA-04 afirmaba que la retención local solo se traza a PN-01, PN-05 y PN-14 (la traza de RN-INT-003). También la exige **RNF-DSP-002** (RNF-010), que habla en general del «registro de movimientos desde tablet». El alcance de la operación sin conectividad no está cerrado; queda como HD-27 (§13).

---

# 2. DECISIONES

Se registran como **decisiones formales de dominio previas a la Fase 5**, tomadas el 29 de septiembre de 2026 en el Prompt Maestro de cierre del CP-04.

## DF5-01 — Identidad del QR

**Decisión.** El QR de mercancía identifica **SKU + Lote**. **No** identifica ubicación, estantería, posición, bodega ni cantidad actual. La ubicación es un dato operativo independiente: un mismo SKU + Lote puede estar a la vez en varias ubicaciones, incluso de bodegas distintas, sin generar otro QR.

**Qué significa conceptualmente** (Prompt, §9). La cadena es **Referencia → SKU → Lote → existencia por ubicación**:

| Nivel | Qué es | Qué lo identifica |
|---|---|---|
| Referencia (E-01) | Modelo comercial | Código de referencia (VO-01) |
| SKU (E-02) | Referencia + talla + color | Combinación SKU (VO-02) |
| Lote (E-04) | Mercancía de un SKU que ingresó en un mismo evento; pertenece a un solo SKU (IN-28) | Código de lote (VO-06) y **el QR de mercancía** |
| Unidad de inventario (E-08) | La existencia de un lote de un SKU **en una ubicación** | **QR de mercancía + ubicación** |

**La definición de Unidad de Inventario sigue siendo válida** (SKU + Lote + Ubicación; RN-INT-005 e IN-04 sin cambios). Lo que cambia es **qué identifica el QR**: el lote de un SKU, no la unidad. Con eso desaparece la contradicción de HA-01 **sin mantener dos modelos**: no hace falta redefinir la unidad, y mover mercancía crea o incrementa otra unidad (otra ubicación) conservando el mismo QR.

**Consecuencia derivada (DF5-01.1, pendiente en la auditoría).** Si el SKU + Lote escaneado tiene existencia en más de una ubicación, la operación necesita la ubicación de origen. Se resuelve con conceptos que ya existían: escaneo del QR de ubicación (PN-03 pasos 3–4) o selección registrada (PN-03 E-05, VO-40). Si no se indica, la operación no se registra. Queda en RN-IDE-001 (SPEC v1.1 RN-015) y en IN-23.

**No se introduce** ninguna tecnología de generación ni de lectura de QR.

## DF5-02 — Estado inicial

**Decisión.** Entrada confirmada → **EN RECEPCIÓN**; después, EN RECEPCIÓN → **DISPONIBLE** cuando la mercancía se ha ubicado correctamente. El estado EN RECEPCIÓN se mantiene y la recepción no se convierte directamente en existencia disponible. Toda zona de recepción tiene al menos una ubicación (antes HD-06). La cantidad dañada sigue ingresando inmovilizada (RN-ENT-006).

## DF5-03 — Ubicación inicial

**Decisión.** La primera ubicación de la mercancía en recepción es un **movimiento interno** en el kardex, desde la ubicación de recepción hacia la ubicación destino. Registra qué, cuánto, desde dónde, hacia dónde, quién, cuándo y por qué (el documento de entrada que la origina).

**Por qué con un concepto existente.** El tipo «Movimiento interno» ya estaba en VO-21. RF-MOV-001 ya describe su flujo (escaneo de mercancía y de ubicación destino) y ya lo cubren la inmutabilidad (IN-02), la indivisibilidad (IN-41, RN-MOV-004), la validación del destino (RN-MOV-002, RN-MOV-005) y la interrupción (RN-MOV-006). No se crea un tipo de movimiento nuevo.

**Regla que se introduce:** RN-MOV-010 (SPEC v1.1 RN-082*), porque ninguna regla existente decía que la primera ubicación **es** un movimiento ni en qué estado queda la cantidad en destino (§10).

## DF5-05 — Sincronización sin conectividad

**Decisión.** Una operación hecha sin conectividad puede quedar pendiente localmente, pero no puede saltarse las reglas de dominio. Al sincronizar:

1. se valida de nuevo contra el estado vigente;
2. se validan las invariantes y reglas aplicables;
3. si es válida, se confirma, con su fecha operativa original;
4. si ya no es válida, **no se aplica**;
5. se registra el rechazo;
6. se abre una novedad cuando corresponda;
7. se conserva la trazabilidad del intento y de su resultado.

La sincronización no puede producir existencia negativa, movimientos inválidos, estados imposibles, duplicados ni pérdida de trazabilidad.

**Criterio de «cuando corresponda»**, definido en este cierre a partir de la decisión: se abre una novedad cuando el registro rechazado **describe un hecho físico ya realizado** (mercancía recibida o trasladada). En ese caso la existencia física puede diferir de la registrada, y la novedad (E-17) es el mecanismo que ya existe para llevar esa diferencia al Coordinador. El criterio es revisable por el Director.

**No se diseña** la implementación técnica (mecanismo de retención, resolución de conflictos, orden de llegada).

## DF5-06 — Aprobación de artefactos

**Decisión.** Después de aplicar las correcciones, las versiones **SPEC v1.1, SRS v1.1, DOMAIN_MODEL v1.1, EVENT_CATALOG v1.1 y GLOSSARY v1.1** quedan identificadas como la base aprobada para continuar a la arquitectura, siempre que no contengan inconsistencias.

**Cómo se aplicó la condición «no declarar aprobado un documento con inconsistencias»:**

| Tipo de inconsistencia | Situación en la v1.1 |
|---|---|
| Las del CP-04 (HA-01, HA-02, HA-04, HD-04, HD-06, HD-07) | **Resueltas** (§3) |
| Introducidas por las correcciones | **Ninguna.** Las validaciones del §15 terminan sin errores; los efectos colaterales de DF5-01 (HD-25, HD-26) quedan registrados como pendientes |
| Heredadas del SPEC y ya registradas (H-01…H-18 del SRS, con las decisiones DEC-01…DEC-09) | **Siguen abiertas.** Son decisiones del Director, no contradicciones del dominio, y ninguna bloquea la arquitectura (§13). No se corrigieron en silencio: la discrepancia 68/82 de las reglas se sigue declarando en SPEC v1.1 y SRS v1.1 |

**La aprobación se registra con esa salvedad** («con limitaciones conocidas no bloqueantes») en la portada de los cinco documentos. Con el criterio más estricto —ninguna decisión abierta—, la aprobación exigiría responder primero DEC-01…DEC-09. Si el Director no acepta tratarlas como limitaciones conocidas, el estado de los cinco documentos vuelve a «Emitido para revisión».

---

# 3. CONTRADICCIONES ENCONTRADAS

| ID | Contradicción | Entre | Resolución |
|---|---|---|---|
| **HA-01 / HD-04** | «El QR identifica la unidad» + «mover no cambia el QR» es imposible si la ubicación forma parte de la identidad de la unidad | CD-07, RN-INT-005 ↔ decisión de diseño previa ↔ PN-02 paso 2, PN-03 E-04, PN-05 | DF5-01: el QR identifica SKU + Lote |
| **HD-07** | La entrada confirmada queda «disponible» (PN-01 paso 10) frente a «en recepción» (CD-16, CD-44) | SPEC consigo mismo | DF5-02; SPEC v1.1 corrige PN-01 |
| **HA-02 / HD-23** | La primera ubicación cambia de unidad sin movimiento, pero la existencia es la suma de los movimientos | SM-06, EV-INV-001 ↔ IN-03, RN-INT-005 | DF5-03 |
| **HA-04 / HD-24** | Un registro retenido puede violar IN-08 al sincronizarse; el SPEC no decía qué pasa | RN-INT-003 ↔ IN-08 | DF5-05 |
| **RN-017 → RN-IDE-003** | «Un código de barras no se asocia a dos unidades» deja de tener sentido si el QR identifica SKU + Lote (un lote puede estar en varias unidades) | RN-IDE-003 ↔ DF5-01 | Se ajusta la regla: «a dos QR de mercancía distintos» (§10). Efecto pendiente en HD-26 |
| **SM-06 (detectada en este cierre)** | PN-06 E-07 recibe una transferencia en la zona de recepción del destino y la resuelve con PN-03, pero SM-06 solo permitía En tránsito → Disponible | SM-06 ↔ PN-06 E-07, CD-16 | Nueva transición En tránsito → En recepción (§8) |
| **Reimpresión (detectada en este cierre, no resuelta)** | Con un QR por lote habrá varias copias impresas del mismo código; RN-IDE-004 emite un código nuevo al reimprimir y el anterior queda Reemplazado, lo que invalidaría las demás copias | RN-IDE-004, SM-05 ↔ DF5-01 | **Pendiente** (HD-25) |

---

# 4. CAMBIOS REALIZADOS

**Método.** Primero se modificaron las fuentes canónicas y después se regeneraron los documentos. No se editó a mano ningún documento generado.

| Artefacto | Tipo de cambio | Cómo |
|---|---|---|
| `01_SPEC_FASE_2/COLBASOFT_SPEC_v1.1.md` | **Nuevo** (la v1.0 queda intacta) | Generado por `99_HERRAMIENTAS/spec/build_spec_v11.py`: 37 reemplazos exactos sobre la v1.0 (cada uno debe aparecer una sola vez, o el script falla), una sección «Control de cambios de la versión 1.1» y una §9.15 con las 3 reglas nuevas |
| `02_SRS_FASE_3/SRS_COLBASOFT_v1.1.md` | **Nuevo** (la v1.0 queda intacta) | Regenerado por `build_srs.py` desde el SPEC v1.1, con cambios en `ids.py` (IDs de las 3 reglas), `trace.py` (RF que las implementan), `cap00.md` (portada y control de cambios), `cap01.md`, `uc_a.md`, `uc_b.md` (CU-06, CU-07, CU-08, CU-10), `g01.txt` (escenarios de HU-QRC-001, 002, 004 y 005) y `annex_c.md` (C.9) |
| `03_DOMINIO_FASE_4/DOMAIN_MODEL.md`, `EVENT_CATALOG.md`, `GLOSSARY.md` | **v1.1** (la v1.0 queda en el historial de git, commit `79f823c`) | Regenerados por `build_f4.py` desde `dm_data.py`, `ev_data.py` y `gl_data.py`; nueva sección DOMAIN_MODEL §0.8 |
| `99_HERRAMIENTAS/dominio/build_f4.py` | Herramienta | Portadas v1.1, §0.8, rangos de IDs calculados desde los datos, **IDs de glosario estables** (los términos de la v1.0 conservan su GL-nnn y los nuevos continúan la numeración), 5.3, RF5-14 |
| `99_HERRAMIENTAS/dominio/xref.py` | Herramienta | Verifica el SPEC y el SRS v1.1, toma el rango de RF5 de los datos y además revisa los documentos de `04_CP04_AUDITORIA/` |
| `99_HERRAMIENTAS/srs/parse_spec.py`, `spec.json`, `dominio/srs_ids.json` | Datos intermedios | Regenerados desde el SPEC v1.1 |
| `04_CP04_AUDITORIA/04_CP04_CIERRE.md` | **Nuevo** | Este documento |
| `CLAUDE.md`, `99_HERRAMIENTAS/README.md` | Guía del repositorio | Estado v1.1 y uso de las herramientas |

**Sin cambios:** la monografía, la Auditoría Fundacional, `COLBASOFT_SPEC_v1.0.md`, `SRS_COLBASOFT_v1.0.md` y `04_CP04_AUDITORIA.md` (la auditoría se conserva tal como se emitió; sus correcciones están en el §1 de este documento).

---

# 5. IMPACTO SOBRE ENTIDADES

26 entidades en la v1.0 y 26 en la v1.1: **ninguna nueva ni retirada**.

| Entidad | Cambio | Decisión |
|---|---|---|
| E-04 Lote | Pasa a ser **lo que identifica el QR de mercancía**; nueva relación con E-09; regla RN-IDE-001 | DF5-01 |
| E-07 Ubicación | Reglas RN-EXI-007 y RN-MOV-010 | DF5-02, DF5-03 |
| E-08 Unidad de inventario | Identidad **sin cambios** (SKU + Lote + Ubicación); se aclara que no tiene QR propio y que se determina con QR de mercancía + ubicación; ciclo de vida: la unidad destino nace con el movimiento de primera ubicación | DF5-01, DF5-03 |
| E-09 Identificador QR | El de mercancía identifica SKU + Lote; la relación pasa de E-08 a E-04; advertencia HD-25 | DF5-01 |
| E-10 Movimiento | La primera ubicación es un movimiento interno; los pendientes de sincronización se confirman o se rechazan una sola vez | DF5-03, DF5-05 |
| E-11 Documento de entrada | Su confirmación deja la existencia en recepción | DF5-02 |
| E-17 Novedad | También la abre el Sistema al rechazar un registro sincronizado que describe un hecho físico | DF5-05 |

---

# 6. IMPACTO SOBRE AGREGADOS

21 agregados en la v1.0 y 21 en la v1.1: **ninguno nuevo**. **No cambia ninguna raíz ni ninguna identidad.**

| Agregado | Cambio |
|---|---|
| AG-05 Unidad de Inventario | Protege además IN-70. Su identidad no cambia (HD-04 resuelto sin tocarla) |
| AG-06 Movimiento | Protege además IN-71 e IN-72 |
| AG-07 Identificador QR | Protege además IN-23; identifica SKU + Lote o ubicación, no la unidad |
| AG-08 Documento de entrada | Protege además IN-70 |
| AG-13 Novedad | Protege además IN-72 (novedad nacida de un rechazo) |

**Operaciones sobre varios agregados (DOMAIN_MODEL §5.3):** pasan de 9 a **11** con «Primera ubicación» (indivisible, AG-06 → dos AG-05) y «Sincronizar un registro retenido» (una sola vez, contra el estado vigente).

---

# 7. IMPACTO SOBRE INVARIANTES

69 invariantes en la v1.0 y **72** en la v1.1.

| Invariante | Cambio | Regla |
|---|---|---|
| IN-23 | **Reformulada:** toda existencia tiene un QR activo, el de su SKU + Lote; la unidad se determina con ese QR más la ubicación; sin ubicación indicada no hay operación | RN-IDE-001 |
| IN-25 | **Reformulada:** el código de barras se asocia a lo sumo a un QR de mercancía | RN-IDE-003 |
| **IN-70** | **Nueva:** la entrada confirmada ingresa En recepción, en una ubicación de una zona de recepción; no se reserva, no sale ni se transfiere hasta ubicarse | RN-EXI-007 |
| **IN-71** | **Nueva:** la primera ubicación es un movimiento interno confirmado en el kardex; ninguna existencia cambia de ubicación sin movimiento | RN-MOV-010 |
| **IN-72** | **Nueva:** un registro retenido se confirma o se rechaza una sola vez, tras validarse de nuevo; nunca se aplica uno que viole una invariante | RN-INT-008 |

**Sin cambios:** IN-03 (la existencia es la suma de los movimientos confirmados), IN-04 (unicidad de SKU + Lote + Ubicación), IN-02 (inmutabilidad), IN-41 (el movimiento interno no altera el total), IN-07 (sin confirmar ni cerrar con pendientes de sincronización). Con IN-71, IN-03 vuelve a cumplirse también en la primera ubicación.

---

# 8. IMPACTO SOBRE ESTADOS Y TRANSICIONES

21 máquinas en ambas versiones. Estados: **75 → 76**. Transiciones: **114 → 117**.

| Máquina | Cambio | Decisión |
|---|---|---|
| SM-06 Estado de inventario | «En recepción» pasa a significar «solo admite el movimiento interno de ubicación». La transición En recepción → Disponible (EV-INV-001) pasa a ser el movimiento de primera ubicación entre dos unidades. **Nueva** En recepción → En tránsito (primera ubicación interrumpida, EV-MOV-003). **Nueva** En tránsito → En recepción (transferencia recibida en la zona de recepción del destino, PN-06 E-07). La guarda de EV-MOV-007 admite completar una primera ubicación interrumpida | DF5-02, DF5-03 |
| SM-07 Movimiento | **Estado nuevo** «Rechazado en sincronización» (final). Pendiente de sincronización → Confirmado exige validar de nuevo (RN-INT-008). **Nueva** Pendiente de sincronización → Rechazado en sincronización (EV-TRZ-007) | DF5-05 |
| SM-05 Identificador QR | Sin cambios; la reimpresión con copias múltiples queda pendiente (HD-25) | — |

---

# 9. IMPACTO SOBRE EVENTOS

164 eventos en la v1.0 y **165** en la v1.1 (derivados: 60 → 61).

| Evento | Cambio |
|---|---|
| **EV-INV-001 Mercancía ubicada** | **Conserva ID y nombre; cambia su semántica.** Antes: cambio de estado de la misma unidad. Ahora: **movimiento interno de primera ubicación confirmado**; la cantidad sale de la unidad de recepción y entra Disponible a la unidad destino. Su entidad origen pasa de E-08 a E-10 Movimiento. |
| **EV-TRZ-007 Registro rechazado al sincronizar** | **Nuevo**, derivado de RN-INT-008. Deja constancia del registro original, su autor, el motivo y el instante; si describe un hecho físico, abre EV-NOV-001 |
| EV-TRZ-004 Registro sincronizado | Ahora exige validar de nuevo contra el estado vigente |
| EV-ENT-012 Entrada confirmada | Deja la existencia en una ubicación de la zona de recepción (RN-EXI-007) |
| EV-QRC-001, EV-QRC-003 | El QR se emite y se activa por SKU + Lote |
| EV-MOV-001, EV-MOV-003 | Reubicación con ubicación de origen si hay varias; interrupción también de la primera ubicación |
| EV-NOV-001 Novedad reportada | También la registra el Sistema al rechazar un registro sincronizado |

**Análisis de EV-INV-001 (Prompt, §11):**

| Opción | Evaluación |
|---|---|
| Sigue siendo correcto sin cambios | **No:** describía un cambio de estado sin movimiento (HD-23) |
| Cambia su semántica | **Sí:** pasa a designar el hecho «movimiento interno de primera ubicación confirmado» |
| Genera un movimiento asociado | Él **es** el movimiento; el registro en el kardex lo sigue EV-TRZ-001, igual que a EV-MOV-001 |
| Requiere un evento nuevo | **No:** crear «Primera ubicación confirmada» duplicaría EV-INV-001 |
| Se divide conceptualmente | **No:** EV-INV-001 (primera ubicación, origen en zona de recepción) y EV-MOV-001 (reubicación) son dos hechos de negocio distintos del mismo tipo de movimiento, sin solaparse |

Todos los eventos siguen nombrando **hechos ocurridos** (participio pasado), no comandos.

**Líneas temporales:** PN-01 incorpora EV-TRZ-007; PN-03, la interrupción (EV-MOV-003) y la nueva semántica de EV-INV-001; PN-05, la retención y la sincronización (EV-TRZ-003, EV-TRZ-004, EV-TRZ-007).

---

# 10. IMPACTO SOBRE REGLAS

**Conteo oficial:** 82 → **85**. El motivo del cambio: DF5-02, DF5-03 y DF5-05 exigen tres comportamientos que ninguna regla existente expresaba. Las tres reglas nuevas están **separadas** de las 82: SPEC v1.1 §9.15, numeradas a continuación de RN-080 con asterisco, como exige la nota de numeración del SPEC (§9.13).

| Regla nueva (SRS) | SPEC v1.1 | Tipo | Decisión | Invariante | RF / HU que la implementan |
|---|---|:--:|---|---|---|
| **RN-EXI-007** | RN-081* | Estructural | DF5-02 | IN-70 | RF-ENT-011, RF-INV-002 / HU-ENT-003, HU-INV-001 |
| **RN-MOV-010** | RN-082* | Estructural | DF5-03 | IN-71 | RF-MOV-001, RF-MOV-002, RF-MOV-005 / HU-ENT-006, HU-MOV-001, HU-MOV-002 |
| **RN-INT-008** | RN-083* | Estructural | DF5-05 | IN-72 | RF-ENT-005 / HU-ENT-002 (ningún RF describe todavía el rechazo; ver §13) |

**Reglas cuyo significado cambia, de forma explícita:**

| Regla | Texto v1.0 | Texto v1.1 | Decisión |
|---|---|---|---|
| RN-015 → RN-IDE-001 | «Toda unidad de inventario debe tener un identificador activo. No existe existencia sin identificador.» | Conserva ese texto y agrega que el identificador de mercancía es el QR del SKU + Lote, que la unidad se determina con ese QR más la ubicación, y que sin ubicación indicada no hay operación | DF5-01 |
| RN-017 → RN-IDE-003 | «… no puede asociarse a dos unidades de inventario distintas» | «… no puede asociarse a dos identificadores QR de mercancía distintos (es decir, a dos SKU + Lote distintos)» | DF5-01 |

**Sin cambios:** las otras 80 reglas, incluida **RN-066 → RN-INT-005** (la unidad es SKU + Lote + Ubicación).

**Cobertura:** **85/85**. 71 reglas quedan cubiertas por invariantes y 14 por políticas (PO-01…PO-14, sin cambios). Ninguna regla queda huérfana; ninguna aparece dos veces en el catálogo del SRS; ninguna invariante cita una regla inexistente.

**La discrepancia 68/82 no se oculta:** SPEC v1.1 la declara en su índice, en §9.13 y en su control de cambios; SRS v1.1 la mantiene en H-01, en el Cap. 8 y en el Anexo B (DEC-03 abierta).

---

# 11. IMPACTO SOBRE TRAZABILIDAD

**Definición operativa (CD-21) sin cambios:** para cualquier unidad o existencia y cualquier momento histórico se puede responder qué, cuánto, dónde, quién, cuándo y por qué. **Alcance MVP sin cambios:** de la entrada a la salida (OP-02).

| Elemento | Antes (v1.0) | Después (v1.1) |
|---|---|---|
| **CD-21** (seis preguntas) | Hueco: el «dónde» de la primera ubicación no quedaba en el kardex (HA-02) | **Completo:** todo cambio de ubicación es un movimiento (IN-71). El «por qué» de la primera ubicación es el documento de entrada |
| Identificación en el tiempo | El QR «de la unidad» se perdía al reubicar | El QR del SKU + Lote es estable en todas las ubicaciones; su historial (RN-IDE-004) se consulta por SKU + Lote |
| **RNF-AUD-003** (H1: reconstruir el inventario a cualquier fecha) | Imposible de forma exacta para la primera ubicación | Posible: existencia = suma de movimientos confirmados (IN-03), sin cambios fuera del kardex. Los registros rechazados nunca entran al kardex y los confirmados conservan su fecha operativa (VO-32). El orden del kardex con registros tardíos sigue en HD-16 (Fase 5) |
| **RF-117 → RF-INV-006** (consulta a fecha de corte, H2) | H2 | **Sigue en H2.** Se distingue la **capacidad interna necesaria desde el MVP** (RNF-AUD-003, H1) de la **funcionalidad disponible para el usuario** (RF-INV-006, H2). No se movió ningún horizonte |
| **KPI-18** (ocupación, H2) | Depende de HD-17 | **Sin cambios:** la existencia por ubicación sigue disponible, pero la ocupación con unidades heterogéneas requiere información real (HD-17) |
| Eventos operacionales | EV-INV-001 sin movimiento | EV-INV-001 es un movimiento; EV-TRZ-007 deja constancia de los rechazos |
| Sincronización | Sin regla para registros inválidos | Todo intento sin conectividad y su resultado quedan registrados (IN-72) |

**Horizontes (Prompt, §14):** no se movió ninguna funcionalidad. Transferencias y conteo general siguen en el Horizonte 2 del backlog (DEC-01 abierta); la consulta a fecha de corte sigue en H2; KPI-18 sigue en H2. La primera ubicación (PN-03, HU-ENT-006) ya era MVP. La nueva transición «En tránsito → En recepción» describe una excepción de transferencias (H2) y no adelanta esa funcionalidad.

---

# 12. IMPACTO SOBRE SRS Y SPEC

**SPEC v1.1:**
- Portada y control de cambios.
- CD-07, CD-08 y CD-09.
- PN-01 (paso 10, resultado y E-07), PN-02 (paso 1 y resultado), PN-03 (pasos 6–7 y E-04) y PN-05 (pasos 1–2 y E-06).
- M-06.
- HU-025, HU-026, HU-028 y HU-029.
- RF-040 y RF-042.
- RN-015 y RN-017.
- §9.13 y §9.14 (notas), §9.15 nueva y §13.7.

**No cambian:** los objetivos, el alcance, los roles, los módulos, los KPI, los RNF, los riesgos ni el backlog.

**SRS v1.1:**

| Elemento | v1.0 | v1.1 |
|---|:--:|:--:|
| Historias de usuario | 103 | 103 (4 con criterios reformulados: HU-QRC-001, HU-QRC-002, HU-QRC-004, HU-QRC-005) |
| Requisitos funcionales | 162 | 162 (2 reformulados: RF-QRC-001, RF-QRC-003) |
| Requisitos no funcionales | 47 | 47 |
| Reglas de negocio | 82 | **85** (+3; 2 reformuladas) |
| Escenarios Gherkin | 462 | 462 (6 escenarios reformulados) |
| Casos de uso | 24 | 24 (CU-06, CU-07, CU-08 y CU-10 actualizados) |
| KPI | 24 | 24 |
| Horizonte H1/H2 de cada HU y RF | — | Sin cambios |

El Anexo C del SRS incorpora la sección C.9 con las decisiones DF5, sin responder ninguna DEC-nn.

---

# 13. PENDIENTES QUE NO BLOQUEAN LA FASE 5

Cada pendiente indica **por qué no bloquea** y, cuando depende de la operación real, qué dato falta (**DECISIÓN PENDIENTE / INFORMACIÓN REQUERIDA**).

| Pendiente | Qué falta | Por qué no bloquea la arquitectura |
|---|---|---|
| **HD-17** Capacidad con unidades heterogéneas | **INFORMACIÓN REQUERIDA:** si la empresa mezcla metros, rollos y unidades en una misma ubicación | La capacidad es un valor de la ubicación en su unidad (VO-12); lo pendiente es la regla de comparación, no la estructura. Afecta a RF-BOD-005 y RF-MOV-005 (H1) y a KPI-18 (H2) |
| **HD-18** Precisión de las cantidades | **INFORMACIÓN REQUERIDA:** con qué precisión se mide la tela | Es un parámetro de VO-13, no una forma del modelo |
| **HD-25** Copias impresas de un QR y reimpresión | **DECISIÓN PENDIENTE / INFORMACIÓN REQUERIDA:** si se rotula cada rollo o pieza, cada bulto o solo el lote; y si la reimpresión por deterioro emite un código nuevo o imprime otra copia | Afecta el ciclo de vida de AG-07 (SM-05), no su identidad ni la de AG-05 |
| **HD-26** Código de barras por SKU frente a QR por SKU + Lote | **INFORMACIÓN REQUERIDA:** qué identifica el código de barras de los proveedores reales | Funcionalidad del Horizonte 2 (SPEC §12.3, elemento 11) |
| **HD-27** Operaciones que se pueden registrar sin conectividad | **INFORMACIÓN REQUERIDA:** conectividad real de la bodega | Con RN-INT-008, cualquier operación retenida es segura; el alcance es una decisión de producto |
| **Número de bodegas** | **INFORMACIÓN REQUERIDA** (y DEC-01) | El dominio ya modela varias bodegas (AG-03); la arquitectura debe soportarlas desde el inicio |
| **Ubicación de origen cuando el lote está en varias (DF5-01.1)** | Confirmación del Director de la consecuencia registrada en RN-IDE-001 | Ya está definida; solo se pide confirmarla |
| **Criterio «cuando corresponda» de DF5-05** | Confirmación del Director (§2) | Ya está definido; solo se pide confirmarlo |
| **RN-INT-008 sin RF propio** | Un RF que describa la revalidación y el rechazo (como las PROP-RN del Anexo C del SRS) | La regla y el evento ya existen; falta el criterio de aceptación |
| **DEC-01** Umbral aprobatorio; transferencias y conteo general | Director | Si la arquitectura se diseña para el alcance completo, solo afecta el plan de entrega |
| **DEC-02** Lista de alcance | Director | La recomendación del SRS mantiene los 20 módulos |
| **DEC-03** 68/82 reglas y renumeración | Director | Es documental; el modelo usa las 85 reales |
| **DEC-04** Estructural frente a configurable | Director | Condiciona el subsistema de configuración; hace falta antes del modelo de datos detallado, no para la arquitectura general |
| **DEC-05** Cierre de jornada | Director | El dominio lo modela (⚠️); falta el criterio de aceptación |
| **DEC-06** Reglas y KPI sin RF (incluido KPI-05) | Director | La captura del dato de KPI-05 debe decidirse antes del modelo de datos detallado |
| **DEC-07** Valorización | Director | El dominio no tiene atributos monetarios |
| **DEC-08** Numeración de fases | Director | DF5-06 atiende la parte de aprobación |
| **DEC-09** Fecha límite de lote | Director | Afecta a un tipo de alerta |
| **HD-05** Existencia en tránsito respecto de su unidad origen | Fase 5 | Decisión de representación |
| **HD-16** Orden del kardex con registros tardíos | Fase 5 | Decisión de diseño; la fecha operativa ya está definida |
| HD-01, HD-08, HD-13, HD-15, HD-19, HD-22 | Confirmación del Director | Tratamiento provisional ya aplicado en el modelo |
| **R-S01** Modelo TO-BE sin levantamiento AS-IS | Levantamiento AS-IS | Riesgo de validación, no de estructura. Las respuestas de HD-17, HD-18, HD-25, HD-26, HD-27 y el número de bodegas salen de ahí |

---

# 14. PENDIENTES QUE SÍ BLOQUEARÍAN LA FASE 5

**Hoy no queda ninguno abierto.** Estos serían los eventos que volverían a bloquearla:

| Situación | Por qué bloquearía | Cómo se detectaría |
|---|---|---|
| El Director **no acepta** tratar DEC-01…DEC-09 como limitaciones conocidas no bloqueantes (§2, DF5-06) | La base quedaría «Emitida para revisión»; la cadena Monografía → … → Arquitectura exige una base aprobada | Respuesta del Director a este cierre |
| Se revierte o modifica **DF5-01** | Cambiaría otra vez la identidad de AG-07 y la forma de determinar AG-05 | Nueva decisión |
| El levantamiento AS-IS muestra que la empresa necesita **trazabilidad por pieza** (cada rollo con identidad propia) | Exigiría «unidades de manejo» (Horizonte 3, HD-22) y cambiaría la identidad de la mercancía | Respuesta a la información requerida de HD-25 |
| Aparece una inconsistencia nueva en la base v1.1 | Violaría la condición de DF5-06 | Las validaciones del §15, repetidas antes de cada fase |

---

# 15. RESULTADO FINAL DE VALIDACIÓN

## 15.1 Validaciones ejecutadas

| # | Validación | Método | Resultado |
|---|---|---|:--:|
| V-1 | Referencias rotas en SRS v1.1, DOMAIN_MODEL, EVENT_CATALOG, GLOSSARY, CLAUDE.md, 04_CP04_AUDITORIA y este documento | `python3 99_HERRAMIENTAS/dominio/xref.py` | ✅ 0 |
| V-2 | IDs del SPEC sin emparejar en los documentos del dominio | `xref.py` | ✅ 0 |
| V-3 | Tablas descuadradas en SRS v1.1, dominio, CLAUDE.md, auditoría y cierre | `xref.py` | ✅ 0 |
| V-4 | Tablas descuadradas en SPEC v1.1 | Mismo criterio que `xref.py` | ✅ 0 |
| V-5 | Cobertura de reglas | Cruce de IN y PO con las RN del SRS | ✅ 85/85 (71 por invariantes + 14 por políticas) |
| V-6 | Reglas duplicadas o huérfanas | Filas del Cap. 8 del SRS; reglas citadas por invariantes | ✅ 85 filas únicas; 0 invariantes con reglas inexistentes |
| V-7 | Ningún ID renumerado ni reutilizado | Comparación v1.0 ↔ v1.1 de GL, PO, IN, HD y EV | ✅ 0 desaparecidos, 0 cambiados de sentido. Nuevos: GL-204, GL-205, IN-70…IN-72, HD-23…HD-27, EV-TRZ-007. EV-INV-001 cambia de semántica de forma explícita (§9) |
| V-8 | Escenarios Gherkin 1:1 con los criterios | Recuento en SRS v1.1 | ✅ 462 |
| V-9 | Extracción del SPEC v1.1 | `parse_spec.py` y comparación con la v1.0 | ✅ Solo cambian HU-025, HU-026, HU-028, HU-029, RF-040, RF-042, RN-015, RN-017, y entran RN-081*…RN-083* |
| V-10 | Reproducibilidad | SPEC v1.1, SRS v1.1 y los tres documentos del dominio, generados dos veces en carpetas temporales y comparados byte a byte, entre sí y con los oficiales | ✅ Idénticos |
| V-11 | Documentos anteriores intactos | `git diff` contra el commit `79f823c` | ✅ Monografía, Auditoría Fundacional, SPEC v1.0 y SRS v1.0 sin cambios |
| V-12 | Sin arquitectura, tecnologías, modelo de datos ni código de producción | Revisión de los cambios | ✅ Los únicos scripts son herramientas de generación documental (`99_HERRAMIENTAS/`) |

## 15.2 Cifras finales

| Elemento | v1.0 | v1.1 |
|---|:--:|:--:|
| Historias / RF / RNF / KPI / Casos de uso / Gherkin | 103 / 162 / 47 / 24 / 24 / 462 | Sin cambios |
| Reglas de negocio | 82 | **85** |
| Subdominios / Entidades / Objetos de valor / Agregados | 15 / 26 / 42 / 21 | Sin cambios |
| Invariantes | 69 | **72** |
| Políticas reactivas | 14 | 14 |
| Máquinas / Estados / Transiciones | 21 / 75 / 114 | 21 / **76** / **117** |
| Eventos (derivados) | 164 (60) | **165** (61) |
| Términos del glosario | 203 | **205** |
| Hallazgos del dominio | 22 | **27** (5 resueltos: HD-04, HD-06, HD-07, HD-23, HD-24) |
| Riesgos para la Fase 5 | 13 (3 críticos) | **14** (2 críticos abiertos: RF5-02 y RF5-03, que son requisitos de entrada de la arquitectura; RF5-01 resuelto) |

## 15.3 Matriz de auditoría del CP-04, repetida

| ID | Decisión | Antes | Ahora |
|---|---|---|---|
| AC-03 | El QR identifica… | CONTRADICTORIO | **CONFIRMADO** — el QR identifica SKU + Lote (DF5-01) |
| AC-05 | Reubicar no cambia el QR | CONTRADICTORIO | **CONFIRMADO** (DF5-01) |
| AC-06 | La entrada queda En recepción | Requiere ratificación | **CONFIRMADO** (DF5-02, RN-EXI-007) |
| AC-07 | En recepción → Disponible al ubicarse | INCOMPLETO | **CONFIRMADO** (DF5-03, RN-MOV-010) |
| AC-09 | Capacidad sin conversiones | INCOMPLETO | INCOMPLETO — información requerida (HD-17); **no bloquea** |
| AC-12 | Seis preguntas de trazabilidad | Confirmado salvo la primera ubicación | **CONFIRMADO** sin excepciones |
| AC-16 | Operaciones indivisibles | Lista incompleta | **CONSISTENTE** (11 operaciones en §5.3) |
| AC-18 | Retención local | INCOMPLETO | **CONFIRMADO** (DF5-05, RN-INT-008); alcance pendiente (HD-27), **no bloquea** |
| AC-19 | Aprobación | Requiere decisión | **CONFIRMADO** (DF5-06), con limitaciones conocidas |
| AC-01, 02, 04, 08, 10, 11, 13, 14, 15, 17 | — | Confirmados o consistentes | Sin cambios |

**Ya no queda ninguna fila CONTRADICTORIO.** AC-07 dejó de estar INCOMPLETO.

## 15.4 Criterio formal de cierre (auditoría, Cap. 10)

| # | Condición | Resultado |
|---|---|:--:|
| C-1 | DF5-01, DF5-02, DF5-03 y DF5-05 respondidas por escrito | ✅ (§2). DF5-01.1 quedó resuelta como consecuencia de DF5-01; DF5-05.1 pasó a HD-27 (no bloquea) |
| C-2 | Dominio v1.1 regenerado desde los datos | ✅ |
| C-3 | `xref.py` sin errores | ✅ |
| C-4 | Ningún ID renumerado ni reutilizado | ✅ (V-7) |
| C-5 | Ninguna fila CONTRADICTORIO; AC-07 ya no INCOMPLETO | ✅ (§15.3) |
| C-6 | Cambios al SPEC y al SRS documentados sin modificar la v1.0 | ✅ Versiones 1.1 nuevas, con control de cambios; las v1.0 intactas |
| C-7 | DEC-01…DEC-09 resueltas o aceptadas por escrito como limitación conocida | 🟡 **Aceptadas mediante DF5-06**, que aprueba la base para la Fase 5 con las decisiones abiertas. Se pide al Director confirmarlo expresamente (§2) |
| C-8 | Aprobación formal de la base v1.1 | ✅ DF5-06, registrada en las cinco portadas y en este documento |
| C-9 | `CLAUDE.md` actualizado | ✅ |

---

**ESTADO: CP-04 VALIDADO — FASE 5 DESBLOQUEADA**

La base aprobada para la arquitectura es: **COLBASOFT_SPEC v1.1 · SRS_COLBASOFT v1.1 · DOMAIN_MODEL v1.1 · EVENT_CATALOG v1.1 · GLOSSARY v1.1**.

Requisitos de entrada obligatorios para la Fase 5 (no son decisiones pendientes):
- indivisibilidad de las 11 operaciones de DOMAIN_MODEL §5.3 (RF5-02);
- concurrencia sobre la disponibilidad de una misma unidad (RF5-03);
- revalidación al sincronizar (RN-INT-008, RF5-05);
- reconstrucción histórica desde el MVP (RNF-AUD-003);
- trazabilidad Monografía → SPEC → SRS → Dominio → Arquitectura → Implementación → Pruebas.

**La arquitectura no se inicia en este documento.**

*Fin de 04_CP04_CIERRE v1.0. La monografía original permanece sin modificaciones.*
