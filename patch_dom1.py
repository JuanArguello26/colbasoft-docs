from patch_srs_lib import patch

# ================================================================= dm_data.py
E27 = '''
 dict(id="E-27", nombre="Pieza", solicitado=None, cd="CD-49", sd="SD-01", ag="AG-22",
      desc="Unidad física individual de mercancía dentro de un lote —un rollo, un paquete o una bolsa, o un contenedor agrupado— con **cantidad propia registrada en la recepción** e identidad interna en el sistema `[Q-11]` `[F-1]` `[F-2]` `[F-6]`. Pertenece a un solo SKU + Lote y se encuentra en una sola ubicación. **El QR no la identifica**: identifica el SKU + Lote `[DF5-01]`; el operario la selecciona en pantalla después del escaneo y la ubicación filtra y verifica `[F-4]`.",
      resp="Conservar su cantidad propia y su tipo; permitir que un corte parcial la reduzca dejándola con su remanente; impedir que su cantidad supere lo que el kardex respalda o quede negativa; hacer posible la trazabilidad por pieza (qué, cuánto, dónde, quién, cuándo y por qué).",
      identidad="Identidad interna asignada por el sistema al registrarse la pieza (no es el QR de mercancía). ⚠️ Cómo se distingue físicamente una pieza de otra del mismo lote, sin QR propio, no está definido: HD-28.",
      info="Tipo de pieza (VO-43) · SKU + Lote · ubicación actual · cantidad actual (derivada del kardex) · documento de entrada de origen.",
      sm="— (sin estados propios; «sin cantidad» es una condición derivada)",
      ciclo="Nace en la recepción con su tipo y su cantidad; se ubica y se mueve por movimientos internos; su cantidad baja por cortes parciales y salidas; llega a cero sin desaparecer; nunca se elimina `[RN-MAE-007]`.",
      rel=[("E-04", "pertenece a exactamente 1 lote (y por él, a 1 SKU)"), ("E-07", "se encuentra en 1 ubicación"), ("E-08", "aporta su cantidad a la unidad de inventario de su SKU + Lote + ubicación"), ("E-11", "nace de 1 línea de un documento de entrada"), ("E-10", "es afectada por 1..n movimientos (su kardex)")],
      rn=["RN-LOT-006", "RN-LOT-007", "RN-SAL-008", "RN-MOV-011", "RN-SAL-009", "RN-CNT-009", "RN-MAE-007"]),
'''
VO43 = ' ("VO-43", "Tipo de pieza", "Clase física de una pieza.", "Uno de: rollo (referencias en metros o kilogramos), paquete o bolsa (referencias en unidades) o contenedor agrupado `[F-1]` `[F-6]`. Mezcla de lotes en un contenedor: DECISIÓN PENDIENTE (HD-28).", "Rollo · Bolsa · Contenedor agrupado", "RN-LOT-006"),\n'
AG22 = ' ("AG-22", "Pieza", "E-27", [], "La pieza tiene identidad, tipo y cantidad propias y es el nivel al que se selecciona, se corta y se cuenta (v1.2). Su cantidad cambia solo por movimientos confirmados y nunca puede quedar negativa ni superar lo que respalda el kardex. La coherencia entre la suma de las cantidades de sus piezas y la existencia de la unidad de inventario (AG-05) es una invariante entre agregados (RF5-15).", ["IN-73", "IN-74", "IN-75", "IN-76", "IN-77", "IN-78"], "E-04 Lote, E-07 Ubicación, E-08 Unidad de inventario (por identidad)"),\n'
IN_NEW = ''' # --- v1.2: decisiones del 30-sep-2026 (reglas nuevas del SPEC v1.2 §9.16)
 ("IN-73", "Toda mercancía recibida se registra por piezas: cada pieza pertenece a un solo SKU + Lote, tiene un tipo (rollo, paquete o bolsa, contenedor agrupado) y una cantidad propia registrada en la recepción; el QR no la identifica, tiene identidad interna.", ["RN-LOT-006"], "AG-22 / AG-08", "Estructural"),
 ("IN-74", "La existencia de una unidad de inventario es la suma de las cantidades de sus piezas en esa ubicación; la cantidad de una pieza solo cambia por un movimiento del kardex, y la cantidad recibida de una línea de entrada es la suma de sus piezas.", ["RN-LOT-007"], "AG-22 / AG-05 / AG-06", "Estructural"),
 ("IN-75", "Un corte parcial descuenta de la pieza solo la cantidad cortada y la deja con su remanente y su identidad; la cantidad cortada no supera la de la pieza; el corte es una salida y cumple las reglas de salida.", ["RN-SAL-008"], "AG-22 / AG-09", "Estructural"),
 ("IN-76", "Toda operación que mueve, toma o cuenta mercancía identifica la pieza afectada: tras el escaneo del SKU + Lote el operario selecciona la pieza, y la ubicación filtra y verifica qué piezas se ofrecen; no se confirma sin pieza seleccionada.", ["RN-MOV-011"], "AG-22 / AG-06", "Estructural"),
 ("IN-77", "En la preparación de una salida el escaneo verifica y cuenta: cada pieza tomada se cuenta una sola vez y la preparación no se confirma completa mientras falten piezas o cantidad solicitada, salvo salida parcial autorizada.", ["RN-SAL-009"], "AG-22 / AG-09", "Estructural"),
 ("IN-78", "El conteo es manual, pieza por pieza: el contador registra la cantidad de cada pieza sin ver la esperada, y la cantidad contada de la unidad de inventario es la suma de sus piezas.", ["RN-CNT-009"], "AG-12 / AG-22", "Estructural"),
]

# ================================================================== CICLOS DE VIDA (Cap. 7)'''

patch("dm_data.py", [
 ('modulos="M-13", entidades=["E-08"],', 'modulos="M-13", entidades=["E-08", "E-27"],'),
 ('("E-08", "se reparte en 1..n unidades de inventario"), ("E-09", "se identifica con 1 QR de mercancía activo (DF5-01)")],',
  '("E-08", "se reparte en 1..n unidades de inventario"), ("E-27", "se compone de 1..n piezas (v1.2)"), ("E-09", "se identifica con 1 QR de mercancía activo (DF5-01)")],'),
 ('**No tiene QR propio**: se identifica con el QR de su SKU + Lote más su ubicación `[DF5-01]`.",',
  '**No tiene QR propio**: se identifica con el QR de su SKU + Lote más su ubicación `[DF5-01]`. Su existencia es la suma de las cantidades de sus piezas `[RN-LOT-007]` (v1.2).",'),
 ('("E-09", "se identifica con el QR de su SKU + Lote junto con su ubicación (DF5-01)")],\n      rn=["RN-INT-004", "RN-INT-005",',
  '("E-09", "se identifica con el QR de su SKU + Lote junto con su ubicación (DF5-01)"), ("E-27", "agrupa las piezas de su SKU + Lote presentes en su ubicación (v1.2)")],\n      rn=["RN-LOT-007", "RN-INT-004", "RN-INT-005",'),
 ('ciclo="Se genera, se imprime, se activa al verificarse su legibilidad; puede ser reemplazado (reimpresión) o anulado; nunca se reutiliza. ⚠️ Copias impresas de un mismo QR de mercancía y su reimpresión: HD-25.",',
  'ciclo="Se genera, se imprime, se activa al verificarse su legibilidad; puede reimprimirse cuantas veces haga falta conservando el mismo QR y sin cambiar de estado `[Q-09]`; puede anularse; el reemplazo por otros motivos queda pendiente (HD-28); nunca se reutiliza.",'),
 ('conservar su historia al ser reemplazado;', 'conservar su historia al ser reemplazado o reimpreso;'),
 ("      rn=[\"RN-AUD-004\", \"RN-AJU-002\", \"RN-SAL-001\", \"RN-MOV-008\", \"RN-CNT-003\"]),\n", "      rn=[\"RN-AUD-004\", \"RN-AJU-002\", \"RN-SAL-001\", \"RN-MOV-008\", \"RN-CNT-003\"]),\n"),
 ('      rn=["RN-INT-003", "RN-MOV-006"]),\n]\n\n# ================================================================== OBJETOS DE VALOR',
  '      rn=["RN-INT-003", "RN-MOV-006"]),' + E27 + ']\n\n# ================================================================== OBJETOS DE VALOR'),
 ('"Al menos un criterio; no altera nada.", "Ajustes de septiembre 2026", "RN-AUD-002"),\n]',
  '"Al menos un criterio; no altera nada.", "Ajustes de septiembre 2026", "RN-AUD-002"),\n' + VO43 + ']'),
 ('Su regla central —un código se emite una sola vez en toda la vida del sistema y el reemplazo hereda la trazabilidad— es independiente',
  'Su regla central —un código se emite una sola vez en toda la vida del sistema y la reimpresión conserva el mismo QR— es independiente'),
 (' ("AG-21", "Cierre de jornada", "E-26", [], ', AG22.replace('\n','') + '\n ("AG-21", "Cierre de jornada", "E-26", [], '),
 (' ("IN-26", "El identificador que reemplaza a otro hereda íntegramente su trazabilidad; el reemplazado permanece consultable.", ["RN-IDE-004"], "AG-07", "Estructural"),',
  ' ("IN-26", "La reimpresión de un identificador conserva el mismo QR: produce otra copia del mismo código, no crea una nueva identidad ni cambia su estado, y queda consultable en el historial; los motivos de reemplazo de un identificador están pendientes (HD-28).", ["RN-IDE-004"], "AG-07", "Estructural"),'),
 ('\n]\n\n# ================================================================== CICLOS DE VIDA (Cap. 7)', '\n' + IN_NEW.replace(']\n\n# ================================================================== CICLOS DE VIDA (Cap. 7)', ']\n\n# ================================================================== CICLOS DE VIDA (Cap. 7)')),
 ('("E-09 Identificador QR", "**Generado** → impreso → **Activo** al verificarse su legibilidad → **Reemplazado** (reimpresión con herencia) o **Anulado**.", "Un código jamás vuelve a emitirse. El QR de mercancía identifica un SKU + Lote y no cambia al reubicar (DF5-01). ⚠️ Copias impresas y reimpresión: HD-25."),',
  '("E-09 Identificador QR", "**Generado** → impreso → **Activo** al verificarse su legibilidad → **Anulado**; la reimpresión conserva el mismo QR y lo deja **Activo** `[Q-09]`; el estado **Reemplazado** se conserva, pero sus motivos están pendientes (HD-28).", "Un código jamás vuelve a emitirse. El QR de mercancía identifica un SKU + Lote y no cambia al reubicar (DF5-01)."),\n ("E-27 Pieza", "Registrada en la recepción con su tipo y su cantidad → ubicada y movida por movimientos internos → su cantidad baja por cortes parciales y salidas → **sin cantidad** al llegar a cero.", "No tiene estados propios: «sin cantidad» es una condición derivada. Nunca se elimina `[RN-MAE-007]`. El movimiento parcial de una pieza entre ubicaciones y el destino del remanente de un corte parcial están pendientes (HD-29)."),'),
 ('("Reemplazado", "Sustituido por reimpresión; consultable", "final")', '("Reemplazado", "Sustituido por otro identificador (motivos pendientes, HD-28); consultable", "final")'),
 ('   ("Generado", "Reemplazado", "EV-QRC-004", "Coordinador", "Impresión ilegible (PN-02 E-01)"),\n   ("Activo", "Reemplazado", "EV-QRC-004", "Coordinador / Auxiliar", "Motivo de reimpresión (RN-IDE-004)"),\n',
  '   ("Activo", "Activo", "EV-QRC-004", "Coordinador / Auxiliar", "Reimpresión con motivo: otra copia del mismo QR, sin cambio de estado (RN-IDE-004, Q-09)"),\n   ("Generado", "Generado", "EV-QRC-004", "Coordinador", "Impresión ilegible: se imprime de nuevo el mismo QR (PN-02 E-01, RN-IDE-004)"),\n'),
])
print("dm_data ok")
