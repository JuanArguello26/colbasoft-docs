# 06 · Guion de observación y línea base AS-IS

| Campo | Dato |
|---|---|
| **Documento** | Guía de observación en piso y hojas de medición de la línea base |
| **Estado** | Borrador; sin usar en campo |
| **Base** | SRS v1.4 Cap. 10 (fórmulas de los KPI) · Auditoría (C.2.4, V-03) |

> **Sin cifras inventadas.** Este documento define **qué** medir y **cómo**, con las fórmulas que ya tiene el SRS. El **tamaño de cada muestra** y la **duración** de la medición no están decididos (V-05, V-08 abiertas) y se acuerdan con el asesor antes de medir. Donde diga «N», es un valor por acordar.

---

# A. Reconocimiento (primera visita)

| # | Qué hacer | Anotar |
|---|---|---|
| A1 | Recorrer la bodega con quien la conozca | Croquis a mano: zonas, estantes, puertas, zona de recepción, zona de mercancía dañada |
| A2 | Contar zonas y ubicaciones, sin nombrar a la empresa | Número de bodegas, zonas y ubicaciones (aproximado); cómo las llaman |
| A3 | Ver cómo se rotula hoy la mercancía y los lugares | Tipo de etiqueta o marca; qué dice; dónde está puesta |
| A4 | Identificar los **artefactos de registro** (cuadernos, hojas, formatos) | Nombre, quién lo llena, cuándo, qué columnas tiene. **No fotografiar datos comerciales** |
| A5 | Identificar dispositivos y conectividad | Computadores, celulares, tablets; dónde hay señal; impresoras |
| A6 | Ver la **mercancía en rollos, bolsas, cajas o paquetes** | Cómo se apilan y se guardan; si hay mezcla de lotes; cuántas piezas hay por lote (aproximado) |

# B. Observación de procesos en piso

Acompañar, sin intervenir, **operaciones reales**. Anotar solo lo que se ve; la interpretación va en otra columna.

## B.1 Ficha de una operación observada

Una ficha por operación. Copiar la tabla tantas veces como haga falta.

| Campo | Anotación |
|---|---|
| Código de la observación | OBS-____ |
| Fecha | |
| Proceso (PN-01 recepción, PN-03 ubicación, PN-05 movimiento interno, PN-10 salida, PN-08/09 conteo, otro) | |
| Rol de quien ejecuta (código, no nombre) | |
| Rol de quien autoriza o verifica | |
| **Hora de inicio** (cuando la persona empieza la operación) | |
| **Hora en que queda registrada** (cuando anota lo que hizo, o «no se registró») | |
| Hora de fin de la operación física | |
| Medio de registro (cuaderno, hoja, mensaje, memoria, ninguno) | |
| Mercancía (tipo general, unidad de medida: metros, kilos, unidades) | |
| ¿Piezas, rollos o bolsas? ¿Cuántos? | |
| ¿Se verificó lo que se movía? ¿Cómo? (vista, conteo, pesaje, etiqueta) | |
| Errores o correcciones vistos (tachón, repetición, duda) | |
| Imprevistos (faltaba algo, se interrumpió, se cayó la señal) | |
| **Lo observado** (hechos) | |
| **Interpretación del observador** (aparte) | |

## B.2 Qué mirar en cada proceso

| Proceso | Mirar especialmente |
|---|---|
| **Recepción (PN-01)** | Cómo se cuenta o pesa; si se compara con lo esperado; qué se hace con faltantes, sobrantes y daños; quién confirma; cuánto pasa desde que llega hasta que se anota |
| **Ubicación (PN-03)** | Cómo se decide el lugar; si se registra; qué pasa si está lleno; cuánto tarda |
| **Movimiento interno (PN-05)** | Si se registra; qué se mueve (pieza completa o parte) |
| **Salida (PN-10)** | Quién pide, quién autoriza, quién prepara; si se verifica lo que se toma y cómo; si se cuenta unidad por unidad; dónde queda el registro |
| **Conteo (PN-08 / PN-09)** | Cómo se cuenta (pieza por pieza, por bultos); si el contador conoce la cantidad registrada; qué pasa con las diferencias; si se detiene la operación |
| **Cierre (PN-14)** | Si se hace algo al final del turno |

---

# C. Línea base de los KPI

Las fórmulas son las del SRS (Cap. 10). Se miden primero los **tres indicadores que compromete la monografía** (§8.2) y, si hay datos, los demás.

| Prioridad | KPI | Por qué |
|---|---|---|
| **1** | KPI-01 Exactitud del inventario | Indicador 1 de la monografía |
| **1** | KPI-05 Tiempo medio de registro de un movimiento | Indicador 2 de la monografía |
| **1** | KPI-08 Frecuencia de errores de registro | Indicador 3 de la monografía |
| 2 | KPI-11 Volumen de movimientos · KPI-12 Tiempo medio de recepción · KPI-24 Adopción (denominador) | Alimentan el cálculo del resto |
| 3 | KPI-13 Merma · KPI-14 Ajustes · KPI-17 Existencia sin movimiento · KPI-21 Rupturas · KPI-10 Desviaciones de ubicación | Si hay datos disponibles |

## C.1 KPI-01 · Exactitud del inventario

**Fórmula:** `(líneas contadas conformes ÷ total de líneas contadas) × 100`.

**Procedimiento:**

1. Acordar con el asesor una **muestra** de N ubicaciones (o referencias) y cómo se elige (al azar, estratificada por zona). Anotar el criterio.
2. Para cada ubicación de la muestra, obtener de la empresa lo que **su registro actual dice** que hay (cuaderno u hoja), **sin que lo vea quien va a contar**.
3. Quien cuenta **no conoce** la cantidad registrada mientras cuenta (equivale a la regla RN-CNT-002 del SRS: la cantidad esperada no se muestra al contador).
4. Contar físicamente **pieza por pieza** (F-5) y anotar la cantidad de cada pieza.
5. Comparar. Anotar **la diferencia exacta**, no solo «coincide / no coincide»: así se puede aplicar después cualquier tolerancia.

**Hoja de registro:**

| Código línea | Zona | Referencia (código interno) | Unidad de medida | Cantidad registrada por la empresa | Cantidad contada | Diferencia | ¿Conforme? (exacta) | Observaciones |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

**Resultado:** líneas conformes exactas ÷ líneas contadas, y la distribución de diferencias.

## C.2 KPI-05 · Tiempo medio de registro de un movimiento

**Fórmula:** `Σ (instante de confirmación − instante de inicio) ÷ número de movimientos`.

En la situación actual no hay «confirmación del sistema»: se usa **el instante en que queda anotado el movimiento en el medio actual**. Se cronometran N operaciones por tipo (entrada, ubicación, movimiento, salida) usando la ficha B.1.

| Tipo de operación | Nº de operaciones medidas | Suma de tiempos (inicio → registro) | Promedio | Observaciones (p. ej. «no se registró en el momento») |
|---|---|---|---|---|
| Entrada | | | | |
| Ubicación | | | | |
| Movimiento interno | | | | |
| Salida | | | | |

> **Importante.** Además del tiempo, anotar **cuántas operaciones no se registraron en el momento** (se anotan después o nunca). Es el punto de partida del KPI-24 y de la resistencia a registrar.

## C.3 KPI-08 · Frecuencia de errores de registro

**Fórmula SRS:** `(ajustes correctivos + movimientos anulados + líneas de conteo con diferencia) ÷ total de movimientos del período × 100`.

Con el registro actual (cuaderno u hoja), sobre un **período** de N días que ya esté escrito:

| Dato | Cómo obtenerlo | Valor |
|---|---|---|
| Total de movimientos del período | Contar las anotaciones | |
| Correcciones (tachones, reescrituras, anulaciones) | Contar las visibles en el registro | |
| Ajustes correctivos | Preguntar y verificar en el registro | |
| Líneas de conteo con diferencia | Del KPI-01 (C.1) o de conteos previos | |

> **Limitación.** Un registro en papel puede no mostrar todos los errores. Anotar esa limitación en el informe.

## C.4 Indicadores de prioridad 2 y 3

| KPI | Dato a pedir o medir | Cómo |
|---|---|---|
| **KPI-11 Volumen de movimientos** | Movimientos por día | Contar anotaciones de N días; preguntar por días atípicos |
| **KPI-12 Tiempo medio de recepción** | Desde que llega la mercancía hasta que queda confirmada | Cronometrar N recepciones (inicio = llegada) |
| **KPI-24 Adopción (denominador)** | Movimientos totales reales por día, con y sin registro | Observación directa en días de muestra: comparar lo que ocurre con lo que queda anotado |
| **KPI-13 Merma** | Unidades dadas de baja por daño o pérdida en un período | Preguntar; revisar el registro si existe |
| **KPI-14 Ajustes** | Número de ajustes y magnitud | Preguntar; revisar |
| **KPI-17 Existencia sin movimiento** | Mercancía sin tocar hace mucho | Recorrido y preguntas; acordar el umbral de días con el asesor |
| **KPI-21 Rupturas** | Veces que una referencia se agotó | Preguntar por el último mes; revisar |
| **KPI-10 Desviaciones de ubicación** | Veces que se guarda donde no estaba previsto | Hoy no hay «propuesta», así que solo se anota cómo se decide el lugar |

# D. Ficha de resumen de la línea base

| KPI | Método | Muestra (N) | Período o fecha | Resultado | Limitaciones |
|---|---|---|---|---|---|
| KPI-01 | | | | | |
| KPI-05 | | | | | |
| KPI-08 | | | | | |
| KPI-11 | | | | | |
| KPI-12 | | | | | |
| KPI-24 (denominador) | | | | | |

---

*Fin del guion de observación y línea base.*
