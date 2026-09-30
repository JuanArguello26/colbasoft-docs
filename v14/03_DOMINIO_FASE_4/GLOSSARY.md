# GLOSSARY
## Glosario Oficial de COLBASOFT

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | GLOSSARY |
| **Versión** | 1.4 |
| **Fase** | Fase 4 del proyecto — Modelo de Dominio (Checkpoint CP-04) |
| **Fecha** | 28 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) · 30 de septiembre de 2026 (v1.2, v1.3 y v1.4) |
| **Estado** | **Borrador v1.4** (30-sep-2026): incorpora la trazabilidad por pieza (v1.2), las respuestas a DEC-02…DEC-09 (v1.3) y las de H-19, H-20, HD-29 y HD-30. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: acta de DEC-08 sin firmar y pendientes HD-28, HD-29 y HD-30 |
| **Jerarquía documental** | Monografía → Auditoría Fundacional → COLBASOFT_SPEC v1.4 → SRS_COLBASOFT v1.4 → **Modelo de Dominio v1.4** (DOMAIN_MODEL · EVENT_CATALOG · GLOSSARY) |
| **Documentos hermanos** | `DOMAIN_MODEL.md` · `EVENT_CATALOG.md` |
| **Autoría del proyecto** | Juan Esteban Argüello · Brayan Alexander Osorio · Brandon José Guerrero |
| **Institución / asesor** | Escuela de Ingeniería — CIAF · Edwin Andrés Cabrera Arredondo |
| **Fuera de alcance** | Arquitectura, modelo de datos, tecnologías, interfaces de integración, notaciones de diseño y código: pertenecen a la Fase 5 y posteriores |

> **Naturaleza.** Este documento es **derivado**: no modifica la monografía, la auditoría, el SPEC ni el SRS. Modela el negocio que esos documentos describen. Toda diferencia entre ellos o frente al Prompt Maestro #004 se registra como **Hallazgo del Dominio (HD-nn)**; no se corrige en silencio.

> **Versión 1.1.** Incorpora las decisiones del cierre del CP-04 (DF5-01, DF5-02, DF5-03, DF5-05 y DF5-06), registradas en `04_CP04_AUDITORIA/04_CP04_CIERRE.md`. El detalle de los cambios está en DOMAIN_MODEL §0.8. La v1.0 se conserva en el historial del repositorio (commit `79f823c`).

> **Versión 1.2.** Incorpora las decisiones del Director del 30 de septiembre de 2026 (DEC-01 = A, Q-11, F-1…F-6, Q-09 y Q-10), que agregan la **Pieza** al modelo y resuelven HD-25. El detalle está en DOMAIN_MODEL §0.9.

> **Versión 1.3.** Incorpora las respuestas del Director a DEC-02…DEC-09. El detalle está en DOMAIN_MODEL §0.10.

> **Versión 1.4.** Incorpora las respuestas a H-19, H-20, HD-29 y HD-30. El detalle está en DOMAIN_MODEL §0.11.


> **Reconstrucción de contexto.** Ver DOMAIN_MODEL, Cap. 0 (ESTADO: CONTEXTO RECONSTRUIDO).

# CAPÍTULO 1 — USO DEL GLOSARIO

1. **Única definición permitida.** Este glosario es la única fuente de definiciones de COLBASOFT. Ningún documento posterior (arquitectura, modelo de datos, interfaz, pruebas, manuales) puede redefinir un término: lo cita.
2. **Mismo texto que el lenguaje ubicuo.** Los 55 términos centrales tienen en DOMAIN_MODEL Cap. 1 exactamente la misma definición.
3. **Sinónimos prohibidos.** No se usan ni como aclaración. El índice inverso (Cap. 3) remite de cada término prohibido al oficial.
4. **Definición prohibida.** Es la interpretación errónea que el término **no** debe recibir.
5. **Cambios.** Un término se agrega o se reformula solo con aprobación del Director; su ID `GL-nnn` no se reutiliza.

**Campos de cada entrada:** definición oficial · definición prohibida · sinónimos prohibidos · contexto (subdominio o ámbito) · documento de origen · relaciones.

**Distribución por contexto:** Movimientos 30 · Conteos y exactitud 19 · Trazabilidad 17 · Modelado 16 · Alertas y reglas 15 · Ubicaciones 15 · Inventario y existencia 15 · Transversal 12 · Proyecto 12 · Usuarios y acceso 10 · Catálogo textil 10 · Reportes y medición 8 · Identificación 7 · Auditoría 6 · Configuración 5 · Tareas y notificaciones 5 · Novedades 4 · Operación diaria 3 · Salidas 1

**Total de términos: 210.**


---

**ESTADO DEL CAPÍTULO — 1**

| | |
|---|---|
| **Completado** | Reglas de uso, campos y distribución |
| **Riesgos** | Uso de sinónimos en la interfaz o en documentos futuros |
| **Dependencias** | SPEC §0.5 · DOMAIN_MODEL Cap. 1 |
| **Hallazgos** | HD-01 |


---

# CAPÍTULO 2 — TÉRMINOS


## A

### GL-001 · Acción

| Campo | Contenido |
|---|---|
| **Definición oficial** | Intención de un actor (solicitar, escanear, consultar, aprobar) que el sistema evalúa; si se acepta, produce uno o más eventos; si no, puede producir un evento de rechazo. |
| **Definición prohibida** | No es un hecho consumado. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Evento de dominio (GL-069) |

### GL-002 · Actor

| Campo | Contenido |
|---|---|
| **Definición oficial** | Quien ejecuta un hecho: un usuario identificado o el Sistema. |
| **Definición prohibida** | Nunca vacío ni compartido. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Transversal |
| **Documento origen** | Nuevo (Fase 4) · VO-38 |
| **Relaciones** | Usuario (GL-196); Sistema (actor) (GL-164) |

### GL-003 · Administrador

| Campo | Contenido |
|---|---|
| **Definición oficial** | Rol que configura el sistema, gestiona usuarios, roles y estructura de bodega, y aprueba ajustes mayores; decisor de compra. |
| **Definición prohibida** | No puede editar movimientos ni la bitácora ni aprobar lo que solicitó. |
| **Sinónimos prohibidos** | superusuario |
| **Contexto** | Usuarios y acceso |
| **Documento origen** | SPEC · ROL-01 |
| **Relaciones** | Rol (GL-155); Ajuste mayor (GL-008) |

### GL-004 · Adopción

| Campo | Contenido |
|---|---|
| **Definición oficial** | Grado en que la operación real pasa efectivamente por el sistema; se mide con el KPI-24 y verificación de campo. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Proyecto |
| **Documento origen** | SPEC · KPI-24 · Monografía §4 |
| **Relaciones** | Usuario crítico (GL-197); KPI (GL-103) |

### GL-005 · Adopción escalonada

| Campo | Contenido |
|---|---|
| **Definición oficial** | Posibilidad de empezar a operar por procesos (entradas y salidas primero) y habilitar el resto después. |
| **Definición prohibida** | No es una implantación completa de una sola vez. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Proyecto |
| **Documento origen** | SPEC · RNF-024 (SRS RNF-ESC-005) · Monografía §8.2 |
| **Relaciones** | Adopción (GL-004) |

### GL-006 · Agregado

| Campo | Contenido |
|---|---|
| **Definición oficial** | Conjunto de entidades y objetos de valor que se modifica como una unidad para proteger sus invariantes; se accede por su raíz. |
| **Definición prohibida** | No es un módulo funcional. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Raíz de agregado (GL-134); Invariante (GL-092) |

### GL-007 · Ajuste ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Movimiento que modifica la existencia sin contrapartida física para hacer coincidir el registro con la realidad; exige motivo tipificado y aprobación de un tercero y queda marcado para siempre. Es el movimiento de mayor riesgo. |
| **Definición prohibida** | No es una edición del kardex ni una forma rutinaria de cuadrar el inventario. |
| **Sinónimos prohibidos** | corrección, nivelación, cuadre |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · CD-33 · Monografía §8.2 |
| **Relaciones** | Solicitud de ajuste (GL-169); Motivo tipificado (GL-111); Ajuste menor (GL-009); Ajuste mayor (GL-008) |

### GL-008 · Ajuste mayor

| Campo | Contenido |
|---|---|
| **Definición oficial** | Ajuste por encima del umbral configurado; lo aprueba el Administrador. |
| **Definición prohibida** | No lo aprueba quien lo solicitó. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · RN-024 (SRS RN-AJU-002) |
| **Relaciones** | Solicitud de ajuste (GL-169); Umbral (GL-188) |

### GL-009 · Ajuste menor

| Campo | Contenido |
|---|---|
| **Definición oficial** | Ajuste por debajo del umbral configurado; lo aprueba el Jefe de Bodega. |
| **Definición prohibida** | No lo aprueba quien lo solicitó. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · RN-024 (SRS RN-AJU-002) |
| **Relaciones** | Solicitud de ajuste (GL-169); Umbral (GL-188) |

### GL-010 · Ajuste por sobrante

| Campo | Contenido |
|---|---|
| **Definición oficial** | Ajuste que incorpora existencia encontrada sin registro, con motivo tipificado y aprobación del Jefe. |
| **Definición prohibida** | No es una entrada. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Novedades |
| **Documento origen** | SPEC · RN-043 (SRS RN-NOV-001) |
| **Relaciones** | Mercancía sin registro (GL-109) |

### GL-011 · Alcance de auditoría

| Campo | Contenido |
|---|---|
| **Definición oficial** | Período, referencias, ubicaciones, usuarios o tipos de movimiento que el Auditor revisa. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | campaña (no modelada como entidad, HD) |
| **Contexto** | Auditoría |
| **Documento origen** | SPEC · PN-13 |
| **Relaciones** | Observación de auditoría (GL-120) |

### GL-012 · Alerta ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Notificación generada automáticamente cuando una regla de negocio evalúa verdadera su condición de disparo. Manifestación operativa de la «inteligencia» del producto. |
| **Definición prohibida** | No es una predicción ni el resultado de un modelo de aprendizaje `[DC-07]`; no es una novedad. |
| **Sinónimos prohibidos** | aviso inteligente, predicción |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · CD-45 · DC-07 |
| **Relaciones** | Umbral (GL-188); Tipo de alerta (GL-180); Severidad (GL-162) |

### GL-013 · Ámbito

| Campo | Contenido |
|---|---|
| **Definición oficial** | Bodega y zonas en que un usuario opera; filtra consultas y tareas. Jefe, Administrador y Auditor no tienen restricción de ámbito de consulta. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Usuarios y acceso |
| **Documento origen** | SPEC · HU-008 (SRS HU-USR-004) |
| **Relaciones** | Usuario (GL-196); Zona (GL-199) |

### GL-014 · Antigüedad de lote

| Campo | Contenido |
|---|---|
| **Definición oficial** | Días transcurridos desde la fecha de ingreso de un lote; sobre el umbral configurado genera alerta informativa. |
| **Definición prohibida** | No es una fecha de vencimiento del producto (HD-10). |
| **Sinónimos prohibidos** | — |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · RN-074 (SRS RN-LOT-005) |
| **Relaciones** | Lote (GL-107); Alerta (GL-012) |

### GL-015 · Anulación ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Movimiento inverso que neutraliza el efecto de un movimiento previo erróneo; no borra el original: ambos permanecen en el kardex. Requiere motivo y autorización. |
| **Definición prohibida** | No es un borrado ni una edición. |
| **Sinónimos prohibidos** | reversión, borrado, eliminación |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · CD-34 |
| **Relaciones** | Movimiento (GL-112); Kardex (GL-102) |

### GL-016 · Aprobación propia

| Campo | Contenido |
|---|---|
| **Definición oficial** | Caso en que quien originó una solicitud la aprueba; la regla lo impide y, si se detecta, es hallazgo crítico. |
| **Definición prohibida** | No es permisible con ningún rol. |
| **Sinónimos prohibidos** | autoaprobación permitida |
| **Contexto** | Auditoría |
| **Documento origen** | SPEC · RN-023 (SRS RN-AJU-001) |
| **Relaciones** | Segregación de funciones (GL-158) |

### GL-017 · Atención de alerta

| Campo | Contenido |
|---|---|
| **Definición oficial** | Registro de la acción correctiva ejecutada ante una alerta: quién, cuándo y qué. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · RN-058 (SRS RN-ALE-004) |
| **Relaciones** | Alerta (GL-012) |

### GL-018 · Atribución

| Campo | Contenido |
|---|---|
| **Definición oficial** | Propiedad de toda acción que altera el estado de estar asignada a un usuario identificado o al Sistema como actor explícito. |
| **Definición prohibida** | No admite cuentas compartidas. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Transversal |
| **Documento origen** | SPEC · PR-05, RN-001 (SRS RN-INT-001) |
| **Relaciones** | Actor (GL-002); Usuario (GL-196) |

### GL-019 · Auditor

| Campo | Contenido |
|---|---|
| **Definición oficial** | Rol de revisión independiente con lectura completa y sin ninguna escritura sobre el inventario; su única escritura son observaciones de auditoría. |
| **Definición prohibida** | No aprueba, no ajusta, no configura. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Usuarios y acceso |
| **Documento origen** | SPEC · ROL-05, PR-02 |
| **Relaciones** | Rol (GL-155); Observación de auditoría (GL-120) |

### GL-020 · Automatización

| Campo | Contenido |
|---|---|
| **Definición oficial** | Uso de tecnologías para ejecutar tareas repetitivas sin intervención humana, con niveles parciales y totales. |
| **Definición prohibida** | En COLBASOFT no incluye IA `[DC-07]`. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Proyecto |
| **Documento origen** | Monografía §7.1 · SPEC |
| **Relaciones** | Inteligente (GL-091); Regla de negocio (GL-146) |

### GL-021 · Auxiliar de Bodega

| Campo | Contenido |
|---|---|
| **Definición oficial** | Rol del operario que mueve físicamente la mercancía; opera solo desde tablet. Es el usuario crítico del producto. |
| **Definición prohibida** | No ve costos ni indicadores de desempeño individual; no aprueba nada. |
| **Sinónimos prohibidos** | operario (como nombre de rol) |
| **Contexto** | Usuarios y acceso |
| **Documento origen** | SPEC · ROL-04 |
| **Relaciones** | Rol (GL-155); Usuario crítico (GL-197); Panel de tareas (GL-123) |


## B

### GL-022 · Baja por daño

| Campo | Contenido |
|---|---|
| **Definición oficial** | Salida con motivo de daño que exige aprobación del Jefe, observación y evidencia cualquiera sea la cantidad; alimenta el reporte de mermas. |
| **Definición prohibida** | No es un ajuste ni una salida ordinaria. |
| **Sinónimos prohibidos** | merma (como sinónimo del movimiento) |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · RN-052 (SRS RN-SAL-006) |
| **Relaciones** | Salida (GL-157); KPI-13 |

### GL-023 · Bitácora de auditoría ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Registro inmutable de toda acción relevante del sistema, incluidas las que no alteran el inventario: accesos, configuración, roles, aprobaciones, rechazos, anulaciones y exportaciones. No es editable por ningún rol. |
| **Definición prohibida** | No es el kardex ni un registro técnico de errores. |
| **Sinónimos prohibidos** | log, historial de sistema |
| **Contexto** | Auditoría |
| **Documento origen** | SPEC · CD-47 |
| **Relaciones** | Registro de bitácora (GL-144); Kardex (GL-102); Hallazgo crítico (GL-085) |

### GL-024 · Bloqueo de movimientos

| Campo | Contenido |
|---|---|
| **Definición oficial** | Impedimento de registrar movimientos entre el corte y el cierre de un conteo general, salvo excepciones del Jefe. |
| **Definición prohibida** | No aplica al conteo cíclico. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · RN-045 (SRS RN-CNT-006) |
| **Relaciones** | Conteo general (GL-045); Movimiento de excepción (GL-113) |

### GL-025 · Bodega ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Ámbito físico mayor donde se almacena inventario y ámbito de responsabilidad de un Jefe de Bodega; contiene zonas y al menos una zona de recepción. |
| **Definición prohibida** | No es la empresa ni un almacén de un tercero. |
| **Sinónimos prohibidos** | almacén (como sinónimo), depósito |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · CD-12 |
| **Relaciones** | Zona (GL-199); Ubicación (GL-186); Jefe de Bodega (GL-099) |


## C

### GL-026 · Cantidad

| Campo | Contenido |
|---|---|
| **Definición oficial** | Magnitud de existencia o de movimiento expresada en la unidad de medida de su referencia. |
| **Definición prohibida** | No se convierte entre unidades. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Transversal |
| **Documento origen** | Nuevo (Fase 4) · VO-13 |
| **Relaciones** | Unidad de medida (GL-195) |

### GL-027 · Capacidad de ubicación ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Cantidad máxima que admite una ubicación, expresada en la unidad configurada; se usa para proponer destinos y alertar sobreocupación. |
| **Definición prohibida** | No es la existencia actual de la ubicación. |
| **Sinónimos prohibidos** | cupo |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · CD-15 |
| **Relaciones** | Ubicación (GL-186); Ocupación (GL-121); Sobreocupación (GL-168) |

### GL-028 · Carga masiva de catálogo

| Campo | Contenido |
|---|---|
| **Definición oficial** | Incorporación del catálogo inicial desde un archivo tabular validado antes de cargar, con errores reportados por línea. |
| **Definición prohibida** | No es una integración con otro sistema. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Catálogo textil |
| **Documento origen** | SPEC · HU-014 (SRS HU-CAT-005) |
| **Relaciones** | Catálogo (GL-029); Bitácora de auditoría (GL-023) |

### GL-029 · Catálogo

| Campo | Contenido |
|---|---|
| **Definición oficial** | Conjunto de referencias, SKU, categorías y unidades de medida que define qué puede existir en inventario. |
| **Definición prohibida** | No es una lista de precios ni un catálogo comercial de venta `[DC-03]`. |
| **Sinónimos prohibidos** | maestro de productos |
| **Contexto** | Catálogo textil |
| **Documento origen** | SPEC · M-03 |
| **Relaciones** | Referencia (GL-142); SKU (GL-165); Categoría (GL-030) |

### GL-030 · Categoría ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Agrupación de referencias con propósito de organización, zona preferente y reporte. Una referencia pertenece a una sola categoría. |
| **Definición prohibida** | No es una zona física ni un tipo de movimiento. |
| **Sinónimos prohibidos** | familia, línea |
| **Contexto** | Catálogo textil |
| **Documento origen** | SPEC · CD-10 |
| **Relaciones** | Referencia (GL-142); Zona (GL-199) |

### GL-031 · Cierre automático de alerta

| Campo | Contenido |
|---|---|
| **Definición oficial** | Cierre de una alerta cuando su condición deja de cumplirse; queda marcada como no atendida si nadie actuó. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · RN-057 (SRS RN-ALE-003) |
| **Relaciones** | Alerta (GL-012) |

### GL-032 · Cierre de jornada

| Campo | Contenido |
|---|---|
| **Definición oficial** | Consolidación de la actividad del día que deja la bodega en estado consistente y traspasa los pendientes al turno siguiente. |
| **Definición prohibida** | No puede ejecutarse con registros sin sincronizar. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Operación diaria |
| **Documento origen** | SPEC · PN-14 |
| **Relaciones** | Jornada (GL-100); Pendiente de sincronización (GL-125) |

### GL-033 · Cobertura de conteo

| Campo | Contenido |
|---|---|
| **Definición oficial** | Proporción del inventario verificada en el período, o de ubicaciones cubiertas en un conteo general. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · KPI-03, RN-046 (SRS RN-CNT-007) |
| **Relaciones** | Conteo general (GL-045) |

### GL-034 · Código de lote

| Campo | Contenido |
|---|---|
| **Definición oficial** | Identidad de un lote, única dentro de su SKU; si la empresa no distingue lotes, el sistema genera uno por evento de entrada. |
| **Definición prohibida** | No es único en todo el sistema, solo dentro del SKU. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · RN-014 (SRS RN-MAE-006), RN-071 (SRS RN-LOT-001) |
| **Relaciones** | Lote (GL-107) |

### GL-035 · Código de referencia

| Campo | Contenido |
|---|---|
| **Definición oficial** | Identidad única de una referencia en todo el catálogo, activa o inactiva. |
| **Definición prohibida** | No se reutiliza al desactivar la referencia. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Catálogo textil |
| **Documento origen** | SPEC · RN-002 (SRS RN-MAE-001) |
| **Relaciones** | Referencia (GL-142) |

### GL-036 · Código de ubicación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Identidad de una ubicación, única dentro de su bodega. |
| **Definición prohibida** | No es único entre bodegas distintas. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · RN-014 (SRS RN-MAE-006) |
| **Relaciones** | Ubicación (GL-186) |

### GL-037 · Código QR

| Campo | Contenido |
|---|---|
| **Definición oficial** | Valor codificado de un identificador QR, irrepetible en toda la vida del sistema. |
| **Definición prohibida** | No es reutilizable tras anulación o reemplazo. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Identificación |
| **Documento origen** | Nuevo (Fase 4) · VO-07 |
| **Relaciones** | Identificador QR (GL-088) |

### GL-038 · Color ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Dimensión de variación de una referencia que expresa el acabado cromático; toma valores de un conjunto definido por la empresa. |
| **Definición prohibida** | No es un atributo libre de texto ni una referencia distinta. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Catálogo textil |
| **Documento origen** | SPEC · CD-04 |
| **Relaciones** | SKU (GL-165); Talla (GL-175) |

### GL-039 · Conciliación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Revisión de las diferencias de un conteo, considerando los movimientos ocurridos durante su ejecución, antes del cierre. |
| **Definición prohibida** | No modifica la existencia congelada. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · PN-08 |
| **Relaciones** | Conteo (GL-042); Existencia teórica congelada (GL-078) |

### GL-040 · Confirmación de entrada

| Campo | Contenido |
|---|---|
| **Definición oficial** | Verificación por una persona distinta de quien recibió, que incorpora la mercancía al inventario y genera lote y movimiento de entrada. |
| **Definición prohibida** | No puede hacerla quien registró la recepción física. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · PN-01, RN-057b (SRS RN-ENT-007) |
| **Relaciones** | Segregación de funciones (GL-158); Entrada (GL-065) |

### GL-041 · Contador

| Campo | Contenido |
|---|---|
| **Definición oficial** | Persona asignada a una tarea de conteo. |
| **Definición prohibida** | No es un rol: es una función que cumple un usuario. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · RN-040 (SRS RN-CNT-002) |
| **Relaciones** | Tarea de conteo (GL-176); Segundo conteo (GL-159) |

### GL-209 · Contenedor agrupado

| Campo | Contenido |
|---|---|
| **Definición oficial** | Contenedor rotulado que agrupa mercancía sin rotulado individual y se registra como una sola pieza con su cantidad de unidades; pertenece a un solo SKU + Lote (la mezcla de lotes está pendiente, HD-28). |
| **Definición prohibida** | No es una entidad aparte del modelo: es un tipo de pieza. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Inventario y existencia |
| **Documento origen** | Decisión F-6 · SPEC PN-02 E-03 · SPEC v1.2 · CD-49 |
| **Relaciones** | Pieza (GL-206); Paquete o bolsa (GL-208); Identificador QR (GL-088) |

### GL-042 · Conteo ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Proceso de verificación de la existencia física contra la registrada sobre un ámbito definido; estados: programado, en ejecución, en conciliación, cerrado, abortado o vencido. |
| **Definición prohibida** | No es un ajuste ni modifica la existencia por sí mismo. |
| **Sinónimos prohibidos** | toma física, inventario físico (como verbo) |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · CD-38 · Monografía §8.2 |
| **Relaciones** | Conteo cíclico (GL-044); Conteo general (GL-045); Exactitud del inventario (GL-072) |

### GL-043 · Conteo abortado

| Campo | Contenido |
|---|---|
| **Definición oficial** | Conteo detenido por el Jefe sin generar ajustes; sus conteos parciales se conservan como evidencia. |
| **Definición prohibida** | No es un conteo cerrado. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · PN-09 E-04 |
| **Relaciones** | Conteo (GL-042) |

### GL-044 · Conteo cíclico ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Conteo de un ámbito parcial (ubicaciones, referencias o categorías) ejecutable sin detener la operación. Mecanismo continuo de medición de exactitud. |
| **Definición prohibida** | No bloquea movimientos. |
| **Sinónimos prohibidos** | inventario rotativo |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · CD-39 |
| **Relaciones** | Conteo (GL-042); KPI-01 |

### GL-045 · Conteo general ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Conteo de la totalidad del inventario, que bloquea el registro de movimientos desde el corte hasta el cierre. |
| **Definición prohibida** | No es un conteo cíclico grande. |
| **Sinónimos prohibidos** | inventario anual |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · CD-40 |
| **Relaciones** | Bloqueo de movimientos (GL-024); KPI-02 |

### GL-046 · Conteo vencido

| Campo | Contenido |
|---|---|
| **Definición oficial** | Conteo no ejecutado o no cerrado dentro de su plazo; al exceder el máximo se libera la existencia congelada. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · RN-044 (SRS RN-CNT-005) |
| **Relaciones** | Conteo (GL-042); Alerta (GL-012) |

### GL-047 · Contraseña

| Campo | Contenido |
|---|---|
| **Definición oficial** | Credencial individual y secreta del usuario; su valor original no es recuperable por ningún medio. |
| **Definición prohibida** | No se registra en bitácora ni se muestra. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Usuarios y acceso |
| **Documento origen** | SPEC · RNF-002 (SRS RNF-SEG-002) |
| **Relaciones** | Usuario (GL-196); Sesión (GL-161) |

### GL-048 · Coordinador de Bodega

| Campo | Contenido |
|---|---|
| **Definición oficial** | Rol de mando medio en piso: confirma entradas, asigna ubicaciones, crea transferencias, programa conteos cíclicos, solicita ajustes y autoriza salidas bajo su umbral. |
| **Definición prohibida** | No aprueba sus propios ajustes ni cierra conteos. |
| **Sinónimos prohibidos** | supervisor (como sinónimo del rol) |
| **Contexto** | Usuarios y acceso |
| **Documento origen** | SPEC · ROL-03 |
| **Relaciones** | Rol (GL-155); Zona (GL-199) |

### GL-210 · Corte parcial

| Campo | Contenido |
|---|---|
| **Definición oficial** | Salida de una parte de una pieza —por ejemplo, metros cortados de un rollo—: descuenta la cantidad cortada y deja la pieza con su remanente y su identidad. Cumple las reglas de toda salida. |
| **Definición prohibida** | No es un movimiento interno ni una división de la pieza en dos (HD-29). |
| **Sinónimos prohibidos** | — |
| **Contexto** | Salidas |
| **Documento origen** | Decisión F-3 · RN-SAL-008 · SPEC v1.2 |
| **Relaciones** | Pieza (GL-206); Rollo (GL-207); Salida (GL-157); Movimiento (GL-112) |

### GL-049 · Criterio de asignación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Regla configurable, con orden de aplicación, que el sistema usa para proponer ubicación. |
| **Definición prohibida** | No es una regla estructural. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · HU-024 (SRS HU-BOD-005) |
| **Relaciones** | Propuesta de ubicación (GL-132) |


## D

### GL-050 · Dashboard operativo

| Campo | Contenido |
|---|---|
| **Definición oficial** | Vista inmediata por rol del estado de la bodega y de lo que requiere atención: existencia por estado, alertas, pendientes y exactitud vigente. |
| **Definición prohibida** | No es el tablero analítico de la herramienta externa `[DC-06]`. |
| **Sinónimos prohibidos** | tablero de BI |
| **Contexto** | Reportes y medición |
| **Documento origen** | SPEC · M-17 |
| **Relaciones** | Panel de tareas (GL-123); Alerta (GL-012) |

### GL-051 · Decisión constitucional

| Campo | Contenido |
|---|---|
| **Definición oficial** | Determinación del Director, inmodificable dentro del proyecto (DC-01…DC-08). |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Proyecto |
| **Documento origen** | SPEC · §0.1 |
| **Relaciones** | MVP (GL-116); Rol (GL-155); Inteligente (GL-091) |

### GL-052 · Desactivación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Paso de un elemento a estado inactivo: deja de participar en operaciones nuevas y conserva su historia. |
| **Definición prohibida** | No es eliminar. |
| **Sinónimos prohibidos** | eliminación, baja (de un maestro) |
| **Contexto** | Transversal |
| **Documento origen** | SPEC · RN-063 (SRS RN-MAE-007), RN-076 (SRS RN-MAE-008) |
| **Relaciones** | Eliminación lógica (GL-062); Reactivación (GL-135) |

### GL-053 · Descarte de alerta

| Campo | Contenido |
|---|---|
| **Definición oficial** | Cierre manual de una alerta sin acción correctiva, que exige motivo. |
| **Definición prohibida** | No se permite sin motivo. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · RN-058 (SRS RN-ALE-004) |
| **Relaciones** | Alerta (GL-012); Motivo tipificado (GL-111) |

### GL-054 · Desglose de existencia

| Campo | Contenido |
|---|---|
| **Definición oficial** | Reparto de la existencia de una unidad entre sus estados; la suma de las porciones es la existencia derivada del kardex. |
| **Definición prohibida** | No es un conjunto de valores independientes. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Inventario y existencia |
| **Documento origen** | Nuevo (Fase 4) · VO-15 |
| **Relaciones** | Estado de inventario (GL-068) |

### GL-055 · Despacho

| Campo | Contenido |
|---|---|
| **Definición oficial** | Confirmación, por escaneo del Auxiliar del origen, de que la mercancía de una transferencia salió; la pone en tránsito. |
| **Definición prohibida** | No es una salida del inventario. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · PN-06 |
| **Relaciones** | Transferencia (GL-183); Inventario en tránsito (GL-096) |

### GL-056 · Desviación de ubicación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Diferencia entre la ubicación propuesta y la confirmada; se registra como información operativa y no como falta imputable. |
| **Definición prohibida** | No es un error del operario ni un indicador de desempeño individual `[PR-06]`. |
| **Sinónimos prohibidos** | error de ubicación |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · RN-022 (SRS RN-MOV-003) |
| **Relaciones** | Propuesta de ubicación (GL-132); KPI-10 |

### GL-057 · Diferencia de inventario ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Existencia contada menos existencia teórica congelada; positiva es sobrante, negativa es faltante. |
| **Definición prohibida** | No es automáticamente un ajuste. |
| **Sinónimos prohibidos** | descuadre |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · CD-27 |
| **Relaciones** | Conteo (GL-042); Ajuste (GL-007); KPI-04 |

### GL-058 · Diferencia de transferencia

| Campo | Contenido |
|---|---|
| **Definición oficial** | Discrepancia entre lo despachado y lo recibido; si falta, abre novedad; si sobra, se rechaza la recepción; en ambos casos resuelve el Jefe. |
| **Definición prohibida** | No se ajusta automáticamente. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · RN-033 (SRS RN-MOV-007) |
| **Relaciones** | Transferencia (GL-183); Novedad (GL-118) |

### GL-059 · Discrepancia de integridad

| Campo | Contenido |
|---|---|
| **Definición oficial** | Diferencia entre la existencia y la suma de movimientos de una unidad, un lote o el total; es hallazgo crítico. |
| **Definición prohibida** | No es una diferencia de conteo. |
| **Sinónimos prohibidos** | lote inconsistente (HD-14) |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · RN-065 (SRS RN-INT-004) |
| **Relaciones** | Verificación de integridad (GL-198); Hallazgo crítico (GL-085) |

### GL-060 · Documento de entrada ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Registro que agrupa la mercancía esperada en un evento de recepción, con origen, referencias y cantidades; soporte contra el cual se verifica lo recibido. |
| **Definición prohibida** | No es una orden de compra ni un documento comercial `[DC-03]`. |
| **Sinónimos prohibidos** | remisión, ingreso, recepción (como sustantivo) |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · CD-35 |
| **Relaciones** | Entrada (GL-065); Origen de entrada (GL-122); Faltante de recepción (GL-080); Sobrante de recepción (GL-166) |

### GL-061 · Documento de respaldo

| Campo | Contenido |
|---|---|
| **Definición oficial** | Documento del dominio que originó un movimiento (documento de entrada, solicitud de salida, transferencia, solicitud de ajuste o conteo). |
| **Definición prohibida** | No es un documento comercial. |
| **Sinónimos prohibidos** | soporte comercial |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · CD-37 |
| **Relaciones** | Movimiento (GL-112); Kardex (GL-102) |


## E

### GL-062 · Eliminación lógica

| Campo | Contenido |
|---|---|
| **Definición oficial** | Principio por el cual nada se borra: los elementos se desactivan o se cierran y conservan su identidad histórica. |
| **Definición prohibida** | No existe borrado físico. |
| **Sinónimos prohibidos** | borrado |
| **Contexto** | Transversal |
| **Documento origen** | SPEC · RN-063 (SRS RN-MAE-007) |
| **Relaciones** | Desactivación (GL-052); Reactivación (GL-135) |

### GL-063 · Empresa de estudio

| Campo | Contenido |
|---|---|
| **Definición oficial** | Organización del sector textil del Eje Cafetero con la que se levanta el proceso real y se opera el piloto, sin identificación comercial. |
| **Definición prohibida** | No se nombra `[DC-01]`. |
| **Sinónimos prohibidos** | cliente, empresa X |
| **Contexto** | Proyecto |
| **Documento origen** | SPEC · DC-01 |
| **Relaciones** | Línea base (GL-106) |

### GL-064 · Entidad

| Campo | Contenido |
|---|---|
| **Definición oficial** | Elemento del dominio con identidad propia que persiste a través de sus cambios de estado. |
| **Definición prohibida** | No es una estructura de almacenamiento. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Objeto de valor (GL-119); Agregado (GL-006) |

### GL-065 · Entrada ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Movimiento que incrementa la existencia por incorporación de mercancía procedente del exterior de la bodega. |
| **Definición prohibida** | No es una compra ni una recepción física sin confirmar. |
| **Sinónimos prohibidos** | ingreso, remisión (como sinónimos) |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · CD-29 · Monografía §8.2 |
| **Relaciones** | Documento de entrada (GL-060); Confirmación de entrada (GL-040) |

### GL-066 · Escalamiento

| Campo | Contenido |
|---|---|
| **Definición oficial** | Traslado automático de una alerta, solicitud o novedad al rol superior al vencer su plazo o al coincidir solicitante y aprobador. |
| **Definición prohibida** | No es una reasignación manual. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Transversal |
| **Documento origen** | SPEC · RN-023 (SRS RN-AJU-001), RN-038 (SRS RN-AJU-005), RN-056 (SRS RN-ALE-002), RN-059 (SRS RN-NOV-002) |
| **Relaciones** | Plazo (GL-126); Rol (GL-155) |

### GL-067 · Escaneo

| Campo | Contenido |
|---|---|
| **Definición oficial** | Lectura de un identificador con la cámara de la tablet que resuelve el elemento identificado. |
| **Definición prohibida** | No es un evento del dominio: leer no cambia estado. |
| **Sinónimos prohibidos** | digitación |
| **Contexto** | Identificación |
| **Documento origen** | SPEC · M-06 |
| **Relaciones** | Identificador QR (GL-088); Selección manual (GL-160) |

### GL-068 · Estado de inventario ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Condición de una porción de existencia que determina qué puede hacerse con ella: Disponible, Reservado, En tránsito, Inmovilizado o En recepción; mutuamente excluyentes para una misma cantidad. |
| **Definición prohibida** | No es el estado de una referencia, de un lote ni de un documento. |
| **Sinónimos prohibidos** | estatus de stock |
| **Contexto** | Inventario y existencia |
| **Documento origen** | SPEC · CD-44 |
| **Relaciones** | Existencia (GL-074); Inventario disponible (GL-094) |

### GL-069 · Evento de dominio ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Hecho relevante para el negocio que ya ocurrió, con nombre en pasado, actor, entidad de origen y resultado; tiene ID permanente EV-<DOM>-nnn. |
| **Definición prohibida** | No es una acción (intención) ni un movimiento (que es un tipo particular de hecho sobre la existencia). |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Acción (GL-001); Movimiento (GL-112); Evento derivado (GL-070) |

### GL-070 · Evento derivado ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Evento que el Sistema genera automáticamente cuando una regla de negocio o un umbral evalúa verdadera su condición; nunca por predicción. |
| **Definición prohibida** | No es producto de inteligencia artificial `[DC-07]`. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Evento de dominio (GL-069); Regla de negocio (GL-146); Alerta (GL-012) |

### GL-071 · Evidencia

| Campo | Contenido |
|---|---|
| **Definición oficial** | Adjunto (fotografía o documento) que respalda una solicitud; obligatoria cuando el motivo lo exige. |
| **Definición prohibida** | No es opcional si el motivo la exige. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · RN-029 (SRS RN-AJU-003), RN-052 (SRS RN-SAL-006) |
| **Relaciones** | Motivo tipificado (GL-111); Ajuste (GL-007) |

### GL-072 · Exactitud del inventario ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Proporción de líneas contadas cuya existencia contada coincide con la teórica congelada; es el KPI-01 y el indicador central del compromiso de valor. |
| **Definición prohibida** | No tiene meta numérica hasta existir línea base. |
| **Sinónimos prohibidos** | precisión (como sinónimo del KPI) |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · CD-43 · Monografía §8.2 |
| **Relaciones** | KPI-01; Conteo (GL-042); Línea base (GL-106) |

### GL-073 · Exclusión de ubicación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Retiro justificado de una ubicación del alcance de un conteo general para permitir su cierre. |
| **Definición prohibida** | No se permite sin justificación. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · RN-046 (SRS RN-CNT-007) |
| **Relaciones** | Conteo general (GL-045); Justificación (GL-101) |

### GL-074 · Existencia ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Cantidad de una unidad de inventario presente en el sistema en un momento dado; siempre es la suma algebraica de sus movimientos confirmados, nunca un valor ingresado directamente. |
| **Definición prohibida** | No es un valor que se escriba o corrija a mano. |
| **Sinónimos prohibidos** | stock, saldo, disponible (como sustantivo genérico) |
| **Contexto** | Inventario y existencia |
| **Documento origen** | SPEC · CD-18 · Monografía §7.1 |
| **Relaciones** | Kardex (GL-102); Movimiento (GL-112); Estado de inventario (GL-068) |

### GL-075 · Existencia contada ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Cantidad física registrada por un contador; solo modifica la existencia si el cierre genera un ajuste aprobado. |
| **Definición prohibida** | No es un estado del inventario. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · CD-26 |
| **Relaciones** | Tarea de conteo (GL-176); Diferencia de inventario (GL-057) |

### GL-076 · Existencia histórica

| Campo | Contenido |
|---|---|
| **Definición oficial** | Existencia reconstruida desde el kardex a una fecha de corte; da siempre el mismo resultado para la misma fecha. |
| **Definición prohibida** | No es una copia guardada del pasado. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · HU-075 (SRS HU-INV-005) |
| **Relaciones** | Kardex (GL-102); Fecha de corte (GL-081) |

### GL-077 · Existencia sin movimiento

| Campo | Contenido |
|---|---|
| **Definición oficial** | Existencia que lleva más del umbral de días sin ningún movimiento. |
| **Definición prohibida** | No es existencia inmovilizada. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Reportes y medición |
| **Documento origen** | SPEC · KPI-17 |
| **Relaciones** | Kardex (GL-102) |

### GL-078 · Existencia teórica congelada ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Fotografía de la existencia tomada al iniciar un conteo contra la cual se compara lo contado; no se altera por movimientos posteriores. |
| **Definición prohibida** | No se muestra al contador. |
| **Sinónimos prohibidos** | saldo congelado |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · CD-25 |
| **Relaciones** | Conteo (GL-042); Diferencia de inventario (GL-057) |

### GL-079 · Exportación de datos

| Campo | Contenido |
|---|---|
| **Definición oficial** | Extracción de datos del sistema en formato tabular o estructurado; siempre queda en la bitácora con usuario, alcance y fecha. |
| **Definición prohibida** | No elude las restricciones de visibilidad por rol. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Reportes y medición |
| **Documento origen** | SPEC · RN-078 (SRS RN-AUD-003) |
| **Relaciones** | Bitácora de auditoría (GL-023); Herramienta analítica externa (GL-087) |


## F

### GL-080 · Faltante de recepción

| Campo | Contenido |
|---|---|
| **Definición oficial** | Diferencia en la que lo recibido es menor que lo esperado; se registra y notifica al Jefe sin bloquear la confirmación de lo recibido. |
| **Definición prohibida** | No es un ajuste. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · RN-006 (SRS RN-ENT-004) |
| **Relaciones** | Documento de entrada (GL-060) |

### GL-081 · Fecha de corte

| Campo | Contenido |
|---|---|
| **Definición oficial** | Instante de referencia de un conteo general o de una consulta histórica, declarado en todo resultado que lo use. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Transversal |
| **Documento origen** | SPEC · PN-09, HU-075 (SRS HU-INV-005) |
| **Relaciones** | Conteo general (GL-045); Existencia histórica (GL-076) |

### GL-082 · Fecha operativa

| Campo | Contenido |
|---|---|
| **Definición oficial** | Instante (fecha y hora) en que ocurrió un hecho, con su jornada; distinto del instante en que se sincronizó. |
| **Definición prohibida** | No es la fecha de sincronización (HD-16). |
| **Sinónimos prohibidos** | — |
| **Contexto** | Transversal |
| **Documento origen** | Nuevo (Fase 4) · VO-32 |
| **Relaciones** | Movimiento (GL-112); Sincronización (GL-163) |

### GL-083 · Frecuencia de errores de registro

| Campo | Contenido |
|---|---|
| **Definición oficial** | Ajustes correctivos, movimientos anulados y líneas de conteo con diferencia sobre el total de movimientos; es el KPI-08. |
| **Definición prohibida** | No se desglosa por persona ante el operario `[PR-06]`. |
| **Sinónimos prohibidos** | tasa de error del operario |
| **Contexto** | Reportes y medición |
| **Documento origen** | SPEC · KPI-08 · Monografía §8.2 |
| **Relaciones** | KPI (GL-103); Ajuste (GL-007); Anulación (GL-015) |


## G

### GL-084 · Gestión de inventarios

| Campo | Contenido |
|---|---|
| **Definición oficial** | Control de existencias para equilibrar disponibilidad de materiales y costos y prevenir rupturas o excesos. |
| **Definición prohibida** | No incluye la valorización contable en el MVP (HD-09). |
| **Sinónimos prohibidos** | — |
| **Contexto** | Proyecto |
| **Documento origen** | Monografía §7.1 |
| **Relaciones** | Existencia (GL-074); Ruptura de stock (GL-156); Sobre stock (GL-167) |


## H

### GL-085 · Hallazgo crítico

| Campo | Contenido |
|---|---|
| **Definición oficial** | Resultado de auditoría que indica una falla de integridad o de segregación: discrepancia de integridad, aprobación propia, movimiento sin usuario atribuible o discontinuidad de bitácora. |
| **Definición prohibida** | No es una observación ordinaria. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Auditoría |
| **Documento origen** | SPEC · PN-13 |
| **Relaciones** | Verificación de integridad (GL-198); Aprobación propia (GL-016) |

### GL-086 · Hallazgo del dominio

| Campo | Contenido |
|---|---|
| **Definición oficial** | Inconsistencia o vacío detectado al modelar entre la monografía, el SPEC, el SRS o el Prompt, registrado sin corregirse en silencio (HD-nn). |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Decisión constitucional (GL-051) |

### GL-087 · Herramienta analítica externa

| Campo | Contenido |
|---|---|
| **Definición oficial** | Sistema externo (Power BI) al que COLBASOFT expone datos estructurados; allí se construyen los tableros analíticos. |
| **Definición prohibida** | No forma parte del dominio de COLBASOFT. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Reportes y medición |
| **Documento origen** | SPEC · DC-06 |
| **Relaciones** | Exportación de datos (GL-079) |


## I

### GL-088 · Identificador QR ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Código único generado por el sistema, asociado a un SKU + Lote (QR de mercancía) o a una ubicación (QR de ubicación); medio primario de interacción del operario. El de mercancía no identifica ubicación, bodega ni cantidad, y no cambia al reubicar. Es de un solo uso: nunca se repite ni se reutiliza. Estados: generado, activo, reemplazado, anulado. |
| **Definición prohibida** | No es el código de barras del proveedor, ni un dato que el usuario digite, ni el identificador de una unidad de inventario (DF5-01). |
| **Sinónimos prohibidos** | etiqueta (como sinónimo del código), código de barras |
| **Contexto** | Identificación |
| **Documento origen** | SPEC · CD-08 · DC-08 · DF5-01 |
| **Relaciones** | Código QR (GL-037); Identificador secundario (GL-089); Lote (GL-107); Unidad de inventario (GL-193) |

### GL-089 · Identificador secundario ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Código de barras u otro código externo asociado a mercancía; admitido para consulta, nunca para escritura, y asociado a lo sumo a un QR de mercancía (un SKU + Lote). |
| **Definición prohibida** | No reemplaza al QR como identificador principal. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Identificación |
| **Documento origen** | SPEC · CD-09 · DC-08 |
| **Relaciones** | Identificador QR (GL-088) |

### GL-090 · Inmovilización

| Campo | Contenido |
|---|---|
| **Definición oficial** | Acto de impedir que una porción de existencia —o un lote completo— se mueva o salga sin autorización expresa. |
| **Definición prohibida** | No es una baja ni una salida. |
| **Sinónimos prohibidos** | bloqueo |
| **Contexto** | Inventario y existencia |
| **Documento origen** | SPEC · RN-036 (SRS RN-EXI-006) |
| **Relaciones** | Inventario inmovilizado (GL-097); Liberación (GL-105) |

### GL-091 · Inteligente

| Campo | Contenido |
|---|---|
| **Definición oficial** | En COLBASOFT significa exactamente automatización basada en reglas y analítica operativa por indicadores. |
| **Definición prohibida** | No significa aprendizaje automático, predicción, visión por computador, procesamiento de lenguaje natural ni IA generativa `[DC-07]`. |
| **Sinónimos prohibidos** | inteligencia artificial, IA |
| **Contexto** | Proyecto |
| **Documento origen** | SPEC · §1.6 · DC-07 |
| **Relaciones** | Regla de negocio (GL-146); KPI (GL-103); Alerta (GL-012) |

### GL-092 · Invariante

| Campo | Contenido |
|---|---|
| **Definición oficial** | Condición del dominio que debe cumplirse siempre, antes y después de cualquier cambio. |
| **Definición prohibida** | No es una política reactiva (que actúa cuando algo ocurre). |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Regla de negocio (GL-146); Política del dominio (GL-128) |

### GL-093 · Inventario ajustado

| Campo | Contenido |
|---|---|
| **Definición oficial** | Existencia cuyo valor fue modificado por un movimiento de ajuste; la marca es consultable y se deriva del kardex. |
| **Definición prohibida** | No es un estado de la existencia ni un error en sí mismo. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · CD-24 |
| **Relaciones** | Ajuste (GL-007); Kardex (GL-102) |

### GL-094 · Inventario disponible ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Porción de la existencia que puede comprometerse para una salida o transferencia: existencia menos reservado, inmovilizado, en tránsito y en recepción. Es la cifra que el operario ve por defecto. |
| **Definición prohibida** | No es la existencia total. |
| **Sinónimos prohibidos** | stock libre |
| **Contexto** | Inventario y existencia |
| **Documento origen** | SPEC · CD-19 |
| **Relaciones** | Existencia (GL-074); Reserva (GL-150) |

### GL-095 · Inventario en recepción

| Campo | Contenido |
|---|---|
| **Definición oficial** | Existencia ya incorporada al inventario en la zona de recepción, aún no ubicada ni disponible; es donde queda toda entrada confirmada. |
| **Definición prohibida** | No es disponible (DF5-02). |
| **Sinónimos prohibidos** | — |
| **Contexto** | Inventario y existencia |
| **Documento origen** | SPEC · CD-16, CD-44 |
| **Relaciones** | Zona de recepción (GL-203); Estado de inventario (GL-068) |

### GL-096 · Inventario en tránsito ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Existencia que salió de una ubicación origen y aún no se confirmó en su destino; no está disponible en ninguna de las dos y tiene plazo máximo. |
| **Definición prohibida** | No es existencia perdida ni ya recibida. |
| **Sinónimos prohibidos** | en camino |
| **Contexto** | Inventario y existencia |
| **Documento origen** | SPEC · CD-23 |
| **Relaciones** | Transferencia (GL-183); Movimiento interno (GL-114); Tiempo máximo en tránsito (GL-179) |

### GL-097 · Inventario inmovilizado ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Porción de la existencia que existe físicamente pero no puede moverse ni salir sin autorización expresa: dañada, en verificación, bloqueada o en cuarentena. |
| **Definición prohibida** | No es existencia dada de baja. |
| **Sinónimos prohibidos** | bloqueado (como sustantivo), congelado |
| **Contexto** | Inventario y existencia |
| **Documento origen** | SPEC · CD-22 |
| **Relaciones** | Inmovilización (GL-090); Zona de cuarentena (GL-201); Lote (GL-107) |

### GL-098 · Inventario reservado ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Porción de la existencia comprometida por una salida autorizada o una transferencia creada, aún no ejecutada. Sigue en la bodega pero no puede comprometerse otra vez. |
| **Definición prohibida** | No es existencia que ya salió. |
| **Sinónimos prohibidos** | apartado |
| **Contexto** | Inventario y existencia |
| **Documento origen** | SPEC · CD-20 |
| **Relaciones** | Reserva (GL-150); Solicitud de salida (GL-170); Transferencia (GL-183) |


## J

### GL-099 · Jefe de Bodega

| Campo | Contenido |
|---|---|
| **Definición oficial** | Rol responsable de la exactitud del inventario: aprueba ajustes menores, autoriza salidas, cierra conteos y resuelve diferencias. |
| **Definición prohibida** | No gestiona usuarios ni la estructura de la bodega. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Usuarios y acceso |
| **Documento origen** | SPEC · ROL-02 |
| **Relaciones** | Rol (GL-155); Conteo (GL-042); Ajuste menor (GL-009) |

### GL-100 · Jornada

| Campo | Contenido |
|---|---|
| **Definición oficial** | Período operativo diario de la bodega al que pertenecen los hechos y que termina con el cierre de jornada. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Operación diaria |
| **Documento origen** | SPEC · PN-14 |
| **Relaciones** | Cierre de jornada (GL-032); Turno (GL-185) |

### GL-101 · Justificación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Texto obligatorio que explica una decisión de rechazo, descarte, exclusión o cancelación. |
| **Definición prohibida** | No sustituye a un motivo tipificado. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Transversal |
| **Documento origen** | SPEC · RN-062 (SRS RN-AJU-006), RN-046 (SRS RN-CNT-007) |
| **Relaciones** | Motivo tipificado (GL-111) |


## K

### GL-102 · Kardex ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Registro cronológico, completo e inmutable de todos los movimientos de una unidad de inventario desde su creación. Es la fuente de verdad de la existencia: la existencia se deriva del kardex, nunca al revés. |
| **Definición prohibida** | No es la bitácora del sistema ni un reporte editable. |
| **Sinónimos prohibidos** | log, historial (de inventario), libro |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · CD-37 · Monografía §7.1, §8.2 |
| **Relaciones** | Movimiento (GL-112); Existencia (GL-074); Trazabilidad (GL-184) |

### GL-103 · KPI ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Indicador operativo calculado por el sistema sobre su propio registro; existen 24 y ninguno tiene meta numérica sin línea base. |
| **Definición prohibida** | No es una meta ni un indicador de desempeño individual ante el operario. |
| **Sinónimos prohibidos** | métrica de desempeño personal |
| **Contexto** | Reportes y medición |
| **Documento origen** | SPEC · Cap. 10 |
| **Relaciones** | Exactitud del inventario (GL-072); Línea base (GL-106) |


## L

### GL-104 · Lenguaje ubicuo

| Campo | Contenido |
|---|---|
| **Definición oficial** | Vocabulario oficial y único del dominio, compartido por negocio y equipo, que se usa sin sinónimos en documentos, conversaciones e interfaz. |
| **Definición prohibida** | No admite sinónimos ni términos técnicos de implementación. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Hallazgo del dominio (GL-086) |

### GL-105 · Liberación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Acto de devolver a sus estados normales la existencia de un lote inmovilizado; solo Jefe o Administrador, con motivo tipificado. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | desbloqueo |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · RN-073 (SRS RN-LOT-004) |
| **Relaciones** | Inmovilización (GL-090); Lote (GL-107) |

### GL-106 · Línea base

| Campo | Contenido |
|---|---|
| **Definición oficial** | Medición del desempeño antes de implantar el sistema; no existe aún y sin ella los KPI-01, 05 y 08 no demuestran mejora. |
| **Definición prohibida** | No es una meta. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Proyecto |
| **Documento origen** | SPEC · §13.1 · Auditoría C.2.4 |
| **Relaciones** | KPI (GL-103); Empresa de estudio (GL-063) |

### GL-107 · Lote ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Conjunto de mercancía de un mismo SKU que ingresó en un mismo evento de entrada y comparte origen y condiciones. Permite rastrear un problema hasta su procedencia y se inmoviliza y libera como un todo. |
| **Definición prohibida** | No es un lote de producción ni agrupa referencias, tallas o colores distintos. |
| **Sinónimos prohibidos** | partida, tanda |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · CD-06 · Monografía §7.1 |
| **Relaciones** | SKU (GL-165); Unidad de inventario (GL-193); Inmovilización (GL-090); Documento de entrada (GL-060) |

### GL-108 · Lote habilitado

| Campo | Contenido |
|---|---|
| **Definición oficial** | Estado del lote cuya existencia sigue sus estados normales (no inmovilizado). |
| **Definición prohibida** | No significa «disponible»: la disponibilidad es un estado de la existencia. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Trazabilidad |
| **Documento origen** | Nuevo (Fase 4) · HD-19 |
| **Relaciones** | Lote (GL-107); Inmovilización (GL-090) |


## M

### GL-109 · Mercancía sin registro

| Campo | Contenido |
|---|---|
| **Definición oficial** | Mercancía encontrada en la bodega que no existe en el sistema; no se cuenta ni se usa hasta ser identificada e incorporada por ajuste por sobrante aprobado. |
| **Definición prohibida** | No es un sobrante de recepción. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Novedades |
| **Documento origen** | SPEC · RN-043 (SRS RN-NOV-001) |
| **Relaciones** | Ajuste por sobrante (GL-010); Novedad (GL-118) |

### GL-110 · Motivo aplicado

| Campo | Contenido |
|---|---|
| **Definición oficial** | Motivo tipificado seleccionado en una operación, junto con el texto complementario opcional. |
| **Definición prohibida** | No es solo texto libre. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | Nuevo (Fase 4) · VO-22 |
| **Relaciones** | Motivo tipificado (GL-111) |

### GL-111 · Motivo tipificado ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Causa seleccionada de una lista cerrada, obligatoria en ajustes, anulaciones, salidas, inmovilizaciones, cancelaciones y descartes de alerta. El texto libre nunca lo sustituye. |
| **Definición prohibida** | No es un comentario libre. |
| **Sinónimos prohibidos** | razón libre, observación (como sustituto) |
| **Contexto** | Configuración |
| **Documento origen** | SPEC · CD-36 |
| **Relaciones** | Ajuste (GL-007); Salida (GL-157); Evidencia (GL-071); Justificación (GL-101) |

### GL-112 · Movimiento ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Hecho registrado que altera la existencia o la ubicación de una unidad de inventario. Unidad transaccional del sistema; inmutable una vez confirmado. Nada cambia en el inventario sin un movimiento. |
| **Definición prohibida** | No es cualquier acción del usuario ni un registro de bitácora. |
| **Sinónimos prohibidos** | transacción, registro, apunte |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · CD-28 · Monografía §8.2 |
| **Relaciones** | Kardex (GL-102); Entrada (GL-065); Salida (GL-157); Ajuste (GL-007); Anulación (GL-015) |

### GL-113 · Movimiento de excepción

| Campo | Contenido |
|---|---|
| **Definición oficial** | Movimiento autorizado por el Jefe durante el bloqueo de un conteo general y marcado como excepción en el kardex. |
| **Definición prohibida** | No es un movimiento normal durante el conteo. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · RN-045 (SRS RN-CNT-006) |
| **Relaciones** | Conteo general (GL-045); Bloqueo de movimientos (GL-024) |

### GL-114 · Movimiento interno ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Movimiento que cambia la ubicación de existencia dentro de la misma bodega sin alterar la existencia total; incluye la primera ubicación de la mercancía en recepción. |
| **Definición prohibida** | No es una transferencia entre ámbitos con responsables distintos. |
| **Sinónimos prohibidos** | traslado, reubicación (como sinónimos del movimiento) |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · CD-31 |
| **Relaciones** | Transferencia (GL-183); Ubicación (GL-186) |

### GL-115 · Movimiento inverso

| Campo | Contenido |
|---|---|
| **Definición oficial** | Movimiento de cantidad y sentido opuestos a otro, usado para anularlo o para el retorno al origen de una transferencia cancelada en tránsito. |
| **Definición prohibida** | No modifica el movimiento original. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · RN-012 (SRS RN-INT-002), RN-035 (SRS RN-MOV-009) |
| **Relaciones** | Anulación (GL-015) |

### GL-116 · MVP

| Campo | Contenido |
|---|---|
| **Definición oficial** | Conjunto mínimo con el que la bodega opera íntegramente en el sistema, con trazabilidad completa y capacidad de medir su impacto. |
| **Definición prohibida** | No incluye ventas, compras completas, producción, contabilidad, nómina, CRM, facturación ni IA `[DC-03]` `[DC-07]`. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Proyecto |
| **Documento origen** | SPEC · §12.2 · SRS Cap. 12 |
| **Relaciones** | Decisión constitucional (GL-051) |


## N

### GL-117 · Notificación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Aviso dentro del sistema web al usuario que debe actuar o conocer un resultado; no expone información fuera de su ámbito. |
| **Definición prohibida** | No es una aplicación móvil nativa `[DC-05]`. |
| **Sinónimos prohibidos** | push |
| **Contexto** | Tareas y notificaciones |
| **Documento origen** | SPEC · M-20 |
| **Relaciones** | Tarea operativa (GL-177); Alerta (GL-012) |

### GL-118 · Novedad ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Reporte de una anomalía física observada por un operario que el sistema no puede detectar por sí solo; también la abre el Sistema al rechazar en la sincronización un registro que describe un hecho físico ya realizado. Nunca se elimina: se cierra. No se imputa al reportante. |
| **Definición prohibida** | No es una alerta (las alertas las genera el sistema) ni una falta del operario. |
| **Sinónimos prohibidos** | reclamo, incidente (como sinónimos) |
| **Contexto** | Novedades |
| **Documento origen** | SPEC · CD-48 |
| **Relaciones** | Tipo de novedad (GL-181); Ajuste (GL-007); Mercancía sin registro (GL-109) |


## O

### GL-119 · Objeto de valor

| Campo | Contenido |
|---|---|
| **Definición oficial** | Elemento del dominio definido solo por sus atributos, sin identidad propia e inmutable: para cambiarlo se reemplaza. |
| **Definición prohibida** | No tiene ciclo de vida propio. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Entidad (GL-064) |

### GL-120 · Observación de auditoría ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Hallazgo o comentario del Auditor sobre un movimiento, unidad, período o usuario, guardado en un registro separado que no altera el inventario; se cierra con respuesta. |
| **Definición prohibida** | No es una corrección del inventario. |
| **Sinónimos prohibidos** | ajuste del auditor |
| **Contexto** | Auditoría |
| **Documento origen** | SPEC · RN-064 (SRS RN-AUD-002) |
| **Relaciones** | Auditor (GL-019); Bitácora de auditoría (GL-023) |

### GL-121 · Ocupación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Cantidad de existencia que aloja una ubicación frente a su capacidad. |
| **Definición prohibida** | No es calculable entre unidades de medida distintas sin una regla de equivalencia (HD-17). |
| **Sinónimos prohibidos** | — |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · KPI-18 |
| **Relaciones** | Capacidad de ubicación (GL-027); Sobreocupación (GL-168) |

### GL-122 · Origen de entrada

| Campo | Contenido |
|---|---|
| **Definición oficial** | Procedencia declarada de la mercancía que entra. |
| **Definición prohibida** | No es un proveedor como entidad comercial `[DC-03]`. |
| **Sinónimos prohibidos** | proveedor (como entidad) |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · CD-35 |
| **Relaciones** | Documento de entrada (GL-060) |


## P

### GL-123 · Panel de tareas

| Campo | Contenido |
|---|---|
| **Definición oficial** | Vista del usuario con sus tareas ordenadas por prioridad; es lo único que ve el Auxiliar en lugar del dashboard. |
| **Definición prohibida** | No muestra indicadores de desempeño individual. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Tareas y notificaciones |
| **Documento origen** | SPEC · HU-092 (SRS HU-DSH-002) |
| **Relaciones** | Tarea operativa (GL-177); Auxiliar de Bodega (GL-021) |

### GL-208 · Paquete o bolsa

| Campo | Contenido |
|---|---|
| **Definición oficial** | Tipo de pieza propio de las referencias que se cuentan en unidades; tiene cantidad propia de unidades. |
| **Definición prohibida** | No es un contenedor agrupado ni una unidad de inventario. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Inventario y existencia |
| **Documento origen** | Decisión F-1 · SPEC v1.2 · CD-49 |
| **Relaciones** | Pieza (GL-206); Contenedor agrupado (GL-209); Unidad de medida (GL-195) |

### GL-124 · Parámetro de configuración

| Campo | Contenido |
|---|---|
| **Definición oficial** | Valor configurable por el Administrador, dentro de un rango admisible, que gobierna umbrales, plazos y políticas; su cambio queda en bitácora y no es retroactivo. |
| **Definición prohibida** | No alcanza las reglas estructurales. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Configuración |
| **Documento origen** | SPEC · M-19 |
| **Relaciones** | Umbral (GL-188); Plazo (GL-126); Regla configurable (GL-145) |

### GL-125 · Pendiente de sincronización

| Campo | Contenido |
|---|---|
| **Definición oficial** | Estado de un movimiento registrado sin conectividad; impide confirmar documentos y cerrar la jornada. |
| **Definición prohibida** | No es un movimiento confirmado. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · RN-054 (SRS RN-INT-003) |
| **Relaciones** | Movimiento (GL-112); Sincronización (GL-163) |

### GL-206 · Pieza ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Unidad física individual de mercancía dentro de un lote —rollo, paquete o bolsa, o contenedor agrupado— con cantidad propia registrada en la recepción e identidad interna en el sistema. Pertenece a un solo SKU + Lote y a una sola ubicación; el QR no la identifica: el operario la selecciona tras el escaneo. |
| **Definición prohibida** | No es la unidad de inventario (que es SKU + Lote + Ubicación y agrupa piezas) ni tiene un QR propio. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Inventario y existencia |
| **Documento origen** | Decisiones Q-11, F-1, F-2, F-4, F-6 · SPEC v1.2 · CD-49 |
| **Relaciones** | Unidad de inventario (GL-193); Lote (GL-107); Rollo (GL-207); Paquete o bolsa (GL-208); Contenedor agrupado (GL-209); Corte parcial (GL-210) |

### GL-126 · Plazo

| Campo | Contenido |
|---|---|
| **Definición oficial** | Duración máxima configurable de un estado (tránsito, reserva, aprobación, novedad, conteo, atención de alerta, inactividad). |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Configuración |
| **Documento origen** | SPEC · M-19 |
| **Relaciones** | Escalamiento (GL-066); Parámetro de configuración (GL-124) |

### GL-127 · Política de toma

| Campo | Contenido |
|---|---|
| **Definición oficial** | Criterio configurable para indicar de qué ubicación tomar en una salida: primero en entrar primero en salir por lote, ubicación de mayor cantidad o más próxima. |
| **Definición prohibida** | No es una regla estructural. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · RN-049 (SRS RN-SAL-003) |
| **Relaciones** | Preparación de salida (GL-130) |

### GL-128 · Política del dominio

| Campo | Contenido |
|---|---|
| **Definición oficial** | Regla reactiva del tipo «cuando ocurre X, entonces Y» (por ejemplo, escalar al vencer un plazo); se manifiesta como evento derivado. |
| **Definición prohibida** | No es una invariante. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Evento derivado (GL-070); Invariante (GL-092) |

### GL-129 · Prenda ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Artículo textil terminado o insumo textil que la empresa almacena. Es el objeto físico del que hablan las personas; el sistema no lo controla directamente sino a través de su Referencia y de sus unidades de inventario. |
| **Definición prohibida** | No es la unidad que el sistema controla ni un registro del catálogo. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Catálogo textil |
| **Documento origen** | SPEC · CD-01 · Monografía §5, §7.1 |
| **Relaciones** | Referencia (GL-142); Unidad de inventario (GL-193) |

### GL-130 · Preparación de salida

| Campo | Contenido |
|---|---|
| **Definición oficial** | Toma física de la mercancía autorizada, guiada por la política de toma y validada por escaneo. |
| **Definición prohibida** | No es la salida misma: la salida se registra al confirmar la preparación. |
| **Sinónimos prohibidos** | picking |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · PN-10 |
| **Relaciones** | Política de toma (GL-127); Solicitud de salida (GL-170) |

### GL-204 · Primera ubicación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Movimiento interno que lleva existencia en recepción desde la ubicación de la zona de recepción hasta su ubicación destino, donde queda disponible; queda en el kardex como cualquier movimiento. |
| **Definición prohibida** | No es un cambio de estado sin movimiento, ni una asignación que se registre fuera del kardex. |
| **Sinónimos prohibidos** | asignación de ubicación (como hecho sin movimiento) |
| **Contexto** | Movimientos |
| **Documento origen** | DF5-03 · RN-MOV-010 · SPEC PN-03 |
| **Relaciones** | Movimiento interno (GL-114); Inventario en recepción (GL-095); Zona de recepción (GL-203) |

### GL-131 · Prioridad de tarea

| Campo | Contenido |
|---|---|
| **Definición oficial** | Orden en que el panel presenta las tareas; su escala no está definida (HD-15). |
| **Definición prohibida** | No es la severidad de una alerta. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Tareas y notificaciones |
| **Documento origen** | SPEC · HU-092 (SRS HU-DSH-002) |
| **Relaciones** | Panel de tareas (GL-123) |

### GL-132 · Propuesta de ubicación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Ubicación destino que el sistema sugiere según los criterios configurados (zona por categoría, capacidad, agrupación por referencia). Es sugerencia, no imposición. |
| **Definición prohibida** | No obliga al operario ni su desviación es una falta. |
| **Sinónimos prohibidos** | asignación obligatoria |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · RN-020 (SRS RN-MOV-001), PN-03 |
| **Relaciones** | Desviación de ubicación (GL-056); Criterio de asignación (GL-049) |

### GL-133 · PYME textil

| Campo | Contenido |
|---|---|
| **Definición oficial** | Pequeña o mediana empresa del sector textil; su definición legal para el proyecto sigue pendiente (A-03). |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Proyecto |
| **Documento origen** | Monografía §5 |
| **Relaciones** | Empresa de estudio (GL-063) |


## R

### GL-134 · Raíz de agregado

| Campo | Contenido |
|---|---|
| **Definición oficial** | Entidad por la que se accede y se modifica un agregado; guardiana de sus invariantes. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Agregado (GL-006) |

### GL-135 · Reactivación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Vuelta de un elemento inactivo a estado activo, registrada en bitácora. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Transversal |
| **Documento origen** | SPEC · RN-077 (SRS RN-MAE-009) |
| **Relaciones** | Desactivación (GL-052) |

### GL-136 · Reasignación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Cambio del responsable de una tarea, registrando a ambos y sin violar la regla del segundo conteo. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Tareas y notificaciones |
| **Documento origen** | SPEC · HU-103 (SRS HU-TAR-003) |
| **Relaciones** | Tarea operativa (GL-177); Segundo conteo (GL-159) |

### GL-137 · Recepción de transferencia

| Campo | Contenido |
|---|---|
| **Definición oficial** | Confirmación, por escaneo del Auxiliar del destino, de que la mercancía de una transferencia llegó; se compara con lo despachado. |
| **Definición prohibida** | No es una entrada. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · PN-06 |
| **Relaciones** | Transferencia (GL-183); Diferencia de transferencia (GL-058) |

### GL-138 · Recepción física

| Campo | Contenido |
|---|---|
| **Definición oficial** | Conteo y registro, línea por línea, de la mercancía que llega contra el documento de entrada, hecho desde la tablet. |
| **Definición prohibida** | No incorpora la mercancía al inventario: eso ocurre al confirmar. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · PN-01 |
| **Relaciones** | Documento de entrada (GL-060); Confirmación de entrada (GL-040) |

### GL-139 · Recepción parcial

| Campo | Contenido |
|---|---|
| **Definición oficial** | Estado del documento de entrada cuya recepción se interrumpió y puede continuar, incluso por otro usuario. |
| **Definición prohibida** | No es una recepción con faltante. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · PN-01 E-06 |
| **Relaciones** | Documento de entrada (GL-060) |

### GL-205 · Rechazado en sincronización

| Campo | Contenido |
|---|---|
| **Definición oficial** | Estado final de un registro retenido sin conectividad que, al validarse de nuevo en la sincronización, ya no cumplía las reglas: no se aplicó y conserva su motivo; si describía un hecho físico, abrió una novedad. |
| **Definición prohibida** | No es un movimiento anulado (nunca se confirmó) ni un registro perdido. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Trazabilidad |
| **Documento origen** | DF5-05 · RN-INT-008 |
| **Relaciones** | Sincronización (GL-163); Pendiente de sincronización (GL-125); Novedad (GL-118) |

### GL-140 · Recibido con novedad

| Campo | Contenido |
|---|---|
| **Definición oficial** | Estado del documento de entrada con faltante, sobrante o daño registrados. |
| **Definición prohibida** | No es lo mismo que una novedad de mercancía. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · PN-01 |
| **Relaciones** | Faltante de recepción (GL-080); Sobrante de recepción (GL-166) |

### GL-141 · Recibido conforme

| Campo | Contenido |
|---|---|
| **Definición oficial** | Estado del documento de entrada en el que lo recibido coincide con lo esperado. |
| **Definición prohibida** | No es confirmado. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · PN-01 |
| **Relaciones** | Documento de entrada (GL-060) |

### GL-142 · Referencia ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Identificador comercial de un modelo o artículo textil, independiente de talla, color y lote. Es la unidad de catálogo; se activa y desactiva, nunca se elimina. |
| **Definición prohibida** | No es una prenda física, ni un SKU, ni un código de barras de proveedor. |
| **Sinónimos prohibidos** | producto (designa a COLBASOFT, HD-01), modelo, estilo, artículo |
| **Contexto** | Catálogo textil |
| **Documento origen** | SPEC · CD-02 |
| **Relaciones** | SKU (GL-165); Categoría (GL-030); Unidad de medida (GL-195); Código de referencia (GL-035) |

### GL-143 · Registro

| Campo | Contenido |
|---|---|
| **Definición oficial** | Constancia persistente de un hecho: línea de kardex, registro de bitácora u observación. |
| **Definición prohibida** | No es sinónimo de «movimiento» (SPEC §0.5). |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Kardex (GL-102); Bitácora de auditoría (GL-023) |

### GL-144 · Registro de bitácora

| Campo | Contenido |
|---|---|
| **Definición oficial** | Cada constancia individual de la bitácora; se agrega y nunca se modifica. |
| **Definición prohibida** | No se edita ni se purga. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Auditoría |
| **Documento origen** | Nuevo (Fase 4) · E-21 |
| **Relaciones** | Bitácora de auditoría (GL-023) |

### GL-145 · Regla configurable

| Campo | Contenido |
|---|---|
| **Definición oficial** | Regla cuyo umbral se ajusta en la configuración pero cuya lógica no puede desactivarse. |
| **Definición prohibida** | No es desactivable. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · §9 |
| **Relaciones** | Regla de negocio (GL-146); Umbral (GL-188) |

### GL-146 · Regla de negocio ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Enunciado explícito que el sistema evalúa para impedir estados inválidos, disparar alertas o ejecutar acciones sin intervención humana. Es el corazón de la «inteligencia» del producto. |
| **Definición prohibida** | No es un modelo predictivo ni lógica oculta. |
| **Sinónimos prohibidos** | algoritmo inteligente |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · Cap. 9 · SRS Cap. 8 |
| **Relaciones** | Regla estructural (GL-147); Regla configurable (GL-145); Invariante (GL-092) |

### GL-147 · Regla estructural

| Campo | Contenido |
|---|---|
| **Definición oficial** | Regla inviolable y no parametrizable; ningún rol puede eludirla, incluido el Administrador. |
| **Definición prohibida** | No se configura (DEC-04: toda regla estructural es no configurable). |
| **Sinónimos prohibidos** | — |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · §9.1 |
| **Relaciones** | Regla de negocio (GL-146); Invariante (GL-092) |

### GL-148 · Reimpresión

| Campo | Contenido |
|---|---|
| **Definición oficial** | Impresión de otra copia del mismo QR por deterioro o ilegibilidad, con motivo. Conserva el mismo identificador: no crea una nueva identidad ni cambia su estado, por lo que las demás copias del QR siguen válidas. |
| **Definición prohibida** | No emite un código nuevo ni deja reemplazado el anterior (Q-09). |
| **Sinónimos prohibidos** | reetiquetado |
| **Contexto** | Identificación |
| **Documento origen** | SPEC · RN-018 (SRS RN-IDE-004) |
| **Relaciones** | Identificador QR (GL-088) |

### GL-149 · Reporte

| Campo | Contenido |
|---|---|
| **Definición oficial** | Información consolidada generada a demanda o programada, que declara fecha, hora y usuario de generación; nunca modifica datos. |
| **Definición prohibida** | No es un tablero analítico `[DC-06]`. |
| **Sinónimos prohibidos** | dashboard analítico |
| **Contexto** | Reportes y medición |
| **Documento origen** | SPEC · M-16 |
| **Relaciones** | Exportación de datos (GL-079); KPI (GL-103) |

### GL-150 · Reserva

| Campo | Contenido |
|---|---|
| **Definición oficial** | Acto y resultado de comprometer existencia disponible para una salida autorizada o una transferencia creada; se libera al ejecutarse, cancelarse o vencer. |
| **Definición prohibida** | No descuenta existencia. |
| **Sinónimos prohibidos** | apartado |
| **Contexto** | Inventario y existencia |
| **Documento origen** | SPEC · RN-031 (SRS RN-EXI-004), RN-051 (SRS RN-SAL-005) |
| **Relaciones** | Inventario reservado (GL-098) |

### GL-151 · Resistencia a la automatización

| Campo | Contenido |
|---|---|
| **Definición oficial** | Barreras culturales, financieras y técnicas que retrasan la adopción de tecnologías; razón de los requisitos de usabilidad y del principio «registrar, no castigar». |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Proyecto |
| **Documento origen** | Monografía §7.1 |
| **Relaciones** | Adopción (GL-004); Usuario crítico (GL-197) |

### GL-152 · Resultado de línea de conteo

| Campo | Contenido |
|---|---|
| **Definición oficial** | Clasificación de una línea contada: conforme, sobrante o faltante. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · PN-08 |
| **Relaciones** | Diferencia de inventario (GL-057) |

### GL-153 · Retención local

| Campo | Contenido |
|---|---|
| **Definición oficial** | Conservación en el dispositivo de un registro hecho sin conectividad, hasta sincronizarlo. |
| **Definición prohibida** | No confirma el registro. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · RN-054 (SRS RN-INT-003) |
| **Relaciones** | Sincronización (GL-163) |

### GL-154 · Retorno

| Campo | Contenido |
|---|---|
| **Definición oficial** | Vuelta de mercancía que había salido; se registra como entrada nueva que referencia la salida original, sin reversar la salida. |
| **Definición prohibida** | No es una anulación de la salida. |
| **Sinónimos prohibidos** | devolución (como reversión) |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · RN-053 (SRS RN-SAL-007) |
| **Relaciones** | Entrada (GL-065); Salida (GL-157) |

### GL-155 · Rol ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Función oficial de un usuario; existen exactamente cinco: Administrador, Jefe de Bodega, Coordinador de Bodega, Auxiliar de Bodega y Auditor. |
| **Definición prohibida** | No se crean roles adicionales `[DC-04]`; el Sistema no es un rol. |
| **Sinónimos prohibidos** | perfil (como sinónimo), cargo |
| **Contexto** | Usuarios y acceso |
| **Documento origen** | SPEC · DC-04 |
| **Relaciones** | Usuario (GL-196); Segregación de funciones (GL-158) |

### GL-207 · Rollo

| Campo | Contenido |
|---|---|
| **Definición oficial** | Tipo de pieza propio de las referencias que se cuentan en metros o kilogramos; tiene cantidad propia y admite cortes parciales. |
| **Definición prohibida** | No es un lote ni una referencia. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Inventario y existencia |
| **Documento origen** | Decisiones F-1, F-3 · SPEC v1.2 · CD-49 |
| **Relaciones** | Pieza (GL-206); Corte parcial (GL-210); Unidad de medida (GL-195) |

### GL-156 · Ruptura de stock

| Campo | Contenido |
|---|---|
| **Definición oficial** | Condición en que la existencia disponible de un SKU baja de su mínimo (ruptura inminente) o llega a cero. Término consagrado por la monografía; no sustituye a «existencia». |
| **Definición prohibida** | No autoriza usar «stock» como sinónimo de existencia. |
| **Sinónimos prohibidos** | quiebre, faltante (como sinónimo) |
| **Contexto** | Alertas y reglas |
| **Documento origen** | Monografía §3 · SPEC PN-11 |
| **Relaciones** | Umbral de existencia mínima (GL-191); KPI-21; Alerta (GL-012) |


## S

### GL-157 · Salida ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Movimiento que disminuye la existencia por retiro de mercancía hacia el exterior de la bodega, con motivo tipificado y autorización. |
| **Definición prohibida** | No es una venta, un despacho comercial ni una factura `[DC-03]`. |
| **Sinónimos prohibidos** | venta, despacho comercial |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · CD-30 · Monografía §8.2 |
| **Relaciones** | Solicitud de salida (GL-170); Motivo tipificado (GL-111) |

### GL-158 · Segregación de funciones

| Campo | Contenido |
|---|---|
| **Definición oficial** | Principio por el cual quien ejecuta una acción no es quien la autoriza. |
| **Definición prohibida** | No es una recomendación opcional. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Transversal |
| **Documento origen** | SPEC · PR-01 |
| **Relaciones** | Aprobación propia (GL-016); Confirmación de entrada (GL-040); Segundo conteo (GL-159) |

### GL-159 · Segundo conteo ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Repetición de una tarea de conteo ejecutada obligatoriamente por un contador distinto del primero cuando la diferencia supera la tolerancia. |
| **Definición prohibida** | No lo hace quien hizo el primero. |
| **Sinónimos prohibidos** | reconteo por la misma persona |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · CD-42 |
| **Relaciones** | Umbral de tolerancia (GL-192); Segregación de funciones (GL-158) |

### GL-160 · Selección manual

| Campo | Contenido |
|---|---|
| **Definición oficial** | Identificación de mercancía o ubicación eligiéndola de una lista cuando el escaneo es imposible; queda registrada como tal. |
| **Definición prohibida** | No es equivalente a un escaneo para efectos de KPI-07. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Identificación |
| **Documento origen** | SPEC · PN-03 E-05 |
| **Relaciones** | Escaneo (GL-067); KPI-07 |

### GL-161 · Sesión

| Campo | Contenido |
|---|---|
| **Definición oficial** | Período de trabajo autenticado de un usuario en un dispositivo; se cierra manualmente, por inactividad o por cambio de contraseña. |
| **Definición prohibida** | No se comparte entre personas. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Usuarios y acceso |
| **Documento origen** | SPEC · M-01 |
| **Relaciones** | Usuario (GL-196); Atribución (GL-018) |

### GL-162 · Severidad

| Campo | Contenido |
|---|---|
| **Definición oficial** | Importancia de una alerta; incluye al menos el nivel «crítica», que escala por plazo. Los demás niveles no están definidos (HD-15). |
| **Definición prohibida** | No es la prioridad de una tarea. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · RN-056 (SRS RN-ALE-002) |
| **Relaciones** | Alerta (GL-012); Escalamiento (GL-066) |

### GL-163 · Sincronización

| Campo | Contenido |
|---|---|
| **Definición oficial** | Envío al sistema de los registros retenidos al restablecerse la conectividad; cada uno se valida de nuevo contra el estado vigente y se confirma, conservando su fecha operativa, o se rechaza. |
| **Definición prohibida** | No altera el orden ni el contenido del hecho. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · RN-054 (SRS RN-INT-003) |
| **Relaciones** | Retención local (GL-153); Pendiente de sincronización (GL-125) |

### GL-164 · Sistema (actor)

| Campo | Contenido |
|---|---|
| **Definición oficial** | Actor explícito al que se atribuyen las acciones automáticas: cierres de alertas, escalamientos, liberación de reservas vencidas, generación de tareas, cálculo de indicadores. |
| **Definición prohibida** | No es un sexto rol ni tiene permisos (HD-12). |
| **Sinónimos prohibidos** | usuario del sistema, robot |
| **Contexto** | Transversal |
| **Documento origen** | SPEC · RN-001 (SRS RN-INT-001) |
| **Relaciones** | Actor (GL-002); Evento derivado (GL-070) |

### GL-165 · SKU ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Combinación única e irrepetible de Referencia + Talla + Color. Unidad de control de catálogo con la que se planifica, se consulta y se fijan los umbrales mínimo y máximo. No tiene existencia propia: su existencia es la suma de sus unidades de inventario. |
| **Definición prohibida** | No es la unidad que se cuenta y mueve (esa es la unidad de inventario) ni incluye el lote. |
| **Sinónimos prohibidos** | variante (HD-01), ítem |
| **Contexto** | Catálogo textil |
| **Documento origen** | SPEC · CD-05 |
| **Relaciones** | Referencia (GL-142); Lote (GL-107); Unidad de inventario (GL-193); Umbral de existencia mínima (GL-191) |

### GL-166 · Sobrante de recepción

| Campo | Contenido |
|---|---|
| **Definición oficial** | Diferencia en la que lo recibido es mayor que lo esperado; no ingresa sin autorización del Jefe. |
| **Definición prohibida** | No es un ajuste por sobrante. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · RN-007 (SRS RN-ENT-005) |
| **Relaciones** | Documento de entrada (GL-060); Jefe de Bodega (GL-099) |

### GL-167 · Sobre stock

| Campo | Contenido |
|---|---|
| **Definición oficial** | Condición en que la existencia de un SKU supera su máximo configurado. Término consagrado por la monografía. |
| **Definición prohibida** | No autoriza usar «stock» como sinónimo de existencia. |
| **Sinónimos prohibidos** | exceso |
| **Contexto** | Alertas y reglas |
| **Documento origen** | Monografía §3 · SPEC PN-11 |
| **Relaciones** | Umbral de existencia máxima (GL-190); KPI-16 |

### GL-168 · Sobreocupación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Condición en que la ocupación de una ubicación supera su capacidad; genera alerta. |
| **Definición prohibida** | No es un estado de la ubicación ni impide por sí sola registrar el movimiento ya hecho. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · RN-021 (SRS RN-MOV-002) |
| **Relaciones** | Capacidad de ubicación (GL-027); Alerta (GL-012) |

### GL-169 · Solicitud de ajuste

| Campo | Contenido |
|---|---|
| **Definición oficial** | Petición de corregir la existencia registrada, con motivo tipificado y evidencia, que se clasifica, se enruta y se aprueba o rechaza por un tercero. |
| **Definición prohibida** | No cambia la existencia hasta su aprobación. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · PN-07 |
| **Relaciones** | Ajuste (GL-007); Ajuste menor (GL-009); Ajuste mayor (GL-008) |

### GL-170 · Solicitud de salida

| Campo | Contenido |
|---|---|
| **Definición oficial** | Pedido interno de retirar mercancía, con motivo tipificado, que se autoriza, reserva, prepara y ejecuta. |
| **Definición prohibida** | No es un pedido de venta `[DC-03]`. |
| **Sinónimos prohibidos** | pedido, orden de venta |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · M-08, RN-023 (SRS RN-AJU-001) |
| **Relaciones** | Salida (GL-157); Reserva (GL-150); Preparación de salida (GL-130) |

### GL-171 · Subdominio

| Campo | Contenido |
|---|---|
| **Definición oficial** | Área del negocio con problemática propia; se clasifica como núcleo, de soporte o genérico. |
| **Definición prohibida** | No es un módulo ni un componente técnico. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Subdominio núcleo (GL-174); Subdominio de soporte (GL-172); Subdominio genérico (GL-173) |

### GL-172 · Subdominio de soporte

| Campo | Contenido |
|---|---|
| **Definición oficial** | Subdominio específico del negocio que el núcleo necesita pero que no es en sí la ventaja (Supporting Domain). |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Subdominio (GL-171) |

### GL-173 · Subdominio genérico

| Campo | Contenido |
|---|---|
| **Definición oficial** | Subdominio con problemas resueltos de forma general en cualquier sistema (Generic Domain). |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Subdominio (GL-171) |

### GL-174 · Subdominio núcleo

| Campo | Contenido |
|---|---|
| **Definición oficial** | Subdominio donde está la ventaja del producto y donde se concentra el esfuerzo de modelado (Core Domain). |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | core |
| **Contexto** | Modelado |
| **Documento origen** | Nuevo (Fase 4) |
| **Relaciones** | Subdominio (GL-171) |


## T

### GL-175 · Talla ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Dimensión de variación de una referencia que expresa el tamaño; toma valores de un conjunto definido por la empresa. |
| **Definición prohibida** | No es un atributo libre de texto ni una referencia distinta. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Catálogo textil |
| **Documento origen** | SPEC · CD-03 |
| **Relaciones** | SKU (GL-165); Color (GL-038) |

### GL-176 · Tarea de conteo ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Unidad de trabajo asignada a un contador sobre un subconjunto del ámbito del conteo. |
| **Definición prohibida** | No muestra la cantidad esperada. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · CD-41 |
| **Relaciones** | Contador (GL-041); Conteo (GL-042) |

### GL-177 · Tarea operativa

| Campo | Contenido |
|---|---|
| **Definición oficial** | Unidad de trabajo asignada a una persona (recepción, ubicación, preparación, transferencia) que indica qué, dónde y cuánto; se cierra por el hecho asociado, nunca por declaración. |
| **Definición prohibida** | No se cierra marcándola como hecha. |
| **Sinónimos prohibidos** | pendiente (como sustantivo) |
| **Contexto** | Tareas y notificaciones |
| **Documento origen** | SPEC · M-20 |
| **Relaciones** | Panel de tareas (GL-123); Reasignación (GL-136) |

### GL-178 · Tiempo de registro

| Campo | Contenido |
|---|---|
| **Definición oficial** | Duración desde que un operario inicia un movimiento hasta que el sistema lo confirma; es el KPI-05. |
| **Definición prohibida** | No se mide sin el instante de inicio (PROP-KPI-01 del SRS). |
| **Sinónimos prohibidos** | — |
| **Contexto** | Reportes y medición |
| **Documento origen** | SPEC · KPI-05 · Monografía §8.2 |
| **Relaciones** | KPI (GL-103); Movimiento (GL-112) |

### GL-179 · Tiempo máximo en tránsito

| Campo | Contenido |
|---|---|
| **Definición oficial** | Plazo configurable tras el cual una transferencia o un movimiento interno en tránsito genera alerta. |
| **Definición prohibida** | No cancela la transferencia. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · RN-028 (SRS RN-MOV-006), RN-034 (SRS RN-MOV-008) |
| **Relaciones** | Inventario en tránsito (GL-096); Alerta (GL-012) |

### GL-180 · Tipo de alerta

| Campo | Contenido |
|---|---|
| **Definición oficial** | Condición de negocio que representa una alerta; el MVP define diez tipos. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · PN-11 |
| **Relaciones** | Alerta (GL-012) |

### GL-181 · Tipo de novedad

| Campo | Contenido |
|---|---|
| **Definición oficial** | Clase de anomalía reportada: dañada, sin identificador, en ubicación incorrecta o inexistente (lista tipificada). |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Novedades |
| **Documento origen** | SPEC · PN-12 |
| **Relaciones** | Novedad (GL-118) |

### GL-182 · Tipo de zona

| Campo | Contenido |
|---|---|
| **Definición oficial** | Propósito operativo de una zona: recepción, almacenamiento, preparación de salida o cuarentena. |
| **Definición prohibida** | No es un estado de la zona. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · M-05 |
| **Relaciones** | Zona (GL-199) |

### GL-183 · Transferencia ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Movimiento compuesto que traslada existencia entre zonas o bodegas con responsables distintos, mediante despacho y recepción, atravesando el estado en tránsito. |
| **Definición prohibida** | No es un movimiento interno simple. |
| **Sinónimos prohibidos** | traslado entre bodegas |
| **Contexto** | Movimientos |
| **Documento origen** | SPEC · CD-32 |
| **Relaciones** | Despacho (GL-055); Recepción de transferencia (GL-137); Inventario en tránsito (GL-096) |

### GL-184 · Trazabilidad ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Capacidad de responder, para cualquier unidad de inventario y cualquier momento pasado, qué es, cuánto había, dónde estaba, quién la movió, cuándo y por qué. Es retrospectiva y completa, desde la entrada hasta la salida de bodega. |
| **Definición prohibida** | No cubre la cadena de suministro aguas arriba ni la distribución aguas abajo `[DC-03]`. |
| **Sinónimos prohibidos** | rastreo (como alcance mayor) |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · CD-21 · Monografía §2, §6, §7.1 |
| **Relaciones** | Kardex (GL-102); Lote (GL-107); Verificación de integridad (GL-198) |

### GL-185 · Turno

| Campo | Contenido |
|---|---|
| **Definición oficial** | Fracción de la jornada asignada a un equipo; los pendientes se traspasan explícitamente al siguiente. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Operación diaria |
| **Documento origen** | SPEC · PN-14 |
| **Relaciones** | Jornada (GL-100) |


## U

### GL-186 · Ubicación ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Posición física identificable dentro de una zona donde reside mercancía; tiene QR propio, capacidad y estado. Es el nivel mínimo de precisión espacial; toda existencia disponible reside en una. |
| **Definición prohibida** | No es una zona completa ni la dirección de la empresa. |
| **Sinónimos prohibidos** | posición, casilla, celda, slot, hueco |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · CD-14 |
| **Relaciones** | Zona (GL-199); Capacidad de ubicación (GL-027); Identificador QR (GL-088); Unidad de inventario (GL-193) |

### GL-187 · Ubicación física

| Campo | Contenido |
|---|---|
| **Definición oficial** | Dirección completa Bodega › Zona › Ubicación de una existencia. |
| **Definición prohibida** | No es la zona sola ni un texto libre. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Ubicaciones |
| **Documento origen** | Nuevo (Fase 4) · VO-10 |
| **Relaciones** | Bodega (GL-025); Zona (GL-199); Ubicación (GL-186) |

### GL-188 · Umbral ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Valor configurable por el Administrador que define cuándo dispara una regla: mínimo y máximo de existencia, tolerancia, monto de ajuste, tiempo en tránsito, plazos. |
| **Definición prohibida** | No es una meta de desempeño. |
| **Sinónimos prohibidos** | meta, objetivo |
| **Contexto** | Configuración |
| **Documento origen** | SPEC · CD-46 |
| **Relaciones** | Parámetro de configuración (GL-124); Alerta (GL-012) |

### GL-189 · Umbral de autorización del Coordinador

| Campo | Contenido |
|---|---|
| **Definición oficial** | Cantidad bajo la cual el Coordinador puede autorizar salidas; por encima autoriza el Jefe. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Configuración |
| **Documento origen** | SPEC · RN-030 (SRS RN-SAL-001) |
| **Relaciones** | Salida (GL-157); Coordinador de Bodega (GL-048) |

### GL-190 · Umbral de existencia máxima

| Campo | Contenido |
|---|---|
| **Definición oficial** | Existencia por encima de la cual un SKU dispara la alerta de sobre stock. |
| **Definición prohibida** | No es un límite físico que impida recibir mercancía. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · HU-013 (SRS HU-CAT-004) |
| **Relaciones** | SKU (GL-165); Sobre stock (GL-167); Alerta (GL-012) |

### GL-191 · Umbral de existencia mínima

| Campo | Contenido |
|---|---|
| **Definición oficial** | Existencia disponible por debajo de la cual un SKU dispara la alerta de ruptura de stock inminente. |
| **Definición prohibida** | No es una meta de inventario ni una orden de reposición automática. |
| **Sinónimos prohibidos** | punto de reorden |
| **Contexto** | Alertas y reglas |
| **Documento origen** | SPEC · HU-013 (SRS HU-CAT-004) |
| **Relaciones** | SKU (GL-165); Ruptura de stock (GL-156); Alerta (GL-012) |

### GL-192 · Umbral de tolerancia

| Campo | Contenido |
|---|---|
| **Definición oficial** | Diferencia máxima admitida en una línea de conteo antes de exigir segundo conteo. |
| **Definición prohibida** | No es la exactitud objetivo. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Conteos y exactitud |
| **Documento origen** | SPEC · RN-041 (SRS RN-CNT-003) |
| **Relaciones** | Segundo conteo (GL-159) |

### GL-193 · Unidad de inventario ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | La entidad que COLBASOFT controla: la combinación SKU + Lote + Ubicación. Nivel al que se registra existencia, se ejecutan movimientos y se lleva kardex. No tiene QR propio: se identifica con el QR de su SKU + Lote más su ubicación. |
| **Definición prohibida** | No es «el inventario» completo, ni una prenda individual, ni un SKU, ni lo que identifica un QR de mercancía (DF5-01). |
| **Sinónimos prohibidos** | inventario (como entidad, HD-01), ítem, artículo |
| **Contexto** | Inventario y existencia |
| **Documento origen** | SPEC · CD-07 |
| **Relaciones** | SKU (GL-165); Lote (GL-107); Ubicación (GL-186); Existencia (GL-074); Kardex (GL-102) |

### GL-194 · Unidad de manejo agrupada

| Campo | Contenido |
|---|---|
| **Definición oficial** | Término de la v1.0 para el contenedor rotulado que agrupa mercancía sin rotulado individual. Desde la v1.2 se modela como una pieza de tipo contenedor agrupado (HD-22 resuelto, F-6); su gestión avanzada sigue en el Horizonte 3. |
| **Definición prohibida** | No es una entidad aparte del modelo del MVP. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Identificación |
| **Documento origen** | SPEC · PN-02 E-03 · Decisión F-6 (v1.2) |
| **Relaciones** | Identificador QR (GL-088); Pieza (GL-206); Contenedor agrupado (GL-209) |

### GL-195 · Unidad de medida ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Magnitud en que se cuenta una referencia (unidades, metros, rollos, kilogramos). Es fija por referencia y no cambia si existen movimientos; el dominio no convierte entre unidades. |
| **Definición prohibida** | No es la capacidad de una ubicación ni una conversión entre unidades. |
| **Sinónimos prohibidos** | — |
| **Contexto** | Catálogo textil |
| **Documento origen** | SPEC · CD-11 |
| **Relaciones** | Referencia (GL-142); Cantidad (GL-026) |

### GL-196 · Usuario ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Persona identificada que opera el sistema con exactamente uno de los cinco roles oficiales y un ámbito; nunca se elimina. |
| **Definición prohibida** | No es una cuenta genérica o compartida. |
| **Sinónimos prohibidos** | cuenta compartida |
| **Contexto** | Usuarios y acceso |
| **Documento origen** | SPEC · M-02 |
| **Relaciones** | Rol (GL-155); Ámbito (GL-013); Sesión (GL-161) |

### GL-197 · Usuario crítico

| Campo | Contenido |
|---|---|
| **Definición oficial** | El Auxiliar de Bodega: quien más usa el sistema, menos formación tiene y más puede hacer fracasar su adopción. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Proyecto |
| **Documento origen** | SPEC · §1.3.2 · Monografía §4 |
| **Relaciones** | Auxiliar de Bodega (GL-021); Adopción (GL-004) |


## V

### GL-198 · Verificación de integridad

| Campo | Contenido |
|---|---|
| **Definición oficial** | Comprobación, por unidad, lote o global, de que la existencia actual es igual a la suma de los movimientos del kardex. |
| **Definición prohibida** | No corrige nada: solo detecta. |
| **Sinónimos prohibidos** | cuadre |
| **Contexto** | Trazabilidad |
| **Documento origen** | SPEC · RN-065 (SRS RN-INT-004), RN-080 (SRS RN-AUD-005) |
| **Relaciones** | Kardex (GL-102); Discrepancia de integridad (GL-059); KPI-09 |


## Z

### GL-199 · Zona ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Subdivisión de una bodega con propósito operativo: recepción, almacenamiento, preparación de salida o cuarentena. Agrupa ubicaciones y puede tener un Coordinador responsable. |
| **Definición prohibida** | No es una ubicación ni un área administrativa de la empresa. |
| **Sinónimos prohibidos** | área (HD-01), sector, pasillo |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · CD-13 |
| **Relaciones** | Bodega (GL-025); Ubicación (GL-186); Tipo de zona (GL-182); Coordinador de Bodega (GL-048) |

### GL-200 · Zona de almacenamiento

| Campo | Contenido |
|---|---|
| **Definición oficial** | Zona destinada a mantener la existencia disponible en sus ubicaciones. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · M-05 |
| **Relaciones** | Zona (GL-199) |

### GL-201 · Zona de cuarentena ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Zona donde reside mercancía inmovilizada: dañada, en verificación o pendiente de decisión. Su existencia no es disponible. |
| **Definición prohibida** | No es una zona de baja ni implica que la mercancía salió del inventario. |
| **Sinónimos prohibidos** | zona de rechazos |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · CD-17 |
| **Relaciones** | Inmovilización (GL-090); Novedad (GL-118) |

### GL-202 · Zona de preparación

| Campo | Contenido |
|---|---|
| **Definición oficial** | Zona destinada a preparar salidas. |
| **Definición prohibida** | — |
| **Sinónimos prohibidos** | — |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · M-05 |
| **Relaciones** | Zona (GL-199); Salida (GL-157) |

### GL-203 · Zona de recepción ★

| Campo | Contenido |
|---|---|
| **Definición oficial** | Zona donde permanece la mercancía entre su llegada y su ubicación definitiva; su existencia está en el inventario pero no está disponible. Toda bodega tiene al menos una, y toda zona de recepción tiene al menos una ubicación. |
| **Definición prohibida** | No es un lugar fuera del inventario ni existencia disponible. |
| **Sinónimos prohibidos** | muelle, andén (como sinónimos) |
| **Contexto** | Ubicaciones |
| **Documento origen** | SPEC · CD-16 |
| **Relaciones** | Inventario en recepción (GL-095); Entrada (GL-065) |

> ★ = término central del lenguaje ubicuo (DOMAIN_MODEL Cap. 1).


---

**ESTADO DEL CAPÍTULO — 2**

| | |
|---|---|
| **Completado** | 210 términos con los cinco campos exigidos más sinónimos prohibidos |
| **Riesgos** | — |
| **Dependencias** | DOMAIN_MODEL · EVENT_CATALOG |
| **Hallazgos** | HD-01, HD-14, HD-22 (resuelto, v1.2), HD-28 |


---

# CAPÍTULO 3 — ÍNDICE INVERSO DE SINÓNIMOS PROHIBIDOS

| No usar | Usar | ID |
|---|---|---|
| ajuste del auditor | **Observación de auditoría** | GL-120 |
| algoritmo inteligente | **Regla de negocio** | GL-146 |
| almacén (como sinónimo) | **Bodega** | GL-025 |
| andén (como sinónimos) | **Zona de recepción** | GL-203 |
| apartado | **Inventario reservado** | GL-098 |
| apartado | **Reserva** | GL-150 |
| apunte | **Movimiento** | GL-112 |
| área (HD-01) | **Zona** | GL-199 |
| artículo | **Referencia** | GL-142 |
| artículo | **Unidad de inventario** | GL-193 |
| asignación de ubicación (como hecho sin movimiento) | **Primera ubicación** | GL-204 |
| asignación obligatoria | **Propuesta de ubicación** | GL-132 |
| autoaprobación permitida | **Aprobación propia** | GL-016 |
| aviso inteligente | **Alerta** | GL-012 |
| baja (de un maestro) | **Desactivación** | GL-052 |
| bloqueado (como sustantivo) | **Inventario inmovilizado** | GL-097 |
| bloqueo | **Inmovilización** | GL-090 |
| borrado | **Anulación** | GL-015 |
| borrado | **Eliminación lógica** | GL-062 |
| campaña (no modelada como entidad | **Alcance de auditoría** | GL-011 |
| cargo | **Rol** | GL-155 |
| casilla | **Ubicación** | GL-186 |
| celda | **Ubicación** | GL-186 |
| cliente | **Empresa de estudio** | GL-063 |
| código de barras | **Identificador QR** | GL-088 |
| congelado | **Inventario inmovilizado** | GL-097 |
| core | **Subdominio núcleo** | GL-174 |
| corrección | **Ajuste** | GL-007 |
| cuadre | **Ajuste** | GL-007 |
| cuadre | **Verificación de integridad** | GL-198 |
| cuenta compartida | **Usuario** | GL-196 |
| cupo | **Capacidad de ubicación** | GL-027 |
| dashboard analítico | **Reporte** | GL-149 |
| depósito | **Bodega** | GL-025 |
| desbloqueo | **Liberación** | GL-105 |
| descuadre | **Diferencia de inventario** | GL-057 |
| despacho comercial | **Salida** | GL-157 |
| devolución (como reversión) | **Retorno** | GL-154 |
| digitación | **Escaneo** | GL-067 |
| disponible (como sustantivo genérico) | **Existencia** | GL-074 |
| eliminación | **Anulación** | GL-015 |
| eliminación | **Desactivación** | GL-052 |
| empresa X | **Empresa de estudio** | GL-063 |
| en camino | **Inventario en tránsito** | GL-096 |
| error de ubicación | **Desviación de ubicación** | GL-056 |
| estatus de stock | **Estado de inventario** | GL-068 |
| estilo | **Referencia** | GL-142 |
| etiqueta (como sinónimo del código) | **Identificador QR** | GL-088 |
| exceso | **Sobre stock** | GL-167 |
| faltante (como sinónimo) | **Ruptura de stock** | GL-156 |
| familia | **Categoría** | GL-030 |
| HD) | **Alcance de auditoría** | GL-011 |
| HD-01) | **Referencia** | GL-142 |
| HD-01) | **Unidad de inventario** | GL-193 |
| historial (de inventario) | **Kardex** | GL-102 |
| historial de sistema | **Bitácora de auditoría** | GL-023 |
| hueco | **Ubicación** | GL-186 |
| IA | **Inteligente** | GL-091 |
| incidente (como sinónimos) | **Novedad** | GL-118 |
| ingreso | **Documento de entrada** | GL-060 |
| ingreso | **Entrada** | GL-065 |
| inteligencia artificial | **Inteligente** | GL-091 |
| inventario (como entidad | **Unidad de inventario** | GL-193 |
| inventario anual | **Conteo general** | GL-045 |
| inventario físico (como verbo) | **Conteo** | GL-042 |
| inventario rotativo | **Conteo cíclico** | GL-044 |
| ítem | **SKU** | GL-165 |
| ítem | **Unidad de inventario** | GL-193 |
| libro | **Kardex** | GL-102 |
| línea | **Categoría** | GL-030 |
| log | **Bitácora de auditoría** | GL-023 |
| log | **Kardex** | GL-102 |
| lote inconsistente (HD-14) | **Discrepancia de integridad** | GL-059 |
| maestro de productos | **Catálogo** | GL-029 |
| merma (como sinónimo del movimiento) | **Baja por daño** | GL-022 |
| meta | **Umbral** | GL-188 |
| métrica de desempeño personal | **KPI** | GL-103 |
| modelo | **Referencia** | GL-142 |
| muelle | **Zona de recepción** | GL-203 |
| nivelación | **Ajuste** | GL-007 |
| objetivo | **Umbral** | GL-188 |
| observación (como sustituto) | **Motivo tipificado** | GL-111 |
| operario (como nombre de rol) | **Auxiliar de Bodega** | GL-021 |
| orden de venta | **Solicitud de salida** | GL-170 |
| partida | **Lote** | GL-107 |
| pasillo | **Zona** | GL-199 |
| pedido | **Solicitud de salida** | GL-170 |
| pendiente (como sustantivo) | **Tarea operativa** | GL-177 |
| perfil (como sinónimo) | **Rol** | GL-155 |
| picking | **Preparación de salida** | GL-130 |
| posición | **Ubicación** | GL-186 |
| precisión (como sinónimo del KPI) | **Exactitud del inventario** | GL-072 |
| predicción | **Alerta** | GL-012 |
| producto (designa a COLBASOFT | **Referencia** | GL-142 |
| proveedor (como entidad) | **Origen de entrada** | GL-122 |
| punto de reorden | **Umbral de existencia mínima** | GL-191 |
| push | **Notificación** | GL-117 |
| quiebre | **Ruptura de stock** | GL-156 |
| rastreo (como alcance mayor) | **Trazabilidad** | GL-184 |
| razón libre | **Motivo tipificado** | GL-111 |
| recepción (como sustantivo) | **Documento de entrada** | GL-060 |
| reclamo | **Novedad** | GL-118 |
| reconteo por la misma persona | **Segundo conteo** | GL-159 |
| reetiquetado | **Reimpresión** | GL-148 |
| registro | **Movimiento** | GL-112 |
| remisión | **Documento de entrada** | GL-060 |
| remisión (como sinónimos) | **Entrada** | GL-065 |
| reubicación (como sinónimos del movimiento) | **Movimiento interno** | GL-114 |
| reversión | **Anulación** | GL-015 |
| robot | **Sistema (actor)** | GL-164 |
| saldo | **Existencia** | GL-074 |
| saldo congelado | **Existencia teórica congelada** | GL-078 |
| sector | **Zona** | GL-199 |
| slot | **Ubicación** | GL-186 |
| soporte comercial | **Documento de respaldo** | GL-061 |
| stock | **Existencia** | GL-074 |
| stock libre | **Inventario disponible** | GL-094 |
| superusuario | **Administrador** | GL-003 |
| supervisor (como sinónimo del rol) | **Coordinador de Bodega** | GL-048 |
| tablero de BI | **Dashboard operativo** | GL-050 |
| tanda | **Lote** | GL-107 |
| tasa de error del operario | **Frecuencia de errores de registro** | GL-083 |
| toma física | **Conteo** | GL-042 |
| transacción | **Movimiento** | GL-112 |
| traslado | **Movimiento interno** | GL-114 |
| traslado entre bodegas | **Transferencia** | GL-183 |
| usuario del sistema | **Sistema (actor)** | GL-164 |
| variante (HD-01) | **SKU** | GL-165 |
| venta | **Salida** | GL-157 |
| zona de rechazos | **Zona de cuarentena** | GL-201 |

---

**ESTADO DEL CAPÍTULO — 3**

| | |
|---|---|
| **Completado** | 130 sinónimos prohibidos con su término oficial |
| **Riesgos** | — |
| **Dependencias** | Cap. 2 |
| **Hallazgos** | — |


---

# AUDITORÍA INTERNA DE LA FASE 4

> Verificación de los tres documentos (DOMAIN_MODEL, EVENT_CATALOG, GLOSSARY). Los totales se calcularon sobre la misma fuente de datos de la que se generaron los documentos.

## A. Totales

| Elemento | Total | Mínimo exigido | Cumple |
|---|:--:|:--:|:--:|
| Subdominios | 15 (Core 5 · Supporting 7 · Generic 3) | 9 | ✅ |
| **Entidades** | **27** | 13 | ✅ |
| **Objetos de valor** | **43** | — (7 ejemplos) | ✅ |
| **Agregados** | **22** | — | ✅ |
| **Invariantes** | **79** (+ 14 políticas reactivas) | 40 | ✅ |
| **Estados oficiales** | **76** en 21 máquinas (118 transiciones) | — | ✅ |
| **Eventos** | **168** (61 derivados) | 70 | ✅ |
| **Términos del glosario** | **210** (55 centrales; 130 sinónimos prohibidos indexados) | 120 | ✅ |
| Hallazgos del dominio | 30 | — | — |
| Líneas temporales | 14 procesos | 14 | ✅ |
| Matrices | A, B, C (DOMAIN_MODEL Cap. 9) · D, E (EVENT_CATALOG Cap. 6) | 5 | ✅ |

## B. Verificaciones de consistencia

| # | Verificación | Resultado |
|---|---|:--:|
| V-1 | Toda regla, historia, requisito y KPI citado existe en el SRS/SPEC | ✅ 0 referencias rotas |
| V-2 | Toda entidad citada por un evento, relación o agregado existe | ✅ |
| V-3 | Todo evento citado en estados y líneas temporales existe | ✅ |
| V-4 | Toda invariante citada por un agregado existe | ✅ |
| V-5 | Las 92 reglas del SRS (82 + 3 de la v1.1 + 6 de la v1.2 + 1 de la v1.4) quedan cubiertas como invariante o política | ✅ 78 + 14 = 92/92 |
| V-6 | Los 24 KPI aparecen en al menos un evento | ✅ 24/24 |
| V-7 | Historias con evento | 🟡 105/114 (el resto son de consulta) |
| V-8 | RF con evento | 🟡 157/185 (el resto son de consulta, restricción o presentación) |
| V-9 | Toda invariante cita al menos una regla del SRS | ✅ 79/79 |
| V-10 | Las definiciones del lenguaje ubicuo y del glosario son idénticas | ✅ (misma fuente) |
| V-11 | Ninguna relación del glosario apunta a un término inexistente | ✅ |
| V-12 | Ningún término nombra a la empresa de estudio (DC-01) ni introduce IA (DC-07) | ✅ |
| V-13 | Sin arquitectura, modelo de datos, tecnologías ni código | ✅ |
| V-14 | Ningún documento previo fue modificado | ✅ |

## C. Riesgos abiertos para la Arquitectura (Fase 5)

| ID | Riesgo | Origen | Sev. | Consecuencia si no se atiende |
|---|---|---|:--:|---|
| **RF5-01** | Identidad de la mercancía identificada por QR — **resuelto por DF5-01** (el QR identifica SKU + Lote) | HD-04 | ✅ | Ya no condiciona la Fase 5; queda el tratamiento de copias impresas (RF5-14) |
| **RF5-02** | Operaciones que deben ser indivisibles sobre dos unidades (movimiento interno, primera ubicación, transferencia, confirmación de entrada) | Cap. 5.3 · RN-MOV-004 · RN-MOV-010 | 🔴 | Si se confirma solo una mitad, la existencia total cambia |
| **RF5-03** | Concurrencia sobre la disponibilidad de una misma unidad | IN-08, IN-10, IN-11 | 🔴 | Dos operaciones simultáneas podrían comprometer la misma existencia |
| **RF5-04** | Existencia derivada del kardex frente a tiempos de consulta | IN-03 · RNF-REN-001 · RNF-ESC-004 | 🟠 | Derivar en cada consulta puede degradar el rendimiento al crecer el kardex |
| **RF5-05** | Registros sin conectividad que al sincronizarse ya no cumplen una regla — la regla ya está definida (DF5-05, RN-INT-008, IN-72); falta garantizarla técnicamente | HD-16 · HD-24 · RN-INT-003 · RN-INT-008 | 🟠 | Sin la revalidación, la sincronización podría dejar existencia negativa o duplicados |
| **RF5-06** | Capacidad y ocupación con unidades de medida heterogéneas | HD-17 | 🟠 | KPI-18 y la alerta de sobreocupación no son calculables |
| **RF5-07** | Inmutabilidad y continuidad demostrables de kardex y bitácora | IN-02, IN-63 · RNF-AUD-002 | 🟠 | El jurado y el Auditor deben poder comprobarlas |
| **RF5-08** | Aprobación formal pendiente: el acta de DEC-08 no está firmada; las nueve decisiones DEC ya tienen respuesta (v1.3) | DEC-08 · HD-21 | 🟡 | El documento puede cambiar si la aprobación formal introduce correcciones |
| **RF5-09** | Escalas no definidas de severidad y prioridad | HD-15 | 🟡 | Ordenamiento de alertas y tareas indefinido |
| **RF5-10** | Ubicación de la existencia en tránsito (HD-05); la zona de recepción y el estado inicial quedaron resueltos por DF5-02 | HD-05 | 🟡 | Cómo se representa la porción en tránsito respecto de su unidad origen |
| **RF5-11** | Carga del Administrador por ajustes derivados de conteo | HD-08 · RG-18 | 🟡 | Cuello de botella de aprobaciones |
| **RF5-12** | Eventos sin requisito que los implemente | EVENT_CATALOG Cap. 6 | 🟠 | Comportamientos del dominio sin criterio de aceptación |
| **RF5-13** | Crecimiento ilimitado de kardex, bitácora e historiales (sin purga) | RNF-AUD-004 · RNF-ESC-004 | 🟡 | Volumen a tres años sin estimación |
| **RF5-14** | Qué identifica físicamente cada etiqueta de mercancía (HD-25): resuelto en la v1.2 (la pieza tiene identidad interna; el QR sigue siendo SKU + Lote; la reimpresión conserva el QR). Queda cómo se distingue físicamente una pieza de otra del mismo lote (HD-28) | HD-25 · HD-28 · RN-IDE-004 · RN-MOV-011 | 🟡 | Sin distinguir físicamente las piezas del mismo lote la selección en pantalla depende por completo del operario |
| **RF5-15** | Coherencia entre la suma de las cantidades de las piezas y la existencia de la unidad de inventario (AG-22 ↔ AG-05): una operación sobre una pieza afecta a dos agregados | IN-74 · RN-LOT-007 · RN-MOV-011 | 🟠 | Existencia de la unidad de inventario distinta de la suma de sus piezas |
| **RF5-16** | Reserva y selección de piezas: la autorización reserva cantidad sobre la unidad de inventario (RN-EXI-003), pero las piezas se seleccionan recién al tomarlas (RN-SAL-009); dos preparaciones pueden apuntar a la misma pieza | RN-SAL-009 · RN-EXI-003 · RN-EXI-004 | 🟠 | Doble compromiso de una misma pieza en preparaciones distintas |

**Estado frente a la Fase 5 (v1.4).** El cierre del CP-04 resolvió HD-04, HD-06, HD-07, HD-23 y HD-24 (DF5-01, DF5-02, DF5-03, DF5-05); las decisiones del 30-sep-2026 resolvieron **HD-25** y **HD-22** (Q-11, F-1…F-6, Q-09, Q-10). **HD-29 y HD-30** se resolvieron en la v1.4; **HD-28** queda pendiente, junto con HD-17, HD-26 y HD-27, que requieren información de la operación real sin bloquear la arquitectura. Las nueve decisiones DEC tienen respuesta (DEC-01 en la v1.2; DEC-02…DEC-09 en la v1.3); queda pendiente el acta firmada de DEC-08 (ver `05_V13_DECISIONES/`). Siguen vigentes R-S01 (modelo TO-BE sin contraste con la operación real) y los riesgos críticos de adopción del SPEC.

---

**ESTADO DE LA FASE 4**

| | |
|---|---|
| **Completado** | DOMAIN_MODEL (11 capítulos), EVENT_CATALOG (6 capítulos), GLOSSARY (3 capítulos + auditoría interna) |
| **Riesgos** | 16 riesgos para la Fase 5 (2 críticos abiertos; RF5-01 resuelto) · R-S01 heredado |
| **Dependencias** | Acta de DEC-08 y hallazgos pendientes (DOMAIN_MODEL Cap. 10) |
| **Hallazgos** | 30 hallazgos del dominio (DOMAIN_MODEL Cap. 10) |


---

*Fin de GLOSSARY v1.4. La monografía original permanece sin modificaciones.*
