# EVENT_CATALOG
## Catálogo de Eventos del Dominio de COLBASOFT

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | EVENT_CATALOG |
| **Versión** | 1.2 |
| **Fase** | Fase 4 del proyecto — Modelo de Dominio (Checkpoint CP-04) |
| **Fecha** | 28 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) · 30 de septiembre de 2026 (v1.2) |
| **Estado** | **Borrador v1.2** (30-sep-2026): incorpora la trazabilidad por pieza y resuelve HD-25. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: DEC-02…DEC-09 sin responder y acta de DEC-08 |
| **Jerarquía documental** | Monografía → Auditoría Fundacional → COLBASOFT_SPEC v1.2 → SRS_COLBASOFT v1.2 → **Modelo de Dominio v1.2** (DOMAIN_MODEL · EVENT_CATALOG · GLOSSARY) |
| **Documentos hermanos** | `DOMAIN_MODEL.md` · `GLOSSARY.md` |
| **Autoría del proyecto** | Juan Esteban Argüello · Brayan Alexander Osorio · Brandon José Guerrero |
| **Institución / asesor** | Escuela de Ingeniería — CIAF · Edwin Andrés Cabrera Arredondo |
| **Fuera de alcance** | Arquitectura, modelo de datos, tecnologías, interfaces de integración, notaciones de diseño y código: pertenecen a la Fase 5 y posteriores |

> **Naturaleza.** Este documento es **derivado**: no modifica la monografía, la auditoría, el SPEC ni el SRS. Modela el negocio que esos documentos describen. Toda diferencia entre ellos o frente al Prompt Maestro #004 se registra como **Hallazgo del Dominio (HD-nn)**; no se corrige en silencio.

> **Versión 1.1.** Incorpora las decisiones del cierre del CP-04 (DF5-01, DF5-02, DF5-03, DF5-05 y DF5-06), registradas en `04_CP04_AUDITORIA/04_CP04_CIERRE.md`. El detalle de los cambios está en DOMAIN_MODEL §0.8. La v1.0 se conserva en el historial del repositorio (commit `79f823c`).

> **Versión 1.2.** Incorpora las decisiones del Director del 30 de septiembre de 2026 (DEC-01 = A, Q-11, F-1…F-6, Q-09 y Q-10), que agregan la **Pieza** al modelo y resuelven HD-25. El detalle está en DOMAIN_MODEL §0.9.

## Índice

| Cap. | Título |
|---|---|
| 1 | Filosofía de eventos |
| 2 | Catálogo completo de eventos |
| 3 | Línea temporal de eventos por proceso |
| 4 | Eventos auditables |
| 5 | Eventos derivados |
| 6 | Matrices D (Evento ↔ HU) y E (Evento ↔ RF) |

---

> **Reconstrucción de contexto.** La auditoría de reanudación de la Fase 4 está en DOMAIN_MODEL, Cap. 0 (ESTADO: CONTEXTO RECONSTRUIDO) y rige también este documento.

# CAPÍTULO 1 — FILOSOFÍA DE EVENTOS

## 1.1 Qué es un evento en COLBASOFT

Un **evento de dominio** es un **hecho relevante para el negocio que ya ocurrió**. Se nombra en pasado («Entrada confirmada»), tiene un **actor** (usuario identificado o Sistema, RN-INT-001), una **fecha operativa** (VO-32), una **entidad de origen** y un **resultado**. Un evento **no se modifica ni se retira**: si fue un error, se corrige con otro evento.

## 1.2 Evento, acción, movimiento y registro

| Concepto | Qué es | Tiempo | ¿Cambia el estado? | Ejemplo |
|---|---|---|:--:|---|
| **Acción** | Intención de un actor que el sistema evalúa contra las reglas | Presente («quiero…») | No por sí misma | El Coordinador pide confirmar la entrada DE-0087 |
| **Evento** | Hecho que resulta de una acción aceptada, de una acción rechazada relevante para el control, o de una regla que se cumple | Pasado («ocurrió») | Sí, o deja constancia de un intento de control | EV-ENT-012 Entrada confirmada · EV-ENT-014 Autoconfirmación rechazada · EV-INV-006 Existencia mínima alcanzada |
| **Movimiento** | Tipo particular de hecho que **altera la existencia o la ubicación** de una unidad de inventario (CD-28). Todo movimiento confirmado es un evento; no todo evento es un movimiento | Pasado | Sí, sobre la existencia | Movimiento de entrada de 120 unidades |
| **Registro** | **Constancia persistente** de un evento: línea de kardex, registro de bitácora o historial de la entidad | Permanente | No: es la huella del evento | Línea del kardex de la unidad; registro de bitácora del cambio de umbral |

Relación: **acción → (reglas) → evento(s) → registro(s)**. Una acción rechazada no produce movimiento; si el rechazo es relevante para el control (segregación, reglas estructurales, operación no autorizada), produce un **evento de rechazo** que se registra en la bitácora.

## 1.3 Qué no es un evento

- **Consultar** existencia, kardex, reportes o el dashboard: leer nunca escribe (RN-INT-006). Por eso las historias de consulta no tienen eventos (Matriz D).
- **Escanear** para ver qué es una etiqueta: es una acción de lectura; el escaneo solo forma parte de un evento cuando identifica mercancía en un movimiento.
- **Preparar un registro** que todavía no se confirma (estado «En registro»).
- **Visualizar** una notificación.

## 1.4 Propiedades de todo evento

| Propiedad | Regla |
|---|---|
| Inmutable | Una vez ocurrido no se modifica (RN-INT-002, RN-AUD-001) |
| Atribuido | Siempre tiene actor: usuario identificado o Sistema (RN-INT-001) |
| Fechado | Lleva la fecha operativa del hecho, no la de su sincronización (VO-32, HD-16) |
| Trazable | Se registra en el kardex (si altera la existencia), en la bitácora (si es auditable) o en el historial de su entidad |
| Explicable | Si es derivado, cita la regla o el umbral que lo produjo; nunca una predicción (DC-07) |

## 1.5 Convención de nombres e identificadores

- **ID permanente** `EV-<DOM>-nnn`: el dominio es el subdominio o módulo del evento; `nnn` es correlativo y nunca se reutiliza.
- **Nombre**: sustantivo del lenguaje ubicuo + participio («Lote inmovilizado»), sin sinónimos prohibidos.
- **Actor** «Sistema» indica evento derivado de una regla (Cap. 5).

## 1.6 Dominios de eventos

| Código | Dominio | Subdominio | Eventos |
|---|---|---|:--:|
| **ACC** | Acceso y sesión | SD-12 Usuarios y acceso | 7 |
| **USR** | Usuarios y roles | SD-12 Usuarios y acceso | 6 |
| **CAT** | Catálogo | SD-07 Catálogo textil | 9 |
| **BOD** | Estructura de bodega | SD-06 Ubicaciones | 8 |
| **QRC** | Identificación QR | SD-08 Identificación | 7 |
| **ENT** | Entradas y recepción | SD-02 Movimientos | 16 |
| **LOT** | Lotes | SD-03 Trazabilidad | 4 |
| **INV** | Inventario y existencia | SD-01 Inventario y existencia | 9 |
| **MOV** | Movimientos internos y transferencias | SD-02 Movimientos | 13 |
| **SAL** | Salidas | SD-02 Movimientos | 13 |
| **AJU** | Ajustes | SD-02 Movimientos | 10 |
| **CNT** | Conteos | SD-04 Conteos y exactitud | 18 |
| **NOV** | Novedades | SD-09 Novedades | 7 |
| **TRZ** | Trazabilidad y kardex | SD-03 Trazabilidad | 7 |
| **ALE** | Alertas | SD-05 Alertas y reglas | 7 |
| **REP** | Reportes y exportación | SD-11 Reportes y medición | 5 |
| **AUD** | Auditoría y control | SD-10 Auditoría | 6 |
| **PAR** | Configuración | SD-13 Configuración | 5 |
| **TAR** | Tareas y notificaciones | SD-14 Tareas y notificaciones | 6 |
| **JOR** | Operación diaria (cierre de jornada) | SD-15 Operación diaria (cierre de jornada) | 5 |
| **Total** | | | **168** |

---

**ESTADO DEL CAPÍTULO — 1**

| | |
|---|---|
| **Completado** | Definición de evento, diferencias entre evento, acción, movimiento y registro, propiedades, convenciones y 20 dominios de eventos |
| **Riesgos** | Tratar consultas o escaneos como eventos inflaría el catálogo y la bitácora |
| **Dependencias** | DOMAIN_MODEL Cap. 1 (lenguaje ubicuo) |
| **Hallazgos** | HD-16 |

---

# CAPÍTULO 2 — CATÁLOGO COMPLETO DE EVENTOS

> Cada evento declara nombre, actor, entidad de origen, entidades afectadas, disparador, resultado esperado, KPI y reglas. Las historias y los requisitos relacionados están en las matrices D y E (Cap. 6). **⚠️** marca eventos modelados desde el SPEC que no tienen historia o requisito que los implemente.

## 2.1 ACC · Acceso y sesión (7)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-ACC-001** | Sesión iniciada | Cualquier usuario | E-19 Usuario | E-20 Sesión | Credenciales individuales válidas de un usuario activo | Sesión abierta a nombre del usuario; vista según su rol | — | RN-INT-001 |
| **EV-ACC-002** | Acceso rechazado | Cualquier persona | E-19 Usuario | E-19 Usuario | Credenciales inválidas | Sin sesión; mensaje que no revela qué dato falló; intento contabilizado | — | RN-INT-001 |
| **EV-ACC-003** | Cuenta bloqueada | Sistema | E-19 Usuario | E-19 Usuario | Intentos fallidos consecutivos alcanzan el número configurado | Usuario Bloqueado; Administrador notificado | — | — |
| **EV-ACC-004** | Sesión cerrada por inactividad | Sistema | E-20 Sesión | E-20 Sesión | Inactividad igual al tiempo configurado, tras aviso previo | Sesión cerrada; el registro en curso no confirmado se conserva | — | RN-INT-001 |
| **EV-ACC-005** | Sesión cerrada por el usuario | Cualquier usuario | E-20 Sesión | E-20 Sesión | El usuario cierra su sesión | Sesión cerrada | — | — |
| **EV-ACC-006** | Contraseña cambiada | Cualquier usuario | E-19 Usuario | E-19 Usuario, E-20 Sesión | El usuario presenta la actual y una nueva que cumple la política | Nueva credencial vigente; demás sesiones cerradas; sin registrar valores | — | — |
| **EV-ACC-007** | Acceso restablecido | Administrador | E-19 Usuario | E-19 Usuario | El Administrador desbloquea una cuenta | Usuario Activo con cambio de contraseña forzado; usuario notificado | — | — |

## 2.2 USR · Usuarios y roles (6)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-USR-001** | Usuario creado | Administrador | E-19 Usuario | E-19 Usuario | Alta de una persona con uno de los cinco roles | Usuario Activo con rol y ámbito; cambio de contraseña en primer acceso | — | RN-INT-001, RN-MAE-006 |
| **EV-USR-002** | Rol cambiado | Administrador | E-19 Usuario | E-19 Usuario | Cambio de responsabilidades de un usuario | Nuevo rol vigente desde la siguiente sesión; movimientos anteriores conservan el rol de su momento | — | RN-MAE-004 |
| **EV-USR-003** | Ámbito asignado | Administrador | E-19 Usuario | E-19 Usuario | Asignación de bodega y zonas | Consultas y tareas filtradas por el nuevo ámbito | — | — |
| **EV-USR-004** | Usuario desactivado | Administrador | E-19 Usuario | E-19 Usuario, E-20 Sesión | La persona deja de operar | Acceso cerrado de inmediato; historia conservada con su identidad | — | RN-MAE-004, RN-MAE-007 |
| **EV-USR-005** | Usuario reactivado | Administrador | E-19 Usuario | E-19 Usuario | La persona vuelve a operar | Usuario Activo con su rol | — | RN-MAE-009 |
| **EV-USR-006** | Retiro del último Administrador o Jefe rechazado | Sistema | E-19 Usuario | E-19 Usuario | Intento de desactivar o cambiar de rol al último Administrador activo o al último Jefe de una bodega | Operación rechazada con explicación | — | RN-MAE-004 |

## 2.3 CAT · Catálogo (9)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-CAT-001** | Referencia creada | Administrador / Jefe | E-01 Referencia | E-01 Referencia | Alta de una referencia con código, descripción, categoría, tallas y colores | Referencia Activa | — | RN-MAE-001 |
| **EV-CAT-002** | SKU generados | Sistema | E-01 Referencia | E-02 SKU | Referencia creada o ampliada en tallas o colores | Un SKU por cada combinación talla × color | — | RN-LOT-002 |
| **EV-CAT-003** | Unidad de medida asignada | Administrador / Jefe | E-01 Referencia | E-01 Referencia | Definición de la unidad de medida de la referencia | Todas sus cantidades se expresan en esa unidad | — | RN-MAE-002, RN-INT-007 |
| **EV-CAT-004** | Umbrales de existencia definidos | Administrador / Jefe | E-02 SKU | E-02 SKU | Definición de existencia mínima y máxima de un SKU | El SKU queda sujeto a alertas de mínimo y máximo | KPI-19, KPI-21 | RN-AUD-004 |
| **EV-CAT-005** | Referencia desactivada | Administrador / Jefe | E-01 Referencia | E-01 Referencia | Referencia descontinuada con existencia cero | No aparece en operaciones nuevas; historia consultable | — | RN-MAE-003, RN-MAE-007, RN-MAE-008 |
| **EV-CAT-006** | Referencia reactivada | Administrador / Jefe | E-01 Referencia | E-01 Referencia | Referencia vuelve a usarse | Referencia Activa | — | RN-MAE-009 |
| **EV-CAT-007** | Catálogo cargado masivamente | Administrador | E-01 Referencia | E-01 Referencia, E-02 SKU | Carga de un archivo tabular validado | Referencias válidas creadas (o ninguna, según la opción); errores por línea reportados | — | RN-MAE-001 |
| **EV-CAT-008** | Categoría registrada | Administrador / Jefe | E-03 Categoría | E-03 Categoría | Alta o modificación de una categoría y su zona preferente | Categoría Activa disponible para agrupar referencias | — | RN-MOV-001 |
| **EV-CAT-009** | Categoría desactivada | Administrador / Jefe | E-03 Categoría | E-03 Categoría | Categoría en desuso | No se asigna a referencias nuevas; historia consultable | — | RN-MAE-007, RN-MAE-008 |

## 2.4 BOD · Estructura de bodega (8)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-BOD-001** | Bodega creada | Administrador | E-05 Bodega | E-05 Bodega | Alta del ámbito físico mayor | Bodega disponible para zonas | — | RN-EXI-002 |
| **EV-BOD-002** | Zona creada | Administrador | E-05 Bodega | E-06 Zona | Alta de una zona con tipo asignado | Zona disponible para ubicaciones; la bodega cumple la exigencia de zona de recepción | — | RN-EXI-002 |
| **EV-BOD-003** | Ubicación creada | Administrador | E-05 Bodega | E-07 Ubicación | Alta de una ubicación dentro de una zona | Ubicación Activa; su QR se genera | — | RN-MAE-006 |
| **EV-BOD-004** | Capacidad de ubicación definida | Administrador | E-07 Ubicación | E-07 Ubicación | Definición de la capacidad | La propuesta de destinos y la alerta de sobreocupación usan la capacidad | KPI-18 | RN-MOV-002 |
| **EV-BOD-005** | Ubicación desactivada | Administrador | E-07 Ubicación | E-07 Ubicación | Ubicación fuera de servicio y sin existencia | No se propone ni acepta como destino | — | RN-MAE-005, RN-MAE-007 |
| **EV-BOD-006** | Ubicación reactivada | Administrador | E-07 Ubicación | E-07 Ubicación | Ubicación vuelve a servicio | Ubicación Activa | — | RN-MAE-009 |
| **EV-BOD-007** | Coordinador asignado a zona | Administrador | E-06 Zona | E-06 Zona, E-19 Usuario | Designación del responsable de una zona | Alertas y tareas de la zona se dirigen a él | — | RN-ALE-005 |
| **EV-BOD-008** | Criterios de asignación configurados | Administrador | E-05 Bodega | E-05 Bodega | Definición de criterios y orden de propuesta de ubicación | Propuestas futuras siguen los criterios | KPI-10 | RN-MOV-001 |

## 2.5 QRC · Identificación QR (7)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-QRC-001** | Identificador QR generado | Sistema / Coordinador | E-09 Identificador QR | E-09 Identificador QR | SKU + Lote confirmado que requiere identificación (un QR por SKU + Lote, DF5-01) | Código nunca antes emitido, en estado Generado, listo para imprimir | — | RN-IDE-002 |
| **EV-QRC-002** | Identificador QR impreso | Coordinador | E-09 Identificador QR | E-09 Identificador QR | Impresión individual o por lote de impresión | Etiqueta física con información legible de respaldo | — | — |
| **EV-QRC-003** | Identificador QR activado | Auxiliar | E-09 Identificador QR | E-09 Identificador QR, E-04 Lote | Escaneo de verificación tras adherir la etiqueta | Identificador Activo; el SKU + Lote queda identificable en cualquier ubicación donde esté (DF5-01) | — | RN-IDE-001 |
| **EV-QRC-004** | Identificador QR reimpreso | Coordinador / Auxiliar | E-09 Identificador QR | E-09 Identificador QR | Reimpresión por deterioro o ilegibilidad, con motivo `[Q-09]` | Otra copia del mismo QR: el identificador no cambia de identidad ni de estado; la reimpresión queda en el historial | — | RN-IDE-004, RN-IDE-002 |
| **EV-QRC-005** | Identificador QR anulado | Coordinador | E-09 Identificador QR | E-09 Identificador QR | El identificador deja de tener efecto | Estado Anulado; su código jamás se reemite; su escaneo se rechaza | — | RN-IDE-002 |
| **EV-QRC-006** | Identificador secundario asociado | Coordinador | E-09 Identificador QR | E-09 Identificador QR | Asociación del código de barras del proveedor | Código de barras habilitado solo para consulta | — | RN-IDE-003 |
| **EV-QRC-007** | QR de ubicación generado | Sistema / Administrador | E-07 Ubicación | E-09 Identificador QR | Ubicación creada o impresión por zona | Identificador de ubicación distinguible del de mercancía | — | RN-IDE-002 |

## 2.6 ENT · Entradas y recepción (16)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-ENT-001** | Documento de entrada creado | Coordinador | E-11 Documento de entrada | E-11 Documento de entrada | Mercancía esperada o recién llegada | Documento Pendiente de recepción, sin datos comerciales | KPI-12 | RN-ENT-001 |
| **EV-ENT-002** | Posible duplicado advertido | Sistema | E-11 Documento de entrada | E-11 Documento de entrada | Otro documento con igual origen, referencia y fecha | Advertencia que exige confirmación explícita; no bloquea | — | RN-ENT-002 |
| **EV-ENT-003** | Recepción física iniciada ⚠️ | Auxiliar | E-11 Documento de entrada | E-11 Documento de entrada | El Auxiliar abre el documento en la tablet | Recepción en curso atribuida al Auxiliar | KPI-12 | RN-INT-001 |
| **EV-ENT-004** | Línea de recepción registrada | Auxiliar | E-11 Documento de entrada | E-11 Documento de entrada | Conteo físico de una línea recibida | Cantidad recibida por línea con confirmación visible | — | RN-INT-003 |
| **EV-ENT-005** | Recepción interrumpida | Auxiliar | E-11 Documento de entrada | E-11 Documento de entrada | Fin de turno o interrupción antes de terminar | Documento en Recepción parcial | — | — |
| **EV-ENT-006** | Recepción continuada | Auxiliar | E-11 Documento de entrada | E-11 Documento de entrada | Otro usuario retoma una recepción parcial | Ambos receptores registrados | — | RN-INT-001 |
| **EV-ENT-007** | Recibido conforme determinado | Sistema | E-11 Documento de entrada | E-11 Documento de entrada | Comparación línea a línea sin diferencias | Documento Recibido conforme | — | RN-ENT-003 |
| **EV-ENT-008** | Faltante de recepción registrado | Sistema | E-11 Documento de entrada | E-11 Documento de entrada | Recibido < esperado en una línea | Documento Recibido con novedad; Jefe notificado; no bloquea confirmar lo recibido | — | RN-ENT-004 |
| **EV-ENT-009** | Sobrante de recepción registrado | Sistema | E-11 Documento de entrada | E-11 Documento de entrada | Recibido > esperado en una línea | Documento Recibido con novedad; confirmación detenida hasta autorización | — | RN-ENT-005 |
| **EV-ENT-010** | Sobrante autorizado | Jefe de Bodega | E-11 Documento de entrada | E-11 Documento de entrada | El Jefe acepta el sobrante | El sobrante puede ingresar al confirmar | — | RN-ENT-005, RN-AJU-001 |
| **EV-ENT-011** | Mercancía dañada registrada en recepción | Auxiliar | E-11 Documento de entrada | E-11 Documento de entrada, E-08 Unidad de Inventario, E-17 Novedad | Parte de lo recibido llega dañada | Cantidad dañada separada; ingresa inmovilizada en cuarentena; novedad abierta; Jefe notificado | KPI-23 | RN-ENT-006 |
| **EV-ENT-012** | Entrada confirmada | Coordinador | E-11 Documento de entrada | E-11 Documento de entrada, E-04 Lote, E-08 Unidad de Inventario, E-10 Movimiento | Verificación por una persona distinta de quien recibió | Lote creado o asociado; movimiento de entrada en el kardex; existencia En recepción en una ubicación de la zona de recepción (RN-EXI-007, DF5-02) | KPI-05, KPI-11, KPI-12 | RN-ENT-007, RN-EXI-007, RN-INT-002, RN-INT-004, RN-INT-003, RN-LOT-001 |
| **EV-ENT-013** | Retorno registrado como entrada | Coordinador | E-11 Documento de entrada | E-11 Documento de entrada, E-10 Movimiento | Vuelve mercancía que había salido | Entrada nueva que referencia la salida original; la salida no se reversa | — | RN-SAL-007 |
| **EV-ENT-014** | Autoconfirmación de entrada rechazada | Sistema | E-11 Documento de entrada | E-11 Documento de entrada | Quien registró la recepción intenta confirmarla | Confirmación rechazada; se exige un segundo actor | — | RN-ENT-007 |
| **EV-ENT-015** | Documento de entrada reversado ⚠️ | Coordinador | E-11 Documento de entrada | E-11 Documento de entrada | Documento aún no confirmado que no procede | Documento Reversado, sin efecto en el inventario | — | RN-MAE-007 |
| **EV-ENT-016** | Pieza registrada en la recepción | Auxiliar | E-11 Documento de entrada | E-11 Documento de entrada, E-27 Pieza | Conteo físico de una pieza recibida (rollo, paquete, bolsa o contenedor agrupado) `[Q-11]` `[F-1]` `[F-2]` `[F-6]` | Pieza con su tipo y su cantidad propia asociada a un SKU + Lote; la cantidad recibida de la línea es la suma de sus piezas; confirmación visible | — | RN-LOT-006, RN-LOT-007 |

- **EV-ENT-003**: KPI-12 exige el instante de llegada, que ningún RF captura (PROP-KPI-04 del SRS)
- **EV-ENT-015**: Función de M-07 sin HU ni RF (HD-19)

## 2.7 LOT · Lotes (4)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-LOT-001** | Lote creado | Sistema | E-11 Documento de entrada | E-04 Lote | Confirmación de una entrada | Lote Habilitado con origen y fecha de ingreso, único en su SKU | — | RN-LOT-001, RN-LOT-002, RN-MAE-006 |
| **EV-LOT-002** | Lote inmovilizado | Jefe / Administrador | E-04 Lote | E-04 Lote, E-08 Unidad de Inventario | Sospecha de calidad u origen, con motivo tipificado | Toda la existencia del lote pasa a Inmovilizado en todas sus ubicaciones | — | RN-LOT-003, RN-EXI-006 |
| **EV-LOT-003** | Lote liberado | Jefe / Administrador | E-04 Lote | E-04 Lote, E-08 Unidad de Inventario | Verificación concluida, con motivo tipificado | La existencia vuelve a sus estados normales | — | RN-LOT-004 |
| **EV-LOT-004** | Antigüedad de lote superada | Sistema | E-04 Lote | E-18 Alerta | Días en bodega sobre el umbral configurado | Lote destacado; alerta informativa al Jefe | KPI-17 | RN-LOT-005 |

## 2.8 INV · Inventario y existencia (9)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-INV-001** | Mercancía ubicada | Auxiliar | E-10 Movimiento | E-10 Movimiento, E-08 Unidad de Inventario, E-07 Ubicación | Escaneo de la mercancía en recepción y de la ubicación destino | Movimiento interno de primera ubicación confirmado: la cantidad sale de la unidad de la ubicación de recepción y entra Disponible a la unidad destino; existencia total invariante; kardex con qué, cuánto, origen, destino, quién, cuándo y documento de entrada; confirmación visible | KPI-05, KPI-10, KPI-18 | RN-MOV-010, RN-MOV-004, RN-EXI-002, RN-MOV-002, RN-MOV-001, RN-MOV-011 |
| **EV-INV-002** | Desviación de ubicación registrada ⚠️ | Sistema | E-08 Unidad de Inventario | E-08 Unidad de Inventario | Mercancía ubicada en un lugar distinto al propuesto | Desviación registrada como información (no falta); Coordinador notificado | KPI-10 | RN-MOV-003 |
| **EV-INV-003** | Existencia reservada | Sistema | E-08 Unidad de Inventario | E-08 Unidad de Inventario | Salida autorizada o transferencia creada | Porción Disponible → Reservado; ninguna otra operación puede comprometerla | — | RN-EXI-004, RN-EXI-003 |
| **EV-INV-004** | Reserva liberada | Sistema | E-08 Unidad de Inventario | E-08 Unidad de Inventario | Cancelación de la salida o de la transferencia antes del despacho | Porción Reservado → Disponible | — | RN-EXI-004, RN-MOV-009 |
| **EV-INV-005** | Reserva vencida liberada ⚠️ | Sistema | E-12 Solicitud de salida | E-08 Unidad de Inventario, E-12 Solicitud de salida | Salida autorizada no ejecutada dentro del plazo | Reserva liberada; solicitud Vencida; alerta al solicitante | — | RN-SAL-005 |
| **EV-INV-006** | Existencia mínima alcanzada | Sistema | E-02 SKU | E-18 Alerta | Existencia disponible del SKU por debajo de su mínimo | Condición de ruptura inminente vigente; genera una sola alerta | KPI-19, KPI-21 | RN-ALE-001, RN-ALE-005 |
| **EV-INV-007** | Existencia máxima superada | Sistema | E-02 SKU | E-18 Alerta | Existencia del SKU por encima de su máximo | Condición de sobre stock vigente; alimenta la rotación | KPI-16, KPI-19 | RN-ALE-001 |
| **EV-INV-008** | Existencia en cero alcanzada | Sistema | E-02 SKU | E-18 Alerta | Una referencia activa queda sin existencia | Evento de ruptura contabilizado; alerta de existencia en cero | KPI-21, KPI-19 | RN-ALE-001 |
| **EV-INV-009** | Ubicación sobreocupada ⚠️ | Sistema | E-07 Ubicación | E-18 Alerta | La ocupación de una ubicación supera su capacidad | Alerta de sobreocupación al Coordinador de la zona | KPI-18, KPI-19 | RN-MOV-002, RN-ALE-001 |

- **EV-INV-002**: Sin RF que la implemente (H-11 del SRS)
- **EV-INV-005**: Sin RF que la implemente (H-11 del SRS)
- **EV-INV-009**: Cálculo de ocupación con unidades heterogéneas pendiente (HD-17)

## 2.9 MOV · Movimientos internos y transferencias (13)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-MOV-001** | Movimiento interno confirmado | Auxiliar | E-10 Movimiento | E-08 Unidad de Inventario, E-07 Ubicación | Escaneo de mercancía, selección de la pieza (la ubicación filtra y verifica, F-4), ubicación de origen si hay varias (DF5-01) y ubicación destino; la primera ubicación desde la zona de recepción es EV-INV-001 | Existencia descontada del origen y sumada al destino; total invariante; kardex actualizado | KPI-05, KPI-11 | RN-MOV-004, RN-MOV-005, RN-INT-002, RN-EXI-003, RN-MOV-011 |
| **EV-MOV-002** | Movimiento interno rechazado | Sistema | E-10 Movimiento | E-08 Unidad de Inventario | Cantidad mayor a la disponible, destino igual al origen, destino inactivo o sin capacidad, o existencia inmovilizada | Operación rechazada con explicación comprensible | — | RN-EXI-003, RN-MOV-005, RN-MOV-002, RN-EXI-006 |
| **EV-MOV-003** | Movimiento interno interrumpido ⚠️ | Auxiliar / Sistema | E-10 Movimiento | E-08 Unidad de Inventario | El traslado se inicia y no se cierra (también el de primera ubicación) | Porción En tránsito: no disponible en origen ni destino | — | RN-MOV-006, RN-EXI-005 |
| **EV-MOV-004** | Tránsito interno prolongado detectado ⚠️ | Sistema | E-10 Movimiento | E-18 Alerta | Movimiento interno en tránsito supera el tiempo máximo | Alerta de tránsito prolongado | — | RN-MOV-006 |
| **EV-MOV-005** | Transferencia creada | Coordinador | E-13 Transferencia | E-13 Transferencia, E-08 Unidad de Inventario | Necesidad de mover existencia entre zonas o bodegas | Transferencia Pendiente de despacho; reserva en origen; tarea al Auxiliar del origen | — | RN-EXI-003, RN-EXI-004 |
| **EV-MOV-006** | Despacho de transferencia confirmado | Auxiliar (origen) | E-13 Transferencia | E-13 Transferencia, E-08 Unidad de Inventario | Escaneo de la mercancía despachada | Transferencia En tránsito; porción Reservado → En tránsito | KPI-15 | RN-EXI-005 |
| **EV-MOV-007** | Transferencia completada | Auxiliar (destino) | E-13 Transferencia | E-13 Transferencia, E-08 Unidad de Inventario, E-10 Movimiento | Recepción escaneada igual a lo despachado | Existencia descontada del origen y sumada al destino; ambos movimientos en el kardex | KPI-15, KPI-11, KPI-05 | RN-MOV-007, RN-INT-002 |
| **EV-MOV-008** | Diferencia de transferencia registrada | Sistema | E-13 Transferencia | E-13 Transferencia, E-17 Novedad | Recibido < despachado | Transferencia Con diferencia; novedad abierta; resolución del Jefe requerida | KPI-23 | RN-MOV-007 |
| **EV-MOV-009** | Recepción de transferencia rechazada por exceso | Sistema | E-13 Transferencia | E-13 Transferencia | Recibido > despachado | Recepción rechazada; escalamiento al Jefe | — | RN-MOV-007 |
| **EV-MOV-010** | Diferencia de transferencia resuelta | Jefe de Bodega | E-13 Transferencia | E-13 Transferencia | El Jefe investiga y resuelve | Transferencia Completada; resolución documentada | — | RN-MOV-007 |
| **EV-MOV-011** | Tiempo máximo en tránsito excedido | Sistema | E-13 Transferencia | E-18 Alerta | Transferencia en tránsito más allá del plazo | Alerta al Jefe con contenido y responsable de despacho | KPI-15, KPI-19 | RN-MOV-008 |
| **EV-MOV-012** | Transferencia cancelada antes del despacho | Coordinador | E-13 Transferencia | E-13 Transferencia, E-08 Unidad de Inventario | La transferencia ya no procede | Transferencia Cancelada con motivo; reserva liberada | — | RN-MOV-009 |
| **EV-MOV-013** | Transferencia cancelada en tránsito | Jefe de Bodega | E-13 Transferencia | E-13 Transferencia, E-08 Unidad de Inventario, E-10 Movimiento | La mercancía no puede llegar a destino | Transferencia Cancelada con motivo; movimiento de retorno al origen | — | RN-MOV-009 |

- **EV-MOV-003**: Sin HU ni RF (H-11 del SRS)
- **EV-MOV-004**: Sin HU (H-11 del SRS)

## 2.10 SAL · Salidas (13)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-SAL-001** | Salida solicitada | Jefe / Coordinador | E-12 Solicitud de salida | E-12 Solicitud de salida | Requerimiento de mercancía (consumo, despacho, devolución, baja) | Solicitud con motivo tipificado, sin datos comerciales; disponibilidad verificada | — | RN-SAL-002, RN-EXI-003 |
| **EV-SAL-002** | Salida rechazada por existencia insuficiente | Sistema | E-12 Solicitud de salida | E-12 Solicitud de salida | Cantidad solicitada mayor que la disponible | Rechazo con la cantidad disponible; ofrecimiento de salida parcial | — | RN-EXI-001, RN-EXI-003 |
| **EV-SAL-003** | Salida autorizada | Jefe / Coordinador | E-12 Solicitud de salida | E-12 Solicitud de salida, E-08 Unidad de Inventario, E-23 Tarea operativa | Aprobación de la solicitud por quien corresponde | Solicitud Autorizada; existencia reservada; tarea de preparación generada | KPI-22 | RN-SAL-001, RN-AJU-001, RN-EXI-004, RN-SAL-003 |
| **EV-SAL-004** | Salida escalada al Jefe | Sistema | E-12 Solicitud de salida | E-12 Solicitud de salida | Solicitud sobre el umbral del Coordinador | Autorización enrutada al Jefe | — | RN-SAL-001 |
| **EV-SAL-005** | Escaneo de preparación rechazado | Sistema | E-12 Solicitud de salida | E-12 Solicitud de salida | Unidad escaneada distinta de la solicitada | Rechazo con la discrepancia concreta (referencia, talla, color o lote) | — | RN-SAL-004 |
| **EV-SAL-006** | Salida ejecutada | Auxiliar | E-12 Solicitud de salida | E-12 Solicitud de salida, E-08 Unidad de Inventario, E-10 Movimiento | Preparación completa confirmada | Movimiento de salida en el kardex; existencia descontada; reserva liberada | KPI-05, KPI-11, KPI-16 | RN-EXI-001, RN-INT-002, RN-INT-004 |
| **EV-SAL-007** | Salida parcial autorizada | Jefe de Bodega | E-12 Solicitud de salida | E-12 Solicitud de salida, E-08 Unidad de Inventario | Disponible insuficiente y se acepta retirar lo que hay | Solicitud ajustada a la cantidad disponible | KPI-22 | RN-EXI-001, RN-AJU-001 |
| **EV-SAL-008** | Baja por daño aprobada | Jefe de Bodega | E-12 Solicitud de salida | E-12 Solicitud de salida, E-08 Unidad de Inventario, E-10 Movimiento | Solicitud de baja con motivo específico, observación y evidencia | Movimiento de salida marcado como baja; alimenta el reporte de mermas | KPI-13 | RN-SAL-006, RN-AJU-001 |
| **EV-SAL-009** | Salida rechazada por el autorizador ⚠️ | Jefe / Coordinador | E-12 Solicitud de salida | E-12 Solicitud de salida | El autorizador no aprueba la solicitud | Solicitud Rechazada; solicitante notificado | KPI-22 | RN-AJU-001 |
| **EV-SAL-010** | Preparación de salida iniciada | Auxiliar | E-12 Solicitud de salida | E-12 Solicitud de salida | Primer escaneo válido de la tarea de preparación | Solicitud En preparación; progreso visible | — | RN-SAL-003, RN-SAL-004 |
| **EV-SAL-011** | Salida cancelada ⚠️ | Jefe / Coordinador | E-12 Solicitud de salida | E-12 Solicitud de salida, E-08 Unidad de Inventario | La salida autorizada ya no procede | Solicitud Cancelada; reserva liberada | — | RN-EXI-004 |
| **EV-SAL-012** | Pieza tomada en la preparación | Auxiliar | E-12 Solicitud de salida | E-12 Solicitud de salida, E-27 Pieza | Escaneo del SKU + Lote y selección de la pieza que se toma `[Q-10]` `[F-4]` | La pieza se cuenta una sola vez en la preparación; el progreso muestra piezas y cantidad tomadas frente a lo solicitado | — | RN-SAL-009, RN-MOV-011 |
| **EV-SAL-013** | Corte parcial registrado | Auxiliar | E-12 Solicitud de salida | E-12 Solicitud de salida, E-27 Pieza, E-10 Movimiento | Corte de parte de un rollo durante una salida `[F-3]` | Cantidad cortada descontada de la pieza, que conserva su identidad y su remanente; salida con motivo tipificado, autorización y atribución personal | — | RN-SAL-008, RN-LOT-007 |

- **EV-SAL-009**: Función de M-08 sin RF propio
- **EV-SAL-011**: Actor y RF no definidos en el SPEC (HD-19)

## 2.11 AJU · Ajustes (10)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-AJU-001** | Ajuste solicitado | Coordinador | E-14 Solicitud de ajuste | E-14 Solicitud de ajuste | Diferencia entre existencia registrada y física (hallazgo, conteo o novedad) | Solicitud Pendiente de aprobación con motivo y evidencia; existencia sin cambios | KPI-14 | RN-AJU-003, RN-EXI-001 |
| **EV-AJU-002** | Ajuste clasificado y enrutado | Sistema | E-14 Solicitud de ajuste | E-14 Solicitud de ajuste | Solicitud recibida | Clasificación menor/mayor con umbral aplicado; enrutamiento al Jefe o al Administrador | — | RN-AJU-002, RN-EXI-006 |
| **EV-AJU-003** | Ajuste escalado por autoaprobación | Sistema | E-14 Solicitud de ajuste | E-14 Solicitud de ajuste | El aprobador designado es el solicitante | Solicitud Escalada al nivel superior | — | RN-AJU-001 |
| **EV-AJU-004** | Ajuste aprobado | Jefe / Administrador | E-14 Solicitud de ajuste | E-14 Solicitud de ajuste | Revisión de unidad, diferencia, motivo, solicitante y evidencia | Solicitud Aprobada; se origina el movimiento de ajuste | KPI-14, KPI-22 | RN-AJU-001, RN-EXI-001 |
| **EV-AJU-005** | Ajuste aplicado | Sistema | E-14 Solicitud de ajuste | E-10 Movimiento, E-08 Unidad de Inventario | Aprobación de la solicitud | Movimiento de ajuste en el kardex; existencia corregida; unidad marcada como ajustada | KPI-08, KPI-14 | RN-INT-004, RN-AJU-007, RN-EXI-001 |
| **EV-AJU-006** | Ajuste rechazado | Jefe / Administrador | E-14 Solicitud de ajuste | E-14 Solicitud de ajuste | El aprobador no acepta la solicitud | Solicitud Rechazada con justificación; solicitante notificado; existencia sin cambios | KPI-22 | RN-AJU-006 |
| **EV-AJU-007** | Ajuste negativo impedido | Sistema | E-14 Solicitud de ajuste | E-14 Solicitud de ajuste | El ajuste dejaría existencia negativa | Rechazo sin excepción; explicación de existencia y diferencia | — | RN-EXI-001 |
| **EV-AJU-008** | Solicitud de ajuste vencida escalada | Sistema | E-14 Solicitud de ajuste | E-14 Solicitud de ajuste, E-18 Alerta | Solicitud sin resolver más allá del plazo | Escalamiento al nivel superior y alerta | KPI-22 | RN-AJU-005 |
| **EV-AJU-009** | Patrón de ajustes recurrentes detectado | Sistema | E-14 Solicitud de ajuste | E-18 Alerta | Ajustes sobre una misma unidad superan el umbral en la ventana | Alerta al Jefe y al Auditor con ajustes, solicitantes y aprobadores | KPI-14, KPI-19 | RN-AJU-004 |
| **EV-AJU-010** | Solicitud bloqueada sin aprobador | Sistema | E-14 Solicitud de ajuste | E-14 Solicitud de ajuste | No existe nivel superior disponible | Solicitud Bloqueada; Administrador notificado | — | RN-AJU-001 |

## 2.12 CNT · Conteos (18)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-CNT-001** | Conteo cíclico programado | Coordinador | E-15 Conteo | E-15 Conteo | Programación periódica, alerta de exactitud o decisión del Coordinador | Conteo Programado con alcance; no bloquea la bodega | KPI-03 | — |
| **EV-CNT-002** | Conteo general programado | Jefe de Bodega | E-15 Conteo | E-15 Conteo | Cierre de período o exigencia de auditoría | Conteo Programado con fecha de corte; usuarios notificados con anticipación | KPI-02 | RN-CNT-006 |
| **EV-CNT-003** | Existencia teórica congelada | Sistema | E-15 Conteo | E-15 Conteo | Inicio del conteo | Fotografía inmutable del ámbito; conteo En ejecución | — | RN-CNT-001 |
| **EV-CNT-004** | Movimientos bloqueados por conteo general | Sistema | E-15 Conteo | E-10 Movimiento | Llegada de la fecha de corte | Registro de movimientos bloqueado en la bodega | — | RN-CNT-006 |
| **EV-CNT-005** | Movimiento de excepción autorizado | Jefe de Bodega | E-15 Conteo | E-10 Movimiento | Necesidad urgente durante el bloqueo | Movimiento permitido y marcado como excepción en el kardex | — | RN-CNT-006 |
| **EV-CNT-006** | Tarea de conteo asignada | Sistema / Coordinador | E-15 Conteo | E-16 Tarea de conteo | Generación de tareas del ámbito | Tarea Asignada a un contador identificado | — | RN-CNT-003 |
| **EV-CNT-007** | Conteo físico registrado | Auxiliar | E-16 Tarea de conteo | E-16 Tarea de conteo | Escaneo de ubicación y registro de la cantidad de cada pieza contada a mano `[F-5]` | Existencia contada guardada pieza por pieza sin mostrar la esperada; tarea Confirmada | KPI-03 | RN-CNT-002, RN-CNT-009 |
| **EV-CNT-008** | Línea de conteo clasificada | Sistema | E-15 Conteo | E-15 Conteo | Comparación de lo contado con la existencia congelada | Línea Conforme, Sobrante o Faltante; conteo En conciliación | KPI-01, KPI-04, KPI-08 | RN-CNT-001 |
| **EV-CNT-009** | Segundo conteo requerido | Sistema | E-15 Conteo | E-16 Tarea de conteo | Diferencia de una línea sobre la tolerancia | Tarea de segundo conteo para una persona distinta | KPI-06 | RN-CNT-003 |
| **EV-CNT-010** | Diferencia persistente escalada | Sistema | E-15 Conteo | E-15 Conteo | El segundo conteo también difiere | Escalamiento al Jefe para verificación presencial | — | RN-CNT-003 |
| **EV-CNT-011** | Tarea de conteo reasignada | Coordinador | E-16 Tarea de conteo | E-16 Tarea de conteo | El contador asignado no está disponible | Nuevo contador; ambos registrados; conteo parcial conservado | — | RN-CNT-003 |
| **EV-CNT-012** | Ubicación excluida del conteo general | Jefe de Bodega | E-15 Conteo | E-15 Conteo | Ubicación imposible de cubrir | Exclusión con justificación; cobertura documentada | KPI-03 | RN-CNT-007 |
| **EV-CNT-013** | Diferencia global crítica detectada ⚠️ | Sistema | E-15 Conteo | E-15 Conteo | Diferencia global del conteo general sobre el umbral crítico | Administrador y Auditor notificados antes de permitir el cierre | KPI-02 | RN-CNT-008 |
| **EV-CNT-014** | Conteo cerrado | Jefe de Bodega | E-15 Conteo | E-15 Conteo, E-14 Solicitud de ajuste | Revisión del consolidado de diferencias | Conteo Cerrado (no se reabre); ajustes derivados solicitados; en el general, fin del bloqueo | KPI-01, KPI-02 | RN-CNT-004, RN-CNT-003, RN-CNT-007, RN-AJU-001 |
| **EV-CNT-015** | Exactitud del inventario calculada | Sistema | E-15 Conteo | E-15 Conteo | Cierre del conteo | Exactitud del ámbito almacenada históricamente (KPI-01; KPI-02 en el general) | KPI-01, KPI-02, KPI-03, KPI-04 | RN-CNT-004 |
| **EV-CNT-016** | Movimientos desbloqueados | Sistema | E-15 Conteo | E-10 Movimiento | Cierre o aborto del conteo general | Registro de movimientos habilitado | — | RN-CNT-006 |
| **EV-CNT-017** | Conteo abortado ⚠️ | Jefe de Bodega | E-15 Conteo | E-15 Conteo | El conteo no puede completarse | Congelamiento liberado; conteos parciales conservados sin ajustes | — | — |
| **EV-CNT-018** | Conteo vencido ⚠️ | Sistema | E-15 Conteo | E-15 Conteo, E-18 Alerta | Conteo no ejecutado o no cerrado en el plazo | Alerta; si excede el máximo, congelamiento liberado y conteo Vencido | — | RN-CNT-005 |

- **EV-CNT-013**: Sin HU ni RF (H-11 del SRS)
- **EV-CNT-017**: PN-09 E-04; función de M-11 sin HU ni RF propios
- **EV-CNT-018**: Sin HU propia

## 2.13 NOV · Novedades (7)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-NOV-001** | Novedad reportada | Auxiliar (o rol operativo) · Sistema, al rechazar un registro sincronizado | E-17 Novedad | E-17 Novedad | Hallazgo físico: dañada, sin identificador, en ubicación incorrecta o inexistente; o registro rechazado al sincronizar que describe un hecho físico ya realizado (EV-TRZ-007) | Novedad Abierta dirigida al Coordinador de la zona, sin imputación al reportante | KPI-23 | RN-NOV-003, RN-INT-008 |
| **EV-NOV-002** | Novedad vinculada a novedad abierta | Sistema | E-17 Novedad | E-17 Novedad | Reporte sobre una unidad que ya tiene novedad abierta | Se vincula; no se duplica | — | RN-NOV-003 |
| **EV-NOV-003** | Acción de novedad determinada | Coordinador | E-17 Novedad | E-17 Novedad | Evaluación de la novedad | Acción: ajuste, reidentificación, reubicación o baja | — | — |
| **EV-NOV-004** | Novedad resuelta y cerrada | Coordinador / Jefe | E-17 Novedad | E-17 Novedad | El movimiento de resolución se confirma | Novedad Cerrada resuelta, vinculada a su resolución | KPI-23 | RN-MAE-007 |
| **EV-NOV-005** | Novedad cerrada como improcedente | Coordinador / Jefe | E-17 Novedad | E-17 Novedad | La novedad se reportó por error | Novedad Cerrada improcedente con justificación; no se elimina | KPI-23 | RN-MAE-007 |
| **EV-NOV-006** | Novedad escalada por vencimiento ⚠️ | Sistema | E-17 Novedad | E-17 Novedad, E-18 Alerta | Novedad sin resolver más allá del plazo | Novedad Escalada al Jefe; alerta | KPI-23 | RN-NOV-002 |
| **EV-NOV-007** | Mercancía sin registro incorporada ⚠️ | Coordinador / Jefe | E-17 Novedad | E-08 Unidad de Inventario, E-14 Solicitud de ajuste, E-09 Identificador QR | Identificación de mercancía encontrada sin registro | Unidad creada o seleccionada, ajuste por sobrante aprobado por el Jefe, QR y ubicación asignados | — | RN-NOV-001, RN-AJU-003 |

- **EV-NOV-006**: Cobertura RF parcial (H-11, H-13 del SRS)
- **EV-NOV-007**: Cobertura RF parcial (H-13 del SRS)

## 2.14 TRZ · Trazabilidad y kardex (7)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-TRZ-001** | Movimiento confirmado en el kardex | Usuario / Sistema | E-10 Movimiento | E-08 Unidad de Inventario | Cualquier movimiento satisface sus reglas y se confirma | Línea inmutable con fecha, hora, tipo, cantidad, existencia resultante, ubicación, usuario, motivo y documento | KPI-05, KPI-11, KPI-17, KPI-24 | RN-INT-001, RN-INT-002, RN-INT-004, RN-LOT-007 |
| **EV-TRZ-002** | Movimiento anulado | Jefe / Administrador | E-10 Movimiento | E-10 Movimiento, E-08 Unidad de Inventario | Error detectado en un movimiento confirmado | Movimiento inverso con motivo y autorización; ambos visibles | KPI-08 | RN-INT-002 |
| **EV-TRZ-003** | Registro retenido sin conectividad | Sistema | E-10 Movimiento | E-10 Movimiento | Pérdida de conectividad durante un registro | Registro Pendiente de sincronización; no confirma documentos | — | RN-INT-003 |
| **EV-TRZ-004** | Registro sincronizado | Sistema | E-10 Movimiento | E-10 Movimiento | Conectividad restablecida y el registro sigue cumpliendo las reglas frente al estado vigente | Registro validado de nuevo (RN-INT-008) y Confirmado con su fecha operativa original (HD-16) | — | RN-INT-003, RN-INT-008 |
| **EV-TRZ-005** | Verificación de integridad ejecutada | Auditor | E-08 Unidad de Inventario | E-08 Unidad de Inventario | Solicitud de verificación por unidad, lote o global | Resultado exportable de la comparación existencia vs. suma de movimientos | KPI-09 | RN-AUD-005, RN-INT-004 |
| **EV-TRZ-007** | Registro rechazado al sincronizar ⚠️ | Sistema | E-10 Movimiento | E-10 Movimiento, E-17 Novedad | Al sincronizar, el registro retenido ya no cumple alguna regla o invariante frente al estado vigente | Registro Rechazado en sincronización, sin efecto en la existencia; constancia del registro original, su autor, el motivo y el instante; si describe un hecho físico, abre una novedad (EV-NOV-001) | — | RN-INT-008 |
| **EV-TRZ-006** | Discrepancia de integridad detectada | Sistema | E-08 Unidad de Inventario | E-08 Unidad de Inventario | Existencia ≠ suma de movimientos (unidad, lote o global) | Hallazgo crítico notificado al Administrador | KPI-09 | RN-INT-004 |

- **EV-TRZ-007**: Nuevo en la v1.1 (DF5-05, HD-24). Ningún RF describe todavía el rechazo; se apoya en RF-ENT-005 y RNF-DSP-002

## 2.15 ALE · Alertas (7)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-ALE-001** | Alerta generada | Sistema | E-18 Alerta | E-18 Alerta | Una condición de regla se cumple (eventos EV-INV-006…009, EV-MOV-004, EV-MOV-011, EV-AJU-008, EV-AJU-009, EV-CNT-018, EV-LOT-004, EV-ALE-007) | Alerta Activa con tipo, severidad y destinatario por rol; una sola por condición | KPI-19 | RN-ALE-001, RN-ALE-005 |
| **EV-ALE-002** | Alerta atendida | Jefe / Coordinador | E-18 Alerta | E-18 Alerta | El destinatario ejecuta la acción correctiva | Alerta Atendida con quién, cuándo y qué se hizo | KPI-19, KPI-20 | — |
| **EV-ALE-003** | Alerta descartada | Jefe / Coordinador | E-18 Alerta | E-18 Alerta | El destinatario considera que no requiere acción | Alerta Descartada con motivo obligatorio | KPI-19 | RN-ALE-004 |
| **EV-ALE-004** | Alerta escalada | Sistema | E-18 Alerta | E-18 Alerta | Alerta crítica sin atención dentro del plazo | Alerta Escalada al rol superior con notificación adicional | KPI-20 | RN-ALE-002 |
| **EV-ALE-005** | Alerta cerrada automáticamente | Sistema | E-18 Alerta | E-18 Alerta | La condición de disparo deja de cumplirse | Alerta Cerrada sin atención si nadie actuó | KPI-19 | RN-ALE-003 |
| **EV-ALE-006** | Frecuencia anómala de disparo reportada | Sistema | E-18 Alerta | E-25 Parámetro de configuración | Un tipo de alerta se dispara con frecuencia anómala | Reporte al Administrador para recalibrar umbrales | KPI-19 | RN-ALE-001 |
| **EV-ALE-007** | Exactitud bajo el umbral detectada ⚠️ | Sistema | E-15 Conteo | E-18 Alerta | Exactitud calculada inferior al umbral configurado (no es meta: DEC/línea base) | Alerta de exactitud por debajo del objetivo | KPI-01 | RN-ALE-001 |

- **EV-ALE-007**: Sin HU propia

## 2.16 REP · Reportes y exportación (5)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-REP-001** | Datos exportados | Jefe / Administrador / Auditor / Coordinador | E-21 Registro de bitácora | E-21 Registro de bitácora | Exportación de un reporte, del kardex o de la bitácora | Exportación registrada con usuario, alcance y fecha, respetando la visibilidad por rol | — | RN-AUD-003 |
| **EV-REP-002** | Exportación analítica habilitada | Administrador | E-25 Parámetro de configuración | E-25 Parámetro de configuración | Decisión de alimentar la herramienta analítica externa | Datos expuestos de forma estructurada `[DC-06]` | — | RN-AUD-004 |
| **EV-REP-003** | Reporte programado | Jefe de Bodega | E-25 Parámetro de configuración | E-25 Parámetro de configuración | Definición de reporte, periodicidad y destinatarios | Programación vigente (puede desactivarse) | — | — |
| **EV-REP-004** | Reporte programado generado | Sistema | E-25 Parámetro de configuración | E-25 Parámetro de configuración | Llega la periodicidad programada | Reporte con fecha, hora y generador, puesto a disposición | — | — |
| **EV-REP-005** | Indicadores del período calculados | Sistema | E-15 Conteo | E-25 Parámetro de configuración | Cierre del período de cada KPI (diario, semanal, mensual) | Los 24 KPI calculados sobre el registro del sistema | KPI-02, KPI-03, KPI-04, KPI-05, KPI-06, KPI-07, KPI-08, KPI-09, KPI-10, KPI-11, KPI-12, KPI-13, KPI-14, KPI-15, KPI-16, KPI-17, KPI-18, KPI-19, KPI-20, KPI-21, KPI-22, KPI-23, KPI-24 | — |

## 2.17 AUD · Auditoría y control (6)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-AUD-001** | Observación de auditoría registrada | Auditor | E-22 Observación de auditoría | E-22 Observación de auditoría | Hallazgo o comentario del Auditor | Observación Abierta en registro separado; el inventario no cambia | — | RN-AUD-002 |
| **EV-AUD-002** | Observación de auditoría cerrada ⚠️ | Por definir (DEC-04) | E-22 Observación de auditoría | E-22 Observación de auditoría | Respuesta a la observación | Observación Cerrada con respuesta; no se elimina | — | RN-AUD-002, RN-MAE-007 |
| **EV-AUD-003** | Intento de escritura del Auditor rechazado | Sistema | E-19 Usuario | E-21 Registro de bitácora | El Auditor intenta cualquier escritura sobre el inventario | Rechazo sin excepción y registro del intento | — | RN-AUD-002 |
| **EV-AUD-004** | Operación no autorizada rechazada ⚠️ | Sistema | E-19 Usuario | E-21 Registro de bitácora | Cualquier rol intenta una operación fuera de sus permisos | Rechazo con usuario, operación y fecha (RNF-SEG-007) | — | RN-INT-001 |
| **EV-AUD-005** | Aprobación propia detectada | Sistema | E-21 Registro de bitácora | E-21 Registro de bitácora | Verificación encuentra solicitante = aprobador en ajuste, salida o conteo | Hallazgo crítico: la regla debió impedirlo | KPI-14 | RN-AJU-001 |
| **EV-AUD-006** | Discontinuidad de bitácora detectada | Sistema | E-21 Registro de bitácora | E-21 Registro de bitácora | Falta un eslabón en la secuencia de la bitácora | Hallazgo crítico de integridad | — | RN-AUD-001 |

- **EV-AUD-002**: Actor que responde no definido (DEC-04)
- **EV-AUD-004**: Respaldado por RNF-SEG-003, RNF-SEG-004, RNF-SEG-007

## 2.18 PAR · Configuración (5)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-PAR-001** | Parámetro modificado | Administrador | E-25 Parámetro de configuración | E-25 Parámetro de configuración | Cambio de un umbral, plazo o política dentro de su rango | Nuevo valor vigente hacia adelante; valor anterior y nuevo en bitácora | — | RN-AUD-004, RN-AJU-002, RN-SAL-001, RN-MOV-008, RN-CNT-003 |
| **EV-PAR-002** | Motivo tipificado creado | Administrador | E-24 Motivo tipificado | E-24 Motivo tipificado | Nueva causa para un tipo de operación | Motivo Activo, con indicación de si exige evidencia | — | RN-AJU-003 |
| **EV-PAR-003** | Motivo tipificado desactivado | Administrador | E-24 Motivo tipificado | E-24 Motivo tipificado | Motivo en desuso | Motivo Inactivo: fuera de operaciones nuevas, visible en el histórico | — | RN-MAE-007, RN-MAE-008 |
| **EV-PAR-004** | Configuración de regla estructural rechazada | Sistema | E-25 Parámetro de configuración | E-25 Parámetro de configuración | Intento de parametrizar o eludir una regla estructural | Rechazo y registro del intento | — | RN-INT-002, RN-EXI-001, RN-AJU-001 |
| **EV-PAR-005** | Motivo tipificado reactivado | Administrador | E-24 Motivo tipificado | E-24 Motivo tipificado | Motivo vuelve a usarse | Motivo Activo | — | RN-MAE-009 |

## 2.19 TAR · Tareas y notificaciones (6)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-TAR-001** | Tarea generada | Sistema | E-23 Tarea operativa | E-23 Tarea operativa | Asignación de trabajo de recepción, ubicación, preparación o transferencia | Tarea Pendiente en el panel del responsable (qué, dónde, cuánto) | — | RN-INT-001 |
| **EV-TAR-002** | Tarea completada | Sistema | E-23 Tarea operativa | E-23 Tarea operativa | Confirmación del hecho asociado | Tarea Completada; no se cierra por declaración | — | — |
| **EV-TAR-003** | Tarea reasignada | Coordinador | E-23 Tarea operativa | E-23 Tarea operativa | Equilibrio de carga o ausencia | Nuevo responsable notificado; ambos registrados | — | RN-CNT-003 |
| **EV-TAR-004** | Solicitud de aprobación notificada | Sistema | E-14 Solicitud de ajuste | E-19 Usuario | Solicitud de ajuste o salida pendiente para un aprobador | Solicitud visible en el panel del aprobador, ordenada por antigüedad y monto | KPI-22 | — |
| **EV-TAR-005** | Resultado notificado al solicitante | Sistema | E-14 Solicitud de ajuste | E-19 Usuario | Resolución de una solicitud | El solicitante conoce el resultado | — | — |
| **EV-TAR-006** | Tarea cancelada ⚠️ | Sistema | E-23 Tarea operativa | E-23 Tarea operativa | La operación de origen se cancela o vence | Tarea Cancelada | — | — |

- **EV-TAR-006**: Estado nuevo (HD-19)

## 2.20 JOR · Operación diaria (cierre de jornada) (5)

| ID | Nombre | Actor | Entidad origen | Entidad afectada | Disparador | Resultado esperado | KPI | Reglas (SRS) |
|---|---|---|---|---|---|---|---|---|
| **EV-JOR-001** | Pendientes de jornada consolidados ⚠️ | Sistema | E-26 Cierre de jornada | E-26 Cierre de jornada | Fin de jornada o de turno | Lista de recepciones sin confirmar, tránsitos, conteos abiertos, ajustes sin resolver, novedades y alertas | — | RN-MOV-006 |
| **EV-JOR-002** | Pendientes traspasados ⚠️ | Coordinador | E-26 Cierre de jornada | E-26 Cierre de jornada, E-23 Tarea operativa | Revisión de pendientes no resueltos en el turno | Responsabilidad de los pendientes traspasada explícitamente | — | — |
| **EV-JOR-003** | Jornada cerrada ⚠️ | Jefe / Coordinador | E-26 Cierre de jornada | E-26 Cierre de jornada | Resumen revisado y sin registros pendientes de sincronización | Cierre registrado con quién lo ejecutó | — | RN-INT-003 |
| **EV-JOR-004** | Cierre de jornada bloqueado ⚠️ | Sistema | E-26 Cierre de jornada | E-26 Cierre de jornada | Existen registros sin sincronizar | Cierre impedido hasta sincronizar (RNF-DSP-003) | — | RN-INT-003 |
| **EV-JOR-005** | Cierre de jornada omitido ⚠️ | Sistema | E-26 Cierre de jornada | E-26 Cierre de jornada, E-18 Alerta | Termina la jornada sin cierre | Omisión registrada; alerta al Jefe al día siguiente | — | — |

- **EV-JOR-001**: ⚠️ Sin HU ni RF (DEC-05)
- **EV-JOR-002**: ⚠️ Sin HU ni RF (DEC-05)
- **EV-JOR-003**: ⚠️ Sin HU ni RF (DEC-05)
- **EV-JOR-004**: ⚠️ Sin HU ni RF (DEC-05)
- **EV-JOR-005**: ⚠️ Sin HU ni RF (DEC-05)

---

**ESTADO DEL CAPÍTULO — 2**

| | |
|---|---|
| **Completado** | 168 eventos (mínimo exigido: 70) con IDs permanentes en 20 dominios y los ocho atributos pedidos |
| **Riesgos** | 24 eventos ⚠️ sin requisito completo que los implemente |
| **Dependencias** | DOMAIN_MODEL Caps. 3 y 8 · SRS Caps. 5–8 |
| **Hallazgos** | HD-11, HD-17, HD-19 · H-10, H-11, H-12 del SRS |

---

# CAPÍTULO 3 — LÍNEA TEMPORAL DE EVENTOS

> Orden en que ocurren los eventos en cada uno de los 14 procesos del MVP (SPEC Cap. 3; casos de uso del SRS Cap. 4). «A o B» indica alternativas excluyentes; el comentario indica cuándo ocurre un paso opcional.

## PN-01 · Recepción de mercancía (CU-06)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-ENT-001 | Documento de entrada creado | El Coordinador crea el documento |
| 2 | EV-ENT-002 | Posible duplicado advertido | si hay posible duplicado |
| 3 | EV-TAR-001 | Tarea generada | tarea de recepción |
| 4 | EV-ENT-003 | Recepción física iniciada | siempre |
| 5 | EV-ENT-004 | Línea de recepción registrada | una vez por línea |
| 6 | EV-ENT-016 | Pieza registrada en la recepción | por cada pieza de la línea |
| 7 | EV-TRZ-003 | Registro retenido sin conectividad | si se pierde la conectividad |
| 8 | EV-TRZ-004 | Registro sincronizado | al restablecerse, si sigue siendo válido |
| 9 | EV-TRZ-007 | Registro rechazado al sincronizar | si al sincronizar ya no es válido → EV-NOV-001 si describe un hecho físico |
| 10 | EV-ENT-005 | Recepción interrumpida | si se interrumpe |
| 11 | EV-ENT-006 | Recepción continuada | si otro usuario la continúa |
| 12 | EV-ENT-011 | Mercancía dañada registrada en recepción | si llega mercancía dañada → abre EV-NOV-001 |
| 13 | EV-ENT-007 o EV-ENT-008 o EV-ENT-009 | Recibido conforme determinado / Faltante de recepción registrado / Sobrante de recepción registrado | según la comparación |
| 14 | EV-ENT-010 | Sobrante autorizado | solo si hubo sobrante |
| 15 | EV-ENT-014 | Autoconfirmación de entrada rechazada | si el receptor intenta confirmar |
| 16 | EV-ENT-012 | Entrada confirmada | confirmación por una segunda persona |
| 17 | EV-LOT-001 | Lote creado | siempre |
| 18 | EV-TRZ-001 | Movimiento confirmado en el kardex | movimiento de entrada |
| 19 | EV-TAR-002 | Tarea completada | tarea de recepción completada |

## PN-02 · Registro inicial e identificación (CU-07)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-QRC-001 | Identificador QR generado | siempre |
| 2 | EV-QRC-002 | Identificador QR impreso | siempre |
| 3 | EV-QRC-003 | Identificador QR activado | tras adherir y escanear |
| 4 | EV-QRC-004 | Identificador QR reimpreso | si la impresión sale ilegible |
| 5 | EV-QRC-006 | Identificador secundario asociado | si viene código de barras del proveedor |

## PN-03 · Ubicación física de mercancía (CU-08)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-TAR-001 | Tarea generada | tarea de ubicación con propuesta |
| 2 | EV-MOV-003 | Movimiento interno interrumpido | si el traslado se interrumpe |
| 3 | EV-INV-001 | Mercancía ubicada | movimiento interno de primera ubicación (DF5-03) |
| 4 | EV-INV-002 | Desviación de ubicación registrada | si ubica en otro lugar |
| 5 | EV-INV-009 | Ubicación sobreocupada | si se excede la capacidad |
| 6 | EV-TRZ-001 | Movimiento confirmado en el kardex | siempre |
| 7 | EV-TAR-002 | Tarea completada | siempre |

## PN-04 · Consulta de existencia y ubicación (CU-09)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | — | — | La consulta no produce eventos: leer nunca escribe (RN-INT-006). Solo si el identificador no se reconoce puede seguir EV-NOV-001. |

## PN-05 · Movimiento interno (reubicación) (CU-10)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-MOV-002 | Movimiento interno rechazado | si alguna regla lo impide (fin) |
| 2 | EV-MOV-003 | Movimiento interno interrumpido | si se interrumpe |
| 3 | EV-MOV-004 | Tránsito interno prolongado detectado | si el tránsito se prolonga |
| 4 | EV-TRZ-003 | Registro retenido sin conectividad | si se pierde la conectividad |
| 5 | EV-TRZ-004 o EV-TRZ-007 | Registro sincronizado / Registro rechazado al sincronizar | al sincronizar: confirmado o rechazado (→ EV-NOV-001) |
| 6 | EV-MOV-001 | Movimiento interno confirmado | confirmación |
| 7 | EV-TRZ-001 | Movimiento confirmado en el kardex | siempre |

## PN-06 · Transferencia entre zonas o bodegas (CU-11)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-MOV-005 | Transferencia creada | siempre |
| 2 | EV-INV-003 | Existencia reservada | siempre |
| 3 | EV-TAR-001 | Tarea generada | tarea de despacho |
| 4 | EV-MOV-012 | Transferencia cancelada antes del despacho | si se cancela antes del despacho → EV-INV-004 (fin) |
| 5 | EV-MOV-006 | Despacho de transferencia confirmado | siempre |
| 6 | EV-MOV-011 | Tiempo máximo en tránsito excedido | si se excede el tiempo en tránsito |
| 7 | EV-MOV-013 | Transferencia cancelada en tránsito | si el Jefe la cancela en tránsito (fin) |
| 8 | EV-MOV-007 | Transferencia completada | si lo recibido coincide |
| 9 | EV-MOV-008 o EV-MOV-009 | Diferencia de transferencia registrada / Recepción de transferencia rechazada por exceso | si no coincide |
| 10 | EV-MOV-010 | Diferencia de transferencia resuelta | resolución del Jefe |
| 11 | EV-TRZ-001 | Movimiento confirmado en el kardex | movimientos de despacho y recepción |

## PN-07 · Ajuste de inventario (CU-12)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-AJU-001 | Ajuste solicitado | siempre |
| 2 | EV-AJU-007 | Ajuste negativo impedido | si dejaría existencia negativa (fin) |
| 3 | EV-AJU-002 | Ajuste clasificado y enrutado | siempre |
| 4 | EV-TAR-004 | Solicitud de aprobación notificada | siempre |
| 5 | EV-AJU-003 | Ajuste escalado por autoaprobación | si aprobador = solicitante |
| 6 | EV-AJU-010 | Solicitud bloqueada sin aprobador | si no hay nivel superior |
| 7 | EV-AJU-008 | Solicitud de ajuste vencida escalada | si vence el plazo |
| 8 | EV-AJU-004 o EV-AJU-006 | Ajuste aprobado / Ajuste rechazado | decisión |
| 9 | EV-AJU-005 | Ajuste aplicado | solo si fue aprobado |
| 10 | EV-TRZ-001 | Movimiento confirmado en el kardex | siempre |
| 11 | EV-TAR-005 | Resultado notificado al solicitante | siempre |
| 12 | EV-AJU-009 | Patrón de ajustes recurrentes detectado | si se acumulan ajustes sobre la misma unidad |

## PN-08 · Conteo cíclico (CU-13)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-CNT-001 | Conteo cíclico programado | siempre |
| 2 | EV-CNT-003 | Existencia teórica congelada | siempre |
| 3 | EV-CNT-006 | Tarea de conteo asignada | una por contador |
| 4 | EV-CNT-011 | Tarea de conteo reasignada | si un contador no está |
| 5 | EV-CNT-007 | Conteo físico registrado | sin ver lo esperado |
| 6 | EV-CNT-008 | Línea de conteo clasificada | siempre |
| 7 | EV-CNT-009 | Segundo conteo requerido | si la diferencia supera la tolerancia |
| 8 | EV-CNT-010 | Diferencia persistente escalada | si el segundo también difiere |
| 9 | EV-NOV-001 | Novedad reportada | si aparece mercancía sin identificador |
| 10 | EV-CNT-018 | Conteo vencido | si vence el plazo |
| 11 | EV-CNT-014 | Conteo cerrado | cierre por el Jefe |
| 12 | EV-AJU-001 | Ajuste solicitado | por cada línea que el Jefe decide ajustar → PN-07 |
| 13 | EV-CNT-015 | Exactitud del inventario calculada | siempre |
| 14 | EV-ALE-007 | Exactitud bajo el umbral detectada | si la exactitud queda bajo el umbral |

## PN-09 · Conteo general (CU-14)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-CNT-002 | Conteo general programado | siempre |
| 2 | EV-CNT-004 | Movimientos bloqueados por conteo general | al llegar el corte |
| 3 | EV-CNT-003 | Existencia teórica congelada | siempre |
| 4 | EV-CNT-006 | Tarea de conteo asignada | cubriendo todas las ubicaciones |
| 5 | EV-CNT-005 | Movimiento de excepción autorizado | si urge un movimiento de excepción |
| 6 | EV-CNT-007 | Conteo físico registrado | siempre |
| 7 | EV-CNT-008 | Línea de conteo clasificada | siempre |
| 8 | EV-CNT-009 | Segundo conteo requerido | siempre |
| 9 | EV-CNT-012 | Ubicación excluida del conteo general | si una ubicación se excluye |
| 10 | EV-CNT-013 | Diferencia global crítica detectada | si la diferencia global es crítica |
| 11 | EV-CNT-017 | Conteo abortado | si se aborta (→ EV-CNT-016, fin) |
| 12 | EV-CNT-014 | Conteo cerrado | siempre |
| 13 | EV-AJU-001 | Ajuste solicitado | ajustes derivados → PN-07 |
| 14 | EV-CNT-016 | Movimientos desbloqueados | siempre |
| 15 | EV-CNT-015 | Exactitud del inventario calculada | KPI-01 y KPI-02 |

## PN-10 · Salida de mercancía (CU-15)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-SAL-001 | Salida solicitada | siempre |
| 2 | EV-SAL-002 | Salida rechazada por existencia insuficiente | si no hay disponible suficiente |
| 3 | EV-SAL-004 | Salida escalada al Jefe | si supera el umbral del Coordinador |
| 4 | EV-TAR-004 | Solicitud de aprobación notificada | siempre |
| 5 | EV-SAL-003 o EV-SAL-009 | Salida autorizada / Salida rechazada por el autorizador | decisión |
| 6 | EV-SAL-007 | Salida parcial autorizada | salida parcial autorizada |
| 7 | EV-INV-003 | Existencia reservada | siempre |
| 8 | EV-TAR-001 | Tarea generada | tarea de preparación |
| 9 | EV-SAL-010 | Preparación de salida iniciada | siempre |
| 10 | EV-SAL-012 | Pieza tomada en la preparación | por cada pieza tomada |
| 11 | EV-SAL-013 | Corte parcial registrado | si se corta parte de un rollo |
| 12 | EV-SAL-005 | Escaneo de preparación rechazado | por cada escaneo incorrecto |
| 13 | EV-INV-005 | Reserva vencida liberada | si la reserva vence (fin) |
| 14 | EV-SAL-011 | Salida cancelada | si se cancela (fin) |
| 15 | EV-SAL-006 | Salida ejecutada | siempre |
| 16 | EV-SAL-008 | Baja por daño aprobada | si el motivo es baja por daño |
| 17 | EV-TRZ-001 | Movimiento confirmado en el kardex | siempre |
| 18 | EV-TAR-002 | Tarea completada | siempre |
| 19 | EV-INV-006 o EV-INV-008 | Existencia mínima alcanzada / Existencia en cero alcanzada | si la salida deja el SKU bajo el mínimo o en cero |

## PN-11 · Gestión de alerta operativa (CU-16)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-INV-006 … EV-INV-009 · EV-MOV-004 · EV-MOV-011 · EV-AJU-008 · EV-AJU-009 · EV-CNT-018 · EV-LOT-004 · EV-ALE-007 | Existencia mínima alcanzada / Ubicación sobreocupada / Tránsito interno prolongado detectado / Tiempo máximo en tránsito excedido / Solicitud de ajuste vencida escalada / Patrón de ajustes recurrentes detectado / Conteo vencido / Antigüedad de lote superada / Exactitud bajo el umbral detectada | condición detectada |
| 2 | EV-ALE-001 | Alerta generada | siempre |
| 3 | EV-ALE-004 | Alerta escalada | si es crítica y vence el plazo |
| 4 | EV-ALE-002 o EV-ALE-003 o EV-ALE-005 | Alerta atendida / Alerta descartada / Alerta cerrada automáticamente | desenlace |
| 5 | EV-ALE-006 | Frecuencia anómala de disparo reportada | si el tipo se dispara con frecuencia anómala |

## PN-12 · Reporte de novedad de mercancía (CU-17)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-NOV-001 o EV-NOV-002 | Novedad reportada / Novedad vinculada a novedad abierta | nueva o vinculada |
| 2 | EV-NOV-006 | Novedad escalada por vencimiento | si vence el plazo |
| 3 | EV-NOV-003 | Acción de novedad determinada | siempre |
| 4 | EV-AJU-001 | Ajuste solicitado | si implica ajuste → PN-07 |
| 5 | EV-NOV-007 | Mercancía sin registro incorporada | si es mercancía sin registro |
| 6 | EV-NOV-004 o EV-NOV-005 | Novedad resuelta y cerrada / Novedad cerrada como improcedente | cierre |

## PN-13 · Auditoría de inventario (CU-18)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-TRZ-005 | Verificación de integridad ejecutada | siempre |
| 2 | EV-TRZ-006 | Discrepancia de integridad detectada | si hay discrepancia |
| 3 | EV-AUD-005 | Aprobación propia detectada | si hay aprobación propia |
| 4 | EV-AUD-006 | Discontinuidad de bitácora detectada | si la bitácora tiene discontinuidad |
| 5 | EV-AUD-003 | Intento de escritura del Auditor rechazado | si el Auditor intenta escribir |
| 6 | EV-AUD-001 | Observación de auditoría registrada | siempre |
| 7 | EV-REP-001 | Datos exportados | exportación del reporte de auditoría |
| 8 | EV-AUD-002 | Observación de auditoría cerrada | al responderse la observación |

## PN-14 · Cierre operativo de jornada ⚠️ (CU-19)

| Orden | Evento(s) | Nombre | Cuándo |
|:--:|---|---|---|
| 1 | EV-JOR-001 | Pendientes de jornada consolidados | siempre |
| 2 | EV-JOR-004 | Cierre de jornada bloqueado | si hay registros sin sincronizar |
| 3 | EV-JOR-002 | Pendientes traspasados | siempre |
| 4 | EV-JOR-003 | Jornada cerrada | siempre |
| 5 | EV-JOR-005 | Cierre de jornada omitido | si nadie cierra |

---

**ESTADO DEL CAPÍTULO — 3**

| | |
|---|---|
| **Completado** | Línea temporal de los 14 procesos del MVP |
| **Riesgos** | PN-14 sin requisitos (DEC-05); PN-04 sin eventos por diseño (solo lectura) |
| **Dependencias** | SPEC Cap. 3 · SRS Cap. 4 |
| **Hallazgos** | HD-07 y HD-23 (orden entrada → primera ubicación, resueltos por DF5-02 y DF5-03) |

---

# CAPÍTULO 4 — EVENTOS AUDITABLES

> **Todo evento del catálogo queda registrado de forma permanente** —nada se purga (RNF-AUD-004)— en al menos uno de tres registros: **Kardex** (si altera la existencia, RN-INT-002), **Bitácora** (si es relevante para el control, RN-AUD-001) o **Historial** de su entidad. La criticidad indica la prioridad de revisión en una auditoría (PN-13).

## 4.1 Criterios de criticidad

| Criticidad | Criterio | Eventos |
|---|---|:--:|
| **Crítica** | Afecta la integridad del inventario, la segregación de funciones o las reglas estructurales: aprobaciones y rechazos de ajustes y salidas, anulaciones, inmovilizaciones, cierres de conteo, cambios de configuración y de rol, hallazgos de integridad, intentos de violar reglas estructurales. | 27 |
| **Alta** | Altera la existencia o un dato maestro, o registra acceso: movimientos confirmados, altas y desactivaciones, accesos, exportaciones, rechazos de control. | 66 |
| **Media** | Avance de un flujo de trabajo: solicitudes, recepciones, tareas, alertas generadas y atendidas. | 57 |
| **Baja** | Informativo o de apoyo: impresión, notificaciones, reportes programados, frecuencia de alertas. | 18 |

**Destino del registro permanente:** Bitácora 83 · Historial 70 · Kardex 9 · Kardex + Bitácora 6

## 4.2 Criticidad Crítica

| ID | Evento | Actor | Registro permanente | Reglas |
|---|---|---|---|---|
| EV-USR-002 | Rol cambiado | Administrador | Bitácora | RN-MAE-004 |
| EV-ENT-010 | Sobrante autorizado | Jefe de Bodega | Bitácora | RN-ENT-005, RN-AJU-001 |
| EV-LOT-002 | Lote inmovilizado | Jefe / Administrador | Bitácora | RN-LOT-003, RN-EXI-006 |
| EV-LOT-003 | Lote liberado | Jefe / Administrador | Bitácora | RN-LOT-004 |
| EV-MOV-013 | Transferencia cancelada en tránsito | Jefe de Bodega | Kardex + Bitácora | RN-MOV-009 |
| EV-SAL-003 | Salida autorizada | Jefe / Coordinador | Bitácora | RN-SAL-001, RN-AJU-001, RN-EXI-004, RN-SAL-003 |
| EV-SAL-008 | Baja por daño aprobada | Jefe de Bodega | Kardex + Bitácora | RN-SAL-006, RN-AJU-001 |
| EV-AJU-003 | Ajuste escalado por autoaprobación | Sistema | Bitácora | RN-AJU-001 |
| EV-AJU-004 | Ajuste aprobado | Jefe / Administrador | Bitácora | RN-AJU-001, RN-EXI-001 |
| EV-AJU-005 | Ajuste aplicado | Sistema | Kardex | RN-INT-004, RN-AJU-007, RN-EXI-001 |
| EV-AJU-006 | Ajuste rechazado | Jefe / Administrador | Bitácora | RN-AJU-006 |
| EV-AJU-007 | Ajuste negativo impedido | Sistema | Bitácora | RN-EXI-001 |
| EV-AJU-009 | Patrón de ajustes recurrentes detectado | Sistema | Bitácora | RN-AJU-004 |
| EV-AJU-010 | Solicitud bloqueada sin aprobador | Sistema | Bitácora | RN-AJU-001 |
| EV-CNT-004 | Movimientos bloqueados por conteo general | Sistema | Bitácora | RN-CNT-006 |
| EV-CNT-005 | Movimiento de excepción autorizado | Jefe de Bodega | Kardex + Bitácora | RN-CNT-006 |
| EV-CNT-013 | Diferencia global crítica detectada | Sistema | Bitácora | RN-CNT-008 |
| EV-CNT-014 | Conteo cerrado | Jefe de Bodega | Bitácora | RN-CNT-004, RN-CNT-003, RN-CNT-007, RN-AJU-001 |
| EV-NOV-007 | Mercancía sin registro incorporada | Coordinador / Jefe | Kardex + Bitácora | RN-NOV-001, RN-AJU-003 |
| EV-TRZ-002 | Movimiento anulado | Jefe / Administrador | Kardex + Bitácora | RN-INT-002 |
| EV-TRZ-006 | Discrepancia de integridad detectada | Sistema | Bitácora | RN-INT-004 |
| EV-REP-002 | Exportación analítica habilitada | Administrador | Bitácora | RN-AUD-004 |
| EV-AUD-003 | Intento de escritura del Auditor rechazado | Sistema | Bitácora | RN-AUD-002 |
| EV-AUD-005 | Aprobación propia detectada | Sistema | Bitácora | RN-AJU-001 |
| EV-AUD-006 | Discontinuidad de bitácora detectada | Sistema | Bitácora | RN-AUD-001 |
| EV-PAR-001 | Parámetro modificado | Administrador | Bitácora | RN-AUD-004, RN-AJU-002, RN-SAL-001, RN-MOV-008, RN-CNT-003 |
| EV-PAR-004 | Configuración de regla estructural rechazada | Sistema | Bitácora | RN-INT-002, RN-EXI-001, RN-AJU-001 |

## 4.3 Criticidad Alta

| ID | Evento | Actor | Registro permanente | Reglas |
|---|---|---|---|---|
| EV-ACC-001 | Sesión iniciada | Cualquier usuario | Bitácora | RN-INT-001 |
| EV-ACC-002 | Acceso rechazado | Cualquier persona | Bitácora | RN-INT-001 |
| EV-ACC-003 | Cuenta bloqueada | Sistema | Bitácora | — |
| EV-ACC-006 | Contraseña cambiada | Cualquier usuario | Bitácora | — |
| EV-ACC-007 | Acceso restablecido | Administrador | Bitácora | — |
| EV-USR-001 | Usuario creado | Administrador | Bitácora | RN-INT-001, RN-MAE-006 |
| EV-USR-004 | Usuario desactivado | Administrador | Bitácora | RN-MAE-004, RN-MAE-007 |
| EV-USR-005 | Usuario reactivado | Administrador | Bitácora | RN-MAE-009 |
| EV-USR-006 | Retiro del último Administrador o Jefe rechazado | Sistema | Bitácora | RN-MAE-004 |
| EV-CAT-001 | Referencia creada | Administrador / Jefe | Bitácora | RN-MAE-001 |
| EV-CAT-003 | Unidad de medida asignada | Administrador / Jefe | Bitácora | RN-MAE-002, RN-INT-007 |
| EV-CAT-005 | Referencia desactivada | Administrador / Jefe | Bitácora | RN-MAE-003, RN-MAE-007, RN-MAE-008 |
| EV-CAT-006 | Referencia reactivada | Administrador / Jefe | Bitácora | RN-MAE-009 |
| EV-CAT-007 | Catálogo cargado masivamente | Administrador | Bitácora | RN-MAE-001 |
| EV-BOD-001 | Bodega creada | Administrador | Bitácora | RN-EXI-002 |
| EV-BOD-002 | Zona creada | Administrador | Bitácora | RN-EXI-002 |
| EV-BOD-003 | Ubicación creada | Administrador | Bitácora | RN-MAE-006 |
| EV-BOD-005 | Ubicación desactivada | Administrador | Bitácora | RN-MAE-005, RN-MAE-007 |
| EV-BOD-006 | Ubicación reactivada | Administrador | Bitácora | RN-MAE-009 |
| EV-QRC-001 | Identificador QR generado | Sistema / Coordinador | Historial | RN-IDE-002 |
| EV-QRC-004 | Identificador QR reimpreso | Coordinador / Auxiliar | Bitácora | RN-IDE-004, RN-IDE-002 |
| EV-QRC-005 | Identificador QR anulado | Coordinador | Bitácora | RN-IDE-002 |
| EV-ENT-008 | Faltante de recepción registrado | Sistema | Historial | RN-ENT-004 |
| EV-ENT-009 | Sobrante de recepción registrado | Sistema | Historial | RN-ENT-005 |
| EV-ENT-011 | Mercancía dañada registrada en recepción | Auxiliar | Historial | RN-ENT-006 |
| EV-ENT-012 | Entrada confirmada | Coordinador | Kardex + Bitácora | RN-ENT-007, RN-EXI-007, RN-INT-002, RN-INT-004, RN-INT-003, RN-LOT-001 |
| EV-ENT-013 | Retorno registrado como entrada | Coordinador | Kardex | RN-SAL-007 |
| EV-ENT-014 | Autoconfirmación de entrada rechazada | Sistema | Bitácora | RN-ENT-007 |
| EV-ENT-016 | Pieza registrada en la recepción | Auxiliar | Historial | RN-LOT-006, RN-LOT-007 |
| EV-LOT-001 | Lote creado | Sistema | Historial | RN-LOT-001, RN-LOT-002, RN-MAE-006 |
| EV-INV-001 | Mercancía ubicada | Auxiliar | Kardex | RN-MOV-010, RN-MOV-004, RN-EXI-002, RN-MOV-002, RN-MOV-001, RN-MOV-011 |
| EV-MOV-001 | Movimiento interno confirmado | Auxiliar | Kardex | RN-MOV-004, RN-MOV-005, RN-INT-002, RN-EXI-003, RN-MOV-011 |
| EV-MOV-006 | Despacho de transferencia confirmado | Auxiliar (origen) | Kardex | RN-EXI-005 |
| EV-MOV-007 | Transferencia completada | Auxiliar (destino) | Kardex | RN-MOV-007, RN-INT-002 |
| EV-MOV-008 | Diferencia de transferencia registrada | Sistema | Historial | RN-MOV-007 |
| EV-MOV-009 | Recepción de transferencia rechazada por exceso | Sistema | Bitácora | RN-MOV-007 |
| EV-MOV-010 | Diferencia de transferencia resuelta | Jefe de Bodega | Bitácora | RN-MOV-007 |
| EV-MOV-012 | Transferencia cancelada antes del despacho | Coordinador | Bitácora | RN-MOV-009 |
| EV-SAL-006 | Salida ejecutada | Auxiliar | Kardex | RN-EXI-001, RN-INT-002, RN-INT-004 |
| EV-SAL-007 | Salida parcial autorizada | Jefe de Bodega | Bitácora | RN-EXI-001, RN-AJU-001 |
| EV-SAL-009 | Salida rechazada por el autorizador | Jefe / Coordinador | Bitácora | RN-AJU-001 |
| EV-SAL-011 | Salida cancelada | Jefe / Coordinador | Bitácora | RN-EXI-004 |
| EV-SAL-013 | Corte parcial registrado | Auxiliar | Kardex | RN-SAL-008, RN-LOT-007 |
| EV-AJU-001 | Ajuste solicitado | Coordinador | Bitácora | RN-AJU-003, RN-EXI-001 |
| EV-AJU-008 | Solicitud de ajuste vencida escalada | Sistema | Bitácora | RN-AJU-005 |
| EV-CNT-002 | Conteo general programado | Jefe de Bodega | Bitácora | RN-CNT-006 |
| EV-CNT-003 | Existencia teórica congelada | Sistema | Historial | RN-CNT-001 |
| EV-CNT-010 | Diferencia persistente escalada | Sistema | Historial | RN-CNT-003 |
| EV-CNT-012 | Ubicación excluida del conteo general | Jefe de Bodega | Bitácora | RN-CNT-007 |
| EV-CNT-015 | Exactitud del inventario calculada | Sistema | Historial | RN-CNT-004 |
| EV-CNT-016 | Movimientos desbloqueados | Sistema | Bitácora | RN-CNT-006 |
| EV-CNT-017 | Conteo abortado | Jefe de Bodega | Bitácora | — |
| EV-TRZ-001 | Movimiento confirmado en el kardex | Usuario / Sistema | Kardex | RN-INT-001, RN-INT-002, RN-INT-004, RN-LOT-007 |
| EV-TRZ-005 | Verificación de integridad ejecutada | Auditor | Bitácora | RN-AUD-005, RN-INT-004 |
| EV-TRZ-007 | Registro rechazado al sincronizar | Sistema | Bitácora | RN-INT-008 |
| EV-ALE-003 | Alerta descartada | Jefe / Coordinador | Bitácora | RN-ALE-004 |
| EV-ALE-004 | Alerta escalada | Sistema | Bitácora | RN-ALE-002 |
| EV-REP-001 | Datos exportados | Jefe / Administrador / Auditor / Coordinador | Bitácora | RN-AUD-003 |
| EV-AUD-001 | Observación de auditoría registrada | Auditor | Bitácora | RN-AUD-002 |
| EV-AUD-002 | Observación de auditoría cerrada | Por definir (DEC-04) | Bitácora | RN-AUD-002, RN-MAE-007 |
| EV-AUD-004 | Operación no autorizada rechazada | Sistema | Bitácora | RN-INT-001 |
| EV-PAR-002 | Motivo tipificado creado | Administrador | Bitácora | RN-AJU-003 |
| EV-PAR-003 | Motivo tipificado desactivado | Administrador | Bitácora | RN-MAE-007, RN-MAE-008 |
| EV-PAR-005 | Motivo tipificado reactivado | Administrador | Bitácora | RN-MAE-009 |
| EV-JOR-003 | Jornada cerrada | Jefe / Coordinador | Bitácora | RN-INT-003 |
| EV-JOR-004 | Cierre de jornada bloqueado | Sistema | Bitácora | RN-INT-003 |

## 4.4 Criticidad Media

| ID | Evento | Actor | Registro permanente | Reglas |
|---|---|---|---|---|
| EV-ACC-004 | Sesión cerrada por inactividad | Sistema | Bitácora | RN-INT-001 |
| EV-USR-003 | Ámbito asignado | Administrador | Bitácora | — |
| EV-CAT-002 | SKU generados | Sistema | Historial | RN-LOT-002 |
| EV-CAT-004 | Umbrales de existencia definidos | Administrador / Jefe | Bitácora | RN-AUD-004 |
| EV-CAT-008 | Categoría registrada | Administrador / Jefe | Bitácora | RN-MOV-001 |
| EV-CAT-009 | Categoría desactivada | Administrador / Jefe | Bitácora | RN-MAE-007, RN-MAE-008 |
| EV-BOD-004 | Capacidad de ubicación definida | Administrador | Bitácora | RN-MOV-002 |
| EV-BOD-007 | Coordinador asignado a zona | Administrador | Bitácora | RN-ALE-005 |
| EV-BOD-008 | Criterios de asignación configurados | Administrador | Bitácora | RN-MOV-001 |
| EV-QRC-003 | Identificador QR activado | Auxiliar | Historial | RN-IDE-001 |
| EV-QRC-006 | Identificador secundario asociado | Coordinador | Historial | RN-IDE-003 |
| EV-QRC-007 | QR de ubicación generado | Sistema / Administrador | Historial | RN-IDE-002 |
| EV-ENT-001 | Documento de entrada creado | Coordinador | Historial | RN-ENT-001 |
| EV-ENT-004 | Línea de recepción registrada | Auxiliar | Historial | RN-INT-003 |
| EV-ENT-005 | Recepción interrumpida | Auxiliar | Historial | — |
| EV-ENT-006 | Recepción continuada | Auxiliar | Historial | RN-INT-001 |
| EV-ENT-007 | Recibido conforme determinado | Sistema | Historial | RN-ENT-003 |
| EV-ENT-015 | Documento de entrada reversado | Coordinador | Bitácora | RN-MAE-007 |
| EV-INV-003 | Existencia reservada | Sistema | Historial | RN-EXI-004, RN-EXI-003 |
| EV-INV-004 | Reserva liberada | Sistema | Historial | RN-EXI-004, RN-MOV-009 |
| EV-INV-005 | Reserva vencida liberada | Sistema | Historial | RN-SAL-005 |
| EV-INV-006 | Existencia mínima alcanzada | Sistema | Historial | RN-ALE-001, RN-ALE-005 |
| EV-INV-007 | Existencia máxima superada | Sistema | Historial | RN-ALE-001 |
| EV-INV-008 | Existencia en cero alcanzada | Sistema | Historial | RN-ALE-001 |
| EV-INV-009 | Ubicación sobreocupada | Sistema | Historial | RN-MOV-002, RN-ALE-001 |
| EV-MOV-002 | Movimiento interno rechazado | Sistema | Bitácora | RN-EXI-003, RN-MOV-005, RN-MOV-002, RN-EXI-006 |
| EV-MOV-003 | Movimiento interno interrumpido | Auxiliar / Sistema | Historial | RN-MOV-006, RN-EXI-005 |
| EV-MOV-004 | Tránsito interno prolongado detectado | Sistema | Historial | RN-MOV-006 |
| EV-MOV-005 | Transferencia creada | Coordinador | Historial | RN-EXI-003, RN-EXI-004 |
| EV-MOV-011 | Tiempo máximo en tránsito excedido | Sistema | Historial | RN-MOV-008 |
| EV-SAL-001 | Salida solicitada | Jefe / Coordinador | Historial | RN-SAL-002, RN-EXI-003 |
| EV-SAL-002 | Salida rechazada por existencia insuficiente | Sistema | Bitácora | RN-EXI-001, RN-EXI-003 |
| EV-SAL-004 | Salida escalada al Jefe | Sistema | Historial | RN-SAL-001 |
| EV-SAL-005 | Escaneo de preparación rechazado | Sistema | Historial | RN-SAL-004 |
| EV-SAL-012 | Pieza tomada en la preparación | Auxiliar | Historial | RN-SAL-009, RN-MOV-011 |
| EV-AJU-002 | Ajuste clasificado y enrutado | Sistema | Historial | RN-AJU-002, RN-EXI-006 |
| EV-CNT-001 | Conteo cíclico programado | Coordinador | Historial | — |
| EV-CNT-007 | Conteo físico registrado | Auxiliar | Historial | RN-CNT-002, RN-CNT-009 |
| EV-CNT-008 | Línea de conteo clasificada | Sistema | Historial | RN-CNT-001 |
| EV-CNT-009 | Segundo conteo requerido | Sistema | Historial | RN-CNT-003 |
| EV-CNT-011 | Tarea de conteo reasignada | Coordinador | Historial | RN-CNT-003 |
| EV-CNT-018 | Conteo vencido | Sistema | Historial | RN-CNT-005 |
| EV-NOV-001 | Novedad reportada | Auxiliar (o rol operativo) · Sistema, al rechazar un registro sincronizado | Historial | RN-NOV-003, RN-INT-008 |
| EV-NOV-003 | Acción de novedad determinada | Coordinador | Historial | — |
| EV-NOV-004 | Novedad resuelta y cerrada | Coordinador / Jefe | Historial | RN-MAE-007 |
| EV-NOV-005 | Novedad cerrada como improcedente | Coordinador / Jefe | Historial | RN-MAE-007 |
| EV-NOV-006 | Novedad escalada por vencimiento | Sistema | Historial | RN-NOV-002 |
| EV-TRZ-003 | Registro retenido sin conectividad | Sistema | Historial | RN-INT-003 |
| EV-TRZ-004 | Registro sincronizado | Sistema | Historial | RN-INT-003, RN-INT-008 |
| EV-ALE-001 | Alerta generada | Sistema | Historial | RN-ALE-001, RN-ALE-005 |
| EV-ALE-002 | Alerta atendida | Jefe / Coordinador | Historial | — |
| EV-ALE-007 | Exactitud bajo el umbral detectada | Sistema | Historial | RN-ALE-001 |
| EV-REP-003 | Reporte programado | Jefe de Bodega | Bitácora | — |
| EV-TAR-003 | Tarea reasignada | Coordinador | Historial | RN-CNT-003 |
| EV-JOR-001 | Pendientes de jornada consolidados | Sistema | Historial | RN-MOV-006 |
| EV-JOR-002 | Pendientes traspasados | Coordinador | Bitácora | — |
| EV-JOR-005 | Cierre de jornada omitido | Sistema | Bitácora | — |

## 4.5 Criticidad Baja

| ID | Evento | Actor | Registro permanente | Reglas |
|---|---|---|---|---|
| EV-ACC-005 | Sesión cerrada por el usuario | Cualquier usuario | Bitácora | — |
| EV-QRC-002 | Identificador QR impreso | Coordinador | Historial | — |
| EV-ENT-002 | Posible duplicado advertido | Sistema | Historial | RN-ENT-002 |
| EV-ENT-003 | Recepción física iniciada | Auxiliar | Historial | RN-INT-001 |
| EV-LOT-004 | Antigüedad de lote superada | Sistema | Historial | RN-LOT-005 |
| EV-INV-002 | Desviación de ubicación registrada | Sistema | Historial | RN-MOV-003 |
| EV-SAL-010 | Preparación de salida iniciada | Auxiliar | Historial | RN-SAL-003, RN-SAL-004 |
| EV-CNT-006 | Tarea de conteo asignada | Sistema / Coordinador | Historial | RN-CNT-003 |
| EV-NOV-002 | Novedad vinculada a novedad abierta | Sistema | Historial | RN-NOV-003 |
| EV-ALE-005 | Alerta cerrada automáticamente | Sistema | Historial | RN-ALE-003 |
| EV-ALE-006 | Frecuencia anómala de disparo reportada | Sistema | Historial | RN-ALE-001 |
| EV-REP-004 | Reporte programado generado | Sistema | Historial | — |
| EV-REP-005 | Indicadores del período calculados | Sistema | Historial | — |
| EV-TAR-001 | Tarea generada | Sistema | Historial | RN-INT-001 |
| EV-TAR-002 | Tarea completada | Sistema | Historial | — |
| EV-TAR-004 | Solicitud de aprobación notificada | Sistema | Historial | — |
| EV-TAR-005 | Resultado notificado al solicitante | Sistema | Historial | — |
| EV-TAR-006 | Tarea cancelada | Sistema | Historial | — |

## 4.6 Reglas de auditoría de eventos

1. Los eventos **Críticos** y **Altos** se registran siempre en la bitácora o en el kardex, con actor, fecha operativa y detalle suficiente para reconstruirlos (RNF-AUD-001).
2. Los cambios de configuración registran **valor anterior y nuevo** (RN-AUD-004).
3. Los eventos de rechazo por reglas estructurales o de segregación (EV-ENT-014, EV-AJU-007, EV-AUD-003, EV-AUD-004, EV-PAR-004) son **Críticos o Altos aunque no cambien el inventario**: prueban que el control funcionó.
4. La discontinuidad de la bitácora (EV-AUD-006) y la discrepancia de integridad (EV-TRZ-006) son **hallazgos críticos** que se notifican al Administrador.


---

**ESTADO DEL CAPÍTULO — 4**

| | |
|---|---|
| **Completado** | Clasificación de los 168 eventos por criticidad (Crítica 27, Alta 66, Media 57, Baja 18) y registro permanente |
| **Riesgos** | La continuidad de la bitácora debe poder demostrarse (RF5-07) |
| **Dependencias** | SRS RNF-AUD-001…005 · RN-AUD-001 |
| **Hallazgos** | — |

---

# CAPÍTULO 5 — EVENTOS DERIVADOS

> Eventos que el **Sistema** genera automáticamente cuando una regla de negocio o un umbral configurado evalúa verdadera su condición. **No hay inteligencia artificial**: cada evento derivado cita la regla que lo produce (DC-07). Son la manifestación operativa de la «inteligencia» del producto.

| ID | Evento derivado | Condición / regla | Parámetro configurable | ¿Genera alerta? | Criticidad |
|---|---|---|---|:--:|:--:|
| EV-ACC-003 | Cuenta bloqueada | Umbral configurable de intentos fallidos (RF-ACC-004) | Intentos fallidos | — | Alta |
| EV-ACC-004 | Sesión cerrada por inactividad | Plazo de inactividad configurado (RF-ACC-005) | Tiempo de inactividad | — | Media |
| EV-USR-006 | Retiro del último Administrador o Jefe rechazado | RN-MAE-004 | — | — | Alta |
| EV-CAT-002 | SKU generados | Regla de composición del SKU (CD-05) | — | — | Media |
| EV-ENT-002 | Posible duplicado advertido | RN-ENT-002 | — | — | Baja |
| EV-ENT-007 | Recibido conforme determinado | RN-ENT-003 | — | — | Media |
| EV-ENT-008 | Faltante de recepción registrado | RN-ENT-004 | — | — | Alta |
| EV-ENT-009 | Sobrante de recepción registrado | RN-ENT-005 | — | — | Alta |
| EV-ENT-014 | Autoconfirmación de entrada rechazada | RN-ENT-007 | — | — | Alta |
| EV-LOT-004 | Antigüedad de lote superada | RN-LOT-005 | Umbral de antigüedad | Sí | Baja |
| EV-INV-002 | Desviación de ubicación registrada | RN-MOV-003 | — | — | Baja |
| EV-INV-005 | Reserva vencida liberada | RN-SAL-005 | Plazo de reserva | — | Media |
| EV-INV-006 | Existencia mínima alcanzada | Umbral mínimo por SKU (RF-CAT-007) + RN-ALE-001 | Existencia mínima por SKU | Sí | Media |
| EV-INV-007 | Existencia máxima superada | Umbral máximo por SKU (RF-CAT-007) + RN-ALE-001 | Existencia máxima por SKU | Sí | Media |
| EV-INV-008 | Existencia en cero alcanzada | Tipo de alerta «existencia en cero» (RF-ALE-004) | — | Sí | Media |
| EV-INV-009 | Ubicación sobreocupada | RN-MOV-002 | Capacidad de ubicación | Sí | Media |
| EV-MOV-002 | Movimiento interno rechazado | RN-EXI-003, RN-MOV-005, RN-MOV-002, RN-EXI-006 | — | — | Media |
| EV-MOV-004 | Tránsito interno prolongado detectado | RN-MOV-006 | Tiempo máximo en tránsito | Sí | Media |
| EV-MOV-008 | Diferencia de transferencia registrada | RN-MOV-007 | — | — | Alta |
| EV-MOV-009 | Recepción de transferencia rechazada por exceso | RN-MOV-007 | — | — | Alta |
| EV-MOV-011 | Tiempo máximo en tránsito excedido | RN-MOV-008 | Tiempo máximo en tránsito | Sí | Media |
| EV-SAL-002 | Salida rechazada por existencia insuficiente | RN-EXI-001 | — | — | Media |
| EV-SAL-004 | Salida escalada al Jefe | RN-SAL-001 | Umbral de autorización del Coordinador | — | Media |
| EV-SAL-005 | Escaneo de preparación rechazado | RN-SAL-004 | — | — | Media |
| EV-AJU-002 | Ajuste clasificado y enrutado | RN-AJU-002 | Umbral ajuste menor/mayor | — | Media |
| EV-AJU-003 | Ajuste escalado por autoaprobación | RN-AJU-001 | — | — | Crítica |
| EV-AJU-007 | Ajuste negativo impedido | RN-EXI-001 | — | — | Crítica |
| EV-AJU-008 | Solicitud de ajuste vencida escalada | RN-AJU-005 | Plazo de aprobación | Sí | Alta |
| EV-AJU-009 | Patrón de ajustes recurrentes detectado | RN-AJU-004 | Umbral y ventana de ajustes recurrentes | Sí | Crítica |
| EV-AJU-010 | Solicitud bloqueada sin aprobador | RN-AJU-001 | — | — | Crítica |
| EV-CNT-004 | Movimientos bloqueados por conteo general | RN-CNT-006 | Fecha de corte | — | Crítica |
| EV-CNT-008 | Línea de conteo clasificada | Regla de clasificación (CD-27) | — | — | Media |
| EV-CNT-009 | Segundo conteo requerido | RN-CNT-003 | Tolerancia de conteo | — | Media |
| EV-CNT-010 | Diferencia persistente escalada | RN-CNT-003 | — | — | Alta |
| EV-CNT-013 | Diferencia global crítica detectada | RN-CNT-008 | Umbral crítico de diferencia global | — | Crítica |
| EV-CNT-015 | Exactitud del inventario calculada | Fórmula de KPI-01 | — | — | Alta |
| EV-CNT-016 | Movimientos desbloqueados | RN-CNT-006 | — | — | Alta |
| EV-CNT-018 | Conteo vencido | RN-CNT-005 | Plazo de conteo | Sí | Media |
| EV-NOV-002 | Novedad vinculada a novedad abierta | RN-NOV-003 | — | — | Baja |
| EV-NOV-006 | Novedad escalada por vencimiento | RN-NOV-002 | Plazo de resolución de novedad | Sí | Media |
| EV-TRZ-003 | Registro retenido sin conectividad | RN-INT-003 | — | — | Media |
| EV-TRZ-004 | Registro sincronizado | RN-INT-003, RN-INT-008 | — | — | Media |
| EV-TRZ-007 | Registro rechazado al sincronizar | RN-INT-008 | — | — | Alta |
| EV-TRZ-006 | Discrepancia de integridad detectada | RN-INT-004 | — | — | Crítica |
| EV-ALE-001 | Alerta generada | RN-ALE-001 | — | — | Media |
| EV-ALE-004 | Alerta escalada | RN-ALE-002 | Plazo de atención por severidad | — | Alta |
| EV-ALE-005 | Alerta cerrada automáticamente | RN-ALE-003 | — | — | Baja |
| EV-ALE-006 | Frecuencia anómala de disparo reportada | PN-11 E-04 | — | — | Baja |
| EV-ALE-007 | Exactitud bajo el umbral detectada | Tipo de alerta «exactitud por debajo del objetivo» (RF-ALE-004) | Umbral de exactitud | Sí | Media |
| EV-REP-004 | Reporte programado generado | Periodicidad programada (RF-REP-007) | Periodicidad del reporte | — | Baja |
| EV-REP-005 | Indicadores del período calculados | Frecuencia de cada KPI (SPEC Cap. 10) | Frecuencia de cada KPI | — | Baja |
| EV-AUD-003 | Intento de escritura del Auditor rechazado | RN-AUD-002 / PR-02 | — | — | Crítica |
| EV-AUD-004 | Operación no autorizada rechazada | Matriz de segregación §2.7 | — | — | Alta |
| EV-AUD-005 | Aprobación propia detectada | RN-AJU-001 | — | — | Crítica |
| EV-AUD-006 | Discontinuidad de bitácora detectada | RN-AUD-001 | — | — | Crítica |
| EV-PAR-004 | Configuración de regla estructural rechazada | RF-PAR-006 / IN-67 | — | — | Crítica |
| EV-TAR-002 | Tarea completada | IN-69 | — | — | Baja |
| EV-TAR-006 | Tarea cancelada | Cancelación o vencimiento del origen | — | — | Baja |
| EV-JOR-001 | Pendientes de jornada consolidados | PN-14 | — | — | Media |
| EV-JOR-004 | Cierre de jornada bloqueado | RN-INT-003 | — | — | Alta |
| EV-JOR-005 | Cierre de jornada omitido | PN-14 E-03 | — | Sí | Media |

**Ejemplos pedidos por el Prompt #004:**

| Ejemplo del prompt | Evento del catálogo | Observación |
|---|---|---|
| Stock mínimo alcanzado | **EV-INV-006 Existencia mínima alcanzada** | Se evita el término prohibido «stock» (HD-14) |
| Conteo vencido | **EV-CNT-018 Conteo vencido** | RN-CNT-005 |
| Lote inconsistente | **EV-TRZ-006 Discrepancia de integridad detectada** (alcance lote) | El SPEC no define «lote inconsistente»; la verificación por lote es RF-KDX-006 (HD-14) |


---

**ESTADO DEL CAPÍTULO — 5**

| | |
|---|---|
| **Completado** | 61 eventos derivados, todos por regla o umbral explícitos, sin IA |
| **Riesgos** | Umbrales sin calibrar hasta tener línea base; escalas de severidad sin definir (HD-15) |
| **Dependencias** | DOMAIN_MODEL Cap. 6.2 (políticas) · SRS Cap. 8 |
| **Hallazgos** | HD-14, HD-15 |

---

# CAPÍTULO 6 — MATRICES D Y E

## Matriz D — Evento ↔ Historia de usuario

| Evento | Nombre | Historias de usuario (SRS) |
|---|---|---|
| EV-ACC-001 | Sesión iniciada | HU-ACC-001 |
| EV-ACC-002 | Acceso rechazado | HU-ACC-001 |
| EV-ACC-003 | Cuenta bloqueada | HU-ACC-001 |
| EV-ACC-004 | Sesión cerrada por inactividad | HU-ACC-002 |
| EV-ACC-005 | Sesión cerrada por el usuario | HU-ACC-002 |
| EV-ACC-006 | Contraseña cambiada | HU-ACC-003 |
| EV-ACC-007 | Acceso restablecido | HU-ACC-004 |
| EV-USR-001 | Usuario creado | HU-USR-001 |
| EV-USR-002 | Rol cambiado | HU-USR-003 |
| EV-USR-003 | Ámbito asignado | HU-USR-004 |
| EV-USR-004 | Usuario desactivado | HU-USR-002 |
| EV-USR-005 | Usuario reactivado | HU-USR-002 |
| EV-USR-006 | Retiro del último Administrador o Jefe rechazado | HU-USR-005, HU-USR-003 |
| EV-CAT-001 | Referencia creada | HU-CAT-001 |
| EV-CAT-002 | SKU generados | HU-CAT-001 |
| EV-CAT-003 | Unidad de medida asignada | HU-CAT-002 |
| EV-CAT-004 | Umbrales de existencia definidos | HU-CAT-004 |
| EV-CAT-005 | Referencia desactivada | HU-CAT-003 |
| EV-CAT-006 | Referencia reactivada | HU-CAT-003 |
| EV-CAT-007 | Catálogo cargado masivamente | HU-CAT-005 |
| EV-CAT-008 | Categoría registrada | HU-CAT-006 |
| EV-CAT-009 | Categoría desactivada | HU-CAT-006 |
| EV-BOD-001 | Bodega creada | HU-BOD-001 |
| EV-BOD-002 | Zona creada | HU-BOD-001 |
| EV-BOD-003 | Ubicación creada | HU-BOD-001 |
| EV-BOD-004 | Capacidad de ubicación definida | HU-BOD-002 |
| EV-BOD-005 | Ubicación desactivada | HU-BOD-003 |
| EV-BOD-006 | Ubicación reactivada | HU-BOD-003 |
| EV-BOD-007 | Coordinador asignado a zona | HU-BOD-004 |
| EV-BOD-008 | Criterios de asignación configurados | HU-BOD-005 |
| EV-QRC-001 | Identificador QR generado | HU-QRC-001 |
| EV-QRC-002 | Identificador QR impreso | HU-QRC-001 |
| EV-QRC-003 | Identificador QR activado | HU-QRC-002 |
| EV-QRC-004 | Identificador QR reimpreso | HU-QRC-004 |
| EV-QRC-005 | Identificador QR anulado | HU-QRC-002 |
| EV-QRC-006 | Identificador secundario asociado | HU-QRC-005 |
| EV-QRC-007 | QR de ubicación generado | HU-QRC-003, HU-BOD-001 |
| EV-ENT-001 | Documento de entrada creado | HU-ENT-001, HU-ENT-007 |
| EV-ENT-002 | Posible duplicado advertido | HU-ENT-001 |
| EV-ENT-003 | Recepción física iniciada | HU-ENT-002 |
| EV-ENT-004 | Línea de recepción registrada | HU-ENT-002 |
| EV-ENT-005 | Recepción interrumpida | HU-ENT-002 |
| EV-ENT-006 | Recepción continuada | HU-ENT-002 |
| EV-ENT-007 | Recibido conforme determinado | HU-ENT-004 |
| EV-ENT-008 | Faltante de recepción registrado | HU-ENT-004 |
| EV-ENT-009 | Sobrante de recepción registrado | HU-ENT-004 |
| EV-ENT-010 | Sobrante autorizado | HU-ENT-004 |
| EV-ENT-011 | Mercancía dañada registrada en recepción | HU-ENT-005 |
| EV-ENT-012 | Entrada confirmada | HU-ENT-003 |
| EV-ENT-013 | Retorno registrado como entrada | HU-SAL-006 |
| EV-ENT-014 | Autoconfirmación de entrada rechazada | HU-ENT-003 |
| EV-ENT-015 | Documento de entrada reversado | — ⚠️ |
| EV-ENT-016 | Pieza registrada en la recepción | HU-ENT-009, HU-ENT-010 |
| EV-LOT-001 | Lote creado | HU-LOT-001 |
| EV-LOT-002 | Lote inmovilizado | HU-LOT-003, HU-LOT-002, HU-KDX-004 |
| EV-LOT-003 | Lote liberado | HU-LOT-003 |
| EV-LOT-004 | Antigüedad de lote superada | HU-LOT-004 |
| EV-INV-001 | Mercancía ubicada | HU-ENT-006, HU-MOV-008 |
| EV-INV-002 | Desviación de ubicación registrada | HU-ENT-006 |
| EV-INV-003 | Existencia reservada | HU-SAL-002, HU-MOV-003 |
| EV-INV-004 | Reserva liberada | HU-SAL-002, HU-MOV-007 |
| EV-INV-005 | Reserva vencida liberada | HU-SAL-002 |
| EV-INV-006 | Existencia mínima alcanzada | HU-ALE-001 |
| EV-INV-007 | Existencia máxima superada | HU-ALE-002 |
| EV-INV-008 | Existencia en cero alcanzada | HU-ALE-001 |
| EV-INV-009 | Ubicación sobreocupada | HU-BOD-002 |
| EV-MOV-001 | Movimiento interno confirmado | HU-MOV-001, HU-MOV-008 |
| EV-MOV-002 | Movimiento interno rechazado | HU-MOV-002 |
| EV-MOV-003 | Movimiento interno interrumpido | — ⚠️ |
| EV-MOV-004 | Tránsito interno prolongado detectado | — ⚠️ |
| EV-MOV-005 | Transferencia creada | HU-MOV-003 |
| EV-MOV-006 | Despacho de transferencia confirmado | HU-MOV-004 |
| EV-MOV-007 | Transferencia completada | HU-MOV-004 |
| EV-MOV-008 | Diferencia de transferencia registrada | HU-MOV-005 |
| EV-MOV-009 | Recepción de transferencia rechazada por exceso | HU-MOV-005 |
| EV-MOV-010 | Diferencia de transferencia resuelta | HU-MOV-005 |
| EV-MOV-011 | Tiempo máximo en tránsito excedido | HU-MOV-006 |
| EV-MOV-012 | Transferencia cancelada antes del despacho | HU-MOV-007 |
| EV-MOV-013 | Transferencia cancelada en tránsito | HU-MOV-007 |
| EV-SAL-001 | Salida solicitada | HU-SAL-001 |
| EV-SAL-002 | Salida rechazada por existencia insuficiente | HU-SAL-004 |
| EV-SAL-003 | Salida autorizada | HU-SAL-002, HU-SAL-007 |
| EV-SAL-004 | Salida escalada al Jefe | HU-SAL-007 |
| EV-SAL-005 | Escaneo de preparación rechazado | HU-SAL-003 |
| EV-SAL-006 | Salida ejecutada | HU-SAL-003 |
| EV-SAL-007 | Salida parcial autorizada | HU-SAL-004 |
| EV-SAL-008 | Baja por daño aprobada | HU-SAL-005 |
| EV-SAL-009 | Salida rechazada por el autorizador | HU-TAR-002 |
| EV-SAL-010 | Preparación de salida iniciada | HU-SAL-003 |
| EV-SAL-011 | Salida cancelada | HU-SAL-002 |
| EV-SAL-012 | Pieza tomada en la preparación | HU-SAL-008 |
| EV-SAL-013 | Corte parcial registrado | HU-SAL-009 |
| EV-AJU-001 | Ajuste solicitado | HU-AJU-001 |
| EV-AJU-002 | Ajuste clasificado y enrutado | HU-AJU-003 |
| EV-AJU-003 | Ajuste escalado por autoaprobación | HU-AJU-002 |
| EV-AJU-004 | Ajuste aprobado | HU-AJU-002, HU-AJU-003 |
| EV-AJU-005 | Ajuste aplicado | HU-AJU-002 |
| EV-AJU-006 | Ajuste rechazado | HU-AJU-002 |
| EV-AJU-007 | Ajuste negativo impedido | HU-AJU-004 |
| EV-AJU-008 | Solicitud de ajuste vencida escalada | HU-TAR-002 |
| EV-AJU-009 | Patrón de ajustes recurrentes detectado | HU-AJU-005 |
| EV-AJU-010 | Solicitud bloqueada sin aprobador | HU-AJU-002 |
| EV-CNT-001 | Conteo cíclico programado | HU-CNT-001 |
| EV-CNT-002 | Conteo general programado | HU-CNT-006 |
| EV-CNT-003 | Existencia teórica congelada | HU-CNT-001, HU-CNT-003 |
| EV-CNT-004 | Movimientos bloqueados por conteo general | HU-CNT-006 |
| EV-CNT-005 | Movimiento de excepción autorizado | HU-CNT-006 |
| EV-CNT-006 | Tarea de conteo asignada | HU-CNT-001 |
| EV-CNT-007 | Conteo físico registrado | HU-CNT-002, HU-CNT-010 |
| EV-CNT-008 | Línea de conteo clasificada | HU-CNT-003 |
| EV-CNT-009 | Segundo conteo requerido | HU-CNT-004 |
| EV-CNT-010 | Diferencia persistente escalada | HU-CNT-004 |
| EV-CNT-011 | Tarea de conteo reasignada | HU-CNT-009 |
| EV-CNT-012 | Ubicación excluida del conteo general | HU-CNT-007 |
| EV-CNT-013 | Diferencia global crítica detectada | — ⚠️ |
| EV-CNT-014 | Conteo cerrado | HU-CNT-005, HU-CNT-007 |
| EV-CNT-015 | Exactitud del inventario calculada | HU-CNT-008 |
| EV-CNT-016 | Movimientos desbloqueados | HU-CNT-006 |
| EV-CNT-017 | Conteo abortado | — ⚠️ |
| EV-CNT-018 | Conteo vencido | — ⚠️ |
| EV-NOV-001 | Novedad reportada | HU-NOV-001 |
| EV-NOV-002 | Novedad vinculada a novedad abierta | HU-NOV-002 |
| EV-NOV-003 | Acción de novedad determinada | HU-NOV-002 |
| EV-NOV-004 | Novedad resuelta y cerrada | HU-NOV-002 |
| EV-NOV-005 | Novedad cerrada como improcedente | HU-NOV-002 |
| EV-NOV-006 | Novedad escalada por vencimiento | HU-NOV-003 |
| EV-NOV-007 | Mercancía sin registro incorporada | HU-NOV-004 |
| EV-TRZ-001 | Movimiento confirmado en el kardex | HU-KDX-001, HU-KDX-006 |
| EV-TRZ-002 | Movimiento anulado | HU-KDX-002 |
| EV-TRZ-003 | Registro retenido sin conectividad | HU-ENT-002 |
| EV-TRZ-004 | Registro sincronizado | HU-ENT-002 |
| EV-TRZ-005 | Verificación de integridad ejecutada | HU-KDX-003 |
| EV-TRZ-007 | Registro rechazado al sincronizar | HU-ENT-002 |
| EV-TRZ-006 | Discrepancia de integridad detectada | HU-KDX-003 |
| EV-ALE-001 | Alerta generada | HU-ALE-001, HU-ALE-002 |
| EV-ALE-002 | Alerta atendida | HU-ALE-003 |
| EV-ALE-003 | Alerta descartada | HU-ALE-003 |
| EV-ALE-004 | Alerta escalada | HU-ALE-004 |
| EV-ALE-005 | Alerta cerrada automáticamente | HU-ALE-001 |
| EV-ALE-006 | Frecuencia anómala de disparo reportada | HU-ALE-005 |
| EV-ALE-007 | Exactitud bajo el umbral detectada | — ⚠️ |
| EV-REP-001 | Datos exportados | HU-REP-002, HU-REP-003, HU-ENT-008, HU-AJU-006 |
| EV-REP-002 | Exportación analítica habilitada | HU-REP-003 |
| EV-REP-003 | Reporte programado | HU-REP-004 |
| EV-REP-004 | Reporte programado generado | HU-REP-004 |
| EV-REP-005 | Indicadores del período calculados | HU-CNT-008 |
| EV-AUD-001 | Observación de auditoría registrada | HU-AUD-003 |
| EV-AUD-002 | Observación de auditoría cerrada | HU-AUD-003 |
| EV-AUD-003 | Intento de escritura del Auditor rechazado | HU-AUD-002 |
| EV-AUD-004 | Operación no autorizada rechazada | HU-PAR-003 |
| EV-AUD-005 | Aprobación propia detectada | HU-AUD-004 |
| EV-AUD-006 | Discontinuidad de bitácora detectada | HU-AUD-001 |
| EV-PAR-001 | Parámetro modificado | HU-PAR-001 |
| EV-PAR-002 | Motivo tipificado creado | HU-PAR-002 |
| EV-PAR-003 | Motivo tipificado desactivado | HU-PAR-002 |
| EV-PAR-004 | Configuración de regla estructural rechazada | HU-PAR-003 |
| EV-PAR-005 | Motivo tipificado reactivado | HU-PAR-002 |
| EV-TAR-001 | Tarea generada | HU-TAR-001 |
| EV-TAR-002 | Tarea completada | HU-TAR-001, HU-DSH-002 |
| EV-TAR-003 | Tarea reasignada | HU-TAR-003, HU-DSH-003 |
| EV-TAR-004 | Solicitud de aprobación notificada | HU-TAR-002 |
| EV-TAR-005 | Resultado notificado al solicitante | HU-TAR-002, HU-AJU-002 |
| EV-TAR-006 | Tarea cancelada | — ⚠️ |
| EV-JOR-001 | Pendientes de jornada consolidados | — ⚠️ |
| EV-JOR-002 | Pendientes traspasados | — ⚠️ |
| EV-JOR-003 | Jornada cerrada | — ⚠️ |
| EV-JOR-004 | Cierre de jornada bloqueado | — ⚠️ |
| EV-JOR-005 | Cierre de jornada omitido | — ⚠️ |

**Cobertura de historias:** 101/110 historias tienen al menos un evento. Las 9 restantes son **historias de consulta** —leer no produce eventos (RN-INT-006)—: HU-DSH-001, HU-INV-001, HU-INV-002, HU-INV-003, HU-INV-004, HU-INV-005, HU-INV-006, HU-KDX-005, HU-REP-001.

**Eventos sin historia (13):** EV-ENT-015, EV-MOV-003, EV-MOV-004, EV-CNT-013, EV-CNT-017, EV-CNT-018, EV-ALE-007, EV-TAR-006, EV-JOR-001, EV-JOR-002, EV-JOR-003, EV-JOR-004, EV-JOR-005. Provienen de procesos del SPEC sin historia propia (H-10, H-11 del SRS; HD-11, HD-19).

## Matriz E — Evento ↔ Requisito funcional

| Evento | Nombre | Requisitos funcionales (SRS) |
|---|---|---|
| EV-ACC-001 | Sesión iniciada | RF-ACC-001, RF-ACC-003 |
| EV-ACC-002 | Acceso rechazado | RF-ACC-003 |
| EV-ACC-003 | Cuenta bloqueada | RF-ACC-004 |
| EV-ACC-004 | Sesión cerrada por inactividad | RF-ACC-005 |
| EV-ACC-005 | Sesión cerrada por el usuario | RF-ACC-005 |
| EV-ACC-006 | Contraseña cambiada | RF-ACC-006 |
| EV-ACC-007 | Acceso restablecido | RF-ACC-007 |
| EV-USR-001 | Usuario creado | RF-USR-001, RF-USR-002, RF-USR-003 |
| EV-USR-002 | Rol cambiado | RF-USR-006, RF-USR-008 |
| EV-USR-003 | Ámbito asignado | RF-USR-007 |
| EV-USR-004 | Usuario desactivado | RF-USR-004, RF-USR-005, RF-USR-008 |
| EV-USR-005 | Usuario reactivado | RF-USR-004, RF-USR-008 |
| EV-USR-006 | Retiro del último Administrador o Jefe rechazado | RF-USR-006 |
| EV-CAT-001 | Referencia creada | RF-CAT-001, RF-CAT-002, RF-CAT-003 |
| EV-CAT-002 | SKU generados | RF-CAT-004 |
| EV-CAT-003 | Unidad de medida asignada | RF-CAT-005 |
| EV-CAT-004 | Umbrales de existencia definidos | RF-CAT-007, RF-CAT-008 |
| EV-CAT-005 | Referencia desactivada | RF-CAT-006 |
| EV-CAT-006 | Referencia reactivada | RF-CAT-006 |
| EV-CAT-007 | Catálogo cargado masivamente | RF-CAT-009 |
| EV-CAT-008 | Categoría registrada | RF-CAT-010 |
| EV-CAT-009 | Categoría desactivada | RF-CAT-010 |
| EV-BOD-001 | Bodega creada | RF-BOD-001 |
| EV-BOD-002 | Zona creada | RF-BOD-001, RF-BOD-003 |
| EV-BOD-003 | Ubicación creada | RF-BOD-001, RF-BOD-002 |
| EV-BOD-004 | Capacidad de ubicación definida | RF-BOD-005 |
| EV-BOD-005 | Ubicación desactivada | RF-BOD-006 |
| EV-BOD-006 | Ubicación reactivada | RF-BOD-006 |
| EV-BOD-007 | Coordinador asignado a zona | RF-BOD-007 |
| EV-BOD-008 | Criterios de asignación configurados | RF-BOD-008 |
| EV-QRC-001 | Identificador QR generado | RF-QRC-001, RF-QRC-002 |
| EV-QRC-002 | Identificador QR impreso | RF-QRC-005 |
| EV-QRC-003 | Identificador QR activado | RF-QRC-003 |
| EV-QRC-004 | Identificador QR reimpreso | RF-QRC-006, RF-QRC-007 |
| EV-QRC-005 | Identificador QR anulado | RF-QRC-002, RF-QRC-007 |
| EV-QRC-006 | Identificador secundario asociado | RF-QRC-008 |
| EV-QRC-007 | QR de ubicación generado | RF-QRC-004 |
| EV-ENT-001 | Documento de entrada creado | RF-ENT-001, RF-ENT-002, RF-ENT-003 |
| EV-ENT-002 | Posible duplicado advertido | RF-ENT-004 |
| EV-ENT-003 | Recepción física iniciada | RF-ENT-005 |
| EV-ENT-004 | Línea de recepción registrada | RF-ENT-005 |
| EV-ENT-005 | Recepción interrumpida | RF-ENT-006 |
| EV-ENT-006 | Recepción continuada | RF-ENT-006 |
| EV-ENT-007 | Recibido conforme determinado | RF-ENT-007 |
| EV-ENT-008 | Faltante de recepción registrado | RF-ENT-007, RF-ENT-008 |
| EV-ENT-009 | Sobrante de recepción registrado | RF-ENT-007, RF-ENT-009 |
| EV-ENT-010 | Sobrante autorizado | RF-ENT-009 |
| EV-ENT-011 | Mercancía dañada registrada en recepción | RF-ENT-012 |
| EV-ENT-012 | Entrada confirmada | RF-ENT-010, RF-ENT-011, RF-LOT-001 |
| EV-ENT-013 | Retorno registrado como entrada | RF-SAL-011 |
| EV-ENT-014 | Autoconfirmación de entrada rechazada | RF-ENT-010 |
| EV-ENT-015 | Documento de entrada reversado | — ⚠️ |
| EV-ENT-016 | Pieza registrada en la recepción | RF-ENT-014, RF-ENT-015, RF-ENT-016 |
| EV-LOT-001 | Lote creado | RF-LOT-001, RF-LOT-002, RF-LOT-003 |
| EV-LOT-002 | Lote inmovilizado | RF-LOT-005 |
| EV-LOT-003 | Lote liberado | RF-LOT-005 |
| EV-LOT-004 | Antigüedad de lote superada | RF-LOT-006 |
| EV-INV-001 | Mercancía ubicada | RF-BOD-004, RF-BOD-005, RF-MOV-001, RF-MOV-002, RF-MOV-005, RF-MOV-012 |
| EV-INV-002 | Desviación de ubicación registrada | — ⚠️ |
| EV-INV-003 | Existencia reservada | RF-SAL-005, RF-MOV-007 |
| EV-INV-004 | Reserva liberada | RF-SAL-009, RF-MOV-011 |
| EV-INV-005 | Reserva vencida liberada | — ⚠️ |
| EV-INV-006 | Existencia mínima alcanzada | RF-ALE-001, RF-ALE-004 |
| EV-INV-007 | Existencia máxima superada | RF-ALE-001, RF-ALE-004 |
| EV-INV-008 | Existencia en cero alcanzada | RF-ALE-004 |
| EV-INV-009 | Ubicación sobreocupada | RF-BOD-005, RF-ALE-004 |
| EV-MOV-001 | Movimiento interno confirmado | RF-MOV-001, RF-MOV-002, RF-MOV-012 |
| EV-MOV-002 | Movimiento interno rechazado | RF-MOV-003, RF-MOV-004, RF-MOV-005, RF-MOV-006 |
| EV-MOV-003 | Movimiento interno interrumpido | — ⚠️ |
| EV-MOV-004 | Tránsito interno prolongado detectado | RF-ALE-004 |
| EV-MOV-005 | Transferencia creada | RF-MOV-007 |
| EV-MOV-006 | Despacho de transferencia confirmado | RF-MOV-008, RF-MOV-009 |
| EV-MOV-007 | Transferencia completada | RF-MOV-008, RF-MOV-010 |
| EV-MOV-008 | Diferencia de transferencia registrada | RF-MOV-010 |
| EV-MOV-009 | Recepción de transferencia rechazada por exceso | RF-MOV-010 |
| EV-MOV-010 | Diferencia de transferencia resuelta | RF-MOV-010 |
| EV-MOV-011 | Tiempo máximo en tránsito excedido | RF-MOV-011 |
| EV-MOV-012 | Transferencia cancelada antes del despacho | RF-MOV-011 |
| EV-MOV-013 | Transferencia cancelada en tránsito | RF-MOV-011 |
| EV-SAL-001 | Salida solicitada | RF-SAL-001, RF-SAL-002, RF-SAL-003 |
| EV-SAL-002 | Salida rechazada por existencia insuficiente | RF-SAL-004 |
| EV-SAL-003 | Salida autorizada | RF-SAL-005, RF-SAL-006, RF-SAL-007 |
| EV-SAL-004 | Salida escalada al Jefe | RF-SAL-006 |
| EV-SAL-005 | Escaneo de preparación rechazado | RF-SAL-008 |
| EV-SAL-006 | Salida ejecutada | RF-SAL-009 |
| EV-SAL-007 | Salida parcial autorizada | RF-SAL-004 |
| EV-SAL-008 | Baja por daño aprobada | RF-SAL-010 |
| EV-SAL-009 | Salida rechazada por el autorizador | — ⚠️ |
| EV-SAL-010 | Preparación de salida iniciada | RF-SAL-007, RF-SAL-008 |
| EV-SAL-011 | Salida cancelada | — ⚠️ |
| EV-SAL-012 | Pieza tomada en la preparación | RF-SAL-012 |
| EV-SAL-013 | Corte parcial registrado | RF-SAL-013 |
| EV-AJU-001 | Ajuste solicitado | RF-AJU-001, RF-AJU-002, RF-AJU-003 |
| EV-AJU-002 | Ajuste clasificado y enrutado | RF-AJU-004 |
| EV-AJU-003 | Ajuste escalado por autoaprobación | RF-AJU-005 |
| EV-AJU-004 | Ajuste aprobado | RF-AJU-005, RF-AJU-007 |
| EV-AJU-005 | Ajuste aplicado | RF-AJU-007 |
| EV-AJU-006 | Ajuste rechazado | RF-AJU-008 |
| EV-AJU-007 | Ajuste negativo impedido | RF-AJU-006 |
| EV-AJU-008 | Solicitud de ajuste vencida escalada | RF-ALE-004 |
| EV-AJU-009 | Patrón de ajustes recurrentes detectado | RF-AJU-009 |
| EV-AJU-010 | Solicitud bloqueada sin aprobador | RF-AJU-005 |
| EV-CNT-001 | Conteo cíclico programado | RF-CNT-001, RF-CNT-002 |
| EV-CNT-002 | Conteo general programado | RF-CNT-011 |
| EV-CNT-003 | Existencia teórica congelada | RF-CNT-003, RF-CNT-004 |
| EV-CNT-004 | Movimientos bloqueados por conteo general | RF-CNT-011 |
| EV-CNT-005 | Movimiento de excepción autorizado | RF-CNT-011 |
| EV-CNT-006 | Tarea de conteo asignada | RF-CNT-005 |
| EV-CNT-007 | Conteo físico registrado | RF-CNT-006, RF-CNT-014 |
| EV-CNT-008 | Línea de conteo clasificada | RF-CNT-007 |
| EV-CNT-009 | Segundo conteo requerido | RF-CNT-008, RF-CNT-009 |
| EV-CNT-010 | Diferencia persistente escalada | RF-CNT-008 |
| EV-CNT-011 | Tarea de conteo reasignada | RF-TAR-004 |
| EV-CNT-012 | Ubicación excluida del conteo general | RF-CNT-012 |
| EV-CNT-013 | Diferencia global crítica detectada | — ⚠️ |
| EV-CNT-014 | Conteo cerrado | RF-CNT-010, RF-CNT-012 |
| EV-CNT-015 | Exactitud del inventario calculada | RF-CNT-013, RF-REP-003 |
| EV-CNT-016 | Movimientos desbloqueados | RF-CNT-011 |
| EV-CNT-017 | Conteo abortado | — ⚠️ |
| EV-CNT-018 | Conteo vencido | RF-ALE-004 |
| EV-NOV-001 | Novedad reportada | RF-NOV-001, RF-NOV-002, RF-NOV-003, RF-NOV-004 |
| EV-NOV-002 | Novedad vinculada a novedad abierta | RF-NOV-005 |
| EV-NOV-003 | Acción de novedad determinada | RF-NOV-004 |
| EV-NOV-004 | Novedad resuelta y cerrada | RF-NOV-006 |
| EV-NOV-005 | Novedad cerrada como improcedente | RF-NOV-006 |
| EV-NOV-006 | Novedad escalada por vencimiento | RF-ALE-007 |
| EV-NOV-007 | Mercancía sin registro incorporada | RF-AJU-001, RF-AJU-002, RF-QRC-001, RF-BOD-004 |
| EV-TRZ-001 | Movimiento confirmado en el kardex | RF-KDX-001, RF-KDX-002, RF-KDX-003, RF-KDX-008 |
| EV-TRZ-002 | Movimiento anulado | RF-KDX-004 |
| EV-TRZ-003 | Registro retenido sin conectividad | RF-ENT-005 |
| EV-TRZ-004 | Registro sincronizado | RF-ENT-005 |
| EV-TRZ-005 | Verificación de integridad ejecutada | RF-KDX-006 |
| EV-TRZ-007 | Registro rechazado al sincronizar | RF-ENT-005 |
| EV-TRZ-006 | Discrepancia de integridad detectada | RF-KDX-006, RF-AUD-007 |
| EV-ALE-001 | Alerta generada | RF-ALE-001, RF-ALE-002, RF-ALE-003, RF-ALE-004 |
| EV-ALE-002 | Alerta atendida | RF-ALE-005 |
| EV-ALE-003 | Alerta descartada | RF-ALE-005 |
| EV-ALE-004 | Alerta escalada | RF-ALE-007 |
| EV-ALE-005 | Alerta cerrada automáticamente | RF-ALE-007 |
| EV-ALE-006 | Frecuencia anómala de disparo reportada | RF-ALE-006 |
| EV-ALE-007 | Exactitud bajo el umbral detectada | RF-ALE-004 |
| EV-REP-001 | Datos exportados | RF-REP-006 |
| EV-REP-002 | Exportación analítica habilitada | RF-REP-004, RF-REP-005 |
| EV-REP-003 | Reporte programado | RF-REP-007 |
| EV-REP-004 | Reporte programado generado | RF-REP-002, RF-REP-007 |
| EV-REP-005 | Indicadores del período calculados | RF-REP-003 |
| EV-AUD-001 | Observación de auditoría registrada | RF-AUD-006 |
| EV-AUD-002 | Observación de auditoría cerrada | RF-AUD-006 |
| EV-AUD-003 | Intento de escritura del Auditor rechazado | RF-AUD-005 |
| EV-AUD-004 | Operación no autorizada rechazada | — ⚠️ |
| EV-AUD-005 | Aprobación propia detectada | RF-AUD-007 |
| EV-AUD-006 | Discontinuidad de bitácora detectada | RF-AUD-007 |
| EV-PAR-001 | Parámetro modificado | RF-PAR-001, RF-PAR-002, RF-PAR-003, RF-PAR-004 |
| EV-PAR-002 | Motivo tipificado creado | RF-PAR-005 |
| EV-PAR-003 | Motivo tipificado desactivado | RF-PAR-005 |
| EV-PAR-004 | Configuración de regla estructural rechazada | RF-PAR-006 |
| EV-PAR-005 | Motivo tipificado reactivado | RF-PAR-005 |
| EV-TAR-001 | Tarea generada | RF-TAR-001, RF-TAR-002 |
| EV-TAR-002 | Tarea completada | RF-TAR-003 |
| EV-TAR-003 | Tarea reasignada | RF-TAR-004 |
| EV-TAR-004 | Solicitud de aprobación notificada | RF-AJU-004 |
| EV-TAR-005 | Resultado notificado al solicitante | RF-AJU-008 |
| EV-TAR-006 | Tarea cancelada | — ⚠️ |
| EV-JOR-001 | Pendientes de jornada consolidados | — ⚠️ |
| EV-JOR-002 | Pendientes traspasados | — ⚠️ |
| EV-JOR-003 | Jornada cerrada | — ⚠️ |
| EV-JOR-004 | Cierre de jornada bloqueado | — ⚠️ |
| EV-JOR-005 | Cierre de jornada omitido | — ⚠️ |

**Cobertura de requisitos:** 146/171 RF se relacionan con al menos un evento. Los 25 restantes son de **consulta, restricción transversal o presentación**, que no producen hechos nuevos: RF-ACC-002, RF-AJU-010, RF-AUD-001, RF-AUD-002, RF-AUD-003, RF-AUD-004, RF-DSH-001, RF-DSH-002, RF-DSH-003, RF-DSH-004, RF-ENT-013, RF-INV-001, RF-INV-002, RF-INV-003, RF-INV-004, RF-INV-005, RF-INV-006, RF-INV-007, RF-INV-008, RF-INV-009, RF-KDX-005, RF-KDX-007, RF-LOT-004, RF-REP-001, RF-TAR-005.

**Eventos sin RF (15):** EV-ENT-015, EV-INV-002, EV-INV-005, EV-MOV-003, EV-SAL-009, EV-SAL-011, EV-CNT-013, EV-CNT-017, EV-AUD-004, EV-TAR-006, EV-JOR-001, EV-JOR-002, EV-JOR-003, EV-JOR-004, EV-JOR-005. Son la traducción al dominio de las brechas del SRS: reglas sin RF (H-11), cierre de jornada (H-10) y funciones de módulo sin requisito (HD-19). Implementarlos exige que el Director apruebe las propuestas del Anexo C del SRS (DEC-05, DEC-06).


---

**ESTADO DEL CAPÍTULO — 6**

| | |
|---|---|
| **Completado** | Matriz D (168 eventos ↔ 101 historias) y Matriz E (168 eventos ↔ 146 RF), con coberturas y exclusiones justificadas |
| **Riesgos** | 15 eventos sin RF y 13 sin historia (RF5-12) |
| **Dependencias** | SRS Caps. 5 y 6 |
| **Hallazgos** | H-10, H-11 del SRS · HD-11, HD-19 |

---

*Fin de EVENT_CATALOG v1.2.*
