# ADR-001 · Pila tecnológica

| Campo | Dato |
|---|---|
| **Fase** | 5 — Arquitectura y diseño (habilitada por el Director el 30-sep-2026; en paralelo al AS-IS) |
| **Estado** | **Aprobada por el Director el 30 de septiembre de 2026** (borrador del documento; el detalle de arquitectura sigue abierto) |
| **Decide** | Con qué tecnologías se construye el corte de entrega C1 (SPEC v1.5 §12.7) |
| **Fuentes** | SRS v1.5 (RNF de tablet, disponibilidad y seguridad), modelo de dominio v1.5 (AG-05, AG-06, AG-22, IN-01…IN-79) |

> **Nota.** Las tecnologías viven en la Fase 5, no en el SPEC ni en el SRS (que las excluyen). Este ADR solo registra la elección; el diseño detallado (modelo de datos, módulos, API) se documenta aparte.

# 1. Contexto

- Aplicación **web responsive**, sin app nativa, usable desde **tablet** con lectura de QR por la **cámara** (RNF-TAB-001…003, DC-05, DC-08).
- **Integridad del dominio:** kardex inmutable (IN-02), existencia derivada de los movimientos (IN-03), no-negativo sin excepción (IN-08), unidad de inventario única (IN-04), piezas con cantidad propia (IN-73, IN-74).
- **Concurrencia:** dos operarios no pueden comprometer la misma existencia (RF5-03, RF5-15).
- **Datos de prueba ficticios**, cargados desde un Excel a una base de datos real (SPEC §12.8).
- Equipo de tres personas; 10 a 20 horas semanales cada una; MVP en noviembre de 2026.

# 2. Decisión

| Capa | Elección |
|---|---|
| Lenguaje | **TypeScript** (Node 24) en servidor y cliente |
| Servidor | **Fastify** |
| Acceso a datos | **Prisma**, con migraciones SQL para lo que el ORM no expresa (restricciones, triggers) |
| Base de datos | **PostgreSQL**, ejecutada con **Docker Compose** |
| Cliente | **React** con **Vite** (aplicación web; PWA más adelante) |
| Lectura de QR | Cámara del navegador (biblioteca por elegir en el diseño) |
| Datos de prueba | Script de carga del Excel (DS-1) a la base de datos |
| Pruebas | **Vitest** |
| Estructura | Monorepo con `npm workspaces`: `apps/api`, `apps/web`, `packages/shared` |

# 3. Consecuencias para el diseño

1. **El Excel nunca es la base de datos.** Solo alimenta la carga de DS-1.
2. **La inmutabilidad del kardex y la regla de no-negativo se aplican en la base de datos**, no solo en el código: permisos y restricciones que impiden `UPDATE` y `DELETE` sobre movimientos, y validación dentro de la misma transacción que escribe el movimiento.
3. **La existencia no se almacena como valor independiente** (IN-03): se deriva de los movimientos. Se decidirá en el diseño detallado si se usa una vista, una tabla derivada con verificación, o ambas.
4. **Una operación que cambia de unidad de inventario** (movimiento interno, primera ubicación, corte parcial) **se ejecuta en una sola transacción** (DOMAIN_MODEL §5.3).
5. **Cada escritura queda atribuida a un usuario** (IN-01) y pasa por la bitácora cuando corresponde.

# 4. Alternativas descartadas

| Alternativa | Por qué no |
|---|---|
| Excel como base de datos | No garantiza kardex inmutable, existencia derivada ni concurrencia: obligaría a recortar las reglas estructurales |
| SQLite | Suficiente para una demo, pero sin la concurrencia ni los permisos por rol que exige el dominio |
| NestJS en el servidor | Más estructura, pero más lenta de arrancar con el tiempo disponible |
| Next.js | Mezcla cliente y servidor en un solo proyecto; se prefiere separar capas para probar las reglas |

# 5. Fuera del corte C1 y por decidir

- La **retención local y la sincronización sin conectividad** (RN-INT-003, RNF-DSP-002, HD-27) **no están en el corte C1**: se diseñan después de noviembre.
- El **modelo de datos** y la **API** se documentan en los siguientes documentos de la Fase 5.
- Autenticación y almacenamiento de credenciales: se detallan en un ADR aparte, respetando los RNF de seguridad del SRS.
- Despliegue para la demostración (local o nube): pendiente.

---

*Fin de ADR-001.*
