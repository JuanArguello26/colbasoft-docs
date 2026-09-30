
---

# CAPÍTULO 2 — VISIÓN GENERAL DEL SISTEMA

> Descripción **funcional** de COLBASOFT. No describe arquitectura, tecnologías ni estructura de datos.

## 2.1 Perspectiva del producto

COLBASOFT es un sistema **autónomo y de alcance deliberadamente estrecho**: gestiona el inventario y la logística de una bodega textil y nada más `[DC-02]` `[DC-03]`. No forma parte de un ERP ni se integra con sistemas de ventas, compras, producción, contabilidad, nómina, CRM ni facturación.

**Contexto funcional (quién y qué interactúa con el sistema):**

```
   Personas (5 roles)                                              Elementos externos al sistema
 ┌──────────────────────┐                                       ┌─────────────────────────────────┐
 │ Administrador        │                                       │ Herramienta analítica externa   │ ◄── recibe datos estructurados
 │ Jefe de Bodega       │                                       │ (Power BI) [DC-06]              │     (RF-REP-004, RF-REP-005)
 │ Coordinador          │ ── web responsive / tablet ─► COLBASOFT│ Cámara de la tablet (escaneo QR)│ ──► captura de identificadores
 │ Auxiliar             │       [DC-05]                          │ Impresión de etiquetas QR       │ ◄── etiquetas físicas (ver 2.8)
 │ Auditor (solo lectura│                                       └─────────────────────────────────┘
 └──────────────────────┘        Sistema como actor de acciones automáticas [RN-INT-001]
```

**Interfaces con el usuario.** Aplicación web responsive utilizable en escritorio y en tablet `[DC-05]`; captura de identificadores con la cámara de la tablet, sin lector externo obligatorio (RNF-TAB-003). No existe aplicación móvil nativa.

**Interfaces con otros sistemas.** Una sola, unidireccional y de datos: la **exposición estructurada de información** a la herramienta analítica externa `[DC-06]`. El SRS no especifica el mecanismo.

## 2.2 Problema que el sistema resuelve

La monografía documenta que las PYMES textiles del Eje Cafetero gestionan su inventario con cuadernos, hojas de cálculo sueltas y registros manuales `[MON §3]`, lo que produce una **cadena causal de nueve eslabones** (SPEC §1.1.2): registro manual → errores frecuentes → información desactualizada → pérdida de trazabilidad → rupturas de stock y sobre stock → interrupciones de producción → reprocesos y pérdida de materia prima → plazos de entrega más largos → pérdida de competitividad. El obstáculo principal no es tecnológico sino la **resistencia a la adopción** `[MON §4, §7.1]`; por eso el SRS trata la usabilidad y la adopción como requisitos de primer orden (Cap. 7).

> **Nota de integridad `[AUD E.1, E.2]`.** Varias cifras de magnitud del problema (60 %, +30 % de pérdidas, 25–45 % de productividad) provienen de fuentes ausentes de la bibliografía de la monografía y **no se usan en este SRS como justificación cuantitativa**. Las cifras respaldadas (72 % ANDI 2023; 67 % Martínez y Gómez 2019) se citan solo como contexto.

## 2.3 Funciones del producto

Las funciones se agrupan en cinco familias (SPEC §5.1). La tabla siguiente se genera del contenido del SRS y muestra el volumen de requisitos por módulo.

{{TABLA_MODULOS}}

**Capacidades transversales del producto:**

| Capacidad | Cómo se manifiesta | Regla / requisito núcleo |
|---|---|---|
| **Registro atribuido** | Toda acción queda a nombre de una persona identificada (o del Sistema como actor explícito) | RN-INT-001 · RF-ACC-001 · RF-KDX-002 |
| **Trazabilidad completa** | Kardex inmutable; la existencia se deriva del kardex | RN-INT-002 · RN-INT-004 · RF-KDX-003 |
| **Identificación por escaneo** | QR único de un solo uso por unidad y por ubicación | RN-IDE-002 · RF-QRC-001…003 |
| **Control por segregación** | Nadie aprueba su propia solicitud; el Auditor solo lee | RN-AJU-001 · RN-AUD-002 · RF-AUD-005 |
| **Automatización por reglas** | Reglas explícitas y umbrales configurables disparan alertas | Cap. 8 · RF-ALE-002 |
| **Medición del propio beneficio** | 24 KPI calculados por el sistema | Cap. 9 · RF-REP-003 |
| **Operación sin conectividad estable** | Retención local y sincronización posterior | RN-INT-003 · RNF-DSP-002 |

## 2.4 Ciclo de vida de una unidad de inventario

```
Llegada ─► Documento de entrada ─► Recepción física ─► Confirmación (2.ª persona) ─► Lote + Existencia
  (CU-06)                                                                                  │
   ┌────────────────────────────────────────────────────────────────────────────────────┘
   ▼
Identificación QR (CU-07) ─► Ubicación (CU-08) ─► [ Consulta CU-09 · Reubicación CU-10 · Transferencia CU-11 ]
                                                                    │
                       Conteo cíclico/general (CU-13/14) ─► Ajuste con aprobación (CU-12)
                                                                    │
                                                          Salida autorizada (CU-15) ─► fin del alcance de trazabilidad
```

**Estados de la existencia (CD-44)** — mutuamente excluyentes para una misma cantidad:

| Estado | Puede salir | Puede transferirse | Puede reubicarse | Cuenta en disponible |
|---|:--:|:--:|:--:|:--:|
| Disponible | ✅ | ✅ | ✅ | ✅ |
| Reservado | Solo por su operación | ❌ | ❌ | ❌ |
| En tránsito | ❌ | ❌ | ❌ | ❌ |
| Inmovilizado | ⚠️ con autorización | ⚠️ con autorización | ⚠️ con autorización | ❌ |
| En recepción | ❌ | ❌ | ✅ | ❌ |

## 2.5 Qué significa «inteligente» en COLBASOFT `[DC-07]` `[AUD C.1.5]`

«Inteligente» significa **exactamente** dos cosas: (1) **automatización basada en reglas** —el sistema aplica de forma autónoma un cuerpo de reglas de negocio explícitas que impiden estados inválidos, disparan alertas y ejecutan acciones sin intervención humana (Cap. 8)— y (2) **analítica operativa** —el sistema calcula indicadores sobre su propio registro (Cap. 9). **No** incluye aprendizaje automático, predicción de demanda, visión por computador, procesamiento de lenguaje natural, agentes autónomos ni IA generativa. Toda afirmación de «inteligencia» del producto debe poder señalarse con una regla numerada (RN-…) o un KPI.

## 2.6 Características de los usuarios (síntesis)

| Rol | Frecuencia | Dispositivo | Nivel digital | Nota de diseño |
|---|---|---|---|---|
| Administrador | Baja | Escritorio o portátil | Medio | Decisor de compra; configura |
| Jefe de Bodega | Alta | Escritorio y tablet | Medio | Responsable de la exactitud |
| Coordinador de Bodega | Muy alta | Tablet en piso | Medio-bajo | Supervisa en piso |
| **Auxiliar de Bodega** | **Intensiva** | **Tablet, exclusivamente** | **Bajo** | **Usuario crítico: el diseño de interacción se optimiza para él** `[MON §4]` |
| Auditor | Baja (por campañas) | Escritorio | Medio-alto | Solo lectura absoluta |

Detalle de cada actor en el Capítulo 3.

## 2.7 Restricciones

| # | Restricción | Origen |
|---|---|---|
| RS-1 | Alcance funcional cerrado (DC-02) y exclusiones absolutas (DC-03) | DC-02, DC-03 |
| RS-2 | Exactamente cinco roles; ninguno adicional | DC-04 |
| RS-3 | Web responsive + tablet; sin app nativa | DC-05 |
| RS-4 | Sin IA de ningún tipo | DC-07 |
| RS-5 | QR como identificador principal; el código de barras solo consulta | DC-08, RN-IDE-003 |
| RS-6 | Capacidad financiera limitada de las PYMES: el producto debe ser de bajo costo de entrada | `[MON §1, §3, §6]` R-08 |
| RS-7 | Baja alfabetización digital: usabilidad extrema como requisito prioritario | `[MON §3, §8.2]` R-09 |
| RS-8 | Infraestructura tecnológica deficiente: no puede asumirse conectividad permanente | `[MON §3]` R-11 |
| RS-9 | Adopción escalonada por proceso, no de golpe | `[MON §8.2]` R-13 |
| RS-10 | Cumplimiento de la normativa colombiana de protección de datos personales (Ley 1581 de 2012) | `[AUD C.2.11]` · RNF-SEG-008 |
| RS-11 | Barreras regulatorias del sector: fuera del control del producto | `[MON §3]` |
| RS-12 | Ningún elemento del SRS puede contradecir la monografía (RI-1) ni inventar funcionalidad (RI-3) | Auditoría |

## 2.8 Supuestos y dependencias

| # | Supuesto / dependencia | Estado | Riesgo asociado |
|---|---|---|---|
| S-1 | Existe una **empresa de estudio** dispuesta a participar en levantamiento, piloto y medición `[DC-01]` | 🔴 Abierto (V-01) | RG-37 |
| S-2 | Los procesos del Cap. 4 (TO-BE) son compatibles con la operación real de la empresa | 🔴 No verificado: AS-IS sin levantar | R-S01 |
| S-3 | Cada punto de operación dispone de una **tablet con cámara** capaz de escanear QR (RNF-TAB-003) | 🟡 Por confirmar en el levantamiento de infraestructura | RG-24 |
| S-4 | La empresa dispone de un medio para **imprimir etiquetas** legibles y resistentes a la operación de bodega (el SRS lo requiere funcionalmente, no lo especifica) | 🟡 Por confirmar | RG-25 |
| S-5 | La conectividad es **intermitente**: el sistema debe tolerar su pérdida | 🟢 Requisito (RN-INT-003) | RG-23 |
| S-6 | Existe la herramienta analítica externa (Power BI) a la que se exponen los datos `[DC-06]` | 🟡 Por confirmar | RG-29 |
| S-7 | La **línea base** de KPI-01, KPI-05 y KPI-08 se levantará antes del piloto | 🔴 Abierto (V-03) | RG-36 |
| S-8 | El equipo de tres autores mantiene la autoría del producto | 🟡 A-12 abierto | — |

---

**ESTADO DEL CAPÍTULO 2**

| | |
|---|---|
| **Completado** | Perspectiva funcional · problema · funciones · ciclo de vida · definición de «inteligente» · restricciones · supuestos |
| **Pendiente** | Confirmar los supuestos S-1…S-4 y S-6 con la empresa de estudio (Fase 3 del roadmap) |
| **Riesgos encontrados** | S-1, S-2 y S-7 abiertos (RG-36, RG-37, R-S01) |
| **Dependencias** | Cap. 3 (actores), Cap. 4 (casos de uso), Anexo C |
