# 06 · Kit de levantamiento AS-IS — Plan y guía de uso

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | Kit de levantamiento AS-IS (Fase 3 del roadmap de la Auditoría) |
| **Fecha** | 30 de septiembre de 2026 |
| **Estado** | **Borrador para revisión del Director y del asesor.** No se ha usado en campo |
| **Base** | Auditoría Fundacional, Fase D (Fase 3: levantamiento del dominio) y Fase F (V-01, V-03, V-10) · SPEC v1.4 · SRS v1.4 · Modelo de dominio v1.4 |
| **Regla DC-01** | La empresa piloto **no se nombra** en ningún documento del proyecto. En todo el kit se la llama «la empresa de estudio» o «la empresa piloto» |

> **Naturaleza.** El SPEC, el SRS y el dominio describen el proceso **TO-BE**: cómo debería funcionar el sistema. Ningún documento describe cómo funciona **hoy** la bodega (vacío C.1.8) ni mide su desempeño actual (vacío C.2.4). Este kit sirve para hacerlo, **sin sugerir respuestas ni presentar el sistema como algo ya decidido**.

---

# 1. Para qué sirve

| Objetivo | Por qué importa |
|---|---|
| **Contrastar los requisitos con la realidad** | El SRS se emitió antes del AS-IS (riesgo R-S01): sus 185 requisitos no están contrastados con la operación real |
| **Cerrar decisiones que dependen de datos de campo** | HD-28, reabrir HD-29 si hiciera falta, HD-17, HD-18, HD-26, HD-27, número de bodegas (DEC-01) y la verificación de campo de KPI-24 |
| **Establecer la línea base** | Sin medir cómo estaba la operación no se puede demostrar mejora: es la condición de la demostración de impacto (V-03, SPEC §13.6 asunto 5) |
| **Completar los productos de la Fase 3** | Proceso actual, glosario textil, artefactos actuales, perfiles reales de usuario, línea base cuantificada y restricciones técnicas reales |

**Criterio de cierre de la Fase 3 (Auditoría):** *proceso AS-IS validado por al menos una empresa del sector.*

# 2. Contenido del kit

| Archivo | Para qué |
|---|---|
| `01_GUION_ENTREVISTA.md` | Preguntas por bloque y por rol, cada una con la decisión que alimenta |
| `02_GUION_OBSERVACION_Y_LINEA_BASE.md` | Observación en piso y hojas de medición de los KPI de línea base |
| `03_AUTORIZACION_Y_CONSENTIMIENTO.md` | Borrador de autorización de contacto (V-01) y consentimiento informado (V-10) |
| `04_PLANTILLA_INFORME_ASIS.md` | Estructura del informe final y contraste supuesto TO-BE frente a lo observado |

# 3. Antes de salir a campo (condiciones)

| # | Condición | Estado | Quién |
|---|---|---|---|
| 1 | **Autorización de contacto con empresas reales** (V-01): la monografía dice «sin intervenir empresas reales» | Pendiente | Director |
| 2 | Acuerdo con el asesor sobre el **método de medición** y el tamaño de las muestras de la línea base (V-05, V-08 están abiertas: duración del piloto y grupo de control) | Pendiente | Director y asesor |
| 3 | Revisión del formato de consentimiento por el CIAF (y por el comité de ética si aplica) | Pendiente | Director y asesor |
| 4 | Definición de **empresa piloto**: PYME, sector textil y municipio (A-03, A-04, A-05, SPEC §13.6 asuntos 1 a 3) | Pendiente | Director |
| 5 | Persona de contacto en la empresa y fechas de visita | Pendiente | Equipo |

> **No hay cifras de muestra en este kit.** El tamaño de cada muestra (ubicaciones a contar, movimientos a cronometrar, días a revisar) **no está decidido** y no se inventa: se acuerda con el asesor antes de medir.

# 4. Plan de trabajo sugerido

| Etapa | Qué se hace | Material |
|---|---|---|
| **0. Preparación** | Cerrar las condiciones de §3; leer las guías; decidir quién entrevista, quién observa y quién mide | Este kit |
| **1. Reconocimiento** | Recorrido de la bodega, artefactos actuales (cuadernos, formatos, hojas), fotos **solo con permiso** | `02` (parte A) |
| **2. Entrevistas** | Una por rol real: quien autoriza, quien coordina, quien opera, quien lleva el registro | `01` |
| **3. Observación** | Acompañar entradas, ubicación, salidas y conteos reales, con tiempos | `02` (parte B) |
| **4. Línea base** | Mediciones de los KPI prioritarios (01, 05, 08) y, si hay datos, los demás | `02` (parte C) |
| **5. Informe y validación** | Redactar el informe; devolverlo a la empresa para que confirme que describe su proceso | `04` |

# 5. Trazabilidad: qué pregunta cierra qué

| Pregunta o dato | Decisión o hallazgo que alimenta | Documento afectado |
|---|---|---|
| Q-01, Q-02, Q-03, Q-05, Q-06, Q-07, Q-08, Q-12 (etiquetas, piezas, rollos) | **HD-28**: identidad física de la pieza sin QR propio; mezcla de lotes en un contenedor; reemplazo de QR | Dominio, SPEC (CD-49, RN-LOT-006) |
| Q-04 (cortes: frecuencia y forma) | Reabrir **HD-29** si el no poder dividir un paquete o bolsa estorba la operación | SPEC (RN-090*), dominio |
| Q-09, Q-10, Q-11 | **Ya decididas** por el Director (mismo QR al reimprimir; el escaneo de salida verifica y cuenta; la trazabilidad por pieza está en el MVP). Se **validan** en campo, no se vuelven a preguntar como abiertas | SPEC v1.2 |
| Mezcla de unidades por ubicación y cómo miden el espacio | **HD-17** (capacidad frente a unidades heterogéneas) y KPI-18 | Dominio, SRS |
| Precisión de metros, kilos y unidades | **HD-18** (precisión de las cantidades) | Fase 5 |
| Qué identifica el código de barras del proveedor | **HD-26** | SRS (Horizonte 2) |
| Conectividad y dispositivos de la bodega | **HD-27** y RNF de disponibilidad | SRS, Fase 5 |
| Dispositivos con cámara, impresión de etiquetas y herramienta analítica | Supuestos **S-3, S-4 y S-6** del SRS (hoy «por confirmar») | SRS Cap. 2, Fase 5 |
| Número de bodegas y zonas | Condición de **DEC-01** (piloto de 1 bodega) | SPEC, SRS |
| Volumen diario de movimientos | Denominador de **KPI-24** (adopción) | SRS |
| Cómo se hace hoy cada proceso | Contraste con los 14 procesos TO-BE (PN-01 a PN-14) | SPEC Cap. 3 |
| Roles reales y quién hace qué | Perfiles reales de usuario (C.2.2) frente a los 5 roles oficiales | SPEC Cap. 2 |
| Artefactos actuales | Inventario de artefactos (Fase 3) | Informe |
| Línea base de KPI-01, 05, 08 | Demostración de impacto (V-03) | SRS Cap. 10 |

# 6. Reglas de campo

1. **No sugerir respuestas.** Preguntar cómo se hace, no si se hace como lo pensamos nosotros.
2. **No presentar COLBASOFT como algo decidido.** Es una propuesta en diseño.
3. **No juzgar ni imputar.** Lo que se observa describe el proceso, no a las personas (principio PR-06 del SPEC: registrar no es castigar).
4. **Anonimato.** La empresa y las personas se identifican por códigos (p. ej. «EMP-1», «Rol-Bodega-1») en todo documento que salga del equipo.
5. **Datos comerciales.** Precios, clientes y proveedores **no** se anotan (DC-03 excluye compras, ventas y contabilidad). Si aparecen, no se registran.
6. **Grabar solo con permiso** por escrito (`03`). Sin permiso, tomar notas.
7. **Separar dato de interpretación.** En las notas, lo observado va en una columna y lo que creemos va en otra.
8. **Guardar los datos crudos aparte** de los documentos del proyecto (repositorio), porque pueden identificar a la empresa.

# 7. Lo que este kit no hace

- No define muestras, plazos ni criterios de éxito: están abiertos (V-05, V-06, V-08) y se acuerdan con el asesor.
- No reemplaza la revisión del CIAF ni asesoría legal sobre el consentimiento.
- No levanta el proceso de **varias** empresas: el criterio de cierre exige al menos una.

---

*Fin del plan del kit AS-IS. La monografía original permanece sin modificaciones.*
