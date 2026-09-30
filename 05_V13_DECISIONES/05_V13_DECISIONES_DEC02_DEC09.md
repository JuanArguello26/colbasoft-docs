# 05_V13 — Respuestas a DEC-02…DEC-09 y borrador del acta de DEC-08

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | Registro de decisiones de la versión 1.3 |
| **Fecha** | 30 de septiembre de 2026 |
| **Estado** | **Borrador.** Las respuestas están registradas; el acta de DEC-08 **no está firmada** |
| **Documentos que lo recogen** | `COLBASOFT_SPEC_v1.3.md` · `SRS_COLBASOFT_v1.3.md` (Anexo C, C.11) · `DOMAIN_MODEL.md` §0.10 |
| **Antecedentes** | `04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md` (análisis de cada decisión) · SPEC v1.2 §«Control de cambios» (DEC-01 = A) |

> **Naturaleza.** Este documento solo registra lo que el Director confirmó el 30 de septiembre de 2026: las nueve decisiones DEC tienen respuesta, todas en la opción recomendada por el SRS. No introduce decisiones nuevas.

---

# 1. Respuestas

| ID | Decisión | Respuesta | Qué se modificó |
|---|---|---|---|
| **DEC-01** | Umbral aprobatorio | **A — Núcleo, con 1 bodega piloto**, más la capa de trazabilidad por pieza (registrada en la v1.2) | SPEC, SRS y dominio v1.2 |
| **DEC-02** | Lista de alcance del MVP | **(a)** 20 módulos, incluido el dashboard M-17; exclusión de **toda** IA | Nada |
| **DEC-03** | Cifra y numeración de reglas | **(a)** El SRS es la numeración canónica; fe de erratas del SPEC | SPEC §9.17 |
| **DEC-04** | «Estructural» frente a «configurable» | **(a)** Toda regla estructural es no configurable; el Jefe lee los parámetros; el Administrador o el Jefe responden y cierran las observaciones de auditoría | SPEC §2.7, M-18, HU-096, RF-152; dominio (EV-AUD-002, SM-18) |
| **DEC-05** | Cierre de jornada (PN-14) | **(a)** Se crean las HU y RF | HU-113, HU-114; RF-182, RF-183, RF-184 |
| **DEC-06** | Brechas de trazabilidad | **(a)** Se aprueban todas las propuestas PROP-RN y PROP-KPI | RF-172…RF-181; HU-111, HU-112; RF-152 |
| **DEC-07** | Valorización | **(a)** Se retira del MVP; queda como restricción preventiva | SPEC §2.7, M-16, HU-087 |
| **DEC-08** | Aprobación formal y numeración de fases | **(a)** Acta de aprobación y tabla de equivalencia de fases | Este documento (§3 y §4): **borrador** |
| **DEC-09** | Alerta «lote próximo a vencer inmovilización» | **(a)** Se redefine sobre el umbral de antigüedad del lote | SPEC PN-11 |

## 1.1 Elementos nuevos de la v1.3

**4 historias y 13 requisitos funcionales.** Ninguna regla, entidad, invariante, evento ni término nuevos.

| Propuesta | Requisito (SPEC) | ID permanente (SRS) | Horizonte |
|---|---|---|:--:|
| PROP-RN-01 desviación de ubicación | RF-172 | RF-BOD-009 | H1 |
| PROP-RN-02 movimiento interno en tránsito | RF-173 · HU-111 | RF-MOV-013 · HU-MOV-009 | H1 |
| PROP-RN-03 mercancía sin registro | RF-174 | RF-NOV-007 | H1 |
| PROP-RN-04 diferencia crítica del conteo general | RF-175 · HU-112 | RF-CNT-015 · HU-CNT-011 | **H2** |
| PROP-RN-05 reserva vencida | RF-176 | RF-SAL-014 | H1 |
| PROP-RN-06 novedad vencida | RF-177 | RF-NOV-008 | H1 |
| PROP-KPI-01 KPI-05 inicio y confirmación | RF-178 | RF-KDX-009 | H1 |
| PROP-KPI-02 KPI-07 modo de identificación | RF-179 | RF-QRC-009 | H1 |
| PROP-KPI-04 KPI-12 llegada de la mercancía | RF-180 | RF-ENT-017 | H1 |
| PROP-KPI-06 KPI-24 volumen de referencia | RF-181 | RF-PAR-007 | H1 |
| PROP-CIE-01, 02 | RF-182, RF-183 · HU-113 | RF-TAR-006, RF-TAR-007 · HU-TAR-004 | H1 |
| PROP-CIE-03 | RF-184 · HU-114 | RF-TAR-008 · HU-TAR-005 | H1 |
| PROP-KPI-03 (KPI-10), PROP-KPI-05 (KPI-17) | Se cubren con RF-172 y con dos parámetros nuevos en RF-152 | RF-BOD-009 · RF-PAR-001 | H1 |

La diferencia crítica del conteo general (RF-175, HU-112) queda en el Horizonte 2, con el resto del conteo general.

## 1.2 Cifras

| | v1.2 | **v1.3** |
|---|:--:|:--:|
| Historias | 110 | **114** |
| Requisitos funcionales | 171 | **184** |
| Escenarios Gherkin | 498 | **515** |
| Núcleo (umbral aprobatorio) | 91 HU · 152 RF | **94 HU · 164 RF** |
| Completo | 110 HU · 171 RF | **114 HU · 184 RF** |
| Horizonte 2 | 19 HU · 19 RF | **20 HU · 20 RF** |
| Reglas | 91 | 91 |

# 2. Lo que sigue abierto

| Asunto | Qué falta |
|---|---|
| **DEC-08** | Acta firmada (§3) |
| **HD-28, HD-29, HD-30** | Decisiones del modelo de dominio sobre la pieza (identidad física, contenedores y reemplazo de QR; corte parcial; alcance del control por pieza) |
| **H-19, H-20** | HU-ENT-006 remite a HU-BOD-005 (Horizonte 2); RF-REP-003 calcula los 24 KPI aunque KPI-02 exige conteo general (Horizonte 2) |
| **KPI-24** | Verificación de campo (actividad de la Fase 3 del roadmap) |
| Asuntos de SPEC §13.6 | PYME, sector y municipios, autorización de contacto con empresas, línea base, fuentes no verificadas, reproyección del horizonte |

# 3. Borrador del acta de aprobación (DEC-08)

> **Este texto es un borrador. No está firmado ni aprueba nada.** Solo adquiere efecto cuando lo firme quien corresponda. No se debe escribir «Aprobado» en ningún documento del proyecto hasta entonces.

**ACTA DE APROBACIÓN DE LA BASE DOCUMENTAL COLBASOFT**

Fecha: ____ de ____________ de 2026
Lugar: ______________________

**Documentos que se aprueban** (versión vigente al momento de la firma):

| Documento | Versión | Fecha |
|---|---|---|
| `COLBASOFT_SPEC` | 1.3 | 30-sep-2026 |
| `SRS_COLBASOFT` | 1.3 | 30-sep-2026 |
| `DOMAIN_MODEL`, `EVENT_CATALOG`, `GLOSSARY` | 1.3 | 30-sep-2026 |

**Constancia.** El Director del Proyecto declara que:

1. Ha respondido las decisiones DEC-01 a DEC-09 del Anexo C del SRS, en los términos del §1 del registro `05_V13_DECISIONES_DEC02_DEC09.md`.
2. Aprueba el **Núcleo (Horizonte 1)**, con **1 bodega piloto**, como umbral aprobatorio del MVP (DEC-01 = A), con la capa de trazabilidad por pieza.
3. Acepta por escrito, como limitaciones conocidas, los asuntos abiertos del §2 del registro, **uno por uno**: DEC-08 (esta acta), HD-28, HD-29, HD-30, H-19, H-20 y la verificación de campo de KPI-24. [ ] Acepta / [ ] No acepta (tachar lo que no aplique, por asunto)
4. Reconoce que los requisitos son un modelo **TO-BE** no contrastado con la operación real de la empresa piloto (riesgo R-S01) y que el levantamiento AS-IS sigue pendiente.
5. Adopta la **tabla de equivalencia de fases** del §4.

Firma del Director del Proyecto: ______________________   Nombre: ______________________
Firma del asesor académico: ______________________   Nombre: ______________________

# 4. Borrador de la tabla de equivalencia de fases

> La equivalencia de las fases 0 a 3 sale del SRS (Cap. 0, §0.4). Las filas de las fases 4 y 5 del proyecto son **una propuesta de este borrador**: el roadmap de la Auditoría no las nombra y deben confirmarse al firmar.

| Fase del proyecto | Producto | Fase equivalente del roadmap de la Auditoría (Fase D) | Estado |
|---|---|---|---|
| **0** | Auditoría Fundacional | 0 — Auditoría Fundacional | Cerrada |
| **1** | Constitución (DC-01…DC-08) | 1 — Resolución de ambigüedades y autorización de alcance | Cerrada parcialmente: persisten preguntas bloqueantes (SPEC §13.6) |
| **2** | `COLBASOFT_SPEC` | Materializa vacíos de la Auditoría y cubre la **Ingeniería de requisitos (4)** | Borrador v1.3 |
| **3** | `SRS_COLBASOFT` | Formaliza el entregable de la **Ingeniería de requisitos (4)** | Borrador v1.3 |
| **4** | Modelo de dominio | Insumo de **5 — Diseño** (propuesta) | Borrador v1.3 |
| **5** | Arquitectura y modelo de datos | **5 — Diseño** (propuesta) | No iniciada |
| — | *Sin fase de proyecto* | 2 — Saneamiento académico · 3 — Levantamiento AS-IS y línea base | **Pendientes**: sin ellas el SRS y el dominio son TO-BE (R-S01) |
| — | *Sin fase de proyecto* | 6 — Construcción · 7 — Validación · 8 — Integración | Posteriores a la Fase 5 |

**Advertencia de dependencia (H-16).** El roadmap exige que cada fase tenga cerrados los entregables de su antecesora. El SRS se emitió por instrucción expresa del Director sin haber cerrado las fases 2 y 3 del roadmap. Esta tabla no subsana esa dependencia: la deja documentada.

---

*Fin del registro de decisiones de la versión 1.3. La monografía original permanece sin modificaciones.*
