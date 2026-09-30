# SRS_COLBASOFT v1.4
## Especificación de Requisitos de Software (Software Requirements Specification)

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | SRS_COLBASOFT |
| **Versión** | 1.4 |
| **Fase** | Fase 3 del proyecto — Especificación de Requisitos de Software (SRS) |
| **Fecha** | 28 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) · 30 de septiembre de 2026 (v1.2, v1.3 y v1.4) |
| **Estado** | **Borrador v1.4** (30-sep-2026): registra las respuestas a DEC-01…DEC-09, H-19, H-20, HD-29 y HD-30. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar y pendiente HD-28 |
| **Versión anterior** | `SRS_COLBASOFT_v1.3.md`, `SRS_COLBASOFT_v1.2.md` (30-sep-2026), `SRS_COLBASOFT_v1.1.md` (29-sep-2026) y `SRS_COLBASOFT_v1.0.md` (28-sep-2026), conservadas sin cambios |
| **Norma de referencia** | ISO/IEC/IEEE 29148 (Ingeniería de requisitos), adaptada al proyecto y en español |
| **Jerarquía documental** | Monografía → Auditoría Fundacional → COLBASOFT_SPEC v1.4 → **SRS v1.4** |
| **Fuente de verdad** | `MONOGRAFÍA  COLBASOFT.docx` (íntegra, sin modificación) |
| **Documentos antecesores** | `AUDITORIA_FUNDACIONAL_COLBASOFT.md` (Fase 0) · `COLBASOFT_SPEC_v1.4.md` (Fase 2, con las respuestas a H-19, H-20, HD-29 y HD-30) |
| **Autoría del proyecto** | Juan Esteban Argüello · Brayan Alexander Osorio · Brandon José Guerrero |
| **Institución / asesor** | Escuela de Ingeniería — CIAF · Edwin Andrés Cabrera Arredondo |
| **Alcance de este documento** | Requisitos funcionales, no funcionales, reglas de negocio, casos de uso, historias normalizadas, trazabilidad y criterios de aceptación |
| **Fuera de alcance de este documento** | Código · Base de datos · Arquitectura técnica · ERD/UML · Endpoints/APIs · Frameworks · Tecnologías |

> **Naturaleza del documento.** Este SRS **no crea requisitos nuevos**: normaliza, reorganiza y hace trazable el contenido del COLBASOFT_SPEC v1.4. Aporta identificadores permanentes, prioridad MoSCoW, criterios en Gherkin, casos de uso completos, matrices de trazabilidad y criterios de aceptación del MVP. Todo elemento que este documento deriva (y que el SPEC no traía) se marca con la etiqueta `[SRS]` y se somete a validación del Director. Las brechas que se detectan **se registran como hallazgos y decisiones pendientes; no se resuelven inventando funcionalidad** (Regla Innegociable 3).

## Control de cambios de la versión 1.4

> La v1.4 se regenera desde las mismas fuentes, tras incorporar al SPEC v1.4 las respuestas del Director a **H-19, H-20, HD-29 y HD-30** (30 de septiembre de 2026). La v1.3 se conserva sin cambios en `SRS_COLBASOFT_v1.3.md`.

| Asunto | Respuesta (a) | Efecto en este SRS |
|---|---|---|
| **H-19** | La ubicación se propone con una regla fija en el Núcleo | HU-ENT-006 (criterio 1) y su escenario, RN-MOV-001, CU-08. El hallazgo queda resuelto |
| **H-20** | RF-REP-003 se acota a los 12 KPI del Núcleo; los otros 12 pasan a un RF nuevo | **RF-REP-008** (Horizonte 2); RF-REP-003 (texto); los KPI-02, 03, 04, 06, 07, 10, 12, 15, 18, 20, 22 y 23 se asocian a RF-REP-008. El hallazgo queda resuelto |
| **HD-29** | Una pieza no se divide | Regla nueva **RN-MOV-012**; HU-MOV-001 (criterio 2) y su escenario; RF-MOV-012; CU-10 |
| **HD-30** | Toda la mercancía se controla por piezas | RN-LOT-006 (texto) |

Cifras de la v1.4: requisitos funcionales **184 → 185**, reglas **91 → 92**. No cambian las historias (114), los escenarios (515), los RNF, los KPI ni el Núcleo (94 HU · 164 RF). El Horizonte 2 pasa de 20 a 21 RF.

**Limitación conocida (HD-29).** Una parte de un paquete o bolsa de unidades no puede trasladarse a otra ubicación como movimiento interno, porque exigiría dividir la pieza; la parte que se toma se registra como salida.

## Control de cambios de la versión 1.3

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

## Control de cambios de la versión 1.2

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

## Control de cambios de la versión 1.1

> La v1.1 se regenera desde las mismas fuentes que la v1.0, tras incorporar al SPEC v1.1 las decisiones del **cierre del CP-04** (`04_CP04_AUDITORIA/04_CP04_CIERRE.md`). La v1.0 se conserva sin cambios en `SRS_COLBASOFT_v1.0.md`.

| Decisión | Efecto en este SRS |
|---|---|
| **DF5-01** — el QR de mercancía identifica SKU + Lote | Cambia el texto de RF-QRC-001, RF-QRC-003, RN-IDE-001 y RN-IDE-003, de los criterios de HU-QRC-001, HU-QRC-002, HU-QRC-004 y HU-QRC-005 y de sus escenarios Gherkin. La unidad de inventario sigue definida por SKU + Lote + Ubicación (RN-INT-005, sin cambios) |
| **DF5-02** — la entrada confirmada queda en recepción | Regla nueva **RN-EXI-007** |
| **DF5-03** — la primera ubicación es un movimiento interno | Regla nueva **RN-MOV-010** |
| **DF5-05** — revalidación al sincronizar | Regla nueva **RN-INT-008** |
| **DF5-06** (revisada) — validación técnica | Estado del documento: validado técnicamente; aprobación pendiente de HD-25 y DEC-01…DEC-09 |

No cambia ninguna cifra de historias (103), requisitos funcionales (162), requisitos no funcionales (47), escenarios (462), casos de uso (24) ni KPI (24), ni ningún horizonte H1/H2. Las reglas pasan de 82 a **85**. Los números de capítulo 0 que siguen describen la reconstrucción de contexto de la v1.0 y se conservan como registro histórico.

## Índice general

| Cap. | Título | Contenido |
|---|---|---|
| **0** | Auditoría de Reanudación | Documentos recibidos · versiones · decisiones constitucionales · fases cerradas · pendientes · hallazgos |
| **1** | Introducción | Propósito · alcance · audiencia · convenciones · definiciones · referencias |
| **2** | Visión General del Sistema | Perspectiva funcional · funciones · usuarios · restricciones · supuestos |
| **3** | Actores | Los cinco roles y el Sistema · matriz de permisos funcional |
| **4** | Casos de Uso | 24 casos de uso completos |
| **5** | Historias de Usuario Normalizadas | 114 historias · ID estable · MoSCoW · dependencias · Gherkin |
| **6** | Requisitos Funcionales Normalizados | 185 RF con ID permanente |
| **7** | Requisitos No Funcionales | 47 RNF por categoría con ID permanente |
| **8** | Reglas de Negocio | 82 reglas por dominio con ID permanente |
| **9** | Matriz de Trazabilidad | KPI · objetivo → concepto → historia → RF → regla → KPI |
| **10** | Matriz CRUD | Actores × módulos |
| **11** | Dependencias Funcionales | Módulos que dependen de otros |
| **12** | Criterios de Aceptación del MVP | Cuándo el MVP está terminado |
| **A–C** | Anexos | Equivalencia de IDs · Auditoría interna · Hallazgos, decisiones y riesgos abiertos |

---

# CAPÍTULO 0 — AUDITORÍA DE REANUDACIÓN

> Esta auditoría se ejecutó **antes** de escribir el SRS, tal como exige el Prompt Maestro #003. Se leyeron íntegros los tres documentos adjuntos y se verificaron programáticamente los conteos del SPEC (historias, requisitos, reglas, indicadores) contra sus propias tablas. Donde el SPEC declara un número y sus tablas contienen otro, **prevalece el contenido de las tablas** y la discrepancia se registra como hallazgo.

## 0.1 Qué documentos se recibieron

| # | Documento | Archivo | Versión / estado | Fecha | Extensión | Papel en la jerarquía |
|---|---|---|---|---|---|---|
| 1 | **Monografía original** — *Automatización del proceso logístico en la gestión de inventarios para PYMES del sector textil del Eje Cafetero* | `00_MONOGRAFIA_ORIGINAL/MONOGRAFÍA  COLBASOFT.docx` | Entrega única; **inmutable** | 27 de noviembre de 2025 (Pereira) | 14 apartados · 15 referencias formales · aprox. 17 páginas | **Fuente de verdad.** Estudio de revisión documental; no es una especificación de producto |
| 2 | **Auditoría Fundacional — Fase 0** | `00_AUDITORIA_FASE_0/AUDITORIA_FUNDACIONAL_COLBASOFT.md` | Fase 0 (aprobada según SPEC §0) | 1 de septiembre de 2026 | 980 líneas · Fases A–F | Extiende la monografía sin tocarla: 24 problemas, 22 beneficios, 19 restricciones, 10 hipótesis, 41 vacíos de ingeniería (10 críticos), 44 riesgos académicos, roadmap de 9 fases y 60 preguntas al Director (24 bloqueantes) |
| 3 | **COLBASOFT_SPEC v1.0** | `01_SPEC_FASE_2/COLBASOFT_SPEC_v1.0.md` | v1.0 — el archivo declara «Emitido para revisión del Director»; el Prompt #003 lo declara «auditado y aprobado» (ver H-15) | 5 de septiembre de 2026 | 3.501 líneas · 13 capítulos | **Fuente principal del SRS.** Especificación funcional: 14 procesos, 48 conceptos de dominio, 20 módulos, 103 historias, 162 RF, 47 RNF, reglas de negocio, 24 KPI, 42 riesgos, backlog en 4 horizontes |

**Lo que dice la monografía y determina todo lo demás.** Es un estudio teórico que se autodefine como *revisión documental* y excluye explícitamente la implementación (Cap. 4: «sin proponer soluciones prácticas de implementación»; Cap. 8.1: «Más que desarrollar un sistema completo, buscamos plantear un modelo flexible»). Su descripción funcional más concreta —la semilla de todo el producto— es la recomendación del Cap. 8.2: *«implementar desde el principio aplicativos o sistemas de registro digital que permitan estandarizar entradas, salidas y movimientos de inventario»*, medidos con **exactitud del inventario, tiempos de registro y frecuencia de errores**. Los tres indicadores son el compromiso demostrable del proyecto (KPI-01, KPI-05, KPI-08).

## 0.2 Qué versión representa cada documento y cómo se relacionan

```
MONOGRAFÍA (27-nov-2025, inmutable)
      │  se extiende, nunca se modifica ni se corrige
      ▼
AUDITORÍA FUNDACIONAL — Fase 0 (1-sep-2026)      → detecta vacíos, no los resuelve
      │
      ▼
COLBASOFT_SPEC v1.0 — Fase 2 (5-sep-2026)        → materializa el modelo conceptual que la monografía no presentó (vacío C.1.2)
      │
      ▼
SRS_COLBASOFT v1.0 — Fase 3 (este documento)     → normaliza, hace trazable y define cuándo está terminado
```

| Elemento | Origen | Tratamiento en el SRS |
|---|---|---|
| Dominio del problema (24 problemas P-01…P-24, beneficios B-01…B-22) | Monografía / Auditoría | Se referencia; no se reformula |
| Decisiones DC-01…DC-08, principios PR-01…PR-06 | SPEC | Se conservan como restricciones constitucionales del SRS |
| 103 HU · 162 RF · 47 RNF · 82 RN · 24 KPI · 14 PN · 48 CD · 20 módulos | SPEC | Se reorganizan con IDs permanentes; **ninguno se pierde** (Anexo B) |
| Casos de uso, Gherkin, MoSCoW, dependencias entre historias, mapeo HU↔RF↔KPI, CRUD | **Esta fase** | Etiquetados `[SRS]` |

## 0.3 Decisiones constitucionales detectadas

**a) Reglas Innegociables de la Auditoría (Fase 0)** — vigentes en todo el proyecto:

| # | Regla |
|---|---|
| RI-1 | La monografía no se modifica (ni se corrige ni se reescribe; solo se extiende) |
| RI-2 | No eliminar conceptos esenciales |
| RI-3 | **No inventar funcionalidades** |
| RI-4 | No escribir código |
| RI-5 | No crear arquitectura (habilitada solo desde la Fase 5 del roadmap) |
| RI-6 | No cambiar objetivos sin justificar |
| RI-7 | Todo hallazgo cita el apartado de origen |

**b) Decisiones constitucionales del Director (SPEC §0.1)** — inmodificables:

| # | Decisión | Efecto en el SRS |
|---|---|---|
| **DC-01** | Empresa de estudio sin nombre comercial | Ningún nombre de empresa aparece en el SRS |
| **DC-02** | Alcance MVP cerrado: gestión de inventarios, logística de bodega, trazabilidad, kardex, entradas, salidas, ajustes, conteos, transferencias, reportes, alertas y dashboard operativo | Frontera funcional del SRS |
| **DC-03** | Exclusiones absolutas: ventas, compras completas, producción, contabilidad, nómina, CRM, facturación | Ningún requisito cruza esta frontera |
| **DC-04** | Cinco roles oficiales; no se agregan roles | Capítulo 3 |
| **DC-05** | Web responsive + tablet; sin app móvil nativa | RNF de compatibilidad |
| **DC-06** | Integración con Power BI existirá; no se diseñan dashboards analíticos | El SRS solo exige exposición estructurada de datos |
| **DC-07** | Sin Inteligencia Artificial: «inteligente» = automatización por reglas + analítica | Reglas de negocio y KPI son la «inteligencia» |
| **DC-08** | QR como identificador principal; código de barras solo secundario | Módulo de identificación |

**c) Principios de diseño de roles (SPEC §2.1)**: PR-01 segregación de funciones · PR-02 el Auditor nunca escribe · PR-03 escalada de privilegio explícita · PR-04 el Auxiliar no ve información sensible · PR-05 toda acción atribuida a una persona · PR-06 el sistema registra, no castiga.

**d) Resumen constitucional del Prompt #003 (congelado) frente al SPEC** — conciliación:

| Aspecto | Prompt #003 | SPEC v1.0 | Tratamiento en el SRS |
|---|---|---|---|
| Roles | Los cinco oficiales | DC-04 | ✅ Coinciden |
| Plataforma | Web responsive + tablet | DC-05 | ✅ Coinciden |
| Inteligencia | Solo reglas de negocio y KPI | DC-07 | ✅ Coinciden |
| QR | Identificador principal | DC-08 | ✅ Coinciden |
| Alcance incluido | Inventario, entradas, salidas, kardex, conteos, ajustes, transferencias, trazabilidad, alertas, reportes, **usuarios, auditoría** | DC-02: gestión de inventarios, logística de bodega, trazabilidad, kardex, entradas, salidas, ajustes, conteos, transferencias, reportes, alertas, **dashboard operativo** | El SRS conserva los **20 módulos** del SPEC: «Usuarios» y «Auditoría» son los módulos M-02 y M-18; el dashboard (M-17) está expresamente en DC-02. Se registra la diferencia (H-17) y la decisión DEC-02 |
| Exclusiones | Ventas, producción, compras completas, facturación, nómina, CRM, **IA generativa** | DC-03 añade **contabilidad**; DC-07 excluye **toda** IA, no solo la generativa | Prevalece el SPEC (más estricto). La IA generativa queda incluida en la exclusión de DC-07 |
| Estado del SPEC | «Auditado y aprobado» | Archivo: «Emitido para revisión del Director» | Se toma como aprobado por instrucción del Director; se registra H-15 |

## 0.4 Qué fases ya están cerradas

El Prompt #003 numera las fases del *proyecto* (0, 1, 2, 3). El roadmap de la Auditoría (Fase D) numera 9 fases de ingeniería distintas (0–8). Ambas numeraciones coexisten; esta tabla las concilia (ver H-16).

| Fase del proyecto | Producto | Estado | Fase equivalente del roadmap de la Auditoría | Observación |
|---|---|---|---|---|
| **Fase 0** | Auditoría Fundacional | ✅ **Cerrada** (acuse del Director) | Fase 0 — Auditoría Fundacional | Sin observaciones |
| **Fase 1** | Constitución del proyecto: decisiones del Director DC-01…DC-08 | 🟡 **Cerrada parcialmente** — cierran «total o parcialmente 19 de las 24 preguntas bloqueantes» (SPEC, encabezado) | Fase 1 — Resolución de ambigüedades y autorización de alcance | Persisten preguntas bloqueantes abiertas (§0.5) |
| **Fase 2** | COLBASOFT_SPEC v1.0 | ✅ **Cerrada** (aprobación declarada en el Prompt #003) | Materializa vacíos C.1.2, C.1.4, C.1.5, C.1.6, C.2.2, C.2.3; cubre la Ingeniería de Requisitos de la Fase 4 del roadmap | El SPEC modela procesos **TO-BE**, no AS-IS |
| **Fase 3** | **SRS_COLBASOFT v1.0 (este documento)** | 🟡 **En emisión** | Formaliza el entregable de la Fase 4 del roadmap («Ingeniería de Requisitos») | Ver advertencia de dependencia |

> **Advertencia de dependencia (H-16).** El roadmap de la Auditoría establece que *«ninguna fase puede iniciar mientras su fase antecesora tenga entregables abiertos»* y que la Fase 4 (Requisitos) depende de las Fases 1, 2 y 3 completas. Hoy siguen abiertos el saneamiento académico (Fase 2 del roadmap: 9 fuentes sin verificar) y el levantamiento AS-IS con línea base (Fase 3 del roadmap). Este SRS se emite **por instrucción expresa del Director** (Prompt #003) y por eso **hereda un riesgo**: sus requisitos no han sido contrastados con el proceso real de la empresa de estudio. El riesgo queda registrado en el Anexo C (R-S01).

## 0.5 Qué información queda pendiente

**a) Pendientes heredados del SPEC (§13.6)** — no bloquean el SRS pero sí fases posteriores:

| # | Asunto | Pregunta de la Fase F | Bloquea |
|---|---|---|---|
| 1 | Definición legal de PYME | A-03 | Dimensionamiento del mercado |
| 2 | Delimitación de «sector textil» | A-04 | Selección de la empresa piloto |
| 3 | Municipios del ámbito geográfico | A-05 | Alcance del estudio |
| 4 | Autorización de contacto con empresas reales | V-01 | Fase 3 del roadmap completa |
| 5 | Levantamiento de la línea base | V-03 | Demostración de impacto |
| 6 | Qué ocurre si el piloto no alcanza las cifras citadas | V-06 | Criterio de aprobación |
| 7 | Verificación de las nueve fuentes ausentes de la bibliografía | I-03 | Defensa académica |
| 8 | Contradicciones estadísticas (25 % vs 40 % CEPAL; 40 % OIT vs Hernández y Salazar) | I-04, I-05 | Defensa académica |
| 9 | Reproyección del horizonte temporal (2025 vencido) | I-09 | Vigencia de proyecciones |
| 10 | Entregable mínimo aprobatorio | S-15 | Alcance de construcción |
| 11 | Renumeración canónica de las reglas de negocio | — | Limpieza documental |
| 12 | Calibración de los valores numéricos de los RNF | — | Requiere línea base |

**b) Hallazgos de la reconstrucción (nuevos, detectados al verificar el SPEC contra sí mismo).** Cada uno se detalla y se convierte en decisión en el Anexo C.

| # | Hallazgo | Evidencia | Tratamiento en el SRS |
|---|---|---|---|
| **H-01** | **El SPEC declara 68 reglas de negocio; sus tablas contienen 82** (60 estructurales + 22 configurables). El encabezado del Cap. 9 y §9.14 (68 = 51 + 17) no coinciden con las filas de §9.2–§9.12; la propia suma de la tabla §9.14 es 82 | Recuento programático de filas RN | Se conservan **las 82** (ninguna se pierde). Se reporta la cifra real. Decisión DEC-03 |
| **H-02** | Las prioridades de los 162 RF no coinciden con el resumen §7.1: filas = **74 P0 / 70 P1 / 18 P2**; el resumen declara 72 / 69 / 21 | Recuento de filas RF | Se usa la prioridad de cada fila |
| **H-03** | §0.4 declara rangos `HU-001…HU-096` y `RF-001…RF-138`; el contenido llega a HU-103 y RF-162 | §0.4 vs Caps. 6–7 | Prevalece el contenido (103 HU, 162 RF) |
| **H-04** | Proporciones de trazabilidad distintas: §0.3 (41 % / 12 % / 9 % / 38 %) vs §13.3 (34 % / 12 % / 17 % / 37 %) | §0.3 vs §13.3 | Se toma §13.3 (más reciente y con cifras absolutas); no afecta requisitos |
| **H-05** | Referencias cruzadas a RNF incorrectas: HU-026 cita RNF-014 para la resolución del escaneo (corresponde RNF-015 del SPEC); HU-071 cita RNF-012 (respaldo) para el tiempo de consulta (corresponde RNF-014) | HU-026 crit. 5; HU-071 crit. 3 | El SRS redacta ambos criterios sin la referencia errónea y enlaza los RNF correctos |
| **H-06** | «Estructural» (60 reglas: inviolables, no parametrizables) frente a §9.1 «no configurables» (solo 10 reglas) y RF-157 («no exponer como configurables las reglas de §9.1»). Es ambiguo si las otras 50 estructurales son configurables | §9.1 vs columna Tipo | Se interpreta que **toda regla estructural es no configurable** y que §9.1 es el subconjunto crítico. Decisión DEC-04 |
| **H-07** | **«Valorización»** se usa como permiso (§2.7, PR-04, RF-116, RF-143, HU-087) pero **ningún requisito captura costo o precio** (RF-049 y RF-062 lo prohíben) y §12.4 sitúa la valorización en el Horizonte 3 rozando DC-03 | Grep de «valoriz» | El permiso se conserva como restricción preventiva; **en el MVP no existe dato que valorizar**. Decisión DEC-07 |
| **H-08** | **Tensión de alcance entre DC-02/Prompt #003 y el backlog:** 16 elementos —entre ellos transferencias y conteo general— (que el SRS mapea a 19 HU y 19 RF) están en el **Horizonte 2 (v1.1)** de §12.3, aunque DC-02 y el Prompt incluyen transferencias y conteos en el MVP y M-09 es P0 (incl. 2 HU P0 y 1 RF P0 en H2) | §12.3 vs §5.1 vs DC-02 | El SRS distingue **importancia** (MoSCoW) de **horizonte de entrega** (H1/H2) y no descarta ningún requisito. Decisión DEC-01 (relacionada con S-15) |
| **H-09** | Identificadores sin contenido: `RN-069*` («reservado») y `RN-026b*` («ver nota de numeración») | §9.3, §9.7 | No se cuentan como reglas ni reciben ID permanente |
| **H-10** | **PN-14 (Cierre operativo de jornada)** está en el backlog del MVP (elemento 39) y modelado en §3, pero **no tiene ninguna HU ni RF**; solo la afectan RN-054 y RNF-011 | Búsqueda en Caps. 6–7 | Se documenta el caso de uso (CU-19) marcándolo «requisitos pendientes». Decisión DEC-05 |
| **H-11** | **Reglas sin RF que las implemente:** RN-022, RN-028, RN-043, RN-047, RN-051, RN-059 (y RN-028 y RN-047 tampoco tienen HU) | Trazabilidad del Cap. 9 | Se listan en el Anexo C con propuesta de cierre (no se crean RF). Decisión DEC-06 |
| **H-12** | **KPI cuyo dato de origen ningún requisito exige capturar:** KPI-05 (instante de inicio de la operación), KPI-07 (registro de selección manual sin escaneo), KPI-10 (registro de la desviación de ubicación), KPI-12 (instante de llegada), KPI-17 (parámetro «N días» sin movimiento), KPI-24 (volumen estimado de movimientos y verificación de campo) | Cap. 10 vs Cap. 7 | Se listan en el Anexo C. Decisión DEC-06 |
| **H-13** | HU con cobertura RF solo parcial: HU-069 y HU-070 | Mapeo HU↔RF | Se marcan «cobertura parcial» en el Cap. 5 |
| **H-14** | El campo «actor» de algunas HU es «Todos» pero la historia se redacta desde un rol (HU-055, 071, 073, 076, 078) | Cap. 6 SPEC | Se conserva el actor del SPEC; sin impacto funcional |
| **H-15** | Estado del SPEC: el archivo dice «Emitido para revisión del Director»; el Prompt #003 lo declara aprobado | SPEC §portada | Se toma como aprobado por instrucción; se pide confirmación formal (DEC-08) |
| **H-16** | Numeración de fases y principio de dependencia del roadmap (§0.4 de este capítulo) | Auditoría Fase D | Riesgo R-S01 |
| **H-17** | Diferencias entre el resumen de alcance del Prompt #003 y DC-02/DC-03/DC-07 (§0.3-d) | Prompt vs SPEC | Prevalece el SPEC; decisión DEC-02 |
| **H-18** | La alerta «Lote próximo a vencer inmovilización» exige una «fecha límite» de lote que **ni CD-06 ni ningún RF definen** (solo existe el umbral de antigüedad de RN-074) | PN-11 vs CD-06 | Se conserva la alerta como la define el SPEC; decisión DEC-09 |
| **H-19** | **(Resuelto en la v1.4, opción a)** *(v1.2, detectado al auditar DEC-01)* El criterio 1 de HU-ENT-006 (proponer la ubicación «según los criterios de HU-BOD-005») remite a una historia del Horizonte 2, mientras el SPEC (§12.3 #12) afirma que el MVP opera con una propuesta simple | HU-ENT-006 vs HU-BOD-005, SPEC §12.3 | No se corrige. Con DEC-01 = A, HU-ENT-006 forma parte del umbral aprobatorio y HU-BOD-005 no: se eleva al Director aceptar la propuesta simple como suficiente o acotar el criterio |
| **H-20** | **(Resuelto en la v1.4, opción a)** *(v1.2, detectado al auditar DEC-01)* RF-REP-003 (Horizonte 1) exige calcular los 24 KPI, pero KPI-02 solo existe con conteo general (RF-CNT-011, Horizonte 2) y el SPEC (§12.3 #15) ubica otros 11 KPI en el Horizonte 2 | RF-REP-003 vs §12.3 #15 y RF-CNT-011 | No se corrige. Con DEC-01 = A se eleva al Director acotar RF-REP-003 a los KPI que el Núcleo puede alimentar, o aceptar la diferencia por escrito |

## 0.6 Método de verificación de integridad

1. Se extrajo el texto de la monografía (.docx) y se leyeron íntegros la Auditoría y el SPEC.
2. Se analizaron las tablas del SPEC de forma programática y se compararon los conteos declarados con los reales: **103 HU**, **462 criterios de aceptación**, **162 RF**, **47 RNF**, **82 RN** (declaradas 68), **24 KPI**, **14 PN**, **48 CD**, **20 módulos**, **42 riesgos**.
3. Se verificó que toda referencia cruzada del SPEC (`RN-…`, `HU-…`, `RF-…`, `RNF-…`, `KPI-…`) apunte a un elemento existente: **no hay referencias colgantes**; sí hay 2 referencias semánticamente erróneas (H-05).
4. Se verificó que cada criterio de aceptación del SPEC tenga exactamente un escenario Gherkin en este SRS (462 = 462).

**ESTADO: CONTEXTO RECONSTRUIDO.**

---

**ESTADO DEL CAPÍTULO 0**

| | |
|---|---|
| **Completado** | Inventario de documentos y versiones · decisiones constitucionales · fases · pendientes · 20 hallazgos de reconstrucción (H-19 y H-20, en la v1.2) |
| **Pendiente** | Resolución de los hallazgos H-01…H-20 (decisiones DEC-01…DEC-09 del Anexo C) |
| **Riesgos encontrados** | R-S01 (SRS anterior a AS-IS y línea base) · H-08 (tensión MVP/backlog) · H-10 (PN-14 sin requisitos) · H-11/H-12 (brechas de trazabilidad) |
| **Dependencias** | Decisión del Director sobre DEC-01 (alcance de entrega) condiciona el Cap. 12 |


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

Los 49 conceptos de dominio están definidos operativamente en el **Capítulo 4 del SPEC** (CD-01…CD-49) y **no se redefinen aquí** (una definición duplicada podría divergir). La tabla siguiente recoge únicamente los conceptos que el SRS usa con más frecuencia y remite a su definición canónica.

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
| **Pieza** | Unidad física individual de mercancía dentro de un lote (rollo, paquete o bolsa, contenedor agrupado), con cantidad propia registrada en la recepción; el QR no la identifica | CD-49 |

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
| 3 | `COLBASOFT_SPEC_v1.4.md` (5 sep. 2026; v1.1 del 29 sep. 2026; v1.2, v1.3 y v1.4 del 30 sep. 2026) | Fuente principal del SRS |
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


---

# CAPÍTULO 2 — VISIÓN GENERAL DEL SISTEMA

> Descripción **funcional** de COLBASOFT. No describe arquitectura, tecnologías ni estructura de datos.

## 2.1 Perspectiva del producto

COLBASOFT es un sistema **autónomo y de alcance deliberadamente estrecho**: gestiona el inventario y la logística de una bodega textil y nada más `[DC-02]` `[DC-03]`. No forma parte de un ERP ni se integra con sistemas de ventas, compras, producción, contabilidad, nómina, CRM ni facturación.

**Contexto funcional (quién y qué interactúa con el sistema):**

```
   Personas (5 roles)                                              Elementos externos al sistema
 ┌──────────────────────┐                                       ┌─────────────────────────────────┐
 │ Administrador        │                                       │ Herramienta analítica externa   │ ◄── recibe datos estructurados
 │ Jefe de Bodega       │                                       │ (Power BI) [DC-06]              │     (RF-REP-004, RF-REP-005)
 │ Coordinador          │ ── web responsive / tablet ─► COLBASOFT│ Cámara de la tablet (escaneo QR)│ ──► captura de identificadores
 │ Auxiliar             │       [DC-05]                          │ Impresión de etiquetas QR       │ ◄── etiquetas físicas (ver 2.8)
 │ Auditor (solo lectura│                                       └─────────────────────────────────┘
 └──────────────────────┘        Sistema como actor de acciones automáticas [RN-INT-001]
```

**Interfaces con el usuario.** Aplicación web responsive utilizable en escritorio y en tablet `[DC-05]`; captura de identificadores con la cámara de la tablet, sin lector externo obligatorio (RNF-TAB-003). No existe aplicación móvil nativa.

**Interfaces con otros sistemas.** Una sola, unidireccional y de datos: la **exposición estructurada de información** a la herramienta analítica externa `[DC-06]`. El SRS no especifica el mecanismo.

## 2.2 Problema que el sistema resuelve

La monografía documenta que las PYMES textiles del Eje Cafetero gestionan su inventario con cuadernos, hojas de cálculo sueltas y registros manuales `[MON §3]`, lo que produce una **cadena causal de nueve eslabones** (SPEC §1.1.2): registro manual → errores frecuentes → información desactualizada → pérdida de trazabilidad → rupturas de stock y sobre stock → interrupciones de producción → reprocesos y pérdida de materia prima → plazos de entrega más largos → pérdida de competitividad. El obstáculo principal no es tecnológico sino la **resistencia a la adopción** `[MON §4, §7.1]`; por eso el SRS trata la usabilidad y la adopción como requisitos de primer orden (Cap. 7).

> **Nota de integridad `[AUD E.1, E.2]`.** Varias cifras de magnitud del problema (60 %, +30 % de pérdidas, 25–45 % de productividad) provienen de fuentes ausentes de la bibliografía de la monografía y **no se usan en este SRS como justificación cuantitativa**. Las cifras respaldadas (72 % ANDI 2023; 67 % Martínez y Gómez 2019) se citan solo como contexto.

## 2.3 Funciones del producto

Las funciones se agrupan en cinco familias (SPEC §5.1). La tabla siguiente se genera del contenido del SRS y muestra el volumen de requisitos por módulo.

| Módulo | Dominio | Grupo | Prio. SPEC | HU | RF | Procesos | Casos de uso |
|---|:--:|---|:--:|:--:|:--:|---|---|
| **M-01** Acceso y Autenticación | ACC | Fundacional | P0 | 4 | 7 | — | CU-01 |
| **M-02** Usuarios y Roles | USR | Fundacional | P0 | 5 | 8 | — | CU-02 |
| **M-03** Catálogo de Referencias | CAT | Maestro | P0 | 6 | 10 | — | CU-03 |
| **M-04** Gestión de Lotes | LOT | Maestro | P0 | 4 | 6 | — | CU-20 |
| **M-05** Estructura de Bodega | BOD | Maestro | P0 | 5 | 9 | — | CU-04, CU-08 |
| **M-06** Identificación QR | QRC | Maestro | P0 | 5 | 9 | — | CU-07 |
| **M-07** Entradas y Recepción | ENT | Operativo | P0 | 10 | 17 | PN-01, PN-02, PN-03 | CU-06, CU-08 |
| **M-08** Salidas | SAL | Operativo | P0 | 9 | 14 | PN-10 | CU-15 |
| **M-09** Movimientos y Transferencias | MOV | Operativo | P0 | 9 | 13 | PN-05, PN-06 | CU-10, CU-11 |
| **M-10** Ajustes de Inventario | AJU | Operativo | P0 | 6 | 10 | PN-07 | CU-12 |
| **M-11** Conteos | CNT | Operativo | P1 | 11 | 15 | PN-08, PN-09 | CU-13, CU-14 |
| **M-12** Novedades de Mercancía | NOV | Operativo | P1 | 4 | 8 | PN-12 | CU-17 |
| **M-13** Consulta de Existencia | INV | Información | P0 | 6 | 9 | PN-04 | CU-09 |
| **M-14** Kardex y Trazabilidad | KDX | Información | P0 | 6 | 9 | — | CU-21 |
| **M-15** Alertas y Reglas | ALE | Información | P1 | 5 | 7 | PN-11 | CU-16 |
| **M-16** Reportes y Exportación Analítica | REP | Información | P1 | 4 | 8 | — | CU-22 |
| **M-17** Dashboard Operativo | DSH | Información | P1 | 3 | 4 | — | CU-23 |
| **M-18** Auditoría y Bitácora | AUD | Control | P1 | 4 | 7 | PN-13 | CU-18 |
| **M-19** Parámetros y Configuración | PAR | Fundacional | P0 | 3 | 7 | — | CU-05 |
| **M-20** Notificaciones y Tareas | TAR | Fundacional | P1 | 5 | 8 | — | CU-24, CU-23, CU-19 |
| **Total** | | | | **114** | **185** | 14 PN | 24 CU |

**Capacidades transversales del producto:**

| Capacidad | Cómo se manifiesta | Regla / requisito núcleo |
|---|---|---|
| **Registro atribuido** | Toda acción queda a nombre de una persona identificada (o del Sistema como actor explícito) | RN-INT-001 · RF-ACC-001 · RF-KDX-002 |
| **Trazabilidad completa** | Kardex inmutable; la existencia se deriva del kardex | RN-INT-002 · RN-INT-004 · RF-KDX-003 |
| **Identificación por escaneo** | QR único de un solo uso por unidad y por ubicación | RN-IDE-002 · RF-QRC-001…003 |
| **Control por segregación** | Nadie aprueba su propia solicitud; el Auditor solo lee | RN-AJU-001 · RN-AUD-002 · RF-AUD-005 |
| **Automatización por reglas** | Reglas explícitas y umbrales configurables disparan alertas | Cap. 8 · RF-ALE-002 |
| **Medición del propio beneficio** | 24 KPI calculados por el sistema | Cap. 9 · RF-REP-003 |
| **Operación sin conectividad estable** | Retención local y sincronización posterior | RN-INT-003 · RNF-DSP-002 |

## 2.4 Ciclo de vida de una unidad de inventario

```
Llegada ─► Documento de entrada ─► Recepción física ─► Confirmación (2.ª persona) ─► Lote + Existencia
  (CU-06)                                                                                  │
   ┌────────────────────────────────────────────────────────────────────────────────────┘
   ▼
Identificación QR (CU-07) ─► Ubicación (CU-08) ─► [ Consulta CU-09 · Reubicación CU-10 · Transferencia CU-11 ]
                                                                    │
                       Conteo cíclico/general (CU-13/14) ─► Ajuste con aprobación (CU-12)
                                                                    │
                                                          Salida autorizada (CU-15) ─► fin del alcance de trazabilidad
```

**Estados de la existencia (CD-44)** — mutuamente excluyentes para una misma cantidad:

| Estado | Puede salir | Puede transferirse | Puede reubicarse | Cuenta en disponible |
|---|:--:|:--:|:--:|:--:|
| Disponible | ✅ | ✅ | ✅ | ✅ |
| Reservado | Solo por su operación | ❌ | ❌ | ❌ |
| En tránsito | ❌ | ❌ | ❌ | ❌ |
| Inmovilizado | ⚠️ con autorización | ⚠️ con autorización | ⚠️ con autorización | ❌ |
| En recepción | ❌ | ❌ | ✅ | ❌ |

## 2.5 Qué significa «inteligente» en COLBASOFT `[DC-07]` `[AUD C.1.5]`

«Inteligente» significa **exactamente** dos cosas: (1) **automatización basada en reglas** —el sistema aplica de forma autónoma un cuerpo de reglas de negocio explícitas que impiden estados inválidos, disparan alertas y ejecutan acciones sin intervención humana (Cap. 8)— y (2) **analítica operativa** —el sistema calcula indicadores sobre su propio registro (Cap. 9). **No** incluye aprendizaje automático, predicción de demanda, visión por computador, procesamiento de lenguaje natural, agentes autónomos ni IA generativa. Toda afirmación de «inteligencia» del producto debe poder señalarse con una regla numerada (RN-…) o un KPI.

## 2.6 Características de los usuarios (síntesis)

| Rol | Frecuencia | Dispositivo | Nivel digital | Nota de diseño |
|---|---|---|---|---|
| Administrador | Baja | Escritorio o portátil | Medio | Decisor de compra; configura |
| Jefe de Bodega | Alta | Escritorio y tablet | Medio | Responsable de la exactitud |
| Coordinador de Bodega | Muy alta | Tablet en piso | Medio-bajo | Supervisa en piso |
| **Auxiliar de Bodega** | **Intensiva** | **Tablet, exclusivamente** | **Bajo** | **Usuario crítico: el diseño de interacción se optimiza para él** `[MON §4]` |
| Auditor | Baja (por campañas) | Escritorio | Medio-alto | Solo lectura absoluta |

Detalle de cada actor en el Capítulo 3.

## 2.7 Restricciones

| # | Restricción | Origen |
|---|---|---|
| RS-1 | Alcance funcional cerrado (DC-02) y exclusiones absolutas (DC-03) | DC-02, DC-03 |
| RS-2 | Exactamente cinco roles; ninguno adicional | DC-04 |
| RS-3 | Web responsive + tablet; sin app nativa | DC-05 |
| RS-4 | Sin IA de ningún tipo | DC-07 |
| RS-5 | QR como identificador principal; el código de barras solo consulta | DC-08, RN-IDE-003 |
| RS-6 | Capacidad financiera limitada de las PYMES: el producto debe ser de bajo costo de entrada | `[MON §1, §3, §6]` R-08 |
| RS-7 | Baja alfabetización digital: usabilidad extrema como requisito prioritario | `[MON §3, §8.2]` R-09 |
| RS-8 | Infraestructura tecnológica deficiente: no puede asumirse conectividad permanente | `[MON §3]` R-11 |
| RS-9 | Adopción escalonada por proceso, no de golpe | `[MON §8.2]` R-13 |
| RS-10 | Cumplimiento de la normativa colombiana de protección de datos personales (Ley 1581 de 2012) | `[AUD C.2.11]` · RNF-SEG-008 |
| RS-11 | Barreras regulatorias del sector: fuera del control del producto | `[MON §3]` |
| RS-12 | Ningún elemento del SRS puede contradecir la monografía (RI-1) ni inventar funcionalidad (RI-3) | Auditoría |

## 2.8 Supuestos y dependencias

| # | Supuesto / dependencia | Estado | Riesgo asociado |
|---|---|---|---|
| S-1 | Existe una **empresa de estudio** dispuesta a participar en levantamiento, piloto y medición `[DC-01]` | 🔴 Abierto (V-01) | RG-37 |
| S-2 | Los procesos del Cap. 4 (TO-BE) son compatibles con la operación real de la empresa | 🔴 No verificado: AS-IS sin levantar | R-S01 |
| S-3 | Cada punto de operación dispone de una **tablet con cámara** capaz de escanear QR (RNF-TAB-003) | 🟡 Por confirmar en el levantamiento de infraestructura | RG-24 |
| S-4 | La empresa dispone de un medio para **imprimir etiquetas** legibles y resistentes a la operación de bodega (el SRS lo requiere funcionalmente, no lo especifica) | 🟡 Por confirmar | RG-25 |
| S-5 | La conectividad es **intermitente**: el sistema debe tolerar su pérdida | 🟢 Requisito (RN-INT-003) | RG-23 |
| S-6 | Existe la herramienta analítica externa (Power BI) a la que se exponen los datos `[DC-06]` | 🟡 Por confirmar | RG-29 |
| S-7 | La **línea base** de KPI-01, KPI-05 y KPI-08 se levantará antes del piloto | 🔴 Abierto (V-03) | RG-36 |
| S-8 | El equipo de tres autores mantiene la autoría del producto | 🟡 A-12 abierto | — |

---

**ESTADO DEL CAPÍTULO 2**

| | |
|---|---|
| **Completado** | Perspectiva funcional · problema · funciones · ciclo de vida · definición de «inteligente» · restricciones · supuestos |
| **Pendiente** | Confirmar los supuestos S-1…S-4 y S-6 con la empresa de estudio (Fase 3 del roadmap) |
| **Riesgos encontrados** | S-1, S-2 y S-7 abiertos (RG-36, RG-37, R-S01) |
| **Dependencias** | Cap. 3 (actores), Cap. 4 (casos de uso), Anexo C |


---

# CAPÍTULO 3 — ACTORES

`[DC-04]` COLBASOFT reconoce **cinco roles oficiales** más el **Sistema** como actor de acciones automáticas. No se admiten roles adicionales. Toda función es ejecutable por al menos un rol y ninguna queda sin responsable.

## 3.1 Principios que gobiernan los roles

| # | Principio | Consecuencia funcional |
|---|---|---|
| PR-01 | **Segregación de funciones:** quien registra no es necesariamente quien autoriza | RN-ENT-007 · RN-AJU-001 · RN-CNT-003 |
| PR-02 | **El Auditor nunca escribe** en el inventario | RF-AUD-005 · RN-AUD-002 |
| PR-03 | **Escalada de privilegio explícita:** un rol superior puede hacer lo que hace el inferior, salvo donde la segregación lo prohíba | Cap. 3.5 |
| PR-04 | **El Auxiliar no ve información sensible** de negocio | RF-INV-005 · RF-KDX-007 |
| PR-05 | **Toda acción queda atribuida** a una persona identificada; no hay cuentas compartidas | RN-INT-001 · RF-ACC-002 |
| PR-06 | **El rol no castiga: registra.** El operario no ve rankings ni indicadores de error personal | RF-NOV-003 · RF-DSH-004 · RNF-USA-005 |

## 3.2 Ficha de los actores

### ACT-01 · Administrador (ROL-01)

| Campo | Contenido |
|---|---|
| **Perfil típico** | Propietario, gerente o responsable de sistemas de la PYME (decisor de compra) |
| **Frecuencia / dispositivo / nivel digital** | Baja · Escritorio o portátil · Medio |
| **Objetivos** | Inventario confiable sin revisarlo a diario · inversión con retorno medible · que la operación no dependa de una persona irremplazable |
| **Dolor principal** | *«No sé qué tengo realmente en bodega y descubro los faltantes cuando ya detuvieron la producción.»* `[MON §3]` |
| **Responsabilidades** | Configurar el sistema y sus parámetros · crear, modificar, activar y desactivar usuarios · asignar roles · definir bodega, zonas y ubicaciones · configurar umbrales de alerta · autorizar la integración analítica · aprobar ajustes mayores |
| **Casos de uso principales** | CU-01, CU-02, CU-03, CU-04, CU-05, CU-12 (aprobación mayor), CU-16 (configura umbrales), CU-18 (consulta), CU-22 (habilita exportación) |
| **No puede** | Editar ni eliminar un movimiento confirmado (RN-INT-002) · alterar la bitácora (RN-AUD-001) · aprobar su propia solicitud (RN-AJU-001) · desactivarse a sí mismo si es el único activo (RN-MAE-004) |
| **Lectura** | Sin restricción de lectura dentro del alcance del MVP |

### ACT-02 · Jefe de Bodega (ROL-02)

| Campo | Contenido |
|---|---|
| **Perfil típico** | Responsable máximo de la operación logística de la bodega |
| **Frecuencia / dispositivo / nivel digital** | Alta · Computador y tablet · Medio |
| **Objetivos** | Que el inventario cuadre sin recuentos de emergencia · que la producción no se detenga por un faltante · justificar con evidencia cualquier diferencia · reducir reprocesos |
| **Dolor principal** | *«Cuando el inventario no cuadra, la responsabilidad es mía y no tengo cómo demostrar qué pasó ni quién lo movió.»* `[MON §3, §4]` |
| **Responsabilidades** | Responder por la exactitud · aprobar ajustes menores · programar y cerrar conteos · autorizar salidas · resolver diferencias · distribuir trabajo · atender alertas |
| **Casos de uso principales** | CU-03, CU-11 (autoriza y cancela en tránsito), CU-12, CU-13, CU-14, CU-15, CU-16, CU-19, CU-20, CU-21, CU-22, CU-23 |
| **No puede** | Gestionar usuarios y roles · modificar la estructura de la bodega · configurar parámetros globales · aprobar ajustes mayores (escalan al Administrador, RN-AJU-002) · alterar la bitácora |

### ACT-03 · Coordinador de Bodega (ROL-03)

| Campo | Contenido |
|---|---|
| **Perfil típico** | Mando medio que supervisa a los auxiliares en piso |
| **Frecuencia / dispositivo / nivel digital** | Muy alta · Tablet en piso · Medio-bajo |
| **Objetivos** | Que el trabajo del turno quede registrado sin pendientes · que la mercancía esté donde el sistema dice · que su equipo no repita trabajo |
| **Dolor principal** | *«Recibimos mercancía, la ubicamos y la movemos todo el día; para cuando llega la hora de anotar, ya nadie recuerda con exactitud qué pasó.»* `[MON §3]` |
| **Responsabilidades** | Supervisar entradas, salidas y transferencias · verificar lo recibido contra el documento de entrada · asignar ubicaciones · ejecutar y supervisar conteos cíclicos · solicitar ajustes · capacitar a los auxiliares |
| **Casos de uso principales** | CU-06, CU-07, CU-08, CU-11, CU-12 (solicita), CU-13, CU-15 (dentro de umbral), CU-17, CU-23 (su zona), CU-24 |
| **No puede** | Aprobar sus propios ajustes (RN-AJU-001) · cerrar conteos (RN-CNT-004) · modificar la estructura de bodega · configurar umbrales · ver reportes de desempeño individual (PR-06) · alterar la bitácora |

### ACT-04 · Auxiliar de Bodega (ROL-04) — **usuario crítico**

| Campo | Contenido |
|---|---|
| **Perfil típico** | Operario de bodega; mueve la mercancía físicamente |
| **Frecuencia / dispositivo / nivel digital** | Intensiva y continua · **Tablet, exclusivamente** · **Bajo** `[MON §3, §8.2]` |
| **Objetivos** | Terminar su trabajo sin quedarse después de hora · no ser señalado por diferencias que no causó · que el sistema le diga qué hacer |
| **Dolor principal** | *«Anoto en un papel para pasarlo después al computador, y ahí es donde se pierde o se equivoca; después la culpa termina siendo mía.»* `[MON §3, §4]` |
| **Responsabilidades** | Recibir físicamente y registrar entradas · ubicar la mercancía · ejecutar movimientos internos asignados · preparar y registrar salidas autorizadas · contar las ubicaciones asignadas · reportar novedades |
| **Casos de uso principales** | CU-01, CU-06 (recepción física), CU-08, CU-10, CU-11 (ejecuta), CU-13 (cuenta), CU-15 (prepara), CU-17 (reporta), CU-09 (consulta), CU-23 (panel de tareas) |
| **No puede** | Ver costos ni valorización (PR-04) · aprobar ajustes de ningún monto · crear ni modificar referencias · modificar ubicaciones · cerrar conteos · anular movimientos confirmados · ver reportes gerenciales · ver indicadores de desempeño individual (PR-06) · ver el dashboard operativo completo ni la bitácora |
| **Barrera cultural documentada** | Teme que el sistema sea un mecanismo de vigilancia o el primer paso hacia su reemplazo `[MON §4, §6]`. **El producto debe desmentirlo con su comportamiento** (RNF-USA-005, RF-NOV-003) |

### ACT-05 · Auditor (ROL-05)

| Campo | Contenido |
|---|---|
| **Perfil típico** | Revisor interno o externo; puede ser el asesor académico durante el piloto |
| **Frecuencia / dispositivo / nivel digital** | Baja (por campañas) · Escritorio · Medio-alto |
| **Objetivos** | Reconstruir la historia de cualquier unidad · detectar patrones anómalos · confirmar que la segregación de funciones se respeta |
| **Dolor principal** | *«Cuando el registro es manual no hay nada que auditar: no hay quién, ni cuándo, ni por qué.»* `[MON §3]` |
| **Responsabilidades** | Verificar integridad y consistencia · revisar la trazabilidad · examinar ajustes, sus motivos y aprobadores · contrastar conteos · emitir observaciones · durante el piloto, recolectar la evidencia de impacto |
| **Casos de uso principales** | CU-18, CU-21, CU-22, CU-09 (histórico) |
| **Restricción absoluta** | **No escribe nada en el inventario**; su única escritura son las observaciones de auditoría, en un registro separado (RN-AUD-002) |
| **Lectura** | El Auditor lee todo (RF-AUD-004) |

### ACT-06 · Sistema (actor de acciones automáticas)

| Campo | Contenido |
|---|---|
| **Naturaleza** | Actor explícito para toda acción sin persona: cierre automático de alertas, escalamientos, liberación de reservas vencidas, generación de tareas, congelamiento de existencia teórica, cálculo de KPI `[RN-INT-001]` |
| **Regla** | Las acciones del Sistema se atribuyen al **Sistema**, nunca a un usuario (RN-INT-001) |

### ACT-07 · Herramienta analítica externa (actor de sistema externo)

| Campo | Contenido |
|---|---|
| **Naturaleza** | Consumidor de datos estructurados expuestos por el sistema `[DC-06]` |
| **Restricción** | Los datos exportados respetan la visibilidad por rol (HU-REP-003, criterio C5); su habilitación es exclusiva del Administrador |

### Historias en las que participa cada rol `[SRS]`

| Rol | Historias (según el campo «actor» del SPEC) | N.º |
|---|---|:--:|
| **Administrador** | HU-ACC-004, HU-USR-001, HU-USR-002, HU-USR-003, HU-USR-004, HU-USR-005, HU-CAT-001, HU-CAT-002, HU-CAT-003, HU-CAT-004, HU-CAT-005, HU-CAT-006, HU-BOD-001, HU-BOD-002, HU-BOD-003, HU-BOD-004, HU-BOD-005, HU-QRC-003, HU-AJU-002, HU-AJU-003, HU-CNT-008, HU-ALE-004, HU-REP-001, HU-REP-003, HU-AUD-001, HU-PAR-001, HU-PAR-002, HU-PAR-003, HU-TAR-002 | 29 |
| **Jefe de Bodega** | HU-CAT-001, HU-CAT-002, HU-CAT-003, HU-CAT-004, HU-CAT-006, HU-LOT-002, HU-LOT-003, HU-LOT-004, HU-ENT-004, HU-ENT-008, HU-SAL-001, HU-SAL-002, HU-SAL-004, HU-SAL-005, HU-SAL-007, HU-MOV-005, HU-MOV-006, HU-MOV-007, HU-MOV-009, HU-AJU-002, HU-AJU-005, HU-AJU-006, HU-CNT-004, HU-CNT-005, HU-CNT-006, HU-CNT-007, HU-CNT-008, HU-CNT-011, HU-NOV-003, HU-NOV-004, HU-INV-004, HU-INV-005, HU-KDX-001, HU-KDX-004, HU-KDX-006, HU-ALE-001, HU-ALE-002, HU-ALE-003, HU-ALE-004, HU-ALE-005, HU-REP-001, HU-REP-002, HU-REP-004, HU-DSH-001, HU-TAR-002, HU-TAR-004, HU-TAR-005 | 47 |
| **Coordinador de Bodega** | HU-LOT-001, HU-QRC-001, HU-QRC-004, HU-QRC-005, HU-ENT-001, HU-ENT-003, HU-ENT-004, HU-ENT-007, HU-ENT-008, HU-SAL-001, HU-SAL-004, HU-SAL-006, HU-SAL-007, HU-MOV-003, HU-MOV-006, HU-AJU-001, HU-CNT-001, HU-CNT-003, HU-CNT-004, HU-CNT-009, HU-NOV-002, HU-NOV-004, HU-INV-004, HU-ALE-001, HU-ALE-003, HU-ALE-005, HU-DSH-003, HU-TAR-003, HU-TAR-004 | 29 |
| **Auxiliar de Bodega** | HU-ACC-002, HU-QRC-002, HU-QRC-004, HU-ENT-002, HU-ENT-005, HU-ENT-006, HU-ENT-009, HU-ENT-010, HU-SAL-003, HU-SAL-008, HU-SAL-009, HU-MOV-001, HU-MOV-002, HU-MOV-004, HU-MOV-008, HU-CNT-002, HU-CNT-010, HU-NOV-001, HU-INV-002, HU-KDX-005, HU-DSH-002, HU-TAR-001 | 22 |
| **Auditor** | HU-AJU-005, HU-AJU-006, HU-INV-005, HU-KDX-001, HU-KDX-003, HU-KDX-004, HU-KDX-006, HU-REP-002, HU-AUD-001, HU-AUD-002, HU-AUD-003, HU-AUD-004 | 12 |
| **Sistema** | HU-CNT-003 | 1 |
| **Todos los roles** (transversales) | HU-ACC-001, HU-ACC-003, HU-AJU-004, HU-INV-001, HU-INV-003, HU-INV-006, HU-KDX-002 | 7 |

## 3.3 Matriz de permisos funcional

Leyenda: **✅** permitido · **⚠️** permitido con restricción o aprobación · **❌** denegado. Transcribe la matriz de segregación del SPEC (§2.7) y le agrega el caso de uso y la regla que gobierna cada restricción `[SRS]`.

| Función | Admin | Jefe | Coord. | Aux. | Auditor | CU | Regla / restricción |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| Iniciar sesión | ✅ | ✅ | ✅ | ✅ | ✅ | CU-01 | RN-INT-001 |
| Crear y desactivar usuarios | ✅ | ❌ | ❌ | ❌ | ❌ | CU-02 | RN-MAE-007 · RN-MAE-004 |
| Asignar roles | ✅ | ❌ | ❌ | ❌ | ❌ | CU-02 | Solo los 5 roles oficiales |
| Crear y editar referencias del catálogo | ✅ | ✅ | ❌ | ❌ | ❌ | CU-03 | RN-MAE-001 |
| Definir zonas y ubicaciones | ✅ | ❌ | ❌ | ❌ | ❌ | CU-04 | RN-MAE-006 |
| Generar identificador QR | ✅ | ✅ | ✅ | ❌ | ❌ | CU-07 | RN-IDE-002 |
| Reimprimir identificador QR | ✅ | ✅ | ✅ | ⚠️ | ❌ | CU-07 | ⚠️ Aux.: solo por deterioro, con motivo (RN-IDE-004) |
| Crear documento de entrada | ✅ | ✅ | ✅ | ❌ | ❌ | CU-06 | RN-ENT-002 |
| Registrar recepción física | ✅ | ✅ | ✅ | ✅ | ❌ | CU-06 | RN-ENT-007 |
| Confirmar entrada al inventario | ✅ | ✅ | ✅ | ❌ | ❌ | CU-06 | RN-ENT-007: quien recibe no confirma |
| Asignar ubicación | ✅ | ✅ | ✅ | ⚠️ | ❌ | CU-08 | ⚠️ Aux.: solo confirma la propuesta (RN-MOV-001) |
| Autorizar salida | ✅ | ✅ | ⚠️ | ❌ | ❌ | CU-15 | ⚠️ Coord.: hasta su umbral (RN-SAL-001) |
| Registrar salida autorizada | ✅ | ✅ | ✅ | ✅ | ❌ | CU-15 | RN-SAL-004 |
| Crear transferencia interna | ✅ | ✅ | ✅ | ❌ | ❌ | CU-11 | RN-EXI-004 |
| Ejecutar transferencia asignada | ✅ | ✅ | ✅ | ✅ | ❌ | CU-11 | RN-MOV-007 |
| Solicitar ajuste | ✅ | ✅ | ✅ | ❌ | ❌ | CU-12 | RN-AJU-003 |
| Aprobar ajuste menor | ✅ | ✅ | ❌ | ❌ | ❌ | CU-12 | RN-AJU-001: nunca el propio (Admin/Jefe) |
| Aprobar ajuste mayor | ✅ | ❌ | ❌ | ❌ | ❌ | CU-12 | RN-AJU-002 · RN-EXI-006 |
| Programar conteo cíclico | ✅ | ✅ | ✅ | ❌ | ❌ | CU-13 | — |
| Programar conteo general | ✅ | ✅ | ❌ | ❌ | ❌ | CU-14 | RN-CNT-006 |
| Registrar conteo físico | ✅ | ✅ | ✅ | ✅ | ❌ | CU-13 / CU-14 | RN-CNT-002 · RN-CNT-003 |
| Cerrar conteo y aplicar diferencias | ✅ | ✅ | ❌ | ❌ | ❌ | CU-13 / CU-14 | RN-CNT-004 · RN-CNT-003 |
| Anular movimiento confirmado | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | CU-21 | ⚠️ Nunca se borra: movimiento inverso con motivo (RN-INT-002) |
| Consultar existencia | ✅ | ✅ | ✅ | ✅ | ✅ | CU-09 | RN-INT-004 · RN-INT-006 |
| Consultar kardex | ✅ | ✅ | ✅ | ⚠️ | ✅ | CU-21 | ⚠️ Aux.: solo lo que él movió y últimos 30 días |
| Consultar valorización | ✅ | ✅ | ❌ | ❌ | ✅ | CU-22 | PR-04 · **sin dato en MVP (H-07)** |
| Consultar bitácora de auditoría | ✅ | ⚠️ | ❌ | ❌ | ✅ | CU-18 | ⚠️ Jefe: solo eventos de su bodega, sin configuración |
| Configurar umbrales de alerta | ✅ | ❌ | ❌ | ❌ | ❌ | CU-05 | RN-AUD-004 |
| Gestionar alertas | ✅ | ✅ | ✅ | ❌ | ❌ | CU-16 | RN-ALE-004 |
| Generar reportes operativos | ✅ | ✅ | ✅ | ❌ | ✅ | CU-22 | — |
| Generar reportes gerenciales | ✅ | ✅ | ❌ | ❌ | ✅ | CU-22 | PR-04 |
| Ver dashboard operativo completo | ✅ | ✅ | ⚠️ | ❌ | ✅ | CU-23 | ⚠️ Coord.: restringido a su zona |
| Ver panel de tareas propio | ✅ | ✅ | ✅ | ✅ | ❌ | CU-23 | PR-06 |
| Habilitar exportación analítica | ✅ | ❌ | ❌ | ❌ | ❌ | CU-22 | RN-AUD-003 |
| Registrar observación de auditoría | ❌ | ❌ | ❌ | ❌ | ✅ | CU-18 | RN-AUD-002 |
| Reportar novedad de mercancía | ✅ | ✅ | ✅ | ✅ | ❌ | CU-17 | RN-MAE-007: nunca se elimina |

## 3.4 Cadena de aprobación y escalamiento `[SRS]`

Consolidación de las reglas de segregación (no agrega reglas nuevas).

| Solicitud | Solicita | Aprueba / autoriza | Si solicitante = aprobador | Regla |
|---|---|---|---|---|
| Ajuste menor | Coordinador (o Jefe / Administrador) | Jefe de Bodega (o Administrador) | Escala al nivel superior; si no hay, se bloquea y se notifica al Administrador | RN-AJU-002 · RN-AJU-001 |
| Ajuste mayor | Coordinador (o Jefe / Administrador) | Administrador | Ídem | RN-AJU-002 · RN-AJU-001 |
| Ajuste sobre mercancía inmovilizada | Coordinador | Administrador (sin importar el monto) | Ídem | RN-EXI-006 |
| Salida bajo umbral del Coordinador | Jefe / Coordinador | Coordinador | Ídem | RN-SAL-001 · RN-AJU-001 |
| Salida sobre el umbral | Jefe / Coordinador | Jefe de Bodega | Ídem | RN-SAL-001 |
| Baja por daño (cualquier cantidad) | Jefe / Coordinador | Jefe de Bodega | Ídem | RN-SAL-006 |
| Sobrante de recepción | Auxiliar / Coordinador | Jefe de Bodega | Ídem | RN-ENT-005 |
| Confirmación de entrada | Auxiliar (recibe) | Coordinador (confirma) — nunca la misma persona | — | RN-ENT-007 |
| Cierre de conteo | Coordinador / Auxiliar (ejecutan) | Jefe de Bodega (nunca quien ejecutó) | Escala | RN-CNT-004 · RN-CNT-003 |
| Cancelación de transferencia en tránsito | Coordinador | Jefe de Bodega | — | RN-MOV-009 |

---

**ESTADO DEL CAPÍTULO 3**

| | |
|---|---|
| **Completado** | 5 roles + Sistema + actor externo · matriz de permisos (36 funciones) · cadena de aprobación |
| **Pendiente** | Lectura de parámetros por el Jefe (§2.7 del SPEC no la define; ver Cap. 10, nota) · política de «valorización» (H-07, DEC-07) |
| **Riesgos encontrados** | RG-13, RG-14, RG-17 (adopción por el Auxiliar) — riesgos críticos del SPEC |
| **Dependencias** | Cap. 4 (casos de uso), Cap. 10 (CRUD) |


---

# CAPÍTULO 4 — CASOS DE USO

> **24 casos de uso** que cubren los **14 procesos de negocio (PN-01…PN-14)** del SPEC y los 10 módulos que no tienen proceso propio. Cada caso declara objetivo, actor, precondiciones, postcondiciones, flujo principal, flujos alternos, excepciones y trazabilidad. Los flujos **transcriben y estructuran los procesos TO-BE del SPEC (Cap. 3)** `[SRS]`; no se agrega comportamiento nuevo. Recuérdese que el proceso real de la empresa **no fue levantado** (AS-IS pendiente, H-16).

## 4.1 Índice de casos de uso

| CU | Caso de uso | Proceso SPEC | Módulo | Actor principal |
|---|---|:--:|:--:|---|
| CU-01 | Autenticarse y gestionar la sesión | — | M-01 | Todos |
| CU-02 | Gestionar usuarios y roles | — | M-02 | Administrador |
| CU-03 | Gestionar el catálogo de referencias | — | M-03 | Jefe de Bodega |
| CU-04 | Definir la estructura de la bodega | — | M-05 | Administrador |
| CU-05 | Configurar parámetros y motivos tipificados | — | M-19 | Administrador |
| CU-06 | Recepcionar mercancía | PN-01 | M-07 | Coordinador |
| CU-07 | Identificar mercancía con QR | PN-02 | M-06 | Coordinador |
| CU-08 | Ubicar mercancía | PN-03 | M-07 / M-05 | Auxiliar |
| CU-09 | Consultar existencia y ubicación | PN-04 | M-13 | Todos |
| CU-10 | Reubicar mercancía (movimiento interno) | PN-05 | M-09 | Auxiliar |
| CU-11 | Transferir mercancía entre zonas o bodegas | PN-06 | M-09 | Coordinador / Auxiliar |
| CU-12 | Ajustar inventario | PN-07 | M-10 | Coordinador → Jefe/Admin |
| CU-13 | Ejecutar un conteo cíclico | PN-08 | M-11 | Coordinador / Auxiliar |
| CU-14 | Ejecutar un conteo general | PN-09 | M-11 | Jefe de Bodega |
| CU-15 | Registrar la salida de mercancía | PN-10 | M-08 | Jefe → Auxiliar |
| CU-16 | Gestionar alertas operativas | PN-11 | M-15 | Jefe / Coordinador |
| CU-17 | Reportar y resolver novedades de mercancía | PN-12 | M-12 | Auxiliar |
| CU-18 | Auditar el inventario | PN-13 | M-18 | Auditor |
| CU-19 | Cerrar la jornada operativa | PN-14 | M-20 / M-17 | Jefe / Coordinador |
| CU-20 | Gestionar lotes | — | M-04 | Jefe de Bodega |
| CU-21 | Consultar el kardex y verificar la trazabilidad | — | M-14 | Auditor / Jefe |
| CU-22 | Generar reportes y exportar datos | — | M-16 | Jefe / Admin / Auditor |
| CU-23 | Consultar el dashboard operativo y el panel de tareas | — | M-17 / M-20 | Jefe / Auxiliar |
| CU-24 | Gestionar tareas, notificaciones y aprobaciones | — | M-20 | Sistema |

## 4.2 Especificación de los casos de uso


### CU-01 — Autenticarse y gestionar la sesión

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | M-01 Acceso y Autenticación (sin proceso PN propio) |
| **Objetivo** | Garantizar que toda acción quede atribuida a una persona identificada `[PR-05]`. |
| **Actor principal** | Cualquier usuario con cuenta activa (los cinco roles). |
| **Actores secundarios** | Administrador (desbloqueo y restablecimiento). Sistema (bitácora). |
| **Precondiciones** | El usuario existe y está activo (CU-02). |
| **Postcondiciones (éxito)** | Sesión abierta a nombre del usuario; el acceso queda en la bitácora. |
| **Postcondiciones (fallo)** | No se abre sesión; el intento queda en la bitácora; tras el número configurado de fallos consecutivos la cuenta queda bloqueada y el Administrador es notificado. |
| **Trazabilidad** | HU: HU-ACC-001 HU-ACC-002 HU-ACC-003 HU-ACC-004 · RF: RF-ACC-001 RF-ACC-002 RF-ACC-003 RF-ACC-004 RF-ACC-005 RF-ACC-006 RF-ACC-007 · RN: RN-INT-001 RN-AUD-001 |

**Flujo principal**
1. El usuario ingresa su identificador y su contraseña individuales.
2. El sistema valida las credenciales.
3. El sistema abre la sesión y muestra al usuario la vista que corresponde a su rol (panel de tareas para el Auxiliar; dashboard operativo para los demás según §2.7).
4. El sistema registra el acceso en la bitácora con fecha, hora y origen.
5. Durante la jornada la sesión permanece activa mientras haya actividad.
6. El usuario cierra la sesión manualmente, o el sistema la cierra tras el tiempo de inactividad configurado, avisando antes de hacerlo; el cierre queda en la bitácora.

**Flujos alternos**
- **A1 · Cambio de contraseña propia:** el usuario indica la contraseña actual y una nueva que cumple la política mínima y difiere de la anterior; el sistema cierra sus demás sesiones activas y registra el evento sin guardar ningún valor de contraseña.
- **A2 · Primer acceso:** un usuario recién creado debe cambiar su contraseña antes de continuar.
- **A3 · Restablecimiento por el Administrador:** el Administrador desbloquea la cuenta, se fuerza el cambio de contraseña en el siguiente acceso y el usuario es notificado; el sistema nunca muestra la contraseña anterior.
- **A4 · Reanudación tras aviso de inactividad:** si el usuario reanuda antes del cierre, el registro en curso no confirmado se conserva.

**Excepciones**
- **E1 · Credenciales incorrectas:** se rechaza el acceso con un mensaje que no revela si el error fue del usuario o de la contraseña.
- **E2 · Cinco intentos fallidos consecutivos:** la cuenta se bloquea y se notifica al Administrador.
- **E3 · Cuenta desactivada:** se rechaza el acceso (ver CU-02).
- **E4 · Intento de cuenta genérica o compartida:** el sistema no ofrece esa posibilidad.

---

### CU-02 — Gestionar usuarios y roles

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | M-02 Usuarios y Roles |
| **Objetivo** | Administrar las personas que usan el sistema y el alcance de lo que cada una puede hacer `[DC-04]`. |
| **Actor principal** | Administrador (en exclusiva). |
| **Actores secundarios** | Sistema (bitácora, notificaciones). |
| **Precondiciones** | El Administrador está autenticado (CU-01); existen las bodegas y zonas a asignar (CU-04) cuando se asigna ámbito. |
| **Postcondiciones (éxito)** | El usuario queda creado, modificado, desactivado o reactivado, con un único rol activo y su ámbito; el evento queda en la bitácora. |
| **Postcondiciones (fallo)** | El estado de usuarios y roles no cambia; el rechazo se explica al Administrador. |
| **Trazabilidad** | HU: HU-USR-001 HU-USR-002 HU-USR-003 HU-USR-004 HU-USR-005 · RF: RF-USR-001 RF-USR-002 RF-USR-003 RF-USR-004 RF-USR-005 RF-USR-006 RF-USR-007 RF-USR-008 · RN: RN-MAE-004 RN-MAE-007 RN-MAE-006 RN-MAE-008 RN-MAE-009 |

**Flujo principal (crear usuario)**
1. El Administrador abre la gestión de usuarios y elige crear un usuario.
2. Ingresa los datos de identificación.
3. Selecciona uno de los cinco roles oficiales (no existe opción de crear un rol nuevo).
4. Asigna bodega y zona(s) de ámbito cuando el rol lo requiere.
5. El sistema valida la unicidad del identificador, crea el usuario y exige el cambio de contraseña en su primer acceso.
6. El sistema registra la creación en la bitácora.

**Flujos alternos**
- **A1 · Desactivar usuario:** el acceso se cierra de inmediato; los movimientos históricos se conservan íntegros con su nombre; el usuario puede reactivarse; nunca se elimina.
- **A2 · Cambiar rol:** surte efecto en la siguiente sesión; los movimientos anteriores conservan el rol vigente en su momento; queda registro del rol anterior y del nuevo.
- **A3 · Reasignar ámbito:** el Coordinador puede tener una o más zonas; el Auxiliar opera en las zonas de su Coordinador.

**Excepciones**
- **E1 · Se intenta desactivar o cambiar de rol al último Administrador activo:** se rechaza con explicación.
- **E2 · Se intenta dejar la bodega sin Jefe de Bodega activo:** se rechaza.
- **E3 · Se intenta asignar más de un rol activo o crear un rol adicional:** el sistema no lo permite.
- **E4 · Identificador de usuario duplicado:** se rechaza.

---

### CU-03 — Gestionar el catálogo de referencias

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | M-03 Catálogo de Referencias |
| **Objetivo** | Mantener el maestro de referencias, tallas, colores, categorías, unidades de medida y SKU que define qué puede existir en inventario. |
| **Actor principal** | Jefe de Bodega. |
| **Actores secundarios** | Administrador (mismas funciones y carga masiva). |
| **Precondiciones** | Usuario Administrador o Jefe autenticado. |
| **Postcondiciones (éxito)** | Referencia creada o modificada con sus SKU generados; umbrales de existencia mínima y máxima registrados cuando se definen. |
| **Postcondiciones (fallo)** | El catálogo no cambia; se informa el motivo. |
| **Trazabilidad** | HU: HU-CAT-001 HU-CAT-002 HU-CAT-003 HU-CAT-004 HU-CAT-005 HU-CAT-006 · RF: RF-CAT-001 RF-CAT-002 RF-CAT-003 RF-CAT-004 RF-CAT-005 RF-CAT-006 RF-CAT-007 RF-CAT-008 RF-CAT-009 RF-CAT-010 · RN: RN-MAE-001 RN-MAE-002 RN-MAE-003 RN-MAE-007 RN-INT-007 |

**Flujo principal (crear referencia)**
1. El Jefe indica el código, la descripción y la categoría de la referencia.
2. Asigna la unidad de medida desde la lista configurada.
3. Asigna los valores de talla y de color aplicables.
4. El sistema valida que el código no exista, crea la referencia activa y genera automáticamente los SKU de cada combinación referencia + talla + color.
5. El Jefe define, si corresponde, la existencia mínima y máxima por SKU (el mínimo no puede superar al máximo).

**Flujos alternos**
- **A1 · Desactivar referencia:** solo si su existencia es cero; deja de aparecer en operaciones nuevas y su kardex sigue consultable; puede reactivarse.
- **A2 · Carga masiva del catálogo inicial (Administrador):** el sistema valida el archivo antes de cargar, reporta errores por línea y carga según la opción elegida; el evento queda en la bitácora con el número de registros.
- **A3 · Organizar por categoría:** una referencia pertenece a una sola categoría, que puede asociarse a una zona preferente.
- **A4 · Listar SKU sin umbrales:** el sistema los presenta como pendientes de parametrización.

**Excepciones**
- **E1 · Código de referencia existente (activo o inactivo):** se rechaza.
- **E2 · Cambio de unidad de medida con movimientos existentes:** se rechaza con explicación.
- **E3 · Desactivación con existencia distinta de cero:** se rechaza.
- **E4 · Se busca eliminar una referencia:** el sistema solo ofrece desactivar.

---

### CU-04 — Definir la estructura de la bodega

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | M-05 Estructura de Bodega |
| **Objetivo** | Representar el espacio físico real (bodegas, zonas, ubicaciones y capacidades) para que el sistema pueda decir dónde está cada cosa. |
| **Actor principal** | Administrador (en exclusiva). |
| **Actores secundarios** | Sistema (generación de identificadores QR de ubicación, ver CU-07). |
| **Precondiciones** | Administrador autenticado. |
| **Postcondiciones (éxito)** | Bodega, zonas y ubicaciones definidas, cada ubicación con su identificador QR y capacidad; al menos una zona de recepción por bodega. |
| **Postcondiciones (fallo)** | La estructura no cambia. |
| **Trazabilidad** | HU: HU-BOD-001 HU-BOD-002 HU-BOD-003 HU-BOD-004 HU-BOD-005 · RF: RF-BOD-001 RF-BOD-002 RF-BOD-003 RF-BOD-004 RF-BOD-005 RF-BOD-006 RF-BOD-007 RF-BOD-008 · RN: RN-MAE-006 RN-EXI-002 RN-MOV-002 RN-MAE-005 RN-MOV-001 |

**Flujo principal**
1. El Administrador crea la bodega.
2. Crea zonas y les asigna tipo (almacenamiento, recepción, preparación, cuarentena).
3. Crea ubicaciones dentro de cada zona; el código de ubicación es único en la bodega.
4. Define la capacidad de cada ubicación.
5. Asigna un Coordinador responsable a cada zona.
6. El sistema genera el identificador QR de cada ubicación.
7. Opcionalmente configura los criterios de asignación automática de ubicación y su orden de aplicación.

**Flujos alternos**
- **A1 · Desactivar ubicación fuera de servicio:** solo si no tiene existencia; deja de proponerse y aceptarse como destino; su historial sigue consultable; puede reactivarse.
- **A2 · Ubicación sin capacidad definida:** se trata como de capacidad ilimitada y se lista como pendiente de configurar.
- **A3 · Consultar ocupación** por zona y ubicación.

**Excepciones**
- **E1 · Código de ubicación repetido en la bodega:** se rechaza.
- **E2 · Bodega sin zona de recepción:** el sistema exige al menos una.
- **E3 · Desactivación de ubicación con existencia:** se rechaza.
- **E4 · Se busca eliminar una ubicación:** el sistema solo ofrece desactivar.

---

### CU-05 — Configurar parámetros y motivos tipificados

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | M-19 Parámetros y Configuración |
| **Objetivo** | Permitir que la empresa adapte umbrales, plazos y motivos a su operación sin intervención técnica, sin debilitar los controles estructurales. |
| **Actor principal** | Administrador (en exclusiva). |
| **Actores secundarios** | Sistema (validación de rangos, bitácora). |
| **Precondiciones** | Administrador autenticado. |
| **Postcondiciones (éxito)** | Parámetros o motivos guardados; el cambio aplica a evaluaciones futuras y queda en bitácora con valor anterior y nuevo. |
| **Postcondiciones (fallo)** | Ningún parámetro cambia; el intento de eludir una regla estructural se rechaza y se registra. |
| **Trazabilidad** | HU: HU-PAR-001 HU-PAR-002 HU-PAR-003 · RF: RF-PAR-001 RF-PAR-002 RF-PAR-003 RF-PAR-004 RF-PAR-005 RF-PAR-006 RF-PAR-007 · RN: RN-AUD-004 RN-AUD-001 RN-MAE-007 RN-AJU-003 RN-AJU-002 RN-SAL-001 RN-CNT-003 RN-MOV-008 |

**Flujo principal**
1. El Administrador abre Parámetros y Configuración.
2. Modifica un umbral o plazo (ajuste menor/mayor, tolerancia de conteo, tiempo máximo en tránsito, plazos de vencimiento, umbral de autorización del Coordinador, inactividad de sesión, destinatarios de alerta, política de toma en salida).
3. El sistema valida que el valor esté dentro del rango admisible.
4. El sistema guarda el cambio, lo aplica a evaluaciones futuras (nunca retroactivamente) y lo registra en la bitácora con valor anterior y nuevo.

**Flujos alternos**
- **A1 · Administrar motivos tipificados** por tipo de operación e indicar cuáles exigen evidencia adjunta; un motivo en uso se desactiva, nunca se elimina.
- **A2 · Consultar el historial de cambios de configuración.**

**Excepciones**
- **E1 · Valor fuera de rango:** se rechaza.
- **E2 · Intento de configurar una regla estructural** (existencia negativa, inmutabilidad del kardex, aprobación propia, escritura del Auditor): el sistema no la ofrece como parametrizable; si se intenta eludir, se rechaza y se registra.

---

### CU-06 — Recepcionar mercancía

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-01** · M-07 Entradas y Recepción |
| **Objetivo** | Incorporar al inventario la mercancía que llega físicamente a la bodega, con registro exacto de qué llegó, cuánto y en qué condición `[MON §8.2]`. |
| **Actor principal** | Coordinador de Bodega. |
| **Actores secundarios** | Auxiliar de Bodega (recepción física) · Jefe de Bodega (excepciones: faltante y sobrante). |
| **Precondiciones** | Llegada física de mercancía a la zona de recepción; las referencias existen y están activas (CU-03); existe la zona de recepción (CU-04). |
| **Postcondiciones (éxito)** | La existencia **en recepción** refleja la mercancía físicamente recibida (pasa a disponible al ubicarse, CU-08; RN-EXI-007, DF5-02); existe un movimiento de entrada en el kardex, atribuido a personas identificadas, con fecha y documento de respaldo; se crea o asocia el lote. |
| **Postcondiciones (fallo)** | El documento queda en su estado (pendiente, recepción parcial, recibido con novedad); no se modifica el inventario. |
| **Trazabilidad** | HU: HU-ENT-001 HU-ENT-002 HU-ENT-003 HU-ENT-004 HU-ENT-005 HU-ENT-007 HU-ENT-008 HU-LOT-001 HU-ENT-009 HU-ENT-010 · RF: RF-ENT-001 RF-ENT-002 RF-ENT-003 RF-ENT-004 RF-ENT-005 RF-ENT-006 RF-ENT-007 RF-ENT-008 RF-ENT-009 RF-ENT-010 RF-ENT-011 RF-ENT-012 RF-ENT-013 RF-ENT-014 RF-ENT-015 RF-ENT-016 RF-ENT-017 · RN: RN-ENT-001 RN-ENT-002 RN-ENT-003 RN-ENT-004 RN-ENT-005 RN-ENT-006 RN-ENT-007 RN-INT-003 RN-LOT-001 RN-EXI-007 RN-INT-008 RN-LOT-006 RN-LOT-007 |

**Flujo principal**
1. El Coordinador crea el documento de entrada (origen, fecha esperada y líneas con referencia, talla, color y cantidad esperada) o selecciona uno existente; el sistema no solicita precio ni datos de orden de compra.
2. El sistema deja el documento en **Pendiente de recepción**.
3. El Auxiliar abre el documento en su tablet.
4. El Auxiliar cuenta físicamente la mercancía pieza por pieza y registra cada pieza (rollo, paquete, bolsa o contenedor agrupado) con su cantidad propia; la cantidad recibida por línea es la suma de sus piezas (RN-LOT-006, RN-LOT-007); el sistema confirma visualmente cada registro guardado.
5. El sistema compara automáticamente cantidad recibida contra esperada, línea por línea.
6. Si coinciden, marca el documento como **Recibido conforme**.
7. El Coordinador —distinto de quien registró la recepción física— verifica y confirma la entrada.
8. El sistema crea o asocia el lote, genera el movimiento de entrada en el kardex e incrementa la existencia **en recepción**, en una ubicación de la zona de recepción; todavía no está disponible (RN-EXI-007).
9. El proceso continúa en CU-07 (identificación) y CU-08 (ubicación).

**Flujos alternos**
- **A1 · Recepción parcial / interrumpida:** el documento queda en **Recepción parcial**; otro usuario puede continuarla, quedando ambos registrados.
- **A2 · Mercancía dañada:** se registra por separado la cantidad conforme y la dañada; la dañada no ingresa como disponible (si ingresa, va a cuarentena como inmovilizada), se abre una novedad (CU-17) y se notifica al Jefe.
- **A3 · Retorno de mercancía que había salido (CU-15 E7):** se registra como entrada nueva que referencia la salida original.
- **A4 · Consulta del historial de entradas** con filtros por período, origen, estado y referencia, exportable.

**Excepciones**
- **E1 · Cantidad recibida menor que la esperada:** se registra faltante de recepción, el documento pasa a **Recibido con novedad** y se notifica al Jefe; el faltante no bloquea confirmar lo efectivamente recibido.
- **E2 · Cantidad recibida mayor que la esperada:** se registra sobrante; requiere autorización del Jefe antes de confirmar y un sobrante no autorizado no ingresa.
- **E3 · Referencia inexistente o inactiva:** el registro se bloquea; solo Coordinador o Jefe pueden crearla; el Auxiliar no.
- **E4 · Documento posiblemente duplicado** (mismo origen, referencia y fecha): el sistema advierte y exige confirmación explícita.
- **E5 · Quien registró la recepción intenta confirmarla:** se rechaza; la confirmación exige un segundo actor.
- **E6 · Sin conectividad:** el registro se retiene localmente y se sincroniza al restablecerse; al sincronizar se valida de nuevo contra el estado vigente y, si ya no cumple las reglas, no se aplica: se rechaza con constancia y, si describe un hecho físico, se abre una novedad (RN-INT-008, DF5-05); el documento no se confirma hasta sincronizar.
- **E7 · Entrada confirmada que requiere corrección:** no se edita; se anula con movimiento inverso, motivo y autorización.

---

### CU-07 — Identificar mercancía con QR

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-02** · M-06 Identificación QR |
| **Objetivo** | Dotar a la mercancía ingresada de un identificador QR único que permita su trazabilidad durante todo su ciclo de vida `[DC-08]`. |
| **Actor principal** | Coordinador de Bodega. |
| **Actores secundarios** | Auxiliar de Bodega (adhiere y verifica la etiqueta) · Administrador (QR de ubicaciones). |
| **Precondiciones** | Entrada confirmada (CU-06); el SKU + Lote existe con referencia, talla, color y lote definidos. |
| **Postcondiciones (éxito)** | Toda unidad de inventario en bodega es identificable mediante escaneo —el QR de su SKU + Lote más el identificador de su ubicación—; ninguna existencia carece de identificador activo (DF5-01). |
| **Postcondiciones (fallo)** | El SKU + Lote queda sin identificador activo y no puede operar hasta resolverse (novedad, CU-17). |
| **Trazabilidad** | HU: HU-QRC-001 HU-QRC-002 HU-QRC-003 HU-QRC-004 HU-QRC-005 · RF: RF-QRC-001 RF-QRC-002 RF-QRC-003 RF-QRC-004 RF-QRC-005 RF-QRC-006 RF-QRC-007 RF-QRC-008 RF-QRC-009 · RN: RN-IDE-001 RN-IDE-002 RN-IDE-003 RN-IDE-004 |

**Flujo principal**
1. El sistema genera un identificador QR único por **SKU + Lote** (referencia + talla + color + lote), que no incluye la ubicación: un mismo SKU + Lote puede estar en varias ubicaciones con el mismo QR (DF5-01).
2. El Coordinador imprime el identificador (individual o por lote de impresión), con información legible de respaldo.
3. El Auxiliar adhiere el identificador a la mercancía o a su contenedor.
4. El Auxiliar escanea el identificador para confirmar su legibilidad.
5. El sistema registra el identificador como **Activo**.
6. El proceso continúa en CU-08.

**Flujos alternos**
- **A1 · Reimpresión por deterioro:** el Auxiliar o Coordinador la solicita indicando motivo; se imprime otra copia del mismo QR: el identificador no cambia, no se crea una nueva identidad y la reimpresión queda consultable en el historial (RN-IDE-004, Q-09).
- **A2 · Código de barras del proveedor:** se admite como identificador secundario asociado al QR primario; permite consultar pero no ejecutar escrituras.
- **A3 · Mercancía sin posibilidad de rotulado individual:** se rotula el contenedor con el QR del SKU + Lote y se registra como pieza de tipo contenedor agrupado, con su cantidad de unidades (RN-LOT-006, F-6); la mezcla de lotes en un contenedor es DECISIÓN PENDIENTE (HD-28).
- **A4 · QR de ubicaciones:** cada ubicación tiene un identificador propio, distinguible del de mercancía, imprimible por zona.

**Excepciones**
- **E1 · Impresión ilegible:** se reimprime; el anterior queda Reemplazado.
- **E2 · Identificador duplicado detectado:** el sistema rechaza la generación; ningún identificador se repite jamás, ni tras la anulación.
- **E3 · Código de barras ya asociado al QR de otro SKU + Lote:** se rechaza.
- **E4 · Se escanea un identificador anulado:** se informa y se rechaza la operación.
- **E5 · Se escanea un identificador no reconocido:** se informa y se ofrece reportar una novedad.

---

### CU-08 — Ubicar mercancía

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-03** · M-07 / M-05 |
| **Objetivo** | Registrar dónde queda físicamente cada unidad de inventario, de modo que el sistema siempre sepa dónde encontrarla. |
| **Actor principal** | Auxiliar de Bodega. |
| **Actores secundarios** | Coordinador de Bodega (reasignación y recepción de desviaciones). |
| **Precondiciones** | Mercancía identificada y lista para almacenar (CU-07); existe al menos una ubicación activa con capacidad disponible. |
| **Postcondiciones (éxito)** | Toda existencia disponible tiene una ubicación conocida; consultar una referencia devuelve dónde está. |
| **Postcondiciones (fallo)** | La mercancía permanece en la zona de recepción (existencia en recepción, no disponible). |
| **Trazabilidad** | HU: HU-ENT-006 HU-BOD-005 HU-BOD-002 HU-MOV-008 · RF: RF-BOD-004 RF-BOD-005 RF-BOD-008 RF-MOV-001 RF-MOV-002 RF-MOV-005 RF-MOV-012 RF-BOD-009 · RN: RN-EXI-002 RN-MOV-001 RN-MOV-002 RN-MOV-003 RN-MOV-004 RN-MOV-010 RN-MOV-011 |

**Flujo principal**
1. El sistema propone una ubicación destino según los criterios configurados (zona por categoría, capacidad, agrupación por referencia).
2. El Auxiliar traslada físicamente la mercancía a la ubicación propuesta.
3. Escanea el identificador de la mercancía, selecciona la pieza que ubica (RN-MOV-011) y después escanea el de la ubicación.
4. El sistema valida que la ubicación esté activa y tenga capacidad.
5. El sistema registra la primera ubicación como **movimiento interno** en el kardex, desde la ubicación de recepción hacia la destino (qué, cuánto, origen, destino, quién, cuándo y documento de entrada), y la cantidad pasa de en recepción a **disponible** en el destino; la existencia total no cambia (RN-MOV-010, DF5-03).
6. El sistema confirma visualmente al Auxiliar que el registro quedó guardado.

**Flujos alternos**
- **A1 · Ubicación distinta a la propuesta:** el sistema lo permite, registra la desviación como información operativa (no como falta) y notifica al Coordinador.
- **A2 · Mercancía repartida en varias ubicaciones:** se registran asignaciones parciales —un movimiento interno por cada una— hasta completar la cantidad; el QR del SKU + Lote no cambia.
- **A3 · Identificador de ubicación ilegible:** el Auxiliar la selecciona de una lista; el sistema registra que no hubo escaneo.

**Excepciones**
- **E1 · Ubicación propuesta llena:** el sistema propone una alternativa; el Auxiliar puede solicitar reasignación al Coordinador.
- **E2 · Ubicación escaneada inactiva:** se rechaza y se solicita otra.
- **E3 · Sin conectividad:** el registro se retiene localmente y se sincroniza al restablecerse; al sincronizar se valida de nuevo contra el estado vigente y, si ya no cumple las reglas, no se aplica: se rechaza con constancia y, si describe un hecho físico, se abre una novedad (RN-INT-008, DF5-05).


---

### CU-09 — Consultar existencia y ubicación

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-04** · M-13 Consulta de Existencia |
| **Objetivo** | Responder en el momento qué hay, cuánto hay y dónde está, sin recuento previo, sustituyendo la consulta al cuaderno `[MON §3, §6]`. |
| **Actor principal** | Todos los roles, con visibilidad diferenciada (§2.7). |
| **Actores secundarios** | Sistema (deriva la cifra del kardex). |
| **Precondiciones** | Usuario autenticado. |
| **Postcondiciones (éxito)** | El usuario obtiene existencia desglosada por talla, color, lote, ubicación y estado; el estado del inventario no se modifica. |
| **Postcondiciones (fallo)** | Se informa la ausencia de resultados o de permiso; nada se modifica. |
| **Trazabilidad** | HU: HU-INV-001 HU-INV-002 HU-INV-003 HU-INV-004 HU-INV-005 HU-INV-006 HU-KDX-006 · RF: RF-INV-001 RF-INV-002 RF-INV-003 RF-INV-004 RF-INV-005 RF-INV-006 RF-INV-007 RF-INV-008 RF-INV-009 · RN: RN-INT-004 RN-INT-006 RN-EXI-003 RN-EXI-004 RN-EXI-005 RN-EXI-006 RN-INT-005 RN-LOT-006 |

**Flujo principal**
1. El usuario indica qué busca: por referencia, por identificador escaneado, por ubicación, por lote o por texto parcial.
2. El sistema devuelve la existencia derivada del kardex, desglosada por talla, color, lote y ubicación.
3. El sistema muestra el desglose por estado: disponible, reservado, inmovilizado, en tránsito y en recepción.
4. El usuario puede abrir el kardex de la unidad seleccionada, según su rol (CU-21).

**Flujos alternos**
- **A1 · Escaneo de etiqueta (Auxiliar):** el escaneo devuelve referencia, talla, color, lote, ubicación y existencia, sin costo ni valorización.
- **A2 · Consulta por ubicación:** lista las unidades presentes, la ocupación frente a la capacidad, indica sobreocupación y permite iniciar un movimiento.
- **A3 · Existencia histórica (Jefe/Auditor):** a una fecha y hora de corte, reconstruida desde el kardex, con resultado idéntico ante consultas repetidas y exportable.
- **A4 · Búsqueda aproximada:** texto parcial tolerante a mayúsculas y tildes, ordenada por relevancia.

**Excepciones**
- **E1 · No existe la referencia buscada:** se informa explícitamente y se ofrece búsqueda aproximada.
- **E2 · Existencia en cero:** se muestra cero con la fecha del último movimiento.
- **E3 · Identificador no reconocido:** se informa y se ofrece reportar novedad (CU-17).
- **E4 · El usuario no tiene permiso sobre el dato (costo, valorización):** el campo se oculta sin exponer su existencia.
- **E5 · Existencia registrada en una ubicación inactiva:** se muestra y se marca como anomalía para el Coordinador.

---

### CU-10 — Reubicar mercancía (movimiento interno)

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-05** · M-09 Movimientos y Transferencias |
| **Objetivo** | Registrar el traslado de mercancía de una ubicación a otra dentro de la misma bodega, manteniendo la exactitud de la existencia por ubicación. |
| **Actor principal** | Auxiliar de Bodega. |
| **Actores secundarios** | Jefe de Bodega (autoriza mover mercancía inmovilizada). |
| **Precondiciones** | La unidad de inventario existe y tiene ubicación actual registrada. |
| **Postcondiciones (éxito)** | La ubicación registrada corresponde a la física real; la existencia total permanece invariante; el movimiento queda en el kardex. |
| **Postcondiciones (fallo)** | Ninguna existencia cambia de ubicación; el rechazo se explica. |
| **Trazabilidad** | HU: HU-MOV-001 HU-MOV-002 HU-MOV-008 HU-MOV-009 · RF: RF-MOV-001 RF-MOV-002 RF-MOV-003 RF-MOV-004 RF-MOV-005 RF-MOV-006 RF-MOV-012 RF-MOV-013 · RN: RN-MOV-004 RN-EXI-003 RN-MOV-005 RN-MOV-002 RN-EXI-006 RN-MOV-006 RN-INT-003 RN-IDE-001 RN-INT-008 RN-MOV-011 |

**Flujo principal**
1. El Auxiliar escanea el identificador de la mercancía, que identifica su SKU + Lote.
2. El sistema muestra las ubicaciones donde ese SKU + Lote tiene existencia; si hay más de una, el Auxiliar indica la de origen escaneando su identificador o seleccionándola, y la selección queda registrada (RN-IDE-001, DF5-01).
3. El Auxiliar selecciona la pieza que mueve; con varias piezas del mismo lote en la ubicación de origen, la ubicación filtra y verifica qué piezas se ofrecen (RN-MOV-011). La pieza se mueve completa: no se divide, y tomar una parte de ella es un corte parcial que se registra como salida (RN-MOV-012, HD-29).
4. El Auxiliar traslada físicamente la mercancía y escanea el identificador de la ubicación destino.
5. El sistema valida la ubicación destino.
6. El sistema registra el movimiento interno en el kardex, descuenta de la ubicación origen y suma a la destino.
7. La existencia total no cambia; el sistema confirma visualmente el registro.

**Flujos alternos**
- **A1 · Movimiento interrumpido a mitad de camino:** queda **En tránsito**; la existencia no está disponible en origen ni en destino hasta cerrarlo y el sistema alerta si supera el tiempo configurado.
- **A2 · Sin conectividad:** el registro se retiene localmente y se sincroniza al restablecerse; al sincronizar se valida de nuevo contra el estado vigente y, si ya no cumple las reglas, no se aplica: se rechaza con constancia y, si describe un hecho físico, se abre una novedad (RN-INT-008, DF5-05).

**Excepciones**
- **E1 · Cantidad mayor que la existencia en origen:** se rechaza.
- **E2 · Destino sin capacidad o inactivo:** se rechaza y se sugiere alternativa.
- **E3 · Destino igual al origen:** se rechaza por inútil.
- **E4 · Mercancía inmovilizada:** se rechaza; solo el Jefe puede autorizar moverla.

---

### CU-11 — Transferir mercancía entre zonas o bodegas

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-06** · M-09 Movimientos y Transferencias |
| **Objetivo** | Trasladar mercancía entre zonas distintas o entre bodegas, con control de despacho y recepción. |
| **Actor principal** | Coordinador de Bodega (crea) · Auxiliar de Bodega (ejecuta despacho y recepción). |
| **Actores secundarios** | Jefe de Bodega (autoriza cuando aplica, resuelve diferencias, cancela en tránsito). |
| **Precondiciones** | Existencia disponible suficiente en el origen. |
| **Postcondiciones (éxito)** | La existencia se traslada íntegra entre ámbitos; despacho y recepción quedan con responsables identificados; ambos movimientos quedan en el kardex. |
| **Postcondiciones (fallo)** | La reserva se libera o la transferencia queda abierta con diferencia hasta resolución del Jefe. |
| **Trazabilidad** | HU: HU-MOV-003 HU-MOV-004 HU-MOV-005 HU-MOV-006 HU-MOV-007 · RF: RF-MOV-007 RF-MOV-008 RF-MOV-009 RF-MOV-010 RF-MOV-011 · RN: RN-EXI-004 RN-EXI-005 RN-MOV-007 RN-MOV-008 RN-MOV-009 RN-EXI-003 · KPI: KPI-15 |

**Flujo principal**
1. El Coordinador crea la transferencia indicando origen, destino, referencias y cantidades.
2. El sistema reserva la existencia en origen (deja de estar disponible) y pone la transferencia en **Pendiente de despacho**, generando la tarea al Auxiliar del origen.
3. El Auxiliar del origen escanea la mercancía y confirma el despacho.
4. El sistema cambia el estado a **En tránsito**.
5. El Auxiliar del destino recibe físicamente y escanea la mercancía.
6. El sistema compara lo despachado contra lo recibido.
7. Si coincide, la transferencia pasa a **Completada**; el sistema descuenta del origen, suma al destino y registra ambos movimientos en el kardex.

**Flujos alternos**
- **A1 · Cancelación antes del despacho:** el Coordinador cancela con motivo; la reserva se libera y la existencia vuelve a disponible.
- **A2 · Cancelación en tránsito:** solo el Jefe, con motivo; genera un movimiento de retorno al origen.
- **A3 · Destino sin capacidad al recibir:** se recibe en la zona de recepción del destino y se resuelve con CU-08.

**Excepciones**
- **E1 · Existencia insuficiente al crear:** se rechaza la creación.
- **E2 · Recibido menor que despachado:** se registra diferencia de transferencia, se abre novedad y requiere resolución del Jefe.
- **E3 · Recibido mayor que despachado:** el sistema rechaza la recepción y escala al Jefe.
- **E4 · Tiempo máximo en tránsito superado:** el sistema genera alerta automática al Jefe (CU-16).

---

### CU-12 — Ajustar inventario

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-07** · M-10 Ajustes de Inventario |
| **Objetivo** | Corregir la existencia registrada cuando difiere de la física real, dejando evidencia auditable de la causa `[MON §8.2]`. Es el proceso más sensible del sistema. |
| **Actor principal** | Coordinador de Bodega (solicita). |
| **Actores secundarios** | Jefe de Bodega (aprueba ajuste menor) · Administrador (aprueba ajuste mayor y ajustes sobre mercancía inmovilizada) · Auditor (recibe alerta de patrón). |
| **Precondiciones** | La unidad de inventario existe; hay un motivo tipificado disponible. |
| **Postcondiciones (éxito)** | La existencia registrada corresponde a la física; el kardex muestra quién detectó la diferencia, por qué, quién la autorizó y cuándo; la unidad queda marcada como ajustada. |
| **Postcondiciones (fallo)** | La existencia no cambia; el rechazo y su justificación quedan registrados. |
| **Trazabilidad** | HU: HU-AJU-001 HU-AJU-002 HU-AJU-003 HU-AJU-004 HU-AJU-005 HU-AJU-006 HU-TAR-002 · RF: RF-AJU-001 RF-AJU-002 RF-AJU-003 RF-AJU-004 RF-AJU-005 RF-AJU-006 RF-AJU-007 RF-AJU-008 RF-AJU-009 RF-AJU-010 · RN: RN-AJU-001 RN-AJU-002 RN-AJU-003 RN-EXI-001 RN-EXI-006 RN-AJU-004 RN-AJU-005 RN-AJU-006 RN-AJU-007 · KPI: KPI-08 KPI-14 KPI-22 |

**Flujo principal**
1. El Coordinador identifica la unidad de inventario a ajustar y el sistema muestra su existencia registrada.
2. El Coordinador ingresa la existencia física real observada; el sistema calcula la diferencia y su sentido (sobrante o faltante).
3. El Coordinador selecciona un motivo tipificado obligatorio y adjunta observación y, si el motivo lo exige, evidencia.
4. El sistema clasifica el ajuste como menor o mayor según el umbral configurado, registra el umbral aplicado y enruta la solicitud al aprobador que corresponde.
5. El aprobador revisa unidad, diferencia, motivo, solicitante y evidencia.
6. El aprobador aprueba.
7. El sistema genera el movimiento de ajuste en el kardex, actualiza la existencia y notifica al solicitante.

**Flujos alternos**
- **A1 · Rechazo:** el aprobador rechaza con justificación obligatoria; la existencia no cambia; el rechazo queda registrado con la misma permanencia que una aprobación.
- **A2 · Ajuste derivado de un conteo o de una novedad:** llega desde CU-13, CU-14 o CU-17 conservando el vínculo de origen.
- **A3 · Solicitud sin resolver en el plazo configurado:** escala automáticamente al nivel superior y genera alerta.

**Excepciones**
- **E1 · Solicitante = aprobador designado:** el sistema escala al nivel superior; si no existe, la solicitud se bloquea y se notifica al Administrador.
- **E2 · El ajuste dejaría la existencia en negativo:** se rechaza sin excepción; la regla no es configurable.
- **E3 · Ajustes repetidos sobre la misma unidad en la ventana configurada:** alerta de patrón anómalo al Jefe y al Auditor.
- **E4 · Ajuste sobre mercancía inmovilizada:** requiere aprobación del Administrador sin importar el monto.
- **E5 · Ajuste aplicado con error:** no se edita ni se revierte; se corrige con un nuevo ajuste.

---

### CU-13 — Ejecutar un conteo cíclico

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-08** · M-11 Conteos |
| **Objetivo** | Verificar periódicamente la exactitud del inventario por partes, sin detener la operación de la bodega `[MON §8.2]`; alimenta el KPI-01. |
| **Actor principal** | Coordinador de Bodega (programa y supervisa). |
| **Actores secundarios** | Auxiliar de Bodega (cuenta) · Jefe de Bodega (cierra y decide ajustes). |
| **Precondiciones** | Existen ubicaciones o referencias con existencia registrada. |
| **Postcondiciones (éxito)** | Se conoce la exactitud del ámbito contado; la operación no se interrumpió; las diferencias quedaron identificadas con responsable y motivo. |
| **Postcondiciones (fallo)** | Conteo vencido o abortado: la existencia congelada se libera y no se generan ajustes. |
| **Trazabilidad** | HU: HU-CNT-001 HU-CNT-002 HU-CNT-003 HU-CNT-004 HU-CNT-005 HU-CNT-008 HU-CNT-009 HU-CNT-010 · RF: RF-CNT-001 RF-CNT-002 RF-CNT-003 RF-CNT-004 RF-CNT-005 RF-CNT-006 RF-CNT-007 RF-CNT-008 RF-CNT-009 RF-CNT-010 RF-CNT-013 RF-CNT-014 · RN: RN-CNT-001 RN-CNT-002 RN-CNT-003 RN-CNT-004 RN-NOV-001 RN-CNT-005 RN-AJU-003 RN-CNT-009 · KPI: KPI-01 KPI-03 KPI-04 KPI-06 |

**Flujo principal**
1. El Coordinador programa el conteo definiendo su ámbito (ubicaciones, referencias o categorías).
2. El sistema genera las tareas de conteo, las asigna a auxiliares y congela la existencia teórica del ámbito.
3. El Auxiliar recibe sus tareas en la tablet, escanea la ubicación y cuenta físicamente, a mano, pieza por pieza (RN-CNT-009).
4. El Auxiliar registra la cantidad de cada pieza contada, y la cantidad contada de la unidad de inventario es la suma de sus piezas; el sistema no le muestra la cantidad esperada, ni antes ni después.
5. El sistema compara lo contado contra la existencia congelada y clasifica cada línea: conforme, sobrante o faltante.
6. Si hay diferencias sobre la tolerancia, el sistema exige un segundo conteo por un contador distinto.
7. El Coordinador revisa las diferencias confirmadas.
8. El Jefe (que no ejecutó el conteo) cierra el conteo y decide, por línea, ajustar, no ajustar o recontar; las líneas ajustadas generan solicitudes de ajuste (CU-12).
9. El sistema calcula la exactitud del ámbito contado y alimenta el KPI-01.

**Flujos alternos**
- **A1 · Reasignación de tarea** cuando el auxiliar no está: ambos responsables quedan registrados; un conteo parcial se conserva.
- **A2 · Segundo conteo también difiere:** escala al Jefe para verificación presencial.
- **A3 · Movimiento durante el conteo:** se registra y se señala en la conciliación; la existencia congelada no se altera.

**Excepciones**
- **E1 · Aparece mercancía sin identificador:** se registra novedad (CU-17); no se cuenta hasta identificarla.
- **E2 · Conteo no cerrado en el plazo:** alerta; la existencia congelada se libera si excede el máximo y el conteo queda vencido.
- **E3 · Ubicación vacía con existencia registrada:** se registra como faltante total; requiere ajuste con motivo.
- **E4 · Quien ejecutó el conteo intenta cerrarlo o hacer el segundo conteo:** se rechaza.

---

### CU-14 — Ejecutar un conteo general

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-09** · M-11 Conteos |
| **Objetivo** | Verificar la totalidad del inventario en un momento determinado, estableciendo un punto de referencia completo. |
| **Actor principal** | Jefe de Bodega. |
| **Actores secundarios** | Coordinadores y Auxiliares (ejecutan) · Auditor (observa) · Administrador (notificado por diferencia crítica). |
| **Precondiciones** | Autorización del Jefe; la operación de bodega es suspendible durante la ventana de conteo. |
| **Postcondiciones (éxito)** | Fotografía verificada del inventario completo con todas las diferencias identificadas, ajustadas y trazables; el registro de movimientos se desbloquea; KPI-01 y KPI-02 actualizados. |
| **Postcondiciones (fallo)** | Conteo abortado: se libera la existencia congelada y los conteos parciales se conservan como evidencia, sin generar ajustes. |
| **Trazabilidad** | HU: HU-CNT-006 HU-CNT-007 HU-CNT-005 HU-CNT-008 HU-CNT-011 · RF: RF-CNT-011 RF-CNT-012 RF-CNT-003 RF-CNT-004 RF-CNT-006 RF-CNT-008 RF-CNT-009 RF-CNT-010 RF-CNT-013 RF-CNT-015 · RN: RN-CNT-006 RN-CNT-007 RN-CNT-008 RN-CNT-001 RN-CNT-002 RN-CNT-003 RN-CNT-004 · KPI: KPI-02 KPI-03 |

**Flujo principal**
1. El Jefe programa el conteo general con fecha y hora de corte.
2. El sistema notifica a todos los usuarios con la anticipación configurada.
3. Al llegar el corte, el sistema bloquea el registro de movimientos y congela la existencia teórica completa.
4. El sistema genera tareas cubriendo la totalidad de las ubicaciones.
5. Los Auxiliares cuentan por ubicación, escaneando, sin ver la cantidad esperada.
6. El sistema consolida los conteos, detecta ubicaciones no cubiertas y clasifica todas las diferencias.
7. Se ejecutan segundos conteos donde corresponda, por personas distintas.
8. El Jefe revisa el consolidado, cierra el conteo y genera los ajustes derivados (CU-12).
9. El sistema desbloquea el registro de movimientos y calcula la exactitud global (KPI-01 y KPI-02).

**Flujos alternos**
- **A1 · Movimiento de excepción durante el bloqueo:** solo el Jefe puede autorizarlo y queda marcado como excepción en el kardex.
- **A2 · Conteo excede la ventana prevista:** alerta; el Jefe decide continuar o abortar.

**Excepciones**
- **E1 · Ubicaciones sin contar al cierre:** el sistema impide cerrar hasta cubrirlas o justificar su exclusión.
- **E2 · Diferencia global sobre el umbral crítico:** el sistema notifica al Administrador y al Auditor antes de permitir el cierre.
- **E3 · Mercancía encontrada sin registro:** se registra novedad y requiere ajuste por sobrante con motivo tipificado (CU-17).
- **E4 · Conteo abortado:** ver postcondición de fallo.

---

### CU-15 — Registrar la salida de mercancía

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-10** · M-08 Salidas |
| **Objetivo** | Retirar mercancía del inventario dejando registro de qué salió, cuánto, con qué destino y bajo qué autorización `[MON §8.2]`. |
| **Actor principal** | Jefe de Bodega (autoriza) · Auxiliar de Bodega (ejecuta). |
| **Actores secundarios** | Coordinador de Bodega (autoriza dentro de su umbral, registra retornos). |
| **Precondiciones** | Existencia disponible suficiente; autorización vigente. |
| **Postcondiciones (éxito)** | La existencia refleja la salida; el kardex documenta qué salió, cuánto, por qué, quién lo autorizó y quién lo ejecutó. |
| **Postcondiciones (fallo)** | La reserva se libera; la existencia vuelve a disponible; no se registra la salida. |
| **Trazabilidad** | HU: HU-SAL-001 HU-SAL-002 HU-SAL-003 HU-SAL-004 HU-SAL-005 HU-SAL-006 HU-SAL-007 HU-SAL-008 HU-SAL-009 · RF: RF-SAL-001 RF-SAL-002 RF-SAL-003 RF-SAL-004 RF-SAL-005 RF-SAL-006 RF-SAL-007 RF-SAL-008 RF-SAL-009 RF-SAL-010 RF-SAL-011 RF-SAL-012 RF-SAL-013 RF-SAL-014 · RN: RN-SAL-002 RN-EXI-003 RN-EXI-004 RN-SAL-001 RN-SAL-003 RN-SAL-004 RN-EXI-001 RN-EXI-006 RN-SAL-005 RN-SAL-006 RN-SAL-007 RN-SAL-008 RN-SAL-009 · KPI: KPI-11 KPI-13 KPI-16 |

> **Frontera de alcance `[DC-03]`.** El sistema registra la salida física del inventario. No gestiona el pedido de venta, la factura, el documento de despacho comercial ni la orden de producción que la originan; recibe un motivo tipificado y actúa sobre el inventario, nada más.

**Flujo principal**
1. Se solicita la salida indicando referencias, cantidades y motivo tipificado.
2. El sistema verifica la existencia disponible.
3. El Jefe autoriza la salida, o el Coordinador si está dentro de su umbral; el sistema reserva la existencia.
4. El sistema genera la tarea de preparación y la asigna a un Auxiliar, indicando las ubicaciones de toma según la política configurada.
5. El Auxiliar escanea lo que toma y selecciona la pieza tomada; si corta parte de un rollo, registra la cantidad cortada (RN-SAL-008, RN-MOV-011); el sistema valida que lo escaneado corresponda a lo solicitado y cuenta cada pieza tomada una sola vez (RN-SAL-004, RN-SAL-009).
6. El Auxiliar confirma la preparación completa.
7. El sistema registra el movimiento de salida en el kardex, descuenta la existencia y libera la reserva.

**Flujos alternos**
- **A1 · Salida parcial autorizada** por la cantidad disponible cuando la solicitada es insuficiente.
- **A2 · Baja por daño:** requiere motivo tipificado específico, observación, evidencia y aprobación del Jefe, cualquiera sea la cantidad; alimenta el reporte de mermas.
- **A3 · Autorización escalada:** por encima del umbral del Coordinador la solicitud se enruta al Jefe.

**Excepciones**
- **E1 · Existencia disponible insuficiente:** el sistema rechaza y ofrece salida parcial con autorización; nunca deja existencia negativa.
- **E2 · Escaneo de unidad distinta a la solicitada:** se rechaza indicando la discrepancia (referencia, talla, color o lote).
- **E3 · Existencia física ausente pese a estar registrada:** se registra novedad (CU-17) y se abre ajuste (CU-12); la salida queda pendiente.
- **E4 · Mercancía inmovilizada:** rechazada; requiere liberación previa por el Jefe.
- **E5 · Salida autorizada no ejecutada en el plazo:** la reserva se libera automáticamente y se alerta al solicitante.
- **E6 · Salida sin motivo tipificado:** no se acepta.
- **E7 · Devolución posterior:** se registra como entrada nueva (CU-06) que referencia la salida original; la salida no se reversa.

---

### CU-16 — Gestionar alertas operativas

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-11** · M-15 Alertas y Reglas |
| **Objetivo** | Convertir una condición anómala detectada por reglas en una acción correctiva antes de que produzca daño operativo `[MON §3, §7.1]` `[DC-07]`. |
| **Actor principal** | Jefe de Bodega · Coordinador de Bodega. |
| **Actores secundarios** | Sistema (evalúa, genera, dirige y escala) · Administrador (configura umbrales y recibe la frecuencia de disparo). |
| **Precondiciones** | El umbral de la alerta está configurado (CU-05, CU-03). |
| **Postcondiciones (éxito)** | La condición anómala fue atendida o descartada con motivo, o se cerró al cesar; el historial registra quién, cuándo y qué se hizo. |
| **Postcondiciones (fallo)** | La alerta permanece activa y, si es crítica, escala. |
| **Trazabilidad** | HU: HU-ALE-001 HU-ALE-002 HU-ALE-003 HU-ALE-004 HU-ALE-005 · RF: RF-ALE-001 RF-ALE-002 RF-ALE-003 RF-ALE-004 RF-ALE-005 RF-ALE-006 RF-ALE-007 · RN: RN-ALE-001 RN-ALE-002 RN-ALE-003 RN-ALE-004 RN-ALE-005 · KPI: KPI-19 KPI-20 KPI-21 |

**Flujo principal**
1. El sistema evalúa continuamente las condiciones de alerta configuradas (solo por reglas y umbrales; sin modelos predictivos).
2. Al cumplirse una condición, el sistema genera la alerta con su severidad.
3. El sistema la dirige al rol responsable según su tipo.
4. El destinatario la visualiza en su panel y recibe notificación si aplica.
5. El destinatario ejecuta la acción correctiva o la descarta con motivo.
6. El sistema registra la atención: quién, cuándo y qué se hizo.
7. Si la condición desaparece, el sistema cierra la alerta automáticamente.

**Tipos de alerta del MVP** (RF-ALE-004): ruptura de stock inminente · sobre stock · existencia en cero · lote próximo a vencer inmovilización · movimiento en tránsito prolongado · ajustes recurrentes · exactitud por debajo del objetivo · conteo vencido · ubicación sobreocupada · solicitud de ajuste sin resolver.

**Flujos alternos**
- **A1 · Recalibración de umbrales:** el sistema reporta al Administrador los tipos con frecuencia de disparo anómala.
- **A2 · Zona o rol sin destinatario activo:** la alerta escala al superior.

**Excepciones**
- **E1 · Condición repetida:** se agrupa; no se generan duplicados de una condición vigente.
- **E2 · Descarte sin motivo:** el sistema lo exige y no permite cerrar sin él.
- **E3 · Alerta crítica sin atender en plazo:** escala automáticamente al rol superior con notificación adicional.
- **E4 · Condición cesa antes de atenderse:** se cierra automáticamente y queda en el historial como no atendida.


---

### CU-17 — Reportar y resolver novedades de mercancía

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-12** · M-12 Novedades de Mercancía |
| **Objetivo** | Permitir que cualquier operario reporte una anomalía física que el sistema no puede detectar por sí solo, sin exponerse `[MON §4]` `[PR-06]`. |
| **Actor principal** | Auxiliar de Bodega (reporta). |
| **Actores secundarios** | Coordinador y Jefe de Bodega (resuelven y reciben el escalamiento). |
| **Precondiciones** | Usuario autenticado. |
| **Postcondiciones (éxito)** | La anomalía llegó al sistema; su tratamiento quedó documentado y vinculado al movimiento que la resolvió; la novedad queda cerrada con constancia. |
| **Postcondiciones (fallo)** | La novedad permanece abierta y escala al Jefe al vencer el plazo. |
| **Trazabilidad** | HU: HU-NOV-001 HU-NOV-002 HU-NOV-003 HU-NOV-004 · RF: RF-NOV-001 RF-NOV-002 RF-NOV-003 RF-NOV-004 RF-NOV-005 RF-NOV-006 RF-NOV-007 RF-NOV-008 · RN: RN-NOV-001 RN-NOV-002 RN-NOV-003 RN-MAE-007 · KPI: KPI-23 |

**Flujo principal**
1. El Auxiliar abre el reporte de novedad desde su tablet en pocos pasos.
2. Selecciona el tipo de novedad de una lista tipificada.
3. Escanea el identificador si existe, o declara que no lo hay.
4. Indica la ubicación y describe brevemente lo observado; puede adjuntar fotografía.
5. El sistema registra la novedad, sin presentarla ni contabilizarla como falta del reportante, y la dirige al Coordinador de la zona.
6. El Coordinador la evalúa y determina la acción: ajuste, reidentificación, reubicación o baja.
7. El sistema vincula la novedad con el movimiento que la resuelve.
8. La novedad se cierra con constancia de la resolución.

**Flujos alternos**
- **A1 · Novedad que implica ajuste de existencia:** deriva a CU-12 conservando el vínculo.
- **A2 · Mercancía encontrada sin ningún registro:** no se cuenta ni se usa hasta ser identificada; se crea la unidad, se genera ajuste por sobrante con motivo tipificado, aprobación del Jefe, identificador QR y ubicación.

**Excepciones**
- **E1 · Novedad sin resolver en el plazo configurado:** escala al Jefe y genera alerta.
- **E2 · Novedad sobre una unidad con novedad abierta:** se vincula a la existente; no se duplica.
- **E3 · Novedad reportada por error:** se cierra como improcedente, con justificación; no se elimina.

---

### CU-18 — Auditar el inventario

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-13** · M-18 Auditoría y Bitácora |
| **Objetivo** | Verificar de forma independiente la integridad del registro, la trazabilidad de los movimientos y el respeto a la segregación de funciones `[PR-01, PR-02]`. |
| **Actor principal** | Auditor. |
| **Actores secundarios** | Administrador (recibe hallazgos críticos) · Administrador y Jefe (consultan observaciones). |
| **Precondiciones** | Usuario con rol Auditor autenticado. |
| **Postcondiciones (éxito)** | Existe evidencia independiente de que el registro es íntegro y trazable; las observaciones quedan en un registro separado; el reporte de auditoría queda exportado. |
| **Postcondiciones (fallo)** | Los hallazgos críticos quedan registrados y notificados; el inventario no se modifica. |
| **Trazabilidad** | HU: HU-KDX-001 HU-KDX-002 HU-KDX-003 HU-AUD-001 HU-AUD-002 HU-AUD-003 HU-AUD-004 HU-AJU-006 HU-INV-005 · RF: RF-KDX-006 RF-AUD-001 RF-AUD-002 RF-AUD-003 RF-AUD-004 RF-AUD-005 RF-AUD-006 RF-AUD-007 · RN: RN-INT-004 RN-AUD-005 RN-AUD-001 RN-AUD-002 RN-AJU-001 RN-INT-002 · KPI: KPI-09 KPI-14 |

**Flujo principal**
1. El Auditor define el alcance: período, referencias, ubicaciones, usuarios o tipos de movimiento.
2. Consulta el kardex de las unidades en alcance.
3. Verifica la continuidad: toda existencia actual es explicable por la suma de movimientos.
4. Revisa los ajustes: motivo, evidencia, solicitante y aprobador.
5. Verifica que no existan aprobaciones propias (ajustes, salidas, conteos).
6. Contrasta los resultados de conteo contra la existencia registrada.
7. Revisa los movimientos anulados y sus justificaciones.
8. Consulta la bitácora de auditoría del período.
9. Registra observaciones en un registro separado.
10. Exporta el reporte de auditoría; la exportación queda en la bitácora.

**Flujos alternos**
- **A1 · Existencia histórica:** el Auditor reconstruye la existencia a una fecha de corte a partir del kardex.
- **A2 · Cierre de observaciones:** una observación se cierra con respuesta; nunca se elimina.

**Excepciones**
- **E1 · Existencia no explicable por la suma de movimientos:** hallazgo crítico; se notifica al Administrador.
- **E2 · Ajuste sin motivo o sin evidencia exigida:** hallazgo; el sistema no debió permitirlo.
- **E3 · Aprobación propia detectada:** hallazgo crítico; indica falla de la regla.
- **E4 · Movimiento sin usuario atribuible:** hallazgo crítico.
- **E5 · El Auditor intenta modificar un dato:** el sistema lo impide sin excepción y lo registra.
- **E6 · Bitácora con discontinuidad:** hallazgo crítico de integridad.

---

### CU-19 — Cerrar la jornada operativa

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | **PN-14** · M-20 / M-17 (elemento 39 del backlog MVP) |
| **Objetivo** | Consolidar la actividad del día, detectar pendientes y dejar la bodega en estado consistente. |
| **Actor principal** | Jefe de Bodega · Coordinador de Bodega. |
| **Actores secundarios** | Sistema (consolida, detecta y bloquea el cierre por registros sin sincronizar). |
| **Precondiciones** | Jornada con movimientos registrados. |
| **Postcondiciones (éxito)** | Cada jornada cierra con un estado conocido, sin registros pendientes ocultos y con la responsabilidad de los pendientes explícitamente traspasada al turno siguiente; el cierre queda registrado con quién lo ejecutó. |
| **Postcondiciones (fallo)** | El cierre no se registra; el sistema lo trata como omisión y alerta al Jefe al día siguiente. |
| **Trazabilidad** | HU: HU-TAR-004 HU-TAR-005 · RF: RF-TAR-006 RF-TAR-007 RF-TAR-008 · RN: RN-INT-003 RN-MOV-006 · RNF: RNF-DSP-002 RNF-DSP-003 · RG: RG-03, RG-08 |

> **Nota de trazabilidad — hallazgo H-10 (resuelto).** El SPEC v1.0 a v1.2 modelaba PN-14 (§3) y lo incluía en el backlog del MVP (elemento 39, §12.2) sin historia ni requisito. El Director resolvió DEC-05 (a) el 30-sep-2026: el SPEC v1.3 crea HU-TAR-004, HU-TAR-005 y RF-TAR-006 a RF-TAR-008, que este caso de uso recorre.

**Flujo principal**
1. El sistema consolida los movimientos de la jornada.
2. El sistema identifica pendientes: recepciones sin confirmar, movimientos en tránsito, tareas de conteo abiertas, ajustes sin resolver, novedades sin atender y alertas activas.
3. El Coordinador revisa el listado de pendientes y resuelve lo que puede resolverse en el turno.
4. Lo no resuelto se traspasa explícitamente al turno siguiente.
5. El Jefe revisa el resumen de la jornada y los indicadores del día.
6. El sistema registra el cierre con constancia de quién lo ejecutó.

**Flujos alternos**
- **A1 · Movimientos en tránsito al cierre:** se listan explícitamente y se traspasan; generan alerta si superan el plazo.

**Excepciones**
- **E1 · Registros sin sincronizar por falta de conectividad:** el sistema impide el cierre hasta sincronizar.
- **E2 · Cierre no ejecutado:** el sistema lo registra como omisión y alerta al Jefe al día siguiente.
- **E3 · Diferencia significativa detectada en el consolidado:** se genera alerta antes de permitir el cierre.

---

### CU-20 — Gestionar lotes

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | M-04 Gestión de Lotes |
| **Objetivo** | Rastrear un problema de calidad u origen hasta el conjunto de mercancía que lo comparte `[MON §7.1]`, y poder actuar sobre el lote completo. |
| **Actor principal** | Jefe de Bodega. |
| **Actores secundarios** | Coordinador (crea el lote al confirmar la entrada, CU-06) · Administrador (puede liberar). |
| **Precondiciones** | Existen lotes creados por entradas confirmadas. |
| **Postcondiciones (éxito)** | Lote consultado, inmovilizado o liberado; el evento queda en la bitácora. |
| **Postcondiciones (fallo)** | El estado del lote no cambia. |
| **Trazabilidad** | HU: HU-LOT-001 HU-LOT-002 HU-LOT-003 HU-LOT-004 HU-KDX-004 · RF: RF-LOT-001 RF-LOT-002 RF-LOT-003 RF-LOT-004 RF-LOT-005 RF-LOT-006 · RN: RN-LOT-001 RN-LOT-002 RN-LOT-003 RN-LOT-004 RN-LOT-005 RN-MAE-006 |

**Flujo principal (inmovilizar un lote)**
1. El Jefe consulta la distribución del lote: ubicaciones, cantidades, total y estado.
2. Elige inmovilizar el lote, desde la consulta o desde su kardex.
3. Selecciona un motivo tipificado.
4. El sistema inmoviliza toda la existencia del lote, en todas sus ubicaciones, de forma simultánea; la existencia deja de contar como disponible.
5. Toda salida, transferencia o movimiento sobre esa existencia se rechaza mientras dure la inmovilización.
6. El sistema registra la inmovilización en la bitácora.

**Flujos alternos**
- **A1 · Liberar el lote:** solo el Jefe o el Administrador, con motivo tipificado.
- **A2 · Listar lotes por antigüedad:** ordenados por fecha de ingreso, con días en bodega y destacando los que superan el umbral; genera alerta informativa al Jefe.
- **A3 · Consultar el kardex del lote:** consolida los movimientos de todas sus unidades.

**Excepciones**
- **E1 · Código de lote repetido dentro del SKU:** se rechaza.
- **E2 · Intento de inmovilizar parcialmente un lote:** no es posible.
- **E3 · Intento de liberar por un rol no autorizado:** se rechaza.

---

### CU-21 — Consultar el kardex y verificar la trazabilidad

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | M-14 Kardex y Trazabilidad |
| **Objetivo** | Reconstruir la historia completa de una unidad, un lote o una ubicación y responder las seis preguntas de trazabilidad: qué, cuánto, dónde, quién, cuándo y por qué `[CD-21]`. |
| **Actor principal** | Auditor y Jefe de Bodega (kardex completo). |
| **Actores secundarios** | Administrador y Coordinador (según §2.7) · Auxiliar (solo lo que él movió, últimos 30 días) · Sistema (registra cada movimiento). |
| **Precondiciones** | Usuario autenticado; existen movimientos registrados. |
| **Postcondiciones (éxito)** | El usuario obtiene la historia cronológica sin huecos; la consulta no modifica nada. |
| **Postcondiciones (fallo)** | Se informa la ausencia de resultados o de permiso. |
| **Trazabilidad** | HU: HU-KDX-001 HU-KDX-002 HU-KDX-003 HU-KDX-004 HU-KDX-005 HU-KDX-006 · RF: RF-KDX-001 RF-KDX-002 RF-KDX-003 RF-KDX-004 RF-KDX-005 RF-KDX-006 RF-KDX-007 RF-KDX-008 RF-KDX-009 · RN: RN-INT-002 RN-INT-001 RN-INT-004 RN-AJU-007 RN-LOT-007 · KPI: KPI-05 KPI-09 KPI-11 KPI-17 KPI-24 |

**Flujo principal**
1. El usuario elige la unidad de inventario, el lote o la ubicación.
2. El sistema presenta los movimientos en orden cronológico con fecha, hora, tipo, cantidad, existencia resultante, ubicación, usuario, motivo y documento.
3. El usuario aplica filtros por tipo, período, usuario y motivo.
4. El usuario exporta el kardex si lo necesita.

**Flujos alternos**
- **A1 · Corrección de un error:** no se edita ni elimina el movimiento; el Jefe o Administrador genera un movimiento inverso con motivo y autorización y ambos quedan visibles.
- **A2 · Verificación de integridad:** el Auditor verifica que la existencia actual equivale a la suma algebraica de los movimientos, por unidad, lote o globalmente.
- **A3 · Consulta del Auxiliar:** restringida a las unidades que él movió y a los últimos 30 días, sin valorización ni indicadores de error personal.

**Excepciones**
- **E1 · Discrepancia entre existencia y suma de movimientos:** hallazgo crítico de integridad.
- **E2 · Se busca editar o eliminar un movimiento confirmado, con cualquier rol:** el sistema no ofrece esas funciones.
- **E3 · Movimiento sin usuario atribuible:** no debe existir; si se detecta, es hallazgo crítico.

---

### CU-22 — Generar reportes y exportar datos

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | M-16 Reportes y Exportación Analítica |
| **Objetivo** | Entregar información consolidada al usuario, calcular los indicadores y poner los datos a disposición de la herramienta analítica externa `[DC-06]` `[MON §8.2]`. |
| **Actor principal** | Jefe de Bodega · Administrador · Auditor. |
| **Actores secundarios** | Coordinador (reportes operativos) · Sistema (cálculo de KPI, bitácora, generación programada). |
| **Precondiciones** | Usuario autenticado con permiso sobre el reporte solicitado. |
| **Postcondiciones (éxito)** | Reporte generado con fecha, hora y usuario; exportación registrada en la bitácora; datos expuestos respetando la visibilidad por rol. |
| **Postcondiciones (fallo)** | No se genera o no se exporta; ningún dato se modifica. |
| **Trazabilidad** | HU: HU-REP-001 HU-REP-002 HU-REP-003 HU-REP-004 HU-CNT-008 · RF: RF-REP-001 RF-REP-002 RF-REP-003 RF-REP-004 RF-REP-005 RF-REP-006 RF-REP-007 RF-REP-008 · RN: RN-AUD-003 RN-AUD-001 · KPI: KPI-01 a KPI-24 |

**Flujo principal**
1. El usuario elige el reporte (existencia, movimientos, entradas, salidas, ajustes, conteos, exactitud, alertas, novedades, productividad).
2. Define los filtros.
3. El sistema genera el reporte declarando fecha, hora de generación y usuario que lo generó; la valorización solo aparece para roles autorizados.
4. El usuario exporta en formato tabular; la exportación queda en la bitácora con usuario, alcance y fecha.

**Flujos alternos**
- **A1 · Exportación para la herramienta analítica:** el Administrador habilita la exposición estructurada de datos; toda extracción queda en bitácora y respeta la visibilidad por rol.
- **A2 · Reporte programado:** el Jefe define reporte, periodicidad y destinatarios; el sistema lo genera y lo pone a disposición; puede desactivarse.
- **A3 · Cálculo de indicadores:** el sistema calcula los 24 KPI del Cap. 10 del SPEC.

**Excepciones**
- **E1 · Reporte con valorización solicitado por Coordinador o Auxiliar:** se omite la valorización.
- **E2 · Se intenta diseñar un tablero analítico dentro del sistema:** fuera de alcance `[DC-06]`.

---

### CU-23 — Consultar el dashboard operativo y el panel de tareas

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | M-17 Dashboard Operativo · M-20 Notificaciones y Tareas |
| **Objetivo** | Dar a cada rol una vista inmediata del estado de la bodega y de lo que requiere su atención. |
| **Actor principal** | Jefe de Bodega (dashboard completo) · Auxiliar de Bodega (panel de tareas). |
| **Actores secundarios** | Coordinador (dashboard de su zona) · Administrador y Auditor (dashboard completo). |
| **Precondiciones** | Usuario autenticado; el rol determina la vista. |
| **Postcondiciones (éxito)** | El usuario ve el estado y sus pendientes y puede navegar al detalle de cada elemento. |
| **Postcondiciones (fallo)** | No aplica: la consulta no altera el inventario. |
| **Trazabilidad** | HU: HU-DSH-001 HU-DSH-002 HU-DSH-003 HU-TAR-001 · RF: RF-DSH-001 RF-DSH-002 RF-DSH-003 RF-DSH-004 RF-TAR-001 RF-TAR-002 RF-TAR-003 · RN: RN-INT-006 · KPI: KPI-01 |

**Flujo principal**
1. Al iniciar sesión el sistema presenta la vista del rol: dashboard operativo para Jefe, Administrador y Auditor; dashboard restringido a su zona para el Coordinador; panel de tareas para el Auxiliar.
2. El dashboard muestra existencia total y desglose por estado, alertas activas por severidad, pendientes (recepciones sin confirmar, tránsitos, ajustes por aprobar, conteos abiertos, novedades sin resolver), movimientos del día y exactitud vigente.
3. El panel de tareas muestra, ordenadas por prioridad, las tareas del turno con tipo, referencia, cantidad y ubicación; las no vistas se destacan.
4. El usuario navega desde cualquier elemento hacia su detalle.

**Flujos alternos**
- **A1 · Coordinador:** ve solo su zona, sin valorización, y puede reasignar tareas de su equipo.

**Excepciones**
- **E1 · El Auxiliar solicita el dashboard operativo:** no se le presenta; solo su panel de tareas, sin indicadores de desempeño individual.

---

### CU-24 — Gestionar tareas, notificaciones y aprobaciones

| Campo | Contenido |
|---|---|
| **Proceso / módulo SPEC** | M-20 Notificaciones y Tareas |
| **Objetivo** | Llevar a cada persona lo que debe hacer y lo que debe saber, en el dispositivo en que trabaja `[DC-05]`. |
| **Actor principal** | Sistema (genera tareas y notificaciones). |
| **Actores secundarios** | Todos los roles (reciben); Coordinador (reasigna); Jefe y Administrador (reciben solicitudes por aprobar). |
| **Precondiciones** | Existe trabajo asignado o una solicitud pendiente. |
| **Postcondiciones (éxito)** | Cada tarea tiene un responsable identificado y se cierra por la ejecución del movimiento asociado; las solicitudes de aprobación llegan al aprobador y el resultado llega al solicitante. |
| **Postcondiciones (fallo)** | La tarea permanece abierta y escala por vencimiento. |
| **Trazabilidad** | HU: HU-TAR-001 HU-TAR-002 HU-TAR-003 HU-CNT-009 · RF: RF-TAR-001 RF-TAR-002 RF-TAR-003 RF-TAR-004 RF-TAR-005 · RN: RN-AJU-005 RN-ALE-002 RN-NOV-002 RN-CNT-003 RN-INT-001 |

**Flujo principal**
1. El sistema genera una tarea al asignarse trabajo (recepción, ubicación, conteo, preparación de salida, transferencia).
2. El responsable la ve en su panel, ordenada por prioridad.
3. El responsable ejecuta el movimiento asociado.
4. El sistema cierra la tarea por la confirmación del movimiento, no por declaración del usuario.
5. Para las solicitudes de ajuste o de salida que requieren aprobación, el sistema las presenta al aprobador ordenadas por antigüedad y monto y notifica el resultado al solicitante.

**Flujos alternos**
- **A1 · Reasignación de tarea:** el Coordinador reasigna desde su panel; ambos responsables quedan registrados y el nuevo es notificado.
- **A2 · Escalamiento por vencimiento:** las solicitudes, alertas críticas y novedades sin resolver escalan por plazo.

**Excepciones**
- **E1 · Reasignación que violaría la regla del segundo conteo:** se rechaza.
- **E2 · Notificación fuera del ámbito del destinatario:** el sistema no expone información fuera de su ámbito; las notificaciones viven dentro del sistema web, sin aplicación móvil nativa.



---

**ESTADO DEL CAPÍTULO 4**

| | |
|---|---|
| **Completado** | 24 casos de uso con objetivo, actor, precondiciones, postcondiciones, flujo principal, flujos alternos y excepciones; los 14 procesos PN tienen caso de uso |
| **Pendiente** | CU-19 (Cierre de jornada) sin HU ni RF asociados (H-10, DEC-05) · validación contra el proceso AS-IS de la empresa de estudio |
| **Riesgos encontrados** | R-S01 (procesos TO-BE sin contrastar con la operación real) |
| **Dependencias** | Cap. 3 (actores), Caps. 5–8 (requisitos y reglas que cada caso cita), Cap. 9 |


---

# CAPÍTULO 5 — HISTORIAS DE USUARIO NORMALIZADAS

> Reorganización de las **114 historias** del SPEC (Cap. 6) con ID estable por dominio, prioridad MoSCoW, dependencias y criterios Gherkin. **No se perdió ninguna historia** (Anexo A) **ni ningún criterio de aceptación** (515 criterios → 515 escenarios). Las historias conservan su redacción «COMO / QUIERO / PARA» del SPEC.

## 5.1 Cómo leer una historia

| Atributo | Significado |
|---|---|
| **ID** | `HU-<DOM>-nnn` permanente (ver §1.4.3). El ID del SPEC se conserva como *legacy* |
| **Prioridad** | MoSCoW derivada mecánicamente de la prioridad P0–P3 del SPEC (§1.4.4) |
| **Horizonte** | H1 = MVP-Núcleo; H2 = versión 1.1 según §12.3 del SPEC (§1.4.5) |
| **Depende de** | Historias que deben existir u operar antes `[SRS]` |
| **RF / RN / KPI** | Requisitos, reglas e indicadores relacionados (RF y KPI derivados en esta fase `[SRS]`; RN provienen de las etiquetas del SPEC más las de sus RF) |
| **Gherkin** | Un escenario por criterio de aceptación del SPEC; el comentario `# Criterio SPEC (n)` reproduce el texto original |

## 5.2 Distribución


| Módulo | Dominio | HU | Must | Should | Could | Won't | H2 | Rango legacy |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **M-01** Acceso y Autenticación | ACC | 4 | 2 | 2 | 0 | 0 | 0 | HU-001–HU-004 |
| **M-02** Usuarios y Roles | USR | 5 | 2 | 2 | 1 | 0 | 0 | HU-005–HU-009 |
| **M-03** Catálogo de Referencias | CAT | 6 | 2 | 2 | 2 | 0 | 1 | HU-010–HU-015 |
| **M-04** Gestión de Lotes | LOT | 4 | 1 | 2 | 1 | 0 | 2 | HU-016–HU-019 |
| **M-05** Estructura de Bodega | BOD | 5 | 1 | 2 | 2 | 0 | 1 | HU-020–HU-024 |
| **M-06** Identificación QR | QRC | 5 | 2 | 2 | 1 | 0 | 1 | HU-025–HU-029 |
| **M-07** Entradas y Recepción | ENT | 10 | 6 | 3 | 1 | 0 | 0 | HU-030–HU-105 |
| **M-08** Salidas | SAL | 9 | 6 | 3 | 0 | 0 | 0 | HU-038–HU-108 |
| **M-09** Movimientos y Transferencias | MOV | 9 | 5 | 4 | 0 | 0 | 5 | HU-045–HU-111 |
| **M-10** Ajustes de Inventario | AJU | 6 | 4 | 2 | 0 | 0 | 1 | HU-052–HU-057 |
| **M-11** Conteos | CNT | 11 | 1 | 9 | 1 | 0 | 3 | HU-058–HU-112 |
| **M-12** Novedades de Mercancía | NOV | 4 | 0 | 4 | 0 | 0 | 0 | HU-067–HU-070 |
| **M-13** Consulta de Existencia | INV | 6 | 3 | 2 | 1 | 0 | 1 | HU-071–HU-076 |
| **M-14** Kardex y Trazabilidad | KDX | 6 | 3 | 2 | 1 | 0 | 0 | HU-077–HU-110 |
| **M-15** Alertas y Reglas | ALE | 5 | 0 | 4 | 1 | 0 | 1 | HU-082–HU-086 |
| **M-16** Reportes y Exportación Analítica | REP | 4 | 0 | 3 | 1 | 0 | 2 | HU-087–HU-090 |
| **M-17** Dashboard Operativo | DSH | 3 | 0 | 2 | 1 | 0 | 1 | HU-091–HU-093 |
| **M-18** Auditoría y Bitácora | AUD | 4 | 0 | 4 | 0 | 0 | 0 | HU-094–HU-097 |
| **M-19** Parámetros y Configuración | PAR | 3 | 2 | 1 | 0 | 0 | 0 | HU-098–HU-100 |
| **M-20** Notificaciones y Tareas | TAR | 5 | 0 | 4 | 1 | 0 | 1 | HU-101–HU-114 |
| **Total** | | **114** | **40** | **59** | **15** | **0** | **20** | HU-001–HU-114 |


## 5.3 M-01 · Acceso y Autenticación (dominio ACC)

### HU-ACC-001 — Iniciar sesión con credencial individual

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Todos los roles · **Legacy:** HU-001  
**Depende de:** — · **RF:** RF-ACC-001, RF-ACC-002, RF-ACC-003, RF-ACC-004 · **RN:** RN-AUD-001, RN-INT-001 · **KPI:** —  
**Origen (SPEC):** `[PR-05]`

**Historia.** **COMO** usuario del sistema **QUIERO** iniciar sesión con una credencial que solo yo conozco **PARA** que todo lo que registre quede a mi nombre y nadie pueda actuar suplantándome.

```gherkin
@HU-ACC-001 @Must @M-01
Característica: HU-ACC-001 — Iniciar sesión con credencial individual
  # Criterio SPEC (1): El acceso exige identificador y contraseña individuales.
  Escenario: C1 · El acceso exige identificador y contraseña individuales
    Dado un usuario activo con identificador y contraseña propios
    Cuando intenta acceder al sistema sin presentar ambos datos
    Entonces el sistema no abre sesión y solicita las dos credenciales
  # Criterio SPEC (2): No existe cuenta genérica ni compartida.
  Escenario: C2 · No existen cuentas genéricas ni compartidas
    Dado el Administrador que crea o edita una cuenta
    Cuando intenta registrar una cuenta genérica o compartida por varias personas
    Entonces el sistema no ofrece esa posibilidad y cada cuenta queda asociada a una sola persona identificada
  # Criterio SPEC (3): Un acceso exitoso abre sesión y registra el evento en la bitácora.
  Escenario: C3 · El acceso exitoso abre sesión y queda en bitácora
    Dado un usuario activo con credenciales válidas
    Cuando inicia sesión
    Entonces el sistema abre la sesión a su nombre
    Y registra el acceso en la bitácora con fecha, hora y origen
  # Criterio SPEC (4): Un acceso fallido no revela si el error fue en el usuario o en la contraseña.
  Escenario: C4 · El acceso fallido no revela cuál dato fue incorrecto
    Dado un intento de acceso con usuario o contraseña incorrectos
    Cuando el sistema rechaza el acceso
    Entonces el mensaje es el mismo sin indicar si el error fue del usuario o de la contraseña
  # Criterio SPEC (5): Tras cinco intentos fallidos consecutivos la cuenta se bloquea y se notifica al Administrador.
  Escenario: C5 · Cinco intentos fallidos consecutivos bloquean la cuenta
    Dada una cuenta activa con cuatro intentos fallidos consecutivos
    Cuando ocurre el quinto intento fallido consecutivo
    Entonces el sistema bloquea la cuenta
    Y notifica al Administrador
```

### HU-ACC-002 — Mantener la sesión abierta durante la jornada en tablet

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar de Bodega · **Legacy:** HU-002  
**Depende de:** HU-ACC-001 · **RF:** RF-ACC-005 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[DC-05]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** que mi sesión permanezca abierta mientras trabajo en la tablet **PARA** no tener que autenticarme cada vez que registro un movimiento.

```gherkin
@HU-ACC-002 @Must @M-01
Característica: HU-ACC-002 — Mantener la sesión abierta durante la jornada en tablet
  # Criterio SPEC (1): La sesión permanece activa mientras haya actividad.
  Escenario: C1 · La sesión permanece activa mientras hay actividad
    Dado un Auxiliar con sesión abierta en la tablet
    Cuando registra movimientos de forma continua
    Entonces la sesión permanece activa sin pedirle autenticarse de nuevo
  # Criterio SPEC (2): El cierre por inactividad ocurre tras el tiempo configurado en M-19.
  Escenario: C2 · Cierre por inactividad según tiempo configurado
    Dado un tiempo de inactividad configurado en Parámetros y Configuración
    Cuando el usuario no registra actividad durante ese tiempo
    Entonces el sistema cierra la sesión
  # Criterio SPEC (3): Antes de cerrar, el sistema avisa.
  Escenario: C3 · Aviso previo al cierre
    Dada una sesión próxima a cumplir el tiempo de inactividad
    Cuando falta poco para el cierre
    Entonces el sistema avisa al usuario antes de cerrarla
  # Criterio SPEC (4): Al reanudar, el sistema no pierde el registro en curso no confirmado.
  Escenario: C4 · Al reanudar no se pierde el registro en curso
    Dado un registro en curso aún no confirmado
    Cuando el usuario reanuda su trabajo tras un aviso o reconexión
    Entonces el sistema conserva el registro en curso sin pérdida de datos
  # Criterio SPEC (5): El cierre por inactividad queda en la bitácora.
  Escenario: C5 · El cierre por inactividad queda en bitácora
    Dada una sesión cerrada por inactividad
    Cuando el cierre se produce
    Entonces el evento queda registrado en la bitácora
```

### HU-ACC-003 — Cambiar la contraseña propia

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Todos los roles · **Legacy:** HU-003  
**Depende de:** HU-ACC-001 · **RF:** RF-ACC-006 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** usuario **QUIERO** cambiar mi contraseña cuando lo necesite **PARA** mantener el control sobre mi acceso.

```gherkin
@HU-ACC-003 @Should @M-01
Característica: HU-ACC-003 — Cambiar la contraseña propia
  # Criterio SPEC (1): El cambio exige la contraseña actual.
  Escenario: C1 · El cambio exige la contraseña actual
    Dado un usuario autenticado
    Cuando solicita cambiar su contraseña sin ingresar la actual
    Entonces el sistema rechaza el cambio
  # Criterio SPEC (2): La nueva contraseña cumple la política mínima configurada.
  Escenario: C2 · La nueva contraseña cumple la política mínima
    Dada una política mínima de contraseña configurada
    Cuando el usuario propone una contraseña que no la cumple
    Entonces el sistema rechaza el cambio e indica qué requisito falta
  # Criterio SPEC (3): La nueva no puede coincidir con la anterior.
  Escenario: C3 · La nueva contraseña no puede coincidir con la anterior
    Dado un usuario que ingresa correctamente su contraseña actual
    Cuando propone como nueva la misma contraseña actual
    Entonces el sistema rechaza el cambio
  # Criterio SPEC (4): El cambio cierra las demás sesiones activas del usuario.
  Escenario: C4 · El cambio cierra las demás sesiones activas
    Dado un usuario con otras sesiones activas en distintos dispositivos
    Cuando el cambio de contraseña se completa
    Entonces el sistema cierra las demás sesiones activas de ese usuario
  # Criterio SPEC (5): El evento queda en la bitácora sin registrar ningún valor de contraseña.
  Escenario: C5 · El evento queda en bitácora sin valores de contraseña
    Dado un cambio de contraseña completado
    Cuando el sistema registra el evento
    Entonces la bitácora guarda el evento con usuario, fecha y hora
    Y no registra ningún valor de contraseña
```

### HU-ACC-004 — Restablecer el acceso de un usuario bloqueado

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-004  
**Depende de:** HU-ACC-001, HU-USR-001 · **RF:** RF-ACC-007 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Administrador **QUIERO** restablecer el acceso de un usuario bloqueado **PARA** que la operación no se detenga por un olvido.

```gherkin
@HU-ACC-004 @Should @M-01
Característica: HU-ACC-004 — Restablecer el acceso de un usuario bloqueado
  # Criterio SPEC (1): El Administrador desbloquea la cuenta y fuerza el cambio en el próximo acceso.
  Escenario: C1 · El Administrador desbloquea y fuerza el cambio de contraseña
    Dada una cuenta bloqueada por intentos fallidos
    Cuando el Administrador restablece el acceso
    Entonces la cuenta queda desbloqueada
    Y el usuario debe cambiar su contraseña en el siguiente acceso
  # Criterio SPEC (2): El sistema nunca muestra la contraseña anterior.
  Escenario: C2 · El sistema nunca muestra la contraseña anterior
    Dado un restablecimiento de acceso en curso
    Cuando el Administrador consulta cualquier pantalla del proceso
    Entonces el sistema no muestra ni permite recuperar la contraseña anterior
  # Criterio SPEC (3): El restablecimiento queda en la bitácora con quién lo ejecutó.
  Escenario: C3 · El restablecimiento queda en bitácora con su ejecutor
    Dado un restablecimiento completado
    Cuando el sistema registra el evento
    Entonces la bitácora indica quién lo ejecutó, sobre qué cuenta y cuándo
  # Criterio SPEC (4): El usuario afectado es notificado.
  Escenario: C4 · El usuario afectado es notificado
    Dada una cuenta restablecida por el Administrador
    Cuando el restablecimiento se completa
    Entonces el usuario afectado recibe una notificación
```


## 5.4 M-02 · Usuarios y Roles (dominio USR)

### HU-USR-001 — Crear usuarios con uno de los cinco roles oficiales

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-005  
**Depende de:** HU-ACC-001 · **RF:** RF-USR-001, RF-USR-002, RF-USR-003 · **RN:** RN-INT-001, RN-MAE-006 · **KPI:** —  
**Origen (SPEC):** `[DC-04]`

**Historia.** **COMO** Administrador **QUIERO** crear usuarios y asignarles uno de los cinco roles oficiales **PARA** que cada persona acceda solo a lo que su función requiere.

```gherkin
@HU-USR-001 @Must @M-02
Característica: HU-USR-001 — Crear usuarios con uno de los cinco roles oficiales
  # Criterio SPEC (1): El formulario ofrece exclusivamente los cinco roles de `[DC-04]`.
  Escenario: C1 · El formulario ofrece exclusivamente los cinco roles oficiales
    Dado el Administrador creando un usuario
    Cuando despliega la lista de roles
    Entonces solo aparecen Administrador, Jefe de Bodega, Coordinador de Bodega, Auxiliar de Bodega y Auditor
  # Criterio SPEC (2): No existe opción de crear un rol nuevo.
  Escenario: C2 · No existe la opción de crear un rol nuevo
    Dado el Administrador en el módulo de usuarios y roles
    Cuando busca una función para crear un rol adicional
    Entonces el sistema no ofrece esa función
  # Criterio SPEC (3): Un usuario tiene exactamente un rol activo.
  Escenario: C3 · Un usuario tiene exactamente un rol activo
    Dado un usuario en creación o edición
    Cuando el Administrador intenta asignarle más de un rol activo
    Entonces el sistema solo admite un rol activo por usuario
  # Criterio SPEC (4): La creación queda en la bitácora.
  Escenario: C4 · La creación queda en bitácora
    Dado un usuario creado
    Cuando se completa el alta
    Entonces el evento queda en la bitácora con quién lo creó y el rol asignado
  # Criterio SPEC (5): El usuario nuevo debe cambiar su contraseña en el primer acceso.
  Escenario: C5 · El usuario nuevo cambia su contraseña en el primer acceso
    Dado un usuario recién creado
    Cuando accede por primera vez
    Entonces el sistema le exige cambiar su contraseña antes de continuar
```

### HU-USR-002 — Desactivar usuarios sin perder su rastro

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-006  
**Depende de:** HU-USR-001 · **RF:** RF-USR-004, RF-USR-005 · **RN:** RN-MAE-007, RN-MAE-008, RN-MAE-009 · **KPI:** —  
**Origen (SPEC):** `[RN-MAE-007]`

**Historia.** **COMO** Administrador **QUIERO** desactivar a un usuario que ya no trabaja en la bodega **PARA** cerrar su acceso sin perder el rastro de lo que hizo.

```gherkin
@HU-USR-002 @Must @M-02
Característica: HU-USR-002 — Desactivar usuarios sin perder su rastro
  # Criterio SPEC (1): La desactivación cierra su acceso de inmediato.
  Escenario: C1 · La desactivación cierra el acceso de inmediato
    Dado un usuario activo con sesión abierta
    Cuando el Administrador lo desactiva
    Entonces el acceso del usuario se cierra de inmediato
  # Criterio SPEC (2): Los movimientos históricos del usuario se conservan íntegros y siguen mostrando su nombre.
  Escenario: C2 · Los movimientos históricos se conservan íntegros con su nombre
    Dado un usuario con movimientos registrados
    Cuando el Administrador lo desactiva
    Entonces los movimientos históricos del usuario se conservan íntegros
    Y siguen mostrando su nombre
  # Criterio SPEC (3): No existe la opción de eliminar un usuario.
  Escenario: C3 · No existe la opción de eliminar un usuario
    Dado el Administrador en la gestión de usuarios
    Cuando busca una función para eliminar a un usuario
    Entonces el sistema solo ofrece desactivar
  # Criterio SPEC (4): Un usuario desactivado puede reactivarse.
  Escenario: C4 · Un usuario desactivado puede reactivarse
    Dado un usuario desactivado
    Cuando el Administrador lo reactiva
    Entonces el usuario recupera su acceso con su rol
  # Criterio SPEC (5): El evento queda en la bitácora.
  Escenario: C5 · El evento queda en bitácora
    Dada una desactivación o reactivación
    Cuando se completa
    Entonces el evento queda en la bitácora
```

### HU-USR-003 — Cambiar el rol de un usuario

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-007  
**Depende de:** HU-USR-001 · **RF:** RF-USR-006, RF-USR-008 · **RN:** RN-AUD-001, RN-MAE-004 · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Administrador **QUIERO** cambiar el rol de un usuario **PARA** reflejar un cambio de responsabilidades sin crear una cuenta nueva.

```gherkin
@HU-USR-003 @Should @M-02
Característica: HU-USR-003 — Cambiar el rol de un usuario
  # Criterio SPEC (1): El cambio surte efecto en la siguiente sesión del usuario.
  Escenario: C1 · El cambio surte efecto en la siguiente sesión
    Dado un usuario con sesión abierta cuyo rol cambia
    Cuando el usuario inicia su siguiente sesión
    Entonces opera con el nuevo rol
  # Criterio SPEC (2): Los movimientos anteriores conservan el rol vigente al momento en que ocurrieron.
  Escenario: C2 · Los movimientos anteriores conservan el rol vigente en su momento
    Dado un usuario con movimientos anteriores al cambio de rol
    Cuando se consultan esos movimientos
    Entonces cada movimiento muestra el rol que el usuario tenía cuando ocurrió
  # Criterio SPEC (3): El cambio queda en la bitácora con rol anterior y nuevo.
  Escenario: C3 · El cambio queda en bitácora con rol anterior y nuevo
    Dado un cambio de rol completado
    Cuando el sistema registra el evento
    Entonces la bitácora guarda el rol anterior y el rol nuevo
  # Criterio SPEC (4): El sistema impide dejar la bodega sin ningún Jefe activo.
  Escenario: C4 · No se deja la bodega sin Jefe activo
    Dada una bodega con un único Jefe de Bodega activo
    Cuando el Administrador intenta cambiarle el rol
    Entonces el sistema rechaza el cambio para no dejar la bodega sin Jefe
```

### HU-USR-004 — Asignar bodega y zona a cada usuario

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-008  
**Depende de:** HU-USR-001, HU-BOD-001 · **RF:** RF-USR-007 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Administrador **QUIERO** asignar a cada usuario su bodega y su zona **PARA** que solo vea y opere sobre el ámbito que le corresponde.

```gherkin
@HU-USR-004 @Should @M-02
Característica: HU-USR-004 — Asignar bodega y zona a cada usuario
  # Criterio SPEC (1): Un Coordinador puede tener una o más zonas asignadas.
  Escenario: C1 · Un Coordinador puede tener una o más zonas
    Dado un usuario con rol Coordinador
    Cuando el Administrador le asigna una o varias zonas
    Entonces el sistema registra todas las zonas asignadas
  # Criterio SPEC (2): Un Auxiliar opera dentro de las zonas de su Coordinador.
  Escenario: C2 · El Auxiliar opera dentro de las zonas de su Coordinador
    Dado un Auxiliar asociado a un Coordinador
    Cuando consulta o recibe tareas
    Entonces solo opera dentro de las zonas de su Coordinador
  # Criterio SPEC (3): Jefe, Administrador y Auditor no tienen restricción de ámbito de consulta.
  Escenario: C3 · Jefe, Administrador y Auditor sin restricción de ámbito de consulta
    Dado un usuario con rol Jefe, Administrador o Auditor
    Cuando consulta información de cualquier zona
    Entonces el sistema no restringe su ámbito de consulta
  # Criterio SPEC (4): La consulta y las tareas se filtran automáticamente por ámbito.
  Escenario: C4 · Consultas y tareas se filtran por ámbito
    Dado un usuario con ámbito de bodega y zona asignado
    Cuando consulta información o revisa sus tareas
    Entonces el sistema filtra automáticamente los resultados por su ámbito
```

### HU-USR-005 — Impedir quedarse sin administradores

**Prioridad:** Could (P2) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-009  
**Depende de:** HU-USR-001 · **RF:** RF-USR-006 · **RN:** RN-MAE-004 · **KPI:** —  
**Origen (SPEC):** `[RN-MAE-004]`

**Historia.** **COMO** Administrador **QUIERO** que el sistema me impida quedarme sin administradores **PARA** no perder el control del sistema por error.

```gherkin
@HU-USR-005 @Could @M-02
Característica: HU-USR-005 — Impedir quedarse sin administradores
  # Criterio SPEC (1): El sistema rechaza desactivar al último Administrador activo.
  Escenario: C1 · Se rechaza desactivar al último Administrador activo
    Dado un único Administrador activo
    Cuando se intenta desactivarlo
    Entonces el sistema rechaza la desactivación
  # Criterio SPEC (2): El sistema rechaza cambiarle el rol al último Administrador activo.
  Escenario: C2 · Se rechaza cambiar el rol al último Administrador activo
    Dado un único Administrador activo
    Cuando se intenta cambiarle el rol
    Entonces el sistema rechaza el cambio
  # Criterio SPEC (3): El mensaje explica el motivo del rechazo.
  Escenario: C3 · El mensaje explica el motivo del rechazo
    Dado un rechazo por ser el último Administrador activo
    Cuando el sistema informa el resultado
    Entonces el mensaje explica claramente el motivo del rechazo
```


## 5.5 M-03 · Catálogo de Referencias (dominio CAT)

### HU-CAT-001 — Crear una referencia con tallas y colores

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Administrador / Jefe · **Legacy:** HU-010  
**Depende de:** HU-USR-001 · **RF:** RF-CAT-001, RF-CAT-002, RF-CAT-003, RF-CAT-004 · **RN:** RN-MAE-001 · **KPI:** —  
**Origen (SPEC):** `[NUEVO]` `[D-01]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** crear una referencia con sus tallas y colores **PARA** que la mercancía textil se registre con las dimensiones reales del negocio y no con campos improvisados.

```gherkin
@HU-CAT-001 @Must @M-03
Característica: HU-CAT-001 — Crear una referencia con tallas y colores
  # Criterio SPEC (1): La referencia tiene código único `[RN-MAE-001]`.
  Escenario: C1 · La referencia tiene código único
    Dado el Jefe de Bodega creando una referencia con un código no utilizado
    Cuando guarda la referencia
    Entonces la referencia queda creada con ese código único
  # Criterio SPEC (2): Se le asignan uno o más valores de talla y de color.
  Escenario: C2 · Se asignan valores de talla y de color
    Dada una referencia en creación
    Cuando el Jefe le asigna uno o más valores de talla y de color
    Entonces la referencia queda asociada a esos conjuntos de tallas y colores
  # Criterio SPEC (3): El sistema genera automáticamente los SKU resultantes de la combinación.
  Escenario: C3 · El sistema genera los SKU de la combinación
    Dada una referencia con tallas y colores asignados
    Cuando se guarda
    Entonces el sistema genera automáticamente los SKU de cada combinación referencia, talla y color
  # Criterio SPEC (4): La referencia queda activa al crearse.
  Escenario: C4 · La referencia queda activa al crearse
    Dada una referencia recién guardada
    Cuando se consulta su estado
    Entonces figura como activa
  # Criterio SPEC (5): Si el código ya existe, el sistema rechaza y lo informa.
  Escenario: C5 · Un código existente se rechaza
    Dada una referencia ya existente con cierto código
    Cuando se intenta crear otra con el mismo código
    Entonces el sistema rechaza la creación e informa que el código ya existe
```

### HU-CAT-002 — Definir la unidad de medida de cada referencia

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Administrador / Jefe · **Legacy:** HU-011  
**Depende de:** HU-CAT-001 · **RF:** RF-CAT-005 · **RN:** RN-INT-007, RN-MAE-002 · **KPI:** —  
**Origen (SPEC):** `[RN-MAE-002]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** definir la unidad de medida de cada referencia **PARA** que la mercancía se cuente como realmente se maneja: unidades, metros, rollos o kilogramos.

```gherkin
@HU-CAT-002 @Must @M-03
Característica: HU-CAT-002 — Definir la unidad de medida de cada referencia
  # Criterio SPEC (1): La unidad se selecciona de una lista configurada.
  Escenario: C1 · La unidad se selecciona de una lista configurada
    Dada una referencia en creación o edición
    Cuando el Jefe elige su unidad de medida
    Entonces solo puede seleccionarla de la lista configurada
  # Criterio SPEC (2): La unidad no puede cambiarse si la referencia ya tiene movimientos `[RN-MAE-002]`.
  Escenario: C2 · La unidad no cambia si hay movimientos
    Dada una referencia con movimientos registrados
    Cuando se intenta cambiar su unidad de medida
    Entonces el sistema rechaza el cambio
  # Criterio SPEC (3): Todas las cantidades de esa referencia se expresan en su unidad.
  Escenario: C3 · Toda cantidad se expresa en la unidad de la referencia
    Dada una referencia con su unidad definida
    Cuando se registra cualquier cantidad de esa referencia
    Entonces la cantidad se expresa en esa unidad de medida
  # Criterio SPEC (4): El intento de cambio con movimientos existentes se rechaza con explicación.
  Escenario: C4 · El rechazo del cambio explica el motivo
    Dado un intento de cambio de unidad con movimientos existentes
    Cuando el sistema lo rechaza
    Entonces explica que existen movimientos que lo impiden
```

### HU-CAT-003 — Desactivar una referencia descontinuada

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Administrador / Jefe · **Legacy:** HU-012  
**Depende de:** HU-CAT-001 · **RF:** RF-CAT-006 · **RN:** RN-MAE-003, RN-MAE-007 · **KPI:** —  
**Origen (SPEC):** `[RN-MAE-003]` `[RN-MAE-007]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** desactivar una referencia descontinuada **PARA** que no se use en nuevas operaciones sin perder su historial.

```gherkin
@HU-CAT-003 @Should @M-03
Característica: HU-CAT-003 — Desactivar una referencia descontinuada
  # Criterio SPEC (1): No existe la opción de eliminar una referencia.
  Escenario: C1 · No existe la opción de eliminar una referencia
    Dado el Jefe en la gestión del catálogo
    Cuando busca una función para eliminar una referencia
    Entonces el sistema solo ofrece desactivarla
  # Criterio SPEC (2): El sistema rechaza desactivar una referencia con existencia distinta de cero `[RN-MAE-003]`.
  Escenario: C2 · No se desactiva con existencia distinta de cero
    Dada una referencia con existencia distinta de cero
    Cuando se intenta desactivar
    Entonces el sistema rechaza la desactivación
  # Criterio SPEC (3): Una referencia desactivada no aparece en la creación de documentos ni de movimientos.
  Escenario: C3 · La referencia desactivada no aparece en operaciones nuevas
    Dada una referencia desactivada
    Cuando se crea un documento o un movimiento
    Entonces la referencia no aparece entre las opciones
  # Criterio SPEC (4): Su kardex sigue siendo consultable.
  Escenario: C4 · El kardex de la referencia desactivada sigue consultable
    Dada una referencia desactivada con historial
    Cuando se consulta su kardex
    Entonces el kardex se muestra completo
  # Criterio SPEC (5): Puede reactivarse.
  Escenario: C5 · La referencia puede reactivarse
    Dada una referencia desactivada
    Cuando el Jefe la reactiva
    Entonces vuelve a estar disponible para operaciones nuevas
```

### HU-CAT-004 — Definir existencia mínima y máxima por SKU

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Administrador / Jefe · **Legacy:** HU-013  
**Depende de:** HU-CAT-001 · **RF:** RF-CAT-007, RF-CAT-008 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[MON §3, §7.1]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** definir la existencia mínima y máxima de cada SKU **PARA** que el sistema me avise antes de quedarme sin material o de acumular de más.

```gherkin
@HU-CAT-004 @Should @M-03
Característica: HU-CAT-004 — Definir existencia mínima y máxima por SKU
  # Criterio SPEC (1): Los umbrales se definen por SKU.
  Escenario: C1 · Los umbrales se definen por SKU
    Dado un SKU existente
    Cuando el Jefe define su existencia mínima y máxima
    Entonces los umbrales quedan asociados a ese SKU
  # Criterio SPEC (2): El mínimo no puede ser mayor que el máximo.
  Escenario: C2 · El mínimo no puede superar al máximo
    Dado un SKU con umbrales en edición
    Cuando el mínimo ingresado es mayor que el máximo
    Entonces el sistema rechaza los valores
  # Criterio SPEC (3): Al cruzar un umbral, el sistema genera la alerta correspondiente (M-15).
  Escenario: C3 · Al cruzar un umbral se genera la alerta correspondiente
    Dado un SKU con umbrales configurados
    Cuando su existencia cruza el mínimo o el máximo
    Entonces el sistema genera la alerta correspondiente en Alertas y Reglas
  # Criterio SPEC (4): Un SKU sin umbrales configurados no genera esas alertas y aparece en un listado de pendientes de configurar.
  Escenario: C4 · Un SKU sin umbrales aparece como pendiente de configurar
    Dado un SKU sin umbrales configurados
    Cuando se revisa el listado de pendientes
    Entonces el SKU aparece como pendiente de configurar
    Y no genera alertas de mínimo ni de máximo
```

### HU-CAT-005 — Cargar el catálogo inicial de forma masiva

**Prioridad:** Could (P2) · **Horizonte:** H2 · **Actor (SPEC):** Administrador · **Legacy:** HU-014  
**Depende de:** HU-CAT-001 · **RF:** RF-CAT-009 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Administrador **QUIERO** cargar el catálogo inicial de forma masiva **PARA** no tener que crear cientos de referencias una por una al arrancar.

```gherkin
@HU-CAT-005 @Could @M-03
Característica: HU-CAT-005 — Cargar el catálogo inicial de forma masiva
  # Criterio SPEC (1): El sistema acepta un archivo tabular con la estructura definida.
  Escenario: C1 · El sistema acepta un archivo tabular con estructura definida
    Dado el Administrador con un archivo tabular con la estructura definida
    Cuando lo carga en el sistema
    Entonces el sistema acepta el archivo para su procesamiento
  # Criterio SPEC (2): Valida antes de cargar y reporta los errores por línea.
  Escenario: C2 · Se valida antes de cargar y se reportan errores por línea
    Dado un archivo con líneas válidas e inválidas
    Cuando el sistema lo valida antes de cargar
    Entonces reporta los errores indicando la línea de cada uno
  # Criterio SPEC (3): No carga parcialmente: o carga todo lo válido y reporta lo rechazado, o no carga nada, según la opción elegida.
  Escenario: C3 · Carga total de lo válido o ninguna, según la opción elegida
    Dado un archivo con errores y la opción de carga elegida por el Administrador
    Cuando confirma la carga
    Entonces el sistema carga todo lo válido y reporta lo rechazado, o no carga nada, según la opción elegida
  # Criterio SPEC (4): La carga queda en la bitácora con el número de registros procesados.
  Escenario: C4 · La carga queda en bitácora con el número de registros
    Dada una carga masiva completada
    Cuando el sistema registra el evento
    Entonces la bitácora guarda el número de registros procesados
```

### HU-CAT-006 — Organizar las referencias por categoría

**Prioridad:** Could (P2) · **Horizonte:** H1 · **Actor (SPEC):** Administrador / Jefe · **Legacy:** HU-015  
**Depende de:** HU-CAT-001 · **RF:** RF-CAT-010 · **RN:** RN-MAE-007 · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** organizar las referencias por categoría **PARA** poder asignarlas a zonas y agrupar los reportes.

```gherkin
@HU-CAT-006 @Could @M-03
Característica: HU-CAT-006 — Organizar las referencias por categoría
  # Criterio SPEC (1): Una referencia pertenece a una sola categoría.
  Escenario: C1 · Una referencia pertenece a una sola categoría
    Dada una referencia en creación o edición
    Cuando se le asigna una categoría
    Entonces solo puede pertenecer a una categoría
  # Criterio SPEC (2): La categoría puede asociarse a una zona preferente para la asignación automática de ubicación.
  Escenario: C2 · La categoría puede asociarse a una zona preferente
    Dada una categoría existente
    Cuando el Administrador la asocia a una zona preferente
    Entonces la asignación automática de ubicación puede usar esa zona
  # Criterio SPEC (3): Los reportes permiten agrupar por categoría.
  Escenario: C3 · Los reportes agrupan por categoría
    Dado un reporte con datos de varias categorías
    Cuando se solicita agruparlo por categoría
    Entonces el reporte presenta los datos agrupados por categoría
  # Criterio SPEC (4): Una categoría en uso no se elimina, se desactiva `[RN-MAE-007]`.
  Escenario: C4 · Una categoría en uso no se elimina, se desactiva
    Dada una categoría con referencias asociadas
    Cuando el Administrador intenta eliminarla
    Entonces el sistema solo permite desactivarla
```


## 5.6 M-04 · Gestión de Lotes (dominio LOT)

### HU-LOT-001 — Asociar toda mercancía a un lote

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador · **Legacy:** HU-016  
**Depende de:** HU-CAT-001 · **RF:** RF-LOT-001, RF-LOT-002, RF-LOT-003 · **RN:** RN-LOT-001, RN-MAE-006 · **KPI:** —  
**Origen (SPEC):** `[MON §7.1]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** que la mercancía que ingresa quede asociada a un lote **PARA** poder rastrear después de dónde vino cada unidad.

```gherkin
@HU-LOT-001 @Must @M-04
Característica: HU-LOT-001 — Asociar toda mercancía a un lote
  # Criterio SPEC (1): Al confirmar una entrada se crea o se selecciona un lote.
  Escenario: C1 · Al confirmar una entrada se crea o selecciona un lote
    Dada una entrada que se confirma
    Cuando el Coordinador completa la confirmación
    Entonces el sistema crea un lote nuevo o asocia uno existente
  # Criterio SPEC (2): El lote registra origen y fecha de ingreso.
  Escenario: C2 · El lote registra origen y fecha de ingreso
    Dado un lote asociado a una entrada
    Cuando se consulta el lote
    Entonces muestra su origen y su fecha de ingreso
  # Criterio SPEC (3): El código de lote es único dentro de su SKU `[RN-MAE-006]`.
  Escenario: C3 · El código de lote es único dentro de su SKU
    Dado un SKU con un lote de cierto código
    Cuando se intenta crear otro lote del mismo SKU con el mismo código
    Entonces el sistema lo rechaza
  # Criterio SPEC (4): Ninguna existencia queda sin lote asociado.
  Escenario: C4 · Ninguna existencia queda sin lote
    Dado cualquier ingreso de mercancía al inventario
    Cuando se confirma
    Entonces la existencia queda asociada a un lote
  # Criterio SPEC (5): El lote aparece en toda consulta y en el kardex.
  Escenario: C5 · El lote aparece en toda consulta y en el kardex
    Dada una unidad de inventario con lote
    Cuando se consulta su existencia o su kardex
    Entonces el lote se muestra en el resultado
```

### HU-LOT-002 — Consultar la distribución de un lote

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe de Bodega · **Legacy:** HU-017  
**Depende de:** HU-LOT-001, HU-INV-001 · **RF:** RF-LOT-004 · **RN:** RN-LOT-002 · **KPI:** —  
**Origen (SPEC):** `[MON §7.1]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** consultar dónde está distribuida toda la existencia de un lote **PARA** poder actuar sobre él completo si aparece un problema de calidad.

```gherkin
@HU-LOT-002 @Should @M-04
Característica: HU-LOT-002 — Consultar la distribución de un lote
  # Criterio SPEC (1): La consulta devuelve todas las ubicaciones donde hay existencia del lote, con su cantidad.
  Escenario: C1 · La consulta devuelve todas las ubicaciones con existencia del lote
    Dado un lote con existencia repartida en varias ubicaciones
    Cuando el Jefe consulta el lote
    Entonces el sistema lista cada ubicación con su cantidad
  # Criterio SPEC (2): Muestra el total del lote y su estado.
  Escenario: C2 · Muestra el total del lote y su estado
    Dado un lote consultado
    Cuando se presenta el resultado
    Entonces muestra el total del lote y su estado
  # Criterio SPEC (3): Permite abrir el kardex completo del lote.
  Escenario: C3 · Permite abrir el kardex completo del lote
    Dado un lote consultado
    Cuando el Jefe elige ver su kardex
    Entonces el sistema abre el kardex completo del lote
  # Criterio SPEC (4): Permite inmovilizarlo desde la misma consulta.
  Escenario: C4 · Permite inmovilizar el lote desde la consulta
    Dado un lote consultado por el Jefe
    Cuando elige inmovilizarlo desde la consulta
    Entonces el sistema inicia la inmovilización del lote
```

### HU-LOT-003 — Inmovilizar un lote completo

**Prioridad:** Should (P1) · **Horizonte:** H2 · **Actor (SPEC):** Jefe de Bodega · **Legacy:** HU-018  
**Depende de:** HU-LOT-001, HU-LOT-002 · **RF:** RF-LOT-005 · **RN:** RN-EXI-006, RN-LOT-003, RN-LOT-004 · **KPI:** —  
**Origen (SPEC):** `[RN-EXI-006]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** inmovilizar un lote completo **PARA** impedir que salga mercancía sospechosa mientras se verifica.

```gherkin
@HU-LOT-003 @Should @M-04
Característica: HU-LOT-003 — Inmovilizar un lote completo
  # Criterio SPEC (1): La inmovilización afecta toda la existencia del lote, en todas sus ubicaciones.
  Escenario: C1 · La inmovilización afecta toda la existencia del lote en todas sus ubicaciones
    Dado un lote con existencia en varias ubicaciones
    Cuando el Jefe lo inmoviliza
    Entonces toda su existencia queda inmovilizada en todas sus ubicaciones
  # Criterio SPEC (2): La existencia inmovilizada deja de contar como disponible.
  Escenario: C2 · La existencia inmovilizada deja de contar como disponible
    Dado un lote inmovilizado
    Cuando se consulta el disponible
    Entonces la existencia inmovilizada no cuenta como disponible
  # Criterio SPEC (3): Todo intento de salida, transferencia o movimiento sobre ella se rechaza `[RN-EXI-006]`.
  Escenario: C3 · Salidas, transferencias y movimientos se rechazan
    Dado un lote inmovilizado
    Cuando se intenta una salida, transferencia o movimiento sobre su existencia
    Entonces el sistema rechaza la operación
  # Criterio SPEC (4): Requiere motivo tipificado.
  Escenario: C4 · La inmovilización requiere motivo tipificado
    Dado el Jefe inmovilizando un lote
    Cuando intenta confirmar sin seleccionar un motivo tipificado
    Entonces el sistema no permite la inmovilización
  # Criterio SPEC (5): Solo Jefe o Administrador pueden liberarlo.
  Escenario: C5 · Solo Jefe o Administrador pueden liberar el lote
    Dado un lote inmovilizado
    Cuando un usuario con otro rol intenta liberarlo
    Entonces el sistema lo impide
    Y solo el Jefe o el Administrador pueden liberarlo
  # Criterio SPEC (6): Queda en la bitácora.
  Escenario: C6 · La inmovilización y la liberación quedan en bitácora
    Dada una inmovilización o liberación de lote
    Cuando se completa
    Entonces el evento queda en la bitácora
```

### HU-LOT-004 — Listar los lotes por antigüedad

**Prioridad:** Could (P2) · **Horizonte:** H2 · **Actor (SPEC):** Jefe de Bodega · **Legacy:** HU-019  
**Depende de:** HU-LOT-001 · **RF:** RF-LOT-006 · **RN:** RN-LOT-005 · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** ver los lotes ordenados por antigüedad **PARA** priorizar la salida de los más viejos y evitar que se deterioren en bodega.

```gherkin
@HU-LOT-004 @Could @M-04
Característica: HU-LOT-004 — Listar los lotes por antigüedad
  # Criterio SPEC (1): El listado ordena por fecha de ingreso.
  Escenario: C1 · El listado se ordena por fecha de ingreso
    Dados varios lotes con distintas fechas de ingreso
    Cuando el Jefe abre el listado
    Entonces los lotes se ordenan por fecha de ingreso
  # Criterio SPEC (2): Muestra los días en bodega.
  Escenario: C2 · Muestra los días en bodega
    Dado un lote listado
    Cuando se presenta el listado
    Entonces cada lote muestra sus días en bodega
  # Criterio SPEC (3): Permite filtrar por referencia y por categoría.
  Escenario: C3 · Permite filtrar por referencia y categoría
    Dado el listado de lotes por antigüedad
    Cuando el Jefe filtra por referencia o categoría
    Entonces el sistema muestra solo los lotes que cumplen el filtro
  # Criterio SPEC (4): Los lotes por encima del umbral de antigüedad configurado se destacan.
  Escenario: C4 · Se destacan los lotes por encima del umbral de antigüedad
    Dado un umbral de antigüedad configurado
    Cuando un lote lo supera
    Entonces el listado lo destaca
```


## 5.7 M-05 · Estructura de Bodega (dominio BOD)

### HU-BOD-001 — Definir zonas y ubicaciones de la bodega

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-020  
**Depende de:** HU-USR-001 · **RF:** RF-BOD-001, RF-BOD-002, RF-BOD-003, RF-BOD-004 · **RN:** RN-EXI-002, RN-MAE-006 · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Administrador **QUIERO** definir las zonas y ubicaciones de la bodega **PARA** que el sistema pueda decir dónde está físicamente cada cosa.

```gherkin
@HU-BOD-001 @Must @M-05
Característica: HU-BOD-001 — Definir zonas y ubicaciones de la bodega
  # Criterio SPEC (1): Se crean zonas dentro de una bodega, con tipo asignado.
  Escenario: C1 · Se crean zonas con tipo asignado
    Dado el Administrador definiendo la estructura de una bodega
    Cuando crea una zona y le asigna un tipo
    Entonces la zona queda creada dentro de la bodega con su tipo
  # Criterio SPEC (2): Se crean ubicaciones dentro de una zona.
  Escenario: C2 · Se crean ubicaciones dentro de una zona
    Dada una zona existente
    Cuando el Administrador crea una ubicación
    Entonces la ubicación queda asociada a esa zona
  # Criterio SPEC (3): El código de ubicación es único en la bodega `[RN-MAE-006]`.
  Escenario: C3 · El código de ubicación es único en la bodega
    Dada una ubicación con cierto código en una bodega
    Cuando se intenta crear otra con el mismo código en esa bodega
    Entonces el sistema lo rechaza
  # Criterio SPEC (4): Debe existir al menos una zona de recepción por bodega `[RN-EXI-002]`.
  Escenario: C4 · Debe existir al menos una zona de recepción por bodega
    Dada una bodega sin zona de recepción
    Cuando se intenta dejar la estructura de la bodega como completa para operar
    Entonces el sistema exige al menos una zona de recepción
  # Criterio SPEC (5): Cada ubicación creada obtiene su identificador QR (M-06).
  Escenario: C5 · Cada ubicación creada obtiene su identificador QR
    Dada una ubicación recién creada
    Cuando se guarda
    Entonces el sistema le asigna su identificador QR
```

### HU-BOD-002 — Definir la capacidad de cada ubicación

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-021  
**Depende de:** HU-BOD-001 · **RF:** RF-BOD-005 · **RN:** RN-MOV-002 · **KPI:** KPI-18  
**Origen (SPEC):** `[RN-MOV-002]`

**Historia.** **COMO** Administrador **QUIERO** definir la capacidad de cada ubicación **PARA** que el sistema no proponga guardar mercancía donde no cabe.

```gherkin
@HU-BOD-002 @Should @M-05
Característica: HU-BOD-002 — Definir la capacidad de cada ubicación
  # Criterio SPEC (1): La capacidad se expresa en una unidad configurada.
  Escenario: C1 · La capacidad se expresa en una unidad configurada
    Dada una ubicación en configuración
    Cuando el Administrador define su capacidad
    Entonces la capacidad se expresa en una unidad configurada
  # Criterio SPEC (2): El sistema no propone como destino una ubicación sin capacidad suficiente.
  Escenario: C2 · No se propone una ubicación sin capacidad suficiente
    Dada una ubicación cuya capacidad libre es insuficiente
    Cuando el sistema propone una ubicación destino
    Entonces no propone esa ubicación
  # Criterio SPEC (3): Si la ocupación supera la capacidad, se genera alerta `[RN-MOV-002]`.
  Escenario: C3 · La sobreocupación genera alerta
    Dada una ubicación con capacidad definida
    Cuando su ocupación supera la capacidad
    Entonces el sistema genera una alerta de sobreocupación
  # Criterio SPEC (4): Una ubicación sin capacidad definida se trata como de capacidad ilimitada y se lista como pendiente de configurar.
  Escenario: C4 · Sin capacidad definida se trata como ilimitada y se lista como pendiente
    Dada una ubicación sin capacidad definida
    Cuando el sistema evalúa su capacidad
    Entonces la trata como de capacidad ilimitada
    Y la incluye en el listado de pendientes de configurar
```

### HU-BOD-003 — Desactivar una ubicación fuera de servicio

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-022  
**Depende de:** HU-BOD-001 · **RF:** RF-BOD-006 · **RN:** RN-MAE-005, RN-MAE-007 · **KPI:** —  
**Origen (SPEC):** `[RN-MAE-005]` `[RN-MAE-007]`

**Historia.** **COMO** Administrador **QUIERO** desactivar una ubicación fuera de servicio **PARA** que no se asigne mercancía a un lugar inutilizable.

```gherkin
@HU-BOD-003 @Should @M-05
Característica: HU-BOD-003 — Desactivar una ubicación fuera de servicio
  # Criterio SPEC (1): No existe la opción de eliminar una ubicación.
  Escenario: C1 · No existe la opción de eliminar una ubicación
    Dado el Administrador en la gestión de ubicaciones
    Cuando busca una función para eliminar una ubicación
    Entonces el sistema solo ofrece desactivarla
  # Criterio SPEC (2): El sistema rechaza desactivar una ubicación con existencia `[RN-MAE-005]`.
  Escenario: C2 · No se desactiva una ubicación con existencia
    Dada una ubicación con existencia
    Cuando se intenta desactivar
    Entonces el sistema rechaza la desactivación
  # Criterio SPEC (3): Una ubicación desactivada no se propone ni se acepta como destino.
  Escenario: C3 · Una ubicación desactivada no se propone ni se acepta como destino
    Dada una ubicación desactivada
    Cuando se propone o se escanea como destino
    Entonces el sistema no la propone ni la acepta
  # Criterio SPEC (4): Su historial sigue consultable.
  Escenario: C4 · El historial de la ubicación desactivada sigue consultable
    Dada una ubicación desactivada con historial
    Cuando se consulta su historial
    Entonces el historial se muestra completo
  # Criterio SPEC (5): Puede reactivarse.
  Escenario: C5 · La ubicación puede reactivarse
    Dada una ubicación desactivada
    Cuando el Administrador la reactiva
    Entonces vuelve a estar disponible como destino
```

### HU-BOD-004 — Asignar un Coordinador responsable a cada zona

**Prioridad:** Could (P2) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-023  
**Depende de:** HU-BOD-001, HU-USR-001 · **RF:** RF-BOD-007 · **RN:** RN-ALE-005 · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Administrador **QUIERO** asignar un Coordinador responsable a cada zona **PARA** que las alertas y las tareas lleguen a la persona correcta.

```gherkin
@HU-BOD-004 @Could @M-05
Característica: HU-BOD-004 — Asignar un Coordinador responsable a cada zona
  # Criterio SPEC (1): Una zona tiene un Coordinador responsable.
  Escenario: C1 · Una zona tiene un Coordinador responsable
    Dada una zona sin responsable
    Cuando el Administrador le asigna un Coordinador
    Entonces la zona queda con ese Coordinador como responsable
  # Criterio SPEC (2): Las alertas de la zona se dirigen a él.
  Escenario: C2 · Las alertas de la zona se dirigen al Coordinador
    Dada una zona con Coordinador responsable
    Cuando se genera una alerta de esa zona
    Entonces la alerta se dirige a ese Coordinador
  # Criterio SPEC (3): El dashboard del Coordinador se filtra a sus zonas.
  Escenario: C3 · El dashboard del Coordinador se filtra a sus zonas
    Dado un Coordinador con zonas asignadas
    Cuando abre su dashboard
    Entonces solo ve información de sus zonas
  # Criterio SPEC (4): Una zona sin responsable escala al Jefe.
  Escenario: C4 · Una zona sin responsable escala al Jefe
    Dada una zona sin Coordinador responsable
    Cuando se genera una alerta de esa zona
    Entonces la alerta escala al Jefe de Bodega
```

### HU-BOD-005 — Configurar la propuesta automática de ubicación

**Prioridad:** Could (P2) · **Horizonte:** H2 · **Actor (SPEC):** Administrador · **Legacy:** HU-024  
**Depende de:** HU-CAT-006, HU-BOD-001, HU-BOD-002 · **RF:** RF-BOD-008 · **RN:** RN-MOV-001, RN-MOV-003 · **KPI:** KPI-10  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Administrador **QUIERO** configurar cómo el sistema propone la ubicación de la mercancía que ingresa **PARA** que el Auxiliar no tenga que decidirlo cada vez.

```gherkin
@HU-BOD-005 @Could @M-05
Característica: HU-BOD-005 — Configurar la propuesta automática de ubicación
  # Criterio SPEC (1): Se configuran criterios de asignación: zona por categoría, agrupación por referencia, ubicación con mayor capacidad libre.
  Escenario: C1 · Se configuran criterios de asignación
    Dado el Administrador configurando la asignación de ubicación
    Cuando define criterios como zona por categoría, agrupación por referencia o mayor capacidad libre
    Entonces el sistema guarda los criterios configurados
  # Criterio SPEC (2): El sistema aplica los criterios en el orden configurado.
  Escenario: C2 · Los criterios se aplican en el orden configurado
    Dados varios criterios configurados en cierto orden
    Cuando el sistema propone una ubicación
    Entonces aplica los criterios siguiendo ese orden
  # Criterio SPEC (3): Si ninguno aplica, propone la zona de recepción.
  Escenario: C3 · Si ningún criterio aplica se propone la zona de recepción
    Dada una mercancía para la que ningún criterio produce una ubicación
    Cuando el sistema propone destino
    Entonces propone la zona de recepción
  # Criterio SPEC (4): La propuesta siempre es sugerencia: el Coordinador puede reasignar `[RN-MOV-003]`.
  Escenario: C4 · La propuesta es una sugerencia que el Coordinador puede reasignar
    Dada una ubicación propuesta por el sistema
    Cuando el Coordinador decide otra ubicación
    Entonces el sistema permite reasignarla porque la propuesta no es una imposición
```


## 5.8 M-06 · Identificación QR (dominio QRC)

### HU-QRC-001 — Generar e imprimir códigos QR para la mercancía

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador · **Legacy:** HU-025  
**Depende de:** HU-CAT-001, HU-LOT-001 · **RF:** RF-QRC-001, RF-QRC-002, RF-QRC-005 · **RN:** RN-IDE-001, RN-IDE-002 · **KPI:** —  
**Origen (SPEC):** `[DC-08]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** generar e imprimir un código QR para la mercancía que ingresa **PARA** que después se pueda escanear en lugar de escribir a mano.

```gherkin
@HU-QRC-001 @Must @M-06
Característica: HU-QRC-001 — Generar e imprimir códigos QR para la mercancía
  # Criterio SPEC (1): El sistema genera un identificador único por SKU + Lote `[RN-IDE-002]` `[DF5-01]`.
  Escenario: C1 · Un identificador único por SKU + Lote
    Dado un SKU + Lote sin identificador
    Cuando el Coordinador genera su código QR
    Entonces el sistema le asigna un identificador único, que no depende de la ubicación
  # Criterio SPEC (2): Permite impresión individual y por lote de impresión.
  Escenario: C2 · Impresión individual y por lote de impresión
    Dados varios identificadores generados
    Cuando el Coordinador imprime
    Entonces puede imprimir un identificador individual o un lote de impresión
  # Criterio SPEC (3): El identificador impreso incluye información legible de respaldo: referencia, talla, color y lote.
  Escenario: C3 · El identificador impreso incluye información legible de respaldo
    Dado un identificador QR impreso
    Cuando se lee la etiqueta
    Entonces incluye referencia, talla, color y lote de forma legible
  # Criterio SPEC (4): El identificador queda en estado activo.
  Escenario: C4 · El identificador queda activo
    Dado un identificador recién generado
    Cuando se consulta su estado
    Entonces figura como activo
  # Criterio SPEC (5): Ningún identificador se repite jamás, ni tras su anulación `[RN-IDE-002]`.
  Escenario: C5 · Ningún identificador se repite jamás, ni tras su anulación
    Dado un identificador anulado o reemplazado
    Cuando el sistema genera nuevos identificadores
    Entonces ninguno reutiliza un identificador ya emitido
```

### HU-QRC-002 — Escanear el código QR en lugar de escribir códigos

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-026  
**Depende de:** HU-QRC-001 · **RF:** RF-QRC-003, RF-QRC-009 · **RN:** RN-IDE-001 · **KPI:** KPI-07  
**Origen (SPEC):** `[DC-08]` `[MON §7.2]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** escanear el código QR en lugar de escribir códigos **PARA** no equivocarme y terminar más rápido.

```gherkin
@HU-QRC-002 @Must @M-06
Característica: HU-QRC-002 — Escanear el código QR en lugar de escribir códigos
  # Criterio SPEC (1): El escaneo se hace desde la tablet `[DC-05]`.
  Escenario: C1 · El escaneo se hace desde la tablet
    Dado un Auxiliar con la tablet en su punto de trabajo
    Cuando escanea una etiqueta con la cámara de la tablet
    Entonces el sistema recibe el código escaneado
  # Criterio SPEC (2): El sistema resuelve el identificador y muestra el SKU + Lote y las ubicaciones donde tiene existencia `[DF5-01]`.
  Escenario: C2 · El sistema resuelve el identificador y muestra el SKU + Lote
    Dado un identificador reconocido
    Cuando se escanea
    Entonces el sistema muestra el SKU + Lote y las ubicaciones donde tiene existencia
  # Criterio SPEC (3): Si el identificador no se reconoce, lo informa y ofrece reportar novedad.
  Escenario: C3 · Identificador no reconocido ofrece reportar novedad
    Dado un identificador que no existe en el sistema
    Cuando se escanea
    Entonces el sistema lo informa y ofrece reportar una novedad
  # Criterio SPEC (4): Si el identificador está anulado, lo informa y rechaza la operación.
  Escenario: C4 · Identificador anulado se rechaza
    Dado un identificador en estado anulado
    Cuando se escanea
    Entonces el sistema lo informa y rechaza la operación
  # Criterio SPEC (5): El tiempo entre escaneo y respuesta cumple RNF-REN-002. [SRS: el SPEC cita RNF-014 (ID legacy, referencia errónea); el requisito aplicable es RNF-REN-002 (H-05)]
  Escenario: C5 · El tiempo de respuesta cumple el requisito de rendimiento
    Dado un escaneo de un identificador válido
    Cuando el sistema lo resuelve
    Entonces la respuesta se presenta dentro del tiempo definido para la resolución de identificadores
```

### HU-QRC-003 — Generar códigos QR para las ubicaciones

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-027  
**Depende de:** HU-BOD-001 · **RF:** RF-QRC-004 · **RN:** RN-IDE-002 · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Administrador **QUIERO** generar códigos QR para las ubicaciones **PARA** que el Auxiliar confirme dónde deja la mercancía escaneando, sin escribir el código del estante.

```gherkin
@HU-QRC-003 @Should @M-06
Característica: HU-QRC-003 — Generar códigos QR para las ubicaciones
  # Criterio SPEC (1): Cada ubicación tiene su identificador QR propio.
  Escenario: C1 · Cada ubicación tiene su identificador QR propio
    Dada una ubicación creada
    Cuando se consulta su identificador
    Entonces tiene un identificador QR propio
  # Criterio SPEC (2): Se puede imprimir por zona completa.
  Escenario: C2 · Se puede imprimir por zona completa
    Dada una zona con varias ubicaciones
    Cuando el Administrador solicita la impresión de la zona
    Entonces el sistema imprime los identificadores de todas sus ubicaciones
  # Criterio SPEC (3): El escaneo de una ubicación la selecciona como origen o destino según el contexto.
  Escenario: C3 · El escaneo de una ubicación la selecciona como origen o destino
    Dada una operación que solicita una ubicación
    Cuando el usuario escanea el identificador de una ubicación
    Entonces el sistema la selecciona como origen o destino según el contexto
  # Criterio SPEC (4): El identificador de ubicación es distinguible del de mercancía.
  Escenario: C4 · El identificador de ubicación es distinguible del de mercancía
    Dado un identificador de ubicación y uno de mercancía
    Cuando se escanean
    Entonces el sistema los distingue como tipos de identificador diferentes
```

### HU-QRC-004 — Reimprimir una etiqueta deteriorada

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar / Coordinador · **Legacy:** HU-028  
**Depende de:** HU-QRC-001 · **RF:** RF-QRC-006, RF-QRC-007 · **RN:** RN-IDE-004 · **KPI:** —  
**Origen (SPEC):** `[RN-IDE-004]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** solicitar la reimpresión de una etiqueta deteriorada **PARA** poder seguir trabajando sin perder la trazabilidad de esa mercancía.

```gherkin
@HU-QRC-004 @Should @M-06
Característica: HU-QRC-004 — Reimprimir una etiqueta deteriorada
  # Criterio SPEC (1): La reimpresión exige motivo.
  Escenario: C1 · La reimpresión exige motivo
    Dada una etiqueta deteriorada
    Cuando se solicita la reimpresión sin indicar motivo
    Entonces el sistema no permite la reimpresión
  # Criterio SPEC (2): La reimpresión produce otra copia del mismo QR: el identificador no cambia y no se crea una nueva identidad `[RN-IDE-004]` `[Q-09]`.
  Escenario: C2 · La reimpresión produce otra copia del mismo QR sin crear una nueva identidad
    Dada una reimpresión con motivo registrado
    Cuando se imprime la etiqueta de nuevo
    Entonces el identificador es el mismo y no se crea una nueva identidad
  # Criterio SPEC (3): Reimprimir no marca el identificador como reemplazado.
  Escenario: C3 · Reimprimir no marca el identificador como reemplazado
    Dada una reimpresión completada
    Cuando se consulta el identificador
    Entonces sigue activo y no figura como reemplazado
  # Criterio SPEC (4): El historial de reimpresiones del SKU + Lote es consultable.
  Escenario: C4 · El historial de reimpresiones del SKU + Lote es consultable
    Dado un SKU + Lote con reimpresiones
    Cuando se consulta su historial de reimpresiones
    Entonces se muestran todas las reimpresiones con su motivo
  # Criterio SPEC (5): La reimpresión queda en la bitácora.
  Escenario: C5 · La reimpresión queda en bitácora
    Dada una reimpresión completada
    Cuando el sistema registra el evento
    Entonces la reimpresión queda en la bitácora con su motivo
```

### HU-QRC-005 — Asociar el código de barras del proveedor como identificador secundario

**Prioridad:** Could (P2) · **Horizonte:** H2 · **Actor (SPEC):** Coordinador · **Legacy:** HU-029  
**Depende de:** HU-QRC-001 · **RF:** RF-QRC-008 · **RN:** RN-IDE-003 · **KPI:** —  
**Origen (SPEC):** `[DC-08]` `[RN-IDE-003]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** asociar el código de barras del proveedor a nuestro identificador QR de SKU + Lote **PARA** aprovechar la etiqueta que ya viene, sin dejar de usar el QR como identificador principal.

```gherkin
@HU-QRC-005 @Could @M-06
Característica: HU-QRC-005 — Asociar el código de barras del proveedor como identificador secundario
  # Criterio SPEC (1): El código de barras se asocia como identificador secundario.
  Escenario: C1 · El código de barras se asocia como identificador secundario
    Dado un identificador QR de SKU + Lote y un código de barras del proveedor
    Cuando el Coordinador los asocia
    Entonces el código de barras queda como identificador secundario de ese SKU + Lote
  # Criterio SPEC (2): Su lectura permite consultar el SKU + Lote.
  Escenario: C2 · Su lectura permite consultar el SKU + Lote
    Dado un código de barras asociado a un SKU + Lote
    Cuando se lee en el sistema
    Entonces el sistema muestra el SKU + Lote para consulta
  # Criterio SPEC (3): `[RN-IDE-003]` No permite por sí solo ejecutar operaciones de escritura: estas exigen el QR.
  Escenario: C3 · No permite por sí solo operaciones de escritura
    Dada una operación de escritura iniciada solo con el código de barras
    Cuando el usuario intenta confirmarla
    Entonces el sistema la rechaza porque la escritura exige el identificador QR
  # Criterio SPEC (4): Un mismo código de barras no puede asociarse a dos identificadores QR distintos `[DF5-01]`.
  Escenario: C4 · Un código de barras no se asocia a dos identificadores QR
    Dado un código de barras asociado al identificador QR de un SKU + Lote
    Cuando se intenta asociarlo al identificador QR de otro SKU + Lote
    Entonces el sistema lo rechaza
```


## 5.9 M-07 · Entradas y Recepción (dominio ENT)

### HU-ENT-001 — Crear el documento de entrada con lo esperado

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador · **Legacy:** HU-030  
**Depende de:** HU-CAT-001, HU-USR-001 · **RF:** RF-ENT-001, RF-ENT-002, RF-ENT-004 · **RN:** RN-ENT-002 · **KPI:** KPI-12  
**Origen (SPEC):** `[MON §8.2]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** crear un documento de entrada con lo que espero recibir **PARA** poder verificar contra él lo que realmente llega.

```gherkin
@HU-ENT-001 @Must @M-07
Característica: HU-ENT-001 — Crear el documento de entrada con lo esperado
  # Criterio SPEC (1): El documento registra origen, fecha esperada y líneas con referencia, talla, color y cantidad esperada.
  Escenario: C1 · El documento registra origen, fecha esperada y líneas esperadas
    Dado el Coordinador creando un documento de entrada
    Cuando registra origen, fecha esperada y líneas con referencia, talla, color y cantidad esperada
    Entonces el documento queda guardado con esos datos
  # Criterio SPEC (2): `[DC-03]` No solicita precio, condiciones comerciales ni datos de orden de compra.
  Escenario: C2 · No solicita precio ni datos de orden de compra
    Dado el formulario del documento de entrada
    Cuando el Coordinador lo completa
    Entonces el sistema no solicita precio, condiciones comerciales ni datos de orden de compra
  # Criterio SPEC (3): Queda en estado pendiente de recepción.
  Escenario: C3 · El documento queda pendiente de recepción
    Dado un documento de entrada recién creado
    Cuando se consulta su estado
    Entonces figura como pendiente de recepción
  # Criterio SPEC (4): Si existe otro documento con mismo origen, referencia y fecha, el sistema advierte de posible duplicado `[RN-ENT-002]`.
  Escenario: C4 · Se advierte de posible duplicado
    Dado un documento existente con el mismo origen, referencia y fecha
    Cuando el Coordinador crea otro documento con esos mismos datos
    Entonces el sistema advierte de un posible duplicado y exige confirmación explícita
```

### HU-ENT-002 — Registrar en tablet lo que se recibe, en el momento

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-031  
**Depende de:** HU-ENT-001 · **RF:** RF-ENT-005, RF-ENT-006, RF-ENT-017 · **RN:** RN-INT-003, RN-INT-008 · **KPI:** KPI-12  
**Origen (SPEC):** `[MON §3, §8.2]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** registrar en la tablet lo que voy recibiendo, en el momento de recibirlo **PARA** no tener que anotarlo en un papel y pasarlo después.

```gherkin
@HU-ENT-002 @Must @M-07
Característica: HU-ENT-002 — Registrar en tablet lo que se recibe, en el momento
  # Criterio SPEC (1): El registro se hace desde la tablet, en la zona de recepción `[DC-05]`.
  Escenario: C1 · El registro se hace desde la tablet en la zona de recepción
    Dado un Auxiliar en la zona de recepción con su tablet
    Cuando abre el documento de entrada
    Entonces puede registrar la recepción desde la tablet
  # Criterio SPEC (2): Se registra cantidad recibida por línea.
  Escenario: C2 · Se registra la cantidad recibida por línea
    Dado un documento con líneas esperadas
    Cuando el Auxiliar cuenta y registra lo recibido
    Entonces la cantidad recibida queda registrada por cada línea
  # Criterio SPEC (3): El sistema confirma visualmente cada registro guardado.
  Escenario: C3 · Confirmación visible de cada registro guardado
    Dada una cantidad registrada por el Auxiliar
    Cuando el sistema la guarda
    Entonces muestra una confirmación visible de que el registro quedó guardado
  # Criterio SPEC (4): La recepción puede interrumpirse y continuarse, incluso por otro usuario, quedando ambos registrados.
  Escenario: C4 · La recepción puede interrumpirse y continuarse por otro usuario
    Dada una recepción interrumpida al fin del turno
    Cuando otro usuario la continúa
    Entonces la recepción continúa y quedan registrados ambos usuarios
  # Criterio SPEC (5): Sin conectividad, el registro se retiene y sincroniza después `[RN-INT-003]`.
  Escenario: C5 · Sin conectividad el registro se retiene y sincroniza después
    Dada una pérdida de conectividad durante la recepción
    Cuando el Auxiliar sigue registrando
    Entonces el sistema retiene el registro localmente
    Y lo sincroniza al restablecerse la conexión
```

### HU-ENT-003 — Confirmar la entrada por una segunda persona

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador · **Legacy:** HU-032  
**Depende de:** HU-ENT-002, HU-LOT-001 · **RF:** RF-ENT-010, RF-ENT-011 · **RN:** RN-ENT-007, RN-EXI-007, RN-INT-002, RN-INT-004 · **KPI:** KPI-05, KPI-11, KPI-12  
**Origen (SPEC):** `[PR-01]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** confirmar la entrada después de que el Auxiliar la recibió **PARA** que exista una verificación por una segunda persona antes de afectar el inventario.

```gherkin
@HU-ENT-003 @Must @M-07
Característica: HU-ENT-003 — Confirmar la entrada por una segunda persona
  # Criterio SPEC (1): `[PR-01]` Quien registró la recepción física no puede confirmarla.
  Escenario: C1 · Quien registró la recepción física no puede confirmarla
    Dada una recepción registrada por un usuario
    Cuando ese mismo usuario intenta confirmar la entrada
    Entonces el sistema lo impide y exige un segundo actor
  # Criterio SPEC (2): Al confirmar, el sistema genera el movimiento de entrada en el kardex.
  Escenario: C2 · Al confirmar se genera el movimiento de entrada en el kardex
    Dada una recepción lista para confirmar
    Cuando el Coordinador confirma la entrada
    Entonces el sistema genera el movimiento de entrada en el kardex
  # Criterio SPEC (3): La existencia se incrementa.
  Escenario: C3 · La existencia se incrementa
    Dada una entrada confirmada
    Cuando se consulta la existencia
    Entonces la existencia refleja el incremento de la mercancía recibida
  # Criterio SPEC (4): Se crea o asocia el lote.
  Escenario: C4 · Se crea o asocia el lote
    Dada una entrada confirmada
    Cuando se consulta la mercancía recibida
    Entonces está asociada a un lote creado o existente
  # Criterio SPEC (5): Una entrada confirmada no puede editarse `[RN-INT-002]`.
  Escenario: C5 · Una entrada confirmada no puede editarse
    Dada una entrada confirmada
    Cuando se intenta editarla
    Entonces el sistema no lo permite y solo admite corregirla con un movimiento inverso
```

### HU-ENT-004 — Ver la diferencia entre lo esperado y lo recibido

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador / Jefe · **Legacy:** HU-033  
**Depende de:** HU-ENT-001, HU-ENT-002 · **RF:** RF-ENT-007, RF-ENT-008, RF-ENT-009 · **RN:** RN-ENT-003, RN-ENT-004, RN-ENT-005 · **KPI:** —  
**Origen (SPEC):** `[RN-ENT-003]` `[RN-ENT-004]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** que el sistema me muestre la diferencia entre lo esperado y lo recibido **PARA** detectar faltantes de proveedor en el momento y no días después.

```gherkin
@HU-ENT-004 @Must @M-07
Característica: HU-ENT-004 — Ver la diferencia entre lo esperado y lo recibido
  # Criterio SPEC (1): El sistema compara línea por línea.
  Escenario: C1 · El sistema compara línea por línea
    Dado un documento con cantidades esperadas y recibidas
    Cuando se registra la recepción
    Entonces el sistema compara cada línea esperada contra la recibida
  # Criterio SPEC (2): Si lo recibido es menor, marca faltante de recepción y notifica al Jefe `[RN-ENT-004]`.
  Escenario: C2 · Faltante de recepción notifica al Jefe
    Dada una línea con cantidad recibida menor que la esperada
    Cuando se compara
    Entonces el sistema marca faltante de recepción
    Y notifica al Jefe
  # Criterio SPEC (3): Si es mayor, marca sobrante y exige autorización del Jefe antes de confirmar `[RN-ENT-005]`.
  Escenario: C3 · Sobrante exige autorización del Jefe antes de confirmar
    Dada una línea con cantidad recibida mayor que la esperada
    Cuando se compara
    Entonces el sistema marca sobrante
    Y exige la autorización del Jefe antes de confirmar la entrada
  # Criterio SPEC (4): Si coincide, marca recibido conforme.
  Escenario: C4 · Coincidencia queda como recibido conforme
    Dada una línea con cantidad recibida igual a la esperada
    Cuando se compara
    Entonces el sistema la marca como recibido conforme
  # Criterio SPEC (5): La diferencia queda registrada en el documento.
  Escenario: C5 · La diferencia queda registrada en el documento
    Dada una comparación con diferencias
    Cuando el sistema finaliza la comparación
    Entonces las diferencias quedan registradas en el documento
```

### HU-ENT-005 — Registrar mercancía dañada en la recepción

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-034  
**Depende de:** HU-ENT-002, HU-NOV-001 · **RF:** RF-ENT-012 · **RN:** RN-ENT-006 · **KPI:** —  
**Origen (SPEC):** `[RN-ENT-006]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** registrar que parte de la mercancía llegó dañada **PARA** que no entre al inventario disponible y quede constancia de la novedad.

```gherkin
@HU-ENT-005 @Should @M-07
Característica: HU-ENT-005 — Registrar mercancía dañada en la recepción
  # Criterio SPEC (1): Se registra la cantidad conforme y la cantidad dañada por separado.
  Escenario: C1 · Cantidad conforme y cantidad dañada por separado
    Dada una recepción con parte de la mercancía dañada
    Cuando el Auxiliar registra la recepción
    Entonces puede indicar por separado la cantidad conforme y la cantidad dañada
  # Criterio SPEC (2): La dañada no ingresa como disponible `[RN-ENT-006]`.
  Escenario: C2 · La mercancía dañada no ingresa como disponible
    Dada una cantidad registrada como dañada
    Cuando se confirma la entrada
    Entonces esa cantidad no ingresa como disponible
  # Criterio SPEC (3): Se abre automáticamente una novedad (M-12).
  Escenario: C3 · Se abre automáticamente una novedad
    Dada una cantidad registrada como dañada
    Cuando se guarda el registro
    Entonces el sistema abre automáticamente una novedad
  # Criterio SPEC (4): La mercancía dañada, si ingresa, lo hace a zona de cuarentena en estado inmovilizado.
  Escenario: C4 · Si ingresa, lo hace a cuarentena como inmovilizada
    Dada mercancía dañada que ingresa al inventario
    Cuando se ubica
    Entonces ingresa a la zona de cuarentena en estado inmovilizado
  # Criterio SPEC (5): El Jefe es notificado.
  Escenario: C5 · El Jefe es notificado
    Dada una novedad por mercancía dañada
    Cuando se abre
    Entonces el Jefe recibe una notificación
```

### HU-ENT-006 — Recibir del sistema la ubicación donde dejar la mercancía

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-035  
**Depende de:** HU-BOD-001, HU-BOD-002, HU-BOD-005, HU-QRC-001 · **RF:** RF-BOD-004, RF-BOD-005, RF-BOD-008, RF-MOV-005, RF-BOD-009 · **RN:** RN-EXI-002, RN-MOV-001, RN-MOV-002, RN-MOV-003, RN-MOV-010 · **KPI:** KPI-10, KPI-18  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** que el sistema me diga dónde dejar la mercancía **PARA** no tener que decidirlo yo ni preguntar cada vez.

```gherkin
@HU-ENT-006 @Must @M-07
Característica: HU-ENT-006 — Recibir del sistema la ubicación donde dejar la mercancía
  # Criterio SPEC (1): El sistema propone la ubicación con una regla fija —zona por categoría, agrupación por referencia y mayor capacidad libre, en ese orden—; si ninguna aplica, propone la zona de recepción `[RN-MOV-001]` `[H-19]`.
  Escenario: C1 · El sistema propone la ubicación con una regla fija
    Dada una mercancía por ubicar
    Cuando el sistema calcula el destino
    Entonces propone una ubicación por zona por categoría, agrupación por referencia y mayor capacidad libre, o la zona de recepción si ninguna aplica
  # Criterio SPEC (2): El Auxiliar confirma escaneando la mercancía y luego la ubicación `[DC-08]`.
  Escenario: C2 · El Auxiliar confirma escaneando mercancía y luego ubicación
    Dada una ubicación propuesta
    Cuando el Auxiliar escanea la mercancía y después la ubicación
    Entonces el sistema registra la ubicación confirmada
  # Criterio SPEC (3): Si ubica en un lugar distinto, el sistema lo permite pero registra la desviación y avisa al Coordinador `[RN-MOV-003]`.
  Escenario: C3 · Una ubicación distinta se permite y registra la desviación
    Dada una ubicación distinta a la propuesta
    Cuando el Auxiliar la usa como destino
    Entonces el sistema lo permite, registra la desviación y avisa al Coordinador
  # Criterio SPEC (4): El sistema valida que la ubicación esté activa y tenga capacidad `[RN-MOV-002]`.
  Escenario: C4 · Se valida que la ubicación esté activa y con capacidad
    Dada una ubicación escaneada como destino
    Cuando el sistema la valida
    Entonces acepta el destino solo si la ubicación está activa y tiene capacidad
  # Criterio SPEC (5): Confirma visualmente el registro.
  Escenario: C5 · Confirmación visual del registro
    Dada una ubicación confirmada
    Cuando el sistema guarda el registro
    Entonces confirma visualmente al Auxiliar que quedó guardado
```

### HU-ENT-007 — Impedir recibir una referencia inexistente en el catálogo

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador · **Legacy:** HU-036  
**Depende de:** HU-CAT-001, HU-ENT-001 · **RF:** RF-ENT-003 · **RN:** RN-ENT-001, RN-MAE-001 · **KPI:** —  
**Origen (SPEC):** `[RN-MAE-001]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** que el sistema me impida recibir una referencia que no existe en el catálogo **PARA** que no entre mercancía sin identidad definida.

```gherkin
@HU-ENT-007 @Should @M-07
Característica: HU-ENT-007 — Impedir recibir una referencia inexistente en el catálogo
  # Criterio SPEC (1): El documento de entrada solo admite referencias activas del catálogo `[RN-MAE-001]`.
  Escenario: C1 · El documento solo admite referencias activas del catálogo
    Dado un documento de entrada en creación
    Cuando se agrega una línea
    Entonces solo se admiten referencias activas del catálogo
  # Criterio SPEC (2): Si la referencia no existe, el sistema lo informa y ofrece crearla, si el usuario tiene permiso.
  Escenario: C2 · Referencia inexistente: se informa y se ofrece crearla
    Dada una referencia que no existe en el catálogo
    Cuando el usuario intenta agregarla
    Entonces el sistema informa que no existe
    Y ofrece crearla si el usuario tiene permiso
  # Criterio SPEC (3): El Auxiliar no puede crear referencias.
  Escenario: C3 · El Auxiliar no puede crear referencias
    Dado un usuario con rol Auxiliar
    Cuando se topa con una referencia inexistente
    Entonces el sistema no le permite crearla
  # Criterio SPEC (4): La entrada no avanza hasta resolverlo.
  Escenario: C4 · La entrada no avanza hasta resolverlo
    Dado un documento con una referencia inexistente
    Cuando se intenta avanzar la entrada
    Entonces la entrada no avanza hasta resolver la referencia
```

### HU-ENT-008 — Consultar el historial de entradas

**Prioridad:** Could (P2) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador / Jefe · **Legacy:** HU-037  
**Depende de:** HU-ENT-003 · **RF:** RF-ENT-013 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** consultar el historial de entradas **PARA** revisar qué se recibió, de quién y con qué novedades.

```gherkin
@HU-ENT-008 @Could @M-07
Característica: HU-ENT-008 — Consultar el historial de entradas
  # Criterio SPEC (1): Filtro por período, origen, estado y referencia.
  Escenario: C1 · Filtro por período, origen, estado y referencia
    Dadas varias entradas registradas
    Cuando el usuario aplica filtros por período, origen, estado o referencia
    Entonces el sistema muestra solo las entradas que cumplen el filtro
  # Criterio SPEC (2): Muestra esperado, recibido y diferencia.
  Escenario: C2 · Muestra esperado, recibido y diferencia
    Dada una entrada consultada
    Cuando se presenta su detalle
    Entonces muestra la cantidad esperada, la recibida y la diferencia
  # Criterio SPEC (3): Permite abrir el detalle y el movimiento de kardex asociado.
  Escenario: C3 · Permite abrir el detalle y el movimiento de kardex asociado
    Dada una entrada consultada
    Cuando el usuario abre su detalle
    Entonces puede acceder al movimiento de kardex asociado
  # Criterio SPEC (4): Exportable.
  Escenario: C4 · El historial es exportable
    Dado un historial de entradas filtrado
    Cuando el usuario solicita exportarlo
    Entonces el sistema entrega la exportación
```

### HU-ENT-009 — Registrar cada pieza recibida con su cantidad

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-104  
**Depende de:** HU-ENT-002, HU-LOT-001 · **RF:** RF-ENT-014, RF-ENT-015 · **RN:** RN-ENT-003, RN-LOT-006, RN-LOT-007 · **KPI:** —  
**Origen (SPEC):** `[Q-11]` `[F-1]` `[F-2]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** registrar cada rollo, paquete o bolsa que recibo con su cantidad **PARA** saber después cuál pieza es cuál y cuánto trae cada una sin tener que medirla otra vez.

```gherkin
@HU-ENT-009 @Must @M-07
Característica: HU-ENT-009 — Registrar cada pieza recibida con su cantidad
  # Criterio SPEC (1): Cada pieza se registra con su tipo —rollo para referencias en metros o kilogramos; paquete o bolsa para referencias en unidades— y con su cantidad propia `[F-1]` `[F-2]`.
  Escenario: C1 · Cada pieza se registra con su tipo y su cantidad propia
    Dada una línea de entrada en recepción
    Cuando el Auxiliar registra un rollo, un paquete o una bolsa
    Entonces el sistema guarda la pieza con su tipo y su cantidad propia
  # Criterio SPEC (2): Cada pieza pertenece a un solo SKU + Lote `[RN-LOT-006]`.
  Escenario: C2 · Cada pieza pertenece a un solo SKU + Lote
    Dada una pieza en registro
    Cuando el Auxiliar intenta asociarla a más de un SKU + Lote
    Entonces el sistema no lo permite y la pieza queda asociada a un solo SKU + Lote
  # Criterio SPEC (3): La cantidad recibida de la línea es la suma de las cantidades de sus piezas y se compara contra la esperada `[RN-LOT-007]` `[RN-ENT-003]`.
  Escenario: C3 · La cantidad recibida de la línea es la suma de sus piezas
    Dada una línea con varias piezas registradas
    Cuando el sistema calcula la cantidad recibida de la línea
    Entonces es la suma de las cantidades de sus piezas y se compara contra la esperada
  # Criterio SPEC (4): La pieza conserva su identidad en el sistema desde la recepción; el QR de mercancía sigue identificando solo el SKU + Lote `[DF5-01]`.
  Escenario: C4 · La pieza conserva su identidad sin cambiar el QR
    Dada una pieza registrada en la recepción
    Cuando se consulta su identidad en el sistema
    Entonces la pieza tiene identidad interna y el QR de mercancía sigue identificando solo el SKU + Lote
  # Criterio SPEC (5): El sistema confirma visualmente cada pieza registrada.
  Escenario: C5 · El sistema confirma visualmente cada pieza registrada
    Dado un Auxiliar que registra una pieza
    Cuando el sistema guarda el registro
    Entonces muestra una confirmación visible
```

### HU-ENT-010 — Registrar un contenedor o bolsa agrupada como una sola pieza

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-105  
**Depende de:** HU-ENT-009 · **RF:** RF-ENT-016 · **RN:** RN-LOT-006 · **KPI:** —  
**Origen (SPEC):** `[F-6]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** registrar como una sola pieza el contenedor o la bolsa agrupada en que llega mercancía sin rotulado individual **PARA** poder ubicarla, moverla y contarla sin rotular cada prenda.

```gherkin
@HU-ENT-010 @Should @M-07
Característica: HU-ENT-010 — Registrar un contenedor o bolsa agrupada como una sola pieza
  # Criterio SPEC (1): El contenedor o bolsa agrupada se registra como una pieza de tipo contenedor agrupado, con su cantidad de unidades `[F-6]`.
  Escenario: C1 · El contenedor se registra como pieza de tipo contenedor agrupado
    Dada mercancía sin rotulado individual que llega en un contenedor
    Cuando el Auxiliar lo registra
    Entonces el sistema guarda una pieza de tipo contenedor agrupado con su cantidad de unidades
  # Criterio SPEC (2): El contenedor pertenece a un solo SKU + Lote; registrar un contenedor con mezcla de lotes o de SKU no se admite hasta que el Director lo decida `[DECISIÓN PENDIENTE — HD-28]`.
  Escenario: C2 · El contenedor pertenece a un solo SKU + Lote
    Dado un contenedor con mezcla de lotes o de SKU
    Cuando el Auxiliar intenta registrarlo
    Entonces el sistema no lo admite hasta que el Director decida la regla
  # Criterio SPEC (3): Se ubica, mueve, cuenta y sale como cualquier otra pieza.
  Escenario: C3 · El contenedor se ubica, mueve, cuenta y sale como cualquier pieza
    Dado un contenedor agrupado registrado
    Cuando se ubica, se mueve, se cuenta o sale
    Entonces el sistema lo trata como una pieza más
  # Criterio SPEC (4): Lleva la etiqueta QR del SKU + Lote `[PN-02 E-03]`.
  Escenario: C4 · El contenedor lleva la etiqueta QR del SKU + Lote
    Dado un contenedor agrupado registrado
    Cuando se imprime su etiqueta
    Entonces lleva el QR del SKU + Lote
```


## 5.10 M-08 · Salidas (dominio SAL)

### HU-SAL-001 — Registrar una salida indicando su motivo

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Coordinador · **Legacy:** HU-038  
**Depende de:** HU-CAT-001, HU-BOD-001, HU-PAR-002 · **RF:** RF-SAL-001, RF-SAL-002, RF-SAL-003, RF-SAL-009 · **RN:** RN-EXI-003, RN-EXI-004, RN-INT-004, RN-SAL-002 · **KPI:** KPI-05, KPI-11, KPI-16  
**Origen (SPEC):** `[MON §8.2]` `[DC-03]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** registrar una salida indicando su motivo **PARA** que quede claro por qué salió la mercancía sin necesidad de gestionar la venta en este sistema.

```gherkin
@HU-SAL-001 @Must @M-08
Característica: HU-SAL-001 — Registrar una salida indicando su motivo
  # Criterio SPEC (1): La salida exige motivo tipificado de una lista cerrada `[RN-SAL-002]`.
  Escenario: C1 · La salida exige motivo tipificado de una lista cerrada
    Dada una solicitud de salida
    Cuando se intenta registrar sin motivo tipificado
    Entonces el sistema no la acepta
  # Criterio SPEC (2): `[DC-03]` No se solicita cliente, precio, factura ni documento comercial.
  Escenario: C2 · No se solicita cliente, precio, factura ni documento comercial
    Dado el formulario de salida
    Cuando se completa
    Entonces el sistema no solicita cliente, precio, factura ni documento comercial
  # Criterio SPEC (3): Se indican referencias, tallas, colores, lotes y cantidades.
  Escenario: C3 · Se indican referencias, tallas, colores, lotes y cantidades
    Dada una salida en registro
    Cuando el usuario detalla lo que sale
    Entonces puede indicar referencias, tallas, colores, lotes y cantidades
  # Criterio SPEC (4): El sistema verifica disponibilidad antes de aceptar `[RN-EXI-003]`.
  Escenario: C4 · El sistema verifica disponibilidad antes de aceptar
    Dada una salida solicitada
    Cuando el sistema evalúa la solicitud
    Entonces verifica que exista existencia disponible antes de aceptarla
```

### HU-SAL-002 — Reservar la existencia al autorizar la salida

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Jefe · **Legacy:** HU-039  
**Depende de:** HU-SAL-001 · **RF:** RF-SAL-005, RF-SAL-014 · **RN:** RN-EXI-004, RN-SAL-005 · **KPI:** —  
**Origen (SPEC):** `[RN-EXI-004]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que la existencia se reserve al autorizar la salida **PARA** que nadie más comprometa la misma mercancía mientras se prepara.

```gherkin
@HU-SAL-002 @Must @M-08
Característica: HU-SAL-002 — Reservar la existencia al autorizar la salida
  # Criterio SPEC (1): Al autorizar, la cantidad pasa a reservada `[RN-EXI-004]`.
  Escenario: C1 · Al autorizar, la cantidad pasa a reservada
    Dada una salida solicitada
    Cuando el Jefe la autoriza
    Entonces la cantidad comprometida pasa a reservada
  # Criterio SPEC (2): La existencia reservada no cuenta como disponible.
  Escenario: C2 · La existencia reservada no cuenta como disponible
    Dada existencia reservada para una salida
    Cuando se consulta el disponible
    Entonces la existencia reservada no cuenta como disponible
  # Criterio SPEC (3): Otra operación sobre la misma existencia se rechaza.
  Escenario: C3 · Otra operación sobre la misma existencia se rechaza
    Dada existencia reservada para una salida
    Cuando otra operación intenta comprometer esa misma existencia
    Entonces el sistema rechaza la operación
  # Criterio SPEC (4): La reserva se libera al ejecutarse la salida, al cancelarse o al vencer su plazo `[RN-SAL-005]`.
  Escenario: C4 · La reserva se libera al ejecutar, cancelar o vencer
    Dada una reserva vigente
    Cuando la salida se ejecuta, se cancela o vence su plazo
    Entonces la reserva se libera
```

### HU-SAL-003 — Recibir la ubicación de toma y validar el escaneo al preparar

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-040  
**Depende de:** HU-SAL-002, HU-QRC-002 · **RF:** RF-SAL-007, RF-SAL-008, RF-SAL-009 · **RN:** RN-EXI-004, RN-INT-004, RN-SAL-003, RN-SAL-004 · **KPI:** KPI-05, KPI-11, KPI-16  
**Origen (SPEC):** `[DC-08]` `[RN-SAL-004]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** que el sistema me indique de qué ubicación tomar cada cosa y me valide el escaneo **PARA** no equivocarme de talla, color o lote.

```gherkin
@HU-SAL-003 @Must @M-08
Característica: HU-SAL-003 — Recibir la ubicación de toma y validar el escaneo al preparar
  # Criterio SPEC (1): El sistema indica ubicación y cantidad por línea, según la política configurada `[RN-SAL-003]`.
  Escenario: C1 · El sistema indica ubicación y cantidad por línea
    Dada una salida autorizada con política de toma configurada
    Cuando el Auxiliar abre la tarea de preparación
    Entonces el sistema indica ubicación y cantidad para cada línea
  # Criterio SPEC (2): El Auxiliar escanea cada unidad al tomarla.
  Escenario: C2 · El Auxiliar escanea cada unidad al tomarla
    Dada una línea por preparar
    Cuando el Auxiliar toma la mercancía
    Entonces escanea cada unidad para registrarla
  # Criterio SPEC (3): Si lo escaneado no corresponde a lo solicitado, el sistema rechaza el escaneo y explica la discrepancia `[RN-SAL-004]`.
  Escenario: C3 · Un escaneo que no corresponde se rechaza explicando la discrepancia
    Dada una unidad escaneada que no corresponde a lo solicitado
    Cuando el sistema la valida
    Entonces rechaza el escaneo
    Y explica la discrepancia
  # Criterio SPEC (4): El progreso de preparación es visible.
  Escenario: C4 · El progreso de preparación es visible
    Dada una preparación en curso
    Cuando el Auxiliar escanea unidades
    Entonces el progreso de la preparación es visible
  # Criterio SPEC (5): Confirma al completar.
  Escenario: C5 · Confirma al completar
    Dada una preparación con todas las líneas completas
    Cuando el Auxiliar la confirma
    Entonces el sistema registra la salida
```

### HU-SAL-004 — Impedir sacar más de lo que hay

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Coordinador · **Legacy:** HU-041  
**Depende de:** HU-SAL-001 · **RF:** RF-SAL-004 · **RN:** RN-EXI-001 · **KPI:** —  
**Origen (SPEC):** `[RN-EXI-001]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que el sistema me impida sacar más de lo que hay **PARA** que el inventario nunca quede en negativo.

```gherkin
@HU-SAL-004 @Must @M-08
Característica: HU-SAL-004 — Impedir sacar más de lo que hay
  # Criterio SPEC (1): `[RN-EXI-001]` Ninguna salida puede dejar la existencia por debajo de cero, sin excepción ni autorización posible.
  Escenario: C1 · Ninguna salida deja la existencia por debajo de cero
    Dada una salida que dejaría la existencia por debajo de cero
    Cuando se intenta registrar
    Entonces el sistema la rechaza sin excepción ni autorización posible
  # Criterio SPEC (2): Si lo disponible es insuficiente, el sistema rechaza e informa cuánto hay.
  Escenario: C2 · Si lo disponible es insuficiente se informa cuánto hay
    Dada una solicitud mayor que la existencia disponible
    Cuando el sistema la rechaza
    Entonces informa cuánta existencia disponible hay
  # Criterio SPEC (3): Ofrece registrar una salida parcial por la cantidad disponible, previa autorización.
  Escenario: C3 · Ofrece salida parcial previa autorización
    Dada una solicitud rechazada por insuficiencia
    Cuando el sistema ofrece alternativas
    Entonces permite registrar una salida parcial por la cantidad disponible, previa autorización
  # Criterio SPEC (4): El rechazo queda registrado.
  Escenario: C4 · El rechazo queda registrado
    Dada una salida rechazada por existencia insuficiente
    Cuando se completa el rechazo
    Entonces el rechazo queda registrado
```

### HU-SAL-005 — Exigir aprobación del Jefe para toda baja por daño

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe · **Legacy:** HU-042  
**Depende de:** HU-SAL-001, HU-PAR-002 · **RF:** RF-SAL-010 · **RN:** RN-SAL-006 · **KPI:** KPI-13  
**Origen (SPEC):** `[RN-SAL-006]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que la baja de mercancía dañada exija mi aprobación siempre **PARA** que nadie pueda dar de baja inventario sin que yo lo sepa.

```gherkin
@HU-SAL-005 @Should @M-08
Característica: HU-SAL-005 — Exigir aprobación del Jefe para toda baja por daño
  # Criterio SPEC (1): El motivo de baja por daño siempre requiere aprobación del Jefe, cualquiera sea la cantidad `[RN-SAL-006]`.
  Escenario: C1 · La baja por daño siempre requiere aprobación del Jefe
    Dada una salida con motivo de baja por daño de cualquier cantidad
    Cuando se solicita
    Entonces requiere la aprobación del Jefe
  # Criterio SPEC (2): Exige observación y evidencia.
  Escenario: C2 · Exige observación y evidencia
    Dada una solicitud de baja por daño
    Cuando se intenta enviar sin observación o evidencia
    Entonces el sistema no la acepta
  # Criterio SPEC (3): Genera movimiento de salida marcado como baja.
  Escenario: C3 · Genera un movimiento de salida marcado como baja
    Dada una baja aprobada
    Cuando se ejecuta
    Entonces el sistema genera un movimiento de salida marcado como baja
  # Criterio SPEC (4): Alimenta el reporte de mermas y el KPI-13.
  Escenario: C4 · Alimenta el reporte de mermas y el indicador de merma
    Dada una baja registrada
    Cuando se calculan los indicadores
    Entonces la baja alimenta el reporte de mermas y la tasa de merma
```

### HU-SAL-006 — Registrar el retorno de mercancía que había salido

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador · **Legacy:** HU-043  
**Depende de:** HU-ENT-003, HU-SAL-001 · **RF:** RF-SAL-011 · **RN:** RN-SAL-007 · **KPI:** —  
**Origen (SPEC):** `[RN-SAL-007]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** registrar el retorno de mercancía que había salido **PARA** que vuelva al inventario dejando claro de dónde vino.

```gherkin
@HU-SAL-006 @Should @M-08
Característica: HU-SAL-006 — Registrar el retorno de mercancía que había salido
  # Criterio SPEC (1): `[RN-SAL-007]` El retorno se registra como una entrada nueva, no como reversión de la salida original.
  Escenario: C1 · El retorno se registra como entrada nueva
    Dada mercancía que retorna tras una salida
    Cuando el Coordinador la registra
    Entonces el sistema la registra como una entrada nueva y no como reversión
  # Criterio SPEC (2): La entrada de retorno referencia la salida original.
  Escenario: C2 · La entrada de retorno referencia la salida original
    Dada una entrada de retorno
    Cuando se consulta
    Entonces referencia la salida original
  # Criterio SPEC (3): El kardex muestra ambos movimientos.
  Escenario: C3 · El kardex muestra ambos movimientos
    Dada una salida y su retorno posterior
    Cuando se consulta el kardex
    Entonces muestra ambos movimientos
  # Criterio SPEC (4): La mercancía retornada puede requerir inspección antes de quedar disponible.
  Escenario: C4 · La mercancía retornada puede requerir inspección antes de quedar disponible
    Dada mercancía retornada
    Cuando el proceso de recepción la evalúa
    Entonces puede requerir inspección antes de quedar disponible
```

### HU-SAL-007 — Autorizar salidas pequeñas sin depender del Jefe

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Coordinador · **Legacy:** HU-044  
**Depende de:** HU-SAL-001, HU-PAR-001 · **RF:** RF-SAL-006 · **RN:** RN-SAL-001 · **KPI:** KPI-22  
**Origen (SPEC):** `[RN-SAL-001]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** poder autorizar salidas pequeñas sin molestar al Jefe **PARA** que la operación no se detenga por cada movimiento menor.

```gherkin
@HU-SAL-007 @Should @M-08
Característica: HU-SAL-007 — Autorizar salidas pequeñas sin depender del Jefe
  # Criterio SPEC (1): El Administrador configura el umbral de autorización del Coordinador `[RN-SAL-001]`.
  Escenario: C1 · El Administrador configura el umbral de autorización del Coordinador
    Dado el Administrador en Parámetros y Configuración
    Cuando define el umbral de autorización del Coordinador
    Entonces el umbral queda configurado
  # Criterio SPEC (2): Por debajo del umbral, el Coordinador autoriza.
  Escenario: C2 · Por debajo del umbral, el Coordinador autoriza
    Dada una salida por debajo del umbral configurado
    Cuando el Coordinador la revisa
    Entonces puede autorizarla
  # Criterio SPEC (3): Por encima, la solicitud se enruta al Jefe.
  Escenario: C3 · Por encima del umbral, se enruta al Jefe
    Dada una salida por encima del umbral configurado
    Cuando se solicita
    Entonces el sistema la enruta al Jefe
  # Criterio SPEC (4): El umbral es consultable por el Coordinador.
  Escenario: C4 · El umbral es consultable por el Coordinador
    Dado un Coordinador
    Cuando consulta su umbral de autorización
    Entonces el sistema le muestra el valor vigente
  # Criterio SPEC (5): Toda autorización queda atribuida a quien la otorgó.
  Escenario: C5 · Toda autorización queda atribuida a quien la otorgó
    Dada una salida autorizada
    Cuando se consulta su registro
    Entonces la autorización figura atribuida a quien la otorgó
```

### HU-SAL-008 — Que el escaneo de salida verifique y cuente las piezas tomadas

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-107  
**Depende de:** HU-ENT-009, HU-SAL-003 · **RF:** RF-SAL-012 · **RN:** RN-EXI-003, RN-SAL-004, RN-SAL-009 · **KPI:** —  
**Origen (SPEC):** `[Q-10]` `[RN-SAL-009*]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** que, al preparar una salida, el escaneo me confirme que tomo lo correcto y cuente las piezas que tomo **PARA** no dejar la salida incompleta ni contar dos veces lo mismo.

```gherkin
@HU-SAL-008 @Must @M-08
Característica: HU-SAL-008 — Que el escaneo de salida verifique y cuente las piezas tomadas
  # Criterio SPEC (1): El escaneo verifica que lo tomado corresponde a lo solicitado `[RN-SAL-004]` y cuenta las piezas tomadas `[Q-10]`.
  Escenario: C1 · El escaneo verifica y cuenta las piezas tomadas
    Dada una preparación de salida en curso
    Cuando el Auxiliar escanea lo que toma
    Entonces el sistema verifica que corresponde a lo solicitado y cuenta las piezas tomadas
  # Criterio SPEC (2): Después de escanear, el Auxiliar selecciona la pieza; cada pieza se cuenta una sola vez y seleccionar de nuevo la misma no suma `[RN-SAL-009]`.
  Escenario: C2 · Cada pieza se cuenta una sola vez
    Dada una pieza ya seleccionada en la preparación
    Cuando el Auxiliar selecciona de nuevo la misma pieza
    Entonces el sistema no la suma otra vez
  # Criterio SPEC (3): El progreso muestra las piezas y la cantidad tomadas frente a lo solicitado.
  Escenario: C3 · El progreso muestra lo tomado frente a lo solicitado
    Dada una preparación de salida en curso
    Cuando el Auxiliar consulta el progreso
    Entonces el sistema muestra las piezas y la cantidad tomadas frente a lo solicitado
  # Criterio SPEC (4): La preparación no se confirma completa mientras falten piezas o cantidad, salvo salida parcial autorizada `[RN-EXI-003]`.
  Escenario: C4 · No se confirma completa mientras falten piezas o cantidad
    Dada una preparación con piezas o cantidad pendientes
    Cuando el Auxiliar intenta confirmarla como completa
    Entonces el sistema no la confirma, salvo salida parcial autorizada
  # Criterio SPEC (5): Cada pieza tomada queda en el kardex.
  Escenario: C5 · Cada pieza tomada queda en el kardex
    Dada una salida confirmada
    Cuando se consulta el kardex
    Entonces cada pieza tomada figura en el movimiento de salida
```

### HU-SAL-009 — Registrar el corte parcial de un rollo

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-108  
**Depende de:** HU-SAL-008 · **RF:** RF-SAL-013 · **RN:** RN-EXI-001, RN-SAL-002, RN-SAL-008 · **KPI:** —  
**Origen (SPEC):** `[F-3]` `[RN-SAL-008*]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** registrar que corté solo una parte de un rollo **PARA** que el resto siga en el inventario con la cantidad correcta.

```gherkin
@HU-SAL-009 @Must @M-08
Característica: HU-SAL-009 — Registrar el corte parcial de un rollo
  # Criterio SPEC (1): Se selecciona la pieza y se indica la cantidad cortada `[F-3]`.
  Escenario: C1 · Se selecciona la pieza y se indica la cantidad cortada
    Dada una salida con un rollo
    Cuando el Auxiliar selecciona la pieza e indica la cantidad cortada
    Entonces el sistema registra el corte
  # Criterio SPEC (2): La cantidad cortada no puede superar la cantidad de la pieza `[RN-EXI-001]` `[RN-SAL-008]`.
  Escenario: C2 · La cantidad cortada no puede superar la de la pieza
    Dada una pieza con una cantidad determinada
    Cuando el Auxiliar indica una cantidad cortada mayor a la de la pieza
    Entonces el sistema rechaza el corte
  # Criterio SPEC (3): El sistema descuenta lo cortado de la pieza, que conserva su identidad con el remanente `[RN-SAL-008]`.
  Escenario: C3 · La pieza conserva su identidad con el remanente
    Dado un corte parcial registrado
    Cuando se consulta la pieza
    Entonces conserva su identidad y muestra la cantidad restante
  # Criterio SPEC (4): El corte se registra como una salida, con motivo tipificado, autorización y atribución personal `[RN-SAL-002]`.
  Escenario: C4 · El corte se registra como una salida con motivo y autorización
    Dado un corte parcial
    Cuando el sistema lo registra
    Entonces queda como salida con motivo tipificado, autorización y atribución personal
  # Criterio SPEC (5): El kardex registra qué pieza, cuánto, quién, cuándo y por qué.
  Escenario: C5 · El kardex registra qué pieza, cuánto, quién, cuándo y por qué
    Dado un corte confirmado
    Cuando se consulta el kardex
    Entonces muestra la pieza, la cantidad, el responsable, la fecha y el motivo
  # Criterio SPEC (6): La cantidad restante de la pieza queda visible de inmediato.
  Escenario: C6 · La cantidad restante queda visible de inmediato
    Dado un corte confirmado
    Cuando el Auxiliar consulta la pieza
    Entonces ve de inmediato la cantidad restante
```


## 5.11 M-09 · Movimientos y Transferencias (dominio MOV)

### HU-MOV-001 — Registrar que se movió mercancía de un estante a otro

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-045  
**Depende de:** HU-QRC-002, HU-BOD-001 · **RF:** RF-MOV-001, RF-MOV-002 · **RN:** RN-MOV-002, RN-MOV-004, RN-MOV-010, RN-MOV-012 · **KPI:** KPI-05, KPI-11  
**Origen (SPEC):** `[RN-MOV-004]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** registrar que moví mercancía de un estante a otro **PARA** que el sistema siga sabiendo dónde está.

```gherkin
@HU-MOV-001 @Must @M-09
Característica: HU-MOV-001 — Registrar que se movió mercancía de un estante a otro
  # Criterio SPEC (1): Se escanea la mercancía y luego la ubicación destino `[DC-08]`.
  Escenario: C1 · Se escanea la mercancía y luego la ubicación destino
    Dado un Auxiliar con mercancía identificada
    Cuando escanea la mercancía y después la ubicación destino
    Entonces el sistema registra el movimiento interno
  # Criterio SPEC (2): Se mueve la pieza completa: una pieza no se divide, y tomar una parte de ella es un corte parcial que se registra como salida `[RN-MOV-012]` `[HD-29]`.
  Escenario: C2 · Se mueve la pieza completa y no se divide
    Dada una pieza en la ubicación de origen
    Cuando el Auxiliar la mueve a otra ubicación
    Entonces el sistema mueve la pieza completa y tomar una parte de ella se registra como corte parcial, no como movimiento
  # Criterio SPEC (3): `[RN-MOV-004]` La existencia total no cambia: solo cambia su distribución.
  Escenario: C3 · La existencia total no cambia
    Dado un movimiento interno registrado
    Cuando se consulta la existencia total de la unidad
    Entonces es igual a la de antes del movimiento y solo cambió su distribución
  # Criterio SPEC (4): El movimiento queda en el kardex.
  Escenario: C4 · El movimiento queda en el kardex
    Dado un movimiento interno confirmado
    Cuando se consulta el kardex
    Entonces el movimiento aparece registrado
  # Criterio SPEC (5): El sistema confirma visualmente.
  Escenario: C5 · El sistema confirma visualmente
    Dado un movimiento interno guardado
    Cuando finaliza el registro
    Entonces el sistema confirma visualmente que quedó guardado
```

### HU-MOV-002 — Impedir movimientos imposibles

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-046  
**Depende de:** HU-MOV-001 · **RF:** RF-MOV-003, RF-MOV-004, RF-MOV-005, RF-MOV-006 · **RN:** RN-EXI-003, RN-EXI-006, RN-MOV-002, RN-MOV-005, RN-MOV-010 · **KPI:** —  
**Origen (SPEC):** `[RN-EXI-003]` `[RN-MOV-005]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** que el sistema me impida movimientos imposibles **PARA** no dejar el inventario descuadrado por un error mío.

```gherkin
@HU-MOV-002 @Must @M-09
Característica: HU-MOV-002 — Impedir movimientos imposibles
  # Criterio SPEC (1): Rechaza mover más de lo existente en origen `[RN-EXI-003]`.
  Escenario: C1 · Se rechaza mover más de lo existente en origen
    Dado un movimiento con cantidad mayor a la existente en la ubicación de origen
    Cuando se intenta registrar
    Entonces el sistema lo rechaza
  # Criterio SPEC (2): Rechaza destino igual a origen `[RN-MOV-005]`.
  Escenario: C2 · Se rechaza destino igual a origen
    Dado un movimiento cuyo destino coincide con el origen
    Cuando se intenta registrar
    Entonces el sistema lo rechaza
  # Criterio SPEC (3): Rechaza destino inactivo o sin capacidad `[RN-MOV-002]`.
  Escenario: C3 · Se rechaza destino inactivo o sin capacidad
    Dada una ubicación destino inactiva o sin capacidad
    Cuando se intenta registrar el movimiento
    Entonces el sistema lo rechaza
  # Criterio SPEC (4): Rechaza mover existencia inmovilizada `[RN-EXI-006]`.
  Escenario: C4 · Se rechaza mover existencia inmovilizada
    Dada existencia inmovilizada
    Cuando se intenta moverla sin la autorización correspondiente
    Entonces el sistema lo rechaza
  # Criterio SPEC (5): Cada rechazo explica el motivo en lenguaje comprensible `[MON §8.2 — usabilidad]`.
  Escenario: C5 · Cada rechazo explica el motivo en lenguaje comprensible
    Dado cualquier movimiento rechazado
    Cuando el sistema informa el resultado
    Entonces explica el motivo en lenguaje comprensible para un usuario sin formación técnica
```

### HU-MOV-003 — Crear una transferencia entre zonas o bodegas

**Prioridad:** Must (P0) · **Horizonte:** H2 · **Actor (SPEC):** Coordinador · **Legacy:** HU-047  
**Depende de:** HU-BOD-001, HU-INV-001 · **RF:** RF-MOV-007 · **RN:** RN-EXI-003, RN-EXI-004 · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** crear una transferencia hacia otra zona o bodega **PARA** mover mercancía entre ámbitos con control de despacho y recepción.

```gherkin
@HU-MOV-003 @Must @M-09
Característica: HU-MOV-003 — Crear una transferencia entre zonas o bodegas
  # Criterio SPEC (1): Se indican origen, destino, referencias y cantidades.
  Escenario: C1 · Se indican origen, destino, referencias y cantidades
    Dado el Coordinador creando una transferencia
    Cuando indica origen, destino, referencias y cantidades
    Entonces la transferencia queda registrada con esos datos
  # Criterio SPEC (2): Al crearse, la existencia se reserva en origen `[RN-EXI-004]`.
  Escenario: C2 · Al crearse, la existencia se reserva en origen
    Dada una transferencia creada
    Cuando se consulta la existencia del origen
    Entonces la cantidad transferida figura como reservada
  # Criterio SPEC (3): Queda en estado pendiente de despacho.
  Escenario: C3 · Queda en estado pendiente de despacho
    Dada una transferencia recién creada
    Cuando se consulta su estado
    Entonces figura como pendiente de despacho
  # Criterio SPEC (4): Genera tarea para el Auxiliar del origen (M-20).
  Escenario: C4 · Genera tarea para el Auxiliar del origen
    Dada una transferencia pendiente de despacho
    Cuando se crea
    Entonces el sistema genera una tarea para el Auxiliar del origen
```

### HU-MOV-004 — Confirmar despacho y recepción de una transferencia escaneando

**Prioridad:** Must (P0) · **Horizonte:** H2 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-048  
**Depende de:** HU-MOV-003, HU-QRC-002, HU-TAR-001 · **RF:** RF-MOV-008, RF-MOV-009 · **RN:** RN-EXI-005 · **KPI:** KPI-15  
**Origen (SPEC):** `[RN-EXI-005]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** confirmar el despacho y la recepción de una transferencia escaneando **PARA** que quede claro quién la entregó y quién la recibió.

```gherkin
@HU-MOV-004 @Must @M-09
Característica: HU-MOV-004 — Confirmar despacho y recepción de una transferencia escaneando
  # Criterio SPEC (1): El despacho lo confirma el Auxiliar del origen escaneando.
  Escenario: C1 · El Auxiliar del origen confirma el despacho escaneando
    Dada una transferencia pendiente de despacho
    Cuando el Auxiliar del origen escanea la mercancía y confirma el despacho
    Entonces el despacho queda confirmado
  # Criterio SPEC (2): La transferencia pasa a en tránsito `[RN-EXI-005]`.
  Escenario: C2 · La transferencia pasa a en tránsito
    Dado un despacho confirmado
    Cuando se consulta el estado de la transferencia
    Entonces figura como en tránsito
  # Criterio SPEC (3): `[RN-EXI-005]` La existencia en tránsito no está disponible ni en origen ni en destino.
  Escenario: C3 · La existencia en tránsito no está disponible en origen ni en destino
    Dada una transferencia en tránsito
    Cuando se consulta el disponible del origen y del destino
    Entonces la existencia en tránsito no figura disponible en ninguno
  # Criterio SPEC (4): La recepción la confirma el Auxiliar del destino escaneando.
  Escenario: C4 · El Auxiliar del destino confirma la recepción escaneando
    Dada una transferencia en tránsito
    Cuando el Auxiliar del destino escanea la mercancía y confirma la recepción
    Entonces la recepción queda confirmada
  # Criterio SPEC (5): Ambos responsables quedan registrados.
  Escenario: C5 · Ambos responsables quedan registrados
    Dada una transferencia con despacho y recepción confirmados
    Cuando se consulta su registro
    Entonces figuran el responsable del despacho y el de la recepción
```

### HU-MOV-005 — Ser avisado si lo recibido no coincide con lo despachado

**Prioridad:** Should (P1) · **Horizonte:** H2 · **Actor (SPEC):** Jefe · **Legacy:** HU-049  
**Depende de:** HU-MOV-004 · **RF:** RF-MOV-010 · **RN:** RN-MOV-007 · **KPI:** KPI-15  
**Origen (SPEC):** `[RN-MOV-007]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que el sistema me avise si lo recibido no coincide con lo despachado **PARA** investigar antes de que se pierda el rastro.

```gherkin
@HU-MOV-005 @Should @M-09
Característica: HU-MOV-005 — Ser avisado si lo recibido no coincide con lo despachado
  # Criterio SPEC (1): El sistema compara despachado contra recibido `[RN-MOV-007]`.
  Escenario: C1 · El sistema compara despachado contra recibido
    Dada una transferencia con recepción registrada
    Cuando el sistema procesa la recepción
    Entonces compara lo despachado contra lo recibido
  # Criterio SPEC (2): Si lo recibido es menor, registra diferencia y abre novedad.
  Escenario: C2 · Si lo recibido es menor, registra diferencia y abre novedad
    Dada una recepción con cantidad menor a la despachada
    Cuando se compara
    Entonces el sistema registra la diferencia y abre una novedad
  # Criterio SPEC (3): Si lo recibido es mayor, rechaza la recepción y escala al Jefe.
  Escenario: C3 · Si lo recibido es mayor, rechaza la recepción y escala al Jefe
    Dada una recepción con cantidad mayor a la despachada
    Cuando se compara
    Entonces el sistema rechaza la recepción y escala al Jefe
  # Criterio SPEC (4): La transferencia no se completa hasta que el Jefe resuelva.
  Escenario: C4 · La transferencia no se completa hasta que el Jefe resuelva
    Dada una transferencia con diferencia
    Cuando el Jefe aún no ha resuelto
    Entonces la transferencia no pasa a completada
  # Criterio SPEC (5): La resolución queda documentada.
  Escenario: C5 · La resolución queda documentada
    Dada una diferencia resuelta por el Jefe
    Cuando se consulta la transferencia
    Entonces la resolución queda documentada
```

### HU-MOV-006 — Alertar una transferencia con demasiado tiempo en tránsito

**Prioridad:** Should (P1) · **Horizonte:** H2 · **Actor (SPEC):** Jefe / Coordinador · **Legacy:** HU-050  
**Depende de:** HU-MOV-004, HU-PAR-001 · **RF:** RF-MOV-011 · **RN:** RN-MOV-008, RN-MOV-009 · **KPI:** —  
**Origen (SPEC):** `[RN-MOV-008]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que el sistema me alerte si una transferencia lleva demasiado tiempo en tránsito **PARA** que no se pierda mercancía en el camino.

```gherkin
@HU-MOV-006 @Should @M-09
Característica: HU-MOV-006 — Alertar una transferencia con demasiado tiempo en tránsito
  # Criterio SPEC (1): El tiempo máximo en tránsito es configurable `[RN-MOV-008]`.
  Escenario: C1 · El tiempo máximo en tránsito es configurable
    Dado el Administrador en Parámetros y Configuración
    Cuando define el tiempo máximo en tránsito
    Entonces el sistema lo aplica a las transferencias
  # Criterio SPEC (2): Al superarlo, se genera alerta dirigida al Jefe.
  Escenario: C2 · Al superarlo se genera alerta dirigida al Jefe
    Dada una transferencia que supera el tiempo máximo en tránsito
    Cuando el sistema evalúa la condición
    Entonces genera una alerta dirigida al Jefe
  # Criterio SPEC (3): La alerta identifica la transferencia, su contenido y su responsable de despacho.
  Escenario: C3 · La alerta identifica transferencia, contenido y responsable de despacho
    Dada una alerta de tránsito prolongado
    Cuando el Jefe la abre
    Entonces identifica la transferencia, su contenido y su responsable de despacho
  # Criterio SPEC (4): La alerta se cierra al completarse o cancelarse la transferencia.
  Escenario: C4 · La alerta se cierra al completarse o cancelarse la transferencia
    Dada una alerta de tránsito prolongado vigente
    Cuando la transferencia se completa o se cancela
    Entonces la alerta se cierra
```

### HU-MOV-007 — Cancelar una transferencia

**Prioridad:** Should (P1) · **Horizonte:** H2 · **Actor (SPEC):** Jefe · **Legacy:** HU-051  
**Depende de:** HU-MOV-003, HU-MOV-004 · **RF:** RF-MOV-011 · **RN:** RN-MOV-008, RN-MOV-009 · **KPI:** —  
**Origen (SPEC):** `[RN-MOV-009]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** poder cancelar una transferencia **PARA** resolver situaciones donde la mercancía no puede llegar a su destino.

```gherkin
@HU-MOV-007 @Should @M-09
Característica: HU-MOV-007 — Cancelar una transferencia
  # Criterio SPEC (1): Antes del despacho, el Coordinador puede cancelar y la reserva se libera `[RN-MOV-009]`.
  Escenario: C1 · Antes del despacho el Coordinador cancela y se libera la reserva
    Dada una transferencia pendiente de despacho
    Cuando el Coordinador la cancela
    Entonces la reserva se libera
  # Criterio SPEC (2): En tránsito, solo el Jefe puede cancelar, y se genera un movimiento de retorno al origen.
  Escenario: C2 · En tránsito solo el Jefe cancela y se genera un retorno al origen
    Dada una transferencia en tránsito
    Cuando el Jefe la cancela
    Entonces se genera un movimiento de retorno al origen
    Y ningún otro rol puede cancelarla
  # Criterio SPEC (3): La cancelación exige motivo.
  Escenario: C3 · La cancelación exige motivo
    Dada una cancelación de transferencia
    Cuando se intenta confirmar sin motivo
    Entonces el sistema no la permite
  # Criterio SPEC (4): Queda en la bitácora.
  Escenario: C4 · La cancelación queda en bitácora
    Dada una transferencia cancelada
    Cuando se completa la cancelación
    Entonces el evento queda en la bitácora
```

### HU-MOV-008 — Elegir en pantalla la pieza que se ubica o se mueve

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-106  
**Depende de:** HU-ENT-009, HU-MOV-001 · **RF:** RF-MOV-012 · **RN:** RN-MOV-004, RN-MOV-010, RN-MOV-011, RN-MOV-012 · **KPI:** —  
**Origen (SPEC):** `[F-4]` `[RN-MOV-011*]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** elegir en pantalla la pieza que estoy ubicando o moviendo, después de escanear **PARA** que el sistema sepa exactamente qué pieza cambió de lugar aunque haya varias del mismo lote en el mismo estante.

```gherkin
@HU-MOV-008 @Must @M-09
Característica: HU-MOV-008 — Elegir en pantalla la pieza que se ubica o se mueve
  # Criterio SPEC (1): Tras escanear el QR del SKU + Lote, el sistema muestra las piezas de ese lote y el Auxiliar selecciona la que mueve `[F-4]`.
  Escenario: C1 · Tras escanear se muestran las piezas del lote y se selecciona una
    Dado un Auxiliar que escanea el QR de un SKU + Lote
    Cuando el sistema resuelve el lote
    Entonces muestra las piezas del lote y el Auxiliar selecciona la que mueve
  # Criterio SPEC (2): Con varias piezas del mismo lote en la ubicación de origen, la ubicación actúa como filtro de verificación: solo se ofrecen las piezas que el sistema registra allí.
  Escenario: C2 · La ubicación filtra las piezas ofrecidas
    Dadas varias piezas del mismo lote en la ubicación de origen
    Cuando el Auxiliar elige la ubicación de origen
    Entonces el sistema ofrece solo las piezas que registra en esa ubicación
  # Criterio SPEC (3): No se confirma un movimiento sin pieza seleccionada `[RN-MOV-011]`.
  Escenario: C3 · No se confirma un movimiento sin pieza seleccionada
    Dado un movimiento en registro
    Cuando el Auxiliar intenta confirmarlo sin seleccionar pieza
    Entonces el sistema no lo confirma
  # Criterio SPEC (4): Aplica al movimiento interno y a la primera ubicación desde recepción `[RN-MOV-010]`.
  Escenario: C4 · Aplica al movimiento interno y a la primera ubicación
    Dada una primera ubicación desde recepción o un movimiento interno
    Cuando el Auxiliar lo registra
    Entonces el sistema exige la selección de la pieza en ambos casos
  # Criterio SPEC (5): El movimiento queda en el kardex con la pieza.
  Escenario: C5 · El movimiento queda en el kardex con la pieza
    Dado un movimiento confirmado
    Cuando se consulta el kardex
    Entonces el movimiento muestra la pieza afectada
  # Criterio SPEC (6): La existencia total no cambia `[RN-MOV-004]`.
  Escenario: C6 · La existencia total no cambia
    Dado un movimiento interno de una pieza
    Cuando se confirma
    Entonces la existencia total no cambia y solo cambia su distribución
```

### HU-MOV-009 — Que un movimiento interno interrumpido quede en tránsito

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe · **Legacy:** HU-111  
**Depende de:** HU-MOV-001, HU-ALE-001 · **RF:** RF-MOV-013 · **RN:** RN-MOV-006 · **KPI:** —  
**Origen (SPEC):** `[RN-MOV-006]` `[DEC-06]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que un movimiento interno interrumpido quede en tránsito y se me avise si tarda demasiado **PARA** no perder el rastro de la mercancía que quedó a medio camino.

```gherkin
@HU-MOV-009 @Should @M-09
Característica: HU-MOV-009 — Que un movimiento interno interrumpido quede en tránsito
  # Criterio SPEC (1): Un movimiento interno que se inicia y no se cierra queda en estado en tránsito `[RN-MOV-006]`.
  Escenario: C1 · Un movimiento interno que no se cierra queda en tránsito
    Dado un movimiento interno iniciado
    Cuando no se cierra
    Entonces queda en estado en tránsito
  # Criterio SPEC (2): La existencia en tránsito no está disponible ni en el origen ni en el destino.
  Escenario: C2 · La existencia en tránsito no está disponible en origen ni en destino
    Dado un movimiento interno en tránsito
    Cuando se consulta la existencia
    Entonces no figura como disponible ni en el origen ni en el destino
  # Criterio SPEC (3): Si el tiempo en tránsito supera el máximo configurado, el sistema genera una alerta al Jefe.
  Escenario: C3 · Supera el tiempo máximo y se alerta al Jefe
    Dado un movimiento interno en tránsito
    Cuando supera el tiempo máximo configurado
    Entonces el sistema genera una alerta al Jefe
  # Criterio SPEC (4): Los movimientos en tránsito se listan en el cierre de la jornada `[PN-14]`.
  Escenario: C4 · Se lista en el cierre de la jornada
    Dado un movimiento interno en tránsito al terminar la jornada
    Cuando se consolida el cierre
    Entonces figura entre los pendientes
```


## 5.12 M-10 · Ajustes de Inventario (dominio AJU)

### HU-AJU-001 — Solicitar un ajuste cuando la existencia no coincide

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador · **Legacy:** HU-052  
**Depende de:** HU-INV-001, HU-PAR-002 · **RF:** RF-AJU-001, RF-AJU-002, RF-AJU-003, RF-AJU-007 · **RN:** RN-AJU-003, RN-EXI-001, RN-INT-002, RN-INT-004 · **KPI:** KPI-08, KPI-14  
**Origen (SPEC):** `[MON §8.2]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** solicitar un ajuste cuando lo que hay no coincide con lo que dice el sistema **PARA** que el registro refleje la realidad, dejando constancia de por qué.

```gherkin
@HU-AJU-001 @Must @M-10
Característica: HU-AJU-001 — Solicitar un ajuste cuando la existencia no coincide
  # Criterio SPEC (1): Se ingresa la existencia física observada; el sistema calcula la diferencia.
  Escenario: C1 · Se ingresa la existencia física observada y se calcula la diferencia
    Dada una unidad cuya existencia registrada difiere de la física
    Cuando el Coordinador ingresa la existencia física observada
    Entonces el sistema calcula la diferencia y su sentido
  # Criterio SPEC (2): `[RN-AJU-003]` El motivo tipificado es obligatorio; el texto libre no lo sustituye.
  Escenario: C2 · El motivo tipificado es obligatorio y el texto libre no lo sustituye
    Dada una solicitud de ajuste con solo texto libre
    Cuando se intenta enviar sin motivo tipificado
    Entonces el sistema no la acepta
  # Criterio SPEC (3): Se puede adjuntar observación y evidencia.
  Escenario: C3 · Se puede adjuntar observación y evidencia
    Dada una solicitud de ajuste en preparación
    Cuando el Coordinador adjunta observación y evidencia
    Entonces la solicitud las conserva
  # Criterio SPEC (4): La solicitud queda pendiente de aprobación.
  Escenario: C4 · La solicitud queda pendiente de aprobación
    Dada una solicitud de ajuste enviada
    Cuando se consulta su estado
    Entonces figura pendiente de aprobación
  # Criterio SPEC (5): La existencia no cambia hasta la aprobación.
  Escenario: C5 · La existencia no cambia hasta la aprobación
    Dada una solicitud de ajuste pendiente
    Cuando se consulta la existencia de la unidad
    Entonces la existencia permanece sin cambios
```

### HU-AJU-002 — Aprobar o rechazar ajustes solicitados

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Administrador · **Legacy:** HU-053  
**Depende de:** HU-AJU-001, HU-USR-001 · **RF:** RF-AJU-005, RF-AJU-007, RF-AJU-008 · **RN:** RN-AJU-001, RN-AJU-006, RN-INT-002, RN-INT-004 · **KPI:** KPI-22  
**Origen (SPEC):** `[RN-AJU-001]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** aprobar o rechazar los ajustes solicitados **PARA** que nadie modifique el inventario por su cuenta.

```gherkin
@HU-AJU-002 @Must @M-10
Característica: HU-AJU-002 — Aprobar o rechazar ajustes solicitados
  # Criterio SPEC (1): La pantalla muestra unidad, diferencia, motivo, solicitante y evidencia.
  Escenario: C1 · La pantalla muestra unidad, diferencia, motivo, solicitante y evidencia
    Dada una solicitud de ajuste pendiente
    Cuando el aprobador la abre
    Entonces ve la unidad, la diferencia, el motivo, el solicitante y la evidencia
  # Criterio SPEC (2): `[RN-AJU-001]` El sistema impide aprobar un ajuste que uno mismo solicitó, escalando al nivel superior.
  Escenario: C2 · Nadie aprueba un ajuste que él mismo solicitó
    Dado un ajuste solicitado por el mismo usuario que sería su aprobador
    Cuando intenta aprobarlo
    Entonces el sistema lo impide y escala la solicitud al nivel superior
  # Criterio SPEC (3): El rechazo exige justificación.
  Escenario: C3 · El rechazo exige justificación
    Dada una solicitud de ajuste que el aprobador rechaza
    Cuando confirma el rechazo sin justificación
    Entonces el sistema no lo permite
  # Criterio SPEC (4): Al aprobar, se genera el movimiento y cambia la existencia.
  Escenario: C4 · Al aprobar se genera el movimiento y cambia la existencia
    Dada una solicitud de ajuste aprobada
    Cuando se aplica
    Entonces el sistema genera el movimiento de ajuste y la existencia cambia
  # Criterio SPEC (5): El solicitante es notificado del resultado.
  Escenario: C5 · El solicitante es notificado del resultado
    Dada una solicitud de ajuste aprobada o rechazada
    Cuando se resuelve
    Entonces el solicitante recibe la notificación del resultado
```

### HU-AJU-003 — Requerir aprobación del Administrador para ajustes grandes

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-054  
**Depende de:** HU-AJU-001, HU-PAR-001 · **RF:** RF-AJU-004 · **RN:** RN-AJU-002 · **KPI:** KPI-22  
**Origen (SPEC):** `[RN-AJU-002]`

**Historia.** **COMO** Administrador **QUIERO** que los ajustes grandes requieran mi aprobación **PARA** mantener control sobre los cambios de inventario de mayor impacto.

```gherkin
@HU-AJU-003 @Must @M-10
Característica: HU-AJU-003 — Requerir aprobación del Administrador para ajustes grandes
  # Criterio SPEC (1): El umbral que separa ajuste menor de mayor es configurable `[RN-AJU-002]`.
  Escenario: C1 · El umbral entre ajuste menor y mayor es configurable
    Dado el Administrador en Parámetros y Configuración
    Cuando define el umbral que separa ajuste menor de mayor
    Entonces el umbral queda configurado
  # Criterio SPEC (2): Bajo el umbral, aprueba el Jefe.
  Escenario: C2 · Bajo el umbral aprueba el Jefe
    Dado un ajuste con magnitud bajo el umbral
    Cuando se envía a aprobación
    Entonces le corresponde aprobarlo al Jefe
  # Criterio SPEC (3): Sobre el umbral, aprueba el Administrador.
  Escenario: C3 · Sobre el umbral aprueba el Administrador
    Dado un ajuste con magnitud sobre el umbral
    Cuando se envía a aprobación
    Entonces le corresponde aprobarlo al Administrador
  # Criterio SPEC (4): El sistema enruta automáticamente.
  Escenario: C4 · El sistema enruta automáticamente
    Dado un ajuste solicitado
    Cuando el sistema lo clasifica
    Entonces lo enruta automáticamente al aprobador que corresponde
  # Criterio SPEC (5): El umbral aplicado queda registrado en el ajuste.
  Escenario: C5 · El umbral aplicado queda registrado en el ajuste
    Dado un ajuste clasificado
    Cuando se consulta el ajuste después de un cambio posterior del umbral
    Entonces conserva el umbral que se aplicó en su momento
```

### HU-AJU-004 — Impedir que un ajuste deje la existencia en negativo

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Todos · **Legacy:** HU-055  
**Depende de:** HU-AJU-001 · **RF:** RF-AJU-006 · **RN:** RN-EXI-001 · **KPI:** —  
**Origen (SPEC):** `[RN-EXI-001]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que ningún ajuste pueda dejar la existencia en negativo **PARA** que el inventario nunca muestre una cifra imposible.

```gherkin
@HU-AJU-004 @Must @M-10
Característica: HU-AJU-004 — Impedir que un ajuste deje la existencia en negativo
  # Criterio SPEC (1): `[RN-EXI-001]` El sistema rechaza todo ajuste que resulte en existencia negativa, sin excepción ni autorización posible.
  Escenario: C1 · Se rechaza todo ajuste que resulte en existencia negativa
    Dado un ajuste que dejaría la existencia por debajo de cero
    Cuando se intenta solicitar o aprobar
    Entonces el sistema lo rechaza sin excepción ni autorización posible
  # Criterio SPEC (2): El mensaje explica la existencia actual y la diferencia solicitada.
  Escenario: C2 · El mensaje explica la existencia actual y la diferencia solicitada
    Dado un ajuste rechazado por dejar existencia negativa
    Cuando el sistema informa el resultado
    Entonces el mensaje muestra la existencia actual y la diferencia solicitada
  # Criterio SPEC (3): El rechazo queda registrado.
  Escenario: C3 · El rechazo queda registrado
    Dado un ajuste rechazado por existencia negativa
    Cuando se completa el rechazo
    Entonces el rechazo queda registrado
  # Criterio SPEC (4): Esta regla no es configurable.
  Escenario: C4 · La regla no es configurable
    Dado el Administrador en Parámetros y Configuración
    Cuando busca desactivar o modificar la prohibición de existencia negativa
    Entonces el sistema no la ofrece como parametrizable
```

### HU-AJU-005 — Ser avisado de ajustes recurrentes sobre una misma referencia

**Prioridad:** Should (P1) · **Horizonte:** H2 · **Actor (SPEC):** Jefe / Auditor · **Legacy:** HU-056  
**Depende de:** HU-AJU-001, HU-ALE-003 · **RF:** RF-AJU-009 · **RN:** RN-AJU-004 · **KPI:** —  
**Origen (SPEC):** `[RN-AJU-004]` `[DC-07]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que el sistema me avise si una misma referencia se ajusta demasiadas veces **PARA** detectar un problema de proceso o algo peor.

```gherkin
@HU-AJU-005 @Should @M-10
Característica: HU-AJU-005 — Ser avisado de ajustes recurrentes sobre una misma referencia
  # Criterio SPEC (1): El sistema cuenta ajustes por unidad de inventario en una ventana configurable `[RN-AJU-004]`.
  Escenario: C1 · Se cuentan ajustes por unidad en una ventana configurable
    Dada una ventana de tiempo y un umbral configurados
    Cuando se aplican ajustes sobre una misma unidad de inventario
    Entonces el sistema cuenta los ajustes de esa unidad dentro de la ventana
  # Criterio SPEC (2): Al superar el umbral, genera alerta dirigida al Jefe y al Auditor.
  Escenario: C2 · Al superar el umbral se alerta al Jefe y al Auditor
    Dada una unidad cuyos ajustes superan el umbral en la ventana
    Cuando el sistema evalúa la regla
    Entonces genera una alerta dirigida al Jefe y al Auditor
  # Criterio SPEC (3): La alerta lista los ajustes involucrados con solicitante y aprobador.
  Escenario: C3 · La alerta lista los ajustes con solicitante y aprobador
    Dada una alerta de ajustes recurrentes
    Cuando el destinatario la abre
    Entonces lista los ajustes involucrados con su solicitante y su aprobador
  # Criterio SPEC (4): `[DC-07]` La detección es por regla y umbral, no por modelo predictivo.
  Escenario: C4 · La detección es por regla y umbral, no por modelo predictivo
    Dada la generación de la alerta de ajustes recurrentes
    Cuando el sistema la evalúa
    Entonces lo hace únicamente por regla explícita y umbral configurado
```

### HU-AJU-006 — Consultar todos los ajustes de un período

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auditor / Jefe · **Legacy:** HU-057  
**Depende de:** HU-AJU-001 · **RF:** RF-AJU-010 · **RN:** — · **KPI:** KPI-14  
**Origen (SPEC):** `[MON §7.1]`

**Historia.** **COMO** Auditor **QUIERO** consultar todos los ajustes de un período con su motivo, solicitante y aprobador **PARA** verificar que cada modificación del inventario está justificada.

```gherkin
@HU-AJU-006 @Should @M-10
Característica: HU-AJU-006 — Consultar todos los ajustes de un período
  # Criterio SPEC (1): Filtro por período, motivo, solicitante, aprobador y referencia.
  Escenario: C1 · Filtro por período, motivo, solicitante, aprobador y referencia
    Dados varios ajustes registrados
    Cuando el Auditor aplica filtros
    Entonces el sistema muestra solo los ajustes que cumplen los filtros
  # Criterio SPEC (2): Muestra cantidad ajustada, sentido y evidencia adjunta.
  Escenario: C2 · Muestra cantidad ajustada, sentido y evidencia adjunta
    Dado un ajuste consultado
    Cuando se presenta su detalle
    Entonces muestra la cantidad ajustada, su sentido y la evidencia adjunta
  # Criterio SPEC (3): Permite abrir el kardex de la unidad afectada.
  Escenario: C3 · Permite abrir el kardex de la unidad afectada
    Dado un ajuste consultado
    Cuando el Auditor elige abrir el kardex
    Entonces el sistema muestra el kardex de la unidad afectada
  # Criterio SPEC (4): Identifica ajustes sin evidencia cuando el motivo la exigía.
  Escenario: C4 · Identifica ajustes sin evidencia cuando el motivo la exigía
    Dado un ajuste con motivo que exige evidencia y sin evidencia adjunta
    Cuando se consulta el listado
    Entonces el sistema lo identifica
  # Criterio SPEC (5): Exportable.
  Escenario: C5 · La consulta es exportable
    Dado un listado de ajustes filtrado
    Cuando el usuario solicita exportarlo
    Entonces el sistema entrega la exportación
```


## 5.13 M-11 · Conteos (dominio CNT)

### HU-CNT-001 — Programar un conteo cíclico sin parar la bodega

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador · **Legacy:** HU-058  
**Depende de:** HU-BOD-001, HU-CAT-001, HU-TAR-001 · **RF:** RF-CNT-001, RF-CNT-002, RF-CNT-003, RF-CNT-005 · **RN:** RN-CNT-001 · **KPI:** KPI-03  
**Origen (SPEC):** `[NUEVO]` `[D-05]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** programar un conteo de unas cuantas ubicaciones **PARA** verificar el inventario sin tener que parar la bodega.

```gherkin
@HU-CNT-001 @Should @M-11
Característica: HU-CNT-001 — Programar un conteo cíclico sin parar la bodega
  # Criterio SPEC (1): El ámbito se define por ubicaciones, referencias o categorías.
  Escenario: C1 · El ámbito se define por ubicaciones, referencias o categorías
    Dado el Coordinador programando un conteo cíclico
    Cuando define el ámbito por ubicaciones, referencias o categorías
    Entonces el conteo queda programado con ese ámbito
  # Criterio SPEC (2): `[D-05]` La operación de la bodega no se bloquea durante un conteo cíclico.
  Escenario: C2 · La operación de la bodega no se bloquea durante el conteo cíclico
    Dado un conteo cíclico en ejecución
    Cuando otros usuarios registran movimientos
    Entonces el sistema no bloquea la operación de la bodega
  # Criterio SPEC (3): El sistema congela la existencia teórica del ámbito `[RN-CNT-001]`.
  Escenario: C3 · El sistema congela la existencia teórica del ámbito
    Dado un conteo cíclico que inicia
    Cuando el sistema lo pone en ejecución
    Entonces congela la existencia teórica del ámbito
  # Criterio SPEC (4): Genera tareas y las asigna.
  Escenario: C4 · Genera tareas y las asigna
    Dado un conteo cíclico programado
    Cuando inicia
    Entonces el sistema genera las tareas de conteo y las asigna
  # Criterio SPEC (5): El conteo queda en estado en ejecución.
  Escenario: C5 · El conteo queda en estado en ejecución
    Dado un conteo con tareas asignadas
    Cuando se consulta su estado
    Entonces figura en ejecución
```

### HU-CNT-002 — Contar sin ver la cantidad esperada

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-059  
**Depende de:** HU-CNT-001, HU-QRC-002 · **RF:** RF-CNT-006 · **RN:** RN-CNT-002 · **KPI:** —  
**Origen (SPEC):** `[RN-CNT-002]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** contar lo que hay en una ubicación sin que el sistema me diga antes cuánto debería haber **PARA** que mi conteo sea real y no una confirmación de lo que ya dice el sistema.

```gherkin
@HU-CNT-002 @Should @M-11
Característica: HU-CNT-002 — Contar sin ver la cantidad esperada
  # Criterio SPEC (1): `[RN-CNT-002]` La cantidad esperada no se muestra al contador antes de registrar su conteo, en ninguna circunstancia.
  Escenario: C1 · La cantidad esperada no se muestra antes de contar
    Dado un Auxiliar con una tarea de conteo
    Cuando abre la tarea antes de registrar su conteo
    Entonces el sistema no le muestra la cantidad esperada
  # Criterio SPEC (2): El Auxiliar escanea la ubicación e ingresa lo contado.
  Escenario: C2 · Escanea la ubicación e ingresa lo contado
    Dada una tarea de conteo asignada
    Cuando el Auxiliar escanea la ubicación e ingresa la cantidad contada
    Entonces el sistema registra el conteo
  # Criterio SPEC (3): Después de registrar, tampoco se le muestra la diferencia.
  Escenario: C3 · Después de registrar tampoco se muestra la diferencia
    Dado un conteo registrado por el Auxiliar
    Cuando termina el registro
    Entonces el sistema no le muestra la diferencia respecto de lo esperado
  # Criterio SPEC (4): Puede corregir su propio registro antes de confirmar la tarea.
  Escenario: C4 · Puede corregir su propio registro antes de confirmar la tarea
    Dado un registro de conteo aún no confirmado
    Cuando el Auxiliar lo corrige
    Entonces el sistema conserva la corrección antes de confirmar la tarea
```

### HU-CNT-003 — Que los movimientos durante el conteo no alteren la base de comparación

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Sistema / Coordinador · **Legacy:** HU-060  
**Depende de:** HU-CNT-001 · **RF:** RF-CNT-003, RF-CNT-004 · **RN:** RN-CNT-001 · **KPI:** —  
**Origen (SPEC):** `[RN-CNT-001]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** que los movimientos que ocurran durante el conteo no alteren la base de comparación **PARA** que la diferencia detectada sea real.

```gherkin
@HU-CNT-003 @Should @M-11
Característica: HU-CNT-003 — Que los movimientos durante el conteo no alteren la base de comparación
  # Criterio SPEC (1): `[RN-CNT-001]` La existencia teórica congelada no cambia por movimientos posteriores al congelamiento.
  Escenario: C1 · La existencia teórica congelada no cambia por movimientos posteriores
    Dada una existencia teórica congelada
    Cuando ocurren movimientos posteriores al congelamiento
    Entonces la existencia teórica congelada no cambia
  # Criterio SPEC (2): Los movimientos ocurridos durante el conteo se listan en la conciliación.
  Escenario: C2 · Los movimientos durante el conteo se listan en la conciliación
    Dados movimientos ocurridos durante un conteo
    Cuando se abre la conciliación
    Entonces los movimientos aparecen listados
  # Criterio SPEC (3): El Coordinador puede ver qué movimientos afectaron el ámbito.
  Escenario: C3 · El Coordinador ve qué movimientos afectaron el ámbito
    Dados movimientos ocurridos sobre el ámbito contado
    Cuando el Coordinador revisa la conciliación
    Entonces puede ver qué movimientos afectaron el ámbito
  # Criterio SPEC (4): La conciliación los considera antes de generar ajustes.
  Escenario: C4 · La conciliación los considera antes de generar ajustes
    Dada una conciliación con movimientos concurrentes
    Cuando se preparan los ajustes derivados
    Entonces la conciliación considera esos movimientos antes de generarlos
```

### HU-CNT-004 — Exigir segundo conteo por otra persona ante diferencias grandes

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador / Jefe · **Legacy:** HU-061  
**Depende de:** HU-CNT-001, HU-PAR-001 · **RF:** RF-CNT-007, RF-CNT-008, RF-CNT-009 · **RN:** RN-CNT-001, RN-CNT-003 · **KPI:** KPI-01, KPI-04, KPI-06, KPI-08  
**Origen (SPEC):** `[RN-CNT-003]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** que una diferencia grande obligue a un segundo conteo por otra persona **PARA** descartar un error de quien contó.

```gherkin
@HU-CNT-004 @Should @M-11
Característica: HU-CNT-004 — Exigir segundo conteo por otra persona ante diferencias grandes
  # Criterio SPEC (1): El umbral de tolerancia es configurable `[RN-CNT-003]`.
  Escenario: C1 · El umbral de tolerancia es configurable
    Dado el Administrador en Parámetros y Configuración
    Cuando define el umbral de tolerancia de conteo
    Entonces el umbral queda configurado
  # Criterio SPEC (2): Al superarlo, el sistema genera automáticamente una tarea de segundo conteo.
  Escenario: C2 · Al superarlo se genera automáticamente el segundo conteo
    Dada una línea de conteo con diferencia sobre el umbral de tolerancia
    Cuando el sistema la evalúa
    Entonces genera automáticamente una tarea de segundo conteo
  # Criterio SPEC (3): `[RN-CNT-003]` El segundo conteo lo ejecuta obligatoriamente una persona distinta a la primera.
  Escenario: C3 · El segundo conteo lo ejecuta una persona distinta a la primera
    Dada una tarea de segundo conteo
    Cuando se intenta asignar a quien hizo el primer conteo
    Entonces el sistema lo impide y exige una persona distinta
  # Criterio SPEC (4): Si el segundo también difiere, escala al Jefe.
  Escenario: C4 · Si el segundo también difiere, escala al Jefe
    Dado un segundo conteo que también difiere de lo esperado
    Cuando se registra
    Entonces el sistema escala al Jefe
  # Criterio SPEC (5): Ambos conteos quedan registrados.
  Escenario: C5 · Ambos conteos quedan registrados
    Dado un primer y un segundo conteo
    Cuando se consulta la línea
    Entonces quedan registrados ambos conteos
```

### HU-CNT-005 — Revisar diferencias y decidir qué se ajusta antes de cerrar

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe · **Legacy:** HU-062  
**Depende de:** HU-CNT-001, HU-CNT-002, HU-CNT-004, HU-AJU-001 · **RF:** RF-CNT-007, RF-CNT-010 · **RN:** RN-CNT-001, RN-CNT-003, RN-CNT-004 · **KPI:** KPI-01, KPI-04, KPI-08  
**Origen (SPEC):** `[RN-CNT-004]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** revisar las diferencias y decidir qué se ajusta antes de cerrar el conteo **PARA** que el inventario no se modifique automáticamente sin criterio.

```gherkin
@HU-CNT-005 @Should @M-11
Característica: HU-CNT-005 — Revisar diferencias y decidir qué se ajusta antes de cerrar
  # Criterio SPEC (1): `[RN-CNT-004]` Solo el Jefe cierra un conteo.
  Escenario: C1 · Solo el Jefe cierra un conteo
    Dado un conteo listo para cerrar
    Cuando un usuario distinto del Jefe intenta cerrarlo
    Entonces el sistema lo impide
  # Criterio SPEC (2): Quien ejecutó el conteo no puede cerrarlo `[RN-CNT-003]`.
  Escenario: C2 · Quien ejecutó el conteo no puede cerrarlo
    Dado un conteo ejecutado por un usuario
    Cuando ese usuario intenta cerrarlo
    Entonces el sistema lo impide
  # Criterio SPEC (3): El Jefe ve el consolidado de diferencias por línea.
  Escenario: C3 · El Jefe ve el consolidado de diferencias por línea
    Dado un conteo en conciliación
    Cuando el Jefe lo abre
    Entonces ve el consolidado de diferencias por línea
  # Criterio SPEC (4): Puede decidir ajustar, no ajustar o recontar por línea.
  Escenario: C4 · Puede decidir ajustar, no ajustar o recontar por línea
    Dada una línea con diferencia
    Cuando el Jefe decide sobre ella
    Entonces puede elegir ajustar, no ajustar o recontar
  # Criterio SPEC (5): Las líneas ajustadas generan ajustes con motivo derivado del conteo.
  Escenario: C5 · Las líneas ajustadas generan ajustes con motivo derivado del conteo
    Dadas líneas que el Jefe decide ajustar
    Cuando cierra el conteo
    Entonces se generan ajustes con motivo derivado del conteo
  # Criterio SPEC (6): Un conteo cerrado no se reabre.
  Escenario: C6 · Un conteo cerrado no se reabre
    Dado un conteo cerrado
    Cuando se intenta reabrirlo
    Entonces el sistema no lo permite
```

### HU-CNT-006 — Programar un conteo general con bloqueo de movimientos

**Prioridad:** Should (P1) · **Horizonte:** H2 · **Actor (SPEC):** Jefe · **Legacy:** HU-063  
**Depende de:** HU-CNT-001 · **RF:** RF-CNT-011 · **RN:** RN-CNT-006 · **KPI:** KPI-02  
**Origen (SPEC):** `[RN-CNT-006]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** programar un conteo general con bloqueo de movimientos **PARA** obtener una fotografía completa y confiable del inventario.

```gherkin
@HU-CNT-006 @Should @M-11
Característica: HU-CNT-006 — Programar un conteo general con bloqueo de movimientos
  # Criterio SPEC (1): Se define fecha y hora de corte.
  Escenario: C1 · Se define fecha y hora de corte
    Dado el Jefe programando un conteo general
    Cuando define la fecha y hora de corte
    Entonces el conteo queda programado con ese corte
  # Criterio SPEC (2): El sistema notifica anticipadamente a todos los usuarios.
  Escenario: C2 · Se notifica anticipadamente a todos los usuarios
    Dado un conteo general programado
    Cuando se acerca el corte
    Entonces el sistema notifica anticipadamente a todos los usuarios
  # Criterio SPEC (3): `[RN-CNT-006]` Al llegar el corte, el registro de movimientos se bloquea.
  Escenario: C3 · Al llegar el corte se bloquea el registro de movimientos
    Dado un conteo general programado
    Cuando llega la hora de corte
    Entonces el sistema bloquea el registro de movimientos
  # Criterio SPEC (4): Solo el Jefe puede autorizar un movimiento de excepción, que queda marcado.
  Escenario: C4 · Solo el Jefe autoriza un movimiento de excepción, que queda marcado
    Dado un bloqueo de movimientos vigente
    Cuando surge la necesidad de un movimiento urgente
    Entonces solo el Jefe puede autorizarlo y queda marcado como excepción
  # Criterio SPEC (5): Al cerrar, el registro se desbloquea.
  Escenario: C5 · Al cerrar se desbloquea el registro
    Dado un conteo general que se cierra
    Cuando el cierre se completa
    Entonces el registro de movimientos se desbloquea
```

### HU-CNT-007 — Impedir cerrar un conteo general con ubicaciones sin contar

**Prioridad:** Should (P1) · **Horizonte:** H2 · **Actor (SPEC):** Jefe · **Legacy:** HU-064  
**Depende de:** HU-CNT-006 · **RF:** RF-CNT-012 · **RN:** RN-CNT-007 · **KPI:** KPI-03  
**Origen (SPEC):** `[RN-CNT-007]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que el sistema no me deje cerrar un conteo general con ubicaciones sin contar **PARA** que la fotografía sea realmente completa.

```gherkin
@HU-CNT-007 @Should @M-11
Característica: HU-CNT-007 — Impedir cerrar un conteo general con ubicaciones sin contar
  # Criterio SPEC (1): `[RN-CNT-007]` El sistema impide el cierre mientras existan ubicaciones del ámbito sin cubrir.
  Escenario: C1 · Se impide el cierre mientras haya ubicaciones sin cubrir
    Dado un conteo general con ubicaciones del ámbito sin cubrir
    Cuando el Jefe intenta cerrarlo
    Entonces el sistema lo impide
  # Criterio SPEC (2): Lista las ubicaciones faltantes.
  Escenario: C2 · Lista las ubicaciones faltantes
    Dado un conteo general con ubicaciones sin cubrir
    Cuando el Jefe intenta cerrarlo
    Entonces el sistema lista las ubicaciones faltantes
  # Criterio SPEC (3): Permite excluir una ubicación solo con justificación registrada.
  Escenario: C3 · Permite excluir una ubicación solo con justificación registrada
    Dada una ubicación sin cubrir
    Cuando el Jefe la excluye con una justificación registrada
    Entonces el sistema acepta la exclusión
  # Criterio SPEC (4): La cobertura alcanzada queda documentada en el conteo.
  Escenario: C4 · La cobertura alcanzada queda documentada
    Dado un conteo general cerrado
    Cuando se consulta el conteo
    Entonces la cobertura alcanzada queda documentada
```

### HU-CNT-008 — Conocer la exactitud del inventario después de cada conteo

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Administrador · **Legacy:** HU-065  
**Depende de:** HU-CNT-005 · **RF:** RF-CNT-013, RF-REP-003, RF-REP-008 · **RN:** — · **KPI:** KPI-01, KPI-02  
**Origen (SPEC):** `[MON §8.2]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** conocer la exactitud del inventario después de cada conteo **PARA** demostrar si estamos mejorando.

```gherkin
@HU-CNT-008 @Should @M-11
Característica: HU-CNT-008 — Conocer la exactitud del inventario después de cada conteo
  # Criterio SPEC (1): Al cerrar, el sistema calcula la exactitud del ámbito contado (KPI-01).
  Escenario: C1 · Al cerrar, se calcula la exactitud del ámbito contado
    Dado un conteo que se cierra
    Cuando se completa el cierre
    Entonces el sistema calcula la exactitud del ámbito contado
  # Criterio SPEC (2): La expresa como porcentaje de líneas conformes sobre líneas contadas.
  Escenario: C2 · Se expresa como porcentaje de líneas conformes sobre líneas contadas
    Dada la exactitud calculada
    Cuando se presenta el resultado
    Entonces se expresa como porcentaje de líneas conformes sobre líneas contadas
  # Criterio SPEC (3): La almacena históricamente para comparar entre conteos.
  Escenario: C3 · Se almacena históricamente para comparar entre conteos
    Dada una exactitud calculada
    Cuando se guarda
    Entonces queda almacenada históricamente para comparar entre conteos
  # Criterio SPEC (4): `[MON §8.2]` Este es el indicador con el que el proyecto demostrará su impacto.
  Escenario: C4 · Es el indicador con el que el proyecto demostrará su impacto
    Dado el indicador de exactitud del inventario
    Cuando se consulta
    Entonces está disponible como indicador central del compromiso de valor del producto
  # Criterio SPEC (5): Es exportable para la herramienta analítica `[DC-06]`.
  Escenario: C5 · Es exportable para la herramienta analítica
    Dada la exactitud histórica almacenada
    Cuando se solicita exportarla
    Entonces está disponible en exportación para la herramienta analítica
```

### HU-CNT-009 — Reasignar una tarea de conteo cuando el auxiliar no está

**Prioridad:** Could (P2) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador · **Legacy:** HU-066  
**Depende de:** HU-CNT-001, HU-TAR-001 · **RF:** RF-TAR-004 · **RN:** RN-CNT-003 · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** reasignar una tarea de conteo cuando el auxiliar asignado no está **PARA** que el conteo no se detenga.

```gherkin
@HU-CNT-009 @Could @M-11
Característica: HU-CNT-009 — Reasignar una tarea de conteo cuando el auxiliar no está
  # Criterio SPEC (1): La tarea se reasigna a otro usuario habilitado.
  Escenario: C1 · La tarea se reasigna a otro usuario habilitado
    Dada una tarea de conteo asignada a un auxiliar no disponible
    Cuando el Coordinador la reasigna
    Entonces la tarea queda asignada a otro usuario habilitado
  # Criterio SPEC (2): Ambos responsables quedan registrados.
  Escenario: C2 · Ambos responsables quedan registrados
    Dada una tarea reasignada
    Cuando se consulta su historial
    Entonces figuran el responsable anterior y el nuevo
  # Criterio SPEC (3): Si había un conteo parcial, se conserva y se marca.
  Escenario: C3 · Un conteo parcial se conserva y se marca
    Dada una tarea con un conteo parcial previo
    Cuando se reasigna
    Entonces el conteo parcial se conserva y se marca
  # Criterio SPEC (4): La reasignación no puede violar la regla del segundo conteo `[RN-CNT-003]`.
  Escenario: C4 · La reasignación no puede violar la regla del segundo conteo
    Dada una tarea de segundo conteo
    Cuando se intenta reasignar a quien hizo el primer conteo
    Entonces el sistema lo impide
```

### HU-CNT-010 — Contar pieza por pieza

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-109  
**Depende de:** HU-ENT-009, HU-CNT-002 · **RF:** RF-CNT-014 · **RN:** RN-CNT-001, RN-CNT-002, RN-CNT-009 · **KPI:** KPI-01  
**Origen (SPEC):** `[F-5]` `[RN-CNT-009*]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** contar a mano cada pieza de una ubicación y registrar su cantidad **PARA** que el conteo verifique la realidad pieza por pieza.

```gherkin
@HU-CNT-010 @Must @M-11
Característica: HU-CNT-010 — Contar pieza por pieza
  # Criterio SPEC (1): El conteo se hace manualmente, pieza por pieza `[F-5]`.
  Escenario: C1 · El conteo se hace a mano, pieza por pieza
    Dada una tarea de conteo
    Cuando el Auxiliar cuenta la ubicación
    Entonces cuenta manualmente cada pieza
  # Criterio SPEC (2): El Auxiliar registra la cantidad de cada pieza contada.
  Escenario: C2 · El Auxiliar registra la cantidad de cada pieza contada
    Dada una pieza contada
    Cuando el Auxiliar registra su cantidad
    Entonces el sistema guarda la cantidad de esa pieza
  # Criterio SPEC (3): `[RN-CNT-002]` La cantidad esperada no se muestra antes ni después de registrar.
  Escenario: C3 · La cantidad esperada no se muestra antes ni después de registrar
    Dado un conteo pieza por pieza
    Cuando el Auxiliar registra la cantidad de una pieza
    Entonces el sistema no muestra la cantidad esperada ni antes ni después
  # Criterio SPEC (4): La cantidad contada de la unidad de inventario es la suma de sus piezas `[RN-CNT-009]`.
  Escenario: C4 · La cantidad contada de la unidad de inventario es la suma de sus piezas
    Dadas varias piezas contadas en una ubicación
    Cuando el sistema consolida el conteo
    Entonces la cantidad contada de la unidad de inventario es la suma de sus piezas
  # Criterio SPEC (5): El sistema compara lo contado con la existencia congelada y clasifica cada línea como conforme, sobrante o faltante `[RN-CNT-001]`.
  Escenario: C5 · Se compara contra la existencia congelada y se clasifica cada línea
    Dado un conteo registrado
    Cuando el sistema lo compara contra la existencia congelada
    Entonces clasifica cada línea como conforme, sobrante o faltante
```

### HU-CNT-011 — Avisar cuando la diferencia global de un conteo general es crítica

**Prioridad:** Should (P1) · **Horizonte:** H2 · **Actor (SPEC):** Jefe · **Legacy:** HU-112  
**Depende de:** HU-CNT-006, HU-PAR-001 · **RF:** RF-CNT-015 · **RN:** RN-CNT-008 · **KPI:** KPI-02  
**Origen (SPEC):** `[RN-CNT-008]` `[DEC-06]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que el sistema avise al Administrador y al Auditor cuando la diferencia global de un conteo general sea crítica **PARA** que un conteo con un problema grave no se cierre sin que nadie lo sepa.

```gherkin
@HU-CNT-011 @Should @M-11
Característica: HU-CNT-011 — Avisar cuando la diferencia global de un conteo general es crítica
  # Criterio SPEC (1): El umbral crítico de diferencia global es un parámetro configurable `[RF-PAR-001]`.
  Escenario: C1 · El umbral crítico de diferencia global es configurable
    Dado el Administrador en la configuración
    Cuando define el umbral crítico de diferencia global
    Entonces el sistema lo guarda como parámetro configurable
  # Criterio SPEC (2): Si la diferencia global del conteo general lo supera, el sistema notifica al Administrador y al Auditor.
  Escenario: C2 · Se notifica al Administrador y al Auditor
    Dado un conteo general con una diferencia global sobre el umbral crítico
    Cuando el sistema la evalúa
    Entonces notifica al Administrador y al Auditor
  # Criterio SPEC (3): El cierre del conteo general queda condicionado a esa notificación `[RN-CNT-008]`.
  Escenario: C3 · El cierre queda condicionado a la notificación
    Dado un conteo general con diferencia global crítica
    Cuando el Jefe intenta cerrarlo
    Entonces el sistema no lo cierra antes de haber notificado
  # Criterio SPEC (4): La notificación queda en la bitácora.
  Escenario: C4 · La notificación queda en la bitácora
    Dada una notificación por diferencia crítica
    Cuando el sistema la envía
    Entonces queda registrada en la bitácora
```


## 5.14 M-12 · Novedades de Mercancía (dominio NOV)

### HU-NOV-001 — Reportar una anomalía sin que parezca una falta propia

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-067  
**Depende de:** HU-QRC-002, HU-ACC-001 · **RF:** RF-NOV-001, RF-NOV-002, RF-NOV-003 · **RN:** — · **KPI:** KPI-23  
**Origen (SPEC):** `[MON §4]` `[PR-06]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** reportar fácilmente que encontré algo raro **PARA** avisar sin que parezca que yo hice algo mal.

```gherkin
@HU-NOV-001 @Should @M-12
Característica: HU-NOV-001 — Reportar una anomalía sin que parezca una falta propia
  # Criterio SPEC (1): El reporte se abre desde la tablet en pocos pasos `[DC-05]`.
  Escenario: C1 · El reporte se abre desde la tablet en pocos pasos
    Dado un Auxiliar con la tablet
    Cuando decide reportar una novedad
    Entonces puede abrir el reporte en pocos pasos
  # Criterio SPEC (2): El tipo de novedad se selecciona de una lista tipificada.
  Escenario: C2 · El tipo de novedad se selecciona de una lista tipificada
    Dado un reporte de novedad en curso
    Cuando el Auxiliar elige el tipo
    Entonces selecciona de una lista tipificada
  # Criterio SPEC (3): Se puede escanear el identificador o declarar que no existe.
  Escenario: C3 · Se puede escanear el identificador o declarar que no existe
    Dado un reporte de novedad en curso
    Cuando el Auxiliar escanea el identificador o declara su ausencia
    Entonces el sistema registra cualquiera de las dos opciones
  # Criterio SPEC (4): Se puede adjuntar fotografía.
  Escenario: C4 · Se puede adjuntar fotografía
    Dado un reporte de novedad en curso
    Cuando el Auxiliar adjunta una fotografía
    Entonces la fotografía queda asociada a la novedad
  # Criterio SPEC (5): `[PR-06]` El sistema no presenta el reporte como una falta del reportante ni lo contabiliza en su contra.
  Escenario: C5 · El reporte no se presenta como falta ni se contabiliza en contra del reportante
    Dada una novedad reportada por un Auxiliar
    Cuando el sistema la presenta y calcula indicadores
    Entonces no la presenta como una falta del reportante ni la contabiliza en su contra
```

### HU-NOV-002 — Recibir y resolver las novedades reportadas

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador · **Legacy:** HU-068  
**Depende de:** HU-NOV-001 · **RF:** RF-NOV-004, RF-NOV-005, RF-NOV-006 · **RN:** RN-MAE-007, RN-NOV-003 · **KPI:** KPI-23  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** recibir y resolver las novedades reportadas **PARA** que los problemas físicos no se queden sin atender.

```gherkin
@HU-NOV-002 @Should @M-12
Característica: HU-NOV-002 — Recibir y resolver las novedades reportadas
  # Criterio SPEC (1): Las novedades de su zona llegan a su panel.
  Escenario: C1 · Las novedades de su zona llegan a su panel
    Dada una novedad reportada en la zona de un Coordinador
    Cuando se registra
    Entonces llega al panel de ese Coordinador
  # Criterio SPEC (2): Puede determinar la acción: ajuste, reidentificación, reubicación o baja.
  Escenario: C2 · Puede determinar la acción: ajuste, reidentificación, reubicación o baja
    Dada una novedad abierta
    Cuando el Coordinador la evalúa
    Entonces puede determinar ajuste, reidentificación, reubicación o baja
  # Criterio SPEC (3): `[RN-NOV-003]` Una novedad sobre una unidad con novedad abierta se vincula, no se duplica.
  Escenario: C3 · Una novedad sobre unidad con novedad abierta se vincula, no se duplica
    Dada una unidad con una novedad abierta
    Cuando se reporta otra novedad sobre la misma unidad
    Entonces el sistema la vincula a la existente y no crea una nueva
  # Criterio SPEC (4): La novedad se cierra con constancia de la resolución.
  Escenario: C4 · La novedad se cierra con constancia de la resolución
    Dada una novedad resuelta
    Cuando el Coordinador la cierra
    Entonces queda cerrada con constancia de la resolución
  # Criterio SPEC (5): `[RN-MAE-007]` No existe la opción de eliminar una novedad.
  Escenario: C5 · No existe la opción de eliminar una novedad
    Dada una novedad en cualquier estado
    Cuando el usuario busca eliminarla
    Entonces el sistema no ofrece esa opción
```

### HU-NOV-003 — Escalar al Jefe las novedades sin resolver

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe · **Legacy:** HU-069  
**Depende de:** HU-NOV-001, HU-PAR-001 · **RF:** RF-NOV-004, RF-ALE-007, RF-NOV-008 · **RN:** RN-ALE-002, RN-ALE-003, RN-NOV-002 · **KPI:** KPI-23  
**Origen (SPEC):** `[RN-NOV-002]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que las novedades sin resolver escalen hacia mí **PARA** que ningún problema quede olvidado.

```gherkin
@HU-NOV-003 @Should @M-12
Característica: HU-NOV-003 — Escalar al Jefe las novedades sin resolver
  # Criterio SPEC (1): El plazo de resolución es configurable `[RN-NOV-002]`.
  Escenario: C1 · El plazo de resolución es configurable
    Dado el Administrador en Parámetros y Configuración
    Cuando define el plazo de resolución de novedades
    Entonces el plazo queda configurado
  # Criterio SPEC (2): Al vencer, la novedad escala al Jefe y genera alerta.
  Escenario: C2 · Al vencer, la novedad escala al Jefe y genera alerta
    Dada una novedad sin resolver que supera el plazo
    Cuando el sistema evalúa el plazo
    Entonces la novedad escala al Jefe y genera una alerta
  # Criterio SPEC (3): El escalamiento queda registrado.
  Escenario: C3 · El escalamiento queda registrado
    Dada una novedad escalada
    Cuando se consulta su historial
    Entonces el escalamiento figura registrado
  # Criterio SPEC (4): El listado de novedades vencidas es consultable.
  Escenario: C4 · El listado de novedades vencidas es consultable
    Dadas novedades vencidas
    Cuando el Jefe consulta el listado
    Entonces las novedades vencidas aparecen en él
```

### HU-NOV-004 — Registrar mercancía encontrada que no está en el sistema

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador / Jefe · **Legacy:** HU-070  
**Depende de:** HU-NOV-001, HU-AJU-001, HU-QRC-001, HU-ENT-006 · **RF:** RF-BOD-004, RF-QRC-001, RF-AJU-001, RF-AJU-002, RF-NOV-007 · **RN:** RN-AJU-003, RN-EXI-001, RN-EXI-002, RN-IDE-001, RN-IDE-002, RN-NOV-001 · **KPI:** —  
**Origen (SPEC):** `[RN-NOV-001]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** registrar mercancía encontrada que no está en el sistema **PARA** incorporarla sin saltarme los controles.

```gherkin
@HU-NOV-004 @Should @M-12
Característica: HU-NOV-004 — Registrar mercancía encontrada que no está en el sistema
  # Criterio SPEC (1): `[RN-NOV-001]` La mercancía sin registro no se cuenta ni se usa hasta ser identificada.
  Escenario: C1 · La mercancía sin registro no se cuenta ni se usa hasta ser identificada
    Dada mercancía encontrada sin registro en el sistema
    Cuando se procesa un conteo o una operación
    Entonces esa mercancía no se cuenta ni se usa hasta ser identificada
  # Criterio SPEC (2): Se crea o selecciona la unidad de inventario correspondiente.
  Escenario: C2 · Se crea o selecciona la unidad de inventario correspondiente
    Dada mercancía encontrada ya identificada
    Cuando el Coordinador la registra
    Entonces se crea o selecciona la unidad de inventario correspondiente
  # Criterio SPEC (3): Se genera un ajuste por sobrante con motivo tipificado.
  Escenario: C3 · Se genera un ajuste por sobrante con motivo tipificado
    Dada mercancía encontrada por incorporar
    Cuando se solicita su incorporación
    Entonces se genera un ajuste por sobrante con motivo tipificado
  # Criterio SPEC (4): Requiere aprobación del Jefe.
  Escenario: C4 · Requiere aprobación del Jefe
    Dado un ajuste por sobrante de mercancía encontrada
    Cuando se envía a aprobación
    Entonces requiere la aprobación del Jefe
  # Criterio SPEC (5): Se genera identificador QR y se asigna ubicación.
  Escenario: C5 · Se genera el identificador QR y se asigna ubicación
    Dado un ajuste por sobrante aprobado
    Cuando se aplica
    Entonces se genera el identificador QR y se asigna la ubicación de la mercancía
```


## 5.15 M-13 · Consulta de Existencia (dominio INV)

### HU-INV-001 — Saber en el momento cuánto hay de una referencia

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Todos · **Legacy:** HU-071  
**Depende de:** HU-ENT-003, HU-KDX-001 · **RF:** RF-INV-001, RF-INV-002, RF-INV-003 · **RN:** RN-EXI-003, RN-EXI-004, RN-EXI-005, RN-EXI-006, RN-EXI-007, RN-INT-004, RN-INT-006 · **KPI:** KPI-09  
**Origen (SPEC):** `[MON §6, §7.2]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** saber en el momento cuánto tengo de una referencia **PARA** responder sin tener que ir a contar ni revisar el cuaderno.

```gherkin
@HU-INV-001 @Must @M-13
Característica: HU-INV-001 — Saber en el momento cuánto hay de una referencia
  # Criterio SPEC (1): La consulta por referencia devuelve existencia desglosada por talla, color y lote.
  Escenario: C1 · La consulta por referencia devuelve existencia por talla, color y lote
    Dada una referencia con existencia
    Cuando el usuario la consulta
    Entonces el sistema devuelve la existencia desglosada por talla, color y lote
  # Criterio SPEC (2): Muestra el desglose por estado: disponible, reservado, inmovilizado, en tránsito.
  Escenario: C2 · Muestra el desglose por estado
    Dada una consulta de existencia
    Cuando se presenta el resultado
    Entonces muestra el desglose por disponible, reservado, inmovilizado y en tránsito
  # Criterio SPEC (3): Responde dentro del tiempo de RNF-REN-001. [SRS: el SPEC cita RNF-012 (ID legacy, referencia errónea); el requisito aplicable es RNF-REN-001 (H-05)]
  Escenario: C3 · Responde dentro del tiempo de rendimiento definido
    Dada una consulta de existencia por referencia con el volumen esperado
    Cuando el sistema responde
    Entonces la respuesta llega dentro del tiempo definido para la consulta de existencia
  # Criterio SPEC (4): `[RN-INT-004]` La cifra mostrada siempre se deriva del kardex.
  Escenario: C4 · La cifra mostrada siempre se deriva del kardex
    Dada una existencia mostrada
    Cuando se verifica su origen
    Entonces la cifra se deriva del kardex y no de un valor independiente
```

### HU-INV-002 — Escanear una etiqueta y ver qué es y cuánto hay

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-072  
**Depende de:** HU-QRC-002, HU-INV-001 · **RF:** RF-INV-001, RF-INV-005, RF-INV-008 · **RN:** RN-INT-004, RN-INT-006 · **KPI:** —  
**Origen (SPEC):** `[DC-08]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** escanear una etiqueta y ver de inmediato qué es y cuánto hay **PARA** resolver dudas sin preguntarle a nadie.

```gherkin
@HU-INV-002 @Must @M-13
Característica: HU-INV-002 — Escanear una etiqueta y ver qué es y cuánto hay
  # Criterio SPEC (1): El escaneo devuelve referencia, talla, color, lote, ubicación y existencia.
  Escenario: C1 · El escaneo devuelve referencia, talla, color, lote, ubicación y existencia
    Dada una etiqueta reconocida
    Cuando el Auxiliar la escanea
    Entonces el sistema muestra referencia, talla, color, lote, ubicación y existencia
  # Criterio SPEC (2): `[PR-04]` No muestra costo ni valorización.
  Escenario: C2 · No muestra costo ni valorización
    Dada una consulta de un Auxiliar
    Cuando se presenta el resultado
    Entonces no muestra costo ni valorización
  # Criterio SPEC (3): Si el identificador no se reconoce, ofrece reportar novedad.
  Escenario: C3 · Si el identificador no se reconoce ofrece reportar novedad
    Dado un identificador no reconocido
    Cuando se escanea
    Entonces el sistema ofrece reportar una novedad
  # Criterio SPEC (4): La consulta no modifica nada.
  Escenario: C4 · La consulta no modifica nada
    Dada una consulta por escaneo
    Cuando finaliza
    Entonces el estado del inventario permanece sin modificaciones
```

### HU-INV-003 — Buscar dónde está una referencia

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Todos · **Legacy:** HU-073  
**Depende de:** HU-INV-001 · **RF:** RF-INV-001, RF-INV-004 · **RN:** RN-INT-004, RN-INT-005, RN-INT-006 · **KPI:** KPI-18  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** buscar dónde está una referencia **PARA** ir directo al lugar en vez de recorrer la bodega.

```gherkin
@HU-INV-003 @Must @M-13
Característica: HU-INV-003 — Buscar dónde está una referencia
  # Criterio SPEC (1): La consulta devuelve todas las ubicaciones con existencia de esa referencia y su cantidad.
  Escenario: C1 · Devuelve todas las ubicaciones con existencia y su cantidad
    Dada una referencia con existencia en varias ubicaciones
    Cuando el usuario la busca
    Entonces el sistema devuelve todas las ubicaciones con su cantidad
  # Criterio SPEC (2): Ordena por cantidad o por zona.
  Escenario: C2 · Ordena por cantidad o por zona
    Dado un resultado de ubicaciones
    Cuando el usuario elige un orden
    Entonces el sistema ordena por cantidad o por zona
  # Criterio SPEC (3): Permite filtrar por talla, color y lote.
  Escenario: C3 · Permite filtrar por talla, color y lote
    Dado un resultado de ubicaciones
    Cuando el usuario filtra por talla, color o lote
    Entonces el sistema muestra solo las ubicaciones que cumplen el filtro
  # Criterio SPEC (4): Marca las ubicaciones cuya existencia no está disponible.
  Escenario: C4 · Marca las ubicaciones cuya existencia no está disponible
    Dadas ubicaciones con existencia reservada, inmovilizada o en tránsito
    Cuando se presenta el resultado
    Entonces las marca como no disponibles
```

### HU-INV-004 — Consultar todo lo que hay en una ubicación

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Coordinador · **Legacy:** HU-074  
**Depende de:** HU-INV-001, HU-BOD-001 · **RF:** RF-INV-001 · **RN:** RN-INT-004, RN-INT-006 · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** consultar todo lo que hay en una ubicación **PARA** saber qué tengo en cada estante antes de asignar mercancía nueva.

```gherkin
@HU-INV-004 @Should @M-13
Característica: HU-INV-004 — Consultar todo lo que hay en una ubicación
  # Criterio SPEC (1): La consulta por ubicación lista todas las unidades de inventario presentes.
  Escenario: C1 · Lista todas las unidades de inventario presentes
    Dada una ubicación con existencias
    Cuando el usuario la consulta
    Entonces el sistema lista todas las unidades de inventario presentes
  # Criterio SPEC (2): Muestra la ocupación frente a la capacidad.
  Escenario: C2 · Muestra la ocupación frente a la capacidad
    Dada una ubicación con capacidad definida
    Cuando se presenta la consulta
    Entonces muestra la ocupación frente a la capacidad
  # Criterio SPEC (3): Indica si la ubicación está sobreocupada.
  Escenario: C3 · Indica si la ubicación está sobreocupada
    Dada una ubicación cuya ocupación supera su capacidad
    Cuando se presenta la consulta
    Entonces indica que está sobreocupada
  # Criterio SPEC (4): Permite iniciar un movimiento desde la consulta.
  Escenario: C4 · Permite iniciar un movimiento desde la consulta
    Dada una ubicación consultada
    Cuando el usuario elige iniciar un movimiento
    Entonces el sistema inicia el movimiento desde la consulta
```

### HU-INV-005 — Consultar la existencia de una fecha pasada

**Prioridad:** Should (P1) · **Horizonte:** H2 · **Actor (SPEC):** Jefe / Auditor · **Legacy:** HU-075  
**Depende de:** HU-KDX-001 · **RF:** RF-INV-006 · **RN:** RN-INT-004 · **KPI:** —  
**Origen (SPEC):** `[MON §7.1]`

**Historia.** **COMO** Auditor **QUIERO** consultar cuánta existencia había en una fecha pasada **PARA** verificar el estado del inventario en un momento determinado.

```gherkin
@HU-INV-005 @Should @M-13
Característica: HU-INV-005 — Consultar la existencia de una fecha pasada
  # Criterio SPEC (1): Se indica fecha y hora de corte.
  Escenario: C1 · Se indica fecha y hora de corte
    Dado el Auditor en la consulta histórica
    Cuando indica una fecha y hora de corte
    Entonces el sistema toma ese corte para la consulta
  # Criterio SPEC (2): El sistema reconstruye la existencia a partir del kardex `[RN-INT-004]`.
  Escenario: C2 · El sistema reconstruye la existencia a partir del kardex
    Dada una fecha de corte indicada
    Cuando el sistema calcula la existencia
    Entonces la reconstruye a partir del kardex
  # Criterio SPEC (3): El resultado es idéntico si se consulta dos veces la misma fecha.
  Escenario: C3 · El resultado es idéntico si se consulta dos veces la misma fecha
    Dada una consulta histórica repetida sobre la misma fecha de corte
    Cuando se comparan ambos resultados
    Entonces son idénticos
  # Criterio SPEC (4): Declara explícitamente la fecha de corte aplicada.
  Escenario: C4 · Declara explícitamente la fecha de corte aplicada
    Dada una consulta histórica
    Cuando se presenta el resultado
    Entonces declara explícitamente la fecha de corte aplicada
  # Criterio SPEC (5): Es exportable.
  Escenario: C5 · El resultado es exportable
    Dado un resultado histórico
    Cuando el usuario solicita exportarlo
    Entonces el sistema entrega la exportación
```

### HU-INV-006 — Buscar escribiendo parte del nombre

**Prioridad:** Could (P2) · **Horizonte:** H1 · **Actor (SPEC):** Todos · **Legacy:** HU-076  
**Depende de:** HU-INV-001 · **RF:** RF-INV-007 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[MON §8.2 — usabilidad]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** buscar escribiendo parte del nombre **PARA** encontrar lo que necesito sin conocer el código exacto.

```gherkin
@HU-INV-006 @Could @M-13
Característica: HU-INV-006 — Buscar escribiendo parte del nombre
  # Criterio SPEC (1): La búsqueda acepta texto parcial de referencia o descripción.
  Escenario: C1 · La búsqueda acepta texto parcial de referencia o descripción
    Dado el buscador de existencia
    Cuando el usuario escribe parte de una referencia o descripción
    Entonces el sistema realiza la búsqueda con ese texto parcial
  # Criterio SPEC (2): Devuelve coincidencias aproximadas ordenadas por relevancia.
  Escenario: C2 · Devuelve coincidencias aproximadas ordenadas por relevancia
    Dada una búsqueda con texto parcial
    Cuando se presentan los resultados
    Entonces son coincidencias aproximadas ordenadas por relevancia
  # Criterio SPEC (3): Tolera diferencias de mayúsculas y tildes.
  Escenario: C3 · Tolera diferencias de mayúsculas y tildes
    Dada una búsqueda escrita con mayúsculas o sin tildes distintas a las del dato
    Cuando el sistema la procesa
    Entonces encuentra las coincidencias sin distinguir mayúsculas ni tildes
  # Criterio SPEC (4): Si no hay coincidencias, lo informa claramente en lugar de mostrar una lista vacía.
  Escenario: C4 · Si no hay coincidencias lo informa claramente
    Dada una búsqueda sin coincidencias
    Cuando se presenta el resultado
    Entonces informa claramente que no hay coincidencias en lugar de mostrar una lista vacía
```


## 5.16 M-14 · Kardex y Trazabilidad (dominio KDX)

### HU-KDX-001 — Ver la historia completa de una unidad de inventario

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Auditor · **Legacy:** HU-077  
**Depende de:** HU-ENT-003 · **RF:** RF-KDX-001, RF-KDX-002, RF-KDX-005, RF-KDX-009 · **RN:** RN-INT-001, RN-INT-002 · **KPI:** KPI-05, KPI-17, KPI-24  
**Origen (SPEC):** `[MON §7.1]` `[CD-21]`

**Historia.** **COMO** Auditor **QUIERO** ver la historia completa de una unidad de inventario **PARA** reconstruir qué pasó con ella desde que entró.

```gherkin
@HU-KDX-001 @Must @M-14
Característica: HU-KDX-001 — Ver la historia completa de una unidad de inventario
  # Criterio SPEC (1): El kardex muestra todos los movimientos en orden cronológico.
  Escenario: C1 · El kardex muestra todos los movimientos en orden cronológico
    Dada una unidad de inventario con movimientos
    Cuando el Auditor consulta su kardex
    Entonces muestra todos los movimientos en orden cronológico
  # Criterio SPEC (2): Cada línea contiene fecha, hora, tipo, cantidad, existencia resultante, ubicación, usuario, motivo y documento.
  Escenario: C2 · Cada línea contiene fecha, hora, tipo, cantidad, existencia resultante, ubicación, usuario, motivo y documento
    Dado un kardex consultado
    Cuando se revisa una línea
    Entonces contiene fecha, hora, tipo, cantidad, existencia resultante, ubicación, usuario, motivo y documento
  # Criterio SPEC (3): `[CD-21]` Permite responder las seis preguntas de trazabilidad: qué, cuánto, dónde, quién, cuándo y por qué.
  Escenario: C3 · Permite responder las seis preguntas de trazabilidad
    Dado el kardex de una unidad
    Cuando se analiza su historia
    Entonces permite responder qué, cuánto, dónde, quién, cuándo y por qué
  # Criterio SPEC (4): No tiene huecos.
  Escenario: C4 · No tiene huecos
    Dado el kardex de una unidad desde su creación
    Cuando se verifica su continuidad
    Entonces no presenta huecos
  # Criterio SPEC (5): Es exportable.
  Escenario: C5 · El kardex es exportable
    Dado un kardex consultado
    Cuando el usuario solicita exportarlo
    Entonces el sistema entrega la exportación
```

### HU-KDX-002 — Impedir que un movimiento pueda borrarse o editarse

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Todos los roles · **Legacy:** HU-078  
**Depende de:** HU-KDX-001 · **RF:** RF-KDX-003, RF-KDX-004 · **RN:** RN-AJU-007, RN-INT-002 · **KPI:** KPI-08  
**Origen (SPEC):** `[RN-INT-002]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que ningún movimiento pueda borrarse ni editarse **PARA** que la historia del inventario sea confiable.

```gherkin
@HU-KDX-002 @Must @M-14
Característica: HU-KDX-002 — Impedir que un movimiento pueda borrarse o editarse
  # Criterio SPEC (1): `[RN-INT-002]` No existe función de edición ni de eliminación de un movimiento confirmado, para ningún rol, incluido el Administrador.
  Escenario: C1 · No existe edición ni eliminación de un movimiento confirmado, para ningún rol
    Dado un movimiento confirmado
    Cuando cualquier usuario, incluido el Administrador, busca editarlo o eliminarlo
    Entonces el sistema no ofrece esas funciones
  # Criterio SPEC (2): Un error se corrige generando un movimiento inverso.
  Escenario: C2 · Un error se corrige generando un movimiento inverso
    Dado un movimiento confirmado con error
    Cuando se corrige
    Entonces se genera un movimiento inverso
  # Criterio SPEC (3): Ambos movimientos permanecen visibles en el kardex.
  Escenario: C3 · Ambos movimientos permanecen visibles en el kardex
    Dado un movimiento y su movimiento inverso
    Cuando se consulta el kardex
    Entonces ambos permanecen visibles
  # Criterio SPEC (4): La anulación exige motivo y autorización.
  Escenario: C4 · La anulación exige motivo y autorización
    Dada una anulación de movimiento
    Cuando se intenta ejecutar sin motivo o sin autorización
    Entonces el sistema no la permite
  # Criterio SPEC (5): La anulación queda en la bitácora.
  Escenario: C5 · La anulación queda en bitácora
    Dada una anulación completada
    Cuando el sistema registra el evento
    Entonces queda en la bitácora
```

### HU-KDX-003 — Verificar que la existencia equivale a la suma de movimientos

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auditor · **Legacy:** HU-079  
**Depende de:** HU-KDX-001 · **RF:** RF-KDX-006 · **RN:** RN-AUD-005, RN-INT-004 · **KPI:** KPI-09  
**Origen (SPEC):** `[RN-INT-004]`

**Historia.** **COMO** Auditor **QUIERO** verificar que la existencia actual corresponde exactamente a la suma de los movimientos **PARA** confirmar que nadie alteró el inventario por fuera del sistema.

```gherkin
@HU-KDX-003 @Should @M-14
Característica: HU-KDX-003 — Verificar que la existencia equivale a la suma de movimientos
  # Criterio SPEC (1): `[RN-INT-004]` El sistema verifica que existencia actual = suma algebraica de movimientos del kardex.
  Escenario: C1 · El sistema verifica existencia actual igual a la suma algebraica del kardex
    Dado el Auditor solicitando la verificación de integridad
    Cuando el sistema la ejecuta
    Entonces compara la existencia actual con la suma algebraica de los movimientos del kardex
  # Criterio SPEC (2): Cualquier discrepancia se reporta como hallazgo crítico.
  Escenario: C2 · Cualquier discrepancia se reporta como hallazgo crítico
    Dada una unidad cuya existencia difiere de la suma de sus movimientos
    Cuando la verificación la detecta
    Entonces la reporta como hallazgo crítico
  # Criterio SPEC (3): La verificación es ejecutable por unidad, por lote o global.
  Escenario: C3 · La verificación es ejecutable por unidad, por lote o global
    Dado el Auditor en la verificación de integridad
    Cuando elige el alcance
    Entonces puede ejecutarla por unidad, por lote o de forma global
  # Criterio SPEC (4): El resultado es exportable.
  Escenario: C4 · El resultado es exportable
    Dado un resultado de verificación
    Cuando el usuario solicita exportarlo
    Entonces el sistema entrega la exportación
```

### HU-KDX-004 — Ver el kardex de un lote completo

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Auditor · **Legacy:** HU-080  
**Depende de:** HU-KDX-001, HU-LOT-001 · **RF:** RF-KDX-005 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[MON §7.1]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** ver el kardex de un lote completo **PARA** rastrear un problema de calidad hasta todas las unidades afectadas.

```gherkin
@HU-KDX-004 @Should @M-14
Característica: HU-KDX-004 — Ver el kardex de un lote completo
  # Criterio SPEC (1): El kardex de lote consolida los movimientos de todas sus unidades.
  Escenario: C1 · El kardex de lote consolida los movimientos de todas sus unidades
    Dado un lote con varias unidades de inventario
    Cuando el Jefe consulta su kardex
    Entonces consolida los movimientos de todas sus unidades
  # Criterio SPEC (2): Muestra en qué ubicaciones estuvo y está.
  Escenario: C2 · Muestra en qué ubicaciones estuvo y está
    Dado un kardex de lote
    Cuando se presenta
    Entonces muestra las ubicaciones donde estuvo y donde está el lote
  # Criterio SPEC (3): Muestra qué salió, cuándo y con qué motivo.
  Escenario: C3 · Muestra qué salió, cuándo y con qué motivo
    Dado un kardex de lote con salidas
    Cuando se presenta
    Entonces muestra qué salió, cuándo y con qué motivo
  # Criterio SPEC (4): Permite inmovilizar desde la consulta.
  Escenario: C4 · Permite inmovilizar desde la consulta
    Dado un kardex de lote consultado por el Jefe
    Cuando elige inmovilizar el lote
    Entonces el sistema inicia la inmovilización desde la consulta
```

### HU-KDX-005 — Revisar los movimientos que yo registré

**Prioridad:** Could (P2) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-081  
**Depende de:** HU-KDX-001 · **RF:** RF-KDX-007 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[§2.7]` `[PR-04]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** revisar los movimientos que yo registré **PARA** verificar mi propio trabajo del turno.

```gherkin
@HU-KDX-005 @Could @M-14
Característica: HU-KDX-005 — Revisar los movimientos que yo registré
  # Criterio SPEC (1): `[§2.7]` El Auxiliar ve únicamente el kardex de las unidades que él movió y de los últimos 30 días.
  Escenario: C1 · El Auxiliar ve solo el kardex de las unidades que movió y de los últimos 30 días
    Dado un Auxiliar consultando el kardex
    Cuando se presenta el resultado
    Entonces ve únicamente las unidades que él movió y los últimos 30 días
  # Criterio SPEC (2): No ve movimientos de otros usuarios.
  Escenario: C2 · No ve movimientos de otros usuarios
    Dados movimientos registrados por otros usuarios
    Cuando el Auxiliar consulta el kardex
    Entonces esos movimientos no aparecen
  # Criterio SPEC (3): No ve valorización `[PR-04]`.
  Escenario: C3 · No ve valorización
    Dado un Auxiliar consultando el kardex
    Cuando se presenta el resultado
    Entonces no muestra valorización
  # Criterio SPEC (4): `[PR-06]` No se le presentan indicadores de error personal.
  Escenario: C4 · No se le presentan indicadores de error personal
    Dado un Auxiliar consultando sus movimientos
    Cuando se presenta el resultado
    Entonces no se le presentan indicadores de error personal
```

### HU-KDX-006 — Consultar dónde está y qué ha pasado con cada pieza de un lote

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Auditor · **Legacy:** HU-110  
**Depende de:** HU-ENT-009, HU-KDX-001 · **RF:** RF-KDX-008, RF-INV-009 · **RN:** RN-LOT-006, RN-LOT-007 · **KPI:** —  
**Origen (SPEC):** `[Q-11]` `[CD-21]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** consultar dónde está y qué ha pasado con cada pieza de un lote **PARA** rastrear un rollo o un paquete concreto y no solo el lote completo.

```gherkin
@HU-KDX-006 @Must @M-14
Característica: HU-KDX-006 — Consultar dónde está y qué ha pasado con cada pieza de un lote
  # Criterio SPEC (1): La consulta de un lote muestra sus piezas con tipo, cantidad actual, ubicación y estado `[Q-11]`.
  Escenario: C1 · La consulta de un lote muestra sus piezas
    Dado un lote con piezas
    Cuando se consulta el lote
    Entonces se muestran sus piezas con tipo, cantidad actual, ubicación y estado
  # Criterio SPEC (2): El kardex de una pieza muestra todos sus movimientos en orden cronológico.
  Escenario: C2 · El kardex de una pieza muestra sus movimientos en orden cronológico
    Dada una pieza con movimientos
    Cuando se consulta su kardex
    Entonces los movimientos aparecen en orden cronológico
  # Criterio SPEC (3): `[CD-21]` Permite responder las seis preguntas de trazabilidad: qué, cuánto, dónde, quién, cuándo y por qué.
  Escenario: C3 · Permite responder las seis preguntas de trazabilidad
    Dado el kardex de una pieza
    Cuando el Auditor lo revisa
    Entonces puede responder qué, cuánto, dónde, quién, cuándo y por qué
  # Criterio SPEC (4): La trazabilidad por pieza no requiere un QR propio `[DF5-01]`.
  Escenario: C4 · La trazabilidad por pieza no requiere un QR propio
    Dada una pieza sin QR propio
    Cuando se consulta su trazabilidad
    Entonces el sistema la resuelve con la identidad interna de la pieza
  # Criterio SPEC (5): Responde dentro del tiempo de RNF-DSP-004.
  Escenario: C5 · La consulta responde dentro del tiempo de RNF-012
    Dada una consulta de piezas de un lote
    Cuando el usuario la solicita
    Entonces el sistema responde dentro del tiempo definido por RNF-012
```


## 5.17 M-15 · Alertas y Reglas (dominio ALE)

### HU-ALE-001 — Ser avisado antes de quedarse sin material

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Coordinador · **Legacy:** HU-082  
**Depende de:** HU-CAT-004, HU-INV-001 · **RF:** RF-ALE-001, RF-ALE-002, RF-ALE-003, RF-ALE-004 · **RN:** RN-AJU-004, RN-AJU-005, RN-ALE-003, RN-ALE-005, RN-CNT-005, RN-MOV-002, RN-MOV-008 · **KPI:** KPI-19, KPI-21  
**Origen (SPEC):** `[MON §3, §7.1]` `[DC-07]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que el sistema me avise antes de quedarme sin material **PARA** que la producción no se detenga por un faltante.

```gherkin
@HU-ALE-001 @Should @M-15
Característica: HU-ALE-001 — Ser avisado antes de quedarse sin material
  # Criterio SPEC (1): La alerta se dispara cuando la existencia disponible baja del mínimo configurado `[HU-CAT-004]`.
  Escenario: C1 · La alerta se dispara al bajar del mínimo configurado
    Dado un SKU con existencia mínima configurada
    Cuando su existencia disponible baja de ese mínimo
    Entonces el sistema dispara la alerta de ruptura inminente
  # Criterio SPEC (2): Identifica referencia, existencia actual y umbral.
  Escenario: C2 · La alerta identifica referencia, existencia actual y umbral
    Dada una alerta de ruptura inminente
    Cuando el destinatario la abre
    Entonces identifica la referencia, la existencia actual y el umbral
  # Criterio SPEC (3): Se dirige al Jefe y al Coordinador de la zona.
  Escenario: C3 · Se dirige al Jefe y al Coordinador de la zona
    Dada una alerta de ruptura inminente
    Cuando el sistema la genera
    Entonces la dirige al Jefe y al Coordinador de la zona
  # Criterio SPEC (4): `[DC-07]` La detección es por regla y umbral, no por predicción.
  Escenario: C4 · La detección es por regla y umbral, no por predicción
    Dada la evaluación de la condición de ruptura
    Cuando el sistema decide generar la alerta
    Entonces lo hace únicamente por regla explícita y umbral configurado
  # Criterio SPEC (5): Se cierra automáticamente al recuperarse la existencia `[RN-ALE-003]`.
  Escenario: C5 · Se cierra automáticamente al recuperarse la existencia
    Dada una alerta de ruptura vigente
    Cuando la existencia disponible se recupera sobre el mínimo
    Entonces la alerta se cierra automáticamente
```

### HU-ALE-002 — Ser avisado cuando hay demasiado de algo

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe · **Legacy:** HU-083  
**Depende de:** HU-CAT-004 · **RF:** RF-ALE-001, RF-ALE-004 · **RN:** RN-AJU-004, RN-AJU-005, RN-CNT-005, RN-MOV-002, RN-MOV-008 · **KPI:** KPI-16, KPI-19, KPI-21  
**Origen (SPEC):** `[MON §3]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que el sistema me avise cuando tengo demasiado de algo **PARA** no seguir acumulando material que no rota.

```gherkin
@HU-ALE-002 @Should @M-15
Característica: HU-ALE-002 — Ser avisado cuando hay demasiado de algo
  # Criterio SPEC (1): La alerta se dispara al superar el máximo configurado.
  Escenario: C1 · La alerta se dispara al superar el máximo configurado
    Dado un SKU con existencia máxima configurada
    Cuando su existencia supera ese máximo
    Entonces el sistema dispara la alerta de sobre stock
  # Criterio SPEC (2): Muestra la existencia, el umbral y los días sin movimiento de salida.
  Escenario: C2 · Muestra existencia, umbral y días sin movimiento de salida
    Dada una alerta de sobre stock
    Cuando el destinatario la abre
    Entonces muestra la existencia, el umbral y los días sin movimiento de salida
  # Criterio SPEC (3): Se dirige al Jefe.
  Escenario: C3 · Se dirige al Jefe
    Dada una alerta de sobre stock
    Cuando el sistema la genera
    Entonces la dirige al Jefe
  # Criterio SPEC (4): Alimenta el reporte de rotación (KPI-16).
  Escenario: C4 · Alimenta el reporte de rotación
    Dadas alertas de sobre stock generadas
    Cuando se calculan los indicadores
    Entonces alimentan el reporte de rotación por referencia
```

### HU-ALE-003 — Registrar qué se hizo con cada alerta

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Coordinador · **Legacy:** HU-084  
**Depende de:** HU-ALE-001 · **RF:** RF-ALE-005 · **RN:** RN-ALE-004 · **KPI:** KPI-19, KPI-20  
**Origen (SPEC):** `[RN-ALE-004]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** registrar qué hice con cada alerta **PARA** que quede claro que se atendió y cómo.

```gherkin
@HU-ALE-003 @Should @M-15
Característica: HU-ALE-003 — Registrar qué se hizo con cada alerta
  # Criterio SPEC (1): Cada alerta se atiende con una acción o se descarta.
  Escenario: C1 · Cada alerta se atiende con una acción o se descarta
    Dada una alerta activa
    Cuando el Jefe la gestiona
    Entonces puede atenderla con una acción o descartarla
  # Criterio SPEC (2): `[RN-ALE-004]` El descarte exige motivo; sin motivo la alerta no puede cerrarse.
  Escenario: C2 · El descarte exige motivo
    Dada una alerta que se intenta descartar
    Cuando se confirma el descarte sin motivo
    Entonces el sistema no permite cerrarla
  # Criterio SPEC (3): Queda registrado quién la atendió y cuándo.
  Escenario: C3 · Queda registrado quién la atendió y cuándo
    Dada una alerta atendida o descartada
    Cuando se consulta su registro
    Entonces figura quién la atendió, cuándo y qué hizo
  # Criterio SPEC (4): El historial de alertas es consultable y exportable.
  Escenario: C4 · El historial de alertas es consultable y exportable
    Dadas alertas cerradas
    Cuando el usuario consulta o exporta el historial
    Entonces el sistema lo muestra y lo exporta
```

### HU-ALE-004 — Escalar automáticamente las alertas críticas sin atender

**Prioridad:** Should (P1) · **Horizonte:** H2 · **Actor (SPEC):** Jefe / Administrador · **Legacy:** HU-085  
**Depende de:** HU-ALE-001, HU-PAR-001 · **RF:** RF-ALE-007 · **RN:** RN-ALE-002, RN-ALE-003 · **KPI:** KPI-20  
**Origen (SPEC):** `[RN-ALE-002]`

**Historia.** **COMO** Administrador **QUIERO** que las alertas críticas sin atender escalen automáticamente **PARA** que un problema grave no se quede esperando.

```gherkin
@HU-ALE-004 @Should @M-15
Característica: HU-ALE-004 — Escalar automáticamente las alertas críticas sin atender
  # Criterio SPEC (1): El plazo de atención por severidad es configurable `[RN-ALE-002]`.
  Escenario: C1 · El plazo de atención por severidad es configurable
    Dado el Administrador en Parámetros y Configuración
    Cuando define el plazo de atención por severidad
    Entonces el plazo queda configurado
  # Criterio SPEC (2): Al vencer, la alerta escala al rol superior.
  Escenario: C2 · Al vencer, la alerta escala al rol superior
    Dada una alerta crítica sin atender que supera su plazo
    Cuando el sistema evalúa el plazo
    Entonces la alerta escala al rol superior
  # Criterio SPEC (3): El escalamiento genera una notificación adicional.
  Escenario: C3 · El escalamiento genera una notificación adicional
    Dada una alerta escalada
    Cuando se completa el escalamiento
    Entonces se genera una notificación adicional
  # Criterio SPEC (4): Queda registrado en la bitácora.
  Escenario: C4 · El escalamiento queda en bitácora
    Dada una alerta escalada
    Cuando el sistema registra el evento
    Entonces queda en la bitácora
  # Criterio SPEC (5): La alerta original conserva su historial.
  Escenario: C5 · La alerta original conserva su historial
    Dada una alerta escalada
    Cuando se consulta su historial
    Entonces conserva todo su historial previo
```

### HU-ALE-005 — Evitar la saturación de alertas repetidas

**Prioridad:** Could (P2) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Coordinador · **Legacy:** HU-086  
**Depende de:** HU-ALE-001 · **RF:** RF-ALE-006 · **RN:** RN-ALE-001 · **KPI:** —  
**Origen (SPEC):** `[RN-ALE-001]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** que el sistema no me llene la pantalla de alertas repetidas **PARA** poder distinguir lo importante.

```gherkin
@HU-ALE-005 @Could @M-15
Característica: HU-ALE-005 — Evitar la saturación de alertas repetidas
  # Criterio SPEC (1): `[RN-ALE-001]` Una condición vigente genera una sola alerta activa, no una por evaluación.
  Escenario: C1 · Una condición vigente genera una sola alerta activa
    Dada una condición de alerta que se mantiene vigente
    Cuando el sistema la reevalúa en cada ciclo
    Entonces mantiene una sola alerta activa y no genera una por evaluación
  # Criterio SPEC (2): Las alertas se agrupan por tipo y severidad.
  Escenario: C2 · Las alertas se agrupan por tipo y severidad
    Dadas varias alertas activas
    Cuando se presentan al usuario
    Entonces se agrupan por tipo y severidad
  # Criterio SPEC (3): Se ordenan por severidad y antigüedad.
  Escenario: C3 · Se ordenan por severidad y antigüedad
    Dadas varias alertas activas
    Cuando se presentan al usuario
    Entonces se ordenan por severidad y antigüedad
  # Criterio SPEC (4): El sistema reporta al Administrador los tipos de alerta con frecuencia de disparo anómala, para recalibrar umbrales.
  Escenario: C4 · Se reporta al Administrador la frecuencia anómala de disparo
    Dados tipos de alerta con frecuencia de disparo anómala
    Cuando el sistema los detecta
    Entonces los reporta al Administrador para recalibrar umbrales
```


## 5.18 M-16 · Reportes y Exportación Analítica (dominio REP)

### HU-REP-001 — Generar el reporte de existencia por referencia, lote y ubicación

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Administrador · **Legacy:** HU-087  
**Depende de:** HU-INV-001 · **RF:** RF-REP-001, RF-REP-002 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[MON §8.2]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** generar el reporte de existencia por referencia, lote y ubicación **PARA** revisar el estado del inventario y compartirlo.

```gherkin
@HU-REP-001 @Should @M-16
Característica: HU-REP-001 — Generar el reporte de existencia por referencia, lote y ubicación
  # Criterio SPEC (1): Filtro por referencia, categoría, lote, ubicación y estado.
  Escenario: C1 · Filtro por referencia, categoría, lote, ubicación y estado
    Dado el reporte de existencia
    Cuando el usuario aplica filtros
    Entonces el reporte muestra solo lo que cumple los filtros
  # Criterio SPEC (2): Muestra existencia total y su desglose por estado.
  Escenario: C2 · Muestra existencia total y su desglose por estado
    Dado un reporte de existencia generado
    Cuando se presenta
    Entonces muestra la existencia total y su desglose por estado
  # Criterio SPEC (3): Declara fecha, hora y usuario de generación.
  Escenario: C3 · Declara fecha, hora y usuario de generación
    Dado un reporte generado
    Cuando se presenta o exporta
    Entonces declara la fecha, la hora y el usuario que lo generó
  # Criterio SPEC (4): Es exportable en formato tabular.
  Escenario: C4 · Es exportable en formato tabular
    Dado un reporte generado
    Cuando el usuario solicita exportarlo
    Entonces el sistema lo entrega en formato tabular
  # Criterio SPEC (5): `[PR-04]` `[DEC-07]` Ningún reporte muestra costo ni valorización: el MVP no captura costos.
  Escenario: C5 · Ningún reporte muestra costo ni valorización
    Dado un reporte generado por cualquier rol
    Cuando se revisa su contenido
    Entonces no muestra costo ni valorización porque el MVP no captura costos
```

### HU-REP-002 — Generar el reporte de movimientos de un período

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Auditor · **Legacy:** HU-088  
**Depende de:** HU-KDX-001 · **RF:** RF-REP-001, RF-REP-006 · **RN:** RN-AUD-001, RN-AUD-003 · **KPI:** —  
**Origen (SPEC):** `[MON §8.2]`

**Historia.** **COMO** Auditor **QUIERO** generar el reporte de movimientos de un período **PARA** revisar toda la actividad del inventario de una sola vez.

```gherkin
@HU-REP-002 @Should @M-16
Característica: HU-REP-002 — Generar el reporte de movimientos de un período
  # Criterio SPEC (1): Filtro por período, tipo de movimiento, usuario, referencia y motivo.
  Escenario: C1 · Filtro por período, tipo, usuario, referencia y motivo
    Dado el reporte de movimientos
    Cuando el Auditor aplica filtros
    Entonces el reporte muestra solo los movimientos que los cumplen
  # Criterio SPEC (2): Muestra cada movimiento con todos sus atributos.
  Escenario: C2 · Muestra cada movimiento con todos sus atributos
    Dado un reporte de movimientos generado
    Cuando se presenta
    Entonces cada movimiento aparece con todos sus atributos
  # Criterio SPEC (3): Totaliza por tipo.
  Escenario: C3 · Totaliza por tipo
    Dado un reporte de movimientos generado
    Cuando se presenta
    Entonces totaliza los movimientos por tipo
  # Criterio SPEC (4): Es exportable.
  Escenario: C4 · Es exportable
    Dado un reporte de movimientos generado
    Cuando el usuario solicita exportarlo
    Entonces el sistema lo entrega
  # Criterio SPEC (5): La exportación queda en la bitácora `[RN-AUD-001]`.
  Escenario: C5 · La exportación queda en bitácora
    Dada una exportación del reporte
    Cuando se completa
    Entonces queda registrada en la bitácora
```

### HU-REP-003 — Alimentar la herramienta analítica externa con los datos del sistema

**Prioridad:** Should (P1) · **Horizonte:** H2 · **Actor (SPEC):** Administrador · **Legacy:** HU-089  
**Depende de:** HU-REP-001, HU-REP-002 · **RF:** RF-REP-004, RF-REP-005, RF-REP-006 · **RN:** RN-AUD-001, RN-AUD-003 · **KPI:** —  
**Origen (SPEC):** `[DC-06]`

**Historia.** **COMO** Administrador **QUIERO** que los datos del sistema puedan alimentar nuestra herramienta analítica **PARA** construir allí los tableros que necesitemos.

```gherkin
@HU-REP-003 @Should @M-16
Característica: HU-REP-003 — Alimentar la herramienta analítica externa con los datos del sistema
  # Criterio SPEC (1): El sistema expone los datos de forma estructurada y consistente.
  Escenario: C1 · El sistema expone los datos de forma estructurada y consistente
    Dada la exportación analítica habilitada
    Cuando la herramienta externa consume los datos
    Entonces el sistema los expone de forma estructurada y consistente
  # Criterio SPEC (2): `[DC-06]` Este documento no diseña los tableros analíticos: solo garantiza la disponibilidad de los datos.
  Escenario: C2 · El sistema no diseña los tableros analíticos
    Dado el alcance del sistema
    Cuando se revisan sus funciones de reportes
    Entonces solo garantiza la disponibilidad de los datos y no incluye el diseño de tableros analíticos
  # Criterio SPEC (3): La habilitación de la exportación es exclusiva del Administrador.
  Escenario: C3 · La habilitación de la exportación es exclusiva del Administrador
    Dado un usuario con rol distinto de Administrador
    Cuando intenta habilitar la exportación analítica
    Entonces el sistema no se lo permite
  # Criterio SPEC (4): Toda extracción queda en la bitácora.
  Escenario: C4 · Toda extracción queda en bitácora
    Dada una extracción de datos
    Cuando se completa
    Entonces queda en la bitácora con usuario, alcance y fecha
  # Criterio SPEC (5): Los datos exportados respetan las restricciones de visibilidad por rol.
  Escenario: C5 · Los datos exportados respetan las restricciones de visibilidad por rol
    Dados datos restringidos según el rol
    Cuando se exportan
    Entonces respetan las mismas restricciones de visibilidad por rol
```

### HU-REP-004 — Programar la generación periódica de reportes

**Prioridad:** Could (P2) · **Horizonte:** H2 · **Actor (SPEC):** Jefe · **Legacy:** HU-090  
**Depende de:** HU-REP-001 · **RF:** RF-REP-007 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que ciertos reportes se generen solos cada semana **PARA** no tener que acordarme de pedirlos.

```gherkin
@HU-REP-004 @Could @M-16
Característica: HU-REP-004 — Programar la generación periódica de reportes
  # Criterio SPEC (1): Se programa reporte, periodicidad y destinatarios.
  Escenario: C1 · Se programa reporte, periodicidad y destinatarios
    Dado el Jefe programando un reporte
    Cuando define el reporte, la periodicidad y los destinatarios
    Entonces la programación queda guardada
  # Criterio SPEC (2): El sistema lo genera y lo pone a disposición del destinatario.
  Escenario: C2 · El sistema lo genera y lo pone a disposición del destinatario
    Dado un reporte programado que llega a su fecha
    Cuando el sistema lo ejecuta
    Entonces lo genera y lo pone a disposición de los destinatarios
  # Criterio SPEC (3): La generación programada queda registrada.
  Escenario: C3 · La generación programada queda registrada
    Dada una generación programada ejecutada
    Cuando se consulta el registro
    Entonces la generación figura registrada
  # Criterio SPEC (4): La programación puede desactivarse.
  Escenario: C4 · La programación puede desactivarse
    Dada una programación existente
    Cuando el Jefe la desactiva
    Entonces el sistema deja de generar ese reporte
```


## 5.19 M-17 · Dashboard Operativo (dominio DSH)

### HU-DSH-001 — Ver de un vistazo el estado de la bodega

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe · **Legacy:** HU-091  
**Depende de:** HU-INV-001, HU-ALE-001 · **RF:** RF-DSH-001, RF-DSH-002 · **RN:** — · **KPI:** KPI-01  
**Origen (SPEC):** `[DC-02]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** ver de un vistazo el estado de la bodega al llegar **PARA** saber qué requiere mi atención hoy.

```gherkin
@HU-DSH-001 @Should @M-17
Característica: HU-DSH-001 — Ver de un vistazo el estado de la bodega
  # Criterio SPEC (1): Muestra existencia total y desglose por estado.
  Escenario: C1 · Muestra existencia total y desglose por estado
    Dado el Jefe abriendo el dashboard operativo
    Cuando se presenta
    Entonces muestra la existencia total y su desglose por estado
  # Criterio SPEC (2): Muestra alertas activas por severidad.
  Escenario: C2 · Muestra alertas activas por severidad
    Dadas alertas activas
    Cuando se presenta el dashboard
    Entonces las muestra por severidad
  # Criterio SPEC (3): Muestra pendientes: recepciones sin confirmar, en tránsito, ajustes por aprobar, conteos abiertos, novedades sin resolver.
  Escenario: C3 · Muestra pendientes de operación
    Dadas recepciones sin confirmar, tránsitos, ajustes por aprobar, conteos abiertos y novedades sin resolver
    Cuando se presenta el dashboard
    Entonces los muestra como pendientes
  # Criterio SPEC (4): Muestra la exactitud vigente (KPI-01).
  Escenario: C4 · Muestra la exactitud vigente
    Dado un indicador de exactitud del inventario calculado
    Cuando se presenta el dashboard
    Entonces muestra la exactitud vigente
  # Criterio SPEC (5): Cada elemento navega a su detalle.
  Escenario: C5 · Cada elemento navega a su detalle
    Dado un elemento del dashboard
    Cuando el Jefe lo selecciona
    Entonces el sistema navega a su detalle
```

### HU-DSH-002 — Ver mis tareas del turno en orden

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-092  
**Depende de:** HU-TAR-001 · **RF:** RF-DSH-004, RF-TAR-002, RF-TAR-003 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[MON §8.2]` `[PR-06]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** ver mis tareas del turno en orden **PARA** saber qué hacer sin que nadie tenga que decírmelo.

```gherkin
@HU-DSH-002 @Should @M-17
Característica: HU-DSH-002 — Ver mis tareas del turno en orden
  # Criterio SPEC (1): `[§2.7]` El Auxiliar ve su panel de tareas, no el dashboard operativo.
  Escenario: C1 · El Auxiliar ve su panel de tareas y no el dashboard operativo
    Dado un Auxiliar autenticado
    Cuando entra al sistema
    Entonces ve su panel de tareas y no el dashboard operativo
  # Criterio SPEC (2): Las tareas se ordenan por prioridad.
  Escenario: C2 · Las tareas se ordenan por prioridad
    Dadas varias tareas asignadas
    Cuando se presenta el panel
    Entonces se ordenan por prioridad
  # Criterio SPEC (3): Cada tarea indica qué, dónde y cuánto.
  Escenario: C3 · Cada tarea indica qué, dónde y cuánto
    Dada una tarea del panel
    Cuando se presenta
    Entonces indica qué hacer, dónde y cuánto
  # Criterio SPEC (4): La tarea se cierra al confirmarse el movimiento, no por declaración.
  Escenario: C4 · La tarea se cierra al confirmarse el movimiento, no por declaración
    Dada una tarea pendiente
    Cuando se confirma el movimiento asociado
    Entonces la tarea se cierra
    Y no puede cerrarse por declaración del usuario
  # Criterio SPEC (5): `[PR-06]` El panel no muestra indicadores de desempeño individual.
  Escenario: C5 · El panel no muestra indicadores de desempeño individual
    Dado el panel de tareas de un Auxiliar
    Cuando se presenta
    Entonces no muestra indicadores de desempeño individual
```

### HU-DSH-003 — Ver el estado de mi zona

**Prioridad:** Could (P2) · **Horizonte:** H2 · **Actor (SPEC):** Coordinador · **Legacy:** HU-093  
**Depende de:** HU-DSH-001, HU-BOD-001 · **RF:** RF-DSH-003 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[§2.7]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** ver el estado de mi zona **PARA** gestionar mi equipo sin distraerme con lo que no me corresponde.

```gherkin
@HU-DSH-003 @Could @M-17
Característica: HU-DSH-003 — Ver el estado de mi zona
  # Criterio SPEC (1): `[§2.7]` El dashboard del Coordinador se restringe a sus zonas asignadas.
  Escenario: C1 · El dashboard del Coordinador se restringe a sus zonas
    Dado un Coordinador con zonas asignadas
    Cuando abre su dashboard
    Entonces solo ve información de sus zonas
  # Criterio SPEC (2): Muestra tareas de su equipo, alertas de su zona y ocupación de sus ubicaciones.
  Escenario: C2 · Muestra tareas del equipo, alertas de la zona y ocupación
    Dado el dashboard de un Coordinador
    Cuando se presenta
    Entonces muestra las tareas de su equipo, las alertas de su zona y la ocupación de sus ubicaciones
  # Criterio SPEC (3): No muestra valorización `[PR-04]`.
  Escenario: C3 · No muestra valorización
    Dado el dashboard de un Coordinador
    Cuando se presenta
    Entonces no muestra valorización
  # Criterio SPEC (4): Permite reasignar tareas.
  Escenario: C4 · Permite reasignar tareas
    Dado el dashboard de un Coordinador
    Cuando decide reasignar una tarea de su equipo
    Entonces el sistema le permite hacerlo desde ahí
```


## 5.20 M-18 · Auditoría y Bitácora (dominio AUD)

### HU-AUD-001 — Consultar el registro de todo lo que pasó en el sistema

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auditor / Administrador · **Legacy:** HU-094  
**Depende de:** HU-ACC-001 · **RF:** RF-ACC-003, RF-AUD-001, RF-AUD-002, RF-AUD-003 · **RN:** RN-AUD-001 · **KPI:** —  
**Origen (SPEC):** `[RN-AUD-001]`

**Historia.** **COMO** Auditor **QUIERO** consultar el registro de todo lo que pasó en el sistema **PARA** verificar que las cosas se hicieron como debían.

```gherkin
@HU-AUD-001 @Should @M-18
Característica: HU-AUD-001 — Consultar el registro de todo lo que pasó en el sistema
  # Criterio SPEC (1): La bitácora registra accesos, cambios de configuración, cambios de rol, aprobaciones, rechazos, anulaciones y exportaciones.
  Escenario: C1 · La bitácora registra accesos, configuración, roles, aprobaciones, rechazos, anulaciones y exportaciones
    Dada la bitácora de auditoría
    Cuando ocurren esos tipos de evento
    Entonces todos quedan registrados
  # Criterio SPEC (2): Filtro por usuario, fecha, tipo de evento y módulo.
  Escenario: C2 · Filtro por usuario, fecha, tipo de evento y módulo
    Dada la bitácora consultada
    Cuando el usuario aplica filtros
    Entonces el sistema muestra solo los eventos que los cumplen
  # Criterio SPEC (3): `[RN-AUD-001]` La bitácora no es editable ni borrable por ningún rol, incluido el Administrador.
  Escenario: C3 · La bitácora no es editable ni borrable por ningún rol
    Dado un evento registrado en la bitácora
    Cuando cualquier usuario, incluido el Administrador, busca editarlo o borrarlo
    Entonces el sistema no ofrece esas funciones
  # Criterio SPEC (4): Toda discontinuidad detectada es un hallazgo crítico.
  Escenario: C4 · Toda discontinuidad detectada es hallazgo crítico
    Dada una discontinuidad en la bitácora
    Cuando el sistema la detecta
    Entonces la reporta como hallazgo crítico
  # Criterio SPEC (5): Es exportable.
  Escenario: C5 · La bitácora es exportable
    Dada una consulta de bitácora
    Cuando el usuario solicita exportarla
    Entonces el sistema entrega la exportación
```

### HU-AUD-002 — Consultar todo sin poder modificar nada

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auditor · **Legacy:** HU-095  
**Depende de:** HU-USR-001 · **RF:** RF-AUD-004, RF-AUD-005 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[PR-02]`

**Historia.** **COMO** Auditor **QUIERO** poder consultar absolutamente todo sin poder modificar nada **PARA** que mi revisión sea independiente y nadie dude de ella.

```gherkin
@HU-AUD-002 @Should @M-18
Característica: HU-AUD-002 — Consultar todo sin poder modificar nada
  # Criterio SPEC (1): `[PR-02]` El Auditor tiene lectura completa sobre todo el sistema.
  Escenario: C1 · El Auditor tiene lectura completa sobre todo el sistema
    Dado un usuario con rol Auditor
    Cuando consulta cualquier información del sistema
    Entonces tiene acceso de lectura completo
  # Criterio SPEC (2): `[PR-02]` El Auditor no puede ejecutar ninguna operación de escritura sobre el inventario, ni siquiera por configuración.
  Escenario: C2 · El Auditor no puede escribir sobre el inventario, ni por configuración
    Dado un usuario con rol Auditor
    Cuando intenta cualquier operación de escritura sobre el inventario
    Entonces el sistema la rechaza aun si existiera configuración que lo permitiera
  # Criterio SPEC (3): Las funciones de escritura no se le presentan.
  Escenario: C3 · Las funciones de escritura no se le presentan
    Dada la interfaz de un Auditor
    Cuando se presenta
    Entonces no muestra funciones de escritura
  # Criterio SPEC (4): Todo intento de escritura se rechaza y se registra.
  Escenario: C4 · Todo intento de escritura se rechaza y se registra
    Dado un intento de escritura de un Auditor
    Cuando el sistema lo procesa
    Entonces lo rechaza y lo registra
```

### HU-AUD-003 — Dejar registradas las observaciones de auditoría

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auditor · **Legacy:** HU-096  
**Depende de:** HU-AUD-001 · **RF:** RF-AUD-006 · **RN:** RN-AUD-002 · **KPI:** —  
**Origen (SPEC):** `[RN-AUD-002]`

**Historia.** **COMO** Auditor **QUIERO** dejar registradas mis observaciones **PARA** que quede constancia de mis hallazgos sin alterar el inventario.

```gherkin
@HU-AUD-003 @Should @M-18
Característica: HU-AUD-003 — Dejar registradas las observaciones de auditoría
  # Criterio SPEC (1): La observación se asocia a un movimiento, unidad, período o usuario.
  Escenario: C1 · La observación se asocia a un movimiento, unidad, período o usuario
    Dado el Auditor registrando una observación
    Cuando elige a qué se refiere
    Entonces puede asociarla a un movimiento, una unidad, un período o un usuario
  # Criterio SPEC (2): `[RN-AUD-002]` La observación se almacena en un registro separado y no altera el estado del inventario.
  Escenario: C2 · Se almacena en un registro separado y no altera el inventario
    Dada una observación registrada
    Cuando se guarda
    Entonces queda en un registro separado y no altera el estado del inventario
  # Criterio SPEC (3): Es consultable por el Administrador y el Jefe.
  Escenario: C3 · Es consultable por el Administrador y el Jefe
    Dada una observación registrada
    Cuando el Administrador o el Jefe la consultan
    Entonces pueden verla
  # Criterio SPEC (4): No se elimina; el Administrador o el Jefe la cierra con su respuesta `[DEC-04]`.
  Escenario: C4 · No se elimina; el Administrador o el Jefe la cierra con su respuesta
    Dada una observación registrada
    Cuando el Administrador o el Jefe la atiende
    Entonces la cierra con su respuesta y no se elimina
```

### HU-AUD-004 — Detectar si alguien aprobó su propia solicitud

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auditor · **Legacy:** HU-097  
**Depende de:** HU-AJU-002, HU-AUD-001 · **RF:** RF-AUD-007 · **RN:** RN-AJU-001, RN-AUD-001 · **KPI:** KPI-09  
**Origen (SPEC):** `[RN-AJU-001]` `[PR-01]`

**Historia.** **COMO** Auditor **QUIERO** detectar si alguien aprobó su propia solicitud **PARA** confirmar que la segregación de funciones se está cumpliendo.

```gherkin
@HU-AUD-004 @Should @M-18
Característica: HU-AUD-004 — Detectar si alguien aprobó su propia solicitud
  # Criterio SPEC (1): El sistema reporta cualquier caso donde solicitante y aprobador coincidan.
  Escenario: C1 · El sistema reporta cualquier caso donde solicitante y aprobador coincidan
    Dadas solicitudes con solicitante y aprobador
    Cuando el Auditor ejecuta el reporte
    Entonces el sistema reporta cualquier caso en que coincidan
  # Criterio SPEC (2): `[RN-AJU-001]` Si aparece algún caso, es un hallazgo crítico, porque la regla debió impedirlo.
  Escenario: C2 · Si aparece algún caso es un hallazgo crítico
    Dado un caso detectado de coincidencia entre solicitante y aprobador
    Cuando se reporta
    Entonces se clasifica como hallazgo crítico
  # Criterio SPEC (3): El reporte cubre ajustes, salidas y conteos.
  Escenario: C3 · El reporte cubre ajustes, salidas y conteos
    Dado el reporte de aprobaciones propias
    Cuando se ejecuta
    Entonces cubre ajustes, salidas y conteos
  # Criterio SPEC (4): Es exportable.
  Escenario: C4 · El reporte es exportable
    Dado el reporte generado
    Cuando el usuario solicita exportarlo
    Entonces el sistema entrega la exportación
```


## 5.21 M-19 · Parámetros y Configuración (dominio PAR)

### HU-PAR-001 — Configurar los umbrales del sistema

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-098  
**Depende de:** HU-ACC-001, HU-USR-001 · **RF:** RF-PAR-001, RF-PAR-002, RF-PAR-003, RF-PAR-004, RF-PAR-007 · **RN:** RN-AJU-002, RN-AUD-001, RN-AUD-004, RN-CNT-003, RN-MOV-008, RN-SAL-001 · **KPI:** KPI-17, KPI-24  
**Origen (SPEC):** `[CD-46]`

**Historia.** **COMO** Administrador **QUIERO** configurar los umbrales del sistema **PARA** adaptarlo a cómo trabaja realmente nuestra bodega.

```gherkin
@HU-PAR-001 @Must @M-19
Característica: HU-PAR-001 — Configurar los umbrales del sistema
  # Criterio SPEC (1): Se configuran: umbral de ajuste menor/mayor, tolerancia de conteo, tiempo máximo en tránsito, plazos de vencimiento, umbral de autorización del Coordinador.
  Escenario: C1 · Se configuran umbrales y plazos principales
    Dado el Administrador en Parámetros y Configuración
    Cuando configura el umbral de ajuste menor y mayor, la tolerancia de conteo, el tiempo máximo en tránsito, los plazos de vencimiento y el umbral de autorización del Coordinador
    Entonces el sistema guarda cada valor
  # Criterio SPEC (2): El sistema valida rangos admisibles.
  Escenario: C2 · El sistema valida rangos admisibles
    Dado un valor de configuración fuera del rango admisible
    Cuando el Administrador intenta guardarlo
    Entonces el sistema lo rechaza
  # Criterio SPEC (3): `[RN-AUD-001]` Todo cambio queda en la bitácora, con valor anterior y nuevo.
  Escenario: C3 · Todo cambio queda en bitácora con valor anterior y nuevo
    Dado un cambio de configuración guardado
    Cuando el sistema registra el evento
    Entonces la bitácora guarda el valor anterior y el valor nuevo
  # Criterio SPEC (4): El cambio surte efecto inmediato sobre las evaluaciones futuras, no retroactivamente.
  Escenario: C4 · El cambio aplica a evaluaciones futuras, no retroactivamente
    Dado un cambio de configuración guardado
    Cuando el sistema evalúa situaciones posteriores
    Entonces aplica el nuevo valor solo hacia adelante y no de forma retroactiva
```

### HU-PAR-002 — Mantener la lista de motivos tipificados

**Prioridad:** Must (P0) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-099  
**Depende de:** HU-USR-001 · **RF:** RF-PAR-005 · **RN:** RN-AJU-003, RN-MAE-007 · **KPI:** —  
**Origen (SPEC):** `[CD-36]`

**Historia.** **COMO** Administrador **QUIERO** mantener la lista de motivos tipificados **PARA** que las razones de ajuste y salida sean consistentes y comparables.

```gherkin
@HU-PAR-002 @Must @M-19
Característica: HU-PAR-002 — Mantener la lista de motivos tipificados
  # Criterio SPEC (1): Se administran motivos por tipo de operación.
  Escenario: C1 · Se administran motivos por tipo de operación
    Dado el Administrador en el catálogo de motivos
    Cuando crea o edita motivos
    Entonces los organiza por tipo de operación
  # Criterio SPEC (2): Se indica si el motivo exige evidencia adjunta.
  Escenario: C2 · Se indica si el motivo exige evidencia adjunta
    Dado un motivo en configuración
    Cuando el Administrador define si exige evidencia
    Entonces el sistema guarda ese requisito
  # Criterio SPEC (3): `[RN-MAE-007]` Un motivo en uso no se elimina, se desactiva.
  Escenario: C3 · Un motivo en uso no se elimina, se desactiva
    Dado un motivo utilizado en operaciones
    Cuando el Administrador intenta eliminarlo
    Entonces el sistema solo permite desactivarlo
  # Criterio SPEC (4): Un motivo desactivado no aparece en nuevas operaciones pero sí en el histórico.
  Escenario: C4 · Un motivo desactivado no aparece en operaciones nuevas pero sí en el histórico
    Dado un motivo desactivado
    Cuando se crean operaciones nuevas y se consulta el histórico
    Entonces no aparece en las operaciones nuevas y sí en el histórico
  # Criterio SPEC (5): El texto libre nunca sustituye al motivo tipificado `[RN-AJU-003]`.
  Escenario: C5 · El texto libre nunca sustituye al motivo tipificado
    Dada una operación que exige motivo tipificado
    Cuando el usuario ingresa solo texto libre
    Entonces el sistema no lo acepta como sustituto del motivo
```

### HU-PAR-003 — Impedir configurar algo que rompa los controles del sistema

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Administrador · **Legacy:** HU-100  
**Depende de:** HU-PAR-001 · **RF:** RF-PAR-006 · **RN:** RN-AJU-001, RN-AJU-003, RN-AUD-001, RN-CNT-002, RN-CNT-003, RN-EXI-001, RN-INT-001, RN-INT-002, RN-INT-004, RN-MAE-007 · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Administrador **QUIERO** que el sistema me impida configurar algo que rompa sus controles **PARA** no debilitar por accidente la seguridad del inventario.

```gherkin
@HU-PAR-003 @Should @M-19
Característica: HU-PAR-003 — Impedir configurar algo que rompa los controles del sistema
  # Criterio SPEC (1): Las reglas estructurales del Cap. 9 marcadas como no configurables no aparecen como parametrizables.
  Escenario: C1 · Las reglas estructurales no aparecen como parametrizables
    Dado el Administrador en Parámetros y Configuración
    Cuando revisa lo configurable
    Entonces las reglas estructurales marcadas como no configurables no aparecen como parametrizables
  # Criterio SPEC (2): Entre ellas: prohibición de existencia negativa `[RN-EXI-001]`, inmutabilidad del kardex `[RN-INT-002]`, prohibición de aprobar la propia solicitud `[RN-AJU-001]`, restricción de escritura del Auditor `[PR-02]`.
  Escenario: C2 · Entre ellas: existencia negativa, kardex, aprobación propia y escritura del Auditor
    Dadas las reglas estructurales no configurables
    Cuando el Administrador busca modificar la prohibición de existencia negativa, la inmutabilidad del kardex, la prohibición de aprobar la propia solicitud o la restricción de escritura del Auditor
    Entonces el sistema no las ofrece como configurables
  # Criterio SPEC (3): El intento de eludirlas se rechaza y se registra.
  Escenario: C3 · El intento de eludirlas se rechaza y se registra
    Dado un intento de eludir una regla estructural
    Cuando el sistema lo procesa
    Entonces lo rechaza y lo registra
```


## 5.22 M-20 · Notificaciones y Tareas (dominio TAR)

### HU-TAR-001 — Recibir las tareas en la tablet

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Auxiliar · **Legacy:** HU-101  
**Depende de:** HU-ACC-001 · **RF:** RF-TAR-001, RF-TAR-002, RF-TAR-003, RF-TAR-005 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[DC-05]`

**Historia.** **COMO** Auxiliar de Bodega **QUIERO** recibir mis tareas en la tablet **PARA** trabajar sin depender de que alguien venga a decirme qué hacer.

```gherkin
@HU-TAR-001 @Should @M-20
Característica: HU-TAR-001 — Recibir las tareas en la tablet
  # Criterio SPEC (1): Las tareas asignadas aparecen en su panel.
  Escenario: C1 · Las tareas asignadas aparecen en el panel del Auxiliar
    Dada una tarea asignada a un Auxiliar
    Cuando abre su panel
    Entonces la tarea aparece en él
  # Criterio SPEC (2): Cada tarea indica tipo, referencia, cantidad y ubicación.
  Escenario: C2 · Cada tarea indica tipo, referencia, cantidad y ubicación
    Dada una tarea en el panel
    Cuando se presenta
    Entonces indica tipo, referencia, cantidad y ubicación
  # Criterio SPEC (3): `[DC-05]` Las notificaciones viven dentro del sistema web; no hay aplicación móvil nativa.
  Escenario: C3 · Las notificaciones viven dentro del sistema web, sin aplicación móvil nativa
    Dado el envío de una notificación
    Cuando el usuario la recibe
    Entonces la recibe dentro del sistema web sin requerir una aplicación móvil nativa
  # Criterio SPEC (4): La tarea se cierra al confirmarse el movimiento asociado.
  Escenario: C4 · La tarea se cierra al confirmarse el movimiento asociado
    Dada una tarea pendiente
    Cuando se confirma el movimiento asociado
    Entonces la tarea se cierra
  # Criterio SPEC (5): Las tareas no vistas se destacan.
  Escenario: C5 · Las tareas no vistas se destacan
    Dadas tareas que el usuario aún no ha visto
    Cuando se presenta el panel
    Entonces las destaca
```

### HU-TAR-002 — Recibir las solicitudes que requieren mi aprobación

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe / Administrador · **Legacy:** HU-102  
**Depende de:** HU-AJU-002, HU-TAR-001 · **RF:** RF-AJU-004, RF-AJU-008 · **RN:** RN-AJU-002, RN-AJU-005, RN-AJU-006 · **KPI:** KPI-22  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que me lleguen las solicitudes que requieren mi aprobación **PARA** no ser el cuello de botella de la operación.

```gherkin
@HU-TAR-002 @Should @M-20
Característica: HU-TAR-002 — Recibir las solicitudes que requieren mi aprobación
  # Criterio SPEC (1): Las solicitudes de ajuste y salida pendientes aparecen en su panel.
  Escenario: C1 · Las solicitudes pendientes aparecen en el panel del Jefe
    Dadas solicitudes de ajuste y de salida pendientes
    Cuando el Jefe abre su panel
    Entonces aparecen en él
  # Criterio SPEC (2): Se ordenan por antigüedad y monto.
  Escenario: C2 · Se ordenan por antigüedad y monto
    Dadas varias solicitudes pendientes
    Cuando se presenta el panel
    Entonces se ordenan por antigüedad y monto
  # Criterio SPEC (3): El solicitante es notificado del resultado.
  Escenario: C3 · El solicitante es notificado del resultado
    Dada una solicitud resuelta
    Cuando el Jefe la aprueba o rechaza
    Entonces el solicitante recibe la notificación del resultado
  # Criterio SPEC (4): Las solicitudes sin resolver escalan por plazo `[RN-AJU-005]`.
  Escenario: C4 · Las solicitudes sin resolver escalan por plazo
    Dada una solicitud sin resolver que supera el plazo configurado
    Cuando el sistema evalúa el plazo
    Entonces la solicitud escala automáticamente
```

### HU-TAR-003 — Reasignar tareas entre auxiliares

**Prioridad:** Could (P2) · **Horizonte:** H2 · **Actor (SPEC):** Coordinador · **Legacy:** HU-103  
**Depende de:** HU-TAR-001 · **RF:** RF-TAR-004 · **RN:** RN-CNT-003 · **KPI:** —  
**Origen (SPEC):** `[NUEVO]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** reasignar tareas entre mis auxiliares **PARA** equilibrar la carga del turno.

```gherkin
@HU-TAR-003 @Could @M-20
Característica: HU-TAR-003 — Reasignar tareas entre auxiliares
  # Criterio SPEC (1): La reasignación se hace desde el panel del Coordinador.
  Escenario: C1 · La reasignación se hace desde el panel del Coordinador
    Dado el Coordinador en su panel
    Cuando decide reasignar una tarea
    Entonces puede hacerlo desde ese panel
  # Criterio SPEC (2): Ambos responsables quedan registrados.
  Escenario: C2 · Ambos responsables quedan registrados
    Dada una tarea reasignada
    Cuando se consulta su historial
    Entonces quedan registrados ambos responsables
  # Criterio SPEC (3): El nuevo responsable es notificado.
  Escenario: C3 · El nuevo responsable es notificado
    Dada una tarea reasignada
    Cuando se completa la reasignación
    Entonces el nuevo responsable recibe una notificación
  # Criterio SPEC (4): La reasignación no puede violar la regla del segundo conteo `[RN-CNT-003]`.
  Escenario: C4 · La reasignación no puede violar la regla del segundo conteo
    Dada una tarea de segundo conteo
    Cuando se intenta reasignar a quien hizo el primer conteo
    Entonces el sistema lo impide
```

### HU-TAR-004 — Consolidar el cierre de la jornada y traspasar los pendientes

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Coordinador / Jefe · **Legacy:** HU-113  
**Depende de:** HU-TAR-001 · **RF:** RF-TAR-006, RF-TAR-007 · **RN:** — · **KPI:** —  
**Origen (SPEC):** `[PN-14]` `[DEC-05]`

**Historia.** **COMO** Coordinador de Bodega **QUIERO** ver al cierre de la jornada qué quedó pendiente y traspasarlo explícitamente al turno siguiente **PARA** que nada quede oculto ni sin responsable.

```gherkin
@HU-TAR-004 @Should @M-20
Característica: HU-TAR-004 — Consolidar el cierre de la jornada y traspasar los pendientes
  # Criterio SPEC (1): El sistema consolida los movimientos de la jornada.
  Escenario: C1 · El sistema consolida los movimientos de la jornada
    Dada una jornada con movimientos registrados
    Cuando el Coordinador inicia el cierre
    Entonces el sistema consolida los movimientos de la jornada
  # Criterio SPEC (2): Lista las recepciones sin confirmar, los movimientos en tránsito, las tareas de conteo abiertas, los ajustes sin resolver, las novedades sin atender y las alertas activas.
  Escenario: C2 · Lista los pendientes
    Dado un cierre de jornada en curso
    Cuando el sistema identifica los pendientes
    Entonces lista recepciones sin confirmar, movimientos en tránsito, tareas de conteo abiertas, ajustes sin resolver, novedades sin atender y alertas activas
  # Criterio SPEC (3): Lo que no se resuelve en el turno se traspasa explícitamente al turno siguiente.
  Escenario: C3 · Lo no resuelto se traspasa explícitamente al turno siguiente
    Dado pendientes que no se resolvieron en el turno
    Cuando el Coordinador cierra la jornada
    Entonces los pendientes se traspasan de forma explícita al turno siguiente
  # Criterio SPEC (4): El cierre queda registrado con quién lo ejecutó `[PR-05]`.
  Escenario: C4 · El cierre queda registrado con quién lo ejecutó
    Dado un cierre de jornada confirmado
    Cuando se consulta el registro
    Entonces muestra quién lo ejecutó
  # Criterio SPEC (5): El Jefe ve el resumen de la jornada.
  Escenario: C5 · El Jefe ve el resumen de la jornada
    Dada una jornada cerrada
    Cuando el Jefe consulta el resumen
    Entonces ve los movimientos, los pendientes y su traspaso
```

### HU-TAR-005 — Impedir cerrar la jornada con registros sin sincronizar

**Prioridad:** Should (P1) · **Horizonte:** H1 · **Actor (SPEC):** Jefe · **Legacy:** HU-114  
**Depende de:** HU-TAR-004 · **RF:** RF-TAR-008 · **RN:** RN-INT-003 · **KPI:** —  
**Origen (SPEC):** `[PN-14]` `[RN-INT-003]` `[DEC-05]`

**Historia.** **COMO** Jefe de Bodega **QUIERO** que el sistema no deje cerrar la jornada con registros sin sincronizar y me avise si no se cerró **PARA** que el cierre refleje siempre lo que realmente pasó.

```gherkin
@HU-TAR-005 @Should @M-20
Característica: HU-TAR-005 — Impedir cerrar la jornada con registros sin sincronizar
  # Criterio SPEC (1): El sistema impide el cierre mientras haya registros sin sincronizar `[RN-INT-003]`.
  Escenario: C1 · No se cierra con registros sin sincronizar
    Dado registros retenidos sin sincronizar
    Cuando se intenta cerrar la jornada
    Entonces el sistema impide el cierre hasta sincronizar
  # Criterio SPEC (2): Un cierre no ejecutado se registra como omisión.
  Escenario: C2 · Un cierre no ejecutado se registra como omisión
    Dada una jornada que terminó sin cierre
    Cuando el sistema lo detecta
    Entonces registra el cierre como omisión
  # Criterio SPEC (3): El Jefe recibe una alerta al día siguiente por el cierre omitido.
  Escenario: C3 · El Jefe recibe una alerta al día siguiente
    Dado un cierre omitido
    Cuando comienza el día siguiente
    Entonces el Jefe recibe una alerta
  # Criterio SPEC (4): Una diferencia significativa en el consolidado genera una alerta antes de permitir el cierre.
  Escenario: C4 · Una diferencia significativa genera alerta antes del cierre
    Dado un consolidado con una diferencia significativa
    Cuando se va a permitir el cierre
    Entonces el sistema genera una alerta antes de permitirlo
```


---

**ESTADO DEL CAPÍTULO 5**

| | |
|---|---|
| **Completado** | 114 historias con ID `HU-<DOM>-nnn`, MoSCoW, horizonte, dependencias, RF/RN/KPI relacionados y 515 escenarios Gherkin (1 por criterio del SPEC) |
| **Pendiente** | Validación de los mapeos `[SRS]` por el Director (R-S02) · cobertura RF parcial de HU-NOV-003 y HU-NOV-004 (H-13, DEC-06) |
| **Riesgos encontrados** | H-05 (dos criterios del SPEC citaban un RNF equivocado; se redactaron sin la referencia errónea) · los escenarios no sustituyen las pruebas de usabilidad (R-S09) |
| **Dependencias** | Cap. 6 (RF), Cap. 8 (reglas), Cap. 9 (trazabilidad) |


---

# CAPÍTULO 6 — REQUISITOS FUNCIONALES NORMALIZADOS

> Reorganización de los **185 RF** del SPEC (Cap. 7) con ID permanente `RF-<DOM>-nnn`. Cada RF indica actor, historia(s) relacionada(s), prioridad, regla(s) de negocio y KPI relacionados. La redacción del requisito, su actor, su prioridad, sus dependencias y su origen **se reproducen del SPEC**; la historia, la regla y el KPI relacionados son derivados de esta fase `[SRS]` (las reglas incluyen todas las que el SPEC cita en el propio requisito). **Ningún RF se perdió** (Anexo A). Los RF que no se relacionan con ningún KPI o regla muestran «—».

## 6.1 Distribución


| Módulo | Dominio | RF | Must | Should | Could | H2 | Rango legacy |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **M-01** Acceso y Autenticación | ACC | 7 | 4 | 2 | 1 | 0 | RF-001–RF-007 |
| **M-02** Usuarios y Roles | USR | 8 | 4 | 3 | 1 | 0 | RF-008–RF-015 |
| **M-03** Catálogo de Referencias | CAT | 10 | 5 | 3 | 2 | 1 | RF-016–RF-025 |
| **M-04** Gestión de Lotes | LOT | 6 | 3 | 2 | 1 | 2 | RF-026–RF-031 |
| **M-05** Estructura de Bodega | BOD | 9 | 4 | 4 | 1 | 1 | RF-032–RF-172 |
| **M-06** Identificación QR | QRC | 9 | 4 | 4 | 1 | 1 | RF-040–RF-179 |
| **M-07** Entradas y Recepción | ENT | 17 | 10 | 5 | 2 | 0 | RF-048–RF-180 |
| **M-08** Salidas | SAL | 14 | 9 | 5 | 0 | 0 | RF-061–RF-176 |
| **M-09** Movimientos y Transferencias | MOV | 13 | 6 | 7 | 0 | 5 | RF-072–RF-173 |
| **M-10** Ajustes de Inventario | AJU | 10 | 6 | 3 | 1 | 1 | RF-083–RF-092 |
| **M-11** Conteos | CNT | 15 | 4 | 10 | 1 | 3 | RF-093–RF-175 |
| **M-12** Novedades de Mercancía | NOV | 8 | 1 | 6 | 1 | 0 | RF-106–RF-177 |
| **M-13** Consulta de Existencia | INV | 9 | 6 | 2 | 1 | 1 | RF-112–RF-171 |
| **M-14** Kardex y Trazabilidad | KDX | 9 | 6 | 3 | 0 | 0 | RF-120–RF-178 |
| **M-15** Alertas y Reglas | ALE | 7 | 1 | 5 | 1 | 1 | RF-127–RF-133 |
| **M-16** Reportes y Exportación Analítica | REP | 8 | 1 | 5 | 2 | 3 | RF-134–RF-185 |
| **M-17** Dashboard Operativo | DSH | 4 | 0 | 3 | 1 | 1 | RF-141–RF-144 |
| **M-18** Auditoría y Bitácora | AUD | 7 | 3 | 4 | 0 | 0 | RF-145–RF-151 |
| **M-19** Parámetros y Configuración | PAR | 7 | 4 | 2 | 1 | 0 | RF-152–RF-181 |
| **M-20** Notificaciones y Tareas | TAR | 8 | 1 | 6 | 1 | 1 | RF-158–RF-184 |
| **Total** | | **185** | **82** | **84** | **19** | **21** | RF-001–RF-185 |

> **Hallazgo H-02.** El resumen del SPEC (§7.1) declara 72 P0 / 69 P1 / 21 P2; las filas de los requisitos suman **74 / 70 / 18**. Este SRS usa la prioridad de cada fila.


## 6.2 M-01 · Acceso y Autenticación (dominio ACC)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-ACC-001**<br>*(RF-001)* | El sistema debe autenticar a cada usuario mediante credencial individual antes de permitir cualquier operación | Todos | HU-ACC-001 | Must<br>P0 | RN-INT-001 | — | M-02 | `[PR-05]` |
| **RF-ACC-002**<br>*(RF-002)* | El sistema no debe admitir cuentas genéricas, compartidas ni acceso anónimo a ninguna función | — | HU-ACC-001 | Must<br>P0 | RN-INT-001 | — | RF-ACC-001 | `[PR-05]` |
| **RF-ACC-003**<br>*(RF-003)* | El sistema debe registrar en la bitácora todo acceso exitoso y todo intento fallido, con fecha, hora y origen | — | HU-ACC-001, HU-AUD-001 | Must<br>P0 | RN-AUD-001 | — | M-18 | `[NUEVO]` |
| **RF-ACC-004**<br>*(RF-004)* | El sistema debe bloquear la cuenta tras el número configurado de intentos fallidos consecutivos y notificar al Administrador | — | HU-ACC-001 | Must<br>P0 | — | — | RF-ACC-003, M-19 | `[NUEVO]` |
| **RF-ACC-005**<br>*(RF-005)* | El sistema debe cerrar la sesión automáticamente tras el tiempo de inactividad configurado, avisando previamente al usuario | Todos | HU-ACC-002 | Should<br>P1 | — | — | M-19 | `[DC-05]` |
| **RF-ACC-006**<br>*(RF-006)* | El sistema debe permitir al usuario cambiar su propia contraseña, exigiendo la actual y aplicando la política mínima configurada | Todos | HU-ACC-003 | Should<br>P1 | — | — | RF-ACC-001 | `[NUEVO]` |
| **RF-ACC-007**<br>*(RF-007)* | El sistema debe permitir al Administrador restablecer el acceso de una cuenta bloqueada sin revelar jamás la contraseña anterior | Administrador | HU-ACC-004 | Could<br>P2 | — | — | RF-ACC-004 | `[NUEVO]` |

## 6.3 M-02 · Usuarios y Roles (dominio USR)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-USR-001**<br>*(RF-008)* | El sistema debe permitir al Administrador crear usuarios con datos de identificación | Administrador | HU-USR-001 | Must<br>P0 | RN-INT-001, RN-MAE-006 | — | M-01 | `[DC-04]` |
| **RF-USR-002**<br>*(RF-009)* | El sistema debe ofrecer exclusivamente los cinco roles oficiales y **no debe permitir crear roles adicionales** | Administrador | HU-USR-001 | Must<br>P0 | — | — | RF-USR-001 | `[DC-04]` |
| **RF-USR-003**<br>*(RF-010)* | El sistema debe asignar exactamente un rol activo por usuario | Administrador | HU-USR-001 | Must<br>P0 | — | — | RF-USR-002 | `[DC-04]` |
| **RF-USR-004**<br>*(RF-011)* | El sistema debe permitir desactivar y reactivar usuarios, **sin ofrecer nunca la eliminación** | Administrador | HU-USR-002 | Must<br>P0 | RN-MAE-007, RN-MAE-008, RN-MAE-009 | — | RN-MAE-007 | `[RN-MAE-007]` |
| **RF-USR-005**<br>*(RF-012)* | El sistema debe conservar íntegros los movimientos históricos de un usuario desactivado, mostrando su identidad | — | HU-USR-002 | Should<br>P1 | RN-MAE-007, RN-MAE-008 | — | RF-USR-004, M-14 | `[MON §7.1]` |
| **RF-USR-006**<br>*(RF-013)* | El sistema debe impedir desactivar o cambiar de rol al último Administrador activo | Administrador | HU-USR-005, HU-USR-003 | Should<br>P1 | RN-MAE-004 | — | RF-USR-004 | `[RN-MAE-004]` |
| **RF-USR-007**<br>*(RF-014)* | El sistema debe permitir asignar bodega y zonas de ámbito a cada usuario, y filtrar consultas y tareas por ese ámbito | Administrador | HU-USR-004 | Should<br>P1 | — | — | M-05 | `[NUEVO]` |
| **RF-USR-008**<br>*(RF-015)* | El sistema debe registrar todo cambio de rol y de estado de usuario en la bitácora, con valor anterior y nuevo | — | HU-USR-003 | Could<br>P2 | RN-AUD-001 | — | M-18 | `[NUEVO]` |

## 6.4 M-03 · Catálogo de Referencias (dominio CAT)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-CAT-001**<br>*(RF-016)* | El sistema debe permitir crear referencias con código único, descripción y categoría | Admin / Jefe | HU-CAT-001 | Must<br>P0 | RN-MAE-001 | — | — | `[NUEVO]` `[D-01]` |
| **RF-CAT-002**<br>*(RF-017)* | El sistema debe rechazar la creación de una referencia con código ya existente | — | HU-CAT-001 | Must<br>P0 | RN-MAE-001 | — | RF-CAT-001 | `[RN-MAE-001]` |
| **RF-CAT-003**<br>*(RF-018)* | El sistema debe permitir asociar a cada referencia su conjunto aplicable de tallas y de colores | Admin / Jefe | HU-CAT-001 | Must<br>P0 | — | — | RF-CAT-001 | `[NUEVO]` `[D-01]` |
| **RF-CAT-004**<br>*(RF-019)* | El sistema debe generar automáticamente los SKU resultantes de la combinación referencia + talla + color | — | HU-CAT-001 | Must<br>P0 | — | — | RF-CAT-003 | `[CD-05]` |
| **RF-CAT-005**<br>*(RF-020)* | El sistema debe permitir asignar una unidad de medida por referencia e **impedir su cambio si existen movimientos** | Admin / Jefe | HU-CAT-002 | Must<br>P0 | RN-INT-007, RN-MAE-002 | — | M-14 | `[RN-MAE-002]` |
| **RF-CAT-006**<br>*(RF-021)* | El sistema debe permitir desactivar referencias y **rechazar la desactivación si la existencia es distinta de cero** | Admin / Jefe | HU-CAT-003 | Should<br>P1 | RN-MAE-003 | — | M-13 | `[RN-MAE-003]` |
| **RF-CAT-007**<br>*(RF-022)* | El sistema debe permitir definir existencia mínima y máxima por SKU, validando que el mínimo no supere al máximo | Admin / Jefe | HU-CAT-004 | Should<br>P1 | — | — | RF-CAT-004 | `[MON §3, §7.1]` |
| **RF-CAT-008**<br>*(RF-023)* | El sistema debe listar los SKU sin umbrales configurados como pendientes de parametrización | Admin / Jefe | HU-CAT-004 | Could<br>P2 | — | — | RF-CAT-007 | `[NUEVO]` |
| **RF-CAT-009**<br>*(RF-024)* | El sistema debe permitir la carga masiva del catálogo inicial, validando previamente y reportando errores por línea | Administrador | HU-CAT-005 | Should<br>P1 · H2 | — | — | RF-CAT-001 | `[NUEVO]` |
| **RF-CAT-010**<br>*(RF-025)* | El sistema debe permitir administrar categorías y asociarlas a una zona preferente para asignación automática | Admin / Jefe | HU-CAT-006 | Could<br>P2 | — | — | M-05 | `[NUEVO]` |

## 6.5 M-04 · Gestión de Lotes (dominio LOT)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-LOT-001**<br>*(RF-026)* | El sistema debe crear o asociar un lote al confirmar toda entrada, registrando origen y fecha de ingreso | Coordinador | HU-LOT-001 | Must<br>P0 | RN-LOT-001 | — | M-07 | `[MON §7.1]` |
| **RF-LOT-002**<br>*(RF-027)* | El sistema debe garantizar que ninguna existencia quede sin lote asociado | — | HU-LOT-001 | Must<br>P0 | RN-LOT-001 | — | RF-LOT-001 | `[MON §7.1]` |
| **RF-LOT-003**<br>*(RF-028)* | El sistema debe garantizar la unicidad del código de lote dentro de su SKU | — | HU-LOT-001 | Must<br>P0 | RN-MAE-006 | — | RF-LOT-001 | `[RN-MAE-006]` |
| **RF-LOT-004**<br>*(RF-029)* | El sistema debe permitir consultar la distribución de un lote en todas sus ubicaciones, con cantidad y estado | Jefe / Coord. | HU-LOT-002 | Should<br>P1 | RN-LOT-002 | — | M-13 | `[MON §7.1]` |
| **RF-LOT-005**<br>*(RF-030)* | El sistema debe permitir inmovilizar y liberar un lote completo, afectando toda su existencia en todas sus ubicaciones | Jefe / Admin | HU-LOT-003 | Should<br>P1 · H2 | RN-EXI-006, RN-LOT-003, RN-LOT-004 | — | RN-EXI-006 | `[RN-EXI-006]` |
| **RF-LOT-006**<br>*(RF-031)* | El sistema debe permitir listar lotes por antigüedad, mostrando días en bodega y destacando los que superan el umbral | Jefe | HU-LOT-004 | Could<br>P2 · H2 | RN-LOT-005 | — | RF-LOT-001, M-19 | `[NUEVO]` |

## 6.6 M-05 · Estructura de Bodega (dominio BOD)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-BOD-001**<br>*(RF-032)* | El sistema debe permitir crear bodegas, zonas con tipo asignado y ubicaciones dentro de zona | Administrador | HU-BOD-001 | Must<br>P0 | RN-EXI-002, RN-MAE-006 | — | — | `[NUEVO]` |
| **RF-BOD-002**<br>*(RF-033)* | El sistema debe garantizar la unicidad del código de ubicación dentro de su bodega | — | HU-BOD-001 | Must<br>P0 | RN-MAE-006 | — | RF-BOD-001 | `[RN-MAE-006]` |
| **RF-BOD-003**<br>*(RF-034)* | El sistema debe exigir la existencia de al menos una zona de recepción por bodega | Administrador | HU-BOD-001 | Must<br>P0 | RN-EXI-002 | — | RF-BOD-001 | `[RN-EXI-002]` |
| **RF-BOD-004**<br>*(RF-035)* | El sistema debe garantizar que toda existencia disponible resida en una ubicación identificada | — | HU-BOD-001, HU-ENT-006 | Must<br>P0 | RN-EXI-002 | — | RF-BOD-001, M-13 | `[RN-EXI-002]` |
| **RF-BOD-005**<br>*(RF-036)* | El sistema debe permitir definir la capacidad de cada ubicación y usarla al proponer destinos | Administrador | HU-BOD-002, HU-ENT-006 | Should<br>P1 | RN-MOV-002 | KPI-18 | RF-BOD-001 | `[RN-MOV-002]` |
| **RF-BOD-006**<br>*(RF-037)* | El sistema debe permitir desactivar ubicaciones y **rechazar la desactivación si tienen existencia** | Administrador | HU-BOD-003 | Should<br>P1 | RN-MAE-005 | — | M-13 | `[RN-MAE-005]` |
| **RF-BOD-007**<br>*(RF-038)* | El sistema debe permitir asignar un Coordinador responsable por zona y dirigir a él las alertas de esa zona | Administrador | HU-BOD-004 | Should<br>P1 | RN-ALE-005 | — | M-02, M-15 | `[NUEVO]` |
| **RF-BOD-008**<br>*(RF-039)* | El sistema debe permitir configurar los criterios de asignación automática de ubicación y su orden de aplicación | Administrador | HU-BOD-005, HU-ENT-006 | Could<br>P2 · H2 | RN-MOV-001 | KPI-10 | M-19 | `[NUEVO]` |
| **RF-BOD-009**<br>*(RF-172)* | El sistema debe registrar como información operativa la desviación entre la ubicación propuesta y la confirmada y notificar al Coordinador, sin imputarla al Auxiliar | — | HU-ENT-006 | Should<br>P1 | RN-MOV-003 | KPI-10 | RF-MOV-001 | `[RN-MOV-003]` `[DEC-06]` |

## 6.7 M-06 · Identificación QR (dominio QRC)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-QRC-001**<br>*(RF-040)* | El sistema debe generar un identificador QR único por SKU + Lote (no por ubicación) | Coordinador | HU-QRC-001 | Must<br>P0 | RN-IDE-001, RN-IDE-002 | — | M-07 | `[DC-08]` `[DF5-01]` |
| **RF-QRC-002**<br>*(RF-041)* | El sistema debe garantizar que **ningún identificador se repita jamás, ni tras su anulación** | — | HU-QRC-001 | Must<br>P0 | RN-IDE-002 | — | RF-QRC-001 | `[RN-IDE-002]` |
| **RF-QRC-003**<br>*(RF-042)* | El sistema debe permitir el escaneo de identificadores desde tablet y resolverlos a su SKU + Lote y, junto con la ubicación, a la unidad de inventario | Auxiliar | HU-QRC-002 | Must<br>P0 | RN-IDE-001 | KPI-07 | `[DC-05]` | `[DC-08]` `[DF5-01]` |
| **RF-QRC-004**<br>*(RF-043)* | El sistema debe generar un identificador QR propio para cada ubicación, distinguible del de mercancía | Administrador | HU-QRC-003 | Must<br>P0 | RN-IDE-002 | — | M-05 | `[NUEVO]` |
| **RF-QRC-005**<br>*(RF-044)* | El sistema debe permitir la impresión individual y por lote de impresión, incluyendo información legible de respaldo | Coordinador | HU-QRC-001 | Should<br>P1 | — | — | RF-QRC-001 | `[NUEVO]` |
| **RF-QRC-006**<br>*(RF-045)* | El sistema debe permitir la reimpresión con motivo obligatorio, **conservando el mismo QR y sin crear una nueva identidad** | Coord. / Aux. | HU-QRC-004 | Should<br>P1 | RN-IDE-004 | — | M-14 | `[RN-IDE-004]` `[Q-09]` |
| **RF-QRC-007**<br>*(RF-046)* | El sistema debe marcar como reemplazado el identificador sustituido, **sin eliminarlo**, y conservar el historial consultable | — | HU-QRC-004 | Should<br>P1 | RN-IDE-004 | — | RF-QRC-006 | `[RN-IDE-004]` |
| **RF-QRC-008**<br>*(RF-047)* | El sistema debe permitir asociar un identificador secundario de código de barras, **habilitado solo para consulta, nunca para escritura** | Coordinador | HU-QRC-005 | Could<br>P2 · H2 | RN-IDE-003 | — | RF-QRC-001 | `[DC-08]` `[RN-IDE-003]` |
| **RF-QRC-009**<br>*(RF-179)* | El sistema debe registrar en cada movimiento si la identificación se hizo por escaneo o por selección manual | — | HU-QRC-002 | Should<br>P1 | — | KPI-07 | RF-QRC-003, RF-KDX-001 | `[KPI-07]` `[DEC-06]` |

## 6.8 M-07 · Entradas y Recepción (dominio ENT)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-ENT-001**<br>*(RF-048)* | El sistema debe permitir crear documentos de entrada con origen, fecha esperada y líneas de referencia, talla, color y cantidad | Coordinador | HU-ENT-001 | Must<br>P0 | — | KPI-12 | M-03 | `[MON §8.2]` |
| **RF-ENT-002**<br>*(RF-049)* | El documento de entrada **no debe solicitar precio, condiciones comerciales ni datos de orden de compra** | — | HU-ENT-001 | Must<br>P0 | — | — | RF-ENT-001 | `[DC-03]` |
| **RF-ENT-003**<br>*(RF-050)* | El sistema debe admitir en el documento de entrada únicamente referencias activas del catálogo | — | HU-ENT-007 | Must<br>P0 | RN-ENT-001, RN-MAE-001 | — | RF-CAT-006 | `[RN-MAE-001]` |
| **RF-ENT-004**<br>*(RF-051)* | El sistema debe advertir de posible duplicado cuando exista otro documento con mismo origen, referencia y fecha | Coordinador | HU-ENT-001 | Could<br>P2 | RN-ENT-002 | — | RF-ENT-001 | `[RN-ENT-002]` |
| **RF-ENT-005**<br>*(RF-052)* | El sistema debe permitir registrar la recepción física por línea desde tablet, en el punto de recepción | Auxiliar | HU-ENT-002 | Must<br>P0 | RN-INT-003, RN-INT-008 | — | `[DC-05]` | `[MON §3, §8.2]` |
| **RF-ENT-006**<br>*(RF-053)* | El sistema debe permitir interrumpir y continuar una recepción, incluso por otro usuario, registrando a ambos | Auxiliar | HU-ENT-002 | Should<br>P1 | — | — | RF-ENT-005 | `[NUEVO]` |
| **RF-ENT-007**<br>*(RF-054)* | El sistema debe comparar automáticamente cantidad recibida contra esperada, línea por línea | — | HU-ENT-004 | Must<br>P0 | RN-ENT-003 | — | RF-ENT-005 | `[RN-ENT-003]` |
| **RF-ENT-008**<br>*(RF-055)* | El sistema debe registrar faltante de recepción y notificar al Jefe cuando lo recibido sea menor que lo esperado | — | HU-ENT-004 | Should<br>P1 | RN-ENT-004 | — | RF-ENT-007, M-20 | `[RN-ENT-004]` |
| **RF-ENT-009**<br>*(RF-056)* | El sistema debe **exigir autorización del Jefe antes de confirmar** una entrada con sobrante | Jefe | HU-ENT-004 | Must<br>P0 | RN-ENT-005 | — | RF-ENT-007 | `[RN-ENT-005]` |
| **RF-ENT-010**<br>*(RF-057)* | El sistema debe **impedir que quien registró la recepción física confirme la misma entrada** | — | HU-ENT-003 | Must<br>P0 | RN-ENT-007 | — | RF-ENT-005, PR-01 | `[PR-01]` |
| **RF-ENT-011**<br>*(RF-058)* | El sistema debe generar el movimiento de entrada en el kardex e incrementar la existencia al confirmar | — | HU-ENT-003 | Must<br>P0 | RN-EXI-007, RN-INT-002, RN-INT-004 | KPI-05, KPI-11, KPI-12 | M-14 | `[MON §7.1]` |
| **RF-ENT-012**<br>*(RF-059)* | El sistema debe permitir registrar mercancía dañada por separado, **impidiendo su ingreso como disponible** | Auxiliar | HU-ENT-005 | Should<br>P1 | RN-ENT-006 | — | M-12, CD-22 | `[RN-ENT-006]` |
| **RF-ENT-013**<br>*(RF-060)* | El sistema debe permitir consultar el historial de entradas con filtro por período, origen, estado y referencia, y exportarlo | Coord. / Jefe | HU-ENT-008 | Could<br>P2 | — | — | M-16 | `[NUEVO]` |
| **RF-ENT-014**<br>*(RF-163)* | El sistema debe permitir registrar cada pieza recibida —rollo, paquete o bolsa— con su tipo y su cantidad propia, dentro de una línea de entrada | Auxiliar | HU-ENT-009 | Must<br>P0 | RN-LOT-006, RN-LOT-007 | — | RF-ENT-005, CD-49 | `[Q-11]` `[F-1]` `[F-2]` |
| **RF-ENT-015**<br>*(RF-164)* | El sistema debe derivar la cantidad recibida de cada línea como la suma de las cantidades de sus piezas y compararla contra la esperada | — | HU-ENT-009 | Must<br>P0 | RN-ENT-003, RN-LOT-007 | — | RF-ENT-014, RF-ENT-007 | `[RN-LOT-007*]` |
| **RF-ENT-016**<br>*(RF-165)* | El sistema debe permitir registrar un contenedor o bolsa agrupada como una pieza con su cantidad de unidades, perteneciente a un solo SKU + Lote | Auxiliar | HU-ENT-010 | Should<br>P1 | RN-LOT-006 | — | RF-ENT-014 | `[F-6]` |
| **RF-ENT-017**<br>*(RF-180)* | El sistema debe registrar el instante de llegada de la mercancía al documento de entrada | Auxiliar | HU-ENT-002 | Should<br>P1 | — | KPI-12 | RF-ENT-001 | `[KPI-12]` `[DEC-06]` |

## 6.9 M-08 · Salidas (dominio SAL)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-SAL-001**<br>*(RF-061)* | El sistema debe permitir solicitar salidas indicando referencias, lotes, cantidades y motivo tipificado obligatorio | Jefe / Coord. | HU-SAL-001 | Must<br>P0 | RN-SAL-002 | — | M-19 | `[RN-SAL-002]` |
| **RF-SAL-002**<br>*(RF-062)* | La salida **no debe solicitar cliente, precio, factura ni documento comercial de despacho** | — | HU-SAL-001 | Must<br>P0 | RN-SAL-002 | — | RF-SAL-001 | `[DC-03]` |
| **RF-SAL-003**<br>*(RF-063)* | El sistema debe verificar la existencia disponible antes de aceptar una solicitud de salida | — | HU-SAL-001 | Must<br>P0 | RN-EXI-003 | — | M-13 | `[RN-EXI-003]` |
| **RF-SAL-004**<br>*(RF-064)* | El sistema debe **rechazar toda salida que deje la existencia por debajo de cero, sin excepción ni autorización posible** | — | HU-SAL-004 | Must<br>P0 | RN-EXI-001 | — | RF-SAL-003 | `[RN-EXI-001]` |
| **RF-SAL-005**<br>*(RF-065)* | El sistema debe reservar la existencia al autorizarse la salida, excluyéndola del disponible | — | HU-SAL-002 | Must<br>P0 | RN-EXI-004 | — | CD-20 | `[RN-EXI-004]` |
| **RF-SAL-006**<br>*(RF-066)* | El sistema debe permitir al Coordinador autorizar salidas por debajo de su umbral configurado, escalando el resto al Jefe | Coordinador | HU-SAL-007 | Should<br>P1 | RN-SAL-001 | KPI-22 | M-19 | `[RN-SAL-001]` |
| **RF-SAL-007**<br>*(RF-067)* | El sistema debe generar la tarea de preparación e indicar las ubicaciones de toma según la política configurada | — | HU-SAL-003 | Should<br>P1 | RN-SAL-003 | — | M-20, M-19 | `[RN-SAL-003]` |
| **RF-SAL-008**<br>*(RF-068)* | El sistema debe **rechazar el escaneo de una unidad que no corresponda a lo solicitado**, explicando la discrepancia | — | HU-SAL-003 | Must<br>P0 | RN-SAL-004 | — | M-06 | `[RN-SAL-004]` |
| **RF-SAL-009**<br>*(RF-069)* | El sistema debe registrar el movimiento de salida, descontar la existencia y liberar la reserva al confirmarse | — | HU-SAL-003, HU-SAL-001 | Must<br>P0 | RN-EXI-004, RN-INT-004 | KPI-05, KPI-11, KPI-16 | M-14 | `[MON §7.1]` |
| **RF-SAL-010**<br>*(RF-070)* | El sistema debe **exigir aprobación del Jefe para toda baja por daño, cualquiera sea la cantidad** | Jefe | HU-SAL-005 | Should<br>P1 | RN-SAL-006 | KPI-13 | RF-SAL-001 | `[RN-SAL-006]` |
| **RF-SAL-011**<br>*(RF-071)* | El sistema debe registrar el retorno de mercancía **como entrada nueva referenciando la salida original, nunca como reversión** | Coordinador | HU-SAL-006 | Should<br>P1 | RN-SAL-007 | — | M-07 | `[RN-SAL-007]` |
| **RF-SAL-012**<br>*(RF-167)* | El sistema debe, en la preparación de una salida, verificar lo escaneado y **contar cada pieza seleccionada una sola vez** | Auxiliar | HU-SAL-008 | Must<br>P0 | RN-SAL-004, RN-SAL-009 | — | RF-SAL-008, RF-ENT-014 | `[Q-10]` `[RN-SAL-009*]` |
| **RF-SAL-013**<br>*(RF-168)* | El sistema debe permitir registrar el corte parcial de una pieza, descontando la cantidad cortada y **conservando la pieza con su remanente**, sin superar la cantidad de la pieza | Auxiliar | HU-SAL-009 | Must<br>P0 | RN-EXI-001, RN-SAL-008 | — | RF-SAL-012, RF-SAL-009 | `[F-3]` `[RN-SAL-008*]` |
| **RF-SAL-014**<br>*(RF-176)* | El sistema debe liberar automáticamente la reserva no ejecutada dentro del plazo configurado y alertar al solicitante | — | HU-SAL-002 | Should<br>P1 | RN-SAL-005 | — | RF-SAL-005, M-19 | `[RN-SAL-005]` `[DEC-06]` |

## 6.10 M-09 · Movimientos y Transferencias (dominio MOV)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-MOV-001**<br>*(RF-072)* | El sistema debe permitir registrar movimientos internos mediante escaneo de mercancía y ubicación destino | Auxiliar | HU-MOV-001 | Must<br>P0 | RN-MOV-002, RN-MOV-004, RN-MOV-010 | KPI-05, KPI-11 | M-06 | `[DC-08]` |
| **RF-MOV-002**<br>*(RF-073)* | El sistema debe garantizar que **un movimiento interno nunca altere la existencia total**, solo su distribución | — | HU-MOV-001 | Must<br>P0 | RN-MOV-004, RN-MOV-010 | — | RF-MOV-001 | `[RN-MOV-004]` |
| **RF-MOV-003**<br>*(RF-074)* | El sistema debe rechazar mover una cantidad superior a la existente en la ubicación origen | — | HU-MOV-002 | Must<br>P0 | RN-EXI-003 | — | M-13 | `[RN-EXI-003]` |
| **RF-MOV-004**<br>*(RF-075)* | El sistema debe rechazar movimientos cuya ubicación destino coincida con la de origen | — | HU-MOV-002 | Should<br>P1 | RN-MOV-005 | — | RF-MOV-001 | `[RN-MOV-005]` |
| **RF-MOV-005**<br>*(RF-076)* | El sistema debe rechazar como destino toda ubicación inactiva o sin capacidad disponible | — | HU-MOV-002, HU-ENT-006 | Should<br>P1 | RN-MOV-002, RN-MOV-010 | — | M-05 | `[RN-MOV-002]` |
| **RF-MOV-006**<br>*(RF-077)* | El sistema debe rechazar todo movimiento sobre existencia inmovilizada sin autorización del Jefe | — | HU-MOV-002 | Must<br>P0 | RN-EXI-006 | — | CD-22 | `[RN-EXI-006]` |
| **RF-MOV-007**<br>*(RF-078)* | El sistema debe permitir crear transferencias entre zonas o bodegas, reservando la existencia en origen | Coordinador | HU-MOV-003 | Must<br>P0 · H2 | RN-EXI-003, RN-EXI-004 | — | RF-SAL-005 | `[NUEVO]` |
| **RF-MOV-008**<br>*(RF-079)* | El sistema debe registrar confirmación de despacho y de recepción por separado, con responsables distintos identificados | Auxiliar | HU-MOV-004 | Should<br>P1 · H2 | RN-EXI-005 | KPI-15 | M-20 | `[NUEVO]` |
| **RF-MOV-009**<br>*(RF-080)* | El sistema debe mantener la existencia en tránsito **fuera del disponible tanto en origen como en destino** | — | HU-MOV-004 | Should<br>P1 · H2 | RN-EXI-005 | — | RF-MOV-008, CD-23 | `[RN-EXI-005]` |
| **RF-MOV-010**<br>*(RF-081)* | El sistema debe comparar despachado contra recibido, registrando diferencia si es menor y **rechazando la recepción si es mayor** | — | HU-MOV-005 | Should<br>P1 · H2 | RN-MOV-007 | KPI-15 | RF-MOV-008 | `[RN-MOV-007]` |
| **RF-MOV-011**<br>*(RF-082)* | El sistema debe generar alerta al superarse el tiempo máximo en tránsito configurado, y permitir la cancelación con retorno al origen solo por el Jefe | Jefe | HU-MOV-006, HU-MOV-007 | Should<br>P1 · H2 | RN-MOV-008, RN-MOV-009 | — | M-15, M-19 | `[RN-MOV-008]` `[RN-MOV-009]` |
| **RF-MOV-012**<br>*(RF-166)* | El sistema debe **exigir la selección de la pieza** en todo movimiento interno y en la primera ubicación, usando la ubicación como filtro de verificación cuando haya varias piezas del mismo lote | Auxiliar | HU-MOV-008 | Must<br>P0 | RN-MOV-010, RN-MOV-011, RN-MOV-012 | — | RF-MOV-001, RF-ENT-014 | `[F-4]` `[RN-MOV-011*]` `[RN-MOV-012*]` |
| **RF-MOV-013**<br>*(RF-173)* | El sistema debe mantener en tránsito un movimiento interno interrumpido y generar alerta al superar el tiempo máximo configurado | — | HU-MOV-009 | Should<br>P1 | RN-MOV-006 | — | RF-MOV-001, M-15 | `[RN-MOV-006]` `[DEC-06]` |

## 6.11 M-10 · Ajustes de Inventario (dominio AJU)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-AJU-001**<br>*(RF-083)* | El sistema debe permitir solicitar ajustes ingresando la existencia física observada y calculando la diferencia | Coordinador | HU-AJU-001 | Must<br>P0 | RN-AJU-003, RN-EXI-001 | KPI-08, KPI-14 | M-13 | `[MON §8.2]` |
| **RF-AJU-002**<br>*(RF-084)* | El sistema debe **exigir motivo tipificado obligatorio en todo ajuste; el texto libre no debe sustituirlo** | — | HU-AJU-001 | Must<br>P0 | RN-AJU-003 | — | M-19, CD-36 | `[RN-AJU-003]` |
| **RF-AJU-003**<br>*(RF-085)* | El sistema debe permitir adjuntar observación y evidencia, y exigir evidencia cuando el motivo así lo determine | Coordinador | HU-AJU-001 | Should<br>P1 | RN-AJU-003 | — | RF-AJU-002 | `[RN-AJU-003]` |
| **RF-AJU-004**<br>*(RF-086)* | El sistema debe clasificar el ajuste como menor o mayor según el umbral configurado y enrutarlo al aprobador correspondiente | — | HU-AJU-003, HU-TAR-002 | Must<br>P0 | RN-AJU-002 | KPI-22 | M-19 | `[RN-AJU-002]` |
| **RF-AJU-005**<br>*(RF-087)* | El sistema debe **impedir que un usuario apruebe un ajuste que él mismo solicitó, escalando al nivel superior** | — | HU-AJU-002 | Must<br>P0 | RN-AJU-001 | — | RF-AJU-004, PR-01 | `[RN-AJU-001]` |
| **RF-AJU-006**<br>*(RF-088)* | El sistema debe **rechazar todo ajuste que resulte en existencia negativa**; esta regla **no debe ser configurable** | — | HU-AJU-004 | Must<br>P0 | RN-EXI-001 | — | RF-AJU-001 | `[RN-EXI-001]` |
| **RF-AJU-007**<br>*(RF-089)* | El sistema debe mantener la existencia sin cambios hasta la aprobación, y generar el movimiento solo al aprobarse | — | HU-AJU-001, HU-AJU-002 | Must<br>P0 | RN-INT-002, RN-INT-004 | — | M-14 | `[MON §7.1]` |
| **RF-AJU-008**<br>*(RF-090)* | El sistema debe exigir justificación al rechazar un ajuste y notificar el resultado al solicitante | Jefe / Admin | HU-AJU-002, HU-TAR-002 | Should<br>P1 | RN-AJU-006 | KPI-22 | M-20 | `[RN-AJU-006]` |
| **RF-AJU-009**<br>*(RF-091)* | El sistema debe detectar y alertar patrones de ajuste recurrente sobre una misma unidad dentro de la ventana configurada | — | HU-AJU-005 | Should<br>P1 · H2 | RN-AJU-004 | — | M-15, M-19 | `[RN-AJU-004]` `[DC-07]` |
| **RF-AJU-010**<br>*(RF-092)* | El sistema debe permitir consultar ajustes filtrando por período, motivo, solicitante, aprobador y referencia, y exportarlos | Auditor / Jefe | HU-AJU-006 | Could<br>P2 | — | KPI-14 | M-16 | `[NUEVO]` |

## 6.12 M-11 · Conteos (dominio CNT)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-CNT-001**<br>*(RF-093)* | El sistema debe permitir programar conteos cíclicos definiendo el ámbito por ubicaciones, referencias o categorías | Coordinador | HU-CNT-001 | Should<br>P1 | — | KPI-03 | M-05, M-03 | `[NUEVO]` `[D-05]` |
| **RF-CNT-002**<br>*(RF-094)* | El sistema **no debe bloquear la operación de la bodega durante un conteo cíclico** | — | HU-CNT-001 | Must<br>P0 | — | — | RF-CNT-001 | `[NUEVO]` `[D-05]` |
| **RF-CNT-003**<br>*(RF-095)* | El sistema debe congelar la existencia teórica del ámbito al iniciar el conteo | — | HU-CNT-001, HU-CNT-003 | Should<br>P1 | RN-CNT-001 | — | CD-25 | `[RN-CNT-001]` |
| **RF-CNT-004**<br>*(RF-096)* | El sistema debe garantizar que **la existencia teórica congelada no se altere por movimientos posteriores al congelamiento** | — | HU-CNT-003 | Must<br>P0 | RN-CNT-001 | — | RF-CNT-003 | `[RN-CNT-001]` |
| **RF-CNT-005**<br>*(RF-097)* | El sistema debe generar y asignar tareas de conteo a contadores identificados | Coordinador | HU-CNT-001 | Should<br>P1 | — | — | M-20 | `[NUEVO]` |
| **RF-CNT-006**<br>*(RF-098)* | El sistema **no debe mostrar al contador la cantidad esperada antes ni después de registrar su conteo** | — | HU-CNT-002 | Must<br>P0 | RN-CNT-002 | — | RF-CNT-005 | `[RN-CNT-002]` |
| **RF-CNT-007**<br>*(RF-099)* | El sistema debe comparar lo contado contra la existencia congelada y clasificar cada línea como conforme, sobrante o faltante | — | HU-CNT-004, HU-CNT-005 | Should<br>P1 | RN-CNT-001 | KPI-01, KPI-04, KPI-08 | RF-CNT-003 | `[MON §8.2]` |
| **RF-CNT-008**<br>*(RF-100)* | El sistema debe generar automáticamente un segundo conteo cuando la diferencia supere el umbral de tolerancia | — | HU-CNT-004 | Should<br>P1 | RN-CNT-003 | KPI-06 | M-19 | `[RN-CNT-003]` |
| **RF-CNT-009**<br>*(RF-101)* | El sistema debe **exigir que el segundo conteo lo ejecute una persona distinta a la del primero** | — | HU-CNT-004 | Should<br>P1 | RN-CNT-003 | — | RF-CNT-008 | `[RN-CNT-003]` |
| **RF-CNT-010**<br>*(RF-102)* | El sistema debe **permitir el cierre de un conteo únicamente al Jefe, e impedirlo a quien lo ejecutó** | Jefe | HU-CNT-005 | Should<br>P1 | RN-CNT-003, RN-CNT-004 | — | RF-CNT-005 | `[RN-CNT-003]` `[RN-CNT-004]` |
| **RF-CNT-011**<br>*(RF-103)* | El sistema debe permitir programar conteos generales con corte, **bloqueando el registro de movimientos** y permitiendo excepciones solo al Jefe | Jefe | HU-CNT-006 | Should<br>P1 · H2 | RN-CNT-006 | KPI-02 | RF-CNT-001 | `[RN-CNT-006]` |
| **RF-CNT-012**<br>*(RF-104)* | El sistema debe **impedir cerrar un conteo general con ubicaciones del ámbito sin cubrir**, admitiendo exclusión solo con justificación registrada | — | HU-CNT-007 | Should<br>P1 · H2 | RN-CNT-007 | KPI-03 | RF-CNT-011 | `[RN-CNT-007]` |
| **RF-CNT-013**<br>*(RF-105)* | El sistema debe calcular la exactitud del ámbito contado al cierre, almacenarla históricamente y exponerla como KPI-01 | — | HU-CNT-008 | Could<br>P2 | — | KPI-01, KPI-02 | M-16, KPI-01 | `[MON §8.2]` |
| **RF-CNT-014**<br>*(RF-169)* | El sistema debe permitir contar manualmente pieza por pieza, registrando la cantidad de cada pieza **sin mostrar la esperada** | Auxiliar | HU-CNT-010 | Must<br>P0 | RN-CNT-002, RN-CNT-009 | KPI-01 | RF-CNT-006, RF-ENT-014 | `[F-5]` `[RN-CNT-009*]` |
| **RF-CNT-015**<br>*(RF-175)* | El sistema debe notificar al Administrador y al Auditor y condicionar el cierre de un conteo general cuando la diferencia global supere el umbral crítico configurado | — | HU-CNT-011 | Should<br>P1 · H2 | RN-CNT-008 | KPI-02 | RF-CNT-011, M-19 | `[RN-CNT-008]` `[DEC-06]` |

## 6.13 M-12 · Novedades de Mercancía (dominio NOV)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-NOV-001**<br>*(RF-106)* | El sistema debe permitir al Auxiliar reportar novedades desde tablet, con tipo tipificado, ubicación y descripción | Auxiliar | HU-NOV-001 | Should<br>P1 | — | KPI-23 | `[DC-05]` | `[MON §4]` |
| **RF-NOV-002**<br>*(RF-107)* | El sistema debe permitir escanear el identificador o declarar explícitamente su ausencia, y adjuntar evidencia fotográfica | Auxiliar | HU-NOV-001 | Should<br>P1 | — | — | M-06 | `[NUEVO]` |
| **RF-NOV-003**<br>*(RF-108)* | El sistema **no debe presentar ni contabilizar la novedad como falta imputable al reportante** | — | HU-NOV-001 | Should<br>P1 | — | — | PR-06 | `[MON §4]` `[PR-06]` |
| **RF-NOV-004**<br>*(RF-109)* | El sistema debe dirigir la novedad al Coordinador de la zona y permitir su resolución con acción determinada | Coordinador | HU-NOV-002, HU-NOV-003 | Should<br>P1 | — | KPI-23 | M-20 | `[NUEVO]` |
| **RF-NOV-005**<br>*(RF-110)* | El sistema debe vincular una novedad nueva a la existente cuando la unidad ya tenga una novedad abierta, **sin duplicarla** | — | HU-NOV-002 | Could<br>P2 | RN-NOV-003 | — | RF-NOV-004 | `[RN-NOV-003]` |
| **RF-NOV-006**<br>*(RF-111)* | El sistema debe **cerrar novedades con constancia de resolución y no ofrecer nunca su eliminación** | — | HU-NOV-002 | Must<br>P0 | RN-MAE-007 | KPI-23 | RN-MAE-007 | `[RN-MAE-007]` |
| **RF-NOV-007**<br>*(RF-174)* | El sistema debe impedir contar o usar mercancía sin registro hasta su identificación y permitir su incorporación solo mediante ajuste por sobrante con motivo tipificado y aprobación del Jefe | — | HU-NOV-004 | Should<br>P1 | RN-NOV-001 | — | RF-AJU-001 | `[RN-NOV-001]` `[DEC-06]` |
| **RF-NOV-008**<br>*(RF-177)* | El sistema debe escalar al Jefe y alertar las novedades no resueltas dentro del plazo configurado | — | HU-NOV-003 | Should<br>P1 | RN-NOV-002 | — | RF-NOV-001, M-19 | `[RN-NOV-002]` `[DEC-06]` |

## 6.14 M-13 · Consulta de Existencia (dominio INV)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-INV-001**<br>*(RF-112)* | El sistema debe permitir consultar existencia por referencia, SKU, lote, ubicación e identificador escaneado | Todos | HU-INV-001, HU-INV-002, HU-INV-003, HU-INV-004 | Must<br>P0 | RN-INT-004, RN-INT-006 | — | M-14 | `[MON §6, §7.2]` |
| **RF-INV-002**<br>*(RF-113)* | El sistema debe mostrar el desglose de existencia por estado: disponible, reservado, inmovilizado, en tránsito y en recepción | Todos | HU-INV-001 | Must<br>P0 | RN-EXI-003, RN-EXI-004, RN-EXI-005, RN-EXI-006, RN-EXI-007 | — | CD-44 | `[NUEVO]` |
| **RF-INV-003**<br>*(RF-114)* | El sistema debe derivar **siempre** la existencia mostrada del kardex, sin depender de un valor almacenado de forma independiente | — | HU-INV-001 | Must<br>P0 | RN-INT-004 | KPI-09 | M-14 | `[RN-INT-004]` |
| **RF-INV-004**<br>*(RF-115)* | El sistema debe mostrar la distribución de una referencia entre todas sus ubicaciones, con cantidad por cada una | Todos | HU-INV-003 | Must<br>P0 | RN-INT-005 | KPI-18 | M-05 | `[NUEVO]` |
| **RF-INV-005**<br>*(RF-116)* | El sistema **no debe mostrar costo ni valorización al Coordinador ni al Auxiliar** | — | HU-INV-002 | Must<br>P0 | — | — | PR-04 | `[PR-04]` |
| **RF-INV-006**<br>*(RF-117)* | El sistema debe permitir consultar la existencia histórica a una fecha y hora de corte, reconstruyéndola desde el kardex | Jefe / Auditor | HU-INV-005 | Should<br>P1 · H2 | RN-INT-004 | — | RF-INV-003 | `[MON §7.1]` |
| **RF-INV-007**<br>*(RF-118)* | El sistema debe ofrecer búsqueda por texto parcial tolerante a mayúsculas y tildes, e informar explícitamente cuando no haya coincidencias | Todos | HU-INV-006 | Should<br>P1 | — | — | — | `[MON §8.2]` |
| **RF-INV-008**<br>*(RF-119)* | El sistema debe garantizar que **ninguna operación de consulta modifique el estado del inventario** | — | HU-INV-002 | Could<br>P2 | RN-INT-006 | — | — | `[NUEVO]` |
| **RF-INV-009**<br>*(RF-171)* | El sistema debe permitir consultar las piezas de un lote con su tipo, cantidad actual, ubicación y estado | Todos | HU-KDX-006 | Must<br>P0 | RN-LOT-006 | — | RF-INV-001, RF-ENT-014 | `[Q-11]` |

## 6.15 M-14 · Kardex y Trazabilidad (dominio KDX)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-KDX-001**<br>*(RF-120)* | El sistema debe registrar todo movimiento con fecha, hora, tipo, cantidad, existencia resultante, ubicación, usuario, motivo y documento | — | HU-KDX-001 | Must<br>P0 | RN-INT-001, RN-INT-002 | KPI-05, KPI-17, KPI-24 | — | `[MON §7.1]` |
| **RF-KDX-002**<br>*(RF-121)* | El sistema debe garantizar que **todo movimiento tenga un usuario atribuible; no deben existir movimientos anónimos** | — | HU-KDX-001 | Must<br>P0 | RN-INT-001 | — | M-01 | `[PR-05]` |
| **RF-KDX-003**<br>*(RF-122)* | El sistema **no debe ofrecer función alguna de edición ni de eliminación de un movimiento confirmado, para ningún rol, incluido el Administrador** | — | HU-KDX-002 | Must<br>P0 | RN-INT-002 | — | — | `[RN-INT-002]` |
| **RF-KDX-004**<br>*(RF-123)* | El sistema debe permitir corregir errores mediante movimiento inverso con motivo y autorización, **conservando ambos movimientos visibles** | Jefe / Admin | HU-KDX-002 | Must<br>P0 | RN-AJU-007, RN-INT-002 | KPI-08 | RF-KDX-003 | `[CD-34]` |
| **RF-KDX-005**<br>*(RF-124)* | El sistema debe permitir consultar el kardex de una unidad de inventario, de un lote y de una ubicación, con filtros por tipo, período, usuario y motivo | Ver §2.7 | HU-KDX-001, HU-KDX-004 | Must<br>P0 | — | — | — | `[MON §7.1]` |
| **RF-KDX-006**<br>*(RF-125)* | El sistema debe permitir verificar que la existencia actual equivale a la suma algebraica de los movimientos, por unidad, por lote y globalmente | Auditor | HU-KDX-003 | Should<br>P1 | RN-AUD-005, RN-INT-004 | KPI-09 | RF-KDX-001 | `[RN-INT-004]` |
| **RF-KDX-007**<br>*(RF-126)* | El sistema debe restringir la consulta de kardex del Auxiliar a las unidades que él movió y a los últimos 30 días | — | HU-KDX-005 | Should<br>P1 | — | — | §2.7 | `[PR-04]` |
| **RF-KDX-008**<br>*(RF-170)* | El sistema debe registrar en el kardex la pieza afectada por cada movimiento que la toque | — | HU-KDX-006 | Must<br>P0 | RN-LOT-007 | — | RF-KDX-001, RF-ENT-014 | `[Q-11]` `[RN-LOT-007*]` |
| **RF-KDX-009**<br>*(RF-178)* | El sistema debe registrar el instante de inicio y el de confirmación de cada movimiento | — | HU-KDX-001 | Should<br>P1 | — | KPI-05 | RF-KDX-001 | `[KPI-05]` `[DEC-06]` |

## 6.16 M-15 · Alertas y Reglas (dominio ALE)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-ALE-001**<br>*(RF-127)* | El sistema debe evaluar de forma continua las condiciones de alerta configuradas y generar la alerta al cumplirse | — | HU-ALE-001, HU-ALE-002 | Should<br>P1 | — | KPI-19 | M-19 | `[DC-07]` |
| **RF-ALE-002**<br>*(RF-128)* | El sistema debe generar alertas **exclusivamente por reglas explícitas y umbrales configurados, sin modelos predictivos ni de aprendizaje** | — | HU-ALE-001 | Must<br>P0 | — | — | RF-ALE-001 | `[DC-07]` |
| **RF-ALE-003**<br>*(RF-129)* | El sistema debe asignar a toda alerta un destinatario por rol; **ninguna alerta debe quedar sin responsable** | — | HU-ALE-001 | Should<br>P1 | RN-ALE-005 | — | M-02 | `[NUEVO]` |
| **RF-ALE-004**<br>*(RF-130)* | El sistema debe implementar como mínimo los diez tipos de alerta enumerados en PN-11 | — | HU-ALE-001, HU-ALE-002 | Should<br>P1 | RN-AJU-004, RN-AJU-005, RN-CNT-005, RN-MOV-002, RN-MOV-008 | KPI-19, KPI-21 | Cap. 9 | `[MON §3, §7.1]` |
| **RF-ALE-005**<br>*(RF-131)* | El sistema debe **exigir motivo para descartar una alerta e impedir su cierre sin él** | Jefe / Coord. | HU-ALE-003 | Should<br>P1 | RN-ALE-004 | KPI-19, KPI-20 | — | `[RN-ALE-004]` |
| **RF-ALE-006**<br>*(RF-132)* | El sistema debe agrupar en una sola alerta activa cada condición vigente, evitando duplicados por reevaluación | — | HU-ALE-005 | Should<br>P1 | RN-ALE-001 | — | RF-ALE-001 | `[RN-ALE-001]` |
| **RF-ALE-007**<br>*(RF-133)* | El sistema debe escalar automáticamente al rol superior las alertas críticas no atendidas en el plazo configurado, y cerrarlas al cesar su condición | — | HU-ALE-004 | Could<br>P2 · H2 | RN-ALE-002, RN-ALE-003 | KPI-20 | M-19, M-20 | `[RN-ALE-002]` `[RN-ALE-003]` |

## 6.17 M-16 · Reportes y Exportación Analítica (dominio REP)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-REP-001**<br>*(RF-134)* | El sistema debe generar reportes de existencia, movimientos, entradas, salidas, ajustes, conteos, alertas y novedades | Ver §2.7 | HU-REP-001, HU-REP-002 | Should<br>P1 | — | — | M-13, M-14 | `[MON §8.2]` |
| **RF-REP-002**<br>*(RF-135)* | Todo reporte debe declarar su fecha, hora de generación y el usuario que lo generó | — | HU-REP-001 | Should<br>P1 | — | — | RF-REP-001 | `[NUEVO]` |
| **RF-REP-003**<br>*(RF-136)* | El sistema debe calcular los 12 indicadores del Núcleo definidos en el Capítulo 10 (KPI-01, 05, 08, 09, 11, 13, 14, 16, 17, 19, 21 y 24); los otros 12 son el RF-REP-008 | — | HU-CNT-008 | Should<br>P1 | — | KPI-01, KPI-05, KPI-08, KPI-09, KPI-11, KPI-13, KPI-14, KPI-16, KPI-17, KPI-19, KPI-21, KPI-24 | Cap. 10 | `[MON §8.2]` `[H-20]` |
| **RF-REP-004**<br>*(RF-137)* | El sistema debe exponer los datos de forma estructurada para consumo de la herramienta analítica externa | Administrador | HU-REP-003 | Should<br>P1 · H2 | — | — | `[DC-06]` | `[DC-06]` |
| **RF-REP-005**<br>*(RF-138)* | El sistema **no debe incluir el diseño de tableros analíticos**: la visualización analítica se resuelve en la herramienta externa | — | HU-REP-003 | Must<br>P0 | — | — | RF-REP-004 | `[DC-06]` |
| **RF-REP-006**<br>*(RF-139)* | El sistema debe registrar en la bitácora toda exportación de datos, con usuario, alcance y fecha | — | HU-REP-002, HU-REP-003 | Could<br>P2 | RN-AUD-001, RN-AUD-003 | — | M-18 | `[RN-AUD-001]` |
| **RF-REP-007**<br>*(RF-140)* | El sistema debe permitir programar la generación periódica de reportes y su puesta a disposición de destinatarios definidos | Jefe | HU-REP-004 | Could<br>P2 · H2 | — | — | M-20 | `[NUEVO]` |
| **RF-REP-008**<br>*(RF-185)* | El sistema debe calcular los 12 indicadores restantes del Capítulo 10 (KPI-02, 03, 04, 06, 07, 10, 12, 15, 18, 20, 22 y 23), que el backlog ubica en el Horizonte 2 (§12.3, elemento 15) o que requieren el conteo general (KPI-02) | — | HU-CNT-008 | Should<br>P1 · H2 | — | KPI-02, KPI-03, KPI-04, KPI-06, KPI-07, KPI-10, KPI-12, KPI-15, KPI-18, KPI-20, KPI-22, KPI-23 | Cap. 10, RF-REP-003 | `[NUEVO]` `[H-20]` |

## 6.18 M-17 · Dashboard Operativo (dominio DSH)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-DSH-001**<br>*(RF-141)* | El sistema debe presentar un dashboard operativo con existencia, alertas activas, pendientes y exactitud vigente | Jefe / Admin | HU-DSH-001 | Should<br>P1 | — | KPI-01 | M-13, M-15 | `[DC-02]` |
| **RF-DSH-002**<br>*(RF-142)* | El sistema debe permitir navegar desde cualquier elemento del dashboard hacia su detalle | Jefe / Admin | HU-DSH-001 | Should<br>P1 | — | — | RF-DSH-001 | `[NUEVO]` |
| **RF-DSH-003**<br>*(RF-143)* | El sistema debe restringir el dashboard del Coordinador a sus zonas asignadas y sin valorización | Coordinador | HU-DSH-003 | Should<br>P1 · H2 | — | — | §2.7 | `[PR-04]` |
| **RF-DSH-004**<br>*(RF-144)* | El sistema debe presentar al Auxiliar únicamente su panel de tareas, **sin indicadores de desempeño individual** | Auxiliar | HU-DSH-002 | Could<br>P2 | — | — | M-20, PR-06 | `[PR-06]` |

## 6.19 M-18 · Auditoría y Bitácora (dominio AUD)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-AUD-001**<br>*(RF-145)* | El sistema debe registrar en la bitácora accesos, cambios de configuración, cambios de rol, aprobaciones, rechazos, anulaciones y exportaciones | — | HU-AUD-001 | Must<br>P0 | RN-AUD-001 | — | Todos | `[NUEVO]` |
| **RF-AUD-002**<br>*(RF-146)* | El sistema debe garantizar que **la bitácora no sea editable ni borrable por ningún rol, incluido el Administrador** | — | HU-AUD-001 | Must<br>P0 | RN-AUD-001 | — | RF-AUD-001 | `[RN-AUD-001]` |
| **RF-AUD-003**<br>*(RF-147)* | El sistema debe permitir consultar la bitácora con filtros por usuario, fecha, tipo de evento y módulo, y exportarla | Auditor / Admin | HU-AUD-001 | Should<br>P1 | RN-AUD-001 | — | RF-AUD-001 | `[NUEVO]` |
| **RF-AUD-004**<br>*(RF-148)* | El sistema debe otorgar al rol Auditor **acceso de lectura completo sobre todo el sistema, sin restricción alguna** | Auditor | HU-AUD-002 | Should<br>P1 | — | — | M-02 | `[PR-02]` |
| **RF-AUD-005**<br>*(RF-149)* | El sistema debe **impedir al rol Auditor toda operación de escritura sobre el inventario, incluso mediante configuración** | — | HU-AUD-002 | Must<br>P0 | — | — | RF-AUD-004 | `[PR-02]` |
| **RF-AUD-006**<br>*(RF-150)* | El sistema debe permitir al Auditor registrar observaciones en un registro separado que **no altere el estado del inventario** | Auditor | HU-AUD-003 | Should<br>P1 | RN-AUD-002 | — | RF-AUD-005 | `[RN-AUD-002]` |
| **RF-AUD-007**<br>*(RF-151)* | El sistema debe reportar como hallazgo crítico toda coincidencia entre solicitante y aprobador, y toda discontinuidad de la bitácora | Auditor | HU-AUD-004 | Should<br>P1 | RN-AJU-001, RN-AUD-001 | KPI-09 | RF-AJU-005 | `[RN-AJU-001]` `[RN-AUD-001]` |

## 6.20 M-19 · Parámetros y Configuración (dominio PAR)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-PAR-001**<br>*(RF-152)* | El sistema debe permitir al Administrador configurar umbrales de ajuste, tolerancia de conteo, tiempo en tránsito, plazos, umbral de autorización del Coordinador, umbral crítico de diferencia global del conteo general y días sin movimiento, y al Jefe consultarlos sin modificarlos | Administrador | HU-PAR-001 | Must<br>P0 | RN-AJU-002, RN-CNT-003, RN-MOV-008, RN-SAL-001 | KPI-17 | — | `[CD-46]` `[DEC-04]` `[DEC-06]` |
| **RF-PAR-002**<br>*(RF-153)* | El sistema debe validar que los valores configurados estén dentro de rangos admisibles | — | HU-PAR-001 | Must<br>P0 | — | — | RF-PAR-001 | `[NUEVO]` |
| **RF-PAR-003**<br>*(RF-154)* | El sistema debe registrar todo cambio de configuración en la bitácora, con valor anterior y nuevo | — | HU-PAR-001 | Must<br>P0 | RN-AUD-001, RN-AUD-004 | — | M-18 | `[RN-AUD-001]` |
| **RF-PAR-004**<br>*(RF-155)* | El sistema debe aplicar los cambios de configuración a evaluaciones futuras, **nunca de forma retroactiva** | — | HU-PAR-001 | Should<br>P1 | RN-AUD-004 | — | RF-PAR-001 | `[NUEVO]` |
| **RF-PAR-005**<br>*(RF-156)* | El sistema debe permitir administrar el catálogo de motivos tipificados por tipo de operación, indicando cuáles exigen evidencia | Administrador | HU-PAR-002 | Must<br>P0 | RN-AJU-003 | — | CD-36 | `[RN-AJU-003]` |
| **RF-PAR-006**<br>*(RF-157)* | El sistema **no debe exponer como configurables las reglas estructurales** enumeradas en §9.1 | — | HU-PAR-003 | Should<br>P1 | RN-AJU-001, RN-AJU-003, RN-AUD-001, RN-CNT-002, RN-CNT-003, RN-EXI-001, RN-INT-001, RN-INT-002, RN-INT-004, RN-MAE-007 | — | Cap. 9 | `[NUEVO]` |
| **RF-PAR-007**<br>*(RF-181)* | El sistema debe permitir registrar el volumen de movimientos de referencia estimado en campo para calcular la adopción | Administrador | HU-PAR-001 | Could<br>P2 | — | KPI-24 | RF-PAR-001 | `[KPI-24]` `[DEC-06]` |

## 6.21 M-20 · Notificaciones y Tareas (dominio TAR)

| ID (legacy) | Requisito | Actor | Historia(s) | Prioridad | Regla(s) | KPI | Depende de | Origen (SPEC) |
|---|---|---|---|---|---|---|---|---|
| **RF-TAR-001**<br>*(RF-158)* | El sistema debe generar tareas al asignar trabajo de recepción, ubicación, conteo, preparación de salida y transferencia | — | HU-TAR-001 | Should<br>P1 | — | — | M-07 a M-11 | `[NUEVO]` |
| **RF-TAR-002**<br>*(RF-159)* | El sistema debe presentar a cada usuario su panel de tareas ordenado por prioridad, indicando qué, dónde y cuánto | Todos | HU-TAR-001, HU-DSH-002 | Should<br>P1 | — | — | RF-TAR-001 | `[DC-05]` |
| **RF-TAR-003**<br>*(RF-160)* | El sistema debe cerrar una tarea **por la confirmación del movimiento asociado, nunca por declaración del usuario** | — | HU-TAR-001, HU-DSH-002 | Must<br>P0 | — | — | M-14 | `[NUEVO]` |
| **RF-TAR-004**<br>*(RF-161)* | El sistema debe permitir reasignar tareas registrando a ambos responsables, **sin violar la regla del segundo conteo** | Coordinador | HU-TAR-003, HU-CNT-009 | Should<br>P1 · H2 | RN-CNT-003 | — | RF-CNT-009 | `[RN-CNT-003]` |
| **RF-TAR-005**<br>*(RF-162)* | El sistema **no debe exponer en las notificaciones información fuera del ámbito del destinatario**, y debe operar sin aplicación móvil nativa | — | HU-TAR-001 | Could<br>P2 | — | — | PR-04, `[DC-05]` | `[DC-05]` `[PR-04]` |
| **RF-TAR-006**<br>*(RF-182)* | El sistema debe consolidar al cierre de la jornada los movimientos y los pendientes: recepciones sin confirmar, movimientos en tránsito, tareas de conteo abiertas, ajustes sin resolver, novedades sin atender y alertas activas | Coordinador | HU-TAR-004 | Should<br>P1 | — | — | M-13, M-15 | `[PN-14]` `[DEC-05]` |
| **RF-TAR-007**<br>*(RF-183)* | El sistema debe permitir traspasar explícitamente los pendientes al turno siguiente y registrar el cierre con quién lo ejecutó | Jefe / Coord. | HU-TAR-004 | Should<br>P1 | — | — | RF-TAR-006 | `[PN-14]` `[DEC-05]` |
| **RF-TAR-008**<br>*(RF-184)* | El sistema debe impedir el cierre con registros sin sincronizar, registrar como omisión el cierre no ejecutado y alertar ante una diferencia significativa | — | HU-TAR-005 | Should<br>P1 | RN-INT-003 | — | RF-TAR-006 | `[RN-INT-003]` `[DEC-05]` |

---

**ESTADO DEL CAPÍTULO 6**

| | |
|---|---|
| **Completado** | 185 RF con ID `RF-<DOM>-nnn`, actor, historia(s), MoSCoW, regla(s) y KPI |
| **Pendiente** | Validación de los mapeos `[SRS]` (R-S02) · RF propuestos para reglas y KPI sin requisito (Anexo C, DEC-05 y DEC-06; **no incorporados**) |
| **Riesgos encontrados** | H-02 (prioridades del resumen del SPEC no coinciden) · H-11 y H-12 (brechas) · H-08 (19 RF en H2) |
| **Dependencias** | Cap. 5 (historias), Cap. 7 (RNF), Cap. 8 (reglas) |


---

# CAPÍTULO 7 — REQUISITOS NO FUNCIONALES

> Reorganización de los **47 RNF** del SPEC (Cap. 8) por categoría, con ID permanente `RNF-<CAT>-nnn`. Todos se conservan con su criterio de verificación y su origen. **Los valores numéricos son objetivos de diseño propuestos por el SPEC; su calibración requiere la línea base de la empresa piloto** (§1.4.7): el SRS no introduce metas nuevas. La usabilidad es la categoría prioritaria del producto `[MON §3, §4, §8.2]`.

## 7.1 Distribución


| Categoría | Código | RNF | Rango legacy | H2 |
|---|:--:|:--:|---|:--:|
| Seguridad | SEG | 8 | RNF-001–RNF-008 | 0 |
| Disponibilidad | DSP | 5 | RNF-009–RNF-013 | 0 |
| Rendimiento | REN | 6 | RNF-014–RNF-019 | 0 |
| Escalabilidad | ESC | 5 | RNF-020–RNF-024 | 0 |
| Accesibilidad | ACS | 5 | RNF-025–RNF-029 | 0 |
| Auditoría | AUD | 5 | RNF-030–RNF-034 | 0 |
| Usabilidad | USA | 7 | RNF-035–RNF-041 | 0 |
| Compatibilidad Tablet | TAB | 4 | RNF-042–RNF-045 | 0 |
| Compatibilidad Navegador | NAV | 2 | RNF-046–RNF-047 | 0 |
| **Total** | | **47** | RNF-001–RNF-047 | 1 |

> **Nota `[SRS]` — prioridad.** El SPEC no asigna prioridad P0–P3 a los RNF. El SRS no la inventa: la columna «Horizonte» indica H1 salvo el que el backlog (§12.3) declara Horizonte 2 (RNF-ACS-004, tamaño de texto ajustable). Los RNF que el backlog lista explícitamente en el Bloque 5 «Adopción» (MVP obligatorio) se marcan con ★.


## 7.2 Seguridad (SEG)

| ID (legacy) | Requisito | Verificación | Origen (SPEC) | Hor. |
|---|---|---|---|:--:|
| **RNF-SEG-001**<br>*(RNF-001)* | Toda operación del sistema debe exigir autenticación previa; no debe existir función accesible sin sesión válida | Intento de acceso sin sesión a cada función: todas rechazadas | `[PR-05]` | H1 |
| **RNF-SEG-002**<br>*(RNF-002)* | Las contraseñas deben almacenarse de forma que su valor original no sea recuperable por ningún medio ni por ningún rol | Inspección: ningún proceso, reporte o pantalla expone contraseñas | `[NUEVO]` | H1 |
| **RNF-SEG-003**<br>*(RNF-003)* | El control de acceso debe aplicarse en el momento de ejecutar la operación, no únicamente al presentar la interfaz | Intento de ejecución directa de operación no autorizada: rechazada | `[PR-01]` | H1 |
| **RNF-SEG-004**<br>*(RNF-004)* | La segregación de funciones definida en §2.7 debe ser inviolable por configuración | Recorrido completo de la matriz §2.7 con cada rol | `[PR-01]` `[DC-04]` | H1 |
| **RNF-SEG-005**<br>*(RNF-005)* | El rol Auditor debe carecer de toda capacidad de escritura sobre el inventario, sin excepción posible | Intento de cada operación de escritura con rol Auditor: todas rechazadas | `[PR-02]` | H1 |
| **RNF-SEG-006**<br>*(RNF-006)* | Toda comunicación entre el dispositivo del usuario y el sistema debe estar cifrada | Verificación de transporte cifrado en todas las rutas | `[NUEVO]` | H1 |
| **RNF-SEG-007**<br>*(RNF-007)* | El sistema debe registrar todo intento de operación no autorizada, con usuario, operación y fecha | Provocación de intentos no autorizados y verificación en bitácora | `[NUEVO]` | H1 |
| **RNF-SEG-008**<br>*(RNF-008)* | Los datos de la empresa deben tratarse conforme a la normativa colombiana de protección de datos personales aplicable | Revisión de cumplimiento previa a producción | `[AUD C.2.11]` | H1 |

## 7.3 Disponibilidad (DSP)

| ID (legacy) | Requisito | Verificación | Origen (SPEC) | Hor. |
|---|---|---|---|:--:|
| **RNF-DSP-001**<br>*(RNF-009)* | El sistema debe estar disponible durante la totalidad de la jornada operativa de la bodega | Medición de disponibilidad en ventana operativa durante el piloto | `[NUEVO]` | H1 |
| **RNF-DSP-002**<br>*(RNF-010)* ★ | Ante pérdida de conectividad, el registro de movimientos desde tablet debe retenerse localmente y sincronizarse al restablecerse | Desconexión durante registro y verificación de sincronización posterior | `[RN-INT-003]` `[MON §3]` | H1 |
| **RNF-DSP-003**<br>*(RNF-011)* ★ | El sistema debe impedir el cierre de jornada mientras existan registros sin sincronizar | Intento de cierre con registros pendientes: rechazado | `[RN-INT-003]` | H1 |
| **RNF-DSP-004**<br>*(RNF-012)* | Debe existir respaldo periódico de la información, con procedimiento de restauración probado | Ejecución de una restauración de prueba | `[NUEVO]` | H1 |
| **RNF-DSP-005**<br>*(RNF-013)* | La pérdida máxima de información tolerable ante una falla no debe exceder los movimientos de la última hora | Prueba de recuperación ante falla simulada | `[NUEVO]` | H1 |

## 7.4 Rendimiento (REN)

| ID (legacy) | Requisito | Verificación | Origen (SPEC) | Hor. |
|---|---|---|---|:--:|
| **RNF-REN-001**<br>*(RNF-014)* | La consulta de existencia por referencia debe responder en menos de 3 segundos con el volumen esperado de la empresa piloto | Medición con volumen de datos representativo | `[MON §6 — «tiempo real»]` | H1 |
| **RNF-REN-002**<br>*(RNF-015)* | La resolución de un identificador escaneado debe completarse en menos de 2 segundos | Medición desde escaneo hasta presentación del resultado | `[DC-08]` | H1 |
| **RNF-REN-003**<br>*(RNF-016)* | El registro de un movimiento debe confirmarse al usuario en menos de 3 segundos | Medición desde confirmación hasta acuse visible | `[MON §8.2 — tiempos de registro]` | H1 |
| **RNF-REN-004**<br>*(RNF-017)* | La carga del panel de tareas del Auxiliar debe completarse en menos de 3 segundos | Medición en tablet, en condiciones de red de la bodega | `[DC-05]` | H1 |
| **RNF-REN-005**<br>*(RNF-018)* | La generación de un reporte de período mensual no debe exceder los 30 segundos | Medición con volumen representativo | `[NUEVO]` | H1 |
| **RNF-REN-006**<br>*(RNF-019)* ★ | El tiempo de registro de un movimiento debe ser **menor que el del método manual actual**, medido contra la línea base | Comparación KPI-05 contra línea base de la Fase 3 | `[MON §8.2]` `[AUD C.2.4]` | H1 |

## 7.5 Escalabilidad (ESC)

| ID (legacy) | Requisito | Verificación | Origen (SPEC) | Hor. |
|---|---|---|---|:--:|
| **RNF-ESC-001**<br>*(RNF-020)* | El sistema debe sostener el volumen de referencias, SKU, ubicaciones y movimientos de una PYME textil sin degradación perceptible | Prueba con volumen proyectado a tres años | `[MON §5]` | H1 |
| **RNF-ESC-002**<br>*(RNF-021)* | El sistema debe admitir la operación simultánea de todos los usuarios de la bodega sin degradación de los tiempos de RNF-REN-001 a RNF-REN-004 | Prueba de concurrencia con el número real de usuarios | `[NUEVO]` | H1 |
| **RNF-ESC-003**<br>*(RNF-022)* | El sistema debe permitir incorporar bodegas y zonas adicionales sin rediseñar la información existente | Alta de una bodega adicional en ambiente de prueba | `[NUEVO]` | H1 |
| **RNF-ESC-004**<br>*(RNF-023)* | El crecimiento del kardex no debe degradar el tiempo de consulta de existencia | Medición con kardex de volumen proyectado a tres años | `[RN-INT-004]` | H1 |
| **RNF-ESC-005**<br>*(RNF-024)* | El sistema debe permitir la adopción escalonada por proceso: operar con entradas y salidas antes de habilitar conteos y transferencias | Verificación de operación con módulos parcialmente habilitados | `[MON §8.2]` `[D-10]` | H1 |

## 7.6 Accesibilidad (ACS)

| ID (legacy) | Requisito | Verificación | Origen (SPEC) | Hor. |
|---|---|---|---|:--:|
| **RNF-ACS-001**<br>*(RNF-025)* | Los elementos táctiles deben tener un tamaño suficiente para ser accionados con precisión en tablet, incluso con guantes de trabajo | Prueba con usuarios reales en condiciones de bodega | `[DC-05]` `[MON §3]` | H1 |
| **RNF-ACS-002**<br>*(RNF-026)* | El contraste de texto y fondo debe permitir la lectura bajo la iluminación real de la bodega | Prueba en el sitio de la empresa piloto | `[NUEVO]` | H1 |
| **RNF-ACS-003**<br>*(RNF-027)* | La información crítica no debe transmitirse únicamente mediante color | Revisión de todas las pantallas operativas | `[NUEVO]` | H1 |
| **RNF-ACS-004**<br>*(RNF-028)* | El tamaño de texto debe ser ajustable sin ruptura del diseño | Prueba con tamaños aumentados | `[NUEVO]` | H1 |
| **RNF-ACS-005**<br>*(RNF-029)* ★ | Los mensajes de error deben estar redactados en lenguaje comprensible para un usuario sin formación técnica, indicando qué hacer | Revisión con usuarios de perfil Auxiliar | `[MON §3, §8.2]` | H1 |

## 7.7 Auditoría (AUD)

| ID (legacy) | Requisito | Verificación | Origen (SPEC) | Hor. |
|---|---|---|---|:--:|
| **RNF-AUD-001**<br>*(RNF-030)* | Toda acción relevante debe quedar registrada con usuario, fecha, hora y detalle suficiente para reconstruirla | Recorrido de operaciones y verificación en bitácora | `[MON §7.1]` | H1 |
| **RNF-AUD-002**<br>*(RNF-031)* | La bitácora y el kardex deben ser inmutables: no debe existir mecanismo alguno de edición ni de borrado | Búsqueda exhaustiva de funciones de escritura sobre ambos registros | `[RN-INT-002]` `[RN-AUD-001]` | H1 |
| **RNF-AUD-003**<br>*(RNF-032)* | Debe ser posible reconstruir el estado del inventario a cualquier fecha pasada, con resultado idéntico ante consultas repetidas | Consulta histórica repetida sobre la misma fecha | `[RN-INT-004]` | H1 |
| **RNF-AUD-004**<br>*(RNF-033)* | La información de auditoría debe conservarse durante todo el período de vida del sistema, sin purga automática | Verificación de la política de retención | `[NUEVO]` | H1 |
| **RNF-AUD-005**<br>*(RNF-034)* | La verificación de integridad —existencia igual a suma de movimientos— debe poder ejecutarse a demanda sobre todo el inventario | Ejecución de la verificación global | `[RN-INT-004]` | H1 |

## 7.8 Usabilidad (USA)

| ID (legacy) | Requisito | Verificación | Origen (SPEC) | Hor. |
|---|---|---|---|:--:|
| **RNF-USA-001**<br>*(RNF-035)* ★ | Un Auxiliar sin experiencia previa debe poder registrar una entrada, una salida y un movimiento interno tras una capacitación breve | Prueba con usuarios reales sin formación previa | `[MON §3, §8.2]` | H1 |
| **RNF-USA-002**<br>*(RNF-036)* ★ | Las operaciones frecuentes del Auxiliar deben completarse en el mínimo número de pasos posible | Conteo de pasos por operación frecuente | `[MON §8.2]` | H1 |
| **RNF-USA-003**<br>*(RNF-037)* ★ | Toda operación de registro debe entregar confirmación visible e inequívoca de que quedó guardada | Revisión de cada operación de escritura | `[NUEVO — requisito de confianza del operario]` | H1 |
| **RNF-USA-004**<br>*(RNF-038)* ★ | El sistema debe explicar por qué rechaza una operación, en lugar de limitarse a impedirla | Revisión de todos los mensajes de rechazo | `[D-07]` `[MON §4]` | H1 |
| **RNF-USA-005**<br>*(RNF-039)* ★ | El sistema **no debe presentar al operario indicadores de desempeño individual ni comparaciones entre personas** | Revisión de todas las pantallas de rol Auxiliar | `[PR-06]` `[MON §4]` | H1 |
| **RNF-USA-006**<br>*(RNF-040)* | La terminología de la interfaz debe corresponder a la del Capítulo 4, sin sinónimos ni variantes | Revisión terminológica de toda la interfaz | `[§0.5]` | H1 |
| **RNF-USA-007**<br>*(RNF-041)* | El sistema debe permitir corregir un registro en curso antes de confirmarlo, sin perder el trabajo ya ingresado | Prueba de corrección previa a confirmación | `[NUEVO]` | H1 |

## 7.9 Compatibilidad Tablet (TAB)

| ID (legacy) | Requisito | Verificación | Origen (SPEC) | Hor. |
|---|---|---|---|:--:|
| **RNF-TAB-001**<br>*(RNF-042)* ★ | El sistema debe ser plenamente operable desde tablet para todas las funciones de los roles Auxiliar y Coordinador | Recorrido completo de sus funciones en tablet | `[DC-05]` | H1 |
| **RNF-TAB-002**<br>*(RNF-043)* ★ | El sistema debe funcionar como aplicación web responsive; **no debe requerir instalación de aplicación móvil nativa** | Verificación de acceso por navegador de tablet sin instalación | `[DC-05]` | H1 |
| **RNF-TAB-003**<br>*(RNF-044)* ★ | La captura de códigos QR debe funcionar con la cámara de la tablet, sin requerir lector externo obligatorio | Prueba de escaneo con cámara de dispositivo estándar | `[DC-08]` `[DC-05]` | H1 |
| **RNF-TAB-004**<br>*(RNF-045)* | La interfaz debe ser operable en orientación vertical y horizontal, sin pérdida de función | Prueba en ambas orientaciones | `[DC-05]` | H1 |

## 7.10 Compatibilidad Navegador (NAV)

| ID (legacy) | Requisito | Verificación | Origen (SPEC) | Hor. |
|---|---|---|---|:--:|
| **RNF-NAV-001**<br>*(RNF-046)* | El sistema debe funcionar en las versiones vigentes de los navegadores de uso mayoritario, en escritorio y en tablet | Prueba en la matriz de navegadores definida | `[DC-05]` | H1 |
| **RNF-NAV-002**<br>*(RNF-047)* | El sistema debe informar explícitamente al usuario cuando su navegador no sea compatible, en lugar de fallar de forma silenciosa | Prueba con navegador no soportado | `[NUEVO]` | H1 |

> ★ = RNF que el backlog del SPEC (§12.2, Bloques 4 y 5) declara MVP obligatorio o condición de medición.

---

**ESTADO DEL CAPÍTULO 7**

| | |
|---|---|
| **Completado** | 47 RNF en 9 categorías con ID `RNF-<CAT>-nnn`, verificación y origen |
| **Pendiente** | Calibración de valores numéricos con la línea base (pendiente #12, CA-12) · prioridad por RNF (no definida en el SPEC) |
| **Riesgos encontrados** | RG-36 (sin línea base no se calibran) · R-S07 |
| **Dependencias** | Cap. 12 (criterios de aceptación) |


---

# CAPÍTULO 8 — REGLAS DE NEGOCIO

> Reorganización de las reglas de negocio del SPEC (Cap. 9) por **dominio**, con ID permanente `RN-<DOM>-nnn`. Este capítulo es el corazón operativo de la «inteligencia» de COLBASOFT `[DC-07]`: la automatización del producto es este cuerpo de reglas evaluándose de forma explícita.

> **Hallazgo H-01 — cifra real.** El SPEC declara «68 reglas» y su §9.14 «68 = 51 estructurales + 17 configurables», pero las tablas §9.2–§9.12 contienen **82 reglas distintas: 60 estructurales + 22 configurables** (la propia suma de la tabla §9.14 da 82). Este SRS conserva **las 82**; ninguna se perdió. Los dos marcadores sin contenido `RN-069*` («reservado») y `RN-026b*` («ver nota de numeración») **no son reglas** y no reciben ID permanente (H-09).

> **Versión 1.1 — cierre del CP-04.** Se incorporan **3 reglas estructurales nuevas**, separadas de las 82: RN-EXI-007 (la entrada confirmada queda en recepción, DF5-02), RN-MOV-010 (la primera ubicación es un movimiento interno, DF5-03) y RN-INT-008 (revalidación al sincronizar, DF5-05); vienen de SPEC v1.1 §9.15. Además cambia el texto de **RN-IDE-001** y **RN-IDE-003** por DF5-01 (el QR de mercancía identifica SKU + Lote). Total del SRS v1.1: **85 reglas**. La discrepancia 68/82 del SPEC sigue abierta (H-01, DEC-03).
>
> **Versión 1.2 — decisiones del 30-sep-2026.** Se incorporan **6 reglas estructurales nuevas**, separadas de las 85: RN-LOT-006 (toda mercancía se registra por piezas), RN-LOT-007 (la existencia de una unidad de inventario es la suma de sus piezas), RN-SAL-008 (el corte parcial), RN-MOV-011 (selección de la pieza tras el escaneo), RN-SAL-009 (el escaneo de salida verifica y cuenta) y RN-CNT-009 (el conteo es pieza por pieza); vienen de SPEC v1.2 §9.16. Además cambia el texto de **RN-IDE-004** (Q-09: la reimpresión conserva el mismo QR). Total del SRS v1.2: **91 reglas**.
>
> **Versión 1.4 — respuesta a HD-29.** Se incorpora **1 regla estructural nueva**, separada de las 91: RN-MOV-012 (una pieza no se divide: el movimiento interno mueve la pieza completa y tomar una parte es un corte parcial). Viene de SPEC v1.4 §9.18. Además cambian los textos de **RN-MOV-001** (propuesta de ubicación con regla fija en el Núcleo, H-19) y **RN-LOT-006** (sin excepción: lo suelto es un paquete o bolsa, HD-30). Total del SRS v1.4: **92 reglas**.

## 8.1 Distribución por dominio


| Dominio | Nombre | Reglas | Estructurales | Configurables |
|---|---|:--:|:--:|:--:|
| **INT** | Integridad y atribución del registro | 8 | 8 | 0 |
| **EXI** | Existencia, disponibilidad y estados | 7 | 7 | 0 |
| **MAE** | Maestros, unicidad y eliminación lógica | 9 | 8 | 1 |
| **IDE** | Identificación por QR | 4 | 4 | 0 |
| **LOT** | Lotes | 7 | 6 | 1 |
| **ENT** | Entradas y recepción | 7 | 5 | 2 |
| **SAL** | Salidas | 9 | 6 | 3 |
| **MOV** | Movimientos, ubicación y transferencias | 12 | 7 | 5 |
| **AJU** | Ajustes y aprobaciones | 7 | 4 | 3 |
| **CNT** | Conteos | 9 | 7 | 2 |
| **NOV** | Novedades y mercancía sin registro | 3 | 1 | 2 |
| **ALE** | Alertas | 5 | 2 | 3 |
| **AUD** | Auditoría, bitácora y exportación | 5 | 5 | 0 |
| **Total** | | **92** | **70** | **22** |

**Definiciones (SPEC §9):** una regla **estructural** es inviolable y no parametrizable; una regla **configurable** ajusta su umbral en Parámetros y Configuración (M-19) pero su lógica no se desactiva. La columna «§9.1» marca las 10 reglas del núcleo no configurable que el SPEC enumera expresamente (RF-PAR-006); **la relación entre «estructural» y «núcleo §9.1» es ambigua en el SPEC** (H-06, DEC-04): el SRS interpreta que **toda regla estructural es no configurable**.


## 8.2 INT · Integridad y atribución del registro

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-INT-001**<br>*(RN-001)* | **Toda acción que altere el estado del sistema debe ser atribuible a un usuario identificado.** No existen acciones anónimas, automáticas sin origen ni ejecutadas por cuentas compartidas. Las acciones del sistema (cierre automático de alertas, escalamientos, liberación de reservas vencidas) se atribuyen al sistema como actor explícito, nunca a un usuario. | Estructural | ● | `[PR-05]` `[MON §7.1]` | RF-ACC-001, RF-ACC-002, RF-USR-001, RF-KDX-001, RF-KDX-002, RF-PAR-006 | HU-ACC-001, HU-USR-001, HU-KDX-001, HU-PAR-003 |
| **RN-INT-002**<br>*(RN-012)* | **Ningún movimiento confirmado puede editarse ni eliminarse.** Un error se corrige generando un movimiento inverso con motivo y autorización; ambos movimientos permanecen visibles en el kardex de forma permanente. | Estructural | ● | `[MON §7.1, §8.2]` | RF-ENT-011, RF-AJU-007, RF-KDX-001, RF-KDX-003, RF-KDX-004, RF-PAR-006 | HU-ENT-003, HU-AJU-001, HU-AJU-002, HU-KDX-001, HU-KDX-002, HU-PAR-003 |
| **RN-INT-003**<br>*(RN-054)* | Ante pérdida de conectividad, el registro se retiene localmente y se sincroniza al restablecerse. **Un documento no se confirma hasta haber sincronizado**, y el cierre de jornada se bloquea mientras existan registros sin sincronizar. | Estructural |  | `[MON §3]` | RF-ENT-005, RF-TAR-008 | HU-ENT-002, HU-TAR-005 |
| **RN-INT-004**<br>*(RN-065)* | **La existencia de una unidad de inventario es siempre la suma algebraica de sus movimientos en el kardex.** El sistema no almacena la existencia como un valor independiente que pueda divergir del kardex. Toda discrepancia detectada entre ambos es un hallazgo crítico de integridad. | Estructural | ● | `[MON §7.1]` `[CD-37]` | RF-ENT-011, RF-SAL-009, RF-AJU-007, RF-INV-001, RF-INV-003, RF-INV-006, RF-KDX-006, RF-PAR-006 | HU-ENT-003, HU-SAL-001, HU-SAL-003, HU-AJU-001, HU-AJU-002, HU-INV-001, HU-INV-002, HU-INV-003, HU-INV-004, HU-INV-005, HU-KDX-003, HU-PAR-003 |
| **RN-INT-005**<br>*(RN-066)* | **Una unidad de inventario queda definida de forma única por la combinación SKU + Lote + Ubicación.** No pueden coexistir dos unidades de inventario con la misma combinación. | Estructural |  | `[CD-07]` | RF-INV-004 | HU-INV-003 |
| **RN-INT-006**<br>*(RN-067)* | **Ninguna operación de consulta puede modificar el estado del inventario.** Leer nunca escribe. | Estructural |  | `[NUEVO]` | RF-INV-001, RF-INV-008 | HU-INV-001, HU-INV-002, HU-INV-003, HU-INV-004 |
| **RN-INT-007**<br>*(RN-068)* | **Toda cantidad se expresa en la unidad de medida de su referencia.** El sistema no realiza conversiones implícitas entre unidades de medida. | Estructural |  | `[CD-11]` | RF-CAT-005 | HU-CAT-002 |
| **RN-INT-008**<br>*(RN-083\*)* | **Un registro retenido sin conectividad no se aplica sin validarse de nuevo.** Al sincronizarse se valida contra el estado vigente y contra todas las reglas aplicables. Si las cumple, se confirma conservando la fecha y hora en que ocurrió el hecho; si no, **no se aplica**: se rechaza dejando constancia del registro original, de su autor, del motivo del rechazo y del instante. Cuando el registro rechazado describe un hecho físico ya realizado (mercancía recibida o trasladada), se abre una novedad para su resolución. Cada registro retenido se confirma o se rechaza una sola vez: la sincronización nunca produce existencia negativa, movimientos inválidos, estados imposibles, duplicados ni pérdida de trazabilidad. | Estructural |  | `[DF5-05]` `[RN-INT-003]` | RF-ENT-005 | HU-ENT-002 |

## 8.3 EXI · Existencia, disponibilidad y estados

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-EXI-001**<br>*(RN-009)* | **Ninguna operación puede dejar la existencia de una unidad de inventario por debajo de cero.** Esta prohibición aplica a salidas, transferencias, movimientos internos y ajustes. **No admite excepción, autorización ni configuración**: no existe rol que pueda eludirla. | Estructural | ● | `[NUEVO]` | RF-SAL-004, RF-AJU-001, RF-AJU-006, RF-PAR-006, RF-SAL-013 | HU-SAL-004, HU-AJU-001, HU-AJU-004, HU-NOV-004, HU-PAR-003, HU-SAL-009 |
| **RN-EXI-002**<br>*(RN-019)* | **Toda existencia disponible debe residir en una ubicación identificada.** No existe existencia disponible «en la bodega» sin ubicación concreta. Toda bodega debe tener al menos una zona de recepción para admitir mercancía aún no ubicada. | Estructural |  | `[NUEVO]` | RF-BOD-001, RF-BOD-003, RF-BOD-004 | HU-BOD-001, HU-ENT-006, HU-NOV-004 |
| **RN-EXI-003**<br>*(RN-025)* | Ninguna operación puede comprometer una cantidad superior a la **existencia disponible** en la ubicación de origen. La existencia reservada, inmovilizada o en tránsito no está disponible para nuevas operaciones. | Estructural |  | `[CD-19]` | RF-SAL-003, RF-MOV-003, RF-MOV-007, RF-INV-002 | HU-SAL-001, HU-MOV-002, HU-MOV-003, HU-INV-001, HU-SAL-008 |
| **RN-EXI-004**<br>*(RN-031)* | Al autorizarse una salida o crearse una transferencia, la existencia comprometida pasa a **reservada** y deja de contar como disponible. Ninguna otra operación puede comprometer esa misma cantidad. | Estructural |  | `[CD-20]` | RF-SAL-005, RF-SAL-009, RF-MOV-007, RF-INV-002 | HU-SAL-001, HU-SAL-002, HU-SAL-003, HU-MOV-003, HU-INV-001 |
| **RN-EXI-005**<br>*(RN-032)* | La existencia **en tránsito** no está disponible ni en la ubicación de origen ni en la de destino. Solo vuelve a estar disponible al confirmarse la recepción o al cancelarse la transferencia con retorno. | Estructural |  | `[CD-23]` | RF-MOV-008, RF-MOV-009, RF-INV-002 | HU-MOV-004, HU-INV-001 |
| **RN-EXI-006**<br>*(RN-036)* | Toda operación sobre existencia **inmovilizada** —ajuste, salida, transferencia o movimiento interno— requiere autorización expresa. El ajuste sobre mercancía inmovilizada requiere aprobación del **Administrador**, sin importar su monto. | Estructural |  | `[CD-22]` | RF-LOT-005, RF-MOV-006, RF-INV-002 | HU-LOT-003, HU-MOV-002, HU-INV-001 |
| **RN-EXI-007**<br>*(RN-081\*)* | **La existencia que ingresa por una entrada confirmada queda en recepción**, en una ubicación de una zona de recepción de la bodega: ya está en el inventario pero **no está disponible**, por lo que no se reserva, no sale ni se transfiere hasta ubicarse. Toda zona de recepción tiene al menos una ubicación. Se exceptúa la cantidad dañada, que ingresa inmovilizada en cuarentena (RN-ENT-006). | Estructural |  | `[DF5-02]` `[CD-16]` `[CD-44]` | RF-ENT-011, RF-INV-002 | HU-ENT-003, HU-INV-001 |

## 8.4 MAE · Maestros, unicidad y eliminación lógica

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-MAE-001**<br>*(RN-002)* | El código de referencia es único en todo el catálogo. El sistema rechaza la creación de una referencia con código ya existente, activa o inactiva. | Estructural |  | `[NUEVO]` | RF-CAT-001, RF-CAT-002, RF-ENT-003 | HU-CAT-001, HU-ENT-007 |
| **RN-MAE-002**<br>*(RN-004)* | La unidad de medida de una referencia **no puede modificarse si existen movimientos registrados** sobre ella. | Estructural |  | `[NUEVO]` | RF-CAT-005 | HU-CAT-002 |
| **RN-MAE-003**<br>*(RN-010)* | Una referencia con existencia distinta de cero **no puede desactivarse**. | Estructural |  | `[NUEVO]` | RF-CAT-006 | HU-CAT-003 |
| **RN-MAE-004**<br>*(RN-011)* | El sistema **impide desactivar o cambiar de rol al último Administrador activo**, y de forma análoga impide dejar una bodega sin ningún Jefe de Bodega activo. | Estructural |  | `[NUEVO]` | RF-USR-006 | HU-USR-003, HU-USR-005 |
| **RN-MAE-005**<br>*(RN-013)* | Una ubicación con existencia **no puede desactivarse**. | Estructural |  | `[NUEVO]` | RF-BOD-006 | HU-BOD-003 |
| **RN-MAE-006**<br>*(RN-014)* | El código de lote es único dentro de su SKU. El código de ubicación es único dentro de su bodega. El identificador de usuario es único en todo el sistema. | Estructural |  | `[NUEVO]` | RF-USR-001, RF-LOT-003, RF-BOD-001, RF-BOD-002 | HU-USR-001, HU-LOT-001, HU-BOD-001 |
| **RN-MAE-007**<br>*(RN-063)* | **Nada se elimina en COLBASOFT.** Usuarios, referencias, categorías, lotes, ubicaciones, motivos tipificados, novedades y observaciones **se desactivan o se cierran, nunca se borran**. No existe función de eliminación física en ninguna pantalla del sistema, para ningún rol, incluido el Administrador. | Estructural | ● | `[MON §7.1]` | RF-USR-004, RF-USR-005, RF-NOV-006, RF-PAR-006 | HU-USR-002, HU-CAT-003, HU-CAT-006, HU-BOD-003, HU-NOV-002, HU-PAR-002, HU-PAR-003 |
| **RN-MAE-008**<br>*(RN-076\*)* | Un elemento desactivado **no aparece en operaciones nuevas pero sí en el histórico**, conservando su identidad para que los registros pasados sigan siendo interpretables. | Estructural |  | `[NUEVO]` | RF-USR-004, RF-USR-005 | HU-USR-002 |
| **RN-MAE-009**<br>*(RN-077\*)* | Un elemento desactivado **puede reactivarse**, y tanto la desactivación como la reactivación quedan en la bitácora. | Configurable |  | `[NUEVO]` | RF-USR-004 | HU-USR-002 |

## 8.5 IDE · Identificación por QR

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-IDE-001**<br>*(RN-015)* | **Toda unidad de inventario debe tener un identificador activo.** No existe existencia sin identificador. El identificador de mercancía es el QR de su **SKU + Lote**; la unidad de inventario se determina con ese QR más su ubicación, obtenida por escaneo del QR de ubicación o por selección registrada. Si el SKU + Lote está en más de una ubicación y no se indica cuál, la operación no se registra. | Estructural |  | `[DC-08]` `[DF5-01]` | RF-QRC-001, RF-QRC-003 | HU-QRC-001, HU-QRC-002, HU-NOV-004 |
| **RN-IDE-002**<br>*(RN-016)* | **Ningún identificador QR se repite jamás**, ni siquiera después de haber sido anulado o reemplazado. El espacio de identificadores es de un solo uso. | Estructural |  | `[DC-08]` | RF-QRC-001, RF-QRC-002, RF-QRC-004 | HU-QRC-001, HU-QRC-003, HU-NOV-004 |
| **RN-IDE-003**<br>*(RN-017)* | Un mismo identificador secundario de código de barras no puede asociarse a dos identificadores QR de mercancía distintos (es decir, a dos SKU + Lote distintos). | Estructural |  | `[DC-08]` `[DF5-01]` | RF-QRC-008 | HU-QRC-005 |
| **RN-IDE-004**<br>*(RN-018)* | La reimpresión de un identificador exige motivo. **La reimpresión conserva el mismo QR: produce otra copia del mismo identificador y no crea una nueva identidad**, por lo que el identificador no cambia de estado ni pierde su trazabilidad. La reimpresión queda consultable en el historial del SKU + Lote. Los motivos por los que un identificador se reemplaza o se anula son DECISIÓN PENDIENTE (HD-28) | Estructural |  | `[DC-08]` `[MON §7.1]` `[Q-09]` | RF-QRC-006, RF-QRC-007 | HU-QRC-004 |

## 8.6 LOT · Lotes

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-LOT-001**<br>*(RN-071\*)* | **Ninguna existencia puede carecer de lote asociado.** Todo ingreso al inventario crea o se asocia a un lote, incluso cuando la empresa no distinga lotes comercialmente: en ese caso se genera un lote por evento de entrada. | Estructural |  | `[MON §7.1]` | RF-LOT-001, RF-LOT-002 | HU-LOT-001 |
| **RN-LOT-002**<br>*(RN-072\*)* | Un lote pertenece a un solo SKU. No existen lotes que agrupen referencias, tallas o colores distintos. | Estructural |  | `[CD-06]` | RF-LOT-004 | HU-LOT-002 |
| **RN-LOT-003**<br>*(RN-036b\*)* | **La inmovilización de un lote afecta toda su existencia, en todas sus ubicaciones y bodegas, de forma simultánea.** No es posible inmovilizar parcialmente un lote. | Estructural |  | `[NUEVO]` | RF-LOT-005 | HU-LOT-003 |
| **RN-LOT-004**<br>*(RN-073\*)* | Solo el Jefe de Bodega o el Administrador pueden liberar un lote inmovilizado, y la liberación exige motivo tipificado. | Estructural |  | `[NUEVO]` | RF-LOT-005 | HU-LOT-003 |
| **RN-LOT-005**<br>*(RN-074\*)* | Un lote que supera el umbral de antigüedad configurado se destaca en las consultas y genera alerta informativa al Jefe. | Configurable |  | `[NUEVO]` | RF-LOT-006 | HU-LOT-004 |
| **RN-LOT-006**<br>*(RN-084\*)* | **Toda mercancía recibida se registra por piezas.** Cada pieza pertenece a un solo SKU + Lote, tiene un tipo —rollo, paquete o bolsa, o contenedor agrupado— y una **cantidad propia registrada en la recepción**. El QR no identifica la pieza: la pieza tiene identidad interna en el sistema y el QR sigue identificando SKU + Lote. **Sin excepción**: la mercancía que llega suelta se registra como paquete o bolsa con su cantidad de unidades `[HD-30]` | Estructural |  | `[Q-11]` `[F-1]` `[F-2]` `[F-6]` `[CD-49]` `[HD-30]` | RF-ENT-014, RF-ENT-016, RF-INV-009 | HU-ENT-009, HU-ENT-010, HU-KDX-006 |
| **RN-LOT-007**<br>*(RN-085\*)* | **La existencia de una unidad de inventario es la suma de las cantidades de sus piezas en esa ubicación.** La cantidad de una pieza solo cambia por un movimiento del kardex (entrada, salida, movimiento interno, ajuste); la cantidad recibida de una línea de entrada es la suma de las cantidades de sus piezas | Estructural |  | `[Q-11]` `[F-2]` `[RN-INT-004]` `[RN-INT-005]` | RF-ENT-014, RF-ENT-015, RF-KDX-008 | HU-ENT-009, HU-KDX-006 |

## 8.7 ENT · Entradas y recepción

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-ENT-001**<br>*(RN-002b\*)* | Un documento de entrada solo admite **referencias activas del catálogo**. No es posible recibir mercancía sin identidad previamente definida. | Estructural |  | `[NUEVO]` | RF-ENT-003 | HU-ENT-007 |
| **RN-ENT-002**<br>*(RN-003)* | Al crear un documento de entrada con el mismo origen, referencia y fecha que otro existente, el sistema **advierte de posible duplicado** y exige confirmación explícita. No lo bloquea: puede tratarse de dos remesas legítimas. | Configurable |  | `[NUEVO]` | RF-ENT-004 | HU-ENT-001 |
| **RN-ENT-003**<br>*(RN-005)* | El sistema compara automáticamente, línea por línea, la cantidad recibida contra la esperada en el documento de entrada. | Estructural |  | `[NUEVO]` | RF-ENT-007, RF-ENT-015 | HU-ENT-004, HU-ENT-009 |
| **RN-ENT-004**<br>*(RN-006)* | Un faltante de recepción se registra como tal, el documento pasa a **recibido con novedad** y se notifica al Jefe. El faltante **no bloquea** la confirmación de lo efectivamente recibido. | Configurable |  | `[NUEVO]` | RF-ENT-008 | HU-ENT-004 |
| **RN-ENT-005**<br>*(RN-007)* | Un **sobrante** de recepción **exige autorización del Jefe antes de confirmar** la entrada. Un sobrante no autorizado no ingresa al inventario. | Estructural |  | `[NUEVO]` | RF-ENT-009 | HU-ENT-004 |
| **RN-ENT-006**<br>*(RN-008)* | La mercancía recibida en estado dañado **no ingresa como disponible**. Si ingresa, lo hace a zona de cuarentena en estado inmovilizado, y se abre novedad automáticamente. | Estructural |  | `[NUEVO]` | RF-ENT-012 | HU-ENT-005 |
| **RN-ENT-007**<br>*(RN-057b\*)* | `[PR-01]` **Quien registra la recepción física no puede confirmar la misma entrada.** La confirmación exige un segundo actor. | Estructural |  | `[PR-01]` | RF-ENT-010 | HU-ENT-003 |

## 8.8 SAL · Salidas

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-SAL-001**<br>*(RN-030)* | El Coordinador puede autorizar salidas por debajo de su **umbral de autorización configurado**. Por encima, la solicitud escala al Jefe de Bodega. El umbral es consultable por el propio Coordinador. | Configurable |  | `[NUEVO]` | RF-SAL-006, RF-PAR-001 | HU-SAL-007, HU-PAR-001 |
| **RN-SAL-002**<br>*(RN-048)* | **Toda salida exige motivo tipificado** seleccionado de lista cerrada. `[DC-03]` El sistema **no solicita ni almacena cliente, precio, factura ni documento comercial de despacho**. | Estructural |  | `[DC-03]` `[MON §8.2]` | RF-SAL-001, RF-SAL-002 | HU-SAL-001, HU-SAL-009 |
| **RN-SAL-003**<br>*(RN-049)* | La toma de mercancía para una salida sigue la **política configurada** de selección de ubicación: primero en entrar primero en salir por lote, ubicación de mayor cantidad, o ubicación más próxima. El sistema propone; el operario ejecuta. | Configurable |  | `[NUEVO]` | RF-SAL-007 | HU-SAL-003 |
| **RN-SAL-004**<br>*(RN-050)* | Durante la preparación de una salida, **el escaneo de una unidad que no corresponde a lo solicitado se rechaza**, indicando la discrepancia concreta: referencia, talla, color o lote. | Estructural |  | `[DC-08]` | RF-SAL-008, RF-SAL-012 | HU-SAL-003, HU-SAL-008 |
| **RN-SAL-005**<br>*(RN-051)* | Una reserva no ejecutada dentro del plazo configurado **se libera automáticamente**, la existencia vuelve a disponible y se genera alerta al solicitante. | Configurable |  | `[NUEVO]` | RF-SAL-014 | HU-SAL-002 |
| **RN-SAL-006**<br>*(RN-052)* | La **baja por daño** exige aprobación del Jefe de Bodega **cualquiera sea la cantidad**, junto con observación y evidencia. Alimenta el reporte de mermas y el KPI-13. | Estructural |  | `[NUEVO]` | RF-SAL-010 | HU-SAL-005 |
| **RN-SAL-007**<br>*(RN-053)* | El retorno de mercancía previamente despachada **se registra como una entrada nueva que referencia la salida original**. La salida original **nunca se reversa**: ambos movimientos permanecen en el kardex. | Estructural |  | `[MON §7.1]` | RF-SAL-011 | HU-SAL-006 |
| **RN-SAL-008**<br>*(RN-086\*)* | **Un corte parcial descuenta de la pieza solo la cantidad cortada** y deja la pieza con su remanente, con la misma identidad. La cantidad cortada no puede superar la cantidad de la pieza (RN-EXI-001). El corte es una salida y cumple las reglas de salida | Estructural |  | `[F-3]` `[RN-EXI-001]` `[RN-SAL-002]` | RF-SAL-013 | HU-SAL-009 |
| **RN-SAL-009**<br>*(RN-088\*)* | **En la preparación de una salida el escaneo verifica y cuenta.** Cada pieza tomada se cuenta una sola vez: seleccionar de nuevo la misma pieza no suma. La preparación no se confirma completa mientras falten piezas o cantidad solicitada, salvo salida parcial autorizada | Estructural |  | `[Q-10]` `[RN-SAL-004]` `[RN-EXI-003]` | RF-SAL-012 | HU-SAL-008 |

## 8.9 MOV · Movimientos, ubicación y transferencias

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-MOV-001**<br>*(RN-020)* | El sistema **propone** la ubicación destino según los criterios vigentes —en el Núcleo, una regla fija: zona por categoría, agrupación por referencia y mayor capacidad libre; configurables desde el Horizonte 2 (HU-BOD-005)—; el Auxiliar **confirma o desvía**. La propuesta nunca es una imposición. | Configurable |  | `[NUEVO]` `[H-19]` | RF-BOD-008 | HU-BOD-005, HU-ENT-006 |
| **RN-MOV-002**<br>*(RN-021)* | Una ubicación **inactiva** no puede recibir mercancía. Una ubicación cuya ocupación superaría su capacidad no se propone como destino, y si se excede, genera alerta de sobreocupación. | Configurable |  | `[CD-15]` | RF-BOD-005, RF-MOV-001, RF-MOV-005, RF-ALE-004 | HU-BOD-002, HU-ENT-006, HU-MOV-001, HU-MOV-002, HU-ALE-001, HU-ALE-002 |
| **RN-MOV-003**<br>*(RN-022)* | Cuando el Auxiliar ubica mercancía en un lugar distinto al propuesto, **el sistema lo permite pero registra la desviación** y notifica al Coordinador. `[PR-06]` La desviación se registra como información operativa, **no como falta imputable**. | Configurable |  | `[PR-06]` `[MON §4]` | RF-BOD-009 | HU-BOD-005, HU-ENT-006 |
| **RN-MOV-004**<br>*(RN-026)* | **Un movimiento interno nunca altera la existencia total** de una unidad de inventario: solo redistribuye su ubicación. La suma de la existencia por ubicación antes y después debe ser idéntica. | Estructural |  | `[NUEVO]` | RF-MOV-001, RF-MOV-002 | HU-MOV-001, HU-MOV-008 |
| **RN-MOV-005**<br>*(RN-027)* | Un movimiento cuya ubicación destino coincide con la de origen se rechaza por carecer de efecto. | Estructural |  | `[NUEVO]` | RF-MOV-004 | HU-MOV-002 |
| **RN-MOV-006**<br>*(RN-028)* | Un movimiento interno interrumpido queda en estado **en tránsito**. Su existencia no está disponible en origen ni en destino. Si el tiempo en tránsito supera el máximo configurado, el sistema genera alerta. | Configurable |  | `[CD-23]` | RF-MOV-013 | HU-MOV-009 |
| **RN-MOV-007**<br>*(RN-033)* | Al recibirse una transferencia, el sistema compara lo despachado contra lo recibido. Si lo recibido es **menor**, registra diferencia de transferencia y abre novedad. Si lo recibido es **mayor**, **rechaza la recepción** y escala al Jefe. La transferencia no se completa hasta la resolución. | Estructural |  | `[NUEVO]` | RF-MOV-010 | HU-MOV-005 |
| **RN-MOV-008**<br>*(RN-034)* | Una transferencia que supera el tiempo máximo en tránsito configurado genera alerta dirigida al Jefe, identificando su contenido y su responsable de despacho. | Configurable |  | `[NUEVO]` | RF-MOV-011, RF-ALE-004, RF-PAR-001 | HU-MOV-006, HU-MOV-007, HU-ALE-001, HU-ALE-002, HU-PAR-001 |
| **RN-MOV-009**<br>*(RN-035)* | Una transferencia **pendiente de despacho** puede cancelarla el Coordinador, liberándose la reserva. Una transferencia **en tránsito** solo puede cancelarla el Jefe, y su cancelación genera un movimiento de retorno al origen. Toda cancelación exige motivo. | Estructural |  | `[NUEVO]` | RF-MOV-011 | HU-MOV-006, HU-MOV-007 |
| **RN-MOV-010**<br>*(RN-082\*)* | **La primera ubicación de la existencia en recepción es un movimiento interno** desde la ubicación de recepción hacia la ubicación destino, y queda en el kardex con qué, cuánto, origen, destino, quién, cuándo y el documento de entrada que la origina. Cumple las reglas del movimiento interno (RN-MOV-002, RN-MOV-004, RN-MOV-005): la existencia total no cambia y el descuento en origen y el incremento en destino son indivisibles. Al confirmarse, la cantidad movida queda **disponible** en el destino, salvo que el destino pertenezca a una zona de recepción, donde sigue en recepción. | Estructural |  | `[DF5-03]` `[PN-03]` `[RN-MOV-004]` | RF-MOV-001, RF-MOV-002, RF-MOV-005, RF-MOV-012 | HU-ENT-006, HU-MOV-001, HU-MOV-002, HU-MOV-008 |
| **RN-MOV-011**<br>*(RN-087\*)* | **Toda operación que mueve, toma o cuenta mercancía identifica la pieza afectada.** Después de escanear el QR del SKU + Lote el operario selecciona la pieza; si hay varias del mismo lote en la ubicación, la ubicación (escaneada o seleccionada) filtra y verifica qué piezas se ofrecen. No se confirma la operación sin pieza seleccionada | Estructural |  | `[F-4]` `[RN-IDE-001]` | RF-MOV-012 | HU-MOV-008 |
| **RN-MOV-012**<br>*(RN-090\*)* | **Una pieza no se divide.** Un movimiento interno mueve la pieza completa; tomar una parte de una pieza es un corte parcial (RN-SAL-008*), que se registra como salida. La división de una pieza en dos no existe en el MVP | Estructural |  | `[HD-29]` `[F-3]` `[RN-SAL-008*]` | RF-MOV-012 | HU-MOV-001, HU-MOV-008 |

## 8.10 AJU · Ajustes y aprobaciones

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-AJU-001**<br>*(RN-023)* | **Ningún usuario puede aprobar una solicitud que él mismo originó.** Aplica a ajustes, salidas y cierres de conteo. Si el aprobador designado coincide con el solicitante, la solicitud **escala automáticamente al nivel superior**. Si no existe nivel superior disponible, la solicitud queda bloqueada y se notifica al Administrador. | Estructural | ● | `[PR-01]` `[MON §6]` | RF-AJU-005, RF-AUD-007, RF-PAR-006 | HU-AJU-002, HU-AUD-004, HU-PAR-003 |
| **RN-AJU-002**<br>*(RN-024)* | Todo ajuste se clasifica como **menor** o **mayor** según el umbral configurado. El ajuste menor lo aprueba el Jefe de Bodega; el mayor, el Administrador. El umbral aplicado queda registrado en el ajuste, de modo que un cambio posterior de configuración no altera la interpretación histórica. | Configurable |  | `[NUEVO]` | RF-AJU-004, RF-PAR-001 | HU-AJU-003, HU-PAR-001, HU-TAR-002 |
| **RN-AJU-003**<br>*(RN-029)* | **Todo ajuste exige un motivo tipificado seleccionado de una lista cerrada.** El texto libre puede complementarlo pero **nunca sustituirlo**. Determinados motivos exigen además evidencia adjunta, según se configure en M-19. | Estructural | ● | `[MON §8.2]` | RF-AJU-001, RF-AJU-002, RF-AJU-003, RF-PAR-005, RF-PAR-006 | HU-AJU-001, HU-NOV-004, HU-PAR-002, HU-PAR-003 |
| **RN-AJU-004**<br>*(RN-037)* | Cuando una misma unidad de inventario acumula más ajustes que el umbral configurado dentro de una ventana de tiempo configurada, el sistema genera **alerta de patrón anómalo** dirigida al Jefe y al Auditor, listando los ajustes involucrados con su solicitante y aprobador. | Configurable |  | `[MON §6]` `[DC-07]` | RF-AJU-009, RF-ALE-004 | HU-AJU-005, HU-ALE-001, HU-ALE-002 |
| **RN-AJU-005**<br>*(RN-038)* | Una solicitud de ajuste sin resolver más allá del plazo configurado **escala automáticamente** al nivel superior y genera alerta. | Configurable |  | `[NUEVO]` | RF-ALE-004 | HU-ALE-001, HU-ALE-002, HU-TAR-002 |
| **RN-AJU-006**<br>*(RN-062)* | El rechazo de un ajuste **exige justificación** y queda registrado con la misma permanencia que una aprobación. La existencia no cambia, pero el intento y su rechazo forman parte del rastro auditable. | Estructural |  | `[NUEVO]` | RF-AJU-008 | HU-AJU-002, HU-TAR-002 |
| **RN-AJU-007**<br>*(RN-070\*)* | Un ajuste aplicado **no se edita ni se revierte**: un error en un ajuste se corrige mediante un nuevo ajuste, quedando ambos en el kardex. | Estructural |  | `[RN-INT-002]` | RF-KDX-004 | HU-KDX-002 |

## 8.11 CNT · Conteos

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-CNT-001**<br>*(RN-039)* | La **existencia teórica congelada** al iniciar un conteo no se altera por movimientos posteriores al congelamiento. Los movimientos ocurridos durante el conteo se listan en la conciliación pero no modifican la base de comparación. | Estructural |  | `[NUEVO]` | RF-CNT-003, RF-CNT-004, RF-CNT-007 | HU-CNT-001, HU-CNT-003, HU-CNT-004, HU-CNT-005, HU-CNT-010 |
| **RN-CNT-002**<br>*(RN-040)* | **La cantidad esperada no se muestra al contador**, ni antes ni después de registrar su conteo. El objetivo es impedir el sesgo de confirmación. La diferencia solo la ve quien concilia. | Estructural | ● | `[NUEVO]` | RF-CNT-006, RF-PAR-006, RF-CNT-014 | HU-CNT-002, HU-PAR-003, HU-CNT-010 |
| **RN-CNT-003**<br>*(RN-041)* | Cuando la diferencia de una línea supera el umbral de tolerancia, el sistema genera **segundo conteo obligatorio, ejecutado por una persona distinta a la del primero**. Adicionalmente, **quien ejecutó un conteo no puede cerrarlo**. | Estructural | ● | `[PR-01]` | RF-CNT-008, RF-CNT-009, RF-CNT-010, RF-PAR-001, RF-PAR-006, RF-TAR-004 | HU-CNT-004, HU-CNT-005, HU-CNT-009, HU-PAR-001, HU-PAR-003, HU-TAR-003 |
| **RN-CNT-004**<br>*(RN-042)* | **Solo el Jefe de Bodega cierra un conteo** y decide qué diferencias generan ajuste. Un conteo cerrado no se reabre. | Estructural |  | `[NUEVO]` | RF-CNT-010 | HU-CNT-005 |
| **RN-CNT-005**<br>*(RN-044)* | Un conteo programado y no ejecutado dentro de su plazo genera alerta. Si excede el plazo máximo, la existencia congelada se libera y el conteo se marca como vencido. | Configurable |  | `[NUEVO]` | RF-ALE-004 | HU-ALE-001, HU-ALE-002 |
| **RN-CNT-006**<br>*(RN-045)* | El conteo general **bloquea el registro de movimientos** desde su hora de corte hasta su cierre. Solo el Jefe puede autorizar un movimiento de excepción, que queda marcado como tal en el kardex. | Estructural |  | `[NUEVO]` | RF-CNT-011 | HU-CNT-006 |
| **RN-CNT-007**<br>*(RN-046)* | Un conteo general **no puede cerrarse mientras existan ubicaciones del ámbito sin cubrir**. La exclusión de una ubicación exige justificación registrada, y la cobertura alcanzada queda documentada. | Estructural |  | `[NUEVO]` | RF-CNT-012 | HU-CNT-007 |
| **RN-CNT-008**<br>*(RN-047)* | Cuando la diferencia global de un conteo general supera el umbral crítico configurado, el sistema **notifica al Administrador y al Auditor antes de permitir el cierre**. | Configurable |  | `[NUEVO]` | RF-CNT-015 | HU-CNT-011 |
| **RN-CNT-009**<br>*(RN-089\*)* | **El conteo se hace manualmente, pieza por pieza.** El contador registra la cantidad de cada pieza sin ver la cantidad esperada (RN-CNT-002); la cantidad contada de la unidad de inventario es la suma de sus piezas | Estructural |  | `[F-5]` `[RN-CNT-002]` | RF-CNT-014 | HU-CNT-010 |

## 8.12 NOV · Novedades y mercancía sin registro

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-NOV-001**<br>*(RN-043)* | La mercancía encontrada sin registro en el sistema **no se cuenta ni se usa hasta ser identificada**. Su incorporación exige creación de la unidad, ajuste por sobrante con motivo tipificado y aprobación del Jefe. | Estructural |  | `[NUEVO]` | RF-NOV-007 | HU-NOV-004 |
| **RN-NOV-002**<br>*(RN-059)* | Una novedad sin resolver más allá del plazo configurado **escala al Jefe de Bodega** y genera alerta. | Configurable |  | `[NUEVO]` | RF-NOV-008 | HU-NOV-003 |
| **RN-NOV-003**<br>*(RN-060)* | Una novedad reportada sobre una unidad que ya tiene una novedad abierta **se vincula a la existente en lugar de crear una nueva**. | Configurable |  | `[NUEVO]` | RF-NOV-005 | HU-NOV-002 |

## 8.13 ALE · Alertas

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-ALE-001**<br>*(RN-055)* | Una condición de alerta vigente genera **una sola alerta activa**, no una por cada ciclo de evaluación. Las alertas se agrupan por tipo, unidad y condición. | Configurable |  | `[NUEVO]` | RF-ALE-006 | HU-ALE-005 |
| **RN-ALE-002**<br>*(RN-056)* | Una alerta de severidad crítica no atendida dentro del plazo configurado **escala automáticamente al rol superior** y genera notificación adicional. El escalamiento queda en la bitácora. | Configurable |  | `[NUEVO]` | RF-ALE-007 | HU-NOV-003, HU-ALE-004 |
| **RN-ALE-003**<br>*(RN-057)* | Una alerta **se cierra automáticamente cuando su condición de disparo deja de cumplirse**, quedando en el historial marcada como no atendida si nadie actuó sobre ella. | Configurable |  | `[NUEVO]` | RF-ALE-007 | HU-NOV-003, HU-ALE-001, HU-ALE-004 |
| **RN-ALE-004**<br>*(RN-058)* | **El descarte de una alerta exige motivo.** Sin motivo, la alerta no puede cerrarse manualmente. Quien la atendió y qué hizo quedan registrados. | Estructural |  | `[NUEVO]` | RF-ALE-005 | HU-ALE-003 |
| **RN-ALE-005**<br>*(RN-075\*)* | **Toda alerta tiene un destinatario por rol.** Ninguna alerta puede quedar sin responsable asignado; si el rol destinatario no tiene usuario activo, escala al superior. | Estructural |  | `[NUEVO]` | RF-BOD-007, RF-ALE-003 | HU-BOD-004, HU-ALE-001 |

## 8.14 AUD · Auditoría, bitácora y exportación

| ID (legacy) | Regla | Tipo | §9.1 | Origen (SPEC) | RF | Historias |
|---|---|:--:|:--:|---|---|---|
| **RN-AUD-001**<br>*(RN-061)* | **La bitácora de auditoría es inmutable.** No existe mecanismo de edición ni de borrado, para ningún rol, incluido el Administrador. Toda discontinuidad detectada en ella constituye hallazgo crítico de integridad. | Estructural | ● | `[NUEVO]` | RF-ACC-003, RF-USR-008, RF-REP-006, RF-AUD-001, RF-AUD-002, RF-AUD-003, RF-AUD-007, RF-PAR-003, RF-PAR-006 | HU-ACC-001, HU-USR-003, HU-REP-002, HU-REP-003, HU-AUD-001, HU-AUD-004, HU-PAR-001, HU-PAR-003 |
| **RN-AUD-002**<br>*(RN-064)* | Las **observaciones del Auditor** se almacenan en un registro separado y **no alteran el estado del inventario**. Son la única capacidad de escritura del rol Auditor. Se cierran con respuesta; nunca se eliminan. | Estructural |  | `[PR-02]` | RF-AUD-006 | HU-AUD-003 |
| **RN-AUD-003**<br>*(RN-078\*)* | Toda **exportación de datos** queda registrada en la bitácora con usuario, alcance temporal y fecha. | Estructural |  | `[NUEVO]` | RF-REP-006 | HU-REP-002, HU-REP-003 |
| **RN-AUD-004**<br>*(RN-079\*)* | Todo **cambio de configuración** queda registrado en la bitácora con su valor anterior y su valor nuevo. Los cambios aplican a evaluaciones futuras, **nunca de forma retroactiva**. | Estructural |  | `[NUEVO]` | RF-PAR-003, RF-PAR-004 | HU-PAR-001 |
| **RN-AUD-005**<br>*(RN-080\*)* | El sistema debe poder **verificar a demanda** que la existencia actual equivale a la suma de los movimientos, por unidad, por lote y globalmente. | Estructural |  | `[RN-INT-004]` | RF-KDX-006 | HU-KDX-003 |

\* Las reglas con asterisco en el SPEC (`RN-002b`, `RN-036b`, `RN-057b`, `RN-070` a `RN-080`) se incorporaron durante la consolidación del Cap. 9 del SPEC (§9.13); `RN-081` a `RN-083` se incorporaron en la v1.1 del SPEC (§9.15, cierre del CP-04), `RN-084` a `RN-089` en la v1.2 (§9.16) y `RN-090` en la v1.4 (§9.18); su contenido se conserva íntegro y ya no requieren el asterisco.

---

**ESTADO DEL CAPÍTULO 8**

| | |
|---|---|
| **Completado** | 92 reglas en 13 dominios (82 del SPEC v1.0 + 3 de la v1.1 + 6 de la v1.2 + 1 de la v1.4) con ID `RN-<DOM>-nnn`, tipo, origen, RF e HU relacionados |
| **Pendiente** | Confirmar la cifra de 82 y la renumeración canónica (DEC-03) · ambigüedad estructural/configurable (DEC-04) · 6 reglas sin RF (Anexo C, PROP-RN) |
| **Riesgos encontrados** | H-01, H-06, H-09, H-11 · R-S06, R-S08 |
| **Dependencias** | Cap. 6 (RF), Cap. 5 (HU), Cap. 12 (CA-06 y CA-07) |


---

# CAPÍTULO 9 — MATRIZ DE TRAZABILIDAD

> Cadena obligatoria **Objetivo de la monografía → Concepto del SPEC → Historia de usuario → Requisito funcional → Regla de negocio → KPI**. La monografía **no contiene requisitos**; por eso el eslabón «objetivo» se deriva del **módulo** al que pertenece cada requisito y se acompaña del **ancla directa** `[MON §n]` cuando el SPEC la declara en el origen del requisito. Los eslabones marcados `[SRS]` (objetivo por módulo, concepto, historia, KPI) se derivaron en esta fase y **requieren validación del Director** (R-S02).

```
Objetivo de la monografía (OG, OE-1, OE-2, OE-3)
        │  ── se materializa en ──►  Módulo (M-nn)
        ▼
Concepto del SPEC (CD-nn / PR-nn / DC-nn) ──► Historia de usuario (HU-<DOM>-nnn) ──► Requisito funcional (RF-<DOM>-nnn)
                                                                                        │
                                                          Regla de negocio (RN-<DOM>-nnn) ◄──┤──► KPI (KPI-nn)
```

## 9.1 Objetivos de la monografía (transcripción literal)

| ID | Objetivo (Cap. 5 y 5.5 de la monografía, sin modificación) |
|---|---|
| **OG** | «Analizar los factores teóricos para proponer un modelo conceptual de automatización en la gestión de inventarios de PYMES textiles del Eje Cafetero, con el fin de comprender su potencial para mejorar la eficiencia operativa y la competitividad, a partir de una revisión documental.» |
| **OE-1** | «Describir los conceptos clave de automatización de procesos, gestión de inventarios y eficiencia operativa en el contexto de PYMES textiles, identificando definiciones, tipos y beneficios documentos en literatura especializada.» |
| **OE-2** | «Revisar modelos teóricos de automatización aplicados a operaciones logísticas, como frameworks de adopción tecnológica, para evaluar su aplicabilidad en sectores fabricantes tradicionales como el textil colombiano.» |
| **OE-3** | «Sintetizar hallazgos teóricos que permitirán proponer un modelo conceptual integrado, destacando cómo la automatización puede optimizar la trazabilidad, reducir errores y potenciar la competitividad en el Eje Cafetero para 2025, calculando en comparaciones de enfoques documentados.» |

> **Regla `[SRS]`.** Todo requisito contribuye al **OG**; el objetivo específico indicado es el que **más directamente** materializa el módulo. El SPEC/SRS es el modelo conceptual integrado que el OE-3 prometía y la monografía no presentó (vacío C.1.2 de la Auditoría). Las diferencias entre el objetivo transcrito y el proyecto (producto de software frente a modelo conceptual) están registradas en la Auditoría (A.3) y aprobadas como extensión de alcance por el Director.

## 9.2 Objetivos → módulos `[SRS]`

| Módulo | Objetivo más directo | Justificación (ancla) |
|---|:--:|---|
| **M-01** Acceso y Autenticación | OE-3 | Atribución personal de toda acción: base de la trazabilidad [MON §7.1] |
| **M-02** Usuarios y Roles | OE-3 | Segregación de funciones y control: reducción de errores [MON §6] |
| **M-03** Catálogo de Referencias | OE-1 | Gestión de inventarios: maestro de lo que puede existir [MON §7.1] |
| **M-04** Gestión de Lotes | OE-3 | Trazabilidad de origen por lote [MON §7.1] |
| **M-05** Estructura de Bodega | OE-1 | Gestión de inventarios: dónde está la existencia [MON §7.1] |
| **M-06** Identificación QR | OE-3 | Sustitución de digitación por escaneo: reduce errores humanos [MON §7.2] |
| **M-07** Entradas y Recepción | OE-1 | Registro digital de entradas [MON §8.2] |
| **M-08** Salidas | OE-1 | Registro digital de salidas [MON §8.2] |
| **M-09** Movimientos y Transferencias | OE-1 | Registro digital de movimientos [MON §8.2] |
| **M-10** Ajustes de Inventario | OE-3 | Corrección controlada del registro: reducción de errores [MON §6, §8.2] |
| **M-11** Conteos | OE-3 | Medición de exactitud del inventario [MON §8.2] |
| **M-12** Novedades de Mercancía | OE-2 | Vía de reporte sin imputación: mitiga resistencia cultural [MON §4] |
| **M-13** Consulta de Existencia | OE-3 | Visibilidad de la existencia en el momento [MON §6, §7.2] |
| **M-14** Kardex y Trazabilidad | OE-3 | Kardex: materialización de la trazabilidad [MON §7.1] |
| **M-15** Alertas y Reglas | OE-3 | Automatización basada en reglas: anticipar rupturas y sobre stock [MON §3, §7.1] |
| **M-16** Reportes y Exportación Analítica | OE-3 | Evaluación del impacto con indicadores [MON §8.2] |
| **M-17** Dashboard Operativo | OE-3 | Visibilidad operativa para la toma de decisiones [MON §6] |
| **M-18** Auditoría y Bitácora | OE-3 | Verificación independiente de la trazabilidad [MON §7.1] |
| **M-19** Parámetros y Configuración | OE-2 | Adaptación escalonada a la operación real [MON §8.2] |
| **M-20** Notificaciones y Tareas | OE-2 | Guía al operario: reduce la barrera de capacitación [MON §3, §8.2] |

## 9.3 Catálogo de KPI (24)

Se conservan los 24 indicadores del SPEC (Cap. 10) con su fórmula. **Ninguno declara meta numérica**: solo puede fijarse contra la línea base de la empresa piloto (V-03). Los tres primeros son los propuestos por la monografía (Cap. 8.2). La columna «RF» es derivada `[SRS]`.

| KPI | Nombre | Qué mide | Fórmula | Frecuencia | Usuario | Fuente del dato | Origen (SPEC) | RF relacionados |
|---|---|---|---|---|---|---|---|---|
| **KPI-01** | Exactitud del Inventario | La proporción de unidades de inventario cuya existencia registrada coincide con la existencia física verificada mediante conteo | `(Líneas contadas conformes ÷ Total de líneas contadas) × 100` | Al cierre de cada conteo, cíclico o general | Jefe de Bodega · Administrador · Auditor | Módulo M-11 — comparación entre existencia teórica congelada (CD-25) y existencia contada (CD-26) | `[MON §8.2 — «Indicadores como exactitud del inventario»]` | RF-CNT-007, RF-CNT-013, RF-DSH-001, RF-CNT-014, RF-REP-003 |
| **KPI-02** | Exactitud Global del Inventario | Exactitud del inventario completo, medida en el último conteo general | `(Líneas conformes en conteo general ÷ Total de líneas del conteo general) × 100` | A cada conteo general | Administrador · Jefe de Bodega · Auditor | M-11, conteos de tipo general exclusivamente | `[MON §8.2]` `[NUEVO en su distinción del KPI-01]` | RF-CNT-011, RF-CNT-013, RF-CNT-015, RF-REP-008 |
| **KPI-03** | Cobertura de conteo | Qué proporción del inventario fue verificada en el período | `(Líneas contadas ÷ Líneas totales del inventario) × 100` | Mensual | Jefe · Auditor | M-11 | `[NUEVO]` | RF-CNT-001, RF-CNT-012, RF-REP-008 |
| **KPI-04** | Diferencia neta de conteo | Magnitud agregada del descuadre detectado | `Σ (existencia contada − existencia congelada)` en unidades | Por conteo | Jefe · Auditor | M-11 | `[NUEVO]` | RF-CNT-007, RF-REP-008 |
| **KPI-05** | Tiempo Medio de Registro de un Movimiento | Cuánto tarda un operario en registrar un movimiento completo, desde que inicia la operación hasta que el sistema la confirma | `Σ (instante de confirmación − instante de inicio) ÷ Número de movimientos registrados` | Diaria, con acumulado semanal y mensual | Jefe de Bodega · Administrador | M-14 — marcas temporales de inicio y confirmación de cada movimiento | `[MON §8.2 — «tiempos de registro»]` | RF-ENT-011, RF-SAL-009, RF-MOV-001, RF-KDX-001, RF-KDX-009, RF-REP-003 |
| **KPI-06** | Tasa de segundo conteo | Proporción de líneas que requirieron recuento por diferencia sobre tolerancia | `(Líneas con segundo conteo ÷ Líneas contadas) × 100` | Por conteo | Jefe | M-11 | `[NUEVO]` | RF-CNT-008, RF-REP-008 |
| **KPI-07** | Movimientos sin identificador escaneado | Proporción de movimientos registrados sin escaneo, por selección manual | `(Movimientos sin escaneo ÷ Total de movimientos) × 100` | Semanal | Jefe · Coordinador | M-06 · M-14 | `[DC-08]` `[NUEVO]` | RF-QRC-003, RF-QRC-009, RF-REP-008 |
| **KPI-08** | Frecuencia de Errores de Registro | Con qué frecuencia el registro resulta incorrecto y debe corregirse | `(Ajustes correctivos + Movimientos anulados + Líneas de conteo con diferencia) ÷ Total de movimientos del período × 100` | Semanal, con acumulado mensual | Jefe de Bodega · Administrador · Auditor | M-10 (ajustes), M-14 (anulaciones), M-11 (diferencias de conteo) | `[MON §8.2 — «frecuencia de errores»]` | RF-AJU-001, RF-CNT-007, RF-KDX-004, RF-REP-003 |
| **KPI-09** | Integridad del kardex | Unidades donde la existencia no equivale a la suma de sus movimientos | `Número de unidades con discrepancia` (objetivo estructural: cero) | Diaria | Auditor · Administrador | M-18 · RN-INT-004 | `[RN-INT-004]` | RF-INV-003, RF-KDX-006, RF-AUD-007, RF-REP-003 |
| **KPI-10** | Desviaciones de ubicación | Proporción de ubicaciones realizadas en un lugar distinto al propuesto | `(Ubicaciones desviadas ÷ Ubicaciones asignadas) × 100` | Semanal | Coordinador | M-07 · RN-MOV-003 | `[NUEVO]` | RF-BOD-008, RF-BOD-009, RF-REP-008 |
| **KPI-11** | Volumen de movimientos | Actividad total registrada en la bodega | `Número de movimientos confirmados en el período` | Diaria | Jefe · Administrador | M-14 | `[NUEVO]` | RF-ENT-011, RF-SAL-009, RF-MOV-001, RF-REP-003 |
| **KPI-12** | Tiempo medio de recepción | Cuánto tarda una entrada desde su llegada hasta su confirmación | `Σ (instante de confirmación − instante de llegada) ÷ Número de entradas` | Semanal | Coordinador · Jefe | M-07 | `[NUEVO]` | RF-ENT-001, RF-ENT-011, RF-ENT-017, RF-REP-008 |
| **KPI-13** | Tasa de merma | Proporción del inventario dado de baja por daño o pérdida | `(Unidades dadas de baja ÷ Existencia media del período) × 100` | Mensual | Jefe · Administrador | M-08 · RN-SAL-006 | `[MON §7.2 — pérdida de materia prima]` | RF-SAL-010, RF-REP-003 |
| **KPI-14** | Volumen y magnitud de ajustes | Cuánto se corrige el inventario fuera del movimiento físico | `Número de ajustes` y `Σ valor absoluto de las diferencias ajustadas` | Semanal | Jefe · Auditor | M-10 | `[MON §8.2]` | RF-AJU-001, RF-AJU-010, RF-REP-003 |
| **KPI-15** | Tiempo medio en tránsito | Cuánto tardan las transferencias en completarse | `Σ (instante de recepción − instante de despacho) ÷ Número de transferencias` | Semanal | Jefe | M-09 | `[NUEVO]` | RF-MOV-008, RF-MOV-010, RF-REP-008 |
| **KPI-16** | Rotación por referencia | Con qué velocidad sale cada referencia | `Unidades salidas en el período ÷ Existencia media del período` | Mensual | Jefe · Administrador | M-08 · M-13 | `[MON §3 — sobre stock]` | RF-SAL-009, RF-REP-003 |
| **KPI-17** | Existencia sin movimiento | Cuánto inventario lleva más del umbral sin moverse | `Número de unidades sin movimiento en N días` | Mensual | Jefe | M-14 · M-19 | `[MON §3]` | RF-KDX-001, RF-PAR-001, RF-REP-003 |
| **KPI-18** | Ocupación de bodega | Qué proporción de la capacidad física está utilizada | `(Ocupación total ÷ Capacidad total) × 100` | Semanal | Jefe · Coordinador | M-05 · M-13 | `[NUEVO]` | RF-BOD-005, RF-INV-004, RF-REP-008 |
| **KPI-19** | Alertas generadas y atendidas | Cuánto anticipa el sistema y cuánto se actúa sobre ello | `Número de alertas por tipo` y `(Alertas atendidas ÷ Alertas generadas) × 100` | Semanal | Jefe · Administrador | M-15 | `[DC-07]` `[MON §3]` | RF-ALE-001, RF-ALE-004, RF-ALE-005, RF-REP-003 |
| **KPI-20** | Tiempo medio de atención de alerta | Cuánto tarda el equipo en responder a una condición anómala | `Σ (instante de atención − instante de generación) ÷ Número de alertas atendidas` | Semanal | Jefe · Administrador | M-15 | `[NUEVO]` | RF-ALE-005, RF-ALE-007, RF-REP-008 |
| **KPI-21** | Eventos de ruptura de stock | Cuántas veces una referencia activa llegó a existencia cero | `Número de eventos de existencia cero en referencias activas` | Mensual | Jefe · Administrador | M-15 · M-13 | `[MON §3 — rupturas de stock]` | RF-ALE-004, RF-REP-003 |
| **KPI-22** | Tiempo medio de aprobación | Cuánto tarda resolverse una solicitud de ajuste o de salida | `Σ (instante de resolución − instante de solicitud) ÷ Número de solicitudes` | Semanal | Administrador | M-10 · M-08 | `[NUEVO]` | RF-SAL-006, RF-AJU-004, RF-AJU-008, RF-REP-008 |
| **KPI-23** | Novedades reportadas y resueltas | Cuántas anomalías físicas afloran y con qué velocidad se cierran | `Número de novedades por tipo` y `tiempo medio de resolución` | Mensual | Jefe · Coordinador | M-12 | `[NUEVO]` | RF-NOV-001, RF-NOV-004, RF-NOV-006, RF-REP-008 |
| **KPI-24** | Adopción del sistema | Qué proporción de la operación pasa efectivamente por el sistema | `(Movimientos registrados en el sistema ÷ Movimientos estimados totales) × 100` | Mensual | Administrador · Auditor | M-14 + verificación de campo | `[MON §4 — resistencia a la adopción]` `[AUD OP-01]` | RF-KDX-001, RF-PAR-007, RF-REP-003 |

> **Hallazgo H-12.** KPI-05, KPI-07, KPI-10, KPI-12, KPI-17 y KPI-24 necesitan un dato que ningún RF exige capturar (Anexo C, C.2.2).

## 9.4 Matriz principal: objetivo → concepto → historia → RF → regla → KPI

Una fila por cada uno de los 185 RF. «Ancla MON» = apartado(s) de la monografía que el SPEC declara en el origen del RF; vacío si el origen es `[NUEVO]`, `[DC]`, `[PR]`, `[AUD]`.

| Objetivo `[SRS]` | Ancla MON | Concepto (SPEC) | Historia(s) | RF | Regla(s) | KPI |
|:--:|---|---|---|---|---|---|
| OE-3 | — | PR-05 | HU-ACC-001 | **RF-ACC-001** | RN-INT-001 | — |
| OE-3 | — | PR-05 | HU-ACC-001 | **RF-ACC-002** | RN-INT-001 | — |
| OE-3 | — | CD-47 | HU-ACC-001, HU-AUD-001 | **RF-ACC-003** | RN-AUD-001 | — |
| OE-3 | — | CD-47 | HU-ACC-001 | **RF-ACC-004** | — | — |
| OE-3 | — | PR-05 | HU-ACC-002 | **RF-ACC-005** | — | — |
| OE-3 | — | PR-05 | HU-ACC-003 | **RF-ACC-006** | — | — |
| OE-3 | — | PR-05 | HU-ACC-004 | **RF-ACC-007** | — | — |
| OE-3 | — | DC-04 | HU-USR-001 | **RF-USR-001** | RN-INT-001, RN-MAE-006 | — |
| OE-3 | — | DC-04 | HU-USR-001 | **RF-USR-002** | — | — |
| OE-3 | — | DC-04 | HU-USR-001 | **RF-USR-003** | — | — |
| OE-3 | — | DC-04 | HU-USR-002 | **RF-USR-004** | RN-MAE-007, RN-MAE-008, RN-MAE-009 | — |
| OE-3 | §7.1 | CD-28 | HU-USR-002 | **RF-USR-005** | RN-MAE-007, RN-MAE-008 | — |
| OE-3 | — | DC-04 | HU-USR-005, HU-USR-003 | **RF-USR-006** | RN-MAE-004 | — |
| OE-3 | — | CD-12, CD-13 | HU-USR-004 | **RF-USR-007** | — | — |
| OE-3 | — | CD-47 | HU-USR-003 | **RF-USR-008** | RN-AUD-001 | — |
| OE-1 | — | CD-01, CD-02, CD-10 | HU-CAT-001 | **RF-CAT-001** | RN-MAE-001 | — |
| OE-1 | — | CD-02 | HU-CAT-001 | **RF-CAT-002** | RN-MAE-001 | — |
| OE-1 | — | CD-03, CD-04 | HU-CAT-001 | **RF-CAT-003** | — | — |
| OE-1 | — | CD-05 | HU-CAT-001 | **RF-CAT-004** | — | — |
| OE-1 | — | CD-11 | HU-CAT-002 | **RF-CAT-005** | RN-INT-007, RN-MAE-002 | — |
| OE-1 | — | CD-02, CD-18 | HU-CAT-003 | **RF-CAT-006** | RN-MAE-003 | — |
| OE-1 | §3, §7.1 | CD-05, CD-46 | HU-CAT-004 | **RF-CAT-007** | — | — |
| OE-1 | — | CD-05, CD-46 | HU-CAT-004 | **RF-CAT-008** | — | — |
| OE-1 | — | CD-02 | HU-CAT-005 | **RF-CAT-009** | — | — |
| OE-1 | — | CD-10, CD-13 | HU-CAT-006 | **RF-CAT-010** | — | — |
| OE-3 | §7.1 | CD-06 | HU-LOT-001 | **RF-LOT-001** | RN-LOT-001 | — |
| OE-3 | §7.1 | CD-06, CD-07 | HU-LOT-001 | **RF-LOT-002** | RN-LOT-001 | — |
| OE-3 | — | CD-06 | HU-LOT-001 | **RF-LOT-003** | RN-MAE-006 | — |
| OE-3 | §7.1 | CD-06, CD-14 | HU-LOT-002 | **RF-LOT-004** | RN-LOT-002 | — |
| OE-3 | — | CD-06, CD-22 | HU-LOT-003 | **RF-LOT-005** | RN-EXI-006, RN-LOT-003, RN-LOT-004 | — |
| OE-3 | — | CD-06 | HU-LOT-004 | **RF-LOT-006** | RN-LOT-005 | — |
| OE-1 | — | CD-12, CD-13, CD-14 | HU-BOD-001 | **RF-BOD-001** | RN-EXI-002, RN-MAE-006 | — |
| OE-1 | — | CD-14 | HU-BOD-001 | **RF-BOD-002** | RN-MAE-006 | — |
| OE-1 | — | CD-16 | HU-BOD-001 | **RF-BOD-003** | RN-EXI-002 | — |
| OE-1 | — | CD-14, CD-19 | HU-BOD-001, HU-ENT-006 | **RF-BOD-004** | RN-EXI-002 | — |
| OE-1 | — | CD-15 | HU-BOD-002, HU-ENT-006 | **RF-BOD-005** | RN-MOV-002 | KPI-18 |
| OE-1 | — | CD-14 | HU-BOD-003 | **RF-BOD-006** | RN-MAE-005 | — |
| OE-1 | — | CD-13 | HU-BOD-004 | **RF-BOD-007** | RN-ALE-005 | — |
| OE-1 | — | CD-13, CD-14 | HU-BOD-005, HU-ENT-006 | **RF-BOD-008** | RN-MOV-001 | KPI-10 |
| OE-1 | — | CD-14 | HU-ENT-006 | **RF-BOD-009** | RN-MOV-003 | KPI-10 |
| OE-3 | — | CD-07, CD-08 | HU-QRC-001 | **RF-QRC-001** | RN-IDE-001, RN-IDE-002 | — |
| OE-3 | — | CD-08 | HU-QRC-001 | **RF-QRC-002** | RN-IDE-002 | — |
| OE-3 | — | CD-08 | HU-QRC-002 | **RF-QRC-003** | RN-IDE-001 | KPI-07 |
| OE-3 | — | CD-08, CD-14 | HU-QRC-003 | **RF-QRC-004** | RN-IDE-002 | — |
| OE-3 | — | CD-08 | HU-QRC-001 | **RF-QRC-005** | — | — |
| OE-3 | — | CD-08 | HU-QRC-004 | **RF-QRC-006** | RN-IDE-004 | — |
| OE-3 | — | CD-08 | HU-QRC-004 | **RF-QRC-007** | RN-IDE-004 | — |
| OE-3 | — | CD-09 | HU-QRC-005 | **RF-QRC-008** | RN-IDE-003 | — |
| OE-3 | — | CD-08, CD-28 | HU-QRC-002 | **RF-QRC-009** | — | KPI-07 |
| OE-1 | §8.2 | CD-35 | HU-ENT-001 | **RF-ENT-001** | — | KPI-12 |
| OE-1 | — | CD-35 | HU-ENT-001 | **RF-ENT-002** | — | — |
| OE-1 | — | CD-02, CD-35 | HU-ENT-007 | **RF-ENT-003** | RN-ENT-001, RN-MAE-001 | — |
| OE-1 | — | CD-35 | HU-ENT-001 | **RF-ENT-004** | RN-ENT-002 | — |
| OE-1 | §3, §8.2 | CD-16, CD-35 | HU-ENT-002 | **RF-ENT-005** | RN-INT-003, RN-INT-008 | — |
| OE-1 | — | CD-35 | HU-ENT-002 | **RF-ENT-006** | — | — |
| OE-1 | — | CD-35 | HU-ENT-004 | **RF-ENT-007** | RN-ENT-003 | — |
| OE-1 | — | CD-35 | HU-ENT-004 | **RF-ENT-008** | RN-ENT-004 | — |
| OE-1 | — | CD-35 | HU-ENT-004 | **RF-ENT-009** | RN-ENT-005 | — |
| OE-1 | — | CD-29, CD-35 | HU-ENT-003 | **RF-ENT-010** | RN-ENT-007 | — |
| OE-1 | §7.1 | CD-29, CD-37 | HU-ENT-003 | **RF-ENT-011** | RN-EXI-007, RN-INT-002, RN-INT-004 | KPI-05, KPI-11, KPI-12 |
| OE-1 | — | CD-17, CD-22 | HU-ENT-005 | **RF-ENT-012** | RN-ENT-006 | — |
| OE-1 | — | CD-35 | HU-ENT-008 | **RF-ENT-013** | — | — |
| OE-1 | — | CD-49, CD-35 | HU-ENT-009 | **RF-ENT-014** | RN-LOT-006, RN-LOT-007 | — |
| OE-1 | — | CD-49, CD-35 | HU-ENT-009 | **RF-ENT-015** | RN-ENT-003, RN-LOT-007 | — |
| OE-1 | — | CD-49 | HU-ENT-010 | **RF-ENT-016** | RN-LOT-006 | — |
| OE-1 | — | CD-35 | HU-ENT-002 | **RF-ENT-017** | — | KPI-12 |
| OE-1 | — | CD-30, CD-36 | HU-SAL-001 | **RF-SAL-001** | RN-SAL-002 | — |
| OE-1 | — | CD-30 | HU-SAL-001 | **RF-SAL-002** | RN-SAL-002 | — |
| OE-1 | — | CD-19 | HU-SAL-001 | **RF-SAL-003** | RN-EXI-003 | — |
| OE-1 | — | CD-18 | HU-SAL-004 | **RF-SAL-004** | RN-EXI-001 | — |
| OE-1 | — | CD-20 | HU-SAL-002 | **RF-SAL-005** | RN-EXI-004 | — |
| OE-1 | — | CD-30, CD-46 | HU-SAL-007 | **RF-SAL-006** | RN-SAL-001 | KPI-22 |
| OE-1 | — | CD-30 | HU-SAL-003 | **RF-SAL-007** | RN-SAL-003 | — |
| OE-1 | — | CD-08 | HU-SAL-003 | **RF-SAL-008** | RN-SAL-004 | — |
| OE-1 | §7.1 | CD-20, CD-30 | HU-SAL-003, HU-SAL-001 | **RF-SAL-009** | RN-EXI-004, RN-INT-004 | KPI-05, KPI-11, KPI-16 |
| OE-1 | — | CD-30, CD-36 | HU-SAL-005 | **RF-SAL-010** | RN-SAL-006 | KPI-13 |
| OE-1 | — | CD-29, CD-30 | HU-SAL-006 | **RF-SAL-011** | RN-SAL-007 | — |
| OE-1 | — | CD-49, CD-30 | HU-SAL-008 | **RF-SAL-012** | RN-SAL-004, RN-SAL-009 | — |
| OE-1 | — | CD-49, CD-30 | HU-SAL-009 | **RF-SAL-013** | RN-EXI-001, RN-SAL-008 | — |
| OE-1 | — | CD-20, CD-30 | HU-SAL-002 | **RF-SAL-014** | RN-SAL-005 | — |
| OE-1 | — | CD-31 | HU-MOV-001 | **RF-MOV-001** | RN-MOV-002, RN-MOV-004, RN-MOV-010 | KPI-05, KPI-11 |
| OE-1 | — | CD-18, CD-31 | HU-MOV-001 | **RF-MOV-002** | RN-MOV-004, RN-MOV-010 | — |
| OE-1 | — | CD-31 | HU-MOV-002 | **RF-MOV-003** | RN-EXI-003 | — |
| OE-1 | — | CD-31 | HU-MOV-002 | **RF-MOV-004** | RN-MOV-005 | — |
| OE-1 | — | CD-14, CD-15 | HU-MOV-002, HU-ENT-006 | **RF-MOV-005** | RN-MOV-002, RN-MOV-010 | — |
| OE-1 | — | CD-22 | HU-MOV-002 | **RF-MOV-006** | RN-EXI-006 | — |
| OE-1 | — | CD-20, CD-32 | HU-MOV-003 | **RF-MOV-007** | RN-EXI-003, RN-EXI-004 | — |
| OE-1 | — | CD-32 | HU-MOV-004 | **RF-MOV-008** | RN-EXI-005 | KPI-15 |
| OE-1 | — | CD-23 | HU-MOV-004 | **RF-MOV-009** | RN-EXI-005 | — |
| OE-1 | — | CD-32 | HU-MOV-005 | **RF-MOV-010** | RN-MOV-007 | KPI-15 |
| OE-1 | — | CD-23, CD-32, CD-45 | HU-MOV-006, HU-MOV-007 | **RF-MOV-011** | RN-MOV-008, RN-MOV-009 | — |
| OE-1 | — | CD-49, CD-31 | HU-MOV-008 | **RF-MOV-012** | RN-MOV-010, RN-MOV-011, RN-MOV-012 | — |
| OE-1 | — | CD-23, CD-31 | HU-MOV-009 | **RF-MOV-013** | RN-MOV-006 | — |
| OE-3 | §8.2 | CD-27, CD-33 | HU-AJU-001 | **RF-AJU-001** | RN-AJU-003, RN-EXI-001 | KPI-08, KPI-14 |
| OE-3 | — | CD-33, CD-36 | HU-AJU-001 | **RF-AJU-002** | RN-AJU-003 | — |
| OE-3 | — | CD-33 | HU-AJU-001 | **RF-AJU-003** | RN-AJU-003 | — |
| OE-3 | — | CD-33, CD-46 | HU-AJU-003, HU-TAR-002 | **RF-AJU-004** | RN-AJU-002 | KPI-22 |
| OE-3 | — | CD-33 | HU-AJU-002 | **RF-AJU-005** | RN-AJU-001 | — |
| OE-3 | — | CD-18, CD-33 | HU-AJU-004 | **RF-AJU-006** | RN-EXI-001 | — |
| OE-3 | §7.1 | CD-24, CD-33, CD-37 | HU-AJU-001, HU-AJU-002 | **RF-AJU-007** | RN-INT-002, RN-INT-004 | — |
| OE-3 | — | CD-33 | HU-AJU-002, HU-TAR-002 | **RF-AJU-008** | RN-AJU-006 | KPI-22 |
| OE-3 | — | CD-33, CD-45 | HU-AJU-005 | **RF-AJU-009** | RN-AJU-004 | — |
| OE-3 | — | CD-33 | HU-AJU-006 | **RF-AJU-010** | — | KPI-14 |
| OE-3 | — | CD-39 | HU-CNT-001 | **RF-CNT-001** | — | KPI-03 |
| OE-3 | — | CD-39 | HU-CNT-001 | **RF-CNT-002** | — | — |
| OE-3 | — | CD-25 | HU-CNT-001, HU-CNT-003 | **RF-CNT-003** | RN-CNT-001 | — |
| OE-3 | — | CD-25 | HU-CNT-003 | **RF-CNT-004** | RN-CNT-001 | — |
| OE-3 | — | CD-41 | HU-CNT-001 | **RF-CNT-005** | — | — |
| OE-3 | — | CD-26 | HU-CNT-002 | **RF-CNT-006** | RN-CNT-002 | — |
| OE-3 | §8.2 | CD-27 | HU-CNT-004, HU-CNT-005 | **RF-CNT-007** | RN-CNT-001 | KPI-01, KPI-04, KPI-08 |
| OE-3 | — | CD-42 | HU-CNT-004 | **RF-CNT-008** | RN-CNT-003 | KPI-06 |
| OE-3 | — | CD-42 | HU-CNT-004 | **RF-CNT-009** | RN-CNT-003 | — |
| OE-3 | — | CD-38 | HU-CNT-005 | **RF-CNT-010** | RN-CNT-003, RN-CNT-004 | — |
| OE-3 | — | CD-40 | HU-CNT-006 | **RF-CNT-011** | RN-CNT-006 | KPI-02 |
| OE-3 | — | CD-40 | HU-CNT-007 | **RF-CNT-012** | RN-CNT-007 | KPI-03 |
| OE-3 | §8.2 | CD-43 | HU-CNT-008 | **RF-CNT-013** | — | KPI-01, KPI-02 |
| OE-3 | — | CD-49, CD-38 | HU-CNT-010 | **RF-CNT-014** | RN-CNT-002, RN-CNT-009 | KPI-01 |
| OE-3 | — | CD-40, CD-45 | HU-CNT-011 | **RF-CNT-015** | RN-CNT-008 | KPI-02 |
| OE-2 | §4 | CD-48 | HU-NOV-001 | **RF-NOV-001** | — | KPI-23 |
| OE-2 | — | CD-08, CD-48 | HU-NOV-001 | **RF-NOV-002** | — | — |
| OE-2 | §4 | CD-48 | HU-NOV-001 | **RF-NOV-003** | — | — |
| OE-2 | — | CD-48 | HU-NOV-002, HU-NOV-003 | **RF-NOV-004** | — | KPI-23 |
| OE-2 | — | CD-48 | HU-NOV-002 | **RF-NOV-005** | RN-NOV-003 | — |
| OE-2 | — | CD-48 | HU-NOV-002 | **RF-NOV-006** | RN-MAE-007 | KPI-23 |
| OE-2 | — | CD-33, CD-48 | HU-NOV-004 | **RF-NOV-007** | RN-NOV-001 | — |
| OE-2 | — | CD-45, CD-48 | HU-NOV-003 | **RF-NOV-008** | RN-NOV-002 | — |
| OE-3 | §6, §7.2 | CD-18 | HU-INV-001, HU-INV-002, HU-INV-003, HU-INV-004 | **RF-INV-001** | RN-INT-004, RN-INT-006 | — |
| OE-3 | — | CD-44 | HU-INV-001 | **RF-INV-002** | RN-EXI-003, RN-EXI-004, RN-EXI-005, RN-EXI-006, RN-EXI-007 | — |
| OE-3 | — | CD-18, CD-37 | HU-INV-001 | **RF-INV-003** | RN-INT-004 | KPI-09 |
| OE-3 | — | CD-14, CD-18 | HU-INV-003 | **RF-INV-004** | RN-INT-005 | KPI-18 |
| OE-3 | — | CD-18 | HU-INV-002 | **RF-INV-005** | — | — |
| OE-3 | §7.1 | CD-18, CD-37 | HU-INV-005 | **RF-INV-006** | RN-INT-004 | — |
| OE-3 | §8.2 | CD-02 | HU-INV-006 | **RF-INV-007** | — | — |
| OE-3 | — | CD-18 | HU-INV-002 | **RF-INV-008** | RN-INT-006 | — |
| OE-3 | — | CD-49, CD-18 | HU-KDX-006 | **RF-INV-009** | RN-LOT-006 | — |
| OE-3 | §7.1 | CD-21, CD-28, CD-37 | HU-KDX-001 | **RF-KDX-001** | RN-INT-001, RN-INT-002 | KPI-05, KPI-17, KPI-24 |
| OE-3 | — | CD-28 | HU-KDX-001 | **RF-KDX-002** | RN-INT-001 | — |
| OE-3 | — | CD-37 | HU-KDX-002 | **RF-KDX-003** | RN-INT-002 | — |
| OE-3 | — | CD-34 | HU-KDX-002 | **RF-KDX-004** | RN-AJU-007, RN-INT-002 | KPI-08 |
| OE-3 | §7.1 | CD-21, CD-37 | HU-KDX-001, HU-KDX-004 | **RF-KDX-005** | — | — |
| OE-3 | — | CD-18, CD-37 | HU-KDX-003 | **RF-KDX-006** | RN-AUD-005, RN-INT-004 | KPI-09 |
| OE-3 | — | CD-37 | HU-KDX-005 | **RF-KDX-007** | — | — |
| OE-3 | — | CD-49, CD-37 | HU-KDX-006 | **RF-KDX-008** | RN-LOT-007 | — |
| OE-3 | — | CD-28, CD-37 | HU-KDX-001 | **RF-KDX-009** | — | KPI-05 |
| OE-3 | — | CD-45 | HU-ALE-001, HU-ALE-002 | **RF-ALE-001** | — | KPI-19 |
| OE-3 | — | CD-45 | HU-ALE-001 | **RF-ALE-002** | — | — |
| OE-3 | — | CD-45 | HU-ALE-001 | **RF-ALE-003** | RN-ALE-005 | — |
| OE-3 | §3, §7.1 | CD-45 | HU-ALE-001, HU-ALE-002 | **RF-ALE-004** | RN-AJU-004, RN-AJU-005, RN-CNT-005, RN-MOV-002, RN-MOV-008 | KPI-19, KPI-21 |
| OE-3 | — | CD-45 | HU-ALE-003 | **RF-ALE-005** | RN-ALE-004 | KPI-19, KPI-20 |
| OE-3 | — | CD-45 | HU-ALE-005 | **RF-ALE-006** | RN-ALE-001 | — |
| OE-3 | — | CD-45 | HU-ALE-004 | **RF-ALE-007** | RN-ALE-002, RN-ALE-003 | KPI-20 |
| OE-3 | §8.2 | CD-18, CD-28 | HU-REP-001, HU-REP-002 | **RF-REP-001** | — | — |
| OE-3 | — | CD-43 | HU-REP-001 | **RF-REP-002** | — | — |
| OE-3 | §8.2 | CD-43 | HU-CNT-008 | **RF-REP-003** | — | KPI-01, KPI-05, KPI-08, KPI-09, KPI-11, KPI-13, KPI-14, KPI-16, KPI-17, KPI-19, KPI-21, KPI-24 |
| OE-3 | — | DC-06 | HU-REP-003 | **RF-REP-004** | — | — |
| OE-3 | — | DC-06 | HU-REP-003 | **RF-REP-005** | — | — |
| OE-3 | — | CD-47 | HU-REP-002, HU-REP-003 | **RF-REP-006** | RN-AUD-001, RN-AUD-003 | — |
| OE-3 | — | DC-06 | HU-REP-004 | **RF-REP-007** | — | — |
| OE-3 | — | CD-43 | HU-CNT-008 | **RF-REP-008** | — | KPI-02, KPI-03, KPI-04, KPI-06, KPI-07, KPI-10, KPI-12, KPI-15, KPI-18, KPI-20, KPI-22, KPI-23 |
| OE-3 | — | CD-19, CD-45 | HU-DSH-001 | **RF-DSH-001** | — | KPI-01 |
| OE-3 | — | CD-18 | HU-DSH-001 | **RF-DSH-002** | — | — |
| OE-3 | — | CD-13 | HU-DSH-003 | **RF-DSH-003** | — | — |
| OE-3 | — | PR-06 | HU-DSH-002 | **RF-DSH-004** | — | — |
| OE-3 | — | CD-47 | HU-AUD-001 | **RF-AUD-001** | RN-AUD-001 | — |
| OE-3 | — | CD-47 | HU-AUD-001 | **RF-AUD-002** | RN-AUD-001 | — |
| OE-3 | — | CD-47 | HU-AUD-001 | **RF-AUD-003** | RN-AUD-001 | — |
| OE-3 | — | ROL-05 | HU-AUD-002 | **RF-AUD-004** | — | — |
| OE-3 | — | ROL-05 | HU-AUD-002 | **RF-AUD-005** | — | — |
| OE-3 | — | ROL-05 | HU-AUD-003 | **RF-AUD-006** | RN-AUD-002 | — |
| OE-3 | — | CD-47 | HU-AUD-004 | **RF-AUD-007** | RN-AJU-001, RN-AUD-001 | KPI-09 |
| OE-2 | — | CD-46 | HU-PAR-001 | **RF-PAR-001** | RN-AJU-002, RN-CNT-003, RN-MOV-008, RN-SAL-001 | KPI-17 |
| OE-2 | — | CD-46 | HU-PAR-001 | **RF-PAR-002** | — | — |
| OE-2 | — | CD-47 | HU-PAR-001 | **RF-PAR-003** | RN-AUD-001, RN-AUD-004 | — |
| OE-2 | — | CD-46 | HU-PAR-001 | **RF-PAR-004** | RN-AUD-004 | — |
| OE-2 | — | CD-36 | HU-PAR-002 | **RF-PAR-005** | RN-AJU-003 | — |
| OE-2 | — | CD-46 | HU-PAR-003 | **RF-PAR-006** | RN-AJU-001, RN-AJU-003, RN-AUD-001, RN-CNT-002, RN-CNT-003, RN-EXI-001, RN-INT-001, RN-INT-002, RN-INT-004, RN-MAE-007 | — |
| OE-2 | — | CD-46 | HU-PAR-001 | **RF-PAR-007** | — | KPI-24 |
| OE-2 | — | CD-41 | HU-TAR-001 | **RF-TAR-001** | — | — |
| OE-2 | — | CD-41 | HU-TAR-001, HU-DSH-002 | **RF-TAR-002** | — | — |
| OE-2 | — | CD-28 | HU-TAR-001, HU-DSH-002 | **RF-TAR-003** | — | — |
| OE-2 | — | CD-41, CD-42 | HU-TAR-003, HU-CNT-009 | **RF-TAR-004** | RN-CNT-003 | — |
| OE-2 | — | DC-05 | HU-TAR-001 | **RF-TAR-005** | — | — |
| OE-2 | — | PN-14 | HU-TAR-004 | **RF-TAR-006** | — | — |
| OE-2 | — | PN-14 | HU-TAR-004 | **RF-TAR-007** | — | — |
| OE-2 | — | PN-14 | HU-TAR-005 | **RF-TAR-008** | RN-INT-003 | — |

## 9.5 Cobertura por regla de negocio (92)

| Regla | Tipo | Proceso(s) | Caso(s) de uso | Historia(s) | RF |
|---|:--:|---|---|---|---|
| **RN-INT-001** | Estr. | — | — | HU-ACC-001, HU-USR-001, HU-KDX-001, HU-PAR-003 | RF-ACC-001, RF-ACC-002, RF-USR-001, RF-KDX-001, RF-KDX-002, RF-PAR-006 |
| **RN-INT-002** | Estr. | PN-13 | CU-18 | HU-ENT-003, HU-AJU-001, HU-AJU-002, HU-KDX-001, HU-KDX-002, HU-PAR-003 | RF-ENT-011, RF-AJU-007, RF-KDX-001, RF-KDX-003, RF-KDX-004, RF-PAR-006 |
| **RN-INT-003** | Estr. | PN-01, PN-05, PN-14 | CU-06, CU-10, CU-19 | HU-ENT-002, HU-TAR-005 | RF-ENT-005, RF-TAR-008 |
| **RN-INT-004** | Estr. | PN-13 | CU-18 | HU-ENT-003, HU-SAL-001, HU-SAL-003, HU-AJU-001, HU-AJU-002, HU-INV-001, HU-INV-002, HU-INV-003, HU-INV-004, HU-INV-005, HU-KDX-003, HU-PAR-003 | RF-ENT-011, RF-SAL-009, RF-AJU-007, RF-INV-001, RF-INV-003, RF-INV-006, RF-KDX-006, RF-PAR-006 |
| **RN-INT-005** | Estr. | — | — | HU-INV-003 | RF-INV-004 |
| **RN-INT-006** | Estr. | — | — | HU-INV-001, HU-INV-002, HU-INV-003, HU-INV-004 | RF-INV-001, RF-INV-008 |
| **RN-INT-007** | Estr. | — | — | HU-CAT-002 | RF-CAT-005 |
| **RN-INT-008** | Estr. | PN-01, PN-05 | CU-06, CU-10 | HU-ENT-002 | RF-ENT-005 |
| **RN-EXI-001** | Estr. | PN-07 | CU-12 | HU-SAL-004, HU-AJU-001, HU-AJU-004, HU-NOV-004, HU-PAR-003, HU-SAL-009 | RF-SAL-004, RF-AJU-001, RF-AJU-006, RF-PAR-006, RF-SAL-013 |
| **RN-EXI-002** | Estr. | — | — | HU-BOD-001, HU-ENT-006, HU-NOV-004 | RF-BOD-001, RF-BOD-003, RF-BOD-004 |
| **RN-EXI-003** | Estr. | PN-05, PN-06, PN-10 | CU-10, CU-11, CU-15 | HU-SAL-001, HU-MOV-002, HU-MOV-003, HU-INV-001, HU-SAL-008 | RF-SAL-003, RF-MOV-003, RF-MOV-007, RF-INV-002 |
| **RN-EXI-004** | Estr. | PN-06, PN-10 | CU-11, CU-15 | HU-SAL-001, HU-SAL-002, HU-SAL-003, HU-MOV-003, HU-INV-001 | RF-SAL-005, RF-SAL-009, RF-MOV-007, RF-INV-002 |
| **RN-EXI-005** | Estr. | PN-06 | CU-11 | HU-MOV-004, HU-INV-001 | RF-MOV-008, RF-MOV-009, RF-INV-002 |
| **RN-EXI-006** | Estr. | PN-05, PN-07, PN-10 | CU-10, CU-12, CU-15 | HU-LOT-003, HU-MOV-002, HU-INV-001 | RF-LOT-005, RF-MOV-006, RF-INV-002 |
| **RN-EXI-007** | Estr. | PN-01 | CU-06 | HU-ENT-003, HU-INV-001 | RF-ENT-011, RF-INV-002 |
| **RN-MAE-001** | Estr. | PN-01 | CU-06 | HU-CAT-001, HU-ENT-007 | RF-CAT-001, RF-CAT-002, RF-ENT-003 |
| **RN-MAE-002** | Estr. | — | — | HU-CAT-002 | RF-CAT-005 |
| **RN-MAE-003** | Estr. | — | — | HU-CAT-003 | RF-CAT-006 |
| **RN-MAE-004** | Estr. | — | — | HU-USR-003, HU-USR-005 | RF-USR-006 |
| **RN-MAE-005** | Estr. | — | — | HU-BOD-003 | RF-BOD-006 |
| **RN-MAE-006** | Estr. | — | — | HU-USR-001, HU-LOT-001, HU-BOD-001 | RF-USR-001, RF-LOT-003, RF-BOD-001, RF-BOD-002 |
| **RN-MAE-007** | Estr. | PN-12 | CU-17 | HU-USR-002, HU-CAT-003, HU-CAT-006, HU-BOD-003, HU-NOV-002, HU-PAR-002, HU-PAR-003 | RF-USR-004, RF-USR-005, RF-NOV-006, RF-PAR-006 |
| **RN-MAE-008** | Estr. | — | — | HU-USR-002 | RF-USR-004, RF-USR-005 |
| **RN-MAE-009** | Conf. | — | — | HU-USR-002 | RF-USR-004 |
| **RN-IDE-001** | Estr. | PN-02, PN-05 | CU-07, CU-10 | HU-QRC-001, HU-QRC-002, HU-NOV-004 | RF-QRC-001, RF-QRC-003 |
| **RN-IDE-002** | Estr. | PN-02 | CU-07 | HU-QRC-001, HU-QRC-003, HU-NOV-004 | RF-QRC-001, RF-QRC-002, RF-QRC-004 |
| **RN-IDE-003** | Estr. | PN-02 | CU-07 | HU-QRC-005 | RF-QRC-008 |
| **RN-IDE-004** | Estr. | PN-02 | CU-07 | HU-QRC-004 | RF-QRC-006, RF-QRC-007 |
| **RN-LOT-001** | Estr. | — | — | HU-LOT-001 | RF-LOT-001, RF-LOT-002 |
| **RN-LOT-002** | Estr. | — | — | HU-LOT-002 | RF-LOT-004 |
| **RN-LOT-003** | Estr. | — | — | HU-LOT-003 | RF-LOT-005 |
| **RN-LOT-004** | Estr. | — | — | HU-LOT-003 | RF-LOT-005 |
| **RN-LOT-005** | Conf. | — | — | HU-LOT-004 | RF-LOT-006 |
| **RN-LOT-006** | Estr. | — | — | HU-ENT-009, HU-ENT-010, HU-KDX-006 | RF-ENT-014, RF-ENT-016, RF-INV-009 |
| **RN-LOT-007** | Estr. | — | — | HU-ENT-009, HU-KDX-006 | RF-ENT-014, RF-ENT-015, RF-KDX-008 |
| **RN-ENT-001** | Estr. | — | — | HU-ENT-007 | RF-ENT-003 |
| **RN-ENT-002** | Conf. | PN-01 | CU-06 | HU-ENT-001 | RF-ENT-004 |
| **RN-ENT-003** | Estr. | PN-01 | CU-06 | HU-ENT-004, HU-ENT-009 | RF-ENT-007, RF-ENT-015 |
| **RN-ENT-004** | Conf. | PN-01 | CU-06 | HU-ENT-004 | RF-ENT-008 |
| **RN-ENT-005** | Estr. | PN-01 | CU-06 | HU-ENT-004 | RF-ENT-009 |
| **RN-ENT-006** | Estr. | PN-01 | CU-06 | HU-ENT-005 | RF-ENT-012 |
| **RN-ENT-007** | Estr. | — | — | HU-ENT-003 | RF-ENT-010 |
| **RN-SAL-001** | Conf. | PN-10 | CU-15 | HU-SAL-007, HU-PAR-001 | RF-SAL-006, RF-PAR-001 |
| **RN-SAL-002** | Estr. | PN-10 | CU-15 | HU-SAL-001, HU-SAL-009 | RF-SAL-001, RF-SAL-002 |
| **RN-SAL-003** | Conf. | PN-10 | CU-15 | HU-SAL-003 | RF-SAL-007 |
| **RN-SAL-004** | Estr. | PN-10 | CU-15 | HU-SAL-003, HU-SAL-008 | RF-SAL-008, RF-SAL-012 |
| **RN-SAL-005** | Conf. | PN-10 | CU-15 | HU-SAL-002 | RF-SAL-014 |
| **RN-SAL-006** | Estr. | PN-10 | CU-15 | HU-SAL-005 | RF-SAL-010 |
| **RN-SAL-007** | Estr. | PN-10 | CU-15 | HU-SAL-006 | RF-SAL-011 |
| **RN-SAL-008** | Estr. | — | — | HU-SAL-009 | RF-SAL-013 |
| **RN-SAL-009** | Estr. | — | — | HU-SAL-008 | RF-SAL-012 |
| **RN-MOV-001** | Conf. | — | — | HU-BOD-005, HU-ENT-006 | RF-BOD-008 |
| **RN-MOV-002** | Conf. | PN-03, PN-05, PN-11 | CU-08, CU-10, CU-16 | HU-BOD-002, HU-ENT-006, HU-MOV-001, HU-MOV-002, HU-ALE-001, HU-ALE-002 | RF-BOD-005, RF-MOV-001, RF-MOV-005, RF-ALE-004 |
| **RN-MOV-003** | Conf. | PN-03 | CU-08 | HU-BOD-005, HU-ENT-006 | RF-BOD-009 |
| **RN-MOV-004** | Estr. | PN-03, PN-05 | CU-08, CU-10 | HU-MOV-001, HU-MOV-008 | RF-MOV-001, RF-MOV-002 |
| **RN-MOV-005** | Estr. | PN-05 | CU-10 | HU-MOV-002 | RF-MOV-004 |
| **RN-MOV-006** | Conf. | PN-05, PN-14 | CU-10, CU-19 | HU-MOV-009 | RF-MOV-013 |
| **RN-MOV-007** | Estr. | PN-06 | CU-11 | HU-MOV-005 | RF-MOV-010 |
| **RN-MOV-008** | Conf. | PN-06, PN-11 | CU-11, CU-16 | HU-MOV-006, HU-MOV-007, HU-ALE-001, HU-ALE-002, HU-PAR-001 | RF-MOV-011, RF-ALE-004, RF-PAR-001 |
| **RN-MOV-009** | Estr. | PN-06 | CU-11 | HU-MOV-006, HU-MOV-007 | RF-MOV-011 |
| **RN-MOV-010** | Estr. | PN-03 | CU-08 | HU-ENT-006, HU-MOV-001, HU-MOV-002, HU-MOV-008 | RF-MOV-001, RF-MOV-002, RF-MOV-005, RF-MOV-012 |
| **RN-MOV-011** | Estr. | — | — | HU-MOV-008 | RF-MOV-012 |
| **RN-MOV-012** | Estr. | — | — | HU-MOV-001, HU-MOV-008 | RF-MOV-012 |
| **RN-AJU-001** | Estr. | PN-07, PN-13 | CU-12, CU-18 | HU-AJU-002, HU-AUD-004, HU-PAR-003 | RF-AJU-005, RF-AUD-007, RF-PAR-006 |
| **RN-AJU-002** | Conf. | PN-07 | CU-12 | HU-AJU-003, HU-PAR-001, HU-TAR-002 | RF-AJU-004, RF-PAR-001 |
| **RN-AJU-003** | Estr. | PN-07, PN-08, PN-13 | CU-12, CU-13, CU-18 | HU-AJU-001, HU-NOV-004, HU-PAR-002, HU-PAR-003 | RF-AJU-001, RF-AJU-002, RF-AJU-003, RF-PAR-005, RF-PAR-006 |
| **RN-AJU-004** | Conf. | PN-07, PN-11 | CU-12, CU-16 | HU-AJU-005, HU-ALE-001, HU-ALE-002 | RF-AJU-009, RF-ALE-004 |
| **RN-AJU-005** | Conf. | PN-07, PN-11 | CU-12, CU-16 | HU-ALE-001, HU-ALE-002, HU-TAR-002 | RF-ALE-004 |
| **RN-AJU-006** | Estr. | PN-07 | CU-12 | HU-AJU-002, HU-TAR-002 | RF-AJU-008 |
| **RN-AJU-007** | Estr. | — | — | HU-KDX-002 | RF-KDX-004 |
| **RN-CNT-001** | Estr. | PN-08, PN-09 | CU-13, CU-14 | HU-CNT-001, HU-CNT-003, HU-CNT-004, HU-CNT-005, HU-CNT-010 | RF-CNT-003, RF-CNT-004, RF-CNT-007 |
| **RN-CNT-002** | Estr. | PN-08 | CU-13 | HU-CNT-002, HU-PAR-003, HU-CNT-010 | RF-CNT-006, RF-PAR-006, RF-CNT-014 |
| **RN-CNT-003** | Estr. | PN-08, PN-09 | CU-13, CU-14 | HU-CNT-004, HU-CNT-005, HU-CNT-009, HU-PAR-001, HU-PAR-003, HU-TAR-003 | RF-CNT-008, RF-CNT-009, RF-CNT-010, RF-PAR-001, RF-PAR-006, RF-TAR-004 |
| **RN-CNT-004** | Estr. | PN-08 | CU-13 | HU-CNT-005 | RF-CNT-010 |
| **RN-CNT-005** | Conf. | PN-08, PN-11 | CU-13, CU-16 | HU-ALE-001, HU-ALE-002 | RF-ALE-004 |
| **RN-CNT-006** | Estr. | PN-09 | CU-14 | HU-CNT-006 | RF-CNT-011 |
| **RN-CNT-007** | Estr. | PN-09 | CU-14 | HU-CNT-007 | RF-CNT-012 |
| **RN-CNT-008** | Conf. | PN-09 | CU-14 | HU-CNT-011 | RF-CNT-015 |
| **RN-CNT-009** | Estr. | — | — | HU-CNT-010 | RF-CNT-014 |
| **RN-NOV-001** | Estr. | PN-08, PN-09, PN-12 | CU-13, CU-14, CU-17 | HU-NOV-004 | RF-NOV-007 |
| **RN-NOV-002** | Conf. | PN-12 | CU-17 | HU-NOV-003 | RF-NOV-008 |
| **RN-NOV-003** | Conf. | PN-12 | CU-17 | HU-NOV-002 | RF-NOV-005 |
| **RN-ALE-001** | Conf. | PN-11 | CU-16 | HU-ALE-005 | RF-ALE-006 |
| **RN-ALE-002** | Conf. | PN-11 | CU-16 | HU-NOV-003, HU-ALE-004 | RF-ALE-007 |
| **RN-ALE-003** | Conf. | PN-11 | CU-16 | HU-NOV-003, HU-ALE-001, HU-ALE-004 | RF-ALE-007 |
| **RN-ALE-004** | Estr. | PN-11 | CU-16 | HU-ALE-003 | RF-ALE-005 |
| **RN-ALE-005** | Estr. | — | — | HU-BOD-004, HU-ALE-001 | RF-BOD-007, RF-ALE-003 |
| **RN-AUD-001** | Estr. | PN-13 | CU-18 | HU-ACC-001, HU-USR-003, HU-REP-002, HU-REP-003, HU-AUD-001, HU-AUD-004, HU-PAR-001, HU-PAR-003 | RF-ACC-003, RF-USR-008, RF-REP-006, RF-AUD-001, RF-AUD-002, RF-AUD-003, RF-AUD-007, RF-PAR-003, RF-PAR-006 |
| **RN-AUD-002** | Estr. | PN-13 | CU-18 | HU-AUD-003 | RF-AUD-006 |
| **RN-AUD-003** | Estr. | — | — | HU-REP-002, HU-REP-003 | RF-REP-006 |
| **RN-AUD-004** | Estr. | — | — | HU-PAR-001 | RF-PAR-003, RF-PAR-004 |
| **RN-AUD-005** | Estr. | — | — | HU-KDX-003 | RF-KDX-006 |

## 9.6 Cobertura por KPI (24)

| KPI | Objetivo de la monografía | Concepto | Historia(s) | RF | Regla(s) relacionada(s) |
|---|---|---|---|---|---|
| **KPI-01** Exactitud del Inventario | OG / OE-3 (§8.2) | CD-43, CD-27 | HU-CNT-004, HU-CNT-005, HU-CNT-008, HU-DSH-001, HU-CNT-010 | RF-CNT-007, RF-CNT-013, RF-DSH-001, RF-CNT-014, RF-REP-003 | RN-CNT-001, RN-CNT-002, RN-CNT-009 |
| **KPI-02** Exactitud Global del Inventario | OE-3 (§8.2) | CD-43 | HU-CNT-006, HU-CNT-008, HU-CNT-011 | RF-CNT-011, RF-CNT-013, RF-CNT-015, RF-REP-008 | RN-CNT-006, RN-CNT-008 |
| **KPI-03** Cobertura de conteo | OE-3 (nuevo aporte) | CD-38 | HU-CNT-001, HU-CNT-007 | RF-CNT-001, RF-CNT-012, RF-REP-008 | RN-CNT-007 |
| **KPI-04** Diferencia neta de conteo | OE-3 (nuevo aporte) | CD-27 | HU-CNT-004, HU-CNT-005 | RF-CNT-007, RF-REP-008 | RN-CNT-001 |
| **KPI-05** Tiempo Medio de Registro de un Movimiento | OG / OE-3 (§8.2) | CD-28 | HU-ENT-003, HU-SAL-001, HU-SAL-003, HU-MOV-001, HU-KDX-001 | RF-ENT-011, RF-SAL-009, RF-MOV-001, RF-KDX-001, RF-KDX-009, RF-REP-003 | RN-EXI-004, RN-EXI-007, RN-INT-001, RN-INT-002, RN-INT-004, RN-MOV-002, RN-MOV-004, RN-MOV-010 |
| **KPI-06** Tasa de segundo conteo | OE-3 (nuevo aporte) | CD-42 | HU-CNT-004 | RF-CNT-008, RF-REP-008 | RN-CNT-003 |
| **KPI-07** Movimientos sin identificador escaneado | OE-3 (nuevo aporte) | CD-08 | HU-QRC-002 | RF-QRC-003, RF-QRC-009, RF-REP-008 | RN-IDE-001 |
| **KPI-08** Frecuencia de Errores de Registro | OG / OE-3 (§8.2) | CD-33, CD-34, CD-27 | HU-AJU-001, HU-CNT-004, HU-CNT-005, HU-KDX-002 | RF-AJU-001, RF-CNT-007, RF-KDX-004, RF-REP-003 | RN-AJU-003, RN-AJU-007, RN-CNT-001, RN-EXI-001, RN-INT-002 |
| **KPI-09** Integridad del kardex | OE-3 (nuevo aporte) | CD-37, CD-18 | HU-INV-001, HU-KDX-003, HU-AUD-004 | RF-INV-003, RF-KDX-006, RF-AUD-007, RF-REP-003 | RN-AJU-001, RN-AUD-001, RN-AUD-005, RN-INT-004 |
| **KPI-10** Desviaciones de ubicación | OE-3 (nuevo aporte) | CD-14 | HU-BOD-005, HU-ENT-006 | RF-BOD-008, RF-BOD-009, RF-REP-008 | RN-MOV-001, RN-MOV-003 |
| **KPI-11** Volumen de movimientos | OE-3 (nuevo aporte) | CD-28 | HU-ENT-003, HU-SAL-001, HU-SAL-003, HU-MOV-001 | RF-ENT-011, RF-SAL-009, RF-MOV-001, RF-REP-003 | RN-EXI-004, RN-EXI-007, RN-INT-002, RN-INT-004, RN-MOV-002, RN-MOV-004, RN-MOV-010 |
| **KPI-12** Tiempo medio de recepción | OE-3 (nuevo aporte) | CD-35 | HU-ENT-001, HU-ENT-002, HU-ENT-003 | RF-ENT-001, RF-ENT-011, RF-ENT-017, RF-REP-008 | RN-EXI-007, RN-INT-002, RN-INT-004 |
| **KPI-13** Tasa de merma | OE-3 (§7.2) | CD-30 | HU-SAL-005 | RF-SAL-010, RF-REP-003 | RN-SAL-006 |
| **KPI-14** Volumen y magnitud de ajustes | OE-3 (§8.2) | CD-33 | HU-AJU-001, HU-AJU-006 | RF-AJU-001, RF-AJU-010, RF-REP-003 | RN-AJU-003, RN-EXI-001 |
| **KPI-15** Tiempo medio en tránsito | OE-3 (nuevo aporte) | CD-23, CD-32 | HU-MOV-004, HU-MOV-005 | RF-MOV-008, RF-MOV-010, RF-REP-008 | RN-EXI-005, RN-MOV-007 |
| **KPI-16** Rotación por referencia | OE-3 (§3) | CD-30, CD-18 | HU-SAL-001, HU-SAL-003, HU-ALE-002 | RF-SAL-009, RF-REP-003 | RN-EXI-004, RN-INT-004 |
| **KPI-17** Existencia sin movimiento | OE-3 (§3) | CD-28 | HU-KDX-001, HU-PAR-001 | RF-KDX-001, RF-PAR-001, RF-REP-003 | RN-AJU-002, RN-CNT-003, RN-INT-001, RN-INT-002, RN-MOV-008, RN-SAL-001 |
| **KPI-18** Ocupación de bodega | OE-3 (nuevo aporte) | CD-14, CD-15 | HU-BOD-002, HU-ENT-006, HU-INV-003 | RF-BOD-005, RF-INV-004, RF-REP-008 | RN-INT-005, RN-MOV-002 |
| **KPI-19** Alertas generadas y atendidas | OE-3 (§3) | CD-45 | HU-ALE-001, HU-ALE-002, HU-ALE-003 | RF-ALE-001, RF-ALE-004, RF-ALE-005, RF-REP-003 | RN-AJU-004, RN-AJU-005, RN-ALE-004, RN-CNT-005, RN-MOV-002, RN-MOV-008 |
| **KPI-20** Tiempo medio de atención de alerta | OE-3 (nuevo aporte) | CD-45 | HU-ALE-003, HU-ALE-004 | RF-ALE-005, RF-ALE-007, RF-REP-008 | RN-ALE-002, RN-ALE-003, RN-ALE-004 |
| **KPI-21** Eventos de ruptura de stock | OE-3 (§3) | CD-18 | HU-ALE-001, HU-ALE-002 | RF-ALE-004, RF-REP-003 | RN-AJU-004, RN-AJU-005, RN-CNT-005, RN-MOV-002, RN-MOV-008 |
| **KPI-22** Tiempo medio de aprobación | OE-3 (nuevo aporte) | CD-33 | HU-SAL-007, HU-AJU-002, HU-AJU-003, HU-TAR-002 | RF-SAL-006, RF-AJU-004, RF-AJU-008, RF-REP-008 | RN-AJU-002, RN-AJU-006, RN-SAL-001 |
| **KPI-23** Novedades reportadas y resueltas | OE-3 (nuevo aporte) | CD-48 | HU-NOV-001, HU-NOV-002, HU-NOV-003 | RF-NOV-001, RF-NOV-004, RF-NOV-006, RF-REP-008 | RN-MAE-007 |
| **KPI-24** Adopción del sistema | OE-3 (§4) | CD-28 | HU-KDX-001, HU-PAR-001 | RF-KDX-001, RF-PAR-007, RF-REP-003 | RN-INT-001, RN-INT-002 |

## 9.7 Cobertura por proceso de negocio (14)

| Proceso | Caso de uso | Módulo(s) | Historias | RF | Reglas citadas en el proceso |
|---|---|---|---|---|---|
| **PN-01** Recepción de mercancía | CU-06 | M-04, M-07 | HU-ENT-001, HU-ENT-002, HU-ENT-003, HU-ENT-004, HU-ENT-005, HU-ENT-007, HU-ENT-008, HU-LOT-001 | RF-LOT-001, RF-LOT-002, RF-LOT-003, RF-ENT-001, RF-ENT-002, RF-ENT-003, RF-ENT-004, RF-ENT-005, RF-ENT-006, RF-ENT-007, RF-ENT-008, RF-ENT-009, RF-ENT-010, RF-ENT-011, RF-ENT-012, RF-ENT-013, RF-ENT-017 | RN-ENT-002, RN-ENT-003, RN-ENT-004, RN-ENT-005, RN-ENT-006, RN-EXI-007, RN-INT-003, RN-INT-008, RN-MAE-001 |
| **PN-02** Registro inicial e identificación | CU-07 | M-06 | HU-QRC-001, HU-QRC-002, HU-QRC-003, HU-QRC-004, HU-QRC-005 | RF-QRC-001, RF-QRC-002, RF-QRC-003, RF-QRC-004, RF-QRC-005, RF-QRC-006, RF-QRC-007, RF-QRC-008, RF-QRC-009 | RN-IDE-001, RN-IDE-002, RN-IDE-003, RN-IDE-004 |
| **PN-03** Ubicación física de mercancía | CU-08 | M-05, M-07 | HU-ENT-006, HU-BOD-005, HU-BOD-002 | RF-BOD-004, RF-BOD-005, RF-BOD-008, RF-MOV-005, RF-BOD-009 | RN-MOV-002, RN-MOV-003, RN-MOV-004, RN-MOV-010 |
| **PN-04** Consulta de existencia y ubicación | CU-09 | M-13 | HU-INV-001, HU-INV-002, HU-INV-003, HU-INV-004, HU-INV-005, HU-INV-006 | RF-INV-001, RF-INV-002, RF-INV-003, RF-INV-004, RF-INV-005, RF-INV-006, RF-INV-007, RF-INV-008 | — |
| **PN-05** Movimiento interno (reubicación) | CU-10 | M-09 | HU-MOV-001, HU-MOV-002 | RF-MOV-001, RF-MOV-002, RF-MOV-003, RF-MOV-004, RF-MOV-005, RF-MOV-006 | RN-EXI-003, RN-EXI-006, RN-IDE-001, RN-INT-003, RN-INT-008, RN-MOV-002, RN-MOV-004, RN-MOV-005, RN-MOV-006 |
| **PN-06** Transferencia entre zonas o bodegas | CU-11 | M-09 | HU-MOV-003, HU-MOV-004, HU-MOV-005, HU-MOV-006, HU-MOV-007 | RF-MOV-007, RF-MOV-008, RF-MOV-009, RF-MOV-010, RF-MOV-011 | RN-EXI-003, RN-EXI-004, RN-EXI-005, RN-MOV-007, RN-MOV-008, RN-MOV-009 |
| **PN-07** Ajuste de inventario | CU-12 | M-10, M-20 | HU-AJU-001, HU-AJU-002, HU-AJU-003, HU-AJU-004, HU-AJU-005, HU-AJU-006, HU-TAR-002 | RF-AJU-001, RF-AJU-002, RF-AJU-003, RF-AJU-004, RF-AJU-005, RF-AJU-006, RF-AJU-007, RF-AJU-008, RF-AJU-009, RF-AJU-010 | RN-AJU-001, RN-AJU-002, RN-AJU-003, RN-AJU-004, RN-AJU-005, RN-AJU-006, RN-EXI-001, RN-EXI-006 |
| **PN-08** Conteo cíclico | CU-13 | M-11 | HU-CNT-001, HU-CNT-002, HU-CNT-003, HU-CNT-004, HU-CNT-005, HU-CNT-008, HU-CNT-009 | RF-CNT-001, RF-CNT-002, RF-CNT-003, RF-CNT-004, RF-CNT-005, RF-CNT-006, RF-CNT-007, RF-CNT-008, RF-CNT-009, RF-CNT-010, RF-CNT-013, RF-REP-003, RF-TAR-004, RF-REP-008 | RN-AJU-003, RN-CNT-001, RN-CNT-002, RN-CNT-003, RN-CNT-004, RN-CNT-005, RN-NOV-001 |
| **PN-09** Conteo general | CU-14 | M-11 | HU-CNT-006, HU-CNT-007 | RF-CNT-011, RF-CNT-012 | RN-CNT-001, RN-CNT-003, RN-CNT-006, RN-CNT-007, RN-CNT-008, RN-NOV-001 |
| **PN-10** Salida de mercancía | CU-15 | M-08 | HU-SAL-001, HU-SAL-002, HU-SAL-003, HU-SAL-004, HU-SAL-005, HU-SAL-006, HU-SAL-007 | RF-SAL-001, RF-SAL-002, RF-SAL-003, RF-SAL-004, RF-SAL-005, RF-SAL-006, RF-SAL-007, RF-SAL-008, RF-SAL-009, RF-SAL-010, RF-SAL-011, RF-SAL-014 | RN-EXI-003, RN-EXI-004, RN-EXI-006, RN-SAL-001, RN-SAL-002, RN-SAL-003, RN-SAL-004, RN-SAL-005, RN-SAL-006, RN-SAL-007 |
| **PN-11** Gestión de alerta operativa | CU-16 | M-15 | HU-ALE-001, HU-ALE-002, HU-ALE-003, HU-ALE-004, HU-ALE-005 | RF-ALE-001, RF-ALE-002, RF-ALE-003, RF-ALE-004, RF-ALE-005, RF-ALE-006, RF-ALE-007 | RN-AJU-004, RN-AJU-005, RN-ALE-001, RN-ALE-002, RN-ALE-003, RN-ALE-004, RN-CNT-005, RN-MOV-002, RN-MOV-008 |
| **PN-12** Reporte de novedad de mercancía | CU-17 | M-12 | HU-NOV-001, HU-NOV-002, HU-NOV-003, HU-NOV-004 | RF-BOD-004, RF-QRC-001, RF-AJU-001, RF-AJU-002, RF-NOV-001, RF-NOV-002, RF-NOV-003, RF-NOV-004, RF-NOV-005, RF-NOV-006, RF-ALE-007, RF-NOV-007, RF-NOV-008 | RN-MAE-007, RN-NOV-001, RN-NOV-002, RN-NOV-003 |
| **PN-13** Auditoría de inventario | CU-18 | M-14, M-18 | HU-AUD-001, HU-AUD-002, HU-AUD-003, HU-AUD-004, HU-KDX-001, HU-KDX-002, HU-KDX-003 | RF-ACC-003, RF-KDX-001, RF-KDX-002, RF-KDX-003, RF-KDX-004, RF-KDX-005, RF-KDX-006, RF-AUD-001, RF-AUD-002, RF-AUD-003, RF-AUD-004, RF-AUD-005, RF-AUD-006, RF-AUD-007, RF-KDX-009 | RN-AJU-001, RN-AJU-003, RN-AUD-001, RN-AUD-002, RN-INT-002, RN-INT-004 |
| **PN-14** Cierre operativo de jornada | CU-19 | M-20 | HU-TAR-004, HU-TAR-005 | RF-TAR-006, RF-TAR-007, RF-TAR-008 | RN-INT-003, RN-MOV-006 |

## 9.8 Brechas de trazabilidad detectadas

| Brecha | Elementos | Hallazgo |
|---|---|---|
| Proceso sin HU ni RF | ninguno (PN-14 se cerró en la v1.3 con HU-TAR-004, HU-TAR-005 y RF-TAR-006…RF-TAR-008, DEC-05) | H-10 (resuelto) |
| Reglas sin RF | ninguna (cerradas en la v1.3, DEC-06) | H-11 |
| Reglas sin HU | ninguna (cerradas en la v1.3, DEC-06) | H-11 |
| KPI cuyo dato de origen no se exige capturar | ninguno (KPI-05, KPI-07, KPI-10, KPI-12, KPI-17 y KPI-24 se cerraron en la v1.3, DEC-06; KPI-24 requiere además verificación de campo) | H-12 (resuelto) |
| HU con cobertura RF parcial | ninguna (HU-NOV-003 y HU-NOV-004 se cerraron con RF-NOV-008 y RF-NOV-007, DEC-06) | H-13 (resuelto) |
| RF sin historia · HU sin RF | ninguno · ninguna | — |
| Objetivos de la monografía sin requisito | ninguno (todos los módulos derivan de OG/OE-1/OE-2/OE-3); OE-2 se materializa solo en M-12, M-19, M-20 y en los RNF de usabilidad | — |

> **Lectura.** La cadena está completa para 185 de 185 RF y 114 de 114 HU. Las brechas que tenía la v1.2 (reglas sin RF, KPI sin dato de origen y PN-14 sin requisitos) se cerraron en la v1.3 por las decisiones DEC-05 y DEC-06 (Anexo C).

---

**ESTADO DEL CAPÍTULO 9**

| | |
|---|---|
| **Completado** | Objetivos transcritos · objetivos→módulos · catálogo de 24 KPI · matriz de 185 RF · cobertura de 92 reglas · de 24 KPI · de 14 procesos · brechas |
| **Pendiente** | Validación por el Director de los eslabones `[SRS]` (R-S02) · brechas cerradas en la v1.3 (DEC-05, DEC-06) |
| **Riesgos encontrados** | H-10, H-11, H-12, H-13 (resueltos en la v1.3) · RG-42 (pérdida de trazabilidad hacia la monografía) |
| **Dependencias** | Caps. 5–8 |


---

# CAPÍTULO 10 — MATRIZ CRUD

> Relaciona los **actores** (Cap. 3) con los **módulos funcionales** (M-01…M-20). Derivada de la matriz de segregación del SPEC (§2.7), de las fichas de rol y de las funciones de cada módulo `[SRS]`. No describe estructura de datos: el «objeto» de cada operación es el elemento funcional propio del módulo.

**Leyenda.**

| Letra | Significado |
|---|---|
| **C** | Crear / registrar / generar |
| **R** | Leer / consultar |
| **U** | Actualizar / modificar / cambiar de estado |
| **D** | Desactivar, anular con movimiento inverso o cerrar — **eliminación lógica**. **No existe borrado físico para ningún rol, incluido el Administrador** (RN-MAE-007) |
| **A** | Aprobar / autorizar / confirmar (extensión del CRUD: la segregación de funciones exige distinguirla) |
| **⚠️** | Permitido con restricción (ver nota) |
| **—** | Sin acceso |

| Módulo | Admin | Jefe | Coord. | Aux. | Auditor | Sistema | Notas |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **M-01** Acceso y Autenticación | C R U D | C U D | C U D | C U D | C U D | C U D | Los roles operan sobre su propia sesión y contraseña; el Administrador además restablece accesos ajenos (R vía bitácora). El Sistema bloquea cuentas y cierra sesiones por inactividad |
| **M-02** Usuarios y Roles | C R U D | — | — | — | R | — | Solo Administrador. «D» = desactivar (RN-MAE-004: nunca al último Administrador) |
| **M-03** Catálogo de Referencias | C R U D | C R U D | R | R | R | C | Sistema genera los SKU. «D» = desactivar (solo con existencia cero, RN-MAE-003) |
| **M-04** Gestión de Lotes | C R U | C R U | C R | R | R | C | Sistema crea o asocia el lote al confirmar la entrada. «U» = inmovilizar / liberar (solo Jefe o Administrador, RN-LOT-004) |
| **M-05** Estructura de Bodega | C R U D | R | R | R | R | C | Solo Administrador define la estructura. Sistema genera los QR de ubicación. «D» = desactivar (RN-MAE-005) |
| **M-06** Identificación QR | C R U D | C R U D | C R U D | R U ⚠️ | R | C | ⚠️ Aux.: solo reimprime por deterioro, con motivo (RN-IDE-004). El Auxiliar escanea (R) |
| **M-07** Entradas y Recepción | C R U A D | C R U A D | C R U A D | R U | R | C | Aux. registra la recepción física (U) pero **no confirma** (RN-ENT-007). «D» = reversar una entrada no confirmada. Sistema genera el movimiento de entrada |
| **M-08** Salidas | C R U A D | C R U A D | C R U A ⚠️ D | R U | R | C U D | ⚠️ Coord.: autoriza solo hasta su umbral (RN-SAL-001). Aux. prepara y confirma lo autorizado. Sistema reserva, descuenta y libera reservas vencidas |
| **M-09** Movimientos y Transferencias | C R U A D | C R U A D | C R U D | C R U | R | C U | Aux.: crea movimientos internos y ejecuta transferencias asignadas, pero **no crea transferencias**. «D» = cancelar (en tránsito solo Jefe, RN-MOV-009) |
| **M-10** Ajustes de Inventario | C R A | C R A | C R | — | R | C U | Nadie aprueba su propio ajuste (RN-AJU-001). Admin aprueba mayores; Jefe menores. Sistema aplica el movimiento al aprobarse y escala |
| **M-11** Conteos | C R U A D | C R U A D | C R U | C R ⚠️ | R | C U D | Cierra solo el Jefe/Admin (RN-CNT-004) y nunca quien ejecutó (RN-CNT-003). ⚠️ Aux.: registra el conteo de sus tareas, sin ver la cantidad esperada (RN-CNT-002). Coord.: solo conteos cíclicos |
| **M-12** Novedades de Mercancía | C R U D | C R U D | C R U D | C R ⚠️ | R | C U | «D» = cerrar (nunca eliminar, RN-MAE-007). ⚠️ Aux.: reporta y consulta las propias |
| **M-13** Consulta de Existencia | R | R | R | R ⚠️ | R | — | Solo lectura (RN-INT-006). ⚠️ Aux.: sin costo ni valorización |
| **M-14** Kardex y Trazabilidad | R C ⚠️ | R C ⚠️ | R | R ⚠️ | R | C | El kardex **nunca** admite U ni D (RN-INT-002). ⚠️ «C» = movimiento inverso de anulación con motivo y autorización. ⚠️ Aux.: solo lo que él movió, últimos 30 días |
| **M-15** Alertas y Reglas | R U D | R U D | R U D | — | R | C U D | «U/D» = atender, descartar con motivo (RN-ALE-004). Sistema genera, agrupa, cierra y escala |
| **M-16** Reportes y Exportación | C R U | C R U D | C R ⚠️ | — | C R | C | ⚠️ Coord.: solo reportes operativos. «U» Admin = habilitar exportación analítica; «U/D» Jefe = programar / desactivar reportes periódicos |
| **M-17** Dashboard Operativo | R | R | R ⚠️ | — | R | — | ⚠️ Coord.: solo su zona y sin valorización. El Auxiliar no ve el dashboard: ve su panel de tareas (M-20) |
| **M-18** Auditoría y Bitácora | R | R ⚠️ | — | — | C R | C | ⚠️ Jefe: solo eventos de su bodega, sin configuración. Auditor «C» = observaciones en registro separado (RN-AUD-002). La bitácora nunca admite U ni D (RN-AUD-001) |
| **M-19** Parámetros y Configuración | C R U D | — | R ⚠️ | — | R | — | Solo Administrador configura. ⚠️ Coord.: consulta su propio umbral de autorización (HU-SAL-007) |
| **M-20** Notificaciones y Tareas | R U | R U | R U | R | — | C U D | «U» = reasignar tareas (Coord. y superiores). La tarea la cierra el movimiento asociado, no el usuario (RF-TAR-003). El Auditor no tiene panel de tareas |

**Notas de la matriz `[SRS]`:**

1. **Sin «D» física.** Toda «D» de la tabla es desactivación, anulación con movimiento inverso o cierre; se auditará con RN-MAE-007, RN-MAE-008 y RN-MAE-009.
2. **Kardex y bitácora** son de solo *C* y *R*: la ausencia de *U* y *D* es la materialización de RN-INT-002 y RN-AUD-001 y se verifica en RNF-AUD-002.
3. **Auditor.** Su única *C* es la de observaciones de auditoría (registro separado) y la generación de reportes; sobre el inventario solo *R* (RF-AUD-005).
4. **Vacíos del SPEC que la matriz no resuelve** (no se inventan permisos): (a) el SPEC no define si el **Jefe** puede *leer* los parámetros de configuración; (b) RN-AUD-002 indica que las observaciones «se cierran con respuesta» pero no dice **quién** responde; (c) la «valorización» aparece como permiso sin dato de origen (H-07). Se elevan al Director en el Anexo C (DEC-04, DEC-07) y en la nota final de este capítulo.

---

**ESTADO DEL CAPÍTULO 10**

| | |
|---|---|
| **Completado** | Matriz CRUD 20 módulos × 5 roles + Sistema con restricciones y notas |
| **Pendiente** | Definir lectura de parámetros por el Jefe y actor que cierra observaciones de auditoría (SPEC no lo dice) |
| **Riesgos encontrados** | Permiso «valorización» sin objeto (H-07); ambigüedad estructural/configurable (H-06) |
| **Dependencias** | Cap. 3 (matriz §2.7) · Cap. 8 (reglas) · Cap. 7 (RNF-SEG-003, RNF-SEG-004) |


---

# CAPÍTULO 11 — DEPENDENCIAS FUNCIONALES

> Qué módulos **necesitan** de otros para tener sentido funcional. Transcribe y consolida las «dependencias funcionales» declaradas en el SPEC (§5) `[SRS]`. Una dependencia funcional **no es** una dependencia técnica ni de arquitectura: significa «este módulo no puede cumplir su propósito sin la capacidad del otro».

## 11.1 Tabla de dependencias por módulo

| Módulo | Depende funcionalmente de | Nota |
|---|---|---|
| **M-01** Acceso y Autenticación | M-02 Usuarios y Roles, M-18 Auditoría y Bitácora, M-19 Parámetros y Configuración |  |
| **M-02** Usuarios y Roles | M-01 Acceso y Autenticación, M-05 Estructura de Bodega, M-18 Auditoría y Bitácora |  |
| **M-03** Catálogo de Referencias | M-19 Parámetros y Configuración, M-13 Consulta de Existencia |  |
| **M-04** Gestión de Lotes | M-03 Catálogo de Referencias, M-07 Entradas y Recepción, M-14 Kardex y Trazabilidad, M-13 Consulta de Existencia |  |
| **M-05** Estructura de Bodega | M-06 Identificación QR, M-13 Consulta de Existencia, M-19 Parámetros y Configuración |  |
| **M-06** Identificación QR | M-05 Estructura de Bodega, M-07 Entradas y Recepción, M-14 Kardex y Trazabilidad |  |
| **M-07** Entradas y Recepción | M-03 Catálogo de Referencias, M-04 Gestión de Lotes, M-05 Estructura de Bodega, M-06 Identificación QR, M-13 Consulta de Existencia, M-14 Kardex y Trazabilidad, M-12 Novedades de Mercancía |  |
| **M-08** Salidas | M-13 Consulta de Existencia, M-14 Kardex y Trazabilidad, M-05 Estructura de Bodega, M-06 Identificación QR, M-19 Parámetros y Configuración, M-20 Notificaciones y Tareas |  |
| **M-09** Movimientos y Transferencias | M-05 Estructura de Bodega, M-06 Identificación QR, M-13 Consulta de Existencia, M-14 Kardex y Trazabilidad, M-15 Alertas y Reglas, M-19 Parámetros y Configuración |  |
| **M-10** Ajustes de Inventario | M-13 Consulta de Existencia, M-14 Kardex y Trazabilidad, M-19 Parámetros y Configuración, M-20 Notificaciones y Tareas, M-18 Auditoría y Bitácora, M-15 Alertas y Reglas |  |
| **M-11** Conteos | M-13 Consulta de Existencia, M-10 Ajustes de Inventario, M-14 Kardex y Trazabilidad, M-05 Estructura de Bodega, M-06 Identificación QR, M-19 Parámetros y Configuración, M-20 Notificaciones y Tareas |  |
| **M-12** Novedades de Mercancía | M-10 Ajustes de Inventario, M-14 Kardex y Trazabilidad, M-06 Identificación QR, M-20 Notificaciones y Tareas, M-13 Consulta de Existencia |  |
| **M-13** Consulta de Existencia | M-14 Kardex y Trazabilidad, M-03 Catálogo de Referencias, M-05 Estructura de Bodega, M-04 Gestión de Lotes, M-02 Usuarios y Roles |  |
| **M-14** Kardex y Trazabilidad | M-01 Acceso y Autenticación | Recibe escritura de todos los módulos operativos (M-07 a M-12); M-13 y M-16 leen de él. Su propia dependencia es la identidad del usuario (M-01, RF-KDX-002) |
| **M-15** Alertas y Reglas | M-13 Consulta de Existencia, M-09 Movimientos y Transferencias, M-10 Ajustes de Inventario, M-11 Conteos, M-19 Parámetros y Configuración, M-20 Notificaciones y Tareas, M-04 Gestión de Lotes |  |
| **M-16** Reportes y Exportación Analítica | M-14 Kardex y Trazabilidad, M-13 Consulta de Existencia, M-10 Ajustes de Inventario, M-11 Conteos, M-15 Alertas y Reglas, M-12 Novedades de Mercancía, M-02 Usuarios y Roles |  |
| **M-17** Dashboard Operativo | M-13 Consulta de Existencia, M-15 Alertas y Reglas, M-16 Reportes y Exportación Analítica, M-20 Notificaciones y Tareas, M-11 Conteos, M-10 Ajustes de Inventario |  |
| **M-18** Auditoría y Bitácora | M-14 Kardex y Trazabilidad, M-02 Usuarios y Roles | Todos los módulos escriben en él; lee del kardex para la verificación de integridad |
| **M-19** Parámetros y Configuración | M-02 Usuarios y Roles, M-18 Auditoría y Bitácora, M-03 Catálogo de Referencias, M-05 Estructura de Bodega, M-15 Alertas y Reglas |  |
| **M-20** Notificaciones y Tareas | M-07 Entradas y Recepción, M-08 Salidas, M-09 Movimientos y Transferencias, M-10 Ajustes de Inventario, M-11 Conteos, M-12 Novedades de Mercancía, M-15 Alertas y Reglas, M-02 Usuarios y Roles |  |

## 11.2 Matriz de dependencia (fila depende de columna)

`●` = la fila depende funcionalmente de la columna.

| Depende de → | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **M-01** | · | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  |
| **M-02** | ● | · |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| **M-03** |  |  | · |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  | ● |  |
| **M-04** |  |  | ● | · |  |  | ● |  |  |  |  |  | ● | ● |  |  |  |  |  |  |
| **M-05** |  |  |  |  | · | ● |  |  |  |  |  |  | ● |  |  |  |  |  | ● |  |
| **M-06** |  |  |  |  | ● | · | ● |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| **M-07** |  |  | ● | ● | ● | ● | · |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |
| **M-08** |  |  |  |  | ● | ● |  | · |  |  |  |  | ● | ● |  |  |  |  | ● | ● |
| **M-09** |  |  |  |  | ● | ● |  |  | · |  |  |  | ● | ● | ● |  |  |  | ● |  |
| **M-10** |  |  |  |  |  |  |  |  |  | · |  |  | ● | ● | ● |  |  | ● | ● | ● |
| **M-11** |  |  |  |  | ● | ● |  |  |  | ● | · |  | ● | ● |  |  |  |  | ● | ● |
| **M-12** |  |  |  |  |  | ● |  |  |  | ● |  | · | ● | ● |  |  |  |  |  | ● |
| **M-13** |  | ● | ● | ● | ● |  |  |  |  |  |  |  | · | ● |  |  |  |  |  |  |
| **M-14** | ● |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| **M-15** |  |  |  | ● |  |  |  |  | ● | ● | ● |  | ● |  | · |  |  |  | ● | ● |
| **M-16** |  | ● |  |  |  |  |  |  |  | ● | ● | ● | ● | ● | ● | · |  |  |  |  |
| **M-17** |  |  |  |  |  |  |  |  |  | ● | ● |  | ● |  | ● | ● | · |  |  | ● |
| **M-18** |  | ● |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  | · |  |  |
| **M-19** |  | ● | ● |  | ● |  |  |  |  |  |  |  |  |  | ● |  |  | ● | · |  |
| **M-20** |  | ● |  |  |  |  | ● | ● | ● | ● | ● | ● |  |  | ● |  |  |  |  | · |

## 11.3 Lectura de la matriz

**Módulos «raíz» (los demás dependen de ellos):**

| Módulo | Por qué es raíz | Cantidad de módulos que dependen de él |
|---|---|---|
| **M-13** Consulta de Existencia | Todo módulo que valida disponibilidad consulta la existencia | 12 (M-03, M-04, M-05, M-07, M-08, M-09, M-10, M-11, M-12, M-15, M-16, M-17) |
| **M-14** Kardex y Trazabilidad | Fuente de verdad de la existencia; todo movimiento se registra en él | 11 (M-04, M-06, M-07, M-08, M-09, M-10, M-11, M-12, M-13, M-16, M-18) |
| **M-05** Estructura de Bodega | Estructura física: dónde puede estar la existencia | 8 (M-02, M-06, M-07, M-08, M-09, M-11, M-13, M-19) |
| **M-19** Parámetros y Configuración | Umbrales, plazos y motivos que gobiernan las reglas configurables | 8 (M-01, M-03, M-05, M-08, M-09, M-10, M-11, M-15) |
| **M-02** Usuarios y Roles | Existencia y ámbito de los usuarios | 6 (M-01, M-13, M-16, M-18, M-19, M-20) |
| **M-06** Identificación QR | Identificación y escaneo de mercancía y ubicaciones | 6 (M-05, M-07, M-08, M-09, M-11, M-12) |
| **M-10** Ajustes de Inventario | Ajustes: destino de las diferencias de conteo y novedades | 6 (M-11, M-12, M-15, M-16, M-17, M-20) |
| **M-15** Alertas y Reglas | Alertas que disparan las reglas de otros módulos | 6 (M-09, M-10, M-16, M-17, M-19, M-20) |

**Ciclos funcionales detectados.** Existen dependencias mutuas que **no son un defecto** sino la consecuencia de que el kardex y la estructura de bodega se alimentan y se leen entre sí. Deben tenerse presentes al planificar la construcción por bloques `[SRS]`:

| Módulos en dependencia mutua | Motivo funcional |
|---|---|
| M-01 Acceso y Autenticación ↔ M-02 Usuarios y Roles | El acceso requiere que el usuario exista; el usuario nace de la gestión de acceso |
| M-02 Usuarios y Roles ↔ M-18 Auditoría y Bitácora | Los cambios de usuarios y roles se registran en la bitácora; la bitácora atribuye cada evento a un usuario |
| M-03 Catálogo de Referencias ↔ M-13 Consulta de Existencia | El catálogo valida la existencia antes de desactivar; la consulta de existencia lee el catálogo |
| M-03 Catálogo de Referencias ↔ M-19 Parámetros y Configuración | El catálogo usa unidades y umbrales configurables; los parámetros se definen sobre SKU y categorías del catálogo |
| M-04 Gestión de Lotes ↔ M-07 Entradas y Recepción | El lote se crea al confirmar la entrada; la entrada asocia o crea el lote |
| M-04 Gestión de Lotes ↔ M-13 Consulta de Existencia | La consulta muestra el lote; el lote consulta la existencia |
| M-05 Estructura de Bodega ↔ M-06 Identificación QR | Cada ubicación necesita su QR; el QR de ubicación necesita la ubicación |
| M-05 Estructura de Bodega ↔ M-13 Consulta de Existencia | La estructura valida existencia antes de desactivar una ubicación; la consulta lee la estructura |
| M-05 Estructura de Bodega ↔ M-19 Parámetros y Configuración | La estructura usa criterios de asignación configurables; los parámetros incluyen capacidades y reglas sobre la estructura |
| M-06 Identificación QR ↔ M-07 Entradas y Recepción | La entrada genera las unidades a identificar; la identificación se ejecuta sobre lo recibido |
| M-08 Salidas ↔ M-20 Notificaciones y Tareas | La salida genera tareas; la tarea se cierra al ejecutarse la salida |
| M-09 Movimientos y Transferencias ↔ M-15 Alertas y Reglas | El tránsito prolongado genera alerta; la alerta se origina en los movimientos |
| M-10 Ajustes de Inventario ↔ M-15 Alertas y Reglas | El ajuste recurrente genera alerta; la alerta se origina en los ajustes |
| M-10 Ajustes de Inventario ↔ M-20 Notificaciones y Tareas | El ajuste genera solicitudes; las solicitudes se notifican y escalan |
| M-11 Conteos ↔ M-20 Notificaciones y Tareas | El conteo genera tareas; la tarea se cierra al registrar el conteo |
| M-12 Novedades de Mercancía ↔ M-20 Notificaciones y Tareas | La novedad escala por plazo; la notificación reporta novedades |
| M-15 Alertas y Reglas ↔ M-19 Parámetros y Configuración | Las alertas usan umbrales; los umbrales se configuran para las alertas |
| M-15 Alertas y Reglas ↔ M-20 Notificaciones y Tareas | Las alertas se notifican; las notificaciones escalan alertas |

**Dependencias de todos hacia los módulos de control.** Por la regla de atribución (RN-INT-001) y de bitácora (RN-AUD-001), **todo módulo que altera el estado del sistema depende de M-01 (identidad) y de M-18 (bitácora)**; y todo módulo operativo (M-07…M-12) **escribe en M-14** (kardex). Esta relación transversal no se repite fila por fila.

## 11.4 Bloques de habilitación funcional (referencia del SPEC §12.2)

Orden en que el backlog del SPEC agrupa la habilitación de funcionalidad; se cita como **referencia**, no como plan de construcción (que corresponde a la Fase 5 del roadmap):

| Bloque | Contenido | Módulos | Depende de |
|---|---|---|---|
| **1 · Fundación** | Acceso, usuarios y roles, catálogo, estructura de bodega, parámetros y motivos, identificación QR | M-01, M-02, M-03, M-05, M-19, M-06 | — |
| **2 · Núcleo transaccional** | Kardex, existencia derivada, entradas, ubicación, salidas, movimientos internos, no-negativo, lotes | M-14, M-13, M-07, M-08, M-09, M-04 | Bloque 1 |
| **3 · Control** | Ajustes con aprobación, bitácora, rol Auditor, eliminación lógica, verificación de integridad | M-10, M-18 | Bloques 1–2 |
| **4 · Medición** | Conteo cíclico, ocultamiento de la cantidad esperada, segundo conteo, KPI-01/05/08, reportes | M-11, M-16 | Bloques 2–3 |
| **5 · Adopción** | Tablet, escaneo, confirmación visible, panel de tareas, sin indicadores individuales, novedades, mensajes claros, sincronización | M-20, M-12 (+ RNF transversales) | Bloques 1–4 |
| **6 · Anticipación** | Alertas por reglas, umbrales por SKU, dashboard del Jefe, cierre de jornada | M-15, M-17 (+ PN-14) | Bloques 2–5 |

> **Observación `[SRS]`.** El SPEC sitúa las **transferencias** (M-09, parte) y el **conteo general** (M-11, parte) en el Horizonte 2, aunque el módulo M-09 es P0. Esto no altera las dependencias de la tabla 11.1 (que son de módulo), pero sí el orden de entrega (H-08, resuelto por DEC-01 = A en la v1.2: las transferencias y el conteo general quedan fuera del umbral aprobatorio).

## 11.5 Dependencias entre historias y entre requisitos

- **Entre historias:** cada historia del Cap. 5 declara sus prerrequisitos en el campo «Depende de» `[SRS]`.
- **Entre requisitos:** cada RF del Cap. 6 conserva la columna «Depende de» del SPEC (con IDs permanentes).
- **Entre reglas y requisitos:** la matriz del §9.5 indica qué RF y HU implementan cada regla.

---

**ESTADO DEL CAPÍTULO 11**

| | |
|---|---|
| **Completado** | Tabla y matriz de dependencias de los 20 módulos · módulos raíz · ciclos funcionales · bloques de referencia |
| **Pendiente** | Planificación de construcción (Fase 5 del roadmap; fuera de este SRS) |
| **Riesgos encontrados** | Ciclos funcionales entre estructura de bodega, QR, kardex y existencia: exigen definir el orden de entrega en la fase de diseño |
| **Dependencias** | Cap. 4 (casos de uso), Cap. 5–6 (dependencias por historia y por RF) |


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
| **MVP-Núcleo (H1) — umbral aprobatorio `[DEC-01]`** | Todo lo que el backlog del SPEC declara Horizonte 1, incluidas la trazabilidad por pieza (elemento 40, v1.2) y el cierre de brechas y de jornada (elemento 41, v1.3): 84 HU y 143 RF de la v1.1, más 7 HU y 9 RF de la v1.2, más 3 HU y 12 RF de la v1.3 | **94** | **164** |
| **MVP-Completo (H1 + H2)** | Todo el alcance DC-02, incluidos los 20 HU / 21 RF del Horizonte 2 (transferencias, conteo general, inmovilización de lotes, escalamientos, carga masiva, existencia histórica, reportes programados, exportación analítica, dashboard del Coordinador, código de barras secundario, criterios de asignación, lotes por antigüedad, reasignación de tareas, alerta de ajustes recurrentes) | **114** | **185** |

**Regla de aceptación:** el MVP se acepta con el **MVP-Núcleo** `[DEC-01]`. Lo que el MVP-Completo añade (Horizonte 2: transferencias, conteo general y demás) **no es criterio de aprobación**; queda como entrega posterior.

Distribución de las HU y RF por prioridad y horizonte `[SRS]`:

| MoSCoW | HU total | de ellas H1 | de ellas H2 | RF total | de ellos H1 | de ellos H2 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| **Must** (P0) | 40 | 38 | 2 | 82 | 81 | 1 |
| **Should** (P1) | 59 | 48 | 11 | 84 | 69 | 15 |
| **Could** (P2) | 15 | 8 | 7 | 19 | 14 | 5 |
| **Won't** (P3) | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **114** | **94** | **20** | **185** | **164** | **21** |

## 12.3 Criterios de aceptación por dimensión

### Dimensión 1 — Completitud funcional

| ID | Criterio | Evidencia de verificación |
|---|---|---|
| **CA-01** | **Todas las HU *Must* del umbral elegido están aceptadas:** todos sus escenarios Gherkin se ejecutan y pasan | Informe de ejecución de escenarios por HU (515 escenarios en total; los del umbral elegido son obligatorios) |
| **CA-02** | **Todos los RF *Must* del umbral elegido están verificados** por prueba o inspección | Matriz RF → prueba (Cap. 9 §9.4) |
| **CA-03** | **Las HU y RF *Should* del umbral elegido están aceptadas**, o su exclusión fue aprobada por escrito por el Director con su riesgo | Acta de decisión |
| **CA-04** | Los 24 casos de uso del Cap. 4 pueden recorrerse de extremo a extremo con datos de la empresa piloto (CU-19 solo si DEC-05 lo incorpora) | Registro de recorrido por caso de uso |
| **CA-05** | Los **cinco procesos del núcleo transaccional** —entrada, salida, movimiento interno, ajuste y conteo— operan **sin cuaderno** durante el período de prueba (OP-01) | Cero movimientos registrados fuera del sistema (verificación de campo) |

### Dimensión 2 — Reglas de negocio

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-06** | **Cada una de las 60 reglas estructurales** se verifica con al menos una prueba **negativa** (el sistema rechaza la operación que la viola) y una positiva | Matriz RN → prueba (Cap. 9 §9.5) |
| **CA-07** | **Cada una de las 22 reglas configurables** se verifica con el umbral configurado y con el comportamiento antes y después del umbral | Ídem |
| **CA-08** | Las reglas del núcleo no configurable de §9.1 (RN-INT-001, RN-EXI-001, RN-INT-002, RN-AJU-001, RN-AJU-003, RN-CNT-002, RN-CNT-003, RN-AUD-001, RN-MAE-007, RN-INT-004) **no aparecen como parametrizables** en Parámetros y Configuración (HU-PAR-003) | Inspección de M-19 |
| **CA-09** | **Ningún rol —incluido el Administrador— dispone de una función de edición o eliminación** de un movimiento confirmado, de la bitácora ni de ningún elemento (RN-INT-002, RN-AUD-001, RN-MAE-007) | Búsqueda exhaustiva de funciones de escritura (RNF-AUD-002) |
| **CA-10** | La verificación de integridad «existencia = suma de movimientos» (RN-INT-004) **no reporta discrepancias** al cierre de la prueba (KPI-09 = 0, objetivo estructural) | Ejecución de la verificación global (RNF-AUD-005) |

### Dimensión 3 — Requisitos no funcionales

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-11** | **Cada RNF (47) fue verificado por el método que declara su columna «Verificación»** | Registro de verificación por RNF (Cap. 7) |
| **CA-12** | Los objetivos numéricos de rendimiento (RNF-REN-001…006) **se calibran contra la línea base y se aprueban antes de usarse como umbral de aceptación**; no se aceptan valores no calibrados | Acta de calibración (pendiente #12) |
| **CA-13** | La categoría de **usabilidad** (RNF-USA-001…007) se verifica con **usuarios reales de perfil Auxiliar sin formación previa** | Prueba de usabilidad con Auxiliares |
| **CA-14** | El cumplimiento de la protección de datos personales (RNF-SEG-008) fue **revisado antes de producción** | Revisión de cumplimiento |
| **CA-15** | Se ejecutó al menos **una restauración de respaldo de prueba** (RNF-DSP-004) y una prueba de recuperación acotada (RNF-DSP-005) | Registro de restauración |

### Dimensión 4 — Medición del propio impacto (compromiso ante el jurado)

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-16** | **KPI-01, KPI-05 y KPI-08 se calculan** con la fórmula del Cap. 9 y se pueden comparar contra la **línea base** | Reporte de los tres KPI |
| **CA-17** | **Existe línea base** de los tres KPI antes de iniciar el piloto (V-03) | Documento de línea base (**precondición externa al software**) |
| **CA-18** | El informe de impacto **reporta el resultado íntegro, favorable o no** (V-06, RG-35). *El software se acepta por cumplir sus requisitos, no por alcanzar las cifras de la literatura* | Informe de impacto |
| **CA-19** | Los 24 KPI son calculables por el sistema; los que dependen de un dato que ningún RF exige capturar (KPI-05, 07, 10, 12, 17, 24; H-12) quedan **explícitamente marcados** «calculable» o «pendiente de DEC-06» | Tabla del Anexo C |
| **CA-20** | El sistema **expone los datos** a la herramienta analítica externa sin diseñar tableros (RF-REP-004, RF-REP-005) | Verificación de la exposición estructurada |

### Dimensión 5 — Adopción (usuario crítico: el Auxiliar)

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-21** | Un **Auxiliar sin experiencia previa** registra una entrada, una salida y un movimiento interno tras una **capacitación breve** (RNF-USA-001) | Prueba con usuarios reales |
| **CA-22** | El Auxiliar **no ve** indicadores de desempeño individual ni comparaciones entre personas (RNF-USA-005, PR-06); la novedad no se contabiliza en contra del reportante (RF-NOV-003) | Revisión de todas las pantallas del rol |
| **CA-23** | Todo rechazo del sistema **explica el motivo** en lenguaje comprensible (RNF-USA-004, RNF-ACS-005) | Revisión de mensajes de rechazo |
| **CA-24** | Toda operación de registro entrega **confirmación visible** de que quedó guardada (RNF-USA-003) | Revisión de cada operación de escritura |
| **CA-25** | **KPI-24 (adopción) se mide con verificación de campo** y su resultado se reporta al Director (RG-01) | Reporte de adopción |
| **CA-26** | La operación es completa desde **tablet**, sin instalación nativa y con cámara (RNF-TAB-001, RNF-TAB-002, RNF-TAB-003) | Recorrido de las funciones del Auxiliar y del Coordinador en tablet |

### Dimensión 6 — Independencia de la auditoría

| ID | Criterio | Evidencia |
|---|---|---|
| **CA-27** | El **Auditor** ejecuta CU-18 completo (kardex, ajustes, conteos, anulaciones, bitácora, observaciones, exportación) **sin poder modificar el inventario** (RNF-SEG-005) | Recorrido con rol Auditor + intentos de escritura rechazados y registrados |
| **CA-28** | **Cero** casos en los que solicitante y aprobador coincidan (HU-AUD-004) y **cero** movimientos sin usuario atribuible | Reporte de auditoría |
| **CA-29** | Toda cuenta corresponde a una persona identificada; **no existen cuentas compartidas** (RN-INT-001) | Revisión de cuentas |

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
| **CA-34** | **No existe** ninguna función de ventas, compras completas, producción, contabilidad, nómina, CRM o facturación (DC-03); ninguna pantalla de entrada o salida solicita precio, cliente, factura ni documento comercial (RN-SAL-002, RF-ENT-002, RF-SAL-002) | Inspección de pantallas y datos solicitados |
| **CA-35** | **No existe** ningún componente de inteligencia artificial (DC-07): las alertas se generan solo por reglas y umbrales (RF-ALE-002) | Inspección de las reglas de alerta |
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

1. Es posible dejar la existencia de una unidad por debajo de cero por cualquier vía (RN-EXI-001).
2. Es posible editar o eliminar un movimiento confirmado, un registro de la bitácora o cualquier elemento maestro, con cualquier rol (RN-INT-002, RN-AUD-001, RN-MAE-007).
3. Un usuario puede aprobar una solicitud que él mismo originó, o el Auditor puede escribir en el inventario (RN-AJU-001, RN-AUD-002).
4. Existen acciones sin usuario atribuible o cuentas compartidas (RN-INT-001).
5. La verificación «existencia = suma de movimientos» reporta discrepancias sin explicación (RN-INT-004).
6. Un contador puede ver la cantidad esperada antes o después de contar (RN-CNT-002).
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


---

# ANEXO A — EQUIVALENCIA DE IDENTIFICADORES (SPEC → SRS)

> Tabla de consulta para quien tenga el SPEC en la mano. Los IDs permanentes de este documento **no cambian**; los del SPEC (*legacy*) quedan como referencia histórica.

## A.1 Historias de usuario (114)

| SPEC | SRS | Módulo | | SPEC | SRS | Módulo | | SPEC | SRS | Módulo |
|---|---|:--:|---|---|---|:--:|---|---|---|:--:|
| HU-001 | HU-ACC-001 | M-01 | | HU-002 | HU-ACC-002 | M-01 | | HU-003 | HU-ACC-003 | M-01 |
| HU-004 | HU-ACC-004 | M-01 | | HU-005 | HU-USR-001 | M-02 | | HU-006 | HU-USR-002 | M-02 |
| HU-007 | HU-USR-003 | M-02 | | HU-008 | HU-USR-004 | M-02 | | HU-009 | HU-USR-005 | M-02 |
| HU-010 | HU-CAT-001 | M-03 | | HU-011 | HU-CAT-002 | M-03 | | HU-012 | HU-CAT-003 | M-03 |
| HU-013 | HU-CAT-004 | M-03 | | HU-014 | HU-CAT-005 | M-03 | | HU-015 | HU-CAT-006 | M-03 |
| HU-016 | HU-LOT-001 | M-04 | | HU-017 | HU-LOT-002 | M-04 | | HU-018 | HU-LOT-003 | M-04 |
| HU-019 | HU-LOT-004 | M-04 | | HU-020 | HU-BOD-001 | M-05 | | HU-021 | HU-BOD-002 | M-05 |
| HU-022 | HU-BOD-003 | M-05 | | HU-023 | HU-BOD-004 | M-05 | | HU-024 | HU-BOD-005 | M-05 |
| HU-025 | HU-QRC-001 | M-06 | | HU-026 | HU-QRC-002 | M-06 | | HU-027 | HU-QRC-003 | M-06 |
| HU-028 | HU-QRC-004 | M-06 | | HU-029 | HU-QRC-005 | M-06 | | HU-030 | HU-ENT-001 | M-07 |
| HU-031 | HU-ENT-002 | M-07 | | HU-032 | HU-ENT-003 | M-07 | | HU-033 | HU-ENT-004 | M-07 |
| HU-034 | HU-ENT-005 | M-07 | | HU-035 | HU-ENT-006 | M-07 | | HU-036 | HU-ENT-007 | M-07 |
| HU-037 | HU-ENT-008 | M-07 | | HU-104 | HU-ENT-009 | M-07 | | HU-105 | HU-ENT-010 | M-07 |
| HU-038 | HU-SAL-001 | M-08 | | HU-039 | HU-SAL-002 | M-08 | | HU-040 | HU-SAL-003 | M-08 |
| HU-041 | HU-SAL-004 | M-08 | | HU-042 | HU-SAL-005 | M-08 | | HU-043 | HU-SAL-006 | M-08 |
| HU-044 | HU-SAL-007 | M-08 | | HU-107 | HU-SAL-008 | M-08 | | HU-108 | HU-SAL-009 | M-08 |
| HU-045 | HU-MOV-001 | M-09 | | HU-046 | HU-MOV-002 | M-09 | | HU-047 | HU-MOV-003 | M-09 |
| HU-048 | HU-MOV-004 | M-09 | | HU-049 | HU-MOV-005 | M-09 | | HU-050 | HU-MOV-006 | M-09 |
| HU-051 | HU-MOV-007 | M-09 | | HU-106 | HU-MOV-008 | M-09 | | HU-111 | HU-MOV-009 | M-09 |
| HU-052 | HU-AJU-001 | M-10 | | HU-053 | HU-AJU-002 | M-10 | | HU-054 | HU-AJU-003 | M-10 |
| HU-055 | HU-AJU-004 | M-10 | | HU-056 | HU-AJU-005 | M-10 | | HU-057 | HU-AJU-006 | M-10 |
| HU-058 | HU-CNT-001 | M-11 | | HU-059 | HU-CNT-002 | M-11 | | HU-060 | HU-CNT-003 | M-11 |
| HU-061 | HU-CNT-004 | M-11 | | HU-062 | HU-CNT-005 | M-11 | | HU-063 | HU-CNT-006 | M-11 |
| HU-064 | HU-CNT-007 | M-11 | | HU-065 | HU-CNT-008 | M-11 | | HU-066 | HU-CNT-009 | M-11 |
| HU-109 | HU-CNT-010 | M-11 | | HU-112 | HU-CNT-011 | M-11 | | HU-067 | HU-NOV-001 | M-12 |
| HU-068 | HU-NOV-002 | M-12 | | HU-069 | HU-NOV-003 | M-12 | | HU-070 | HU-NOV-004 | M-12 |
| HU-071 | HU-INV-001 | M-13 | | HU-072 | HU-INV-002 | M-13 | | HU-073 | HU-INV-003 | M-13 |
| HU-074 | HU-INV-004 | M-13 | | HU-075 | HU-INV-005 | M-13 | | HU-076 | HU-INV-006 | M-13 |
| HU-077 | HU-KDX-001 | M-14 | | HU-078 | HU-KDX-002 | M-14 | | HU-079 | HU-KDX-003 | M-14 |
| HU-080 | HU-KDX-004 | M-14 | | HU-081 | HU-KDX-005 | M-14 | | HU-110 | HU-KDX-006 | M-14 |
| HU-082 | HU-ALE-001 | M-15 | | HU-083 | HU-ALE-002 | M-15 | | HU-084 | HU-ALE-003 | M-15 |
| HU-085 | HU-ALE-004 | M-15 | | HU-086 | HU-ALE-005 | M-15 | | HU-087 | HU-REP-001 | M-16 |
| HU-088 | HU-REP-002 | M-16 | | HU-089 | HU-REP-003 | M-16 | | HU-090 | HU-REP-004 | M-16 |
| HU-091 | HU-DSH-001 | M-17 | | HU-092 | HU-DSH-002 | M-17 | | HU-093 | HU-DSH-003 | M-17 |
| HU-094 | HU-AUD-001 | M-18 | | HU-095 | HU-AUD-002 | M-18 | | HU-096 | HU-AUD-003 | M-18 |
| HU-097 | HU-AUD-004 | M-18 | | HU-098 | HU-PAR-001 | M-19 | | HU-099 | HU-PAR-002 | M-19 |
| HU-100 | HU-PAR-003 | M-19 | | HU-101 | HU-TAR-001 | M-20 | | HU-102 | HU-TAR-002 | M-20 |
| HU-103 | HU-TAR-003 | M-20 | | HU-113 | HU-TAR-004 | M-20 | | HU-114 | HU-TAR-005 | M-20 |

## A.2 Requisitos funcionales (185)

| SPEC | SRS | | SPEC | SRS | | SPEC | SRS | | SPEC | SRS |
|---|---|---|---|---|---|---|---|---|---|---|
| RF-001 | RF-ACC-001 | | RF-002 | RF-ACC-002 | | RF-003 | RF-ACC-003 | | RF-004 | RF-ACC-004 |
| RF-005 | RF-ACC-005 | | RF-006 | RF-ACC-006 | | RF-007 | RF-ACC-007 | | RF-008 | RF-USR-001 |
| RF-009 | RF-USR-002 | | RF-010 | RF-USR-003 | | RF-011 | RF-USR-004 | | RF-012 | RF-USR-005 |
| RF-013 | RF-USR-006 | | RF-014 | RF-USR-007 | | RF-015 | RF-USR-008 | | RF-016 | RF-CAT-001 |
| RF-017 | RF-CAT-002 | | RF-018 | RF-CAT-003 | | RF-019 | RF-CAT-004 | | RF-020 | RF-CAT-005 |
| RF-021 | RF-CAT-006 | | RF-022 | RF-CAT-007 | | RF-023 | RF-CAT-008 | | RF-024 | RF-CAT-009 |
| RF-025 | RF-CAT-010 | | RF-026 | RF-LOT-001 | | RF-027 | RF-LOT-002 | | RF-028 | RF-LOT-003 |
| RF-029 | RF-LOT-004 | | RF-030 | RF-LOT-005 | | RF-031 | RF-LOT-006 | | RF-032 | RF-BOD-001 |
| RF-033 | RF-BOD-002 | | RF-034 | RF-BOD-003 | | RF-035 | RF-BOD-004 | | RF-036 | RF-BOD-005 |
| RF-037 | RF-BOD-006 | | RF-038 | RF-BOD-007 | | RF-039 | RF-BOD-008 | | RF-172 | RF-BOD-009 |
| RF-040 | RF-QRC-001 | | RF-041 | RF-QRC-002 | | RF-042 | RF-QRC-003 | | RF-043 | RF-QRC-004 |
| RF-044 | RF-QRC-005 | | RF-045 | RF-QRC-006 | | RF-046 | RF-QRC-007 | | RF-047 | RF-QRC-008 |
| RF-179 | RF-QRC-009 | | RF-048 | RF-ENT-001 | | RF-049 | RF-ENT-002 | | RF-050 | RF-ENT-003 |
| RF-051 | RF-ENT-004 | | RF-052 | RF-ENT-005 | | RF-053 | RF-ENT-006 | | RF-054 | RF-ENT-007 |
| RF-055 | RF-ENT-008 | | RF-056 | RF-ENT-009 | | RF-057 | RF-ENT-010 | | RF-058 | RF-ENT-011 |
| RF-059 | RF-ENT-012 | | RF-060 | RF-ENT-013 | | RF-163 | RF-ENT-014 | | RF-164 | RF-ENT-015 |
| RF-165 | RF-ENT-016 | | RF-180 | RF-ENT-017 | | RF-061 | RF-SAL-001 | | RF-062 | RF-SAL-002 |
| RF-063 | RF-SAL-003 | | RF-064 | RF-SAL-004 | | RF-065 | RF-SAL-005 | | RF-066 | RF-SAL-006 |
| RF-067 | RF-SAL-007 | | RF-068 | RF-SAL-008 | | RF-069 | RF-SAL-009 | | RF-070 | RF-SAL-010 |
| RF-071 | RF-SAL-011 | | RF-167 | RF-SAL-012 | | RF-168 | RF-SAL-013 | | RF-176 | RF-SAL-014 |
| RF-072 | RF-MOV-001 | | RF-073 | RF-MOV-002 | | RF-074 | RF-MOV-003 | | RF-075 | RF-MOV-004 |
| RF-076 | RF-MOV-005 | | RF-077 | RF-MOV-006 | | RF-078 | RF-MOV-007 | | RF-079 | RF-MOV-008 |
| RF-080 | RF-MOV-009 | | RF-081 | RF-MOV-010 | | RF-082 | RF-MOV-011 | | RF-166 | RF-MOV-012 |
| RF-173 | RF-MOV-013 | | RF-083 | RF-AJU-001 | | RF-084 | RF-AJU-002 | | RF-085 | RF-AJU-003 |
| RF-086 | RF-AJU-004 | | RF-087 | RF-AJU-005 | | RF-088 | RF-AJU-006 | | RF-089 | RF-AJU-007 |
| RF-090 | RF-AJU-008 | | RF-091 | RF-AJU-009 | | RF-092 | RF-AJU-010 | | RF-093 | RF-CNT-001 |
| RF-094 | RF-CNT-002 | | RF-095 | RF-CNT-003 | | RF-096 | RF-CNT-004 | | RF-097 | RF-CNT-005 |
| RF-098 | RF-CNT-006 | | RF-099 | RF-CNT-007 | | RF-100 | RF-CNT-008 | | RF-101 | RF-CNT-009 |
| RF-102 | RF-CNT-010 | | RF-103 | RF-CNT-011 | | RF-104 | RF-CNT-012 | | RF-105 | RF-CNT-013 |
| RF-169 | RF-CNT-014 | | RF-175 | RF-CNT-015 | | RF-106 | RF-NOV-001 | | RF-107 | RF-NOV-002 |
| RF-108 | RF-NOV-003 | | RF-109 | RF-NOV-004 | | RF-110 | RF-NOV-005 | | RF-111 | RF-NOV-006 |
| RF-174 | RF-NOV-007 | | RF-177 | RF-NOV-008 | | RF-112 | RF-INV-001 | | RF-113 | RF-INV-002 |
| RF-114 | RF-INV-003 | | RF-115 | RF-INV-004 | | RF-116 | RF-INV-005 | | RF-117 | RF-INV-006 |
| RF-118 | RF-INV-007 | | RF-119 | RF-INV-008 | | RF-171 | RF-INV-009 | | RF-120 | RF-KDX-001 |
| RF-121 | RF-KDX-002 | | RF-122 | RF-KDX-003 | | RF-123 | RF-KDX-004 | | RF-124 | RF-KDX-005 |
| RF-125 | RF-KDX-006 | | RF-126 | RF-KDX-007 | | RF-170 | RF-KDX-008 | | RF-178 | RF-KDX-009 |
| RF-127 | RF-ALE-001 | | RF-128 | RF-ALE-002 | | RF-129 | RF-ALE-003 | | RF-130 | RF-ALE-004 |
| RF-131 | RF-ALE-005 | | RF-132 | RF-ALE-006 | | RF-133 | RF-ALE-007 | | RF-134 | RF-REP-001 |
| RF-135 | RF-REP-002 | | RF-136 | RF-REP-003 | | RF-137 | RF-REP-004 | | RF-138 | RF-REP-005 |
| RF-139 | RF-REP-006 | | RF-140 | RF-REP-007 | | RF-185 | RF-REP-008 | | RF-141 | RF-DSH-001 |
| RF-142 | RF-DSH-002 | | RF-143 | RF-DSH-003 | | RF-144 | RF-DSH-004 | | RF-145 | RF-AUD-001 |
| RF-146 | RF-AUD-002 | | RF-147 | RF-AUD-003 | | RF-148 | RF-AUD-004 | | RF-149 | RF-AUD-005 |
| RF-150 | RF-AUD-006 | | RF-151 | RF-AUD-007 | | RF-152 | RF-PAR-001 | | RF-153 | RF-PAR-002 |
| RF-154 | RF-PAR-003 | | RF-155 | RF-PAR-004 | | RF-156 | RF-PAR-005 | | RF-157 | RF-PAR-006 |
| RF-181 | RF-PAR-007 | | RF-158 | RF-TAR-001 | | RF-159 | RF-TAR-002 | | RF-160 | RF-TAR-003 |
| RF-161 | RF-TAR-004 | | RF-162 | RF-TAR-005 | | RF-182 | RF-TAR-006 | | RF-183 | RF-TAR-007 |
| RF-184 | RF-TAR-008 | |  |  | |  |  | |  |  |

## A.3 Requisitos no funcionales (47)

| SPEC | SRS | | SPEC | SRS | | SPEC | SRS | | SPEC | SRS |
|---|---|---|---|---|---|---|---|---|---|---|
| RNF-001 | RNF-SEG-001 | | RNF-002 | RNF-SEG-002 | | RNF-003 | RNF-SEG-003 | | RNF-004 | RNF-SEG-004 |
| RNF-005 | RNF-SEG-005 | | RNF-006 | RNF-SEG-006 | | RNF-007 | RNF-SEG-007 | | RNF-008 | RNF-SEG-008 |
| RNF-009 | RNF-DSP-001 | | RNF-010 | RNF-DSP-002 | | RNF-011 | RNF-DSP-003 | | RNF-012 | RNF-DSP-004 |
| RNF-013 | RNF-DSP-005 | | RNF-014 | RNF-REN-001 | | RNF-015 | RNF-REN-002 | | RNF-016 | RNF-REN-003 |
| RNF-017 | RNF-REN-004 | | RNF-018 | RNF-REN-005 | | RNF-019 | RNF-REN-006 | | RNF-020 | RNF-ESC-001 |
| RNF-021 | RNF-ESC-002 | | RNF-022 | RNF-ESC-003 | | RNF-023 | RNF-ESC-004 | | RNF-024 | RNF-ESC-005 |
| RNF-025 | RNF-ACS-001 | | RNF-026 | RNF-ACS-002 | | RNF-027 | RNF-ACS-003 | | RNF-028 | RNF-ACS-004 |
| RNF-029 | RNF-ACS-005 | | RNF-030 | RNF-AUD-001 | | RNF-031 | RNF-AUD-002 | | RNF-032 | RNF-AUD-003 |
| RNF-033 | RNF-AUD-004 | | RNF-034 | RNF-AUD-005 | | RNF-035 | RNF-USA-001 | | RNF-036 | RNF-USA-002 |
| RNF-037 | RNF-USA-003 | | RNF-038 | RNF-USA-004 | | RNF-039 | RNF-USA-005 | | RNF-040 | RNF-USA-006 |
| RNF-041 | RNF-USA-007 | | RNF-042 | RNF-TAB-001 | | RNF-043 | RNF-TAB-002 | | RNF-044 | RNF-TAB-003 |
| RNF-045 | RNF-TAB-004 | | RNF-046 | RNF-NAV-001 | | RNF-047 | RNF-NAV-002 | |  |  |

## A.4 Reglas de negocio (92)

| SPEC | SRS | Tipo | | SPEC | SRS | Tipo | | SPEC | SRS | Tipo |
|---|---|:--:|---|---|---|:--:|---|---|---|:--:|
| RN-001 | RN-INT-001 | Estr. | | RN-012 | RN-INT-002 | Estr. | | RN-054 | RN-INT-003 | Estr. |
| RN-065 | RN-INT-004 | Estr. | | RN-066 | RN-INT-005 | Estr. | | RN-067 | RN-INT-006 | Estr. |
| RN-068 | RN-INT-007 | Estr. | | RN-083 | RN-INT-008 | Estr. | | RN-009 | RN-EXI-001 | Estr. |
| RN-019 | RN-EXI-002 | Estr. | | RN-025 | RN-EXI-003 | Estr. | | RN-031 | RN-EXI-004 | Estr. |
| RN-032 | RN-EXI-005 | Estr. | | RN-036 | RN-EXI-006 | Estr. | | RN-081 | RN-EXI-007 | Estr. |
| RN-002 | RN-MAE-001 | Estr. | | RN-004 | RN-MAE-002 | Estr. | | RN-010 | RN-MAE-003 | Estr. |
| RN-011 | RN-MAE-004 | Estr. | | RN-013 | RN-MAE-005 | Estr. | | RN-014 | RN-MAE-006 | Estr. |
| RN-063 | RN-MAE-007 | Estr. | | RN-076 | RN-MAE-008 | Estr. | | RN-077 | RN-MAE-009 | Conf. |
| RN-015 | RN-IDE-001 | Estr. | | RN-016 | RN-IDE-002 | Estr. | | RN-017 | RN-IDE-003 | Estr. |
| RN-018 | RN-IDE-004 | Estr. | | RN-071 | RN-LOT-001 | Estr. | | RN-072 | RN-LOT-002 | Estr. |
| RN-036b | RN-LOT-003 | Estr. | | RN-073 | RN-LOT-004 | Estr. | | RN-074 | RN-LOT-005 | Conf. |
| RN-084 | RN-LOT-006 | Estr. | | RN-085 | RN-LOT-007 | Estr. | | RN-002b | RN-ENT-001 | Estr. |
| RN-003 | RN-ENT-002 | Conf. | | RN-005 | RN-ENT-003 | Estr. | | RN-006 | RN-ENT-004 | Conf. |
| RN-007 | RN-ENT-005 | Estr. | | RN-008 | RN-ENT-006 | Estr. | | RN-057b | RN-ENT-007 | Estr. |
| RN-030 | RN-SAL-001 | Conf. | | RN-048 | RN-SAL-002 | Estr. | | RN-049 | RN-SAL-003 | Conf. |
| RN-050 | RN-SAL-004 | Estr. | | RN-051 | RN-SAL-005 | Conf. | | RN-052 | RN-SAL-006 | Estr. |
| RN-053 | RN-SAL-007 | Estr. | | RN-086 | RN-SAL-008 | Estr. | | RN-088 | RN-SAL-009 | Estr. |
| RN-020 | RN-MOV-001 | Conf. | | RN-021 | RN-MOV-002 | Conf. | | RN-022 | RN-MOV-003 | Conf. |
| RN-026 | RN-MOV-004 | Estr. | | RN-027 | RN-MOV-005 | Estr. | | RN-028 | RN-MOV-006 | Conf. |
| RN-033 | RN-MOV-007 | Estr. | | RN-034 | RN-MOV-008 | Conf. | | RN-035 | RN-MOV-009 | Estr. |
| RN-082 | RN-MOV-010 | Estr. | | RN-087 | RN-MOV-011 | Estr. | | RN-090 | RN-MOV-012 | Estr. |
| RN-023 | RN-AJU-001 | Estr. | | RN-024 | RN-AJU-002 | Conf. | | RN-029 | RN-AJU-003 | Estr. |
| RN-037 | RN-AJU-004 | Conf. | | RN-038 | RN-AJU-005 | Conf. | | RN-062 | RN-AJU-006 | Estr. |
| RN-070 | RN-AJU-007 | Estr. | | RN-039 | RN-CNT-001 | Estr. | | RN-040 | RN-CNT-002 | Estr. |
| RN-041 | RN-CNT-003 | Estr. | | RN-042 | RN-CNT-004 | Estr. | | RN-044 | RN-CNT-005 | Conf. |
| RN-045 | RN-CNT-006 | Estr. | | RN-046 | RN-CNT-007 | Estr. | | RN-047 | RN-CNT-008 | Conf. |
| RN-089 | RN-CNT-009 | Estr. | | RN-043 | RN-NOV-001 | Estr. | | RN-059 | RN-NOV-002 | Conf. |
| RN-060 | RN-NOV-003 | Conf. | | RN-055 | RN-ALE-001 | Conf. | | RN-056 | RN-ALE-002 | Conf. |
| RN-057 | RN-ALE-003 | Conf. | | RN-058 | RN-ALE-004 | Estr. | | RN-075 | RN-ALE-005 | Estr. |
| RN-061 | RN-AUD-001 | Estr. | | RN-064 | RN-AUD-002 | Estr. | | RN-078 | RN-AUD-003 | Estr. |
| RN-079 | RN-AUD-004 | Estr. | | RN-080 | RN-AUD-005 | Estr. | |  | |  |

**Marcadores sin contenido (no reciben ID):** `RN-069*` («reservado») y `RN-026b*` («ver nota de numeración») — H-09.


## A.5 Elementos que conservan su ID del SPEC

`KPI-01…KPI-24` · `PN-01…PN-14` · `CD-01…CD-49` · `M-01…M-20` · `RG-01…RG-42` · `DC-01…DC-08` · `PR-01…PR-06` · `OP-01…OP-12`.


---

# ANEXO B — AUDITORÍA INTERNA DEL DOCUMENTO

> Verificación final de integridad del SRS frente al SPEC. Los recuentos se calcularon **programáticamente** sobre las mismas tablas de las que se generaron los capítulos 5–9 y los anexos.

## B.1 Totales

| Elemento | Total en el SPEC (declarado) | Total real en las tablas del SPEC | **Total en el SRS** | ¿Se perdió alguno? |
|---|:--:|:--:|:--:|:--:|
| **Historias de usuario** | 114 | 114 | **114** (Must 40 · Should 59 · Could 15 · Won't 0) | **No** |
| Criterios de aceptación → escenarios Gherkin | — | 515 | **515** | **No** (1:1) |
| **Requisitos funcionales** | 185 | 185 | **185** (Must 82 · Should 84 · Could 19 · Won't 0) | **No** |
| **Requisitos no funcionales** | 47 | 47 | **47** (SEG 8, DSP 5, REN 6, ESC 5, ACS 5, AUD 5, USA 7, TAB 4, NAV 2) | **No** |
| **Reglas de negocio** | **68** (v1.0) | **82** (v1.0) + **3** (v1.1) + **6** (v1.2) + **1** (v1.4) | **92** (70 estructurales · 22 configurables) | **No** — discrepancia del SPEC (H-01) |
| **KPI** | 24 | 24 | **24** | **No** |
| **Casos de uso** | — | — | **24** (14 procesos PN + 10 de módulos) | — |
| Procesos de negocio (PN) | 14 | 14 | 14 (14 con caso de uso y con requisitos) | **No** |
| Conceptos de dominio (CD) | 48 (v1.0) | 49 | 49 (referenciados por RF: 49) | **No** |
| Módulos funcionales | 20 | 20 | 20 | **No** |
| Riesgos funcionales (RG) | 42 | 42 | 42 (permanecen en el SPEC) | **No** |

## B.2 Verificaciones de integridad

| # | Verificación | Resultado |
|---|---|:--:|
| V-1 | Todas las HU del SPEC (114) están en el SRS con ID permanente | ✅ 114/114 |
| V-2 | Todos los criterios de aceptación tienen un escenario Gherkin | ✅ 515/515 |
| V-3 | Todos los RF del SPEC (185) están en el SRS | ✅ 185/185 |
| V-4 | Todos los RNF del SPEC (47) están en el SRS | ✅ 47/47 |
| V-5 | Todas las reglas con contenido (92: 82 de la v1.0 + 3 de la v1.1 + 6 de la v1.2 + 1 de la v1.4) están en el SRS; los 2 marcadores vacíos quedan documentados | ✅ 92/92 |
| V-6 | Todos los KPI (24) están en el SRS con su fórmula | ✅ 24/24 |
| V-7 | Los IDs permanentes son únicos | ✅ 438 IDs |
| V-8 | Toda HU tiene al menos un RF | ✅ 114/114 |
| V-9 | Todo RF tiene al menos una HU | ✅ 185/185 |
| V-10 | Toda regla está cubierta por algún RF | ✅ 92/92 |
| V-11 | Toda regla está cubierta por alguna HU | ✅ 92/92 |
| V-12 | Todo KPI tiene al menos un RF que lo alimenta | ✅ 24/24 |
| V-13 | Todo proceso PN tiene caso de uso | ✅ 14/14 |
| V-14 | Todo proceso PN tiene al menos una HU y un RF | ✅ 14/14 (PN-14 con HU-TAR-004, HU-TAR-005 y RF-TAR-006…008 desde la v1.3) |
| V-15 | Todo concepto de dominio (49) es referenciado por algún RF | ✅ 49/49  |
| V-16 | Ninguna meta numérica nueva fue introducida | ✅ (los valores numéricos de RNF son los del SPEC) |
| V-17 | Ningún requisito nuevo fue creado: las propuestas de cierre de brechas están fuera del baseline (Anexo C) | ✅ |
| V-18 | Se respeta la exclusión de código, base de datos, arquitectura, ERD/UML, endpoints, APIs, frameworks y tecnologías | ✅ (la herramienta analítica externa se cita solo por DC-06) |


## B.3 Discrepancias del SPEC que este SRS detectó y tratamiento

| Hallazgo | SPEC declara | Contenido real | Tratamiento |
|---|---|---|---|
| H-01 | 68 reglas (51 est. + 17 conf.) | 82 (60 + 22) | Se conservan 82 (+3 incorporadas en la v1.1, +6 en la v1.2) |
| H-02 | RF: 72 P0 / 69 P1 / 21 P2 | 74 / 70 / 18 | Se usa la prioridad de cada fila |
| H-03 | Rangos HU-001…096 y RF-001…138 (§0.4) | HU-001…114 y RF-001…185 (corregido en la v1.3) | Prevalece el contenido |
| H-04 | Trazabilidad 41/12/9/38 % (§0.3) | 34/12/17/37 % (§13.3) | Sin impacto en requisitos |
| H-05 | HU-026 → RNF-014; HU-071 → RNF-012 | Correctos: RNF-015 y RNF-014 | Se enlazan los correctos |

## B.4 Riesgos abiertos

Ver **Anexo C**: 10 riesgos propios de la fase (R-S01…R-S10, uno crítico), 11 riesgos críticos heredados del SPEC (RG-01, 02, 13, 14, 16, 17, 23, 33, 34, 35, 36) y **9 decisiones pendientes del Director (DEC-01…DEC-09)**.

| Riesgo abierto principal | Sev. |
|---|:--:|
| R-S01 — El SRS se emite antes del AS-IS y de la línea base | 🔴 |
| RG-35 / RG-36 — El piloto puede no alcanzar las cifras; sin línea base no se demuestra mejora | 🔴 |
| RG-01 / RG-13 / RG-14 — Adopción real por el personal (operación fuera del sistema, rechazo, curva de aprendizaje) | 🔴 |
| R-S04 — Tensión entre DC-02 y el Horizonte 2 del backlog | 🟠 |
| R-S05 — Reglas y KPI sin requisito de captura; PN-14 sin requisitos | 🟠 |

---

**ESTADO DEL ANEXO B**

| | |
|---|---|
| **Completado** | Totales · 18 verificaciones · discrepancias del SPEC · riesgos abiertos |
| **Pendiente** | Nada dentro del anexo |
| **Riesgos encontrados** | Ver Anexo C |
| **Dependencias** | Todos los capítulos |


---

# ANEXO C — HALLAZGOS, DECISIONES Y RIESGOS ABIERTOS

> Este anexo **no modifica el baseline de requisitos**. Reúne lo que el Director debe decidir y lo que puede afectar el resultado. Toda «propuesta» aquí descrita **no forma parte del SRS** hasta que el Director la apruebe (Regla Innegociable 3).

## C.1 Decisiones que se solicitan al Director

| ID | Decisión requerida | Hallazgos | Opciones | Recomendación del SRS | Efecto de no decidir |
|---|---|---|---|---|---|
| **DEC-01** | **Umbral de entrega aprobatorio.** ¿El MVP aprobatorio es el Núcleo (H1) o el Completo (H1+H2)? ¿Transferencias y conteo general entran al MVP? | H-08 · S-15 | (a) Núcleo: 84 HU / 143 RF; transferencias y conteo general pasan a v1.1. (b) Completo: 103 HU / 162 RF. (c) Núcleo + transferencias + conteo general | Mantener **alcance = Completo** (respeta DC-02 y el Prompt #003), con **entrega secuenciada H1 → H2** y **umbral mínimo aprobatorio = Núcleo** | **RESUELTA el 30-sep-2026: opción (a) Núcleo, con 1 bodega piloto y la capa de trazabilidad por pieza (v1.2).** El Cap. 12 fija el Núcleo como umbral aprobatorio |
| **DEC-02** | **Lista de alcance del MVP.** Confirmar que «usuarios» y «auditoría» son los módulos M-02 y M-18 y que el **dashboard operativo (M-17)** permanece en el MVP; y que la exclusión es **toda** IA (DC-07) y no solo la generativa | H-17 | (a) Mantener los 20 módulos y la redacción de DC-07. (b) Restringir el MVP a la lista del Prompt #003 (retira M-17: 3 HU, 4 RF) | (a) | **RESUELTA el 30-sep-2026: opción (a).** Se mantienen los 20 módulos y la exclusión de toda IA |
| **DEC-03** | **Reglas de negocio: cifra y renumeración.** El SPEC declara 68; las tablas contienen 82 (60 estructurales + 22 configurables). Confirmar las 82, retirar los marcadores vacíos `RN-069*` y `RN-026b*` y adoptar como canónica la numeración `RN-<DOM>-nnn` | H-01 · H-09 · pendiente #11 | (a) Aceptar el SRS como renumeración canónica y emitir una fe de erratas del SPEC. (b) Mantener la numeración del SPEC | (a) | **RESUELTA el 30-sep-2026: opción (a).** Fe de erratas en el SPEC v1.3 §9.17 |
| **DEC-04** | **Semántica «estructural» vs «configurable».** Confirmar que toda regla estructural es no configurable (no solo las 10 de §9.1); definir si el Jefe puede **leer** parámetros y **quién** responde y cierra las observaciones de auditoría (RN-AUD-002) | H-06 · Cap. 10 nota 4 | (a) Toda estructural no configurable; Jefe lee parámetros; el Administrador o el Jefe responden. (b) Otra | (a) | **RESUELTA el 30-sep-2026: opción (a).** Toda regla estructural es no configurable |
| **DEC-05** | **Cierre operativo de jornada (PN-14).** ¿Se crean HU y RF? | H-10 | (a) Crear HU/RF (ver propuestas PROP-CIE). (b) Mover PN-14 a v1.1. (c) Excluirlo del MVP | (a), porque el backlog lo declara MVP (elemento 39) y RG-03 y RG-08 dependen de él | **RESUELTA el 30-sep-2026: opción (a).** HU-TAR-004, HU-TAR-005 y RF-TAR-006…008 |
| **DEC-06** | **Cierre de brechas de trazabilidad.** Aprobar o descartar las propuestas PROP-RN (reglas sin RF) y PROP-KPI (KPI sin dato de origen) | H-11 · H-12 · H-13 | (a) Aprobar todas. (b) Aprobar solo las de KPI-01/05/08. (c) Descartar | (a); como mínimo (b), porque KPI-05 es uno de los tres indicadores del compromiso | **RESUELTA el 30-sep-2026: opción (a).** Se aprueban todas las propuestas (C.2) |
| **DEC-07** | **«Valorización».** Definir si el permiso «consultar valorización» se retira del MVP o si se define una política de costeo | H-07 · Horizonte 3 | (a) Retirar del MVP (queda como restricción preventiva). (b) Definir política de costeo (roza DC-03) | (a) | **RESUELTA el 30-sep-2026: opción (a).** La valorización se retira del MVP |
| **DEC-08** | **Aprobación formal del SPEC v1.0 y numeración de fases.** Confirmar por escrito la aprobación del SPEC (el archivo dice «Emitido para revisión») y la equivalencia entre las fases del proyecto y las del roadmap | H-15 · H-16 | (a) Acta de aprobación + tabla de equivalencia de fases. (b) Otra | (a) | **Respondida el 30-sep-2026: opción (a); acta pendiente de firma** (borrador en `05_V13_DECISIONES/`) |
| **DEC-09** | **Alerta «lote próximo a vencer inmovilización».** El SPEC la enuncia con «fecha límite» de lote, dato que no existe en CD-06 ni en ningún RF | H-18 | (a) Redefinirla sobre el umbral de antigüedad (RN-LOT-005). (b) Agregar «fecha límite» al lote (funcionalidad nueva `[NUEVO]`) | (a) | **RESUELTA el 30-sep-2026: opción (a).** Umbral de antigüedad del lote |

Además siguen abiertas las **preguntas heredadas** del §0.5 (A-03, A-04, A-05, V-01, V-03, V-06, I-03, I-04, I-05, I-09, S-15).

## C.2 Propuestas de cierre de brechas (**APROBADAS por el Director el 30-sep-2026 e incorporadas al baseline en la v1.3**: DEC-05 y DEC-06)

> Correspondencia con los requisitos de la v1.3: PROP-RN-01 → RF-BOD-009 · PROP-RN-02 → RF-MOV-013 (HU-MOV-009) · PROP-RN-03 → RF-NOV-007 · PROP-RN-04 → RF-CNT-015 (HU-CNT-011; Horizonte 2) · PROP-RN-05 → RF-SAL-014 · PROP-RN-06 → RF-NOV-008 · PROP-KPI-01 → RF-KDX-009 · PROP-KPI-02 → RF-QRC-009 · PROP-KPI-03 → RF-BOD-009 · PROP-KPI-04 → RF-ENT-017 · PROP-KPI-05 → RF-PAR-001 (parámetro «días sin movimiento») · PROP-KPI-06 → RF-PAR-007 · PROP-CIE-01…03 → RF-TAR-006…008 (HU-TAR-004, HU-TAR-005).

### C.2.1 Reglas de negocio sin requisito funcional que las implemente (H-11)

| ID | Regla | Comportamiento sin RF | Origen del comportamiento | Propuesta de RF (texto sugerido) |
|---|---|---|---|---|
| **PROP-RN-01** | RN-MOV-003 (desviación de ubicación) | Registrar la desviación cuando el Auxiliar ubica en un lugar distinto al propuesto, como información y no como falta | PN-03 E-02 · HU-ENT-006 crit. 3 | «El sistema debe registrar como información operativa la desviación entre la ubicación propuesta y la confirmada y notificar al Coordinador, sin imputarla al Auxiliar.» (dominio BOD o ENT) |
| **PROP-RN-02** | RN-MOV-006 (movimiento interno en tránsito) | Un movimiento interno interrumpido queda en tránsito, no disponible en origen ni destino, con alerta al exceder el tiempo | PN-05 E-05 | «El sistema debe mantener en tránsito un movimiento interno interrumpido y generar alerta al superar el tiempo máximo configurado.» (dominio MOV). *Tampoco tiene HU* |
| **PROP-RN-03** | RN-NOV-001 (mercancía sin registro) | No se cuenta ni se usa hasta ser identificada; se incorpora por ajuste por sobrante con aprobación del Jefe | PN-08 E-04 · PN-09 E-06 · PN-12 E-05 | «El sistema debe impedir contar o usar mercancía sin registro hasta su identificación y permitir su incorporación solo mediante ajuste por sobrante con motivo tipificado y aprobación del Jefe.» (dominio NOV). Complementa HU-NOV-004 |
| **PROP-RN-04** | RN-CNT-008 (diferencia crítica en conteo general) | Notificar al Administrador y al Auditor antes de permitir el cierre si la diferencia global supera el umbral crítico | PN-09 E-05 | «El sistema debe notificar al Administrador y al Auditor y condicionar el cierre de un conteo general cuando la diferencia global supere el umbral crítico configurado.» (dominio CNT; incluir el umbral crítico en RF-PAR-001). *Tampoco tiene HU* |
| **PROP-RN-05** | RN-SAL-005 (reserva vencida) | Liberar automáticamente una reserva no ejecutada en su plazo y alertar al solicitante | PN-10 E-05 · HU-SAL-002 crit. 4 | «El sistema debe liberar automáticamente la reserva no ejecutada dentro del plazo configurado y alertar al solicitante.» (dominio SAL) |
| **PROP-RN-06** | RN-NOV-002 (novedad vencida) | Escalar al Jefe la novedad sin resolver en el plazo configurado y generar alerta | PN-12 E-01 · HU-NOV-003 | «El sistema debe escalar al Jefe y alertar las novedades no resueltas dentro del plazo configurado.» (dominio NOV) |

### C.2.2 KPI cuyo dato de origen ningún RF exige capturar (H-12)

| ID | KPI | Dato que falta | Propuesta de RF (texto sugerido) |
|---|---|---|---|
| **PROP-KPI-01** | KPI-05 Tiempo medio de registro | Instante de **inicio** de la operación (RF-KDX-001 solo registra fecha y hora del movimiento) | «El sistema debe registrar el instante de inicio y el de confirmación de cada movimiento.» (dominio KDX) |
| **PROP-KPI-02** | KPI-07 Movimientos sin identificador escaneado | Marca de «selección manual sin escaneo» (PN-03 E-05) | «El sistema debe registrar en cada movimiento si la identificación se hizo por escaneo o por selección manual.» (dominio QRC/KDX) |
| **PROP-KPI-03** | KPI-10 Desviaciones de ubicación | Registro de la desviación | Se cubre con PROP-RN-01 |
| **PROP-KPI-04** | KPI-12 Tiempo medio de recepción | Instante de **llegada** de la mercancía | «El sistema debe registrar el instante de llegada de la mercancía al documento de entrada.» (dominio ENT) |
| **PROP-KPI-05** | KPI-17 Existencia sin movimiento | Parámetro «N días» | Incluir el parámetro en RF-PAR-001 |
| **PROP-KPI-06** | KPI-24 Adopción del sistema | Volumen estimado de movimientos totales y verificación de campo | «El sistema debe permitir registrar el volumen de movimientos de referencia estimado en campo para calcular la adopción.» (dominio PAR/REP); la verificación de campo es una actividad de la Fase 3 |

### C.2.3 Cierre operativo de jornada (H-10)

| ID | Propuesta de RF | Fuente |
|---|---|---|
| **PROP-CIE-01** | El sistema debe consolidar al cierre de la jornada los movimientos y los pendientes: recepciones sin confirmar, movimientos en tránsito, tareas de conteo abiertas, ajustes sin resolver, novedades sin atender y alertas activas | PN-14 pasos 1–2 |
| **PROP-CIE-02** | El sistema debe permitir traspasar explícitamente los pendientes al turno siguiente y registrar el cierre con quién lo ejecutó | PN-14 pasos 4–7 |
| **PROP-CIE-03** | El sistema debe impedir el cierre con registros sin sincronizar, registrar como omisión el cierre no ejecutado y alertar ante una diferencia significativa | PN-14 E-02, E-03, E-04 · RNF-DSP-003 |

## C.3 Registro de riesgos abiertos

### C.3.1 Riesgos propios de la fase del SRS

| ID | Riesgo | Prob. | Impacto | Sev. | Mitigación | Origen |
|---|---|:--:|:--:|:--:|---|---|
| **R-S01** | **El SRS se emite antes del AS-IS y de la línea base**; los requisitos no están contrastados con la operación real | Alta | Alto | 🔴 | Control de cambios sobre el baseline · taller de validación con la empresa de estudio · marcar como «sujeto a validación» todo requisito de proceso | H-16 |
| **R-S02** | Los mapeos `[SRS]` (HU↔RF, RF↔KPI, RF↔concepto, módulo↔objetivo) no han sido validados por el Director | Media | Medio | 🟠 | Revisión del Director de los Caps. 5, 6 y 9 · el SPEC permanece como fuente si hay discrepancia | Esta fase |
| **R-S03** | Alcance desproporcionado para nivel Ingeniería (corregido en la v1.2; decía «Tecnólogo»): 110 HU · 171 RF · 47 RNF · 91 RN (MVP-Completo) | Media | Alto | 🟠 | Umbral MVP-Núcleo (Cap. 12): 91 HU · 152 RF, DEC-01 = A | RG-38 |
| **R-S04** | Tensión entre alcance constitucional (DC-02) y backlog (H2) | Alta | Medio | 🟠 | DEC-01 | H-08 |
| **R-S05** | Reglas y KPI sin requisito de captura: se implementarían de forma incompleta | Media | Alto | 🟠 | DEC-05, DEC-06 | H-10, H-11, H-12 |
| **R-S06** | Circulación de dos cifras de reglas (68 y 82) | Alta | Bajo | 🟡 | DEC-03 · fe de erratas | H-01 |
| **R-S07** | Valores numéricos de RNF sin calibrar usados como umbral | Media | Medio | 🟡 | CA-12 | Pendiente #12 |
| **R-S08** | Ambigüedad «estructural / configurable» → reglas de integridad implementadas como configurables | Media | Alto | 🟠 | DEC-04 · CA-08 | H-06 |
| **R-S09** | Los escenarios Gherkin no pueden validar por sí solos la usabilidad ni la adopción | Alta | Alto | 🟠 | CA-13, CA-21…CA-26 con usuarios reales | RG-14 |
| **R-S10** | Cifras de fuentes no verificadas (RG-33, RG-34) reutilizadas por error como justificación | Media | Alto | 🟠 | El SRS no las usa como justificación cuantitativa (§2.2) | AUD E.1, E.2 |

### C.3.2 Riesgos críticos heredados del SPEC (Cap. 11) — siguen abiertos

De los 42 riesgos funcionales del SPEC (RG-01…RG-42), **11 son críticos** y se concentran en dos frentes; el SRS no los redefine:

| Frente | Riesgos críticos | Cómo se atienden en el SRS |
|---|---|---|
| **Adopción real por el personal** | RG-01 (operación fuera del sistema) · RG-02 (registro diferido) · RG-13 (rechazo por vigilancia) · RG-14 (curva de aprendizaje) · RG-16 (credenciales compartidas) · RG-17 (ocultamiento de problemas) · RG-23 (pérdida de conectividad) | Cap. 7 (usabilidad, disponibilidad) · RN-INT-001 · RN-INT-003 · CA-21…CA-26 · CA-05 · CA-29 |
| **Solidez académica de la evidencia** | RG-33 (nueve fuentes sin verificar) · RG-34 (contradicciones estadísticas) · RG-35 (el piloto puede no alcanzar las cifras) · RG-36 (sin línea base) | §2.2 · CA-16…CA-18 · §12.7 |

## C.4 Historial de hallazgos

Los hallazgos H-01…H-20 se describen con su evidencia en el §0.5-b. Su estado:

| Hallazgo | Estado | Resuelto por |
|---|---|---|
| H-01, H-09 | **Resuelto en la v1.3** | DEC-03 (a) |
| H-02, H-03, H-04, H-05, H-14 | **Tratado en el SRS** (se usa el contenido de las tablas; sin impacto funcional) | — |
| H-06 | **Resuelto en la v1.3** | DEC-04 (a) |
| H-07 | **Resuelto en la v1.3** | DEC-07 (a) |
| H-08 | **Resuelto en la v1.2** | DEC-01 = A |
| H-10 | **Resuelto en la v1.3** | DEC-05 (a) |
| H-11, H-12, H-13 | **Resuelto en la v1.3** | DEC-06 (a) |
| H-15, H-16 | Abierto: acta en borrador, sin firmar | DEC-08 (a) |
| H-17 | **Resuelto en la v1.3** | DEC-02 (a) |
| H-18 | **Resuelto en la v1.3** | DEC-09 (a) |
| H-19, H-20 | **Resuelto en la v1.4** | Respuestas (a) del 30-sep-2026 (C.12) |

## C.9 Decisiones del cierre del CP-04 (versión 1.1)

> Tomadas el 29 de septiembre de 2026 y registradas en `04_CP04_AUDITORIA/04_CP04_CIERRE.md`. No responden ninguna DEC-nn: resuelven los bloqueos de dominio que la auditoría del CP-04 encontró antes de la Fase 5.

| ID | Decisión | Reglas afectadas en este SRS | Relación con este anexo |
|---|---|---|---|
| **DF5-01** | El QR de mercancía identifica **SKU + Lote**; no identifica ubicación, bodega ni cantidad. La unidad de inventario sigue siendo SKU + Lote + Ubicación | Texto de RN-IDE-001 y RN-IDE-003 | — |
| **DF5-02** | La entrada confirmada queda **en recepción**; pasa a disponible al ubicarse | Nueva RN-EXI-007 | — |
| **DF5-03** | La primera ubicación es un **movimiento interno** en el kardex | Nueva RN-MOV-010 | Relacionada con PROP-RN-01 (la desviación de ubicación sigue sin RF propio) |
| **DF5-05** | Un registro retenido sin conectividad se **valida de nuevo** al sincronizar; si ya no es válido, se rechaza con constancia y, si describe un hecho físico, abre una novedad | Nueva RN-INT-008 | — |
| **DF5-06** (revisada) | SPEC, SRS y Modelo de Dominio v1.1 **validados técnicamente**; la aprobación funcional y académica queda pendiente | — | **DEC-01…DEC-09 siguen abiertas** y se analizan una por una en `04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md`. H-15 (DEC-08) sigue abierto |

## C.10 Decisiones del Director del 30 de septiembre de 2026 (versión 1.2)

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

**Decisiones que quedaban pendientes** (no se inventan; HD-29 y HD-30 se resolvieron en la v1.4, C.12): **HD-28** (contenedor con mezcla de lotes; diferencia entre «paquete o bolsa» y «contenedor agrupado»; motivos por los que un identificador se reemplaza ahora que la reimpresión no lo reemplaza), **HD-29** (qué ocurre con el remanente de un corte parcial si se mueve a otra ubicación; movimiento parcial de una pieza) y **HD-30** (si toda referencia se controla por piezas).

## C.11 Respuestas del Director a DEC-02…DEC-09 (versión 1.3)

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

**Pendientes (v1.3):** el acta firmada de DEC-08; H-19 y H-20; HD-28, HD-29 y HD-30 del modelo de dominio; la verificación de campo de KPI-24 (Fase 3 del roadmap). **Actualización (v1.4):** H-19, H-20, HD-29 y HD-30 se resolvieron (C.12); siguen abiertos el acta, HD-28 y KPI-24.

## C.12 Respuestas del Director a H-19, H-20, HD-29 y HD-30 (versión 1.4)

> Dadas el 30 de septiembre de 2026, en la opción (a) propuesta, tras verificarla contra las fuentes.

| Asunto | Respuesta | Efecto en este SRS |
|---|---|---|
| **H-19** | (a) Regla fija de propuesta de ubicación en el Núcleo | HU-ENT-006, RN-MOV-001; HU-BOD-005 sigue en el Horizonte 2 |
| **H-20** | (a) RF-REP-003 acotado a 12 KPI; RF nuevo para los otros 12 | RF-REP-003 · RF-REP-008 (Horizonte 2) |
| **HD-29** | (a) Una pieza no se divide | Regla nueva RN-MOV-012; HU-MOV-001 |
| **HD-30** | (a) Toda la mercancía se controla por piezas | RN-LOT-006 |

**Limitación conocida:** una parte de un paquete o bolsa no puede trasladarse a otra ubicación como movimiento interno. Se puede reabrir con el levantamiento AS-IS (Q-04).

---

**ESTADO DEL ANEXO C**

| | |
|---|---|
| **Completado** | 9 decisiones, todas con respuesta (C.10 y C.11) · 5 decisiones del cierre del CP-04 (C.9) · 6 + 6 + 3 propuestas de cierre de brechas · 10 riesgos de fase · riesgos críticos heredados |
| **Pendiente** | Acta firmada de DEC-08 · HD-28 |
| **Riesgos encontrados** | R-S01 (crítico) y los 9 restantes |
| **Dependencias** | Cap. 12 depende de DEC-01 y DEC-05 |


---

*Fin del documento SRS_COLBASOFT v1.2 — La monografía original permanece sin modificaciones.*
