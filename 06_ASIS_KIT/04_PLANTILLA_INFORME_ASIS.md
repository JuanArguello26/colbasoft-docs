# 06 · Plantilla del informe AS-IS

| Campo | Dato |
|---|---|
| **Documento** | Plantilla del informe final del levantamiento AS-IS |
| **Estado** | Plantilla vacía; se llena después de la campaña de campo |
| **Base** | Fase 3 del roadmap de la Auditoría: productos esperados y criterio de cierre |

> **Criterio de cierre (Auditoría, Fase 3):** *proceso AS-IS validado por al menos una empresa del sector.* El informe se devuelve a la empresa y se registra su validación en la sección 10.

**Regla DC-01.** La empresa se llama «EMP-1» (o el código que se asigne); las personas, por su código de rol. Ningún nombre propio.

---

# 1. Ficha de la campaña

| Campo | Dato |
|---|---|
| Empresa (código) | |
| Actividad y tamaño (sin datos que la identifiquen) | |
| Municipio (si es compartible) | |
| Fechas de visita | |
| Personas entrevistadas (por rol y código) | |
| Operaciones observadas | |
| Autorización y consentimientos (referencia, no copia) | |

# 2. Descripción de la operación actual

| Elemento | Hallazgo |
|---|---|
| Bodegas, zonas y ubicaciones | (DEC-01: número real de bodegas) |
| Tipos de mercancía y unidades de medida | |
| Precisión con que se miden las cantidades (HD-18) | |
| Mezcla de unidades por ubicación y forma de medir la capacidad (HD-17) | |

# 3. Proceso actual, proceso por proceso

Para cada proceso, describir cómo se hace **hoy** y compararlo con el TO-BE del SPEC (Cap. 3).

| Proceso TO-BE | Cómo se hace hoy | Quién | Con qué registro | Tiempo aproximado | Problemas observados | Diferencias con el TO-BE |
|---|---|---|---|---|---|---|
| PN-01 Recepción | | | | | | |
| PN-02 Identificación | | | | | | |
| PN-03 Ubicación | | | | | | |
| PN-04 Consulta | | | | | | |
| PN-05 Movimiento interno | | | | | | |
| PN-06 Transferencia | | | | | | |
| PN-07 Ajuste | | | | | | |
| PN-08 Conteo cíclico | | | | | | |
| PN-09 Conteo general | | | | | | |
| PN-10 Salida | | | | | | |
| PN-11 Alertas | | | | | | |
| PN-12 Novedades | | | | | | |
| PN-13 Auditoría | | | | | | |
| PN-14 Cierre | | | | | | |

# 4. Glosario del dominio textil (vocabulario real)

| Término de la empresa | Qué significa | Equivalente en el glosario oficial (GL-nnn) o «sin equivalente» |
|---|---|---|
| | | |

# 5. Inventario de artefactos actuales

| Artefacto | Quién lo llena | Cuándo | Qué contiene (estructura) | Problemas |
|---|---|---|---|---|
| | | | | |

# 6. Perfiles y roles reales

| Cargo real | Qué hace | Rol oficial más cercano (Administrador, Jefe, Coordinador, Auxiliar, Auditor) | Diferencias |
|---|---|---|---|
| | | | |

**Segregación de funciones observada:** ¿quién autoriza, quién ejecuta, quién confirma, quién corrige? (PR-01)

# 7. Restricciones técnicas reales

| Tema | Hallazgo | Supuesto que contrasta |
|---|---|---|
| Dispositivos y cámara | | S-3 |
| Conectividad (HD-27) | | S-5 |
| Impresión de etiquetas | | S-4 |
| Herramienta analítica (Power BI) | | S-6 |

# 8. Identificación y piezas (cierre de preguntas abiertas)

| Pregunta | Respuesta observada | Qué decisión cambia |
|---|---|---|
| Q-01 ¿Qué representa hoy una etiqueta? | | HD-28 |
| Q-02 ¿Un lote se reparte en varias ubicaciones? | | DF5-01 |
| Q-03 ¿Cada rollo o pieza tiene cantidad propia? | | F-2 |
| Q-04 ¿Hay cortes parciales? ¿Con qué frecuencia? | | **HD-29**: ¿estorba que una pieza no se divida? |
| Q-05 / HD-26 ¿Qué identifica el código de barras del proveedor? | | Horizonte 2 |
| Q-06 ¿Quién imprime las etiquetas? | | SPEC |
| Q-07 ¿Una etiqueta representa varias unidades? | | HD-28 |
| Q-08 ¿Un contenedor mezcla lotes o referencias? | | HD-28 |
| Q-12 ¿Cuántas etiquetas por lote? | | Costo operativo |
| Q-09, Q-10, Q-11 (validar decisiones ya tomadas) | | SPEC v1.2 |
| HD-28 ¿Cómo se distinguen físicamente dos piezas del mismo lote? | | HD-28 |

# 9. Línea base

Completar con la ficha D del archivo `02_GUION_OBSERVACION_Y_LINEA_BASE.md`, con método, muestra, período y limitaciones de cada KPI.

| KPI | Resultado | Método y muestra | Limitaciones |
|---|---|---|---|
| KPI-01 Exactitud | | | |
| KPI-05 Tiempo de registro | | | |
| KPI-08 Errores de registro | | | |
| KPI-24 Adopción (denominador) | | | |

# 10. Contraste con los supuestos del proyecto

| Supuesto TO-BE | ¿Se confirma? | Evidencia | Consecuencia |
|---|---|---|---|
| S-2 Los procesos TO-BE son compatibles con la operación real | | | |
| Piloto de 1 bodega (DEC-01) | | | |
| El MVP cubre lo que la operación necesita (SPEC §12.2) | | | |
| Los 5 roles oficiales cubren los cargos reales | | | |

**Requisitos que cambiarían** (citar el ID del SRS): …
**Requisitos que faltan** (nuevos hallazgos): …
**Decisiones que se reabren o se cierran:** …

# 11. Validación por la empresa

| Campo | Dato |
|---|---|
| Fecha de devolución del informe | |
| Persona que lo validó (código de rol) | |
| ¿Describe fielmente su proceso? | ☐ Sí ☐ Con correcciones ☐ No |
| Correcciones pedidas | |
| Fecha de validación | |

---

*Fin de la plantilla del informe AS-IS.*
