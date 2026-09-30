
---

# CAPÍTULO 12 — CRITERIOS DE ACEPTACIÓN DEL MVP

> Define **cuándo el MVP está terminado**. Los criterios se derivan del objetivo del MVP declarado en el SPEC (§12.2), de los criterios de cierre del roadmap de la Auditoría y de los requisitos de este SRS `[SRS]`. **No se fija ninguna meta numérica nueva**: donde el SPEC no la define, el criterio remite a la calibración con línea base (pendiente #12) o a una decisión del Director.

## 12.1 Definición de «MVP terminado»

**Objetivo del MVP (SPEC §12.2):** *que la bodega de la empresa piloto opere íntegramente en el sistema, sin cuaderno, con trazabilidad completa y con capacidad de medir su propio impacto.*

Por tanto, el MVP **está terminado** cuando se cumplen simultáneamente los criterios de las nueve dimensiones del §12.3 (completitud funcional, reglas, no funcionales, medición, adopción, independencia de la auditoría, trazabilidad documental, frontera de alcance y capacitación) **y** no se cumple ninguno de los criterios de **no aceptación** del §12.6.

## 12.2 Niveles de entrega y decisión DEC-01

El SPEC ubica 19 HU y 19 RF en el Horizonte 2 (v1.1) y, a la vez, mantiene en el alcance MVP (DC-02) las transferencias y los conteos (H-08). **El 30 de septiembre de 2026 el Director resolvió DEC-01 = A**: el «entregable mínimo aprobatorio» (S-15) es el **MVP-Núcleo**, con 1 bodega piloto. Este SRS conserva **dos umbrales** de aceptación, pero solo el primero es aprobatorio:

| Umbral | Contenido | HU | RF |
|---|---|:--:|:--:|
| **MVP-Núcleo (H1) — umbral aprobatorio `[DEC-01]`** | Todo lo que el backlog del SPEC declara Horizonte 1, incluida la trazabilidad por pieza (elemento 40, v1.2): 84 HU y 143 RF de la v1.1 más 7 HU y 9 RF de la v1.2 | **91** | **152** |
| **MVP-Completo (H1 + H2)** | Todo el alcance DC-02, incluidos los 19 HU / 19 RF del Horizonte 2 (transferencias, conteo general, inmovilización de lotes, escalamientos, carga masiva, existencia histórica, reportes programados, exportación analítica, dashboard del Coordinador, código de barras secundario, criterios de asignación, lotes por antigüedad, reasignación de tareas, alerta de ajustes recurrentes) | **110** | **171** |

**Regla de aceptación:** el MVP se acepta con el **MVP-Núcleo** `[DEC-01]`. Lo que el MVP-Completo añade (Horizonte 2: transferencias, conteo general y demás) **no es criterio de aprobación**; queda como entrega posterior.

Distribución de las HU y RF por prioridad y horizonte `[SRS]`:

| MoSCoW | HU total | de ellas H1 | de ellas H2 | RF total | de ellos H1 | de ellos H2 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| **Must** (P0) | 40 | 38 | 2 | 82 | 81 | 1 |
| **Should** (P1) | 55 | 45 | 10 | 71 | 58 | 13 |
| **Could** (P2) | 15 | 8 | 7 | 18 | 13 | 5 |
| **Won't** (P3) | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **110** | **91** | **19** | **171** | **152** | **19** |

## 12.3 Criterios de aceptación por dimensión

### Dimensión 1 — Completitud funcional

| ID | Criterio | Evidencia de verificación |
|---|---|---|
| **CA-01** | **Todas las HU *Must* del umbral elegido están aceptadas:** todos sus escenarios Gherkin se ejecutan y pasan | Informe de ejecución de escenarios por HU (498 escenarios en total; los del umbral elegido son obligatorios) |
| **CA-02** | **Todos los RF *Must* del umbral elegido están verificados** por prueba o inspección | Matriz RF → prueba (Cap. 9 §9.4) |
| **CA-03** | **Las HU y RF *Should* del umbral elegido están aceptadas**, o su exclusión fue aprobada por escrito por el Director con su riesgo | Acta de decisión |
| **CA-04** | Los 24 casos de uso del Cap. 4 pueden recorrerse de extremo a extremo con datos de la empresa piloto (CU-19 solo si DEC-05 lo incorpora) | Registro de recorrido por caso de uso |
| **CA-05** | Los **cinco procesos del núcleo transaccional** —entrada, salida, movimiento interno, ajuste y conteo— operan **sin cuaderno** durante el período de prueba (OP-01) | Cero movimientos registrados fuera del sistema (verificación de campo) |

### Dimensión 2 — Reglas de negocio

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-06** | **Cada una de las 60 reglas estructurales** se verifica con al menos una prueba **negativa** (el sistema rechaza la operación que la viola) y una positiva | Matriz RN → prueba (Cap. 9 §9.5) |
| **CA-07** | **Cada una de las 22 reglas configurables** se verifica con el umbral configurado y con el comportamiento antes y después del umbral | Ídem |
| **CA-08** | Las reglas del núcleo no configurable de §9.1 (@RN001, @RN009, @RN012, @RN023, @RN029, @RN040, @RN041, @RN061, @RN063, @RN065) **no aparecen como parametrizables** en Parámetros y Configuración (HU-PAR-003) | Inspección de M-19 |
| **CA-09** | **Ningún rol —incluido el Administrador— dispone de una función de edición o eliminación** de un movimiento confirmado, de la bitácora ni de ningún elemento (@RN012, @RN061, @RN063) | Búsqueda exhaustiva de funciones de escritura (@RNF031) |
| **CA-10** | La verificación de integridad «existencia = suma de movimientos» (@RN065) **no reporta discrepancias** al cierre de la prueba (KPI-09 = 0, objetivo estructural) | Ejecución de la verificación global (@RNF034) |

### Dimensión 3 — Requisitos no funcionales

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-11** | **Cada RNF (47) fue verificado por el método que declara su columna «Verificación»** | Registro de verificación por RNF (Cap. 7) |
| **CA-12** | Los objetivos numéricos de rendimiento (RNF-REN-001…006) **se calibran contra la línea base y se aprueban antes de usarse como umbral de aceptación**; no se aceptan valores no calibrados | Acta de calibración (pendiente #12) |
| **CA-13** | La categoría de **usabilidad** (RNF-USA-001…007) se verifica con **usuarios reales de perfil Auxiliar sin formación previa** | Prueba de usabilidad con Auxiliares |
| **CA-14** | El cumplimiento de la protección de datos personales (@RNF008) fue **revisado antes de producción** | Revisión de cumplimiento |
| **CA-15** | Se ejecutó al menos **una restauración de respaldo de prueba** (@RNF012) y una prueba de recuperación acotada (@RNF013) | Registro de restauración |

### Dimensión 4 — Medición del propio impacto (compromiso ante el jurado)

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-16** | **KPI-01, KPI-05 y KPI-08 se calculan** con la fórmula del Cap. 9 y se pueden comparar contra la **línea base** | Reporte de los tres KPI |
| **CA-17** | **Existe línea base** de los tres KPI antes de iniciar el piloto (V-03) | Documento de línea base (**precondición externa al software**) |
| **CA-18** | El informe de impacto **reporta el resultado íntegro, favorable o no** (V-06, RG-35). *El software se acepta por cumplir sus requisitos, no por alcanzar las cifras de la literatura* | Informe de impacto |
| **CA-19** | Los 24 KPI son calculables por el sistema; los que dependen de un dato que ningún RF exige capturar (KPI-05, 07, 10, 12, 17, 24; H-12) quedan **explícitamente marcados** «calculable» o «pendiente de DEC-06» | Tabla del Anexo C |
| **CA-20** | El sistema **expone los datos** a la herramienta analítica externa sin diseñar tableros (@RF137, @RF138) | Verificación de la exposición estructurada |

### Dimensión 5 — Adopción (usuario crítico: el Auxiliar)

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-21** | Un **Auxiliar sin experiencia previa** registra una entrada, una salida y un movimiento interno tras una **capacitación breve** (@RNF035) | Prueba con usuarios reales |
| **CA-22** | El Auxiliar **no ve** indicadores de desempeño individual ni comparaciones entre personas (@RNF039, PR-06); la novedad no se contabiliza en contra del reportante (@RF108) | Revisión de todas las pantallas del rol |
| **CA-23** | Todo rechazo del sistema **explica el motivo** en lenguaje comprensible (@RNF038, @RNF029) | Revisión de mensajes de rechazo |
| **CA-24** | Toda operación de registro entrega **confirmación visible** de que quedó guardada (@RNF037) | Revisión de cada operación de escritura |
| **CA-25** | **KPI-24 (adopción) se mide con verificación de campo** y su resultado se reporta al Director (RG-01) | Reporte de adopción |
| **CA-26** | La operación es completa desde **tablet**, sin instalación nativa y con cámara (@RNF042, @RNF043, @RNF044) | Recorrido de las funciones del Auxiliar y del Coordinador en tablet |

### Dimensión 6 — Independencia de la auditoría

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-27** | El **Auditor** ejecuta CU-18 completo (kardex, ajustes, conteos, anulaciones, bitácora, observaciones, exportación) **sin poder modificar el inventario** (@RNF005) | Recorrido con rol Auditor + intentos de escritura rechazados y registrados |
| **CA-28** | **Cero** casos en los que solicitante y aprobador coincidan (HU-AUD-004) y **cero** movimientos sin usuario atribuible | Reporte de auditoría |
| **CA-29** | Toda cuenta corresponde a una persona identificada; **no existen cuentas compartidas** (@RN001) | Revisión de cuentas |

### Dimensión 7 — Trazabilidad documental

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-30** | **100 % de los RF, HU, RNF y RN** tienen ID permanente y aparecen en la matriz de trazabilidad con su fuente `[MON]`, `[AUD]`, `[DC]`, `[NUEVO]` o `[SRS]` | Cap. 9 y Anexo A |
| **CA-31** | **Toda regla estructural y todo RF *Must*** están vinculados a al menos una HU y un escenario de prueba | Cap. 9 §9.4 y §9.5 |
| **CA-32** | Las decisiones DEC-01…DEC-09 del Anexo C están **resueltas o aceptadas por escrito como limitación conocida** | Acta del Director |
| **CA-33** | La **monografía permanece sin modificación** y el SRS no contradice ninguno de sus objetivos (RI-1, RI-6) | Comparación documental |

### Dimensión 8 — Frontera de alcance

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-34** | **No existe** ninguna función de ventas, compras completas, producción, contabilidad, nómina, CRM o facturación (DC-03); ninguna pantalla de entrada o salida solicita precio, cliente, factura ni documento comercial (@RN048, @RF049, @RF062) | Inspección de pantallas y datos solicitados |
| **CA-35** | **No existe** ningún componente de inteligencia artificial (DC-07): las alertas se generan solo por reglas y umbrales (@RF128) | Inspección de las reglas de alerta |
| **CA-36** | El sistema **no incluye el diseño de tableros analíticos** (DC-06) ni una aplicación móvil nativa (DC-05) | Inspección |

### Dimensión 9 — Capacitación y adopción organizacional

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-37** | La **capacitación práctica** del personal forma parte de la entrega y se realizó `[MON §8.2]` (R-14, V-09) | Registro de capacitación |
| **CA-38** | Existe un **manual de usuario orientado al perfil real** (Auxiliar, Coordinador, Jefe, Administrador, Auditor) | Manuales entregados |

## 12.4 Criterios de aceptación por bloque del backlog (SPEC §12.2)

| Bloque | Se acepta cuando | Criterios |
|---|---|---|
| **1 · Fundación** | Acceso individual, cinco roles con segregación, catálogo, estructura de bodega, parámetros y QR funcionan y están auditados | CA-01, CA-08, CA-29 |
| **2 · Núcleo transaccional** | El kardex es inmutable y toda existencia se deriva de él; entradas, salidas y movimientos operan; no hay existencia negativa | CA-05, CA-09, CA-10 |
| **3 · Control** | Los ajustes exigen motivo y aprobación de un tercero; bitácora inmutable; Auditor de solo lectura | CA-06, CA-27, CA-28 |
| **4 · Medición** | El conteo cíclico opera sin detener la bodega; el contador no ve lo esperado; KPI-01, KPI-05, KPI-08 calculables | CA-16, CA-17, CA-19 |
| **5 · Adopción** | Tablet, escaneo, confirmación visible, panel de tareas, sin indicadores individuales, novedades sin imputación, sincronización | CA-21…CA-26 |
| **6 · Anticipación** | Las alertas por reglas y umbrales, el dashboard del Jefe y el cierre de jornada operan (este último sujeto a DEC-05) | CA-04, CA-35 |

## 12.5 Definición de terminado (DoD) por tipo de elemento

| Elemento | Está terminado cuando |
|---|---|
| **Historia de usuario** | Todos sus escenarios Gherkin pasan; sus RF están verificados; las reglas que la gobiernan están cubiertas por prueba negativa y positiva; su trazabilidad está en el Cap. 9 |
| **Requisito funcional** | Fue verificado por prueba o inspección, con evidencia archivada, y sus dependencias están satisfechas |
| **Requisito no funcional** | Fue verificado por el método de su columna «Verificación» y, si es numérico, contra un valor calibrado |
| **Regla de negocio** | Existe evidencia de rechazo de la operación que la viola (estructural) o de su comportamiento antes y después del umbral (configurable) |
| **Caso de uso** | Se recorrieron el flujo principal, cada flujo alterno y cada excepción |
| **KPI** | La fórmula se calcula con el dato capturado y se contrasta con una verificación manual sobre una muestra |

## 12.6 Criterios de NO aceptación (bloqueantes)

El MVP **no se acepta**, aunque el resto de los criterios se cumplan, si se verifica cualquiera de estos hechos:

1. Es posible dejar la existencia de una unidad por debajo de cero por cualquier vía (@RN009).
2. Es posible editar o eliminar un movimiento confirmado, un registro de la bitácora o cualquier elemento maestro, con cualquier rol (@RN012, @RN061, @RN063).
3. Un usuario puede aprobar una solicitud que él mismo originó, o el Auditor puede escribir en el inventario (@RN023, @RN064).
4. Existen acciones sin usuario atribuible o cuentas compartidas (@RN001).
5. La verificación «existencia = suma de movimientos» reporta discrepancias sin explicación (@RN065).
6. Un contador puede ver la cantidad esperada antes o después de contar (@RN040).
7. Se implementó alguna función excluida por DC-03 o alguna forma de IA (DC-07).
8. El Auxiliar ve indicadores de desempeño individual (PR-06).
9. Existen dos o más movimientos registrados fuera del sistema durante el período de prueba sin explicación (OP-01, RG-01).

## 12.7 Condiciones previas al piloto (externas al software)

No son criterios de aceptación del software, pero **sin ellas el MVP no puede demostrar su impacto**:

| Condición | Pregunta del SPEC | Estado |
|---|---|---|
| Autorización de contacto con empresas reales | V-01 | 🔴 Abierta |
| Levantamiento de la línea base de KPI-01, KPI-05, KPI-08 | V-03 | 🔴 Abierta |
| Definición de PYME, sector textil y municipios | A-03, A-04, A-05 | 🔴 Abiertas |
| Criterio si el piloto no alcanza las cifras citadas | V-06 | 🔴 Abierta |
| Entregable mínimo aprobatorio | S-15 | 🔴 Abierta (DEC-01) |
| Levantamiento de la infraestructura real (tablets, cámara, impresión, conectividad) | C.2.7 | 🟡 Por hacer |

---

**ESTADO DEL CAPÍTULO 12**

| | |
|---|---|
| **Completado** | Definición de «MVP terminado» · dos umbrales de entrega · 38 criterios en 9 dimensiones · criterios por bloque · DoD · criterios de no aceptación · condiciones previas |
| **Pendiente** | Decisión DEC-01 (umbral aprobatorio) · calibración de valores numéricos de RNF (pendiente #12) · línea base (V-03) |
| **Riesgos encontrados** | RG-35 (el piloto puede no alcanzar las cifras citadas) · RG-36 (sin línea base no hay demostración) · RG-01 (operación por fuera del sistema) |
| **Dependencias** | Cap. 9 (trazabilidad), Cap. 7 (RNF), Cap. 8 (reglas), Anexo C (decisiones) |
