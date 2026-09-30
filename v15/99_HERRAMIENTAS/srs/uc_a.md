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
| **Trazabilidad** | HU: @HU001 @HU002 @HU003 @HU004 · RF: @RF001 @RF002 @RF003 @RF004 @RF005 @RF006 @RF007 · RN: @RN001 @RN061 |

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
| **Trazabilidad** | HU: @HU005 @HU006 @HU007 @HU008 @HU009 · RF: @RF008 @RF009 @RF010 @RF011 @RF012 @RF013 @RF014 @RF015 · RN: @RN011 @RN063 @RN014 @RN076 @RN077 |

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
| **Trazabilidad** | HU: @HU010 @HU011 @HU012 @HU013 @HU014 @HU015 · RF: @RF016 @RF017 @RF018 @RF019 @RF020 @RF021 @RF022 @RF023 @RF024 @RF025 · RN: @RN002 @RN004 @RN010 @RN063 @RN068 |

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
| **Trazabilidad** | HU: @HU020 @HU021 @HU022 @HU023 @HU024 · RF: @RF032 @RF033 @RF034 @RF035 @RF036 @RF037 @RF038 @RF039 · RN: @RN014 @RN019 @RN021 @RN013 @RN020 |

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
| **Trazabilidad** | HU: @HU098 @HU099 @HU100 · RF: @RF152 @RF153 @RF154 @RF155 @RF156 @RF157 @RF181 · RN: @RN079 @RN061 @RN063 @RN029 @RN024 @RN030 @RN041 @RN034 |

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
| **Postcondiciones (éxito)** | La existencia **en recepción** refleja la mercancía físicamente recibida (pasa a disponible al ubicarse, CU-08; @RN081, DF5-02); existe un movimiento de entrada en el kardex, atribuido a personas identificadas, con fecha y documento de respaldo; se crea o asocia el lote. |
| **Postcondiciones (fallo)** | El documento queda en su estado (pendiente, recepción parcial, recibido con novedad); no se modifica el inventario. |
| **Trazabilidad** | HU: @HU030 @HU031 @HU032 @HU033 @HU034 @HU036 @HU037 @HU016 @HU104 @HU105 · RF: @RF048 @RF049 @RF050 @RF051 @RF052 @RF053 @RF054 @RF055 @RF056 @RF057 @RF058 @RF059 @RF060 @RF163 @RF164 @RF165 @RF180 · RN: @RN002b @RN003 @RN005 @RN006 @RN007 @RN008 @RN057b @RN054 @RN071 @RN081 @RN083 @RN084 @RN085 |

**Flujo principal**
1. El Coordinador crea el documento de entrada (origen, fecha esperada y líneas con referencia, talla, color y cantidad esperada) o selecciona uno existente; el sistema no solicita precio ni datos de orden de compra.
2. El sistema deja el documento en **Pendiente de recepción**.
3. El Auxiliar abre el documento en su tablet.
4. El Auxiliar cuenta físicamente la mercancía pieza por pieza y registra cada pieza (rollo, paquete, bolsa o contenedor agrupado) con su cantidad propia; la cantidad recibida por línea es la suma de sus piezas (@RN084, @RN085); el sistema confirma visualmente cada registro guardado.
5. El sistema compara automáticamente cantidad recibida contra esperada, línea por línea.
6. Si coinciden, marca el documento como **Recibido conforme**.
7. El Coordinador —distinto de quien registró la recepción física— verifica y confirma la entrada.
8. El sistema crea o asocia el lote, genera el movimiento de entrada en el kardex e incrementa la existencia **en recepción**, en una ubicación de la zona de recepción; todavía no está disponible (@RN081).
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
- **E6 · Sin conectividad:** el registro se retiene localmente y se sincroniza al restablecerse; al sincronizar se valida de nuevo contra el estado vigente y, si ya no cumple las reglas, no se aplica: se rechaza con constancia y, si describe un hecho físico, se abre una novedad (@RN083, DF5-05); el documento no se confirma hasta sincronizar.
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
| **Trazabilidad** | HU: @HU025 @HU026 @HU027 @HU028 @HU029 · RF: @RF040 @RF041 @RF042 @RF043 @RF044 @RF045 @RF046 @RF047 @RF179 · RN: @RN015 @RN016 @RN017 @RN018 |

**Flujo principal**
1. El sistema genera un identificador QR único por **SKU + Lote** (referencia + talla + color + lote), que no incluye la ubicación: un mismo SKU + Lote puede estar en varias ubicaciones con el mismo QR (DF5-01).
2. El Coordinador imprime el identificador (individual o por lote de impresión), con información legible de respaldo.
3. El Auxiliar adhiere el identificador a la mercancía o a su contenedor.
4. El Auxiliar escanea el identificador para confirmar su legibilidad.
5. El sistema registra el identificador como **Activo**.
6. El proceso continúa en CU-08.

**Flujos alternos**
- **A1 · Reimpresión por deterioro:** el Auxiliar o Coordinador la solicita indicando motivo; se imprime otra copia del mismo QR: el identificador no cambia, no se crea una nueva identidad y la reimpresión queda consultable en el historial (@RN018, Q-09).
- **A2 · Código de barras del proveedor:** se admite como identificador secundario asociado al QR primario; permite consultar pero no ejecutar escrituras.
- **A3 · Mercancía sin posibilidad de rotulado individual:** se rotula el contenedor con el QR del SKU + Lote y se registra como pieza de tipo contenedor agrupado, con su cantidad de unidades (@RN084, F-6); la mezcla de lotes en un contenedor es DECISIÓN PENDIENTE (HD-28).
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
| **Trazabilidad** | HU: @HU035 @HU024 @HU021 @HU106 · RF: @RF035 @RF036 @RF039 @RF072 @RF073 @RF076 @RF166 @RF172 · RN: @RN019 @RN020 @RN021 @RN022 @RN026 @RN082 @RN087 |

**Flujo principal**
1. El sistema propone una ubicación destino según los criterios configurados (zona por categoría, capacidad, agrupación por referencia).
2. El Auxiliar traslada físicamente la mercancía a la ubicación propuesta.
3. Escanea el identificador de la mercancía, selecciona la pieza que ubica (@RN087) y después escanea el de la ubicación.
4. El sistema valida que la ubicación esté activa y tenga capacidad.
5. El sistema registra la primera ubicación como **movimiento interno** en el kardex, desde la ubicación de recepción hacia la destino (qué, cuánto, origen, destino, quién, cuándo y documento de entrada), y la cantidad pasa de en recepción a **disponible** en el destino; la existencia total no cambia (@RN082, DF5-03).
6. El sistema confirma visualmente al Auxiliar que el registro quedó guardado.

**Flujos alternos**
- **A1 · Ubicación distinta a la propuesta:** el sistema lo permite, registra la desviación como información operativa (no como falta) y notifica al Coordinador.
- **A2 · Mercancía repartida en varias ubicaciones:** se registran asignaciones parciales —un movimiento interno por cada una— hasta completar la cantidad; el QR del SKU + Lote no cambia.
- **A3 · Identificador de ubicación ilegible:** el Auxiliar la selecciona de una lista; el sistema registra que no hubo escaneo.

**Excepciones**
- **E1 · Ubicación propuesta llena:** el sistema propone una alternativa; el Auxiliar puede solicitar reasignación al Coordinador.
- **E2 · Ubicación escaneada inactiva:** se rechaza y se solicita otra.
- **E3 · Sin conectividad:** el registro se retiene localmente y se sincroniza al restablecerse; al sincronizar se valida de nuevo contra el estado vigente y, si ya no cumple las reglas, no se aplica: se rechaza con constancia y, si describe un hecho físico, se abre una novedad (@RN083, DF5-05).
