# COLBASOFT_SPEC v1.3
## Especificación Funcional de Producto

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | COLBASOFT_SPEC |
| **Versión** | 1.3 |
| **Fase** | Fase 2 — Diseño Funcional de Producto |
| **Fecha** | 5 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) · 30 de septiembre de 2026 (v1.2 y v1.3) |
| **Estado** | **Borrador v1.3** (30-sep-2026): registra las respuestas a DEC-01…DEC-09. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar (borrador en `05_V13_DECISIONES/`) y pendientes HD-28, HD-29, HD-30, H-19 y H-20 |
| **Versión anterior** | `COLBASOFT_SPEC_v1.2.md` (30-sep-2026), `COLBASOFT_SPEC_v1.1.md` (29-sep-2026) y `COLBASOFT_SPEC_v1.0.md` (5-sep-2026), conservadas sin cambios |
| **Fuente de Verdad** | `MONOGRAFÍA COLBASOFT.docx` (íntegra, sin modificación) |
| **Documento antecesor** | `AUDITORIA_FUNDACIONAL_COLBASOFT.md` (Fase 0, aprobada) |
| **Autoría del proyecto** | Juan Esteban Argüello · Brayan Alexander Osorio · Brandon José Guerrero |
| **Institución** | Escuela de Ingeniería — CIAF |
| **Asesor académico** | Edwin Andrés Cabrera Arredondo |
| **Naturaleza del documento** | Especificación funcional y de negocio |
| **Fuera de alcance de este documento** | Código · Arquitectura técnica · Base de datos · Tecnologías · Diagramas C4/UML/ERD · Endpoints |

> **Relación con el roadmap de la Fase 0.** Este documento materializa el entregable que la auditoría identificó como ausente en la monografía (vacío C.1.2: «el modelo conceptual comprometido no existe») y cubre la Ingeniería de Requisitos prevista en la Fase 4 del roadmap. Las decisiones constitucionales recibidas del Director cierran, total o parcialmente, 19 de las 24 preguntas bloqueantes del banco de la Fase F.

## Control de cambios de la versión 1.3

> La versión 1.3 registra las respuestas del Director del Proyecto a **DEC-02…DEC-09** (30 de septiembre de 2026), todas en la opción recomendada por el SRS. Las versiones 1.2, 1.1 y 1.0 se conservan sin cambios. Todo pasaje modificado o nuevo lleva la etiqueta de la decisión que lo origina.

| Decisión | Respuesta del Director | Qué cambia en el SPEC |
|---|---|---|
| **DEC-02** | (a) Se mantienen los 20 módulos, incluido el dashboard operativo (M-17); la exclusión es de **toda** IA `[DC-07]` | Nada cambia en el contenido; cierra el hallazgo H-17 del SRS |
| **DEC-03** | (a) El SRS es la numeración canónica de las reglas; fe de erratas del SPEC | Nuevo §9.17 (fe de erratas); §0.4; §13.6 asunto 11 |
| **DEC-04** | (a) Toda regla estructural es no configurable; el **Jefe puede leer** los parámetros; el **Administrador o el Jefe responden y cierran** las observaciones de auditoría | §2.7 (fila nueva «Consultar parámetros de configuración»), M-18, HU-096 (criterio 4), RF-152 |
| **DEC-05** | (a) Se crean las HU y RF del cierre operativo de jornada (PN-14) | HU-113, HU-114; RF-182, RF-183, RF-184; §12.2 elemento 39 |
| **DEC-06** | (a) Se aprueban **todas** las propuestas PROP-RN (reglas sin RF) y PROP-KPI (KPI sin dato de origen) | RF-172…RF-181; HU-111, HU-112; RF-152 (dos parámetros nuevos); §12.2 elemento 41 |
| **DEC-07** | (a) Se retira del MVP el permiso «consultar valorización»; queda como restricción preventiva (RF-116 y RF-143 se conservan) | §2.7, M-16, HU-087 (criterio 5) |
| **DEC-08** | (a) Acta de aprobación y tabla de equivalencia de fases | **Borrador** en `05_V13_DECISIONES/05_V13_DECISIONES_DEC02_DEC09.md`; el acta no está firmada |
| **DEC-09** | (a) La alerta «lote próximo a vencer inmovilización» se redefine sobre el umbral de antigüedad del lote (RN-074) | PN-11 (tipo de alerta «Lote próximo a vencer inmovilización») |

**Elementos nuevos.** **4 historias** (HU-111…HU-114) y **13 requisitos funcionales** (RF-172…RF-184). Ninguna regla nueva: las propuestas PROP-RN dan requisito a reglas que ya existían (RN-022, RN-028, RN-043, RN-047, RN-051, RN-059). **Horizontes:** todos al Horizonte 1, salvo **HU-112 y RF-175** (diferencia crítica del conteo general), que siguen a su proceso en el Horizonte 2. El Núcleo (umbral aprobatorio, `[DEC-01]`) pasa de 91 HU y 152 RF a **94 HU y 164 RF**; el Completo, de 110 HU y 171 RF a **114 HU y 184 RF**. El Horizonte 2 pasa de 19 a 20 HU y de 19 a 20 RF.

**Lo que la v1.3 no cambia.** El QR, la unidad de inventario, la capa de piezas de la v1.2, los 47 RNF, los KPI (24), las reglas (91), los procesos (14) y los módulos (20).

**Pendientes que siguen abiertos** (no se inventa ninguna respuesta): HD-28, HD-29 y HD-30 del modelo de dominio; los hallazgos H-19 y H-20 del SRS; la aprobación formal de DEC-08 (acta firmada); la verificación de campo de KPI-24 (actividad de la Fase 3 del roadmap).

## Control de cambios de la versión 1.2

> La versión 1.2 incorpora las decisiones que el Director del Proyecto tomó el **30 de septiembre de 2026** al auditar DEC-01 (`DEC-01 = A — Núcleo, con 1 bodega piloto`, más la capa de trazabilidad por pieza). La versión 1.1 se conserva sin cambios en `COLBASOFT_SPEC_v1.1.md`. Todo pasaje modificado o nuevo lleva la etiqueta de la decisión que lo origina.

| Etiqueta | Decisión del Director |
|---|---|
| `[DEC-01]` | Alcance aprobatorio = **A, Núcleo (Horizonte 1)**, con **1 bodega piloto**. Transferencias, conteo general y el resto del Horizonte 2 quedan **fuera** del umbral aprobatorio |
| `[Q-11]` | La trazabilidad por **pieza o rollo está dentro del MVP** (antes: Horizonte 3, §12.4 elemento 6) |
| `[F-1]` | **Pieza** = rollo para referencias en metros o kilogramos; paquete o bolsa para referencias en unidades |
| `[F-2]` | La **cantidad de cada rollo o pieza se registra al recibir** |
| `[F-3]` | Se permiten **cortes parciales** de rollos |
| `[F-4]` | Con varias piezas del mismo lote en una ubicación, el operario **selecciona la pieza después del escaneo**; la ubicación funciona como filtro de verificación |
| `[F-5]` | El conteo es **manual, pieza por pieza** |
| `[F-6]` | Los **contenedores y bolsas agrupadas** también entran al MVP |
| `[Q-09]` | Una reimpresión **conserva el mismo QR**; no crea una nueva identidad |
| `[Q-10]` | El escaneo de salida **verifica y cuenta** |
| Otras | Piloto de **1 bodega**; nivel académico **Ingeniería** (la v1.1 y el SRS v1.1 decían «nivel Tecnólogo» en RG-38 y R-S03) |

| # | Decisión | Qué cambia | Dónde | Texto de la v1.1 |
|---|---|---|---|---|
| 1 | **Q-11 · F-1 · F-2** | Aparece el concepto **Pieza** (CD-49): cada rollo, paquete o bolsa tiene identidad interna, tipo y cantidad propia registrada en la recepción. **El QR sigue identificando SKU + Lote** (DF5-01 no se toca) y la unidad de inventario sigue siendo SKU + Lote + Ubicación (RN-066 no se toca) | CD-49, PN-01 (pasos 4–5), HU-104, RF-163, RF-164, RN-084*, RN-085* | «El Auxiliar registra la cantidad recibida por referencia, talla, color y lote» (PN-01 paso 5) |
| 2 | **F-6** | El contenedor o bolsa agrupada se registra como una pieza de tipo «contenedor agrupado» con su cantidad de unidades; pertenece a **un solo SKU + Lote**. La mezcla de lotes en un contenedor queda como DECISIÓN PENDIENTE (HD-28) | PN-02 E-03, HU-105, RF-165 | «Se rotula el contenedor y se registra como unidad de manejo agrupada» (PN-02 E-03) |
| 3 | **F-4** | Tras escanear el QR del SKU + Lote, el operario **selecciona la pieza**; la ubicación filtra y verifica. Aplica a la primera ubicación y al movimiento interno | PN-03 (pasos 3 y 6), PN-05 (pasos 2–3), HU-106, RF-166, RN-087* | PN-03 paso 3; PN-05 pasos 2 y 3 |
| 4 | **Q-10 · F-3** | En la preparación de una salida el escaneo **verifica y cuenta**; cada pieza se cuenta una vez. El **corte parcial** de una pieza descuenta lo cortado y deja el remanente en la misma pieza | PN-10 (pasos 7–8), HU-107, HU-108, RF-167, RF-168, RN-086*, RN-088* | «El Auxiliar escanea cada unidad al tomarla» (PN-10 paso 7) |
| 5 | **F-5** | El conteo se hace **manualmente, pieza por pieza**; la cantidad contada de la unidad de inventario es la suma de sus piezas. La cantidad esperada sigue oculta (RN-040) | PN-08 (pasos 5–6), HU-109, RF-169, RN-089* | «El Auxiliar escanea la ubicación y cuenta físicamente» (PN-08 paso 5) |
| 6 | **Q-11** | Trazabilidad por pieza: kardex y consulta por pieza | HU-110, RF-170, RF-171 | — |
| 7 | **Q-09** | La reimpresión **conserva el mismo QR**: deja de emitir un identificador nuevo y de marcar el anterior como reemplazado. Los demás motivos de reemplazo de un identificador quedan como DECISIÓN PENDIENTE (HD-28) | RN-018, RF-045, HU-028 (criterios 2–4), PN-02 E-01 y E-02, M-06, RG-25 | «El identificador nuevo hereda íntegramente la trazabilidad del anterior, que queda marcado como reemplazado» (RN-018) |
| 8 | **DEC-01** | El Núcleo (Horizonte 1) es el umbral aprobatorio. Se incorpora al Horizonte 1 el elemento 40 «Trazabilidad por pieza» (§12.2). El Horizonte 2 no cambia | §12.2, §12.3, §12.4 (elemento 6), §12.6, §13.6 (asunto 10) | «Hasta que el Director defina el entregable mínimo aprobatorio» |
| 9 | **Nivel Ingeniería** | Se corrige «nivel Tecnólogo» | RG-38 | «un proyecto de nivel Tecnólogo» |
| 10 | **Estado** | Borrador de la v1.2: validación técnica pendiente; aprobación funcional y académica pendiente (DEC-02…DEC-09) | Portada, §13.7 | «Validado técnicamente» |

**Lo que la v1.2 no cambia.** El QR de mercancía (DF5-01), la unidad de inventario (RN-066), las cinco reglas DF5 de la v1.1, los horizontes del Horizonte 2 (19 HU y 19 RF), los KPI, los RNF, los módulos y los procesos (14) no cambian de número. Se agregan **7 historias** (HU-104…HU-110), **9 requisitos funcionales** (RF-163…RF-171), **6 reglas estructurales** (RN-084*…RN-089*, §9.16) y **1 concepto** (CD-49). Las historias y requisitos agregados pertenecen al **Horizonte 1**: el Núcleo pasa de 84 HU y 143 RF a **91 HU y 152 RF**; el Completo, de 103 HU y 162 RF a **110 HU y 171 RF**. Las reglas pasan de 85 a **91**. La discrepancia entre las 68 reglas declaradas y las tablas (H-01 del SRS, DEC-03) **sigue abierta**.

**Decisiones que la v1.2 deja pendientes** (marcadas `DECISIÓN PENDIENTE`; no se inventa ninguna respuesta):

| ID | Pendiente | Por qué |
|---|---|---|
| **HD-28** | Si un contenedor agrupado puede mezclar lotes o SKU (Q-08); cómo se distinguen «paquete o bolsa» (F-1) y «contenedor o bolsa agrupada» (F-6); los motivos por los que un identificador QR se reemplaza ahora que la reimpresión ya no lo reemplaza | Las decisiones del Director no los cubren |
| **HD-29** | Qué ocurre con el remanente de un corte parcial si se mueve a otra ubicación (¿se divide la pieza?); si el movimiento parcial de una pieza entre ubicaciones es posible (HU-045 criterio 2 habla de cantidad parcial) | F-3 habla de cortes; no de divisiones entre ubicaciones |
| **HD-30** | Si toda referencia se controla por piezas o solo las que tienen una pieza física distinguible | F-1 define la pieza para metros, kilogramos y unidades, sin excepciones declaradas |

## Control de cambios de la versión 1.1

> La versión 1.1 incorpora las decisiones del **cierre del Checkpoint CP-04** (29 de septiembre de 2026), registradas en `04_CP04_AUDITORIA/04_CP04_CIERRE.md`. La versión 1.0 se conserva sin cambios en `COLBASOFT_SPEC_v1.0.md`. Todo pasaje modificado lleva la etiqueta de la decisión que lo origina (`[DF5-nn]`); el resto del documento es idéntico a la v1.0.

| # | Decisión | Qué cambia | Dónde | Texto de la v1.0 |
|---|---|---|---|---|
| 1 | **DF5-01** | El QR de mercancía identifica **SKU + Lote**, no la unidad de inventario. La unidad de inventario sigue siendo SKU + Lote + Ubicación (RN-066, sin cambios) y se determina con el QR de mercancía más la ubicación | CD-07, CD-08, CD-09, PN-02 (paso 1 y resultado), PN-05 (pasos 1–2), M-06, HU-025, HU-026, HU-028, HU-029, RF-040, RF-042, RN-015, RN-017 | «un identificador QR único por unidad de inventario» (PN-02, RF-040, HU-025); «asociado a una unidad de inventario» (CD-08, CD-09); «resolverlos a su unidad de inventario» (RF-042); «Un mismo identificador secundario de código de barras no puede asociarse a dos unidades de inventario distintas» (RN-017) |
| 2 | **DF5-02** | La entrada confirmada deja la existencia **En recepción**; pasa a Disponible al ubicarse. Toda zona de recepción tiene al menos una ubicación | PN-01 (paso 10 y resultado), nueva regla RN-081* | «El sistema incrementa la existencia disponible de cada unidad de inventario» (PN-01 paso 10); «La existencia disponible refleja exactamente la mercancía físicamente presente» (PN-01, resultado) |
| 3 | **DF5-03** | La primera ubicación de la mercancía en recepción es un **movimiento interno** registrado en el kardex | PN-03 (pasos 6–7 y E-04), nueva regla RN-082* | «El sistema registra la asignación de ubicación. / El sistema actualiza la existencia por ubicación» (PN-03 pasos 6–7) |
| 4 | **DF5-05** | Un registro retenido sin conectividad se **valida de nuevo** al sincronizarse; si ya no cumple las reglas, no se aplica, se rechaza con constancia y, si describe un hecho físico, abre una novedad | PN-01 E-07, PN-05 E-06, nueva regla RN-083* | «El registro se retiene localmente y se sincroniza al restablecerse» (PN-01 E-07, PN-05 E-06) |
| 5 | **DF5-06** (revisada) | Estado del documento: validado técnicamente; la aprobación funcional y académica sigue pendiente de HD-25 y DEC-01…DEC-09 | Portada, §13.7 | «Emitido para revisión del Director» |

**Lo que la v1.1 no cambia.** No se agregan historias, requisitos funcionales, requisitos no funcionales, KPI, procesos ni módulos; no cambia ningún horizonte del backlog (§12). Las reglas pasan de 82 a **85** (las tres nuevas, estructurales, están separadas en §9.15). La discrepancia entre las 68 reglas declaradas y las 82 de las tablas **sigue abierta** (H-01 del SRS, DEC-03): esta versión no la corrige.

---

## Índice general

| Cap. | Título | Contenido |
|---|---|---|
| **0** | Marco normativo del documento | Decisiones constitucionales · Sistema de trazabilidad · Convenciones |
| **1** | Visión del Producto | Problema · Oportunidad · Público objetivo · Propuesta de valor · Objetivos · Diferenciadores |
| **2** | Perfil de Usuario | Fichas de los 5 roles oficiales · Matriz de segregación |
| **3** | Procesos de Negocio | 14 procesos logísticos modelados |
| **4** | Catálogo del Producto | 49 conceptos de dominio con definición operativa (CD-49 «Pieza» desde la v1.2) |
| **5** | Módulos Funcionales | 20 módulos del MVP |
| **6** | Historias de Usuario | 114 historias con criterios de aceptación (HU-104…HU-110 desde la v1.2; HU-111…HU-114 desde la v1.3) |
| **7** | Requisitos Funcionales | 184 requisitos (RF-001 … RF-184) |
| **8** | Requisitos No Funcionales | 47 requisitos (RNF-001 … RNF-047) |
| **9** | Reglas de Negocio | 68 reglas declaradas en la v1.0 (RN-001 … RN-068; las tablas contienen 82: H-01 del SRS, DEC-03) + 3 incorporadas en la v1.1 (§9.15) + 6 incorporadas en la v1.2 (§9.16) |
| **10** | KPIs Operativos | 24 indicadores |
| **11** | Riesgos Funcionales | 42 riesgos con mitigación |
| **12** | Backlog del MVP | Producto priorizado en 4 horizontes |
| **13** | Glosario y control de versiones | Términos · Siglas · Historial |

---

# CAPÍTULO 0 — MARCO NORMATIVO DEL DOCUMENTO

## 0.1 Decisiones constitucionales recibidas

Las siguientes decisiones fueron emitidas por el Director del Proyecto y tienen carácter **inmodificable** dentro de esta especificación. Toda la Especificación se somete a ellas.

| # | Decisión | Efecto sobre la especificación |
|---|---|---|
| **DC-01** | **Empresa de estudio sin nombre comercial.** Se habla de «empresa de estudio» o «empresa piloto». | Ningún nombre de empresa aparece en el documento. Cierra parcialmente A-03/A-04 de la Fase F. |
| **DC-02** | **Alcance MVP cerrado:** gestión de inventarios, logística de bodega, trazabilidad, kardex, entradas, salidas, ajustes, conteos, transferencias, reportes, alertas y dashboard operativo. | Define la frontera funcional del Cap. 5. Cierra S-05 y A-09. |
| **DC-03** | **Exclusiones absolutas:** ventas, compras completas, producción, contabilidad, nómina, CRM y facturación. | Ningún módulo, historia o requisito puede cruzar esta frontera. Cierra S-07 y S-08. |
| **DC-04** | **Cinco roles oficiales:** Administrador, Jefe de Bodega, Coordinador de Bodega, Auxiliar de Bodega, Auditor. No se agregan roles. | Define el Cap. 2 completo. Cierra C.2.2 de la auditoría. |
| **DC-05** | **Plataforma: web responsive + tablet.** Sin aplicación móvil nativa. | Define los RNF de compatibilidad. Cierra S-10 parcialmente. |
| **DC-06** | **Integración con Power BI existirá.** No se diseñan dashboards analíticos en esta fase. | El Cap. 5 define el módulo de integración; el Cap. 10 define KPIs sin diseñar visualizaciones. |
| **DC-07** | **Sin Inteligencia Artificial.** «Inteligente» significa **automatización basada en reglas y analítica**. | Resuelve el vacío C.1.5 y la pregunta S-03 de la Fase F. Define el Cap. 9 como el corazón de la «inteligencia» del producto. |
| **DC-08** | **QR como identificador principal.** Código de barras admitido como secundario. | Define el módulo de identificación y los procesos de captura. Cierra parcialmente S-06 (sensores). |

## 0.2 Resolución de vacíos críticos de la Fase 0

| Vacío de la auditoría | Estado en COLBASOFT_SPEC v1.0 |
|---|---|
| C.1.1 — Autorización de cambio de naturaleza | ✅ **Resuelto** — alcance aprobado por el Director |
| C.1.2 — El modelo conceptual no existe | ✅ **Resuelto por este documento** — Caps. 3, 4 y 5 lo materializan |
| C.1.4 — «Trazabilidad» sin definición operativa | ✅ **Resuelto** — Cap. 4, concepto CD-21 |
| C.1.5 — Justificación del atributo «inteligente» | ✅ **Resuelto** — DC-07; ver §1.6 |
| C.1.6 — Inexistencia de requisitos | ✅ **Resuelto** — Caps. 6, 7 y 8 |
| C.1.9 — Delimitación del sujeto de estudio | 🟡 **Parcial** — DC-01 delimita la empresa; la definición legal de PYME y el ámbito municipal siguen abiertos (A-03, A-05) |
| C.2.2 — Usuarios y roles sin definir | ✅ **Resuelto** — DC-04; Cap. 2 |
| C.2.3 — Indicadores sin operacionalizar | ✅ **Resuelto** — Cap. 10 |
| C.1.3 — Ausencia de metodología de investigación | ⬜ **No aplica a este documento** — pertenece a la línea académica |
| C.1.7 — Modelo de dominio | 🟡 **Parcial** — el Cap. 4 define el vocabulario del dominio; el modelo de datos pertenece a la Fase 5 |
| C.1.8 — Proceso AS-IS no levantado | ⬜ **Abierto** — el Cap. 3 modela el proceso **TO-BE**; el AS-IS requiere trabajo de campo (Fase 3 del roadmap) |
| C.2.4 — Ausencia de línea base | ⬜ **Abierto** — el Cap. 10 define **cómo** medir; los valores iniciales requieren la empresa piloto |

> **Advertencia de método.** Los procesos del Cap. 3 describen el estado **objetivo (TO-BE)** del producto, no el proceso actual observado en campo. La monografía nunca describió el proceso real (vacío C.1.8) y este documento no lo inventa: modela el proceso que COLBASOFT propone, marcando cada elemento con su origen. La confrontación con el proceso real es tarea de la Fase 3 del roadmap.

## 0.3 Sistema de trazabilidad

Todo elemento sustantivo de esta especificación lleva una etiqueta de origen. **Ningún elemento carece de trazabilidad.**

| Etiqueta | Significado |
|---|---|
| `[MON §n]` | Trazable a un apartado de la monografía (numeración de su Tabla de Contenido) |
| `[AUD x]` | Derivado de un hallazgo de la Auditoría Fundacional Fase 0 |
| `[DC-n]` | Impuesto por una decisión constitucional del Director |
| `[NUEVO]` | **Nuevo aporte derivado de la evolución del proyecto** — no existe en la monografía; se introduce por necesidad de ingeniería de producto |

**Apartados de la monografía referenciados:**
§1 Resumen · §2 Palabras clave · §3 Introducción · §4 Planteamiento del problema y Justificación · §5 Objetivo General · §5.5 Objetivos Específicos · §6 Desarrollo temático · §7.1 Marco conceptual · §7.2 Marco Teórico · §8.1 Conclusiones · §8.2 Recomendaciones

**Balance de trazabilidad de este documento:** de los elementos catalogados, el 41 % traza directamente a la monografía, el 12 % a la auditoría, el 9 % a decisiones constitucionales y el 38 % se declara explícitamente como **nuevo aporte derivado de la evolución del proyecto**. Esa última proporción es esperable y sana: la monografía es un estudio conceptual, no una especificación, y toda la capa operativa del producto es necesariamente nueva.

## 0.4 Convenciones de nomenclatura

| Prefijo | Elemento | Rango |
|---|---|---|
| `DC-nn` | Decisión constitucional | DC-01 … DC-08 |
| `PN-nn` | Proceso de negocio | PN-01 … PN-14 |
| `CD-nn` | Concepto de dominio | CD-01 … CD-49 |
| `M-nn` | Módulo funcional | M-01 … M-20 |
| `HU-nnn` | Historia de usuario | HU-001 … HU-114 (corregido en la v1.3, §9.17) |
| `RF-nnn` | Requisito funcional | RF-001 … RF-184 (corregido en la v1.3, §9.17) |
| `RNF-nnn` | Requisito no funcional | RNF-001 … RNF-047 |
| `RN-nnn` | Regla de negocio | RN-001 … RN-068 (v1.0) · RN-081* … RN-083* (v1.1) · RN-084* … RN-089* (v1.2) |
| `KPI-nn` | Indicador operativo | KPI-01 … KPI-24 |
| `RG-nn` | Riesgo funcional | RG-01 … RG-42 |

**Escala de prioridad** (aplicada a RF, HU y backlog):

| Nivel | Significado |
|---|---|
| **P0 — Crítico** | Sin esto el MVP no existe. El producto no opera. |
| **P1 — Alto** | Necesario para operación real en la empresa piloto. |
| **P2 — Medio** | Aporta valor operativo significativo; el sistema funciona sin ello. |
| **P3 — Bajo** | Mejora de conveniencia. Candidato a versión posterior. |

## 0.5 Consistencia terminológica

Esta especificación adopta un vocabulario único y lo respeta sin sinónimos. Las siguientes equivalencias quedan **prohibidas** dentro del documento y de los artefactos derivados:

| Término oficial | No se usará |
|---|---|
| **Ubicación** | posición, casilla, celda, slot, hueco |
| **Movimiento** | transacción, registro, apunte |
| **Ajuste** | corrección, nivelación, cuadre |
| **Conteo** | toma física, inventario físico (como verbo) |
| **Existencia** | stock, saldo, disponible (como sustantivo genérico) |
| **Documento de entrada** | remisión, ingreso, recepción (como sustantivo) |
| **Referencia** | modelo, estilo, artículo |
| **Bitácora** | log, historial de sistema |

---

# CAPÍTULO 1 — VISIÓN DEL PRODUCTO

## 1.1 Problema

### 1.1.1 Enunciado

Las PYMES del sector textil del Eje Cafetero gestionan su inventario mediante **cuadernos, hojas de cálculo sueltas y registros manuales** `[MON §3]`. Este método produce una cadena de fallas encadenadas que la monografía documenta y que COLBASOFT ataca directamente.

### 1.1.2 Cadena causal del problema

El problema no es un defecto aislado sino una secuencia. Cada eslabón alimenta el siguiente:

| Paso | Manifestación | Origen |
|---|---|---|
| 1 | El movimiento de mercancía se anota a mano, o no se anota | `[MON §3]` |
| 2 | El registro contiene errores humanos frecuentes — el 67 % de las PYMES manufactureras colombianas los reporta | `[MON §7.2]` |
| 3 | La información deja de reflejar el flujo real de mercancía | `[MON §3]` |
| 4 | Se pierde la trazabilidad: no se sabe qué hay, dónde está ni quién lo movió | `[MON §3, §4]` |
| 5 | Aparecen rupturas de stock y sobre stock simultáneos | `[MON §3]` |
| 6 | La producción se interrumpe por faltantes de insumo | `[MON §3, §6]` |
| 7 | Se generan reprocesos costosos y pérdida de materia prima | `[MON §3, §7.2]` |
| 8 | Los plazos de entrega se alargan y la satisfacción del cliente cae | `[MON §3]` |
| 9 | La empresa pierde competitividad frente a competidores digitalizados | `[MON §3, §4]` |

### 1.1.3 Magnitud documentada

| Dato | Cifra | Fuente | Estado de verificación |
|---|---|---|---|
| PYMES colombianas sin herramientas tecnológicas para inventarios | **72 %** | ANDI, 2023 `[MON §7.2]` | ✅ Respaldada en la bibliografía |
| PYMES manufactureras con errores por registro manual | **67 %** | Martínez y Gómez, 2019 `[MON §7.2]` | ✅ Respaldada · contexto Antioquia |
| PYMES del Eje Cafetero sin sistemas digitales | **60 %** | UTP, 2022 `[MON §4]` | 🔴 Fuente ausente de la bibliografía `[AUD E.1.6]` |
| Baja digitalización en ciudades intermedias | Cualitativo | DNP, 2021 `[MON §7.2]` | ✅ Respaldada |
| Problemas de control de inventario en PYMES textiles de Pereira | Cualitativo | C.C. Pereira, 2022 `[MON §7.2, §8.1]` | ✅ Respaldada · **evidencia local más directa** |

> **Nota de integridad.** Las cifras marcadas 🔴 provienen de fuentes que la Auditoría Fase 0 identificó como ausentes de la bibliografía `[AUD E.1, E.2]`. Se conservan por fidelidad a la monografía, con su estado de verificación declarado. **No deben usarse como justificación cuantitativa ante el jurado hasta ser verificadas** (Fase 2 del roadmap).

### 1.1.4 Por qué el problema persiste

La monografía es explícita en que el obstáculo no es la ausencia de tecnología, sino la resistencia a adoptarla `[MON §7.1]`:

| Barrera | Naturaleza | Origen | Implicación para COLBASOFT |
|---|---|---|---|
| Falta de capital para automatizar | Financiera | `[MON §1, §3, §6]` | El producto debe ser de bajo costo de entrada |
| Escasez de capacitación laboral | Formativa | `[MON §3, §8.2]` | La curva de aprendizaje debe ser mínima |
| Miedo a la obsolescencia laboral | Cultural | `[MON §4]` | El producto debe asistir al operario, no reemplazarlo |
| Inercia cultural / resistencia al cambio | Cultural | `[MON §4, §7.1]` | La adopción debe ser escalonada, no de golpe |
| Infraestructura tecnológica deficiente | Técnica | `[MON §3]` | No puede asumirse conectividad ni equipamiento moderno |
| Barreras regulatorias | Contextual | `[MON §3]` | Fuera del alcance del producto `[AUD A-08]` |

> **Consecuencia de diseño.** COLBASOFT no puede limitarse a ser correcto: debe ser **adoptable**. Un sistema funcionalmente impecable que el auxiliar de bodega no quiere usar reproduce exactamente el fracaso que la monografía documenta `[MON §4, §7.1]`. Esta constatación gobierna los requisitos de usabilidad del Cap. 8.

## 1.2 Oportunidad

### 1.2.1 Ventana de oportunidad

| Factor | Evidencia | Origen |
|---|---|---|
| **Mercado desatendido amplio** | El 72 % de las PYMES carece de herramienta; el mercado potencial es la norma, no el nicho | `[MON §7.2]` |
| **Beneficio documentado y cuantificado** | La automatización reduce errores en 40 % y mejora la trazabilidad en 55 % | `[MON §7.2]` |
| **Ganancia de productividad reportada** | Hasta 30 % por digitalización de inventarios | `[MON §7.2]` |
| **Ganancia de eficiencia regional** | Hasta 25 % en PYMES manufactureras de América Latina | `[MON §7.2]` |
| **Recomendación explícita de la fuente** | «Implementar desde el principio aplicativos o sistemas de registro digital que permitan estandarizar entradas, salidas y movimientos de inventario» | `[MON §8.2]` |
| **Vacío de soluciones ajustadas** | Los ERP genéricos no modelan el dominio textil (referencia–talla–color–lote) | `[NUEVO]` |

### 1.2.2 La oportunidad concreta

La monografía formula la recomendación operativa con precisión inusual `[MON §8.2]`: empezar con herramientas **sencillas y escalables**, registrar digitalmente **entradas, salidas y movimientos**, capacitar al personal y **medir el impacto** con indicadores de exactitud, tiempos de registro y frecuencia de errores.

**COLBASOFT es exactamente esa herramienta.** El producto no amplía la recomendación: la implementa. Esa correspondencia uno a uno entre la recomendación de la fuente y el alcance del MVP `[DC-02]` es la principal fortaleza de trazabilidad del proyecto.

### 1.2.3 Lo que NO es la oportunidad

| Tentación | Por qué se rechaza |
|---|---|
| Construir un ERP completo | Contradice `[DC-03]` y la restricción de bajo costo `[MON §1, §3, §6]` |
| Añadir inteligencia artificial | Contradice `[DC-07]`; sin anclaje en la monografía `[AUD C.1.5]` |
| Automatizar la producción textil | Fuera del alcance `[DC-03]` |
| Integrar facturación electrónica | Fuera del alcance `[DC-03]` |
| Vender a grandes empresas | El sujeto declarado es la PYME `[MON §5]` |

## 1.3 Público objetivo

### 1.3.1 Segmento primario

| Dimensión | Definición | Origen |
|---|---|---|
| **Tipo de empresa** | PYME | `[MON §5]` — criterio legal pendiente `[AUD A-03]` |
| **Sector** | Textil: confección y manejo de insumos textiles | `[MON §5]` — delimitación fina pendiente `[AUD A-04]` |
| **Región** | Eje Cafetero: Risaralda, Quindío; referencia a Pereira y Armenia | `[MON §4, §5]` — municipios pendientes `[AUD A-05]` |
| **Estado tecnológico actual** | Registro manual o en hojas de cálculo sueltas | `[MON §3]` |
| **Tamaño de operación estimado** | Una bodega principal, posible bodega secundaria | `[NUEVO]` |
| **Perfil digital del personal** | Baja alfabetización digital | `[MON §3, §8.2]` |
| **Capacidad de inversión** | Limitada | `[MON §1, §3, §6]` |

> **Delimitación pendiente.** Las tres definiciones marcadas siguen abiertas desde la Fase F (A-03, A-04, A-05). Esta especificación es funcionalmente completa sin ellas, pero **el dimensionamiento del mercado y la selección de la empresa piloto las requieren**.

### 1.3.2 Usuario directo del sistema

El comprador y el usuario no son la misma persona. Esta distinción determina el diseño `[NUEVO]`:

| | Quién es | Qué le importa | Rol en COLBASOFT |
|---|---|---|---|
| **Decisor de compra** | Propietario o gerente de la PYME | Costo, retorno visible, no complicarse | Administrador |
| **Responsable operativo** | Jefe de Bodega | Que el inventario cuadre y no lo culpen | Jefe de Bodega |
| **Usuario intensivo real** | Auxiliar de Bodega | Que no le quite tiempo ni lo haga quedar mal | Auxiliar de Bodega |

> **Regla de diseño derivada.** El usuario que más interactúa con el sistema es el que **menos** poder de decisión tiene sobre su compra y el que **más** puede boicotear su adopción `[MON §4 — resistencia cultural]`. El diseño de interacción se optimiza para el Auxiliar de Bodega `[NUEVO]`.

### 1.3.3 Empresa de estudio

`[DC-01]` El proyecto trabaja con una **empresa de estudio** del sector textil del Eje Cafetero, sin identificación comercial en esta especificación. Sirve para: levantar el proceso real (Fase 3), validar el modelo del Cap. 3, establecer la línea base de los KPIs del Cap. 10 y operar el piloto (Fase 7).

## 1.4 Propuesta de valor

### 1.4.1 Enunciado

> **COLBASOFT convierte el inventario de una PYME textil en información confiable, rastreable y consultable en el momento**, sustituyendo el cuaderno y la hoja de cálculo suelta por un registro digital único que cualquier persona de la bodega puede alimentar desde una tablet, escaneando un código QR, en segundos y sin capacitación extensa.

### 1.4.2 Descomposición del valor

| Promesa | Qué elimina | Cómo lo logra | Origen |
|---|---|---|---|
| **Registro confiable** | Errores humanos de transcripción | Captura por QR en lugar de digitación manual | `[MON §7.2]` + `[DC-08]` |
| **Trazabilidad completa** | «No sé quién movió esto ni cuándo» | Kardex inmutable: todo movimiento queda registrado con actor, fecha y motivo | `[MON §2, §6, §7.1]` |
| **Existencia real en el momento** | Información desactualizada | El movimiento actualiza la existencia al instante | `[MON §3, §6]` |
| **Ubicación conocida** | «Está en la bodega, en algún lado» | Toda existencia vive en una ubicación identificada | `[NUEVO]` |
| **Alerta anticipada** | Rupturas de stock por sorpresa | Reglas de negocio que disparan alertas antes del faltante | `[MON §3, §7.1]` + `[DC-07]` |
| **Conteo sin parar la operación** | Inventarios generales que detienen la bodega | Conteo cíclico por ubicación o referencia | `[NUEVO]` |
| **Evidencia auditable** | «Cuadremos el inventario» sin registro de quién ajustó qué | Bitácora de auditoría no editable | `[MON §8.2]` + `[NUEVO]` |
| **Medición del beneficio** | Digitalizar sin poder demostrar la mejora | KPIs de exactitud, tiempo de registro y frecuencia de errores | `[MON §8.2]` |

### 1.4.3 La promesa medible

La monografía propone tres indicadores para demostrar el beneficio `[MON §8.2]`. COLBASOFT los convierte en el compromiso central del producto:

| Indicador de la monografía | Compromiso de COLBASOFT | KPI |
|---|---|---|
| **Exactitud del inventario** | El sistema mide la diferencia entre existencia registrada y existencia contada, por ubicación y por referencia | KPI-01 |
| **Tiempos de registro** | El sistema mide cuánto tarda registrar un movimiento, de principio a fin | KPI-05 |
| **Frecuencia de errores** | El sistema mide ajustes correctivos, movimientos anulados y diferencias de conteo | KPI-08 |

> Estos tres KPIs no son métricas de conveniencia: son **la evidencia con la que el proyecto demostrará ante el jurado que la automatización produce el beneficio que la literatura afirma** `[MON §7.2, §8.2]` `[AUD V-02, V-06]`.

## 1.5 Objetivos del producto

### 1.5.1 Objetivos primarios

| # | Objetivo | Cómo se verifica | Origen |
|---|---|---|---|
| **OP-01** | Sustituir por completo el registro manual de movimientos de inventario en la bodega de la empresa piloto | Cero movimientos registrados fuera del sistema durante el piloto | `[MON §3, §8.2]` |
| **OP-02** | Garantizar trazabilidad íntegra de toda unidad de inventario, desde su entrada hasta su salida | Todo movimiento reconstruible desde el kardex, sin huecos | `[MON §2, §6, §7.1]` |
| **OP-03** | Reducir la frecuencia de errores de registro respecto de la línea base | Comparación KPI-08 antes/después | `[MON §7.2, §8.2]` |
| **OP-04** | Elevar la exactitud del inventario respecto de la línea base | Comparación KPI-01 antes/después | `[MON §8.2]` |
| **OP-05** | Reducir el tiempo de registro de un movimiento respecto de la línea base | Comparación KPI-05 antes/después | `[MON §8.2]` |
| **OP-06** | Entregar existencia consultable en el momento, sin recuento previo | Consulta disponible en cualquier instante de operación | `[MON §6, §7.2]` |
| **OP-07** | Permitir el conteo del inventario sin detener la operación de la bodega | Conteo cíclico ejecutable en horario laboral | `[NUEVO]` |
| **OP-08** | Anticipar rupturas de stock y sobre stock mediante reglas | Alertas emitidas antes de que ocurra el faltante | `[MON §3, §7.1]` `[DC-07]` |

### 1.5.2 Objetivos de adopción

| # | Objetivo | Por qué | Origen |
|---|---|---|---|
| **OP-09** | Un Auxiliar de Bodega debe operar el sistema tras una capacitación breve | La escasez de capacitación es una barrera documentada | `[MON §3, §8.2]` |
| **OP-10** | El sistema debe asistir al operario, nunca evaluarlo punitivamente | El miedo a la obsolescencia laboral es una barrera cultural documentada | `[MON §4, §6]` |
| **OP-11** | La adopción debe ser escalonada: la bodega puede empezar por un solo proceso | La fuente recomienda «iniciar con herramientas sencillas y escalables» | `[MON §8.2]` |
| **OP-12** | El costo de entrada debe ser compatible con la capacidad financiera de una PYME | La falta de capital es la barrera financiera documentada | `[MON §1, §3, §6]` |

### 1.5.3 No-objetivos declarados

`[DC-03]` COLBASOFT **no** persigue: gestionar ventas · gestionar el ciclo completo de compras · planificar o controlar producción · llevar contabilidad · liquidar nómina · administrar relaciones con clientes · emitir facturas · predecir demanda mediante modelos de aprendizaje automático `[DC-07]` · operar como aplicación móvil nativa `[DC-05]`.

## 1.6 Qué significa «inteligente» en COLBASOFT

`[DC-07]` `[AUD C.1.5]`

La auditoría señaló que el atributo «inteligente» del nombre carecía de anclaje suficiente en la monografía: la única mención de inteligencia artificial es tangencial `[MON §6]`. La decisión constitucional resuelve el punto y esta especificación lo formaliza.

**«Inteligente» en COLBASOFT significa exactamente dos cosas:**

| Componente | Definición | Dónde vive |
|---|---|---|
| **1. Automatización basada en reglas** | El sistema aplica de forma autónoma un cuerpo de reglas de negocio explícitas que impiden estados inválidos, disparan alertas y ejecutan acciones sin intervención humana | Cap. 9 — 68 reglas |
| **2. Analítica operativa** | El sistema calcula indicadores sobre su propio registro y los expone al usuario y a la herramienta analítica externa | Cap. 10 — 24 KPIs · M-16 · M-18 |

**Lo que «inteligente» NO significa aquí:** aprendizaje automático · predicción de demanda por modelos estadísticos avanzados · visión por computador · procesamiento de lenguaje natural · agentes autónomos · recomendaciones basadas en modelos entrenados.

> Esta definición es **verificable y honesta**: cada afirmación de «inteligencia» del producto se puede señalar con el dedo sobre una regla numerada del Cap. 9 o un KPI del Cap. 10. Ninguna requiere justificación que la monografía no pueda sostener.

## 1.7 Diferenciadores frente a sistemas genéricos

### 1.7.1 Contra qué compite realmente COLBASOFT

| Competidor real | Cuota estimada del problema | Por qué gana hoy |
|---|---|---|
| **El cuaderno y la hoja de cálculo suelta** | Dominante — el 72 % de PYMES `[MON §7.2]` | Costo cero, cero curva de aprendizaje, control total percibido |
| **ERP genérico** | Minoritaria | Cubre todo, pero no cabe en una PYME textil |
| **Módulo de inventario de un software contable** | Minoritaria | Ya está pagado, pero modela contabilidad, no bodega |
| **No hacer nada** | Persistente | La resistencia cultural documentada `[MON §4, §7.1]` |

> **Constatación estratégica.** El competidor a vencer no es un ERP: es el cuaderno `[MON §3]`. Un producto que sea más lento o más complicado que el cuaderno pierde, por completo que sea.

### 1.7.2 Diferenciadores

| # | Diferenciador | Frente a un sistema genérico | Origen |
|---|---|---|---|
| **D-01** | **Modela el dominio textil real** — referencia, talla, color y lote como dimensiones nativas de la unidad de inventario, no como campos libres improvisados | Un ERP genérico obliga a crear un SKU por combinación o a abusar de campos de texto | `[NUEVO]` |
| **D-02** | **Alcance deliberadamente estrecho** — solo bodega e inventario | Un ERP genérico exige configurar módulos que la PYME nunca usará | `[DC-02]` `[DC-03]` |
| **D-03** | **QR como forma primaria de interacción** — el operario escanea, no digita | Los sistemas genéricos asumen teclado y escritorio | `[DC-08]` |
| **D-04** | **Diseñado para tablet en piso de bodega** — el registro ocurre donde ocurre el movimiento, no en una oficina | Los sistemas genéricos obligan a anotar en papel y transcribir después: el error que se buscaba eliminar | `[DC-05]` `[MON §3]` |
| **D-05** | **Conteo cíclico sin detener la operación** | Los sistemas genéricos privilegian el inventario general que paraliza la bodega | `[NUEVO]` |
| **D-06** | **Kardex inmutable con motivo obligatorio** — nada se borra, todo se anula dejando rastro | Muchos sistemas permiten editar o eliminar movimientos, destruyendo la trazabilidad | `[MON §6, §8.2]` `[NUEVO]` |
| **D-07** | **Reglas de negocio explícitas y visibles**, no lógica oculta | El usuario entiende por qué el sistema le impide algo, lo que reduce la resistencia | `[DC-07]` `[MON §4]` |
| **D-08** | **Mide su propio beneficio** — trae de fábrica los indicadores que la monografía propone | Ningún sistema genérico mide si valió la pena adoptarlo | `[MON §8.2]` |
| **D-09** | **Curva de aprendizaje mínima para el rol operativo** | Los sistemas genéricos requieren formación extensa, barrera documentada | `[MON §3, §8.2]` |
| **D-10** | **Adopción escalonada por proceso** — se puede empezar solo con entradas y salidas | Los ERP exigen implantación completa | `[MON §8.2]` |
| **D-11** | **Segregación de funciones con rol Auditor de solo lectura** | Los sistemas pequeños suelen carecer de separación auditor/operador | `[DC-04]` `[NUEVO]` |
| **D-12** | **Analítica delegada a herramienta externa** — no reinventa el tablero de mando | Los ERP incluyen módulos de BI mediocres y caros | `[DC-06]` |

### 1.7.3 Matriz comparativa

| Capacidad | Cuaderno / hoja suelta | ERP genérico | Módulo de contable | **COLBASOFT** |
|---|---|---|---|---|
| Costo de entrada | Nulo | Alto | Medio | **Bajo** `[MON §1, §3, §6]` |
| Curva de aprendizaje | Nula | Alta | Media | **Mínima** `[MON §8.2]` |
| Trazabilidad de movimiento | Nula | Alta | Media | **Alta** `[MON §7.1]` |
| Modelo textil nativo | — | No | No | **Sí** `[NUEVO]` |
| Captura por QR | — | Opcional | Raro | **Nativa** `[DC-08]` |
| Uso en piso de bodega | Sí | No | No | **Sí** `[DC-05]` |
| Existencia en el momento | No | Sí | Parcial | **Sí** `[MON §6]` |
| Conteo sin parar operación | No | Parcial | No | **Sí** `[NUEVO]` |
| Bitácora de auditoría | No | Sí | Parcial | **Sí** `[NUEVO]` |
| Mide su propio impacto | No | No | No | **Sí** `[MON §8.2]` |
| Alcance ajustado a PYME textil | — | No | No | **Sí** `[DC-02]` |

---

# CAPÍTULO 2 — PERFIL DE USUARIO

`[DC-04]` COLBASOFT reconoce **cinco roles oficiales**. No se admiten roles adicionales. Toda función del sistema es ejecutable por al menos uno de ellos, y ninguna función queda sin responsable asignado.

## 2.1 Principios de diseño de roles

| # | Principio | Justificación |
|---|---|---|
| PR-01 | **Segregación de funciones.** Quien registra un movimiento no es necesariamente quien lo autoriza. | Prevención de error y fraude `[MON §6]` |
| PR-02 | **El Auditor nunca escribe.** Su acceso es de solo lectura, sin excepción. | Independencia de la revisión `[NUEVO]` |
| PR-03 | **Escalada de privilegio explícita.** Un rol superior puede hacer lo que hace el inferior, salvo donde la segregación lo prohíba. | Continuidad operativa `[NUEVO]` |
| PR-04 | **El Auxiliar no ve información sensible de negocio.** | Reduce riesgo y simplifica su interfaz `[NUEVO]` |
| PR-05 | **Toda acción queda atribuida a una persona identificada.** No existen acciones anónimas ni cuentas compartidas. | Trazabilidad `[MON §7.1]` |
| PR-06 | **El rol no castiga: registra.** El sistema no expone rankings de error por persona al operario. | Mitiga el miedo a la obsolescencia laboral `[MON §4, §6]` |

## 2.2 Ficha — Administrador

| Campo | Contenido |
|---|---|
| **Código** | ROL-01 |
| **Perfil típico** | Propietario, gerente o responsable de sistemas de la PYME |
| **Frecuencia de uso** | Baja — sesiones cortas, esporádicas |
| **Dispositivo principal** | Computador de escritorio o portátil |
| **Nivel digital esperado** | Medio |

### Responsabilidades
- Configurar el sistema y sus parámetros generales `[NUEVO]`
- Crear, modificar, activar y desactivar cuentas de usuario `[NUEVO]`
- Asignar roles y mantener la segregación de funciones `[DC-04]`
- Definir la estructura física de la bodega: zonas y ubicaciones `[NUEVO]`
- Configurar los umbrales que disparan alertas `[MON §3, §7.1]`
- Autorizar la integración con la herramienta analítica externa `[DC-06]`
- Aprobar ajustes de inventario por encima del umbral de excepción `[NUEVO]`

### Objetivos
- Que el inventario sea confiable sin que él tenga que revisarlo a diario `[MON §7.2]`
- Que la inversión en digitalización demuestre retorno medible `[MON §8.2]`
- Que la operación no dependa de una sola persona irremplazable `[NUEVO]`

### Dolor principal
> *«No sé qué tengo realmente en bodega y descubro los faltantes cuando ya detuvieron la producción.»* `[MON §3]`

Complementado por la barrera financiera: no puede permitirse una solución costosa `[MON §1, §3, §6]`.

### Acciones en COLBASOFT
Gestionar usuarios y roles · configurar la estructura de bodega · definir referencias y categorías · establecer umbrales de alerta · consultar todos los reportes · aprobar ajustes mayores · consultar el dashboard operativo · habilitar la exportación analítica · consultar la bitácora de auditoría · parametrizar reglas de negocio configurables.

### Información que necesita
Existencia total valorizada en unidades · exactitud del inventario (KPI-01) · alertas activas de nivel crítico · ajustes pendientes de aprobación · tendencia de errores de registro (KPI-08) · productividad de la bodega (KPI-11) · estado de adopción del sistema por usuario `[MON §8.2]`.

### Información que NO puede ver
Ninguna restricción de lectura dentro del alcance del MVP. **Sí tiene restricciones de escritura:** no puede editar ni eliminar un movimiento ya confirmado `[RN-012]`, ni alterar la bitácora de auditoría `[RN-061]`, ni ejecutar un conteo en calidad de contador y aprobarlo él mismo si él lo ejecutó `[RN-041]`.

---

## 2.3 Ficha — Jefe de Bodega

| Campo | Contenido |
|---|---|
| **Código** | ROL-02 |
| **Perfil típico** | Responsable máximo de la operación logística de la bodega |
| **Frecuencia de uso** | Alta — varias veces al día |
| **Dispositivo principal** | Computador y tablet, indistintamente `[DC-05]` |
| **Nivel digital esperado** | Medio |

### Responsabilidades
- Responder por la exactitud del inventario ante la gerencia `[MON §8.2]`
- Aprobar ajustes de inventario dentro de su umbral `[NUEVO]`
- Programar y cerrar conteos cíclicos y generales `[NUEVO]`
- Autorizar salidas de mercancía `[NUEVO]`
- Resolver diferencias detectadas en conteo `[NUEVO]`
- Distribuir el trabajo entre coordinadores y auxiliares `[NUEVO]`
- Atender las alertas de ruptura y sobre stock `[MON §3]`

### Objetivos
- Que el inventario cuadre sin recuentos de emergencia `[MON §3]`
- Que la producción nunca se detenga por un faltante no anticipado `[MON §3, §6]`
- Poder justificar con evidencia cualquier diferencia `[NUEVO]`
- Reducir los reprocesos de su equipo `[MON §3, §8.1]`

### Dolor principal
> *«Cuando el inventario no cuadra, la responsabilidad es mía y no tengo cómo demostrar qué pasó ni quién lo movió.»* `[MON §3, §4]`

### Acciones en COLBASOFT
Consultar existencia por referencia, lote y ubicación · aprobar y rechazar ajustes · programar conteos · cerrar conteos y resolver diferencias · autorizar salidas · crear y anular transferencias · consultar el kardex completo · gestionar alertas · generar reportes operativos · consultar el dashboard · reasignar tareas de conteo · registrar cualquier movimiento que pueda registrar un Auxiliar o Coordinador `[PR-03]`.

### Información que necesita
Existencia en el momento por referencia, talla, color, lote y ubicación · diferencias de conteo pendientes de resolución · ajustes pendientes de aprobación · alertas de ruptura y sobre stock · movimientos del día · lotes próximos a inmovilización · KPI-01, KPI-02, KPI-05, KPI-08, KPI-11.

### Información que NO puede ver
No accede a la gestión de usuarios y roles `[DC-04]` · no modifica la estructura física de la bodega (zonas y ubicaciones) · no configura parámetros globales del sistema · no aprueba ajustes por encima de su umbral, que escalan al Administrador `[RN-024]` · no altera la bitácora de auditoría `[RN-061]`.

---

## 2.4 Ficha — Coordinador de Bodega

| Campo | Contenido |
|---|---|
| **Código** | ROL-03 |
| **Perfil típico** | Mando medio; supervisa a los auxiliares en piso |
| **Frecuencia de uso** | Muy alta — permanente durante la jornada |
| **Dispositivo principal** | Tablet en piso de bodega `[DC-05]` |
| **Nivel digital esperado** | Medio-bajo |

### Responsabilidades
- Supervisar la ejecución de entradas, salidas y transferencias `[MON §8.2]`
- Verificar la mercancía recibida contra el documento de entrada `[NUEVO]`
- Asignar ubicaciones físicas a la mercancía que ingresa `[NUEVO]`
- Ejecutar y supervisar conteos cíclicos `[NUEVO]`
- Registrar ajustes menores dentro de su umbral `[NUEVO]`
- Solicitar ajustes mayores para aprobación del Jefe `[NUEVO]`
- Capacitar y apoyar a los auxiliares en el uso del sistema `[MON §8.2]`

### Objetivos
- Que el trabajo del turno quede registrado sin acumular pendientes `[NUEVO]`
- Que la mercancía siempre esté donde el sistema dice que está `[NUEVO]`
- Que su equipo no tenga que repetir trabajo `[MON §3]`

### Dolor principal
> *«Recibimos mercancía, la ubicamos y la movemos todo el día; para cuando llega la hora de anotar, ya nadie recuerda con exactitud qué pasó.»* `[MON §3]`

### Acciones en COLBASOFT
Registrar y confirmar entradas · asignar y reasignar ubicaciones · registrar salidas dentro de su umbral · crear transferencias internas · ejecutar conteos cíclicos asignados · registrar ajustes menores · solicitar ajustes mayores · consultar existencia y kardex · imprimir y reimprimir identificadores QR · consultar alertas de su zona · consultar el dashboard operativo restringido a su ámbito.

### Información que necesita
Documentos de entrada pendientes de recepción · ubicaciones con capacidad disponible · existencia por ubicación · tareas de conteo asignadas a su equipo · diferencias detectadas en su zona · alertas de su ámbito · movimientos del turno.

### Información que NO puede ver
No accede a la gestión de usuarios ni roles `[DC-04]` · no aprueba sus propios ajustes `[RN-023]` · no cierra conteos generales (solo participa) `[RN-042]` · no modifica la estructura de bodega · no configura umbrales de alerta · no accede a reportes de desempeño individual de otros usuarios `[PR-06]` · no altera la bitácora `[RN-061]`.

---

## 2.5 Ficha — Auxiliar de Bodega

| Campo | Contenido |
|---|---|
| **Código** | ROL-04 |
| **Perfil típico** | Operario de bodega; mueve la mercancía físicamente |
| **Frecuencia de uso** | Intensiva y continua durante toda la jornada |
| **Dispositivo principal** | Tablet, exclusivamente `[DC-05]` |
| **Nivel digital esperado** | **Bajo** `[MON §3, §8.2]` |

> **Este es el usuario crítico del producto.** Es quien más lo usa, quien menos formación tiene y quien puede hacer fracasar la adopción `[MON §4 — resistencia cultural]`. Todo el diseño de interacción se optimiza para él `[NUEVO]`.

### Responsabilidades
- Recibir físicamente la mercancía y registrar su entrada `[MON §8.2]`
- Ubicar la mercancía en la posición indicada `[NUEVO]`
- Ejecutar movimientos internos que le sean asignados `[NUEVO]`
- Preparar y registrar salidas autorizadas `[NUEVO]`
- Contar las existencias de las ubicaciones que se le asignen `[NUEVO]`
- Reportar novedades: mercancía dañada, faltante o no identificable `[NUEVO]`

### Objetivos
- Terminar su trabajo sin quedarse después de hora `[NUEVO]`
- No ser señalado por diferencias que no causó `[MON §4]`
- Que el sistema le diga qué hacer, sin tener que interpretarlo `[MON §8.2]`

### Dolor principal
> *«Anoto en un papel para pasarlo después al computador, y ahí es donde se pierde o se equivoca; después la culpa termina siendo mía.»* `[MON §3, §4]`

Barrera cultural adicional documentada: teme que el sistema sea un mecanismo de vigilancia o el primer paso hacia su reemplazo `[MON §4, §6]`. **El producto debe desmentir ese temor con su comportamiento**, no con un discurso `[PR-06]`.

### Acciones en COLBASOFT
Iniciar sesión con credencial propia · escanear identificadores QR `[DC-08]` · registrar entrada de mercancía contra un documento de entrada · confirmar ubicación de mercancía · ejecutar transferencias asignadas · registrar salidas previamente autorizadas · registrar el conteo de las ubicaciones asignadas · consultar existencia y ubicación de una referencia · reportar novedad de mercancía · consultar sus tareas pendientes.

### Información que necesita
Sus tareas pendientes del turno, en orden · qué mercancía se espera recibir · en qué ubicación va cada cosa · qué debe contar · dónde está una referencia que le piden · confirmación visible de que su registro quedó guardado `[NUEVO]`.

### Información que NO puede ver
No accede a la gestión de usuarios `[DC-04]` · **no ve costos ni valorización del inventario** `[PR-04]` · no aprueba ajustes de ningún monto `[RN-023]` · no crea ni modifica referencias del catálogo · no modifica ubicaciones ni la estructura de bodega · no cierra conteos `[RN-042]` · no anula movimientos ya confirmados `[RN-012]` · no consulta reportes gerenciales · no ve indicadores de desempeño individual, ni el suyo ni el de otros `[PR-06]` · no ve el dashboard operativo completo, solo su panel de tareas · no accede a la bitácora de auditoría.

---

## 2.6 Ficha — Auditor

| Campo | Contenido |
|---|---|
| **Código** | ROL-05 |
| **Perfil típico** | Revisor interno o externo; puede ser el asesor académico durante el piloto |
| **Frecuencia de uso** | Baja — por campañas de revisión |
| **Dispositivo principal** | Computador de escritorio |
| **Nivel digital esperado** | Medio-alto |

### Responsabilidades
- Verificar la integridad y consistencia del registro de inventario `[NUEVO]`
- Revisar la trazabilidad de movimientos seleccionados `[MON §7.1]`
- Examinar ajustes, sus motivos y sus aprobadores `[NUEVO]`
- Contrastar resultados de conteo contra existencia registrada `[MON §8.2]`
- Emitir observaciones sobre el proceso `[NUEVO]`
- Durante el piloto: recolectar la evidencia de impacto del proyecto `[AUD V-06]`

### Objetivos
- Poder reconstruir la historia completa de cualquier unidad de inventario `[MON §7.1]`
- Detectar patrones anómalos: ajustes recurrentes, diferencias sistemáticas `[NUEVO]`
- Confirmar que la segregación de funciones se respeta `[PR-01]`

### Dolor principal
> *«Cuando el registro es manual no hay nada que auditar: no hay quién, ni cuándo, ni por qué.»* `[MON §3]`

### Acciones en COLBASOFT
Consultar el kardex completo de cualquier unidad de inventario · consultar la bitácora de auditoría íntegra · consultar todo movimiento, ajuste, conteo y transferencia · filtrar por usuario, fecha, tipo y motivo · consultar existencia histórica a una fecha dada · generar y exportar reportes de auditoría · consultar todos los KPIs · registrar observaciones de auditoría `[NUEVO]`.

### Información que necesita
Kardex íntegro sin filtros · bitácora de auditoría completa · todos los ajustes con motivo, solicitante y aprobador · historial de conteos y sus diferencias · movimientos anulados con su justificación · accesos y cambios de configuración · KPI-01, KPI-08, KPI-09, KPI-14, KPI-19.

### Información que NO puede ver
Ninguna restricción de lectura: **el Auditor lee todo** `[PR-02]`.

### Restricción absoluta de escritura
`[PR-02]` **El Auditor no escribe nada en el inventario.** No registra entradas, salidas, transferencias, ajustes ni conteos. No aprueba ni rechaza nada. No modifica catálogo, ubicaciones, usuarios ni parámetros. Su única capacidad de escritura es **registrar observaciones de auditoría**, que se almacenan en un registro separado y no alteran el estado del inventario `[RN-064]`.

---

## 2.7 Matriz de segregación de funciones

Leyenda: **✅** permitido · **⚠️** permitido con restricción o aprobación · **❌** denegado

| Función | Admin | Jefe | Coord. | Aux. | Auditor |
|---|:--:|:--:|:--:|:--:|:--:|
| Iniciar sesión | ✅ | ✅ | ✅ | ✅ | ✅ |
| Crear y desactivar usuarios | ✅ | ❌ | ❌ | ❌ | ❌ |
| Asignar roles | ✅ | ❌ | ❌ | ❌ | ❌ |
| Crear y editar referencias del catálogo | ✅ | ✅ | ❌ | ❌ | ❌ |
| Definir zonas y ubicaciones | ✅ | ❌ | ❌ | ❌ | ❌ |
| Generar identificador QR | ✅ | ✅ | ✅ | ❌ | ❌ |
| Reimprimir identificador QR | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| Crear documento de entrada | ✅ | ✅ | ✅ | ❌ | ❌ |
| Registrar recepción física | ✅ | ✅ | ✅ | ✅ | ❌ |
| Confirmar entrada al inventario | ✅ | ✅ | ✅ | ❌ | ❌ |
| Asignar ubicación | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| Autorizar salida | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Registrar salida autorizada | ✅ | ✅ | ✅ | ✅ | ❌ |
| Crear transferencia interna | ✅ | ✅ | ✅ | ❌ | ❌ |
| Ejecutar transferencia asignada | ✅ | ✅ | ✅ | ✅ | ❌ |
| Solicitar ajuste | ✅ | ✅ | ✅ | ❌ | ❌ |
| Aprobar ajuste menor | ✅ | ✅ | ❌ | ❌ | ❌ |
| Aprobar ajuste mayor | ✅ | ❌ | ❌ | ❌ | ❌ |
| Programar conteo cíclico | ✅ | ✅ | ✅ | ❌ | ❌ |
| Programar conteo general | ✅ | ✅ | ❌ | ❌ | ❌ |
| Registrar conteo físico | ✅ | ✅ | ✅ | ✅ | ❌ |
| Cerrar conteo y aplicar diferencias | ✅ | ✅ | ❌ | ❌ | ❌ |
| Anular movimiento confirmado | ⚠️ | ⚠️ | ❌ | ❌ | ❌ |
| Consultar existencia | ✅ | ✅ | ✅ | ✅ | ✅ |
| Consultar kardex | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| Consultar valorización *(función retirada del MVP, DEC-07)* | — | — | — | — | — |
| Consultar bitácora de auditoría | ✅ | ⚠️ | ❌ | ❌ | ✅ |
| Configurar umbrales de alerta | ✅ | ❌ | ❌ | ❌ | ❌ |
| Consultar parámetros de configuración, sin modificarlos `[DEC-04]` | ✅ | ✅ | ❌ | ❌ | ❌ |
| Gestionar alertas | ✅ | ✅ | ✅ | ❌ | ❌ |
| Generar reportes operativos | ✅ | ✅ | ✅ | ❌ | ✅ |
| Generar reportes gerenciales | ✅ | ✅ | ❌ | ❌ | ✅ |
| Ver dashboard operativo completo | ✅ | ✅ | ⚠️ | ❌ | ✅ |
| Ver panel de tareas propio | ✅ | ✅ | ✅ | ✅ | ❌ |
| Habilitar exportación analítica | ✅ | ❌ | ❌ | ❌ | ❌ |
| Registrar observación de auditoría | ❌ | ❌ | ❌ | ❌ | ✅ |
| Reportar novedad de mercancía | ✅ | ✅ | ✅ | ✅ | ❌ |

### Aclaración de las restricciones ⚠️

| Celda | Restricción |
|---|---|
| Reimprimir QR — Auxiliar | Solo por deterioro del identificador, dejando registro del motivo `[RN-018]` |
| Asignar ubicación — Auxiliar | Solo confirma la ubicación que el sistema le propone; no la elige libremente `[RN-020]` |
| Autorizar salida — Coordinador | Solo hasta su umbral de cantidad configurado `[RN-030]` |
| Aprobar ajuste — Admin/Jefe | Nunca puede aprobar un ajuste que él mismo solicitó `[RN-023]` |
| Anular movimiento — Admin/Jefe | El movimiento nunca se borra; se genera un movimiento inverso con motivo obligatorio `[RN-012]` |
| Consultar kardex — Auxiliar | Solo el kardex de las unidades que él movió, y de los últimos 30 días `[PR-04]` |
| Consultar bitácora — Jefe | Solo eventos de su bodega, sin acceso a eventos de configuración del sistema |
| Dashboard — Coordinador | Restringido a su zona asignada |

---

# CAPÍTULO 3 — PROCESOS DE NEGOCIO

> **Nota metodológica.** Los siguientes procesos describen el estado **objetivo (TO-BE)** que COLBASOFT propone. El proceso actual (AS-IS) de la empresa de estudio no fue levantado por la monografía `[AUD C.1.8]` y su documentación corresponde a la Fase 3 del roadmap. Cada proceso declara qué parte proviene de la monografía y qué parte es nuevo aporte.
>
> Sin diagramas: la representación gráfica pertenece a fases posteriores.

## Inventario de procesos

| # | Proceso | Actor principal | Frecuencia |
|---|---|---|---|
| **PN-01** | Recepción de mercancía | Coordinador / Auxiliar | Diaria |
| **PN-02** | Registro inicial e identificación | Coordinador | Por recepción |
| **PN-03** | Ubicación física de mercancía | Auxiliar | Por recepción |
| **PN-04** | Consulta de existencia y ubicación | Todos | Continua |
| **PN-05** | Movimiento interno (reubicación) | Auxiliar | Diaria |
| **PN-06** | Transferencia entre zonas o bodegas | Coordinador / Auxiliar | Semanal |
| **PN-07** | Ajuste de inventario | Coordinador → Jefe | Eventual |
| **PN-08** | Conteo cíclico | Coordinador / Auxiliar | Semanal |
| **PN-09** | Conteo general | Jefe de Bodega | Semestral |
| **PN-10** | Salida de mercancía | Jefe → Auxiliar | Diaria |
| **PN-11** | Gestión de alerta operativa | Jefe / Coordinador | Continua |
| **PN-12** | Reporte de novedad de mercancía | Auxiliar | Eventual |
| **PN-13** | Auditoría de inventario | Auditor | Por campaña |
| **PN-14** | Cierre operativo de jornada | Jefe / Coordinador | Diaria |

---

## PN-01 — Recepción de mercancía

| Campo | Contenido |
|---|---|
| **Objetivo** | Incorporar al inventario la mercancía que llega físicamente a la bodega, con registro exacto de qué llegó, cuánto y en qué condición `[MON §8.2]` |
| **Actor principal** | Coordinador de Bodega |
| **Actores secundarios** | Auxiliar de Bodega (recepción física) · Jefe de Bodega (excepciones) |
| **Disparador** | Llegada física de mercancía a la zona de recepción `[NUEVO]` |
| **Precondición** | Existe un documento de entrada creado o se crea al momento `[NUEVO]` |

### Flujo principal
1. El Coordinador crea el documento de entrada, indicando origen, referencia esperada, cantidad esperada y lote, o lo selecciona si ya existe `[NUEVO]`.
2. El sistema pone el documento de entrada en estado **Pendiente de recepción** `[NUEVO]`.
3. El Auxiliar abre el documento de entrada en su tablet `[DC-05]`.
4. El Auxiliar cuenta físicamente la mercancía recibida, pieza por pieza `[Q-11]`.
5. El Auxiliar registra cada pieza —rollo, paquete, bolsa o contenedor agrupado— con su **cantidad propia**; la cantidad recibida por referencia, talla, color y lote es la suma de sus piezas `[RN-084*]` `[RN-085*]` `[F-1]` `[F-2]`.
6. El sistema compara cantidad recibida contra cantidad esperada `[RN-005]`.
7. Si coinciden, el sistema marca el documento como **Recibido conforme**.
8. El Coordinador verifica y confirma la entrada `[PR-01 — quien recibe no confirma]`.
9. El sistema genera el movimiento de entrada en el kardex `[MON §7.1]`.
10. El sistema incrementa la existencia **en recepción** de cada unidad de inventario, en la ubicación de la zona de recepción; todavía no está disponible `[MON §6]` `[CD-16]` `[RN-081*]` `[DF5-02]`.
11. El proceso continúa en **PN-02**.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | Cantidad recibida menor que la esperada | El sistema registra faltante de recepción; el documento pasa a **Recibido con novedad**; se notifica al Jefe `[RN-006]` |
| E-02 | Cantidad recibida mayor que la esperada | El sistema registra sobrante; requiere autorización del Jefe antes de confirmar `[RN-007]` |
| E-03 | Referencia recibida no existe en el catálogo | El sistema bloquea el registro; el Coordinador o Jefe debe crear la referencia primero `[RN-002]` |
| E-04 | Mercancía llega dañada | Se registra la cantidad conforme y se abre novedad por la dañada (**PN-12**); la dañada no ingresa como disponible `[RN-008]` |
| E-05 | Documento de entrada duplicado | El sistema detecta origen + referencia + fecha coincidentes y advierte antes de crear `[RN-003]` |
| E-06 | Recepción interrumpida (fin de turno) | El documento queda en **Recepción parcial**; otro usuario puede continuarla, quedando ambos registrados `[NUEVO]` |
| E-07 | Sin conectividad durante la recepción | El registro se retiene localmente y se sincroniza al restablecerse, validándose de nuevo contra el estado vigente `[RN-083*]` `[DF5-05]`; el documento no se confirma hasta sincronizar `[RN-054]` `[MON §3 — infraestructura deficiente]` |

### Resultado esperado
La existencia **en recepción** refleja exactamente la mercancía físicamente recibida, y pasa a disponible al ubicarse (PN-03) `[DF5-02]`; existe un movimiento de entrada en el kardex, atribuido a personas identificadas, con fecha y documento de respaldo `[MON §7.1]` `[PR-05]`.

---

## PN-02 — Registro inicial e identificación

| Campo | Contenido |
|---|---|
| **Objetivo** | Dotar a la mercancía ingresada de un identificador QR único que permita su trazabilidad durante todo su ciclo de vida `[DC-08]` `[MON §2, §7.1]` |
| **Actor principal** | Coordinador de Bodega |
| **Disparador** | Confirmación de una entrada (PN-01) |
| **Precondición** | La unidad de inventario existe en el sistema con referencia, talla, color y lote definidos |

### Flujo principal
1. El sistema genera un identificador QR único por **SKU + Lote** (la combinación referencia + talla + color + lote), no por ubicación `[DC-08]` `[RN-015]` `[DF5-01]`.
2. El sistema asocia el identificador a la combinación referencia + talla + color + lote `[NUEVO]`.
3. El Coordinador imprime el identificador.
4. El Auxiliar adhiere físicamente el identificador a la mercancía o a su contenedor.
5. El Auxiliar escanea el identificador para confirmar su legibilidad `[NUEVO]`.
6. El sistema registra el identificador como **Activo**.
7. El proceso continúa en **PN-03**.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | La impresión sale ilegible | Se reimprime la misma etiqueta: el QR no cambia y no se crea una nueva identidad `[RN-018]` `[Q-09]` |
| E-02 | El identificador se deteriora en operación | El Auxiliar solicita reimpresión indicando motivo; se imprime otra copia del mismo QR `[RN-018]` `[Q-09]` |
| E-03 | Mercancía sin posibilidad de rotulado individual | Se rotula el contenedor con el QR del SKU + Lote y se registra como **pieza de tipo contenedor agrupado**, con su cantidad de unidades `[RN-084*]` `[F-6]`; el contenedor pertenece a un solo SKU + Lote (mezcla de lotes: DECISIÓN PENDIENTE, HD-28) |
| E-04 | Identificador duplicado detectado | El sistema rechaza la generación; ningún identificador puede repetirse `[RN-016]` |
| E-05 | La empresa recibe mercancía con código de barras del proveedor | Se admite como identificador secundario, asociado al QR primario `[DC-08]` `[RN-017]` |

### Resultado esperado
Toda unidad de inventario en bodega es identificable mediante escaneo: el QR de su SKU + Lote más el identificador de su ubicación. Ninguna existencia carece de identificador `[RN-015]` `[DF5-01]`.

---

## PN-03 — Ubicación física de mercancía

| Campo | Contenido |
|---|---|
| **Objetivo** | Registrar dónde queda físicamente cada unidad de inventario, de modo que el sistema siempre sepa dónde encontrarla `[NUEVO]` |
| **Actor principal** | Auxiliar de Bodega |
| **Actor secundario** | Coordinador (asignación) |
| **Disparador** | Mercancía identificada y lista para almacenar (PN-02) |
| **Precondición** | Existe al menos una ubicación activa con capacidad disponible |

### Flujo principal
1. El sistema propone una ubicación destino según criterios configurados: zona por categoría, ubicación con capacidad, agrupación por referencia `[NUEVO]`.
2. El Auxiliar traslada físicamente la mercancía a la ubicación propuesta.
3. El Auxiliar escanea el identificador de la mercancía `[DC-08]` y selecciona la pieza que ubica `[RN-087*]` `[F-4]`.
4. El Auxiliar escanea el identificador de la ubicación `[NUEVO]`.
5. El sistema valida que la ubicación esté activa y tenga capacidad `[RN-021]`.
6. El sistema registra la primera ubicación como **movimiento interno** en el kardex, desde la ubicación de recepción hacia la ubicación destino, con qué, cuánto, qué pieza, quién, cuándo y el documento de entrada que la origina `[RN-082*]` `[DF5-03]`.
7. La cantidad ubicada pasa de **en recepción** a **disponible** en la ubicación destino; la existencia total no cambia `[RN-026]` `[RN-082*]`.
8. El sistema confirma visualmente al Auxiliar que el registro quedó guardado `[NUEVO — requisito de confianza del operario]`.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | La ubicación propuesta está llena | El sistema propone una alternativa; el Auxiliar puede solicitar reasignación al Coordinador `[RN-021]` |
| E-02 | El Auxiliar ubica en un lugar distinto al propuesto | El sistema lo permite pero registra la desviación y notifica al Coordinador `[RN-022]` `[PR-06 — registra, no castiga]` |
| E-03 | La ubicación escaneada está inactiva | El sistema rechaza y solicita otra `[RN-021]` |
| E-04 | Mercancía que se reparte en varias ubicaciones | Se registran asignaciones parciales —un movimiento interno por cada una— hasta completar la cantidad; el QR del SKU + Lote no cambia `[NUEVO]` `[DF5-01]` `[DF5-03]` |
| E-05 | Identificador de ubicación ilegible | El Auxiliar puede seleccionarla de una lista; el sistema registra que no hubo escaneo `[NUEVO]` |

### Resultado esperado
Toda existencia disponible tiene una ubicación conocida. Consultar una referencia devuelve dónde está `[NUEVO]`.

---

## PN-04 — Consulta de existencia y ubicación

| Campo | Contenido |
|---|---|
| **Objetivo** | Responder en el momento qué hay, cuánto hay y dónde está, sin necesidad de recuento previo `[MON §6, §7.2]` |
| **Actor principal** | Todos los roles, con visibilidad diferenciada `[§2.7]` |
| **Disparador** | Necesidad operativa: preparar salida, verificar disponibilidad, localizar mercancía |
| **Precondición** | Usuario autenticado |

### Flujo principal
1. El usuario indica qué busca: por referencia, por identificador escaneado, por ubicación o por lote `[NUEVO]`.
2. El sistema devuelve la existencia correspondiente, desglosada por talla, color, lote y ubicación `[NUEVO]`.
3. El sistema muestra el desglose por estado: disponible, reservado, inmovilizado `[NUEVO]`.
4. El usuario puede abrir el kardex de la unidad seleccionada, según su rol `[§2.7]`.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | No existe la referencia buscada | El sistema informa que no existe y ofrece búsqueda aproximada `[NUEVO]` |
| E-02 | Existencia en cero | El sistema muestra cero explícitamente, con la fecha del último movimiento `[NUEVO]` |
| E-03 | Identificador escaneado no reconocido | El sistema informa y ofrece registrar una novedad (PN-12) `[NUEVO]` |
| E-04 | El usuario no tiene permiso sobre el dato solicitado | El sistema oculta el campo sin exponer su existencia `[PR-04]` |
| E-05 | Existencia registrada en una ubicación inactiva | El sistema la muestra y la marca como anomalía para el Coordinador `[NUEVO]` |

### Resultado esperado
Cualquier persona autorizada obtiene una respuesta confiable sobre el inventario en segundos, sustituyendo la consulta al cuaderno `[MON §3, §6]`.

---

## PN-05 — Movimiento interno (reubicación)

| Campo | Contenido |
|---|---|
| **Objetivo** | Registrar el traslado de mercancía de una ubicación a otra dentro de la misma bodega, manteniendo la exactitud de la existencia por ubicación `[NUEVO]` |
| **Actor principal** | Auxiliar de Bodega |
| **Disparador** | Reorganización de bodega, consolidación de existencias, liberación de ubicación |
| **Precondición** | La unidad de inventario existe y tiene ubicación actual registrada |

### Flujo principal
1. El Auxiliar escanea el identificador de la mercancía `[DC-08]`, que identifica su SKU + Lote `[DF5-01]`.
2. El sistema muestra las ubicaciones donde ese SKU + Lote tiene existencia; si hay más de una, el Auxiliar indica la de origen escaneando su identificador o seleccionándola, y la selección queda registrada `[RN-015]` `[DF5-01]`.
3. El Auxiliar selecciona la pieza que mueve; con varias piezas del mismo lote en la ubicación de origen, la ubicación filtra y verifica qué piezas se ofrecen `[RN-087*]` `[F-4]`. El movimiento parcial de una pieza entre ubicaciones es DECISIÓN PENDIENTE (HD-29) `[NUEVO]`.
4. El Auxiliar traslada físicamente la mercancía.
5. El Auxiliar escanea el identificador de la ubicación destino.
6. El sistema valida la ubicación destino `[RN-021]`.
7. El sistema registra el movimiento interno en el kardex `[MON §7.1]`.
8. El sistema descuenta de la ubicación origen y suma a la destino.
9. **La existencia total no cambia** `[RN-026]`.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | Cantidad a mover mayor que la existencia en origen | El sistema rechaza el movimiento `[RN-025]` |
| E-02 | Ubicación destino sin capacidad | El sistema rechaza y sugiere alternativa `[RN-021]` |
| E-03 | Ubicación destino igual a la origen | El sistema rechaza el movimiento por inútil `[RN-027]` |
| E-04 | Mercancía en estado inmovilizado | El sistema rechaza; solo el Jefe puede autorizar mover mercancía inmovilizada `[RN-036]` |
| E-05 | Movimiento interrumpido a mitad de camino | Queda **En tránsito**; la existencia no está en origen ni en destino hasta cerrarlo; el sistema alerta si supera el tiempo configurado `[RN-028]` |
| E-06 | Sin conectividad | Se retiene localmente y sincroniza al restablecerse `[RN-054]`; al sincronizar se valida de nuevo y, si ya no es válido, se rechaza y abre novedad `[RN-083*]` `[DF5-05]` |

### Resultado esperado
La ubicación registrada corresponde a la ubicación física real. La existencia total permanece invariante `[RN-026]`.

---

## PN-06 — Transferencia entre zonas o bodegas

| Campo | Contenido |
|---|---|
| **Objetivo** | Trasladar mercancía entre zonas distintas o entre bodegas, con control de despacho y recepción `[NUEVO]` |
| **Actor principal** | Coordinador de Bodega (crea) · Auxiliar (ejecuta) |
| **Actor secundario** | Jefe de Bodega (autoriza cuando aplica) |
| **Disparador** | Necesidad de mover existencia entre ámbitos con responsables distintos |
| **Precondición** | Existencia disponible suficiente en el origen |

### Flujo principal
1. El Coordinador crea la transferencia indicando origen, destino, referencias y cantidades `[NUEVO]`.
2. El sistema **reserva** la existencia en origen: deja de estar disponible `[RN-031]`.
3. El sistema pone la transferencia en estado **Pendiente de despacho**.
4. El Auxiliar del origen escanea la mercancía y confirma el despacho.
5. El sistema cambia el estado a **En tránsito** `[RN-032]`.
6. El Auxiliar del destino recibe físicamente y escanea la mercancía.
7. El sistema compara lo despachado contra lo recibido `[RN-033]`.
8. Si coincide, la transferencia pasa a **Completada**.
9. El sistema descuenta del origen, suma al destino y registra ambos movimientos en el kardex `[MON §7.1]`.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | Existencia insuficiente al crear | El sistema rechaza la creación `[RN-025]` |
| E-02 | Lo recibido es menor que lo despachado | Se registra diferencia de transferencia; se abre novedad; requiere resolución del Jefe `[RN-033]` |
| E-03 | Lo recibido es mayor que lo despachado | El sistema rechaza la recepción; requiere resolución del Jefe `[RN-033]` |
| E-04 | Transferencia excede el tiempo máximo en tránsito | El sistema genera alerta automática `[RN-034]` `[DC-07]` |
| E-05 | La transferencia se cancela antes del despacho | La reserva se libera y la existencia vuelve a disponible `[RN-035]` |
| E-06 | La transferencia se cancela en tránsito | Solo el Jefe puede hacerlo; genera un movimiento de retorno al origen `[RN-035]` |
| E-07 | Destino sin capacidad al momento de recibir | Se recibe en zona de recepción del destino y se resuelve con PN-03 `[NUEVO]` |

### Resultado esperado
La existencia se traslada íntegra entre ámbitos, con responsables identificados en despacho y recepción, y sin momentos en que la mercancía quede sin registro `[MON §7.1]`.

---

## PN-07 — Ajuste de inventario

| Campo | Contenido |
|---|---|
| **Objetivo** | Corregir la existencia registrada cuando difiere de la existencia física real, dejando evidencia auditable de la causa `[MON §8.2]` `[NUEVO]` |
| **Actor principal** | Coordinador de Bodega (solicita) |
| **Actor secundario** | Jefe de Bodega o Administrador (aprueba, según umbral) |
| **Disparador** | Diferencia detectada en conteo (PN-08/PN-09), novedad de mercancía (PN-12) o hallazgo operativo |
| **Precondición** | La unidad de inventario existe; hay un motivo tipificado disponible |

> **Este es el proceso más sensible del sistema.** Es el único que permite alterar la existencia sin un movimiento físico correspondiente, y por tanto el principal vector de error y de fraude `[MON §6 — detección de fraudes]`. Todas sus reglas son restrictivas por diseño.

### Flujo principal
1. El Coordinador identifica la unidad de inventario a ajustar.
2. El sistema muestra la existencia registrada actual.
3. El Coordinador ingresa la existencia física real observada `[NUEVO]`.
4. El sistema calcula la diferencia y su sentido: sobrante o faltante.
5. El Coordinador selecciona un **motivo tipificado obligatorio** `[RN-029]`.
6. El Coordinador adjunta observación y, si el motivo lo exige, evidencia `[RN-029]`.
7. El sistema determina si el ajuste es menor o mayor según el umbral configurado `[RN-024]`.
8. El sistema enruta la solicitud al aprobador que corresponda `[RN-024]`.
9. El aprobador revisa: unidad, diferencia, motivo, solicitante y evidencia.
10. El aprobador aprueba o rechaza.
11. Si aprueba, el sistema genera el movimiento de ajuste en el kardex y actualiza la existencia `[MON §7.1]`.
12. El sistema notifica al solicitante el resultado.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | El solicitante es también el aprobador designado | El sistema escala al nivel superior; **nadie aprueba su propio ajuste** `[RN-023]` |
| E-02 | El ajuste dejaría la existencia en negativo | El sistema lo rechaza sin excepción `[RN-009]` |
| E-03 | Ajuste rechazado por el aprobador | La existencia no cambia; el rechazo y su motivo quedan registrados `[RN-062]` |
| E-04 | Ajustes repetidos sobre la misma unidad en un período corto | El sistema genera alerta de patrón anómalo dirigida al Jefe y al Auditor `[RN-037]` `[DC-07]` |
| E-05 | Ajuste sobre mercancía inmovilizada | Requiere aprobación del Administrador, sin importar el monto `[RN-036]` |
| E-06 | Solicitud sin resolver más allá del plazo configurado | El sistema escala automáticamente y alerta `[RN-038]` |
| E-07 | Motivo seleccionado no corresponde a la evidencia adjunta | El aprobador rechaza; no es una validación automática del sistema `[NUEVO]` |

### Resultado esperado
La existencia registrada corresponde a la física, y existe un rastro completo de quién detectó la diferencia, por qué se produjo, quién la autorizó y cuándo `[MON §7.1, §8.2]`.

---

## PN-08 — Conteo cíclico

| Campo | Contenido |
|---|---|
| **Objetivo** | Verificar periódicamente la exactitud del inventario por partes, **sin detener la operación de la bodega** `[NUEVO]` `[MON §8.2]` |
| **Actor principal** | Coordinador de Bodega (programa y supervisa) · Auxiliar (cuenta) |
| **Actor secundario** | Jefe de Bodega (cierra) |
| **Disparador** | Programación periódica, alerta de exactitud baja, o decisión del Coordinador |
| **Precondición** | Existen ubicaciones o referencias con existencia registrada |

> **Diferenciador D-05.** El conteo cíclico permite medir la exactitud del inventario de forma continua sin paralizar la bodega, a diferencia del conteo general. Es el mecanismo mediante el cual COLBASOFT alimenta el KPI-01 propuesto por la monografía `[MON §8.2]`.

### Flujo principal
1. El Coordinador programa el conteo definiendo su ámbito: ubicaciones, referencias o categorías `[NUEVO]`.
2. El sistema genera las tareas de conteo y las asigna a auxiliares `[NUEVO]`.
3. El sistema **congela** la existencia teórica de las unidades en ámbito, tomando una foto de referencia `[RN-039]`.
4. El Auxiliar recibe sus tareas en la tablet `[DC-05]`.
5. El Auxiliar escanea la ubicación y cuenta físicamente, a mano, pieza por pieza `[DC-08]` `[F-5]`.
6. El Auxiliar registra la cantidad de cada pieza contada; la cantidad contada de la unidad de inventario es la suma de sus piezas `[RN-089*]`.
7. **El sistema no le muestra la cantidad esperada** `[RN-040]` — para evitar el sesgo de confirmación.
8. El sistema compara lo contado contra la existencia congelada.
9. El sistema clasifica cada línea: conforme, sobrante o faltante.
10. Si hay diferencias, el sistema puede exigir un **segundo conteo** por un contador distinto `[RN-041]`.
11. El Coordinador revisa las diferencias confirmadas.
12. El Jefe cierra el conteo y decide si genera ajustes (PN-07) `[RN-042]`.
13. El sistema calcula la exactitud del ámbito contado y alimenta el KPI-01 `[MON §8.2]`.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | Hay movimiento sobre una ubicación mientras se cuenta | El sistema registra el movimiento y lo señala en la conciliación; la existencia congelada no se altera `[RN-039]` |
| E-02 | Diferencia por encima del umbral de tolerancia | Segundo conteo obligatorio por contador distinto `[RN-041]` |
| E-03 | Segundo conteo también difiere | Escala al Jefe para verificación presencial `[NUEVO]` |
| E-04 | Aparece mercancía sin identificador | Se registra novedad (PN-12); no se cuenta hasta identificarla `[RN-043]` |
| E-05 | El auxiliar asignado no está disponible | El Coordinador reasigna la tarea; ambos quedan registrados `[NUEVO]` |
| E-06 | Conteo no cerrado dentro del plazo | Se genera alerta; la existencia congelada se libera si excede el máximo `[RN-044]` |
| E-07 | Ubicación vacía pero con existencia registrada | Se registra como faltante total; requiere ajuste con motivo `[RN-029]` |

### Resultado esperado
Se conoce la exactitud del inventario en el ámbito contado, la operación continuó sin interrupción, y las diferencias quedaron identificadas con responsable y motivo `[MON §8.2]`.

---

## PN-09 — Conteo general

| Campo | Contenido |
|---|---|
| **Objetivo** | Verificar la totalidad del inventario en un momento determinado, estableciendo un punto de referencia completo `[NUEVO]` |
| **Actor principal** | Jefe de Bodega |
| **Actores secundarios** | Coordinadores y Auxiliares (ejecutan) · Auditor (observa) |
| **Disparador** | Programación periódica, cierre de período, exigencia de auditoría |
| **Precondición** | Autorización del Jefe; operación de bodega suspendible |

### Flujo principal
1. El Jefe programa el conteo general definiendo fecha y hora de corte `[NUEVO]`.
2. El sistema notifica a todos los usuarios con anticipación configurable `[NUEVO]`.
3. Al llegar el corte, el sistema **bloquea el registro de movimientos** `[RN-045]`.
4. El sistema congela la existencia teórica completa `[RN-039]`.
5. El sistema genera tareas de conteo cubriendo la totalidad de ubicaciones `[NUEVO]`.
6. Los Auxiliares cuentan por ubicación, escaneando `[DC-08]`.
7. El sistema consolida los conteos y detecta ubicaciones no cubiertas `[RN-046]`.
8. El sistema compara y clasifica todas las diferencias.
9. Se ejecutan segundos conteos donde corresponda `[RN-041]`.
10. El Jefe revisa el consolidado de diferencias.
11. El Jefe cierra el conteo general y genera los ajustes derivados (PN-07).
12. El sistema **desbloquea** el registro de movimientos `[RN-045]`.
13. El sistema calcula la exactitud global y alimenta KPI-01 y KPI-02.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | Ubicaciones sin contar al cierre | El sistema impide cerrar hasta cubrirlas o justificar su exclusión `[RN-046]` |
| E-02 | Necesidad operativa urgente de mover mercancía durante el bloqueo | Solo el Jefe puede autorizar un movimiento de excepción, que queda marcado `[RN-045]` |
| E-03 | El conteo excede la ventana prevista | Se genera alerta; el Jefe decide continuar o abortar `[NUEVO]` |
| E-04 | Conteo abortado | La existencia congelada se libera; los conteos parciales se conservan como evidencia, sin generar ajustes `[NUEVO]` |
| E-05 | Diferencia global por encima del umbral crítico | El sistema notifica al Administrador y al Auditor antes de permitir el cierre `[RN-047]` |
| E-06 | Mercancía encontrada sin registro alguno | Se registra novedad y requiere ajuste por sobrante con motivo tipificado `[RN-043]` |

### Resultado esperado
Se dispone de una fotografía verificada del inventario completo, con todas las diferencias identificadas, ajustadas y trazables `[MON §7.1, §8.2]`.

---

## PN-10 — Salida de mercancía

| Campo | Contenido |
|---|---|
| **Objetivo** | Retirar mercancía del inventario dejando registro de qué salió, cuánto, con qué destino y bajo qué autorización `[MON §8.2]` |
| **Actor principal** | Jefe de Bodega (autoriza) · Auxiliar (ejecuta) |
| **Disparador** | Requerimiento de mercancía: consumo de producción, despacho, devolución a proveedor, baja |
| **Precondición** | Existencia disponible suficiente; autorización vigente |

> **Frontera de alcance.** `[DC-03]` COLBASOFT registra la **salida física del inventario**. No gestiona el pedido de venta, la factura, el documento de despacho comercial ni la orden de producción que la originan. El sistema recibe un motivo de salida tipificado y actúa sobre el inventario, nada más.

### Flujo principal
1. Se solicita la salida indicando referencias, cantidades y motivo tipificado `[RN-048]`.
2. El sistema verifica la existencia disponible `[RN-025]`.
3. El sistema **reserva** la existencia solicitada `[RN-031]`.
4. El Jefe autoriza la salida, o el Coordinador si está dentro de su umbral `[RN-030]`.
5. El sistema genera la tarea de preparación y la asigna a un Auxiliar `[NUEVO]`.
6. El sistema indica al Auxiliar las ubicaciones de donde tomar, según la política configurada `[RN-049]`.
7. El Auxiliar escanea el identificador de lo que toma `[DC-08]` y selecciona la pieza tomada; si corta parte de un rollo, registra la cantidad cortada `[RN-086*]` `[RN-087*]` `[F-3]`.
8. El sistema valida que lo escaneado corresponda a lo solicitado `[RN-050]` y cuenta cada pieza tomada una sola vez `[RN-088*]` `[Q-10]`.
9. El Auxiliar confirma la preparación completa.
10. El sistema registra el movimiento de salida en el kardex `[MON §7.1]`.
11. El sistema descuenta la existencia y libera la reserva.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | Existencia disponible insuficiente | El sistema rechaza; ofrece salida parcial con autorización `[RN-025]` |
| E-02 | El Auxiliar escanea una unidad distinta a la solicitada | El sistema rechaza el escaneo e informa la discrepancia `[RN-050]` |
| E-03 | Existencia física ausente pese a estar registrada | Se registra novedad (PN-12) y se abre ajuste (PN-07); la salida queda pendiente `[NUEVO]` |
| E-04 | Salida sobre mercancía inmovilizada | Rechazada; requiere liberación previa por el Jefe `[RN-036]` |
| E-05 | Salida autorizada no ejecutada dentro del plazo | La reserva se libera automáticamente y se alerta `[RN-051]` |
| E-06 | Salida por baja de mercancía dañada | Requiere motivo tipificado específico y aprobación del Jefe, cualquiera sea la cantidad `[RN-052]` |
| E-07 | Devolución posterior de mercancía que salió | Se registra como entrada nueva (PN-01) referenciando la salida original; **no se reversa la salida** `[RN-053]` |

### Resultado esperado
La existencia registrada refleja la salida; el kardex documenta qué salió, cuánto, por qué, quién lo autorizó y quién lo ejecutó `[MON §7.1]`.

---

## PN-11 — Gestión de alerta operativa

| Campo | Contenido |
|---|---|
| **Objetivo** | Convertir una condición anómala detectada por reglas en una acción correctiva antes de que produzca daño operativo `[MON §3, §7.1]` `[DC-07]` |
| **Actor principal** | Jefe de Bodega · Coordinador de Bodega |
| **Disparador** | Una regla de negocio del Cap. 9 evalúa verdadera su condición de disparo |
| **Precondición** | El umbral de la alerta está configurado por el Administrador |

> **Esta es la manifestación operativa de la «inteligencia» del producto** `[DC-07]`. No hay predicción ni modelo: hay reglas explícitas evaluándose de forma continua.

### Flujo principal
1. El sistema evalúa continuamente las condiciones de alerta configuradas `[DC-07]`.
2. Al cumplirse una condición, el sistema genera la alerta con su severidad `[NUEVO]`.
3. El sistema la dirige al rol responsable según su tipo `[NUEVO]`.
4. El destinatario la visualiza en su panel y, si aplica, recibe notificación `[NUEVO]`.
5. El destinatario la atiende: ejecuta la acción correctiva o la descarta con justificación.
6. El sistema registra la atención: quién, cuándo y qué se hizo `[RN-058]`.
7. Si la condición desaparece, el sistema cierra la alerta automáticamente `[RN-057]`.

### Tipos de alerta del MVP
| Tipo | Condición | Origen |
|---|---|---|
| Ruptura de stock inminente | Existencia disponible por debajo del mínimo configurado | `[MON §3, §7.1]` |
| Sobre stock | Existencia por encima del máximo configurado | `[MON §3, §7.1]` |
| Existencia en cero | Referencia activa sin existencia | `[MON §3]` |
| Lote próximo a vencer inmovilización | Lote que supera el umbral de antigüedad configurado (el lote no tiene «fecha límite») | `[RN-074]` `[DEC-09]` |
| Movimiento en tránsito prolongado | Transferencia o movimiento interno excedido en tiempo | `[RN-034]` |
| Ajustes recurrentes | Umbral de ajustes sobre la misma unidad en un período | `[RN-037]` |
| Exactitud por debajo del objetivo | KPI-01 bajo el umbral definido | `[MON §8.2]` |
| Conteo vencido | Conteo programado no ejecutado en plazo | `[RN-044]` |
| Ubicación sobreocupada | Capacidad excedida | `[RN-021]` |
| Solicitud de ajuste sin resolver | Plazo de aprobación excedido | `[RN-038]` |

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | La alerta se repite continuamente | El sistema la agrupa; no genera duplicados de una condición vigente `[RN-055]` |
| E-02 | Alerta descartada sin justificación | El sistema exige motivo antes de permitir el descarte `[RN-058]` |
| E-03 | Alerta crítica sin atender en plazo | Escala automáticamente al rol superior `[RN-056]` |
| E-04 | Umbral mal configurado genera exceso de alertas | El sistema reporta la frecuencia al Administrador para recalibrar `[NUEVO]` |
| E-05 | Alerta cuya condición cesa antes de ser atendida | Se cierra automáticamente y queda en el historial como no atendida `[RN-057]` |

### Resultado esperado
Las condiciones anómalas se atienden antes de causar interrupción de producción o pérdida `[MON §3, §6]`.

---

## PN-12 — Reporte de novedad de mercancía

| Campo | Contenido |
|---|---|
| **Objetivo** | Permitir que cualquier operario reporte una anomalía física que el sistema no puede detectar por sí solo `[NUEVO]` |
| **Actor principal** | Auxiliar de Bodega |
| **Actor secundario** | Coordinador y Jefe (resuelven) |
| **Disparador** | Hallazgo físico: mercancía dañada, sin identificador, en ubicación incorrecta o inexistente |
| **Precondición** | Usuario autenticado |

> **Función de adopción.** Este proceso existe porque el operario necesita una vía para decir «aquí hay algo raro» sin que ello lo exponga `[MON §4 — miedo a la obsolescencia laboral]` `[PR-06]`. Un sistema que solo acepta datos perfectos empuja al operario a ocultar los problemas.

### Flujo principal
1. El Auxiliar abre el reporte de novedad desde su tablet `[DC-05]`.
2. El Auxiliar selecciona el tipo de novedad de una lista tipificada `[NUEVO]`.
3. El Auxiliar escanea el identificador si existe, o indica que no lo hay `[DC-08]`.
4. El Auxiliar indica la ubicación y describe brevemente lo observado.
5. El Auxiliar puede adjuntar evidencia fotográfica `[NUEVO]`.
6. El sistema registra la novedad y la dirige al Coordinador.
7. El Coordinador la evalúa y determina la acción: ajuste, reidentificación, reubicación o baja.
8. El sistema vincula la novedad con el movimiento que la resuelva `[NUEVO]`.
9. La novedad se cierra con constancia de la resolución.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | Novedad sin resolver en plazo | Escala al Jefe automáticamente `[RN-059]` |
| E-02 | Novedad reportada sobre una unidad ya en novedad abierta | Se vincula a la existente; no se duplica `[RN-060]` |
| E-03 | Novedad que implica ajuste de existencia | Deriva a PN-07, conservando el vínculo `[NUEVO]` |
| E-04 | Novedad reportada por error | Se cierra como improcedente, con justificación; **no se elimina** `[RN-063]` |
| E-05 | Mercancía encontrada sin ningún registro | Requiere creación de unidad y ajuste por sobrante, con aprobación del Jefe `[RN-043]` |

### Resultado esperado
Las anomalías físicas llegan al sistema en lugar de resolverse informalmente, y su tratamiento queda documentado `[MON §7.1]`.

---

## PN-13 — Auditoría de inventario

| Campo | Contenido |
|---|---|
| **Objetivo** | Verificar de forma independiente la integridad del registro, la trazabilidad de los movimientos y el respeto a la segregación de funciones `[NUEVO]` `[PR-01, PR-02]` |
| **Actor principal** | Auditor |
| **Disparador** | Campaña de auditoría programada, hallazgo previo o requerimiento del Administrador |
| **Precondición** | Usuario con rol Auditor autenticado |

### Flujo principal
1. El Auditor define el alcance: período, referencias, ubicaciones, usuarios o tipos de movimiento `[NUEVO]`.
2. El Auditor consulta el kardex de las unidades en alcance `[MON §7.1]`.
3. El Auditor verifica la continuidad: toda existencia actual es explicable por la suma de movimientos `[RN-065]`.
4. El Auditor revisa los ajustes: motivo, evidencia, solicitante y aprobador `[NUEVO]`.
5. El Auditor verifica que no existan aprobaciones propias `[RN-023]`.
6. El Auditor contrasta los resultados de conteo contra la existencia registrada `[MON §8.2]`.
7. El Auditor revisa los movimientos anulados y sus justificaciones `[RN-012]`.
8. El Auditor consulta la bitácora de auditoría del período `[RN-061]`.
9. El Auditor registra observaciones, que quedan en un registro separado `[RN-064]`.
10. El Auditor exporta el reporte de auditoría `[NUEVO]`.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | Existencia no explicable por la suma de movimientos | Se registra como hallazgo crítico y se notifica al Administrador `[RN-065]` |
| E-02 | Ajuste sin motivo o sin evidencia exigida | Hallazgo; el sistema no debería haberlo permitido `[RN-029]` |
| E-03 | Aprobación propia detectada | Hallazgo crítico; indica falla de la regla `[RN-023]` |
| E-04 | Movimiento sin usuario atribuible | Hallazgo crítico; ninguna acción puede ser anónima `[PR-05]` |
| E-05 | El Auditor intenta modificar un dato | El sistema lo impide sin excepción `[PR-02]` |
| E-06 | Bitácora con discontinuidad | Hallazgo crítico de integridad `[RN-061]` |

### Resultado esperado
Existe evidencia independiente de que el registro es íntegro y trazable. Durante el piloto, este proceso produce la evidencia con la que el proyecto demostrará su impacto ante el jurado `[MON §8.2]` `[AUD V-06]`.

---

## PN-14 — Cierre operativo de jornada

| Campo | Contenido |
|---|---|
| **Objetivo** | Consolidar la actividad del día, detectar pendientes y dejar la bodega en estado consistente `[NUEVO]` |
| **Actor principal** | Jefe de Bodega · Coordinador de Bodega |
| **Disparador** | Fin de jornada laboral o de turno |
| **Precondición** | Jornada con movimientos registrados |

### Flujo principal
1. El sistema consolida los movimientos de la jornada `[NUEVO]`.
2. El sistema identifica pendientes: recepciones sin confirmar, movimientos en tránsito, tareas de conteo abiertas, ajustes sin resolver, novedades sin atender, alertas activas.
3. El Coordinador revisa el listado de pendientes.
4. El Coordinador resuelve lo que puede resolverse en el turno.
5. Lo no resuelto se traspasa explícitamente al turno siguiente `[NUEVO]`.
6. El Jefe revisa el resumen de la jornada y los indicadores del día.
7. El sistema registra el cierre con constancia de quién lo ejecutó `[PR-05]`.

### Excepciones
| # | Excepción | Tratamiento |
|---|---|---|
| E-01 | Movimientos en tránsito al cierre | Se listan explícitamente y se traspasan; generan alerta si superan el plazo `[RN-028]` |
| E-02 | Registros sin sincronizar por falta de conectividad | El sistema impide el cierre hasta sincronizar `[RN-054]` |
| E-03 | Cierre no ejecutado | El sistema lo registra como omisión y alerta al Jefe al día siguiente `[NUEVO]` |
| E-04 | Diferencia significativa detectada en el consolidado | Se genera alerta antes de permitir el cierre `[NUEVO]` |

### Resultado esperado
Cada jornada cierra con un estado conocido, sin registros pendientes ocultos, y con la responsabilidad de los pendientes explícitamente traspasada `[NUEVO]`.

---

# CAPÍTULO 4 — CATÁLOGO DEL PRODUCTO

> Vocabulario único y obligatorio del dominio. Cada concepto tiene **definición operativa**: no describe una idea, describe cómo se comporta el concepto dentro del sistema. Este catálogo resuelve el vacío C.1.7 de la auditoría en su dimensión de vocabulario; el modelo de datos pertenece a fases posteriores.

## 4.1 Conceptos de producto e identidad

### CD-01 · Prenda
**Definición operativa:** artículo textil terminado o insumo textil que la empresa almacena. Es el concepto físico del que hablan las personas; **no es la unidad que el sistema controla**. Una prenda se concreta en el sistema a través de una Referencia y, finalmente, de una Unidad de Inventario. `[MON §5, §7.1]`

### CD-02 · Referencia
**Definición operativa:** identificador comercial de un modelo o artículo, independiente de talla, color y lote. Es la unidad de catálogo. Ejemplo conceptual: un modelo de camiseta. Una referencia agrupa muchas unidades de inventario. Es creada por Administrador o Jefe de Bodega, tiene estado activo o inactivo, y **nunca se elimina** `[RN-063]`. `[NUEVO]`

### CD-03 · Talla
**Definición operativa:** dimensión de variación de una referencia que expresa el tamaño. Pertenece a un conjunto de valores definido por la empresa. Junto con color y lote, discrimina unidades de inventario dentro de una misma referencia. `[NUEVO — dominio textil, D-01]`

### CD-04 · Color
**Definición operativa:** dimensión de variación de una referencia que expresa el acabado cromático. Pertenece a un conjunto de valores definido por la empresa. `[NUEVO — dominio textil, D-01]`

### CD-05 · SKU
**Definición operativa:** combinación única e irrepetible de Referencia + Talla + Color. Es la unidad de control de catálogo con la que se planifica y se consulta. Un SKU no tiene existencia por sí mismo: su existencia es la suma de las unidades de inventario que lo componen. `[NUEVO]`

### CD-06 · Lote
**Definición operativa:** conjunto de mercancía de un mismo SKU que ingresó al inventario en un mismo evento de entrada y comparte origen y condiciones. Permite rastrear un problema hasta su procedencia. Tiene fecha de ingreso, origen y estado. `[MON §7.1 — trazabilidad]` `[NUEVO en su operacionalización]`

### CD-07 · Unidad de Inventario
**Definición operativa:** **la entidad que COLBASOFT controla**. Es la combinación de SKU + Lote + Ubicación. Es el nivel al que se registra existencia, se ejecutan movimientos y se lleva kardex. **Se identifica por el QR de su SKU + Lote más su ubicación**: el QR no incluye la ubicación, de modo que un mismo SKU + Lote puede estar en varias ubicaciones sin generar otro QR `[DF5-01]`. Todo movimiento del sistema opera sobre unidades de inventario. `[NUEVO]`

### CD-08 · Identificador QR
**Definición operativa:** código único, generado por el sistema, asociado a un **SKU + Lote** (QR de mercancía) o a una ubicación (QR de ubicación). El QR de mercancía **no identifica** ubicación, bodega ni cantidad `[DF5-01]`. Es el medio primario de interacción del operario con el sistema `[DC-08]`. Es único, irrepetible y no reutilizable. Tiene estado: activo, reemplazado o anulado. `[DC-08]`

### CD-09 · Identificador secundario
**Definición operativa:** código de barras u otro código externo, típicamente del proveedor, asociado al identificador QR de un SKU + Lote `[DF5-01]`. Es admitido para lectura pero **no reemplaza al QR** como identificador principal. `[DC-08]`

### CD-10 · Categoría
**Definición operativa:** agrupación de referencias con propósito de organización, asignación de zona y reporte. Una referencia pertenece a una sola categoría. `[NUEVO]`

### CD-11 · Unidad de medida
**Definición operativa:** magnitud en que se cuenta una referencia: unidades, metros, rollos, kilogramos. Es fija por referencia y **no puede cambiarse una vez existan movimientos** `[RN-004]`. `[NUEVO]`

## 4.2 Conceptos de espacio físico

### CD-12 · Bodega
**Definición operativa:** ámbito físico mayor donde se almacena inventario. La empresa de estudio puede tener una o varias. Es el nivel superior de la estructura física y el ámbito de responsabilidad de un Jefe de Bodega. `[NUEVO]`

### CD-13 · Zona
**Definición operativa:** subdivisión de una bodega con propósito operativo: recepción, almacenamiento, preparación de salida, cuarentena. Agrupa ubicaciones. Puede tener un Coordinador asignado. `[NUEVO]`

### CD-14 · Ubicación
**Definición operativa:** posición física identificable dentro de una zona donde reside mercancía. Es el nivel mínimo de precisión espacial del sistema. Tiene identificador QR propio, capacidad máxima y estado activo o inactivo. **Toda existencia disponible debe residir en una ubicación** `[RN-019]`. `[NUEVO]`

### CD-15 · Capacidad de ubicación
**Definición operativa:** cantidad máxima que una ubicación admite, expresada en la unidad configurada. El sistema la usa para proponer destinos y para alertar sobreocupación `[RN-021]`. `[NUEVO]`

### CD-16 · Zona de recepción
**Definición operativa:** zona de tránsito donde la mercancía permanece entre su llegada física y su ubicación definitiva. La existencia en zona de recepción **ya está en el inventario pero aún no está disponible** para salida. `[NUEVO]`

### CD-17 · Zona de cuarentena
**Definición operativa:** zona donde reside mercancía inmovilizada: dañada, en verificación o pendiente de decisión. Su existencia no es disponible. `[NUEVO]`

## 4.3 Conceptos de existencia

### CD-18 · Existencia
**Definición operativa:** cantidad de una unidad de inventario presente en el sistema en un momento dado. Es siempre el resultado de la suma algebraica de todos sus movimientos, nunca un valor ingresado directamente `[RN-065]`. Sustituye a los términos «stock» y «saldo», prohibidos por §0.5. `[MON §7.1]`

### CD-19 · Inventario Disponible
**Definición operativa:** porción de la existencia que puede comprometerse para una salida o transferencia. Es la existencia total menos lo reservado y menos lo inmovilizado. **Es la cifra que el operario ve por defecto.** `[MON §7.1]` `[NUEVO en su operacionalización]`

### CD-20 · Inventario Reservado
**Definición operativa:** porción de la existencia comprometida para una salida o transferencia autorizada aún no ejecutada. Sigue físicamente en la bodega pero no puede comprometerse de nuevo. La reserva se libera al ejecutarse el movimiento, al cancelarse la operación o al vencer su plazo `[RN-051]`. `[NUEVO]`

### CD-21 · Trazabilidad
**Definición operativa:** *(resuelve el vacío crítico C.1.4 de la auditoría)*

> **Capacidad del sistema de responder, para cualquier unidad de inventario y cualquier momento del pasado, seis preguntas: qué es, cuánto había, dónde estaba, quién la movió, cuándo la movió y por qué la movió.**

La trazabilidad de COLBASOFT es **retrospectiva y completa**: se apoya en el kardex inmutable, y su integridad se verifica porque la existencia actual siempre equivale a la suma de sus movimientos `[RN-065]`. Su alcance en el MVP es **desde la entrada a bodega hasta la salida de bodega**. No cubre la cadena de suministro aguas arriba ni la distribución aguas abajo `[DC-03]`.

*Trazable a:* `[MON §2 — palabra clave]` `[MON §6 — «la tecnología aumenta la trazabilidad, permite el seguimiento en tiempo real»]` `[MON §7.1 — «la automatización se relaciona con gestión de inventarios al mejorar la trazabilidad»]` `[MON §7.2 — Slack et al. 2010; Barreto y Ruiz 2022]` `[MON §8.1]`. La **definición operativa** es nuevo aporte, dado que la monografía usa el término sin definirlo `[AUD C.1.4]`.

### CD-22 · Inventario Inmovilizado
**Definición operativa:** porción de la existencia que existe físicamente pero no puede moverse ni salir sin autorización expresa del Jefe: mercancía dañada, en verificación, bloqueada por auditoría o en cuarentena `[RN-036]`. `[NUEVO]`

### CD-23 · Inventario en Tránsito
**Definición operativa:** existencia que salió de una ubicación origen y aún no fue confirmada en su destino. No está disponible en ninguna de las dos. Es un estado transitorio con plazo máximo `[RN-028]`. `[NUEVO]`

### CD-24 · Inventario Ajustado
**Definición operativa:** existencia cuyo valor fue modificado mediante un movimiento de ajuste (PN-07), es decir, sin movimiento físico correspondiente. Se marca como tal para efectos de auditoría, y su historial de ajustes es consultable. `[MON §8.2]` `[NUEVO]`

### CD-25 · Existencia Teórica Congelada
**Definición operativa:** fotografía de la existencia tomada al iniciar un conteo, contra la cual se compara lo contado. No se altera por los movimientos que ocurran durante el conteo `[RN-039]`. `[NUEVO]`

### CD-26 · Existencia Contada
**Definición operativa:** cantidad física registrada por un contador durante un conteo. Es un dato de entrada, no un estado del inventario: solo modifica la existencia si el conteo se cierra generando ajuste `[RN-042]`. `[NUEVO]`

### CD-27 · Diferencia de Inventario
**Definición operativa:** resultado de restar la existencia teórica congelada de la existencia contada. Positiva es sobrante, negativa es faltante. Es el insumo del KPI-01. `[MON §8.2]` `[NUEVO]`

## 4.4 Conceptos de movimiento

### CD-28 · Movimiento
**Definición operativa:** **hecho registrado que altera la existencia o la ubicación de una unidad de inventario.** Es la unidad transaccional del sistema. Todo movimiento es inmutable una vez confirmado `[RN-012]`, tiene tipo, cantidad, unidad de inventario, ubicación, usuario responsable, fecha, hora y motivo. **Nada cambia en el inventario sin un movimiento.** `[MON §8.2 — «entradas, salidas y movimientos»]`

### CD-29 · Entrada
**Definición operativa:** movimiento que incrementa la existencia por incorporación de mercancía procedente del exterior de la bodega. `[MON §8.2]`

### CD-30 · Salida
**Definición operativa:** movimiento que disminuye la existencia por retiro de mercancía hacia el exterior de la bodega. `[MON §8.2]`

### CD-31 · Movimiento Interno
**Definición operativa:** movimiento que cambia la ubicación de una unidad de inventario dentro de la misma bodega, **sin alterar la existencia total** `[RN-026]`. `[NUEVO]`

### CD-32 · Transferencia
**Definición operativa:** movimiento compuesto que traslada existencia entre zonas o bodegas con responsables distintos. Se compone de un despacho y una recepción, y atraviesa un estado en tránsito. `[NUEVO]`

### CD-33 · Ajuste
**Definición operativa:** movimiento que modifica la existencia **sin contrapartida física**, para hacer coincidir el registro con la realidad observada. Exige motivo tipificado, aprobación de un tercero y queda marcado permanentemente `[RN-023, RN-029]`. Es el movimiento de mayor riesgo del sistema. `[MON §8.2]`

### CD-34 · Anulación
**Definición operativa:** movimiento inverso que neutraliza el efecto de un movimiento previo erróneo. **No borra el movimiento original**: ambos permanecen en el kardex. Requiere motivo y autorización `[RN-012]`. `[NUEVO]`

### CD-35 · Documento de entrada
**Definición operativa:** registro que agrupa la mercancía esperada en un evento de recepción, con su origen, referencias y cantidades. Es el soporte contra el cual se verifica lo recibido. **No es una orden de compra ni un documento comercial** `[DC-03]`. `[NUEVO]`

### CD-36 · Motivo tipificado
**Definición operativa:** causa seleccionada de una lista cerrada, obligatoria en ajustes, anulaciones, salidas y descartes de alerta. El texto libre nunca sustituye al motivo tipificado `[RN-029]`. Es lo que hace la trazabilidad interpretable, no solo completa. `[NUEVO]`

### CD-37 · Kardex
**Definición operativa:** **registro cronológico, completo e inmutable de todos los movimientos de una unidad de inventario, desde su creación hasta el presente.** Cada línea contiene: fecha y hora, tipo de movimiento, cantidad, existencia resultante, ubicación, usuario responsable, motivo y documento de respaldo. El kardex es la **fuente de verdad** de la existencia: la existencia se deriva del kardex, nunca al revés `[RN-065]`. Es la materialización técnica de la trazabilidad (CD-21). `[MON §7.1, §8.2]`

## 4.5 Conceptos de verificación

### CD-38 · Conteo
**Definición operativa:** proceso de verificación de la existencia física contra la registrada, sobre un ámbito definido. Tiene estados: programado, en ejecución, en conciliación, cerrado o abortado. `[MON §8.2]`

### CD-39 · Conteo Cíclico
**Definición operativa:** conteo cuyo ámbito es parcial (ubicaciones, referencias o categorías seleccionadas), ejecutable **sin detener la operación de la bodega**. Es el mecanismo continuo de medición de exactitud. `[NUEVO — diferenciador D-05]`

### CD-40 · Conteo General
**Definición operativa:** conteo cuyo ámbito es la totalidad del inventario, que **exige bloquear el registro de movimientos** durante su ejecución `[RN-045]`. `[NUEVO]`

### CD-41 · Tarea de conteo
**Definición operativa:** unidad de trabajo asignada a un contador, correspondiente a un subconjunto del ámbito del conteo. Tiene responsable, estado y resultado. `[NUEVO]`

### CD-42 · Segundo conteo
**Definición operativa:** repetición de una tarea de conteo, **ejecutada obligatoriamente por un contador distinto al primero**, cuando la diferencia excede el umbral de tolerancia `[RN-041]`. `[NUEVO]`

### CD-43 · Exactitud del Inventario
**Definición operativa:** proporción de unidades de inventario contadas cuya existencia contada coincide con la teórica congelada, dentro del ámbito de un conteo. Es el KPI-01 y **el indicador central del compromiso de valor del producto** `[MON §8.2]`.

## 4.6 Conceptos de control y estado

### CD-44 · Estado de Inventario
**Definición operativa:** condición que determina qué puede hacerse con una porción de existencia. Los estados del MVP son mutuamente excluyentes para una misma cantidad:

| Estado | Puede salir | Puede transferirse | Puede reubicarse | Cuenta en disponible |
|---|:--:|:--:|:--:|:--:|
| **Disponible** | ✅ | ✅ | ✅ | ✅ |
| **Reservado** | Solo por su operación | ❌ | ❌ | ❌ |
| **En tránsito** | ❌ | ❌ | ❌ | ❌ |
| **Inmovilizado** | ⚠️ con autorización | ⚠️ con autorización | ⚠️ con autorización | ❌ |
| **En recepción** | ❌ | ❌ | ✅ | ❌ |

`[NUEVO]`

### CD-45 · Alerta
**Definición operativa:** notificación generada automáticamente cuando una regla de negocio evalúa verdadera su condición de disparo. Tiene tipo, severidad, destinatario por rol, estado y registro de atención. **Es la manifestación operativa de la «inteligencia» del producto** `[DC-07]`. `[MON §3, §7.1]`

### CD-46 · Umbral
**Definición operativa:** valor configurable por el Administrador que define cuándo una regla dispara: mínimo de existencia, máximo de existencia, tolerancia de diferencia, monto que separa ajuste menor de mayor, tiempo máximo en tránsito. Los umbrales son los parámetros que hacen adaptable la «inteligencia» del sistema `[DC-07]`. `[NUEVO]`

### CD-47 · Bitácora de auditoría
**Definición operativa:** registro inmutable de toda acción relevante ejecutada en el sistema, incluidas las que no alteran el inventario: accesos, cambios de configuración, cambios de rol, aprobaciones, rechazos y consultas sensibles. **No es editable por ningún rol, incluido el Administrador** `[RN-061]`. Es un registro distinto del kardex: el kardex registra el inventario, la bitácora registra el sistema. `[NUEVO]`

### CD-48 · Novedad
**Definición operativa:** reporte de una anomalía física observada por un operario que el sistema no puede detectar por sí solo. Tiene tipo, unidad de inventario asociada si existe, ubicación, descripción, evidencia opcional, estado y resolución vinculada. **Nunca se elimina: se cierra** `[RN-063]`. `[NUEVO]`

### CD-49 · Pieza
**Definición operativa:** unidad física individual de mercancía dentro de un lote, con **cantidad propia registrada en la recepción** `[F-2]` e identidad interna en el sistema. Tipos: **rollo** (referencias medidas en metros o kilogramos), **paquete o bolsa** (referencias contadas en unidades) `[F-1]` y **contenedor agrupado** (contenedor rotulado que agrupa mercancía sin rotulado individual) `[F-6]`. Pertenece a un solo SKU + Lote y se ubica en una sola ubicación. **El QR no identifica la pieza**: identifica el SKU + Lote `[DF5-01]`; el operario selecciona la pieza después del escaneo `[F-4]`. Su cantidad solo cambia por movimientos del kardex; un corte parcial la reduce y la deja con su remanente `[F-3]`. `[Q-11]` `[RN-084*]` `[RN-085*]`

## 4.7 Mapa de relaciones del vocabulario

```
Prenda (CD-01) ──se cataloga como──► Referencia (CD-02) ──pertenece a──► Categoría (CD-10)
                                            │
                       ┌────────────────────┼────────────────────┐
                       ▼                    ▼                    ▼
                  Talla (CD-03)        Color (CD-04)      Unidad de medida (CD-11)
                       └────────────────────┴──── componen ────► SKU (CD-05)
                                                                    │
                                     SKU + Lote (CD-06) + Ubicación (CD-14)
                                                                    │
                                                                    ▼
                                                    ► UNIDAD DE INVENTARIO (CD-07) ◄
                                                                    │
        ┌──────────────────┬──────────────────┬─────────────────────┼──────────────┐
        ▼                  ▼                  ▼                     ▼              ▼
 Identificador QR    Existencia (CD-18)   Estado (CD-44)     Movimiento (CD-28)  Novedad (CD-48)
     (CD-08)               │                                        │
                           │                                        ▼
              ┌────────────┼────────────┐                    KARDEX (CD-37)
              ▼            ▼            ▼                           │
        Disponible    Reservado   Inmovilizado          ┌───────────┼───────────┐
         (CD-19)      (CD-20)       (CD-22)             ▼           ▼           ▼
                                                    Entrada     Salida      Ajuste
                                                    (CD-29)     (CD-30)     (CD-33)
                                                          Mov. Interno  Transferencia
                                                            (CD-31)       (CD-32)

  Ubicación (CD-14) ──está en──► Zona (CD-13) ──está en──► Bodega (CD-12)

  Conteo (CD-38) ──produce──► Diferencia (CD-27) ──alimenta──► Exactitud (CD-43) = KPI-01
  Regla de negocio ──dispara──► Alerta (CD-45) ──según──► Umbral (CD-46)
  Toda acción ──se registra en──► Bitácora de auditoría (CD-47)
```

---

# CAPÍTULO 5 — MÓDULOS FUNCIONALES

> Veinte módulos componen el MVP. Cada uno declara su propósito, alcance, actor responsable, funciones, restricciones y dependencias funcionales. **No se describe arquitectura**: un módulo aquí es una agrupación funcional coherente, no un componente técnico.

## 5.1 Mapa de módulos

| Grupo | Módulos |
|---|---|
| **Fundacionales** | M-01 Acceso · M-02 Usuarios y Roles · M-19 Parámetros · M-20 Notificaciones |
| **Maestros** | M-03 Catálogo · M-04 Lotes · M-05 Estructura de Bodega · M-06 Identificación QR |
| **Operativos** | M-07 Entradas · M-08 Salidas · M-09 Transferencias · M-10 Ajustes · M-11 Conteos · M-12 Novedades |
| **De información** | M-13 Existencia · M-14 Kardex y Trazabilidad · M-15 Alertas · M-16 Reportes · M-17 Dashboard |
| **De control** | M-18 Auditoría y Bitácora |
| **De integración** | La exportación analítica es una capacidad de M-16, no un módulo aparte `[DC-06]` |

| # | Módulo | Grupo | Prioridad |
|---|---|---|---|
| M-01 | Acceso y Autenticación | Fundacional | P0 |
| M-02 | Usuarios y Roles | Fundacional | P0 |
| M-03 | Catálogo de Referencias | Maestro | P0 |
| M-04 | Gestión de Lotes | Maestro | P0 |
| M-05 | Estructura de Bodega | Maestro | P0 |
| M-06 | Identificación QR | Maestro | P0 |
| M-07 | Entradas y Recepción | Operativo | P0 |
| M-08 | Salidas | Operativo | P0 |
| M-09 | Movimientos y Transferencias | Operativo | P0 |
| M-10 | Ajustes de Inventario | Operativo | P0 |
| M-11 | Conteos | Operativo | P1 |
| M-12 | Novedades de Mercancía | Operativo | P1 |
| M-13 | Consulta de Existencia | Información | P0 |
| M-14 | Kardex y Trazabilidad | Información | P0 |
| M-15 | Alertas y Reglas | Información | P1 |
| M-16 | Reportes y Exportación Analítica | Información | P1 |
| M-17 | Dashboard Operativo | Información | P1 |
| M-18 | Auditoría y Bitácora | Control | P1 |
| M-19 | Parámetros y Configuración | Fundacional | P0 |
| M-20 | Notificaciones y Tareas | Fundacional | P1 |

---

## M-01 · Acceso y Autenticación

| Campo | Contenido |
|---|---|
| **Propósito** | Garantizar que toda acción en el sistema sea atribuible a una persona identificada `[PR-05]` |
| **Alcance** | Autenticación, gestión de sesión, cierre de sesión, recuperación de acceso |
| **Actor responsable** | Todos los roles (uso) · Administrador (configuración) |
| **Prioridad** | P0 |

**Funciones:** iniciar sesión con credencial individual · mantener sesión activa durante la jornada · cerrar sesión manual y por inactividad · cambiar contraseña propia · solicitar restablecimiento de acceso · bloquear cuenta tras intentos fallidos · registrar todo acceso y todo intento fallido en la bitácora.

**Restricciones:** `[PR-05]` no existen cuentas compartidas ni genéricas · no existe acceso anónimo a ninguna función · el cierre por inactividad es obligatorio en tablet `[DC-05]` · la recuperación de acceso nunca revela la contraseña anterior.

**Dependencias funcionales:** M-02 (existencia del usuario) · M-18 (registro en bitácora) · M-19 (tiempo de inactividad configurable).

**Origen:** `[PR-05]` `[NUEVO]`

---

## M-02 · Usuarios y Roles

| Campo | Contenido |
|---|---|
| **Propósito** | Administrar las personas que usan el sistema y el alcance de lo que cada una puede hacer `[DC-04]` |
| **Alcance** | Alta, modificación y desactivación de usuarios; asignación de rol; asignación de ámbito (bodega/zona) |
| **Actor responsable** | Administrador, en exclusiva |
| **Prioridad** | P0 |

**Funciones:** crear usuario con datos de identificación · asignar uno de los cinco roles oficiales · asignar ámbito de bodega y zona · desactivar y reactivar usuario · consultar el listado de usuarios y su estado · consultar el historial de cambios de rol.

**Restricciones:** `[DC-04]` solo existen cinco roles; el módulo **no permite crear roles nuevos** · un usuario tiene exactamente un rol activo · **un usuario nunca se elimina, solo se desactiva** `[RN-063]` · desactivar un usuario no borra sus movimientos históricos · el Administrador no puede desactivarse a sí mismo si es el único activo `[RN-011]` · el rol Auditor no puede recibir permisos de escritura por configuración `[PR-02]`.

**Dependencias funcionales:** M-01 · M-05 (ámbitos disponibles) · M-18.

**Origen:** `[DC-04]` `[AUD C.2.2]`

---

## M-03 · Catálogo de Referencias

| Campo | Contenido |
|---|---|
| **Propósito** | Mantener el maestro de referencias, tallas, colores y categorías que define qué puede existir en inventario |
| **Alcance** | Referencias, tallas, colores, categorías, unidades de medida, SKU |
| **Actor responsable** | Administrador · Jefe de Bodega |
| **Prioridad** | P0 |

**Funciones:** crear y editar referencia · definir el conjunto de tallas y colores aplicables · asignar categoría y unidad de medida · generar y consultar SKU · activar y desactivar referencias · definir umbrales de existencia mínima y máxima por SKU · consultar referencias sin movimiento · importar catálogo inicial en carga masiva.

**Restricciones:** una referencia **no se elimina**, se desactiva `[RN-063]` · no puede desactivarse una referencia con existencia distinta de cero `[RN-010]` · la unidad de medida no puede cambiar si existen movimientos `[RN-004]` · el código de referencia es único `[RN-002]` · un SKU se genera automáticamente y no se edita manualmente.

**Dependencias funcionales:** M-19 · M-13 (validación de existencia antes de desactivar).

**Origen:** `[NUEVO — diferenciador D-01]`

---

## M-04 · Gestión de Lotes

| Campo | Contenido |
|---|---|
| **Propósito** | Permitir rastrear un problema de calidad u origen hasta el conjunto de mercancía que lo comparte `[MON §7.1]` |
| **Alcance** | Creación, consulta, inmovilización y liberación de lotes |
| **Actor responsable** | Coordinador (crea en recepción) · Jefe (inmoviliza y libera) |
| **Prioridad** | P0 |

**Funciones:** crear lote al confirmar una entrada · asignar origen y fecha de ingreso · consultar existencia por lote y su distribución en ubicaciones · consultar el kardex completo de un lote · inmovilizar un lote completo · liberar un lote inmovilizado · consultar lotes por antigüedad.

**Restricciones:** un lote pertenece a un solo SKU · un lote no se elimina `[RN-063]` · inmovilizar un lote inmoviliza toda su existencia en todas sus ubicaciones `[RN-036]` · solo el Jefe o el Administrador liberan un lote · el código de lote es único dentro de su SKU `[RN-014]`.

**Dependencias funcionales:** M-03 · M-07 · M-14 · M-13.

**Origen:** `[MON §7.1]` + `[NUEVO en su operacionalización]`

---

## M-05 · Estructura de Bodega

| Campo | Contenido |
|---|---|
| **Propósito** | Representar el espacio físico real de la bodega para que el sistema pueda decir dónde está cada cosa |
| **Alcance** | Bodegas, zonas, ubicaciones, capacidades, tipos de zona |
| **Actor responsable** | Administrador, en exclusiva |
| **Prioridad** | P0 |

**Funciones:** crear bodega · crear zonas y asignarles tipo (almacenamiento, recepción, preparación, cuarentena) · crear ubicaciones dentro de zona · definir capacidad por ubicación · activar y desactivar ubicaciones · asignar Coordinador responsable por zona · generar identificadores QR de ubicación · consultar ocupación por zona y ubicación · configurar reglas de asignación automática de ubicación.

**Restricciones:** una ubicación no se elimina, se desactiva `[RN-063]` · no puede desactivarse una ubicación con existencia `[RN-013]` · toda zona pertenece a una bodega y toda ubicación a una zona · debe existir al menos una zona de recepción por bodega `[RN-019]` · el código de ubicación es único dentro de la bodega `[RN-014]`.

**Dependencias funcionales:** M-06 · M-13 · M-19.

**Origen:** `[NUEVO]`

---

## M-06 · Identificación QR

| Campo | Contenido |
|---|---|
| **Propósito** | Sustituir la digitación manual por escaneo, eliminando la principal fuente de error humano `[DC-08]` `[MON §7.2]` |
| **Alcance** | Generación, impresión, escaneo, reemplazo y anulación de identificadores; lectura de códigos secundarios |
| **Actor responsable** | Coordinador (genera e imprime) · Auxiliar (escanea) |
| **Prioridad** | P0 |

**Funciones:** generar identificador QR único por SKU + Lote `[DF5-01]` · generar identificador QR para ubicación · imprimir individualmente y por lote de impresión · escanear identificador desde tablet `[DC-05]` · validar y resolver el identificador escaneado · reimprimir con registro de motivo · marcar identificador como reemplazado o anulado · asociar identificador secundario de código de barras `[DC-08]` · consultar el historial de identificadores de un SKU + Lote.

**Restricciones:** `[DC-08]` el QR es el identificador primario; el código de barras es exclusivamente secundario y **no puede usarse solo para operaciones de escritura** `[RN-017]` · ningún identificador se repite jamás, ni tras la anulación `[RN-016]` · un identificador reemplazado conserva su vínculo histórico con su SKU + Lote `[RN-018]` · toda reimpresión exige motivo · el Auxiliar solo reimprime por deterioro.

**Funciones modificadas en la v1.2:** la reimpresión produce otra copia del mismo QR y **no** marca el identificador como reemplazado `[Q-09]`; los demás motivos de reemplazo de un identificador quedan como DECISIÓN PENDIENTE (HD-28).

**Dependencias funcionales:** M-05 · M-07 · M-14.

**Origen:** `[DC-08]` `[NUEVO — diferenciador D-03]`

---

## M-07 · Entradas y Recepción

| Campo | Contenido |
|---|---|
| **Propósito** | Incorporar mercancía al inventario con registro exacto de qué entró, cuánto y en qué condición `[MON §8.2]` |
| **Alcance** | Documento de entrada, recepción física, verificación, confirmación, ubicación inicial |
| **Actor responsable** | Coordinador (crea y confirma) · Auxiliar (recibe físicamente) |
| **Prioridad** | P0 |
| **Procesos que implementa** | PN-01, PN-02, PN-03 |

**Funciones:** crear documento de entrada con origen y líneas esperadas · registrar recepción física por línea · comparar recibido contra esperado · registrar faltantes y sobrantes de recepción · confirmar la entrada e incorporar al inventario · asignar ubicación inicial · registrar recepción parcial y continuarla · registrar mercancía dañada en recepción · consultar entradas por período y estado · reversar una entrada no confirmada.

**Restricciones:** `[DC-03]` el documento de entrada **no es una orden de compra**: no gestiona proveedores como entidad comercial, ni precios, ni condiciones de pago · quien recibe físicamente no confirma la entrada `[PR-01]` · un sobrante requiere autorización del Jefe `[RN-007]` · no se recibe una referencia inexistente en catálogo `[RN-002]` · una entrada confirmada no se edita: se anula con movimiento inverso `[RN-012]` · la mercancía dañada no ingresa como disponible `[RN-008]`.

**Funciones incorporadas en la v1.2:** registrar cada pieza recibida con su tipo y cantidad propia `[Q-11]` `[F-1]` `[F-2]` · registrar contenedores y bolsas agrupadas como pieza `[F-6]`. **Restricción:** la cantidad recibida de una línea es la suma de sus piezas `[RN-085*]`.

**Dependencias funcionales:** M-03 · M-04 · M-05 · M-06 · M-13 · M-14 · M-12.

**Origen:** `[MON §8.2]`

---

## M-08 · Salidas

| Campo | Contenido |
|---|---|
| **Propósito** | Retirar mercancía del inventario con autorización, motivo y evidencia de ejecución `[MON §8.2]` |
| **Alcance** | Solicitud, autorización, reserva, preparación, confirmación de salida |
| **Actor responsable** | Jefe (autoriza) · Coordinador (autoriza dentro de umbral) · Auxiliar (prepara) |
| **Prioridad** | P0 |
| **Procesos que implementa** | PN-10 |

**Funciones:** solicitar salida con motivo tipificado · verificar disponibilidad · reservar existencia · autorizar o rechazar la salida · generar tarea de preparación · indicar ubicaciones de toma según política configurada · escanear al tomar `[DC-08]` · confirmar salida y descontar existencia · registrar salida parcial autorizada · anular una salida mediante movimiento inverso · consultar salidas por período, motivo y estado.

**Restricciones:** `[DC-03]` **no gestiona pedidos de venta, facturas ni documentos comerciales de despacho**; recibe un motivo tipificado y actúa sobre el inventario · no se permite salida que deje existencia negativa `[RN-009]` · toda salida exige autorización previa · la mercancía inmovilizada no sale sin liberación `[RN-036]` · la baja por daño exige aprobación del Jefe cualquiera sea la cantidad `[RN-052]` · una devolución se registra como entrada nueva, no como reversión `[RN-053]`.

**Funciones incorporadas en la v1.2:** el escaneo de preparación verifica y cuenta piezas `[Q-10]` · registrar el corte parcial de una pieza `[F-3]`. **Restricciones:** cada pieza se cuenta una sola vez `[RN-088*]` · el corte no supera la cantidad de la pieza `[RN-086*]`.

**Dependencias funcionales:** M-13 · M-14 · M-05 · M-06 · M-19 · M-20.

**Origen:** `[MON §8.2]`

---

## M-09 · Movimientos y Transferencias

| Campo | Contenido |
|---|---|
| **Propósito** | Mantener la correspondencia entre la ubicación física real y la registrada, dentro y entre ámbitos |
| **Alcance** | Movimiento interno de reubicación; transferencia entre zonas y bodegas |
| **Actor responsable** | Coordinador (crea transferencias) · Auxiliar (ejecuta) |
| **Prioridad** | P0 |
| **Procesos que implementa** | PN-05, PN-06 |

**Funciones:** registrar movimiento interno con escaneo de origen y destino · mover cantidad total o parcial · crear transferencia entre zonas o bodegas · reservar existencia al crear la transferencia · confirmar despacho · confirmar recepción en destino · conciliar diferencias de transferencia · cancelar transferencia antes del despacho o en tránsito · consultar movimientos en tránsito · consultar historial de movimientos por ubicación.

**Restricciones:** un movimiento interno **nunca altera la existencia total** `[RN-026]` · no se mueve más de lo existente en origen `[RN-025]` · origen y destino no pueden coincidir `[RN-027]` · la existencia en tránsito no es disponible en ningún extremo `[RN-032]` · cancelar en tránsito solo lo hace el Jefe `[RN-035]` · el tiempo en tránsito tiene máximo configurable que dispara alerta `[RN-034]`.

**Funciones incorporadas en la v1.2:** seleccionar la pieza tras el escaneo, en el movimiento interno y en la primera ubicación, con la ubicación como filtro de verificación `[F-4]` `[RN-087*]`. Las **transferencias** siguen en el Horizonte 2 y quedan fuera del umbral aprobatorio `[DEC-01]`.

**Dependencias funcionales:** M-05 · M-06 · M-13 · M-14 · M-15 · M-19.

**Origen:** `[MON §8.2 — «movimientos de inventario»]`

---

## M-10 · Ajustes de Inventario

| Campo | Contenido |
|---|---|
| **Propósito** | Permitir corregir la existencia registrada cuando difiere de la real, bajo control estricto y con evidencia auditable `[MON §8.2]` |
| **Alcance** | Solicitud, aprobación, aplicación y consulta de ajustes |
| **Actor responsable** | Coordinador (solicita) · Jefe y Administrador (aprueban por umbral) |
| **Prioridad** | P0 |
| **Procesos que implementa** | PN-07 |

**Funciones:** solicitar ajuste indicando existencia real observada · seleccionar motivo tipificado obligatorio · adjuntar observación y evidencia · calcular y clasificar la diferencia · enrutar al aprobador según umbral · aprobar o rechazar con justificación · aplicar el ajuste generando movimiento · consultar ajustes por período, motivo, solicitante y aprobador · consultar ajustes pendientes · detectar y alertar patrones de ajuste recurrente.

**Restricciones:** **nadie aprueba un ajuste que él mismo solicitó** `[RN-023]` · el motivo tipificado es obligatorio y el texto libre no lo sustituye `[RN-029]` · ningún ajuste puede dejar existencia negativa `[RN-009]` · el ajuste sobre mercancía inmovilizada requiere al Administrador `[RN-036]` · un ajuste aplicado no se edita ni se borra: se corrige con otro ajuste `[RN-012]` · todo ajuste queda marcado permanentemente en la unidad afectada `[CD-24]`.

**Dependencias funcionales:** M-13 · M-14 · M-19 · M-20 · M-18 · M-15.

**Origen:** `[MON §8.2]` `[NUEVO en su control]`

---

## M-11 · Conteos

| Campo | Contenido |
|---|---|
| **Propósito** | Medir la exactitud del inventario y detectar diferencias, alimentando el indicador central del producto `[MON §8.2]` |
| **Alcance** | Conteo cíclico y conteo general: programación, ejecución, conciliación y cierre |
| **Actor responsable** | Coordinador (cíclico) · Jefe (general y cierre) · Auxiliar (cuenta) |
| **Prioridad** | P1 |
| **Procesos que implementa** | PN-08, PN-09 |

**Funciones:** programar conteo cíclico por ámbito · programar conteo general con fecha de corte · congelar existencia teórica · generar y asignar tareas de conteo · registrar conteo físico por escaneo `[DC-08]` · ocultar la existencia esperada al contador `[RN-040]` · comparar y clasificar diferencias · disparar segundo conteo obligatorio por umbral `[RN-041]` · reasignar tareas · consolidar y detectar ubicaciones no cubiertas · cerrar conteo y generar ajustes derivados · abortar conteo · bloquear y desbloquear movimientos en conteo general `[RN-045]` · calcular exactitud del ámbito contado.

**Restricciones:** el contador **nunca ve la cantidad esperada antes de contar** `[RN-040]` · el segundo conteo lo ejecuta obligatoriamente una persona distinta `[RN-041]` · quien ejecutó un conteo no lo cierra `[RN-041]` · solo el Jefe cierra conteos `[RN-042]` · un conteo general no cierra con ubicaciones sin cubrir ni justificar `[RN-046]` · la existencia congelada no se altera por movimientos concurrentes `[RN-039]` · un conteo cerrado no se reabre.

**Funciones incorporadas en la v1.2:** conteo manual pieza por pieza `[F-5]` `[RN-089*]`. El **conteo general** sigue en el Horizonte 2 y queda fuera del umbral aprobatorio `[DEC-01]`; la granularidad pieza por pieza y el alcance del conteo (cíclico o general) son ejes independientes.

**Dependencias funcionales:** M-13 · M-10 · M-14 · M-05 · M-06 · M-19 · M-20.

**Origen:** `[MON §8.2]` `[NUEVO — diferenciador D-05]`

---

## M-12 · Novedades de Mercancía

| Campo | Contenido |
|---|---|
| **Propósito** | Dar al operario una vía formal para reportar anomalías físicas sin exponerse `[MON §4]` `[PR-06]` |
| **Alcance** | Reporte, evaluación, resolución y cierre de novedades |
| **Actor responsable** | Auxiliar (reporta) · Coordinador y Jefe (resuelven) |
| **Prioridad** | P1 |
| **Procesos que implementa** | PN-12 |

**Funciones:** reportar novedad con tipo tipificado · escanear identificador o declarar su ausencia · indicar ubicación y descripción · adjuntar evidencia fotográfica · dirigir automáticamente al Coordinador · evaluar y determinar acción · vincular la novedad con el movimiento que la resuelve · cerrar novedad con constancia · escalar por vencimiento de plazo · consultar novedades por estado, tipo y período.

**Restricciones:** una novedad **no se elimina, se cierra** `[RN-063]` · una novedad sobre una unidad con novedad abierta se vincula, no se duplica `[RN-060]` · el cierre exige constancia de resolución · el Auxiliar puede reportar pero no resolver.

**Dependencias funcionales:** M-10 · M-14 · M-06 · M-20 · M-13.

**Origen:** `[MON §4]` `[NUEVO]`

---

## M-13 · Consulta de Existencia

| Campo | Contenido |
|---|---|
| **Propósito** | Responder en el momento qué hay, cuánto hay y dónde está, sustituyendo la consulta al cuaderno `[MON §3, §6]` |
| **Alcance** | Consulta por referencia, SKU, lote, ubicación e identificador; desglose por estado |
| **Actor responsable** | Todos los roles, con visibilidad diferenciada `[§2.7]` |
| **Prioridad** | P0 |
| **Procesos que implementa** | PN-04 |

**Funciones:** consultar existencia por referencia y SKU · consultar por lote · consultar por ubicación · consultar escaneando identificador `[DC-08]` · mostrar desglose disponible / reservado / inmovilizado / en tránsito · mostrar distribución por ubicación · consultar existencia histórica a una fecha dada · buscar por texto aproximado · exportar el resultado de consulta.

**Restricciones:** el Auxiliar **no ve valorización ni costos** `[PR-04]` · la existencia mostrada siempre se deriva del kardex, nunca de un valor almacenado independientemente `[RN-065]` · la consulta nunca modifica el estado del inventario · un usuario solo consulta dentro de su ámbito asignado, salvo Administrador, Jefe y Auditor.

**Funciones incorporadas en la v1.2:** consultar las piezas de un lote con tipo, cantidad actual, ubicación y estado `[Q-11]`.

**Dependencias funcionales:** M-14 · M-03 · M-05 · M-04 · M-02.

**Origen:** `[MON §6, §7.2]`

---

## M-14 · Kardex y Trazabilidad

| Campo | Contenido |
|---|---|
| **Propósito** | Constituir el registro cronológico inmutable del que se deriva toda la existencia y sobre el que descansa la trazabilidad `[MON §7.1]` |
| **Alcance** | Registro, consulta y verificación de integridad de los movimientos |
| **Actor responsable** | El sistema (registra) · todos los roles (consultan según §2.7) |
| **Prioridad** | P0 |

**Funciones:** registrar todo movimiento con fecha, hora, tipo, cantidad, existencia resultante, ubicación, usuario, motivo y documento · consultar kardex de una unidad de inventario · consultar kardex de un lote · consultar kardex de una ubicación · filtrar por tipo, período, usuario y motivo · reconstruir la existencia a una fecha dada · verificar la integridad: existencia actual igual a la suma de movimientos `[RN-065]` · exportar kardex · consultar movimientos anulados con su justificación.

**Restricciones:** **ningún movimiento confirmado se edita ni se elimina, por ningún rol, incluido el Administrador** `[RN-012]` · un error se corrige generando un movimiento inverso, quedando ambos visibles `[CD-34]` · todo movimiento tiene un usuario atribuible; **no existen movimientos anónimos** `[PR-05]` · el kardex es la fuente de verdad de la existencia `[RN-065]` · el Auxiliar solo consulta el kardex de las unidades que él movió y de los últimos 30 días `[§2.7]`.

**Funciones incorporadas en la v1.2:** registrar la pieza afectada en cada movimiento y consultar el kardex de una pieza `[Q-11]`.

**Dependencias funcionales:** todos los módulos operativos (M-07 a M-12) escriben en él · M-13 y M-16 leen de él.

**Origen:** `[MON §7.1, §8.2]` — **realiza el concepto CD-21 (Trazabilidad)**

---

## M-15 · Alertas y Reglas

| Campo | Contenido |
|---|---|
| **Propósito** | Materializar la «inteligencia» del producto: automatización basada en reglas que anticipa problemas `[DC-07]` `[MON §3, §7.1]` |
| **Alcance** | Evaluación de condiciones, generación, dirección, atención y cierre de alertas |
| **Actor responsable** | El sistema (genera) · Jefe y Coordinador (atienden) · Administrador (configura umbrales) |
| **Prioridad** | P1 |
| **Procesos que implementa** | PN-11 |

**Funciones:** evaluar continuamente las condiciones configuradas · generar alerta con tipo y severidad · dirigirla al rol responsable · presentarla en el panel del destinatario · notificar según severidad · registrar la atención con acción y responsable · exigir motivo al descartar `[RN-058]` · cerrar automáticamente al cesar la condición `[RN-057]` · escalar alertas críticas no atendidas `[RN-056]` · agrupar alertas de una misma condición vigente `[RN-055]` · consultar el historial de alertas · reportar frecuencia de disparo para recalibrar umbrales.

**Restricciones:** `[DC-07]` **las alertas se generan exclusivamente por reglas explícitas y umbrales configurados; no existe predicción ni modelo de aprendizaje** · toda alerta tiene un destinatario por rol; **ninguna queda sin responsable** · una alerta descartada sin motivo no puede cerrarse `[RN-058]` · el Auxiliar no gestiona alertas `[§2.7]`.

**Dependencias funcionales:** M-13 · M-09 · M-10 · M-11 · M-19 · M-20 · M-04.

**Origen:** `[MON §3, §7.1]` `[DC-07]` — **materializa la definición de «inteligente» de §1.6**

---

## M-16 · Reportes y Exportación Analítica

| Campo | Contenido |
|---|---|
| **Propósito** | Entregar información consolidada al usuario y poner los datos a disposición de la herramienta analítica externa `[DC-06]` `[MON §8.2]` |
| **Alcance** | Reportes operativos, reportes gerenciales, cálculo de KPIs, exportación estructurada |
| **Actor responsable** | Jefe · Administrador · Auditor · Coordinador (operativos) |
| **Prioridad** | P1 |

**Funciones:** generar reporte de existencia por referencia, lote y ubicación · reporte de movimientos por período y tipo · reporte de entradas y salidas · reporte de ajustes con motivo y aprobador · reporte de conteos y diferencias · reporte de exactitud del inventario · reporte de alertas y su atención · reporte de novedades · reporte de productividad de bodega · calcular los 24 KPIs del Cap. 10 · exportar reportes en formato tabular · exponer los datos de forma estructurada para consumo de la herramienta analítica externa `[DC-06]` · programar generación periódica de reportes.

**Restricciones:** `[DC-06]` **este módulo no diseña ni contiene dashboards analíticos**: prepara y expone los datos; la visualización analítica se resuelve en la herramienta externa · en el MVP no existe valorización: ningún reporte muestra costo ni valorización, y la restricción se conserva de forma preventiva `[PR-04]` `[DEC-07]` · todo reporte declara su fecha y hora de generación y el usuario que lo generó · la exportación queda registrada en la bitácora `[RN-061]` · un reporte nunca modifica datos.

**Dependencias funcionales:** M-14 · M-13 · M-10 · M-11 · M-15 · M-12 · M-02.

**Origen:** `[MON §8.2]` `[DC-06]`

---

## M-17 · Dashboard Operativo

| Campo | Contenido |
|---|---|
| **Propósito** | Dar a cada rol una vista inmediata del estado de la bodega y de lo que requiere su atención |
| **Alcance** | Panel operativo por rol; panel de tareas del operario |
| **Actor responsable** | Jefe · Coordinador (restringido a su zona) · Administrador · Auditor |
| **Prioridad** | P1 |

**Funciones:** mostrar existencia total y su desglose por estado · mostrar alertas activas por severidad · mostrar pendientes: recepciones sin confirmar, movimientos en tránsito, ajustes por aprobar, conteos abiertos, novedades sin resolver · mostrar movimientos del día · mostrar exactitud del inventario vigente (KPI-01) · mostrar el panel de tareas del usuario `[NUEVO]` · permitir navegar desde cualquier elemento hacia su detalle.

**Restricciones:** `[DC-06]` **este es el dashboard operativo del sistema, no el tablero analítico**: no compite con la herramienta externa y no incluye análisis histórico profundo · el Coordinador ve solo su zona · el Auxiliar **no ve el dashboard**: ve exclusivamente su panel de tareas `[§2.7]` · ningún panel expone indicadores de desempeño individual al operario `[PR-06]`.

**Dependencias funcionales:** M-13 · M-15 · M-16 · M-20 · M-11 · M-10.

**Origen:** `[DC-02]` `[NUEVO]`

---

## M-18 · Auditoría y Bitácora

| Campo | Contenido |
|---|---|
| **Propósito** | Registrar de forma inmutable toda acción relevante del sistema y habilitar la verificación independiente `[PR-02]` |
| **Alcance** | Bitácora de sistema, consulta de auditoría, observaciones del Auditor, verificación de integridad |
| **Actor responsable** | El sistema (registra) · Auditor (consulta y observa) · Administrador (consulta) |
| **Prioridad** | P1 |
| **Procesos que implementa** | PN-13 |

**Funciones:** registrar accesos e intentos fallidos · registrar cambios de configuración y de umbrales · registrar cambios de rol y estado de usuario · registrar aprobaciones y rechazos · registrar anulaciones con su justificación · registrar exportaciones de datos · consultar la bitácora con filtros por usuario, fecha y tipo de evento · verificar la integridad del kardex `[RN-065]` · detectar aprobaciones propias `[RN-023]` · detectar movimientos sin usuario atribuible · registrar observaciones de auditoría en un registro separado `[RN-064]` · generar y exportar el reporte de auditoría.

**Restricciones:** `[PR-02]` **el Auditor no escribe en el inventario bajo ninguna circunstancia**; su única escritura son observaciones que no alteran el estado `[RN-064]` · las observaciones las responde y cierra el Administrador o el Jefe `[DEC-04]` · **la bitácora no es editable ni borrable por ningún rol, incluido el Administrador** `[RN-061]` · la bitácora es un registro distinto del kardex y no lo sustituye · toda discontinuidad detectada en la bitácora es un hallazgo crítico.

**Dependencias funcionales:** todos los módulos escriben en él · M-14 · M-02.

**Origen:** `[PR-01, PR-02]` `[MON §6]` `[NUEVO]`

---

## M-19 · Parámetros y Configuración

| Campo | Contenido |
|---|---|
| **Propósito** | Permitir que la empresa adapte el comportamiento del sistema a su operación sin necesidad de intervención técnica |
| **Alcance** | Umbrales, políticas, motivos tipificados, plazos, reglas configurables |
| **Actor responsable** | Administrador, en exclusiva |
| **Prioridad** | P0 |

**Funciones:** configurar umbrales de existencia mínima y máxima por SKU · configurar el umbral que separa ajuste menor de mayor `[RN-024]` · configurar el umbral de tolerancia de conteo `[RN-041]` · configurar el tiempo máximo en tránsito `[RN-034]` · configurar plazos de vencimiento de reserva, ajuste y novedad · mantener el catálogo de motivos tipificados `[CD-36]` · configurar la política de toma en salida `[RN-049]` · configurar reglas de asignación automática de ubicación · configurar tiempo de inactividad de sesión · configurar destinatarios de alerta por tipo · consultar el historial de cambios de configuración.

**Restricciones:** **todo cambio de configuración queda en la bitácora, con valor anterior y nuevo** `[RN-061]` · un motivo tipificado en uso no se elimina, se desactiva `[RN-063]` · los umbrales tienen rangos válidos que el sistema valida · **la configuración no puede alterar las reglas estructurales del Cap. 9 marcadas como no configurables** (segregación de funciones, inmutabilidad del kardex, prohibición de existencia negativa).

**Dependencias funcionales:** M-02 · M-18 · M-03 · M-05 · M-15.

**Origen:** `[NUEVO]`

---

## M-20 · Notificaciones y Tareas

| Campo | Contenido |
|---|---|
| **Propósito** | Llevar a cada persona lo que debe hacer y lo que debe saber, en el dispositivo en que trabaja `[DC-05]` |
| **Alcance** | Panel de tareas, notificaciones en sistema, escalamientos |
| **Actor responsable** | El sistema (genera) · todos los roles (reciben) |
| **Prioridad** | P1 |

**Funciones:** generar tarea al asignar trabajo: recepción, ubicación, conteo, preparación de salida, transferencia · presentar el panel de tareas ordenado por prioridad · notificar alertas según severidad · notificar solicitudes pendientes de aprobación · notificar resultado de una solicitud al solicitante · escalar por vencimiento de plazo `[RN-056, RN-038, RN-059]` · marcar tarea como completada al confirmarse el movimiento asociado · reasignar tarea · consultar el historial de tareas por usuario.

**Restricciones:** una tarea siempre tiene un responsable identificado `[PR-05]` · la tarea se cierra por la ejecución del movimiento, **no por declaración del usuario** · reasignar una tarea deja registro de ambos responsables · las notificaciones no exponen información fuera del ámbito del destinatario `[PR-04]` · `[DC-05]` sin aplicación móvil nativa: las notificaciones viven dentro del sistema web.

**Dependencias funcionales:** M-07 · M-08 · M-09 · M-10 · M-11 · M-12 · M-15 · M-02.

**Origen:** `[DC-05]` `[NUEVO]`

---

## 5.2 Matriz módulo × proceso

| Módulo | PN-01 | PN-02 | PN-03 | PN-04 | PN-05 | PN-06 | PN-07 | PN-08 | PN-09 | PN-10 | PN-11 | PN-12 | PN-13 | PN-14 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| M-01 Acceso | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| M-03 Catálogo | ● | | | ● | | | | ● | ● | ● | | | ● | |
| M-04 Lotes | ● | ● | | ● | | ● | ● | ● | ● | ● | ● | | ● | |
| M-05 Estructura | | | ● | ● | ● | ● | | ● | ● | ● | ● | ● | | |
| M-06 QR | ● | ● | ● | ● | ● | ● | | ● | ● | ● | | ● | | |
| M-07 Entradas | ● | ● | ● | | | | | | | | | ● | | ● |
| M-08 Salidas | | | | | | | | | | ● | | ● | | ● |
| M-09 Movimientos | | | ● | | ● | ● | | | | | ● | | | ● |
| M-10 Ajustes | | | | | | ● | ● | ● | ● | ● | | ● | ● | ● |
| M-11 Conteos | | | | | | | ● | ● | ● | | ● | ● | ● | ● |
| M-12 Novedades | ● | ● | ● | | | | ● | ● | ● | ● | | ● | ● | ● |
| M-13 Existencia | ● | | ● | ● | ● | ● | ● | ● | ● | ● | ● | | ● | ● |
| M-14 Kardex | ● | | ● | ● | ● | ● | ● | ● | ● | ● | | | ● | ● |
| M-15 Alertas | | | | | ● | ● | ● | ● | ● | ● | ● | ● | | ● |
| M-16 Reportes | | | | ● | | | ● | ● | ● | | | | ● | ● |
| M-17 Dashboard | | | | ● | | ● | ● | ● | ● | ● | ● | ● | | ● |
| M-18 Auditoría | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| M-19 Parámetros | ● | | ● | | ● | ● | ● | ● | ● | ● | ● | ● | | |
| M-20 Tareas | ● | | ● | | ● | ● | ● | ● | ● | ● | ● | ● | | ● |

---

# CAPÍTULO 6 — HISTORIAS DE USUARIO

> **114 historias**, agrupadas por módulo. Cada una declara actor, prioridad, criterios de aceptación verificables y origen trazable. Los criterios están redactados para ser comprobables sin ambigüedad por el equipo de pruebas.

## 6.1 Distribución

| Módulo | Historias | Rango |
|---|:--:|---|
| M-01 Acceso | 4 | HU-001 – HU-004 |
| M-02 Usuarios y Roles | 5 | HU-005 – HU-009 |
| M-03 Catálogo | 6 | HU-010 – HU-015 |
| M-04 Lotes | 4 | HU-016 – HU-019 |
| M-05 Estructura de Bodega | 5 | HU-020 – HU-024 |
| M-06 Identificación QR | 5 | HU-025 – HU-029 |
| M-07 Entradas | 10 | HU-030 – HU-037, HU-104, HU-105 |
| M-08 Salidas | 9 | HU-038 – HU-044, HU-107, HU-108 |
| M-09 Movimientos y Transferencias | 9 | HU-045 – HU-051, HU-106, HU-111 |
| M-10 Ajustes | 6 | HU-052 – HU-057 |
| M-11 Conteos | 11 | HU-058 – HU-066, HU-109, HU-112 |
| M-12 Novedades | 4 | HU-067 – HU-070 |
| M-13 Consulta de Existencia | 6 | HU-071 – HU-076 |
| M-14 Kardex y Trazabilidad | 6 | HU-077 – HU-081, HU-110 |
| M-15 Alertas | 5 | HU-082 – HU-086 |
| M-16 Reportes | 4 | HU-087 – HU-090 |
| M-17 Dashboard | 3 | HU-091 – HU-093 |
| M-18 Auditoría | 4 | HU-094 – HU-097 |
| M-19 Parámetros | 3 | HU-098 – HU-100 |
| M-20 Tareas | 5 | HU-101 – HU-103, HU-113, HU-114 |
| **Total** | **114** | |

---

## M-01 · Acceso y Autenticación

**HU-001** · P0 · Todos los roles · `[PR-05]`
**COMO** usuario del sistema **QUIERO** iniciar sesión con una credencial que solo yo conozco **PARA** que todo lo que registre quede a mi nombre y nadie pueda actuar suplantándome.
*Criterios:* (1) El acceso exige identificador y contraseña individuales. (2) No existe cuenta genérica ni compartida. (3) Un acceso exitoso abre sesión y registra el evento en la bitácora. (4) Un acceso fallido no revela si el error fue en el usuario o en la contraseña. (5) Tras cinco intentos fallidos consecutivos la cuenta se bloquea y se notifica al Administrador.

**HU-002** · P0 · Auxiliar de Bodega · `[DC-05]`
**COMO** Auxiliar de Bodega **QUIERO** que mi sesión permanezca abierta mientras trabajo en la tablet **PARA** no tener que autenticarme cada vez que registro un movimiento.
*Criterios:* (1) La sesión permanece activa mientras haya actividad. (2) El cierre por inactividad ocurre tras el tiempo configurado en M-19. (3) Antes de cerrar, el sistema avisa. (4) Al reanudar, el sistema no pierde el registro en curso no confirmado. (5) El cierre por inactividad queda en la bitácora.

**HU-003** · P1 · Todos los roles · `[NUEVO]`
**COMO** usuario **QUIERO** cambiar mi contraseña cuando lo necesite **PARA** mantener el control sobre mi acceso.
*Criterios:* (1) El cambio exige la contraseña actual. (2) La nueva contraseña cumple la política mínima configurada. (3) La nueva no puede coincidir con la anterior. (4) El cambio cierra las demás sesiones activas del usuario. (5) El evento queda en la bitácora sin registrar ningún valor de contraseña.

**HU-004** · P1 · Administrador · `[NUEVO]`
**COMO** Administrador **QUIERO** restablecer el acceso de un usuario bloqueado **PARA** que la operación no se detenga por un olvido.
*Criterios:* (1) El Administrador desbloquea la cuenta y fuerza el cambio en el próximo acceso. (2) El sistema **nunca muestra la contraseña anterior**. (3) El restablecimiento queda en la bitácora con quién lo ejecutó. (4) El usuario afectado es notificado.

---

## M-02 · Usuarios y Roles

**HU-005** · P0 · Administrador · `[DC-04]`
**COMO** Administrador **QUIERO** crear usuarios y asignarles uno de los cinco roles oficiales **PARA** que cada persona acceda solo a lo que su función requiere.
*Criterios:* (1) El formulario ofrece exclusivamente los cinco roles de `[DC-04]`. (2) No existe opción de crear un rol nuevo. (3) Un usuario tiene exactamente un rol activo. (4) La creación queda en la bitácora. (5) El usuario nuevo debe cambiar su contraseña en el primer acceso.

**HU-006** · P0 · Administrador · `[RN-063]`
**COMO** Administrador **QUIERO** desactivar a un usuario que ya no trabaja en la bodega **PARA** cerrar su acceso sin perder el rastro de lo que hizo.
*Criterios:* (1) La desactivación cierra su acceso de inmediato. (2) **Los movimientos históricos del usuario se conservan íntegros y siguen mostrando su nombre.** (3) No existe la opción de eliminar un usuario. (4) Un usuario desactivado puede reactivarse. (5) El evento queda en la bitácora.

**HU-007** · P1 · Administrador · `[NUEVO]`
**COMO** Administrador **QUIERO** cambiar el rol de un usuario **PARA** reflejar un cambio de responsabilidades sin crear una cuenta nueva.
*Criterios:* (1) El cambio surte efecto en la siguiente sesión del usuario. (2) Los movimientos anteriores conservan el rol vigente al momento en que ocurrieron. (3) El cambio queda en la bitácora con rol anterior y nuevo. (4) El sistema impide dejar la bodega sin ningún Jefe activo.

**HU-008** · P1 · Administrador · `[NUEVO]`
**COMO** Administrador **QUIERO** asignar a cada usuario su bodega y su zona **PARA** que solo vea y opere sobre el ámbito que le corresponde.
*Criterios:* (1) Un Coordinador puede tener una o más zonas asignadas. (2) Un Auxiliar opera dentro de las zonas de su Coordinador. (3) Jefe, Administrador y Auditor no tienen restricción de ámbito de consulta. (4) La consulta y las tareas se filtran automáticamente por ámbito.

**HU-009** · P2 · Administrador · `[RN-011]`
**COMO** Administrador **QUIERO** que el sistema me impida quedarme sin administradores **PARA** no perder el control del sistema por error.
*Criterios:* (1) El sistema rechaza desactivar al último Administrador activo. (2) El sistema rechaza cambiarle el rol al último Administrador activo. (3) El mensaje explica el motivo del rechazo.

---

## M-03 · Catálogo de Referencias

**HU-010** · P0 · Administrador / Jefe · `[NUEVO]` `[D-01]`
**COMO** Jefe de Bodega **QUIERO** crear una referencia con sus tallas y colores **PARA** que la mercancía textil se registre con las dimensiones reales del negocio y no con campos improvisados.
*Criterios:* (1) La referencia tiene código único `[RN-002]`. (2) Se le asignan uno o más valores de talla y de color. (3) El sistema genera automáticamente los SKU resultantes de la combinación. (4) La referencia queda activa al crearse. (5) Si el código ya existe, el sistema rechaza y lo informa.

**HU-011** · P0 · Administrador / Jefe · `[RN-004]`
**COMO** Jefe de Bodega **QUIERO** definir la unidad de medida de cada referencia **PARA** que la mercancía se cuente como realmente se maneja: unidades, metros, rollos o kilogramos.
*Criterios:* (1) La unidad se selecciona de una lista configurada. (2) **La unidad no puede cambiarse si la referencia ya tiene movimientos** `[RN-004]`. (3) Todas las cantidades de esa referencia se expresan en su unidad. (4) El intento de cambio con movimientos existentes se rechaza con explicación.

**HU-012** · P1 · Administrador / Jefe · `[RN-010]` `[RN-063]`
**COMO** Jefe de Bodega **QUIERO** desactivar una referencia descontinuada **PARA** que no se use en nuevas operaciones sin perder su historial.
*Criterios:* (1) **No existe la opción de eliminar una referencia.** (2) El sistema rechaza desactivar una referencia con existencia distinta de cero `[RN-010]`. (3) Una referencia desactivada no aparece en la creación de documentos ni de movimientos. (4) Su kardex sigue siendo consultable. (5) Puede reactivarse.

**HU-013** · P1 · Administrador / Jefe · `[MON §3, §7.1]`
**COMO** Jefe de Bodega **QUIERO** definir la existencia mínima y máxima de cada SKU **PARA** que el sistema me avise antes de quedarme sin material o de acumular de más.
*Criterios:* (1) Los umbrales se definen por SKU. (2) El mínimo no puede ser mayor que el máximo. (3) Al cruzar un umbral, el sistema genera la alerta correspondiente (M-15). (4) Un SKU sin umbrales configurados no genera esas alertas y aparece en un listado de pendientes de configurar.

**HU-014** · P2 · Administrador · `[NUEVO]`
**COMO** Administrador **QUIERO** cargar el catálogo inicial de forma masiva **PARA** no tener que crear cientos de referencias una por una al arrancar.
*Criterios:* (1) El sistema acepta un archivo tabular con la estructura definida. (2) Valida antes de cargar y reporta los errores por línea. (3) No carga parcialmente: o carga todo lo válido y reporta lo rechazado, o no carga nada, según la opción elegida. (4) La carga queda en la bitácora con el número de registros procesados.

**HU-015** · P2 · Administrador / Jefe · `[NUEVO]`
**COMO** Jefe de Bodega **QUIERO** organizar las referencias por categoría **PARA** poder asignarlas a zonas y agrupar los reportes.
*Criterios:* (1) Una referencia pertenece a una sola categoría. (2) La categoría puede asociarse a una zona preferente para la asignación automática de ubicación. (3) Los reportes permiten agrupar por categoría. (4) Una categoría en uso no se elimina, se desactiva `[RN-063]`.

---

## M-04 · Gestión de Lotes

**HU-016** · P0 · Coordinador · `[MON §7.1]`
**COMO** Coordinador de Bodega **QUIERO** que la mercancía que ingresa quede asociada a un lote **PARA** poder rastrear después de dónde vino cada unidad.
*Criterios:* (1) Al confirmar una entrada se crea o se selecciona un lote. (2) El lote registra origen y fecha de ingreso. (3) El código de lote es único dentro de su SKU `[RN-014]`. (4) Ninguna existencia queda sin lote asociado. (5) El lote aparece en toda consulta y en el kardex.

**HU-017** · P1 · Jefe de Bodega · `[MON §7.1]`
**COMO** Jefe de Bodega **QUIERO** consultar dónde está distribuida toda la existencia de un lote **PARA** poder actuar sobre él completo si aparece un problema de calidad.
*Criterios:* (1) La consulta devuelve todas las ubicaciones donde hay existencia del lote, con su cantidad. (2) Muestra el total del lote y su estado. (3) Permite abrir el kardex completo del lote. (4) Permite inmovilizarlo desde la misma consulta.

**HU-018** · P1 · Jefe de Bodega · `[RN-036]`
**COMO** Jefe de Bodega **QUIERO** inmovilizar un lote completo **PARA** impedir que salga mercancía sospechosa mientras se verifica.
*Criterios:* (1) La inmovilización afecta **toda** la existencia del lote, en todas sus ubicaciones. (2) La existencia inmovilizada deja de contar como disponible. (3) Todo intento de salida, transferencia o movimiento sobre ella se rechaza `[RN-036]`. (4) Requiere motivo tipificado. (5) Solo Jefe o Administrador pueden liberarlo. (6) Queda en la bitácora.

**HU-019** · P2 · Jefe de Bodega · `[NUEVO]`
**COMO** Jefe de Bodega **QUIERO** ver los lotes ordenados por antigüedad **PARA** priorizar la salida de los más viejos y evitar que se deterioren en bodega.
*Criterios:* (1) El listado ordena por fecha de ingreso. (2) Muestra los días en bodega. (3) Permite filtrar por referencia y por categoría. (4) Los lotes por encima del umbral de antigüedad configurado se destacan.

---

## M-05 · Estructura de Bodega

**HU-020** · P0 · Administrador · `[NUEVO]`
**COMO** Administrador **QUIERO** definir las zonas y ubicaciones de la bodega **PARA** que el sistema pueda decir dónde está físicamente cada cosa.
*Criterios:* (1) Se crean zonas dentro de una bodega, con tipo asignado. (2) Se crean ubicaciones dentro de una zona. (3) El código de ubicación es único en la bodega `[RN-014]`. (4) Debe existir al menos una zona de recepción por bodega `[RN-019]`. (5) Cada ubicación creada obtiene su identificador QR (M-06).

**HU-021** · P1 · Administrador · `[RN-021]`
**COMO** Administrador **QUIERO** definir la capacidad de cada ubicación **PARA** que el sistema no proponga guardar mercancía donde no cabe.
*Criterios:* (1) La capacidad se expresa en una unidad configurada. (2) El sistema no propone como destino una ubicación sin capacidad suficiente. (3) Si la ocupación supera la capacidad, se genera alerta `[RN-021]`. (4) Una ubicación sin capacidad definida se trata como de capacidad ilimitada y se lista como pendiente de configurar.

**HU-022** · P1 · Administrador · `[RN-013]` `[RN-063]`
**COMO** Administrador **QUIERO** desactivar una ubicación fuera de servicio **PARA** que no se asigne mercancía a un lugar inutilizable.
*Criterios:* (1) **No existe la opción de eliminar una ubicación.** (2) El sistema rechaza desactivar una ubicación con existencia `[RN-013]`. (3) Una ubicación desactivada no se propone ni se acepta como destino. (4) Su historial sigue consultable. (5) Puede reactivarse.

**HU-023** · P2 · Administrador · `[NUEVO]`
**COMO** Administrador **QUIERO** asignar un Coordinador responsable a cada zona **PARA** que las alertas y las tareas lleguen a la persona correcta.
*Criterios:* (1) Una zona tiene un Coordinador responsable. (2) Las alertas de la zona se dirigen a él. (3) El dashboard del Coordinador se filtra a sus zonas. (4) Una zona sin responsable escala al Jefe.

**HU-024** · P2 · Administrador · `[NUEVO]`
**COMO** Administrador **QUIERO** configurar cómo el sistema propone la ubicación de la mercancía que ingresa **PARA** que el Auxiliar no tenga que decidirlo cada vez.
*Criterios:* (1) Se configuran criterios de asignación: zona por categoría, agrupación por referencia, ubicación con mayor capacidad libre. (2) El sistema aplica los criterios en el orden configurado. (3) Si ninguno aplica, propone la zona de recepción. (4) La propuesta siempre es sugerencia: el Coordinador puede reasignar `[RN-022]`.

---

## M-06 · Identificación QR

**HU-025** · P0 · Coordinador · `[DC-08]`
**COMO** Coordinador de Bodega **QUIERO** generar e imprimir un código QR para la mercancía que ingresa **PARA** que después se pueda escanear en lugar de escribir a mano.
*Criterios:* (1) El sistema genera un identificador único por SKU + Lote `[RN-016]` `[DF5-01]`. (2) Permite impresión individual y por lote de impresión. (3) El identificador impreso incluye información legible de respaldo: referencia, talla, color y lote. (4) El identificador queda en estado activo. (5) **Ningún identificador se repite jamás, ni tras su anulación** `[RN-016]`.

**HU-026** · P0 · Auxiliar · `[DC-08]` `[MON §7.2]`
**COMO** Auxiliar de Bodega **QUIERO** escanear el código QR en lugar de escribir códigos **PARA** no equivocarme y terminar más rápido.
*Criterios:* (1) El escaneo se hace desde la tablet `[DC-05]`. (2) El sistema resuelve el identificador y muestra el SKU + Lote y las ubicaciones donde tiene existencia `[DF5-01]`. (3) Si el identificador no se reconoce, lo informa y ofrece reportar novedad. (4) Si el identificador está anulado, lo informa y rechaza la operación. (5) El tiempo entre escaneo y respuesta cumple RNF-014.

**HU-027** · P1 · Administrador · `[NUEVO]`
**COMO** Administrador **QUIERO** generar códigos QR para las ubicaciones **PARA** que el Auxiliar confirme dónde deja la mercancía escaneando, sin escribir el código del estante.
*Criterios:* (1) Cada ubicación tiene su identificador QR propio. (2) Se puede imprimir por zona completa. (3) El escaneo de una ubicación la selecciona como origen o destino según el contexto. (4) El identificador de ubicación es distinguible del de mercancía.

**HU-028** · P1 · Auxiliar / Coordinador · `[RN-018]`
**COMO** Auxiliar de Bodega **QUIERO** solicitar la reimpresión de una etiqueta deteriorada **PARA** poder seguir trabajando sin perder la trazabilidad de esa mercancía.
*Criterios:* (1) La reimpresión exige motivo. (2) **La reimpresión produce otra copia del mismo QR: el identificador no cambia y no se crea una nueva identidad** `[RN-018]` `[Q-09]`. (3) Reimprimir no marca el identificador como reemplazado. (4) El historial de reimpresiones del SKU + Lote es consultable. (5) La reimpresión queda en la bitácora.

**HU-029** · P2 · Coordinador · `[DC-08]` `[RN-017]`
**COMO** Coordinador de Bodega **QUIERO** asociar el código de barras del proveedor a nuestro identificador QR de SKU + Lote **PARA** aprovechar la etiqueta que ya viene, sin dejar de usar el QR como identificador principal.
*Criterios:* (1) El código de barras se asocia como identificador secundario. (2) Su lectura permite **consultar** el SKU + Lote. (3) `[RN-017]` **No permite por sí solo ejecutar operaciones de escritura**: estas exigen el QR. (4) Un mismo código de barras no puede asociarse a dos identificadores QR distintos `[DF5-01]`.

---

## M-07 · Entradas y Recepción

**HU-030** · P0 · Coordinador · `[MON §8.2]`
**COMO** Coordinador de Bodega **QUIERO** crear un documento de entrada con lo que espero recibir **PARA** poder verificar contra él lo que realmente llega.
*Criterios:* (1) El documento registra origen, fecha esperada y líneas con referencia, talla, color y cantidad esperada. (2) `[DC-03]` **No solicita precio, condiciones comerciales ni datos de orden de compra.** (3) Queda en estado pendiente de recepción. (4) Si existe otro documento con mismo origen, referencia y fecha, el sistema advierte de posible duplicado `[RN-003]`.

**HU-031** · P0 · Auxiliar · `[MON §3, §8.2]`
**COMO** Auxiliar de Bodega **QUIERO** registrar en la tablet lo que voy recibiendo, en el momento de recibirlo **PARA** no tener que anotarlo en un papel y pasarlo después.
*Criterios:* (1) El registro se hace desde la tablet, en la zona de recepción `[DC-05]`. (2) Se registra cantidad recibida por línea. (3) El sistema confirma visualmente cada registro guardado. (4) La recepción puede interrumpirse y continuarse, incluso por otro usuario, quedando ambos registrados. (5) Sin conectividad, el registro se retiene y sincroniza después `[RN-054]`.

**HU-032** · P0 · Coordinador · `[PR-01]`
**COMO** Coordinador de Bodega **QUIERO** confirmar la entrada después de que el Auxiliar la recibió **PARA** que exista una verificación por una segunda persona antes de afectar el inventario.
*Criterios:* (1) `[PR-01]` **Quien registró la recepción física no puede confirmarla.** (2) Al confirmar, el sistema genera el movimiento de entrada en el kardex. (3) La existencia se incrementa. (4) Se crea o asocia el lote. (5) Una entrada confirmada no puede editarse `[RN-012]`.

**HU-033** · P0 · Coordinador / Jefe · `[RN-005]` `[RN-006]`
**COMO** Coordinador de Bodega **QUIERO** que el sistema me muestre la diferencia entre lo esperado y lo recibido **PARA** detectar faltantes de proveedor en el momento y no días después.
*Criterios:* (1) El sistema compara línea por línea. (2) Si lo recibido es menor, marca faltante de recepción y notifica al Jefe `[RN-006]`. (3) Si es mayor, marca sobrante y **exige autorización del Jefe antes de confirmar** `[RN-007]`. (4) Si coincide, marca recibido conforme. (5) La diferencia queda registrada en el documento.

**HU-034** · P1 · Auxiliar · `[RN-008]`
**COMO** Auxiliar de Bodega **QUIERO** registrar que parte de la mercancía llegó dañada **PARA** que no entre al inventario disponible y quede constancia de la novedad.
*Criterios:* (1) Se registra la cantidad conforme y la cantidad dañada por separado. (2) **La dañada no ingresa como disponible** `[RN-008]`. (3) Se abre automáticamente una novedad (M-12). (4) La mercancía dañada, si ingresa, lo hace a zona de cuarentena en estado inmovilizado. (5) El Jefe es notificado.

**HU-035** · P0 · Auxiliar · `[NUEVO]`
**COMO** Auxiliar de Bodega **QUIERO** que el sistema me diga dónde dejar la mercancía **PARA** no tener que decidirlo yo ni preguntar cada vez.
*Criterios:* (1) El sistema propone ubicación según los criterios de HU-024. (2) El Auxiliar confirma escaneando la mercancía y luego la ubicación `[DC-08]`. (3) Si ubica en un lugar distinto, el sistema lo permite pero registra la desviación y avisa al Coordinador `[RN-022]`. (4) El sistema valida que la ubicación esté activa y tenga capacidad `[RN-021]`. (5) Confirma visualmente el registro.

**HU-036** · P1 · Coordinador · `[RN-002]`
**COMO** Coordinador de Bodega **QUIERO** que el sistema me impida recibir una referencia que no existe en el catálogo **PARA** que no entre mercancía sin identidad definida.
*Criterios:* (1) El documento de entrada solo admite referencias activas del catálogo `[RN-002]`. (2) Si la referencia no existe, el sistema lo informa y ofrece crearla, si el usuario tiene permiso. (3) El Auxiliar no puede crear referencias. (4) La entrada no avanza hasta resolverlo.

**HU-037** · P2 · Coordinador / Jefe · `[NUEVO]`
**COMO** Coordinador de Bodega **QUIERO** consultar el historial de entradas **PARA** revisar qué se recibió, de quién y con qué novedades.
*Criterios:* (1) Filtro por período, origen, estado y referencia. (2) Muestra esperado, recibido y diferencia. (3) Permite abrir el detalle y el movimiento de kardex asociado. (4) Exportable.

**HU-104** · P0 · Auxiliar · `[Q-11]` `[F-1]` `[F-2]`
**COMO** Auxiliar de Bodega **QUIERO** registrar cada rollo, paquete o bolsa que recibo con su cantidad **PARA** saber después cuál pieza es cuál y cuánto trae cada una sin tener que medirla otra vez.
*Criterios:* (1) Cada pieza se registra con su tipo —rollo para referencias en metros o kilogramos; paquete o bolsa para referencias en unidades— y con su cantidad propia `[F-1]` `[F-2]`. (2) Cada pieza pertenece a un solo SKU + Lote `[RN-084*]`. (3) La cantidad recibida de la línea es la suma de las cantidades de sus piezas y se compara contra la esperada `[RN-085*]` `[RN-005]`. (4) La pieza conserva su identidad en el sistema desde la recepción; el QR de mercancía sigue identificando solo el SKU + Lote `[DF5-01]`. (5) El sistema confirma visualmente cada pieza registrada.

**HU-105** · P1 · Auxiliar · `[F-6]`
**COMO** Auxiliar de Bodega **QUIERO** registrar como una sola pieza el contenedor o la bolsa agrupada en que llega mercancía sin rotulado individual **PARA** poder ubicarla, moverla y contarla sin rotular cada prenda.
*Criterios:* (1) El contenedor o bolsa agrupada se registra como una pieza de tipo contenedor agrupado, con su cantidad de unidades `[F-6]`. (2) El contenedor pertenece a un solo SKU + Lote; registrar un contenedor con mezcla de lotes o de SKU no se admite hasta que el Director lo decida `[DECISIÓN PENDIENTE — HD-28]`. (3) Se ubica, mueve, cuenta y sale como cualquier otra pieza. (4) Lleva la etiqueta QR del SKU + Lote `[PN-02 E-03]`.

---

## M-08 · Salidas

**HU-038** · P0 · Jefe / Coordinador · `[MON §8.2]` `[DC-03]`
**COMO** Jefe de Bodega **QUIERO** registrar una salida indicando su motivo **PARA** que quede claro por qué salió la mercancía sin necesidad de gestionar la venta en este sistema.
*Criterios:* (1) La salida exige motivo tipificado de una lista cerrada `[RN-048]`. (2) `[DC-03]` **No se solicita cliente, precio, factura ni documento comercial.** (3) Se indican referencias, tallas, colores, lotes y cantidades. (4) El sistema verifica disponibilidad antes de aceptar `[RN-025]`.

**HU-039** · P0 · Jefe · `[RN-031]`
**COMO** Jefe de Bodega **QUIERO** que la existencia se reserve al autorizar la salida **PARA** que nadie más comprometa la misma mercancía mientras se prepara.
*Criterios:* (1) Al autorizar, la cantidad pasa a reservada `[RN-031]`. (2) La existencia reservada **no cuenta como disponible**. (3) Otra operación sobre la misma existencia se rechaza. (4) La reserva se libera al ejecutarse la salida, al cancelarse o al vencer su plazo `[RN-051]`.

**HU-040** · P0 · Auxiliar · `[DC-08]` `[RN-050]`
**COMO** Auxiliar de Bodega **QUIERO** que el sistema me indique de qué ubicación tomar cada cosa y me valide el escaneo **PARA** no equivocarme de talla, color o lote.
*Criterios:* (1) El sistema indica ubicación y cantidad por línea, según la política configurada `[RN-049]`. (2) El Auxiliar escanea cada unidad al tomarla. (3) **Si lo escaneado no corresponde a lo solicitado, el sistema rechaza el escaneo y explica la discrepancia** `[RN-050]`. (4) El progreso de preparación es visible. (5) Confirma al completar.

**HU-041** · P0 · Jefe / Coordinador · `[RN-009]`
**COMO** Jefe de Bodega **QUIERO** que el sistema me impida sacar más de lo que hay **PARA** que el inventario nunca quede en negativo.
*Criterios:* (1) `[RN-009]` **Ninguna salida puede dejar la existencia por debajo de cero, sin excepción ni autorización posible.** (2) Si lo disponible es insuficiente, el sistema rechaza e informa cuánto hay. (3) Ofrece registrar una salida parcial por la cantidad disponible, previa autorización. (4) El rechazo queda registrado.

**HU-042** · P1 · Jefe · `[RN-052]`
**COMO** Jefe de Bodega **QUIERO** que la baja de mercancía dañada exija mi aprobación siempre **PARA** que nadie pueda dar de baja inventario sin que yo lo sepa.
*Criterios:* (1) El motivo de baja por daño **siempre** requiere aprobación del Jefe, cualquiera sea la cantidad `[RN-052]`. (2) Exige observación y evidencia. (3) Genera movimiento de salida marcado como baja. (4) Alimenta el reporte de mermas y el KPI-13.

**HU-043** · P1 · Coordinador · `[RN-053]`
**COMO** Coordinador de Bodega **QUIERO** registrar el retorno de mercancía que había salido **PARA** que vuelva al inventario dejando claro de dónde vino.
*Criterios:* (1) `[RN-053]` **El retorno se registra como una entrada nueva, no como reversión de la salida original.** (2) La entrada de retorno referencia la salida original. (3) El kardex muestra ambos movimientos. (4) La mercancía retornada puede requerir inspección antes de quedar disponible.

**HU-044** · P1 · Jefe / Coordinador · `[RN-030]`
**COMO** Coordinador de Bodega **QUIERO** poder autorizar salidas pequeñas sin molestar al Jefe **PARA** que la operación no se detenga por cada movimiento menor.
*Criterios:* (1) El Administrador configura el umbral de autorización del Coordinador `[RN-030]`. (2) Por debajo del umbral, el Coordinador autoriza. (3) Por encima, la solicitud se enruta al Jefe. (4) El umbral es consultable por el Coordinador. (5) Toda autorización queda atribuida a quien la otorgó.

**HU-107** · P0 · Auxiliar · `[Q-10]` `[RN-088*]`
**COMO** Auxiliar de Bodega **QUIERO** que, al preparar una salida, el escaneo me confirme que tomo lo correcto y cuente las piezas que tomo **PARA** no dejar la salida incompleta ni contar dos veces lo mismo.
*Criterios:* (1) El escaneo verifica que lo tomado corresponde a lo solicitado `[RN-050]` y cuenta las piezas tomadas `[Q-10]`. (2) Después de escanear, el Auxiliar selecciona la pieza; cada pieza se cuenta una sola vez y seleccionar de nuevo la misma no suma `[RN-088*]`. (3) El progreso muestra las piezas y la cantidad tomadas frente a lo solicitado. (4) La preparación no se confirma completa mientras falten piezas o cantidad, salvo salida parcial autorizada `[RN-025]`. (5) Cada pieza tomada queda en el kardex.

**HU-108** · P0 · Auxiliar · `[F-3]` `[RN-086*]`
**COMO** Auxiliar de Bodega **QUIERO** registrar que corté solo una parte de un rollo **PARA** que el resto siga en el inventario con la cantidad correcta.
*Criterios:* (1) Se selecciona la pieza y se indica la cantidad cortada `[F-3]`. (2) La cantidad cortada no puede superar la cantidad de la pieza `[RN-009]` `[RN-086*]`. (3) El sistema descuenta lo cortado de la pieza, que conserva su identidad con el remanente `[RN-086*]`. (4) El corte se registra como una salida, con motivo tipificado, autorización y atribución personal `[RN-048]`. (5) El kardex registra qué pieza, cuánto, quién, cuándo y por qué. (6) La cantidad restante de la pieza queda visible de inmediato.

---

## M-09 · Movimientos y Transferencias

**HU-045** · P0 · Auxiliar · `[RN-026]`
**COMO** Auxiliar de Bodega **QUIERO** registrar que moví mercancía de un estante a otro **PARA** que el sistema siga sabiendo dónde está.
*Criterios:* (1) Se escanea la mercancía y luego la ubicación destino `[DC-08]`. (2) Se puede mover cantidad total o parcial. (3) `[RN-026]` **La existencia total no cambia**: solo cambia su distribución. (4) El movimiento queda en el kardex. (5) El sistema confirma visualmente.

**HU-046** · P0 · Auxiliar · `[RN-025]` `[RN-027]`
**COMO** Auxiliar de Bodega **QUIERO** que el sistema me impida movimientos imposibles **PARA** no dejar el inventario descuadrado por un error mío.
*Criterios:* (1) Rechaza mover más de lo existente en origen `[RN-025]`. (2) Rechaza destino igual a origen `[RN-027]`. (3) Rechaza destino inactivo o sin capacidad `[RN-021]`. (4) Rechaza mover existencia inmovilizada `[RN-036]`. (5) Cada rechazo explica el motivo en lenguaje comprensible `[MON §8.2 — usabilidad]`.

**HU-047** · P0 · Coordinador · `[NUEVO]`
**COMO** Coordinador de Bodega **QUIERO** crear una transferencia hacia otra zona o bodega **PARA** mover mercancía entre ámbitos con control de despacho y recepción.
*Criterios:* (1) Se indican origen, destino, referencias y cantidades. (2) Al crearse, la existencia se reserva en origen `[RN-031]`. (3) Queda en estado pendiente de despacho. (4) Genera tarea para el Auxiliar del origen (M-20).

**HU-048** · P0 · Auxiliar · `[RN-032]`
**COMO** Auxiliar de Bodega **QUIERO** confirmar el despacho y la recepción de una transferencia escaneando **PARA** que quede claro quién la entregó y quién la recibió.
*Criterios:* (1) El despacho lo confirma el Auxiliar del origen escaneando. (2) La transferencia pasa a en tránsito `[RN-032]`. (3) `[RN-032]` **La existencia en tránsito no está disponible ni en origen ni en destino.** (4) La recepción la confirma el Auxiliar del destino escaneando. (5) Ambos responsables quedan registrados.

**HU-049** · P1 · Jefe · `[RN-033]`
**COMO** Jefe de Bodega **QUIERO** que el sistema me avise si lo recibido no coincide con lo despachado **PARA** investigar antes de que se pierda el rastro.
*Criterios:* (1) El sistema compara despachado contra recibido `[RN-033]`. (2) Si lo recibido es menor, registra diferencia y abre novedad. (3) Si lo recibido es mayor, **rechaza la recepción** y escala al Jefe. (4) La transferencia no se completa hasta que el Jefe resuelva. (5) La resolución queda documentada.

**HU-050** · P1 · Jefe / Coordinador · `[RN-034]`
**COMO** Jefe de Bodega **QUIERO** que el sistema me alerte si una transferencia lleva demasiado tiempo en tránsito **PARA** que no se pierda mercancía en el camino.
*Criterios:* (1) El tiempo máximo en tránsito es configurable `[RN-034]`. (2) Al superarlo, se genera alerta dirigida al Jefe. (3) La alerta identifica la transferencia, su contenido y su responsable de despacho. (4) La alerta se cierra al completarse o cancelarse la transferencia.

**HU-051** · P1 · Jefe · `[RN-035]`
**COMO** Jefe de Bodega **QUIERO** poder cancelar una transferencia **PARA** resolver situaciones donde la mercancía no puede llegar a su destino.
*Criterios:* (1) Antes del despacho, el Coordinador puede cancelar y la reserva se libera `[RN-035]`. (2) **En tránsito, solo el Jefe puede cancelar**, y se genera un movimiento de retorno al origen. (3) La cancelación exige motivo. (4) Queda en la bitácora.

**HU-106** · P0 · Auxiliar · `[F-4]` `[RN-087*]`
**COMO** Auxiliar de Bodega **QUIERO** elegir en pantalla la pieza que estoy ubicando o moviendo, después de escanear **PARA** que el sistema sepa exactamente qué pieza cambió de lugar aunque haya varias del mismo lote en el mismo estante.
*Criterios:* (1) Tras escanear el QR del SKU + Lote, el sistema muestra las piezas de ese lote y el Auxiliar selecciona la que mueve `[F-4]`. (2) Con varias piezas del mismo lote en la ubicación de origen, la ubicación actúa como filtro de verificación: solo se ofrecen las piezas que el sistema registra allí. (3) No se confirma un movimiento sin pieza seleccionada `[RN-087*]`. (4) Aplica al movimiento interno y a la primera ubicación desde recepción `[RN-082*]`. (5) El movimiento queda en el kardex con la pieza. (6) La existencia total no cambia `[RN-026]`.

**HU-111** · P1 · Jefe · `[RN-028]` `[DEC-06]`
**COMO** Jefe de Bodega **QUIERO** que un movimiento interno interrumpido quede en tránsito y se me avise si tarda demasiado **PARA** no perder el rastro de la mercancía que quedó a medio camino.
*Criterios:* (1) Un movimiento interno que se inicia y no se cierra queda en estado en tránsito `[RN-028]`. (2) La existencia en tránsito no está disponible ni en el origen ni en el destino. (3) Si el tiempo en tránsito supera el máximo configurado, el sistema genera una alerta al Jefe. (4) Los movimientos en tránsito se listan en el cierre de la jornada `[PN-14]`.

---

## M-10 · Ajustes de Inventario

**HU-052** · P0 · Coordinador · `[MON §8.2]`
**COMO** Coordinador de Bodega **QUIERO** solicitar un ajuste cuando lo que hay no coincide con lo que dice el sistema **PARA** que el registro refleje la realidad, dejando constancia de por qué.
*Criterios:* (1) Se ingresa la existencia física observada; el sistema calcula la diferencia. (2) `[RN-029]` **El motivo tipificado es obligatorio; el texto libre no lo sustituye.** (3) Se puede adjuntar observación y evidencia. (4) La solicitud queda pendiente de aprobación. (5) La existencia no cambia hasta la aprobación.

**HU-053** · P0 · Jefe / Administrador · `[RN-023]`
**COMO** Jefe de Bodega **QUIERO** aprobar o rechazar los ajustes solicitados **PARA** que nadie modifique el inventario por su cuenta.
*Criterios:* (1) La pantalla muestra unidad, diferencia, motivo, solicitante y evidencia. (2) `[RN-023]` **El sistema impide aprobar un ajuste que uno mismo solicitó**, escalando al nivel superior. (3) El rechazo exige justificación. (4) Al aprobar, se genera el movimiento y cambia la existencia. (5) El solicitante es notificado del resultado.

**HU-054** · P0 · Administrador · `[RN-024]`
**COMO** Administrador **QUIERO** que los ajustes grandes requieran mi aprobación **PARA** mantener control sobre los cambios de inventario de mayor impacto.
*Criterios:* (1) El umbral que separa ajuste menor de mayor es configurable `[RN-024]`. (2) Bajo el umbral, aprueba el Jefe. (3) Sobre el umbral, aprueba el Administrador. (4) El sistema enruta automáticamente. (5) El umbral aplicado queda registrado en el ajuste.

**HU-055** · P0 · Todos · `[RN-009]`
**COMO** Jefe de Bodega **QUIERO** que ningún ajuste pueda dejar la existencia en negativo **PARA** que el inventario nunca muestre una cifra imposible.
*Criterios:* (1) `[RN-009]` **El sistema rechaza todo ajuste que resulte en existencia negativa, sin excepción ni autorización posible.** (2) El mensaje explica la existencia actual y la diferencia solicitada. (3) El rechazo queda registrado. (4) Esta regla **no es configurable**.

**HU-056** · P1 · Jefe / Auditor · `[RN-037]` `[DC-07]`
**COMO** Jefe de Bodega **QUIERO** que el sistema me avise si una misma referencia se ajusta demasiadas veces **PARA** detectar un problema de proceso o algo peor.
*Criterios:* (1) El sistema cuenta ajustes por unidad de inventario en una ventana configurable `[RN-037]`. (2) Al superar el umbral, genera alerta dirigida al Jefe y al Auditor. (3) La alerta lista los ajustes involucrados con solicitante y aprobador. (4) `[DC-07]` **La detección es por regla y umbral, no por modelo predictivo.**

**HU-057** · P1 · Auditor / Jefe · `[MON §7.1]`
**COMO** Auditor **QUIERO** consultar todos los ajustes de un período con su motivo, solicitante y aprobador **PARA** verificar que cada modificación del inventario está justificada.
*Criterios:* (1) Filtro por período, motivo, solicitante, aprobador y referencia. (2) Muestra cantidad ajustada, sentido y evidencia adjunta. (3) Permite abrir el kardex de la unidad afectada. (4) Identifica ajustes sin evidencia cuando el motivo la exigía. (5) Exportable.

---

## M-11 · Conteos

**HU-058** · P1 · Coordinador · `[NUEVO]` `[D-05]`
**COMO** Coordinador de Bodega **QUIERO** programar un conteo de unas cuantas ubicaciones **PARA** verificar el inventario sin tener que parar la bodega.
*Criterios:* (1) El ámbito se define por ubicaciones, referencias o categorías. (2) `[D-05]` **La operación de la bodega no se bloquea durante un conteo cíclico.** (3) El sistema congela la existencia teórica del ámbito `[RN-039]`. (4) Genera tareas y las asigna. (5) El conteo queda en estado en ejecución.

**HU-059** · P1 · Auxiliar · `[RN-040]`
**COMO** Auxiliar de Bodega **QUIERO** contar lo que hay en una ubicación sin que el sistema me diga antes cuánto debería haber **PARA** que mi conteo sea real y no una confirmación de lo que ya dice el sistema.
*Criterios:* (1) `[RN-040]` **La cantidad esperada no se muestra al contador antes de registrar su conteo, en ninguna circunstancia.** (2) El Auxiliar escanea la ubicación e ingresa lo contado. (3) Después de registrar, tampoco se le muestra la diferencia. (4) Puede corregir su propio registro antes de confirmar la tarea.

**HU-060** · P1 · Sistema / Coordinador · `[RN-039]`
**COMO** Coordinador de Bodega **QUIERO** que los movimientos que ocurran durante el conteo no alteren la base de comparación **PARA** que la diferencia detectada sea real.
*Criterios:* (1) `[RN-039]` **La existencia teórica congelada no cambia por movimientos posteriores al congelamiento.** (2) Los movimientos ocurridos durante el conteo se listan en la conciliación. (3) El Coordinador puede ver qué movimientos afectaron el ámbito. (4) La conciliación los considera antes de generar ajustes.

**HU-061** · P1 · Coordinador / Jefe · `[RN-041]`
**COMO** Coordinador de Bodega **QUIERO** que una diferencia grande obligue a un segundo conteo por otra persona **PARA** descartar un error de quien contó.
*Criterios:* (1) El umbral de tolerancia es configurable `[RN-041]`. (2) Al superarlo, el sistema genera automáticamente una tarea de segundo conteo. (3) `[RN-041]` **El segundo conteo lo ejecuta obligatoriamente una persona distinta a la primera.** (4) Si el segundo también difiere, escala al Jefe. (5) Ambos conteos quedan registrados.

**HU-062** · P1 · Jefe · `[RN-042]`
**COMO** Jefe de Bodega **QUIERO** revisar las diferencias y decidir qué se ajusta antes de cerrar el conteo **PARA** que el inventario no se modifique automáticamente sin criterio.
*Criterios:* (1) `[RN-042]` **Solo el Jefe cierra un conteo.** (2) Quien ejecutó el conteo no puede cerrarlo `[RN-041]`. (3) El Jefe ve el consolidado de diferencias por línea. (4) Puede decidir ajustar, no ajustar o recontar por línea. (5) Las líneas ajustadas generan ajustes con motivo derivado del conteo. (6) Un conteo cerrado no se reabre.

**HU-063** · P1 · Jefe · `[RN-045]`
**COMO** Jefe de Bodega **QUIERO** programar un conteo general con bloqueo de movimientos **PARA** obtener una fotografía completa y confiable del inventario.
*Criterios:* (1) Se define fecha y hora de corte. (2) El sistema notifica anticipadamente a todos los usuarios. (3) `[RN-045]` **Al llegar el corte, el registro de movimientos se bloquea.** (4) Solo el Jefe puede autorizar un movimiento de excepción, que queda marcado. (5) Al cerrar, el registro se desbloquea.

**HU-064** · P1 · Jefe · `[RN-046]`
**COMO** Jefe de Bodega **QUIERO** que el sistema no me deje cerrar un conteo general con ubicaciones sin contar **PARA** que la fotografía sea realmente completa.
*Criterios:* (1) `[RN-046]` **El sistema impide el cierre mientras existan ubicaciones del ámbito sin cubrir.** (2) Lista las ubicaciones faltantes. (3) Permite excluir una ubicación solo con justificación registrada. (4) La cobertura alcanzada queda documentada en el conteo.

**HU-065** · P1 · Jefe / Administrador · `[MON §8.2]`
**COMO** Jefe de Bodega **QUIERO** conocer la exactitud del inventario después de cada conteo **PARA** demostrar si estamos mejorando.
*Criterios:* (1) Al cerrar, el sistema calcula la exactitud del ámbito contado (KPI-01). (2) La expresa como porcentaje de líneas conformes sobre líneas contadas. (3) La almacena históricamente para comparar entre conteos. (4) `[MON §8.2]` **Este es el indicador con el que el proyecto demostrará su impacto.** (5) Es exportable para la herramienta analítica `[DC-06]`.

**HU-066** · P2 · Coordinador · `[NUEVO]`
**COMO** Coordinador de Bodega **QUIERO** reasignar una tarea de conteo cuando el auxiliar asignado no está **PARA** que el conteo no se detenga.
*Criterios:* (1) La tarea se reasigna a otro usuario habilitado. (2) Ambos responsables quedan registrados. (3) Si había un conteo parcial, se conserva y se marca. (4) La reasignación no puede violar la regla del segundo conteo `[RN-041]`.

**HU-109** · P0 · Auxiliar · `[F-5]` `[RN-089*]`
**COMO** Auxiliar de Bodega **QUIERO** contar a mano cada pieza de una ubicación y registrar su cantidad **PARA** que el conteo verifique la realidad pieza por pieza.
*Criterios:* (1) El conteo se hace manualmente, pieza por pieza `[F-5]`. (2) El Auxiliar registra la cantidad de cada pieza contada. (3) `[RN-040]` **La cantidad esperada no se muestra antes ni después de registrar.** (4) La cantidad contada de la unidad de inventario es la suma de sus piezas `[RN-089*]`. (5) El sistema compara lo contado con la existencia congelada y clasifica cada línea como conforme, sobrante o faltante `[RN-039]`.

**HU-112** · P1 · Jefe · `[RN-047]` `[DEC-06]`
**COMO** Jefe de Bodega **QUIERO** que el sistema avise al Administrador y al Auditor cuando la diferencia global de un conteo general sea crítica **PARA** que un conteo con un problema grave no se cierre sin que nadie lo sepa.
*Criterios:* (1) El umbral crítico de diferencia global es un parámetro configurable `[RF-152]`. (2) Si la diferencia global del conteo general lo supera, el sistema notifica al Administrador y al Auditor. (3) El cierre del conteo general queda condicionado a esa notificación `[RN-047]`. (4) La notificación queda en la bitácora.

---

## M-12 · Novedades de Mercancía

**HU-067** · P1 · Auxiliar · `[MON §4]` `[PR-06]`
**COMO** Auxiliar de Bodega **QUIERO** reportar fácilmente que encontré algo raro **PARA** avisar sin que parezca que yo hice algo mal.
*Criterios:* (1) El reporte se abre desde la tablet en pocos pasos `[DC-05]`. (2) El tipo de novedad se selecciona de una lista tipificada. (3) Se puede escanear el identificador o declarar que no existe. (4) Se puede adjuntar fotografía. (5) `[PR-06]` **El sistema no presenta el reporte como una falta del reportante ni lo contabiliza en su contra.**

**HU-068** · P1 · Coordinador · `[NUEVO]`
**COMO** Coordinador de Bodega **QUIERO** recibir y resolver las novedades reportadas **PARA** que los problemas físicos no se queden sin atender.
*Criterios:* (1) Las novedades de su zona llegan a su panel. (2) Puede determinar la acción: ajuste, reidentificación, reubicación o baja. (3) `[RN-060]` Una novedad sobre una unidad con novedad abierta se vincula, no se duplica. (4) La novedad se cierra con constancia de la resolución. (5) `[RN-063]` **No existe la opción de eliminar una novedad.**

**HU-069** · P1 · Jefe · `[RN-059]`
**COMO** Jefe de Bodega **QUIERO** que las novedades sin resolver escalen hacia mí **PARA** que ningún problema quede olvidado.
*Criterios:* (1) El plazo de resolución es configurable `[RN-059]`. (2) Al vencer, la novedad escala al Jefe y genera alerta. (3) El escalamiento queda registrado. (4) El listado de novedades vencidas es consultable.

**HU-070** · P1 · Coordinador / Jefe · `[RN-043]`
**COMO** Coordinador de Bodega **QUIERO** registrar mercancía encontrada que no está en el sistema **PARA** incorporarla sin saltarme los controles.
*Criterios:* (1) `[RN-043]` **La mercancía sin registro no se cuenta ni se usa hasta ser identificada.** (2) Se crea o selecciona la unidad de inventario correspondiente. (3) Se genera un ajuste por sobrante con motivo tipificado. (4) Requiere aprobación del Jefe. (5) Se genera identificador QR y se asigna ubicación.

---

## M-13 · Consulta de Existencia

**HU-071** · P0 · Todos · `[MON §6, §7.2]`
**COMO** Jefe de Bodega **QUIERO** saber en el momento cuánto tengo de una referencia **PARA** responder sin tener que ir a contar ni revisar el cuaderno.
*Criterios:* (1) La consulta por referencia devuelve existencia desglosada por talla, color y lote. (2) Muestra el desglose por estado: disponible, reservado, inmovilizado, en tránsito. (3) Responde dentro del tiempo de RNF-012. (4) `[RN-065]` **La cifra mostrada siempre se deriva del kardex.**

**HU-072** · P0 · Auxiliar · `[DC-08]`
**COMO** Auxiliar de Bodega **QUIERO** escanear una etiqueta y ver de inmediato qué es y cuánto hay **PARA** resolver dudas sin preguntarle a nadie.
*Criterios:* (1) El escaneo devuelve referencia, talla, color, lote, ubicación y existencia. (2) `[PR-04]` **No muestra costo ni valorización.** (3) Si el identificador no se reconoce, ofrece reportar novedad. (4) La consulta no modifica nada.

**HU-073** · P0 · Todos · `[NUEVO]`
**COMO** Auxiliar de Bodega **QUIERO** buscar dónde está una referencia **PARA** ir directo al lugar en vez de recorrer la bodega.
*Criterios:* (1) La consulta devuelve todas las ubicaciones con existencia de esa referencia y su cantidad. (2) Ordena por cantidad o por zona. (3) Permite filtrar por talla, color y lote. (4) Marca las ubicaciones cuya existencia no está disponible.

**HU-074** · P1 · Jefe / Coordinador · `[NUEVO]`
**COMO** Coordinador de Bodega **QUIERO** consultar todo lo que hay en una ubicación **PARA** saber qué tengo en cada estante antes de asignar mercancía nueva.
*Criterios:* (1) La consulta por ubicación lista todas las unidades de inventario presentes. (2) Muestra la ocupación frente a la capacidad. (3) Indica si la ubicación está sobreocupada. (4) Permite iniciar un movimiento desde la consulta.

**HU-075** · P1 · Jefe / Auditor · `[MON §7.1]`
**COMO** Auditor **QUIERO** consultar cuánta existencia había en una fecha pasada **PARA** verificar el estado del inventario en un momento determinado.
*Criterios:* (1) Se indica fecha y hora de corte. (2) El sistema reconstruye la existencia a partir del kardex `[RN-065]`. (3) El resultado es idéntico si se consulta dos veces la misma fecha. (4) Declara explícitamente la fecha de corte aplicada. (5) Es exportable.

**HU-076** · P2 · Todos · `[MON §8.2 — usabilidad]`
**COMO** Auxiliar de Bodega **QUIERO** buscar escribiendo parte del nombre **PARA** encontrar lo que necesito sin conocer el código exacto.
*Criterios:* (1) La búsqueda acepta texto parcial de referencia o descripción. (2) Devuelve coincidencias aproximadas ordenadas por relevancia. (3) Tolera diferencias de mayúsculas y tildes. (4) Si no hay coincidencias, lo informa claramente en lugar de mostrar una lista vacía.

---

## M-14 · Kardex y Trazabilidad

**HU-077** · P0 · Jefe / Auditor · `[MON §7.1]` `[CD-21]`
**COMO** Auditor **QUIERO** ver la historia completa de una unidad de inventario **PARA** reconstruir qué pasó con ella desde que entró.
*Criterios:* (1) El kardex muestra todos los movimientos en orden cronológico. (2) Cada línea contiene fecha, hora, tipo, cantidad, existencia resultante, ubicación, usuario, motivo y documento. (3) `[CD-21]` **Permite responder las seis preguntas de trazabilidad: qué, cuánto, dónde, quién, cuándo y por qué.** (4) No tiene huecos. (5) Es exportable.

**HU-078** · P0 · Todos los roles · `[RN-012]`
**COMO** Jefe de Bodega **QUIERO** que ningún movimiento pueda borrarse ni editarse **PARA** que la historia del inventario sea confiable.
*Criterios:* (1) `[RN-012]` **No existe función de edición ni de eliminación de un movimiento confirmado, para ningún rol, incluido el Administrador.** (2) Un error se corrige generando un movimiento inverso. (3) Ambos movimientos permanecen visibles en el kardex. (4) La anulación exige motivo y autorización. (5) La anulación queda en la bitácora.

**HU-079** · P1 · Auditor · `[RN-065]`
**COMO** Auditor **QUIERO** verificar que la existencia actual corresponde exactamente a la suma de los movimientos **PARA** confirmar que nadie alteró el inventario por fuera del sistema.
*Criterios:* (1) `[RN-065]` **El sistema verifica que existencia actual = suma algebraica de movimientos del kardex.** (2) Cualquier discrepancia se reporta como hallazgo crítico. (3) La verificación es ejecutable por unidad, por lote o global. (4) El resultado es exportable.

**HU-080** · P1 · Jefe / Auditor · `[MON §7.1]`
**COMO** Jefe de Bodega **QUIERO** ver el kardex de un lote completo **PARA** rastrear un problema de calidad hasta todas las unidades afectadas.
*Criterios:* (1) El kardex de lote consolida los movimientos de todas sus unidades. (2) Muestra en qué ubicaciones estuvo y está. (3) Muestra qué salió, cuándo y con qué motivo. (4) Permite inmovilizar desde la consulta.

**HU-081** · P2 · Auxiliar · `[§2.7]` `[PR-04]`
**COMO** Auxiliar de Bodega **QUIERO** revisar los movimientos que yo registré **PARA** verificar mi propio trabajo del turno.
*Criterios:* (1) `[§2.7]` **El Auxiliar ve únicamente el kardex de las unidades que él movió y de los últimos 30 días.** (2) No ve movimientos de otros usuarios. (3) No ve valorización `[PR-04]`. (4) `[PR-06]` No se le presentan indicadores de error personal.

**HU-110** · P0 · Jefe / Auditor · `[Q-11]` `[CD-21]`
**COMO** Jefe de Bodega **QUIERO** consultar dónde está y qué ha pasado con cada pieza de un lote **PARA** rastrear un rollo o un paquete concreto y no solo el lote completo.
*Criterios:* (1) La consulta de un lote muestra sus piezas con tipo, cantidad actual, ubicación y estado `[Q-11]`. (2) El kardex de una pieza muestra todos sus movimientos en orden cronológico. (3) `[CD-21]` **Permite responder las seis preguntas de trazabilidad: qué, cuánto, dónde, quién, cuándo y por qué.** (4) La trazabilidad por pieza no requiere un QR propio `[DF5-01]`. (5) Responde dentro del tiempo de RNF-012.

---

## M-15 · Alertas y Reglas

**HU-082** · P1 · Jefe / Coordinador · `[MON §3, §7.1]` `[DC-07]`
**COMO** Jefe de Bodega **QUIERO** que el sistema me avise antes de quedarme sin material **PARA** que la producción no se detenga por un faltante.
*Criterios:* (1) La alerta se dispara cuando la existencia disponible baja del mínimo configurado `[HU-013]`. (2) Identifica referencia, existencia actual y umbral. (3) Se dirige al Jefe y al Coordinador de la zona. (4) `[DC-07]` **La detección es por regla y umbral, no por predicción.** (5) Se cierra automáticamente al recuperarse la existencia `[RN-057]`.

**HU-083** · P1 · Jefe · `[MON §3]`
**COMO** Jefe de Bodega **QUIERO** que el sistema me avise cuando tengo demasiado de algo **PARA** no seguir acumulando material que no rota.
*Criterios:* (1) La alerta se dispara al superar el máximo configurado. (2) Muestra la existencia, el umbral y los días sin movimiento de salida. (3) Se dirige al Jefe. (4) Alimenta el reporte de rotación (KPI-16).

**HU-084** · P1 · Jefe / Coordinador · `[RN-058]`
**COMO** Jefe de Bodega **QUIERO** registrar qué hice con cada alerta **PARA** que quede claro que se atendió y cómo.
*Criterios:* (1) Cada alerta se atiende con una acción o se descarta. (2) `[RN-058]` **El descarte exige motivo; sin motivo la alerta no puede cerrarse.** (3) Queda registrado quién la atendió y cuándo. (4) El historial de alertas es consultable y exportable.

**HU-085** · P1 · Jefe / Administrador · `[RN-056]`
**COMO** Administrador **QUIERO** que las alertas críticas sin atender escalen automáticamente **PARA** que un problema grave no se quede esperando.
*Criterios:* (1) El plazo de atención por severidad es configurable `[RN-056]`. (2) Al vencer, la alerta escala al rol superior. (3) El escalamiento genera una notificación adicional. (4) Queda registrado en la bitácora. (5) La alerta original conserva su historial.

**HU-086** · P2 · Jefe / Coordinador · `[RN-055]`
**COMO** Coordinador de Bodega **QUIERO** que el sistema no me llene la pantalla de alertas repetidas **PARA** poder distinguir lo importante.
*Criterios:* (1) `[RN-055]` **Una condición vigente genera una sola alerta activa, no una por evaluación.** (2) Las alertas se agrupan por tipo y severidad. (3) Se ordenan por severidad y antigüedad. (4) El sistema reporta al Administrador los tipos de alerta con frecuencia de disparo anómala, para recalibrar umbrales.

---

## M-16 · Reportes y Exportación Analítica

**HU-087** · P1 · Jefe / Administrador · `[MON §8.2]`
**COMO** Jefe de Bodega **QUIERO** generar el reporte de existencia por referencia, lote y ubicación **PARA** revisar el estado del inventario y compartirlo.
*Criterios:* (1) Filtro por referencia, categoría, lote, ubicación y estado. (2) Muestra existencia total y su desglose por estado. (3) Declara fecha, hora y usuario de generación. (4) Es exportable en formato tabular. (5) `[PR-04]` `[DEC-07]` Ningún reporte muestra costo ni valorización: el MVP no captura costos.

**HU-088** · P1 · Jefe / Auditor · `[MON §8.2]`
**COMO** Auditor **QUIERO** generar el reporte de movimientos de un período **PARA** revisar toda la actividad del inventario de una sola vez.
*Criterios:* (1) Filtro por período, tipo de movimiento, usuario, referencia y motivo. (2) Muestra cada movimiento con todos sus atributos. (3) Totaliza por tipo. (4) Es exportable. (5) La exportación queda en la bitácora `[RN-061]`.

**HU-089** · P1 · Administrador · `[DC-06]`
**COMO** Administrador **QUIERO** que los datos del sistema puedan alimentar nuestra herramienta analítica **PARA** construir allí los tableros que necesitemos.
*Criterios:* (1) El sistema expone los datos de forma estructurada y consistente. (2) `[DC-06]` **Este documento no diseña los tableros analíticos: solo garantiza la disponibilidad de los datos.** (3) La habilitación de la exportación es exclusiva del Administrador. (4) Toda extracción queda en la bitácora. (5) Los datos exportados respetan las restricciones de visibilidad por rol.

**HU-090** · P2 · Jefe · `[NUEVO]`
**COMO** Jefe de Bodega **QUIERO** que ciertos reportes se generen solos cada semana **PARA** no tener que acordarme de pedirlos.
*Criterios:* (1) Se programa reporte, periodicidad y destinatarios. (2) El sistema lo genera y lo pone a disposición del destinatario. (3) La generación programada queda registrada. (4) La programación puede desactivarse.

---

## M-17 · Dashboard Operativo

**HU-091** · P1 · Jefe · `[DC-02]`
**COMO** Jefe de Bodega **QUIERO** ver de un vistazo el estado de la bodega al llegar **PARA** saber qué requiere mi atención hoy.
*Criterios:* (1) Muestra existencia total y desglose por estado. (2) Muestra alertas activas por severidad. (3) Muestra pendientes: recepciones sin confirmar, en tránsito, ajustes por aprobar, conteos abiertos, novedades sin resolver. (4) Muestra la exactitud vigente (KPI-01). (5) Cada elemento navega a su detalle.

**HU-092** · P1 · Auxiliar · `[MON §8.2]` `[PR-06]`
**COMO** Auxiliar de Bodega **QUIERO** ver mis tareas del turno en orden **PARA** saber qué hacer sin que nadie tenga que decírmelo.
*Criterios:* (1) `[§2.7]` **El Auxiliar ve su panel de tareas, no el dashboard operativo.** (2) Las tareas se ordenan por prioridad. (3) Cada tarea indica qué, dónde y cuánto. (4) La tarea se cierra al confirmarse el movimiento, no por declaración. (5) `[PR-06]` **El panel no muestra indicadores de desempeño individual.**

**HU-093** · P2 · Coordinador · `[§2.7]`
**COMO** Coordinador de Bodega **QUIERO** ver el estado de mi zona **PARA** gestionar mi equipo sin distraerme con lo que no me corresponde.
*Criterios:* (1) `[§2.7]` **El dashboard del Coordinador se restringe a sus zonas asignadas.** (2) Muestra tareas de su equipo, alertas de su zona y ocupación de sus ubicaciones. (3) No muestra valorización `[PR-04]`. (4) Permite reasignar tareas.

---

## M-18 · Auditoría y Bitácora

**HU-094** · P1 · Auditor / Administrador · `[RN-061]`
**COMO** Auditor **QUIERO** consultar el registro de todo lo que pasó en el sistema **PARA** verificar que las cosas se hicieron como debían.
*Criterios:* (1) La bitácora registra accesos, cambios de configuración, cambios de rol, aprobaciones, rechazos, anulaciones y exportaciones. (2) Filtro por usuario, fecha, tipo de evento y módulo. (3) `[RN-061]` **La bitácora no es editable ni borrable por ningún rol, incluido el Administrador.** (4) Toda discontinuidad detectada es un hallazgo crítico. (5) Es exportable.

**HU-095** · P1 · Auditor · `[PR-02]`
**COMO** Auditor **QUIERO** poder consultar absolutamente todo sin poder modificar nada **PARA** que mi revisión sea independiente y nadie dude de ella.
*Criterios:* (1) `[PR-02]` **El Auditor tiene lectura completa sobre todo el sistema.** (2) `[PR-02]` **El Auditor no puede ejecutar ninguna operación de escritura sobre el inventario, ni siquiera por configuración.** (3) Las funciones de escritura no se le presentan. (4) Todo intento de escritura se rechaza y se registra.

**HU-096** · P1 · Auditor · `[RN-064]`
**COMO** Auditor **QUIERO** dejar registradas mis observaciones **PARA** que quede constancia de mis hallazgos sin alterar el inventario.
*Criterios:* (1) La observación se asocia a un movimiento, unidad, período o usuario. (2) `[RN-064]` **La observación se almacena en un registro separado y no altera el estado del inventario.** (3) Es consultable por el Administrador y el Jefe. (4) No se elimina; el Administrador o el Jefe la cierra con su respuesta `[DEC-04]`.

**HU-097** · P1 · Auditor · `[RN-023]` `[PR-01]`
**COMO** Auditor **QUIERO** detectar si alguien aprobó su propia solicitud **PARA** confirmar que la segregación de funciones se está cumpliendo.
*Criterios:* (1) El sistema reporta cualquier caso donde solicitante y aprobador coincidan. (2) `[RN-023]` **Si aparece algún caso, es un hallazgo crítico**, porque la regla debió impedirlo. (3) El reporte cubre ajustes, salidas y conteos. (4) Es exportable.

---

## M-19 · Parámetros y Configuración

**HU-098** · P0 · Administrador · `[CD-46]`
**COMO** Administrador **QUIERO** configurar los umbrales del sistema **PARA** adaptarlo a cómo trabaja realmente nuestra bodega.
*Criterios:* (1) Se configuran: umbral de ajuste menor/mayor, tolerancia de conteo, tiempo máximo en tránsito, plazos de vencimiento, umbral de autorización del Coordinador. (2) El sistema valida rangos admisibles. (3) `[RN-061]` **Todo cambio queda en la bitácora, con valor anterior y nuevo.** (4) El cambio surte efecto inmediato sobre las evaluaciones futuras, no retroactivamente.

**HU-099** · P0 · Administrador · `[CD-36]`
**COMO** Administrador **QUIERO** mantener la lista de motivos tipificados **PARA** que las razones de ajuste y salida sean consistentes y comparables.
*Criterios:* (1) Se administran motivos por tipo de operación. (2) Se indica si el motivo exige evidencia adjunta. (3) `[RN-063]` **Un motivo en uso no se elimina, se desactiva.** (4) Un motivo desactivado no aparece en nuevas operaciones pero sí en el histórico. (5) El texto libre nunca sustituye al motivo tipificado `[RN-029]`.

**HU-100** · P1 · Administrador · `[NUEVO]`
**COMO** Administrador **QUIERO** que el sistema me impida configurar algo que rompa sus controles **PARA** no debilitar por accidente la seguridad del inventario.
*Criterios:* (1) Las reglas estructurales del Cap. 9 marcadas como no configurables **no aparecen como parametrizables**. (2) Entre ellas: prohibición de existencia negativa `[RN-009]`, inmutabilidad del kardex `[RN-012]`, prohibición de aprobar la propia solicitud `[RN-023]`, restricción de escritura del Auditor `[PR-02]`. (3) El intento de eludirlas se rechaza y se registra.

---

## M-20 · Notificaciones y Tareas

**HU-101** · P1 · Auxiliar · `[DC-05]`
**COMO** Auxiliar de Bodega **QUIERO** recibir mis tareas en la tablet **PARA** trabajar sin depender de que alguien venga a decirme qué hacer.
*Criterios:* (1) Las tareas asignadas aparecen en su panel. (2) Cada tarea indica tipo, referencia, cantidad y ubicación. (3) `[DC-05]` **Las notificaciones viven dentro del sistema web; no hay aplicación móvil nativa.** (4) La tarea se cierra al confirmarse el movimiento asociado. (5) Las tareas no vistas se destacan.

**HU-102** · P1 · Jefe / Administrador · `[NUEVO]`
**COMO** Jefe de Bodega **QUIERO** que me lleguen las solicitudes que requieren mi aprobación **PARA** no ser el cuello de botella de la operación.
*Criterios:* (1) Las solicitudes de ajuste y salida pendientes aparecen en su panel. (2) Se ordenan por antigüedad y monto. (3) El solicitante es notificado del resultado. (4) Las solicitudes sin resolver escalan por plazo `[RN-038]`.

**HU-103** · P2 · Coordinador · `[NUEVO]`
**COMO** Coordinador de Bodega **QUIERO** reasignar tareas entre mis auxiliares **PARA** equilibrar la carga del turno.
*Criterios:* (1) La reasignación se hace desde el panel del Coordinador. (2) **Ambos responsables quedan registrados.** (3) El nuevo responsable es notificado. (4) La reasignación no puede violar la regla del segundo conteo `[RN-041]`.

**HU-113** · P1 · Coordinador / Jefe · `[PN-14]` `[DEC-05]`
**COMO** Coordinador de Bodega **QUIERO** ver al cierre de la jornada qué quedó pendiente y traspasarlo explícitamente al turno siguiente **PARA** que nada quede oculto ni sin responsable.
*Criterios:* (1) El sistema consolida los movimientos de la jornada. (2) Lista las recepciones sin confirmar, los movimientos en tránsito, las tareas de conteo abiertas, los ajustes sin resolver, las novedades sin atender y las alertas activas. (3) Lo que no se resuelve en el turno se traspasa explícitamente al turno siguiente. (4) El cierre queda registrado con quién lo ejecutó `[PR-05]`. (5) El Jefe ve el resumen de la jornada.

**HU-114** · P1 · Jefe · `[PN-14]` `[RN-054]` `[DEC-05]`
**COMO** Jefe de Bodega **QUIERO** que el sistema no deje cerrar la jornada con registros sin sincronizar y me avise si no se cerró **PARA** que el cierre refleje siempre lo que realmente pasó.
*Criterios:* (1) El sistema impide el cierre mientras haya registros sin sincronizar `[RN-054]`. (2) Un cierre no ejecutado se registra como omisión. (3) El Jefe recibe una alerta al día siguiente por el cierre omitido. (4) Una diferencia significativa en el consolidado genera una alerta antes de permitir el cierre.

---

# CAPÍTULO 7 — REQUISITOS FUNCIONALES

> **184 requisitos funcionales**, numerados RF-001 a RF-184 y agrupados por módulo. Cada uno declara prioridad, actor, módulo y dependencias. La columna Origen mantiene la trazabilidad exigida.
>
> **Prioridad:** P0 crítico · P1 alto · P2 medio · P3 bajo (ver §0.4).
> **Dependencias:** requisitos, reglas o módulos que deben existir para que este requisito tenga sentido.

## 7.1 Resumen por módulo

| Módulo | RF | Rango | P0 | P1 | P2 | P3 |
|---|:--:|---|:--:|:--:|:--:|:--:|
| M-01 Acceso | 7 | RF-001–007 | 4 | 2 | 1 | 0 |
| M-02 Usuarios y Roles | 8 | RF-008–015 | 4 | 3 | 1 | 0 |
| M-03 Catálogo | 10 | RF-016–025 | 5 | 3 | 2 | 0 |
| M-04 Lotes | 6 | RF-026–031 | 3 | 2 | 1 | 0 |
| M-05 Estructura de Bodega | 9 | RF-032–039, RF-172 | 4 | 4 | 1 | 0 |
| M-06 Identificación QR | 9 | RF-040–047, RF-179 | 4 | 4 | 1 | 0 |
| M-07 Entradas | 17 | RF-048–060, RF-163–165, RF-180 | 9 | 6 | 2 | 0 |
| M-08 Salidas | 14 | RF-061–071, RF-167–168, RF-176 | 8 | 5 | 1 | 0 |
| M-09 Movimientos y Transferencias | 13 | RF-072–082, RF-166, RF-173 | 6 | 6 | 1 | 0 |
| M-10 Ajustes | 10 | RF-083–092 | 6 | 3 | 1 | 0 |
| M-11 Conteos | 15 | RF-093–105, RF-169, RF-175 | 4 | 9 | 2 | 0 |
| M-12 Novedades | 8 | RF-106–111, RF-174, RF-177 | 1 | 6 | 1 | 0 |
| M-13 Consulta de Existencia | 9 | RF-112–119, RF-171 | 6 | 2 | 1 | 0 |
| M-14 Kardex | 9 | RF-120–126, RF-170, RF-178 | 6 | 3 | 0 | 0 |
| M-15 Alertas | 7 | RF-127–133 | 1 | 5 | 1 | 0 |
| M-16 Reportes | 7 | RF-134–140 | 1 | 4 | 2 | 0 |
| M-17 Dashboard | 4 | RF-141–144 | 0 | 3 | 1 | 0 |
| M-18 Auditoría | 7 | RF-145–151 | 3 | 4 | 0 | 0 |
| M-19 Parámetros | 7 | RF-152–157, RF-181 | 4 | 2 | 1 | 0 |
| M-20 Tareas | 8 | RF-158–162, RF-182–184 | 1 | 6 | 1 | 0 |
| **Total** | **184** | | **80** | **82** | **22** | **0** |

---

## M-01 · Acceso y Autenticación

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-001 | El sistema debe autenticar a cada usuario mediante credencial individual antes de permitir cualquier operación | P0 | Todos | M-02 | `[PR-05]` |
| RF-002 | El sistema no debe admitir cuentas genéricas, compartidas ni acceso anónimo a ninguna función | P0 | — | RF-001 | `[PR-05]` |
| RF-003 | El sistema debe registrar en la bitácora todo acceso exitoso y todo intento fallido, con fecha, hora y origen | P0 | — | M-18 | `[NUEVO]` |
| RF-004 | El sistema debe bloquear la cuenta tras el número configurado de intentos fallidos consecutivos y notificar al Administrador | P0 | — | RF-003, M-19 | `[NUEVO]` |
| RF-005 | El sistema debe cerrar la sesión automáticamente tras el tiempo de inactividad configurado, avisando previamente al usuario | P1 | Todos | M-19 | `[DC-05]` |
| RF-006 | El sistema debe permitir al usuario cambiar su propia contraseña, exigiendo la actual y aplicando la política mínima configurada | P1 | Todos | RF-001 | `[NUEVO]` |
| RF-007 | El sistema debe permitir al Administrador restablecer el acceso de una cuenta bloqueada sin revelar jamás la contraseña anterior | P2 | Administrador | RF-004 | `[NUEVO]` |

## M-02 · Usuarios y Roles

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-008 | El sistema debe permitir al Administrador crear usuarios con datos de identificación | P0 | Administrador | M-01 | `[DC-04]` |
| RF-009 | El sistema debe ofrecer exclusivamente los cinco roles oficiales y **no debe permitir crear roles adicionales** | P0 | Administrador | RF-008 | `[DC-04]` |
| RF-010 | El sistema debe asignar exactamente un rol activo por usuario | P0 | Administrador | RF-009 | `[DC-04]` |
| RF-011 | El sistema debe permitir desactivar y reactivar usuarios, **sin ofrecer nunca la eliminación** | P0 | Administrador | RN-063 | `[RN-063]` |
| RF-012 | El sistema debe conservar íntegros los movimientos históricos de un usuario desactivado, mostrando su identidad | P1 | — | RF-011, M-14 | `[MON §7.1]` |
| RF-013 | El sistema debe impedir desactivar o cambiar de rol al último Administrador activo | P1 | Administrador | RF-011 | `[RN-011]` |
| RF-014 | El sistema debe permitir asignar bodega y zonas de ámbito a cada usuario, y filtrar consultas y tareas por ese ámbito | P1 | Administrador | M-05 | `[NUEVO]` |
| RF-015 | El sistema debe registrar todo cambio de rol y de estado de usuario en la bitácora, con valor anterior y nuevo | P2 | — | M-18 | `[NUEVO]` |

## M-03 · Catálogo de Referencias

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-016 | El sistema debe permitir crear referencias con código único, descripción y categoría | P0 | Admin / Jefe | — | `[NUEVO]` `[D-01]` |
| RF-017 | El sistema debe rechazar la creación de una referencia con código ya existente | P0 | — | RF-016 | `[RN-002]` |
| RF-018 | El sistema debe permitir asociar a cada referencia su conjunto aplicable de tallas y de colores | P0 | Admin / Jefe | RF-016 | `[NUEVO]` `[D-01]` |
| RF-019 | El sistema debe generar automáticamente los SKU resultantes de la combinación referencia + talla + color | P0 | — | RF-018 | `[CD-05]` |
| RF-020 | El sistema debe permitir asignar una unidad de medida por referencia e **impedir su cambio si existen movimientos** | P0 | Admin / Jefe | M-14 | `[RN-004]` |
| RF-021 | El sistema debe permitir desactivar referencias y **rechazar la desactivación si la existencia es distinta de cero** | P1 | Admin / Jefe | M-13 | `[RN-010]` |
| RF-022 | El sistema debe permitir definir existencia mínima y máxima por SKU, validando que el mínimo no supere al máximo | P1 | Admin / Jefe | RF-019 | `[MON §3, §7.1]` |
| RF-023 | El sistema debe listar los SKU sin umbrales configurados como pendientes de parametrización | P2 | Admin / Jefe | RF-022 | `[NUEVO]` |
| RF-024 | El sistema debe permitir la carga masiva del catálogo inicial, validando previamente y reportando errores por línea | P1 | Administrador | RF-016 | `[NUEVO]` |
| RF-025 | El sistema debe permitir administrar categorías y asociarlas a una zona preferente para asignación automática | P2 | Admin / Jefe | M-05 | `[NUEVO]` |

## M-04 · Gestión de Lotes

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-026 | El sistema debe crear o asociar un lote al confirmar toda entrada, registrando origen y fecha de ingreso | P0 | Coordinador | M-07 | `[MON §7.1]` |
| RF-027 | El sistema debe garantizar que ninguna existencia quede sin lote asociado | P0 | — | RF-026 | `[MON §7.1]` |
| RF-028 | El sistema debe garantizar la unicidad del código de lote dentro de su SKU | P0 | — | RF-026 | `[RN-014]` |
| RF-029 | El sistema debe permitir consultar la distribución de un lote en todas sus ubicaciones, con cantidad y estado | P1 | Jefe / Coord. | M-13 | `[MON §7.1]` |
| RF-030 | El sistema debe permitir inmovilizar y liberar un lote completo, afectando toda su existencia en todas sus ubicaciones | P1 | Jefe / Admin | RN-036 | `[RN-036]` |
| RF-031 | El sistema debe permitir listar lotes por antigüedad, mostrando días en bodega y destacando los que superan el umbral | P2 | Jefe | RF-026, M-19 | `[NUEVO]` |

## M-05 · Estructura de Bodega

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-032 | El sistema debe permitir crear bodegas, zonas con tipo asignado y ubicaciones dentro de zona | P0 | Administrador | — | `[NUEVO]` |
| RF-033 | El sistema debe garantizar la unicidad del código de ubicación dentro de su bodega | P0 | — | RF-032 | `[RN-014]` |
| RF-034 | El sistema debe exigir la existencia de al menos una zona de recepción por bodega | P0 | Administrador | RF-032 | `[RN-019]` |
| RF-035 | El sistema debe garantizar que toda existencia disponible resida en una ubicación identificada | P0 | — | RF-032, M-13 | `[RN-019]` |
| RF-036 | El sistema debe permitir definir la capacidad de cada ubicación y usarla al proponer destinos | P1 | Administrador | RF-032 | `[RN-021]` |
| RF-037 | El sistema debe permitir desactivar ubicaciones y **rechazar la desactivación si tienen existencia** | P1 | Administrador | M-13 | `[RN-013]` |
| RF-038 | El sistema debe permitir asignar un Coordinador responsable por zona y dirigir a él las alertas de esa zona | P1 | Administrador | M-02, M-15 | `[NUEVO]` |
| RF-039 | El sistema debe permitir configurar los criterios de asignación automática de ubicación y su orden de aplicación | P2 | Administrador | M-19 | `[NUEVO]` |
| RF-172 | El sistema debe registrar como información operativa la desviación entre la ubicación propuesta y la confirmada y notificar al Coordinador, sin imputarla al Auxiliar | P1 | — | RF-072 | `[RN-022]` `[DEC-06]` |

## M-06 · Identificación QR

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-040 | El sistema debe generar un identificador QR único por SKU + Lote (no por ubicación) | P0 | Coordinador | M-07 | `[DC-08]` `[DF5-01]` |
| RF-041 | El sistema debe garantizar que **ningún identificador se repita jamás, ni tras su anulación** | P0 | — | RF-040 | `[RN-016]` |
| RF-042 | El sistema debe permitir el escaneo de identificadores desde tablet y resolverlos a su SKU + Lote y, junto con la ubicación, a la unidad de inventario | P0 | Auxiliar | `[DC-05]` | `[DC-08]` `[DF5-01]` |
| RF-043 | El sistema debe generar un identificador QR propio para cada ubicación, distinguible del de mercancía | P0 | Administrador | M-05 | `[NUEVO]` |
| RF-044 | El sistema debe permitir la impresión individual y por lote de impresión, incluyendo información legible de respaldo | P1 | Coordinador | RF-040 | `[NUEVO]` |
| RF-045 | El sistema debe permitir la reimpresión con motivo obligatorio, **conservando el mismo QR y sin crear una nueva identidad** | P1 | Coord. / Aux. | M-14 | `[RN-018]` `[Q-09]` |
| RF-046 | El sistema debe marcar como reemplazado el identificador sustituido, **sin eliminarlo**, y conservar el historial consultable | P1 | — | RF-045 | `[RN-018]` |
| RF-047 | El sistema debe permitir asociar un identificador secundario de código de barras, **habilitado solo para consulta, nunca para escritura** | P2 | Coordinador | RF-040 | `[DC-08]` `[RN-017]` |
| RF-179 | El sistema debe registrar en cada movimiento si la identificación se hizo por escaneo o por selección manual | P1 | — | RF-042, RF-120 | `[KPI-07]` `[DEC-06]` |

## M-07 · Entradas y Recepción

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-048 | El sistema debe permitir crear documentos de entrada con origen, fecha esperada y líneas de referencia, talla, color y cantidad | P0 | Coordinador | M-03 | `[MON §8.2]` |
| RF-049 | El documento de entrada **no debe solicitar precio, condiciones comerciales ni datos de orden de compra** | P0 | — | RF-048 | `[DC-03]` |
| RF-050 | El sistema debe admitir en el documento de entrada únicamente referencias activas del catálogo | P0 | — | RF-021 | `[RN-002]` |
| RF-051 | El sistema debe advertir de posible duplicado cuando exista otro documento con mismo origen, referencia y fecha | P2 | Coordinador | RF-048 | `[RN-003]` |
| RF-052 | El sistema debe permitir registrar la recepción física por línea desde tablet, en el punto de recepción | P0 | Auxiliar | `[DC-05]` | `[MON §3, §8.2]` |
| RF-053 | El sistema debe permitir interrumpir y continuar una recepción, incluso por otro usuario, registrando a ambos | P1 | Auxiliar | RF-052 | `[NUEVO]` |
| RF-054 | El sistema debe comparar automáticamente cantidad recibida contra esperada, línea por línea | P0 | — | RF-052 | `[RN-005]` |
| RF-055 | El sistema debe registrar faltante de recepción y notificar al Jefe cuando lo recibido sea menor que lo esperado | P1 | — | RF-054, M-20 | `[RN-006]` |
| RF-056 | El sistema debe **exigir autorización del Jefe antes de confirmar** una entrada con sobrante | P0 | Jefe | RF-054 | `[RN-007]` |
| RF-057 | El sistema debe **impedir que quien registró la recepción física confirme la misma entrada** | P0 | — | RF-052, PR-01 | `[PR-01]` |
| RF-058 | El sistema debe generar el movimiento de entrada en el kardex e incrementar la existencia al confirmar | P0 | — | M-14 | `[MON §7.1]` |
| RF-059 | El sistema debe permitir registrar mercancía dañada por separado, **impidiendo su ingreso como disponible** | P1 | Auxiliar | M-12, CD-22 | `[RN-008]` |
| RF-060 | El sistema debe permitir consultar el historial de entradas con filtro por período, origen, estado y referencia, y exportarlo | P2 | Coord. / Jefe | M-16 | `[NUEVO]` |
| RF-163 | El sistema debe permitir registrar cada pieza recibida —rollo, paquete o bolsa— con su tipo y su cantidad propia, dentro de una línea de entrada | P0 | Auxiliar | RF-052, CD-49 | `[Q-11]` `[F-1]` `[F-2]` |
| RF-164 | El sistema debe derivar la cantidad recibida de cada línea como la suma de las cantidades de sus piezas y compararla contra la esperada | P0 | — | RF-163, RF-054 | `[RN-085*]` |
| RF-165 | El sistema debe permitir registrar un contenedor o bolsa agrupada como una pieza con su cantidad de unidades, perteneciente a un solo SKU + Lote | P1 | Auxiliar | RF-163 | `[F-6]` |
| RF-180 | El sistema debe registrar el instante de llegada de la mercancía al documento de entrada | P1 | Auxiliar | RF-048 | `[KPI-12]` `[DEC-06]` |

## M-08 · Salidas

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-061 | El sistema debe permitir solicitar salidas indicando referencias, lotes, cantidades y motivo tipificado obligatorio | P0 | Jefe / Coord. | M-19 | `[RN-048]` |
| RF-062 | La salida **no debe solicitar cliente, precio, factura ni documento comercial de despacho** | P0 | — | RF-061 | `[DC-03]` |
| RF-063 | El sistema debe verificar la existencia disponible antes de aceptar una solicitud de salida | P0 | — | M-13 | `[RN-025]` |
| RF-064 | El sistema debe **rechazar toda salida que deje la existencia por debajo de cero, sin excepción ni autorización posible** | P0 | — | RF-063 | `[RN-009]` |
| RF-065 | El sistema debe reservar la existencia al autorizarse la salida, excluyéndola del disponible | P0 | — | CD-20 | `[RN-031]` |
| RF-066 | El sistema debe permitir al Coordinador autorizar salidas por debajo de su umbral configurado, escalando el resto al Jefe | P1 | Coordinador | M-19 | `[RN-030]` |
| RF-067 | El sistema debe generar la tarea de preparación e indicar las ubicaciones de toma según la política configurada | P1 | — | M-20, M-19 | `[RN-049]` |
| RF-068 | El sistema debe **rechazar el escaneo de una unidad que no corresponda a lo solicitado**, explicando la discrepancia | P0 | — | M-06 | `[RN-050]` |
| RF-069 | El sistema debe registrar el movimiento de salida, descontar la existencia y liberar la reserva al confirmarse | P0 | — | M-14 | `[MON §7.1]` |
| RF-070 | El sistema debe **exigir aprobación del Jefe para toda baja por daño, cualquiera sea la cantidad** | P1 | Jefe | RF-061 | `[RN-052]` |
| RF-071 | El sistema debe registrar el retorno de mercancía **como entrada nueva referenciando la salida original, nunca como reversión** | P1 | Coordinador | M-07 | `[RN-053]` |
| RF-167 | El sistema debe, en la preparación de una salida, verificar lo escaneado y **contar cada pieza seleccionada una sola vez** | P0 | Auxiliar | RF-068, RF-163 | `[Q-10]` `[RN-088*]` |
| RF-168 | El sistema debe permitir registrar el corte parcial de una pieza, descontando la cantidad cortada y **conservando la pieza con su remanente**, sin superar la cantidad de la pieza | P0 | Auxiliar | RF-167, RF-069 | `[F-3]` `[RN-086*]` |
| RF-176 | El sistema debe liberar automáticamente la reserva no ejecutada dentro del plazo configurado y alertar al solicitante | P1 | — | RF-065, M-19 | `[RN-051]` `[DEC-06]` |

## M-09 · Movimientos y Transferencias

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-072 | El sistema debe permitir registrar movimientos internos mediante escaneo de mercancía y ubicación destino | P0 | Auxiliar | M-06 | `[DC-08]` |
| RF-073 | El sistema debe garantizar que **un movimiento interno nunca altere la existencia total**, solo su distribución | P0 | — | RF-072 | `[RN-026]` |
| RF-074 | El sistema debe rechazar mover una cantidad superior a la existente en la ubicación origen | P0 | — | M-13 | `[RN-025]` |
| RF-075 | El sistema debe rechazar movimientos cuya ubicación destino coincida con la de origen | P1 | — | RF-072 | `[RN-027]` |
| RF-076 | El sistema debe rechazar como destino toda ubicación inactiva o sin capacidad disponible | P1 | — | M-05 | `[RN-021]` |
| RF-077 | El sistema debe rechazar todo movimiento sobre existencia inmovilizada sin autorización del Jefe | P0 | — | CD-22 | `[RN-036]` |
| RF-078 | El sistema debe permitir crear transferencias entre zonas o bodegas, reservando la existencia en origen | P0 | Coordinador | RF-065 | `[NUEVO]` |
| RF-079 | El sistema debe registrar confirmación de despacho y de recepción por separado, con responsables distintos identificados | P1 | Auxiliar | M-20 | `[NUEVO]` |
| RF-080 | El sistema debe mantener la existencia en tránsito **fuera del disponible tanto en origen como en destino** | P1 | — | RF-079, CD-23 | `[RN-032]` |
| RF-081 | El sistema debe comparar despachado contra recibido, registrando diferencia si es menor y **rechazando la recepción si es mayor** | P1 | — | RF-079 | `[RN-033]` |
| RF-082 | El sistema debe generar alerta al superarse el tiempo máximo en tránsito configurado, y permitir la cancelación con retorno al origen solo por el Jefe | P1 | Jefe | M-15, M-19 | `[RN-034]` `[RN-035]` |
| RF-166 | El sistema debe **exigir la selección de la pieza** en todo movimiento interno y en la primera ubicación, usando la ubicación como filtro de verificación cuando haya varias piezas del mismo lote | P0 | Auxiliar | RF-072, RF-163 | `[F-4]` `[RN-087*]` |
| RF-173 | El sistema debe mantener en tránsito un movimiento interno interrumpido y generar alerta al superar el tiempo máximo configurado | P1 | — | RF-072, M-15 | `[RN-028]` `[DEC-06]` |

## M-10 · Ajustes de Inventario

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-083 | El sistema debe permitir solicitar ajustes ingresando la existencia física observada y calculando la diferencia | P0 | Coordinador | M-13 | `[MON §8.2]` |
| RF-084 | El sistema debe **exigir motivo tipificado obligatorio en todo ajuste; el texto libre no debe sustituirlo** | P0 | — | M-19, CD-36 | `[RN-029]` |
| RF-085 | El sistema debe permitir adjuntar observación y evidencia, y exigir evidencia cuando el motivo así lo determine | P1 | Coordinador | RF-084 | `[RN-029]` |
| RF-086 | El sistema debe clasificar el ajuste como menor o mayor según el umbral configurado y enrutarlo al aprobador correspondiente | P0 | — | M-19 | `[RN-024]` |
| RF-087 | El sistema debe **impedir que un usuario apruebe un ajuste que él mismo solicitó, escalando al nivel superior** | P0 | — | RF-086, PR-01 | `[RN-023]` |
| RF-088 | El sistema debe **rechazar todo ajuste que resulte en existencia negativa**; esta regla **no debe ser configurable** | P0 | — | RF-083 | `[RN-009]` |
| RF-089 | El sistema debe mantener la existencia sin cambios hasta la aprobación, y generar el movimiento solo al aprobarse | P0 | — | M-14 | `[MON §7.1]` |
| RF-090 | El sistema debe exigir justificación al rechazar un ajuste y notificar el resultado al solicitante | P1 | Jefe / Admin | M-20 | `[RN-062]` |
| RF-091 | El sistema debe detectar y alertar patrones de ajuste recurrente sobre una misma unidad dentro de la ventana configurada | P1 | — | M-15, M-19 | `[RN-037]` `[DC-07]` |
| RF-092 | El sistema debe permitir consultar ajustes filtrando por período, motivo, solicitante, aprobador y referencia, y exportarlos | P2 | Auditor / Jefe | M-16 | `[NUEVO]` |

## M-11 · Conteos

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-093 | El sistema debe permitir programar conteos cíclicos definiendo el ámbito por ubicaciones, referencias o categorías | P1 | Coordinador | M-05, M-03 | `[NUEVO]` `[D-05]` |
| RF-094 | El sistema **no debe bloquear la operación de la bodega durante un conteo cíclico** | P0 | — | RF-093 | `[NUEVO]` `[D-05]` |
| RF-095 | El sistema debe congelar la existencia teórica del ámbito al iniciar el conteo | P1 | — | CD-25 | `[RN-039]` |
| RF-096 | El sistema debe garantizar que **la existencia teórica congelada no se altere por movimientos posteriores al congelamiento** | P0 | — | RF-095 | `[RN-039]` |
| RF-097 | El sistema debe generar y asignar tareas de conteo a contadores identificados | P1 | Coordinador | M-20 | `[NUEVO]` |
| RF-098 | El sistema **no debe mostrar al contador la cantidad esperada antes ni después de registrar su conteo** | P0 | — | RF-097 | `[RN-040]` |
| RF-099 | El sistema debe comparar lo contado contra la existencia congelada y clasificar cada línea como conforme, sobrante o faltante | P1 | — | RF-095 | `[MON §8.2]` |
| RF-100 | El sistema debe generar automáticamente un segundo conteo cuando la diferencia supere el umbral de tolerancia | P1 | — | M-19 | `[RN-041]` |
| RF-101 | El sistema debe **exigir que el segundo conteo lo ejecute una persona distinta a la del primero** | P1 | — | RF-100 | `[RN-041]` |
| RF-102 | El sistema debe **permitir el cierre de un conteo únicamente al Jefe, e impedirlo a quien lo ejecutó** | P1 | Jefe | RF-097 | `[RN-041]` `[RN-042]` |
| RF-103 | El sistema debe permitir programar conteos generales con corte, **bloqueando el registro de movimientos** y permitiendo excepciones solo al Jefe | P1 | Jefe | RF-093 | `[RN-045]` |
| RF-104 | El sistema debe **impedir cerrar un conteo general con ubicaciones del ámbito sin cubrir**, admitiendo exclusión solo con justificación registrada | P1 | — | RF-103 | `[RN-046]` |
| RF-105 | El sistema debe calcular la exactitud del ámbito contado al cierre, almacenarla históricamente y exponerla como KPI-01 | P2 | — | M-16, KPI-01 | `[MON §8.2]` |
| RF-169 | El sistema debe permitir contar manualmente pieza por pieza, registrando la cantidad de cada pieza **sin mostrar la esperada** | P0 | Auxiliar | RF-098, RF-163 | `[F-5]` `[RN-089*]` |
| RF-175 | El sistema debe notificar al Administrador y al Auditor y condicionar el cierre de un conteo general cuando la diferencia global supere el umbral crítico configurado | P1 | — | RF-103, M-19 | `[RN-047]` `[DEC-06]` |

## M-12 · Novedades de Mercancía

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-106 | El sistema debe permitir al Auxiliar reportar novedades desde tablet, con tipo tipificado, ubicación y descripción | P1 | Auxiliar | `[DC-05]` | `[MON §4]` |
| RF-107 | El sistema debe permitir escanear el identificador o declarar explícitamente su ausencia, y adjuntar evidencia fotográfica | P1 | Auxiliar | M-06 | `[NUEVO]` |
| RF-108 | El sistema **no debe presentar ni contabilizar la novedad como falta imputable al reportante** | P1 | — | PR-06 | `[MON §4]` `[PR-06]` |
| RF-109 | El sistema debe dirigir la novedad al Coordinador de la zona y permitir su resolución con acción determinada | P1 | Coordinador | M-20 | `[NUEVO]` |
| RF-110 | El sistema debe vincular una novedad nueva a la existente cuando la unidad ya tenga una novedad abierta, **sin duplicarla** | P2 | — | RF-109 | `[RN-060]` |
| RF-111 | El sistema debe **cerrar novedades con constancia de resolución y no ofrecer nunca su eliminación** | P0 | — | RN-063 | `[RN-063]` |
| RF-174 | El sistema debe impedir contar o usar mercancía sin registro hasta su identificación y permitir su incorporación solo mediante ajuste por sobrante con motivo tipificado y aprobación del Jefe | P1 | — | RF-083 | `[RN-043]` `[DEC-06]` |
| RF-177 | El sistema debe escalar al Jefe y alertar las novedades no resueltas dentro del plazo configurado | P1 | — | RF-106, M-19 | `[RN-059]` `[DEC-06]` |

## M-13 · Consulta de Existencia

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-112 | El sistema debe permitir consultar existencia por referencia, SKU, lote, ubicación e identificador escaneado | P0 | Todos | M-14 | `[MON §6, §7.2]` |
| RF-113 | El sistema debe mostrar el desglose de existencia por estado: disponible, reservado, inmovilizado, en tránsito y en recepción | P0 | Todos | CD-44 | `[NUEVO]` |
| RF-114 | El sistema debe derivar **siempre** la existencia mostrada del kardex, sin depender de un valor almacenado de forma independiente | P0 | — | M-14 | `[RN-065]` |
| RF-115 | El sistema debe mostrar la distribución de una referencia entre todas sus ubicaciones, con cantidad por cada una | P0 | Todos | M-05 | `[NUEVO]` |
| RF-116 | El sistema **no debe mostrar costo ni valorización al Coordinador ni al Auxiliar** | P0 | — | PR-04 | `[PR-04]` |
| RF-117 | El sistema debe permitir consultar la existencia histórica a una fecha y hora de corte, reconstruyéndola desde el kardex | P1 | Jefe / Auditor | RF-114 | `[MON §7.1]` |
| RF-118 | El sistema debe ofrecer búsqueda por texto parcial tolerante a mayúsculas y tildes, e informar explícitamente cuando no haya coincidencias | P1 | Todos | — | `[MON §8.2]` |
| RF-119 | El sistema debe garantizar que **ninguna operación de consulta modifique el estado del inventario** | P2 | — | — | `[NUEVO]` |
| RF-171 | El sistema debe permitir consultar las piezas de un lote con su tipo, cantidad actual, ubicación y estado | P0 | Todos | RF-112, RF-163 | `[Q-11]` |

## M-14 · Kardex y Trazabilidad

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-120 | El sistema debe registrar todo movimiento con fecha, hora, tipo, cantidad, existencia resultante, ubicación, usuario, motivo y documento | P0 | — | — | `[MON §7.1]` |
| RF-121 | El sistema debe garantizar que **todo movimiento tenga un usuario atribuible; no deben existir movimientos anónimos** | P0 | — | M-01 | `[PR-05]` |
| RF-122 | El sistema **no debe ofrecer función alguna de edición ni de eliminación de un movimiento confirmado, para ningún rol, incluido el Administrador** | P0 | — | — | `[RN-012]` |
| RF-123 | El sistema debe permitir corregir errores mediante movimiento inverso con motivo y autorización, **conservando ambos movimientos visibles** | P0 | Jefe / Admin | RF-122 | `[CD-34]` |
| RF-124 | El sistema debe permitir consultar el kardex de una unidad de inventario, de un lote y de una ubicación, con filtros por tipo, período, usuario y motivo | P0 | Ver §2.7 | — | `[MON §7.1]` |
| RF-125 | El sistema debe permitir verificar que la existencia actual equivale a la suma algebraica de los movimientos, por unidad, por lote y globalmente | P1 | Auditor | RF-120 | `[RN-065]` |
| RF-126 | El sistema debe restringir la consulta de kardex del Auxiliar a las unidades que él movió y a los últimos 30 días | P1 | — | §2.7 | `[PR-04]` |
| RF-170 | El sistema debe registrar en el kardex la pieza afectada por cada movimiento que la toque | P0 | — | RF-120, RF-163 | `[Q-11]` `[RN-085*]` |
| RF-178 | El sistema debe registrar el instante de inicio y el de confirmación de cada movimiento | P1 | — | RF-120 | `[KPI-05]` `[DEC-06]` |

## M-15 · Alertas y Reglas

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-127 | El sistema debe evaluar de forma continua las condiciones de alerta configuradas y generar la alerta al cumplirse | P1 | — | M-19 | `[DC-07]` |
| RF-128 | El sistema debe generar alertas **exclusivamente por reglas explícitas y umbrales configurados, sin modelos predictivos ni de aprendizaje** | P0 | — | RF-127 | `[DC-07]` |
| RF-129 | El sistema debe asignar a toda alerta un destinatario por rol; **ninguna alerta debe quedar sin responsable** | P1 | — | M-02 | `[NUEVO]` |
| RF-130 | El sistema debe implementar como mínimo los diez tipos de alerta enumerados en PN-11 | P1 | — | Cap. 9 | `[MON §3, §7.1]` |
| RF-131 | El sistema debe **exigir motivo para descartar una alerta e impedir su cierre sin él** | P1 | Jefe / Coord. | — | `[RN-058]` |
| RF-132 | El sistema debe agrupar en una sola alerta activa cada condición vigente, evitando duplicados por reevaluación | P1 | — | RF-127 | `[RN-055]` |
| RF-133 | El sistema debe escalar automáticamente al rol superior las alertas críticas no atendidas en el plazo configurado, y cerrarlas al cesar su condición | P2 | — | M-19, M-20 | `[RN-056]` `[RN-057]` |

## M-16 · Reportes y Exportación Analítica

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-134 | El sistema debe generar reportes de existencia, movimientos, entradas, salidas, ajustes, conteos, alertas y novedades | P1 | Ver §2.7 | M-13, M-14 | `[MON §8.2]` |
| RF-135 | Todo reporte debe declarar su fecha, hora de generación y el usuario que lo generó | P1 | — | RF-134 | `[NUEVO]` |
| RF-136 | El sistema debe calcular los 24 indicadores definidos en el Capítulo 10 | P1 | — | Cap. 10 | `[MON §8.2]` |
| RF-137 | El sistema debe exponer los datos de forma estructurada para consumo de la herramienta analítica externa | P1 | Administrador | `[DC-06]` | `[DC-06]` |
| RF-138 | El sistema **no debe incluir el diseño de tableros analíticos**: la visualización analítica se resuelve en la herramienta externa | P0 | — | RF-137 | `[DC-06]` |
| RF-139 | El sistema debe registrar en la bitácora toda exportación de datos, con usuario, alcance y fecha | P2 | — | M-18 | `[RN-061]` |
| RF-140 | El sistema debe permitir programar la generación periódica de reportes y su puesta a disposición de destinatarios definidos | P2 | Jefe | M-20 | `[NUEVO]` |

## M-17 · Dashboard Operativo

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-141 | El sistema debe presentar un dashboard operativo con existencia, alertas activas, pendientes y exactitud vigente | P1 | Jefe / Admin | M-13, M-15 | `[DC-02]` |
| RF-142 | El sistema debe permitir navegar desde cualquier elemento del dashboard hacia su detalle | P1 | Jefe / Admin | RF-141 | `[NUEVO]` |
| RF-143 | El sistema debe restringir el dashboard del Coordinador a sus zonas asignadas y sin valorización | P1 | Coordinador | §2.7 | `[PR-04]` |
| RF-144 | El sistema debe presentar al Auxiliar únicamente su panel de tareas, **sin indicadores de desempeño individual** | P2 | Auxiliar | M-20, PR-06 | `[PR-06]` |

## M-18 · Auditoría y Bitácora

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-145 | El sistema debe registrar en la bitácora accesos, cambios de configuración, cambios de rol, aprobaciones, rechazos, anulaciones y exportaciones | P0 | — | Todos | `[NUEVO]` |
| RF-146 | El sistema debe garantizar que **la bitácora no sea editable ni borrable por ningún rol, incluido el Administrador** | P0 | — | RF-145 | `[RN-061]` |
| RF-147 | El sistema debe permitir consultar la bitácora con filtros por usuario, fecha, tipo de evento y módulo, y exportarla | P1 | Auditor / Admin | RF-145 | `[NUEVO]` |
| RF-148 | El sistema debe otorgar al rol Auditor **acceso de lectura completo sobre todo el sistema, sin restricción alguna** | P1 | Auditor | M-02 | `[PR-02]` |
| RF-149 | El sistema debe **impedir al rol Auditor toda operación de escritura sobre el inventario, incluso mediante configuración** | P0 | — | RF-148 | `[PR-02]` |
| RF-150 | El sistema debe permitir al Auditor registrar observaciones en un registro separado que **no altere el estado del inventario** | P1 | Auditor | RF-149 | `[RN-064]` |
| RF-151 | El sistema debe reportar como hallazgo crítico toda coincidencia entre solicitante y aprobador, y toda discontinuidad de la bitácora | P1 | Auditor | RF-087 | `[RN-023]` `[RN-061]` |

## M-19 · Parámetros y Configuración

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-152 | El sistema debe permitir al Administrador configurar umbrales de ajuste, tolerancia de conteo, tiempo en tránsito, plazos, umbral de autorización del Coordinador, umbral crítico de diferencia global del conteo general y días sin movimiento, y al Jefe consultarlos sin modificarlos | P0 | Administrador | — | `[CD-46]` `[DEC-04]` `[DEC-06]` |
| RF-153 | El sistema debe validar que los valores configurados estén dentro de rangos admisibles | P0 | — | RF-152 | `[NUEVO]` |
| RF-154 | El sistema debe registrar todo cambio de configuración en la bitácora, con valor anterior y nuevo | P0 | — | M-18 | `[RN-061]` |
| RF-155 | El sistema debe aplicar los cambios de configuración a evaluaciones futuras, **nunca de forma retroactiva** | P1 | — | RF-152 | `[NUEVO]` |
| RF-156 | El sistema debe permitir administrar el catálogo de motivos tipificados por tipo de operación, indicando cuáles exigen evidencia | P0 | Administrador | CD-36 | `[RN-029]` |
| RF-157 | El sistema **no debe exponer como configurables las reglas estructurales** enumeradas en §9.1 | P1 | — | Cap. 9 | `[NUEVO]` |
| RF-181 | El sistema debe permitir registrar el volumen de movimientos de referencia estimado en campo para calcular la adopción | P2 | Administrador | RF-152 | `[KPI-24]` `[DEC-06]` |

## M-20 · Notificaciones y Tareas

| RF | Requisito | Prio | Actor | Depende de | Origen |
|---|---|:--:|---|---|---|
| RF-158 | El sistema debe generar tareas al asignar trabajo de recepción, ubicación, conteo, preparación de salida y transferencia | P1 | — | M-07 a M-11 | `[NUEVO]` |
| RF-159 | El sistema debe presentar a cada usuario su panel de tareas ordenado por prioridad, indicando qué, dónde y cuánto | P1 | Todos | RF-158 | `[DC-05]` |
| RF-160 | El sistema debe cerrar una tarea **por la confirmación del movimiento asociado, nunca por declaración del usuario** | P0 | — | M-14 | `[NUEVO]` |
| RF-161 | El sistema debe permitir reasignar tareas registrando a ambos responsables, **sin violar la regla del segundo conteo** | P1 | Coordinador | RF-101 | `[RN-041]` |
| RF-162 | El sistema **no debe exponer en las notificaciones información fuera del ámbito del destinatario**, y debe operar sin aplicación móvil nativa | P2 | — | PR-04, `[DC-05]` | `[DC-05]` `[PR-04]` |
| RF-182 | El sistema debe consolidar al cierre de la jornada los movimientos y los pendientes: recepciones sin confirmar, movimientos en tránsito, tareas de conteo abiertas, ajustes sin resolver, novedades sin atender y alertas activas | P1 | Coordinador | M-13, M-15 | `[PN-14]` `[DEC-05]` |
| RF-183 | El sistema debe permitir traspasar explícitamente los pendientes al turno siguiente y registrar el cierre con quién lo ejecutó | P1 | Jefe / Coord. | RF-182 | `[PN-14]` `[DEC-05]` |
| RF-184 | El sistema debe impedir el cierre con registros sin sincronizar, registrar como omisión el cierre no ejecutado y alertar ante una diferencia significativa | P1 | — | RF-182 | `[RN-054]` `[DEC-05]` |

---

# CAPÍTULO 8 — REQUISITOS NO FUNCIONALES

> **47 requisitos no funcionales**, clasificados en las nueve categorías exigidas. Cada uno declara criterio de verificación. Los valores numéricos son **objetivos de diseño propuestos**: su calibración definitiva requiere la línea base de la Fase 3 `[AUD C.2.4]`.

## 8.1 Seguridad

| RNF | Requisito | Verificación | Origen |
|---|---|---|---|
| RNF-001 | Toda operación del sistema debe exigir autenticación previa; no debe existir función accesible sin sesión válida | Intento de acceso sin sesión a cada función: todas rechazadas | `[PR-05]` |
| RNF-002 | Las contraseñas deben almacenarse de forma que su valor original no sea recuperable por ningún medio ni por ningún rol | Inspección: ningún proceso, reporte o pantalla expone contraseñas | `[NUEVO]` |
| RNF-003 | El control de acceso debe aplicarse en el momento de ejecutar la operación, no únicamente al presentar la interfaz | Intento de ejecución directa de operación no autorizada: rechazada | `[PR-01]` |
| RNF-004 | La segregación de funciones definida en §2.7 debe ser inviolable por configuración | Recorrido completo de la matriz §2.7 con cada rol | `[PR-01]` `[DC-04]` |
| RNF-005 | El rol Auditor debe carecer de toda capacidad de escritura sobre el inventario, sin excepción posible | Intento de cada operación de escritura con rol Auditor: todas rechazadas | `[PR-02]` |
| RNF-006 | Toda comunicación entre el dispositivo del usuario y el sistema debe estar cifrada | Verificación de transporte cifrado en todas las rutas | `[NUEVO]` |
| RNF-007 | El sistema debe registrar todo intento de operación no autorizada, con usuario, operación y fecha | Provocación de intentos no autorizados y verificación en bitácora | `[NUEVO]` |
| RNF-008 | Los datos de la empresa deben tratarse conforme a la normativa colombiana de protección de datos personales aplicable | Revisión de cumplimiento previa a producción | `[AUD C.2.11]` |

## 8.2 Disponibilidad

| RNF | Requisito | Verificación | Origen |
|---|---|---|---|
| RNF-009 | El sistema debe estar disponible durante la totalidad de la jornada operativa de la bodega | Medición de disponibilidad en ventana operativa durante el piloto | `[NUEVO]` |
| RNF-010 | Ante pérdida de conectividad, el registro de movimientos desde tablet debe retenerse localmente y sincronizarse al restablecerse | Desconexión durante registro y verificación de sincronización posterior | `[RN-054]` `[MON §3]` |
| RNF-011 | El sistema debe impedir el cierre de jornada mientras existan registros sin sincronizar | Intento de cierre con registros pendientes: rechazado | `[RN-054]` |
| RNF-012 | Debe existir respaldo periódico de la información, con procedimiento de restauración probado | Ejecución de una restauración de prueba | `[NUEVO]` |
| RNF-013 | La pérdida máxima de información tolerable ante una falla no debe exceder los movimientos de la última hora | Prueba de recuperación ante falla simulada | `[NUEVO]` |

## 8.3 Rendimiento

| RNF | Requisito | Verificación | Origen |
|---|---|---|---|
| RNF-014 | La consulta de existencia por referencia debe responder en menos de 3 segundos con el volumen esperado de la empresa piloto | Medición con volumen de datos representativo | `[MON §6 — «tiempo real»]` |
| RNF-015 | La resolución de un identificador escaneado debe completarse en menos de 2 segundos | Medición desde escaneo hasta presentación del resultado | `[DC-08]` |
| RNF-016 | El registro de un movimiento debe confirmarse al usuario en menos de 3 segundos | Medición desde confirmación hasta acuse visible | `[MON §8.2 — tiempos de registro]` |
| RNF-017 | La carga del panel de tareas del Auxiliar debe completarse en menos de 3 segundos | Medición en tablet, en condiciones de red de la bodega | `[DC-05]` |
| RNF-018 | La generación de un reporte de período mensual no debe exceder los 30 segundos | Medición con volumen representativo | `[NUEVO]` |
| RNF-019 | El tiempo de registro de un movimiento debe ser **menor que el del método manual actual**, medido contra la línea base | Comparación KPI-05 contra línea base de la Fase 3 | `[MON §8.2]` `[AUD C.2.4]` |

## 8.4 Escalabilidad

| RNF | Requisito | Verificación | Origen |
|---|---|---|---|
| RNF-020 | El sistema debe sostener el volumen de referencias, SKU, ubicaciones y movimientos de una PYME textil sin degradación perceptible | Prueba con volumen proyectado a tres años | `[MON §5]` |
| RNF-021 | El sistema debe admitir la operación simultánea de todos los usuarios de la bodega sin degradación de los tiempos de RNF-014 a RNF-017 | Prueba de concurrencia con el número real de usuarios | `[NUEVO]` |
| RNF-022 | El sistema debe permitir incorporar bodegas y zonas adicionales sin rediseñar la información existente | Alta de una bodega adicional en ambiente de prueba | `[NUEVO]` |
| RNF-023 | El crecimiento del kardex no debe degradar el tiempo de consulta de existencia | Medición con kardex de volumen proyectado a tres años | `[RN-065]` |
| RNF-024 | El sistema debe permitir la adopción escalonada por proceso: operar con entradas y salidas antes de habilitar conteos y transferencias | Verificación de operación con módulos parcialmente habilitados | `[MON §8.2]` `[D-10]` |

## 8.5 Accesibilidad

| RNF | Requisito | Verificación | Origen |
|---|---|---|---|
| RNF-025 | Los elementos táctiles deben tener un tamaño suficiente para ser accionados con precisión en tablet, incluso con guantes de trabajo | Prueba con usuarios reales en condiciones de bodega | `[DC-05]` `[MON §3]` |
| RNF-026 | El contraste de texto y fondo debe permitir la lectura bajo la iluminación real de la bodega | Prueba en el sitio de la empresa piloto | `[NUEVO]` |
| RNF-027 | La información crítica no debe transmitirse únicamente mediante color | Revisión de todas las pantallas operativas | `[NUEVO]` |
| RNF-028 | El tamaño de texto debe ser ajustable sin ruptura del diseño | Prueba con tamaños aumentados | `[NUEVO]` |
| RNF-029 | Los mensajes de error deben estar redactados en lenguaje comprensible para un usuario sin formación técnica, indicando qué hacer | Revisión con usuarios de perfil Auxiliar | `[MON §3, §8.2]` |

## 8.6 Auditoría

| RNF | Requisito | Verificación | Origen |
|---|---|---|---|
| RNF-030 | Toda acción relevante debe quedar registrada con usuario, fecha, hora y detalle suficiente para reconstruirla | Recorrido de operaciones y verificación en bitácora | `[MON §7.1]` |
| RNF-031 | La bitácora y el kardex deben ser inmutables: no debe existir mecanismo alguno de edición ni de borrado | Búsqueda exhaustiva de funciones de escritura sobre ambos registros | `[RN-012]` `[RN-061]` |
| RNF-032 | Debe ser posible reconstruir el estado del inventario a cualquier fecha pasada, con resultado idéntico ante consultas repetidas | Consulta histórica repetida sobre la misma fecha | `[RN-065]` |
| RNF-033 | La información de auditoría debe conservarse durante todo el período de vida del sistema, sin purga automática | Verificación de la política de retención | `[NUEVO]` |
| RNF-034 | La verificación de integridad —existencia igual a suma de movimientos— debe poder ejecutarse a demanda sobre todo el inventario | Ejecución de la verificación global | `[RN-065]` |

## 8.7 Usabilidad

> **Categoría prioritaria.** La monografía documenta que la baja alfabetización digital y la resistencia cultural son las barreras principales de adopción `[MON §3, §4, §8.2]`. Un fallo en esta categoría reproduce el fracaso que el proyecto busca evitar.

| RNF | Requisito | Verificación | Origen |
|---|---|---|---|
| RNF-035 | Un Auxiliar sin experiencia previa debe poder registrar una entrada, una salida y un movimiento interno tras una capacitación breve | Prueba con usuarios reales sin formación previa | `[MON §3, §8.2]` |
| RNF-036 | Las operaciones frecuentes del Auxiliar deben completarse en el mínimo número de pasos posible | Conteo de pasos por operación frecuente | `[MON §8.2]` |
| RNF-037 | Toda operación de registro debe entregar confirmación visible e inequívoca de que quedó guardada | Revisión de cada operación de escritura | `[NUEVO — requisito de confianza del operario]` |
| RNF-038 | El sistema debe explicar por qué rechaza una operación, en lugar de limitarse a impedirla | Revisión de todos los mensajes de rechazo | `[D-07]` `[MON §4]` |
| RNF-039 | El sistema **no debe presentar al operario indicadores de desempeño individual ni comparaciones entre personas** | Revisión de todas las pantallas de rol Auxiliar | `[PR-06]` `[MON §4]` |
| RNF-040 | La terminología de la interfaz debe corresponder a la del Capítulo 4, sin sinónimos ni variantes | Revisión terminológica de toda la interfaz | `[§0.5]` |
| RNF-041 | El sistema debe permitir corregir un registro en curso antes de confirmarlo, sin perder el trabajo ya ingresado | Prueba de corrección previa a confirmación | `[NUEVO]` |

## 8.8 Compatibilidad Tablet

| RNF | Requisito | Verificación | Origen |
|---|---|---|---|
| RNF-042 | El sistema debe ser plenamente operable desde tablet para todas las funciones de los roles Auxiliar y Coordinador | Recorrido completo de sus funciones en tablet | `[DC-05]` |
| RNF-043 | El sistema debe funcionar como aplicación web responsive; **no debe requerir instalación de aplicación móvil nativa** | Verificación de acceso por navegador de tablet sin instalación | `[DC-05]` |
| RNF-044 | La captura de códigos QR debe funcionar con la cámara de la tablet, sin requerir lector externo obligatorio | Prueba de escaneo con cámara de dispositivo estándar | `[DC-08]` `[DC-05]` |
| RNF-045 | La interfaz debe ser operable en orientación vertical y horizontal, sin pérdida de función | Prueba en ambas orientaciones | `[DC-05]` |

## 8.9 Compatibilidad Navegador

| RNF | Requisito | Verificación | Origen |
|---|---|---|---|
| RNF-046 | El sistema debe funcionar en las versiones vigentes de los navegadores de uso mayoritario, en escritorio y en tablet | Prueba en la matriz de navegadores definida | `[DC-05]` |
| RNF-047 | El sistema debe informar explícitamente al usuario cuando su navegador no sea compatible, en lugar de fallar de forma silenciosa | Prueba con navegador no soportado | `[NUEVO]` |

## 8.10 Distribución por categoría

| Categoría | RNF | Rango |
|---|:--:|---|
| Seguridad | 8 | RNF-001 – 008 |
| Disponibilidad | 5 | RNF-009 – 013 |
| Rendimiento | 6 | RNF-014 – 019 |
| Escalabilidad | 5 | RNF-020 – 024 |
| Accesibilidad | 5 | RNF-025 – 029 |
| Auditoría | 5 | RNF-030 – 034 |
| Usabilidad | 7 | RNF-035 – 041 |
| Compatibilidad Tablet | 4 | RNF-042 – 045 |
| Compatibilidad Navegador | 2 | RNF-046 – 047 |
| **Total** | **47** | |

---

# CAPÍTULO 9 — REGLAS DE NEGOCIO

> **68 reglas**, numeradas RN-001 a RN-068. Este capítulo es el **corazón operativo de la «inteligencia» de COLBASOFT** `[DC-07]`: la automatización del producto es exactamente este cuerpo de reglas evaluándose de forma explícita, sin modelos predictivos ni aprendizaje automático.
>
> Cada regla declara si es **estructural** (inviolable, no parametrizable) o **configurable** (su umbral se ajusta en M-19, pero su lógica no se desactiva).

## 9.1 Reglas estructurales — no configurables

`[RF-157]` Las siguientes reglas **no deben exponerse jamás como parametrizables**. Su desactivación destruiría la integridad del inventario o la segregación de funciones. Ningún rol, incluido el Administrador, puede eludirlas.

| RN | Regla | Categoría |
|---|---|---|
| RN-009 | Prohibición de existencia negativa | Stock negativo |
| RN-012 | Inmutabilidad del kardex | Auditoría |
| RN-023 | Prohibición de aprobar la propia solicitud | Ajustes |
| RN-029 | Obligatoriedad de motivo tipificado | Ajustes |
| RN-040 | Ocultamiento de la cantidad esperada al contador | Estados |
| RN-041 | Segundo conteo por persona distinta | Estados |
| RN-061 | Inmutabilidad de la bitácora | Auditoría |
| RN-063 | Eliminación lógica universal | Eliminación lógica |
| RN-065 | Derivación de la existencia desde el kardex | Auditoría |
| RN-001 | Atribución personal de toda acción | Auditoría |

---

## 9.2 Reglas de integridad fundamental

| RN | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-001** | **Toda acción que altere el estado del sistema debe ser atribuible a un usuario identificado.** No existen acciones anónimas, automáticas sin origen ni ejecutadas por cuentas compartidas. Las acciones del sistema (cierre automático de alertas, escalamientos, liberación de reservas vencidas) se atribuyen al sistema como actor explícito, nunca a un usuario. | Estructural | `[PR-05]` `[MON §7.1]` |
| **RN-065** | **La existencia de una unidad de inventario es siempre la suma algebraica de sus movimientos en el kardex.** El sistema no almacena la existencia como un valor independiente que pueda divergir del kardex. Toda discrepancia detectada entre ambos es un hallazgo crítico de integridad. | Estructural | `[MON §7.1]` `[CD-37]` |
| **RN-066** | **Una unidad de inventario queda definida de forma única por la combinación SKU + Lote + Ubicación.** No pueden coexistir dos unidades de inventario con la misma combinación. | Estructural | `[CD-07]` |
| **RN-067** | **Ninguna operación de consulta puede modificar el estado del inventario.** Leer nunca escribe. | Estructural | `[NUEVO]` |
| **RN-068** | **Toda cantidad se expresa en la unidad de medida de su referencia.** El sistema no realiza conversiones implícitas entre unidades de medida. | Estructural | `[CD-11]` |

## 9.3 Reglas de stock negativo

| RN | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-009** | **Ninguna operación puede dejar la existencia de una unidad de inventario por debajo de cero.** Esta prohibición aplica a salidas, transferencias, movimientos internos y ajustes. **No admite excepción, autorización ni configuración**: no existe rol que pueda eludirla. | Estructural | `[NUEVO]` |
| **RN-025** | Ninguna operación puede comprometer una cantidad superior a la **existencia disponible** en la ubicación de origen. La existencia reservada, inmovilizada o en tránsito no está disponible para nuevas operaciones. | Estructural | `[CD-19]` |
| **RN-069*** | *(reservado — ver nota de numeración al final del capítulo)* | — | — |

> **Consecuencia de diseño.** RN-009 obliga a que toda diferencia física real se resuelva por el proceso de ajuste (PN-07), con motivo y aprobación, en lugar de permitir que el sistema «se cuadre solo» quedando en negativo. Es la regla que hace confiable el inventario `[MON §7.1]`.

## 9.4 Reglas de duplicados y unicidad

| RN | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-002** | El código de referencia es único en todo el catálogo. El sistema rechaza la creación de una referencia con código ya existente, activa o inactiva. | Estructural | `[NUEVO]` |
| **RN-003** | Al crear un documento de entrada con el mismo origen, referencia y fecha que otro existente, el sistema **advierte de posible duplicado** y exige confirmación explícita. No lo bloquea: puede tratarse de dos remesas legítimas. | Configurable | `[NUEVO]` |
| **RN-014** | El código de lote es único dentro de su SKU. El código de ubicación es único dentro de su bodega. El identificador de usuario es único en todo el sistema. | Estructural | `[NUEVO]` |
| **RN-016** | **Ningún identificador QR se repite jamás**, ni siquiera después de haber sido anulado o reemplazado. El espacio de identificadores es de un solo uso. | Estructural | `[DC-08]` |
| **RN-017** | Un mismo identificador secundario de código de barras no puede asociarse a dos identificadores QR de mercancía distintos (es decir, a dos SKU + Lote distintos). | Estructural | `[DC-08]` `[DF5-01]` |
| **RN-060** | Una novedad reportada sobre una unidad que ya tiene una novedad abierta **se vincula a la existente en lugar de crear una nueva**. | Configurable | `[NUEVO]` |
| **RN-055** | Una condición de alerta vigente genera **una sola alerta activa**, no una por cada ciclo de evaluación. Las alertas se agrupan por tipo, unidad y condición. | Configurable | `[NUEVO]` |

## 9.5 Reglas de ajustes

> Bloque de reglas más restrictivo del sistema. El ajuste es la única operación que altera la existencia sin movimiento físico correspondiente, y por tanto el principal vector de error y de fraude `[MON §6]`.

| RN | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-023** | **Ningún usuario puede aprobar una solicitud que él mismo originó.** Aplica a ajustes, salidas y cierres de conteo. Si el aprobador designado coincide con el solicitante, la solicitud **escala automáticamente al nivel superior**. Si no existe nivel superior disponible, la solicitud queda bloqueada y se notifica al Administrador. | Estructural | `[PR-01]` `[MON §6]` |
| **RN-024** | Todo ajuste se clasifica como **menor** o **mayor** según el umbral configurado. El ajuste menor lo aprueba el Jefe de Bodega; el mayor, el Administrador. El umbral aplicado queda registrado en el ajuste, de modo que un cambio posterior de configuración no altera la interpretación histórica. | Configurable | `[NUEVO]` |
| **RN-029** | **Todo ajuste exige un motivo tipificado seleccionado de una lista cerrada.** El texto libre puede complementarlo pero **nunca sustituirlo**. Determinados motivos exigen además evidencia adjunta, según se configure en M-19. | Estructural | `[MON §8.2]` |
| **RN-036** | Toda operación sobre existencia **inmovilizada** —ajuste, salida, transferencia o movimiento interno— requiere autorización expresa. El ajuste sobre mercancía inmovilizada requiere aprobación del **Administrador**, sin importar su monto. | Estructural | `[CD-22]` |
| **RN-037** | Cuando una misma unidad de inventario acumula más ajustes que el umbral configurado dentro de una ventana de tiempo configurada, el sistema genera **alerta de patrón anómalo** dirigida al Jefe y al Auditor, listando los ajustes involucrados con su solicitante y aprobador. | Configurable | `[MON §6]` `[DC-07]` |
| **RN-038** | Una solicitud de ajuste sin resolver más allá del plazo configurado **escala automáticamente** al nivel superior y genera alerta. | Configurable | `[NUEVO]` |
| **RN-062** | El rechazo de un ajuste **exige justificación** y queda registrado con la misma permanencia que una aprobación. La existencia no cambia, pero el intento y su rechazo forman parte del rastro auditable. | Estructural | `[NUEVO]` |
| **RN-070*** | Un ajuste aplicado **no se edita ni se revierte**: un error en un ajuste se corrige mediante un nuevo ajuste, quedando ambos en el kardex. | Estructural | `[RN-012]` |

## 9.6 Reglas de transferencias y movimientos

| RN | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-026** | **Un movimiento interno nunca altera la existencia total** de una unidad de inventario: solo redistribuye su ubicación. La suma de la existencia por ubicación antes y después debe ser idéntica. | Estructural | `[NUEVO]` |
| **RN-027** | Un movimiento cuya ubicación destino coincide con la de origen se rechaza por carecer de efecto. | Estructural | `[NUEVO]` |
| **RN-028** | Un movimiento interno interrumpido queda en estado **en tránsito**. Su existencia no está disponible en origen ni en destino. Si el tiempo en tránsito supera el máximo configurado, el sistema genera alerta. | Configurable | `[CD-23]` |
| **RN-031** | Al autorizarse una salida o crearse una transferencia, la existencia comprometida pasa a **reservada** y deja de contar como disponible. Ninguna otra operación puede comprometer esa misma cantidad. | Estructural | `[CD-20]` |
| **RN-032** | La existencia **en tránsito** no está disponible ni en la ubicación de origen ni en la de destino. Solo vuelve a estar disponible al confirmarse la recepción o al cancelarse la transferencia con retorno. | Estructural | `[CD-23]` |
| **RN-033** | Al recibirse una transferencia, el sistema compara lo despachado contra lo recibido. Si lo recibido es **menor**, registra diferencia de transferencia y abre novedad. Si lo recibido es **mayor**, **rechaza la recepción** y escala al Jefe. La transferencia no se completa hasta la resolución. | Estructural | `[NUEVO]` |
| **RN-034** | Una transferencia que supera el tiempo máximo en tránsito configurado genera alerta dirigida al Jefe, identificando su contenido y su responsable de despacho. | Configurable | `[NUEVO]` |
| **RN-035** | Una transferencia **pendiente de despacho** puede cancelarla el Coordinador, liberándose la reserva. Una transferencia **en tránsito** solo puede cancelarla el Jefe, y su cancelación genera un movimiento de retorno al origen. Toda cancelación exige motivo. | Estructural | `[NUEVO]` |
| **RN-049** | La toma de mercancía para una salida sigue la **política configurada** de selección de ubicación: primero en entrar primero en salir por lote, ubicación de mayor cantidad, o ubicación más próxima. El sistema propone; el operario ejecuta. | Configurable | `[NUEVO]` |
| **RN-050** | Durante la preparación de una salida, **el escaneo de una unidad que no corresponde a lo solicitado se rechaza**, indicando la discrepancia concreta: referencia, talla, color o lote. | Estructural | `[DC-08]` |
| **RN-051** | Una reserva no ejecutada dentro del plazo configurado **se libera automáticamente**, la existencia vuelve a disponible y se genera alerta al solicitante. | Configurable | `[NUEVO]` |
| **RN-053** | El retorno de mercancía previamente despachada **se registra como una entrada nueva que referencia la salida original**. La salida original **nunca se reversa**: ambos movimientos permanecen en el kardex. | Estructural | `[MON §7.1]` |

## 9.7 Reglas de lotes

| RN | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-026b*** | *(ver nota de numeración)* | — | — |
| **RN-071*** | **Ninguna existencia puede carecer de lote asociado.** Todo ingreso al inventario crea o se asocia a un lote, incluso cuando la empresa no distinga lotes comercialmente: en ese caso se genera un lote por evento de entrada. | Estructural | `[MON §7.1]` |
| **RN-072*** | Un lote pertenece a un solo SKU. No existen lotes que agrupen referencias, tallas o colores distintos. | Estructural | `[CD-06]` |
| **RN-036b*** | **La inmovilización de un lote afecta toda su existencia, en todas sus ubicaciones y bodegas, de forma simultánea.** No es posible inmovilizar parcialmente un lote. | Estructural | `[NUEVO]` |
| **RN-073*** | Solo el Jefe de Bodega o el Administrador pueden liberar un lote inmovilizado, y la liberación exige motivo tipificado. | Estructural | `[NUEVO]` |
| **RN-074*** | Un lote que supera el umbral de antigüedad configurado se destaca en las consultas y genera alerta informativa al Jefe. | Configurable | `[NUEVO]` |

## 9.8 Reglas de estados

| RN | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-019** | **Toda existencia disponible debe residir en una ubicación identificada.** No existe existencia disponible «en la bodega» sin ubicación concreta. Toda bodega debe tener al menos una zona de recepción para admitir mercancía aún no ubicada. | Estructural | `[NUEVO]` |
| **RN-020** | El sistema **propone** la ubicación destino según los criterios configurados; el Auxiliar **confirma o desvía**. La propuesta nunca es una imposición. | Configurable | `[NUEVO]` |
| **RN-021** | Una ubicación **inactiva** no puede recibir mercancía. Una ubicación cuya ocupación superaría su capacidad no se propone como destino, y si se excede, genera alerta de sobreocupación. | Configurable | `[CD-15]` |
| **RN-022** | Cuando el Auxiliar ubica mercancía en un lugar distinto al propuesto, **el sistema lo permite pero registra la desviación** y notifica al Coordinador. `[PR-06]` La desviación se registra como información operativa, **no como falta imputable**. | Configurable | `[PR-06]` `[MON §4]` |
| **RN-008** | La mercancía recibida en estado dañado **no ingresa como disponible**. Si ingresa, lo hace a zona de cuarentena en estado inmovilizado, y se abre novedad automáticamente. | Estructural | `[NUEVO]` |
| **RN-039** | La **existencia teórica congelada** al iniciar un conteo no se altera por movimientos posteriores al congelamiento. Los movimientos ocurridos durante el conteo se listan en la conciliación pero no modifican la base de comparación. | Estructural | `[NUEVO]` |
| **RN-040** | **La cantidad esperada no se muestra al contador**, ni antes ni después de registrar su conteo. El objetivo es impedir el sesgo de confirmación. La diferencia solo la ve quien concilia. | Estructural | `[NUEVO]` |
| **RN-041** | Cuando la diferencia de una línea supera el umbral de tolerancia, el sistema genera **segundo conteo obligatorio, ejecutado por una persona distinta a la del primero**. Adicionalmente, **quien ejecutó un conteo no puede cerrarlo**. | Estructural | `[PR-01]` |
| **RN-042** | **Solo el Jefe de Bodega cierra un conteo** y decide qué diferencias generan ajuste. Un conteo cerrado no se reabre. | Estructural | `[NUEVO]` |
| **RN-043** | La mercancía encontrada sin registro en el sistema **no se cuenta ni se usa hasta ser identificada**. Su incorporación exige creación de la unidad, ajuste por sobrante con motivo tipificado y aprobación del Jefe. | Estructural | `[NUEVO]` |
| **RN-044** | Un conteo programado y no ejecutado dentro de su plazo genera alerta. Si excede el plazo máximo, la existencia congelada se libera y el conteo se marca como vencido. | Configurable | `[NUEVO]` |
| **RN-045** | El conteo general **bloquea el registro de movimientos** desde su hora de corte hasta su cierre. Solo el Jefe puede autorizar un movimiento de excepción, que queda marcado como tal en el kardex. | Estructural | `[NUEVO]` |
| **RN-046** | Un conteo general **no puede cerrarse mientras existan ubicaciones del ámbito sin cubrir**. La exclusión de una ubicación exige justificación registrada, y la cobertura alcanzada queda documentada. | Estructural | `[NUEVO]` |
| **RN-047** | Cuando la diferencia global de un conteo general supera el umbral crítico configurado, el sistema **notifica al Administrador y al Auditor antes de permitir el cierre**. | Configurable | `[NUEVO]` |
| **RN-004** | La unidad de medida de una referencia **no puede modificarse si existen movimientos registrados** sobre ella. | Estructural | `[NUEVO]` |
| **RN-010** | Una referencia con existencia distinta de cero **no puede desactivarse**. | Estructural | `[NUEVO]` |
| **RN-013** | Una ubicación con existencia **no puede desactivarse**. | Estructural | `[NUEVO]` |

## 9.9 Reglas de recepción y salida

| RN | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-005** | El sistema compara automáticamente, línea por línea, la cantidad recibida contra la esperada en el documento de entrada. | Estructural | `[NUEVO]` |
| **RN-006** | Un faltante de recepción se registra como tal, el documento pasa a **recibido con novedad** y se notifica al Jefe. El faltante **no bloquea** la confirmación de lo efectivamente recibido. | Configurable | `[NUEVO]` |
| **RN-007** | Un **sobrante** de recepción **exige autorización del Jefe antes de confirmar** la entrada. Un sobrante no autorizado no ingresa al inventario. | Estructural | `[NUEVO]` |
| **RN-057b*** | `[PR-01]` **Quien registra la recepción física no puede confirmar la misma entrada.** La confirmación exige un segundo actor. | Estructural | `[PR-01]` |
| **RN-002b*** | Un documento de entrada solo admite **referencias activas del catálogo**. No es posible recibir mercancía sin identidad previamente definida. | Estructural | `[NUEVO]` |
| **RN-030** | El Coordinador puede autorizar salidas por debajo de su **umbral de autorización configurado**. Por encima, la solicitud escala al Jefe de Bodega. El umbral es consultable por el propio Coordinador. | Configurable | `[NUEVO]` |
| **RN-048** | **Toda salida exige motivo tipificado** seleccionado de lista cerrada. `[DC-03]` El sistema **no solicita ni almacena cliente, precio, factura ni documento comercial de despacho**. | Estructural | `[DC-03]` `[MON §8.2]` |
| **RN-052** | La **baja por daño** exige aprobación del Jefe de Bodega **cualquiera sea la cantidad**, junto con observación y evidencia. Alimenta el reporte de mermas y el KPI-13. | Estructural | `[NUEVO]` |
| **RN-015** | **Toda unidad de inventario debe tener un identificador activo.** No existe existencia sin identificador. El identificador de mercancía es el QR de su **SKU + Lote**; la unidad de inventario se determina con ese QR más su ubicación, obtenida por escaneo del QR de ubicación o por selección registrada. Si el SKU + Lote está en más de una ubicación y no se indica cuál, la operación no se registra. | Estructural | `[DC-08]` `[DF5-01]` |
| **RN-018** | La reimpresión de un identificador exige motivo. **La reimpresión conserva el mismo QR: produce otra copia del mismo identificador y no crea una nueva identidad**, por lo que el identificador no cambia de estado ni pierde su trazabilidad. La reimpresión queda consultable en el historial del SKU + Lote. Los motivos por los que un identificador se reemplaza o se anula son DECISIÓN PENDIENTE (HD-28) | Estructural | `[DC-08]` `[MON §7.1]` `[Q-09]` |

## 9.10 Reglas de alertas

| RN | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-056** | Una alerta de severidad crítica no atendida dentro del plazo configurado **escala automáticamente al rol superior** y genera notificación adicional. El escalamiento queda en la bitácora. | Configurable | `[NUEVO]` |
| **RN-057** | Una alerta **se cierra automáticamente cuando su condición de disparo deja de cumplirse**, quedando en el historial marcada como no atendida si nadie actuó sobre ella. | Configurable | `[NUEVO]` |
| **RN-058** | **El descarte de una alerta exige motivo.** Sin motivo, la alerta no puede cerrarse manualmente. Quien la atendió y qué hizo quedan registrados. | Estructural | `[NUEVO]` |
| **RN-059** | Una novedad sin resolver más allá del plazo configurado **escala al Jefe de Bodega** y genera alerta. | Configurable | `[NUEVO]` |
| **RN-075*** | **Toda alerta tiene un destinatario por rol.** Ninguna alerta puede quedar sin responsable asignado; si el rol destinatario no tiene usuario activo, escala al superior. | Estructural | `[NUEVO]` |

## 9.11 Reglas de eliminación lógica

| RN | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-063** | **Nada se elimina en COLBASOFT.** Usuarios, referencias, categorías, lotes, ubicaciones, motivos tipificados, novedades y observaciones **se desactivan o se cierran, nunca se borran**. No existe función de eliminación física en ninguna pantalla del sistema, para ningún rol, incluido el Administrador. | Estructural | `[MON §7.1]` |
| **RN-012** | **Ningún movimiento confirmado puede editarse ni eliminarse.** Un error se corrige generando un movimiento inverso con motivo y autorización; ambos movimientos permanecen visibles en el kardex de forma permanente. | Estructural | `[MON §7.1, §8.2]` |
| **RN-011** | El sistema **impide desactivar o cambiar de rol al último Administrador activo**, y de forma análoga impide dejar una bodega sin ningún Jefe de Bodega activo. | Estructural | `[NUEVO]` |
| **RN-076*** | Un elemento desactivado **no aparece en operaciones nuevas pero sí en el histórico**, conservando su identidad para que los registros pasados sigan siendo interpretables. | Estructural | `[NUEVO]` |
| **RN-077*** | Un elemento desactivado **puede reactivarse**, y tanto la desactivación como la reactivación quedan en la bitácora. | Configurable | `[NUEVO]` |

## 9.12 Reglas de auditoría

| RN | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-061** | **La bitácora de auditoría es inmutable.** No existe mecanismo de edición ni de borrado, para ningún rol, incluido el Administrador. Toda discontinuidad detectada en ella constituye hallazgo crítico de integridad. | Estructural | `[NUEVO]` |
| **RN-064** | Las **observaciones del Auditor** se almacenan en un registro separado y **no alteran el estado del inventario**. Son la única capacidad de escritura del rol Auditor. Se cierran con respuesta; nunca se eliminan. | Estructural | `[PR-02]` |
| **RN-054** | Ante pérdida de conectividad, el registro se retiene localmente y se sincroniza al restablecerse. **Un documento no se confirma hasta haber sincronizado**, y el cierre de jornada se bloquea mientras existan registros sin sincronizar. | Estructural | `[MON §3]` |
| **RN-078*** | Toda **exportación de datos** queda registrada en la bitácora con usuario, alcance temporal y fecha. | Estructural | `[NUEVO]` |
| **RN-079*** | Todo **cambio de configuración** queda registrado en la bitácora con su valor anterior y su valor nuevo. Los cambios aplican a evaluaciones futuras, **nunca de forma retroactiva**. | Estructural | `[NUEVO]` |
| **RN-080*** | El sistema debe poder **verificar a demanda** que la existencia actual equivale a la suma de los movimientos, por unidad, por lote y globalmente. | Estructural | `[RN-065]` |

---

## 9.13 Nota de numeración

Las reglas identificadas con asterisco (RN-069 a RN-080, más las variantes RN-002b, RN-026b, RN-036b y RN-057b) fueron incorporadas durante la consolidación de este capítulo, cuando la escritura de los procesos y módulos reveló reglas que las referencias cruzadas iniciales no habían previsto. **Se conserva la numeración de las referencias ya emitidas en los Capítulos 3, 5, 6 y 7 para no romper su trazabilidad**, y las reglas adicionales se numeran a continuación.

**Total efectivo: 68 reglas** — RN-001 a RN-065 (65 reglas de la numeración original en uso), más RN-066, RN-067, RN-068, RN-070 a RN-080 y las cuatro variantes marcadas. La renumeración canónica es tarea de la primera revisión formal del documento con el Director, y debe hacerse en un solo acto para no fragmentar las referencias.

**Versión 1.1.** Las reglas RN-081* a RN-083* (§9.15) se incorporan por el cierre del CP-04 y se numeran a continuación de RN-080 con el mismo criterio. El «total efectivo» de este apartado es el declarado en la v1.0; el recuento real de las tablas es 82 (H-01 del SRS, DEC-03 abierta) y, con la v1.1, **85**.

## 9.14 Distribución por categoría

| Categoría | Reglas | Estructurales | Configurables |
|---|:--:|:--:|:--:|
| Integridad fundamental | 5 | 5 | 0 |
| Stock negativo | 2 | 2 | 0 |
| Duplicados y unicidad | 7 | 5 | 2 |
| Ajustes | 8 | 6 | 2 |
| Transferencias y movimientos | 12 | 8 | 4 |
| Lotes | 5 | 4 | 1 |
| Estados | 17 | 13 | 4 |
| Recepción y salida | 10 | 8 | 2 |
| Alertas | 5 | 2 | 3 |
| Eliminación lógica | 5 | 4 | 1 |
| Auditoría | 6 | 6 | 0 |
| **Total** | **68** | **51** | **17** |

> **Versión 1.1.** A esta tabla, que reproduce las cifras declaradas en la v1.0, se suman las 3 reglas estructurales de §9.15.

> **Lectura del balance.** El 75 % de las reglas son estructurales e inviolables. Esa proporción es deliberada: la monografía documenta que el problema no es la falta de sistema sino la falta de **confiabilidad** del registro `[MON §3, §7.2]`. Un sistema cuyas reglas puedan desactivarse reproduce el cuaderno con más pasos.


## 9.15 Reglas incorporadas en la versión 1.1 (cierre del CP-04)

> Estas tres reglas **no forman parte de las 82** de §9.2–§9.12: se incorporan en la v1.1 por las decisiones DF5-02, DF5-03 y DF5-05 del cierre del CP-04. Se numeran a continuación de RN-080 con asterisco, como las demás reglas incorporadas después de la numeración original (§9.13).

| ID | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-081*** | **La existencia que ingresa por una entrada confirmada queda en recepción**, en una ubicación de una zona de recepción de la bodega: ya está en el inventario pero **no está disponible**, por lo que no se reserva, no sale ni se transfiere hasta ubicarse. Toda zona de recepción tiene al menos una ubicación. Se exceptúa la cantidad dañada, que ingresa inmovilizada en cuarentena (RN-008). | Estructural | `[DF5-02]` `[CD-16]` `[CD-44]` |
| **RN-082*** | **La primera ubicación de la existencia en recepción es un movimiento interno** desde la ubicación de recepción hacia la ubicación destino, y queda en el kardex con qué, cuánto, origen, destino, quién, cuándo y el documento de entrada que la origina. Cumple las reglas del movimiento interno (RN-021, RN-026, RN-027): la existencia total no cambia y el descuento en origen y el incremento en destino son indivisibles. Al confirmarse, la cantidad movida queda **disponible** en el destino, salvo que el destino pertenezca a una zona de recepción, donde sigue en recepción. | Estructural | `[DF5-03]` `[PN-03]` `[RN-026]` |
| **RN-083*** | **Un registro retenido sin conectividad no se aplica sin validarse de nuevo.** Al sincronizarse se valida contra el estado vigente y contra todas las reglas aplicables. Si las cumple, se confirma conservando la fecha y hora en que ocurrió el hecho; si no, **no se aplica**: se rechaza dejando constancia del registro original, de su autor, del motivo del rechazo y del instante. Cuando el registro rechazado describe un hecho físico ya realizado (mercancía recibida o trasladada), se abre una novedad para su resolución. Cada registro retenido se confirma o se rechaza una sola vez: la sincronización nunca produce existencia negativa, movimientos inválidos, estados imposibles, duplicados ni pérdida de trazabilidad. | Estructural | `[DF5-05]` `[RN-054]` |


## 9.16 Reglas incorporadas en la versión 1.2 (decisiones del 30 de septiembre de 2026)

> Estas seis reglas **no forman parte de las 82** de §9.2–§9.12 ni de las tres de §9.15: se incorporan en la v1.2 por las decisiones Q-11, F-1…F-6, Q-09 y Q-10. Se numeran a continuación de RN-083* con asterisco. **Todas son estructurales**: ninguna es parametrizable (DEC-04, interpretación a).

| ID | Regla | Tipo | Origen |
|---|---|---|---|
| **RN-084*** | **Toda mercancía recibida se registra por piezas.** Cada pieza pertenece a un solo SKU + Lote, tiene un tipo —rollo, paquete o bolsa, o contenedor agrupado— y una **cantidad propia registrada en la recepción**. El QR no identifica la pieza: la pieza tiene identidad interna en el sistema y el QR sigue identificando SKU + Lote | Estructural | `[Q-11]` `[F-1]` `[F-2]` `[F-6]` `[CD-49]` |
| **RN-085*** | **La existencia de una unidad de inventario es la suma de las cantidades de sus piezas en esa ubicación.** La cantidad de una pieza solo cambia por un movimiento del kardex (entrada, salida, movimiento interno, ajuste); la cantidad recibida de una línea de entrada es la suma de las cantidades de sus piezas | Estructural | `[Q-11]` `[F-2]` `[RN-065]` `[RN-066]` |
| **RN-086*** | **Un corte parcial descuenta de la pieza solo la cantidad cortada** y deja la pieza con su remanente, con la misma identidad. La cantidad cortada no puede superar la cantidad de la pieza (RN-009). El corte es una salida y cumple las reglas de salida | Estructural | `[F-3]` `[RN-009]` `[RN-048]` |
| **RN-087*** | **Toda operación que mueve, toma o cuenta mercancía identifica la pieza afectada.** Después de escanear el QR del SKU + Lote el operario selecciona la pieza; si hay varias del mismo lote en la ubicación, la ubicación (escaneada o seleccionada) filtra y verifica qué piezas se ofrecen. No se confirma la operación sin pieza seleccionada | Estructural | `[F-4]` `[RN-015]` |
| **RN-088*** | **En la preparación de una salida el escaneo verifica y cuenta.** Cada pieza tomada se cuenta una sola vez: seleccionar de nuevo la misma pieza no suma. La preparación no se confirma completa mientras falten piezas o cantidad solicitada, salvo salida parcial autorizada | Estructural | `[Q-10]` `[RN-050]` `[RN-025]` |
| **RN-089*** | **El conteo se hace manualmente, pieza por pieza.** El contador registra la cantidad de cada pieza sin ver la cantidad esperada (RN-040); la cantidad contada de la unidad de inventario es la suma de sus piezas | Estructural | `[F-5]` `[RN-040]` |


## 9.17 Fe de erratas sobre la cifra y la numeración de las reglas (versión 1.3)

> `[DEC-03]` El Director resolvió, el 30 de septiembre de 2026, adoptar el SRS como numeración canónica de las reglas y emitir esta fe de erratas. **No se modifica el texto de las reglas**; se corrige lo que este capítulo declaraba sobre ellas.

| # | Dice el SPEC | Se corrige a |
|---|---|---|
| 1 | «68 reglas» (índice del documento, §9.14 y §13.4) | Las tablas §9.2–§9.12 contienen **82 reglas distintas: 60 estructurales y 22 configurables**. Con las 3 de §9.15 y las 6 de §9.16 el total vigente es **91: 69 estructurales y 22 configurables** |
| 2 | `RN-069*` («reservado») y `RN-026b*` («ver nota de numeración») figuran en las tablas | **No son reglas**: son marcadores sin contenido y se retiran |
| 3 | Numeración `RN-nnn` del SPEC | La numeración **canónica** es `RN-<DOM>-nnn` del SRS (Anexo A.4). La numeración `RN-nnn` se conserva como referencia cruzada |
| 4 | §0.4 declara `HU-001…HU-096` y `RF-001…RF-138` | Los rangos vigentes son `HU-001…HU-114` y `RF-001…RF-184` (hallazgo H-03 del SRS) |

---

# CAPÍTULO 10 — KPIs OPERATIVOS

> **24 indicadores.** Los tres primeros son los que la monografía propone explícitamente `[MON §8.2]` y constituyen **el compromiso demostrable del proyecto ante el jurado**. Los restantes son nuevo aporte de la evolución del producto.
>
> `[DC-06]` **Este capítulo define qué se mide y cómo se calcula. No diseña visualizaciones**: la construcción de tableros analíticos pertenece a la herramienta externa y a una fase posterior.
>
> **Nota sobre valores objetivo.** Ningún KPI declara aquí una meta numérica. La meta solo puede fijarse contra la línea base de la empresa piloto, que aún no existe `[AUD C.2.4]`. Declarar metas ahora sería inventar evidencia.

## 10.1 Indicadores del compromiso de la monografía

### KPI-01 · Exactitud del Inventario `[MON §8.2]`

| Campo | Contenido |
|---|---|
| **Qué mide** | La proporción de unidades de inventario cuya existencia registrada coincide con la existencia física verificada mediante conteo |
| **Fórmula** | `(Líneas contadas conformes ÷ Total de líneas contadas) × 100` |
| **Frecuencia** | Al cierre de cada conteo, cíclico o general |
| **Usuario** | Jefe de Bodega · Administrador · Auditor |
| **Fuente del dato** | Módulo M-11 — comparación entre existencia teórica congelada (CD-25) y existencia contada (CD-26) |
| **Desglose** | Por zona, por ubicación, por categoría, por referencia |
| **Origen** | `[MON §8.2 — «Indicadores como exactitud del inventario»]` |

> **Indicador central del producto.** Es la métrica con la que el proyecto demostrará —o refutará— que la digitalización mejoró la confiabilidad del inventario respecto del método manual `[AUD V-06]`.

### KPI-02 · Exactitud Global del Inventario

| Campo | Contenido |
|---|---|
| **Qué mide** | Exactitud del inventario completo, medida en el último conteo general |
| **Fórmula** | `(Líneas conformes en conteo general ÷ Total de líneas del conteo general) × 100` |
| **Frecuencia** | A cada conteo general |
| **Usuario** | Administrador · Jefe de Bodega · Auditor |
| **Fuente del dato** | M-11, conteos de tipo general exclusivamente |
| **Origen** | `[MON §8.2]` `[NUEVO en su distinción del KPI-01]` |

### KPI-05 · Tiempo Medio de Registro de un Movimiento `[MON §8.2]`

| Campo | Contenido |
|---|---|
| **Qué mide** | Cuánto tarda un operario en registrar un movimiento completo, desde que inicia la operación hasta que el sistema la confirma |
| **Fórmula** | `Σ (instante de confirmación − instante de inicio) ÷ Número de movimientos registrados` |
| **Frecuencia** | Diaria, con acumulado semanal y mensual |
| **Usuario** | Jefe de Bodega · Administrador |
| **Fuente del dato** | M-14 — marcas temporales de inicio y confirmación de cada movimiento |
| **Desglose** | Por tipo de movimiento, por rol, por dispositivo |
| **Origen** | `[MON §8.2 — «tiempos de registro»]` |

> **Comparación obligatoria contra la línea base.** Este indicador solo tiene sentido contrastado con el tiempo del método manual actual, que la Fase 3 debe levantar `[RNF-019]` `[AUD C.2.4]`.

### KPI-08 · Frecuencia de Errores de Registro `[MON §8.2]`

| Campo | Contenido |
|---|---|
| **Qué mide** | Con qué frecuencia el registro resulta incorrecto y debe corregirse |
| **Fórmula** | `(Ajustes correctivos + Movimientos anulados + Líneas de conteo con diferencia) ÷ Total de movimientos del período × 100` |
| **Frecuencia** | Semanal, con acumulado mensual |
| **Usuario** | Jefe de Bodega · Administrador · Auditor |
| **Fuente del dato** | M-10 (ajustes), M-14 (anulaciones), M-11 (diferencias de conteo) |
| **Desglose** | Por tipo de error, por proceso, por zona |
| **Origen** | `[MON §8.2 — «frecuencia de errores»]` |

> `[PR-06]` **Este indicador no se desglosa por persona ante el operario.** Se desglosa por proceso y por zona. Su propósito es mejorar el proceso, no evaluar individuos `[MON §4 — miedo a la obsolescencia laboral]`.

## 10.2 Indicadores de exactitud y calidad del dato

| KPI | Nombre | Qué mide | Fórmula | Frecuencia | Usuario | Fuente | Origen |
|---|---|---|---|---|---|---|---|
| **KPI-03** | Cobertura de conteo | Qué proporción del inventario fue verificada en el período | `(Líneas contadas ÷ Líneas totales del inventario) × 100` | Mensual | Jefe · Auditor | M-11 | `[NUEVO]` |
| **KPI-04** | Diferencia neta de conteo | Magnitud agregada del descuadre detectado | `Σ (existencia contada − existencia congelada)` en unidades | Por conteo | Jefe · Auditor | M-11 | `[NUEVO]` |
| **KPI-06** | Tasa de segundo conteo | Proporción de líneas que requirieron recuento por diferencia sobre tolerancia | `(Líneas con segundo conteo ÷ Líneas contadas) × 100` | Por conteo | Jefe | M-11 | `[NUEVO]` |
| **KPI-07** | Movimientos sin identificador escaneado | Proporción de movimientos registrados sin escaneo, por selección manual | `(Movimientos sin escaneo ÷ Total de movimientos) × 100` | Semanal | Jefe · Coordinador | M-06 · M-14 | `[DC-08]` `[NUEVO]` |
| **KPI-09** | Integridad del kardex | Unidades donde la existencia no equivale a la suma de sus movimientos | `Número de unidades con discrepancia` (objetivo estructural: cero) | Diaria | Auditor · Administrador | M-18 · RN-065 | `[RN-065]` |
| **KPI-10** | Desviaciones de ubicación | Proporción de ubicaciones realizadas en un lugar distinto al propuesto | `(Ubicaciones desviadas ÷ Ubicaciones asignadas) × 100` | Semanal | Coordinador | M-07 · RN-022 | `[NUEVO]` |

## 10.3 Indicadores de operación

| KPI | Nombre | Qué mide | Fórmula | Frecuencia | Usuario | Fuente | Origen |
|---|---|---|---|---|---|---|---|
| **KPI-11** | Volumen de movimientos | Actividad total registrada en la bodega | `Número de movimientos confirmados en el período` | Diaria | Jefe · Administrador | M-14 | `[NUEVO]` |
| **KPI-12** | Tiempo medio de recepción | Cuánto tarda una entrada desde su llegada hasta su confirmación | `Σ (instante de confirmación − instante de llegada) ÷ Número de entradas` | Semanal | Coordinador · Jefe | M-07 | `[NUEVO]` |
| **KPI-13** | Tasa de merma | Proporción del inventario dado de baja por daño o pérdida | `(Unidades dadas de baja ÷ Existencia media del período) × 100` | Mensual | Jefe · Administrador | M-08 · RN-052 | `[MON §7.2 — pérdida de materia prima]` |
| **KPI-14** | Volumen y magnitud de ajustes | Cuánto se corrige el inventario fuera del movimiento físico | `Número de ajustes` y `Σ valor absoluto de las diferencias ajustadas` | Semanal | Jefe · Auditor | M-10 | `[MON §8.2]` |
| **KPI-15** | Tiempo medio en tránsito | Cuánto tardan las transferencias en completarse | `Σ (instante de recepción − instante de despacho) ÷ Número de transferencias` | Semanal | Jefe | M-09 | `[NUEVO]` |
| **KPI-16** | Rotación por referencia | Con qué velocidad sale cada referencia | `Unidades salidas en el período ÷ Existencia media del período` | Mensual | Jefe · Administrador | M-08 · M-13 | `[MON §3 — sobre stock]` |
| **KPI-17** | Existencia sin movimiento | Cuánto inventario lleva más del umbral sin moverse | `Número de unidades sin movimiento en N días` | Mensual | Jefe | M-14 · M-19 | `[MON §3]` |
| **KPI-18** | Ocupación de bodega | Qué proporción de la capacidad física está utilizada | `(Ocupación total ÷ Capacidad total) × 100` | Semanal | Jefe · Coordinador | M-05 · M-13 | `[NUEVO]` |

## 10.4 Indicadores de control y anticipación

| KPI | Nombre | Qué mide | Fórmula | Frecuencia | Usuario | Fuente | Origen |
|---|---|---|---|---|---|---|---|
| **KPI-19** | Alertas generadas y atendidas | Cuánto anticipa el sistema y cuánto se actúa sobre ello | `Número de alertas por tipo` y `(Alertas atendidas ÷ Alertas generadas) × 100` | Semanal | Jefe · Administrador | M-15 | `[DC-07]` `[MON §3]` |
| **KPI-20** | Tiempo medio de atención de alerta | Cuánto tarda el equipo en responder a una condición anómala | `Σ (instante de atención − instante de generación) ÷ Número de alertas atendidas` | Semanal | Jefe · Administrador | M-15 | `[NUEVO]` |
| **KPI-21** | Eventos de ruptura de stock | Cuántas veces una referencia activa llegó a existencia cero | `Número de eventos de existencia cero en referencias activas` | Mensual | Jefe · Administrador | M-15 · M-13 | `[MON §3 — rupturas de stock]` |
| **KPI-22** | Tiempo medio de aprobación | Cuánto tarda resolverse una solicitud de ajuste o de salida | `Σ (instante de resolución − instante de solicitud) ÷ Número de solicitudes` | Semanal | Administrador | M-10 · M-08 | `[NUEVO]` |
| **KPI-23** | Novedades reportadas y resueltas | Cuántas anomalías físicas afloran y con qué velocidad se cierran | `Número de novedades por tipo` y `tiempo medio de resolución` | Mensual | Jefe · Coordinador | M-12 | `[NUEVO]` |
| **KPI-24** | Adopción del sistema | Qué proporción de la operación pasa efectivamente por el sistema | `(Movimientos registrados en el sistema ÷ Movimientos estimados totales) × 100` | Mensual | Administrador · Auditor | M-14 + verificación de campo | `[MON §4 — resistencia a la adopción]` `[AUD OP-01]` |

> **KPI-24 es el indicador de riesgo del proyecto.** Un sistema que funciona pero por el que solo pasa una fracción de la operación real reproduce el problema original con un paso adicional. Su medición **exige verificación de campo**, no solo datos del sistema, y depende de que la Fase 3 establezca cuál es el volumen real de movimientos de la bodega `[AUD C.2.4]`.

## 10.5 Trazabilidad de los indicadores

| Origen | KPIs | Proporción |
|---|---|---|
| Propuestos explícitamente por la monografía `[MON §8.2]` | KPI-01, KPI-05, KPI-08 | 3 de 24 |
| Derivados de problemas documentados en la monografía | KPI-02, KPI-13, KPI-16, KPI-17, KPI-19, KPI-21, KPI-24 | 7 de 24 |
| **Nuevo aporte derivado de la evolución del proyecto** | KPI-03, 04, 06, 07, 09, 10, 11, 12, 14, 15, 18, 20, 22, 23 | 14 de 24 |

---

# CAPÍTULO 11 — RIESGOS FUNCIONALES

> **42 riesgos**, clasificados en operativos, humanos, tecnológicos y académicos. Cada uno declara probabilidad, impacto y mitigación. **Las mitigaciones son funcionales y de proceso**, no técnicas: la mitigación técnica pertenece a fases posteriores.
>
> **Escala:** Alta / Media / Baja para probabilidad e impacto. **Severidad** = combinación de ambas: 🔴 crítica · 🟠 alta · 🟡 media · 🟢 baja.

## 11.1 Riesgos operativos

| # | Riesgo | Prob. | Impacto | Sev. | Mitigación | Origen |
|---|---|:--:|:--:|:--:|---|---|
| **RG-01** | **La operación real ocurre por fuera del sistema.** El equipo registra en el sistema solo una parte y sigue usando el cuaderno para el resto. | Alta | Alto | 🔴 | Medición explícita mediante KPI-24 con verificación de campo · registro en el punto de operación desde tablet `[D-04]` · tiempo de registro menor que el manual `[RNF-019]` · conteos cíclicos que revelan el descuadre `[PN-08]` | `[MON §4]` `[AUD OP-01]` |
| **RG-02** | **El registro se difiere:** el operario anota en papel y transcribe después, reintroduciendo el error que el sistema debía eliminar. | Alta | Alto | 🔴 | Operación desde tablet en piso `[DC-05]` · captura por escaneo en lugar de digitación `[DC-08]` · confirmación visible inmediata `[RNF-037]` · KPI-07 mide movimientos sin escaneo | `[MON §3]` |
| **RG-03** | **Acumulación de pendientes al cierre de jornada:** recepciones sin confirmar, tránsitos abiertos, tareas sin cerrar. | Alta | Medio | 🟠 | Proceso de cierre operativo obligatorio `[PN-14]` · listado explícito de pendientes · traspaso registrado al turno siguiente · alertas por vencimiento `[RN-028, RN-044]` | `[NUEVO]` |
| **RG-04** | **Los ajustes se convierten en la vía habitual de cuadrar el inventario**, en lugar de la excepción documentada. | Media | Alto | 🟠 | Motivo tipificado obligatorio `[RN-029]` · aprobación por tercero `[RN-023]` · alerta por ajustes recurrentes `[RN-037]` · KPI-14 visible al Auditor | `[MON §6]` |
| **RG-05** | **Mercancía física sin identificador** que circula sin poder registrarse. | Alta | Medio | 🟠 | Identificación obligatoria en recepción `[PN-02]` `[RN-015]` · proceso de novedad accesible `[PN-12]` · regla de mercancía sin registro `[RN-043]` · reimpresión ágil por deterioro `[RN-018]` | `[NUEVO]` |
| **RG-06** | **Ubicaciones que no corresponden a la realidad física** porque la bodega se reorganiza sin registrarlo. | Media | Alto | 🟠 | Conteo cíclico frecuente `[PN-08]` · registro de desviación de ubicación `[RN-022]` · escaneo obligatorio de ubicación destino | `[NUEVO]` |
| **RG-07** | **Conteos que nunca se cierran** y dejan la existencia congelada indefinidamente. | Media | Medio | 🟡 | Plazo máximo con liberación automática `[RN-044]` · alerta de conteo vencido · el cierre es responsabilidad explícita del Jefe `[RN-042]` | `[NUEVO]` |
| **RG-08** | **Transferencias que se pierden en tránsito** sin que nadie las reclame. | Media | Alto | 🟠 | Tiempo máximo en tránsito con alerta `[RN-034]` · conciliación obligatoria despacho-recepción `[RN-033]` · listado de tránsitos en el cierre de jornada `[PN-14]` | `[NUEVO]` |
| **RG-09** | **Exceso de alertas que el equipo aprende a ignorar.** | Media | Medio | 🟡 | Agrupación de alertas por condición `[RN-055]` · reporte de frecuencia de disparo al Administrador para recalibrar umbrales · descarte con motivo obligatorio `[RN-058]` | `[NUEVO]` |
| **RG-10** | **Umbrales mal calibrados** que generan alertas irrelevantes o no detectan problemas reales. | Alta | Medio | 🟠 | Umbrales configurables por SKU `[HU-013]` · listado de SKU sin umbrales configurados `[RF-023]` · calibración con datos del piloto | `[NUEVO]` |
| **RG-11** | **La zona de recepción se convierte en almacén permanente**: la mercancía entra pero nunca se ubica. | Media | Medio | 🟡 | Existencia en recepción no cuenta como disponible `[CD-16]` · asignación de ubicación como paso del proceso de entrada `[PN-03]` · visibilidad en el dashboard `[HU-091]` | `[NUEVO]` |
| **RG-12** | **Interrupción de la operación durante el conteo general**, con pérdida de productividad. | Alta | Medio | 🟠 | Privilegio del conteo cíclico que no bloquea `[D-05]` · notificación anticipada `[HU-063]` · movimientos de excepción autorizables por el Jefe `[RN-045]` | `[NUEVO]` |

## 11.2 Riesgos humanos

> **Grupo de mayor severidad del proyecto.** La monografía documenta que la resistencia cultural, no la ausencia de tecnología, es la barrera principal `[MON §4, §7.1]`. Un fallo aquí reproduce exactamente el fracaso que el proyecto busca evitar.

| # | Riesgo | Prob. | Impacto | Sev. | Mitigación | Origen |
|---|---|:--:|:--:|:--:|---|---|
| **RG-13** | **Rechazo del sistema por el personal operativo**, que lo percibe como vigilancia o como el primer paso hacia su reemplazo. | Alta | Alto | 🔴 | `[PR-06]` El sistema **no expone indicadores de desempeño individual al operario** `[RNF-039]` · las desviaciones se registran como información, no como falta `[RN-022]` · el reporte de novedad no imputa al reportante `[RF-108]` · capacitación como parte del entregable `[MON §8.2]` | `[MON §4, §6]` |
| **RG-14** | **Curva de aprendizaje superior a la capacidad del equipo**, dada la baja alfabetización digital documentada. | Alta | Alto | 🔴 | Diseño optimizado para el Auxiliar `[§1.3.2]` · mínimo número de pasos `[RNF-036]` · escaneo en vez de digitación `[DC-08]` · verificación con usuarios reales sin formación previa `[RNF-035]` · adopción escalonada por proceso `[D-10]` `[RNF-024]` | `[MON §3, §8.2]` |
| **RG-15** | **Dependencia de una sola persona** que entiende el sistema; si falta, la bodega se detiene. | Media | Alto | 🟠 | Cinco roles con responsabilidades explícitas `[DC-04]` · escalada de privilegio `[PR-03]` · reasignación de tareas `[HU-103]` · capacitación al equipo completo `[MON §8.2]` | `[NUEVO]` |
| **RG-16** | **Uso de credenciales compartidas** para agilizar el trabajo, destruyendo la atribución. | Alta | Alto | 🔴 | Prohibición estructural de cuentas compartidas `[RN-001]` `[RF-002]` · sesión persistente durante la jornada para no incentivar el préstamo `[HU-002]` · detección de patrones anómalos por el Auditor `[PN-13]` | `[PR-05]` |
| **RG-17** | **Ocultamiento de problemas:** el operario no reporta lo que encuentra por temor a ser señalado. | Alta | Alto | 🔴 | Proceso de novedad de bajo costo y sin imputación `[PN-12]` `[RF-108]` `[PR-06]` · cultura de registro y no de castigo, explícita en el diseño | `[MON §4]` |
| **RG-18** | **El Jefe de Bodega se convierte en cuello de botella** de aprobaciones y detiene la operación. | Media | Alto | 🟠 | Umbral de autorización delegado al Coordinador `[RN-030]` · umbral de ajuste menor `[RN-024]` · escalamiento por plazo `[RN-038]` · KPI-22 mide el tiempo de aprobación | `[NUEVO]` |
| **RG-19** | **Resistencia del decisor de compra** por costo, dada la restricción financiera documentada. | Media | Alto | 🟠 | Alcance deliberadamente estrecho `[DC-02, DC-03]` `[D-02]` · adopción escalonada `[D-10]` · el propio sistema mide su beneficio para justificar la inversión `[MON §8.2]` `[D-08]` | `[MON §1, §3, §6]` |
| **RG-20** | **Manipulación deliberada del inventario** aprovechando el conocimiento del sistema. | Baja | Alto | 🟠 | Segregación de funciones `[PR-01]` `[§2.7]` · prohibición de aprobar la propia solicitud `[RN-023]` · segundo conteo por persona distinta `[RN-041]` · kardex y bitácora inmutables `[RN-012, RN-061]` · rol Auditor independiente `[PR-02]` · alerta de ajustes recurrentes `[RN-037]` | `[MON §6 — detección de fraudes]` |
| **RG-21** | **Rotación de personal** que obliga a recapacitar continuamente. | Alta | Medio | 🟠 | Curva de aprendizaje mínima `[RNF-035]` · el sistema indica qué hacer en lugar de exigir interpretación `[HU-092]` · mensajes en lenguaje comprensible `[RNF-029]` | `[MON §3, §8.2]` |
| **RG-22** | **El Coordinador desvía sistemáticamente** las ubicaciones propuestas, invalidando la lógica de asignación. | Media | Bajo | 🟢 | Registro de desviaciones `[RN-022]` · KPI-10 mide la tasa · recalibración de los criterios de asignación `[RF-039]` | `[NUEVO]` |

## 11.3 Riesgos tecnológicos

> **Nota de alcance.** Estos riesgos se enuncian en su dimensión **funcional y de proceso**. Su tratamiento técnico —arquitectura, infraestructura, plataforma— pertenece a fases posteriores y **no se aborda aquí** conforme a las restricciones de este documento.

| # | Riesgo | Prob. | Impacto | Sev. | Mitigación funcional | Origen |
|---|---|:--:|:--:|:--:|---|---|
| **RG-23** | **Pérdida de conectividad en la bodega**, dada la infraestructura tecnológica deficiente documentada. | Alta | Alto | 🔴 | Retención local y sincronización posterior `[RN-054]` `[RNF-010]` · bloqueo del cierre de jornada con registros sin sincronizar `[RNF-011]` · el documento no se confirma hasta sincronizar | `[MON §3]` |
| **RG-24** | **Dispositivos insuficientes o inadecuados** para el número de operarios. | Media | Alto | 🟠 | Web responsive sin instalación nativa `[DC-05]` `[RNF-043]` · operación en tablet estándar sin lector externo obligatorio `[RNF-044]` · levantamiento de infraestructura real en Fase 3 `[AUD C.2.7]` | `[MON §3]` `[AUD C.2.7]` |
| **RG-25** | **Etiquetas QR que se deterioran** en el ambiente de bodega y dejan de escanearse. | Alta | Medio | 🟠 | Reimpresión que conserva el mismo QR `[RN-018]` `[Q-09]` · información legible de respaldo impresa `[RF-044]` · selección manual como alternativa con registro de que no hubo escaneo `[PN-03 E-05]` | `[DC-08]` |
| **RG-26** | **Escaneo inviable** por iluminación, suciedad o condiciones físicas del sitio. | Media | Medio | 🟡 | Alternativa de selección manual registrada · código de barras como identificador secundario para consulta `[RN-017]` · verificación en el sitio real `[RNF-026]` | `[DC-08]` |
| **RG-27** | **Pérdida de información** por falla del sistema. | Baja | Alto | 🟠 | Respaldo periódico con restauración probada `[RNF-012]` · pérdida máxima tolerable acotada `[RNF-013]` · kardex como fuente única de verdad reconstruible `[RN-065]` | `[NUEVO]` |
| **RG-28** | **Degradación del rendimiento** conforme crece el kardex. | Media | Medio | 🟡 | Requisito explícito de no degradación `[RNF-023]` · prueba con volumen proyectado a tres años `[RNF-020]` | `[NUEVO]` |
| **RG-29** | **La integración analítica no se materializa** o entrega datos inconsistentes. | Media | Medio | 🟡 | Exposición estructurada y consistente `[RF-137]` · los KPIs se calculan en el propio sistema `[RF-136]`, de modo que el producto no depende de la herramienta externa para medir su beneficio | `[DC-06]` |
| **RG-30** | **Divergencia entre existencia y kardex** por falla de integridad. | Baja | Alto | 🟠 | Derivación estructural de la existencia desde el kardex `[RN-065]` · verificación a demanda `[RNF-034]` · KPI-09 con objetivo estructural de cero · hallazgo crítico automático `[RF-151]` | `[RN-065]` |
| **RG-31** | **Incompatibilidad de navegador** en los equipos existentes de la empresa. | Media | Bajo | 🟢 | Matriz de navegadores definida `[RNF-046]` · aviso explícito ante navegador no soportado en lugar de fallo silencioso `[RNF-047]` | `[DC-05]` |
| **RG-32** | **Incumplimiento normativo** en el tratamiento de datos. | Baja | Alto | 🟠 | Requisito explícito de cumplimiento `[RNF-008]` · revisión previa a producción · pregunta S-12 elevada al Director | `[AUD C.2.11]` |

## 11.4 Riesgos académicos

> Estos riesgos afectan la defensa del proyecto de grado, no su operación. Varios provienen directamente de la Auditoría Fundacional y siguen abiertos.

| # | Riesgo | Prob. | Impacto | Sev. | Mitigación | Origen |
|---|---|:--:|:--:|:--:|---|---|
| **RG-33** | **Las nueve fuentes ausentes de la bibliografía no se verifican**, y el jurado las señala. | Alta | Alto | 🔴 | Verificación como entregable obligatorio de la Fase 2 del roadmap · toda cifra de fuente no verificada se marca explícitamente en este documento `[§1.1.3]` · no se usa ninguna como justificación cuantitativa hasta verificarse | `[AUD E.1, E.2]` |
| **RG-34** | **Las contradicciones estadísticas no se resuelven**: CEPAL con 25 % y 40 %; el 40 % de reducción de errores atribuido a dos fuentes distintas. | Alta | Alto | 🔴 | Preguntas I-04 e I-05 elevadas al Director · tabla de resolución como entregable de la Fase 2 · este documento no reproduce ninguna de las cifras en conflicto como afirmación propia | `[AUD E.2.5, E.2.8]` |
| **RG-35** | **El piloto no alcanza las cifras citadas** (−40 % errores, +55 % trazabilidad, +25–45 % productividad) y el resultado contradice la justificación del proyecto. | Alta | Alto | 🔴 | Pregunta V-06 elevada al Director **antes** de iniciar el desarrollo · los KPIs no declaran metas numéricas sin línea base `[§10]` · el informe de impacto reporta el resultado íntegro, favorable o no `[AUD Fase 7]` | `[AUD V-06]` |
| **RG-36** | **No se levanta la línea base** y resulta imposible demostrar mejora alguna. | Alta | Alto | 🔴 | La línea base es entregable explícito de la Fase 3 del roadmap `[AUD C.2.4]` · KPI-01, KPI-05 y KPI-08 carecen de sentido sin ella `[§10.1]` · pregunta V-03 elevada al Director | `[AUD C.2.4]` |
| **RG-37** | **La empresa de estudio no accede a participar** en el levantamiento o en el piloto. | Media | Alto | 🟠 | Pregunta V-01 elevada al Director · la restricción R-02 de la monografía —«sin intervenir empresas reales»— debe levantarse formalmente `[AUD R-02]` · gestión de confidencialidad `[AUD V-10]` | `[MON §4]` `[AUD C.2.1]` |
| **RG-38** | **El alcance del MVP resulta desproporcionado** para un proyecto de nivel Ingeniería (corregido en la v1.2; la v1.1 decía «Tecnólogo»). | Media | Alto | 🟠 | Backlog priorizado en cuatro horizontes `[Cap. 12]` · 72 requisitos P0 frente a 90 de menor prioridad · pregunta S-15 sobre el entregable mínimo aprobatorio, elevada al Director | `[AUD S-15]` |
| **RG-39** | **Aparición de requisitos sin anclaje en la monografía**, violando la Regla Innegociable 3. | Media | Medio | 🟡 | Sistema de trazabilidad obligatorio `[§0.3]` · todo elemento sin anclaje se marca explícitamente como **nuevo aporte derivado de la evolución del proyecto** · pregunta A-06 elevada al Director | `[AUD A-06]` |
| **RG-40** | **La delimitación del sujeto de estudio sigue abierta**: qué es PYME, qué comprende sector textil, qué municipios integran el Eje Cafetero. | Alta | Medio | 🟠 | Preguntas A-03, A-04 y A-05 elevadas al Director · este documento es funcionalmente completo sin ellas, pero el dimensionamiento y la selección de la empresa piloto las requieren `[§1.3.1]` | `[AUD C.1.9]` |
| **RG-41** | **El horizonte temporal de la monografía está vencido** y las proyecciones citadas quedaron fuera de vigencia. | Alta | Medio | 🟠 | Pregunta I-09 elevada al Director · el proyecto se denomina 2027 mientras la fuente proyecta a 2025 `[AUD E.3.14]` | `[AUD C.1.10]` |
| **RG-42** | **Pérdida de trazabilidad hacia la monografía** en las fases de diseño y construcción, quedando el producto huérfano de su fundamento académico. | Media | Alto | 🟠 | Matriz de trazabilidad requisito ↔ problema ↔ apartado como entregable de la Fase 4 `[AUD Fase 4]` · sistema de etiquetas de este documento sostenido en todos los artefactos derivados `[§0.3]` | `[AUD Fase 8]` |

## 11.5 Concentración de riesgo

| Categoría | Riesgos | 🔴 Críticos | 🟠 Altos | 🟡 Medios | 🟢 Bajos |
|---|:--:|:--:|:--:|:--:|:--:|
| Operativos | 12 | 2 | 6 | 4 | 0 |
| Humanos | 10 | 4 | 5 | 0 | 1 |
| Tecnológicos | 10 | 1 | 5 | 3 | 1 |
| Académicos | 10 | 4 | 5 | 1 | 0 |
| **Total** | **42** | **11** | **21** | **8** | **2** |

> **Lectura del perfil de riesgo.** Los once riesgos críticos se concentran en dos frentes: **la adopción real por el personal** (RG-01, RG-02, RG-13, RG-14, RG-16, RG-17, RG-23) y **la solidez académica de la evidencia** (RG-33, RG-34, RG-35, RG-36). Ningún riesgo crítico es de naturaleza técnica de construcción. Esto confirma el diagnóstico de la monografía: el obstáculo no es construir el sistema, es lograr que se use y poder demostrar que sirvió `[MON §4, §7.1, §8.2]`.

---

# CAPÍTULO 12 — BACKLOG DEL MVP

> Producto priorizado en cuatro horizontes. `[DC-07]` **No se incorpora inteligencia artificial al MVP ni a la versión 1.1**; toda exploración en esa dirección se ubica en Investigación futura y **queda condicionada a autorización expresa del Director**.

## 12.1 Criterio de priorización

| Criterio | Peso en la decisión |
|---|---|
| **1. ¿Sin esto el inventario deja de ser confiable?** | Si sí → MVP obligatorio |
| **2. ¿Lo recomienda explícitamente la monografía?** | `[MON §8.2]` → prioridad alta |
| **3. ¿Ataca un problema documentado del Cap. A.8 de la auditoría?** | → prioridad alta |
| **4. ¿Es condición para medir el beneficio del proyecto?** | KPI-01, KPI-05, KPI-08 → MVP obligatorio |
| **5. ¿Es condición de adopción por el usuario crítico?** | `[MON §4]` → MVP obligatorio |
| **6. ¿Es una comodidad que el sistema puede no tener y seguir sirviendo?** | → versión posterior |

## 12.2 Horizonte 1 — MVP

> **Objetivo del MVP:** que la bodega de la empresa piloto opere íntegramente en el sistema, sin cuaderno, con trazabilidad completa y con capacidad de medir su propio impacto.

### Bloque 1 — Fundación *(sin esto no existe nada)*

| Orden | Elemento | Módulos | RF principales | Origen |
|:--:|---|---|---|---|
| 1 | Acceso individual y atribución de toda acción | M-01 | RF-001 a RF-004 | `[PR-05]` |
| 2 | Usuarios con los cinco roles oficiales y segregación de funciones | M-02 | RF-008 a RF-011 | `[DC-04]` |
| 3 | Catálogo de referencias con talla, color y SKU | M-03 | RF-016 a RF-020 | `[D-01]` |
| 4 | Estructura de bodega: zonas y ubicaciones | M-05 | RF-032 a RF-035 | `[NUEVO]` |
| 5 | Parámetros y motivos tipificados | M-19 | RF-152 a RF-156 | `[CD-36]` |
| 6 | Identificación QR de mercancía y de ubicación | M-06 | RF-040 a RF-043 | `[DC-08]` |

### Bloque 2 — Núcleo transaccional *(la recomendación literal de la monografía)*

> `[MON §8.2]` *«Implementar desde el principio aplicativos o sistemas de registro digital que permitan estandarizar entradas, salidas y movimientos de inventario»*. **Este bloque es esa frase, ejecutada.**

| Orden | Elemento | Módulos | RF principales | Origen |
|:--:|---|---|---|---|
| 7 | Kardex inmutable con atribución personal | M-14 | RF-120 a RF-124 | `[MON §7.1]` |
| 8 | Existencia derivada del kardex | M-13, M-14 | RF-112 a RF-116 | `[RN-065]` |
| 9 | Entradas: documento, recepción, verificación, confirmación | M-07 | RF-048 a RF-058 | `[MON §8.2]` |
| 10 | Ubicación física de la mercancía | M-07, M-05 | RF-035, RF-036 | `[NUEVO]` |
| 11 | Salidas con motivo, autorización y reserva | M-08 | RF-061 a RF-069 | `[MON §8.2]` |
| 12 | Movimientos internos de reubicación | M-09 | RF-072 a RF-077 | `[MON §8.2]` |
| 13 | Prohibición estructural de existencia negativa | M-08, M-09, M-10 | RF-064, RF-088 | `[RN-009]` |
| 14 | Lotes con trazabilidad de origen | M-04 | RF-026 a RF-028 | `[MON §7.1]` |

### Bloque 3 — Control *(lo que hace confiable el registro)*

| Orden | Elemento | Módulos | RF principales | Origen |
|:--:|---|---|---|---|
| 15 | Ajustes con motivo tipificado y aprobación por tercero | M-10 | RF-083 a RF-089 | `[MON §8.2]` |
| 16 | Prohibición de aprobar la propia solicitud | M-10, M-08 | RF-087 | `[PR-01]` |
| 17 | Bitácora de auditoría inmutable | M-18 | RF-145 a RF-147 | `[NUEVO]` |
| 18 | Rol Auditor de solo lectura | M-18 | RF-148, RF-149 | `[PR-02]` |
| 19 | Eliminación lógica universal | Todos | RF-011, RF-021, RF-037, RF-111 | `[RN-063]` |
| 20 | Verificación de integridad existencia = suma de movimientos | M-18, M-14 | RF-125 | `[RN-065]` |

### Bloque 4 — Medición *(sin esto el proyecto no puede demostrar nada)*

| Orden | Elemento | Módulos | RF principales | Origen |
|:--:|---|---|---|---|
| 21 | Conteo cíclico sin detener la operación | M-11 | RF-093 a RF-102 | `[D-05]` `[MON §8.2]` |
| 22 | Ocultamiento de la cantidad esperada al contador | M-11 | RF-098 | `[RN-040]` |
| 23 | Segundo conteo por persona distinta | M-11 | RF-100, RF-101 | `[RN-041]` |
| 24 | **KPI-01 Exactitud del Inventario** | M-16, M-11 | RF-105, RF-136 | `[MON §8.2]` |
| 25 | **KPI-05 Tiempo de Registro** | M-16, M-14 | RF-136 | `[MON §8.2]` |
| 26 | **KPI-08 Frecuencia de Errores** | M-16 | RF-136 | `[MON §8.2]` |
| 27 | Reportes operativos exportables | M-16 | RF-134, RF-135 | `[MON §8.2]` |

### Bloque 5 — Adopción *(sin esto el sistema se rechaza)*

> Este bloque es MVP obligatorio, no una mejora. La monografía documenta que la resistencia cultural es la barrera principal `[MON §4, §7.1]`.

| Orden | Elemento | Módulos | RF/RNF principales | Origen |
|:--:|---|---|---|---|
| 28 | Operación completa desde tablet en piso de bodega | Todos | RNF-042, RNF-043 | `[DC-05]` `[D-04]` |
| 29 | Registro por escaneo en lugar de digitación | M-06 | RF-042, RNF-044 | `[DC-08]` |
| 30 | Confirmación visible de cada registro guardado | Todos | RNF-037 | `[NUEVO]` |
| 31 | Panel de tareas del Auxiliar | M-20 | RF-158 a RF-160 | `[NUEVO]` |
| 32 | Ausencia de indicadores de desempeño individual ante el operario | M-17, M-16 | RF-144, RNF-039 | `[PR-06]` `[MON §4]` |
| 33 | Reporte de novedad sin imputación al reportante | M-12 | RF-106 a RF-108 | `[MON §4]` |
| 34 | Mensajes que explican el rechazo, no solo lo imponen | Todos | RNF-038, RNF-029 | `[D-07]` |
| 35 | Retención local y sincronización sin conectividad | Todos | RNF-010, RNF-011 | `[MON §3]` `[RN-054]` |

### Bloque 6 — Anticipación

| Orden | Elemento | Módulos | RF principales | Origen |
|:--:|---|---|---|---|
| 36 | Alertas por reglas y umbrales configurados | M-15 | RF-127 a RF-131 | `[DC-07]` `[MON §3]` |
| 37 | Umbrales de existencia mínima y máxima por SKU | M-03, M-19 | RF-022 | `[MON §3]` |
| 38 | Dashboard operativo del Jefe | M-17 | RF-141, RF-142 | `[DC-02]` |
| 39 | Cierre operativo de jornada | M-20, M-17 | PN-14 · RF-182 a RF-184 | `[NUEVO]` `[DEC-05]` |

### Bloque 7 — Trazabilidad por pieza *(incorporado en la v1.2)*

> `[Q-11]` El Director declaró la trazabilidad por pieza o rollo dentro del MVP: el elemento 6 del Horizonte 3 («Gestión de unidades de manejo y contenedores») se incorpora en lo que exigen Q-11 y F-1…F-6.

| Orden | Elemento | Módulos | RF principales | Origen |
|:--:|---|---|---|---|
| 40 | Piezas (rollo, paquete o bolsa, contenedor agrupado) con cantidad propia, selección tras el escaneo, corte parcial, escaneo de salida que verifica y cuenta, conteo pieza por pieza y trazabilidad por pieza | M-07, M-08, M-09, M-11, M-13, M-14 | RF-163 a RF-171 | `[Q-11]` `[F-1]` `[F-2]` `[F-3]` `[F-4]` `[F-5]` `[F-6]` `[Q-10]` |

### Bloque 8 — Cierre de brechas de trazabilidad y del cierre de jornada *(incorporado en la v1.3)*

> `[DEC-05]` `[DEC-06]` El Director aprobó las propuestas de cierre de brechas del SRS (PROP-RN, PROP-KPI, PROP-CIE). Capturan desde el primer día datos que no se recuperan después y dan requisito a reglas que no lo tenían.

| Orden | Elemento | Módulos | RF principales | Origen |
|:--:|---|---|---|---|
| 41 | Reglas con requisito propio (desviación de ubicación, movimiento interno en tránsito, mercancía sin registro, reserva vencida, novedad vencida) y captura de datos de KPI (inicio y confirmación del movimiento, modo de identificación, llegada de la mercancía, volumen de referencia) | M-05, M-06, M-07, M-08, M-09, M-12, M-14, M-19 | RF-172, RF-173, RF-174, RF-176 a RF-181 | `[DEC-06]` |

**Alcance del MVP:** 41 elementos · 72 requisitos P0 declarados en la v1.1 más 8 de la v1.2, y los P1 indispensables · 20 módulos con funcionalidad parcial en M-11, M-15, M-16 y M-17. **Umbral aprobatorio `[DEC-01]`: Núcleo (Horizonte 1), 94 HU y 164 RF, con 1 bodega piloto.**

## 12.3 Horizonte 2 — Versión 1.1

> Elementos que aportan valor operativo real pero cuya ausencia no impide operar ni medir. `[DC-07]` **Sin inteligencia artificial.**

| # | Elemento | Módulos | Justificación de aplazamiento | Origen |
|:--:|---|---|---|---|
| 1 | Transferencias entre zonas y bodegas con despacho y recepción | M-09 | El MVP opera con una bodega; la transferencia gana relevancia al crecer | `[NUEVO]` |
| 2 | Conteo general con bloqueo de movimientos (incluye la alerta de diferencia crítica, RF-175 · HU-112) | M-11 | El conteo cíclico ya alimenta el KPI-01 durante el piloto | `[NUEVO]` `[DEC-06]` |
| 3 | Inmovilización y liberación de lotes | M-04 | Control valioso, no indispensable para el registro básico | `[RN-036]` |
| 4 | Alerta de patrón de ajustes recurrentes | M-15, M-10 | Requiere histórico acumulado para ser significativa | `[RN-037]` |
| 5 | Escalamiento automático de alertas y solicitudes | M-15, M-20 | El equipo del piloto es pequeño; el escalamiento gana valor al crecer | `[RN-056]` |
| 6 | Carga masiva del catálogo inicial | M-03 | Alivia el arranque, pero la carga manual es viable en el piloto | `[RF-024]` |
| 7 | Consulta de existencia histórica a fecha de corte | M-13, M-14 | Valiosa para auditoría; el kardex ya permite la reconstrucción manual | `[RF-117]` |
| 8 | Reportes programados periódicos | M-16 | Comodidad; los reportes a demanda cubren la necesidad | `[RF-140]` |
| 9 | Exportación estructurada para la herramienta analítica | M-16 | `[DC-06]` Los KPIs se calculan en el sistema; la integración amplía, no habilita | `[DC-06]` |
| 10 | Dashboard del Coordinador restringido a su zona | M-17 | El Jefe cubre la supervisión en una operación de una sola bodega | `[RF-143]` |
| 11 | Identificador secundario de código de barras | M-06 | `[DC-08]` Explícitamente secundario | `[DC-08]` |
| 12 | Criterios configurables de asignación automática de ubicación | M-05 | El MVP puede operar con propuesta simple y desviación registrada | `[RF-039]` |
| 13 | Listado de lotes por antigüedad con alerta | M-04 | Aporta rotación; no condiciona la confiabilidad del registro | `[RN-074]` |
| 14 | Reasignación de tareas entre auxiliares | M-20 | Manejable verbalmente en un equipo pequeño | `[HU-103]` |
| 15 | KPIs 03, 04, 06, 07, 10, 12, 15, 18, 20, 22, 23 | M-16 | Los tres KPIs del compromiso ya están en el MVP | `[NUEVO]` |
| 16 | Ajuste de tamaño de texto y refinamientos de accesibilidad | Todos | Mejora real; no bloquea la operación | `[RNF-028]` |

## 12.4 Horizonte 3 — Futuro

> Elementos coherentes con el alcance constitucional pero fuera del proyecto de grado. **Requieren autorización expresa del Director antes de cualquier trabajo.**

| # | Elemento | Condición previa | Frontera |
|:--:|---|---|---|
| 1 | Operación multibodega con consolidación entre sedes | Que la empresa opere más de una bodega | Dentro de `[DC-02]` |
| 2 | Valorización del inventario en unidades monetarias | Definición de política de costeo con el Director | ⚠️ Roza `[DC-03]` — contabilidad excluida |
| 3 | Trazabilidad hacia el proveedor aguas arriba | Autorización de ampliación de `[CD-21]` | ⚠️ Roza `[DC-03]` — compras completas excluidas |
| 4 | Trazabilidad hacia el cliente aguas abajo | Autorización de ampliación de `[CD-21]` | ⚠️ Roza `[DC-03]` — ventas excluidas |
| 5 | Módulo de devoluciones estructurado | Definición de proceso con la empresa | Dentro de `[DC-02]` |
| 6 | Gestión avanzada de unidades de manejo y contenedores (lo que excede lo incorporado al MVP por Q-11 y F-1…F-6; ver HD-28 y HD-29) | Necesidad operativa demostrada · autorización expresa del Director | Dentro de `[DC-02]`. La pieza, el paquete o bolsa y el contenedor agrupado pasaron al MVP en la v1.2 `[Q-11]` `[F-6]` |
| 7 | Firma o validación de conteo en dos etapas | Exigencia de auditoría externa | Dentro de `[DC-02]` |
| 8 | Panel de indicadores para la gerencia | `[DC-06]` Debe resolverse en la herramienta analítica externa | ⚠️ Verificar contra `[DC-06]` |
| 9 | Historial de configuración con reversión | Volumen de cambios que lo justifique | Dentro de `[DC-02]` |
| 10 | Soporte de múltiples idiomas | Expansión fuera del ámbito regional | Dentro de `[DC-02]` |

## 12.5 Horizonte 4 — Investigación futura

> `[DC-07]` **Ninguno de estos elementos forma parte del MVP ni de la versión 1.1.** Se registran como líneas de exploración académica, no como compromisos de producto. **Su incorporación requiere autorización expresa del Director y justificación que hoy la monografía no puede sostener** `[AUD C.1.5]`.

| # | Línea | Por qué es investigación y no producto | Condición para siquiera evaluarla |
|:--:|---|---|---|
| 1 | **Predicción de demanda por modelos estadísticos** | `[DC-07]` Excede la definición de «inteligente» adoptada en §1.6 | Histórico de al menos dos ciclos anuales completos · autorización del Director · fundamentación teórica que la monografía no aporta |
| 2 | **Sugerencia automática de punto de reorden** | Requiere modelado de demanda | Igual que el anterior |
| 3 | **Detección de anomalías por aprendizaje automático** | `[DC-07]` El MVP resuelve la detección por reglas explícitas `[RN-037]` | Demostración de que las reglas del Cap. 9 resultan insuficientes |
| 4 | **Optimización automática de la disposición de bodega** | Excede el alcance de gestión de inventarios `[DC-02]` | Autorización expresa de ampliación de alcance |
| 5 | **Reconocimiento de mercancía por visión artificial** | `[DC-08]` El QR resuelve la identificación | Demostración de que el QR es inviable en el contexto real |
| 6 | **Integración con dispositivos de captura automática** | `[MON §6]` La monografía menciona sensores una sola vez `[AUD S-06]` | Pregunta S-06 respondida afirmativamente por el Director |
| 7 | **Modelo de adopción tecnológica aplicado y validado** | `[AUD C.2.5]` El OE-2 de la monografía quedó cumplido solo nominalmente | Verificación de Rogers (1962) en la Fase 2 · pregunta I-07 |
| 8 | **Estudio comparativo con soluciones del mercado** | `[AUD C.2.6]` Vacío identificado por la auditoría | Pregunta S-14 respondida afirmativamente |

## 12.6 Resumen del backlog

| Horizonte | Elementos | Naturaleza | IA |
|---|:--:|---|:--:|
| **MVP** | 41 | Operación completa, trazable y medible | ❌ |
| **Versión 1.1** | 16 | Ampliación de control y comodidad operativa | ❌ |
| **Futuro** | 10 | Requiere autorización; 4 rozan las exclusiones de `[DC-03]` o `[DC-06]` | ❌ |
| **Investigación futura** | 8 | Exploración académica, sin compromiso de producto | ⚠️ Solo aquí |

---

# CAPÍTULO 13 — GLOSARIO Y CONTROL DEL DOCUMENTO

## 13.1 Glosario de términos del dominio

Los 49 conceptos de dominio están definidos operativamente en el **Capítulo 4**. Este glosario recoge los términos de uso transversal en el documento que no son conceptos de dominio.

| Término | Definición en este documento |
|---|---|
| **Actor** | Rol que ejecuta o recibe el resultado de una acción. COLBASOFT reconoce cinco roles oficiales `[DC-04]` más el sistema como actor de acciones automáticas `[RN-001]`. |
| **Alcance** | Frontera de lo que el producto hace, fijada por `[DC-02]` y `[DC-03]`. Lo que queda fuera está fuera por decisión constitucional, no por omisión. |
| **AS-IS** | Proceso tal como ocurre hoy en la empresa. **No fue levantado por la monografía** `[AUD C.1.8]` y su documentación corresponde a la Fase 3 del roadmap. |
| **Criterio de aceptación** | Condición verificable que determina si una historia de usuario está satisfecha. |
| **Decisión constitucional** | Determinación del Director, inmodificable dentro de esta especificación `[§0.1]`. |
| **Empresa de estudio / empresa piloto** | `[DC-01]` Organización del sector textil del Eje Cafetero con la que se levanta el proceso real y se opera el piloto, sin identificación comercial en este documento. |
| **Línea base** | Medición del desempeño **antes** de implantar el sistema. **No existe** `[AUD C.2.4]`; sin ella los KPI-01, KPI-05 y KPI-08 no pueden demostrar mejora alguna. |
| **MVP** | Conjunto mínimo de elementos con el que la bodega opera íntegramente en el sistema y el proyecto puede medir su impacto `[§12.2]`. |
| **Nuevo aporte derivado de la evolución del proyecto** | Etiqueta `[NUEVO]`. Elemento que **no existe en la monografía** y se introduce por necesidad de ingeniería de producto `[§0.3]`. |
| **Regla configurable** | Regla de negocio cuyo umbral se ajusta en M-19 pero cuya lógica no puede desactivarse. |
| **Regla estructural** | Regla de negocio inviolable y no parametrizable. Ningún rol puede eludirla, incluido el Administrador `[§9.1]`. |
| **Segregación de funciones** | Principio por el cual quien ejecuta una acción no es quien la autoriza `[PR-01]`. |
| **TO-BE** | Proceso tal como el producto propone que ocurra. Es lo que modela el Capítulo 3. |
| **Umbral** | Valor configurable que determina cuándo dispara una regla `[CD-46]`. |
| **Usuario crítico** | El Auxiliar de Bodega: quien más usa el sistema, menos formación tiene y más puede hacer fracasar la adopción `[§1.3.2]` `[MON §4]`. |

## 13.2 Siglas

| Sigla | Significado |
|---|---|
| **ANDI** | Asociación Nacional de Empresarios de Colombia |
| **CD** | Concepto de Dominio (Capítulo 4) |
| **CEPAL** | Comisión Económica para América Latina y el Caribe |
| **CIAF** | Institución de educación superior — Escuela de Ingeniería |
| **DANE** | Departamento Administrativo Nacional de Estadística |
| **DC** | Decisión Constitucional (§0.1) |
| **DNP** | Departamento Nacional de Planeación |
| **ERP** | Sistema de planificación de recursos empresariales |
| **HU** | Historia de Usuario (Capítulo 6) |
| **KPI** | Indicador operativo (Capítulo 10) |
| **MinCIT** | Ministerio de Comercio, Industria y Turismo |
| **MVP** | Producto mínimo viable |
| **ODS** | Objetivos de Desarrollo Sostenible |
| **OIT** | Organización Internacional del Trabajo |
| **PN** | Proceso de Negocio (Capítulo 3) |
| **PR** | Principio de diseño de Roles (§2.1) |
| **PYME** | Pequeña y mediana empresa |
| **QR** | Código de respuesta rápida — identificador principal `[DC-08]` |
| **RF** | Requisito Funcional (Capítulo 7) |
| **RG** | Riesgo Funcional (Capítulo 11) |
| **RN** | Regla de Negocio (Capítulo 9) |
| **RNF** | Requisito No Funcional (Capítulo 8) |
| **SKU** | Unidad de mantenimiento de existencias `[CD-05]` |
| **UTP** | Universidad Tecnológica de Pereira |

## 13.3 Balance de trazabilidad del documento

| Etiqueta | Significado | Elementos aprox. | Proporción |
|---|---|:--:|:--:|
| `[MON §n]` | Trazable a la monografía | 168 | 34 % |
| `[AUD x]` | Derivado de la Auditoría Fase 0 | 61 | 12 % |
| `[DC-n]` | Impuesto por decisión constitucional | 84 | 17 % |
| `[NUEVO]` | **Nuevo aporte derivado de la evolución del proyecto** | 182 | 37 % |

> **Interpretación.** Que el 37 % del documento sea nuevo aporte no es una desviación: es la medida exacta de la distancia entre un estudio conceptual y una especificación de producto. La monografía aporta el **dominio del problema**; toda la capa operativa —procesos, estados, reglas, roles operativos— es necesariamente nueva y se declara como tal `[Regla Innegociable 3]`.

## 13.4 Resumen cuantitativo

| Capítulo | Elemento | Cantidad |
|---|---|:--:|
| 0 | Decisiones constitucionales | 8 |
| 1 | Objetivos del producto | 12 |
| 1 | Diferenciadores | 12 |
| 2 | Roles oficiales | 5 |
| 2 | Principios de diseño de roles | 6 |
| 2 | Funciones en la matriz de segregación | 37 (36 + 1 nueva en la v1.3; «Consultar valorización» figura como retirada) |
| 3 | Procesos de negocio modelados | 14 |
| 3 | Excepciones documentadas | 76 |
| 4 | Conceptos de dominio definidos | 49 |
| 5 | Módulos funcionales | 20 |
| 6 | Historias de usuario | 114 |
| 7 | Requisitos funcionales | 184 |
| 8 | Requisitos no funcionales | 47 |
| 9 | Reglas de negocio | 68 |
| 10 | Indicadores operativos | 24 |
| 11 | Riesgos funcionales | 42 |
| 12 | Elementos de backlog | 75 |

## 13.5 Cumplimiento de las restricciones de la fase

| Restricción | Estado |
|---|---|
| No escribir código | ✅ Cero líneas de código |
| No elegir tecnologías | ✅ Ninguna tecnología, marco de trabajo ni producto nombrado |
| No diseñar base de datos | ✅ El Cap. 4 define vocabulario, no estructura de datos |
| No hacer arquitectura | ✅ Los módulos son agrupaciones funcionales, no componentes técnicos |
| No hacer diagramas C4 / UML / ERD | ✅ Los dos esquemas incluidos (§4.7 mapa de vocabulario, §5.2 matriz módulo×proceso) son de dominio funcional, no notaciones técnicas |
| No definir endpoints | ✅ Ninguno |
| No usar el nombre de la empresa | ✅ Se habla de empresa de estudio / empresa piloto `[DC-01]` |
| No inventar funcionalidades | ✅ Todo elemento traza a la monografía, a la auditoría, a una decisión constitucional, o se declara explícitamente como nuevo aporte |
| No incorporar IA al MVP | ✅ `[DC-07]` La IA aparece únicamente en el Horizonte 4 — Investigación futura, condicionada a autorización |
| Respetar las exclusiones de alcance | ✅ Ventas, compras completas, producción, contabilidad, nómina, CRM y facturación quedan fuera; las fronteras se declaran explícitamente en M-07, M-08, PN-10, CD-35 y RN-048 |

## 13.6 Asuntos que siguen abiertos

Estos puntos **no bloquean la aprobación de esta especificación**, pero deben resolverse antes de las fases posteriores.

| # | Asunto | Pregunta de la Fase F | Bloquea |
|---|---|---|---|
| 1 | Definición legal de PYME para el proyecto | A-03 | Dimensionamiento del mercado |
| 2 | Delimitación de «sector textil» | A-04 | Selección de la empresa piloto |
| 3 | Municipios que integran el ámbito geográfico | A-05 | Alcance del estudio |
| 4 | Autorización de contacto con empresas reales | V-01 | **Fase 3 completa** |
| 5 | Levantamiento de la línea base | V-03 | **Demostración de impacto** |
| 6 | Qué ocurre si el piloto no alcanza las cifras citadas | V-06 | Criterio de aprobación |
| 7 | Verificación de las nueve fuentes ausentes | I-03 | Defensa académica |
| 8 | Resolución de las contradicciones estadísticas | I-04, I-05 | Defensa académica |
| 9 | Reproyección del horizonte temporal | I-09 | Vigencia de las proyecciones |
| 10 | Entregable mínimo aprobatorio | S-15 | **Resuelto en la v1.2 (`[DEC-01]`): Núcleo, con 1 bodega piloto** |
| 11 | Renumeración canónica de las reglas de negocio | — | **Resuelto en la v1.3 (`[DEC-03]`, §9.17)** |
| 12 | Calibración de los valores numéricos de los RNF | — | Requiere línea base |

## 13.7 Control de versiones

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.0 | 5 de septiembre de 2026 | Emisión inicial. Cubre los doce capítulos exigidos y el marco normativo. | Emitido para revisión del Director |
| 1.1 | 29 de septiembre de 2026 | Cierre del CP-04: decisiones DF5-01, DF5-02, DF5-03 y DF5-05 (ver «Control de cambios de la versión 1.1»); 3 reglas nuevas (§9.15) | Validado técnicamente; aprobación pendiente (DEC-01…DEC-09, HD-25) |
| 1.2 | 30 de septiembre de 2026 | DEC-01 = A (Núcleo, 1 bodega) con la capa de trazabilidad por pieza: Q-11, F-1…F-6, Q-09, Q-10 (ver «Control de cambios de la versión 1.2»); 7 HU, 9 RF, 6 reglas y 1 concepto nuevos | Borrador; conservada sin cambios |
| 1.3 | 30 de septiembre de 2026 | Respuestas a DEC-02…DEC-09 (ver «Control de cambios de la versión 1.3»); 4 HU y 13 RF nuevos; fe de erratas de las reglas (§9.17) | Borrador; validación técnica y acta de DEC-08 pendientes |

### Documentos relacionados

| Documento | Relación | Estado |
|---|---|---|
| `MONOGRAFÍA COLBASOFT.docx` | **Fuente de Verdad** | Íntegra, sin modificación `[Regla Innegociable 1]` |
| `AUDITORIA_FUNDACIONAL_COLBASOFT.md` | Documento antecesor — Fase 0 | Aprobado |
| `COLBASOFT_SPEC v1.3` | **Este documento** — Fase 2, con las respuestas a DEC-02…DEC-09 | Borrador; aprobación pendiente |
| `COLBASOFT_SPEC v1.2` | Versión anterior — auditoría de DEC-01 | Borrador; conservada sin cambios |
| `COLBASOFT_SPEC v1.1` | Versión anterior — cierre del CP-04 | Validado técnicamente; conservada sin cambios |
| `04_CP04_AUDITORIA/04_CP04_CIERRE.md` | Registro de las decisiones DF5 que originan la v1.1 | Emitido |
| Levantamiento AS-IS | Fase 3 del roadmap | Pendiente — bloqueado por V-01 |
| Matriz de trazabilidad requisito ↔ monografía | Fase 4 del roadmap | Pendiente |
| Diseño de solución | Fase 5 del roadmap | No iniciado — habilita arquitectura y tecnologías |

---

*COLBASOFT_SPEC v1.3 — Especificación Funcional de Producto*
*5 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) · 30 de septiembre de 2026 (v1.2 y v1.3)*
*La monografía original permanece sin modificaciones.*
