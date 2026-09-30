# SRS_COLBASOFT v1.1
## Especificación de Requisitos de Software (Software Requirements Specification)

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | SRS_COLBASOFT |
| **Versión** | 1.1 |
| **Fase** | Fase 3 del proyecto — Especificación de Requisitos de Software (SRS) |
| **Fecha** | 28 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) |
| **Estado** | **Validado técnicamente** (cierre del CP-04, 29-sep-2026). **Aprobación funcional y académica pendiente**: HD-25 y DEC-01…DEC-09 sin responder (`04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md`) |
| **Versión anterior** | `SRS_COLBASOFT_v1.0.md` (28-sep-2026), conservada sin cambios |
| **Norma de referencia** | ISO/IEC/IEEE 29148 (Ingeniería de requisitos), adaptada al proyecto y en español |
| **Jerarquía documental** | Monografía → Auditoría Fundacional → COLBASOFT_SPEC v1.1 → **SRS v1.1** |
| **Fuente de verdad** | `MONOGRAFÍA  COLBASOFT.docx` (íntegra, sin modificación) |
| **Documentos antecesores** | `AUDITORIA_FUNDACIONAL_COLBASOFT.md` (Fase 0) · `COLBASOFT_SPEC_v1.1.md` (Fase 2, revisado en el cierre del CP-04) |
| **Autoría del proyecto** | Juan Esteban Argüello · Brayan Alexander Osorio · Brandon José Guerrero |
| **Institución / asesor** | Escuela de Ingeniería — CIAF · Edwin Andrés Cabrera Arredondo |
| **Alcance de este documento** | Requisitos funcionales, no funcionales, reglas de negocio, casos de uso, historias normalizadas, trazabilidad y criterios de aceptación |
| **Fuera de alcance de este documento** | Código · Base de datos · Arquitectura técnica · ERD/UML · Endpoints/APIs · Frameworks · Tecnologías |

> **Naturaleza del documento.** Este SRS **no crea requisitos nuevos**: normaliza, reorganiza y hace trazable el contenido aprobado del COLBASOFT_SPEC v1.1. Aporta identificadores permanentes, prioridad MoSCoW, criterios en Gherkin, casos de uso completos, matrices de trazabilidad y criterios de aceptación del MVP. Todo elemento que este documento deriva (y que el SPEC no traía) se marca con la etiqueta `[SRS]` y se somete a validación del Director. Las brechas que se detectan **se registran como hallazgos y decisiones pendientes; no se resuelven inventando funcionalidad** (Regla Innegociable 3).

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
| **5** | Historias de Usuario Normalizadas | 103 historias · ID estable · MoSCoW · dependencias · Gherkin |
| **6** | Requisitos Funcionales Normalizados | 162 RF con ID permanente |
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
| **Completado** | Inventario de documentos y versiones · decisiones constitucionales · fases · pendientes · 18 hallazgos de reconstrucción |
| **Pendiente** | Resolución de los hallazgos H-01…H-18 (decisiones DEC-01…DEC-09 del Anexo C) |
| **Riesgos encontrados** | R-S01 (SRS anterior a AS-IS y línea base) · H-08 (tensión MVP/backlog) · H-10 (PN-14 sin requisitos) · H-11/H-12 (brechas de trazabilidad) |
| **Dependencias** | Decisión del Director sobre DEC-01 (alcance de entrega) condiciona el Cap. 12 |
