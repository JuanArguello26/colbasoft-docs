
---

# CAPÍTULO 1 — INTRODUCCIÓN

## 1.1 Propósito

Este documento es la **Especificación de Requisitos de Software (SRS)** de COLBASOFT. Su propósito es:

1. Constituir el **acuerdo verificable** entre el Director del Proyecto, el equipo de desarrollo y la empresa de estudio sobre **qué debe hacer el sistema** y **cuándo se considera terminado el MVP**.
2. Servir de **entrada única y trazable** para las fases posteriores del roadmap: diseño de solución (arquitectura y modelo de datos, Fase 5), construcción (Fase 6) y validación de impacto (Fase 7).
3. Preservar la **cadena de trazabilidad completa** Monografía → Auditoría → SPEC → SRS, de modo que ningún requisito quede huérfano de su fundamento académico (riesgo RG-42 del SPEC).

El SRS no diseña la solución: describe **el comportamiento requerido**, no cómo se construye.

## 1.2 Alcance

### 1.2.1 Producto

**COLBASOFT** es una plataforma web (responsive y tablet) para la gestión de inventarios y la logística de bodega de PYMES textiles del Eje Cafetero, que sustituye el cuaderno y la hoja de cálculo suelta por un registro digital único, trazable y auditable, con identificación por QR y con «inteligencia» entendida exclusivamente como **automatización por reglas de negocio y analítica por indicadores** `[DC-07]`.

### 1.2.2 Dentro del alcance (MVP) `[DC-02]`

Gestión de inventarios · logística de bodega · trazabilidad · kardex · entradas · salidas · ajustes · conteos · transferencias · reportes · alertas · dashboard operativo; y, como capacidades de soporte indispensables, acceso, usuarios y roles, catálogo, lotes, estructura de bodega, identificación QR, novedades, auditoría y bitácora, parámetros y notificaciones/tareas. En total, **20 módulos funcionales (M-01…M-20)**.

### 1.2.3 Fuera del alcance `[DC-03]` `[DC-07]`

| Excluido | Razón |
|---|---|
| Ventas, facturación (incluida la electrónica) | DC-03 |
| Compras completas (el documento de entrada **no** es una orden de compra) | DC-03 |
| Producción | DC-03 |
| Contabilidad y valorización monetaria del inventario | DC-03 (ver H-07 y DEC-07) |
| Nómina y CRM | DC-03 |
| **Toda** inteligencia artificial (generativa o no), aprendizaje automático, predicción de demanda | DC-07 |
| Aplicación móvil nativa | DC-05 |
| Diseño de tableros analíticos (se resuelve en la herramienta externa) | DC-06 |
| Código, base de datos, arquitectura, ERD/UML, endpoints, APIs, frameworks, tecnologías | Fases posteriores |

### 1.2.4 Beneficios y objetivos del producto

Los objetivos del producto OP-01…OP-12 (SPEC §1.5) se conservan; los tres primeros beneficios medibles son los que propone la monografía en su Cap. 8.2 y **no llevan meta numérica**, porque una meta solo puede fijarse contra la línea base de la empresa piloto, que aún no existe `[AUD C.2.4]`:

| Indicador de la monografía | KPI |
|---|---|
| Exactitud del inventario | KPI-01 |
| Tiempos de registro | KPI-05 |
| Frecuencia de errores | KPI-08 |

## 1.3 Audiencia

| Lector | Uso del SRS |
|---|---|
| **Director del Proyecto** | Aprobar el alcance, resolver las decisiones DEC-01…DEC-09, aceptar el MVP |
| **Asesor académico** | Verificar la coherencia con la monografía y el rigor de la trazabilidad |
| **Equipo de desarrollo (3 autores)** | Insumo para diseño de solución, construcción y pruebas |
| **Equipo de pruebas / validación** | Derivar casos de prueba de los escenarios Gherkin y de los criterios del Cap. 12 |
| **Empresa de estudio** `[DC-01]` | Confirmar que los requisitos reflejan su operación real (validación AS-IS pendiente) |
| **Jurado** | Evaluar la trazabilidad monografía → producto |

## 1.4 Convenciones

### 1.4.1 Palabras normativas

**«debe»** = requisito obligatorio · **«no debe»** = prohibición · **«puede»** = opcional. Los requisitos se redactan en forma «El sistema debe …».

### 1.4.2 Etiquetas de origen (sistema de trazabilidad)

| Etiqueta | Significado |
|---|---|
| `[MON §n]` | Trazable a un apartado de la monografía (numeración de su Tabla de Contenido) |
| `[AUD x]` | Derivado de un hallazgo de la Auditoría Fase 0 |
| `[DC-n]` | Impuesto por una decisión constitucional del Director |
| `[PR-n]` | Principio de diseño de roles (§2.1 del SPEC) |
| `[NUEVO]` | Nuevo aporte del SPEC, sin correlato en la monografía |
| **`[SRS]`** | **Derivado o normalizado en esta fase** (IDs, MoSCoW, mapeos, Gherkin, casos de uso, CRUD). Requiere validación del Director |

La columna «Origen» de RF, RNF y RN reproduce **literalmente** las etiquetas del SPEC.

### 1.4.3 Identificadores permanentes

Los IDs del SPEC eran secuenciales por capítulo y no sobrevivían a cambios de orden (p. ej. §9.13 de reglas). El SRS asigna **IDs permanentes por dominio**. Una vez emitido este documento, **un ID no se reutiliza ni se renumera**: un requisito retirado se marca «Retirado», nunca se borra. La equivalencia con los IDs del SPEC («legacy») se conserva en cada elemento y en el Anexo A.

| Elemento | Formato | Ejemplo | Dominios |
|---|---|---|---|
| Historia de usuario | `HU-<DOM>-nnn` | `HU-ENT-003` | 20 dominios, uno por módulo |
| Requisito funcional | `RF-<DOM>-nnn` | `RF-KDX-001` | 20 dominios, uno por módulo |
| Requisito no funcional | `RNF-<CAT>-nnn` | `RNF-REN-001` | SEG · DSP · REN · ESC · ACS · AUD · USA · TAB · NAV |
| Regla de negocio | `RN-<DOM>-nnn` | `RN-EXI-001` | 13 dominios de negocio |
| Caso de uso | `CU-nn` | `CU-06` | — |
| KPI | `KPI-nn` | `KPI-01` | Se conserva (ya era estable) |
| Proceso, concepto, módulo, riesgo, decisión | `PN-nn` · `CD-nn` · `M-nn` · `RG-nn` · `DC-nn` | — | Se conservan del SPEC |

**Dominios de HU y RF (uno por módulo):**

| Módulo | Dominio | Módulo | Dominio | Módulo | Dominio |
|---|---|---|---|---|---|
| M-01 Acceso | **ACC** | M-08 Salidas | **SAL** | M-15 Alertas | **ALE** |
| M-02 Usuarios y Roles | **USR** | M-09 Movimientos y Transferencias | **MOV** | M-16 Reportes | **REP** |
| M-03 Catálogo | **CAT** | M-10 Ajustes | **AJU** | M-17 Dashboard | **DSH** |
| M-04 Lotes | **LOT** | M-11 Conteos | **CNT** | M-18 Auditoría y Bitácora | **AUD** |
| M-05 Estructura de Bodega | **BOD** | M-12 Novedades | **NOV** | M-19 Parámetros | **PAR** |
| M-06 Identificación QR | **QRC** | M-13 Consulta de Existencia | **INV** | M-20 Notificaciones y Tareas | **TAR** |
| M-07 Entradas | **ENT** | M-14 Kardex y Trazabilidad | **KDX** | | |

### 1.4.4 Prioridad: del SPEC a MoSCoW `[SRS]`

El SPEC prioriza con P0–P3. El SRS conserva ese valor y agrega su equivalente MoSCoW por una regla **mecánica y reversible** (no se reclasifica ningún elemento):

| Prioridad SPEC | MoSCoW | Significado |
|---|---|---|
| **P0 — Crítico** | **Must** | Sin esto el MVP no existe |
| **P1 — Alto** | **Should** | Necesario para operación real en la empresa piloto |
| **P2 — Medio** | **Could** | Aporta valor; el sistema funciona sin ello |
| **P3 — Bajo** | **Won't (esta versión)** | Candidato a versión posterior (el SPEC no tiene ningún elemento P3) |

### 1.4.5 Horizonte de entrega (SPEC §12) `[SRS]`

Cada HU y RF que el backlog del SPEC (§12.3) ubica en la versión 1.1 lleva la marca **H2**; el resto es **H1** (MVP). La **importancia** (MoSCoW) y el **horizonte** son atributos distintos: el SRS no descarta ningún requisito por estar en H2 (ver H-08 y DEC-01). Las etiquetas «H1/H2» designan **horizontes de entrega**; no deben confundirse con las hipótesis H1–H10 de la Auditoría (que este SRS no usa), con los hallazgos «H-nn» (con guion) del Cap. 0 ni con los diferenciadores «D-nn» del SPEC: las decisiones que este SRS solicita al Director se llaman **«DEC-nn»**.

### 1.4.6 Escenarios Gherkin `[SRS]`

Los criterios de aceptación de cada historia se expresan con la sintaxis Gherkin en español (`Característica`, `Escenario`, `Dado`, `Cuando`, `Entonces`, `Y`). **Cada criterio de aceptación numerado del SPEC corresponde a exactamente un escenario** (`C1`, `C2`, …), de modo que se conserva la equivalencia 1:1 (462 criterios → 462 escenarios). Los valores numéricos de desempeño no se repiten en los escenarios: se remiten al RNF correspondiente.

### 1.4.7 Convención sobre valores numéricos

Los valores numéricos de los RNF (p. ej. tiempos de respuesta) son **objetivos de diseño propuestos por el SPEC**, no metas validadas. Su calibración definitiva requiere la línea base de la empresa piloto `[AUD C.2.4]` (pendiente #12 del §0.5). **El SRS no introduce ninguna meta numérica nueva.**

## 1.5 Definiciones, acrónimos y abreviaturas

Los 48 conceptos de dominio están definidos operativamente en el **Capítulo 4 del SPEC** (CD-01…CD-48) y **no se redefinen aquí** (una definición duplicada podría divergir). La tabla siguiente recoge únicamente los conceptos que el SRS usa con más frecuencia y remite a su definición canónica.

| Término | Definición resumida | Canónica |
|---|---|---|
| **Unidad de Inventario** | Combinación SKU + Lote + Ubicación: la entidad que el sistema controla | CD-07 |
| **Existencia** | Suma algebraica de todos los movimientos de una unidad; nunca un valor ingresado | CD-18 |
| **Inventario Disponible** | Existencia menos reservado e inmovilizado (la cifra que ve el operario) | CD-19 |
| **Movimiento** | Hecho registrado que altera la existencia o la ubicación; inmutable una vez confirmado | CD-28 |
| **Kardex** | Registro cronológico, completo e inmutable de los movimientos; fuente de verdad de la existencia | CD-37 |
| **Trazabilidad** | Capacidad de responder qué, cuánto, dónde, quién, cuándo y por qué, para cualquier unidad y momento; alcance MVP: entrada a bodega → salida de bodega | CD-21 |
| **Ajuste** | Movimiento que modifica la existencia sin contrapartida física; exige motivo tipificado y aprobación de un tercero | CD-33 |
| **Motivo tipificado** | Causa seleccionada de una lista cerrada; el texto libre nunca lo sustituye | CD-36 |
| **Bitácora de auditoría** | Registro inmutable de toda acción relevante del sistema (distinto del kardex) | CD-47 |
| **Novedad** | Reporte de una anomalía física observada por un operario; nunca se elimina, se cierra | CD-48 |

| Sigla | Significado | Sigla | Significado |
|---|---|---|---|
| **AS-IS / TO-BE** | Proceso actual / proceso propuesto | **MVP** | Producto mínimo viable |
| **CD** | Concepto de Dominio | **MoSCoW** | Must / Should / Could / Won't |
| **CU** | Caso de Uso | **PN** | Proceso de Negocio |
| **DC** | Decisión Constitucional | **PR** | Principio de diseño de Roles |
| **HU** | Historia de Usuario | **PYME** | Pequeña y mediana empresa |
| **KPI** | Indicador operativo | **QR** | Código de respuesta rápida |
| **RF / RNF** | Requisito Funcional / No Funcional | **RG** | Riesgo Funcional (SPEC Cap. 11) |
| **RN** | Regla de Negocio | **SKU** | Unidad de mantenimiento de existencias |
| **RI** | Regla Innegociable (Auditoría) | **SRS** | Software Requirements Specification |

## 1.6 Referencias documentales

| # | Documento | Uso |
|---|---|---|
| 1 | `MONOGRAFÍA  COLBASOFT.docx` — Argüello, J. E.; Osorio, B. A.; Guerrero, B. J. (27 nov. 2025). *Automatización del proceso logístico en la gestión de inventarios para PYMES del sector textil del Eje Cafetero.* CIAF | Fuente de verdad (inmutable) |
| 2 | `AUDITORIA_FUNDACIONAL_COLBASOFT.md` (1 sep. 2026) | Vacíos, riesgos académicos, roadmap, preguntas al Director |
| 3 | `COLBASOFT_SPEC_v1.1.md` (5 sep. 2026; v1.1 del 29 sep. 2026) | Fuente principal del SRS |
| 4 | ISO/IEC/IEEE 29148 — *Systems and software engineering — Life cycle processes — Requirements engineering* | Estructura de referencia, adaptada |

**Correspondencia con la estructura de la norma (adaptada):**

| Elemento de ISO/IEC/IEEE 29148 (SRS) | Ubicación en este documento |
|---|---|
| Introducción: propósito, alcance, definiciones, referencias | Cap. 1 |
| Descripción general: perspectiva, funciones, características del usuario, restricciones, supuestos | Cap. 2 y Cap. 3 |
| Requisitos específicos: funcionales, de interfaz de usuario, desempeño, restricciones de diseño, atributos | Caps. 4–8 |
| Verificación | Escenarios Gherkin (Cap. 5), verificación por RNF (Cap. 7), criterios del MVP (Cap. 12) |
| Trazabilidad | Cap. 9 y Anexo A |
| Apéndices | Anexos A, B y C |

---

**ESTADO DEL CAPÍTULO 1**

| | |
|---|---|
| **Completado** | Propósito · alcance · audiencia · convenciones (IDs, MoSCoW, horizonte, Gherkin) · definiciones · referencias |
| **Pendiente** | Nada dentro del capítulo |
| **Riesgos encontrados** | Los valores numéricos de los RNF son propuestas sin línea base (RG-36) |
| **Dependencias** | Capítulo 0 (hallazgos que modifican la lectura de cifras) |
