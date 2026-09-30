from patch_srs_lib import patch
ENT016 = 'E("EV-ENT-016", "Pieza registrada en la recepción", "Auxiliar", "E-11", "E-11, E-27", "Conteo físico de una pieza recibida (rollo, paquete, bolsa o contenedor agrupado) `[Q-11]` `[F-1]` `[F-2]` `[F-6]`", "Pieza con su tipo y su cantidad propia asociada a un SKU + Lote; la cantidad recibida de la línea es la suma de sus piezas; confirmación visible", rn="RN-LOT-006, RN-LOT-007", hu="HU-ENT-009, HU-ENT-010", rf="RF-ENT-014, RF-ENT-015, RF-ENT-016", crit="Alta", reg="Historial")\n'
SAL = ('E("EV-SAL-012", "Pieza tomada en la preparación", "Auxiliar", "E-12", "E-12, E-27", "Escaneo del SKU + Lote y selección de la pieza que se toma `[Q-10]` `[F-4]`", "La pieza se cuenta una sola vez en la preparación; el progreso muestra piezas y cantidad tomadas frente a lo solicitado", rn="RN-SAL-009, RN-MOV-011", hu="HU-SAL-008", rf="RF-SAL-012", crit="Media", reg="Historial")\n'
       'E("EV-SAL-013", "Corte parcial registrado", "Auxiliar", "E-12", "E-12, E-27, E-10", "Corte de parte de un rollo durante una salida `[F-3]`", "Cantidad cortada descontada de la pieza, que conserva su identidad y su remanente; salida con motivo tipificado, autorización y atribución personal", rn="RN-SAL-008, RN-LOT-007", hu="HU-SAL-009", rf="RF-SAL-013", crit="Alta", reg="Kardex")\n')
patch("ev_data.py", [
 ('"SKU + Lote confirmado que requiere identificación (un QR por SKU + Lote, DF5-01), o reimpresión"', '"SKU + Lote confirmado que requiere identificación (un QR por SKU + Lote, DF5-01)"'),
 ('E("EV-QRC-004", "Identificador QR reemplazado", "Coordinador / Auxiliar", "E-09", "E-09", "Reimpresión por deterioro o ilegibilidad, con motivo", "Nuevo identificador hereda la trazabilidad; el anterior queda Reemplazado",',
  'E("EV-QRC-004", "Identificador QR reimpreso", "Coordinador / Auxiliar", "E-09", "E-09", "Reimpresión por deterioro o ilegibilidad, con motivo `[Q-09]`", "Otra copia del mismo QR: el identificador no cambia de identidad ni de estado; la reimpresión queda en el historial",'),
 ('"Escaneo de mercancía, ubicación de origen si hay varias (DF5-01) y ubicación destino, con cantidad total o parcial; la primera ubicación desde la zona de recepción es EV-INV-001"',
  '"Escaneo de mercancía, selección de la pieza (la ubicación filtra y verifica, F-4), ubicación de origen si hay varias (DF5-01) y ubicación destino; la primera ubicación desde la zona de recepción es EV-INV-001"'),
 ('rn="RN-MOV-004, RN-MOV-005, RN-INT-002, RN-EXI-003", hu="HU-MOV-001", rf="RF-MOV-001, RF-MOV-002", crit="Alta", reg="Kardex")',
  'rn="RN-MOV-004, RN-MOV-005, RN-INT-002, RN-EXI-003, RN-MOV-011", hu="HU-MOV-001, HU-MOV-008", rf="RF-MOV-001, RF-MOV-002, RF-MOV-012", crit="Alta", reg="Kardex")'),
 ('rn="RN-MOV-010, RN-MOV-004, RN-EXI-002, RN-MOV-002, RN-MOV-001", hu="HU-ENT-006", rf="RF-BOD-004, RF-BOD-005, RF-MOV-001, RF-MOV-002, RF-MOV-005"',
  'rn="RN-MOV-010, RN-MOV-004, RN-EXI-002, RN-MOV-002, RN-MOV-001, RN-MOV-011", hu="HU-ENT-006, HU-MOV-008", rf="RF-BOD-004, RF-BOD-005, RF-MOV-001, RF-MOV-002, RF-MOV-005, RF-MOV-012"'),
 ('"Escaneo de ubicación y registro de la cantidad contada", "Existencia contada guardada sin mostrar la esperada; tarea Confirmada", kpi="KPI-03", rn="RN-CNT-002", hu="HU-CNT-002", rf="RF-CNT-006"',
  '"Escaneo de ubicación y registro de la cantidad de cada pieza contada a mano `[F-5]`", "Existencia contada guardada pieza por pieza sin mostrar la esperada; tarea Confirmada", kpi="KPI-03", rn="RN-CNT-002, RN-CNT-009", hu="HU-CNT-002, HU-CNT-010", rf="RF-CNT-006, RF-CNT-014"'),
 ('rn="RN-INT-001, RN-INT-002, RN-INT-004", hu="HU-KDX-001", rf="RF-KDX-001, RF-KDX-002, RF-KDX-003", crit="Alta", reg="Kardex")',
  'rn="RN-INT-001, RN-INT-002, RN-INT-004, RN-LOT-007", hu="HU-KDX-001, HU-KDX-006", rf="RF-KDX-001, RF-KDX-002, RF-KDX-003, RF-KDX-008", crit="Alta", reg="Kardex")'),
 ('E("EV-SAL-011", "Salida cancelada",', SAL + 'E("EV-SAL-011", "Salida cancelada",'),
 ('# ---------------------------------------------------------------- LOT', ENT016 + '# ---------------------------------------------------------------- LOT'),
 ('("EV-ENT-004", "una vez por línea"),', '("EV-ENT-004", "una vez por línea"), ("EV-ENT-016", "por cada pieza de la línea"),'),
 ('("EV-SAL-010", ""), ("EV-SAL-005", "por cada escaneo incorrecto"),', '("EV-SAL-010", ""), ("EV-SAL-012", "por cada pieza tomada"), ("EV-SAL-013", "si se corta parte de un rollo"), ("EV-SAL-005", "por cada escaneo incorrecto"),'),
])
print("ev_data ok")
