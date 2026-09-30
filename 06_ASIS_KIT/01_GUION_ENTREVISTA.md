# 06 · Guion de entrevista AS-IS

| Campo | Dato |
|---|---|
| **Documento** | Guion de entrevista semiestructurada |
| **Estado** | Borrador; sin usar en campo |
| **Regla DC-01** | La empresa no se nombra; se usa «la empresa de estudio» |

> **Cómo usarlo.** No es un cuestionario para leer en voz alta. Cada bloque tiene una pregunta abierta (en negrita) y otras de sondeo. Se pregunta **cómo se hace hoy**, no si se hace como lo imaginamos. Cada pregunta indica la decisión o el dato que alimenta. Los roles son los **oficiales** del proyecto como referencia; en la empresa pueden llamarse distinto o no existir (perfiles reales, C.2.2): anote el cargo real.

**Roles.** **J** quien autoriza y supervisa la bodega (Jefe) · **C** quien coordina al equipo (Coordinador) · **O** quien opera en piso (Auxiliar) · **Ad** quien administra el acceso y la configuración (Administrador) · **R** quien revisa o audita.

---

# 0. Apertura (2 a 3 minutos)

1. Presentarse y explicar el propósito: *entender cómo trabajan hoy la bodega y su inventario, para diseñar una herramienta que se ajuste a la realidad.*
2. Aclarar que **no se evalúa a las personas**, que no hay respuestas correctas y que lo dicho no se atribuirá a nadie.
3. Pedir el consentimiento (`03_AUTORIZACION_Y_CONSENTIMIENTO.md`) y el permiso para grabar. Sin permiso, solo notas.
4. No mencionar precios, clientes ni proveedores; si aparecen, no se anotan.

# 1. Perfil de la empresa y del entrevistado

| ID | Pregunta | Rol | Alimenta |
|---|---|---|---|
| AI-01 | **¿Cómo describiría la empresa y su actividad?** (qué produce o vende, tamaño aproximado del equipo) | J | A-03, A-04 (definición de PYME y sector) |
| AI-02 | ¿En qué municipio opera? | J | A-05 (ámbito geográfico) |
| AI-03 | ¿Cuál es su cargo, cuánto lleva y qué hace en un día normal? | Todos | Perfiles reales (C.2.2) |
| AI-04 | ¿Cuántas personas trabajan en la bodega y qué hace cada una? | J, C | Perfiles reales; contraste con los 5 roles |

# 2. Estructura física

| ID | Pregunta | Rol | Alimenta |
|---|---|---|---|
| AI-05 | **¿Cuántas bodegas o espacios de almacenamiento tiene la empresa y cómo se distribuyen?** | J | DEC-01 (piloto de 1 bodega); transferencias (H2) |
| AI-06 | ¿Cómo se dividen por dentro (zonas, estantes, pisos, posiciones)? ¿Cómo llaman a cada lugar? | J, C, O | Zonas y ubicaciones (CD-13, CD-14); vocabulario real |
| AI-07 | ¿Existe un lugar donde se recibe la mercancía antes de guardarla? ¿Y uno de mercancía dañada o en revisión? | C, O | Zona de recepción y cuarentena (RN-EXI-007, CD-17) |
| AI-08 | ¿Cómo saben si en un lugar «cabe» más mercancía? (metros, rollos, cajas, estantes libres) | C, O | **HD-17** capacidad y KPI-18 |
| AI-09 | ¿Un mismo lugar puede tener mercancía medida de formas distintas (metros, rollos, unidades)? Dé un ejemplo | C, O | **HD-17** |
| AI-10 | ¿Se mueve mercancía entre zonas o entre bodegas? ¿Con qué frecuencia y quién lo hace? | C, O | Transferencias (PN-06, Horizonte 2) |

# 3. Mercancía, medidas y lotes

| ID | Pregunta | Rol | Alimenta |
|---|---|---|---|
| AI-11 | **¿Qué tipos de mercancía manejan?** (tela, insumos, prendas terminadas, otros) | J, C | Catálogo; glosario textil |
| AI-12 | ¿Cómo cuentan o miden cada tipo? (metros, kilos, unidades, rollos, cajas, bolsas) | C, O | Unidad de medida (CD-11) |
| AI-13 | ¿Con qué exactitud miden? (¿metros con decimales?, ¿kilos con gramos?, ¿se redondea?) | C, O | **HD-18** precisión de las cantidades |
| AI-14 | ¿Cómo distinguen talla y color de una misma referencia? ¿Cómo las llaman? | C, O | SKU (CD-05); vocabulario real |
| AI-15 | ¿Cómo distinguen mercancía que llegó en momentos distintos? ¿Tienen alguna idea de «lote»? | C, O | Lote (CD-06) |
| AI-16 | ¿Cada rollo, paquete o bolsa se anota con su cantidad propia? ¿Cuándo? | C, O | **Q-03**; validar F-2 (cantidad por pieza al recibir) |
| AI-17 | ¿Se cortan partes de un rollo o se sacan unidades de una bolsa? ¿Con qué frecuencia y cómo lo anotan? | C, O | **Q-04**; **HD-29** (validar que una pieza no se divide); F-3 |
| AI-18 | ¿Alguna vez una bolsa o paquete se divide y las partes quedan en lugares distintos? ¿Cuándo pasa? | C, O | **HD-29** (limitación conocida: no se puede dividir) |

# 4. Identificación y etiquetado

| ID | Pregunta | Rol | Alimenta |
|---|---|---|---|
| AI-19 | **¿Cómo saben hoy qué es cada cosa y dónde está?** (etiquetas, marcas, rótulos, memoria, cuaderno) | C, O | Identificación actual; **Q-01** |
| AI-20 | ¿Qué representa una etiqueta o marca hoy: una pieza, un rollo, un bulto, una caja o todo un lote? | C, O | **Q-01**, **HD-28** |
| AI-21 | ¿Un mismo lote se reparte en varias piezas o rollos que se guardan en lugares distintos? | C, O | **Q-02** (premisa de DF5-01) |
| AI-22 | ¿Cómo distinguen entre sí dos piezas o rollos del mismo lote que están en el mismo estante? | C, O | **HD-28** (identidad física de la pieza sin QR propio) |
| AI-23 | ¿Una etiqueta puede representar varias unidades? (por ejemplo, una bolsa de veinte camisetas) | C, O | **Q-07** |
| AI-24 | ¿Un contenedor, caja o bolsa grande puede mezclar mercancía de lotes o referencias distintas? | C, O | **Q-08**, **HD-28** |
| AI-25 | ¿La mercancía llega ya etiquetada por quien la entrega? ¿Con código de barras? ¿Qué identifica ese código: el producto, el lote o la pieza? | C, O | **Q-05**, **HD-26** |
| AI-26 | ¿Quién hace las etiquetas y cómo? ¿Cuántas se hacen por lote, aproximadamente? | C, O | **Q-06**, **Q-12** |
| AI-27 | Cuando una etiqueta se daña, ¿qué hacen? ¿Importa que la nueva sea igual a la anterior? | C, O | Validar **Q-09** (la reimpresión conserva el mismo QR) |
| AI-28 | Cuando sacan mercancía, ¿cuentan cada unidad que toman o solo verifican que sea la correcta? | O | Validar **Q-10** (el escaneo de salida verifica y cuenta) |
| AI-29 | ¿Qué tan importante es saber *qué rollo o pieza exacta* salió, y no solo de qué lote? | J, C | Validar **Q-11** (trazabilidad por pieza en el MVP) |

# 5. Procesos de hoy (recorrido por los 14 procesos)

Para cada proceso, pedir que lo cuenten **con un caso real reciente**. Para cada uno anotar: quién lo hace, en qué orden, qué usa para registrar, cuánto tarda, qué sale mal y qué hace cuando sale mal.

| ID | Proceso TO-BE (SPEC Cap. 3) | Pregunta guía | Sondeos | Rol |
|---|---|---|---|---|
| AI-30 | **PN-01** Recepción | **Cuénteme la última vez que llegó mercancía: qué hicieron desde que llegó hasta que quedó guardada** | ¿Hay documento o lista de lo esperado? ¿Cuentan o pesan? ¿Qué pasa si llega de más, de menos o dañada? ¿Quién da el visto bueno? | C, O |
| AI-31 | **PN-02** Identificación | ¿Qué le ponen a la mercancía cuando llega? | Ver bloque 4 | O |
| AI-32 | **PN-03** Ubicación | ¿Cómo deciden dónde guardarla? | ¿Hay una regla? ¿Quién decide? ¿Qué pasa si el lugar está lleno? ¿Anotan dónde quedó? | C, O |
| AI-33 | **PN-04** Consulta | Si alguien pregunta cuánto hay de algo, ¿qué hacen para responder? | ¿Cuánto tardan? ¿Fiabilidad de la respuesta? ¿A quién le preguntan? | J, C |
| AI-34 | **PN-05** Movimiento interno | ¿Cuándo y cómo mueven mercancía de un lugar a otro dentro de la bodega? | ¿Lo anotan? ¿Quién? ¿Qué pasa si se interrumpe a medio camino? | C, O |
| AI-35 | **PN-06** Transferencia | (Solo si AI-10 indica que ocurre) ¿Cómo entregan y reciben mercancía entre zonas o bodegas? | ¿Quién firma? ¿Qué pasa si no coincide? | C, O |
| AI-36 | **PN-07** Ajustes | Cuando lo que dice el cuaderno no coincide con lo que hay, ¿qué hacen? | ¿Quién autoriza corregir? ¿Con qué motivo? ¿Quedan rastros? ¿Con qué frecuencia? | J, C |
| AI-37 | **PN-08/09** Conteos | ¿Cada cuánto cuentan y cómo? | ¿Cuentan todo de una vez o por partes? ¿Se detiene la operación? ¿El contador sabe lo que dice el cuaderno? ¿Quién recuenta si hay diferencia? | J, C, O |
| AI-38 | **PN-10** Salidas | **Cuénteme la última salida de mercancía** | ¿Quién la pide? ¿Quién autoriza? ¿Quién la prepara? ¿Verifican lo que toman? ¿Dónde queda el registro? | C, O |
| AI-39 | **PN-11** Alertas | ¿Cómo se enteran de que algo se está agotando o sobrando? | ¿Quién avisa? ¿Con cuánta anticipación? ¿Han tenido rupturas de stock? | J, C |
| AI-40 | **PN-12** Novedades | ¿Qué hacen cuando encuentran mercancía dañada, perdida, sin etiqueta o en lugar equivocado? | ¿A quién avisan? ¿Se anota? ¿Se castiga o se resuelve? | O, C |
| AI-41 | **PN-13** Auditoría | ¿Alguien revisa el inventario o los registros de forma independiente? | ¿Quién y cada cuánto? | J, R |
| AI-42 | **PN-14** Cierre | ¿Hacen algo al terminar el día o el turno para dejar la bodega en orden? | ¿Se traspasan pendientes? ¿Quién? | J, C |

# 6. Artefactos y registros actuales

| ID | Pregunta | Rol | Alimenta |
|---|---|---|---|
| AI-43 | **¿Dónde anotan hoy lo que entra, sale y se mueve?** (cuaderno, hojas de cálculo, formatos, mensajes, nada) | Todos | Inventario de artefactos (Fase 3) |
| AI-44 | ¿Me puede mostrar un ejemplo? (**sin fotografiar** datos comerciales; solo la estructura) | C, O | Inventario de artefactos; KPI-08 |
| AI-45 | ¿Quién tiene acceso a esos registros y quién los puede modificar? | J, C | Segregación de funciones (RN-AJU-001 y otras) |
| AI-46 | ¿Qué hacen cuando se equivocan al anotar? (tachan, corrigen, anulan, reescriben) | O, C | KPI-08 (frecuencia de errores) |
| AI-47 | ¿Desde cuándo guardan estos registros? ¿Por cuánto tiempo se conservan? | J | Línea base (períodos disponibles) |

# 7. Roles y responsabilidades

| ID | Pregunta | Rol | Alimenta |
|---|---|---|---|
| AI-48 | **¿Quién puede autorizar una salida? ¿Hay un límite de cantidad?** | J, C | RN-SAL-001 (umbral del Coordinador) |
| AI-49 | ¿Quién puede corregir una diferencia de inventario y quién lo aprueba? ¿Puede una persona aprobar su propia corrección? | J, C | Segregación de funciones (PR-01, RN-AJU-001) |
| AI-50 | ¿Quién recibe la mercancía y quién confirma que entró? ¿Es la misma persona? | C, O | RN-ENT-007 (receptor distinto del confirmador) |
| AI-51 | ¿Quién revisa o audita? | J, R | Rol Auditor |
| AI-52 | ¿Hay turnos? ¿Cuántas personas por turno? | J, C | Cierre de jornada; carga de tareas |

# 8. Tecnología y conectividad

| ID | Pregunta | Rol | Alimenta |
|---|---|---|---|
| AI-53 | **¿Qué dispositivos usa la bodega?** (computador, celular, tablet) ¿Tienen cámara? | Todos | Supuesto S-3 (tablet con cámara) |
| AI-54 | ¿Hay internet en la bodega? ¿Dónde hay señal y dónde no? ¿Con qué frecuencia se cae? | C, O | **HD-27**, RNF de disponibilidad, S-5 |
| AI-55 | ¿Qué operaciones les parecería indispensable poder hacer aun sin internet? | C, O | **HD-27** |
| AI-56 | ¿Tienen cómo imprimir etiquetas en la bodega? ¿Qué tipo de impresora o papel? ¿Resisten la humedad, el roce o el polvo? | C | Supuesto S-4 |
| AI-57 | ¿Usan Power BI u otra herramienta para ver datos? ¿Quién? | J, Ad | Supuesto S-6 (herramienta analítica externa) |
| AI-58 | ¿Quién administra los accesos o las cuentas de sus herramientas actuales? | J, Ad | Rol Administrador |

# 9. Problemas, errores y adopción

| ID | Pregunta | Rol | Alimenta |
|---|---|---|---|
| AI-59 | **¿Cuáles son los problemas más frecuentes con el inventario?** | Todos | Problemas P-01 a P-24 (Auditoría A.8) |
| AI-60 | ¿Se han quedado sin mercancía cuando la necesitaban? ¿Con cuánta frecuencia? ¿Y con exceso? | J, C | KPI-21 (rupturas); sobre stock |
| AI-61 | ¿Qué hay de mercancía perdida, dañada o sin movimiento por mucho tiempo? | J, C | KPI-13, KPI-17 |
| AI-62 | ¿Han probado alguna herramienta digital antes? ¿Cómo les fue? | J, C, O | Adopción; R-09 |
| AI-63 | **¿Qué haría que el equipo aceptara o rechazara una herramienta nueva?** | O, C | Resistencia cultural (P-16); V-11 |
| AI-64 | ¿Qué tan cómodo se siente el equipo con tablets o celulares? | O, C | Usabilidad (V-07) |
| AI-65 | ¿Habría tiempo y disposición para capacitarse? ¿Cuánto? | J, C | V-09 (capacitación) |

# 10. Datos para la línea base

| ID | Pregunta | Rol | Alimenta |
|---|---|---|---|
| AI-66 | **¿Cuántos movimientos (entradas, salidas, cambios de lugar) hacen en un día normal, más o menos?** | J, C | Denominador de **KPI-24** (adopción); KPI-11 |
| AI-67 | ¿Hay días o épocas de más movimiento? ¿Cuándo? | J | Estacionalidad; planeación del piloto |
| AI-68 | ¿Qué registros históricos pueden compartirnos de un período reciente? (solo la estructura y conteos, sin valores comerciales) | J, C | Línea base KPI-08, 11 |
| AI-69 | ¿Cuántos ajustes o correcciones de inventario hacen al mes, más o menos? | J, C | KPI-14 |

# 11. Cierre (5 minutos)

1. ¿Hay algo importante que no le preguntamos?
2. ¿A quién más deberíamos entrevistar?
3. Agradecer y recordar que el informe final se devolverá a la empresa para que confirme que describe fielmente su proceso.
4. Confirmar qué documentos puede compartir, con qué restricciones y a quién pedírselos.

---

**Matriz de cobertura de preguntas abiertas**

| Pendiente | Preguntas |
|---|---|
| Q-01, Q-02, Q-03, Q-04 | AI-16, AI-17, AI-19 a AI-21 |
| Q-05, Q-06, Q-07, Q-08, Q-12 | AI-23 a AI-26 |
| Q-09, Q-10, Q-11 (ya decididas; se validan) | AI-27, AI-28, AI-29 |
| HD-17, HD-18 | AI-08, AI-09, AI-13 |
| HD-26, HD-27 | AI-25, AI-54, AI-55 |
| HD-28, HD-29 | AI-20, AI-22, AI-24, AI-17, AI-18 |
| DEC-01 (bodegas) | AI-05, AI-10 |
| KPI-24 (denominador) | AI-66 |
| Supuestos S-3, S-4, S-6 | AI-53, AI-56, AI-57 |
| Perfiles reales (C.2.2) | AI-03, AI-04, AI-48 a AI-52 |

---

*Fin del guion de entrevista AS-IS.*
