# MVP COLBASOFT en OutSystems — guía paso a paso

Presentación: **lunes 23 de noviembre de 2026**. Se muestra la aplicación funcionando en OutSystems (sin diapositivas).
Debe cubrir: (1) base de datos y front-end, (2) botones de eliminar en los formularios que lo necesitan, (3) consultas adicionales.

Archivo de datos: `COLBASOFT_OutSystems.xlsx` (esta carpeta). Una hoja = una entidad, ya en orden de dependencias y con datos ficticios.

| Hoja | Filas | Hoja | Filas |
|---|---|---|---|
| UnidadMedida | 4 | Bodega | 1 |
| TipoZona | 4 | Zona | 6 |
| TipoMovimiento | 3 | Ubicacion | 30 |
| EstadoSalida | 4 | Lote | 45 |
| Categoria | 3 | Movimiento (kardex) | 135 |
| Talla / Color | 5 / 10 | Salida | 12 |
| Referencia | 22 | LineaSalida | 30 |
| Sku | 122 | | |

Las columnas que terminan en `Id` traen el número de fila de la hoja a la que apuntan (Categoría 1 = Prendas, 2 = Telas, 3 = Insumos…). En `Zona.CategoriaId` el `0` significa «sin categoría».

---

## Parte 1 — Base de datos y front-end (martes–miércoles)

### 1.1 Crear la aplicación
1. Service Studio → **New Application** → **Reactive Web App** → nombre `COLBASOFT`.
2. Crear el módulo (mismo nombre). Publicar una vez vacío (botón **1-Click Publish**) para verificar el entorno.

### 1.2 Importar las entidades desde el Excel
1. Pestaña **Data** → clic derecho en **Entities** (o en la base de datos) → **Import Entities from Excel…** → elegir `COLBASOFT_OutSystems.xlsx`.
2. OutSystems crea **una entidad por hoja**, con sus atributos y una acción/timer *Bootstrap* que carga los datos al publicar.
3. **Publicar**. Al terminar, verificar los datos: clic derecho en una entidad → *View Data* (O11) o en el portal (ODC).

> Los Id se asignan 1, 2, 3… en el orden de las filas solo si la tabla está vacía. Si se reimporta, borrar antes la entidad y volver a importar, o los `…Id` dejarán de coincidir.

### 1.3 Convertir las columnas `…Id` en relaciones (lo que hace que sea una base de datos relacional)
Para cada atributo de la tabla de abajo: seleccionarlo → propiedad **Data Type** → elegir el identificador de la entidad (p. ej. `Categoria Identifier`) → en **Delete Rule** dejar el valor indicado.

| Entidad.Atributo | Data Type | Delete Rule |
|---|---|---|
| Referencia.CategoriaId | Categoria Identifier | Protect |
| Referencia.UnidadMedidaId | UnidadMedida Identifier | Protect |
| Sku.ReferenciaId / TallaId / ColorId | … Identifier | Protect |
| Zona.BodegaId | Bodega Identifier | Protect |
| Zona.TipoZonaId | TipoZona Identifier | Protect |
| Zona.CategoriaId | Categoria Identifier (Is Mandatory = No) | Ignore |
| Ubicacion.ZonaId | Zona Identifier | Protect |
| Lote.SkuId | Sku Identifier | Protect |
| Movimiento.LoteId / UbicacionId / TipoMovimientoId | … Identifier | Protect |
| Salida.BodegaId | Bodega Identifier | Protect |
| Salida.EstadoSalidaId | EstadoSalida Identifier | Protect |
| LineaSalida.SalidaId | Salida Identifier | **Delete** (cascada) |
| LineaSalida.LoteId | Lote Identifier | Protect |

Revisar también los tipos inferidos: `Movimiento.Cantidad`, `LineaSalida.Cantidad`, `Ubicacion.Capacidad` → **Decimal**; `Fecha` → **Date Time**; `FechaIngreso` → **Date**; `Activa` → **Boolean**. Marcar como **Is Mandatory** los nombres y códigos.

Publicar. Si falla por una relación, es casi siempre un `…Id` que no coincide (ver la nota de 1.2).

**Para mostrar en la presentación:** clic derecho en Entities → **Create Entity Diagram** → arrastrar todas las entidades. Se ven las 16 tablas y sus relaciones.

### 1.4 Front-end (pantallas generadas)
Pestaña **Interface** → abrir **MainFlow** → arrastrar cada entidad desde la pestaña Data al flujo. OutSystems genera dos pantallas por entidad: **lista** (con buscador y paginación) y **detalle** (formulario con Guardar).

Hacerlo para: Categoria, Referencia, Talla, Color, Sku, Bodega, Zona, Ubicacion, Lote, Movimiento, Salida.
Los dropdowns de las llaves foráneas los genera solos.

Ajustes que dan buena impresión (si hay tiempo):
- **Menú**: agrupar en *Catálogo* (Categorías, Referencias, Tallas, Colores, SKU), *Bodega* (Bodegas, Zonas, Ubicaciones), *Inventario* (Lotes, Movimientos, Existencia, Kardex) y *Salidas*.
- En la lista de **Referencias**, mostrar el nombre de la categoría (el Aggregate ya tiene el join; agregar la columna `Categoria.Nombre`).
- En la lista de **Sku**, mostrar `Referencia.Descripcion`, `Talla.Nombre`, `Color.Nombre`.
- En **Salida** detalle, agregar debajo una tabla con sus `LineaSalida` (Aggregate filtrado por `SalidaId`).
- **Roles** (opcional): crear roles `Administrador`, `JefeBodega`, `Auxiliar` y en cada pantalla marcar qué roles la pueden ver.

---

## Parte 2 — Botones de eliminar (jueves)

**Dónde van** (pantallas de detalle): Categoría, Referencia, Talla, Color, Sku, Bodega, Zona, Ubicación, Lote y Salida.
**Dónde NO van, y por qué** (argumento de diseño para la presentación): **Movimiento**. El kardex de COLBASOFT es inmutable: un error se corrige con un movimiento inverso, nunca borrando. Lo mismo para una Salida *Confirmada*.

### 2.1 Server Action de eliminación (ejemplo con Categoría)
Logic → Server Actions → **EliminarCategoria**, parámetro de entrada `CategoriaId` (Categoria Identifier):

1. **Aggregate** `ContarReferencias`: fuente `Referencia`, filtro `Referencia.CategoriaId = CategoriaId`.
2. **If** `ContarReferencias.Count > 0`
   - Verdadero → **Raise Exception** (crear una *User Exception* `NoSePuedeEliminar`) con mensaje `"No se puede eliminar: la categoría tiene " + ContarReferencias.Count + " referencias asociadas."`
   - Falso → **DeleteCategoria** (`Id = CategoriaId`).

Repetir el patrón. La validación de cada una:

| Acción | Se bloquea si tiene… |
|---|---|
| EliminarCategoria | referencias |
| EliminarReferencia | SKU |
| EliminarTalla / EliminarColor | SKU |
| EliminarSku | lotes |
| EliminarBodega | zonas |
| EliminarZona | ubicaciones |
| EliminarUbicacion | movimientos |
| EliminarLote | movimientos o líneas de salida |
| EliminarSalida | estado distinto de *Solicitada* o *Cancelada* (las líneas se borran solas por la cascada) |

(Aunque el *Delete Rule = Protect* ya impide borrar, el mensaje de la base de datos es técnico; la validación propia da un mensaje claro al usuario. Esto se puede decir en la presentación.)

### 2.2 Botón en la pantalla
En la pantalla de detalle (p. ej. `CategoriaDetail`):
1. Arrastrar un **Button** junto a «Save», texto **Eliminar**, estilo `btn btn-error` (o `btn-danger`). Visible solo si el registro ya existe: `Visible = GetCategoriaById.List.Current.Categoria.Id <> NullIdentifier()`.
2. On Click → nueva Client Action **EliminarOnClick**:
   - Confirmación: un **Popup** con «¿Seguro que desea eliminar?» y botones Sí/No (variable local `MostrarConfirmacion`). Alternativa rápida: `JavaScript` con `$resolve(confirm('¿Eliminar la categoría?'))` y un If con el resultado.
   - Llamar `EliminarCategoria(CategoriaId)`.
   - **Message** (Success) «Categoría eliminada» → **Destination** a `Categorias` (la lista).
   - **Exception Handler** `NoSePuedeEliminar` (y `All Exceptions`) → **Message** (Error) con `ExceptionMessage`.

**Demostración:** eliminar «Prendas» → aparece el error (tiene 10 referencias). Crear una categoría «Prueba» → eliminarla → funciona.

---

## Parte 3 — Consultas adicionales (viernes–sábado)

Crear cada una como pantalla nueva en el grupo *Inventario*. Las primeras se hacen con **Aggregates** (sin escribir SQL); el kardex con saldo usa un nodo **SQL**.

### 3.1 Existencia por lote y ubicación (la consulta central)
En COLBASOFT la existencia **no se guarda**: se calcula sumando el kardex.
- Screen `Existencia` → Aggregate `GetExistencia`, fuentes: Movimiento, Lote, Sku, Referencia, Ubicacion, Zona (joins *Only With*).
- **Group By**: `Lote.Codigo`, `Sku.CodigoSku`, `Referencia.Descripcion`, `Zona.Nombre`, `Ubicacion.Codigo`.
- **Sum** de `Movimiento.Cantidad` → renombrar `Existencia`.
- Filtro de la Table: mostrar solo `Existencia > 0` (en el aggregate, filtro sobre el atributo calculado, o `Visible` de la fila; en O11 se puede filtrar el Sum directamente).
- Agregar un **Search** (Input + filtro `Referencia.Descripcion like "%" + Busqueda + "%" or Lote.Codigo like …`).

### 3.2 «¿Dónde está?»
Pantalla con un input de código de lote o de referencia → mismo aggregate de 3.1 filtrado por ese código. Responde «en qué ubicación está y cuánto hay».

### 3.3 Existencia por categoría (con gráfico)
Aggregate: Movimiento → Lote → Sku → Referencia → Categoria. Group By `Categoria.Nombre`, Sum de `Cantidad`.
Arrastrar un **Column Chart** (Charts) y en *SourceDataPointList* usar `ListAppendAll` mapeando `Label = Categoria.Nombre`, `Value = Existencia`.

### 3.4 Kardex de un lote con saldo acumulado (SQL)
Pantalla con dropdown de Lote. Server Action `ObtenerKardex(LoteId)` con un nodo **SQL** (crear una Structure `FilaKardex`: Fecha, Tipo, Ubicacion, Cantidad, Saldo, Responsable, Observacion):

```sql
SELECT {Movimiento}.[Fecha],
       {TipoMovimiento}.[Nombre],
       {Ubicacion}.[Codigo],
       {Movimiento}.[Cantidad],
       SUM({Movimiento}.[Cantidad]) OVER (ORDER BY {Movimiento}.[Fecha], {Movimiento}.[Id]) AS Saldo,
       {Movimiento}.[Responsable],
       {Movimiento}.[Observacion]
FROM {Movimiento}
INNER JOIN {TipoMovimiento} ON {TipoMovimiento}.[Id] = {Movimiento}.[TipoMovimientoId]
INNER JOIN {Ubicacion}      ON {Ubicacion}.[Id]      = {Movimiento}.[UbicacionId]
WHERE {Movimiento}.[LoteId] = @LoteId
ORDER BY {Movimiento}.[Fecha], {Movimiento}.[Id]
```
Parámetro `@LoteId` (Lote Identifier). Output Structure: `FilaKardex`.

### 3.5 Salidas por estado y fechas
Pantalla `ConsultaSalidas`: dropdown de `EstadoSalida` + dos Date Picker (desde/hasta) → Aggregate sobre Salida con filtros
`(EstadoFiltro = NullIdentifier() or Salida.EstadoSalidaId = EstadoFiltro) and Salida.Fecha >= Desde and Salida.Fecha <= Hasta`.
Mostrar también el total de líneas por salida (Group By `Salida.Numero`, Count de `LineaSalida.Id`).

### 3.6 (Opcional) Ocupación de ubicaciones
Por ubicación: Sum de existencia vs `Ubicacion.Capacidad`; marcar en rojo las que superan la capacidad y listar las vacías.

**Mínimo para la presentación:** 3.1, 3.2, 3.3 y 3.4.

---

## Orden de la demostración el lunes (≈10 min)
1. Diagrama de entidades: las 16 tablas y relaciones, Delete Rules (Protect vs cascada).
2. Recorrido por el menú: crear una referencia nueva con su categoría y unidad (dropdowns), crear un SKU.
3. Eliminar: intento bloqueado con mensaje claro → eliminación correcta → por qué Movimiento no tiene botón (kardex inmutable).
4. Consultas: existencia (calculada del kardex), «¿dónde está?», gráfico por categoría, kardex con saldo de un lote.

## Lo que el MVP deja fuera respecto a `colbasoft-app` (para responder si preguntan)
Bitácora encadenada por hash, confirmación por segunda persona, QR y escaneo, reservas con vencimiento, bloqueo por intentos fallidos. El MVP muestra el núcleo: catálogo → lotes → ubicaciones → kardex → existencia → salidas.
