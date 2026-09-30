# 05_V15 — Validación con datos ficticios y corte de entrega C1

| Campo | Dato |
|---|---|
| **Documento** | Registro de decisiones de la versión 1.5 |
| **Fecha** | 30 de septiembre de 2026 |
| **Estado** | **Borrador** (el acta de DEC-08 sigue sin firmar: ver `05_V13_DECISIONES_DEC02_DEC09.md`) |
| **Documentos que lo recogen** | `COLBASOFT_SPEC_v1.5.md` (§12.7 y §12.8) · `SRS_COLBASOFT_v1.5.md` (§1.4.8, Cap. 2, §12.8, Anexo C.13) · `DOMAIN_MODEL.md` §0.12 · `07_FASE_5_ARQUITECTURA/ADR-001_PILA_TECNOLOGICA.md` |

> Registra lo que el Director decidió el 30 de septiembre de 2026. No introduce decisiones nuevas.

# 1. Decisiones

| # | Decisión | Dicha por el Director |
|---|---|---|
| 1 | **No habrá empresa piloto.** El proyecto se valida **solo con datos ficticios**; el asesor lo sabe y lo aceptó | Sí |
| 2 | El Excel con datos aleatorios es **solo carga de datos de prueba**; la base de datos es real | Sí |
| 3 | **MVP de noviembre de 2026** con: acceso, catálogo, bodega, entradas con piezas y QR, ubicación, kardex y consulta, más salidas (con corte parcial) y movimientos internos | Sí |
| 4 | **Pila tecnológica:** TypeScript (Node, Fastify, Prisma, PostgreSQL en Docker, React con Vite) | Sí |
| 5 | La **Fase 5** (arquitectura) avanza **en paralelo**, sin esperar el AS-IS | Sí |
| 6 | El **código vive en un repositorio aparte** (`colbasoft-app`), junto a los documentos | Sí |
| 7 | Plazos: esqueleto funcionando la semana del 5 de octubre; MVP en noviembre; proyecto completo entre marzo y abril de 2027 | Sí |

# 2. Qué se puede y qué no se puede afirmar

| Se puede afirmar | No se puede afirmar |
|---|---|
| El sistema cumple sus requisitos, reglas y criterios de aceptación ejecutables con datos ficticios | Reducción de errores o ganancia de trazabilidad medidas en una operación real |
| Conserva la integridad (kardex inmutable, existencia derivada, no-negativo) | Que los procesos TO-BE coincidan con los de una empresa concreta |
| Puede operarse desde tablet con los flujos del corte C1 | Que el personal de una empresa lo adopte |

**Limitación declarada.** Sin AS-IS ni línea base, el proyecto demuestra **viabilidad funcional**, no **impacto medido**. Debe figurar en el informe final. El kit `06_ASIS_KIT/` queda para si más adelante aparece una empresa.

# 3. Corte C1 (resumen)

**35 historias y 83 requisitos**, todos del Horizonte 1, en seis bloques (C1-1 Fundación, C1-2 Identificación y lotes, C1-3 Entradas, piezas y ubicación, C1-4 Kardex y consulta, C1-5 Movimientos internos, C1-6 Salidas y corte parcial). **Regla de recorte:** desde el último bloque hacia atrás. El detalle está en SPEC §12.7 y SRS §12.8.

**Queda fuera del corte** (sigue en el Núcleo): ajustes, conteos, novedades, alertas, reportes e indicadores, dashboard, tareas, contenedores agrupados (HU-ENT-010), movimiento en tránsito (HU-MOV-009) y cierre de jornada. La sincronización sin conectividad tampoco entra en C1.

# 4. Corrección de trazabilidad

La tabla de dependencias entre historias del SRS seguía indicando que HU-ENT-006 dependía de HU-BOD-005 (Horizonte 2), aunque H-19 ya lo había resuelto en el SPEC v1.4. Se corrigió en la v1.5.

# 5. Lo que sigue abierto

Acta firmada de DEC-08 · HD-28 (depende de información de campo, que ya no se levantará salvo que aparezca una empresa: se decidirá con supuestos, registrados como tales) · modelo de datos y API de la Fase 5.

---

*Fin del registro de decisiones de la versión 1.5.*
