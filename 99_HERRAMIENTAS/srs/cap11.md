
---

# CAPÍTULO 11 — DEPENDENCIAS FUNCIONALES

> Qué módulos **necesitan** de otros para tener sentido funcional. Transcribe y consolida las «dependencias funcionales» declaradas en el SPEC (§5) `[SRS]`. Una dependencia funcional **no es** una dependencia técnica ni de arquitectura: significa «este módulo no puede cumplir su propósito sin la capacidad del otro».

## 11.1 Tabla de dependencias por módulo

{{TABLA_DEP}}

## 11.2 Matriz de dependencia (fila depende de columna)

`●` = la fila depende funcionalmente de la columna.

{{MATRIZ_DEP}}

## 11.3 Lectura de la matriz

**Módulos «raíz» (los demás dependen de ellos):**

| Módulo | Por qué es raíz | Cantidad de módulos que dependen de él |
|---|---|---|
{{TABLA_RAICES}}

**Ciclos funcionales detectados.** Existen dependencias mutuas que **no son un defecto** sino la consecuencia de que el kardex y la estructura de bodega se alimentan y se leen entre sí. Deben tenerse presentes al planificar la construcción por bloques `[SRS]`:

{{TABLA_CICLOS}}

**Dependencias de todos hacia los módulos de control.** Por la regla de atribución (@RN001) y de bitácora (@RN061), **todo módulo que altera el estado del sistema depende de M-01 (identidad) y de M-18 (bitácora)**; y todo módulo operativo (M-07…M-12) **escribe en M-14** (kardex). Esta relación transversal no se repite fila por fila.

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
