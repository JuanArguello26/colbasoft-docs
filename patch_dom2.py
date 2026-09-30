from patch_srs_lib import patch

HD = ''' # --- v1.2: decisiones del 30-sep-2026
 ("HD-28", "Identidad física de la pieza, contenedores y reemplazo de identificadores (consecuencias de Q-11, F-6 y Q-09)",
  "Las decisiones del Director dan a la pieza identidad interna y cantidad propia, pero el QR sigue identificando SKU + Lote (DF5-01) y una reimpresión conserva el mismo QR (Q-09). Quedan sin definir: (1) cómo se distingue físicamente una pieza de otra del mismo lote, sin QR propio, más allá de seleccionarla en pantalla (F-4); (2) si un contenedor agrupado puede mezclar lotes o SKU (Q-08); (3) la diferencia entre «paquete o bolsa» (F-1) y «contenedor o bolsa agrupada» (F-6); (4) los motivos por los que un identificador se reemplaza o anula ahora que la reimpresión ya no lo reemplaza (el estado Reemplazado de SM-05 queda sin disparador).",
  "No se inventa ninguna respuesta. El modelo supone que todo contenedor pertenece a un solo SKU + Lote (RN-LOT-006) y conserva el estado Reemplazado de SM-05 sin disparador definido. La selección de la pieza en pantalla (RN-MOV-011) es el mecanismo vigente.",
  "Director — decidir · **Información requerida:** AS-IS (Q-08 y qué rotula hoy la empresa). No bloquea la Fase 5 por sí mismo"),
 ("HD-29", "Cortes parciales: destino del remanente y movimiento parcial de una pieza",
  "F-3 permite cortes parciales de rollos y RN-SAL-008 los trata como salida que deja la pieza con su remanente. No está decidido qué ocurre si el remanente se mueve a otra ubicación (¿sigue siendo la misma pieza?, ¿se divide?) ni si una pieza puede moverse solo en parte entre ubicaciones (HU-MOV-001 criterio 2 habla de cantidad total o parcial; con pieza, la cantidad parcial solo tiene sentido como corte).",
  "No se decide. El modelo solo admite el corte como salida (RN-SAL-008) y el movimiento interno de la pieza completa (RN-MOV-011); no define la división de una pieza en dos.",
  "Director — decidir · **Información requerida:** Q-04 (frecuencia y forma de los cortes). Decidir antes del detalle de movimientos de la Fase 5"),
 ("HD-30", "Alcance del control por pieza: ¿toda referencia se controla por piezas?",
  "F-1 define la pieza para referencias en metros, kilogramos y unidades, sin declarar excepciones; RN-LOT-006 exige registrar por piezas toda la mercancía recibida. Si una referencia llega suelta y sin pieza física distinguible, el modelo no dice cómo registrarla.",
  "No se decide. El modelo aplica la regla a toda la mercancía (RN-LOT-006) y registra un paquete, bolsa o contenedor agrupado como una pieza con su cantidad de unidades.",
  "Director — decidir · **Información requerida:** AS-IS (qué mercancía llega suelta). No bloquea la Fase 5 por sí mismo"),
]
'''
patch("dm_data.py", [
 ('''  "No se modela como entidad; queda como término del glosario marcado fuera del MVP.",
  "Director — confirmar"),''',
  '''  "**Resuelto en la v1.2 (Q-11 y F-6):** el contenedor agrupado entra al MVP como una pieza de tipo «contenedor agrupado» (E-27, VO-43); no se modela como entidad aparte. La mezcla de lotes en un contenedor sigue pendiente (HD-28).",
  "**Resuelto — Q-11 · F-6 (v1.2)**"),'''),
 ('''  "No se decide. SM-05 y RN-IDE-004 no cambian. Se analizan tres alternativas en `04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md` §2: (A) todas las etiquetas del lote comparten el QR; (B) QR de lote más identificador físico único por etiqueta; (C) el QR identifica un paquete físico, lo que revisa DF5-01.",
  "Director — **decidir antes de la Fase 5**; bloqueante mientras la alternativa C siga abierta · **Información requerida:** qué representa cada etiqueta física (rollo, pieza, bulto o lote), si un escaneo debe equivaler a una cantidad y qué trazabilidad física exige el proyecto"),''',
  '''  "**Resuelto el 30-sep-2026.** El Director decidió: Q-11 (la trazabilidad por pieza o rollo está dentro del MVP), F-1 y F-2 (pieza = rollo o paquete/bolsa, con cantidad propia registrada al recibir), F-3 (cortes parciales), F-4 (el operario selecciona la pieza tras el escaneo; la ubicación filtra), F-5 (conteo pieza por pieza), F-6 (contenedores y bolsas agrupadas), Q-09 (la reimpresión conserva el mismo QR) y Q-10 (el escaneo de salida verifica y cuenta). El modelo **mantiene DF5-01** (el QR identifica SKU + Lote) y agrega la **Pieza** (E-27, AG-22, VO-43, IN-73…IN-78); RN-IDE-004, IN-26, SM-05 y EV-QRC-004 se ajustan a Q-09. Queda como mezcla de las alternativas A y C del análisis del CP-04, sin revocar DF5-01. Pendientes derivados: HD-28, HD-29 y HD-30.",
  "**Resuelto — Q-11 · F-1…F-6 · Q-09 · Q-10 (v1.2)**"),'''),
 ('''  "Director — decidir · **Información requerida:** conectividad real de la bodega. No bloquea la Fase 5"),
]''',
  '''  "Director — decidir · **Información requerida:** conectividad real de la bodega. No bloquea la Fase 5"),
''' + HD.rstrip("\n") + "\n"),
 ('''   ("Activo", "Anulado", "EV-QRC-005", "Coordinador", "—")], "SPEC CD-08, PN-02"),''',
  '''   ("Activo", "Reemplazado", "—", "—", "⚠️ Sin disparador definido: los motivos de reemplazo distintos de la reimpresión son DECISIÓN PENDIENTE (HD-28)"),
   ("Activo", "Anulado", "EV-QRC-005", "Coordinador", "—")], "SPEC CD-08, PN-02"),'''),
])
print("dm_data findings ok")
