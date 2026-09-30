# 04_CP04_AUDITORIA
## Auditoría del Checkpoint CP-04 y bloqueos de la Fase 5

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | 04_CP04_AUDITORIA |
| **Versión** | 1.0 |
| **Fecha** | 29 de septiembre de 2026 |
| **Solicitado por** | Prompt Maestro de reanudación «CP-04 → Bloqueos de Fase 5 → Arquitectura» |
| **Objeto auditado** | Modelo de Dominio v1.0 (DOMAIN_MODEL · EVENT_CATALOG · GLOSSARY), CP-04 |
| **Estado** | Emitido para decisión del Director |
| **Naturaleza** | Documento **derivado y de control**. No modifica la monografía, la Auditoría Fundacional, el SPEC, el SRS ni el Modelo de Dominio. Sin arquitectura, tecnologías, modelo de datos ni código. |

> **Convenciones de este documento.** Además de los IDs existentes, se usan tres prefijos nuevos, propios de esta auditoría y permanentes: **`AC-nn`** (fila de la matriz de auditoría del CP-04), **`HA-nn`** (hallazgo de esta auditoría, distinto de los `HD-nn` del dominio y de los `H-nn` del SRS), **`B-nn`** (bloqueo candidato de la Fase 5) y **`DF5-nn`** (decisión que se solicita al Director antes de la Fase 5; no reemplaza a `DEC-nn`, las agrupa y ordena). Los IDs del SPEC se emparejan con los permanentes del SRS («RN-066 → RN-INT-005»).

## Índice

| Cap. | Título |
|---|---|
| 1 | Estado de reanudación |
| 2 | Archivos encontrados |
| 3 | Evidencia revisada |
| 4 | Auditoría CP-04 |
| 5 | Matriz de coherencia SPEC ↔ SRS ↔ Dominio |
| 6 | Bloqueos de Fase 5 |
| 7 | Decisiones pendientes |
| 8 | Riesgos |
| 9 | Recomendación de siguiente paso |
| 10 | Criterio formal para declarar CP-04 cerrado |

---

# CAPÍTULO 1 — ESTADO DE REANUDACIÓN

> Reconstrucción hecha **solo con los archivos del repositorio** (`colbasoft-docs`, commit `79f823c` «Estado inicial: COLBASOFT hasta CP-04»). No se usó el contexto de conversaciones anteriores.

## 1.1 Estado real del proyecto frente al estado declarado en el Prompt

| Fase | Declarado en el Prompt | Estado según los archivos | Coincide |
|---|---|---|:--:|
| Fase 0 — Auditoría | Completada | `AUDITORIA_FUNDACIONAL_COLBASOFT.md`, 1-sep-2026. Cerrada (CP-00) | ✅ |
| Fase 1 — Constitución | (no mencionada) | DC-01…DC-08 registradas en SPEC §0.1; 19 de 24 preguntas bloqueantes cerradas (CP-01) | — |
| Fase 2 — SPEC | Completada | `COLBASOFT_SPEC_v1.0.md`, 5-sep-2026. **El archivo dice «Emitido para revisión del Director»**; aprobación sin acta (H-15, DEC-08) | 🟡 |
| Fase 3 — SRS | Completada con observaciones | `SRS_COLBASOFT_v1.0.md`, 28-sep-2026. **«Emitido para revisión»**; DEC-01…DEC-09 sin respuesta (HD-21) | ✅ |
| Fase 4 — Dominio | Completada | Tres documentos, 28-sep-2026. **«Emitido para revisión del Director»**; 13 hallazgos HD requieren decisión | 🟡 |
| Fase 5 — Arquitectura | No iniciada | No existe ningún documento de arquitectura | ✅ |

**Conclusión 1.1.** Ninguna de las tres especificaciones (SPEC, SRS, Dominio) tiene constancia escrita de aprobación. El Prompt las da por completadas; los archivos, no. Se registra como **HA-07** y bloqueo de gobierno **B-14**.

## 1.2 Decisiones constitucionales vigentes (SPEC §0.1, inmodificables)

| # | Decisión | Relevancia para CP-04 |
|---|---|---|
| DC-01 | Empresa de estudio sin nombre | Ejemplos anónimos |
| DC-02 | Alcance MVP cerrado: inventario y logística de bodega | Trazabilidad dentro de la bodega (entrada → salida) |
| DC-03 | Sin ventas, compras completas, producción, contabilidad, nómina, CRM ni facturación | Sin atributos monetarios (HD-09) |
| DC-04 | Cinco roles; el Sistema es actor, no rol | VO-38 Actor |
| DC-05 | Web responsive + tablet | Escaneo por cámara; operación con pérdida de conectividad |
| DC-06 | Integración con Power BI; sin tableros analíticos | Fuera del dominio |
| DC-07 | Sin IA de ningún tipo; «inteligente» = reglas + KPI | Eventos derivados solo por reglas |
| DC-08 | QR identificador principal; código de barras solo consulta | **Centro del bloqueo B-01** |

## 1.3 Decisiones abiertas heredadas

- **SRS, Anexo C:** DEC-01 (umbral aprobatorio y transferencias / conteo general) · DEC-02 (lista de alcance) · DEC-03 (82 reglas y renumeración) · DEC-04 (estructural vs configurable) · DEC-05 (cierre de jornada) · DEC-06 (brechas de trazabilidad: reglas y KPI sin RF) · DEC-07 (valorización) · DEC-08 (aprobación del SPEC y numeración de fases) · DEC-09 (fecha límite de lote).
- **Dominio, Cap. 10:** 22 hallazgos HD-01…HD-22; bloqueante declarado: **HD-04**; requieren decisión del Director: HD-01, HD-04, HD-07, HD-08, HD-09, HD-10, HD-11, HD-13, HD-15, HD-17, HD-19, HD-21, HD-22.
- **Riesgos para la Fase 5 (GLOSSARY, Anexo C):** RF5-01…RF5-13 (tres críticos: RF5-01, RF5-02, RF5-03).

## 1.4 Sobre las «decisiones del CP-04» que enuncia el Prompt

El Prompt (§6) presenta seis decisiones «establecidas al cerrar el dominio». **Ningún archivo del repositorio las registra como decisión**: no hay acta, ni anexo de decisiones, ni cambio de estado en el Modelo de Dominio. Tres de ellas coinciden con la *interpretación de trabajo* del dominio (recepción, inmutabilidad, capacidad sin conversiones), una coincide con el SPEC (trazabilidad) y **una es incompatible con una regla estructural vigente** (QR / identidad; ver HA-01). En esta auditoría se tratan como **propuestas de baseline pendientes de ratificación formal**, no como baseline.

**ESTADO: CONTEXTO RECONSTRUIDO.**

---

**ESTADO DEL CAPÍTULO — 1**

| | |
|---|---|
| **Completado** | Estado real de las fases 0–5 · 8 decisiones constitucionales · 9 DEC + 22 HD + 13 RF5 abiertos · estatus de las decisiones del Prompt |
| **Hallazgos** | HA-07 (ninguna especificación tiene aprobación escrita) |
| **Dependencias** | Ninguna |

---

# CAPÍTULO 2 — ARCHIVOS ENCONTRADOS

## 2.1 Inventario del repositorio

| Carpeta / archivo | Contenido | Tamaño | Rol en esta auditoría |
|---|---|---|---|
| `CLAUDE.md` | Guía de trabajo, jerarquía, reglas, convenciones, hechos conocidos | — | Contexto y reglas |
| `00_MONOGRAFIA_ORIGINAL/MONOGRAFÍA  COLBASOFT.docx` | Fuente académica, inmutable (doble espacio en el nombre) | 168 KB · 92 párrafos | Origen del problema; leída por extracción de texto |
| `00_AUDITORIA_FASE_0/AUDITORIA_FUNDACIONAL_COLBASOFT.md` | Auditoría fundacional | 979 líneas | Reglas innegociables, vacíos C.1.4 y C.1.7 |
| `01_SPEC_FASE_2/COLBASOFT_SPEC_v1.0.md` | Especificación funcional | 3 501 líneas | Fuente de conceptos, procesos, reglas, horizontes |
| `02_SRS_FASE_3/SRS_COLBASOFT_v1.0.md` | Requisitos (ISO/IEC/IEEE 29148 adaptada) | 7 140 líneas | IDs permanentes, trazabilidad, DEC |
| `03_DOMINIO_FASE_4/DOMAIN_MODEL.md` | Modelo de dominio | 1 871 líneas | Objeto auditado |
| `03_DOMINIO_FASE_4/EVENT_CATALOG.md` | Catálogo de eventos | 1 316 líneas | Objeto auditado |
| `03_DOMINIO_FASE_4/GLOSSARY.md` | Glosario + auditoría interna de la Fase 4 | 2 594 líneas | Objeto auditado |
| `99_HERRAMIENTAS/srs/*`, `99_HERRAMIENTAS/dominio/*` | Generadores y verificador (`xref.py`) | 37 archivos en total en el repositorio | Recuento programático y verificación |

## 2.2 Archivos buscados y no encontrados

| Buscado por el Prompt | Resultado | Dónde vive esa información |
|---|---|---|
| Archivo de decisiones | **No existe** | DC en SPEC §0.1 · DEC en SRS Anexo C · HD en DOMAIN_MODEL Cap. 10 |
| Archivo de memoria / notas del proyecto | **No existe** (la memoria del asistente está vacía) | `CLAUDE.md` cumple esa función |
| Documento propio del CP-04 | **No existe** | El CP-04 son los tres documentos de la Fase 4; su auditoría interna está en GLOSSARY, Anexo |
| Acta de aprobación de SPEC, SRS o Dominio | **No existe** | — (HA-07) |

---

**ESTADO DEL CAPÍTULO — 2**

| | |
|---|---|
| **Completado** | 8 documentos y 2 carpetas de herramientas localizados; 4 tipos de archivo buscados y ausentes |
| **Hallazgos** | Las decisiones están dispersas en cuatro documentos; no hay registro único (ver recomendación, Cap. 9) |

---

# CAPÍTULO 3 — EVIDENCIA REVISADA

## 3.1 Verificaciones ejecutadas

| # | Verificación | Método | Resultado |
|---|---|---|---|
| V-A | Referencias rotas, IDs del SPEC sin emparejar, tablas descuadradas | `python3 99_HERRAMIENTAS/dominio/xref.py` | ✅ Sin errores |
| V-B | Recuento de elementos del dominio | Importación de `dm_data.py`, `ev_data.py`, `gl_data.py` | Ver 3.2 |
| V-C | Recuento de elementos del SPEC | `99_HERRAMIENTAS/srs/spec.json` | Ver 3.2 |
| V-D | Recuento de elementos del SRS | IDs únicos y escenarios en `SRS_COLBASOFT_v1.0.md` | Ver 3.2 |
| V-E | Cobertura de las 82 reglas por invariantes y políticas | Cruce de IN/PO del DOMAIN_MODEL con las RN del SRS | ✅ 82/82 (68 por invariantes, 14 por políticas, 0 duplicadas) |
| V-F | Evidencia primaria de cada decisión del Prompt §6 | Lectura de CD-07, CD-08, CD-14…CD-16, CD-21, CD-44, PN-01…PN-06, PN-14, §12.3 del SPEC; RF, RN, RNF y DEC del SRS; E-07…E-13, AG, IN, SM-05…SM-07, HD del dominio | Ver Cap. 4 |
| V-G | Monografía | Extracción de `word/document.xml` y búsqueda de «trazab», «recepci», «QR», «código», «ubicaci» | Solo menciones de trazabilidad como objetivo (Resumen, palabras clave, OE-3 en §5.5, §6, §7.1). **No define QR, recepción ni ubicación** |

## 3.2 Números del Prompt frente a los archivos

| Elemento | Prompt | Real | Fuente | Estado |
|---|:--:|:--:|---|:--:|
| Historias de usuario | 103 | **103** | spec.json · SRS | ✅ |
| Requisitos funcionales | 162 | **162** | spec.json · SRS | ✅ |
| Requisitos no funcionales | 47 | **47** | spec.json · SRS | ✅ |
| Reglas de negocio | 82 | **82** (el SPEC **declara 68**; sus tablas contienen 82; `spec.json` guarda 84 filas porque incluye los marcadores vacíos `RN-069*` y `RN-026b*`) | SPEC §9 · SRS H-01 | 🟡 DEC-03 |
| KPI | 24 | **24** | spec.json | ✅ |
| Escenarios Gherkin | 462 | **462** | SRS | ✅ |
| Casos de uso | 24 | **24** (CU-19 sin HU ni RF) | SRS | ✅ |
| Subdominios | — | 15 | dm_data | — |
| Entidades | 26 | **26** | dm_data | ✅ |
| Objetos de valor | 42 | **42** | dm_data | ✅ |
| Agregados | 21 | **21** | dm_data | ✅ |
| Invariantes | 69 | **69** | dm_data | ✅ |
| Reglas reactivas (políticas) | 14 | **14** (PO-01…PO-14) | DOMAIN_MODEL §6.2 | ✅ |
| Estados | 75 | **75** en 21 máquinas | dm_data | ✅ |
| Transiciones | 114 | **114** | dm_data | ✅ |
| Eventos | 164 | **164** en 20 dominios (60 derivados; 15 sin RF; 13 sin HU) | ev_data · EVENT_CATALOG | ✅ |
| Términos del glosario | 203 | **203** | gl_data | ✅ |
| Hallazgos del dominio | — | 22 | dm_data | — |
| Riesgos para Fase 5 | — | 13 | GLOSSARY Anexo C | — |

**Conclusión 3.2.** Todos los números del Prompt coinciden con los archivos. La única salvedad es la cifra de reglas, que tiene dos valores en circulación (68 declaradas, 82 reales), ya registrada como H-01 / DEC-03.

---

**ESTADO DEL CAPÍTULO — 3**

| | |
|---|---|
| **Completado** | 7 verificaciones; 19 cifras contrastadas; 0 referencias rotas; 82/82 reglas cubiertas |
| **Hallazgos** | Ninguno nuevo en cifras; persiste DEC-03 |

---

# CAPÍTULO 4 — AUDITORÍA CP-04

## 4.1 Matriz de auditoría de las decisiones del CP-04

Estados: **CONFIRMADO** (la decisión está en el baseline y los tres niveles la sostienen) · **CONSISTENTE** (el dominio la modela de forma coherente con SPEC y SRS, sin necesitar decisión) · **CONTRADICTORIO** (dos fuentes del baseline se oponen) · **INCOMPLETO** (falta un elemento para que funcione de extremo a extremo) · **REQUIERE DECISIÓN** (solo el Director puede cerrarlo).

| ID | Decisión | Evidencia en SPEC | Evidencia en SRS | Evidencia en Dominio | Estado | Impacto |
|---|---|---|---|---|---|---|
| **AC-01** | Modelo Referencia → SKU → Unidad de inventario | CD-02, CD-05, CD-07 | RN-INT-005, RF-INV-004 | E-01, E-02, E-08; AG-01 contiene E-02; AG-05 | **CONFIRMADO** | Base de la identidad |
| **AC-02** | La Unidad de inventario es la raíz de agregado central | CD-07 («la entidad que COLBASOFT controla») | RN-INT-004, RN-INT-005 | AG-05, SD-01 (Core); protege 9 invariantes | **CONFIRMADO** | Su identidad depende de AC-03 |
| **AC-03** | El QR identifica la Unidad de inventario | CD-07 y CD-08 («asociado a una unidad de inventario»), RF-040 → RF-QRC-001, RN-015 → RN-IDE-001, PN-02 paso 1. **Pero** PN-02 paso 2 lo asocia a «referencia + talla + color + lote», sin ubicación | RF-QRC-001, RF-QRC-003 («resolverlos a su unidad de inventario»), RN-IDE-001 | E-09 remite a HD-04; interpretación de trabajo: el QR identifica SKU + Lote (**no adoptada**); RF5-01 🔴 | **CONTRADICTORIO → REQUIERE DECISIÓN** | Identidad de AG-05 y AG-07; ver HA-01 |
| **AC-04** | El QR no identifica la ubicación | CD-08 (QR de mercancía o de ubicación); PN-03 pasos 3–4 (dos escaneos) | RF-QRC-003 | E-07 con su propio QR (VO-07); E-09 con tipo mercancía / ubicación | **CONFIRMADO** | Ninguno |
| **AC-05** | Reubicar no cambia el QR | PN-05 (movimiento interno sin reetiquetado), PN-03 E-04 (una mercancía repartida en varias ubicaciones). **Pero** CD-07 y RN-066 → RN-INT-005: la ubicación es parte de la identidad de la unidad | Ningún RF exige reetiquetar al mover; RN-INT-005 vigente | HD-04 lo señala como el motivo del conflicto | **CONTRADICTORIO → REQUIERE DECISIÓN** | Junto con AC-03 es lógicamente imposible sin modificar RN-INT-005 o el alcance del QR (HA-01) |
| **AC-06** | La entrada confirmada deja la mercancía En recepción | CD-16 («aún no está disponible»), CD-44 (estado «En recepción»), RG-11 (mitigación: «existencia en recepción no cuenta como disponible»). **Pero** PN-01 paso 10 y su resultado dicen «existencia **disponible**» | RF-INV-002 (estado «en recepción»); RF-ENT-011 («incrementar la existencia», sin estado) | SM-06 estado inicial «En recepción»; EV-ENT-012; HD-07 | **CONSISTENTE en el dominio; contradicción interna del SPEC → REQUIERE DECISIÓN (ratificación)** | Bajo si se ratifica; el Prompt ya lo enuncia |
| **AC-07** | De En recepción pasa a Disponible al ubicarse | PN-03 (pasos 3–7: registra la asignación, «actualiza la existencia por ubicación»); CD-16 | HU-ENT-006 («registra la ubicación confirmada»), RF-MOV-005 | SM-06: En recepción → Disponible por EV-INV-001 «Mercancía ubicada», como cambio de estado **de la misma unidad** | **INCOMPLETO** | Con RN-INT-005, ubicar cambia de unidad sin movimiento (HA-02) |
| **AC-08** | Toda existencia disponible reside en una ubicación; la zona de recepción tiene ubicaciones | CD-14, CD-16, RN-019 → RN-EXI-002 | RN-EXI-002 | IN-09; HD-06 (la zona de recepción contiene ≥ 1 ubicación); HD-05 (en tránsito, asociada a la unidad origen) | **CONSISTENTE** (HD-05 y HD-06 por confirmar) | Condiciona la definición de unidad (RF5-10) |
| **AC-09** | Capacidad en unidades heterogéneas; sin conversiones inventadas | CD-15 («en la unidad configurada»), RN-021 → RN-MOV-002, RN-068 → RN-INT-007; KPI-18 en Horizonte 2 (§12.3, elemento 15) | RF-BOD-005 (H1), RF-MOV-005 (H1), RF-ALE-004 (sobreocupación, H1) | VO-12, IN-06, IN-43, HD-17, HD-18, RF5-06 | **INCOMPLETO → REQUIERE DECISIÓN** | Tres RF del MVP validan capacidad sin regla para ubicaciones con unidades mixtas (HA-05) |
| **AC-10** | El movimiento confirmado es inmutable | RN-012 → RN-INT-002; PN-07 (anulación por movimiento inverso) | RN-INT-002, RF-KDX-003, RF-KDX-004, RNF-AUD-002 | IN-02; SM-07 (Confirmado es final); HD-03 descarta «Ejecutado» y «Auditado» | **CONFIRMADO** | Ninguno |
| **AC-11** | La auditoría no modifica el movimiento confirmado | PR-02; RN-064 → RN-AUD-002; SPEC §2.7 (el Auditor no escribe en el inventario) | RN-AUD-002 | AG-17 Observación de auditoría separada del inventario; HD-03 | **CONFIRMADO** | Ninguno |
| **AC-12** | Trazabilidad: qué, cuánto, dónde, quién, cuándo, por qué | CD-21; criterio (3) de la HU del kardex («las seis preguntas de trazabilidad») | RF-KDX-001 (fecha, hora, tipo, cantidad, existencia resultante, ubicación, usuario, motivo, documento), RF-KDX-002, RNF-AUD-001 | E-10 (responsabilidad: «qué cambió, cuánto, dónde, quién, cuándo y por qué») | **CONFIRMADO**, con la excepción de la ubicación inicial (HA-02) | El «dónde» de la primera ubicación no queda en el kardex |
| **AC-13** | Trazabilidad para un momento histórico | RF-117 → RF-INV-006 en Horizonte 2 (§12.3, elemento 7: «el kardex ya permite la reconstrucción manual») | **RNF-AUD-003 (H1):** reconstruir el inventario a cualquier fecha pasada; RF-INV-006 (H2) | IN-03 (existencia = suma de movimientos); HD-16 (fecha operativa ≠ instante de sincronización) | **CONSISTENTE con matiz** | La capacidad es H1 y la pantalla H2 (HA-03) |
| **AC-14** | Alcance MVP de la trazabilidad: de la entrada a bodega a la salida de bodega | OP-02 («desde su entrada hasta su salida»); DC-02 | Módulos M-07 (entradas) … M-08 (salidas) | 15 subdominios, todos dentro de la bodega | **CONFIRMADO** | Ninguno |
| **AC-15** | Eventos | Procesos PN-01…PN-14 | 162 RF, 103 HU | 164 eventos, 14 líneas temporales, matrices D y E; 15 eventos sin RF y 13 sin HU (heredados de H-10, H-11, HD-19) | **CONSISTENTE / INCOMPLETO** (brechas heredadas, no nuevas) | RF5-12 |
| **AC-16** | Operaciones sobre dos unidades: todo o nada | RN-026 → RN-MOV-004; PN-06 paso 9 | RF-MOV-002 | DOMAIN_MODEL §5.3 (9 operaciones); RF5-02 🔴 | **CONSISTENTE** (la lista de §5.3 no incluye la ubicación inicial: HA-02) | Requisito de entrada para la Fase 5 |
| **AC-17** | Concurrencia sobre la misma unidad | RN-025 → RN-EXI-003; RN-031 → RN-EXI-004 | RN-EXI-003, RN-EXI-004 | IN-08, IN-10, IN-11; RF5-03 🔴 | **CONSISTENTE** | Requisito de entrada para la Fase 5 |
| **AC-18** | Retención local sin conectividad | RN-054 → RN-INT-003; PN-01 E-07, PN-05 E-06, PN-14 E-02 | RN-INT-003 (trazado solo a PN-01, PN-05, PN-14) | SM-07 «Pendiente de sincronización»; IN-07; HD-16; RF5-05 | **INCOMPLETO → REQUIERE DECISIÓN** | No se define qué ocurre si al sincronizar se viola una invariante (HA-04) |
| **AC-19** | Estado de aprobación de las especificaciones | «Emitido para revisión» | «Emitido para revisión»; DEC sin respuesta | «Emitido para revisión»; HD-21 | **REQUIERE DECISIÓN** | La cadena de trazabilidad exige una base aprobada (HA-07) |

**Totales de la matriz:** 19 filas · CONFIRMADO 7 (AC-01, 02, 04, 10, 11, 12, 14) · CONSISTENTE 5 (AC-06 en el dominio, AC-08, 13, 16, 17) · CONTRADICTORIO 2 (AC-03, AC-05) · INCOMPLETO 4 (AC-07, 09, 15, 18) · REQUIERE DECISIÓN 7 (AC-03, 05, 06, 09, 18, 19 y, por dependencia, AC-07). Un mismo elemento puede tener dos estados.

## 4.2 Hallazgos de esta auditoría

| ID | Sev. | Hallazgo | Evidencia | Qué NO se hizo |
|---|:--:|---|---|---|
| **HA-01** | 🔴 | **La decisión del Prompt sobre el QR es incompatible con RN-INT-005 si se lee literalmente.** El Prompt afirma: (1) el QR identifica la Unidad de inventario y (2) mover una unidad no cambia su QR. Por CD-07 y RN-066 → RN-INT-005, la unidad **es** la combinación SKU + Lote + Ubicación: al moverla a otra ubicación se trata de otra unidad. Además, PN-03 E-04 reparte una misma mercancía rotulada en varias ubicaciones (una etiqueta, varias unidades). Las dos afirmaciones solo pueden valer juntas si **(a)** el QR identifica SKU + Lote (lo que ya propone HD-04) o **(b)** se redefine la unidad sin la ubicación (modifica una regla estructural del SPEC). | CD-07, CD-08, RN-INT-005, RN-IDE-001, RF-QRC-001, RF-QRC-003, PN-02 pasos 1–2, PN-03 E-04, PN-05, HD-04 | No se eligió ninguna opción. Se eleva como **DF5-01** |
| **HA-02** | 🔴 | **La primera ubicación de la mercancía cambia la existencia de unidad sin movimiento en el kardex.** Tras la entrada, la existencia está en la unidad (SKU, Lote, *ubicación de recepción*). Al ubicarla (PN-03, HU-ENT-006) pasa a (SKU, Lote, *ubicación de almacenamiento*): otra unidad. El dominio lo modela como un cambio de estado de la misma unidad (SM-06, EV-INV-001), VO-21 no tiene tipo de movimiento para ello y ningún RF exige dejarlo en el kardex. Esto choca con IN-03 / RN-INT-004 (la existencia de una unidad es la suma de sus movimientos) y deja sin «dónde» el primer tramo de la trazabilidad (CD-21). La operación tampoco figura en la lista de operaciones indivisibles (§5.3). | PN-03 pasos 6–7, HU-ENT-006 C2, EV-INV-001, SM-06, VO-21, IN-03, IN-04, IN-41, DOMAIN_MODEL §5.3 | No se corrigió el dominio. Se eleva como **DF5-03** |
| **HA-03** | 🟠 | **La reconstrucción histórica es obligatoria desde el MVP aunque su pantalla sea de v1.1.** RNF-AUD-003 (H1) exige reconstruir el inventario a cualquier fecha pasada, con resultado idéntico; RF-INV-006 (consulta a fecha de corte) está en H2. No es contradicción, pero la Fase 5 no puede postergar la capacidad. | RNF-AUD-003, RF-INV-006, SPEC §12.3 elemento 7 | Se registra como requisito de entrada para la arquitectura |
| **HA-04** | 🟠 | **No está definido qué pasa si un registro retenido sin conectividad viola una invariante al sincronizarse.** IN-08 prohíbe dejar existencia negativa «sin excepción ni autorización posible», pero el hecho físico ya ocurrió. RF5-05 nombra el riesgo sin resolverlo. La retención local solo está trazada a recepción (PN-01), movimiento interno (PN-05) y cierre de jornada (PN-14). | RN-INT-003, IN-07, IN-08, SM-07, RF5-05 | No se inventó política. Se eleva como **DF5-05** |
| **HA-05** | 🟠 | **La capacidad afecta al MVP, no solo al KPI-18.** KPI-18 (ocupación) es H2, pero RF-BOD-005, RF-MOV-005 y RF-ALE-004 (sobreocupación) son H1 y necesitan comparar existencia y capacidad en ubicaciones que pueden mezclar metros, rollos y unidades, sin conversión permitida (IN-06). | RF-BOD-005, RF-MOV-005, RF-ALE-004, RN-MOV-002, IN-06, HD-17, SPEC §12.3 elemento 15 | No se inventaron equivalencias. Se eleva como **DF5-04** |
| **HA-06** | 🟡 | **Un escaneo de mercancía puede resolver a varias unidades.** Si el QR identifica SKU + Lote (HD-04) y ese lote está en varias ubicaciones (PN-03 E-04), RF-QRC-003 («resolverlos a su unidad de inventario») y PN-05 paso 2 («el sistema muestra su ubicación actual») necesitan saber la ubicación de origen. Ningún documento lo define. | RF-QRC-003, PN-05 pasos 1–2, PN-03 E-04 | Se incluye como sub-decisión de **DF5-01** |
| **HA-07** | 🟡 | **Ninguna especificación tiene aprobación escrita** (SPEC, SRS, Dominio), aunque los prompts las declaran aprobadas. | Portadas de los tres niveles; H-15, HD-21, DEC-08 | Se eleva como **DF5-06** |
| **HA-08** | 🟡 | **Las decisiones del proyecto no tienen un registro único.** DC en el SPEC, DEC en el SRS, HD en el Dominio y ahora DF5 aquí; las decisiones del Prompt de reanudación no quedaron escritas en ningún archivo. | Cap. 2.2 | Recomendación en Cap. 9 |
| **HA-09** | 🟡 | **Diferencia de representación del movimiento interno interrumpido.** PN-05 E-05 dice que la existencia «no está en origen ni en destino»; HD-05 la asocia a la unidad origen en estado «En tránsito». Ambas cumplen IN-12 (no disponible en ninguna); la diferencia es de representación. | PN-05 E-05, HD-05, IN-12 | Resoluble en la Fase 5 junto con HD-05 |

## 4.3 Consistencia interna del Modelo de Dominio

| Verificación | Resultado |
|---|---|
| Referencias cruzadas (V-A) | ✅ 0 rotas |
| Reglas cubiertas por invariantes o políticas | ✅ 82/82 |
| Entidades, eventos, estados e invariantes citados existen | ✅ (GLOSSARY Anexo B, V-1…V-4, reverificado con xref) |
| Máquina SM-06 frente a la identidad de E-08 | ❌ **HA-02** |
| Lista de operaciones indivisibles (§5.3) | 🟡 Falta la ubicación inicial (HA-02) |
| Identidad de AG-05 / AG-07 | 🟡 Pendiente de HD-04 (declarado por el propio dominio) |
| Vocabulario controlado | ✅ Sin sinónimos prohibidos en las definiciones (GLOSSARY V-10, V-12) |
| Documentos previos sin modificar | ✅ |

**Dictamen 4.3.** El dominio es internamente consistente **salvo HA-02**, que es un defecto del propio modelo (no heredado). Su corrección es acotada: SM-06, EV-INV-001, §5.3 y, según DF5-03, VO-21. No exige revisar el resto del modelo.

---

**ESTADO DEL CAPÍTULO — 4**

| | |
|---|---|
| **Completado** | 19 filas AC con evidencia en tres niveles · 9 hallazgos HA · dictamen de consistencia interna |
| **Riesgos** | HA-01 y HA-02 afectan la identidad y el kardex, la base de todo lo demás |
| **Dependencias** | DF5-01 condiciona DF5-03 |
| **Hallazgos** | HA-01…HA-09 |

---

# CAPÍTULO 5 — MATRIZ DE COHERENCIA SPEC ↔ SRS ↔ DOMINIO

## 5.1 Coherencia de volumen

| Elemento | Monografía | SPEC | SRS | Dominio | Coherente |
|---|---|---|---|---|:--:|
| Objetivos | OG, OE-1…OE-3 (§5, §5.5) | OP-01…OP-12 | Objetivo por módulo | — | ✅ |
| Procesos | — | 14 (PN-01…PN-14) | 24 CU | 14 líneas temporales | ✅ (CU-19 sin HU/RF) |
| Conceptos | 5 conceptos formales (§7.1) | 48 (CD-01…CD-48) | — | 203 términos; 26 entidades | ✅ |
| Historias | — | 103 | 103 (462 escenarios) | 94 con evento; 9 de consulta | ✅ |
| RF | — | 162 (74/70/18 por prioridad) | 162 | 138 con evento; 24 de consulta, restricción o presentación | ✅ |
| RNF | — | 47 | 47 | No aplica al dominio | ✅ |
| Reglas | — | **68 declaradas / 82 en tablas** | 82 | 82 (68 IN + 14 PO) | 🟡 DEC-03 |
| KPI | Indicadores §8.2 | 24 | 24 | 24/24 en algún evento | ✅ (6 sin dato de captura: DEC-06) |
| Roles | — | 5 + Sistema como actor | 5 | VO-36 (5 valores), VO-38 | ✅ |

## 5.2 Coherencia de conceptos críticos

| Concepto | SPEC | SRS | Dominio | Coherente |
|---|---|---|---|:--:|
| Identidad de la unidad | CD-07: SKU + Lote + Ubicación | RN-INT-005 | E-08, IN-04 | ✅ entre sí; ❌ con el Prompt (HA-01) |
| Alcance del QR | CD-08 / PN-02 paso 1 frente a PN-02 paso 2 | RF-QRC-001, RN-IDE-001 | HD-04 (sin decidir) | ❌ AC-03 |
| Estado inicial de la entrada | CD-16, CD-44 frente a PN-01 paso 10 | RF-INV-002 | SM-06, HD-07 | 🟡 AC-06 |
| Ubicación inicial | PN-03 | HU-ENT-006 | EV-INV-001 sin movimiento | ❌ AC-07 / HA-02 |
| Movimiento inmutable | RN-012 → RN-INT-002 | RF-KDX-003 | IN-02, SM-07 | ✅ |
| Existencia derivada | RN-065 → RN-INT-004 | RF-INV-003, RNF-AUD-005 | IN-03 | ✅ (salvo HA-02) |
| Sin conversiones | RN-068 → RN-INT-007 | RN-INT-007 | IN-06, VO-13 | ✅ |
| Capacidad | CD-15, RN-021 → RN-MOV-002 | RF-BOD-005, RF-MOV-005 | VO-12, HD-17 | 🟡 AC-09 |
| Tránsito | RN-032 → RN-EXI-005 | RN-EXI-005 | IN-12, HD-05 | ✅ (HA-09 de representación) |
| Reubicación | PN-05, RN-026 → RN-MOV-004 | RF-MOV-001, RF-MOV-002 | IN-41, AG-06 | ✅ |
| Auditoría sin escritura | PR-02, §2.7 | RN-AUD-002 | AG-17 | ✅ |
| Retención local | RN-054 → RN-INT-003 | RN-INT-003 | SM-07, IN-07 | 🟡 AC-18 |
| Cierre de jornada | PN-14 (MVP, backlog elemento 39) | Sin HU/RF (H-10) | E-26, AG-21, SM-21 ⚠️ | 🟡 DEC-05 |
| Alcance de entrega | §12.3: transferencias y conteo general en v1.1 | H-08, DEC-01 | Modelados completos (R-S04) | 🟡 DEC-01 |

## 5.3 Monografía → cadena

La monografía aporta el **problema** y el **objetivo de trazabilidad** (OE-3 en §5.5; §6; §7.1: la automatización «mejora la trazabilidad»), pero **no define** QR, recepción, ubicación, capacidad ni kardex por unidad. Todas las decisiones auditadas en el Cap. 4 son de origen `[NUEVO]` (SPEC) o `[DC-08]`. Ninguna contradice la monografía, y ninguna puede justificarse solo con ella: su autoridad está en el SPEC y en las decisiones del Director.

---

**ESTADO DEL CAPÍTULO — 5**

| | |
|---|---|
| **Completado** | 9 filas de volumen · 14 conceptos críticos · lectura desde la monografía |
| **Hallazgos** | 3 incoherencias (❌): identidad frente al Prompt, alcance del QR, ubicación inicial. Las tres convergen en B-01 y B-12 |

---

# CAPÍTULO 6 — BLOQUEOS DE FASE 5

Criterio de «¿Bloquea?»: **Sí** = la arquitectura no puede fijar la identidad, el kardex o el flujo afectado sin la respuesta, y cambiarla después obligaría a rehacer la base. **Parcial** = la arquitectura puede empezar, pero la respuesta hace falta antes del modelo de datos detallado. **No** = puede documentarse como backlog o como requisito de entrada ya definido.

| Bloqueo | Origen | Descripción | Impacto arquitectónico | ¿Bloquea? | Resolución propuesta | Decisión requerida |
|---|---|---|---|:--:|---|---|
| **B-01** Identidad y QR | HD-04, HA-01, HA-06, RF5-01 | El QR de mercancía identifica SKU + Lote **o** la unidad (SKU + Lote + Ubicación). La lectura literal del Prompt es incompatible con RN-INT-005 | Identidad de AG-05 y AG-07; resolución del escaneo; comportamiento al reubicar y al repartir | **Sí** 🔴 | Opción (a) de DF5-01: mantener RN-INT-005 y declarar que el QR de mercancía identifica SKU + Lote; la unidad se resuelve con QR de mercancía + QR de ubicación. Fe de erratas de la redacción «un QR por unidad» en CD-08 / RF-QRC-001 / RN-IDE-001 | **DF5-01** |
| **B-02** Estado en recepción | HD-07, HD-06, AC-06 | La entrada confirmada ¿queda En recepción o Disponible? | Primer estado de la existencia; KPI-05, KPI-12; RG-11 | **Sí**, pero solo requiere ratificar | Ratificar la interpretación del dominio (y del Prompt): En recepción; fe de erratas de PN-01 paso 10 y de su resultado | **DF5-02** |
| **B-03** Capacidad tipada | HD-17, HD-18, HA-05, RF5-06 | La capacidad está en «la unidad configurada», pero una ubicación puede alojar metros, rollos y unidades; no hay conversiones | Validación de destinos y alerta de sobreocupación en H1; precisión de las cantidades | **Parcial** | Ver opciones en DF5-04. No se inventa ninguna equivalencia. La precisión (HD-18) se fija con datos del levantamiento AS-IS | **DF5-04** |
| **B-04** Operaciones sobre dos unidades | RN-MOV-004, §5.3, RF5-02 | Movimiento interno, transferencia, confirmación de entrada, **ubicación inicial (HA-02)**: todo o nada | Garantía de indivisibilidad | **No** (requisito ya definido) | Tomar §5.3, completado con la ubicación inicial, como **requisito de entrada obligatorio** de la Fase 5. El «cómo» es de la Fase 5 | — |
| **B-05** Concurrencia sobre la misma unidad | IN-08, IN-10, IN-11, RF5-03 | Dos operaciones simultáneas no pueden comprometer la misma existencia | Control de concurrencia | **No** (requisito ya definido) | Requisito de entrada obligatorio. Su interacción con la retención local se trata en B-11 | — |
| **B-06** Eventos y trazabilidad | AC-12, AC-13, AC-15, HD-16, HA-03 | 164 eventos definidos; seis preguntas cubiertas salvo la ubicación inicial; reconstrucción histórica exigida en H1 | Registro de hechos, orden del kardex con registros tardíos, reconstrucción a fecha | **No** (salvo lo que depende de B-12) | Requisitos de entrada: RNF-AUD-003 en H1 (HA-03) y fecha operativa = instante del hecho (VO-32, HD-16). El orden del kardex con registros tardíos es decisión de la Fase 5 | — |
| **B-07** Reglas sin requisito | H-11, DEC-06 | RN-MOV-003, RN-MOV-006, RN-NOV-001, RN-NOV-002, RN-CNT-008, RN-SAL-005 sin RF | Bajo: las reglas ya están en el dominio (IN/PO) | **No** | Backlog; aprobar las PROP-RN del SRS (Anexo C) cuando se decida DEC-06 | DEC-06 (no urgente) |
| **B-08** KPI sin dato capturado | H-12, DEC-06 | KPI-05, 07, 10, 12, 17, 24. De ellos, **07, 10 y 12 están en H2** (§12.3, elemento 15); **05, 17 y 24 son del MVP** | Solo **KPI-05** (instante de inicio de la operación; uno de los tres KPI del compromiso) cambia lo que el sistema debe capturar | **Parcial** (solo KPI-05) | Decidir la captura de KPI-05 antes del modelo de datos, porque sin ella no hay línea base desde el primer día (DEC-06, opción mínima b). El resto, backlog | **DF5-09** |
| **B-09** PN-14 Cierre de jornada | H-10, HD-11, DEC-05 | Proceso del MVP sin HU ni RF; el dominio lo modela ⚠️ | Bajo: depende de IN-07 (sin registros sin sincronizar), ya definido | **No** | Backlog con decisión: DEC-05 opción (a) según el SRS | **DF5-10** (no urgente) |
| **B-10** Transferencias y conteo general (MVP frente a v1.1) | H-08, DEC-01, R-S04; SPEC §12.3 («el MVP opera con una bodega») | DC-02 los incluye en el MVP; el backlog los pone en v1.1 | Soporte de varias bodegas y bloqueo de movimientos durante un conteo general | **No**, si la arquitectura se diseña para el alcance completo (el dominio ya lo modela) | DEC-01 recomendación del SRS: alcance completo, entrega H1 → H2, umbral aprobatorio = Núcleo. La arquitectura soporta N bodegas desde el inicio | **DF5-08** |
| **B-11** Sincronización diferida frente a invariantes | HA-04, RF5-05 | Un registro retenido puede, al sincronizarse, violar IN-08 o IN-10 | Diseño del cliente sin conectividad y resolución de conflictos | **Sí** (parcial: el componente de sincronización) | Ver opciones en DF5-05; el SPEC ya limita la retención a recepción y movimiento interno | **DF5-05** |
| **B-12** Ubicación inicial sin movimiento | HA-02 | La primera ubicación cambia la existencia de unidad sin dejar movimiento | Completitud del kardex; indivisibilidad | **Sí** 🔴 | Opción (a) de DF5-03: registrarla como movimiento interno (tipo existente en VO-21) desde la ubicación de recepción | **DF5-03** |
| **B-13** Estructural frente a configurable | H-06, DEC-04, R-S08 | ¿Toda regla estructural es no configurable, o solo las 10 de §9.1? | Qué expone el subsistema de configuración (AG-20, IN-67) | **Parcial** | DEC-04 opción (a) según el SRS | **DF5-07** |
| **B-14** Aprobación formal de la base | HA-07, H-15, HD-21, DEC-08 | SPEC, SRS y Dominio siguen «Emitido para revisión» | La regla de trazabilidad Monografía → … → Arquitectura exige una base aprobada | **Sí** (de gobierno) | Acta única del Director | **DF5-06** |

**Resumen.** 14 bloqueos analizados: **5 bloquean** (B-01, B-02, B-11, B-12, B-14), **4 son parciales** (B-03, B-08, B-13 y, por su dependencia de B-12, parte de B-06), **5 no bloquean** (B-04, B-05, B-07, B-09, B-10). B-04 y B-05 no requieren decisión: son requisitos del negocio ya definidos que la Fase 5 debe resolver técnicamente. Frente a la lista de `CLAUDE.md` (HD-04, HD-07, HD-17, DEC-01, DEC-04, DEC-05), esta auditoría **agrega** B-11, B-12 y B-14 y **degrada** DEC-01 y DEC-05 a no bloqueantes.

---

**ESTADO DEL CAPÍTULO — 6**

| | |
|---|---|
| **Completado** | B-01…B-10 del Prompt analizados + 4 bloqueos nuevos (B-11…B-14) |
| **Riesgos** | Empezar la arquitectura con B-01 o B-12 abiertos obligaría a rehacer la identidad y el kardex |
| **Dependencias** | Cap. 7 |

---

# CAPÍTULO 7 — DECISIONES PENDIENTES

> Cada decisión incluye opciones y una recomendación justificada. **Ninguna está tomada**: la recomendación no es baseline hasta que el Director la apruebe por escrito.

## 7.1 Decisiones que bloquean el inicio de la Fase 5

### DF5-01 — Identidad de la mercancía y alcance del QR (B-01 · HD-04 · HA-01 · HA-06)

**Pregunta.** ¿Qué identifica el QR de mercancía?

| Opción | Consecuencia | Qué cambia en el baseline |
|---|---|---|
| **(a)** El QR identifica **SKU + Lote**; la unidad sigue siendo SKU + Lote + Ubicación | Reubicar no reetiqueta; una etiqueta puede estar en varias ubicaciones; la unidad se resuelve con QR de mercancía + QR de ubicación (PN-03 y PN-05 ya escanean ambos) | Fe de erratas de la redacción «un QR por unidad de inventario» (CD-08, RF-QRC-001, RN-IDE-001). **RN-INT-005 no cambia** |
| **(b)** Se redefine la unidad como **SKU + Lote**; la ubicación pasa a ser una partición de su existencia | Se conserva «un QR por unidad» literal y «mover no cambia el QR» | **Modifica una regla estructural** (RN-INT-005, CD-07) y rehace E-08, AG-05, IN-04, IN-41, el kardex por ubicación (RF-KDX-005) y la matriz B |
| (c) El QR identifica cada bulto o rollo físico | Trazabilidad por pieza | Requiere «unidades de manejo», que el SPEC sitúa en el Horizonte 3 (HD-22). **Fuera del MVP** |

**Recomendación: (a).** Es la única opción que cumple a la vez las dos afirmaciones del Prompt («el QR no identifica la ubicación» y «mover no cambia el QR») sin modificar una regla estructural. Además coincide con PN-02 paso 2, PN-03 E-04 y PN-05. Si al escribir «Unidad de inventario» el Prompt se refería a SKU + Lote, la opción (a) es exactamente lo que enuncia.

**Sub-decisión DF5-01.1 (HA-06).** Cuando el SKU + Lote escaneado está en más de una ubicación, ¿cómo se determina la unidad de origen? Opción sugerida: se exige además el escaneo (o la selección registrada, como en PN-03 E-05) de la ubicación de origen. Es una consecuencia de (a), no funcionalidad nueva, pero debe quedar escrita.

### DF5-02 — Estado de la mercancía al confirmar la entrada (B-02 · HD-07 · HD-06)

**Pregunta.** ¿Se ratifica que la entrada confirmada queda **En recepción** y pasa a **Disponible** solo al ubicarse, y que toda zona de recepción contiene al menos una ubicación?

**Recomendación: ratificar.** Lo sostienen CD-16, CD-44, RG-11, RF-INV-002 y el propio Prompt. Se emite una fe de erratas de PN-01 paso 10 y de su «resultado esperado», que dicen «disponible».

### DF5-03 — Registro de la ubicación inicial (B-12 · HA-02) — depende de DF5-01

**Pregunta.** ¿Cómo queda en el kardex el paso de la ubicación de recepción a la de almacenamiento?

| Opción | Consecuencia |
|---|---|
| **(a)** Es un **movimiento interno** (tipo existente en VO-21), de la ubicación de recepción a la de destino | Se cumple IN-03; aplica IN-41 (la existencia total no cambia) y la indivisibilidad; RF-MOV-001 ya describe el flujo (escaneo de mercancía y de ubicación). SM-06 se corrige: la porción llega Disponible a la unidad destino |
| (b) Se crea un tipo de movimiento nuevo, «Ubicación» | Distingue la primera ubicación de la reubicación (útil para KPI-10). Es un elemento `[NUEVO]` en el catálogo de tipos |
| (c) No es un movimiento | Exige relajar IN-03 o RN-INT-005. **No recomendable** |

**Recomendación: (a).** No crea funcionalidad y cierra el hueco de trazabilidad. Si el Director quiere distinguir la primera ubicación para KPI-10, basta una marca en el movimiento interno, sin tipo nuevo.

### DF5-05 — Conflictos al sincronizar registros retenidos (B-11 · HA-04)

**Pregunta.** Si un registro retenido sin conectividad, al sincronizarse, violaría una invariante (por ejemplo IN-08), ¿qué ocurre?

| Opción | Consecuencia |
|---|---|
| **(a)** Se rechaza al sincronizar, queda constancia y se abre una **Novedad** (E-17) para que la resuelva el Jefe | Respeta IN-08 sin excepción; el hecho físico no se pierde; usa entidades existentes |
| (b) Se acepta y se marca discrepancia | **Viola IN-08** (regla estructural): no admisible sin cambiar RN-EXI-001 |

**Sub-decisión DF5-05.1.** Confirmar que la retención local se limita a lo que el SPEC traza a RN-INT-003: **recepción (PN-01) y movimiento interno (PN-05)**. Salidas, ajustes y transferencias exigirían conectividad. Esto reduce drásticamente los conflictos posibles.

**Recomendación: (a) + DF5-05.1.**

### DF5-06 — Aprobación formal de la base (B-14 · HA-07 · DEC-08 · HD-21)

**Pregunta.** ¿Se aprueban por escrito el SPEC v1.0, el SRS v1.0 y el Modelo de Dominio (en su versión 1.1, que incorporará DF5-01…DF5-03 y DF5-05)?

**Recomendación:** un acta única del Director que (1) apruebe SPEC y SRS con sus fes de erratas, (2) responda o acepte como limitación conocida cada DEC (como exige CA-32) y (3) apruebe el Dominio v1.1.

## 7.2 Decisiones necesarias antes del modelo de datos detallado (pueden tomarse al inicio de la Fase 5)

| ID | Tema | Opciones | Recomendación |
|---|---|---|---|
| **DF5-04** | Capacidad con unidades heterogéneas (B-03 · HD-17 · HA-05) | (a) Cada ubicación declara la unidad de su capacidad; solo cuenta para la ocupación la existencia en esa unidad; lo demás no se valida y se informa como limitación. (b) Una ubicación solo admite referencias en la unidad de su capacidad (restricción `[NUEVO]`). (c) La capacidad es informativa en el MVP (debilita RF-BOD-005, RF-MOV-005 y RF-ALE-004) | Depende de la operación real. **Preguntar en el levantamiento AS-IS** si la empresa mezcla unidades en una misma ubicación. Si no las mezcla, (b) formaliza la práctica sin costo; si las mezcla, (a). Ninguna inventa conversiones. HD-18 (precisión) se fija con el mismo dato |
| **DF5-07** | Semántica estructural / configurable (B-13 · DEC-04) | Opciones del SRS, Anexo C | DEC-04 opción (a) |
| **DF5-08** | Alcance de entrega (B-10 · DEC-01) | Opciones del SRS, Anexo C | DEC-01 recomendación del SRS: alcance completo, entrega H1 → H2, umbral = Núcleo; la arquitectura soporta varias bodegas desde el inicio |
| **DF5-09** | Captura del dato de KPI-05 (B-08 · DEC-06) | DEC-06 (a), (b) o (c) | Como mínimo, DEC-06 (b) para KPI-05 |

## 7.3 Decisiones que no bloquean (backlog)

| ID | Tema | Recomendación |
|---|---|---|
| **DF5-10** | Cierre de jornada (DEC-05) | DEC-05 (a) |
| — | DEC-02, DEC-03, DEC-07, DEC-09 | Según las recomendaciones del SRS, Anexo C |
| — | HD-01, HD-08, HD-13, HD-15, HD-19, HD-22 | Confirmar el tratamiento del dominio. HD-15 (escalas de severidad y prioridad) antes de diseñar alertas y tareas |
| — | DEC-06 (resto: PROP-RN y KPI 07, 10, 12, 17, 24) | Backlog |

---

**ESTADO DEL CAPÍTULO — 7**

| | |
|---|---|
| **Completado** | 5 decisiones bloqueantes · 4 previas al modelo de datos · backlog agrupado |
| **Dependencias** | DF5-03 depende de DF5-01; DF5-06 depende de todas las bloqueantes |

---

# CAPÍTULO 8 — RIESGOS

| ID | Riesgo | Origen | Sev. | Tratamiento |
|---|---|---|:--:|---|
| RF5-01 | Identidad de la mercancía sin decidir | HD-04 | 🔴 | DF5-01 |
| RF5-02 | Operaciones indivisibles sobre dos unidades | §5.3 | 🔴 | Requisito de entrada (B-04), ampliado con HA-02 |
| RF5-03 | Concurrencia sobre la disponibilidad | IN-08, IN-10, IN-11 | 🔴 | Requisito de entrada (B-05) |
| RF5-05 | Registros tardíos que violan reglas | HD-16 | 🟠 | DF5-05 |
| RF5-06 | Capacidad con unidades heterogéneas | HD-17 | 🟠 | DF5-04 |
| RF5-08 | DEC abiertas que cambian el modelo | HD-21 | 🟠 | DF5-06 |
| R-S01 | **Modelo TO-BE sin contraste con la operación real** (no hay levantamiento AS-IS ni línea base) | SRS | 🔴 | Varias decisiones (DF5-04, HD-18, DF5-08: cuántas bodegas tiene la empresa, DF5-05: cómo es la conectividad en bodega) dependen de hechos que solo el AS-IS confirma. Ver Cap. 9 |
| **RA-01** | **Tomar como baseline decisiones que solo existen en un prompt** | HA-01, HA-08 | 🟠 | Toda decisión se registra en un archivo antes de usarse |
| **RA-02** | **Arrastrar HA-02 a la arquitectura** produciría un kardex con huecos, lo que invalida KPI-09 y la verificación de integridad (RF-KDX-006) | HA-02 | 🔴 | DF5-03 antes de la Fase 5 |
| **RA-03** | **Postergar la reconstrucción histórica porque su pantalla es H2** | HA-03 | 🟠 | Requisito de entrada H1 (RNF-AUD-003) |

Se mantienen sin cambio los demás RF5 (04, 07, 09–13) y los riesgos críticos heredados del SPEC (adopción: RG-01, RG-02, RG-13, RG-14, RG-16, RG-17, RG-23; evidencia académica: RG-33…RG-36).

---

**ESTADO DEL CAPÍTULO — 8**

| | |
|---|---|
| **Completado** | 7 riesgos heredados priorizados + 3 riesgos nuevos (RA-01…RA-03) |

---

# CAPÍTULO 9 — RECOMENDACIÓN DE SIGUIENTE PASO

1. **Obtener del Director las respuestas a DF5-01, DF5-02, DF5-03 y DF5-05** (y DF5-01.1, DF5-05.1). Son cuatro preguntas concretas; esta auditoría trae opciones y recomendación para cada una.
2. **Crear un registro único de decisiones** (por ejemplo `DECISIONES.md` en la raíz) que indexe DC, DEC, HD y DF5 con su estado y su acta (HA-08). Las decisiones del Prompt de reanudación se registran ahí en cuanto se ratifiquen.
3. **Emitir el Modelo de Dominio v1.1** editando los datos (`99_HERRAMIENTAS/dominio/*_data.py`), no los `.md`: SM-06, EV-INV-001, §5.3, E-08, E-09 y AG-07 según las respuestas. Se genera primero en una carpeta temporal, se compara y se ejecuta `xref.py`. **Sin renumerar IDs.**
4. **Emitir la fe de erratas** del SPEC y el SRS como documento separado (CD-08, RF-QRC-001, RN-IDE-001, PN-01 paso 10), sin editar esos documentos.
5. **En paralelo, un contraste mínimo con la operación real (R-S01)**: cinco preguntas a la empresa de estudio que desbloquean DF5-04, DF5-05 y DF5-08. (1) ¿Se mezclan metros, rollos y unidades en una misma ubicación? (2) ¿Con qué precisión se mide la tela? (3) ¿Cuántas bodegas hay? (4) ¿Hay conectividad estable en la bodega? (5) ¿Se rotula cada rollo o bulto, o el lote?
6. **Acta de aprobación (DF5-06)** y cierre formal del CP-04 según el Cap. 10.
7. **Solo entonces**, un Prompt Maestro de Fase 5 que reciba como requisitos de entrada obligatorios: B-04 (indivisibilidad, lista §5.3 ampliada), B-05 (concurrencia), HA-03 (reconstrucción histórica H1) y la trazabilidad Monografía → SPEC → SRS → Dominio → Arquitectura.

---

# CAPÍTULO 10 — CRITERIO FORMAL PARA DECLARAR CP-04 CERRADO

El CP-04 se declara **cerrado** cuando se cumplan **todas** estas condiciones, verificables en el repositorio:

| # | Condición | Evidencia verificable |
|---|---|---|
| C-1 | DF5-01 (con DF5-01.1), DF5-02, DF5-03 y DF5-05 (con DF5-05.1) respondidas por escrito | Registro de decisiones con fecha y responsable |
| C-2 | Modelo de Dominio v1.1 regenerado desde los datos, incorporando esas respuestas | Portada v1.1; diferencias frente a v1.0 limitadas a los elementos afectados |
| C-3 | `xref.py` sin errores sobre la v1.1 | Salida del verificador |
| C-4 | Ningún ID renumerado ni reutilizado; los elementos retirados marcados «Retirado» | Comparación de IDs v1.0 frente a v1.1 |
| C-5 | Al repetir la matriz del Cap. 4 no queda ninguna fila **CONTRADICTORIO** y AC-07 deja de estar **INCOMPLETO** | Nueva ejecución de esta auditoría |
| C-6 | Fe de erratas del SPEC y del SRS emitida, sin modificar esos documentos | Documento de erratas |
| C-7 | Cada DEC-01…DEC-09 y cada HD restante resuelta **o aceptada por escrito como limitación conocida** (criterio CA-32 del SRS) | Acta del Director |
| C-8 | SPEC, SRS y Dominio v1.1 aprobados formalmente (DF5-06) | Acta del Director |
| C-9 | `CLAUDE.md` actualizado con el nuevo estado y los bloqueos restantes | Archivo |

Las decisiones de §7.2 (DF5-04, 07, 08, 09) **no** son condición de cierre del CP-04: pueden tomarse al inicio de la Fase 5, siempre antes del modelo de datos detallado.

---

# AUDITORÍA INTERNA DE ESTE DOCUMENTO

| Elemento | Total |
|---|:--:|
| Documentos leídos | 8 (monografía, auditoría, SPEC, SRS, 3 de dominio, CLAUDE.md) + herramientas |
| Cifras contrastadas | 19 (18 coinciden; 1 con dos valores conocidos: reglas 68/82) |
| Filas de la matriz CP-04 | 19 (AC-01…AC-19) |
| Hallazgos nuevos | 9 (HA-01…HA-09: 2 🔴, 3 🟠, 4 🟡) |
| Bloqueos analizados | 14 (B-01…B-14): 5 bloquean, 4 parciales, 5 no bloquean |
| Decisiones solicitadas | 10 (DF5-01…DF5-10) + 2 sub-decisiones |
| Riesgos | 10 priorizados (7 heredados + 3 nuevos) |
| Documentos previos modificados | **0** |
| Arquitectura, tecnologías, modelo de datos o código | **Ninguno** |

---

**ESTADO: CP-04 CON BLOQUEOS — DECISIONES REQUERIDAS**

Decisiones que el Director debe tomar para desbloquear la Fase 5:

1. **DF5-01** — ¿El QR de mercancía identifica SKU + Lote (recomendado) o se redefine la unidad de inventario sin la ubicación? Y **DF5-01.1**: cómo se determina la ubicación de origen cuando el lote está en varias.
2. **DF5-02** — Ratificar: entrada confirmada → En recepción → Disponible al ubicarse; toda zona de recepción tiene ubicaciones.
3. **DF5-03** — La ubicación inicial se registra como movimiento interno en el kardex (recomendado).
4. **DF5-05** — Un registro retenido que al sincronizarse viola una invariante se rechaza y abre una Novedad (recomendado). Y **DF5-05.1**: la retención local se limita a recepción y movimiento interno.
5. **DF5-06** — Aprobación escrita de SPEC, SRS y Dominio v1.1, con cada DEC resuelta o aceptada como limitación.

*Fin de 04_CP04_AUDITORIA v1.0. La monografía original y los documentos de las fases 0–4 permanecen sin modificaciones.*
