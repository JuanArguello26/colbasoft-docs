# 05_V14 — Respuestas a H-19, H-20, HD-29 y HD-30

**COLBASOFT — Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento** | Registro de decisiones de la versión 1.4 |
| **Fecha** | 30 de septiembre de 2026 |
| **Estado** | **Borrador** (el acta de DEC-08 sigue sin firmar: ver `05_V13_DECISIONES_DEC02_DEC09.md`) |
| **Documentos que lo recogen** | `COLBASOFT_SPEC_v1.4.md` · `SRS_COLBASOFT_v1.4.md` (Anexo C, C.12) · `DOMAIN_MODEL.md` §0.11 |

> **Naturaleza.** Registra lo que el Director confirmó el 30 de septiembre de 2026: la opción (a) en los cuatro asuntos, **después de verificar cada una contra las fuentes**. No introduce decisiones nuevas.

# 1. Respuestas y verificación

| Asunto | Respuesta | Qué se verificó | Qué cambió |
|---|---|---|---|
| **H-19** HU-ENT-006 dependía de HU-BOD-005 (Horizonte 2) | **(a)** Regla fija de propuesta de ubicación en el Núcleo: zona por categoría, agrupación por referencia y mayor capacidad libre, en ese orden; si ninguna aplica, la zona de recepción | HU-BOD-005 y RF-039 son prioridad Could, y el SPEC (§12.3, elemento 12) ya afirmaba que el MVP opera con propuesta simple. RN-020 y PN-03 también decían «criterios configurados» y se ajustaron | HU-035 (criterio 1), PN-03 (paso 1), RN-020 |
| **H-20** RF-136 calculaba los 24 KPI | **(a)** Se acota a los 12 KPI del Núcleo y un RF nuevo cubre los otros 12 | Las fuentes de los 12 KPI del Núcleo (01, 05, 08, 09, 11, 13, 14, 16, 17, 19, 21 y 24) están todas en módulos del Horizonte 1. Se prefirió dividir el RF antes que dejarlo con dos horizontes | RF-136 (texto) y **RF-185** (Horizonte 2: KPI-02, 03, 04, 06, 07, 10, 12, 15, 18, 20, 22 y 23) |
| **HD-29** Corte y movimiento parcial | **(a)** Una pieza no se divide: el movimiento interno la mueve completa y tomar una parte es un corte parcial (salida) | Coincide con F-3 (cortes de rollos) y evita adelantar al MVP las «unidades de manejo». Se detectó una limitación (abajo) | Regla nueva **RN-090***; HU-045 (criterio 2), PN-05 (paso 3), RF-166, CD-49 |
| **HD-30** Alcance del control por pieza | **(a)** Toda la mercancía se controla por piezas; lo suelto se registra como paquete o bolsa con su cantidad de unidades | Coincide con F-1 (la pieza cubre metros, kilogramos y unidades, sin excepciones) y con RN-084* | RN-084* (texto) |

## 1.1 Limitación conocida (HD-29)

Una parte de un **paquete o bolsa de unidades** no puede trasladarse a otra ubicación como movimiento interno, porque exigiría dividir la pieza. La parte que se toma se registra como salida. **Se puede reabrir** con la información del levantamiento AS-IS (Q-04: frecuencia y forma de los cortes).

# 2. Cifras

| | v1.3 | **v1.4** |
|---|:--:|:--:|
| Historias | 114 | 114 |
| Requisitos funcionales | 184 | **185** |
| Reglas | 91 | **92** |
| Escenarios Gherkin | 515 | 515 |
| Núcleo (umbral aprobatorio) | 94 HU · 164 RF | 94 HU · 164 RF |
| Horizonte 2 | 20 HU · 20 RF | 20 HU · **21 RF** |

# 3. Lo que sigue abierto

| Asunto | Qué falta |
|---|---|
| **DEC-08** | Acta firmada |
| **HD-28** | Identidad física de la pieza sin QR propio, contenedores con mezcla de lotes (Q-08) y motivos de reemplazo de un QR: dependen del levantamiento AS-IS |
| **KPI-24** | Verificación de campo |

---

*Fin del registro de decisiones de la versión 1.4.*
