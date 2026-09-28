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
| **Trazabilidad** | HU: @HU071 @HU072 @HU073 @HU074 @HU075 @HU076 · RF: @RF112 @RF113 @RF114 @RF115 @RF116 @RF117 @RF118 @RF119 · RN: @RN065 @RN067 @RN025 @RN031 @RN032 @RN036 @RN066 |

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
| **Trazabilidad** | HU: @HU045 @HU046 · RF: @RF072 @RF073 @RF074 @RF075 @RF076 @RF077 · RN: @RN026 @RN025 @RN027 @RN021 @RN036 @RN028 @RN054 |

**Flujo principal**
1. El Auxiliar escanea el identificador de la mercancía.
2. El sistema muestra su ubicación actual y su existencia.
3. El Auxiliar indica la cantidad a mover (total o parcial).
4. El Auxiliar traslada físicamente la mercancía y escanea el identificador de la ubicación destino.
5. El sistema valida la ubicación destino.
6. El sistema registra el movimiento interno en el kardex, descuenta de la ubicación origen y suma a la destino.
7. La existencia total no cambia; el sistema confirma visualmente el registro.

**Flujos alternos**
- **A1 · Movimiento interrumpido a mitad de camino:** queda **En tránsito**; la existencia no está disponible en origen ni en destino hasta cerrarlo y el sistema alerta si supera el tiempo configurado.
- **A2 · Sin conectividad:** el registro se retiene localmente y se sincroniza al restablecerse.

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
| **Trazabilidad** | HU: @HU047 @HU048 @HU049 @HU050 @HU051 · RF: @RF078 @RF079 @RF080 @RF081 @RF082 · RN: @RN031 @RN032 @RN033 @RN034 @RN035 @RN025 · KPI: KPI-15 |

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
| **Trazabilidad** | HU: @HU052 @HU053 @HU054 @HU055 @HU056 @HU057 @HU102 · RF: @RF083 @RF084 @RF085 @RF086 @RF087 @RF088 @RF089 @RF090 @RF091 @RF092 · RN: @RN023 @RN024 @RN029 @RN009 @RN036 @RN037 @RN038 @RN062 @RN070 · KPI: KPI-08 KPI-14 KPI-22 |

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
| **Trazabilidad** | HU: @HU058 @HU059 @HU060 @HU061 @HU062 @HU065 @HU066 · RF: @RF093 @RF094 @RF095 @RF096 @RF097 @RF098 @RF099 @RF100 @RF101 @RF102 @RF105 · RN: @RN039 @RN040 @RN041 @RN042 @RN043 @RN044 @RN029 · KPI: KPI-01 KPI-03 KPI-04 KPI-06 |

**Flujo principal**
1. El Coordinador programa el conteo definiendo su ámbito (ubicaciones, referencias o categorías).
2. El sistema genera las tareas de conteo, las asigna a auxiliares y congela la existencia teórica del ámbito.
3. El Auxiliar recibe sus tareas en la tablet, escanea la ubicación y cuenta físicamente.
4. El Auxiliar registra la cantidad contada; el sistema no le muestra la cantidad esperada, ni antes ni después.
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
| **Trazabilidad** | HU: @HU063 @HU064 @HU062 @HU065 · RF: @RF103 @RF104 @RF095 @RF096 @RF098 @RF100 @RF101 @RF102 @RF105 · RN: @RN045 @RN046 @RN047 @RN039 @RN040 @RN041 @RN042 · KPI: KPI-02 KPI-03 |

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
| **Trazabilidad** | HU: @HU038 @HU039 @HU040 @HU041 @HU042 @HU043 @HU044 · RF: @RF061 @RF062 @RF063 @RF064 @RF065 @RF066 @RF067 @RF068 @RF069 @RF070 @RF071 · RN: @RN048 @RN025 @RN031 @RN030 @RN049 @RN050 @RN009 @RN036 @RN051 @RN052 @RN053 · KPI: KPI-11 KPI-13 KPI-16 |

> **Frontera de alcance `[DC-03]`.** El sistema registra la salida física del inventario. No gestiona el pedido de venta, la factura, el documento de despacho comercial ni la orden de producción que la originan; recibe un motivo tipificado y actúa sobre el inventario, nada más.

**Flujo principal**
1. Se solicita la salida indicando referencias, cantidades y motivo tipificado.
2. El sistema verifica la existencia disponible.
3. El Jefe autoriza la salida, o el Coordinador si está dentro de su umbral; el sistema reserva la existencia.
4. El sistema genera la tarea de preparación y la asigna a un Auxiliar, indicando las ubicaciones de toma según la política configurada.
5. El Auxiliar escanea cada unidad al tomarla; el sistema valida que lo escaneado corresponda a lo solicitado.
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
| **Trazabilidad** | HU: @HU082 @HU083 @HU084 @HU085 @HU086 · RF: @RF127 @RF128 @RF129 @RF130 @RF131 @RF132 @RF133 · RN: @RN055 @RN056 @RN057 @RN058 @RN075 · KPI: KPI-19 KPI-20 KPI-21 |

**Flujo principal**
1. El sistema evalúa continuamente las condiciones de alerta configuradas (solo por reglas y umbrales; sin modelos predictivos).
2. Al cumplirse una condición, el sistema genera la alerta con su severidad.
3. El sistema la dirige al rol responsable según su tipo.
4. El destinatario la visualiza en su panel y recibe notificación si aplica.
5. El destinatario ejecuta la acción correctiva o la descarta con motivo.
6. El sistema registra la atención: quién, cuándo y qué se hizo.
7. Si la condición desaparece, el sistema cierra la alerta automáticamente.

**Tipos de alerta del MVP** (@RF130): ruptura de stock inminente · sobre stock · existencia en cero · lote próximo a vencer inmovilización · movimiento en tránsito prolongado · ajustes recurrentes · exactitud por debajo del objetivo · conteo vencido · ubicación sobreocupada · solicitud de ajuste sin resolver.

**Flujos alternos**
- **A1 · Recalibración de umbrales:** el sistema reporta al Administrador los tipos con frecuencia de disparo anómala.
- **A2 · Zona o rol sin destinatario activo:** la alerta escala al superior.

**Excepciones**
- **E1 · Condición repetida:** se agrupa; no se generan duplicados de una condición vigente.
- **E2 · Descarte sin motivo:** el sistema lo exige y no permite cerrar sin él.
- **E3 · Alerta crítica sin atender en plazo:** escala automáticamente al rol superior con notificación adicional.
- **E4 · Condición cesa antes de atenderse:** se cierra automáticamente y queda en el historial como no atendida.
