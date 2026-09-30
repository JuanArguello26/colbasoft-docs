from patch_srs_lib import patch

NEWT = '''
# ------------------------------------------------------------------ v1.2: decisiones del 30-sep-2026 (IDs a continuación de GL-205)
T("Pieza", "Unidad física individual de mercancía dentro de un lote —rollo, paquete o bolsa, o contenedor agrupado— con cantidad propia registrada en la recepción e identidad interna en el sistema. Pertenece a un solo SKU + Lote y a una sola ubicación; el QR no la identifica: el operario la selecciona tras el escaneo.",
  "No es la unidad de inventario (que es SKU + Lote + Ubicación y agrupa piezas) ni tiene un QR propio.", "", "Inventario y existencia", "Decisiones Q-11, F-1, F-2, F-4, F-6 · SPEC v1.2 · CD-49", "Unidad de inventario; Lote; Rollo; Paquete o bolsa; Contenedor agrupado; Corte parcial", "Un rollo de 40 metros del lote L-2026-0142 en la ubicación A-03", True, v12=True)
T("Rollo", "Tipo de pieza propio de las referencias que se cuentan en metros o kilogramos; tiene cantidad propia y admite cortes parciales.",
  "No es un lote ni una referencia.", "", "Inventario y existencia", "Decisiones F-1, F-3 · SPEC v1.2 · CD-49", "Pieza; Corte parcial; Unidad de medida", "Rollo de tela de 40 m", v12=True)
T("Paquete o bolsa", "Tipo de pieza propio de las referencias que se cuentan en unidades; tiene cantidad propia de unidades.",
  "No es un contenedor agrupado ni una unidad de inventario.", "", "Inventario y existencia", "Decisión F-1 · SPEC v1.2 · CD-49", "Pieza; Contenedor agrupado; Unidad de medida", "Bolsa de 20 camisetas", v12=True)
T("Contenedor agrupado", "Contenedor rotulado que agrupa mercancía sin rotulado individual y se registra como una sola pieza con su cantidad de unidades; pertenece a un solo SKU + Lote (la mezcla de lotes está pendiente, HD-28).",
  "No es una entidad aparte del modelo: es un tipo de pieza.", "", "Inventario y existencia", "Decisión F-6 · SPEC PN-02 E-03 · SPEC v1.2 · CD-49", "Pieza; Paquete o bolsa; Identificador QR", "Caja con prendas sin etiqueta individual", v12=True)
T("Corte parcial", "Salida de una parte de una pieza —por ejemplo, metros cortados de un rollo—: descuenta la cantidad cortada y deja la pieza con su remanente y su identidad. Cumple las reglas de toda salida.",
  "No es un movimiento interno ni una división de la pieza en dos (HD-29).", "", "Salidas", "Decisión F-3 · RN-SAL-008 · SPEC v1.2", "Pieza; Rollo; Salida; Movimiento", "Cortar 6 metros de un rollo de 40 m y dejarlo con 34", v12=True)
'''
patch("gl_data.py", [
 ('def T(term, d, prohib, sin, ctx, origen, rel, ej="", ul=False, v11=False):', 'def T(term, d, prohib, sin, ctx, origen, rel, ej="", ul=False, v11=False, v12=False):'),
 ('    """v11=True: término agregado en la v1.1; recibe un GL-nnn a continuación de los de la v1.0, sin renumerar."""\n    TERMS.append(dict(term=term, d=d, prohib=prohib, sin=sin, ctx=ctx, origen=origen, rel=rel, ej=ej, ul=ul, v11=v11))',
  '    """v11=True: término agregado en la v1.1; v12=True: agregado en la v1.2. Reciben un GL-nnn a continuación de los anteriores, sin renumerar."""\n    TERMS.append(dict(term=term, d=d, prohib=prohib, sin=sin, ctx=ctx, origen=origen, rel=rel, ej=ej, ul=ul, v11=v11, v12=v12))'),
 ('T("Reimpresión", "Emisión de un identificador nuevo para reemplazar uno deteriorado o ilegible, con motivo; el nuevo hereda la trazabilidad y el anterior queda reemplazado. ⚠️ Su efecto sobre las demás copias impresas de un mismo QR de mercancía está pendiente (HD-25).", "No reutiliza el código anterior."',
  'T("Reimpresión", "Impresión de otra copia del mismo QR por deterioro o ilegibilidad, con motivo. Conserva el mismo identificador: no crea una nueva identidad ni cambia su estado, por lo que las demás copias del QR siguen válidas.", "No emite un código nuevo ni deja reemplazado el anterior (Q-09)."'),
 ('T("Unidad de manejo agrupada", "Contenedor rotulado que agrupa mercancía sin rotulado individual. Fuera del MVP: su gestión está en el Horizonte 3 del backlog (HD-22).", "No es una entidad del modelo del MVP."',
  'T("Unidad de manejo agrupada", "Término de la v1.0 para el contenedor rotulado que agrupa mercancía sin rotulado individual. Desde la v1.2 se modela como una pieza de tipo contenedor agrupado (HD-22 resuelto, F-6); su gestión avanzada sigue en el Horizonte 3.", "No es una entidad aparte del modelo del MVP."'),
])
s = open("gl_data.py", encoding="utf8").read().rstrip("\n") + "\n" + NEWT
open("gl_data.py", "w", encoding="utf8", newline="\n").write(s)
print("gl_data ok")
