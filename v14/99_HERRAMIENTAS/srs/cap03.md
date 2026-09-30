
---

# CAPÍTULO 3 — ACTORES

`[DC-04]` COLBASOFT reconoce **cinco roles oficiales** más el **Sistema** como actor de acciones automáticas. No se admiten roles adicionales. Toda función es ejecutable por al menos un rol y ninguna queda sin responsable.

## 3.1 Principios que gobiernan los roles

| # | Principio | Consecuencia funcional |
|---|---|---|
| PR-01 | **Segregación de funciones:** quien registra no es necesariamente quien autoriza | @RN057b · @RN023 · @RN041 |
| PR-02 | **El Auditor nunca escribe** en el inventario | @RF149 · @RN064 |
| PR-03 | **Escalada de privilegio explícita:** un rol superior puede hacer lo que hace el inferior, salvo donde la segregación lo prohíba | Cap. 3.5 |
| PR-04 | **El Auxiliar no ve información sensible** de negocio | @RF116 · @RF126 |
| PR-05 | **Toda acción queda atribuida** a una persona identificada; no hay cuentas compartidas | @RN001 · @RF002 |
| PR-06 | **El rol no castiga: registra.** El operario no ve rankings ni indicadores de error personal | @RF108 · @RF144 · @RNF039 |

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
| **No puede** | Editar ni eliminar un movimiento confirmado (@RN012) · alterar la bitácora (@RN061) · aprobar su propia solicitud (@RN023) · desactivarse a sí mismo si es el único activo (@RN011) |
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
| **No puede** | Gestionar usuarios y roles · modificar la estructura de la bodega · configurar parámetros globales · aprobar ajustes mayores (escalan al Administrador, @RN024) · alterar la bitácora |

### ACT-03 · Coordinador de Bodega (ROL-03)

| Campo | Contenido |
|---|---|
| **Perfil típico** | Mando medio que supervisa a los auxiliares en piso |
| **Frecuencia / dispositivo / nivel digital** | Muy alta · Tablet en piso · Medio-bajo |
| **Objetivos** | Que el trabajo del turno quede registrado sin pendientes · que la mercancía esté donde el sistema dice · que su equipo no repita trabajo |
| **Dolor principal** | *«Recibimos mercancía, la ubicamos y la movemos todo el día; para cuando llega la hora de anotar, ya nadie recuerda con exactitud qué pasó.»* `[MON §3]` |
| **Responsabilidades** | Supervisar entradas, salidas y transferencias · verificar lo recibido contra el documento de entrada · asignar ubicaciones · ejecutar y supervisar conteos cíclicos · solicitar ajustes · capacitar a los auxiliares |
| **Casos de uso principales** | CU-06, CU-07, CU-08, CU-11, CU-12 (solicita), CU-13, CU-15 (dentro de umbral), CU-17, CU-23 (su zona), CU-24 |
| **No puede** | Aprobar sus propios ajustes (@RN023) · cerrar conteos (@RN042) · modificar la estructura de bodega · configurar umbrales · ver reportes de desempeño individual (PR-06) · alterar la bitácora |

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
| **Restricción absoluta** | **No escribe nada en el inventario**; su única escritura son las observaciones de auditoría, en un registro separado (@RN064) |
| **Lectura** | El Auditor lee todo (@RF148) |

### ACT-06 · Sistema (actor de acciones automáticas)

| Campo | Contenido |
|---|---|
| **Naturaleza** | Actor explícito para toda acción sin persona: cierre automático de alertas, escalamientos, liberación de reservas vencidas, generación de tareas, congelamiento de existencia teórica, cálculo de KPI `[RN-INT-001]` |
| **Regla** | Las acciones del Sistema se atribuyen al **Sistema**, nunca a un usuario (@RN001) |

### ACT-07 · Herramienta analítica externa (actor de sistema externo)

| Campo | Contenido |
|---|---|
| **Naturaleza** | Consumidor de datos estructurados expuestos por el sistema `[DC-06]` |
| **Restricción** | Los datos exportados respetan la visibilidad por rol (HU-REP-003, criterio C5); su habilitación es exclusiva del Administrador |

### Historias en las que participa cada rol `[SRS]`

{{HU_POR_ROL}}

## 3.3 Matriz de permisos funcional

Leyenda: **✅** permitido · **⚠️** permitido con restricción o aprobación · **❌** denegado. Transcribe la matriz de segregación del SPEC (§2.7) y le agrega el caso de uso y la regla que gobierna cada restricción `[SRS]`.

| Función | Admin | Jefe | Coord. | Aux. | Auditor | CU | Regla / restricción |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| Iniciar sesión | ✅ | ✅ | ✅ | ✅ | ✅ | CU-01 | @RN001 |
| Crear y desactivar usuarios | ✅ | ❌ | ❌ | ❌ | ❌ | CU-02 | @RN063 · @RN011 |
| Asignar roles | ✅ | ❌ | ❌ | ❌ | ❌ | CU-02 | Solo los 5 roles oficiales |
| Crear y editar referencias del catálogo | ✅ | ✅ | ❌ | ❌ | ❌ | CU-03 | @RN002 |
| Definir zonas y ubicaciones | ✅ | ❌ | ❌ | ❌ | ❌ | CU-04 | @RN014 |
| Generar identificador QR | ✅ | ✅ | ✅ | ❌ | ❌ | CU-07 | @RN016 |
| Reimprimir identificador QR | ✅ | ✅ | ✅ | ⚠️ | ❌ | CU-07 | ⚠️ Aux.: solo por deterioro, con motivo (@RN018) |
| Crear documento de entrada | ✅ | ✅ | ✅ | ❌ | ❌ | CU-06 | @RN003 |
| Registrar recepción física | ✅ | ✅ | ✅ | ✅ | ❌ | CU-06 | @RN057b |
| Confirmar entrada al inventario | ✅ | ✅ | ✅ | ❌ | ❌ | CU-06 | @RN057b: quien recibe no confirma |
| Asignar ubicación | ✅ | ✅ | ✅ | ⚠️ | ❌ | CU-08 | ⚠️ Aux.: solo confirma la propuesta (@RN020) |
| Autorizar salida | ✅ | ✅ | ⚠️ | ❌ | ❌ | CU-15 | ⚠️ Coord.: hasta su umbral (@RN030) |
| Registrar salida autorizada | ✅ | ✅ | ✅ | ✅ | ❌ | CU-15 | @RN050 |
| Crear transferencia interna | ✅ | ✅ | ✅ | ❌ | ❌ | CU-11 | @RN031 |
| Ejecutar transferencia asignada | ✅ | ✅ | ✅ | ✅ | ❌ | CU-11 | @RN033 |
| Solicitar ajuste | ✅ | ✅ | ✅ | ❌ | ❌ | CU-12 | @RN029 |
| Aprobar ajuste menor | ✅ | ✅ | ❌ | ❌ | ❌ | CU-12 | @RN023: nunca el propio (Admin/Jefe) |
| Aprobar ajuste mayor | ✅ | ❌ | ❌ | ❌ | ❌ | CU-12 | @RN024 · @RN036 |
| Programar conteo cíclico | ✅ | ✅ | ✅ | ❌ | ❌ | CU-13 | — |
| Programar conteo general | ✅ | ✅ | ❌ | ❌ | ❌ | CU-14 | @RN045 |
| Registrar conteo físico | ✅ | ✅ | ✅ | ✅ | ❌ | CU-13 / CU-14 | @RN040 · @RN041 |
| Cerrar conteo y aplicar diferencias | ✅ | ✅ | ❌ | ❌ | ❌ | CU-13 / CU-14 | @RN042 · @RN041 |
| Anular movimiento confirmado | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | CU-21 | ⚠️ Nunca se borra: movimiento inverso con motivo (@RN012) |
| Consultar existencia | ✅ | ✅ | ✅ | ✅ | ✅ | CU-09 | @RN065 · @RN067 |
| Consultar kardex | ✅ | ✅ | ✅ | ⚠️ | ✅ | CU-21 | ⚠️ Aux.: solo lo que él movió y últimos 30 días |
| Consultar valorización | ✅ | ✅ | ❌ | ❌ | ✅ | CU-22 | PR-04 · **sin dato en MVP (H-07)** |
| Consultar bitácora de auditoría | ✅ | ⚠️ | ❌ | ❌ | ✅ | CU-18 | ⚠️ Jefe: solo eventos de su bodega, sin configuración |
| Configurar umbrales de alerta | ✅ | ❌ | ❌ | ❌ | ❌ | CU-05 | @RN079 |
| Gestionar alertas | ✅ | ✅ | ✅ | ❌ | ❌ | CU-16 | @RN058 |
| Generar reportes operativos | ✅ | ✅ | ✅ | ❌ | ✅ | CU-22 | — |
| Generar reportes gerenciales | ✅ | ✅ | ❌ | ❌ | ✅ | CU-22 | PR-04 |
| Ver dashboard operativo completo | ✅ | ✅ | ⚠️ | ❌ | ✅ | CU-23 | ⚠️ Coord.: restringido a su zona |
| Ver panel de tareas propio | ✅ | ✅ | ✅ | ✅ | ❌ | CU-23 | PR-06 |
| Habilitar exportación analítica | ✅ | ❌ | ❌ | ❌ | ❌ | CU-22 | @RN078 |
| Registrar observación de auditoría | ❌ | ❌ | ❌ | ❌ | ✅ | CU-18 | @RN064 |
| Reportar novedad de mercancía | ✅ | ✅ | ✅ | ✅ | ❌ | CU-17 | @RN063: nunca se elimina |

## 3.4 Cadena de aprobación y escalamiento `[SRS]`

Consolidación de las reglas de segregación (no agrega reglas nuevas).

| Solicitud | Solicita | Aprueba / autoriza | Si solicitante = aprobador | Regla |
|---|---|---|---|---|
| Ajuste menor | Coordinador (o Jefe / Administrador) | Jefe de Bodega (o Administrador) | Escala al nivel superior; si no hay, se bloquea y se notifica al Administrador | @RN024 · @RN023 |
| Ajuste mayor | Coordinador (o Jefe / Administrador) | Administrador | Ídem | @RN024 · @RN023 |
| Ajuste sobre mercancía inmovilizada | Coordinador | Administrador (sin importar el monto) | Ídem | @RN036 |
| Salida bajo umbral del Coordinador | Jefe / Coordinador | Coordinador | Ídem | @RN030 · @RN023 |
| Salida sobre el umbral | Jefe / Coordinador | Jefe de Bodega | Ídem | @RN030 |
| Baja por daño (cualquier cantidad) | Jefe / Coordinador | Jefe de Bodega | Ídem | @RN052 |
| Sobrante de recepción | Auxiliar / Coordinador | Jefe de Bodega | Ídem | @RN007 |
| Confirmación de entrada | Auxiliar (recibe) | Coordinador (confirma) — nunca la misma persona | — | @RN057b |
| Cierre de conteo | Coordinador / Auxiliar (ejecutan) | Jefe de Bodega (nunca quien ejecutó) | Escala | @RN042 · @RN041 |
| Cancelación de transferencia en tránsito | Coordinador | Jefe de Bodega | — | @RN035 |

---

**ESTADO DEL CAPÍTULO 3**

| | |
|---|---|
| **Completado** | 5 roles + Sistema + actor externo · matriz de permisos (36 funciones) · cadena de aprobación |
| **Pendiente** | Lectura de parámetros por el Jefe (§2.7 del SPEC no la define; ver Cap. 10, nota) · política de «valorización» (H-07, DEC-07) |
| **Riesgos encontrados** | RG-13, RG-14, RG-17 (adopción por el Auxiliar) — riesgos críticos del SPEC |
| **Dependencias** | Cap. 4 (casos de uso), Cap. 10 (CRUD) |
