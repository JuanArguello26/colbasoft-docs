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
| **Trazabilidad** | HU: @HU067 @HU068 @HU069 @HU070 · RF: @RF106 @RF107 @RF108 @RF109 @RF110 @RF111 · RN: @RN043 @RN059 @RN060 @RN063 · KPI: KPI-23 |

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
| **Trazabilidad** | HU: @HU077 @HU078 @HU079 @HU094 @HU095 @HU096 @HU097 @HU057 @HU075 · RF: @RF125 @RF145 @RF146 @RF147 @RF148 @RF149 @RF150 @RF151 · RN: @RN065 @RN080 @RN061 @RN064 @RN023 @RN012 · KPI: KPI-09 KPI-14 |

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
| **Trazabilidad** | HU: **ninguna** · RF: **ninguno** (ver nota) · RN: @RN054 @RN028 · RNF: @RNF010 @RNF011 · RG: RG-03, RG-08 |

> **Nota de trazabilidad — hallazgo H-10.** El SPEC modela PN-14 (§3) y lo incluye en el backlog del MVP (elemento 39, §12.2), pero **no le asigna ninguna historia de usuario ni requisito funcional**; solo la regla @RN054 y el requisito @RNF011 lo afectan indirectamente. Este caso de uso se documenta desde el proceso del SPEC y queda marcado como **requisitos pendientes de definición** hasta que el Director decida (ver Anexo C, decisión DEC-05).

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
| **Trazabilidad** | HU: @HU016 @HU017 @HU018 @HU019 @HU080 · RF: @RF026 @RF027 @RF028 @RF029 @RF030 @RF031 · RN: @RN071 @RN072 @RN036b @RN073 @RN074 @RN014 |

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
| **Trazabilidad** | HU: @HU077 @HU078 @HU079 @HU080 @HU081 @HU110 · RF: @RF120 @RF121 @RF122 @RF123 @RF124 @RF125 @RF126 @RF170 · RN: @RN012 @RN001 @RN065 @RN070 @RN085 · KPI: KPI-05 KPI-09 KPI-11 KPI-17 KPI-24 |

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
| **Trazabilidad** | HU: @HU087 @HU088 @HU089 @HU090 @HU065 · RF: @RF134 @RF135 @RF136 @RF137 @RF138 @RF139 @RF140 · RN: @RN078 @RN061 · KPI: KPI-01 a KPI-24 |

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
| **Trazabilidad** | HU: @HU091 @HU092 @HU093 @HU101 · RF: @RF141 @RF142 @RF143 @RF144 @RF158 @RF159 @RF160 · RN: @RN067 · KPI: KPI-01 |

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
| **Trazabilidad** | HU: @HU101 @HU102 @HU103 @HU066 · RF: @RF158 @RF159 @RF160 @RF161 @RF162 · RN: @RN038 @RN056 @RN059 @RN041 @RN001 |

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
