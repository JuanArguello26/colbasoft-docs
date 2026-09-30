from patch_srs_lib import patch

S09 = """
## 0.9 Control de cambios de la versión 1.2 (decisiones del 30 de septiembre de 2026)

Al auditar DEC-01 el Director tomó decisiones que resuelven **HD-25** y **HD-22** y agregan la trazabilidad por pieza al MVP. Esta versión las incorpora editando los datos fuente y regenerando los tres documentos; el SPEC v1.2 y el SRS v1.2 las recogen antes (`COLBASOFT_SPEC_v1.2.md`, `SRS_COLBASOFT_v1.2.md`).

| Decisión | Contenido | Cambios en el modelo |
|---|---|---|
| **DEC-01 = A** | Umbral aprobatorio: Núcleo, con 1 bodega piloto | Transferencias (E-13, AG-10) y conteo general quedan fuera del umbral aprobatorio, pero **siguen modelados**: el modelo no descarta nada del Horizonte 2 |
| **Q-11 · F-1 · F-2** | La trazabilidad por pieza o rollo está dentro del MVP; pieza = rollo o paquete/bolsa, con cantidad propia registrada al recibir | Entidad nueva **E-27 Pieza**; agregado **AG-22**; objeto de valor **VO-43**; reglas RN-LOT-006 y RN-LOT-007 → **IN-73** e **IN-74**; evento **EV-ENT-016**; subdominio SD-01; término «Pieza» y «Rollo», «Paquete o bolsa»; HD-25 resuelto |
| **F-3** | Cortes parciales | RN-SAL-008 → **IN-75**; eventos **EV-SAL-013**; término «Corte parcial»; nuevo HD-29 |
| **F-4** | Selección de la pieza tras el escaneo; la ubicación filtra | RN-MOV-011 → **IN-76**; EV-MOV-001, EV-INV-001 |
| **Q-10** | El escaneo de salida verifica y cuenta | RN-SAL-009 → **IN-77**; evento **EV-SAL-012** |
| **F-5** | Conteo manual pieza por pieza | RN-CNT-009 → **IN-78**; EV-CNT-007 |
| **F-6** | Contenedores y bolsas agrupadas | Tipo «contenedor agrupado» de VO-43; término «Contenedor agrupado»; «Unidad de manejo agrupada» se redefine; HD-22 resuelto; nuevo HD-28 |
| **Q-09** | La reimpresión conserva el mismo QR | RN-IDE-004 → **IN-26**; SM-05 (la reimpresión no cambia de estado; el estado «Reemplazado» queda sin disparador: HD-28); **EV-QRC-004** pasa a «Identificador QR reimpreso» (conserva su ID); término «Reimpresión» |
| Nivel | Ingeniería | Sin efecto en el modelo |

**Ningún ID se renumeró ni se reutilizó.** Los elementos nuevos continúan la numeración (E-27, VO-43, AG-22, IN-73…IN-78, EV-ENT-016, EV-SAL-012, EV-SAL-013, HD-28…HD-30, RF5-15, RF5-16 y los términos GL-206…GL-210). Las reglas del SRS pasan de 85 a 91; las seis nuevas (SPEC v1.2 §9.16) son invariantes. **Pendientes que la v1.2 deja abiertos** (no bloquean la Fase 5 por sí mismos): HD-28, HD-29 y HD-30.
"""

patch("build_f4.py", [
 ('FECHA = "28 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1)"', 'FECHA = "28 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) · 30 de septiembre de 2026 (v1.2)"'),
 ('| **Versión** | 1.1 |', '| **Versión** | 1.2 |'),
 ('| **Estado** | **Validado técnicamente** (cierre del CP-04, 29-sep-2026). **Aprobación funcional y académica pendiente**: HD-25 y DEC-01…DEC-09 sin responder (`04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md`) |',
  '| **Estado** | **Borrador v1.2** (30-sep-2026): incorpora la trazabilidad por pieza y resuelve HD-25. **Validación técnica pendiente** (verificadores). **Aprobación funcional y académica pendiente**: DEC-02…DEC-09 sin responder y acta de DEC-08 |'),
 ('COLBASOFT_SPEC v1.1 → SRS_COLBASOFT v1.1 → **Modelo de Dominio v1.1**', 'COLBASOFT_SPEC v1.2 → SRS_COLBASOFT v1.2 → **Modelo de Dominio v1.2**'),
 ('La v1.0 se conserva en el historial del repositorio (commit `79f823c`).\n"""',
  'La v1.0 se conserva en el historial del repositorio (commit `79f823c`).\n\n> **Versión 1.2.** Incorpora las decisiones del Director del 30 de septiembre de 2026 (DEC-01 = A, Q-11, F-1…F-6, Q-09 y Q-10), que agregan la **Pieza** al modelo y resuelven HD-25. El detalle está en DOMAIN_MODEL §0.9.\n"""'),
 ('el 0.6 muestra los rangos vigentes y el **0.8** registra los cambios de la v1.1.', 'el 0.6 muestra los rangos vigentes, el **0.8** registra los cambios de la v1.1 y el **0.9** los de la v1.2.'),
 ('| `E-nn` | Entidad | E-01…E-26 |', '| `E-nn` | Entidad | E-01…E-27 |'),
 ('| `VO-nn` | Objeto de valor | VO-01…VO-42 |', '| `VO-nn` | Objeto de valor | VO-01…VO-43 |'),
 ('| `AG-nn` | Agregado | AG-01…AG-21 |', '| `AG-nn` | Agregado | AG-01…AG-22 |'),
 ('(103 HU, 162 RF, 82 RN, 24 KPI)', '(103 HU, 162 RF, 82 RN, 24 KPI en la v1.0; 110 HU, 171 RF, 91 RN en la v1.2)'),
 ('Las reglas del SRS pasan de 82 a 85; las tres nuevas quedan separadas de las 82 originales (SPEC v1.1 §9.15).', 'Las reglas del SRS pasan de 82 a 85; las tres nuevas quedan separadas de las 82 originales (SPEC v1.1 §9.15).\n' + S09),
 # 5.3
 ('| Confirmar una entrada | AG-08 → AG-04, AG-06, AG-05, AG-07 | Lote, movimiento de entrada y existencia en recepción nacen juntos o no nace ninguno | RN-ENT-007, RN-LOT-001, RN-INT-004, RN-EXI-007 |',
  '| Confirmar una entrada | AG-08 → AG-04, AG-06, AG-05, AG-07, AG-22 | Lote, movimiento de entrada, existencia en recepción y piezas (v1.2) nacen juntos o no nace ninguno | RN-ENT-007, RN-LOT-001, RN-INT-004, RN-EXI-007, RN-LOT-006 |'),
 ('| Movimiento interno | AG-06 → AG-05 (origen) y AG-05 (destino) | La existencia total no cambia: el descuento y el incremento son indivisibles | RN-MOV-004 |',
  '| Movimiento interno | AG-06 → AG-05 (origen) y AG-05 (destino) | La existencia total no cambia: el descuento y el incremento son indivisibles | RN-MOV-004 |\n| Mover una pieza (v1.2) | AG-22 → AG-06, AG-05 (origen y destino) | La pieza cambia de ubicación con un movimiento; la suma de sus piezas sigue igualando la existencia de cada unidad de inventario | RN-LOT-007, RN-MOV-011 |\n| Corte parcial de una pieza (v1.2) | AG-22 → AG-09, AG-06, AG-05 | La cantidad de la pieza, el movimiento de salida y la existencia de la unidad cambian juntos o ninguno | RN-SAL-008, RN-LOT-007 |'),
 ('11 operaciones que involucran varios agregados', '13 operaciones que involucran varios agregados'),
 ('"Operaciones indivisibles sobre dos unidades (RF5-02) y concurrencia sobre la disponibilidad (RF5-03)",', '"Operaciones indivisibles sobre dos unidades (RF5-02), concurrencia sobre la disponibilidad (RF5-03) y coherencia pieza–unidad de inventario (RF5-15)",'),
 ('"HD-04 resuelto por DF5-01: la identidad de AG-05 no cambia; AG-07 identifica SKU + Lote", "5"))', '"HD-04 resuelto por DF5-01: la identidad de AG-05 no cambia; AG-07 identifica SKU + Lote; AG-22 agrega la pieza (v1.2)", "5"))'),
 # entidades estado
 ('"Bodega, Zona y SKU sin estados propios definidos en el SPEC (HD-19); copias impresas de un mismo QR de mercancía (HD-25)",', '"Bodega, Zona y SKU sin estados propios definidos en el SPEC (HD-19); identidad física de la pieza (HD-28)",'),
 ('HD-06 (resuelto, DF5-02), HD-11, HD-19, HD-23, HD-25", "3"))', 'HD-06 (resuelto, DF5-02), HD-11, HD-19, HD-23, HD-25 (resuelto, v1.2), HD-28", "3"))'),
 ('"HD-25 debe decidirse antes de la Fase 5 (04_CP04_DECISIONES_PENDIENTES); los demás pendientes no bloquean la arquitectura"', '"HD-25 y HD-22 resueltos en la v1.2; HD-28, HD-29 y HD-30 pendientes, sin bloquear la arquitectura por sí mismos"'),
 ('(82 + 3 de la v1.1: IN-70…IN-72)', '(82 + 3 de la v1.1 + 6 de la v1.2: IN-70…IN-78)'),
 # riesgos Fase 5
 (' ("RF5-14", "Qué identifica físicamente cada etiqueta de mercancía: copias de un QR de lote, etiqueta física única o paquete (HD-25)", "HD-25 · RN-IDE-004 · RN-SAL-004", "🔴", "Sin decidirlo no se sabe si un escaneo equivale a una cantidad, cómo se reimprime sin invalidar otras etiquetas ni si cambia la identidad de la mercancía"),',
  ' ("RF5-14", "Qué identifica físicamente cada etiqueta de mercancía (HD-25): resuelto en la v1.2 (la pieza tiene identidad interna; el QR sigue siendo SKU + Lote; la reimpresión conserva el QR). Queda cómo se distingue físicamente una pieza de otra del mismo lote (HD-28)", "HD-25 · HD-28 · RN-IDE-004 · RN-MOV-011", "🟡", "Sin distinguir físicamente las piezas del mismo lote la selección en pantalla depende por completo del operario"),\n ("RF5-15", "Coherencia entre la suma de las cantidades de las piezas y la existencia de la unidad de inventario (AG-22 ↔ AG-05): una operación sobre una pieza afecta a dos agregados", "IN-74 · RN-LOT-007 · RN-MOV-011", "🟠", "Existencia de la unidad de inventario distinta de la suma de sus piezas"),\n ("RF5-16", "Reserva y selección de piezas: la autorización reserva cantidad sobre la unidad de inventario (RN-EXI-003), pero las piezas se seleccionan recién al tomarlas (RN-SAL-009); dos preparaciones pueden apuntar a la misma pieza", "RN-SAL-009 · RN-EXI-003 · RN-EXI-004", "🟠", "Doble compromiso de una misma pieza en preparaciones distintas"),'),
 # glosario ids
 ('    base = sorted((x for x in TERMS if not x.get("v11")), key=sortkey)\n    nuevos = [x for x in TERMS if x.get("v11")]',
  '    base = sorted((x for x in TERMS if not x.get("v11") and not x.get("v12")), key=sortkey)\n    nuevos = [x for x in TERMS if x.get("v11")] + [x for x in TERMS if x.get("v12")]'),
 ('los agregados después (v11) continúan la numeración.', 'los agregados después (v11, v12) continúan la numeración.'),
 ('"HD-01, HD-14, HD-22", "2"))', '"HD-01, HD-14, HD-22 (resuelto, v1.2), HD-28", "2"))'),
 # auditoría interna
 ('| V-5 | Las {len(S["RN"])} reglas del SRS (82 + 3 de la v1.1) quedan', '| V-5 | Las {len(S["RN"])} reglas del SRS (82 + 3 de la v1.1 + 6 de la v1.2) quedan'),
 ('| V-7 | Historias con evento | 🟡 {hu_cov}/103 (el resto son de consulta) |', '| V-7 | Historias con evento | 🟡 {hu_cov}/110 (el resto son de consulta) |'),
 ('| V-8 | RF con evento | 🟡 {rf_cov}/162 (el resto son de consulta, restricción o presentación) |', '| V-8 | RF con evento | 🟡 {rf_cov}/171 (el resto son de consulta, restricción o presentación) |'),
 ('**Estado frente a la Fase 5 (v1.1).** El cierre del CP-04 resolvió HD-04, HD-06, HD-07, HD-23 y HD-24 (DF5-01, DF5-02, DF5-03, DF5-05). **HD-25** (qué identifica físicamente cada etiqueta) requiere una decisión antes de la Fase 5. HD-17, HD-26 y HD-27 requieren',
  '**Estado frente a la Fase 5 (v1.2).** El cierre del CP-04 resolvió HD-04, HD-06, HD-07, HD-23 y HD-24 (DF5-01, DF5-02, DF5-03, DF5-05); las decisiones del 30-sep-2026 resolvieron **HD-25** y **HD-22** (Q-11, F-1…F-6, Q-09, Q-10). **HD-28, HD-29 y HD-30** quedan pendientes, junto con HD-17, HD-26 y HD-27, que requieren'),
 ('*Fin de DOMAIN_MODEL v1.1.', '*Fin de DOMAIN_MODEL v1.2.'),
 ('*Fin de EVENT_CATALOG v1.1.*', '*Fin de EVENT_CATALOG v1.2.*'),
 ('*Fin de GLOSSARY v1.1.', '*Fin de GLOSSARY v1.2.'),
 ('HD-23…HD-27, RF5-14 y los términos GL-204 y GL-205', 'HD-23…HD-27, RF5-14 y los términos GL-204 y GL-205'),
])

patch("gl_data.py", [('"SPEC · PN-02 E-03", "Identificador QR")', '"SPEC · PN-02 E-03 · Decisión F-6 (v1.2)", "Identificador QR; Pieza; Contenedor agrupado")')])

# xref
patch("xref.py", [
 ('"SRS_COLBASOFT_v1.1.md"', '"SRS_COLBASOFT_v1.2.md"'),
 ('"COLBASOFT_SPEC_v1.1.md"', '"COLBASOFT_SPEC_v1.2.md"'),
 ('"CD": {f"CD-{i:02d}" for i in range(1, 49)}', '"CD": {f"CD-{i:02d}" for i in range(1, 50)}'),
])
print("ok")
