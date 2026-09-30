# 04_CP04_DECISIONES_PENDIENTES
## HD-25 y DEC-01…DEC-09: análisis antes de la Fase 5

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | 04_CP04_DECISIONES_PENDIENTES |
| **Versión** | 1.0 |
| **Fecha** | 29 de septiembre de 2026 |
| **Solicitado por** | Prompt «Cierre de CP-04 y preparación para Fase 5» |
| **Antecedentes** | `04_CP04_AUDITORIA.md` (auditoría) · `04_CP04_CIERRE.md` (decisiones DF5) |
| **Estado** | Emitido: **no decide**; enumera lo que el Director y el equipo deben responder |
| **Naturaleza** | Análisis documental. Sin arquitectura, tecnologías, modelo de datos ni código |

> **Regla de este documento.** Ninguna alternativa se declara «mejor» cuando la elección depende de información de la operación real que el proyecto no tiene. Cada clasificación se apoya en evidencia citada: SPEC v1.1, SRS v1.1 (Anexo C, C.1) y DOMAIN_MODEL v1.1.

---

# 1. ESTADO DEL CP-04

## 1.1 Verificación del estado real (antes de modificar)

| Comprobación | Resultado |
|---|---|
| Documentos v1.0 (monografía, Auditoría Fundacional, SPEC v1.0, SRS v1.0) frente al commit `79f823c` | Sin cambios |
| DOMAIN_MODEL v1.0 | Conservado en el historial de git (`79f823c`); el archivo vigente es la v1.1 |
| `xref.py` sobre SRS v1.1, dominio v1.1, CLAUDE.md y documentos del CP-04 | Sin errores |
| Definición de DEC-01…DEC-09 | SRS v1.1, Anexo C, tabla C.1: **idéntica** a la del SRS v1.0. **Ninguna tiene respuesta registrada** en ningún archivo |
| HD-25 | DOMAIN_MODEL v1.1 Cap. 10; `04_CP04_CIERRE.md` §3 y §13; riesgo RF5-14 |
| Commit / push | No hechos |
| Arquitectura | No iniciada |

## 1.2 Validación técnica frente a aprobación

| Dimensión | Estado | Evidencia |
|---|---|---|
| **Validación técnica del CP-04** | ✅ **Validado** | Contradicciones HD-04, HD-06, HD-07, HD-23 y HD-24 resueltas (DF5-01…DF5-05); 85/85 reglas cubiertas; 0 referencias rotas; IDs estables; generación reproducible (`04_CP04_CIERRE.md` §15) |
| **Aprobación funcional y académica** | ⏳ **Pendiente** | DEC-01…DEC-09 sin respuesta; HD-25 sin decidir |

**Revisión de DF5-06.** El cierre había registrado en las cinco portadas v1.1 «Aprobado para la Fase 5 (DF5-06), con limitaciones conocidas». Esa aprobación ya estaba condicionada: el propio cierre (§2) decía que el estado volvía atrás si el Director no aceptaba tratar DEC-01…DEC-09 como limitaciones. Esa aceptación no existe: esta ejecución pide revisarlas una por una. Por eso las portadas se cambiaron a:

> «**Validado técnicamente** (cierre del CP-04, 29-sep-2026). **Aprobación funcional y académica pendiente**: HD-25 y DEC-01…DEC-09 sin responder.»

No se usa la fórmula «validado para continuar con el análisis arquitectónico», porque HD-25 no lo permite todavía (§2.7).

---

# 2. HD-25 — QUÉ IDENTIFICA FÍSICAMENTE CADA ETIQUETA

## 2.1 Origen

Surge de **DF5-01** (29-sep-2026): el QR de mercancía identifica **SKU + Lote** y no la ubicación. El DOMAIN_MODEL lo recoge así: «un mismo SKU + Lote puede encontrarse simultáneamente en diferentes ubicaciones sin generar un nuevo QR». Se registró primero en `04_CP04_CIERRE.md` §3 como un problema de reimpresión. **Este análisis muestra que es más amplio.**

## 2.2 El problema

Hay cuatro hechos del baseline que no encajan entre sí:

| # | Hecho | Fuente |
|---|---|---|
| 1 | Un QR por SKU + Lote; el mismo QR en todas las ubicaciones del lote | DF5-01 · RF-QRC-001 · RN-IDE-001 |
| 2 | La etiqueta se adhiere «a la mercancía **o a su contenedor**»; si no hay rotulado individual, se rotula el contenedor como «unidad de manejo agrupada» | SPEC PN-02 paso 4 y E-03 |
| 3 | La reimpresión emite **un identificador nuevo** que hereda la trazabilidad; el anterior queda **Reemplazado**, y solo un identificador Activo resuelve escaneos | RN-018 → RN-IDE-004 · RF-045 → RF-QRC-006 · RF-046 → RF-QRC-007 · SM-05 |
| 4 | En la preparación de una salida, el Auxiliar «**escanea cada unidad al tomarla**» y el sistema rechaza lo que no corresponde en referencia, talla, color o lote | SPEC PN-10 paso 7 · HU-SAL-003 · RN-050 → RN-SAL-004 |

**Consecuencias:**
- **(1) + (2):** hay varias etiquetas físicas con el mismo código.
- **(1) + (3):** reimprimir una etiqueta deteriorada invalida todas las demás del lote.
- **(1) + (4):** con copias del mismo código, escanear dos veces la misma etiqueta no se distingue de escanear dos piezas distintas. El SPEC no dice si un escaneo **cuenta cantidad** o solo **verifica qué** se toma.
- **(1):** el QR no dice **cuánto**. Las cantidades se digitan: recepción (PN-01 paso 5), movimiento interno (PN-05 paso 3), conteo (PN-08 paso 6).

**La monografía no aporta evidencia.** No menciona QR, etiquetas ni rotulado; solo la trazabilidad como objetivo (Resumen, palabras clave, §5.5 OE-3, §6, §7.1).

## 2.3 Tres cosas distintas que hoy se confunden

| Concepto | Qué es | En el modelo v1.1 | Tiene cantidad | Tiene ubicación |
|---|---|---|:--:|:--:|
| **QR de lote** (SKU + Lote) | El **qué**: referencia, talla, color y lote | E-09 (tipo mercancía) → E-04 Lote | No | No |
| **Etiqueta física** | El **objeto impreso** pegado a una pieza, rollo, bulto o contenedor | **No existe como concepto**: es implícita (la «copia» del QR) | Depende de la alternativa | Donde esté pegada, pero el sistema no lo sabe |
| **Unidad de inventario** | La **existencia** de un SKU + Lote **en una ubicación** | E-08, identidad SKU + Lote + Ubicación (RN-INT-005) | Sí (derivada del kardex) | Sí (es parte de su identidad) |
| *Unidad física o paquete* | Un rollo, caja o bulto con identidad propia | **Fuera del MVP**: «unidades de manejo y contenedores» están en el Horizonte 3 (SPEC §12.4, elemento 6; HD-22) | Sí | Sí |

**HD-25 pregunta, en el fondo, qué representa una etiqueta física**: una copia del «qué», un objeto con identidad propia pero sin cantidad, o un paquete con identidad y cantidad.

## 2.4 Alternativas

### Alternativa A — Todas las etiquetas del mismo SKU + Lote comparten el mismo QR

| Aspecto | Análisis |
|---|---|
| Qué identifica el QR | El SKU + Lote (DF5-01 literal) |
| **Ventajas** | Es la lectura directa de DF5-01 y de PN-02 paso 2. No agrega conceptos. Reubicar no exige reetiquetar. Una sola impresión sirve para N etiquetas. El núcleo (existencia, kardex, concurrencia) no cambia |
| **Limitaciones** | El sistema no puede distinguir etiquetas: no sabe cuántas hay, dónde están ni si una ya se escaneó |
| Trazabilidad | A nivel de lote y ubicación: suficiente para las seis preguntas de CD-21 sobre la unidad de inventario (qué, cuánto, dónde, quién, cuándo, por qué). **No** permite rastrear un rollo o pieza individual |
| Reimpresión | **Incompatible con RN-IDE-004 tal como está**: emitir un código nuevo deja Reemplazado el del lote y deja sin efecto las demás copias. Para mantener A hay que cambiar RN-IDE-004, RF-QRC-006, RF-QRC-007 y SM-05 para que la reimpresión por deterioro sea **otra copia del mismo código**; el reemplazo quedaría para otros motivos (por ejemplo, un código comprometido) |
| Movimientos | El escaneo da el qué; la ubicación viene del QR de ubicación o de una selección registrada (RN-IDE-001); la cantidad **se digita** (PN-05 paso 3) |
| Múltiples ubicaciones | Resueltas por RN-IDE-001: sin ubicación de origen no hay operación |
| Múltiples cantidades físicas | Un rollo de 40 m y otro de 12 m del mismo lote llevan la misma etiqueta: el escaneo no dice cuál se toma ni cuánto trae |
| **Riesgo de existencia incorrecta** | (a) Si el operario **selecciona** una ubicación de origen equivocada (PN-03 E-05), el movimiento se atribuye a la unidad incorrecta sin que el escaneo lo detecte. (b) En la preparación (PN-10 paso 7), si «escanear cada unidad» se usa para **contar**, un doble escaneo de la misma etiqueta suma una unidad inexistente. Esto afecta KPI-07 y KPI-11 |
| Anulación | Anular el QR del lote invalida todas sus etiquetas a la vez |
| Compatibilidad con SPEC y SRS v1.1 | ✅ DF5-01, PN-02, PN-05. ❌ RN-IDE-004, RF-QRC-006, RF-QRC-007 (reimpresión). ⚠️ PN-10 paso 7 / RN-SAL-004: exige definir que el escaneo verifica y no cuenta |

### Alternativa B — El QR resuelve a SKU + Lote, pero cada etiqueta tiene además un identificador físico único

| Aspecto | Análisis |
|---|---|
| Qué identifica cada componente | El código de la etiqueta identifica **esa etiqueta física**. La etiqueta pertenece a **un solo** SKU + Lote. El inventario sigue operando sobre SKU + Lote + Ubicación |
| Qué contiene el QR | El identificador único de la etiqueta (con el texto legible de respaldo que ya exige HU-QRC-001: referencia, talla, color y lote). **No** contiene ubicación, bodega ni cantidad, como exige DF5-01 |
| Relación con SKU + Lote | N etiquetas → 1 SKU + Lote. Al escanear se resuelve al SKU + Lote, como en A |
| Relación con la unidad de inventario | **Ninguna directa**: la unidad sigue siendo SKU + Lote + Ubicación y se determina con la etiqueta más la ubicación (RN-IDE-001), como en A. La etiqueta no sabe dónde está ni cuánto representa |
| Reimpresión | **Compatible con RN-IDE-004 tal como está**: la etiqueta nueva reemplaza solo a la deteriorada y las demás siguen activas |
| Trazabilidad | La de A, más la trazabilidad **de las etiquetas**: cuáles existen, cuál se escaneó y cuándo. **No** da trazabilidad por pieza: una etiqueta no tiene cantidad (eso sería C) |
| Movimientos | Como en A: cantidad digitada. Permite detectar el **doble escaneo** de la misma etiqueta en una preparación, pero solo convierte escaneos en cantidad si se decide que una etiqueta = una pieza, lo que se acerca a C |
| Separación por ubicación | No la aporta: la ubicación sigue viniendo del QR de ubicación |
| Qué cambia en el baseline | La **redacción** de DF5-01 («un QR por SKU + Lote» pasaría a «un QR por etiqueta, que resuelve a un SKU + Lote»), RF-QRC-001, RN-IDE-001, CD-08 y E-09. Probablemente, un concepto nuevo, «Etiqueta», como entidad o como objeto de valor de AG-07, con sus eventos (emitida, reemplazada) y su término de glosario. **El núcleo no cambia** |
| Compatibilidad con SPEC y SRS v1.1 | ✅ PN-02, PN-05, RN-IDE-002 y RN-IDE-004 sin cambios. ⚠️ DF5-01 y RF-QRC-001 requieren nueva redacción. ⚠️ PN-10 paso 7 sigue exigiendo definir si el escaneo cuenta |

### Alternativa C — El QR identifica una unidad física o paquete único relacionado con SKU + Lote

| Aspecto | Análisis |
|---|---|
| Qué identifica el QR | Un rollo, pieza o bulto **con identidad, cantidad y ubicación propias** |
| Impacto sobre el dominio | **Estructural.** Aparece una entidad nueva (unidad física o de manejo) con su propio agregado, invariantes y máquina de estados. La unidad de inventario pasaría a ser la suma de sus paquetes en una ubicación, o dejaría de ser el nivel operativo. Cambian la granularidad del kardex y la de la concurrencia |
| Trazabilidad | La más fina: cada rollo con su historia |
| Inventario | Existencia por paquete; el escaneo **implica cantidad** (salvo en retiros parciales) |
| Movimientos | Mover un paquete entero = escanearlo; mover parte (cortar metros de un rollo) exige dividirlo y decidir si nace otro paquete con otra etiqueta |
| Reimpresión | Simple: una etiqueta por paquete |
| Redistribución | Compleja: divisiones, fusiones y rollos parcialmente consumidos |
| Complejidad | Alta; agrava R-S03 (alcance grande para nivel Tecnólogo) |
| Compatibilidad con SPEC y SRS v1.1 | ❌ **Revoca DF5-01** (el QR dejaría de identificar SKU + Lote). ❌ Adelanta al MVP las «unidades de manejo», que el backlog sitúa en el Horizonte 3 (§12.4, elemento 6, «necesidad operativa demostrada»; HD-22). ❌ Contradice PN-05 paso 3 y PN-01 paso 5 (cantidades digitadas). Requiere nuevos requisitos: **no es una corrección, es un cambio de alcance** |

### Variante que aparece en los documentos — la etiqueta de contenedor (PN-02 E-03)

La «unidad de manejo agrupada» del MVP **no es una cuarta alternativa independiente**: es un caso de uso del rotulado. Con **A**, el contenedor lleva otra copia del QR del lote. Con **B**, lleva su propia etiqueta. Con **C**, es un paquete. Obliga a responder si un contenedor puede mezclar lotes, porque en ese caso ni A ni B lo describen: una etiqueta pertenece a un solo SKU + Lote.

## 2.5 Impactos comparados

| Dimensión | A | B | C |
|---|---|---|---|
| Identidad de la unidad de inventario (AG-05) | Sin cambio | Sin cambio | **Cambia** |
| Identidad del QR (AG-07) | Sin cambio | Cambia la redacción (QR por etiqueta) | **Cambia** |
| DF5-01 | Se mantiene literal | Se reformula | **Se revoca** |
| RN-IDE-004 (reimpresión) | **Debe cambiar** | Se mantiene | Se mantiene |
| Escaneo ↔ cantidad | Solo verifica | Verifica y detecta repetidos | Implica cantidad |
| Kardex y concurrencia | Sin cambio | Sin cambio | **Cambian de granularidad** |
| Horizonte | MVP | MVP | Hoy en el Horizonte 3 |
| Documentos afectados | RN-IDE-004, RF-QRC-006, RF-QRC-007, HU-QRC-004, SM-05, término «Reimpresión»; aclaración de RN-SAL-004 / PN-10 | DF5-01, CD-08, RF-QRC-001, RN-IDE-001, E-09, AG-07, EV-QRC-*, glosario (término nuevo); aclaración de RN-SAL-004 | SPEC (PN-01, PN-02, PN-03, PN-05, PN-10, CD-07, CD-08, §12), SRS (RF-QRC-*, RF-MOV-*, RF-SAL-*, reglas nuevas), dominio (entidad y agregado nuevos, IN, SM, eventos) |

## 2.6 Información necesaria para decidir

**No se inventa ninguna respuesta.** Cada pregunta indica qué alternativa ayuda a distinguir.

| # | Pregunta a la operación real | Distingue |
|---|---|---|
| Q-01 | ¿Qué representa hoy una etiqueta física: una pieza, un rollo, un bulto o caja, o todo un lote? | A/B frente a C |
| Q-02 | ¿Un mismo lote se divide físicamente en varias piezas o rollos que se guardan en ubicaciones distintas? | Confirma la premisa de DF5-01 |
| Q-03 | ¿Cada rollo o pieza tiene una cantidad propia (metros o kilos) que haya que conocer sin medirla de nuevo? | C |
| Q-04 | ¿Se retiran cantidades parciales de un rollo (cortes)? ¿Con qué frecuencia? | Complejidad de C |
| Q-05 | ¿La mercancía llega ya etiquetada por el proveedor? ¿Con código de barras? ¿Qué identifica ese código: producto, lote o pieza? | Relación con HD-26 y RN-IDE-003 |
| Q-06 | ¿COLBASOFT debe generar e imprimir las etiquetas, o se reutilizan las del proveedor? | Todas |
| Q-07 | ¿Una etiqueta puede representar varias unidades? (por ejemplo, una bolsa de 20 camisetas) | A/B frente a C; unidad de manejo agrupada |
| Q-08 | ¿Un contenedor puede mezclar lotes o SKU distintos? | PN-02 E-03 |
| Q-09 | Cuando una etiqueta se deteriora, ¿se reimprime la misma o se necesita que la anterior deje de valer? | A frente a B |
| Q-10 | En la preparación de salidas, ¿el escaneo debe **contar** unidades o solo **verificar** que se toma lo correcto? | Todas (PN-10 paso 7) |
| Q-11 | ¿Qué nivel de trazabilidad física exige el proyecto: lote y ubicación (CD-21), etiqueta, o pieza individual? | A / B / C |
| Q-12 | ¿Cuántas etiquetas por lote se imprimirían en la práctica? | Costo operativo de A frente a B |

**Quién responde:** Q-01 a Q-10 y Q-12, el levantamiento AS-IS con la empresa de estudio (pendiente desde la Auditoría Fundacional, riesgo R-S01). Q-11, el Director, porque es una decisión de alcance.

## 2.7 ¿Bloquea la arquitectura?

**Pregunta de control:** ¿se puede diseñar una arquitectura correcta sin conocer esta respuesta?

- **Mientras C siga siendo posible: NO.** C cambia la identidad y la granularidad del núcleo: agregado, kardex y concurrencia. Una arquitectura diseñada para A o B tendría que rehacer su núcleo si se elige C.
- **Si C se excluye expresamente del MVP, solo quedan A y B.** Esa elección afecta al subdominio de Identificación (de soporte), a la reimpresión y a la semántica del escaneo en la preparación, no al núcleo. Aun así debería decidirse antes de cerrar la arquitectura de identificación.

**ESTADO DE HD-25: DECISIÓN REQUERIDA · BLOQUEANTE** mientras no se excluya o se elija C. Falta información operacional (§2.6).

**Qué se cambió en los documentos por HD-25 (sin decidir):**
- el título y la evidencia de HD-25 (ahora incluyen la relación escaneo–cantidad de PN-10);
- su responsable («decidir antes de la Fase 5»);
- el riesgo RF5-14, que sube a 🔴.

**No se modificó ningún elemento estructural** (entidades, agregados, invariantes, estados, eventos ni reglas).

---

# 3. DEC-01…DEC-09

Definición literal: **SRS v1.1, Anexo C, tabla C.1** (idéntica a la del SRS v1.0). En cada una se contestan dos preguntas: **«¿Se puede diseñar una arquitectura correcta sin conocer esta respuesta?»** y **«¿depende de información de la operación real?»**

## 3.1 Resumen

| ID | Decisión | Estado actual | ¿Bloquea arquitectura? | Información faltante | Acción |
|---|---|---|---|---|---|
| **DEC-01** | Umbral aprobatorio: ¿MVP Núcleo o Completo? ¿Transferencias y conteo general en el MVP? | PENDIENTE DE USUARIO · PENDIENTE DE INFORMACIÓN OPERACIONAL (número de bodegas) | **NO BLOQUEANTE**, con una condición: diseñar para el alcance completo | Respuesta del Director; número real de bodegas | Director elige (a), (b) o (c) |
| **DEC-02** | Lista de alcance: M-02, M-18, M-17 en el MVP; exclusión de toda IA | PENDIENTE DE USUARIO | **NO BLOQUEANTE** | Respuesta del Director | Confirmar (a) o (b) |
| **DEC-03** | Cifra 68/82 y renumeración de reglas | PENDIENTE DE USUARIO (documental) | **NO BLOQUEANTE** | Respuesta del Director | Confirmar (a) o (b) |
| **DEC-04** | Estructural frente a configurable; lectura de parámetros por el Jefe; quién cierra observaciones | PENDIENTE DE USUARIO | **NO BLOQUEANTE** para la arquitectura general; **necesaria antes del diseño detallado** de configuración y permisos | Respuesta del Director | Confirmar (a) o definir (b) |
| **DEC-05** | Cierre de jornada (PN-14): ¿HU y RF? | PENDIENTE DE USUARIO | **NO BLOQUEANTE** | Respuesta del Director | Elegir (a), (b) o (c) |
| **DEC-06** | Reglas y KPI sin RF (PROP-RN, PROP-KPI) | PENDIENTE DE USUARIO | **NO BLOQUEANTE** para la arquitectura; **necesaria antes del modelo de datos** (KPI-05, KPI-12) | Respuesta del Director; para KPI-24, verificación de campo | Elegir (a), (b) o (c) |
| **DEC-07** | Valorización | PENDIENTE DE USUARIO | **NO BLOQUEANTE** mientras rija DC-03; la opción (b) obligaría a reevaluar | Respuesta del Director | Elegir (a) o (b) |
| **DEC-08** | Aprobación formal del SPEC y numeración de fases | PENDIENTE DE USUARIO (académica/documental) | **NO BLOQUEANTE** para el análisis técnico; **bloquea la aprobación formal** | Acta del Director | Acta + tabla de equivalencia de fases |
| **DEC-09** | Alerta «lote próximo a vencer inmovilización» | PENDIENTE DE USUARIO | **NO BLOQUEANTE** | Respuesta del Director | Elegir (a) o (b) |

**Ninguna está RESUELTA.** Ninguna es BLOQUEANTE para la arquitectura por sí sola, pero cuatro imponen **condiciones de diseño** (DEC-01, DEC-04, DEC-06, DEC-07), y DEC-08 impide la **aprobación formal**. Esto **corrige en parte** la conclusión del cierre, que las trataba en bloque como «limitaciones conocidas no bloqueantes»: no bloquean, pero no son inocuas.

## 3.2 DEC-01 — Umbral de entrega aprobatorio

- **Definición exacta:** «¿El MVP aprobatorio es el Núcleo (H1) o el Completo (H1+H2)? ¿Transferencias y conteo general entran al MVP?»
- **Hallazgos:** H-08, S-15.
- **Opciones:** (a) Núcleo, 84 HU / 143 RF, con transferencias y conteo general en v1.1; (b) Completo, 103 HU / 162 RF; (c) Núcleo + transferencias + conteo general.
- **Recomendación del SRS:** alcance Completo, entrega H1 → H2, umbral mínimo = Núcleo.
- **Estado:** PENDIENTE DE USUARIO. También PENDIENTE DE INFORMACIÓN OPERACIONAL: el SPEC justifica el aplazamiento con «el MVP opera con una bodega» (§12.3, elemento 1), pero el número real de bodegas de la empresa no está verificado.
- **¿Arquitectura correcta sin la respuesta?** **Sí, si se diseña para el alcance completo.** El dominio v1.1 ya modela varias bodegas (AG-03), transferencias (AG-10, SM-10) y el bloqueo de movimientos del conteo general (IN-56). Una arquitectura que los soporte es correcta para (a), (b) y (c): la respuesta cambia el orden de entrega y el criterio de aceptación (SRS Cap. 12), no la estructura. **Si se diseñara solo para una bodega**, las opciones (b) o (c) obligarían a rehacerla.
- **Temas revisados:** multi-bodega, concurrencia (bloqueo por conteo general), trazabilidad (tránsito).
- **Acción:** el Director elige. Mientras tanto, la arquitectura debe soportar el alcance completo.

## 3.3 DEC-02 — Lista de alcance del MVP

- **Definición exacta:** confirmar que «usuarios» y «auditoría» son los módulos M-02 y M-18, que el dashboard operativo (M-17) sigue en el MVP y que la exclusión es de **toda** IA (DC-07), no solo de la generativa.
- **Hallazgo:** H-17.
- **Opciones:** (a) mantener los 20 módulos y DC-07; (b) restringir el MVP a la lista del Prompt #003, lo que retira M-17 (3 HU, 4 RF).
- **Recomendación del SRS:** (a).
- **Estado:** PENDIENTE DE USUARIO.
- **¿Arquitectura correcta sin la respuesta?** **Sí.** M-17 solo lee y presenta datos que ya existen; retirarlo es una resta. La exclusión de toda IA ya es el supuesto más estricto (DC-07), y nada del dominio usa IA.
- **Acción:** confirmar (a) o (b).

## 3.4 DEC-03 — Reglas de negocio: cifra y renumeración

- **Definición exacta:** el SPEC declara 68 reglas y sus tablas contienen 82. Se pide confirmar las 82, retirar los marcadores vacíos `RN-069*` y `RN-026b*` y adoptar como canónica la numeración `RN-<DOM>-nnn`.
- **Hallazgos:** H-01, H-09, pendiente #11.
- **Opciones:** (a) SRS como numeración canónica + fe de erratas del SPEC; (b) mantener la numeración del SPEC.
- **Recomendación del SRS:** (a).
- **Estado:** PENDIENTE DE USUARIO (académica/documental). En la v1.1 hay 85 reglas (82 + 3 del cierre del CP-04, separadas en SPEC §9.15); la discrepancia 68/82 sigue declarada y no corregida.
- **¿Arquitectura correcta sin la respuesta?** **Sí.** El modelo usa las 85 reglas reales con sus IDs permanentes; la cifra declarada es documental.
- **Acción:** confirmar (a) o (b).

## 3.5 DEC-04 — Semántica «estructural» frente a «configurable»

- **Definición exacta:** confirmar que toda regla estructural es no configurable (no solo las 10 de §9.1); definir si el Jefe puede **leer** los parámetros y **quién** responde y cierra las observaciones de auditoría (RN-AUD-002).
- **Hallazgos:** H-06; SRS Cap. 10, nota 4.
- **Opciones:** (a) toda regla estructural no configurable, el Jefe lee parámetros, el Administrador o el Jefe responden; (b) otra.
- **Recomendación del SRS:** (a).
- **Estado:** PENDIENTE DE USUARIO. El dominio aplica provisionalmente (a) en IN-67; SM-18 deja como «Por definir (DEC-04)» quién cierra las observaciones.
- **¿Arquitectura correcta sin la respuesta?** **Sí, para la estructura general.**
  - **Autorización y permisos:** la arquitectura de roles y ámbitos (cinco roles, ámbito por bodega y zona) no depende de estas celdas concretas de la matriz de permisos. «El Jefe lee parámetros» y «quién cierra observaciones» son entradas de esa matriz, no su forma.
  - **Integridad:** con (a), ninguna regla estructural se parametriza. Con (b), algunas pasarían a parametrizables, lo que amplía el subsistema de configuración (AG-20) sin cambiar el núcleo.
- **Pero** hace falta **antes del diseño detallado** de M-19 (configuración) y M-18 (auditoría): con (b), una regla que protege la integridad podría implementarse como configurable (R-S08).
- **Temas revisados:** permisos, autorización, auditoría, integridad.
- **Acción:** confirmar (a) o definir (b).

## 3.6 DEC-05 — Cierre operativo de jornada (PN-14)

- **Definición exacta:** «¿Se crean HU y RF?» para PN-14.
- **Hallazgo:** H-10.
- **Opciones:** (a) crear HU y RF (propuestas PROP-CIE); (b) mover PN-14 a v1.1; (c) excluirlo del MVP.
- **Recomendación del SRS:** (a).
- **Estado:** PENDIENTE DE USUARIO. El dominio modela E-26, AG-21, SM-21 y EV-JOR-* marcados ⚠️.
- **¿Arquitectura correcta sin la respuesta?** **Sí.** El cierre de jornada es una consolidación sobre datos que ya existen (pendientes, tránsitos, alertas). Su única restricción estructural —no cerrar con registros sin sincronizar— ya es regla vigente (RN-INT-003, IN-07) y la arquitectura de sincronización debe cumplirla de todos modos. (a) agrega una función; (c) la quita.
- **Temas revisados:** conectividad.
- **Acción:** elegir (a), (b) o (c).

## 3.7 DEC-06 — Cierre de brechas de trazabilidad

- **Definición exacta:** aprobar o descartar las propuestas PROP-RN (reglas sin RF) y PROP-KPI (KPI sin dato de origen).
- **Hallazgos:** H-11, H-12, H-13.
- **Opciones:** (a) aprobar todas; (b) aprobar solo las de KPI-01, 05 y 08; (c) descartar.
- **Recomendación del SRS:** (a); como mínimo (b), porque KPI-05 es uno de los tres indicadores del compromiso.
- **Estado:** PENDIENTE DE USUARIO. Afecta a 6 reglas (RN-MOV-003, RN-MOV-006, RN-NOV-001, RN-NOV-002, RN-CNT-008, RN-SAL-005) y 6 KPI (05, 07, 10, 12, 17, 24). KPI-24 depende además de una verificación de campo.
- **¿Arquitectura correcta sin la respuesta?** **Sí, en su estructura.** Lo que falta son datos por capturar (instante de inicio de una operación, instante de llegada, selección manual —ya en VO-40—, desviación de ubicación), no componentes nuevos.
- **Pero** es **necesaria antes del modelo de datos**: lo que no se captura desde el primer día no se recupera después. KPI-05 perdería su línea base. Pasa lo mismo con los datos históricos.
- **Temas revisados:** trazabilidad, datos históricos.
- **Acción:** elegir (a), (b) o (c).

## 3.8 DEC-07 — «Valorización»

- **Definición exacta:** definir si el permiso «consultar valorización» se retira del MVP o si se define una política de costeo.
- **Hallazgos:** H-07; Horizonte 3.
- **Opciones:** (a) retirarlo del MVP y dejarlo como restricción preventiva; (b) definir una política de costeo, lo que roza DC-03.
- **Recomendación del SRS:** (a).
- **Estado:** PENDIENTE DE USUARIO. El dominio no tiene ningún atributo monetario (HD-09).
- **¿Arquitectura correcta sin la respuesta?** **Sí, mientras rija DC-03** («sin contabilidad»): el MVP no tiene dato que valorizar. Si el Director eligiera (b), habría que agregar costo a entradas y salidas y un método de valoración sobre el kardex. Sería un **cambio de alcance** contrario a DC-03, que obligaría a reevaluar el diseño.
- **Acción:** elegir (a) o (b).

## 3.9 DEC-08 — Aprobación formal del SPEC y numeración de fases

- **Definición exacta:** confirmar por escrito la aprobación del SPEC (el archivo decía «Emitido para revisión») y la equivalencia entre las fases del proyecto y las del roadmap de la Auditoría.
- **Hallazgos:** H-15, H-16.
- **Opciones:** (a) acta de aprobación + tabla de equivalencia de fases; (b) otra.
- **Recomendación del SRS:** (a).
- **Estado:** PENDIENTE DE USUARIO (académica/documental). DF5-06 no la resuelve: tras su revisión, solo registra la **validación técnica** de la v1.1. La decisión se extiende ahora a SPEC v1.1, SRS v1.1 y dominio v1.1.
- **¿Arquitectura correcta sin la respuesta?** **Sí, técnicamente**: el contenido no depende del acta. **No** se puede declarar la base «aprobada» sin ella, y la cadena Monografía → … → Arquitectura exige, en lo académico, una base aprobada.
- **Acción:** acta del Director sobre la v1.1 y tabla de equivalencia de fases.

## 3.10 DEC-09 — Alerta «lote próximo a vencer inmovilización»

- **Definición exacta:** el SPEC enuncia la alerta con una «fecha límite» de lote, dato que no existe en CD-06 ni en ningún RF.
- **Hallazgo:** H-18.
- **Opciones:** (a) redefinirla sobre el umbral de antigüedad (RN-LOT-005); (b) agregar «fecha límite» al lote, que es funcionalidad nueva `[NUEVO]`.
- **Recomendación del SRS:** (a).
- **Estado:** PENDIENTE DE USUARIO. El dominio modela solo la antigüedad (HD-10).
- **¿Arquitectura correcta sin la respuesta?** **Sí.** Es un tipo de alerta más dentro de un mecanismo de reglas y umbrales que ya existe. (b) agregaría un atributo al lote.
- **Acción:** elegir (a) o (b).

---

# 4. MATRIZ DE BLOQUEOS

## 4.1 Bloqueadores de arquitectura

| Asunto | Por qué bloquea | Qué lo desbloquea |
|---|---|---|
| **HD-25** (alternativa C abierta) | Si se elige C, cambian la identidad de la mercancía, el agregado central y la granularidad del kardex y de la concurrencia | Excluir C del MVP (y elegir entre A y B), o elegir C y abrir un cambio de alcance. Requiere Q-01 a Q-11 (§2.6) |

## 4.2 No bloqueadores, con condición de diseño

| Asunto | Condición que la arquitectura debe cumplir mientras no haya respuesta |
|---|---|
| DEC-01 | Soportar el alcance completo: varias bodegas, transferencias y bloqueo por conteo general |
| DEC-04 | Ninguna regla estructural parametrizable (interpretación (a), ya en IN-67); matriz de permisos como dato, no como estructura. Decidir antes del diseño detallado de M-18 y M-19 |
| DEC-06 | Decidir antes del modelo de datos detallado (captura de instantes para KPI-05 y KPI-12) |
| DEC-07 | Sin atributos monetarios mientras rija DC-03 |

## 4.3 No bloqueadores

DEC-02, DEC-03, DEC-05 y DEC-09. Tampoco bloquean HD-17, HD-18, HD-26 y HD-27, que requieren información de la operación real (`04_CP04_CIERRE.md` §13).

## 4.4 Decisiones que dependen de información operacional

| Asunto | Dato faltante | Fuente |
|---|---|---|
| HD-25 | Q-01…Q-10, Q-12 | Levantamiento AS-IS |
| DEC-01 | Número real de bodegas | Levantamiento AS-IS |
| DEC-06 | Verificación de campo de KPI-24 | Levantamiento AS-IS |
| HD-17 · HD-18 | Mezcla de unidades por ubicación; precisión de las medidas | Levantamiento AS-IS |
| HD-26 · HD-27 | Qué identifica el código de barras del proveedor; conectividad real de la bodega | Levantamiento AS-IS |

## 4.5 Decisiones académicas y documentales

| Asunto | Qué falta |
|---|---|
| DEC-08 | Acta de aprobación (ahora sobre la v1.1) y tabla de equivalencia de fases |
| DEC-03 | Cifra canónica y fe de erratas de la numeración |
| Aprobación de la base v1.1 | Depende de DEC-08 y de que HD-25 y DEC-01…DEC-09 se respondan o se acepten por escrito como limitaciones, una por una |
| Q-11 (HD-25) | Nivel de trazabilidad física que exige el proyecto (decisión de alcance) |

---

# 5. RECOMENDACIÓN DE SIGUIENTE PASO

Sin elegir ninguna alternativa que dependa de información ausente:

1. **Responder primero la pregunta que desbloquea la arquitectura:** ¿la trazabilidad por pieza o paquete (alternativa C) está dentro o fuera del MVP? Es la Q-11. La respuesta puede darla el Director como decisión de alcance, o puede salir de Q-01, Q-03 y Q-07 si se consulta a la operación.
2. **Si C queda fuera:** reunir Q-06, Q-09, Q-10 y Q-12 para elegir entre A y B. Según la alternativa, se actualizarán los documentos del §2.5 en una v1.2 (fuentes y generadores; las v1.0 y v1.1 no se tocan).
3. **Responder DEC-01…DEC-09.** Para cada una: una respuesta, o su aceptación **individual y por escrito** como limitación conocida. Las opciones y las recomendaciones del SRS están en el §3.
4. **Emitir el acta de DEC-08** sobre la base resultante. Solo entonces las portadas pueden pasar de «validado técnicamente» a «aprobado».
5. **Priorizar el levantamiento AS-IS mínimo** (R-S01): concentra las respuestas de HD-25, HD-17, HD-18, HD-26, HD-27, DEC-01 (bodegas) y DEC-06 (KPI-24).
6. **Después**, repetir las validaciones (`xref.py`, cobertura, reproducibilidad), hacer commit y abrir el Prompt de la Fase 5.

---

**ESTADO: DECISIONES REQUERIDAS ANTES DE FASE 5**

*Fin de 04_CP04_DECISIONES_PENDIENTES v1.0. La monografía original permanece sin modificaciones.*
