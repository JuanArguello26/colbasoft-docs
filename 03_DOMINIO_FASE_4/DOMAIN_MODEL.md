# DOMAIN_MODEL
## Modelo de Dominio de COLBASOFT

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | DOMAIN_MODEL |
| **Versión** | 1.1 |
| **Fase** | Fase 4 del proyecto — Modelo de Dominio (Checkpoint CP-04) |
| **Fecha** | 28 de septiembre de 2026 (v1.0) · 29 de septiembre de 2026 (v1.1) |
| **Estado** | **Validado técnicamente** (cierre del CP-04, 29-sep-2026). **Aprobación funcional y académica pendiente**: HD-25 y DEC-01…DEC-09 sin responder (`04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md`) |
| **Jerarquía documental** | Monografía → Auditoría Fundacional → COLBASOFT_SPEC v1.1 → SRS_COLBASOFT v1.1 → **Modelo de Dominio v1.1** (DOMAIN_MODEL · EVENT_CATALOG · GLOSSARY) |
| **Documentos hermanos** | `EVENT_CATALOG.md` (eventos, matrices D y E) · `GLOSSARY.md` (glosario y auditoría interna) |
| **Autoría del proyecto** | Juan Esteban Argüello · Brayan Alexander Osorio · Brandon José Guerrero |
| **Institución / asesor** | Escuela de Ingeniería — CIAF · Edwin Andrés Cabrera Arredondo |
| **Fuera de alcance** | Arquitectura, modelo de datos, tecnologías, interfaces de integración, notaciones de diseño y código: pertenecen a la Fase 5 y posteriores |

> **Naturaleza.** Este documento es **derivado**: no modifica la monografía, la auditoría, el SPEC ni el SRS. Modela el negocio que esos documentos describen. Toda diferencia entre ellos o frente al Prompt Maestro #004 se registra como **Hallazgo del Dominio (HD-nn)**; no se corrige en silencio.

> **Versión 1.1.** Incorpora las decisiones del cierre del CP-04 (DF5-01, DF5-02, DF5-03, DF5-05 y DF5-06), registradas en `04_CP04_AUDITORIA/04_CP04_CIERRE.md`. El detalle de los cambios está en DOMAIN_MODEL §0.8. La v1.0 se conserva en el historial del repositorio (commit `79f823c`).

## Índice

| Cap. | Título |
|---|---|
| 0 | Auditoría de reanudación |
| 1 | Lenguaje ubicuo |
| 2 | Subdominios |
| 3 | Entidades del dominio |
| 4 | Objetos de valor |
| 5 | Agregados |
| 6 | Invariantes del dominio (y políticas) |
| 7 | Ciclos de vida |
| 8 | Estados oficiales |
| 9 | Matrices A, B y C |
| 10 | Hallazgos del dominio |

---

# CAPÍTULO 0 — AUDITORÍA DE REANUDACIÓN

> Reconstrucción del contexto ejecutada **antes** de escribir los tres documentos de la Fase 4. Es común a DOMAIN_MODEL, EVENT_CATALOG y GLOSSARY. Los apartados 0.1 a 0.5 y 0.7 conservan la reconstrucción de la v1.0 (28-sep-2026) como registro histórico; el 0.6 muestra los rangos vigentes y el **0.8** registra los cambios de la v1.1.

## 0.1 Estado del proyecto

| Dimensión | Estado verificado |
|---|---|
| **Monografía** | Congelada. El archivo `MONOGRAFÍA  COLBASOFT.docx` no fue modificado. |
| **Auditoría Fundacional** | Aprobada (Fase 0). |
| **COLBASOFT_SPEC v1.0** | Aprobado según los Prompts #003 y #004; el archivo conserva la leyenda «Emitido para revisión del Director». |
| **SRS_COLBASOFT v1.0** | Declarado aprobado por el Prompt #004. **El archivo sigue en «Emitido para revisión del Director» y sus 9 decisiones DEC-01…DEC-09 no tienen respuesta registrada** (HD-21). |
| **Fase en curso** | Fase 4 — Modelo de Dominio. Sin arquitectura, datos, tecnologías ni código. |
| **Carpeta del proyecto** | `00_MONOGRAFIA_ORIGINAL/`, `00_AUDITORIA_FASE_0/`, `01_SPEC_FASE_2/`, `02_SRS_FASE_3/`; esta fase agrega `03_DOMINIO_FASE_4/`. No se recibieron documentos nuevos. |

## 0.2 Checkpoints existentes

El proyecto no conserva documentos de checkpoint independientes; el Prompt #004 se refiere a «CP-03». La secuencia se reconstruye así (inferida de las fechas y del estado de cada entregable):

| Checkpoint | Hito | Documento | Fecha | Estado |
|---|---|---|---|---|
| **CP-00** | Auditoría fundacional | `AUDITORIA_FUNDACIONAL_COLBASOFT.md` | 1-sep-2026 | ✅ Cerrado |
| **CP-01** | Constitución del proyecto: decisiones DC-01…DC-08 | Registradas en el SPEC §0.1 | antes del 5-sep-2026 | ✅ Cerrado parcialmente (19 de 24 preguntas bloqueantes) |
| **CP-02** | Especificación funcional | `COLBASOFT_SPEC_v1.0.md` | 5-sep-2026 | ✅ Cerrado |
| **CP-03** | Especificación de requisitos | `SRS_COLBASOFT_v1.0.md` | 28-sep-2026 | ✅ Cerrado por instrucción del Prompt #004 (con DEC abiertas) |
| **CP-04** | **Modelo de dominio** | `DOMAIN_MODEL.md` · `EVENT_CATALOG.md` · `GLOSSARY.md` | 28-sep-2026 | 🟡 Emitido (este entregable) |

## 0.3 Documentos recibidos y uso en esta fase

| # | Documento | Versión | Qué aporta al dominio |
|---|---|---|---|
| 1 | Monografía original | Única, inmutable | Problema, objetivos (OG, OE-1…OE-3), cinco conceptos formales (§7.1), indicadores de §8.2, términos consagrados («ruptura de stock», «sobre stock») |
| 2 | Auditoría Fundacional | Fase 0 | Vacíos (C.1.4 trazabilidad, C.1.7 modelo de dominio), problemas P-01…P-24, reglas innegociables |
| 3 | COLBASOFT_SPEC v1.0 | v1.0 | **Fuente principal del vocabulario**: 48 conceptos (CD-01…CD-48), vocabulario controlado (§0.5), 14 procesos (PN), 20 módulos, reglas, KPI, principios de rol |
| 4 | SRS_COLBASOFT v1.0 | v1.0 | IDs permanentes (HU, RF, RNF, RN), 82 reglas por dominio, 24 casos de uso, trazabilidad, hallazgos H-01…H-18, decisiones DEC-01…DEC-09 |

## 0.4 Decisiones constitucionales detectadas

**Reglas Innegociables (Auditoría):** RI-1 la monografía no se modifica · RI-2 no eliminar conceptos esenciales · RI-3 no inventar funcionalidades · RI-4 no escribir código · RI-5 no crear arquitectura · RI-6 no cambiar objetivos sin justificar · RI-7 todo hallazgo cita su origen.

**Decisiones del Director (SPEC §0.1):**

| # | Decisión | Consecuencia en el modelo de dominio |
|---|---|---|
| DC-01 | Empresa de estudio sin nombre | Los ejemplos del dominio son ilustrativos y anónimos |
| DC-02 | Alcance MVP cerrado (inventario y logística de bodega) | 15 subdominios, todos dentro de la bodega |
| DC-03 | Sin ventas, compras completas, producción, contabilidad, nómina, CRM ni facturación | Ninguna entidad comercial: el documento de entrada no es orden de compra; la salida no es venta; no hay atributo monetario (HD-09) |
| DC-04 | Cinco roles oficiales | VO-36 Rol con cinco valores; el Sistema es actor, no rol (HD-12) |
| DC-05 | Web responsive + tablet | Notificaciones dentro del sistema web; escaneo con cámara |
| DC-06 | Integración con Power BI; sin tableros analíticos | La herramienta analítica es externa al dominio |
| DC-07 | Sin IA: «inteligente» = reglas + analítica | Los eventos derivados provienen solo de reglas y umbrales |
| DC-08 | QR como identificador principal | Agregado AG-07 Identificador QR; código de barras solo consulta |

**Resumen constitucional del Prompt #004 frente al baseline:** coincide en roles, plataforma, QR e inteligencia por reglas y KPI. Como en el SRS, prevalece la exclusión más estricta: se excluye **toda** IA (DC-07), no solo la generativa, y también la contabilidad (DC-03). Los nombres de entidad que pide el prompt («Producto», «Variante», «Área», «Inventario», «Auditoría») se concilian con el vocabulario del SPEC en HD-01.

## 0.5 Riesgos abiertos heredados del SRS

| ID | Riesgo | Sev. | Efecto sobre el dominio |
|---|---|:--:|---|
| **R-S01** | El SRS se emitió antes del levantamiento AS-IS y de la línea base | 🔴 | El modelo de dominio tampoco está contrastado con la operación real: es un modelo **TO-BE** |
| R-S02 | Mapeos `[SRS]` sin validar por el Director | 🟠 | Las matrices D y E se construyen sobre esos IDs |
| R-S03 | Alcance grande para nivel Tecnólogo | 🟠 | 26 entidades y 165 eventos amplían la superficie |
| R-S04 | Tensión DC-02 / Horizonte 2 (DEC-01) | 🟠 | Transferencias y conteo general se modelan completos |
| R-S05 | Reglas y KPI sin requisito de captura; PN-14 sin requisitos | 🟠 | Eventos marcados «sin RF» (Cap. 2 del EVENT_CATALOG) |
| R-S06 | Dos cifras de reglas (68 y 82) | 🟡 | El dominio usa las 82 |
| R-S07 | Valores numéricos de RNF sin calibrar | 🟡 | No afecta al dominio |
| R-S08 | Ambigüedad «estructural / configurable» (DEC-04) | 🟠 | IN-67 adopta la interpretación del SRS |
| R-S09 | Gherkin no valida adopción | 🟠 | No afecta al dominio |
| R-S10 | Cifras de fuentes no verificadas | 🟠 | El dominio no usa cifras de la literatura |

**Decisiones del Director aún abiertas (SRS, Anexo C):** DEC-01 umbral aprobatorio · DEC-02 lista de alcance · DEC-03 cifra y renumeración de reglas · DEC-04 semántica estructural/configurable · DEC-05 cierre de jornada · DEC-06 brechas de trazabilidad · DEC-07 valorización · DEC-08 aprobación formal del SPEC · DEC-09 fecha límite de lote. Cada una que toca el dominio se marca ⚠️ donde aplica.

**Riesgos críticos heredados del SPEC:** adopción (RG-01, RG-02, RG-13, RG-14, RG-16, RG-17, RG-23) y evidencia académica (RG-33…RG-36).

## 0.6 Convenciones de esta fase

| Prefijo | Elemento | Rango en esta versión |
|---|---|---|
| `SD-nn` | Subdominio | SD-01…SD-15 |
| `E-nn` | Entidad | E-01…E-26 |
| `VO-nn` | Objeto de valor | VO-01…VO-42 |
| `AG-nn` | Agregado | AG-01…AG-21 |
| `IN-nn` | Invariante | IN-01…IN-72 |
| `PO-nn` | Política del dominio (regla reactiva) | PO-01…PO-14 |
| `SM-nn` | Máquina de estados | SM-01…SM-21 |
| `EV-<DOM>-nnn` | Evento de dominio | 20 dominios, 165 eventos |
| `GL-nnn` | Término del glosario | GL-001…GL-205 |
| `HD-nn` | Hallazgo del dominio | HD-01…HD-27 |
| `RF5-nn` | Riesgo abierto para la Fase 5 | RF5-01…RF5-14 |

Los IDs de esta fase son **permanentes**: no se reutilizan ni se renumeran. Las reglas, historias y requisitos se citan con los IDs permanentes del SRS (`RN-<DOM>-nnn`, `HU-<DOM>-nnn`, `RF-<DOM>-nnn`); los procesos, conceptos y KPI, con los del SPEC.

## 0.7 Método

1. Se releyeron los cuatro documentos y se reutilizó la extracción estructurada del SRS (103 HU, 162 RF, 82 RN, 24 KPI).
2. Entidades, objetos de valor, agregados, invariantes, estados, eventos y términos se escribieron como datos únicos, y de ellos se generaron los tres documentos y las cinco matrices. **Una definición aparece una sola vez**: el Cap. 1 (lenguaje ubicuo) y el GLOSSARY usan el mismo texto.
3. Se verificó automáticamente que toda referencia a RN, HU, RF, KPI, evento, entidad e invariante exista (0 referencias rotas).

## 0.8 Control de cambios de la versión 1.1 (cierre del CP-04)

La auditoría del CP-04 (`04_CP04_AUDITORIA/04_CP04_AUDITORIA.md`) encontró que la identidad del QR (HD-04) contradecía RN-INT-005, que la primera ubicación cambiaba la existencia de unidad sin movimiento (HD-23) y que no estaba definido qué pasa con un registro sin conectividad que deja de ser válido (HD-24). El 29 de septiembre de 2026 se tomaron las decisiones siguientes, que esta versión incorpora editando los datos fuente y regenerando los tres documentos:

| Decisión | Contenido | Cambios en el modelo |
|---|---|---|
| **DF5-01** | El QR de mercancía identifica **SKU + Lote**; no identifica ubicación, bodega ni cantidad. La unidad de inventario sigue siendo SKU + Lote + Ubicación | E-04, E-08, E-09, AG-07, VO-07, VO-08, IN-23, IN-25; eventos EV-QRC-001, EV-QRC-003; términos «Identificador QR», «Unidad de inventario», «Identificador secundario»; HD-04 resuelto; nuevos HD-25 y HD-26 (pendientes, no bloqueantes) |
| **DF5-02** | La entrada confirmada queda **En recepción**; pasa a Disponible al ubicarse | Regla RN-EXI-007 → **IN-70**; SM-06; E-11; EV-ENT-012; HD-06 y HD-07 resueltos |
| **DF5-03** | La primera ubicación es un **movimiento interno** en el kardex | Regla RN-MOV-010 → **IN-71**; E-08, E-10, VO-21; SM-06 (nuevas transiciones En recepción → En tránsito y En tránsito → En recepción, esta última por PN-06 E-07); EV-INV-001 conserva ID y nombre y pasa a designar ese movimiento; Cap. 5.3; término nuevo «Primera ubicación»; HD-23 |
| **DF5-05** | Un registro retenido se **valida de nuevo** al sincronizar; si ya no es válido se rechaza con constancia y, si describe un hecho físico, abre una novedad | Regla RN-INT-008 → **IN-72**; SM-07 (estado nuevo «Rechazado en sincronización»); evento nuevo **EV-TRZ-007**; EV-TRZ-004, EV-NOV-001, E-10, E-17, AG-13, VO-32; término nuevo «Rechazado en sincronización»; HD-24; nuevo HD-27 (alcance sin conectividad, pendiente) |
| **DF5-06** (revisada) | Validación técnica del SPEC, el SRS y este modelo en su v1.1; la aprobación funcional y académica queda pendiente de HD-25 y DEC-01…DEC-09 | Portadas; HD-21; HD-25 |

**Ningún ID se renumeró ni se reutilizó.** Los elementos nuevos continúan la numeración (IN-70…IN-72, EV-TRZ-007, HD-23…HD-27, RF5-14 y los términos GL-204 y GL-205). Las reglas del SRS pasan de 82 a 85; las tres nuevas quedan separadas de las 82 originales (SPEC v1.1 §9.15).

**ESTADO: CONTEXTO RECONSTRUIDO.**

---

**ESTADO DEL CAPÍTULO — 0**

| | |
|---|---|
| **Completado** | Estado del proyecto · 5 checkpoints · 4 documentos · 8 decisiones constitucionales + 7 reglas innegociables · 10 riesgos del SRS · 9 decisiones abiertas |
| **Riesgos** | R-S01 (modelo TO-BE sin contraste con la operación real) |
| **Dependencias** | SRS v1.1 (IDs y reglas) |
| **Hallazgos** | HD-21 (el SRS figura como emitido, no aprobado; atendido en parte por DF5-06) |

---

# CAPÍTULO 1 — LENGUAJE UBICUO

> Vocabulario oficial del dominio: se usa **sin sinónimos** en documentos, conversaciones, pruebas e interfaz (SPEC §0.5, RNF-USA-006). Este capítulo contiene los **54 términos centrales**; el GLOSSARY contiene los 205 términos oficiales con idéntica definición.

## 1.1 Reglas del lenguaje

1. **Un concepto, un término.** Los sinónimos prohibidos no se usan ni como explicación.
2. **El término del SPEC prevalece.** Si el SPEC define un concepto (CD-nn), su nombre es el oficial aunque otro documento use otro.
3. **Los nombres pedidos por el Prompt #004 se concilian, no se sustituyen** (HD-01):

| Nombre pedido en el Prompt #004 | Término oficial | Por qué |
|---|---|---|
| Producto | **Referencia** (E-01) | En el SPEC «producto» designa a COLBASOFT; el objeto físico es la **Prenda** (CD-01) y el de catálogo es la Referencia (CD-02) |
| Variante | **SKU** (E-02) | CD-05 ya nombra la combinación referencia + talla + color |
| Área | **Zona** (E-06) | CD-13; «área» no es término del SPEC |
| Inventario | **Unidad de inventario** (E-08) | CD-07; «inventario» es el conjunto, no la entidad controlada |
| Auditoría | **Registro de bitácora** (E-21) + **Observación de auditoría** (E-22) | CD-47 y RN-AUD-002; «auditoría» es el proceso PN-13 |
| «Stock mínimo alcanzado» | **Existencia mínima alcanzada** (EV-INV-006) | «stock» está prohibido como sinónimo de existencia (§0.5) |

4. **Los términos consagrados de la monografía se conservan con su sentido.** «Ruptura de stock» y «sobre stock» nombran condiciones (Monografía §3) y no autorizan usar «stock» por «existencia».
5. **Origen.** Cada término declara dónde nace: Monografía, Auditoría, SPEC, SRS o «Nuevo (Fase 4)».


## 1.2 Catálogo textil

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Prenda** | Artículo textil terminado o insumo textil que la empresa almacena. Es el objeto físico del que hablan las personas; el sistema no lo controla directamente sino a través de su Referencia y de sus unidades de inventario. | Una camiseta azul talla M en un estante | — | SPEC · CD-01 · Monografía §5, §7.1 |
| **Referencia** | Identificador comercial de un modelo o artículo textil, independiente de talla, color y lote. Es la unidad de catálogo; se activa y desactiva, nunca se elimina. | CAM-001 · camiseta cuello redondo | producto (designa a COLBASOFT, HD-01), modelo, estilo, artículo | SPEC · CD-02 |
| **Talla** | Dimensión de variación de una referencia que expresa el tamaño; toma valores de un conjunto definido por la empresa. | M; 10; XL | — | SPEC · CD-03 |
| **Color** | Dimensión de variación de una referencia que expresa el acabado cromático; toma valores de un conjunto definido por la empresa. | Azul; Crudo | — | SPEC · CD-04 |
| **SKU** | Combinación única e irrepetible de Referencia + Talla + Color. Unidad de control de catálogo con la que se planifica, se consulta y se fijan los umbrales mínimo y máximo. No tiene existencia propia: su existencia es la suma de sus unidades de inventario. | CAM-001 · M · Azul | variante (HD-01), ítem | SPEC · CD-05 |
| **Categoría** | Agrupación de referencias con propósito de organización, zona preferente y reporte. Una referencia pertenece a una sola categoría. | Camisetas | familia, línea | SPEC · CD-10 |
| **Unidad de medida** | Magnitud en que se cuenta una referencia (unidades, metros, rollos, kilogramos). Es fija por referencia y no cambia si existen movimientos; el dominio no convierte entre unidades. | metros (tela en rollo) | — | SPEC · CD-11 |

## 1.3 Trazabilidad

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Lote** | Conjunto de mercancía de un mismo SKU que ingresó en un mismo evento de entrada y comparte origen y condiciones. Permite rastrear un problema hasta su procedencia y se inmoviliza y libera como un todo. | L-2026-0142 de CAM-001 · M · Azul | partida, tanda | SPEC · CD-06 · Monografía §7.1 |
| **Anulación** | Movimiento inverso que neutraliza el efecto de un movimiento previo erróneo; no borra el original: ambos permanecen en el kardex. Requiere motivo y autorización. | Anulación de una entrada registrada por duplicado | reversión, borrado, eliminación | SPEC · CD-34 |
| **Kardex** | Registro cronológico, completo e inmutable de todos los movimientos de una unidad de inventario desde su creación. Es la fuente de verdad de la existencia: la existencia se deriva del kardex, nunca al revés. | Línea: 2026-10-05 09:42 · Entrada · +120 · 120 · Z0-R01 · Coordinador A · DE-0087 | log, historial (de inventario), libro | SPEC · CD-37 · Monografía §7.1, §8.2 |
| **Trazabilidad** | Capacidad de responder, para cualquier unidad de inventario y cualquier momento pasado, qué es, cuánto había, dónde estaba, quién la movió, cuándo y por qué. Es retrospectiva y completa, desde la entrada hasta la salida de bodega. | ¿Quién movió el lote L-2026-0142 a cuarentena y por qué? | rastreo (como alcance mayor) | SPEC · CD-21 · Monografía §2, §6, §7.1 |

## 1.4 Ubicaciones

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Bodega** | Ámbito físico mayor donde se almacena inventario y ámbito de responsabilidad de un Jefe de Bodega; contiene zonas y al menos una zona de recepción. | Bodega Principal | almacén (como sinónimo), depósito | SPEC · CD-12 |
| **Zona** | Subdivisión de una bodega con propósito operativo: recepción, almacenamiento, preparación de salida o cuarentena. Agrupa ubicaciones y puede tener un Coordinador responsable. | Zona Z2 · Almacenamiento | área (HD-01), sector, pasillo | SPEC · CD-13 |
| **Ubicación** | Posición física identificable dentro de una zona donde reside mercancía; tiene QR propio, capacidad y estado. Es el nivel mínimo de precisión espacial; toda existencia disponible reside en una. | Z2-E03-N2 (zona 2, estante 3, nivel 2) | posición, casilla, celda, slot, hueco | SPEC · CD-14 |
| **Capacidad de ubicación** | Cantidad máxima que admite una ubicación, expresada en la unidad configurada; se usa para proponer destinos y alertar sobreocupación. | 200 unidades | cupo | SPEC · CD-15 |
| **Zona de recepción** | Zona donde permanece la mercancía entre su llegada y su ubicación definitiva; su existencia está en el inventario pero no está disponible. Toda bodega tiene al menos una, y toda zona de recepción tiene al menos una ubicación. | Zona Z0 · Recepción | muelle, andén (como sinónimos) | SPEC · CD-16 |
| **Zona de cuarentena** | Zona donde reside mercancía inmovilizada: dañada, en verificación o pendiente de decisión. Su existencia no es disponible. | Zona ZQ · Cuarentena | zona de rechazos | SPEC · CD-17 |

## 1.5 Inventario y existencia

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Unidad de inventario** | La entidad que COLBASOFT controla: la combinación SKU + Lote + Ubicación. Nivel al que se registra existencia, se ejecutan movimientos y se lleva kardex. No tiene QR propio: se identifica con el QR de su SKU + Lote más su ubicación. | CAM-001 · M · Azul · L-2026-0142 · Z2-E03-N2 | inventario (como entidad, HD-01), ítem, artículo | SPEC · CD-07 |
| **Existencia** | Cantidad de una unidad de inventario presente en el sistema en un momento dado; siempre es la suma algebraica de sus movimientos confirmados, nunca un valor ingresado directamente. | 40 unidades | stock, saldo, disponible (como sustantivo genérico) | SPEC · CD-18 · Monografía §7.1 |
| **Inventario disponible** | Porción de la existencia que puede comprometerse para una salida o transferencia: existencia menos reservado, inmovilizado, en tránsito y en recepción. Es la cifra que el operario ve por defecto. | 25 de 40 | stock libre | SPEC · CD-19 |
| **Inventario reservado** | Porción de la existencia comprometida por una salida autorizada o una transferencia creada, aún no ejecutada. Sigue en la bodega pero no puede comprometerse otra vez. | 10 de 40 | apartado | SPEC · CD-20 |
| **Inventario inmovilizado** | Porción de la existencia que existe físicamente pero no puede moverse ni salir sin autorización expresa: dañada, en verificación, bloqueada o en cuarentena. | 5 de 40 | bloqueado (como sustantivo), congelado | SPEC · CD-22 |
| **Inventario en tránsito** | Existencia que salió de una ubicación origen y aún no se confirmó en su destino; no está disponible en ninguna de las dos y tiene plazo máximo. | Despachado de Z1, sin recibir en Z3 | en camino | SPEC · CD-23 |
| **Estado de inventario** | Condición de una porción de existencia que determina qué puede hacerse con ella: Disponible, Reservado, En tránsito, Inmovilizado o En recepción; mutuamente excluyentes para una misma cantidad. | Reservado | estatus de stock | SPEC · CD-44 |

## 1.6 Identificación

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Identificador QR** | Código único generado por el sistema, asociado a un SKU + Lote (QR de mercancía) o a una ubicación (QR de ubicación); medio primario de interacción del operario. El de mercancía no identifica ubicación, bodega ni cantidad, y no cambia al reubicar. Es de un solo uso: nunca se repite ni se reutiliza. Estados: generado, activo, reemplazado, anulado. | Etiqueta impresa con QR y texto legible «CAM-001 · M · Azul · L-2026-0142» | etiqueta (como sinónimo del código), código de barras | SPEC · CD-08 · DC-08 · DF5-01 |
| **Identificador secundario** | Código de barras u otro código externo asociado a mercancía; admitido para consulta, nunca para escritura, y asociado a lo sumo a un QR de mercancía (un SKU + Lote). | Código de barras del proveedor | — | SPEC · CD-09 · DC-08 |

## 1.7 Movimientos

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Movimiento** | Hecho registrado que altera la existencia o la ubicación de una unidad de inventario. Unidad transaccional del sistema; inmutable una vez confirmado. Nada cambia en el inventario sin un movimiento. | Movimiento interno de 5 unidades de Z2-E03-N2 a Z2-E04-N1 | transacción, registro, apunte | SPEC · CD-28 · Monografía §8.2 |
| **Entrada** | Movimiento que incrementa la existencia por incorporación de mercancía procedente del exterior de la bodega. | Entrada de 120 unidades del lote L-2026-0142 | ingreso, remisión (como sinónimos) | SPEC · CD-29 · Monografía §8.2 |
| **Salida** | Movimiento que disminuye la existencia por retiro de mercancía hacia el exterior de la bodega, con motivo tipificado y autorización. | Salida de 30 unidades por consumo de producción | venta, despacho comercial | SPEC · CD-30 · Monografía §8.2 |
| **Movimiento interno** | Movimiento que cambia la ubicación de existencia dentro de la misma bodega sin alterar la existencia total; incluye la primera ubicación de la mercancía en recepción. | Z2-E03-N2 → Z2-E04-N1 | traslado, reubicación (como sinónimos del movimiento) | SPEC · CD-31 |
| **Transferencia** | Movimiento compuesto que traslada existencia entre zonas o bodegas con responsables distintos, mediante despacho y recepción, atravesando el estado en tránsito. | De Zona Z1 a Zona Z3 | traslado entre bodegas | SPEC · CD-32 |
| **Ajuste** | Movimiento que modifica la existencia sin contrapartida física para hacer coincidir el registro con la realidad; exige motivo tipificado y aprobación de un tercero y queda marcado para siempre. Es el movimiento de mayor riesgo. | Faltante de 2 unidades por daño, aprobado por el Jefe | corrección, nivelación, cuadre | SPEC · CD-33 · Monografía §8.2 |
| **Documento de entrada** | Registro que agrupa la mercancía esperada en un evento de recepción, con origen, referencias y cantidades; soporte contra el cual se verifica lo recibido. | DE-0087 · Taller externo · 120 unidades esperadas | remisión, ingreso, recepción (como sustantivo) | SPEC · CD-35 |

## 1.8 Configuración

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Motivo tipificado** | Causa seleccionada de una lista cerrada, obligatoria en ajustes, anulaciones, salidas, inmovilizaciones, cancelaciones y descartes de alerta. El texto libre nunca lo sustituye. | «Faltante por daño en manipulación» | razón libre, observación (como sustituto) | SPEC · CD-36 |
| **Umbral** | Valor configurable por el Administrador que define cuándo dispara una regla: mínimo y máximo de existencia, tolerancia, monto de ajuste, tiempo en tránsito, plazos. | Tolerancia de conteo = 2 unidades | meta, objetivo | SPEC · CD-46 |

## 1.9 Conteos y exactitud

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Conteo** | Proceso de verificación de la existencia física contra la registrada sobre un ámbito definido; estados: programado, en ejecución, en conciliación, cerrado, abortado o vencido. | Conteo de la Zona Z2 | toma física, inventario físico (como verbo) | SPEC · CD-38 · Monografía §8.2 |
| **Conteo cíclico** | Conteo de un ámbito parcial (ubicaciones, referencias o categorías) ejecutable sin detener la operación. Mecanismo continuo de medición de exactitud. | Conteo semanal de la categoría Camisetas | inventario rotativo | SPEC · CD-39 |
| **Conteo general** | Conteo de la totalidad del inventario, que bloquea el registro de movimientos desde el corte hasta el cierre. | Conteo general del 31 de diciembre | inventario anual | SPEC · CD-40 |
| **Tarea de conteo** | Unidad de trabajo asignada a un contador sobre un subconjunto del ámbito del conteo. | Contar Z2-E03 (niveles 1 a 4) | — | SPEC · CD-41 |
| **Segundo conteo** | Repetición de una tarea de conteo ejecutada obligatoriamente por un contador distinto del primero cuando la diferencia supera la tolerancia. | Recuento de Z2-E03-N2 por otro Auxiliar | reconteo por la misma persona | SPEC · CD-42 |
| **Existencia teórica congelada** | Fotografía de la existencia tomada al iniciar un conteo contra la cual se compara lo contado; no se altera por movimientos posteriores. | Unidad Z2-E03-N2: 40, tomada el 2026-10-05 07:00 | saldo congelado | SPEC · CD-25 |
| **Existencia contada** | Cantidad física registrada por un contador; solo modifica la existencia si el cierre genera un ajuste aprobado. | 38 unidades contadas | — | SPEC · CD-26 |
| **Diferencia de inventario** | Existencia contada menos existencia teórica congelada; positiva es sobrante, negativa es faltante. | −2 (faltante) | descuadre | SPEC · CD-27 |
| **Exactitud del inventario** | Proporción de líneas contadas cuya existencia contada coincide con la teórica congelada; es el KPI-01 y el indicador central del compromiso de valor. | 92,5 % | precisión (como sinónimo del KPI) | SPEC · CD-43 · Monografía §8.2 |

## 1.10 Novedades

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Novedad** | Reporte de una anomalía física observada por un operario que el sistema no puede detectar por sí solo; también la abre el Sistema al rechazar en la sincronización un registro que describe un hecho físico ya realizado. Nunca se elimina: se cierra. No se imputa al reportante. | «Bolsa rota en Z2-E03-N2, 3 unidades manchadas» | reclamo, incidente (como sinónimos) | SPEC · CD-48 |

## 1.11 Alertas y reglas

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Alerta** | Notificación generada automáticamente cuando una regla de negocio evalúa verdadera su condición de disparo. Manifestación operativa de la «inteligencia» del producto. | Ruptura inminente de CAM-001 · M · Azul (18 < 30) | aviso inteligente, predicción | SPEC · CD-45 · DC-07 |
| **Regla de negocio** | Enunciado explícito que el sistema evalúa para impedir estados inválidos, disparar alertas o ejecutar acciones sin intervención humana. Es el corazón de la «inteligencia» del producto. | RN-EXI-001: ninguna operación deja existencia negativa | algoritmo inteligente | SPEC · Cap. 9 · SRS Cap. 8 |

## 1.12 Auditoría

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Bitácora de auditoría** | Registro inmutable de toda acción relevante del sistema, incluidas las que no alteran el inventario: accesos, configuración, roles, aprobaciones, rechazos, anulaciones y exportaciones. No es editable por ningún rol. | «2026-10-05 10:15 · Administrador B · umbral de ajuste mayor 40 → 50» | log, historial de sistema | SPEC · CD-47 |
| **Observación de auditoría** | Hallazgo o comentario del Auditor sobre un movimiento, unidad, período o usuario, guardado en un registro separado que no altera el inventario; se cierra con respuesta. | «Tres ajustes de la misma unidad en una semana, aprobados por la misma persona» | ajuste del auditor | SPEC · RN-064 (SRS RN-AUD-002) |

## 1.13 Usuarios y acceso

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Usuario** | Persona identificada que opera el sistema con exactamente uno de los cinco roles oficiales y un ámbito; nunca se elimina. | Usuario «aux.gomez» · Auxiliar de Bodega · Zona Z2 | cuenta compartida | SPEC · M-02 |
| **Rol** | Función oficial de un usuario; existen exactamente cinco: Administrador, Jefe de Bodega, Coordinador de Bodega, Auxiliar de Bodega y Auditor. | Coordinador de Bodega | perfil (como sinónimo), cargo | SPEC · DC-04 |

## 1.14 Reportes y medición

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **KPI** | Indicador operativo calculado por el sistema sobre su propio registro; existen 24 y ninguno tiene meta numérica sin línea base. | KPI-08 Frecuencia de errores de registro | métrica de desempeño personal | SPEC · Cap. 10 |

## 1.15 Modelado

| Término | Definición | Ejemplo | Sinónimos prohibidos | Nace en |
|---|---|---|---|---|
| **Evento de dominio** | Hecho relevante para el negocio que ya ocurrió, con nombre en pasado, actor, entidad de origen y resultado; tiene ID permanente EV-<DOM>-nnn. | EV-ENT-012 Entrada confirmada | — | Nuevo (Fase 4) |
| **Evento derivado** | Evento que el Sistema genera automáticamente cuando una regla de negocio o un umbral evalúa verdadera su condición; nunca por predicción. | EV-INV-006 Existencia mínima alcanzada | — | Nuevo (Fase 4) |

---

**ESTADO DEL CAPÍTULO — 1**

| | |
|---|---|
| **Completado** | 54 términos centrales en 14 contextos, con definición, contexto, ejemplo, sinónimos prohibidos y origen; conciliación de los nombres del Prompt #004 |
| **Riesgos** | Que la interfaz o el equipo usen los nombres pedidos en lugar de los oficiales |
| **Dependencias** | SPEC §0.5 y Cap. 4 · GLOSSARY |
| **Hallazgos** | HD-01, HD-14 |

---

# CAPÍTULO 2 — SUBDOMINIOS

> El negocio de COLBASOFT es **mantener un registro del inventario de bodega que sea confiable, rastreable y medible** `[MON §3, §7.1, §8.2]`. Los subdominios se clasifican según su aporte a ese propósito:
>
> - **Core Domain (núcleo):** donde está la ventaja del producto y el esfuerzo de modelado.
> - **Supporting Domain (soporte):** específico del negocio, necesario para el núcleo, pero no es la ventaja.
> - **Generic Domain (genérico):** problema resuelto de forma general en cualquier sistema.

## 2.1 Mapa de subdominios

| ID | Subdominio | Clasificación | Módulos | Entidades | Diferenciadores |
|---|---|:--:|---|---|---|
| **SD-01** | Inventario y existencia | **Core** | M-13 | E-08 | D-01, D-06 |
| **SD-02** | Movimientos | **Core** | M-07, M-08, M-09, M-10 | E-10, E-11, E-12, E-13, E-14 | D-02, D-06, D-07 |
| **SD-03** | Trazabilidad | **Core** | M-14, M-04 | E-04, E-10 | D-06 |
| **SD-04** | Conteos y exactitud | **Core** | M-11 | E-15, E-16 | D-05, D-08 |
| **SD-05** | Alertas y reglas | **Core** | M-15 | E-18 | D-07 |
| **SD-06** | Ubicaciones | **Supporting** | M-05 | E-05, E-06, E-07 | D-04 |
| **SD-07** | Catálogo textil | **Supporting** | M-03 | E-01, E-02, E-03 | D-01 |
| **SD-08** | Identificación | **Supporting** | M-06 | E-09 | D-03 |
| **SD-09** | Novedades | **Supporting** | M-12 | E-17 | — |
| **SD-10** | Auditoría | **Supporting** | M-18 | E-21, E-22 | D-11 |
| **SD-11** | Reportes y medición | **Supporting** | M-16, M-17 | — (cálculo sobre el registro) | D-08, D-12 |
| **SD-12** | Usuarios y acceso | **Generic** | M-01, M-02 | E-19, E-20 | — |
| **SD-13** | Configuración | **Generic** | M-19 | E-24, E-25 | — |
| **SD-14** | Tareas y notificaciones | **Generic** | M-20 | E-23 | — |
| **SD-15** | Operación diaria (cierre de jornada) | **Supporting** | — (PN-14) | E-26 | — |

**Distribución:** Core 5 · Supporting 7 · Generic 3. Los nueve subdominios mínimos pedidos (Inventario, Movimientos, Trazabilidad, Ubicaciones, Conteos, Alertas, Auditoría, Usuarios, Reportes) están presentes; se agregan Catálogo textil, Identificación, Novedades, Configuración, Tareas y notificaciones y Operación diaria porque el SPEC les dedica módulos o procesos propios.

## 2.2 Justificación de cada clasificación

### SD-01 · Inventario y existencia — Core

**Alcance.** Qué hay, cuánto hay y en qué estado está: la existencia por unidad de inventario, su partición por estado (disponible, reservado, en tránsito, inmovilizado, en recepción) y las reservas.

**Por qué es Core.** Es la razón de ser del producto: sustituir el cuaderno por una cifra confiable y consultable en el momento `[MON §3, §6]`. La monografía identifica la precisión de la información de inventario como factor competitivo (Chopra y Meindl) `[MON §6, §7.2]`. Ningún software genérico resuelve la combinación referencia–talla–color–lote–ubicación de una PYME textil (D-01).

### SD-02 · Movimientos — Core

**Alcance.** Entradas, salidas, movimientos internos, transferencias y ajustes: todo hecho que altera la existencia o su ubicación, con sus flujos de autorización.

**Por qué es Core.** Es la recomendación literal de la monografía: «estandarizar entradas, salidas y movimientos de inventario» `[MON §8.2]`. La segregación de funciones y el motivo tipificado —que convierten el registro en evidencia— son el corazón del control que el producto ofrece (D-06, D-07).

### SD-03 · Trazabilidad — Core

**Alcance.** Kardex inmutable, lotes, anulación por movimiento inverso y verificación de integridad (existencia = suma de movimientos).

**Por qué es Core.** Está en el nombre del proyecto. La monografía la declara palabra clave y beneficio central (−40 % errores, +55 % trazabilidad según Hernández y Salazar) `[MON §2, §7.2]`, y el SPEC la operacionaliza como las seis preguntas de CD-21. Sin trazabilidad no hay auditoría ni demostración de impacto.

### SD-04 · Conteos y exactitud — Core

**Alcance.** Conteo cíclico y general, existencia teórica congelada, segundo conteo, conciliación y cálculo de la exactitud del inventario.

**Por qué es Core.** Produce el KPI-01 (exactitud del inventario), el primero de los tres indicadores con los que la monografía propone demostrar el beneficio `[MON §8.2]`. El conteo cíclico sin detener la operación es un diferenciador explícito (D-05).

### SD-05 · Alertas y reglas — Core

**Alcance.** Evaluación continua de condiciones mediante reglas y umbrales, generación, atención, escalamiento y cierre de alertas.

**Por qué es Core.** Es la definición constitucional de «inteligente» `[DC-07]`: automatización basada en reglas explícitas. Anticipa rupturas y sobre stock, problemas que la monografía documenta `[MON §3, §7.1]`. Toda afirmación de inteligencia del producto debe poder señalarse sobre una regla de este subdominio o sobre un KPI.

### SD-06 · Ubicaciones — Supporting

**Alcance.** Bodegas, zonas, ubicaciones, capacidades y criterios de propuesta de ubicación.

**Por qué es Supporting.** Es necesario para responder «dónde está», pero modelar un espacio físico no es en sí la ventaja del producto: soporta al núcleo. Tiene reglas propias del negocio (zona de recepción obligatoria, desactivación sin existencia), por eso no es genérico.

### SD-07 · Catálogo textil — Supporting

**Alcance.** Referencias, tallas, colores, SKU, categorías, unidades de medida y umbrales de existencia por SKU.

**Por qué es Supporting.** El modelo textil nativo es un diferenciador (D-01), pero el catálogo es dato maestro que el núcleo consume: no produce por sí mismo trazabilidad ni exactitud. Es específico del sector, por eso no es genérico.

### SD-08 · Identificación — Supporting

**Alcance.** Emisión, activación, reemplazo y anulación de identificadores QR de mercancía y de ubicación; identificadores secundarios.

**Por qué es Supporting.** Sustituye la digitación por escaneo, la principal fuente de error humano `[MON §7.2]` `[DC-08]`. Es el mecanismo que alimenta al núcleo, no el núcleo; tiene reglas propias (un solo uso, herencia de trazabilidad).

### SD-09 · Novedades — Supporting

**Alcance.** Reporte, vinculación, resolución y escalamiento de anomalías físicas observadas por el operario.

**Por qué es Supporting.** Existe por la barrera cultural documentada: el operario necesita reportar sin exponerse `[MON §4]` `[PR-06]`. Es una condición de adopción que soporta al núcleo.

### SD-10 · Auditoría — Supporting

**Alcance.** Bitácora inmutable, observaciones del Auditor, detección de hallazgos críticos (aprobación propia, discontinuidad).

**Por qué es Supporting.** La segregación con Auditor de solo lectura es diferenciador (D-11) y la monografía menciona la detección de fraudes `[MON §6]`. Soporta la confianza en el núcleo; el mecanismo de bitácora en sí es de uso general, pero sus reglas aquí son específicas.

### SD-11 · Reportes y medición — Supporting

**Alcance.** Cálculo de los 24 KPI, reportes operativos y gerenciales, dashboard operativo y exposición de datos a la herramienta analítica externa.

**Por qué es Supporting.** El cálculo de los KPI propios es específico y necesario para demostrar el beneficio `[MON §8.2]` (D-08); la generación y exportación de reportes, y la visualización analítica, son capacidades generales delegadas `[DC-06]`. Por eso se clasifica como soporte.

### SD-12 · Usuarios y acceso — Generic

**Alcance.** Autenticación individual, sesión, cinco roles oficiales, ámbito por bodega y zona.

**Por qué es Generic.** La autenticación y la gestión de usuarios son problemas resueltos en cualquier sistema. Lo específico —los cinco roles y la matriz de segregación— se expresa como política sobre un mecanismo genérico `[DC-04]`.

### SD-13 · Configuración — Generic

**Alcance.** Parámetros, umbrales, plazos y catálogo de motivos tipificados, con protección de las reglas estructurales.

**Por qué es Generic.** Administrar parámetros es un mecanismo general. Lo que importa al negocio —qué reglas no son configurables— se protege con invariantes del núcleo.

### SD-14 · Tareas y notificaciones — Generic

**Alcance.** Generación, asignación, reasignación y cierre de tareas; notificaciones y escalamientos dentro del sistema web.

**Por qué es Generic.** Un gestor de tareas y avisos es un mecanismo general. Su valor para el negocio (guiar al Auxiliar sin interpretación) depende del núcleo que lo alimenta.

### SD-15 · Operación diaria (cierre de jornada) — Supporting

**Alcance.** Consolidación de pendientes de la jornada y traspaso explícito al turno siguiente.

**Por qué es Supporting.** Mitiga riesgos operativos del SPEC (RG-03, RG-08). **Sin requisitos funcionales en el SRS** (hallazgo H-10, decisión DEC-05 pendiente): se modela para no perder el concepto, marcado como pendiente.

## 2.3 Lectura

Los cinco subdominios núcleo forman un solo propósito: **la existencia (SD-01) solo cambia por movimientos (SD-02), que quedan en un kardex (SD-03), se verifican por conteo (SD-04) y se vigilan por reglas (SD-05)**. Es exactamente la cadena que la monografía propone: registrar digitalmente entradas, salidas y movimientos, y medir exactitud, tiempos de registro y frecuencia de errores `[MON §8.2]`. Los subdominios de soporte existen porque el núcleo los necesita, y los genéricos, porque todo sistema los tiene.


---

**ESTADO DEL CAPÍTULO — 2**

| | |
|---|---|
| **Completado** | 15 subdominios clasificados y justificados (5 Core, 7 Supporting, 3 Generic) |
| **Riesgos** | Si se sobreinvierte en subdominios genéricos, se resta esfuerzo al núcleo |
| **Dependencias** | SPEC §1.7 (diferenciadores), §5.1 (módulos) |
| **Hallazgos** | HD-11 (SD-15 sin requisitos) |

---

# CAPÍTULO 3 — ENTIDADES DEL DOMINIO

> Una **entidad** tiene identidad propia que persiste a través de sus cambios de estado. Las fichas describen el concepto de negocio: **no describen estructuras de almacenamiento**. La «información que la define» es conceptual y no fija formatos. Las reglas se citan con sus IDs permanentes del SRS; los eventos, con los del EVENT_CATALOG.

## 3.1 Índice de entidades

| ID | Entidad (término oficial) | Pedida como | Concepto SPEC | Subdominio | Agregado |
|---|---|---|:--:|---|:--:|
| E-01 | **Referencia** | Producto | CD-02 | SD-07 Catálogo textil | AG-01 |
| E-02 | **SKU** | Variante | CD-05 | SD-07 Catálogo textil | AG-01 |
| E-03 | **Categoría** | — | CD-10 | SD-07 Catálogo textil | AG-02 |
| E-04 | **Lote** | — | CD-06 | SD-03 Trazabilidad | AG-04 |
| E-05 | **Bodega** | — | CD-12 | SD-06 Ubicaciones | AG-03 |
| E-06 | **Zona** | Área | CD-13 | SD-06 Ubicaciones | AG-03 |
| E-07 | **Ubicación** | — | CD-14 | SD-06 Ubicaciones | AG-03 |
| E-08 | **Unidad de Inventario** | Inventario | CD-07 | SD-01 Inventario y existencia | AG-05 |
| E-09 | **Identificador QR** | — | CD-08 | SD-08 Identificación | AG-07 |
| E-10 | **Movimiento** | — | CD-28 | SD-02 Movimientos | AG-06 |
| E-11 | **Documento de entrada** | — | CD-35 | SD-02 Movimientos | AG-08 |
| E-12 | **Solicitud de salida** | — | CD-30 | SD-02 Movimientos | AG-09 |
| E-13 | **Transferencia** | — | CD-32 | SD-02 Movimientos | AG-10 |
| E-14 | **Solicitud de ajuste** | — | CD-33 | SD-02 Movimientos | AG-11 |
| E-15 | **Conteo** | — | CD-38 | SD-04 Conteos y exactitud | AG-12 |
| E-16 | **Tarea de conteo** | — | CD-41 | SD-04 Conteos y exactitud | AG-12 |
| E-17 | **Novedad** | — | CD-48 | SD-09 Novedades | AG-13 |
| E-18 | **Alerta** | — | CD-45 | SD-05 Alertas y reglas | AG-14 |
| E-19 | **Usuario** | — | — | SD-12 Usuarios y acceso | AG-15 |
| E-20 | **Sesión** | — | — | SD-12 Usuarios y acceso | AG-15 |
| E-21 | **Registro de bitácora** | Auditoría (1/2) | CD-47 | SD-10 Auditoría | AG-16 |
| E-22 | **Observación de auditoría** | Auditoría (2/2) | — | SD-10 Auditoría | AG-17 |
| E-23 | **Tarea operativa** | — | — | SD-14 Tareas y notificaciones | AG-18 |
| E-24 | **Motivo tipificado** | — | CD-36 | SD-13 Configuración | AG-19 |
| E-25 | **Parámetro de configuración** | — | CD-46 | SD-13 Configuración | AG-20 |
| E-26 | **Cierre de jornada** | — | — | SD-15 Operación diaria (cierre de jornada) | AG-21 |

> **Entidades mínimas pedidas:** Producto → E-01 Referencia · Variante → E-02 SKU · Lote → E-04 · Ubicación → E-07 · Movimiento → E-10 · Inventario → E-08 Unidad de inventario · Conteo → E-15 · Novedad → E-17 · Usuario → E-19 · Bodega → E-05 · Área → E-06 Zona · Alerta → E-18 · Auditoría → E-21 Registro de bitácora + E-22 Observación de auditoría. Todas presentes.

## 3.2 Fichas

### E-01 · Referencia (pedida como «Producto»)

| Campo | Contenido |
|---|---|
| **Descripción** | Identificador comercial de un modelo o artículo textil, independiente de talla, color y lote. Es la unidad de catálogo. La **Prenda** (CD-01) es el objeto físico del que hablan las personas; el sistema la conoce a través de su Referencia. |
| **Responsabilidad** | Definir qué puede existir en inventario: su código, descripción, categoría, unidad de medida y los conjuntos de tallas y colores aplicables. Generar sus SKU. |
| **Identidad** | VO-01 Código de referencia (único en todo el catálogo, activa o inactiva). |
| **Información que la define** | Código · descripción · categoría · unidad de medida · tallas aplicables · colores aplicables · estado. |
| **Estado** | SM-01 |
| **Ciclo de vida** | Nace activa al crearse; puede desactivarse solo con existencia cero y reactivarse; nunca se elimina. |
| **Relaciones conceptuales** | → E-02 SKU: genera 1..n SKU (uno por talla × color)<br>→ E-03 Categoría: pertenece a exactamente 1 categoría<br>→ E-11 Documento de entrada: es solicitada en líneas de documentos de entrada |
| **Reglas asociadas** | RN-MAE-001, RN-MAE-002, RN-MAE-003, RN-MAE-007, RN-MAE-008, RN-MAE-009, RN-ENT-001, RN-INT-007 |
| **Eventos que origina** | EV-CAT-001, EV-CAT-002, EV-CAT-003, EV-CAT-005, EV-CAT-006, EV-CAT-007 |
| **Eventos que la afectan** | — |
| **Subdominio / agregado** | SD-07 Catálogo textil · AG-01 |
| **Concepto de origen** | CD-02 |

### E-02 · SKU (pedida como «Variante»)

| Campo | Contenido |
|---|---|
| **Descripción** | Combinación única e irrepetible de Referencia + Talla + Color. Es la unidad de control de catálogo con la que se planifica y se consulta. **No tiene existencia propia**: su existencia es la suma de las unidades de inventario que lo componen. |
| **Responsabilidad** | Portar los umbrales de existencia mínima y máxima que disparan alertas; agrupar lotes y unidades de inventario. |
| **Identidad** | VO-02 Combinación SKU (Referencia + Talla + Color), generada por el sistema; no se edita. |
| **Información que la define** | Referencia · talla · color · existencia mínima · existencia máxima. |
| **Estado** | — (sigue el estado de su Referencia; ver HD-19) |
| **Ciclo de vida** | Nace al crearse o ampliarse la Referencia; se usa mientras la Referencia esté activa. |
| **Relaciones conceptuales** | → E-01 Referencia: pertenece a 1 referencia<br>→ E-04 Lote: agrupa 0..n lotes<br>→ E-08 Unidad de Inventario: se materializa en 0..n unidades de inventario |
| **Reglas asociadas** | RN-LOT-002, RN-ALE-001 |
| **Eventos que origina** | EV-CAT-004, EV-INV-006, EV-INV-007, EV-INV-008 |
| **Eventos que la afectan** | EV-CAT-002, EV-CAT-007 |
| **Subdominio / agregado** | SD-07 Catálogo textil · AG-01 |
| **Concepto de origen** | CD-05 |

### E-03 · Categoría

| Campo | Contenido |
|---|---|
| **Descripción** | Agrupación de referencias con propósito de organización, asignación de zona preferente y reporte. |
| **Responsabilidad** | Agrupar referencias y orientar la propuesta automática de ubicación. |
| **Identidad** | Nombre o código de categoría (único; formato por definir en Fase 5). |
| **Información que la define** | Nombre · zona preferente (opcional) · estado. |
| **Estado** | SM-02 |
| **Ciclo de vida** | Nace activa; si está en uso se desactiva, nunca se elimina. |
| **Relaciones conceptuales** | → E-01 Referencia: agrupa 0..n referencias<br>→ E-06 Zona: puede tener 1 zona preferente |
| **Reglas asociadas** | RN-MAE-007, RN-MAE-008, RN-MOV-001 |
| **Eventos que origina** | EV-CAT-008, EV-CAT-009 |
| **Eventos que la afectan** | — |
| **Subdominio / agregado** | SD-07 Catálogo textil · AG-02 |
| **Concepto de origen** | CD-10 |

### E-04 · Lote

| Campo | Contenido |
|---|---|
| **Descripción** | Conjunto de mercancía de un mismo SKU que ingresó en un mismo evento de entrada y comparte origen y condiciones. Permite rastrear un problema hasta su procedencia. |
| **Responsabilidad** | Conservar el origen y la fecha de ingreso; permitir actuar sobre toda la mercancía que comparte procedencia (inmovilizar y liberar en bloque). Es lo que identifica el QR de mercancía: un QR por SKU + Lote, en cualquier ubicación donde esté `[DF5-01]`. |
| **Identidad** | VO-06 Código de lote (único dentro de su SKU). |
| **Información que la define** | SKU · código · origen · fecha de ingreso · estado. |
| **Estado** | SM-04 |
| **Ciclo de vida** | Nace al confirmarse la entrada; puede inmovilizarse y liberarse; nunca se elimina, aunque su existencia llegue a cero. |
| **Relaciones conceptuales** | → E-02 SKU: pertenece a exactamente 1 SKU<br>→ E-11 Documento de entrada: nace de 1 documento de entrada<br>→ E-08 Unidad de Inventario: se reparte en 1..n unidades de inventario<br>→ E-09 Identificador QR: se identifica con 1 QR de mercancía activo (DF5-01) |
| **Reglas asociadas** | RN-LOT-001, RN-LOT-002, RN-LOT-003, RN-LOT-004, RN-LOT-005, RN-MAE-006, RN-EXI-006, RN-IDE-001 |
| **Eventos que origina** | EV-LOT-002, EV-LOT-003, EV-LOT-004 |
| **Eventos que la afectan** | EV-QRC-003, EV-ENT-012, EV-LOT-001 |
| **Subdominio / agregado** | SD-03 Trazabilidad · AG-04 |
| **Concepto de origen** | CD-06 |

### E-05 · Bodega

| Campo | Contenido |
|---|---|
| **Descripción** | Ámbito físico mayor donde se almacena inventario y ámbito de responsabilidad de un Jefe de Bodega. |
| **Responsabilidad** | Contener zonas y ubicaciones; garantizar que exista al menos una zona de recepción; delimitar el ámbito de los usuarios. |
| **Identidad** | Código de bodega (formato por definir en Fase 5). |
| **Información que la define** | Código · nombre · zonas. |
| **Estado** | — (el SPEC no define estados de bodega; ver HD-19) |
| **Ciclo de vida** | Nace al crearse por el Administrador; el SPEC no define su desactivación. |
| **Relaciones conceptuales** | → E-06 Zona: contiene 1..n zonas (≥ 1 de recepción)<br>→ E-19 Usuario: es ámbito de 0..n usuarios |
| **Reglas asociadas** | RN-EXI-002, RN-MAE-004, RN-MAE-006 |
| **Eventos que origina** | EV-BOD-001, EV-BOD-002, EV-BOD-003, EV-BOD-008 |
| **Eventos que la afectan** | — |
| **Subdominio / agregado** | SD-06 Ubicaciones · AG-03 |
| **Concepto de origen** | CD-12 |

### E-06 · Zona (pedida como «Área»)

| Campo | Contenido |
|---|---|
| **Descripción** | Subdivisión de una bodega con propósito operativo: recepción, almacenamiento, preparación de salida o cuarentena. Agrupa ubicaciones. |
| **Responsabilidad** | Agrupar ubicaciones con un mismo propósito y dirigir alertas y tareas a su Coordinador responsable. |
| **Identidad** | Código de zona dentro de su bodega (formato por definir en Fase 5). |
| **Información que la define** | Bodega · tipo de zona (VO-11) · Coordinador responsable. |
| **Estado** | — (el SPEC no define estados de zona) |
| **Ciclo de vida** | Nace dentro de una bodega; permanece mientras exista la bodega. |
| **Relaciones conceptuales** | → E-05 Bodega: pertenece a 1 bodega<br>→ E-07 Ubicación: contiene 0..n ubicaciones<br>→ E-19 Usuario: tiene 0..1 Coordinador responsable |
| **Reglas asociadas** | RN-EXI-002, RN-ALE-005 |
| **Eventos que origina** | EV-BOD-007 |
| **Eventos que la afectan** | EV-BOD-002 |
| **Subdominio / agregado** | SD-06 Ubicaciones · AG-03 |
| **Concepto de origen** | CD-13 |

### E-07 · Ubicación

| Campo | Contenido |
|---|---|
| **Descripción** | Posición física identificable dentro de una zona donde reside mercancía. Nivel mínimo de precisión espacial del sistema. |
| **Responsabilidad** | Recibir existencia dentro de su capacidad; identificarse mediante su propio QR; servir como origen o destino de movimientos. |
| **Identidad** | VO-09 Código de ubicación (único dentro de su bodega) y su VO-07 Código QR de ubicación. |
| **Información que la define** | Zona · código · capacidad (VO-12) · estado. |
| **Estado** | SM-03 |
| **Ciclo de vida** | Nace activa; se desactiva solo sin existencia; puede reactivarse; nunca se elimina. |
| **Relaciones conceptuales** | → E-06 Zona: pertenece a 1 zona<br>→ E-08 Unidad de Inventario: aloja 0..n unidades de inventario<br>→ E-09 Identificador QR: se identifica con 1 QR de ubicación |
| **Reglas asociadas** | RN-EXI-002, RN-EXI-007, RN-MAE-005, RN-MAE-006, RN-MOV-001, RN-MOV-002, RN-MOV-005, RN-MOV-010 |
| **Eventos que origina** | EV-BOD-004, EV-BOD-005, EV-BOD-006, EV-QRC-007, EV-INV-009 |
| **Eventos que la afectan** | EV-BOD-003, EV-INV-001, EV-MOV-001 |
| **Subdominio / agregado** | SD-06 Ubicaciones · AG-03 |
| **Concepto de origen** | CD-14 |

### E-08 · Unidad de Inventario (pedida como «Inventario»)

| Campo | Contenido |
|---|---|
| **Descripción** | **La entidad que COLBASOFT controla**: la combinación SKU + Lote + Ubicación, es decir, la existencia de un lote de un SKU en una ubicación. Es el nivel al que se registra existencia, se ejecutan movimientos y se lleva kardex. **No tiene QR propio**: se identifica con el QR de su SKU + Lote más su ubicación `[DF5-01]`. |
| **Responsabilidad** | Custodiar la partición de su existencia por estado (disponible, reservado, en tránsito, inmovilizado, en recepción) y rechazar toda operación que la dejaría negativa o comprometería más de lo disponible. |
| **Identidad** | Combinación SKU + Lote + Ubicación (única). En la operación se determina con el QR de mercancía (SKU + Lote) más la ubicación, escaneada o seleccionada con registro (RN-IDE-001, DF5-01). |
| **Información que la define** | SKU · lote · ubicación · existencia derivada del kardex (VO-15 desglose por estado) · marca de inventario ajustado (derivada, CD-24). |
| **Estado** | SM-06 (estados de la existencia, no de la unidad) |
| **Ciclo de vida** | Nace con el primer movimiento que lleva existencia a su combinación (la unidad de la ubicación de recepción, con la entrada; la de destino, con el movimiento interno de primera ubicación: DF5-03); su existencia sube y baja solo por movimientos; puede quedar en cero y conserva su historia. |
| **Relaciones conceptuales** | → E-02 SKU: materializa 1 SKU<br>→ E-04 Lote: pertenece a 1 lote<br>→ E-07 Ubicación: reside en 1 ubicación<br>→ E-10 Movimiento: es afectada por 1..n movimientos (su kardex)<br>→ E-09 Identificador QR: se identifica con el QR de su SKU + Lote junto con su ubicación (DF5-01) |
| **Reglas asociadas** | RN-INT-004, RN-INT-005, RN-EXI-001, RN-EXI-002, RN-EXI-003, RN-EXI-004, RN-EXI-005, RN-EXI-006, RN-EXI-007, RN-IDE-001, RN-LOT-001, RN-MOV-010 |
| **Eventos que origina** | EV-INV-002, EV-INV-003, EV-INV-004, EV-TRZ-005, EV-TRZ-006 |
| **Eventos que la afectan** | EV-ENT-011, EV-ENT-012, EV-LOT-002, EV-LOT-003, EV-INV-001, EV-INV-005, EV-MOV-001, EV-MOV-002, EV-MOV-003, EV-MOV-005, EV-MOV-006, EV-MOV-007, EV-MOV-012, EV-MOV-013, EV-SAL-003, EV-SAL-006, EV-SAL-007, EV-SAL-008, EV-SAL-011, EV-AJU-005, EV-NOV-007, EV-TRZ-001, EV-TRZ-002 |
| **Subdominio / agregado** | SD-01 Inventario y existencia · AG-05 |
| **Concepto de origen** | CD-07 |

### E-09 · Identificador QR

| Campo | Contenido |
|---|---|
| **Descripción** | Código único generado por el sistema. El **QR de mercancía** identifica un **SKU + Lote** y **no** identifica ubicación, bodega ni cantidad; el **QR de ubicación** identifica una ubicación `[DF5-01]`. Medio primario de interacción del operario `[DC-08]`. Es de un solo uso: nunca se repite ni se reutiliza. |
| **Responsabilidad** | Resolver un escaneo al elemento que identifica; conservar su historia al ser reemplazado; impedir escrituras con identificadores secundarios. |
| **Identidad** | VO-07 Código QR (irrepetible en toda la vida del sistema). |
| **Información que la define** | Código · tipo (mercancía / ubicación) · elemento identificado (SKU + Lote o ubicación) · identificador secundario asociado (VO-08) · identificador al que reemplaza · estado. |
| **Estado** | SM-05 |
| **Ciclo de vida** | Se genera, se imprime, se activa al verificarse su legibilidad; puede ser reemplazado (reimpresión) o anulado; nunca se reutiliza. ⚠️ Copias impresas de un mismo QR de mercancía y su reimpresión: HD-25. |
| **Relaciones conceptuales** | → E-04 Lote: identifica 1 SKU + Lote (QR de mercancía, DF5-01)<br>→ E-07 Ubicación: identifica 1 ubicación<br>→ E-09 Identificador QR: reemplaza a 0..1 identificador anterior |
| **Reglas asociadas** | RN-IDE-001, RN-IDE-002, RN-IDE-003, RN-IDE-004 |
| **Eventos que origina** | EV-QRC-001, EV-QRC-002, EV-QRC-003, EV-QRC-004, EV-QRC-005, EV-QRC-006 |
| **Eventos que la afectan** | EV-QRC-007, EV-NOV-007 |
| **Subdominio / agregado** | SD-08 Identificación · AG-07 |
| **Concepto de origen** | CD-08 |

### E-10 · Movimiento

| Campo | Contenido |
|---|---|
| **Descripción** | **Hecho registrado que altera la existencia o la ubicación de una unidad de inventario.** Unidad transaccional del sistema. Tipos: entrada, salida, movimiento interno, ajuste y anulación (la transferencia es un movimiento compuesto). La primera ubicación de la mercancía en recepción es un movimiento interno (DF5-03): ninguna existencia cambia de ubicación sin movimiento. Su conjunto ordenado por unidad es el **kardex** (CD-37). |
| **Responsabilidad** | Dejar constancia inmutable de qué cambió, cuánto, dónde, quién, cuándo y por qué, con su documento de respaldo. |
| **Identidad** | Identificador de movimiento asignado por el sistema (formato por definir en Fase 5). |
| **Información que la define** | Tipo (VO-21) · cantidad · unidad(es) afectada(s) · ubicación · actor (VO-38) · fecha operativa (VO-32) · motivo aplicado (VO-22) · documento de respaldo (VO-25) · modo de identificación (VO-40) · existencia resultante. |
| **Estado** | SM-07 |
| **Ciclo de vida** | Se prepara en registro, puede quedar pendiente de sincronización y se confirma; desde entonces es inmutable. Uno pendiente de sincronización se valida de nuevo al sincronizarse y se confirma o se rechaza, una sola vez (DF5-05). Un error se neutraliza con un movimiento inverso (anulación), nunca editándolo. |
| **Relaciones conceptuales** | → E-08 Unidad de Inventario: afecta 1..2 unidades de inventario<br>→ E-11 Documento de entrada: respalda 0..1 documento de entrada<br>→ E-12 Solicitud de salida: ejecuta 0..1 solicitud de salida<br>→ E-13 Transferencia: forma parte de 0..1 transferencia<br>→ E-14 Solicitud de ajuste: aplica 0..1 solicitud de ajuste<br>→ E-10 Movimiento: anula a 0..1 movimiento previo |
| **Reglas asociadas** | RN-INT-001, RN-INT-002, RN-INT-003, RN-INT-004, RN-INT-008, RN-EXI-001, RN-MOV-004, RN-MOV-005, RN-MOV-010, RN-AJU-007, RN-CNT-006 |
| **Eventos que origina** | EV-INV-001, EV-MOV-001, EV-MOV-002, EV-MOV-003, EV-MOV-004, EV-TRZ-001, EV-TRZ-002, EV-TRZ-003, EV-TRZ-004, EV-TRZ-007 |
| **Eventos que la afectan** | EV-ENT-012, EV-ENT-013, EV-MOV-007, EV-MOV-013, EV-SAL-006, EV-SAL-008, EV-AJU-005, EV-CNT-004, EV-CNT-005, EV-CNT-016 |
| **Subdominio / agregado** | SD-02 Movimientos · AG-06 |
| **Concepto de origen** | CD-28 |

### E-11 · Documento de entrada

| Campo | Contenido |
|---|---|
| **Descripción** | Registro que agrupa la mercancía esperada en un evento de recepción, con su origen, referencias y cantidades. Soporte contra el cual se verifica lo recibido. **No es una orden de compra** `[DC-03]`. |
| **Responsabilidad** | Comparar lo recibido con lo esperado, registrar faltantes, sobrantes y daños, y habilitar la confirmación por una segunda persona. |
| **Identidad** | Identificador de documento asignado por el sistema. |
| **Información que la define** | Origen (VO-39) · fecha esperada · líneas esperadas (SKU, cantidad) · líneas recibidas · receptores · confirmador · estado. |
| **Estado** | SM-08 |
| **Ciclo de vida** | Se crea pendiente de recepción; se recibe total o parcialmente; queda conforme o con novedad; se confirma y genera el movimiento de entrada, que deja la existencia en recepción (DF5-02). |
| **Relaciones conceptuales** | → E-01 Referencia: solicita 1..n referencias activas<br>→ E-04 Lote: origina 1..n lotes<br>→ E-10 Movimiento: genera 1..n movimientos de entrada<br>→ E-17 Novedad: puede abrir novedades por daño |
| **Reglas asociadas** | RN-ENT-001, RN-ENT-002, RN-ENT-003, RN-ENT-004, RN-ENT-005, RN-ENT-006, RN-ENT-007, RN-EXI-007, RN-INT-003, RN-INT-008 |
| **Eventos que origina** | EV-ENT-001, EV-ENT-002, EV-ENT-003, EV-ENT-004, EV-ENT-005, EV-ENT-006, EV-ENT-007, EV-ENT-008, EV-ENT-009, EV-ENT-010, EV-ENT-011, EV-ENT-012, EV-ENT-013, EV-ENT-014, EV-ENT-015, EV-LOT-001 |
| **Eventos que la afectan** | — |
| **Subdominio / agregado** | SD-02 Movimientos · AG-08 |
| **Concepto de origen** | CD-35 |

### E-12 · Solicitud de salida

| Campo | Contenido |
|---|---|
| **Descripción** | Pedido interno para retirar mercancía del inventario, con motivo tipificado, autorización y preparación. **No gestiona pedidos de venta, facturas ni documentos comerciales** `[DC-03]`. |
| **Responsabilidad** | Verificar disponibilidad, reservar al autorizarse, guiar la preparación por escaneo y producir el movimiento de salida. |
| **Identidad** | Identificador de solicitud asignado por el sistema. |
| **Información que la define** | Líneas (SKU, lote, cantidad) · motivo aplicado · solicitante · autorizador · preparador · estado. |
| **Estado** | SM-09 |
| **Ciclo de vida** | Se solicita, se autoriza (reserva), se prepara y se ejecuta; puede rechazarse, cancelarse o vencer (reserva liberada). |
| **Relaciones conceptuales** | → E-08 Unidad de Inventario: reserva existencia de 1..n unidades<br>→ E-10 Movimiento: se ejecuta en 1..n movimientos de salida<br>→ E-23 Tarea operativa: genera 1 tarea de preparación<br>→ E-24 Motivo tipificado: lleva 1 motivo tipificado |
| **Reglas asociadas** | RN-SAL-001, RN-SAL-002, RN-SAL-003, RN-SAL-004, RN-SAL-005, RN-SAL-006, RN-EXI-001, RN-EXI-003, RN-EXI-004, RN-AJU-001 |
| **Eventos que origina** | EV-INV-005, EV-SAL-001, EV-SAL-002, EV-SAL-003, EV-SAL-004, EV-SAL-005, EV-SAL-006, EV-SAL-007, EV-SAL-008, EV-SAL-009, EV-SAL-010, EV-SAL-011 |
| **Eventos que la afectan** | — |
| **Subdominio / agregado** | SD-02 Movimientos · AG-09 |
| **Concepto de origen** | CD-30 |

### E-13 · Transferencia

| Campo | Contenido |
|---|---|
| **Descripción** | Movimiento compuesto que traslada existencia entre zonas o bodegas con responsables distintos, mediante un despacho y una recepción, atravesando el estado en tránsito. |
| **Responsabilidad** | Reservar en origen, controlar el despacho y la recepción por escaneo, conciliar lo despachado con lo recibido y resolver diferencias. |
| **Identidad** | Identificador de transferencia asignado por el sistema. |
| **Información que la define** | Origen · destino · líneas · despachador · receptor · instantes de despacho y recepción · estado. |
| **Estado** | SM-10 |
| **Ciclo de vida** | Se crea pendiente de despacho; pasa a en tránsito; se completa, queda con diferencia hasta resolución del Jefe, o se cancela. |
| **Relaciones conceptuales** | → E-08 Unidad de Inventario: compromete existencia de unidades origen y crea o incrementa unidades destino<br>→ E-10 Movimiento: se compone de movimientos de despacho y recepción<br>→ E-17 Novedad: abre novedad por faltante |
| **Reglas asociadas** | RN-EXI-003, RN-EXI-004, RN-EXI-005, RN-MOV-007, RN-MOV-008, RN-MOV-009 |
| **Eventos que origina** | EV-MOV-005, EV-MOV-006, EV-MOV-007, EV-MOV-008, EV-MOV-009, EV-MOV-010, EV-MOV-011, EV-MOV-012, EV-MOV-013 |
| **Eventos que la afectan** | — |
| **Subdominio / agregado** | SD-02 Movimientos · AG-10 |
| **Concepto de origen** | CD-32 |

### E-14 · Solicitud de ajuste

| Campo | Contenido |
|---|---|
| **Descripción** | Petición de corregir la existencia registrada cuando difiere de la física, sin contrapartida física. Es la operación de mayor riesgo del sistema. |
| **Responsabilidad** | Exigir motivo tipificado y evidencia, clasificar en menor o mayor, enrutar al aprobador que corresponda sin permitir la autoaprobación y, al aprobarse, originar el movimiento de ajuste. |
| **Identidad** | Identificador de solicitud asignado por el sistema. |
| **Información que la define** | Unidad afectada · existencia registrada · existencia observada · diferencia (VO-18) · motivo aplicado · evidencia · clasificación (VO-26) · solicitante · aprobador · justificación de rechazo · origen (conteo, novedad, hallazgo) · estado. |
| **Estado** | SM-11 |
| **Ciclo de vida** | Se solicita pendiente de aprobación; puede escalar o bloquearse; termina aprobada (aplicada) o rechazada. |
| **Relaciones conceptuales** | → E-08 Unidad de Inventario: corrige 1 unidad de inventario<br>→ E-10 Movimiento: origina 0..1 movimiento de ajuste<br>→ E-15 Conteo: puede derivar de 1 conteo<br>→ E-17 Novedad: puede derivar de 1 novedad |
| **Reglas asociadas** | RN-AJU-001, RN-AJU-002, RN-AJU-003, RN-AJU-004, RN-AJU-005, RN-AJU-006, RN-AJU-007, RN-EXI-001, RN-EXI-006 |
| **Eventos que origina** | EV-AJU-001, EV-AJU-002, EV-AJU-003, EV-AJU-004, EV-AJU-005, EV-AJU-006, EV-AJU-007, EV-AJU-008, EV-AJU-009, EV-AJU-010, EV-TAR-004, EV-TAR-005 |
| **Eventos que la afectan** | EV-CNT-014, EV-NOV-007 |
| **Subdominio / agregado** | SD-02 Movimientos · AG-11 |
| **Concepto de origen** | CD-33 |

### E-15 · Conteo

| Campo | Contenido |
|---|---|
| **Descripción** | Proceso de verificación de la existencia física contra la registrada sobre un ámbito definido. Puede ser **cíclico** (parcial, sin detener la operación, CD-39) o **general** (total, con bloqueo de movimientos, CD-40). |
| **Responsabilidad** | Congelar la existencia teórica, distribuir tareas, ocultar la cantidad esperada, exigir segundo conteo, conciliar, permitir el cierre solo al Jefe y calcular la exactitud. |
| **Identidad** | Identificador de conteo asignado por el sistema. |
| **Información que la define** | Tipo (cíclico / general) · alcance (VO-41) · fecha de corte (VO-34) · existencia teórica congelada (VO-16) · tareas · líneas con resultado (VO-19) · cobertura · exactitud (VO-20) · estado. |
| **Estado** | SM-12 |
| **Ciclo de vida** | Se programa, se ejecuta, se concilia y se cierra; puede abortarse o vencer. Un conteo cerrado no se reabre. |
| **Relaciones conceptuales** | → E-16 Tarea de conteo: se divide en 1..n tareas de conteo<br>→ E-08 Unidad de Inventario: verifica 1..n unidades<br>→ E-14 Solicitud de ajuste: origina 0..n solicitudes de ajuste<br>→ E-07 Ubicación: cubre 1..n ubicaciones |
| **Reglas asociadas** | RN-CNT-001, RN-CNT-002, RN-CNT-003, RN-CNT-004, RN-CNT-005, RN-CNT-006, RN-CNT-007, RN-CNT-008, RN-NOV-001, RN-AJU-001 |
| **Eventos que origina** | EV-CNT-001, EV-CNT-002, EV-CNT-003, EV-CNT-004, EV-CNT-005, EV-CNT-006, EV-CNT-008, EV-CNT-009, EV-CNT-010, EV-CNT-012, EV-CNT-013, EV-CNT-014, EV-CNT-015, EV-CNT-016, EV-CNT-017, EV-CNT-018, EV-ALE-007, EV-REP-005 |
| **Eventos que la afectan** | — |
| **Subdominio / agregado** | SD-04 Conteos y exactitud · AG-12 |
| **Concepto de origen** | CD-38 |

### E-16 · Tarea de conteo

| Campo | Contenido |
|---|---|
| **Descripción** | Unidad de trabajo asignada a un contador, correspondiente a un subconjunto del ámbito del conteo. El **segundo conteo** (CD-42) es una tarea adicional ejecutada por una persona distinta. |
| **Responsabilidad** | Recoger la existencia contada (VO-17) de su subconjunto sin exponer la cantidad esperada. |
| **Identidad** | Identificador de tarea dentro de su conteo. |
| **Información que la define** | Contador · ubicaciones o referencias a contar · existencia contada · es segundo conteo (sí/no) · estado. |
| **Estado** | SM-13 |
| **Ciclo de vida** | Se asigna y se confirma; puede reasignarse antes de confirmarse. |
| **Relaciones conceptuales** | → E-15 Conteo: pertenece a 1 conteo<br>→ E-19 Usuario: es ejecutada por 1 contador |
| **Reglas asociadas** | RN-CNT-002, RN-CNT-003 |
| **Eventos que origina** | EV-CNT-007, EV-CNT-011 |
| **Eventos que la afectan** | EV-CNT-006, EV-CNT-009 |
| **Subdominio / agregado** | SD-04 Conteos y exactitud · AG-12 |
| **Concepto de origen** | CD-41 |

### E-17 · Novedad

| Campo | Contenido |
|---|---|
| **Descripción** | Reporte de una anomalía física observada por un operario que el sistema no puede detectar por sí solo: mercancía dañada, sin identificador, en ubicación incorrecta o inexistente. También la abre el Sistema, como actor, cuando rechaza al sincronizar un registro que describe un hecho físico ya realizado (RN-INT-008, DF5-05). **Nunca se elimina: se cierra.** |
| **Responsabilidad** | Llevar la anomalía al Coordinador sin imputarla al reportante, y vincularla al movimiento que la resuelve. |
| **Identidad** | Identificador de novedad asignado por el sistema. |
| **Información que la define** | Tipo (VO-31) · unidad asociada (si existe) · ubicación · descripción · evidencia · reportante · acción determinada · movimiento de resolución · estado. |
| **Estado** | SM-14 |
| **Ciclo de vida** | Se abre al reportarse; puede escalar; se cierra resuelta o improcedente. |
| **Relaciones conceptuales** | → E-08 Unidad de Inventario: se asocia a 0..1 unidad de inventario<br>→ E-07 Ubicación: se localiza en 1 ubicación<br>→ E-14 Solicitud de ajuste: puede derivar en 0..1 solicitud de ajuste<br>→ E-17 Novedad: agrupa novedades vinculadas |
| **Reglas asociadas** | RN-NOV-001, RN-NOV-002, RN-NOV-003, RN-MAE-007, RN-INT-008 |
| **Eventos que origina** | EV-NOV-001, EV-NOV-002, EV-NOV-003, EV-NOV-004, EV-NOV-005, EV-NOV-006, EV-NOV-007 |
| **Eventos que la afectan** | EV-ENT-011, EV-MOV-008, EV-TRZ-007 |
| **Subdominio / agregado** | SD-09 Novedades · AG-13 |
| **Concepto de origen** | CD-48 |

### E-18 · Alerta

| Campo | Contenido |
|---|---|
| **Descripción** | Notificación generada automáticamente cuando una regla de negocio evalúa verdadera su condición de disparo. Manifestación operativa de la «inteligencia» del producto `[DC-07]`. |
| **Responsabilidad** | Llevar la condición anómala al rol responsable, exigir atención o descarte con motivo, escalar y cerrarse al cesar la condición. |
| **Identidad** | Tipo de alerta + condición + elemento afectado (una sola alerta activa por condición vigente). |
| **Información que la define** | Tipo (VO-30) · severidad (VO-28) · condición y umbral · elemento afectado · destinatario por rol · atención registrada · estado. |
| **Estado** | SM-15 |
| **Ciclo de vida** | Se genera activa; puede escalar; termina atendida, descartada con motivo o cerrada automáticamente sin atención. |
| **Relaciones conceptuales** | → E-08 Unidad de Inventario: se refiere a unidades, SKU, lotes, ubicaciones, conteos, transferencias o solicitudes<br>→ E-25 Parámetro de configuración: se dispara según umbrales configurados<br>→ E-19 Usuario: se dirige a un rol |
| **Reglas asociadas** | RN-ALE-001, RN-ALE-002, RN-ALE-003, RN-ALE-004, RN-ALE-005, RN-AJU-004, RN-MOV-008, RN-CNT-005, RN-LOT-005 |
| **Eventos que origina** | EV-ALE-001, EV-ALE-002, EV-ALE-003, EV-ALE-004, EV-ALE-005, EV-ALE-006 |
| **Eventos que la afectan** | EV-LOT-004, EV-INV-006, EV-INV-007, EV-INV-008, EV-INV-009, EV-MOV-004, EV-MOV-011, EV-AJU-008, EV-AJU-009, EV-CNT-018, EV-NOV-006, EV-ALE-007, EV-JOR-005 |
| **Subdominio / agregado** | SD-05 Alertas y reglas · AG-14 |
| **Concepto de origen** | CD-45 |

### E-19 · Usuario

| Campo | Contenido |
|---|---|
| **Descripción** | Persona identificada que opera el sistema con exactamente uno de los cinco roles oficiales `[DC-04]` y un ámbito de bodega y zonas. No existen cuentas genéricas ni compartidas `[PR-05]`. |
| **Responsabilidad** | Ser el sujeto al que se atribuye toda acción; delimitar qué puede hacer (rol) y dónde (ámbito). |
| **Identidad** | Identificador de usuario (único en todo el sistema). |
| **Información que la define** | Identidad personal · rol (VO-36) · ámbito (VO-37) · estado · exigencia de cambio de contraseña. |
| **Estado** | SM-16 |
| **Ciclo de vida** | Se crea activo; puede bloquearse por intentos fallidos y ser restablecido; se desactiva y reactiva; nunca se elimina y sus movimientos conservan su identidad. |
| **Relaciones conceptuales** | → E-20 Sesión: abre 0..n sesiones<br>→ E-05 Bodega: opera en 1 bodega<br>→ E-06 Zona: coordina 0..n zonas<br>→ E-10 Movimiento: es actor de 0..n movimientos |
| **Reglas asociadas** | RN-INT-001, RN-MAE-004, RN-MAE-006, RN-MAE-007, RN-MAE-009 |
| **Eventos que origina** | EV-ACC-001, EV-ACC-002, EV-ACC-003, EV-ACC-006, EV-ACC-007, EV-USR-001, EV-USR-002, EV-USR-003, EV-USR-004, EV-USR-005, EV-USR-006, EV-AUD-003, EV-AUD-004 |
| **Eventos que la afectan** | EV-BOD-007, EV-TAR-004, EV-TAR-005 |
| **Subdominio / agregado** | SD-12 Usuarios y acceso · AG-15 |
| **Concepto de origen** | — |

### E-20 · Sesión

| Campo | Contenido |
|---|---|
| **Descripción** | Período de trabajo autenticado de un usuario en un dispositivo, que se mantiene mientras hay actividad y se cierra manualmente o por inactividad. |
| **Responsabilidad** | Sostener la atribución de cada acción al usuario autenticado sin obligarlo a reautenticarse en cada registro. |
| **Identidad** | Identificador de sesión asignado por el sistema. |
| **Información que la define** | Usuario · dispositivo de origen · inicio · última actividad · estado. |
| **Estado** | SM-17 |
| **Ciclo de vida** | Se abre con credenciales válidas y se cierra manualmente, por inactividad o por cambio de contraseña. |
| **Relaciones conceptuales** | → E-19 Usuario: pertenece a 1 usuario |
| **Reglas asociadas** | RN-INT-001 |
| **Eventos que origina** | EV-ACC-004, EV-ACC-005 |
| **Eventos que la afectan** | EV-ACC-001, EV-ACC-006, EV-USR-004 |
| **Subdominio / agregado** | SD-12 Usuarios y acceso · AG-15 |
| **Concepto de origen** | — |

### E-21 · Registro de bitácora (pedida como «Auditoría (1/2)»)

| Campo | Contenido |
|---|---|
| **Descripción** | Constancia inmutable de una acción relevante del sistema, incluidas las que no alteran el inventario: accesos, cambios de configuración y de rol, aprobaciones, rechazos, anulaciones, exportaciones. **La bitácora registra el sistema; el kardex registra el inventario.** |
| **Responsabilidad** | Permitir la reconstrucción independiente de lo que ocurrió y la detección de discontinuidades. |
| **Identidad** | Posición en la secuencia continua de la bitácora. |
| **Información que la define** | Evento registrado · actor · fecha operativa · detalle suficiente para reconstruir (valor anterior y nuevo cuando aplica). |
| **Estado** | — (inmutable desde su creación) |
| **Ciclo de vida** | Nace al ocurrir el evento auditable y permanece para siempre, sin purga. |
| **Relaciones conceptuales** | → E-19 Usuario: atribuye cada registro a 1 actor<br>→ E-22 Observación de auditoría: puede ser objeto de observaciones |
| **Reglas asociadas** | RN-AUD-001, RN-AUD-003, RN-AUD-004, RN-INT-001 |
| **Eventos que origina** | EV-REP-001, EV-AUD-005, EV-AUD-006 |
| **Eventos que la afectan** | EV-AUD-003, EV-AUD-004 |
| **Subdominio / agregado** | SD-10 Auditoría · AG-16 |
| **Concepto de origen** | CD-47 |

### E-22 · Observación de auditoría (pedida como «Auditoría (2/2)»)

| Campo | Contenido |
|---|---|
| **Descripción** | Hallazgo o comentario que el Auditor deja sobre un movimiento, unidad, período o usuario. Se guarda en un registro separado y **no altera el estado del inventario**; es la única escritura del Auditor. |
| **Responsabilidad** | Dejar constancia de la revisión independiente y obtener respuesta. |
| **Identidad** | Identificador de observación asignado por el sistema. |
| **Información que la define** | Objeto observado · alcance (VO-42) · texto · Auditor · respuesta · estado. |
| **Estado** | SM-18 |
| **Ciclo de vida** | Se abre al registrarse y se cierra con respuesta; nunca se elimina. |
| **Relaciones conceptuales** | → E-10 Movimiento: puede referirse a movimientos, unidades, períodos o usuarios |
| **Reglas asociadas** | RN-AUD-002, RN-MAE-007 |
| **Eventos que origina** | EV-AUD-001, EV-AUD-002 |
| **Eventos que la afectan** | — |
| **Subdominio / agregado** | SD-10 Auditoría · AG-17 |
| **Concepto de origen** | — |

### E-23 · Tarea operativa

| Campo | Contenido |
|---|---|
| **Descripción** | Unidad de trabajo que el sistema asigna a una persona: recepción, ubicación, preparación de salida o transferencia (las de conteo son E-16). Indica qué, dónde y cuánto. |
| **Responsabilidad** | Guiar al operario y cerrarse **por la ejecución del hecho asociado**, nunca por declaración del usuario. |
| **Identidad** | Identificador de tarea asignado por el sistema. |
| **Información que la define** | Tipo · elemento de origen · responsable · prioridad (VO-29) · vista (sí/no) · estado. |
| **Estado** | SM-19 |
| **Ciclo de vida** | Se genera pendiente, puede reasignarse y se completa cuando se confirma el movimiento asociado. |
| **Relaciones conceptuales** | → E-19 Usuario: tiene 1 responsable<br>→ E-11 Documento de entrada: puede originarse en documentos, solicitudes o transferencias |
| **Reglas asociadas** | RN-INT-001, RN-CNT-003 |
| **Eventos que origina** | EV-TAR-001, EV-TAR-002, EV-TAR-003, EV-TAR-006 |
| **Eventos que la afectan** | EV-SAL-003, EV-JOR-002 |
| **Subdominio / agregado** | SD-14 Tareas y notificaciones · AG-18 |
| **Concepto de origen** | — |

### E-24 · Motivo tipificado

| Campo | Contenido |
|---|---|
| **Descripción** | Causa seleccionable de una lista cerrada, obligatoria en ajustes, anulaciones, salidas, inmovilizaciones, cancelaciones y descartes de alerta. El texto libre nunca lo sustituye. |
| **Responsabilidad** | Hacer la trazabilidad interpretable y comparable; indicar si exige evidencia adjunta. |
| **Identidad** | Código de motivo dentro de su tipo de operación. |
| **Información que la define** | Tipo de operación · descripción · exige evidencia (sí/no) · estado. |
| **Estado** | SM-20 |
| **Ciclo de vida** | Se crea activo; si está en uso se desactiva, nunca se elimina. |
| **Relaciones conceptuales** | → E-14 Solicitud de ajuste: justifica ajustes<br>→ E-12 Solicitud de salida: justifica salidas<br>→ E-18 Alerta: justifica descartes |
| **Reglas asociadas** | RN-AJU-003, RN-SAL-002, RN-MAE-007, RN-MAE-008 |
| **Eventos que origina** | EV-PAR-002, EV-PAR-003, EV-PAR-005 |
| **Eventos que la afectan** | — |
| **Subdominio / agregado** | SD-13 Configuración · AG-19 |
| **Concepto de origen** | CD-36 |

### E-25 · Parámetro de configuración

| Campo | Contenido |
|---|---|
| **Descripción** | Valor configurable por el Administrador que define cuándo dispara una regla o qué plazo aplica: umbral de ajuste menor/mayor, tolerancia de conteo, tiempo máximo en tránsito, plazos, umbral de autorización del Coordinador, inactividad de sesión, política de toma. Los umbrales hacen adaptable la «inteligencia» del sistema. |
| **Responsabilidad** | Ajustar el comportamiento de las reglas configurables dentro de rangos admisibles, sin alterar las reglas estructurales y sin efecto retroactivo. |
| **Identidad** | Nombre del parámetro (único). |
| **Información que la define** | Nombre · valor (VO-27 / VO-35) · rango admisible · valor anterior (en bitácora). |
| **Estado** | — (se modifica; cada cambio queda en bitácora) |
| **Ciclo de vida** | Existe desde la puesta en marcha con un valor inicial; cambia solo por decisión del Administrador. |
| **Relaciones conceptuales** | → E-18 Alerta: gobierna el disparo de alertas<br>→ E-14 Solicitud de ajuste: gobierna la clasificación de ajustes<br>→ E-15 Conteo: gobierna la tolerancia de conteo |
| **Reglas asociadas** | RN-AUD-004, RN-AJU-002, RN-SAL-001, RN-MOV-008, RN-CNT-003 |
| **Eventos que origina** | EV-REP-002, EV-REP-003, EV-REP-004, EV-PAR-001, EV-PAR-004 |
| **Eventos que la afectan** | EV-ALE-006, EV-REP-005 |
| **Subdominio / agregado** | SD-13 Configuración · AG-20 |
| **Concepto de origen** | CD-46 |

### E-26 · Cierre de jornada

| Campo | Contenido |
|---|---|
| **Descripción** | Consolidación de la actividad del día que deja la bodega en estado consistente y traspasa explícitamente los pendientes al turno siguiente (PN-14). ⚠️ **Sin HU ni RF en el SRS** (H-10, DEC-05). |
| **Responsabilidad** | Hacer visibles los pendientes ocultos y registrar quién asumió su responsabilidad. |
| **Identidad** | Bodega + jornada (fecha operativa). |
| **Información que la define** | Jornada · pendientes consolidados · pendientes traspasados · ejecutor · estado. |
| **Estado** | SM-21 |
| **Ciclo de vida** | Se abre con la jornada; se cierra al registrar el cierre o queda como omitido. |
| **Relaciones conceptuales** | → E-05 Bodega: pertenece a 1 bodega<br>→ E-23 Tarea operativa: traspasa tareas pendientes |
| **Reglas asociadas** | RN-INT-003, RN-MOV-006 |
| **Eventos que origina** | EV-JOR-001, EV-JOR-002, EV-JOR-003, EV-JOR-004, EV-JOR-005 |
| **Eventos que la afectan** | — |
| **Subdominio / agregado** | SD-15 Operación diaria (cierre de jornada) · AG-21 |
| **Concepto de origen** | — |


---

**ESTADO DEL CAPÍTULO — 3**

| | |
|---|---|
| **Completado** | 26 entidades con descripción, responsabilidad, identidad, estado, ciclo de vida, relaciones, reglas y eventos |
| **Riesgos** | Bodega, Zona y SKU sin estados propios definidos en el SPEC (HD-19); copias impresas de un mismo QR de mercancía (HD-25) |
| **Dependencias** | Cap. 4 (identidades como objetos de valor), Cap. 5 (agregados), EVENT_CATALOG |
| **Hallazgos** | HD-01, HD-04 (resuelto, DF5-01), HD-05, HD-06 (resuelto, DF5-02), HD-11, HD-19, HD-23, HD-25 |

---

# CAPÍTULO 4 — OBJETOS DE VALOR

> Un **objeto de valor** se define solo por su contenido, no tiene identidad propia y es **inmutable**: para cambiarlo se reemplaza por otro. Dos objetos de valor con el mismo contenido son el mismo valor.

**Regla general de inmutabilidad.** Todos los objetos de valor de este capítulo son inmutables. Las entidades que los contienen pueden sustituirlos (por ejemplo, un nuevo umbral), salvo donde se indica lo contrario; en ese caso la sustitución también está prohibida.

| ID | Objeto de valor | Qué representa | Inmutabilidad | Validaciones | Ejemplo | Reglas |
|---|---|---|---|---|---|---|
| **VO-01** | Código de referencia | Identidad comercial de una referencia. | No se sustituye | No vacío; único en todo el catálogo (activa o inactiva) `[RN-MAE-001]`; no se reutiliza. | CAM-001 (camiseta cuello redondo) | RN-MAE-001 |
| **VO-02** | Combinación SKU | Tríada Referencia + Talla + Color que identifica un SKU. | Una vez generado no se sustituye | La talla y el color deben pertenecer a los conjuntos aplicables de la referencia; la tríada es irrepetible; la genera el sistema y no se edita. | CAM-001 · M · Azul | RN-LOT-002 |
| **VO-03** | Talla | Valor de la dimensión de tamaño. | Inmutable; la entidad lo reemplaza completo | Pertenece al conjunto de tallas definido por la empresa. | S, M, L, XL; 8, 10, 12 | — |
| **VO-04** | Color | Valor de la dimensión cromática. | Inmutable; la entidad lo reemplaza completo | Pertenece al conjunto de colores definido por la empresa. | Azul, Negro, Crudo | — |
| **VO-05** | Unidad de medida | Magnitud en que se cuenta una referencia. | No se sustituye si hay movimientos | Pertenece a la lista configurada (unidades, metros, rollos, kilogramos); fija por referencia una vez hay movimientos `[RN-MAE-002]`. | metros (tela), unidades (prenda) | RN-MAE-002, RN-INT-007 |
| **VO-06** | Código de lote | Identidad de un lote dentro de su SKU. | No se sustituye | Único dentro de su SKU `[RN-MAE-006]`; si la empresa no distingue lotes, el sistema genera uno por evento de entrada `[RN-LOT-001]`. | L-2026-0142 | RN-MAE-006, RN-LOT-001 |
| **VO-07** | Código QR | Valor codificado de un identificador QR. | No se sustituye ni se reutiliza jamás | Irrepetible en toda la vida del sistema, incluso tras anulación o reemplazo `[RN-IDE-002]`; distingue si identifica mercancía o ubicación. El de mercancía identifica un SKU + Lote y no contiene ubicación, bodega ni cantidad `[DF5-01]`. | Valor opaco generado por el sistema, acompañado de texto legible de respaldo | RN-IDE-002 |
| **VO-08** | Código de barras secundario | Código externo (típicamente del proveedor) asociado a mercancía. | Inmutable; la entidad lo reemplaza completo | Asociado a lo sumo a un QR de mercancía, es decir, a un SKU + Lote `[RN-IDE-003]` `[DF5-01]` (ver HD-26); habilita consulta, **nunca escritura** `[DC-08]`. | Código de barras impreso por el proveedor en la bolsa | RN-IDE-003 |
| **VO-09** | Código de ubicación | Identidad de una ubicación dentro de su bodega. | Inmutable; la entidad lo reemplaza completo | Único en la bodega `[RN-MAE-006]`. | Z2-E03-N2 | RN-MAE-006 |
| **VO-10** | Ubicación física | Dirección completa Bodega › Zona › Ubicación. | Inmutable; la entidad lo reemplaza completo | Los tres niveles deben existir y la ubicación debe estar activa para recibir mercancía `[RN-MOV-002]`. | Bodega Principal › Almacenamiento › Z2-E03-N2 | RN-MOV-002, RN-EXI-002 |
| **VO-11** | Tipo de zona | Propósito operativo de una zona. | Inmutable; la entidad lo reemplaza completo | Uno de: recepción, almacenamiento, preparación de salida, cuarentena. Toda bodega tiene al menos una de recepción `[RN-EXI-002]`. | Recepción | RN-EXI-002 |
| **VO-12** | Capacidad | Cantidad máxima que admite una ubicación. | Inmutable; la entidad lo reemplaza completo | No negativa; expresada en la unidad configurada; si no se define, se trata como ilimitada y queda pendiente de configurar. Ver HD-17 sobre la unidad. | 200 unidades | RN-MOV-002 |
| **VO-13** | Cantidad | Magnitud de existencia o de movimiento. | Inmutable; la entidad lo reemplaza completo | Expresada siempre en la unidad de medida de su referencia, sin conversiones `[RN-INT-007]`; la existencia resultante nunca es negativa `[RN-EXI-001]`. Precisión decimal por definir (HD-18). | 12 unidades; 35,5 metros | RN-INT-007, RN-EXI-001 |
| **VO-14** | Estado de inventario | Condición de una porción de existencia que determina qué puede hacerse con ella. | Inmutable; la entidad lo reemplaza completo | Uno de: Disponible, Reservado, En tránsito, Inmovilizado, En recepción; mutuamente excluyentes para una misma cantidad (CD-44). | Reservado | RN-EXI-003, RN-EXI-004, RN-EXI-005, RN-EXI-006 |
| **VO-15** | Desglose de existencia | Existencia de una unidad repartida por estado. | Inmutable; la entidad lo reemplaza completo | La suma de las porciones es igual a la existencia derivada del kardex `[RN-INT-004]`; ninguna porción es negativa. | Total 40 = 25 disponible + 10 reservado + 5 inmovilizado | RN-INT-004 |
| **VO-16** | Existencia teórica congelada | Fotografía de la existencia tomada al iniciar un conteo (CD-25). | No se sustituye durante el conteo | Inmutable una vez tomada `[RN-CNT-001]`; nunca se muestra al contador `[RN-CNT-002]`. | Unidad X: 40 al 2026-10-05 07:00 | RN-CNT-001, RN-CNT-002 |
| **VO-17** | Existencia contada | Cantidad física registrada por un contador (CD-26). | Solo corregible por su contador antes de confirmar la tarea | Cantidad no negativa; no modifica la existencia salvo que el cierre genere un ajuste `[RN-CNT-004]`. | 38 | RN-CNT-004 |
| **VO-18** | Diferencia de inventario | Existencia contada (u observada) menos existencia teórica (CD-27). | Inmutable; la entidad lo reemplaza completo | Positiva = sobrante; negativa = faltante; cero = conforme. | −2 (faltante) | RN-CNT-003, RN-AJU-003 |
| **VO-19** | Resultado de línea de conteo | Clasificación de una línea contada. | Inmutable; la entidad lo reemplaza completo | Uno de: Conforme, Sobrante, Faltante; derivado de VO-18. | Faltante | RN-CNT-003 |
| **VO-20** | Exactitud | Proporción de líneas conformes sobre líneas contadas (CD-43, KPI-01). | Inmutable; la entidad lo reemplaza completo | Entre 0 % y 100 %; se calcula al cierre del conteo; **sin meta numérica** hasta existir línea base. | 92,5 % | RN-CNT-004 |
| **VO-21** | Tipo de movimiento | Naturaleza del movimiento. | Inmutable; la entidad lo reemplaza completo | Uno de: Entrada, Salida, Movimiento interno, Ajuste, Anulación; los despachos y recepciones de transferencia son movimientos internos o entre bodegas marcados como parte de una transferencia; la primera ubicación de la mercancía en recepción es un Movimiento interno `[RN-MOV-010]` `[DF5-03]`. | Ajuste | RN-INT-002 |
| **VO-22** | Motivo aplicado | Motivo tipificado seleccionado + texto complementario opcional. | Inmutable; la entidad lo reemplaza completo | El motivo tipificado es obligatorio donde la regla lo exige y debe estar activo; el texto libre nunca lo sustituye `[RN-AJU-003]` `[RN-SAL-002]`. | «Faltante por daño en manipulación» + «bolsa rota en estante» | RN-AJU-003, RN-SAL-002 |
| **VO-23** | Evidencia | Adjunto que respalda una afirmación (fotografía, documento). | Inmutable; la entidad lo reemplaza completo | Obligatoria cuando el motivo tipificado lo exige; inmutable una vez adjuntada a una solicitud confirmada. | Fotografía de la mercancía dañada | RN-AJU-003, RN-SAL-006 |
| **VO-24** | Justificación | Texto que explica una decisión de rechazo, descarte, exclusión o cancelación. | Inmutable; la entidad lo reemplaza completo | No vacía cuando la regla la exige `[RN-AJU-006]` `[RN-CNT-007]`. | «Evidencia no corresponde al motivo declarado» | RN-AJU-006, RN-CNT-007 |
| **VO-25** | Documento de respaldo | Referencia al documento que originó un movimiento. | Inmutable; la entidad lo reemplaza completo | Debe apuntar a un documento existente del dominio (documento de entrada, solicitud de salida, transferencia, solicitud de ajuste, conteo); no es un documento comercial `[DC-03]`. | Documento de entrada DE-0087 | RN-INT-002 |
| **VO-26** | Clasificación de ajuste | Menor o mayor, junto con el umbral vigente al clasificar. | Conserva el umbral aplicado aunque cambie la configuración | Conserva el umbral aplicado para que un cambio posterior de configuración no altere su interpretación `[RN-AJU-002]`. | Mayor (umbral aplicado: 50 unidades) | RN-AJU-002 |
| **VO-27** | Umbral | Valor que define cuándo dispara una regla (CD-46). | Inmutable; la entidad lo reemplaza completo | Dentro del rango admisible del parámetro; mínimo ≤ máximo cuando van en pareja; su cambio no es retroactivo `[RN-AUD-004]`. | Existencia mínima = 30 | RN-AUD-004 |
| **VO-28** | Severidad de alerta | Importancia de una alerta. | Inmutable; la entidad lo reemplaza completo | Incluye al menos el nivel «Crítica», que escala por plazo `[RN-ALE-002]`. **El SPEC no define los demás niveles** (HD-15). | Crítica | RN-ALE-002 |
| **VO-29** | Prioridad de tarea | Orden en que el panel presenta las tareas. | Inmutable; la entidad lo reemplaza completo | **El SPEC no define la escala ni el criterio** (HD-15). | — | — |
| **VO-30** | Tipo de alerta | Condición de negocio que la alerta representa. | Inmutable; la entidad lo reemplaza completo | Uno de los diez tipos del MVP (RF-ALE-004): ruptura inminente, sobre stock, existencia en cero, lote próximo a vencer inmovilización, tránsito prolongado, ajustes recurrentes, exactitud bajo el objetivo, conteo vencido, ubicación sobreocupada, solicitud de ajuste sin resolver. | Sobre stock | RN-ALE-001 |
| **VO-31** | Tipo de novedad | Clase de anomalía física reportada. | Inmutable; la entidad lo reemplaza completo | Seleccionado de lista tipificada; como mínimo: dañada, sin identificador, en ubicación incorrecta, inexistente (PN-12). | Sin identificador | RN-NOV-003 |
| **VO-32** | Fecha operativa | Instante (fecha y hora) en que ocurrió un hecho, con su jornada. | No se sustituye | Es el instante del hecho, no el de su sincronización (HD-16); se conserva al confirmar un registro sincronizado `[RN-INT-008]`; no puede ser futuro. | 2026-10-05 09:42, jornada del 2026-10-05 | RN-INT-003 |
| **VO-33** | Período | Rango de fechas operativas. | Inmutable; la entidad lo reemplaza completo | Inicio ≤ fin. | Semana del 5 al 11 de octubre | — |
| **VO-34** | Fecha de corte | Instante de referencia de un conteo general o de una consulta histórica. | Inmutable; la entidad lo reemplaza completo | Explícita en todo resultado que la use; la reconstrucción a una misma fecha de corte da siempre el mismo resultado. | 2026-12-31 18:00 | RN-CNT-006, RN-INT-004 |
| **VO-35** | Plazo | Duración máxima configurable. | Inmutable; la entidad lo reemplaza completo | Positiva; aplica a tránsito, reserva, aprobación, novedad, conteo, atención de alerta, inactividad. | 48 horas | RN-MOV-008, RN-SAL-005, RN-AJU-005, RN-NOV-002, RN-CNT-005, RN-ALE-002 |
| **VO-36** | Rol | Función oficial de un usuario. | Inmutable; la entidad lo reemplaza completo | Exactamente uno de: Administrador, Jefe de Bodega, Coordinador de Bodega, Auxiliar de Bodega, Auditor `[DC-04]`. | Coordinador de Bodega | RN-MAE-004 |
| **VO-37** | Ámbito | Bodega y zonas en que un usuario opera. | Inmutable; la entidad lo reemplaza completo | Las zonas pertenecen a la bodega; Jefe, Administrador y Auditor no tienen restricción de ámbito de consulta. | Bodega Principal · Zonas Z1, Z2 | — |
| **VO-38** | Actor | Quién ejecutó un hecho: un usuario identificado o el Sistema como actor explícito. | No se sustituye | Nunca vacío; nunca una cuenta compartida `[RN-INT-001]`; el Sistema no es un rol (HD-12). | Sistema (liberación de reserva vencida) | RN-INT-001 |
| **VO-39** | Origen de entrada | Procedencia declarada de la mercancía que entra. | Inmutable; la entidad lo reemplaza completo | Texto o código de origen; **no es un proveedor como entidad comercial** `[DC-03]`. | Taller de confección externo | RN-ENT-002 |
| **VO-40** | Modo de identificación | Cómo se identificó la mercancía o la ubicación en un movimiento. | Inmutable; la entidad lo reemplaza completo | Escaneo o selección manual; la selección manual queda registrada (PN-03 E-05). Ver PROP-KPI-02 del SRS. | Selección manual | RN-SAL-004 |
| **VO-41** | Alcance de conteo | Conjunto de ubicaciones, referencias o categorías de un conteo cíclico, o la totalidad en uno general. | Inmutable; la entidad lo reemplaza completo | No vacío; en el general cubre todas las ubicaciones salvo exclusiones justificadas `[RN-CNT-007]`. | Zona Z2 completa | RN-CNT-007 |
| **VO-42** | Alcance de auditoría | Período, referencias, ubicaciones, usuarios o tipos de movimiento revisados. | Inmutable; la entidad lo reemplaza completo | Al menos un criterio; no altera nada. | Ajustes de septiembre 2026 | RN-AUD-002 |

> Los objetos de valor pedidos como ejemplo por el Prompt #004 están cubiertos: SKU → VO-02 · Código QR → VO-07 · Ubicación física → VO-10 · Cantidad → VO-13 · Estado de inventario → VO-14 · Prioridad → VO-28 (severidad) y VO-29 (prioridad de tarea) · Fecha operativa → VO-32.


---

**ESTADO DEL CAPÍTULO — 4**

| | |
|---|---|
| **Completado** | 42 objetos de valor con inmutabilidad, validaciones y ejemplos |
| **Riesgos** | VO-28 y VO-29 sin escala definida; VO-12 sin regla para unidades heterogéneas; VO-13 sin precisión fijada |
| **Dependencias** | Cap. 3 (entidades que los contienen) |
| **Hallazgos** | HD-15, HD-16, HD-17, HD-18 |

---

# CAPÍTULO 5 — AGREGADOS

> Un **agregado** es un conjunto de entidades y objetos de valor que cambia como una unidad para proteger sus invariantes. Se accede a él por su **raíz**. Entre agregados las referencias son **por identidad**, nunca por contención. Este capítulo describe límites de consistencia del negocio, no decisiones de almacenamiento.

## 5.1 Índice de agregados

| ID | Agregado | Raíz | Entidades internas | Invariantes que protege | Referencias por identidad |
|---|---|---|---|---|---|
| **AG-01** | Referencia | E-01 Referencia | E-02 SKU | IN-15, IN-16, IN-17, IN-06 | E-03 (por identidad) |
| **AG-02** | Categoría | E-03 Categoría | — | IN-21, IN-22 | E-06 zona preferente (por identidad) |
| **AG-03** | Bodega | E-05 Bodega | E-06 Zona, E-07 Ubicación | IN-09, IN-19, IN-20, IN-43 | E-19 Coordinador por zona (por identidad) |
| **AG-04** | Lote | E-04 Lote | — | IN-27, IN-28, IN-29, IN-30 | E-02 SKU, E-11 documento (por identidad) |
| **AG-05** | Unidad de Inventario | E-08 Unidad de Inventario | — | IN-03, IN-04, IN-08, IN-10, IN-11, IN-12, IN-13, IN-14, IN-23, IN-70 | E-02, E-04, E-07 (por identidad) |
| **AG-06** | Movimiento | E-10 Movimiento | — | IN-01, IN-02, IN-07, IN-41, IN-42, IN-51, IN-71, IN-72 | E-08 unidades, documento de respaldo (por identidad) |
| **AG-07** | Identificador QR | E-09 Identificador QR | — | IN-23, IN-24, IN-25, IN-26 | E-04 Lote o E-07 Ubicación identificados (por identidad) |
| **AG-08** | Documento de entrada | E-11 Documento de entrada | — | IN-31, IN-32, IN-33, IN-34, IN-35, IN-07, IN-70 | E-01 referencias, E-04 lotes creados (por identidad) |
| **AG-09** | Solicitud de salida | E-12 Solicitud de salida | — | IN-36, IN-37, IN-38, IN-39, IN-40, IN-47 | E-08 unidades reservadas (por identidad) |
| **AG-10** | Transferencia | E-13 Transferencia | — | IN-12, IN-44, IN-45 | E-08 unidades origen y destino (por identidad) |
| **AG-11** | Solicitud de ajuste | E-14 Solicitud de ajuste | — | IN-47, IN-48, IN-49, IN-50, IN-51, IN-08 | E-08 unidad corregida; conteo o novedad de origen (por identidad) |
| **AG-12** | Conteo | E-15 Conteo | E-16 Tarea de conteo | IN-52, IN-53, IN-54, IN-55, IN-56, IN-57, IN-58 | E-08 unidades, E-07 ubicaciones (por identidad) |
| **AG-13** | Novedad | E-17 Novedad | — | IN-59, IN-58, IN-21, IN-72 | E-08, E-07, E-14 (por identidad) |
| **AG-14** | Alerta | E-18 Alerta | — | IN-60, IN-61, IN-62 | Elemento afectado (por identidad) |
| **AG-15** | Usuario | E-19 Usuario | E-20 Sesión | IN-01, IN-18, IN-68 | E-05, E-06 ámbito (por identidad) |
| **AG-16** | Bitácora de auditoría | E-21 Registro de bitácora | — | IN-63, IN-65, IN-66 | Actor, elemento del evento (por identidad) |
| **AG-17** | Observación de auditoría | E-22 Observación de auditoría | — | IN-64 | Objeto observado (por identidad) |
| **AG-18** | Tarea operativa | E-23 Tarea operativa | — | IN-69 | Elemento de origen, responsable (por identidad) |
| **AG-19** | Motivo tipificado | E-24 Motivo tipificado | — | IN-21, IN-22, IN-48 | — |
| **AG-20** | Configuración | E-25 Parámetro de configuración | — | IN-65, IN-67 | — |
| **AG-21** | Cierre de jornada | E-26 Cierre de jornada | — | IN-07 | E-05 bodega, pendientes (por identidad) |

## 5.2 Por qué existe cada agregado

**AG-01 · Referencia.** La referencia y sus SKU cambian juntos: los SKU nacen de las tallas y colores de la referencia y su unidad de medida es común. Proteger en un solo límite evita SKU huérfanos o con unidades distintas.

**AG-02 · Categoría.** Tiene vida propia (se activa y desactiva) y la referencian muchas referencias; incluirla dentro de cada referencia la duplicaría.

**AG-03 · Bodega.** La estructura física cambia poco, la administra solo el Administrador y tiene reglas de conjunto: al menos una zona de recepción y códigos de ubicación únicos por bodega. La desactivación de una ubicación consulta la existencia de otro agregado (AG-05) antes de aceptarse.

**AG-04 · Lote.** Se inmoviliza y libera **como un todo** en todas sus ubicaciones; el límite del lote es exactamente el límite de esa decisión.

**AG-05 · Unidad de Inventario.** Es el guardián de la disponibilidad: toda operación que comprometa existencia (salida, transferencia, movimiento interno, ajuste) debe consultarse contra la partición por estado de esta unidad para impedir negativos y dobles compromisos. Su existencia no se almacena: se deriva de los movimientos confirmados (AG-06).

**AG-06 · Movimiento.** Un movimiento es un hecho inmutable: una vez confirmado ninguna operación lo modifica. Un movimiento que afecta dos unidades (movimiento interno) debe confirmarse de forma indivisible para conservar la existencia total (ver riesgo RF5-02).

**AG-07 · Identificador QR.** Su regla central —un código se emite una sola vez en toda la vida del sistema y el reemplazo hereda la trazabilidad— es independiente de la mercancía que identifica. El QR de mercancía identifica un SKU + Lote, no una unidad de inventario: la unidad se resuelve con ese QR más la ubicación (DF5-01), por eso reubicar no cambia el QR.

**AG-08 · Documento de entrada.** Las líneas esperadas y recibidas se comparan y confirman juntas; la segregación receptor ≠ confirmador se verifica sobre el documento completo.

**AG-09 · Solicitud de salida.** La solicitud es la unidad de autorización, reserva y preparación; su motivo y su autorizador valen para todas sus líneas.

**AG-10 · Transferencia.** Despacho y recepción deben conciliarse sobre las mismas líneas; la transferencia no se completa hasta resolverse cualquier diferencia.

**AG-11 · Solicitud de ajuste.** El ajuste es la operación más sensible: su motivo, evidencia, clasificación, solicitante y aprobador se protegen como un todo hasta su resolución.

**AG-12 · Conteo.** La existencia congelada, las tareas, los segundos conteos y la conciliación deben ser coherentes entre sí: quién contó, quién recontó y quién cierra se verifica dentro del mismo límite.

**AG-13 · Novedad.** Tiene ciclo propio de reporte, escalamiento y cierre; la regla «no duplicar sobre una unidad con novedad abierta» se evalúa al crearla. La que nace de un registro rechazado al sincronizar se vincula a ese rechazo (IN-72).

**AG-14 · Alerta.** Su invariante —una sola alerta activa por condición vigente— y su ciclo de atención son independientes del elemento que la originó.

**AG-15 · Usuario.** El usuario controla sus sesiones: el cambio de contraseña cierra las demás y la desactivación cierra el acceso de inmediato.

**AG-16 · Bitácora de auditoría.** La continuidad de la bitácora es una propiedad de la secuencia completa: agregar es la única operación y toda discontinuidad es hallazgo crítico.

**AG-17 · Observación de auditoría.** Es la única escritura del Auditor y vive separada del inventario para garantizar que no lo altere.

**AG-18 · Tarea operativa.** Tiene responsable y ciclo propio; se cierra por el hecho asociado del agregado de origen.

**AG-19 · Motivo tipificado.** Lo referencian muchas operaciones; su desactivación no debe alterar las operaciones históricas que lo usaron.

**AG-20 · Configuración.** Los parámetros se validan en conjunto (rangos, parejas mínimo–máximo) y ninguno puede alcanzar las reglas estructurales.

**AG-21 · Cierre de jornada.** ⚠️ Pendiente DEC-05. Consolidación de una bodega en una jornada; su cierre depende de que no queden registros sin sincronizar.

## 5.3 Operaciones de negocio que involucran varios agregados

Algunas operaciones del negocio afectan a más de un agregado. El dominio declara **qué debe quedar coherente**; cómo garantizarlo es decisión de la Fase 5.

| Operación | Agregados involucrados | Coherencia exigida por el negocio | Regla |
|---|---|---|---|
| Confirmar una entrada | AG-08 → AG-04, AG-06, AG-05, AG-07 | Lote, movimiento de entrada y existencia en recepción nacen juntos o no nace ninguno | RN-ENT-007, RN-LOT-001, RN-INT-004, RN-EXI-007 |
| Primera ubicación (v1.1) | AG-06 → AG-05 (unidad de recepción) y AG-05 (unidad destino) | El descuento en la unidad de recepción y el incremento disponible en la unidad destino son indivisibles; la existencia total no cambia | RN-MOV-010, RN-MOV-004 |
| Movimiento interno | AG-06 → AG-05 (origen) y AG-05 (destino) | La existencia total no cambia: el descuento y el incremento son indivisibles | RN-MOV-004 |
| Transferencia | AG-10 → AG-05 (origen y destino), AG-06 | Reserva, tránsito y recepción mantienen la partición por estado | RN-EXI-004, RN-EXI-005, RN-MOV-007 |
| Autorizar una salida | AG-09 → AG-05 | Nadie más compromete la misma existencia | RN-EXI-003, RN-EXI-004 |
| Aprobar un ajuste | AG-11 → AG-06, AG-05 | El movimiento de ajuste solo existe si la solicitud está aprobada; nunca deja existencia negativa | RN-AJU-001, RN-EXI-001 |
| Cerrar un conteo | AG-12 → AG-11 | Cada diferencia elegida para ajuste origina una solicitud de ajuste | RN-CNT-004 |
| Inmovilizar un lote | AG-04 → AG-05 (todas sus unidades) | Toda la existencia del lote cambia de estado a la vez | RN-LOT-003 |
| Desactivar referencia o ubicación | AG-01 / AG-03 → AG-05 (consulta) | Solo con existencia cero | RN-MAE-003, RN-MAE-005 |
| Sincronizar un registro retenido (v1.1) | AG-06 → AG-05 (y AG-13 si se rechaza) | Se confirma o se rechaza una sola vez, contra el estado vigente; si se rechaza y describe un hecho físico, la novedad nace con el rechazo | RN-INT-008 |
| Cualquier evento auditable | Todos → AG-16 | Todo hecho auditable deja su registro en la bitácora | RN-AUD-001 |


---

**ESTADO DEL CAPÍTULO — 5**

| | |
|---|---|
| **Completado** | 21 agregados con raíz, entidades internas, invariantes protegidas, referencias por identidad y justificación; 11 operaciones que involucran varios agregados |
| **Riesgos** | Operaciones indivisibles sobre dos unidades (RF5-02) y concurrencia sobre la disponibilidad (RF5-03) |
| **Dependencias** | Cap. 3, Cap. 6 |
| **Hallazgos** | HD-04 resuelto por DF5-01: la identidad de AG-05 no cambia; AG-07 identifica SKU + Lote |

---

# CAPÍTULO 6 — INVARIANTES DEL DOMINIO

> Una **invariante** es una condición que se cumple **siempre**, antes y después de cualquier cambio. Cada invariante cita las reglas del SRS que la originan, el agregado que la protege y su tipo (estructural = no configurable; configurable = su umbral se ajusta, su lógica no se desactiva).

## 6.1 Invariantes

| ID | Invariante | Reglas (SRS) | Guardián | Tipo |
|---|---|---|---|:--:|
| **IN-01** | Toda acción que altera el estado del sistema es atribuible a un usuario identificado o al Sistema como actor explícito; no existen acciones anónimas ni cuentas compartidas. | RN-INT-001 | Todos (AG-06, AG-15, AG-16) | Estructural |
| **IN-02** | Un movimiento confirmado no se edita ni se elimina, por ningún rol; un error se neutraliza con un movimiento inverso y ambos permanecen. | RN-INT-002 | AG-06 | Estructural |
| **IN-03** | La existencia de una unidad de inventario es, en todo momento, la suma algebraica de sus movimientos confirmados; no existe como valor independiente. | RN-INT-004, RN-AUD-005 | AG-05 / AG-06 | Estructural |
| **IN-04** | No coexisten dos unidades de inventario con la misma combinación SKU + Lote + Ubicación. | RN-INT-005 | AG-05 | Estructural |
| **IN-05** | Ninguna consulta altera el estado del inventario. | RN-INT-006 | Todos | Estructural |
| **IN-06** | Toda cantidad de una referencia se expresa en su unidad de medida; el dominio no convierte entre unidades. | RN-INT-007 | AG-01 | Estructural |
| **IN-07** | Un documento no se confirma, ni una jornada se cierra, mientras existan registros pendientes de sincronización. | RN-INT-003 | AG-08, AG-06, AG-21 | Estructural |
| **IN-08** | Ninguna operación —salida, transferencia, movimiento interno ni ajuste— deja la existencia de una unidad por debajo de cero; no hay excepción ni autorización posible. | RN-EXI-001 | AG-05 | Estructural |
| **IN-09** | Toda existencia disponible reside en una ubicación identificada; toda bodega tiene al menos una zona de recepción. | RN-EXI-002 | AG-03 / AG-05 | Estructural |
| **IN-10** | Ninguna operación compromete una cantidad mayor que la existencia disponible de la unidad origen. | RN-EXI-003 | AG-05 | Estructural |
| **IN-11** | La existencia reservada por una salida autorizada o una transferencia creada no puede comprometerse de nuevo. | RN-EXI-004 | AG-05 | Estructural |
| **IN-12** | La existencia en tránsito no es disponible ni en el origen ni en el destino hasta confirmarse la recepción o cancelarse con retorno. | RN-EXI-005 | AG-05 / AG-10 | Estructural |
| **IN-13** | Toda operación sobre existencia inmovilizada requiere autorización expresa; su ajuste requiere al Administrador, sin importar el monto. | RN-EXI-006 | AG-05 / AG-11 | Estructural |
| **IN-14** | La existencia de una unidad es igual a la suma de sus porciones disponible, reservada, en tránsito, inmovilizada y en recepción; una misma cantidad está en un solo estado. | RN-EXI-003, RN-EXI-004, RN-EXI-005, RN-EXI-006 | AG-05 | Estructural |
| **IN-15** | El código de referencia es único en todo el catálogo, esté la referencia activa o inactiva. | RN-MAE-001 | AG-01 | Estructural |
| **IN-16** | La unidad de medida de una referencia no cambia si existe al menos un movimiento sobre ella. | RN-MAE-002 | AG-01 | Estructural |
| **IN-17** | Una referencia con existencia distinta de cero no puede desactivarse. | RN-MAE-003 | AG-01 | Estructural |
| **IN-18** | Siempre existe al menos un Administrador activo y cada bodega conserva al menos un Jefe de Bodega activo. | RN-MAE-004 | AG-15 | Estructural |
| **IN-19** | Una ubicación con existencia no puede desactivarse. | RN-MAE-005 | AG-03 | Estructural |
| **IN-20** | El código de lote es único en su SKU; el de ubicación, en su bodega; el identificador de usuario, en todo el sistema. | RN-MAE-006 | AG-04, AG-03, AG-15 | Estructural |
| **IN-21** | Nada se elimina físicamente: usuarios, referencias, categorías, lotes, ubicaciones, motivos, novedades y observaciones se desactivan o se cierran. | RN-MAE-007 | Todos | Estructural |
| **IN-22** | Un elemento desactivado no participa en operaciones nuevas pero conserva su identidad en el histórico, y puede reactivarse dejando constancia. | RN-MAE-008, RN-MAE-009 | Todos | Estructural / Configurable |
| **IN-23** | Toda existencia tiene un identificador QR activo: el de su SKU + Lote. La unidad de inventario se determina con ese QR más su ubicación; si el SKU + Lote está en más de una ubicación y no se indica cuál, la operación no se registra (DF5-01). | RN-IDE-001 | AG-05 / AG-07 | Estructural |
| **IN-24** | Un código QR se emite una sola vez en toda la vida del sistema; ni la anulación ni el reemplazo permiten reutilizarlo. | RN-IDE-002 | AG-07 | Estructural |
| **IN-25** | Un código de barras secundario se asocia a lo sumo a un QR de mercancía (un SKU + Lote) y nunca basta por sí solo para una operación de escritura. | RN-IDE-003 | AG-07 | Estructural |
| **IN-26** | El identificador que reemplaza a otro hereda íntegramente su trazabilidad; el reemplazado permanece consultable. | RN-IDE-004 | AG-07 | Estructural |
| **IN-27** | Toda existencia pertenece a un lote; si la empresa no distingue lotes, cada evento de entrada genera uno. | RN-LOT-001 | AG-04 / AG-05 | Estructural |
| **IN-28** | Un lote pertenece a un solo SKU. | RN-LOT-002 | AG-04 | Estructural |
| **IN-29** | Inmovilizar un lote inmoviliza simultáneamente toda su existencia en todas sus ubicaciones y bodegas; no existe inmovilización parcial de lote. | RN-LOT-003 | AG-04 | Estructural |
| **IN-30** | Solo el Jefe de Bodega o el Administrador liberan un lote inmovilizado, con motivo tipificado. | RN-LOT-004 | AG-04 | Estructural |
| **IN-31** | Un documento de entrada solo contiene referencias activas del catálogo. | RN-ENT-001 | AG-08 | Estructural |
| **IN-32** | Lo recibido se compara línea por línea con lo esperado antes de confirmar. | RN-ENT-003 | AG-08 | Estructural |
| **IN-33** | Un sobrante de recepción no ingresa al inventario sin autorización del Jefe de Bodega. | RN-ENT-005 | AG-08 | Estructural |
| **IN-34** | La mercancía recibida dañada nunca ingresa como disponible; si ingresa, lo hace inmovilizada en cuarentena con novedad abierta. | RN-ENT-006 | AG-08 / AG-05 | Estructural |
| **IN-35** | Quien registró la recepción física no confirma esa misma entrada. | RN-ENT-007 | AG-08 | Estructural |
| **IN-36** | Toda salida lleva motivo tipificado y no contiene cliente, precio, factura ni documento comercial. | RN-SAL-002 | AG-09 | Estructural |
| **IN-37** | El Coordinador autoriza salidas solo por debajo de su umbral configurado; por encima autoriza el Jefe. | RN-SAL-001 | AG-09 | Configurable |
| **IN-38** | Durante la preparación de una salida solo se acepta el escaneo de mercancía que corresponde a lo solicitado (referencia, talla, color y lote). | RN-SAL-004 | AG-09 | Estructural |
| **IN-39** | Toda baja por daño requiere aprobación del Jefe de Bodega, observación y evidencia, cualquiera sea la cantidad. | RN-SAL-006 | AG-09 | Estructural |
| **IN-40** | El retorno de mercancía despachada es una entrada nueva que referencia la salida original; la salida nunca se reversa. | RN-SAL-007 | AG-09 / AG-08 | Estructural |
| **IN-41** | Un movimiento interno no altera la existencia total del SKU + Lote: la suma de las unidades origen y destino es la misma antes y después. | RN-MOV-004 | AG-06 | Estructural |
| **IN-42** | La ubicación destino de un movimiento es distinta de la de origen. | RN-MOV-005 | AG-06 | Estructural |
| **IN-43** | Una ubicación inactiva no recibe mercancía y no se propone como destino una ubicación cuya capacidad se excedería. | RN-MOV-002 | AG-03 | Configurable |
| **IN-44** | Una transferencia no se completa mientras lo recibido difiera de lo despachado sin resolución del Jefe; lo recibido nunca puede exceder lo despachado. | RN-MOV-007 | AG-10 | Estructural |
| **IN-45** | Solo el Jefe cancela una transferencia en tránsito, generando retorno al origen; toda cancelación lleva motivo. | RN-MOV-009 | AG-10 | Estructural |
| **IN-46** | La ubicación propuesta es una sugerencia; ubicar en otro lugar se permite y la desviación se registra como información operativa, no como falta. | RN-MOV-001, RN-MOV-003 | AG-05 / AG-06 | Configurable |
| **IN-47** | Nadie aprueba una solicitud que originó: ajustes, salidas y cierres de conteo escalan al nivel superior o se bloquean si no existe. | RN-AJU-001 | AG-11, AG-09, AG-12 | Estructural |
| **IN-48** | Todo ajuste lleva un motivo tipificado activo; el texto libre solo lo complementa. | RN-AJU-003 | AG-11 | Estructural |
| **IN-49** | Todo ajuste se clasifica como menor o mayor y conserva el umbral aplicado al clasificarse. | RN-AJU-002 | AG-11 | Configurable |
| **IN-50** | Un ajuste rechazado lleva justificación y permanece con la misma permanencia que uno aprobado; la existencia no cambia. | RN-AJU-006 | AG-11 | Estructural |
| **IN-51** | Un ajuste aplicado no se edita ni se revierte; su error se corrige con un nuevo ajuste. | RN-AJU-007 | AG-11 / AG-06 | Estructural |
| **IN-52** | La existencia teórica congelada de un conteo no cambia por movimientos posteriores al congelamiento. | RN-CNT-001 | AG-12 | Estructural |
| **IN-53** | El contador nunca ve la cantidad esperada, ni antes ni después de registrar su conteo. | RN-CNT-002 | AG-12 | Estructural |
| **IN-54** | El segundo conteo lo ejecuta una persona distinta a la del primero, y quien ejecutó un conteo no lo cierra. | RN-CNT-003 | AG-12 | Estructural |
| **IN-55** | Solo el Jefe de Bodega cierra un conteo y decide qué diferencias se ajustan; un conteo cerrado no se reabre. | RN-CNT-004 | AG-12 | Estructural |
| **IN-56** | Entre el corte y el cierre de un conteo general no se registran movimientos, salvo excepciones autorizadas por el Jefe y marcadas como tales. | RN-CNT-006 | AG-12 / AG-06 | Estructural |
| **IN-57** | Un conteo general no se cierra con ubicaciones de su alcance sin cubrir, salvo exclusión justificada. | RN-CNT-007 | AG-12 | Estructural |
| **IN-58** | Mercancía sin registro en el sistema no se cuenta ni se usa hasta ser identificada e incorporada por ajuste aprobado. | RN-NOV-001 | AG-12 / AG-13 | Estructural |
| **IN-59** | Una unidad tiene a lo sumo una novedad abierta; los reportes posteriores se vinculan a ella. | RN-NOV-003 | AG-13 | Configurable |
| **IN-60** | Una condición de alerta vigente tiene a lo sumo una alerta activa. | RN-ALE-001 | AG-14 | Configurable |
| **IN-61** | Toda alerta tiene un destinatario por rol; si ese rol no tiene usuario activo, escala al superior. | RN-ALE-005 | AG-14 | Estructural |
| **IN-62** | Ninguna alerta se cierra manualmente sin acción registrada o motivo de descarte. | RN-ALE-004 | AG-14 | Estructural |
| **IN-63** | La bitácora solo admite agregar; es inmutable y continua, y toda discontinuidad es hallazgo crítico. | RN-AUD-001 | AG-16 | Estructural |
| **IN-64** | El Auditor no escribe en el inventario; sus observaciones viven en un registro separado. | RN-AUD-002 | AG-17 | Estructural |
| **IN-65** | Todo cambio de configuración deja valor anterior y nuevo en la bitácora y aplica solo hacia adelante. | RN-AUD-004 | AG-20 / AG-16 | Estructural |
| **IN-66** | Toda exportación de datos queda en la bitácora con usuario, alcance y fecha. | RN-AUD-003 | AG-16 | Estructural |
| **IN-67** | Las reglas estructurales no son parametrizables por ningún rol, incluido el Administrador (interpretación del SRS, DEC-04). | RN-INT-001, RN-INT-002, RN-EXI-001, RN-AJU-001, RN-AJU-003, RN-CNT-002, RN-CNT-003, RN-AUD-001, RN-MAE-007, RN-INT-004 | AG-20 | Estructural |
| **IN-68** | Un usuario tiene exactamente un rol activo, y ese rol es uno de los cinco oficiales `[DC-04]`. | RN-MAE-004 | AG-15 | Estructural |
| **IN-69** | Una tarea operativa se cierra por la confirmación del hecho asociado, nunca por declaración del usuario; su reasignación no viola la regla del segundo conteo. | RN-CNT-003, RN-INT-001 | AG-18 | Estructural |
| **IN-70** | La existencia de una entrada confirmada ingresa En recepción, en una ubicación de una zona de recepción: no se reserva, no sale ni se transfiere hasta ubicarse. Toda zona de recepción tiene al menos una ubicación. La cantidad dañada ingresa inmovilizada (IN-34). | RN-EXI-007 | AG-08 / AG-05 | Estructural |
| **IN-71** | La primera ubicación de la existencia en recepción es un movimiento interno confirmado en el kardex (qué, cuánto, origen, destino, quién, cuándo y documento de entrada); ninguna existencia cambia de ubicación sin movimiento. La cantidad movida queda Disponible en el destino, salvo que el destino pertenezca a una zona de recepción. | RN-MOV-010 | AG-06 / AG-05 | Estructural |
| **IN-72** | Un registro retenido sin conectividad se confirma o se rechaza una sola vez, al sincronizarse y tras validarse de nuevo contra el estado vigente; nunca se aplica un registro que viole una invariante, y el intento y su resultado quedan registrados. | RN-INT-008 | AG-06 | Estructural |

## 6.2 Políticas del dominio (reglas reactivas)

Algunas reglas del SRS no expresan algo que se cumpla siempre, sino **una reacción**: «cuando ocurre X, el sistema hace Y» (escalar al vencer un plazo, generar una alerta al cruzar un umbral). No son invariantes: son **políticas** y se manifiestan como **eventos derivados** (EVENT_CATALOG, Cap. 5).

| ID | Regla (SRS) | Política | Evento(s) derivado(s) |
|---|---|---|---|
| **PO-01** | RN-AJU-004 | Cuando una misma unidad de inventario acumula más ajustes que el umbral configurado dentro de una ventana de tiempo configurada, el sistema genera alerta de patrón anómalo dirigida al Jefe y al Auditor, listando los ajustes… | EV-AJU-009 |
| **PO-02** | RN-AJU-005 | Una solicitud de ajuste sin resolver más allá del plazo configurado escala automáticamente al nivel superior y genera alerta. | EV-AJU-008 |
| **PO-03** | RN-ALE-002 | Una alerta de severidad crítica no atendida dentro del plazo configurado escala automáticamente al rol superior y genera notificación adicional. El escalamiento queda en la bitácora. | EV-ALE-004 |
| **PO-04** | RN-ALE-003 | Una alerta se cierra automáticamente cuando su condición de disparo deja de cumplirse, quedando en el historial marcada como no atendida si nadie actuó sobre ella. | EV-ALE-005 |
| **PO-05** | RN-CNT-005 | Un conteo programado y no ejecutado dentro de su plazo genera alerta. Si excede el plazo máximo, la existencia congelada se libera y el conteo se marca como vencido. | EV-CNT-018 |
| **PO-06** | RN-CNT-008 | Cuando la diferencia global de un conteo general supera el umbral crítico configurado, el sistema notifica al Administrador y al Auditor antes de permitir el cierre. | EV-CNT-013 |
| **PO-07** | RN-ENT-002 | Al crear un documento de entrada con el mismo origen, referencia y fecha que otro existente, el sistema advierte de posible duplicado y exige confirmación explícita. No lo bloquea: puede tratarse de dos remesas legítimas. | EV-ENT-002 |
| **PO-08** | RN-ENT-004 | Un faltante de recepción se registra como tal, el documento pasa a recibido con novedad y se notifica al Jefe. El faltante no bloquea la confirmación de lo efectivamente recibido. | EV-ENT-008 |
| **PO-09** | RN-LOT-005 | Un lote que supera el umbral de antigüedad configurado se destaca en las consultas y genera alerta informativa al Jefe. | EV-LOT-004 |
| **PO-10** | RN-MOV-006 | Un movimiento interno interrumpido queda en estado en tránsito. Su existencia no está disponible en origen ni en destino. Si el tiempo en tránsito supera el máximo configurado, el sistema genera alerta. | EV-MOV-004, EV-JOR-001 |
| **PO-11** | RN-MOV-008 | Una transferencia que supera el tiempo máximo en tránsito configurado genera alerta dirigida al Jefe, identificando su contenido y su responsable de despacho. | EV-MOV-011 |
| **PO-12** | RN-NOV-002 | Una novedad sin resolver más allá del plazo configurado escala al Jefe de Bodega y genera alerta. | EV-NOV-006 |
| **PO-13** | RN-SAL-003 | La toma de mercancía para una salida sigue la política configurada de selección de ubicación: primero en entrar primero en salir por lote, ubicación de mayor cantidad, o ubicación más próxima. El sistema propone; el operario… | EV-SAL-003, EV-SAL-010 |
| **PO-14** | RN-SAL-005 | Una reserva no ejecutada dentro del plazo configurado se libera automáticamente, la existencia vuelve a disponible y se genera alerta al solicitante. | EV-INV-005 |

**Cobertura:** las 85 reglas del SRS quedan cubiertas: 71 como invariantes y 14 como políticas (85/85).


---

**ESTADO DEL CAPÍTULO — 6**

| | |
|---|---|
| **Completado** | 72 invariantes (mínimo exigido: 40), cada una vinculada a reglas del SRS; 14 políticas reactivas; 85/85 reglas cubiertas (82 + 3 de la v1.1: IN-70…IN-72) |
| **Riesgos** | IN-67 depende de DEC-04; IN-46 depende de HD-13; IN-23 actualizada por DF5-01 |
| **Dependencias** | SRS Cap. 8 |
| **Hallazgos** | HD-04, HD-13 · distinción invariante/política (nueva en esta fase) |

---

# CAPÍTULO 7 — CICLOS DE VIDA

> Especificación textual de cómo nace, vive y termina cada entidad principal. Los estados formales y sus transiciones están en el Cap. 8. Los ejemplos de ciclo del Prompt #004 se analizan en HD-02 y HD-03.

| Entidad | Ciclo de vida | Observaciones |
|---|---|---|
| **E-01 Referencia** | Creada **Activa** → (usada en documentos, SKU, movimientos) → **Inactiva** si su existencia es cero → **Activa** al reactivarse. | No existe «Agotada» ni «En movimiento» como estado de la referencia: son condiciones de su existencia (HD-02). Nunca se elimina. |
| **E-02 SKU** | Generado con su referencia → recibe umbrales mínimo/máximo → se materializa en unidades de inventario → sigue el estado de su referencia. | Si no tiene umbrales configurados no dispara alertas de mínimo y máximo y figura como pendiente de parametrizar. |
| **E-04 Lote** | Creado **Habilitado** al confirmarse la entrada → se reparte en ubicaciones → **Inmovilizado** (todo el lote) → **Habilitado** al liberarse → su existencia puede llegar a cero sin que el lote desaparezca. | La antigüedad sobre el umbral genera alerta informativa, no un cambio de estado. |
| **E-07 Ubicación** | Creada **Activa** con su QR → recibe existencia dentro de su capacidad → **Inactiva** solo sin existencia → **Activa** al reactivarse. | «Sobreocupada» es una condición derivada (alerta), no un estado. |
| **E-08 Unidad de inventario** | Nace con el primer movimiento que lleva existencia a su combinación SKU+Lote+Ubicación (la unidad de recepción, con la entrada; la de destino, con el movimiento interno de primera ubicación) → su existencia pasa por los estados **En recepción → Disponible ↔ Reservado / En tránsito / Inmovilizado** → puede llegar a cero y conserva su kardex. | La unidad no tiene estado propio: los estados son de porciones de su existencia (SM-06). Pasar de En recepción a Disponible es un movimiento interno entre dos unidades (DF5-03). |
| **E-09 Identificador QR** | **Generado** → impreso → **Activo** al verificarse su legibilidad → **Reemplazado** (reimpresión con herencia) o **Anulado**. | Un código jamás vuelve a emitirse. El QR de mercancía identifica un SKU + Lote y no cambia al reubicar (DF5-01). ⚠️ Copias impresas y reimpresión: HD-25. |
| **E-10 Movimiento** | **En registro** (corregible por su autor, RNF-USA-007) → **Pendiente de sincronización** (si no hay conectividad) → **Confirmado** (inmutable) o **Rechazado en sincronización** (si al validarse de nuevo ya no cumple las reglas; DF5-05). | No existen los estados «Ejecutado» ni «Auditado» (HD-03): confirmar es ejecutar, y auditar no modifica. La anulación es otro movimiento que neutraliza al primero. |
| **E-11 Documento de entrada** | **Pendiente de recepción** → **Recepción parcial** (interrumpida, continuable por otro usuario) → **Recibido conforme** o **Recibido con novedad** → **Confirmado** por una segunda persona (genera lote y movimiento de entrada). | Un sobrante detiene la confirmación hasta la autorización del Jefe. |
| **E-12 Solicitud de salida** | **Solicitada** → **Autorizada** (reserva) → **En preparación** (escaneo validado) → **Ejecutada** (movimiento de salida, reserva liberada). | Caminos alternos: **Rechazada** por el autorizador; **Vencida** si no se ejecuta en plazo (reserva liberada); **Cancelada**. |
| **E-13 Transferencia** | **Pendiente de despacho** (reserva en origen) → **En tránsito** (despacho confirmado) → **Completada** (recepción conforme). | **Con diferencia** hasta que el Jefe resuelva; **Cancelada** antes del despacho (Coordinador) o en tránsito (solo Jefe, con retorno). |
| **E-14 Solicitud de ajuste** | **Pendiente de aprobación** → **Aprobada** (movimiento de ajuste aplicado) o **Rechazada** (con justificación). | **Escalada** si el aprobador es el solicitante o vence el plazo; **Bloqueada** si no existe nivel superior. |
| **E-15 Conteo** | **Programado** → **En ejecución** (existencia congelada, tareas asignadas; en el general, movimientos bloqueados) → **En conciliación** (diferencias, segundos conteos) → **Cerrado** por el Jefe (ajustes derivados, exactitud calculada). | **Abortado** (conteos parciales conservados sin ajustes) o **Vencido** (existencia congelada liberada). |
| **E-17 Novedad** | **Abierta** → acción determinada por el Coordinador → **Cerrada resuelta** (vinculada al movimiento que la resuelve). | **Escalada** al Jefe por vencimiento; **Cerrada improcedente** si se reportó por error. Nunca se elimina. |
| **E-18 Alerta** | **Activa** → **Atendida** (acción registrada) o **Descartada** (con motivo). | **Escalada** si es crítica y vence el plazo; **Cerrada sin atención** si la condición cesa antes de atenderse. |
| **E-19 Usuario** | **Activo** (cambio de contraseña en primer acceso) → **Bloqueado** tras intentos fallidos → **Activo** al restablecerse → **Inactivo** al desactivarse → **Activo** al reactivarse. | Sus movimientos conservan su identidad y el rol que tenía cuando ocurrieron. |
| **E-22 Observación de auditoría** | **Abierta** al registrarse → **Cerrada** con respuesta. | Quién responde no está definido en el SPEC (DEC-04). |
| **E-26 Cierre de jornada** | **Abierta** durante la jornada → **Cerrada** con pendientes traspasados. | **Omitida** si no se ejecuta; bloqueada mientras haya registros sin sincronizar. ⚠️ DEC-05. |

**Principios comunes a todos los ciclos:**

1. **Nada termina borrado.** El final de todo ciclo es un estado inactivo o cerrado; la identidad persiste (RN-MAE-007).
2. **Lo confirmado no retrocede.** Movimientos, conteos cerrados y ajustes aplicados no vuelven atrás; se corrigen con hechos nuevos (RN-INT-002, RN-CNT-004, RN-AJU-007).
3. **Todo paso tiene actor.** Cada transición la ejecuta un usuario identificado o el Sistema (RN-INT-001).


---

**ESTADO DEL CAPÍTULO — 7**

| | |
|---|---|
| **Completado** | 17 ciclos de vida especificados, sin diagramas |
| **Riesgos** | Estados nuevos sin respaldo explícito en el SPEC (HD-19) |
| **Dependencias** | Cap. 8 |
| **Hallazgos** | HD-02, HD-03, HD-07, HD-19 |

---

# CAPÍTULO 8 — ESTADOS OFICIALES

> Estados válidos del dominio y transiciones permitidas. **Toda transición no listada está prohibida.** «—» como origen indica el nacimiento del elemento. La columna «Evento» remite al EVENT_CATALOG.

## 8.1 Resumen

| Máquina | Elemento | Estados | Transiciones | Origen |
|---|---|:--:|:--:|---|
| SM-01 | Referencia (E-01) | 2 | 3 | SPEC CD-02, M-03 |
| SM-02 | Categoría (E-03) | 2 | 2 | SPEC HU-015 (SRS HU-CAT-006) |
| SM-03 | Ubicación (E-07) | 2 | 3 | SPEC CD-14, M-05 |
| SM-04 | Lote (E-04) | 2 | 3 | SPEC M-04; nombre «Habilitado» nuevo (HD-19) |
| SM-05 | Identificador QR (E-09) | 4 | 5 | SPEC CD-08, PN-02 |
| SM-06 | Estado de inventario (porción de existencia de E-08) | 5 | 14 | SPEC CD-44; CD-16, CD-17 |
| SM-07 | Movimiento (E-10) | 4 | 5 | SPEC CD-28, RN-054 (SRS RN-INT-003); HD-03; «Rechazado en sincronización» nuevo (DF5-05) |
| SM-08 | Documento de entrada (E-11) | 6 | 11 | SPEC PN-01, M-07 |
| SM-09 | Solicitud de salida (E-12) | 7 | 7 | SPEC PN-10, M-08 |
| SM-10 | Transferencia (E-13) | 5 | 8 | SPEC PN-06, M-09 |
| SM-11 | Solicitud de ajuste (E-14) | 5 | 9 | SPEC PN-07, M-10 |
| SM-12 | Conteo (E-15) | 6 | 9 | SPEC CD-38, PN-08, PN-09 |
| SM-13 | Tarea de conteo (E-16) | 2 | 3 | SPEC CD-41, HU-059 (SRS HU-CNT-002) |
| SM-14 | Novedad (E-17) | 4 | 6 | SPEC PN-12, M-12 |
| SM-15 | Alerta (E-18) | 5 | 8 | SPEC PN-11, M-15 |
| SM-16 | Usuario (E-19) | 3 | 6 | SPEC M-01, M-02 |
| SM-17 | Sesión (E-20) | 2 | 4 | SPEC M-01 |
| SM-18 | Observación de auditoría (E-22) | 2 | 2 | SPEC RN-064 (SRS RN-AUD-002) |
| SM-19 | Tarea operativa (E-23) | 3 | 4 | SPEC M-20; «Cancelada» nuevo |
| SM-20 | Motivo tipificado (E-24) | 2 | 3 | SPEC HU-099 (SRS HU-PAR-002) |
| SM-21 | Cierre de jornada (E-26) ⚠️ | 3 | 2 | SPEC PN-14 (sin RF: DEC-05) |
| **Total** | 21 máquinas | **76** | **117** | |

## 8.2 SM-01 · Referencia (E-01)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Activa** | Admite operaciones nuevas | inicial |
| **Inactiva** | No aparece en operaciones nuevas; su historia es consultable | — |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Activa | EV-CAT-001 | Administrador / Jefe | Código único (RN-MAE-001) |
| Activa | Inactiva | EV-CAT-005 | Administrador / Jefe | Existencia = 0 (RN-MAE-003) |
| Inactiva | Activa | EV-CAT-006 | Administrador / Jefe | RN-MAE-009 |

## 8.3 SM-02 · Categoría (E-03)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Activa** | Agrupa referencias | inicial |
| **Inactiva** | No se asigna a referencias nuevas | — |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Activa | EV-CAT-008 | Administrador / Jefe | — |
| Activa | Inactiva | EV-CAT-009 | Administrador / Jefe | RN-MAE-007 |

## 8.4 SM-03 · Ubicación (E-07)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Activa** | Puede recibir mercancía dentro de su capacidad | inicial |
| **Inactiva** | No se propone ni se acepta como destino | — |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Activa | EV-BOD-003 | Administrador | Código único en la bodega (RN-MAE-006) |
| Activa | Inactiva | EV-BOD-005 | Administrador | Sin existencia (RN-MAE-005) |
| Inactiva | Activa | EV-BOD-006 | Administrador | RN-MAE-009 |

## 8.5 SM-04 · Lote (E-04)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Habilitado** | Su existencia sigue los estados normales | inicial |
| **Inmovilizado** | Toda su existencia está inmovilizada en todas sus ubicaciones | — |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Habilitado | EV-LOT-001 | Sistema | Entrada confirmada (RN-LOT-001) |
| Habilitado | Inmovilizado | EV-LOT-002 | Jefe / Administrador | Motivo tipificado (RN-LOT-003) |
| Inmovilizado | Habilitado | EV-LOT-003 | Jefe / Administrador | Motivo tipificado (RN-LOT-004) |

## 8.6 SM-05 · Identificador QR (E-09)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Generado** | Emitido e impreso, sin verificar su legibilidad | inicial |
| **Activo** | Resuelve escaneos | — |
| **Reemplazado** | Sustituido por reimpresión; consultable | final |
| **Anulado** | Sin efecto; consultable | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Generado | EV-QRC-001 | Sistema / Coordinador | Código nunca emitido (RN-IDE-002) |
| Generado | Activo | EV-QRC-003 | Auxiliar | Escaneo de verificación exitoso (PN-02) |
| Generado | Reemplazado | EV-QRC-004 | Coordinador | Impresión ilegible (PN-02 E-01) |
| Activo | Reemplazado | EV-QRC-004 | Coordinador / Auxiliar | Motivo de reimpresión (RN-IDE-004) |
| Activo | Anulado | EV-QRC-005 | Coordinador | — |

## 8.7 SM-06 · Estado de inventario (porción de existencia de E-08)

| Estado | Significado | Tipo |
|---|---|:--:|
| **En recepción** | En el inventario, no disponible; solo admite el movimiento interno de ubicación (RN-EXI-007) | inicial |
| **Disponible** | Puede comprometerse | — |
| **Reservado** | Comprometido por salida o transferencia | — |
| **En tránsito** | Despachado, no recibido | — |
| **Inmovilizado** | Bloqueado por daño, verificación, auditoría o lote | — |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | En recepción | EV-ENT-012 | Coordinador | Entrada confirmada (RN-EXI-007, DF5-02) |
| — | Inmovilizado | EV-ENT-011 | Auxiliar | Mercancía dañada a cuarentena (RN-ENT-006) |
| En recepción | Disponible | EV-INV-001 | Auxiliar | Movimiento interno de primera ubicación confirmado hacia una ubicación activa con capacidad fuera de la zona de recepción: la porción pasa de la unidad de recepción a la unidad destino (RN-MOV-010, RN-MOV-002) |
| En recepción | En tránsito | EV-MOV-003 | Auxiliar | Primera ubicación interrumpida (RN-MOV-006, RN-MOV-010) |
| Disponible | Reservado | EV-INV-003 | Sistema | Salida autorizada o transferencia creada (RN-EXI-004) |
| Reservado | Disponible | EV-INV-004 | Sistema | Cancelación (RN-MOV-009) o vencimiento (RN-SAL-005) |
| Reservado | En tránsito | EV-MOV-006 | Auxiliar | Despacho confirmado (RN-EXI-005) |
| Disponible | En tránsito | EV-MOV-003 | Auxiliar | Movimiento interno interrumpido (RN-MOV-006) |
| En tránsito | Disponible | EV-MOV-007 | Auxiliar | Recepción confirmada en destino; también al completarse un movimiento interno interrumpido (EV-MOV-001 o, si era la primera ubicación, EV-INV-001) |
| En tránsito | En recepción | EV-MOV-007 | Auxiliar (destino) | Destino sin capacidad: se recibe en la zona de recepción del destino y se ubica después como primera ubicación (PN-06 E-07, CD-16, RN-MOV-010) |
| En tránsito | Disponible | EV-MOV-013 | Jefe | Cancelación en tránsito con retorno al origen |
| Disponible | Inmovilizado | EV-LOT-002 | Jefe / Administrador | Inmovilización del lote (RN-LOT-003) |
| Inmovilizado | Disponible | EV-LOT-003 | Jefe / Administrador | Liberación (RN-LOT-004) |
| Reservado | — (sale) | EV-SAL-006 | Auxiliar | Salida ejecutada: la porción deja el inventario |

## 8.8 SM-07 · Movimiento (E-10)

| Estado | Significado | Tipo |
|---|---|:--:|
| **En registro** | Preparado por su autor; corregible antes de confirmar | inicial |
| **Pendiente de sincronización** | Registrado sin conectividad; no confirma documentos | — |
| **Confirmado** | Inmutable; forma parte del kardex | final |
| **Rechazado en sincronización** | Al validarse de nuevo ya no cumplía las reglas; no se aplicó y queda con su motivo | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | En registro | — | Usuario | Acción del usuario (no es evento del dominio) |
| En registro | Pendiente de sincronización | EV-TRZ-003 | Sistema | Sin conectividad (RN-INT-003) |
| Pendiente de sincronización | Confirmado | EV-TRZ-004 | Sistema | Validado de nuevo contra el estado vigente y todas las reglas (RN-INT-008) |
| Pendiente de sincronización | Rechazado en sincronización | EV-TRZ-007 | Sistema | Ya no cumple alguna regla o invariante (RN-INT-008) |
| En registro | Confirmado | EV-TRZ-001 | Usuario / Sistema | Reglas del tipo de movimiento satisfechas |

## 8.9 SM-08 · Documento de entrada (E-11)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Pendiente de recepción** | Creado, esperando la mercancía | inicial |
| **Recepción parcial** | Recepción interrumpida, continuable | — |
| **Recibido conforme** | Recibido = esperado | — |
| **Recibido con novedad** | Faltante, sobrante o daño registrados | — |
| **Confirmado** | Entrada incorporada al inventario | final |
| **Reversado** | Anulado antes de confirmarse | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Pendiente de recepción | EV-ENT-001 | Coordinador | Solo referencias activas (RN-ENT-001) |
| Pendiente de recepción | Recepción parcial | EV-ENT-005 | Auxiliar | — |
| Recepción parcial | Recepción parcial | EV-ENT-006 | Auxiliar | Continuación por otro usuario |
| Pendiente de recepción | Recibido conforme | EV-ENT-007 | Sistema | Recibido = esperado (RN-ENT-003) |
| Recepción parcial | Recibido conforme | EV-ENT-007 | Sistema | RN-ENT-003 |
| Pendiente de recepción | Recibido con novedad | EV-ENT-008 | Sistema | Faltante (RN-ENT-004) |
| Pendiente de recepción | Recibido con novedad | EV-ENT-009 | Sistema | Sobrante (RN-ENT-005) |
| Recepción parcial | Recibido con novedad | EV-ENT-008 | Sistema | Faltante (RN-ENT-004) |
| Recibido conforme | Confirmado | EV-ENT-012 | Coordinador | Confirmador ≠ receptor (RN-ENT-007); sincronizado (RN-INT-003) |
| Recibido con novedad | Confirmado | EV-ENT-012 | Coordinador | Sobrante autorizado (EV-ENT-010) si lo hay |
| Pendiente de recepción | Reversado | EV-ENT-015 | Coordinador | Sin confirmar (función de M-07, sin RF: HD-19) |

## 8.10 SM-09 · Solicitud de salida (E-12)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Solicitada** | Pendiente de autorización | inicial |
| **Autorizada** | Existencia reservada; tarea de preparación generada | — |
| **En preparación** | Escaneo de toma en curso | — |
| **Ejecutada** | Movimiento de salida confirmado | final |
| **Rechazada** | No autorizada | final |
| **Vencida** | No ejecutada en plazo; reserva liberada | final |
| **Cancelada** | Retirada antes de ejecutarse; reserva liberada | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Solicitada | EV-SAL-001 | Jefe / Coordinador | Motivo tipificado; disponibilidad verificada (RN-SAL-002, RN-EXI-003) |
| Solicitada | Autorizada | EV-SAL-003 | Jefe / Coordinador | Coordinador solo bajo su umbral (RN-SAL-001); nunca la propia (RN-AJU-001) |
| Solicitada | Rechazada | EV-SAL-009 | Jefe / Coordinador | — |
| Autorizada | En preparación | EV-SAL-010 | Auxiliar | Primer escaneo válido (RN-SAL-004) |
| En preparación | Ejecutada | EV-SAL-006 | Auxiliar | Preparación completa |
| Autorizada | Vencida | EV-INV-005 | Sistema | Plazo de reserva vencido (RN-SAL-005) |
| Autorizada | Cancelada | EV-SAL-011 | Jefe / Coordinador | Actor no definido en el SPEC (HD-19) |

## 8.11 SM-10 · Transferencia (E-13)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Pendiente de despacho** | Existencia reservada en origen | inicial |
| **En tránsito** | Despachada, no recibida | — |
| **Con diferencia** | Recibido ≠ despachado; espera resolución del Jefe | — |
| **Completada** | Recibida y conciliada | final |
| **Cancelada** | Anulada con reserva liberada o retorno | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Pendiente de despacho | EV-MOV-005 | Coordinador | Disponible suficiente (RN-EXI-003) |
| Pendiente de despacho | En tránsito | EV-MOV-006 | Auxiliar origen | Escaneo de despacho |
| Pendiente de despacho | Cancelada | EV-MOV-012 | Coordinador | Motivo (RN-MOV-009) |
| En tránsito | Completada | EV-MOV-007 | Auxiliar destino | Recibido = despachado (RN-MOV-007) |
| En tránsito | Con diferencia | EV-MOV-008 | Sistema | Recibido < despachado (RN-MOV-007) |
| En tránsito | En tránsito | EV-MOV-009 | Sistema | Recibido > despachado: recepción rechazada (RN-MOV-007) |
| En tránsito | Cancelada | EV-MOV-013 | Jefe | Solo el Jefe; retorno al origen (RN-MOV-009) |
| Con diferencia | Completada | EV-MOV-010 | Jefe | Resolución documentada |

## 8.12 SM-11 · Solicitud de ajuste (E-14)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Pendiente de aprobación** | Enrutada al aprobador por clasificación | inicial |
| **Escalada** | Enviada al nivel superior | — |
| **Bloqueada** | Sin nivel superior disponible; Administrador notificado | — |
| **Aprobada** | Movimiento de ajuste aplicado | final |
| **Rechazada** | Con justificación; existencia sin cambios | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Pendiente de aprobación | EV-AJU-001 | Coordinador | Motivo tipificado y evidencia si se exige (RN-AJU-003) |
| Pendiente de aprobación | Escalada | EV-AJU-003 | Sistema | Aprobador = solicitante (RN-AJU-001) |
| Pendiente de aprobación | Escalada | EV-AJU-008 | Sistema | Plazo vencido (RN-AJU-005) |
| Escalada | Bloqueada | EV-AJU-010 | Sistema | Sin nivel superior (RN-AJU-001) |
| Pendiente de aprobación | Aprobada | EV-AJU-004 | Jefe / Administrador | Aprobador ≠ solicitante; no negativo (RN-EXI-001) |
| Escalada | Aprobada | EV-AJU-004 | Administrador | Idem |
| Bloqueada | Aprobada | EV-AJU-004 | Administrador | Resolución del Administrador notificado (RN-AJU-001) |
| Pendiente de aprobación | Rechazada | EV-AJU-006 | Jefe / Administrador | Justificación (RN-AJU-006) |
| Escalada | Rechazada | EV-AJU-006 | Administrador | Justificación (RN-AJU-006) |

## 8.13 SM-12 · Conteo (E-15)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Programado** | Definido su alcance y, en el general, su corte | inicial |
| **En ejecución** | Existencia congelada; tareas asignadas | — |
| **En conciliación** | Diferencias clasificadas; segundos conteos | — |
| **Cerrado** | Cerrado por el Jefe; no se reabre | final |
| **Abortado** | Sin ajustes; conteos parciales conservados | final |
| **Vencido** | Plazo máximo excedido; congelamiento liberado | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Programado | EV-CNT-001 | Coordinador | Conteo cíclico |
| — | Programado | EV-CNT-002 | Jefe | Conteo general con fecha de corte |
| Programado | En ejecución | EV-CNT-003 | Sistema | Congelamiento (RN-CNT-001); en el general, bloqueo (RN-CNT-006) |
| En ejecución | En conciliación | EV-CNT-008 | Sistema | Líneas clasificadas |
| En conciliación | Cerrado | EV-CNT-014 | Jefe | Cerrador ≠ ejecutor (RN-CNT-003); cobertura completa en el general (RN-CNT-007); aviso previo si diferencia crítica (RN-CNT-008) |
| En ejecución | Abortado | EV-CNT-017 | Jefe | PN-09 E-04 |
| En conciliación | Abortado | EV-CNT-017 | Jefe | PN-09 E-04 |
| Programado | Vencido | EV-CNT-018 | Sistema | Plazo (RN-CNT-005) |
| En ejecución | Vencido | EV-CNT-018 | Sistema | Plazo máximo (RN-CNT-005) |

## 8.14 SM-13 · Tarea de conteo (E-16)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Asignada** | Pendiente de contar; corregible antes de confirmar | inicial |
| **Confirmada** | Conteo registrado y confirmado | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Asignada | EV-CNT-006 | Sistema / Coordinador | Segundo conteo: contador distinto (RN-CNT-003) |
| Asignada | Asignada | EV-CNT-011 | Coordinador | Reasignación; no viola RN-CNT-003 |
| Asignada | Confirmada | EV-CNT-007 | Auxiliar | Cantidad esperada oculta (RN-CNT-002) |

## 8.15 SM-14 · Novedad (E-17)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Abierta** | Reportada, dirigida al Coordinador | inicial |
| **Escalada** | Dirigida al Jefe por vencimiento | — |
| **Cerrada resuelta** | Vinculada a su resolución | final |
| **Cerrada improcedente** | Reportada por error, con justificación | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Abierta | EV-NOV-001 | Auxiliar (o cualquier rol operativo) | Sin novedad abierta sobre la misma unidad (RN-NOV-003) |
| Abierta | Escalada | EV-NOV-006 | Sistema | Plazo vencido (RN-NOV-002) |
| Abierta | Cerrada resuelta | EV-NOV-004 | Coordinador | Constancia de resolución |
| Escalada | Cerrada resuelta | EV-NOV-004 | Jefe | Constancia de resolución |
| Abierta | Cerrada improcedente | EV-NOV-005 | Coordinador | Justificación; nunca se elimina (RN-MAE-007) |
| Escalada | Cerrada improcedente | EV-NOV-005 | Jefe | Justificación |

## 8.16 SM-15 · Alerta (E-18)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Activa** | Condición vigente, dirigida a un rol | inicial |
| **Escalada** | Crítica no atendida en plazo | — |
| **Atendida** | Acción registrada | final |
| **Descartada** | Cerrada con motivo | final |
| **Cerrada sin atención** | La condición cesó sin que nadie actuara | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Activa | EV-ALE-001 | Sistema | Una sola por condición (RN-ALE-001); destinatario por rol (RN-ALE-005) |
| Activa | Escalada | EV-ALE-004 | Sistema | Severidad crítica y plazo vencido (RN-ALE-002) |
| Activa | Atendida | EV-ALE-002 | Jefe / Coordinador | Acción registrada |
| Escalada | Atendida | EV-ALE-002 | Rol superior | Acción registrada |
| Activa | Descartada | EV-ALE-003 | Jefe / Coordinador | Motivo obligatorio (RN-ALE-004) |
| Escalada | Descartada | EV-ALE-003 | Rol superior | Motivo obligatorio (RN-ALE-004) |
| Activa | Cerrada sin atención | EV-ALE-005 | Sistema | La condición cesó (RN-ALE-003) |
| Escalada | Cerrada sin atención | EV-ALE-005 | Sistema | La condición cesó (RN-ALE-003) |

## 8.17 SM-16 · Usuario (E-19)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Activo** | Puede autenticarse | inicial |
| **Bloqueado** | Bloqueado por intentos fallidos | — |
| **Inactivo** | Desactivado; su historia se conserva | — |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Activo | EV-USR-001 | Administrador | Uno de los cinco roles (DC-04) |
| Activo | Bloqueado | EV-ACC-003 | Sistema | Intentos fallidos consecutivos ≥ umbral |
| Bloqueado | Activo | EV-ACC-007 | Administrador | Cambio de contraseña forzado |
| Activo | Inactivo | EV-USR-004 | Administrador | No es el último Administrador activo ni el último Jefe de su bodega (RN-MAE-004) |
| Bloqueado | Inactivo | EV-USR-004 | Administrador | RN-MAE-004 |
| Inactivo | Activo | EV-USR-005 | Administrador | RN-MAE-009 |

## 8.18 SM-17 · Sesión (E-20)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Activa** | Atribuye las acciones al usuario | inicial |
| **Cerrada** | Manual, por inactividad o por cambio de contraseña | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Activa | EV-ACC-001 | Usuario | Credenciales válidas |
| Activa | Cerrada | EV-ACC-004 | Sistema | Inactividad configurada, con aviso previo |
| Activa | Cerrada | EV-ACC-005 | Usuario | — |
| Activa | Cerrada | EV-ACC-006 | Sistema | Cambio de contraseña cierra las demás sesiones |

## 8.19 SM-18 · Observación de auditoría (E-22)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Abierta** | Registrada por el Auditor | inicial |
| **Cerrada** | Con respuesta; nunca se elimina | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Abierta | EV-AUD-001 | Auditor | Registro separado (RN-AUD-002) |
| Abierta | Cerrada | EV-AUD-002 | Por definir (DEC-04) | Respuesta registrada |

## 8.20 SM-19 · Tarea operativa (E-23)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Pendiente** | Asignada a un responsable | inicial |
| **Completada** | Cerrada por el hecho asociado | final |
| **Cancelada** | Su operación de origen se canceló | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Pendiente | EV-TAR-001 | Sistema | Responsable identificado |
| Pendiente | Pendiente | EV-TAR-003 | Coordinador | Reasignación; ambos responsables registrados |
| Pendiente | Completada | EV-TAR-002 | Sistema | Hecho asociado confirmado (RF-TAR-003) |
| Pendiente | Cancelada | EV-TAR-006 | Sistema | Operación de origen cancelada o vencida (HD-19) |

## 8.21 SM-20 · Motivo tipificado (E-24)

| Estado | Significado | Tipo |
|---|---|:--:|
| **Activo** | Seleccionable en operaciones nuevas | inicial |
| **Inactivo** | Visible solo en el histórico | — |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| — | Activo | EV-PAR-002 | Administrador | — |
| Activo | Inactivo | EV-PAR-003 | Administrador | RN-MAE-007 |
| Inactivo | Activo | EV-PAR-005 | Administrador | RN-MAE-009 |

## 8.22 SM-21 · Cierre de jornada (E-26) ⚠️

| Estado | Significado | Tipo |
|---|---|:--:|
| **Abierta** | Jornada en curso | inicial |
| **Cerrada** | Pendientes consolidados y traspasados | final |
| **Omitida** | No se ejecutó el cierre | final |

| Desde | Hacia | Evento | Actor | Condición (guarda) |
|---|---|---|---|---|
| Abierta | Cerrada | EV-JOR-003 | Jefe / Coordinador | Sin registros pendientes de sincronización (RN-INT-003) |
| Abierta | Omitida | EV-JOR-005 | Sistema | Fin de jornada sin cierre |


---

**ESTADO DEL CAPÍTULO — 8**

| | |
|---|---|
| **Completado** | 21 máquinas de estado, 76 estados oficiales y 117 transiciones permitidas |
| **Riesgos** | Nombres de estado nuevos (Habilitado, Generado, Reversado, Cancelada) pendientes de confirmación |
| **Dependencias** | Cap. 7, EVENT_CATALOG |
| **Hallazgos** | HD-03, HD-07, HD-19 |

---

# CAPÍTULO 9 — MATRICES DEL DOMINIO (A, B, C)

> Las matrices D (Evento ↔ Historia de usuario) y E (Evento ↔ RF) están en el EVENT_CATALOG, Cap. 6.

## Matriz A — Entidad ↔ Evento

**O** = eventos que la entidad origina · **A** = eventos que la afectan sin originarlos.

| Entidad | O | Eventos que origina | A | Eventos que la afectan |
|---|:--:|---|:--:|---|
| **E-01 Referencia** | 6 | EV-CAT-001, EV-CAT-002, EV-CAT-003, EV-CAT-005, EV-CAT-006, EV-CAT-007 | 0 | — |
| **E-02 SKU** | 4 | EV-CAT-004, EV-INV-006, EV-INV-007, EV-INV-008 | 2 | EV-CAT-002, EV-CAT-007 |
| **E-03 Categoría** | 2 | EV-CAT-008, EV-CAT-009 | 0 | — |
| **E-04 Lote** | 3 | EV-LOT-002, EV-LOT-003, EV-LOT-004 | 3 | EV-QRC-003, EV-ENT-012, EV-LOT-001 |
| **E-05 Bodega** | 4 | EV-BOD-001, EV-BOD-002, EV-BOD-003, EV-BOD-008 | 0 | — |
| **E-06 Zona** | 1 | EV-BOD-007 | 1 | EV-BOD-002 |
| **E-07 Ubicación** | 5 | EV-BOD-004, EV-BOD-005, EV-BOD-006, EV-QRC-007, EV-INV-009 | 3 | EV-BOD-003, EV-INV-001, EV-MOV-001 |
| **E-08 Unidad de Inventario** | 5 | EV-INV-002, EV-INV-003, EV-INV-004, EV-TRZ-005, EV-TRZ-006 | 23 | EV-ENT-011, EV-ENT-012, EV-LOT-002, EV-LOT-003, EV-INV-001, EV-INV-005, EV-MOV-001, EV-MOV-002, EV-MOV-003, EV-MOV-005, EV-MOV-006, EV-MOV-007, EV-MOV-012, EV-MOV-013, EV-SAL-003, EV-SAL-006, EV-SAL-007, EV-SAL-008, EV-SAL-011, EV-AJU-005, EV-NOV-007, EV-TRZ-001, EV-TRZ-002 |
| **E-09 Identificador QR** | 6 | EV-QRC-001, EV-QRC-002, EV-QRC-003, EV-QRC-004, EV-QRC-005, EV-QRC-006 | 2 | EV-QRC-007, EV-NOV-007 |
| **E-10 Movimiento** | 10 | EV-INV-001, EV-MOV-001, EV-MOV-002, EV-MOV-003, EV-MOV-004, EV-TRZ-001, EV-TRZ-002, EV-TRZ-003, EV-TRZ-004, EV-TRZ-007 | 10 | EV-ENT-012, EV-ENT-013, EV-MOV-007, EV-MOV-013, EV-SAL-006, EV-SAL-008, EV-AJU-005, EV-CNT-004, EV-CNT-005, EV-CNT-016 |
| **E-11 Documento de entrada** | 16 | EV-ENT-001, EV-ENT-002, EV-ENT-003, EV-ENT-004, EV-ENT-005, EV-ENT-006, EV-ENT-007, EV-ENT-008, EV-ENT-009, EV-ENT-010, EV-ENT-011, EV-ENT-012, EV-ENT-013, EV-ENT-014, EV-ENT-015, EV-LOT-001 | 0 | — |
| **E-12 Solicitud de salida** | 12 | EV-INV-005, EV-SAL-001, EV-SAL-002, EV-SAL-003, EV-SAL-004, EV-SAL-005, EV-SAL-006, EV-SAL-007, EV-SAL-008, EV-SAL-009, EV-SAL-010, EV-SAL-011 | 0 | — |
| **E-13 Transferencia** | 9 | EV-MOV-005, EV-MOV-006, EV-MOV-007, EV-MOV-008, EV-MOV-009, EV-MOV-010, EV-MOV-011, EV-MOV-012, EV-MOV-013 | 0 | — |
| **E-14 Solicitud de ajuste** | 12 | EV-AJU-001, EV-AJU-002, EV-AJU-003, EV-AJU-004, EV-AJU-005, EV-AJU-006, EV-AJU-007, EV-AJU-008, EV-AJU-009, EV-AJU-010, EV-TAR-004, EV-TAR-005 | 2 | EV-CNT-014, EV-NOV-007 |
| **E-15 Conteo** | 18 | EV-CNT-001, EV-CNT-002, EV-CNT-003, EV-CNT-004, EV-CNT-005, EV-CNT-006, EV-CNT-008, EV-CNT-009, EV-CNT-010, EV-CNT-012, EV-CNT-013, EV-CNT-014, EV-CNT-015, EV-CNT-016, EV-CNT-017, EV-CNT-018, EV-ALE-007, EV-REP-005 | 0 | — |
| **E-16 Tarea de conteo** | 2 | EV-CNT-007, EV-CNT-011 | 2 | EV-CNT-006, EV-CNT-009 |
| **E-17 Novedad** | 7 | EV-NOV-001, EV-NOV-002, EV-NOV-003, EV-NOV-004, EV-NOV-005, EV-NOV-006, EV-NOV-007 | 3 | EV-ENT-011, EV-MOV-008, EV-TRZ-007 |
| **E-18 Alerta** | 6 | EV-ALE-001, EV-ALE-002, EV-ALE-003, EV-ALE-004, EV-ALE-005, EV-ALE-006 | 13 | EV-LOT-004, EV-INV-006, EV-INV-007, EV-INV-008, EV-INV-009, EV-MOV-004, EV-MOV-011, EV-AJU-008, EV-AJU-009, EV-CNT-018, EV-NOV-006, EV-ALE-007, EV-JOR-005 |
| **E-19 Usuario** | 13 | EV-ACC-001, EV-ACC-002, EV-ACC-003, EV-ACC-006, EV-ACC-007, EV-USR-001, EV-USR-002, EV-USR-003, EV-USR-004, EV-USR-005, EV-USR-006, EV-AUD-003, EV-AUD-004 | 3 | EV-BOD-007, EV-TAR-004, EV-TAR-005 |
| **E-20 Sesión** | 2 | EV-ACC-004, EV-ACC-005 | 3 | EV-ACC-001, EV-ACC-006, EV-USR-004 |
| **E-21 Registro de bitácora** | 3 | EV-REP-001, EV-AUD-005, EV-AUD-006 | 2 | EV-AUD-003, EV-AUD-004 |
| **E-22 Observación de auditoría** | 2 | EV-AUD-001, EV-AUD-002 | 0 | — |
| **E-23 Tarea operativa** | 4 | EV-TAR-001, EV-TAR-002, EV-TAR-003, EV-TAR-006 | 2 | EV-SAL-003, EV-JOR-002 |
| **E-24 Motivo tipificado** | 3 | EV-PAR-002, EV-PAR-003, EV-PAR-005 | 0 | — |
| **E-25 Parámetro de configuración** | 5 | EV-REP-002, EV-REP-003, EV-REP-004, EV-PAR-001, EV-PAR-004 | 2 | EV-ALE-006, EV-REP-005 |
| **E-26 Cierre de jornada** | 5 | EV-JOR-001, EV-JOR-002, EV-JOR-003, EV-JOR-004, EV-JOR-005 | 0 | — |

## Matriz B — Entidad ↔ Regla

Reglas asociadas a la entidad (ficha) más las citadas por los eventos que origina.

| Entidad | N.º | Reglas (SRS) |
|---|:--:|---|
| **E-01 Referencia** | 9 | RN-ENT-001, RN-INT-007, RN-LOT-002, RN-MAE-001, RN-MAE-002, RN-MAE-003, RN-MAE-007, RN-MAE-008, RN-MAE-009 |
| **E-02 SKU** | 4 | RN-ALE-001, RN-ALE-005, RN-AUD-004, RN-LOT-002 |
| **E-03 Categoría** | 3 | RN-MAE-007, RN-MAE-008, RN-MOV-001 |
| **E-04 Lote** | 8 | RN-EXI-006, RN-IDE-001, RN-LOT-001, RN-LOT-002, RN-LOT-003, RN-LOT-004, RN-LOT-005, RN-MAE-006 |
| **E-05 Bodega** | 4 | RN-EXI-002, RN-MAE-004, RN-MAE-006, RN-MOV-001 |
| **E-06 Zona** | 2 | RN-ALE-005, RN-EXI-002 |
| **E-07 Ubicación** | 12 | RN-ALE-001, RN-EXI-002, RN-EXI-007, RN-IDE-002, RN-MAE-005, RN-MAE-006, RN-MAE-007, RN-MAE-009, RN-MOV-001, RN-MOV-002, RN-MOV-005, RN-MOV-010 |
| **E-08 Unidad de Inventario** | 15 | RN-AUD-005, RN-EXI-001, RN-EXI-002, RN-EXI-003, RN-EXI-004, RN-EXI-005, RN-EXI-006, RN-EXI-007, RN-IDE-001, RN-INT-004, RN-INT-005, RN-LOT-001, RN-MOV-003, RN-MOV-009, RN-MOV-010 |
| **E-09 Identificador QR** | 4 | RN-IDE-001, RN-IDE-002, RN-IDE-003, RN-IDE-004 |
| **E-10 Movimiento** | 18 | RN-AJU-007, RN-CNT-006, RN-EXI-001, RN-EXI-002, RN-EXI-003, RN-EXI-005, RN-EXI-006, RN-INT-001, RN-INT-002, RN-INT-003, RN-INT-004, RN-INT-008, RN-MOV-001, RN-MOV-002, RN-MOV-004, RN-MOV-005, RN-MOV-006, RN-MOV-010 |
| **E-11 Documento de entrada** | 19 | RN-AJU-001, RN-ENT-001, RN-ENT-002, RN-ENT-003, RN-ENT-004, RN-ENT-005, RN-ENT-006, RN-ENT-007, RN-EXI-007, RN-INT-001, RN-INT-002, RN-INT-003, RN-INT-004, RN-INT-008, RN-LOT-001, RN-LOT-002, RN-MAE-006, RN-MAE-007, RN-SAL-007 |
| **E-12 Solicitud de salida** | 12 | RN-AJU-001, RN-EXI-001, RN-EXI-003, RN-EXI-004, RN-INT-002, RN-INT-004, RN-SAL-001, RN-SAL-002, RN-SAL-003, RN-SAL-004, RN-SAL-005, RN-SAL-006 |
| **E-13 Transferencia** | 7 | RN-EXI-003, RN-EXI-004, RN-EXI-005, RN-INT-002, RN-MOV-007, RN-MOV-008, RN-MOV-009 |
| **E-14 Solicitud de ajuste** | 10 | RN-AJU-001, RN-AJU-002, RN-AJU-003, RN-AJU-004, RN-AJU-005, RN-AJU-006, RN-AJU-007, RN-EXI-001, RN-EXI-006, RN-INT-004 |
| **E-15 Conteo** | 11 | RN-AJU-001, RN-ALE-001, RN-CNT-001, RN-CNT-002, RN-CNT-003, RN-CNT-004, RN-CNT-005, RN-CNT-006, RN-CNT-007, RN-CNT-008, RN-NOV-001 |
| **E-16 Tarea de conteo** | 2 | RN-CNT-002, RN-CNT-003 |
| **E-17 Novedad** | 6 | RN-AJU-003, RN-INT-008, RN-MAE-007, RN-NOV-001, RN-NOV-002, RN-NOV-003 |
| **E-18 Alerta** | 9 | RN-AJU-004, RN-ALE-001, RN-ALE-002, RN-ALE-003, RN-ALE-004, RN-ALE-005, RN-CNT-005, RN-LOT-005, RN-MOV-008 |
| **E-19 Usuario** | 6 | RN-AUD-002, RN-INT-001, RN-MAE-004, RN-MAE-006, RN-MAE-007, RN-MAE-009 |
| **E-20 Sesión** | 1 | RN-INT-001 |
| **E-21 Registro de bitácora** | 5 | RN-AJU-001, RN-AUD-001, RN-AUD-003, RN-AUD-004, RN-INT-001 |
| **E-22 Observación de auditoría** | 2 | RN-AUD-002, RN-MAE-007 |
| **E-23 Tarea operativa** | 2 | RN-CNT-003, RN-INT-001 |
| **E-24 Motivo tipificado** | 5 | RN-AJU-003, RN-MAE-007, RN-MAE-008, RN-MAE-009, RN-SAL-002 |
| **E-25 Parámetro de configuración** | 8 | RN-AJU-001, RN-AJU-002, RN-AUD-004, RN-CNT-003, RN-EXI-001, RN-INT-002, RN-MOV-008, RN-SAL-001 |
| **E-26 Cierre de jornada** | 2 | RN-INT-003, RN-MOV-006 |

## Matriz C — Entidad ↔ KPI

KPI alimentados por eventos que la entidad origina o que la afectan.

| Entidad | KPI |
|---|---|
| **E-01 Referencia** | — |
| **E-02 SKU** | KPI-16 Rotación por referencia, KPI-19 Alertas generadas y atendidas, KPI-21 Eventos de ruptura de stock |
| **E-03 Categoría** | — |
| **E-04 Lote** | KPI-05 Tiempo Medio de Registro de un Movimiento, KPI-11 Volumen de movimientos, KPI-12 Tiempo medio de recepción, KPI-17 Existencia sin movimiento |
| **E-05 Bodega** | KPI-10 Desviaciones de ubicación |
| **E-06 Zona** | — |
| **E-07 Ubicación** | KPI-05 Tiempo Medio de Registro de un Movimiento, KPI-10 Desviaciones de ubicación, KPI-11 Volumen de movimientos, KPI-18 Ocupación de bodega, KPI-19 Alertas generadas y atendidas |
| **E-08 Unidad de Inventario** | KPI-05 Tiempo Medio de Registro de un Movimiento, KPI-08 Frecuencia de Errores de Registro, KPI-09 Integridad del kardex, KPI-10 Desviaciones de ubicación, KPI-11 Volumen de movimientos, KPI-12 Tiempo medio de recepción, KPI-13 Tasa de merma, KPI-14 Volumen y magnitud de ajustes, KPI-15 Tiempo medio en tránsito, KPI-16 Rotación por referencia, KPI-17 Existencia sin movimiento, KPI-18 Ocupación de bodega, KPI-22 Tiempo medio de aprobación, KPI-23 Novedades reportadas y resueltas, KPI-24 Adopción del sistema |
| **E-09 Identificador QR** | — |
| **E-10 Movimiento** | KPI-05 Tiempo Medio de Registro de un Movimiento, KPI-08 Frecuencia de Errores de Registro, KPI-10 Desviaciones de ubicación, KPI-11 Volumen de movimientos, KPI-12 Tiempo medio de recepción, KPI-13 Tasa de merma, KPI-14 Volumen y magnitud de ajustes, KPI-15 Tiempo medio en tránsito, KPI-16 Rotación por referencia, KPI-17 Existencia sin movimiento, KPI-18 Ocupación de bodega, KPI-24 Adopción del sistema |
| **E-11 Documento de entrada** | KPI-05 Tiempo Medio de Registro de un Movimiento, KPI-11 Volumen de movimientos, KPI-12 Tiempo medio de recepción, KPI-23 Novedades reportadas y resueltas |
| **E-12 Solicitud de salida** | KPI-05 Tiempo Medio de Registro de un Movimiento, KPI-11 Volumen de movimientos, KPI-13 Tasa de merma, KPI-16 Rotación por referencia, KPI-22 Tiempo medio de aprobación |
| **E-13 Transferencia** | KPI-05 Tiempo Medio de Registro de un Movimiento, KPI-11 Volumen de movimientos, KPI-15 Tiempo medio en tránsito, KPI-19 Alertas generadas y atendidas, KPI-23 Novedades reportadas y resueltas |
| **E-14 Solicitud de ajuste** | KPI-01 Exactitud del Inventario, KPI-02 Exactitud Global del Inventario, KPI-08 Frecuencia de Errores de Registro, KPI-14 Volumen y magnitud de ajustes, KPI-19 Alertas generadas y atendidas, KPI-22 Tiempo medio de aprobación |
| **E-15 Conteo** | KPI-01 Exactitud del Inventario, KPI-02 Exactitud Global del Inventario, KPI-03 Cobertura de conteo, KPI-04 Diferencia neta de conteo, KPI-05 Tiempo Medio de Registro de un Movimiento, KPI-06 Tasa de segundo conteo, KPI-07 Movimientos sin identificador escaneado, KPI-08 Frecuencia de Errores de Registro, KPI-09 Integridad del kardex, KPI-10 Desviaciones de ubicación, KPI-11 Volumen de movimientos, KPI-12 Tiempo medio de recepción, KPI-13 Tasa de merma, KPI-14 Volumen y magnitud de ajustes, KPI-15 Tiempo medio en tránsito, KPI-16 Rotación por referencia, KPI-17 Existencia sin movimiento, KPI-18 Ocupación de bodega, KPI-19 Alertas generadas y atendidas, KPI-20 Tiempo medio de atención de alerta, KPI-21 Eventos de ruptura de stock, KPI-22 Tiempo medio de aprobación, KPI-23 Novedades reportadas y resueltas, KPI-24 Adopción del sistema |
| **E-16 Tarea de conteo** | KPI-03 Cobertura de conteo, KPI-06 Tasa de segundo conteo |
| **E-17 Novedad** | KPI-23 Novedades reportadas y resueltas |
| **E-18 Alerta** | KPI-01 Exactitud del Inventario, KPI-14 Volumen y magnitud de ajustes, KPI-15 Tiempo medio en tránsito, KPI-16 Rotación por referencia, KPI-17 Existencia sin movimiento, KPI-18 Ocupación de bodega, KPI-19 Alertas generadas y atendidas, KPI-20 Tiempo medio de atención de alerta, KPI-21 Eventos de ruptura de stock, KPI-22 Tiempo medio de aprobación, KPI-23 Novedades reportadas y resueltas |
| **E-19 Usuario** | KPI-22 Tiempo medio de aprobación |
| **E-20 Sesión** | — |
| **E-21 Registro de bitácora** | KPI-14 Volumen y magnitud de ajustes |
| **E-22 Observación de auditoría** | — |
| **E-23 Tarea operativa** | KPI-22 Tiempo medio de aprobación |
| **E-24 Motivo tipificado** | — |
| **E-25 Parámetro de configuración** | KPI-02 Exactitud Global del Inventario, KPI-03 Cobertura de conteo, KPI-04 Diferencia neta de conteo, KPI-05 Tiempo Medio de Registro de un Movimiento, KPI-06 Tasa de segundo conteo, KPI-07 Movimientos sin identificador escaneado, KPI-08 Frecuencia de Errores de Registro, KPI-09 Integridad del kardex, KPI-10 Desviaciones de ubicación, KPI-11 Volumen de movimientos, KPI-12 Tiempo medio de recepción, KPI-13 Tasa de merma, KPI-14 Volumen y magnitud de ajustes, KPI-15 Tiempo medio en tránsito, KPI-16 Rotación por referencia, KPI-17 Existencia sin movimiento, KPI-18 Ocupación de bodega, KPI-19 Alertas generadas y atendidas, KPI-20 Tiempo medio de atención de alerta, KPI-21 Eventos de ruptura de stock, KPI-22 Tiempo medio de aprobación, KPI-23 Novedades reportadas y resueltas, KPI-24 Adopción del sistema |
| **E-26 Cierre de jornada** | — |

**Vista inversa (KPI → entidades):**

| KPI | Nombre | Entidades |
|---|---|---|
| KPI-01 | Exactitud del Inventario | E-14, E-15, E-18 |
| KPI-02 | Exactitud Global del Inventario | E-14, E-15, E-25 |
| KPI-03 | Cobertura de conteo | E-15, E-16, E-25 |
| KPI-04 | Diferencia neta de conteo | E-15, E-25 |
| KPI-05 | Tiempo Medio de Registro de un Movimiento | E-04, E-07, E-08, E-10, E-11, E-12, E-13, E-15, E-25 |
| KPI-06 | Tasa de segundo conteo | E-15, E-16, E-25 |
| KPI-07 | Movimientos sin identificador escaneado | E-15, E-25 |
| KPI-08 | Frecuencia de Errores de Registro | E-08, E-10, E-14, E-15, E-25 |
| KPI-09 | Integridad del kardex | E-08, E-15, E-25 |
| KPI-10 | Desviaciones de ubicación | E-05, E-07, E-08, E-10, E-15, E-25 |
| KPI-11 | Volumen de movimientos | E-04, E-07, E-08, E-10, E-11, E-12, E-13, E-15, E-25 |
| KPI-12 | Tiempo medio de recepción | E-04, E-08, E-10, E-11, E-15, E-25 |
| KPI-13 | Tasa de merma | E-08, E-10, E-12, E-15, E-25 |
| KPI-14 | Volumen y magnitud de ajustes | E-08, E-10, E-14, E-15, E-18, E-21, E-25 |
| KPI-15 | Tiempo medio en tránsito | E-08, E-10, E-13, E-15, E-18, E-25 |
| KPI-16 | Rotación por referencia | E-02, E-08, E-10, E-12, E-15, E-18, E-25 |
| KPI-17 | Existencia sin movimiento | E-04, E-08, E-10, E-15, E-18, E-25 |
| KPI-18 | Ocupación de bodega | E-07, E-08, E-10, E-15, E-18, E-25 |
| KPI-19 | Alertas generadas y atendidas | E-02, E-07, E-13, E-14, E-15, E-18, E-25 |
| KPI-20 | Tiempo medio de atención de alerta | E-15, E-18, E-25 |
| KPI-21 | Eventos de ruptura de stock | E-02, E-15, E-18, E-25 |
| KPI-22 | Tiempo medio de aprobación | E-08, E-12, E-14, E-15, E-18, E-19, E-23, E-25 |
| KPI-23 | Novedades reportadas y resueltas | E-08, E-11, E-13, E-15, E-17, E-18, E-25 |
| KPI-24 | Adopción del sistema | E-08, E-10, E-15, E-25 |

---

**ESTADO DEL CAPÍTULO — 9**

| | |
|---|---|
| **Completado** | Matrices A (26 entidades × 165 eventos), B (entidad ↔ regla) y C (entidad ↔ KPI, con vista inversa) |
| **Riesgos** | Matriz C depende de datos que ningún RF exige capturar (KPI-05, 07, 10, 12, 17, 24; H-12 del SRS) |
| **Dependencias** | Cap. 3, EVENT_CATALOG |
| **Hallazgos** | H-12 del SRS (heredado) |

---

# CAPÍTULO 10 — HALLAZGOS DEL DOMINIO

> Inconsistencias o vacíos entre la monografía, el SPEC, el SRS y el Prompt #004 detectados al modelar. **Ninguno se corrigió en silencio**: cada uno declara el tratamiento provisional que adopta este modelo y quién debe resolverlo. En la v1.1, los resueltos por las decisiones del cierre del CP-04 conservan su evidencia y registran la decisión (DF5-nn); HD-23 a HD-27 se agregaron en ese cierre.

| ID | Hallazgo | Evidencia | Tratamiento en el modelo | Resuelve |
|---|---|---|---|---|
| **HD-01** | **Nombres pedidos por el Prompt #004 frente al vocabulario controlado del SPEC** | El prompt nombra las entidades «Producto», «Variante», «Área», «Inventario» y «Auditoría». El SPEC (§0.5) impone un vocabulario único sin sinónimos y usa «Referencia» (CD-02), «SKU» (CD-05), «Zona» (CD-13), «Unidad de Inventario» (CD-07) y «Bitácora de auditoría» (CD-47). Además, en el SPEC «producto» designa al propio COLBASOFT («propuesta de valor del producto»). | Se conserva el término oficial del SPEC y se registra el nombre pedido como etiqueta de solicitud. «Producto», «variante», «área» e «inventario» (como entidad) pasan a sinónimos prohibidos en el glosario. «Auditoría» se modela como Registro de bitácora (E-21) + Observación de auditoría (E-22). | Director — confirmar |
| **HD-02** | **El ciclo de vida de ejemplo «Producto: Creado → Disponible → En Movimiento → Agotado → Inactivo» mezcla tres planos** | Mezcla el estado de catálogo de la Referencia (Activa/Inactiva), los estados de la existencia (Disponible, En tránsito…, CD-44) y una condición que dispara alerta (existencia en cero). | Se modelan por separado: SM-01 (Referencia), SM-06 (Estado de inventario) y el evento derivado EV-INV-008 (existencia en cero alcanzada). | Informativo |
| **HD-03** | **El ciclo de vida de ejemplo «Movimiento: Borrador → Confirmado → Ejecutado → Auditado» contradice el SPEC** | En el SPEC un movimiento es inmutable una vez confirmado (RN-012 → RN-INT-002); confirmar es ejecutar (el movimiento **es** el hecho). La auditoría no modifica nada (PR-02, RN-064 → RN-AUD-002), por lo que «Auditado» no puede ser un estado del movimiento. | SM-07: En registro → Pendiente de sincronización → Confirmado. «Ejecutado» y «Auditado» se descartan como estados. | Informativo |
| **HD-04** | **Alcance del identificador QR de mercancía: ¿unidad de inventario o SKU + Lote?** | CD-08, RF-040 (RF-QRC-001) y RN-015 (RN-IDE-001) dicen «un QR por unidad de inventario» (SKU + Lote + **Ubicación**). Pero PN-02 paso 2 asocia el QR a «referencia + talla + color + lote» (sin ubicación), y en PN-05 la mercancía se mueve de ubicación conservando su etiqueta. Si el QR identificara la unidad, cada reubicación exigiría reetiquetar. | **Decisión DF5-01 (29-sep-2026):** el QR de mercancía identifica **SKU + Lote**; no identifica ubicación, bodega ni cantidad. La unidad de inventario **sigue** siendo SKU + Lote + Ubicación (RN-INT-005 sin cambios) y se determina con el QR de mercancía más la ubicación escaneada o seleccionada (RN-IDE-001, IN-23). Reubicar no cambia el QR. Cambian los textos de RN-IDE-001 y RN-IDE-003 y de E-08, E-09, AG-07, IN-23 e IN-25. | **Resuelto — DF5-01** |
| **HD-05** | **La existencia en tránsito no tiene ubicación** | La unidad de inventario se define por SKU + Lote + Ubicación, pero la existencia en tránsito (transferencia, movimiento interno interrumpido) no está en ninguna ubicación (RN-032 → RN-EXI-005). | La porción en tránsito permanece asociada a la unidad **origen** en estado «En tránsito» hasta confirmarse la recepción (coherente con PN-06 paso 9, que descuenta del origen al completar). | Fase 5 — confirmar |
| **HD-06** | **La zona de recepción y la exigencia de ubicación** | CD-16 describe la zona de recepción como zona de tránsito, pero la unidad de inventario exige una ubicación. El SPEC no dice que la zona de recepción tenga ubicaciones. | **Decisión DF5-02:** toda zona de recepción contiene al menos una ubicación; la mercancía recibida reside allí en estado «En recepción» (RN-EXI-007, IN-70). | **Resuelto — DF5-02** |
| **HD-07** | **¿La entrada confirmada es disponible o en recepción?** | PN-01 paso 10 dice que al confirmar «se incrementa la existencia **disponible**», pero CD-16 dice que la existencia en zona de recepción «ya está en el inventario pero **aún no está disponible**», y CD-44 incluye el estado «En recepción». | **Decisión DF5-02:** la entrada confirmada ingresa **En recepción**; pasa a **Disponible** al ubicarse, mediante el movimiento interno de primera ubicación (EV-INV-001, DF5-03). Nueva regla RN-EXI-007 (IN-70); el SPEC v1.1 corrige PN-01 paso 10 y su resultado. | **Resuelto — DF5-02** |
| **HD-08** | **Solicitante de un ajuste derivado de conteo** | Al cerrar un conteo, el Jefe «decide qué diferencias generan ajuste» (RN-042 → RN-CNT-004) y esos ajustes siguen PN-07, cuyo aprobador menor es… el Jefe. No se define quién figura como solicitante, y si es el Jefe, RN-023 (RN-AJU-001) lo obliga a escalar todo ajuste de conteo al Administrador. | Se modela el ajuste de conteo como Solicitud de ajuste con origen «conteo» y solicitante = el Jefe que cierra; por RN-AJU-001 escala al Administrador. Esto puede cargar al Administrador (riesgo RG-18). | Director — decidir |
| **HD-09** | **«Valorización» sin dato de origen (H-07 / DEC-07 del SRS)** | El dominio no contiene costo ni precio (DC-03, RF-ENT-002, RF-SAL-002). El permiso «consultar valorización» no tiene objeto. | El modelo de dominio **no incluye** ningún atributo monetario. Si DEC-07 decide una política de costeo, se abrirá un subdominio nuevo. | DEC-07 |
| **HD-10** | **Alerta «lote próximo a vencer inmovilización» sin fecha límite (H-18 / DEC-09)** | El lote solo tiene fecha de ingreso; ninguna regla define una «fecha límite». | Se modela solo la condición definida: antigüedad del lote sobre el umbral (RN-LOT-005 → EV-LOT-004). El tipo de alerta queda como en el SPEC, sin condición propia. | DEC-09 |
| **HD-11** | **Cierre de jornada sin requisitos (H-10 / DEC-05)** | PN-14 está en el MVP (backlog, elemento 39) pero no tiene HU ni RF. | Se modelan la entidad E-26, el agregado AG-21, la máquina SM-21 y los eventos EV-JOR-*, todos marcados ⚠️ pendientes. | DEC-05 |
| **HD-12** | **El Sistema como actor no es un sexto rol** | RN-001 (RN-INT-001) atribuye acciones automáticas «al sistema como actor explícito». No debe confundirse con un rol (DC-04). | VO-38 Actor = Usuario identificado o Sistema. El Sistema no tiene permisos ni ámbito. | Informativo |
| **HD-13** | **Contradicción sobre la libertad del Auxiliar al ubicar** | La matriz §2.7 del SPEC dice que el Auxiliar «solo confirma la ubicación que el sistema le propone; no la elige libremente» (RN-020 → RN-MOV-001), mientras PN-03 E-02 y RN-022 (RN-MOV-003) dicen que puede ubicar en otro lugar y el sistema registra la desviación. | Se modela IN-46: la propuesta es sugerencia y la desviación se permite y registra (prevalece la regla de negocio sobre la nota de la matriz). | Director — confirmar |
| **HD-14** | **El ejemplo «Stock mínimo alcanzado» usa un término prohibido y «Lote inconsistente» no está definido** | «Stock» está prohibido como sinónimo de existencia (SPEC §0.5). «Lote inconsistente» no aparece en el SPEC ni en el SRS. | Se usan «Existencia mínima alcanzada» (EV-INV-006) y «Discrepancia de integridad detectada» (EV-TRZ-006), que cubre la verificación por lote de RF-KDX-006. No se crea una regla nueva. | Informativo |
| **HD-15** | **Escalas no definidas: severidad de alerta y prioridad de tarea** | El SPEC solo nombra la severidad «crítica» y dice que las tareas se ordenan «por prioridad» sin definir la escala. | VO-28 y VO-29 quedan con validación incompleta. No se inventan niveles. | Director / Fase 5 |
| **HD-16** | **Instante del hecho frente a instante de sincronización** | Con retención local (RN-054 → RN-INT-003) un movimiento ocurre en un instante y se sincroniza en otro. KPI-05 (tiempo de registro) y el orden del kardex dependen de cuál se use. | VO-32 Fecha operativa = instante del hecho; el de sincronización es dato de control. El orden del kardex con registros tardíos queda para Fase 5. | Fase 5 |
| **HD-17** | **Capacidad frente a unidades de medida heterogéneas** | La capacidad se expresa «en la unidad configurada» (CD-15), pero una ubicación puede alojar referencias en metros, rollos o unidades, y RN-068 (RN-INT-007) prohíbe conversiones. La ocupación (KPI-18) no es calculable sin una regla de equivalencia. | Se deja la capacidad como VO-12 sin cálculo de ocupación mixta. Requiere decisión. | Director / Fase 5 |
| **HD-18** | **Precisión de las cantidades** | Unidades de medida como metros o kilogramos requieren cantidades fraccionarias; el SPEC no fija la precisión. | VO-13 admite fracciones según la unidad de medida; la precisión se fija en Fase 5. | Fase 5 |
| **HD-19** | **Estados y actores que el SPEC no nombra** | Para completar las máquinas de estado fue necesario nombrar: «Habilitado» (lote no inmovilizado), «Generado» (QR antes de verificarse), «Reversado» (documento de entrada anulado sin confirmar: función de M-07 sin RF), «Cancelada» (solicitud de salida y tarea operativa: el SPEC menciona la cancelación sin actor ni RF), y no se definen estados propios de Bodega, Zona ni SKU. | Se marcan como nombres nuevos del dominio (origen «Nuevo — Fase 4»), sin crear reglas nuevas. | Director — confirmar |
| **HD-20** | **El cierre de tarea por «movimiento» no cubre las tareas de conteo** | RF-160 (RF-TAR-003) cierra la tarea «por la confirmación del movimiento asociado», pero registrar un conteo no es un movimiento. | Se generaliza a «hecho asociado confirmado» (IN-69): movimiento para tareas operativas, conteo confirmado para tareas de conteo. | Informativo |
| **HD-21** | **Estado de aprobación del SRS** | El Prompt #004 declara el SRS aprobado, pero el archivo sigue «Emitido para revisión del Director» y sus 9 decisiones (DEC-01…DEC-09) no tienen respuesta registrada. | El modelo se construye sobre el baseline del SRS sin asumir respuestas a las decisiones; donde una decisión afecta al dominio se marca ⚠️. **DF5-06** (revisada) registra la **validación técnica** del SPEC, el SRS y este modelo en su v1.1; la aprobación funcional y académica sigue pendiente de DEC-01…DEC-09 y HD-25. | Director — aprobación pendiente (DEC-01…DEC-09) |
| **HD-22** | **Unidades de manejo agrupadas** | PN-02 E-03 (MVP) permite rotular un contenedor como «unidad de manejo agrupada», pero el backlog sitúa la «gestión de unidades de manejo y contenedores» en el Horizonte 3. | No se modela como entidad; queda como término del glosario marcado fuera del MVP. | Director — confirmar |
| **HD-23** | **La primera ubicación cambiaba la existencia de unidad sin movimiento (HA-02 de la auditoría del CP-04)** | Tras la entrada, la existencia está en la unidad (SKU, Lote, ubicación de recepción); al ubicarla (PN-03, HU-ENT-006) pasa a (SKU, Lote, ubicación destino), que es otra unidad (RN-INT-005). La v1.0 lo modelaba como cambio de estado de la misma unidad (SM-06, EV-INV-001) sin movimiento en el kardex, en contra de IN-03 (la existencia es la suma de sus movimientos) y dejando sin «dónde» el primer tramo de la trazabilidad (CD-21). | **Decisión DF5-03:** la primera ubicación es un **movimiento interno** (tipo existente en VO-21) desde la ubicación de recepción hacia la destino. Nueva regla RN-MOV-010 (IN-71). EV-INV-001 conserva su ID y su nombre y pasa a designar ese movimiento confirmado; SM-06 agrega la interrupción de la primera ubicación (En recepción → En tránsito). La operación se suma a las indivisibles del Cap. 5.3. | **Resuelto — DF5-03** |
| **HD-24** | **Registros retenidos sin conectividad que al sincronizarse ya no cumplen una regla (HA-04 de la auditoría del CP-04)** | Con retención local (RN-INT-003) un registro puede ser válido cuando se hace y dejar de serlo al sincronizarse, porque otro usuario cambió la existencia. IN-08 prohíbe la existencia negativa sin excepción, y el hecho físico ya ocurrió. El SPEC v1.0 no decía qué pasa en ese caso (RF5-05). | **Decisión DF5-05:** al sincronizar, el registro se valida de nuevo contra el estado vigente; si cumple, se confirma con su fecha operativa original (EV-TRZ-004); si no, no se aplica y se rechaza con constancia (nuevo estado «Rechazado en sincronización» en SM-07 y nuevo evento EV-TRZ-007) y, si describe un hecho físico, abre una novedad (E-17). Nueva regla RN-INT-008 (IN-72). El orden del kardex con registros tardíos sigue en HD-16. | **Resuelto — DF5-05** |
| **HD-25** | **Qué identifica físicamente cada etiqueta de mercancía (copias de un QR de lote, reimpresión y relación escaneo–cantidad)** | Con DF5-01, un mismo QR de SKU + Lote identifica mercancía repartida en varias ubicaciones, lo que exige varias etiquetas con el mismo código. Pero RN-IDE-004 (reimpresión) emite un código **nuevo** y deja el anterior Reemplazado (SM-05: solo el Activo resuelve escaneos): reimprimir una etiqueta deteriorada invalidaría las demás copias del lote. RN-IDE-002 (el código no se repite) se refiere a emitir códigos, no a imprimir copias; el SPEC no distingue los dos casos. Además, PN-10 paso 7 dice que el Auxiliar «escanea cada unidad al tomarla» (RN-SAL-004): con copias del mismo código, dos escaneos de la misma etiqueta no se distinguen de dos piezas distintas. | No se decide. SM-05 y RN-IDE-004 no cambian. Se analizan tres alternativas en `04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md` §2: (A) todas las etiquetas del lote comparten el QR; (B) QR de lote más identificador físico único por etiqueta; (C) el QR identifica un paquete físico, lo que revisa DF5-01. | Director — **decidir antes de la Fase 5**; bloqueante mientras la alternativa C siga abierta · **Información requerida:** qué representa cada etiqueta física (rollo, pieza, bulto o lote), si un escaneo debe equivaler a una cantidad y qué trazabilidad física exige el proyecto |
| **HD-26** | **Código de barras del proveedor frente al QR por SKU + Lote** | Con DF5-01, RN-IDE-003 limita un código de barras secundario a un solo QR de mercancía (un SKU + Lote). Un código de barras de proveedor suele identificar el producto y repetirse en lotes distintos: con la regla actual, el segundo lote de un mismo SKU no podría asociarlo. | Se aplica RN-IDE-003 tal como quedó en el SRS v1.1. La funcionalidad está en el Horizonte 2 del backlog (SPEC §12.3, elemento 11), por lo que no afecta al MVP. | Director — decidir · **Información requerida:** qué identifica el código de barras de los proveedores reales. No bloquea la Fase 5 (H2) |
| **HD-27** | **Alcance de las operaciones que se pueden registrar sin conectividad** | RN-INT-003 se traza a recepción (PN-01), movimiento interno (PN-05) y cierre de jornada (PN-14), pero RNF-DSP-002 habla, en general, del «registro de movimientos desde tablet». El SPEC no fija qué operaciones deben poder registrarse sin conectividad. | No se decide el alcance. Con DF5-05, toda operación retenida, sea cual sea, se valida de nuevo al sincronizar (RN-INT-008), así que el alcance ya no pone en riesgo las invariantes: es una decisión de producto y de experiencia de uso. | Director — decidir · **Información requerida:** conectividad real de la bodega. No bloquea la Fase 5 |

**Resueltos en el cierre del CP-04:** HD-04, HD-06, HD-07, HD-23, HD-24. **Bloqueantes para la Fase 5:** HD-25. **Requieren decisión del Director:** HD-01, HD-08, HD-09, HD-10, HD-11, HD-13, HD-15, HD-17, HD-19, HD-21, HD-22, HD-25, HD-26, HD-27.


---

**ESTADO DEL CAPÍTULO — 10**

| | |
|---|---|
| **Completado** | 27 hallazgos con evidencia, tratamiento y responsable |
| **Riesgos** | HD-25 debe decidirse antes de la Fase 5 (04_CP04_DECISIONES_PENDIENTES); los demás pendientes no bloquean la arquitectura |
| **Dependencias** | Todos los capítulos |
| **Hallazgos** | — |

---

*Fin de DOMAIN_MODEL v1.1. La monografía original permanece sin modificaciones.*
