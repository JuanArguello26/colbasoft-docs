
---

# ANEXO C — HALLAZGOS, DECISIONES Y RIESGOS ABIERTOS

> Este anexo **no modifica el baseline de requisitos**. Reúne lo que el Director debe decidir y lo que puede afectar el resultado. Toda «propuesta» aquí descrita **no forma parte del SRS** hasta que el Director la apruebe (Regla Innegociable 3).

## C.1 Decisiones que se solicitan al Director

| ID | Decisión requerida | Hallazgos | Opciones | Recomendación del SRS | Efecto de no decidir |
|---|---|---|---|---|---|
| **DEC-01** | **Umbral de entrega aprobatorio.** ¿El MVP aprobatorio es el Núcleo (H1) o el Completo (H1+H2)? ¿Transferencias y conteo general entran al MVP? | H-08 · S-15 | (a) Núcleo: 84 HU / 143 RF; transferencias y conteo general pasan a v1.1. (b) Completo: 103 HU / 162 RF. (c) Núcleo + transferencias + conteo general | Mantener **alcance = Completo** (respeta DC-02 y el Prompt #003), con **entrega secuenciada H1 → H2** y **umbral mínimo aprobatorio = Núcleo** | El Cap. 12 conserva dos umbrales y no puede fijar el criterio de cierre |
| **DEC-02** | **Lista de alcance del MVP.** Confirmar que «usuarios» y «auditoría» son los módulos M-02 y M-18 y que el **dashboard operativo (M-17)** permanece en el MVP; y que la exclusión es **toda** IA (DC-07) y no solo la generativa | H-17 | (a) Mantener los 20 módulos y la redacción de DC-07. (b) Restringir el MVP a la lista del Prompt #003 (retira M-17: 3 HU, 4 RF) | (a) | Se mantiene el SPEC por defecto |
| **DEC-03** | **Reglas de negocio: cifra y renumeración.** El SPEC declara 68; las tablas contienen 82 (60 estructurales + 22 configurables). Confirmar las 82, retirar los marcadores vacíos `RN-069*` y `RN-026b*` y adoptar como canónica la numeración `RN-<DOM>-nnn` | H-01 · H-09 · pendiente #11 | (a) Aceptar el SRS como renumeración canónica y emitir una fe de erratas del SPEC. (b) Mantener la numeración del SPEC | (a) | Persisten dos cifras en circulación (68 y 82) |
| **DEC-04** | **Semántica «estructural» vs «configurable».** Confirmar que toda regla estructural es no configurable (no solo las 10 de §9.1); definir si el Jefe puede **leer** parámetros y **quién** responde y cierra las observaciones de auditoría (@RN064) | H-06 · Cap. 10 nota 4 | (a) Toda estructural no configurable; Jefe lee parámetros; el Administrador o el Jefe responden. (b) Otra | (a) | Riesgo de que se implementen como configurables reglas que protegen la integridad (R-S08) |
| **DEC-05** | **Cierre operativo de jornada (PN-14).** ¿Se crean HU y RF? | H-10 | (a) Crear HU/RF (ver propuestas PROP-CIE). (b) Mover PN-14 a v1.1. (c) Excluirlo del MVP | (a), porque el backlog lo declara MVP (elemento 39) y RG-03 y RG-08 dependen de él | CU-19 queda sin requisitos y sin criterio de aceptación |
| **DEC-06** | **Cierre de brechas de trazabilidad.** Aprobar o descartar las propuestas PROP-RN (reglas sin RF) y PROP-KPI (KPI sin dato de origen) | H-11 · H-12 · H-13 | (a) Aprobar todas. (b) Aprobar solo las de KPI-01/05/08. (c) Descartar | (a); como mínimo (b), porque KPI-05 es uno de los tres indicadores del compromiso | El sistema no implementará reglas ni capturará datos que hoy nadie exige |
| **DEC-07** | **«Valorización».** Definir si el permiso «consultar valorización» se retira del MVP o si se define una política de costeo | H-07 · Horizonte 3 | (a) Retirar del MVP (queda como restricción preventiva). (b) Definir política de costeo (roza DC-03) | (a) | Permiso sin dato de origen (RF-INV-005, RF-DSH-003, HU-REP-001 crit. 5) |
| **DEC-08** | **Aprobación formal del SPEC v1.0 y numeración de fases.** Confirmar por escrito la aprobación del SPEC (el archivo dice «Emitido para revisión») y la equivalencia entre las fases del proyecto y las del roadmap | H-15 · H-16 | (a) Acta de aprobación + tabla de equivalencia de fases. (b) Otra | (a) | Ambigüedad sobre qué versión rige |
| **DEC-09** | **Alerta «lote próximo a vencer inmovilización».** El SPEC la enuncia con «fecha límite» de lote, dato que no existe en CD-06 ni en ningún RF | H-18 | (a) Redefinirla sobre el umbral de antigüedad (@RN074). (b) Agregar «fecha límite» al lote (funcionalidad nueva `[NUEVO]`) | (a) | Alerta sin condición de disparo definida |

Además siguen abiertas las **preguntas heredadas** del §0.5 (A-03, A-04, A-05, V-01, V-03, V-06, I-03, I-04, I-05, I-09, S-15).

## C.2 Propuestas de cierre de brechas (NO incorporadas al baseline)

### C.2.1 Reglas de negocio sin requisito funcional que las implemente (H-11)

| ID | Regla | Comportamiento sin RF | Origen del comportamiento | Propuesta de RF (texto sugerido) |
|---|---|---|---|---|
| **PROP-RN-01** | @RN022 (desviación de ubicación) | Registrar la desviación cuando el Auxiliar ubica en un lugar distinto al propuesto, como información y no como falta | PN-03 E-02 · HU-ENT-006 crit. 3 | «El sistema debe registrar como información operativa la desviación entre la ubicación propuesta y la confirmada y notificar al Coordinador, sin imputarla al Auxiliar.» (dominio BOD o ENT) |
| **PROP-RN-02** | @RN028 (movimiento interno en tránsito) | Un movimiento interno interrumpido queda en tránsito, no disponible en origen ni destino, con alerta al exceder el tiempo | PN-05 E-05 | «El sistema debe mantener en tránsito un movimiento interno interrumpido y generar alerta al superar el tiempo máximo configurado.» (dominio MOV). *Tampoco tiene HU* |
| **PROP-RN-03** | @RN043 (mercancía sin registro) | No se cuenta ni se usa hasta ser identificada; se incorpora por ajuste por sobrante con aprobación del Jefe | PN-08 E-04 · PN-09 E-06 · PN-12 E-05 | «El sistema debe impedir contar o usar mercancía sin registro hasta su identificación y permitir su incorporación solo mediante ajuste por sobrante con motivo tipificado y aprobación del Jefe.» (dominio NOV). Complementa HU-NOV-004 |
| **PROP-RN-04** | @RN047 (diferencia crítica en conteo general) | Notificar al Administrador y al Auditor antes de permitir el cierre si la diferencia global supera el umbral crítico | PN-09 E-05 | «El sistema debe notificar al Administrador y al Auditor y condicionar el cierre de un conteo general cuando la diferencia global supere el umbral crítico configurado.» (dominio CNT; incluir el umbral crítico en RF-PAR-001). *Tampoco tiene HU* |
| **PROP-RN-05** | @RN051 (reserva vencida) | Liberar automáticamente una reserva no ejecutada en su plazo y alertar al solicitante | PN-10 E-05 · HU-SAL-002 crit. 4 | «El sistema debe liberar automáticamente la reserva no ejecutada dentro del plazo configurado y alertar al solicitante.» (dominio SAL) |
| **PROP-RN-06** | @RN059 (novedad vencida) | Escalar al Jefe la novedad sin resolver en el plazo configurado y generar alerta | PN-12 E-01 · HU-NOV-003 | «El sistema debe escalar al Jefe y alertar las novedades no resueltas dentro del plazo configurado.» (dominio NOV) |

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
| **R-S03** | Alcance desproporcionado para nivel Tecnólogo: 103 HU · 162 RF · 47 RNF · 82 RN | Media | Alto | 🟠 | Umbral MVP-Núcleo (Cap. 12) · decisión DEC-01 | RG-38 |
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
| **Adopción real por el personal** | RG-01 (operación fuera del sistema) · RG-02 (registro diferido) · RG-13 (rechazo por vigilancia) · RG-14 (curva de aprendizaje) · RG-16 (credenciales compartidas) · RG-17 (ocultamiento de problemas) · RG-23 (pérdida de conectividad) | Cap. 7 (usabilidad, disponibilidad) · @RN001 · @RN054 · CA-21…CA-26 · CA-05 · CA-29 |
| **Solidez académica de la evidencia** | RG-33 (nueve fuentes sin verificar) · RG-34 (contradicciones estadísticas) · RG-35 (el piloto puede no alcanzar las cifras) · RG-36 (sin línea base) | §2.2 · CA-16…CA-18 · §12.7 |

## C.4 Historial de hallazgos

Los hallazgos H-01…H-18 se describen con su evidencia en el §0.5-b. Su estado:

| Hallazgo | Estado | Resuelto por |
|---|---|---|
| H-01, H-09 | Abierto | DEC-03 |
| H-02, H-03, H-04, H-05, H-14 | **Tratado en el SRS** (se usa el contenido de las tablas; sin impacto funcional) | — |
| H-06 | Abierto | DEC-04 |
| H-07 | Abierto | DEC-07 |
| H-08 | Abierto | DEC-01 |
| H-10 | Abierto | DEC-05 |
| H-11, H-12, H-13 | Abierto | DEC-06 |
| H-15, H-16 | Abierto | DEC-08 |
| H-17 | Abierto | DEC-02 |
| H-18 | Abierto | DEC-09 |

## C.9 Decisiones del cierre del CP-04 (versión 1.1)

> Tomadas el 29 de septiembre de 2026 y registradas en `04_CP04_AUDITORIA/04_CP04_CIERRE.md`. No responden ninguna DEC-nn: resuelven los bloqueos de dominio que la auditoría del CP-04 encontró antes de la Fase 5.

| ID | Decisión | Reglas afectadas en este SRS | Relación con este anexo |
|---|---|---|---|
| **DF5-01** | El QR de mercancía identifica **SKU + Lote**; no identifica ubicación, bodega ni cantidad. La unidad de inventario sigue siendo SKU + Lote + Ubicación | Texto de @RN015 y @RN017 | — |
| **DF5-02** | La entrada confirmada queda **en recepción**; pasa a disponible al ubicarse | Nueva @RN081 | — |
| **DF5-03** | La primera ubicación es un **movimiento interno** en el kardex | Nueva @RN082 | Relacionada con PROP-RN-01 (la desviación de ubicación sigue sin RF propio) |
| **DF5-05** | Un registro retenido sin conectividad se **valida de nuevo** al sincronizar; si ya no es válido, se rechaza con constancia y, si describe un hecho físico, abre una novedad | Nueva @RN083 | — |
| **DF5-06** (revisada) | SPEC, SRS y Modelo de Dominio v1.1 **validados técnicamente**; la aprobación funcional y académica queda pendiente | — | **DEC-01…DEC-09 siguen abiertas** y se analizan una por una en `04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md`. H-15 (DEC-08) sigue abierto |

---

**ESTADO DEL ANEXO C**

| | |
|---|---|
| **Completado** | 9 decisiones · 5 decisiones del cierre del CP-04 (C.9) · 6 + 6 + 3 propuestas de cierre de brechas · 10 riesgos de fase · riesgos críticos heredados |
| **Pendiente** | Respuesta del Director a DEC-01…DEC-09 |
| **Riesgos encontrados** | R-S01 (crítico) y los 9 restantes |
| **Dependencias** | Cap. 12 depende de DEC-01 y DEC-05 |
