
---

# CAPÍTULO 10 — MATRIZ CRUD

> Relaciona los **actores** (Cap. 3) con los **módulos funcionales** (M-01…M-20). Derivada de la matriz de segregación del SPEC (§2.7), de las fichas de rol y de las funciones de cada módulo `[SRS]`. No describe estructura de datos: el «objeto» de cada operación es el elemento funcional propio del módulo.

**Leyenda.**

| Letra | Significado |
|---|---|
| **C** | Crear / registrar / generar |
| **R** | Leer / consultar |
| **U** | Actualizar / modificar / cambiar de estado |
| **D** | Desactivar, anular con movimiento inverso o cerrar — **eliminación lógica**. **No existe borrado físico para ningún rol, incluido el Administrador** (@RN063) |
| **A** | Aprobar / autorizar / confirmar (extensión del CRUD: la segregación de funciones exige distinguirla) |
| **⚠️** | Permitido con restricción (ver nota) |
| **—** | Sin acceso |

| Módulo | Admin | Jefe | Coord. | Aux. | Auditor | Sistema | Notas |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **M-01** Acceso y Autenticación | C R U D | C U D | C U D | C U D | C U D | C U D | Los roles operan sobre su propia sesión y contraseña; el Administrador además restablece accesos ajenos (R vía bitácora). El Sistema bloquea cuentas y cierra sesiones por inactividad |
| **M-02** Usuarios y Roles | C R U D | — | — | — | R | — | Solo Administrador. «D» = desactivar (@RN011: nunca al último Administrador) |
| **M-03** Catálogo de Referencias | C R U D | C R U D | R | R | R | C | Sistema genera los SKU. «D» = desactivar (solo con existencia cero, @RN010) |
| **M-04** Gestión de Lotes | C R U | C R U | C R | R | R | C | Sistema crea o asocia el lote al confirmar la entrada. «U» = inmovilizar / liberar (solo Jefe o Administrador, @RN073) |
| **M-05** Estructura de Bodega | C R U D | R | R | R | R | C | Solo Administrador define la estructura. Sistema genera los QR de ubicación. «D» = desactivar (@RN013) |
| **M-06** Identificación QR | C R U D | C R U D | C R U D | R U ⚠️ | R | C | ⚠️ Aux.: solo reimprime por deterioro, con motivo (@RN018). El Auxiliar escanea (R) |
| **M-07** Entradas y Recepción | C R U A D | C R U A D | C R U A D | R U | R | C | Aux. registra la recepción física (U) pero **no confirma** (@RN057b). «D» = reversar una entrada no confirmada. Sistema genera el movimiento de entrada |
| **M-08** Salidas | C R U A D | C R U A D | C R U A ⚠️ D | R U | R | C U D | ⚠️ Coord.: autoriza solo hasta su umbral (@RN030). Aux. prepara y confirma lo autorizado. Sistema reserva, descuenta y libera reservas vencidas |
| **M-09** Movimientos y Transferencias | C R U A D | C R U A D | C R U D | C R U | R | C U | Aux.: crea movimientos internos y ejecuta transferencias asignadas, pero **no crea transferencias**. «D» = cancelar (en tránsito solo Jefe, @RN035) |
| **M-10** Ajustes de Inventario | C R A | C R A | C R | — | R | C U | Nadie aprueba su propio ajuste (@RN023). Admin aprueba mayores; Jefe menores. Sistema aplica el movimiento al aprobarse y escala |
| **M-11** Conteos | C R U A D | C R U A D | C R U | C R ⚠️ | R | C U D | Cierra solo el Jefe/Admin (@RN042) y nunca quien ejecutó (@RN041). ⚠️ Aux.: registra el conteo de sus tareas, sin ver la cantidad esperada (@RN040). Coord.: solo conteos cíclicos |
| **M-12** Novedades de Mercancía | C R U D | C R U D | C R U D | C R ⚠️ | R | C U | «D» = cerrar (nunca eliminar, @RN063). ⚠️ Aux.: reporta y consulta las propias |
| **M-13** Consulta de Existencia | R | R | R | R ⚠️ | R | — | Solo lectura (@RN067). ⚠️ Aux.: sin costo ni valorización |
| **M-14** Kardex y Trazabilidad | R C ⚠️ | R C ⚠️ | R | R ⚠️ | R | C | El kardex **nunca** admite U ni D (@RN012). ⚠️ «C» = movimiento inverso de anulación con motivo y autorización. ⚠️ Aux.: solo lo que él movió, últimos 30 días |
| **M-15** Alertas y Reglas | R U D | R U D | R U D | — | R | C U D | «U/D» = atender, descartar con motivo (@RN058). Sistema genera, agrupa, cierra y escala |
| **M-16** Reportes y Exportación | C R U | C R U D | C R ⚠️ | — | C R | C | ⚠️ Coord.: solo reportes operativos. «U» Admin = habilitar exportación analítica; «U/D» Jefe = programar / desactivar reportes periódicos |
| **M-17** Dashboard Operativo | R | R | R ⚠️ | — | R | — | ⚠️ Coord.: solo su zona y sin valorización. El Auxiliar no ve el dashboard: ve su panel de tareas (M-20) |
| **M-18** Auditoría y Bitácora | R | R ⚠️ | — | — | C R | C | ⚠️ Jefe: solo eventos de su bodega, sin configuración. Auditor «C» = observaciones en registro separado (@RN064). La bitácora nunca admite U ni D (@RN061) |
| **M-19** Parámetros y Configuración | C R U D | — | R ⚠️ | — | R | — | Solo Administrador configura. ⚠️ Coord.: consulta su propio umbral de autorización (HU-SAL-007) |
| **M-20** Notificaciones y Tareas | R U | R U | R U | R | — | C U D | «U» = reasignar tareas (Coord. y superiores). La tarea la cierra el movimiento asociado, no el usuario (@RF160). El Auditor no tiene panel de tareas |

**Notas de la matriz `[SRS]`:**

1. **Sin «D» física.** Toda «D» de la tabla es desactivación, anulación con movimiento inverso o cierre; se auditará con @RN063, @RN076 y @RN077.
2. **Kardex y bitácora** son de solo *C* y *R*: la ausencia de *U* y *D* es la materialización de @RN012 y @RN061 y se verifica en @RNF031.
3. **Auditor.** Su única *C* es la de observaciones de auditoría (registro separado) y la generación de reportes; sobre el inventario solo *R* (@RF149).
4. **Vacíos del SPEC que la matriz no resuelve** (no se inventan permisos): (a) el SPEC no define si el **Jefe** puede *leer* los parámetros de configuración; (b) @RN064 indica que las observaciones «se cierran con respuesta» pero no dice **quién** responde; (c) la «valorización» aparece como permiso sin dato de origen (H-07). Se elevan al Director en el Anexo C (DEC-04, DEC-07) y en la nota final de este capítulo.

---

**ESTADO DEL CAPÍTULO 10**

| | |
|---|---|
| **Completado** | Matriz CRUD 20 módulos × 5 roles + Sistema con restricciones y notas |
| **Pendiente** | Definir lectura de parámetros por el Jefe y actor que cierra observaciones de auditoría (SPEC no lo dice) |
| **Riesgos encontrados** | Permiso «valorización» sin objeto (H-07); ambigüedad estructural/configurable (H-06) |
| **Dependencias** | Cap. 3 (matriz §2.7) · Cap. 8 (reglas) · Cap. 7 (RNF-SEG-003, RNF-SEG-004) |
