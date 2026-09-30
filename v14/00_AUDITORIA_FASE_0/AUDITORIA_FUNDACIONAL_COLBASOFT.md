# AUDITORÍA FUNDACIONAL — FASE 0
## Proyecto COLBASOFT
**Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero**

---

| Campo | Dato |
|---|---|
| **Documento auditado** | `MONOGRAFÍA  COLBASOFT.docx` |
| **Título original** | *Automatización del proceso logístico en la gestión de inventarios para PYMES del sector textil del Eje Cafetero* |
| **Autores** | Juan Esteban Argüello · Brayan Alexander Osorio · Brandon José Guerrero |
| **Institución** | Escuela de Ingeniería — CIAF |
| **Asesor académico** | Edwin Andrés Cabrera Arredondo |
| **Grado optado** | Tecnólogo en Desarrollo de Software |
| **Fecha del documento** | 27 de noviembre de 2025 — Pereira, Risaralda |
| **Extensión** | 17 páginas · 14 apartados · 15 referencias formales · 1 elemento gráfico |
| **Fecha de auditoría** | 1 de septiembre de 2026 |
| **Rol del auditor** | Arquitecto Principal · Investigador Metodológico · Auditor Técnico |
| **Estado** | FASE 0 — Auditoría y planificación. **Sin código. Sin arquitectura. Sin tecnologías.** |

> **Declaración de integridad documental.** La monografía no ha sido modificada. Esta auditoría es un documento externo y derivado. Todo hallazgo cita el apartado numerado de la monografía del cual proviene, según su Tabla de Contenido oficial.

---

# FASE A — AUDITORÍA DEL DOCUMENTO

## A.1 Resumen ejecutivo

La monografía es un **estudio teórico de revisión documental**, no un proyecto de desarrollo de software. Su producto declarado es un **modelo conceptual de automatización** para la gestión de inventarios en PYMES textiles del Eje Cafetero, construido a partir de literatura especializada y de informes institucionales colombianos y latinoamericanos.

El argumento central se sostiene sobre cinco pilares teóricos —Ballou (2004), Chopra y Meindl (2016), Heizer y Render (2014), Slack et al. (2010) y Bowersox y Closs (2007)— y se contextualiza con evidencia regional que documenta el rezago digital del sector (Cap. 7.2). El documento afirma que el 72 % de las PYMES colombianas carece de herramientas tecnológicas para registrar inventarios (ANDI, 2023, Cap. 7.2) y que la automatización reduce errores en un 40 % y mejora la trazabilidad en un 55 % (Hernández y Salazar, 2021, Cap. 7.2).

**Hallazgo estructural dominante:** existe una **brecha de naturaleza** entre la monografía y el proyecto COLBASOFT. La monografía delimita explícitamente su alcance en el Cap. 4: *«Este estudio analiza estos factores desde fuentes documentales […] sin proponer soluciones prácticas de implementación»*, y lo reafirma en el Cap. 8.1: *«Más que desarrollar un sistema completo, buscamos plantear un modelo flexible»*. COLBASOFT, en cambio, es una **plataforma de software operativa**. Esta transición no es una continuación natural del documento: es una **extensión de alcance que requiere justificación y aprobación formal del Director** antes de iniciar cualquier fase de ingeniería (ver Regla Innegociable 6 y Fase F).

**Segundo hallazgo estructural:** el Objetivo Específico 3 (Cap. 5.5) compromete la síntesis de hallazgos «que permitirán proponer un modelo conceptual integrado», pero **el documento no contiene ningún apartado que presente formalmente dicho modelo**. La Tabla de Contenido pasa del Marco Teórico (Cap. 7.2, p. 12) directamente a Conclusiones (Cap. 8, p. 14). El Cap. 8.1 afirma que «la propuesta presentada en esta monografía demuestra que sí es posible aplicar un modelo», pero esa propuesta no aparece descrita, diagramada ni especificada en ningún punto del texto. **El entregable nuclear del trabajo está declarado pero no materializado.**

**Tercer hallazgo estructural:** no existe un **capítulo de Metodología**. El documento se autodefine como «revisión documental» (Caps. 4, 5, 8.1) sin declarar criterios de inclusión/exclusión, bases de datos consultadas, ecuaciones de búsqueda, ventana temporal ni protocolo de selección de los «15 antecedentes» que menciona el Cap. 7.2. Para una monografía de grado esto constituye un vacío metodológico crítico.

**Cuarto hallazgo estructural:** el horizonte temporal de todo el documento es **«hacia el año 2025»** (Resumen, Caps. 3, 4, 5, 6, 7.1, 7.2, 8.1). El documento fue fechado el 27 de noviembre de 2025 —es decir, al cierre de su propio horizonte— y el proyecto se denomina «COLBASOFT 2027». **El marco temporal está vencido** y debe ser reproyectado con justificación explícita.

**Conclusión de la auditoría:** la monografía es una **base conceptual sólida en lo teórico y débil en lo metodológico y evidencial**. Es suficiente como fuente de verdad para el *dominio del problema* (qué duele, a quién, por qué), pero **insuficiente como especificación de producto**. Requiere una capa de ingeniería completa —requisitos, modelo de dominio, validación— que hoy no existe en ningún grado.

---

## A.2 Índice estructural

Estructura oficial según la Tabla de Contenido del documento (p. 2):

| # | Apartado | Pág. | Naturaleza | Estado |
|---|---|---|---|---|
| 1 | Resumen | 3 | Síntesis | Presente |
| 2 | Palabras clave | 3 | Indexación | Presente (7 términos) |
| 3 | Introducción | 4 | Contextualización | Presente |
| 4 | Planteamiento del problema y Justificación | 5 | Problematización | Presente (fusiona dos apartados normalmente separados) |
| 5 | Objetivo General | 8 | Propósito | Presente |
| 5.5 | Objetivos Específicos | 8 | Propósito | Presente (3 objetivos) — **numeración anómala: debería ser 5.1** |
| 6 | Desarrollo temático | 8 | Análisis | Presente |
| 7 | Marco Referencial | 10 | Fundamentación | Presente (encabezado introductorio) |
| 7.1 | Marco conceptual | 10 | Definiciones | Presente (5 conceptos) |
| 7.2 | Marco Teórico | 12 | Teoría + antecedentes | Presente (15 antecedentes) |
| 8 | Conclusiones y recomendaciones | 14 | Cierre | Presente |
| 8.1 | Conclusiones | 14 | Cierre | Presente (3 párrafos) |
| 8.2 | Recomendaciones | 16 | Cierre | Presente (3 recomendaciones) |
| 9 | Referencias | 17 | Bibliografía | Presente (15 entradas, formato APA) |

### Apartados ausentes respecto de una monografía de grado completa

| Apartado ausente | Severidad | Consecuencia |
|---|---|---|
| **Metodología / Diseño de investigación** | **Crítica** | El método declarado («revisión documental») no está operacionalizado. No hay protocolo replicable. |
| **Presentación del modelo conceptual propuesto** | **Crítica** | El entregable del OE-3 (Cap. 5.5) no existe como sección. |
| **Resultados / Análisis de hallazgos** | **Alta** | No hay separación entre revisión de literatura y hallazgos propios. |
| **Limitaciones del estudio** | **Alta** | No se declaran los límites de validez de las afirmaciones. |
| **Discusión** | **Media** | El contraste crítico entre fuentes queda implícito. |
| **Glosario** | **Media** | Parcialmente cubierto por el Cap. 7.1. |
| **Anexos** | **Media** | Sin instrumentos, matrices de literatura ni evidencia de respaldo. |
| **Lista de tablas y figuras** | **Baja** | El documento contiene 1 elemento gráfico y 0 tablas de contenido analítico. |
| **Cronograma y presupuesto** | **Baja** | Irrelevante para una revisión documental; **obligatorio** si se aprueba COLBASOFT como desarrollo. |

### Observación sobre el orden expositivo

El **Desarrollo temático (Cap. 6, p. 8) precede al Marco Referencial (Cap. 7, p. 10)**. Convencionalmente el marco teórico antecede al análisis, porque el análisis se apoya en él. Esta inversión produce una consecuencia verificable: el Cap. 6 cita a Ballou, Chopra y Meindl, Heizer y Render, y Slack et al. *antes* de que el Cap. 7.2 los presente y fundamente, y reproduce sus tesis de forma casi literal respecto del Resumen y del propio Cap. 7.2. **Existe redundancia sustantiva entre Resumen, Cap. 6 y Cap. 7.2.** No es un error de contenido; es un problema de arquitectura documental que debe consultarse con el Director (ver Fase F).

---

## A.3 Objetivos originales

> **Transcripción literal. No se modifican, no se reinterpretan.**

### Objetivo General (Cap. 5)

> «Analizar los factores teóricos para proponer un modelo conceptual de automatización en la gestión de inventarios de PYMES textiles del Eje Cafetero, con el fin de comprender su potencial para mejorar la eficiencia operativa y la competitividad, a partir de una revisión documental.»

*(El Cap. 3 enuncia una variante de este mismo objetivo que incluye el fragmento «hacia el año 2025», ausente en el Cap. 5. Ver Fase E, hallazgo E.3.1.)*

### Objetivos Específicos (Cap. 5.5)

| # | Enunciado literal | Verbo rector | ¿Cumplido en el documento? |
|---|---|---|---|
| **OE-1** | «Describir los conceptos clave de automatización de procesos, gestión de inventarios y eficiencia operativa en el contexto de PYMES textiles, identificando definiciones, tipos y beneficios documentos en literatura especializada.» | Describir | **Sí** — Cap. 7.1 define 5 conceptos; Cap. 6 desarrolla tipos y beneficios. |
| **OE-2** | «Revisar modelos teóricos de automatización aplicados a operaciones logísticas, como frameworks de adopción tecnológica, para evaluar su aplicabilidad en sectores fabricantes tradicionales como el textil colombiano.» | Revisar / Evaluar | **Parcialmente** — se invoca a Rogers (1962) como framework de adopción (Caps. 4, 7.1, 7.2, 8.1), pero **no se desarrolla ni se evalúa su aplicabilidad**, y Rogers no figura en el Cap. 9. No se revisan otros frameworks (TAM, UTAUT, TOE). |
| **OE-3** | «Sintetizar hallazgos teóricos que permitirán proponer un modelo conceptual integrado, destacando cómo la automatización puede optimizar la trazabilidad, reducir errores y potenciar la competitividad en el Eje Cafetero para 2025, calculando en comparaciones de enfoques documentados.» | Sintetizar / Proponer | **No** — el modelo conceptual integrado **no aparece en ningún apartado**. Ver hallazgo A.1. |

### Análisis de alineación objetivo ↔ proyecto COLBASOFT

| Dimensión | Monografía (fuente de verdad) | COLBASOFT (proyecto propuesto) | Veredicto |
|---|---|---|---|
| **Naturaleza del producto** | Modelo conceptual (Cap. 5) | Plataforma de software operativa | **Divergencia mayor** — requiere aprobación |
| **Método** | Revisión documental (Cap. 5) | Ingeniería de software + validación empírica | **Divergencia mayor** |
| **Implementación** | Explícitamente excluida (Cap. 4) | Núcleo del proyecto | **Divergencia mayor** |
| **Dominio** | Inventarios en PYMES textiles Eje Cafetero | Idéntico | **Alineado** |
| **Automatización** | Concepto central (Caps. 6, 7.1) | Concepto central | **Alineado** |
| **Trazabilidad** | Concepto presente (Palabras clave; Caps. 6, 7.1, 8.1) | En el título del proyecto | **Alineado** |
| **«Inteligente»** | Mención única y tangencial: la automatización total «incorpora inteligencia artificial» (Cap. 6) | En el título del proyecto | **Anclaje débil** — ver hallazgo C.1.5 |
| **Horizonte temporal** | 2025 (transversal) | 2027 (implícito en el nombre del proyecto) | **Divergencia** — requiere reproyección |

> **Aplicación de la Regla Innegociable 6.** Ningún objetivo se modifica en esta fase. Las divergencias quedan registradas como **solicitudes de decisión dirigidas al Director** (Fase F), no como cambios ejecutados.

---

## A.4 Variables implícitas

La monografía no declara un sistema de variables. Las siguientes se **infieren** del texto y se registran con su anclaje literal.

### Variables independientes

| Variable | Definición operativa inferida | Anclaje |
|---|---|---|
| **Nivel de automatización** | Grado de sustitución de tareas manuales por tecnología. El texto declara dos niveles: *parcial* («con software básico») y *total* («sistemas integrados que incorporan inteligencia artificial»). | Cap. 6 |
| **Resistencia a la automatización** | Barreras culturales, financieras y técnicas que retrasan la adopción. Factores citados: miedo a la obsolescencia laboral, inercia cultural, ausencia de capital financiero, falta de capacitación, barreras regulatorias. | Caps. 3, 4, 7.1 |
| **Capacidad de inversión tecnológica** | Disponibilidad de capital para adquirir procesos o maquinaria automatizada. | Resumen (Echeverry); Caps. 3, 6 |
| **Nivel de capacitación del personal** | Comprensión y apropiación de la herramienta por parte de los colaboradores. | Caps. 3, 8.2 |

### Variables dependientes

| Variable | Definición operativa inferida | Anclaje |
|---|---|---|
| **Eficiencia operativa** | «Capacidad de minimizar recursos y maximizar resultados, medida por reducción de tiempos muertos y errores». | Cap. 7.1 |
| **Competitividad empresarial** | «Ventaja sostenible en mercados […] con métricas como tiempo de respuesta y calidad de productos». | Cap. 7.1 |
| **Trazabilidad** | Capacidad de seguimiento del flujo de materiales; se afirma mejora del 55 % con automatización. | Palabras clave; Caps. 6, 7.2 |
| **Tasa de errores humanos** | Frecuencia de errores de registro; se afirma reducción del 40 %. | Caps. 3, 6, 7.2 |
| **Exactitud del inventario** | Correspondencia entre registro y existencia física. Propuesta explícitamente como indicador. | Cap. 8.2 |
| **Tiempos de registro** | Duración de la captura de movimientos. Propuesta explícitamente como indicador. | Cap. 8.2 |
| **Frecuencia de errores** | Propuesta explícitamente como indicador. | Cap. 8.2 |
| **Productividad** | Se afirman incrementos del 25 %, 30 % y 25–45 % en distintos puntos del texto. | Caps. 3, 7.2, 8.1 |
| **Nivel de reprocesos** | Repetición de trabajo por información errónea. | Caps. 3, 6, 7.2, 8.1 |
| **Pérdida de materia prima** | Merma atribuida a falta de digitalización en el sector textil. | Cap. 7.2 (Barreto y Ruiz, 2022) |

### Variables moderadoras / contextuales

| Variable | Anclaje |
|---|---|
| **Estacionalidad de la demanda** — específica del textil, «exacerbando rupturas en el flujo logístico» | Cap. 4 |
| **Tamaño de la empresa** (PYME) — condiciona ciclos productivos cortos | Caps. 4, 7.1, 7.2 |
| **Ubicación geográfica** (ciudades intermedias: Pereira, Risaralda, Quindío) | Caps. 4, 7.2 (DNP, 2021) |
| **Dependencia de mano de obra manual/barata** | Caps. 4, 6 |
| **Presión de importaciones y competencia global** | Cap. 4 |

> **Advertencia metodológica.** Estas 20 variables **no están declaradas como tales en la monografía**. Su formalización es un acto de ingeniería inversa del auditor y **debe ser validada por el Director** antes de servir de base a cualquier instrumento de medición (ver Fase F, categoría Investigación).

---

## A.5 Hipótesis implícitas

La monografía **no formula hipótesis explícitas** —consistente con un diseño de revisión documental. Las siguientes proposiciones funcionan como hipótesis de trabajo no declaradas y **sostienen todo el argumento**. Cada una es un supuesto que COLBASOFT heredará si no se somete a prueba.

| # | Hipótesis implícita | Anclaje | Riesgo si es falsa |
|---|---|---|---|
| **H1** | La gestión manual del inventario es la **principal** causa de ineficiencia logística en las PYMES textiles del Eje Cafetero. | Caps. 3, 4, 8.1 | El producto atacaría un síntoma, no la causa. |
| **H2** | Digitalizar el registro de inventario **produce** mejoras medibles en eficiencia y competitividad (relación causal, no correlacional). | Caps. 6, 7.2, 8.1 | Los beneficios prometidos no se materializarían. |
| **H3** | La resistencia a la adopción es **cultural y financiera**, no funcional (el software existente no falla; las empresas no lo adoptan). | Caps. 3, 4, 7.1 | Si la causa fuera funcional (mal ajuste al proceso textil), COLBASOFT fallaría por las mismas razones. |
| **H4** | Existe **demanda latente**: las PYMES adoptarían una solución si fuera accesible y sencilla. | Caps. 8.1, 8.2; CEPAL (2022) | Riesgo de producto sin usuarios. |
| **H5** | Los hallazgos de otros contextos (Antioquia, México, Medellín, América Latina) son **transferibles** al Eje Cafetero. | Cap. 7.2 | Invalidaría la base evidencial completa. |
| **H6** | La adopción **escalonada** (empezar simple, crecer después) es más efectiva que la implantación completa. | Cap. 8.2 (Heizer y Render) | Condiciona directamente la estrategia de producto. |
| **H7** | El personal operativo de una PYME textil puede **apropiarse** de una herramienta digital con capacitación práctica. | Cap. 8.2 (Slack et al.) | Determina el nivel de exigencia de usabilidad. |
| **H8** | Los indicadores propuestos (exactitud, tiempos de registro, frecuencia de errores) son **suficientes** para demostrar el beneficio. | Cap. 8.2 | El plan de validación sería incompleto. |
| **H9** | Las PYMES textiles del Eje Cafetero comparten un **proceso de inventario suficientemente homogéneo** como para admitir un modelo único. | Implícito en «modelo conceptual» (Caps. 5, 8.1) | Impediría un producto estándar; forzaría alta configurabilidad. |
| **H10** | La automatización **no destruye empleo neto** porque el reentrenamiento mitiga la obsolescencia laboral. | Cap. 6 (Slack et al.) | Riesgo de rechazo social del producto. |

> **Nota crítica.** H2 y H5 son las hipótesis de mayor carga: **toda la justificación cuantitativa de COLBASOFT descansa sobre ellas**, y ninguna de las dos se somete a contraste en el documento.

---

## A.6 Conceptos clave

### A.6.1 Conceptos formalmente definidos (Cap. 7.1 — Marco conceptual)

| Concepto | Definición literal (abreviada) | Autor de anclaje |
|---|---|---|
| **Automatización** | «Uso de tecnologías para ejecutar tareas repetitivas sin intervención humana, incluyendo niveles parciales y totales». | Heizer y Render (2014) |
| **Eficiencia Operativa** | «Capacidad de minimizar recursos y maximizar resultados, medida por reducción de tiempos muertos y errores». | Chopra y Meindl (2016) |
| **Competitividad Empresarial** | «Ventaja sostenible en mercados, influida por innovación tecnológica y reducción de costos». | Slack et al. (2010) |
| **Gestión de Inventarios** | «Control de stocks para equilibrar disponibilidad de materiales y costos, esencial en logística para prevenir rupturas o excesos». | Ballou (2004) |
| **Resistencia a la Automatización** | «Barreras culturales, financieras y técnicas que retrasan la adopción de tecnologías». | Rogers (1962) |

### A.6.2 Palabras clave declaradas (Cap. 2)

`Automatización` · `Inventarios` · `Procesos Logísticos` · `PYMES Textiles` · `Eficiencia` · `Competitividad` · `Trazabilidad`

### A.6.3 Conceptos operativos usados pero **no definidos**

Estos aparecen en el texto y son **indispensables** para especificar COLBASOFT, pero la monografía nunca los define. Constituyen el primer bloque de trabajo conceptual pendiente.

| Concepto no definido | Dónde se usa | Por qué importa para COLBASOFT |
|---|---|---|
| **Trazabilidad** | Palabras clave; Caps. 6, 7.1, 8.1 — **está en el título del proyecto** | Es un concepto nuclear del producto y **carece de definición operativa**. Crítico. |
| **Movimiento de inventario** | Caps. 8.1, 8.2 («entradas, salidas y movimientos») | Es la unidad transaccional del sistema. |
| **Monitoreo en tiempo real** | Caps. 6, 7.1, 7.2, 8.2 | Determina requisitos no funcionales fundamentales. |
| **Sensores** | Cap. 6 («integrando sensores para monitoreo en tiempo real») | Implica hardware; no se especifica cuál ni para qué. |
| **ERP** | Cap. 6 («modelos conceptuales como ERP adaptados a textiles colombianos») | Referencia a una categoría de producto sin delimitar. |
| **Inteligencia artificial** | Cap. 6 (única mención) | **Está en el nombre del proyecto** («inteligente») con un solo anclaje textual tangencial. |
| **PYME** | Transversal | No se adopta un criterio de clasificación (Ley 590/2000, Decreto 957/2019, empleados vs. activos). |
| **Eje Cafetero** | Transversal | Se mencionan Risaralda, Quindío, Pereira, Armenia, pero no se delimita el alcance geográfico. |
| **Sector textil** | Transversal | No se distingue entre confección, tejeduría, comercialización o insumos. |
| **Exactitud del inventario** | Cap. 8.2 | Indicador propuesto sin fórmula ni umbral. |
| **Ruptura de stock / sobre stock** | Caps. 3, 7.1 | Eventos operativos sin definición ni criterio de detección. |
| **Modelo conceptual** | Caps. 5, 5.5, 6, 8.1 | El **entregable principal** del trabajo carece de definición de forma y contenido. |
| **Automatización parcial vs. total** | Cap. 6 | La distinción define el posicionamiento del producto. |
| **Flujo de materiales** | Cap. 6 | Núcleo del dominio logístico. |
| **Coordinación con proveedores** | Cap. 6 | Sugiere un módulo de compras no delimitado. |
| **Detección de fraudes** | Cap. 6 | Funcionalidad insinuada, jamás desarrollada. **No debe convertirse en requisito sin decisión del Director** (Regla Innegociable 3). |

### A.6.4 Teorías y marcos invocados

| Marco | Autor | Estado en el documento |
|---|---|---|
| **Difusión de Innovaciones** | Rogers (1962) | Invocado 4 veces (Caps. 4, 7.1, 7.2, 8.1). **No desarrollado. No referenciado en Cap. 9.** |
| **The Second Machine Age** | Brynjolfsson y McAffe (2014) | Invocado 1 vez (Cap. 4). **No referenciado en Cap. 9.** Apellido escrito «McAffe». |
| **Cadena de suministro** | Chopra y Meindl (2016); Bowersox y Closs (2007) | Desarrollado. Referenciado. |
| **Administración de operaciones** | Heizer y Render (2014); Slack et al. (2010) | Desarrollado. Referenciado. |
| **Logística de inventarios** | Ballou (2004) | Desarrollado. Referenciado. Autor más citado del documento. |
| **ODS de la ONU** | ONU (ODS 8, ODS 9) | Invocado 3 veces con **objetivos distintos** (ODS 8 en Cap. 3; ODS 9 en Cap. 4; «ONU, 2015» en Cap. 6). **No referenciado en Cap. 9.** |
| **Colombia, una economía en transición** | Juan Carlos Echeverry García (2018) | Invocado 1 vez (Resumen). **No referenciado en Cap. 9.** |

---

## A.7 Referencias utilizadas

### A.7.1 Referencias formales (Cap. 9 — 15 entradas)

| # | Referencia | Tipo | ¿Citada en el cuerpo? |
|---|---|---|---|
| 1 | ANDI. (2023). *Informe de transformación digital en PYMES.* | Institucional | Sí — Caps. 3, 4, 6, 7.2, 8.1 |
| 2 | Ballou, R. H. (2004). *Logística: Administración de la cadena de suministro* (5.ª ed.). Pearson. | Libro | Sí — Resumen; Caps. 6, 7.1, 7.2, 8.1 |
| 3 | Barreto, S., & Ruiz, L. (2022). *Trazabilidad en inventarios textiles […] Medellín.* Rev. Colombiana de Producción, 18(4), 112–128. | Artículo | Sí — Cap. 7.2 |
| 4 | Bowersox, D. J., & Closs, D. J. (2007). *Logística de negocios.* McGraw-Hill. | Libro | Sí — Cap. 7.2 (única mención) |
| 5 | Cámara de Comercio de Pereira. (2022). *Informe de competitividad empresarial 2022.* | Institucional | Sí — Caps. 7.2, 8.1 |
| 6 | CEPAL. (2022). *Transformación digital para PYMES en América Latina.* | Institucional | Sí — Caps. 3, 4, 6, 7.2, 8.1 |
| 7 | Chopra, S., & Meindl, P. (2016). *Administración de la cadena de suministro* (6.ª ed.). Pearson. | Libro | Sí — Resumen; Caps. 6, 7.1, 7.2, 8.1 |
| 8 | DNP. (2021). *Índice de Desarrollo Digital Empresarial.* | Institucional | Sí — Cap. 7.2 |
| 9 | Heizer, J., & Render, B. (2014). *Administración de operaciones* (11.ª ed.). Pearson. | Libro | Sí — Resumen; Caps. 6, 7.1, 7.2, 8.1, 8.2 |
| 10 | Hernández, F., & Salazar, D. (2021). *Automatización de procesos logísticos en PYMES manufactureras latinoamericanas.* Rev. Latinoamericana de Tecnología, 15(1), 90–108. | Artículo | Sí — Caps. 6, 7.2, 8.1 |
| 11 | López, A., Ramírez, J., & Torres, M. (2020). *Digitalización de inventarios y productividad en manufactura ligera.* Rev. Ingeniería Industrial, 12(2), 60–75. | Artículo | Sí — Caps. 7.2, 8.1 |
| 12 | Martínez, J., & Gómez, C. (2019). *Problemas de inventario en PYMES manufactureras colombianas.* Rev. Facultad de Ingeniería, 28(3), 45–60. | Artículo | Sí — Cap. 7.2 |
| 13 | MinCIT. (2020). *Reporte de industria textil 2020.* | Institucional | Sí — Caps. 3, 7.2 |
| 14 | Silva, P. (2018). *Sistemas de información para decisiones logísticas en pequeñas empresas.* Journal of Operations, 9(1), 22–35. | Artículo | Sí — Caps. 7.2, 8.2 |
| 15 | Slack, N., Chambers, S., & Johnston, R. (2010). *Administración de operaciones* (6.ª ed.). Pearson. | Libro | Sí — Resumen; Caps. 6, 7.1, 7.2, 8.1, 8.2 |

**Composición:** 5 libros (33 %) · 5 artículos (33 %) · 5 informes institucionales (33 %).
**Antigüedad:** rango 2004–2023 · mediana ≈ 2020 · **5 fuentes con más de 10 años** (Ballou 2004, Bowersox y Closs 2007, Slack et al. 2010, Heizer y Render 2014).
**Cobertura:** 0 fuentes en inglés en la lista formal · 0 fuentes indexadas verificables por DOI · 0 fuentes primarias de campo.

### A.7.2 Fuentes citadas en el cuerpo pero **AUSENTES del Cap. 9**

> Nueve fuentes sostienen afirmaciones sustantivas —incluidas las cifras de mayor impacto— y **no aparecen en la bibliografía**.

| # | Fuente citada | Apartado(s) | Qué sostiene |
|---|---|---|---|
| 1 | **DANE (2023)** | Caps. 3, 4 | El 5–7 % del PIB manufacturero regional; empleo del sector |
| 2 | **Cámara de Comercio de Armenia (2022 y 2023)** | Caps. 3, 4, 6 | Pérdidas «en miles de millones de pesos»; +30 % de pérdidas por errores de inventario |
| 3 | **Universidad Tecnológica de Pereira (2022)** | Cap. 4 | El 60 % de las PYMES locales carece de sistemas digitales |
| 4 | **OIT (2021)** | Caps. 4, 6 | Costos operativos elevados; reducción de errores del 40 % |
| 5 | **Rogers, E. (1962)** — *Diffusion of Innovations* | Caps. 4, 7.1, 7.2, 8.1 | Todo el andamiaje teórico de la resistencia al cambio |
| 6 | **Brynjolfsson y McAffe (2014)** — *The Second Machine Age* | Cap. 4 | El rezago de los sectores tradicionales |
| 7 | **Juan Carlos Echeverry García (2018)** — *Colombia, una economía en transición* | Resumen | Resistencia a la adopción y falta de capital |
| 8 | **Gobernación de Risaralda (2024)** | Cap. 8.1 | Proyecciones de mejora del 25–45 % en productividad |
| 9 | **ONU** — ODS 8, ODS 9, «ONU 2015» | Caps. 3, 4, 6 | Alineación con desarrollo sostenible |

> **Impacto.** El Cap. 7.2 declara integrar «15 antecedentes seleccionados». El conteo de referencias formales coincide (15). Sin embargo, el documento **cita en total 24 fuentes distintas**, de las cuales 9 (37,5 %) carecen de respaldo bibliográfico. Este es el hallazgo académico de mayor severidad de la auditoría.

---

## A.8 Problemas identificados

> **Problemas del dominio**, tal como los enuncia la monografía. Este es el catálogo canónico de dolores que COLBASOFT debe atacar. **No se añade ninguno.**

| # | Problema | Manifestación literal | Anclaje |
|---|---|---|---|
| P-01 | **Registro manual del inventario** | «cuadernos, hojas de cálculo sueltas y registros manuales» | Cap. 3 |
| P-02 | **Errores humanos frecuentes** | Errores de registro derivados del método manual; 67 % de PYMES afectadas | Caps. 3, 7.2 |
| P-03 | **Información desactualizada** | «no refleja el flujo real de mercancía» | Cap. 3 |
| P-04 | **Reprocesos costosos** | Repetición de trabajo por datos incorrectos | Caps. 3, 6, 8.1 |
| P-05 | **Tiempos de respuesta lentos** | Demora en la reacción operativa | Caps. 3, 4 |
| P-06 | **Falta de trazabilidad** | «fallas en la trazabilidad y poca capacidad de control» | Caps. 3, 4 |
| P-07 | **Rupturas de stock y sobre stock** | «riesgos en sobre stock o escasez» | Cap. 3 |
| P-08 | **Interrupciones de producción por faltantes** | Paradas por indisponibilidad de insumos | Caps. 3, 6 |
| P-09 | **Aumento de plazos de entrega** | «reduciendo la satisfacción del cliente» | Cap. 3 |
| P-10 | **Pérdidas económicas** | «miles de millones de pesos anuales para el sector» | Cap. 3 |
| P-11 | **Pérdida de materia prima** | Merma en textiles por falta de digitalización | Cap. 7.2 |
| P-12 | **Baja competitividad global** | Vulnerabilidad frente a importaciones y competidores automatizados de Asia | Caps. 3, 4 |
| P-13 | **Vulnerabilidad de la cadena de suministro** | Mayor exposición a interrupciones | Cap. 4 |
| P-14 | **Informalidad de los procesos logísticos** | Causa principal de ineficiencia según CEPAL/ANDI | Cap. 3 |
| P-15 | **Rezago digital sectorial** | 72 % de PYMES sin herramientas tecnológicas | Cap. 7.2 |
| P-16 | **Resistencia cultural al cambio** | «miedo a la obsolescencia laboral y la inercia cultural» | Cap. 4 |
| P-17 | **Falta de capital para automatizar** | «no cuentan con el capital financiero» | Resumen; Caps. 3, 6 |
| P-18 | **Escasez de capacitación laboral** | Ausencia de competencias digitales | Caps. 3, 8.2 |
| P-19 | **Barreras regulatorias** | «desalientan la adopción de soluciones automatizadas» | Cap. 3 |
| P-20 | **Falta de inversión en infraestructura tecnológica** | Carencia estructural previa al software | Cap. 3 |
| P-21 | **Estacionalidad de la demanda textil** | Rupturas del flujo logístico por ciclos | Cap. 4 |
| P-22 | **Baja resiliencia ante crisis económicas** | Fragilidad de la PYME local | Cap. 4 |
| P-23 | **Descoordinación entre inventario, compras y distribución** | Falta de sincronización logística | Cap. 7.2 (Bowersox y Closs) |
| P-24 | **Riesgo de fraude en logística** | Dificultad de detección sin sistema | Cap. 6 |

> **Observación de trazabilidad.** P-19, P-20, P-21 y P-22 son problemas de **contexto macro**, no resolubles por software. Deben quedar registrados como *restricciones del entorno*, no como requisitos. P-24 se menciona una sola vez y de forma tangencial: **no debe promoverse a funcionalidad sin decisión expresa del Director** (Regla Innegociable 3).

---

## A.9 Beneficios esperados

> Beneficios que la monografía atribuye a la automatización. **Se transcriben con su cifra y su fuente exactas**, incluidas las inconsistencias entre ellos (analizadas en Fase E).

| # | Beneficio | Cuantificación declarada | Anclaje |
|---|---|---|---|
| B-01 | Reducción de errores humanos | **40 %** | Caps. 6 (OIT, 2021), 7.2 (Hernández y Salazar, 2021) |
| B-02 | Mejora de la trazabilidad | **55 %** | Cap. 7.2 (Hernández y Salazar, 2021) |
| B-03 | Incremento de productividad | **hasta 30 %** | Cap. 7.2 (López et al., 2020) |
| B-04 | Mejora de eficiencia (LatAm) | **hasta 25 %** | Cap. 7.2 (CEPAL, 2022) |
| B-05 | Mejora de eficiencia operativa | **hasta 40 %** | Cap. 3 (CEPAL) — **contradice B-04** |
| B-06 | Mejora de productividad regional | **25–45 %** | Cap. 8.1 (Gobernación de Risaralda, 2024) |
| B-07 | Estandarización de tareas repetitivas | Cualitativo | Caps. 6, 7.1, 7.2 |
| B-08 | Visibilidad del inventario en tiempo real | Cualitativo | Caps. 6, 7.2 |
| B-09 | Mejor toma de decisiones | Cualitativo | Caps. 6, 7.2, 8.2 |
| B-10 | Reducción de costos operativos | Cualitativo | Caps. 6, 7.1 |
| B-11 | Reducción de tiempos muertos | Cualitativo | Caps. 6, 7.1 |
| B-12 | Mayor capacidad de respuesta al mercado | Cualitativo | Caps. 6, 7.1, 7.2 |
| B-13 | Mejora de la competitividad | Cualitativo | Transversal |
| B-14 | Reducción de reprocesos | Cualitativo | Caps. 6, 8.1 |
| B-15 | Mejora de la calidad de los datos | Cualitativo | Cap. 8.1 |
| B-16 | Coordinación con proveedores locales | Cualitativo | Cap. 6 |
| B-17 | Detección de fraudes | Cualitativo | Cap. 6 |
| B-18 | Creación de empleos calificados | Cualitativo | Cap. 3 |
| B-19 | Fortalecimiento de la resiliencia económica regional | Cualitativo | Caps. 3, 6 |
| B-20 | Potenciación de exportaciones | Cualitativo | Cap. 6 |
| B-21 | Alineación con los ODS (8 y 9) | Cualitativo | Caps. 3, 4, 6 |
| B-22 | Mitigación de la obsolescencia laboral vía reentrenamiento | Cualitativo | Cap. 6 |

**Balance:** 6 beneficios cuantificados (27 %) · 16 cualitativos (73 %). De los 6 cuantificados, **4 provienen de fuentes ausentes de la bibliografía** (B-01 vía OIT, B-05 vía CEPAL sin cifra respaldada, B-06 vía Gobernación de Risaralda) y **2 se contradicen entre sí** (B-04 vs. B-05).

---

## A.10 Restricciones

### A.10.1 Restricciones declaradas por la monografía (vinculantes)

| # | Restricción | Anclaje | Efecto sobre COLBASOFT |
|---|---|---|---|
| R-01 | **Alcance exclusivamente documental** — «sin proponer soluciones prácticas de implementación» | Cap. 4 | **Bloquea el desarrollo** hasta que el Director autorice la extensión de alcance |
| R-02 | **Sin intervención en empresas reales** — «facilitando análisis críticos sin intervenir empresas reales» | Cap. 4 | **Impide validación de campo** bajo el marco actual |
| R-03 | **El producto es un modelo conceptual, no un sistema** — «Más que desarrollar un sistema completo» | Cap. 8.1 | Redefine el entregable comprometido |
| R-04 | **Horizonte temporal: 2025** | Transversal | Marco vencido; requiere reproyección |
| R-05 | **Ámbito geográfico: Eje Cafetero** (Pereira, Risaralda, Quindío, Armenia) | Transversal | Delimita el mercado objetivo |
| R-06 | **Segmento: PYMES del sector textil** | Transversal | Delimita el perfil de usuario |
| R-07 | **Base evidencial: 15 antecedentes** | Cap. 7.2 | Techo de la fundamentación disponible |

### A.10.2 Restricciones del contexto (heredadas del dominio)

| # | Restricción | Anclaje | Efecto sobre COLBASOFT |
|---|---|---|---|
| R-08 | **Capacidad financiera limitada de las PYMES** | Resumen; Caps. 3, 6 | Obliga a un modelo de bajo costo; excluye soluciones onerosas |
| R-09 | **Baja alfabetización digital del personal** | Caps. 3, 8.2 | Impone usabilidad extrema como requisito no funcional prioritario |
| R-10 | **Resistencia cultural al cambio** | Caps. 4, 7.1 | Exige estrategia de adopción, no solo producto |
| R-11 | **Infraestructura tecnológica deficiente** | Cap. 3 | Condiciona supuestos de conectividad y equipamiento |
| R-12 | **Barreras regulatorias** | Cap. 3 | Fuera del control del proyecto |
| R-13 | **Adopción escalonada, no big-bang** | Cap. 8.2 | Restricción de estrategia de producto |
| R-14 | **Dependencia del reentrenamiento del personal** | Caps. 6, 8.2 | La capacitación es parte del entregable, no un extra |

### A.10.3 Restricciones académicas del proyecto de grado

| # | Restricción | Origen |
|---|---|---|
| R-15 | Nivel formativo: Tecnólogo en Desarrollo de Software | Portada |
| R-16 | Institución: CIAF — Escuela de Ingeniería | Portada |
| R-17 | Equipo de 3 autores | Portada |
| R-18 | Asesor único: Edwin Andrés Cabrera Arredondo | Portada |
| R-19 | La monografía es inmodificable | Regla Innegociable 1 |

---

# FASE B — INVENTARIO DE CONOCIMIENTO

> Matriz completa de conceptos. **Ningún concepto relevante se omite.** La tercera columna registra la decisión de preservación, según las Reglas Innegociables 2 y 3.
>
> **Leyenda:** 🟢 *Conservar íntegro* — se traslada sin alteración · 🔵 *Conservar y ampliar* — se preserva y se le añade capa de ingeniería · 🟡 *Conservar y definir* — se usa pero carece de definición operativa · 🔴 *Conservar y verificar* — su respaldo documental es deficiente · ⚪ *Conservar como contexto* — no genera requisito

## B.1 Conceptos teóricos fundacionales

| Concepto | Ubicación en la monografía | Debe conservarse / ampliarse |
|---|---|---|
| El inventario como estabilizador del flujo logístico | Cap. 7.2; Resumen; Cap. 6 (Ballou, 2004) | 🔵 **Conservar y ampliar** — es el axioma raíz del proyecto. Ampliar hacia un modelo de dominio (Fase 2). |
| Precisión de la información de inventario como factor competitivo | Caps. 6, 7.1, 7.2 (Chopra y Meindl, 2016) | 🔵 **Conservar y ampliar** — fundamenta el requisito de exactitud. |
| La automatización estandariza tareas y reduce error humano | Caps. 6, 7.1, 7.2 (Heizer y Render, 2014) | 🔵 **Conservar y ampliar** — justificación central del producto. |
| La tecnología aumenta visibilidad y trazabilidad | Caps. 6, 7.2 (Slack et al., 2010) | 🔵 **Conservar y ampliar** — fundamenta el eje «trazabilidad» del título de COLBASOFT. |
| Los procesos logísticos requieren sincronización inventario–compras–distribución | Cap. 7.2 (Bowersox y Closs, 2007) | 🔵 **Conservar y ampliar** — define la frontera del sistema. Fuente subutilizada (1 sola mención). |
| Difusión de Innovaciones / etapas de adopción | Caps. 4, 7.1, 7.2, 8.1 (Rogers, 1962) | 🔴 **Conservar y verificar** — marco invocado 4 veces, jamás desarrollado y **ausente del Cap. 9**. Requiere la referencia formal antes de sostener el OE-2. |
| Rezago tecnológico de los sectores tradicionales | Cap. 4 (Brynjolfsson y McAffe, 2014) | 🔴 **Conservar y verificar** — **ausente del Cap. 9**; apellido posiblemente mal transcrito. |
| Resistencia a la adopción por falta de capital | Resumen (Echeverry, 2018) | 🔴 **Conservar y verificar** — **ausente del Cap. 9**. |

## B.2 Conceptos operativos del dominio

| Concepto | Ubicación en la monografía | Debe conservarse / ampliarse |
|---|---|---|
| **Automatización** (definición formal) | Cap. 7.1 | 🟢 **Conservar íntegro** — definición canónica del proyecto. |
| Automatización parcial vs. total | Cap. 6 | 🔵 **Conservar y ampliar** — define el posicionamiento de COLBASOFT en una escala de madurez. |
| **Eficiencia operativa** (definición formal) | Cap. 7.1 | 🟢 **Conservar íntegro** + 🔵 operacionalizar en métricas. |
| **Competitividad empresarial** (definición formal) | Cap. 7.1 | 🟢 **Conservar íntegro** — nivel estratégico, no funcional. |
| **Gestión de inventarios** (definición formal) | Cap. 7.1 | 🔵 **Conservar y ampliar** — es el núcleo funcional. |
| **Resistencia a la automatización** (definición formal) | Cap. 7.1 | 🔵 **Conservar y ampliar** — se traduce en requisitos de adopción y usabilidad. |
| **Trazabilidad** | Palabras clave; Caps. 6, 7.1, 8.1 | 🟡 **Conservar y definir** — **CRÍTICO**: está en el título del proyecto y **no tiene definición operativa en la monografía**. |
| Movimiento de inventario (entradas, salidas, movimientos) | Caps. 8.1, 8.2 | 🟡 **Conservar y definir** — unidad transaccional del sistema. |
| Monitoreo en tiempo real | Caps. 6, 7.1, 7.2, 8.2 | 🟡 **Conservar y definir** — «tiempo real» requiere umbral cuantificado. |
| Flujo de materiales | Cap. 6 | 🟡 **Conservar y definir** |
| Coordinación con proveedores | Cap. 6 | 🟡 **Conservar y definir** — insinúa un módulo de compras aún sin delimitar. |
| Ruptura de stock / sobre stock | Caps. 3, 7.1 | 🟡 **Conservar y definir** — eventos que el sistema debería detectar. |
| Ciclos productivos cortos en PYMES | Caps. 4, 7.1 | 🔵 **Conservar y ampliar** — condiciona el ritmo de actualización de datos. |
| Estandarización de entradas, salidas y movimientos | Cap. 8.2 | 🔵 **Conservar y ampliar** — recomendación explícita, traducible a requisito. |
| Estacionalidad de la demanda textil | Cap. 4 | 🔵 **Conservar y ampliar** — particularidad diferencial del sector. |
| Sensores para monitoreo | Cap. 6 | 🟡 **Conservar y definir** — mención única; **no promover a requisito sin decisión del Director** (Regla 3). |
| ERP adaptado a textiles colombianos | Cap. 6 | 🟡 **Conservar y definir** — referencia de categoría, no especificación. |
| Inteligencia artificial | Cap. 6 (mención única) | 🔴 **Conservar y verificar** — **anclaje textual mínimo frente al peso que tiene en el nombre «Plataforma inteligente»**. |
| Detección de fraudes | Cap. 6 (mención única) | ⚪ **Conservar como contexto** — **no convertir en funcionalidad sin autorización** (Regla 3). |

## B.3 Problemática documentada

| Concepto | Ubicación en la monografía | Debe conservarse / ampliarse |
|---|---|---|
| Registro manual (cuadernos, hojas sueltas) | Cap. 3 | 🔵 **Conservar y ampliar** — es el *statu quo* que COLBASOFT reemplaza. |
| Errores humanos frecuentes | Caps. 3, 6, 7.2 | 🔵 **Conservar y ampliar** — es el problema P-02, medible. |
| Información desactualizada | Cap. 3 | 🔵 **Conservar y ampliar** |
| Reprocesos | Caps. 3, 6, 8.1 | 🔵 **Conservar y ampliar** |
| Fallas de trazabilidad | Caps. 3, 4 | 🔵 **Conservar y ampliar** |
| Interrupciones productivas por faltantes | Caps. 3, 6 | 🔵 **Conservar y ampliar** |
| Retrasos en entregas / insatisfacción del cliente | Cap. 3 | 🔵 **Conservar y ampliar** |
| Pérdida de materia prima en textiles | Cap. 7.2 (Barreto y Ruiz, 2022) | 🔵 **Conservar y ampliar** — evidencia sectorial más próxima al caso. |
| Informalidad logística | Cap. 3 | ⚪ **Conservar como contexto** |
| Descoordinación inventario–compras–distribución | Cap. 7.2 | 🔵 **Conservar y ampliar** |
| Barreras regulatorias | Cap. 3 | ⚪ **Conservar como contexto** — fuera del alcance del software. |
| Falta de infraestructura tecnológica | Cap. 3 | ⚪ **Conservar como contexto** — condiciona supuestos técnicos. |
| Escasez de capacitación laboral | Caps. 3, 8.2 | 🔵 **Conservar y ampliar** — la capacitación es parte del entregable. |
| Miedo a la obsolescencia laboral | Cap. 4 | ⚪ **Conservar como contexto** — riesgo de adopción. |
| Presión de importaciones / competidores asiáticos | Cap. 4 | ⚪ **Conservar como contexto** |
| Baja resiliencia ante crisis | Cap. 4 | ⚪ **Conservar como contexto** |

## B.4 Evidencia cuantitativa

| Concepto | Ubicación en la monografía | Debe conservarse / ampliarse |
|---|---|---|
| 5–7 % del PIB manufacturero regional | Caps. 3, 4 (DANE, 2023) | 🔴 **Conservar y verificar** — fuente ausente del Cap. 9. En Cap. 4 la cifra aparece como «5-7 del PIB», sin el símbolo de porcentaje. |
| Más de 50.000 empleos en el sector | Cap. 4 | 🔴 **Conservar y verificar** — sin citación directa adjunta. |
| 30 % menor productividad vs. empresas digitalizadas | Cap. 3 (CEPAL, 2022 / ANDI, 2023) | 🔴 **Conservar y verificar** |
| +30 % de pérdidas por errores de inventario | Cap. 4 (C.C. Armenia, 2023) | 🔴 **Conservar y verificar** — fuente ausente del Cap. 9. |
| 60 % de PYMES locales sin sistemas digitales | Cap. 4 (UTP, 2022) | 🔴 **Conservar y verificar** — fuente ausente del Cap. 9. |
| 67 % de PYMES con errores por registro manual | Cap. 7.2 (Martínez y Gómez, 2019) | 🟢 **Conservar íntegro** — fuente respaldada en el Cap. 9. |
| 72 % de PYMES sin herramientas tecnológicas | Cap. 7.2 (ANDI, 2023) | 🟢 **Conservar íntegro** — fuente respaldada. **Cifra ancla del proyecto.** |
| +30 % de productividad por digitalización | Cap. 7.2 (López et al., 2020) | 🟢 **Conservar íntegro** — fuente respaldada. |
| −40 % errores / +55 % trazabilidad | Cap. 7.2 (Hernández y Salazar, 2021) | 🟢 **Conservar íntegro** — fuente respaldada. **Cifras ancla del proyecto.** |
| +25 % de eficiencia en PYMES LatAm | Cap. 7.2 (CEPAL, 2022) | 🟢 **Conservar íntegro** — fuente respaldada. |
| +40 % de eficiencia operativa | Cap. 3 (CEPAL) | 🔴 **Conservar y verificar** — **contradice el 25 % del Cap. 7.2 atribuido a la misma fuente**. |
| −40 % errores atribuido a la OIT | Cap. 6 (OIT, 2021) | 🔴 **Conservar y verificar** — fuente ausente; **la misma cifra se atribuye a Hernández y Salazar en Cap. 7.2**. |
| 25–45 % de mejora en productividad | Cap. 8.1 (Gob. de Risaralda, 2024) | 🔴 **Conservar y verificar** — fuente ausente del Cap. 9. |
| Pérdidas de «miles de millones de pesos anuales» | Cap. 3 (C.C. Armenia, 2022) | 🔴 **Conservar y verificar** — magnitud imprecisa; fuente ausente. |
| Baja digitalización en ciudades intermedias | Cap. 7.2 (DNP, 2021) | 🟢 **Conservar íntegro** — fuente respaldada. |
| Problemas de control de inventario en PYMES textiles de Pereira | Caps. 7.2, 8.1 (C.C. Pereira, 2022) | 🟢 **Conservar íntegro** — **evidencia local más directa y respaldada del documento**. |

## B.5 Propuestas y recomendaciones

| Concepto | Ubicación en la monografía | Debe conservarse / ampliarse |
|---|---|---|
| Digitalización progresiva del inventario | Cap. 8.2 | 🔵 **Conservar y ampliar** — define la hoja de ruta de adopción. |
| Iniciar con herramientas sencillas y escalables | Cap. 8.2 (Heizer y Render) | 🔵 **Conservar y ampliar** — restricción de diseño de producto. |
| Aplicativos de registro digital de entradas/salidas/movimientos | Cap. 8.2 | 🔵 **Conservar y ampliar** — **la descripción funcional más concreta de toda la monografía**. Semilla del núcleo transaccional. |
| Capacitación práctica del personal | Cap. 8.2 (Slack et al.) | 🔵 **Conservar y ampliar** — entregable complementario obligatorio. |
| Evaluaciones periódicas del proceso logístico | Cap. 8.2 | 🔵 **Conservar y ampliar** — base del plan de validación. |
| Indicador: exactitud del inventario | Cap. 8.2 | 🟡 **Conservar y definir** — falta fórmula y umbral. |
| Indicador: tiempos de registro | Cap. 8.2 | 🟡 **Conservar y definir** — falta línea base. |
| Indicador: frecuencia de errores | Cap. 8.2 | 🟡 **Conservar y definir** — falta línea base. |
| Datos en tiempo real para decisión | Cap. 8.2 (Silva, 2018) | 🔵 **Conservar y ampliar** |
| Modelo flexible, no sistema completo | Cap. 8.1 | 🔵 **Conservar y ampliar** — **restricción explícita del alcance**; su modificación exige decisión del Director. |
| Integración de niveles parcial/total según Rogers | Cap. 8.1 | 🔴 **Conservar y verificar** — depende de una fuente sin respaldo bibliográfico. |
| Justificación de futuras inversiones mediante indicadores | Cap. 8.2 | 🔵 **Conservar y ampliar** — base del caso de negocio. |

## B.6 Marco institucional y ético

| Concepto | Ubicación en la monografía | Debe conservarse / ampliarse |
|---|---|---|
| Alineación con ODS 8 (trabajo decente) | Cap. 3 | 🔴 **Conservar y verificar** — ONU ausente del Cap. 9; **conflicto con el ODS 9 del Cap. 4**. |
| Alineación con ODS 9 (industria e innovación) | Cap. 4 | 🔴 **Conservar y verificar** — mismo conflicto. |
| Liderazgo sostenible del textil colombiano en LatAm | Cap. 3 (ANDI, MinCIT) | ⚪ **Conservar como contexto** |
| Reducción de desigualdades y atracción de inversión | Cap. 3 | ⚪ **Conservar como contexto** |
| Reentrenamiento para mitigar obsolescencia laboral | Cap. 6 (Slack et al.) | 🔵 **Conservar y ampliar** — dimensión ética del producto. |
| Creación de empleos calificados | Cap. 3 | ⚪ **Conservar como contexto** |

---

# FASE C — VACÍOS DE INGENIERÍA

> Todo lo que falta para convertir la propuesta conceptual en un proyecto profesional de ingeniería de software. **Se identifican vacíos; no se resuelven en esta fase.**

## 🔴 C.1 — CRÍTICO
*Bloquean el inicio del proyecto. Sin resolverlos, cualquier trabajo posterior carece de fundamento.*

| # | Vacío | Evidencia de origen | Impacto |
|---|---|---|---|
| **C.1.1** | **Autorización de cambio de naturaleza del proyecto.** La monografía excluye explícitamente la implementación (Cap. 4) y declara que no se busca «desarrollar un sistema completo» (Cap. 8.1). COLBASOFT es exactamente eso. | Caps. 4, 8.1 | **Bloqueante absoluto.** Sin la aprobación formal del Director, COLBASOFT contradice su propia fuente de verdad y viola la Regla Innegociable 6. |
| **C.1.2** | **El modelo conceptual comprometido no existe.** El OE-3 promete «proponer un modelo conceptual integrado» y ningún apartado lo presenta. | Caps. 5.5, 8.1 | El puente entre teoría y software **no está construido**. COLBASOFT no tiene de qué partir. |
| **C.1.3** | **Ausencia total de metodología de investigación.** No hay criterios de inclusión/exclusión, bases consultadas, ecuaciones de búsqueda ni protocolo de selección de los 15 antecedentes. | Toda la estructura (no existe apartado de metodología) | La base evidencial **no es replicable ni auditable**. Riesgo académico severo. |
| **C.1.4** | **Definición operativa de «trazabilidad».** Aparece en las palabras clave, en el cuerpo y **en el título del proyecto**, sin definirse en el Cap. 7.1 —a diferencia de los otros cinco conceptos. | Cap. 7.1 (por omisión); Palabras clave | El **segundo eje del nombre del producto** carece de contenido definido. |
| **C.1.5** | **Justificación del atributo «inteligente».** La única mención de IA es tangencial: la automatización total «incorpora inteligencia artificial» (Cap. 6). | Cap. 6 | El nombre promete una capacidad **sin respaldo en la fuente de verdad**. Violación potencial de la Regla Innegociable 3. |
| **C.1.6** | **Inexistencia de requisitos.** Cero requisitos funcionales y cero no funcionales en todo el documento. La descripción más concreta es «aplicativos o sistemas de registro digital que permitan estandarizar entradas, salidas y movimientos» (Cap. 8.2). | Cap. 8.2 | No hay especificación. **No hay qué construir.** |
| **C.1.7** | **Ausencia de modelo de dominio.** No se identifican entidades, atributos ni relaciones del negocio (producto, insumo, lote, referencia, talla, color, bodega, proveedor, orden). | Ausencia total | Sin vocabulario del dominio no hay diseño posible. |
| **C.1.8** | **Ausencia de mapeo del proceso actual (AS-IS).** El documento afirma que el proceso es manual pero **nunca describe cómo funciona realmente** en una PYME textil del Eje Cafetero. | Cap. 3 (afirmación sin descripción) | No se puede automatizar un proceso que no se ha levantado. |
| **C.1.9** | **Delimitación del sujeto de estudio.** No se define qué es «PYME» (criterio legal), qué comprende «sector textil» (confección, tejeduría, comercialización) ni qué municipios integran el «Eje Cafetero» del estudio. | Transversal | Imposible dimensionar el mercado, seleccionar la muestra o validar. |
| **C.1.10** | **Reproyección del horizonte temporal.** Todo el documento apunta a 2025, horizonte ya vencido; el proyecto se denomina «2027». | Transversal | Todas las proyecciones citadas están fuera de vigencia. |

## 🟠 C.2 — ALTO
*No bloquean el inicio, pero comprometen la calidad y la defendibilidad del resultado.*

| # | Vacío | Evidencia de origen | Impacto |
|---|---|---|---|
| **C.2.1** | **Ausencia de validación empírica.** El Cap. 4 excluye explícitamente intervenir empresas reales; el proyecto de software necesita usuarios reales. | Cap. 4 (R-02) | Sin evidencia de campo, COLBASOFT no puede demostrar su beneficio. |
| **C.2.2** | **Ausencia de definición de usuarios y roles.** Se mencionan «personal encargado de los procesos logísticos» y «colaboradores», sin perfiles. | Cap. 8.2 | Sin actores no hay casos de uso ni permisos. |
| **C.2.3** | **Indicadores sin operacionalizar.** Se proponen tres indicadores sin fórmula, unidad, umbral, frecuencia ni línea base. | Cap. 8.2 | El plan de validación no es ejecutable. |
| **C.2.4** | **Ausencia de línea base.** Ninguna cifra describe el desempeño *actual* de una PYME concreta del Eje Cafetero. | Todos los datos son sectoriales o externos | Sin línea base **no se puede demostrar mejora**. |
| **C.2.5** | **OE-2 incumplido: frameworks de adopción no revisados.** Solo se nombra a Rogers (1962), sin desarrollo ni evaluación de aplicabilidad. No se consideran TAM, UTAUT ni TOE. | Caps. 5.5, 7.2 | Un objetivo específico queda sin cumplir. |
| **C.2.6** | **Ausencia de análisis de soluciones existentes.** No hay revisión de ERP/WMS del mercado ni justificación de por qué construir en lugar de adoptar. | Cap. 6 (mención genérica a ERP) | Riesgo de reinventar una solución disponible; debilita la novedad. |
| **C.2.7** | **Ausencia de restricciones técnicas del contexto.** No se documenta la infraestructura real: conectividad, dispositivos, sistemas operativos, energía. | Cap. 3 (afirmación genérica de infraestructura deficiente) | Los supuestos técnicos serían ficticios. |
| **C.2.8** | **Ausencia de modelo de negocio / viabilidad económica.** La R-08 exige bajo costo, pero no se define costo aceptable ni forma de sostenimiento. | Resumen; Caps. 3, 6 | Sin viabilidad económica no hay adopción. |
| **C.2.9** | **Ausencia de estrategia de adopción y gestión del cambio.** La resistencia es un concepto central (Cap. 7.1) pero no se propone tratamiento. | Caps. 4, 7.1, 8.2 | Se repetiría el fracaso que la monografía documenta. |
| **C.2.10** | **Ausencia de apartado de limitaciones.** No se declaran los límites de validez de las conclusiones. | Estructura | Debilidad académica exigible en sustentación. |
| **C.2.11** | **Ausencia de consideraciones legales.** No hay tratamiento de la Ley 1581 de 2012 (protección de datos), facturación electrónica DIAN ni requisitos de retención documental. | Ausencia total | Riesgo de incumplimiento normativo del producto. |
| **C.2.12** | **Ausencia de plan de pruebas y criterios de aceptación.** | Ausencia total | Sin criterios de aceptación, «terminado» no es verificable. |

## 🟡 C.3 — MEDIO
*Afectan la calidad, la mantenibilidad y la presentación profesional.*

| # | Vacío | Evidencia de origen | Impacto |
|---|---|---|---|
| **C.3.1** | Ausencia de apartado de Resultados/Discusión diferenciado de la revisión. | Estructura | No se distingue el aporte propio del ajeno. |
| **C.3.2** | Redundancia sustantiva entre Resumen, Cap. 6 y Cap. 7.2 (mismos autores, mismas tesis, casi literalmente). | Resumen; Caps. 6, 7.2 | Diluye el aporte; riesgo de observación en sustentación. |
| **C.3.3** | Inversión del orden expositivo: Desarrollo temático (Cap. 6) antecede al Marco Referencial (Cap. 7). | TDC | Debilidad de arquitectura documental. |
| **C.3.4** | Anomalía de numeración: «5.5 Objetivos Específicos» debería ser 5.1. | TDC | Error formal visible en la tabla de contenido. |
| **C.3.5** | Ausencia de glosario formal y de lista de siglas (ANDI, CEPAL, DNP, MinCIT, OIT, DANE, ODS, PYME, ERP). | Estructura | Dificulta la lectura externa. |
| **C.3.6** | Ausencia de anexos: matriz de literatura, fichas bibliográficas, instrumentos. | Estructura | No hay evidencia verificable del proceso de revisión. |
| **C.3.7** | Ausencia de lista de tablas y figuras. El documento contiene 1 elemento gráfico y ninguna tabla analítica. | Estructura | El texto carece de apoyo visual del argumento. |
| **C.3.8** | El apartado 4 fusiona «Planteamiento del problema» y «Justificación», normalmente separados. | Cap. 4 | Mezcla diagnóstico con argumentación de valor. |
| **C.3.9** | Ausencia de la marca «COLBASOFT» en toda la monografía. El nombre del producto **no aparece en la fuente de verdad**. | Ausencia total | Debe documentarse el origen y la justificación del nombre. |
| **C.3.10** | Ausencia de cronograma y presupuesto. | Estructura | Exigibles si se aprueba la extensión a desarrollo. |
| **C.3.11** | Defectos de redacción detectados (sin corregir aquí): «beneficios **documentos** en literatura» (Cap. 5.5); «calculando en comparaciones de enfoques documentados» (Cap. 5.5, sentido oscuro); «este **regazo**» (Cap. 4); «**él** sector» (Cap. 3); «**es** sectores como el textil» (Cap. 6); «una elaboración personal […] **propuesta** que» (Cap. 6); «Indicadores […] **permitirá** comprobar» (Cap. 8.2); «capacidad **competitividad**» (Cap. 3); «**Diffusión** of Innovations» (Cap. 4); «Brynjolfsson y **McAffe**» (Cap. 4). | Múltiples | Afectan la calidad formal. **No se corrigen: la monografía no se modifica** (Regla 1). |
| **C.3.12** | La expresión «Una elaboración personal» se usa 5 veces en el Cap. 6 para introducir inferencias propias, sin marcarlas metodológicamente como tales. | Cap. 6 | Difumina la frontera entre fuente y autoría. |

## 🟢 C.4 — BAJO
*Mejoras de presentación y completitud institucional.*

| # | Vacío | Impacto |
|---|---|---|
| **C.4.1** | Ausencia de resumen en inglés (*abstract*) y *keywords*. | Requisito frecuente en normativa institucional. |
| **C.4.2** | Ausencia de dedicatoria y agradecimientos. | Convención de presentación. |
| **C.4.3** | Ausencia de identificación de la línea de investigación institucional. | Trazabilidad académica. |
| **C.4.4** | Ausencia de declaración de originalidad / antiplagio. | Requisito frecuente. |
| **C.4.5** | Referencias sin DOI ni URL de recuperación. | Verificabilidad reducida. |
| **C.4.6** | Ausencia de números de página en las citas textuales de libros. | Precisión APA. |
| **C.4.7** | Uso de estilo «Párrafo de lista» en lugar de estilos de título jerárquicos, salvo un caso. | La tabla de contenido depende de estilos correctos. |

### Resumen cuantitativo de vacíos

| Prioridad | Cantidad | Naturaleza dominante |
|---|---|---|
| 🔴 Crítico | 10 | Autorización, alcance, especificación, metodología |
| 🟠 Alto | 12 | Validación, requisitos, contexto técnico, legalidad |
| 🟡 Medio | 12 | Estructura documental, redacción, redundancia |
| 🟢 Bajo | 7 | Presentación institucional |
| **Total** | **41** | |

---

# FASE D — PLAN MAESTRO

> Roadmap de evolución de la propuesta conceptual hacia un proyecto profesional. **Ninguna fase se implementa en este documento.** El plan se detiene en fronteras explícitas: nada de arquitectura, nada de tecnologías, nada de código, hasta que las fases previas lo habiliten y el Director lo apruebe.

## Principio rector del plan

> **Ninguna fase puede iniciar mientras su fase antecesora tenga entregables abiertos.** El vacío C.1.1 (autorización de cambio de naturaleza) es **precondición absoluta de todo el roadmap**: si el Director no autoriza la extensión de alcance, el plan se detiene en la Fase 1 y el proyecto continúa como trabajo conceptual.

---

### FASE 0 — Auditoría Fundacional
*(Fase actual — en ejecución)*

| Elemento | Contenido |
|---|---|
| **Objetivo** | Establecer la línea base de conocimiento: qué dice la monografía, qué omite y qué se requiere para profesionalizar la propuesta, sin alterar la fuente de verdad. |
| **Entradas** | `MONOGRAFÍA COLBASOFT.docx` (íntegra) · Reglas Innegociables 1–7 · Nombre y alcance declarado de COLBASOFT |
| **Salidas** | Este documento: auditoría (A) · inventario de 90+ conceptos (B) · 41 vacíos priorizados (C) · roadmap (D) · 44 riesgos académicos (E) · banco de 60 preguntas al Director (F) |
| **Dependencias** | Ninguna. Es la fase raíz. |
| **Riesgos** | Interpretación errónea de la intención autoral · Sobreinterpretación de conceptos tangenciales como requisitos · Omisión de contenido no textual (elementos gráficos, notas) |
| **Criterio de cierre** | El Director recibe y acusa recibo de la auditoría. |
| **Frontera** | Sin código · sin arquitectura · sin tecnologías · sin diagramas |

---

### FASE 1 — Resolución de Ambigüedades y Autorización de Alcance
*(Siguiente fase — bloqueante)*

| Elemento | Contenido |
|---|---|
| **Objetivo** | Obtener del Director las decisiones que la monografía no permite inferir, en especial la autorización formal para transformar un estudio documental en un proyecto de desarrollo de software (vacío C.1.1). |
| **Entradas** | Fase F de este documento (banco de preguntas) · Vacíos críticos C.1.1 a C.1.10 · Normativa institucional del CIAF para proyectos de grado |
| **Salidas** | Acta de decisiones firmada · Alcance autorizado y delimitado (qué entra, qué no) · Horizonte temporal reproyectado · Definición formal de PYME, sector textil y ámbito geográfico · Resolución sobre el atributo «inteligente» (C.1.5) · Resolución sobre validación de campo (R-02) |
| **Dependencias** | Fase 0 completa · Disponibilidad del Director · Posible consulta al comité curricular |
| **Riesgos** | **El Director no autoriza la extensión → el proyecto se detiene aquí** · Autorización parcial que fragmenta el alcance · Demora que comprime el cronograma · Exigencia de modificar la monografía (colisiona con la Regla 1) |
| **Criterio de cierre** | Acta de decisiones con respuesta a **todas** las preguntas de la Fase F clasificadas como bloqueantes. |
| **Frontera** | Sin código · sin arquitectura · sin tecnologías |

---

### FASE 2 — Consolidación Teórica y Saneamiento Académico

| Elemento | Contenido |
|---|---|
| **Objetivo** | Cerrar los vacíos académicos sin tocar la monografía: verificar las 9 fuentes ausentes, resolver las inconsistencias estadísticas, formalizar la metodología de revisión y **construir el modelo conceptual comprometido en el OE-3** (vacío C.1.2). |
| **Entradas** | Acta de la Fase 1 · Catálogo de riesgos académicos (Fase E) · Matriz de inventario (Fase B) · Acceso a bases de datos académicas |
| **Salidas** | Documento anexo de verificación de fuentes (las 9 ausentes: DANE, C.C. Armenia, UTP, OIT, Rogers, Brynjolfsson, Echeverry, Gob. Risaralda, ONU) · Protocolo de revisión documental replicable · Tabla de resolución de las contradicciones estadísticas (25 % vs. 40 %; atribución del 40 % de reducción de errores) · **Modelo conceptual formalizado** · Definiciones operativas de los 16 conceptos no definidos (Fase B, 🟡) |
| **Dependencias** | Fase 1 (alcance autorizado) · Disponibilidad real de las fuentes por verificar |
| **Riesgos** | **Alguna fuente resulte inexistente o inverificable → colapsa una afirmación del documento** · Las cifras verificadas contradigan las citadas → debilita la justificación · Rogers (1962) no accesible → el OE-2 queda sin sustento · El modelo conceptual construido *a posteriori* difiera de la intención autoral |
| **Criterio de cierre** | Cero afirmaciones cuantitativas sin fuente verificable en el corpus del proyecto. |
| **Frontera** | Sin código · sin arquitectura · sin tecnologías |

---

### FASE 3 — Levantamiento del Dominio (AS-IS)

| Elemento | Contenido |
|---|---|
| **Objetivo** | Documentar cómo funciona **realmente** la gestión de inventario en las PYMES textiles del Eje Cafetero, cerrando el vacío C.1.8 y estableciendo la línea base ausente (C.2.4). |
| **Entradas** | Alcance y delimitación de la Fase 1 · Modelo conceptual de la Fase 2 · Problemas P-01 a P-24 (Fase A.8) · Autorización de contacto con empresas (resuelve R-02) |
| **Salidas** | Descripción del proceso actual · Glosario del dominio textil (referencia, talla, color, lote, rollo, corte, bodega) · Inventario de artefactos actuales (formatos, cuadernos, hojas de cálculo) · Perfiles de usuario y roles reales (cierra C.2.2) · **Línea base cuantificada** de los tres indicadores del Cap. 8.2 · Restricciones técnicas reales del contexto (cierra C.2.7) |
| **Dependencias** | Fase 1 (autorización de trabajo de campo) · Fase 2 (vocabulario conceptual) · Acceso a empresas reales · Posible aval de comité de ética |
| **Riesgos** | **Las empresas no accedan a participar** (la resistencia documentada en Cap. 4 aplica también al investigador) · Confidencialidad de datos comerciales · Heterogeneidad de procesos que invalide la H9 · Muestra no representativa · Restricción R-02 no levantada → la fase se vuelve inviable |
| **Criterio de cierre** | Proceso AS-IS validado por al menos una empresa del sector. |
| **Frontera** | Sin código · sin arquitectura · sin tecnologías |

---

### FASE 4 — Ingeniería de Requisitos

| Elemento | Contenido |
|---|---|
| **Objetivo** | Traducir problemas documentados y proceso real en una especificación completa, trazable y verificable (cierra C.1.6). |
| **Entradas** | Proceso AS-IS (Fase 3) · Catálogo de problemas P-01 a P-24 · Beneficios B-01 a B-22 · Restricciones R-01 a R-19 · Recomendaciones del Cap. 8.2 |
| **Salidas** | Catálogo de requisitos funcionales · Catálogo de requisitos no funcionales (usabilidad prioritaria por R-09; costo por R-08; conectividad por R-11) · Modelo de dominio (cierra C.1.7) · **Matriz de trazabilidad requisito ↔ problema ↔ apartado de la monografía** · Criterios de aceptación (cierra C.2.12) · Requisitos legales (Ley 1581/2012 — cierra C.2.11) · Alcance explícito de lo excluido |
| **Dependencias** | Fases 1, 2 y 3 completas |
| **Riesgos** | **Aparición de requisitos sin anclaje en la monografía → violación de la Regla 3** · Sobredimensionamiento del alcance para un proyecto de nivel tecnólogo · Requisitos no trazables a un problema documentado · Conflicto entre usabilidad extrema (R-09) y riqueza funcional |
| **Criterio de cierre** | 100 % de requisitos trazables a un apartado de la monografía o a un hallazgo de la Fase 3, con aprobación del Director. |
| **Frontera** | Sin código · sin arquitectura · sin tecnologías — **la selección tecnológica se habilita en la Fase 5** |

---

### FASE 5 — Diseño de Solución
*(Habilita arquitectura y tecnologías — no antes)*

| Elemento | Contenido |
|---|---|
| **Objetivo** | Definir la arquitectura, el modelo de datos y el stack tecnológico que satisfacen los requisitos aprobados. |
| **Entradas** | Especificación de requisitos aprobada (Fase 4) · Restricciones técnicas reales (Fase 3) · Restricciones económicas R-08 |
| **Salidas** | Arquitectura de la solución · Modelo de datos · Diseño de interacción · Justificación tecnológica trazada a requisitos no funcionales · Plan de evolución parcial → total (Cap. 6) · Decisiones de diseño documentadas |
| **Dependencias** | Fase 4 aprobada |
| **Riesgos** | Elecciones tecnológicas por preferencia y no por requisito · Arquitectura desproporcionada frente a la R-08 · Diseño que ignora la R-11 (infraestructura deficiente) · Complejidad que contradice la R-13 (adopción escalonada) |
| **Criterio de cierre** | Cada decisión de diseño justificada por un requisito trazable. |

---

### FASE 6 — Construcción

| Elemento | Contenido |
|---|---|
| **Objetivo** | Materializar la solución diseñada. |
| **Entradas** | Diseño aprobado (Fase 5) · Criterios de aceptación (Fase 4) |
| **Salidas** | Producto ejecutable · Suite de pruebas · Documentación técnica · Manual de usuario orientado al perfil real (R-09) |
| **Dependencias** | Fase 5 aprobada |
| **Riesgos** | Desviación silenciosa respecto de los requisitos · Deuda técnica por presión de calendario · Alcance creciente · Pérdida de trazabilidad hacia la monografía |
| **Criterio de cierre** | Todos los criterios de aceptación satisfechos. |

---

### FASE 7 — Validación y Medición de Impacto

| Elemento | Contenido |
|---|---|
| **Objetivo** | Demostrar empíricamente que los beneficios prometidos (B-01 a B-22) se materializan, contrastando contra la línea base de la Fase 3. |
| **Entradas** | Producto (Fase 6) · Línea base (Fase 3) · Indicadores operacionalizados (Fase 2) · Empresa(s) piloto |
| **Salidas** | Resultados de la prueba piloto · Comparativo línea base vs. post-implantación en exactitud, tiempos de registro y frecuencia de errores (Cap. 8.2) · Contraste de las hipótesis H1–H10 · Evidencia de usabilidad con usuarios reales · Informe de impacto |
| **Dependencias** | Fase 6 completa · Empresa dispuesta a operar el piloto · Ventana temporal suficiente para medir |
| **Riesgos** | **Los resultados no alcancen las cifras citadas (40 %, 55 %, 25–45 %) → contradicen la propia justificación del proyecto** · Piloto demasiado corto para efectos medibles · Abandono de la empresa piloto · Resistencia del personal (P-16) que impida la adopción · Ausencia de grupo de control |
| **Criterio de cierre** | Informe de impacto con evidencia medida, favorable o desfavorable, reportada íntegramente. |

---

### FASE 8 — Integración Académica y Sustentación

| Elemento | Contenido |
|---|---|
| **Objetivo** | Consolidar el corpus completo del proyecto profesional preservando íntegramente la monografía original como documento fundacional. |
| **Entradas** | Todos los entregables de las Fases 0–7 · Normativa institucional del CIAF |
| **Salidas** | Documento final del proyecto profesional · **Monografía original preservada sin modificación** (Regla 1) · Trazabilidad completa concepto → requisito → diseño → producto → evidencia · Material de sustentación |
| **Dependencias** | Todas las fases anteriores |
| **Riesgos** | Pérdida de trazabilidad hacia los apartados originales · Los hallazgos empíricos contradigan las conclusiones del Cap. 8.1 · Incompatibilidad entre el formato de monografía y el de proyecto de desarrollo · Observaciones de jurado sobre los riesgos de la Fase E no saneados |
| **Criterio de cierre** | Aprobación institucional. |

---

### Mapa de dependencias del roadmap

```
FASE 0 (Auditoría) ──► FASE 1 (Autorización) ──┬──► FASE 2 (Consolidación teórica)
                              │                 │
                        [BLOQUEANTE]            └──► FASE 3 (Dominio AS-IS)
                                                          │
                                            FASE 2 + 3 ──► FASE 4 (Requisitos)
                                                                  │
                                                                  ▼
                                                          FASE 5 (Diseño)
                                                                  │
                                                                  ▼
                                                          FASE 6 (Construcción)
                                                                  │
                                                                  ▼
                                                          FASE 7 (Validación)
                                                                  │
                                                                  ▼
                                                          FASE 8 (Integración)
```

**Puntos de no retorno:** la Fase 1 condiciona la existencia misma del proyecto. La Fase 4 congela el alcance. La Fase 7 es el único punto donde las hipótesis H1–H10 se someten a prueba real.

---

# FASE E — RIESGOS ACADÉMICOS

> Detección, no corrección. **No se propone ninguna enmienda**: se registran los hallazgos para decisión del Director.

## E.1 Citas débiles

| # | Hallazgo | Apartado | Severidad |
|---|---|---|---|
| E.1.1 | **Rogers (1962)** sostiene el concepto «Resistencia a la Automatización» (Cap. 7.1), fundamenta el OE-2 y se invoca en 4 apartados —**y no figura en el Cap. 9**. Además se escribe «Diffusión of Innovations». | Caps. 4, 7.1, 7.2, 8.1, 9 | **Crítica** |
| E.1.2 | **Brynjolfsson y McAffe (2014)**, *The Second Machine Age*: citado para explicar el rezago sectorial; **ausente del Cap. 9**. Apellido probablemente mal transcrito. | Caps. 4, 9 | **Alta** |
| E.1.3 | **Juan Carlos Echeverry García (2018)**, *«Colombia una Economía en transición»*: sostiene dos afirmaciones del Resumen; **ausente del Cap. 9**. Formato de cita irregular. | Resumen; Cap. 9 | **Alta** |
| E.1.4 | **DANE (2023)**: sostiene la cifra del PIB regional en dos apartados; **ausente del Cap. 9**. | Caps. 3, 4, 9 | **Crítica** |
| E.1.5 | **Cámara de Comercio de Armenia (2022 y 2023)**: sostiene las pérdidas económicas y el +30 % de pérdidas por errores; **ausente del Cap. 9**. Nótese que el Cap. 9 sí incluye a la **Cámara de Comercio de Pereira**: son entidades distintas. | Caps. 3, 4, 6, 9 | **Crítica** |
| E.1.6 | **Universidad Tecnológica de Pereira (2022)**: sostiene el dato del 60 %; **ausente del Cap. 9**. | Caps. 4, 9 | **Crítica** |
| E.1.7 | **OIT (2021)**: citada dos veces, incluida una cifra del 40 %; **ausente del Cap. 9**. | Caps. 4, 6, 9 | **Crítica** |
| E.1.8 | **Gobernación de Risaralda (2024)**: sostiene la proyección 25–45 % en la conclusión; **ausente del Cap. 9**. | Caps. 8.1, 9 | **Crítica** |
| E.1.9 | **ONU / ODS**: invocada tres veces (ODS 8, ODS 9, «ONU 2015»); **ausente del Cap. 9**. | Caps. 3, 4, 6, 9 | **Alta** |
| E.1.10 | **Bowersox y Closs (2007)** aparece en el Cap. 9 pero se cita **una sola vez** en todo el cuerpo. | Caps. 7.2, 9 | Media |
| E.1.11 | Ninguna cita textual de libro incluye número de página, incumpliendo APA para citas directas. | Transversal | Media |
| E.1.12 | Cinco de las quince referencias tienen más de diez años (Ballou 2004; Bowersox y Closs 2007; Slack et al. 2010; Heizer y Render 2014), en un tema —transformación digital— de obsolescencia rápida. | Cap. 9 | Media |
| E.1.13 | La expresión **«Una elaboración personal»** se emplea cinco veces en el Cap. 6 para introducir inferencias del autor apoyadas en terceros, sin marco metodológico que respalde ese procedimiento. | Cap. 6 | Alta |

## E.2 Estadísticas sin soporte

| # | Cifra | Apartado | Problema |
|---|---|---|---|
| E.2.1 | **«5-7% del PIB manufacturero»** | Cap. 3 | Atribuida a DANE (2023), fuente ausente del Cap. 9. En el Cap. 4 la misma cifra se escribe «5-7 del PIB fabricante regional», **sin símbolo de porcentaje**. |
| E.2.2 | **«más de 50.000 personas»** empleadas | Cap. 4 | Sin cita directa adjunta a la cifra. |
| E.2.3 | **«hasta un 30% menores»** en productividad | Cap. 3 | Atribuida conjuntamente a CEPAL (2022) y ANDI (2023) sin precisar cuál la aporta. |
| E.2.4 | **«miles de millones de pesos anuales»** en pérdidas | Cap. 3 | Magnitud imprecisa (rango de tres órdenes de magnitud). Fuente: C.C. Armenia 2022, ausente del Cap. 9. Se escribe «Según informes de la Cámara de Comercio de Armenia,2022» (sin espacio). |
| E.2.5 | **«hasta un 40%»** de eficiencia operativa, «según CEPAL» | Cap. 3 | **Contradice directamente** el «hasta un 25 % en eficiencia» atribuido a **la misma CEPAL (2022)** en el Cap. 7.2. |
| E.2.6 | **«30% más de pérdidas por errores en inventarios en el último año»** | Cap. 4 | Fuente ausente. «El último año» no está anclado a una fecha concreta. |
| E.2.7 | **«el 60% de las PYMES locales carecen de sistemas digitales»** | Cap. 4 | Fuente (UTP 2022) ausente del Cap. 9. |
| E.2.8 | **«reducción de errores en un 40% según estudios de la OIT (2021)»** | Cap. 6 | Fuente ausente **y** la misma cifra del 40 % se atribuye a **Hernández y Salazar (2021)** en el Cap. 7.2. **Conflicto de atribución.** |
| E.2.9 | **«mejoras del 25-45 % en productividad»** | Cap. 8.1 | Aparece por primera vez en las conclusiones, sin haber sido presentada en el desarrollo. Fuente (Gob. Risaralda 2024) ausente del Cap. 9. Un rango de 20 puntos porcentuales carece de utilidad predictiva. |
| E.2.10 | **«el 72% de las PYMES colombianas carecen de herramientas tecnológicas»** | Cap. 7.2 | Fuente respaldada (ANDI 2023). **Verificar contra el informe original**: es la cifra ancla del proyecto. |
| E.2.11 | **«el 67% reportaba errores por registros manuales»** | Cap. 7.2 | Fuente respaldada (Martínez y Gómez 2019), estudio en Antioquia. **Su transferibilidad al Eje Cafetero es un supuesto (H5), no un dato.** |
| E.2.12 | **«incrementa hasta en un 30% la productividad»** | Cap. 7.2 | Fuente respaldada (López et al. 2020), estudio en México. **Mismo problema de transferibilidad.** |
| E.2.13 | **«reduce los errores en un 40% y mejora la trazabilidad en un 55%»** | Cap. 7.2 | Fuente respaldada (Hernández y Salazar 2021). **Verificar en el original**: es la cifra más citada del proyecto y la que sostiene el eje de trazabilidad. |
| E.2.14 | Existen **tres cifras distintas de mejora de productividad/eficiencia** —25 %, 30 %, 40 % y un rango 25–45 %— sin reconciliación ni explicación de la divergencia. | Caps. 3, 7.2, 8.1 | Debilita toda la promesa cuantitativa. |
| E.2.15 | **«El marco teórico […] integrando aportes de 15 antecedentes»** | Cap. 7.2 | El Cap. 9 contiene efectivamente 15 entradas, pero el cuerpo cita **24 fuentes distintas**. La declaración de «15 antecedentes» no coincide con el corpus realmente utilizado. |

## E.3 Posibles inconsistencias metodológicas

| # | Inconsistencia | Apartados | Naturaleza |
|---|---|---|---|
| E.3.1 | **El Objetivo General aparece con dos redacciones.** El Cap. 3 lo enuncia incluyendo «hacia el año 2025»; el Cap. 5 lo enuncia sin ese fragmento. | Caps. 3, 5 | **Alta** — el objetivo rector no es idéntico consigo mismo. |
| E.3.2 | **OE-3 no cumplido.** Compromete «proponer un modelo conceptual integrado» y **ningún apartado presenta el modelo**. | Caps. 5.5, 8.1 | **Crítica** — objetivo declarado sin entregable. |
| E.3.3 | **OE-2 cumplido solo nominalmente.** Compromete «revisar modelos teóricos […] como frameworks de adopción tecnológica» y solo nombra a Rogers sin desarrollarlo ni evaluar su aplicabilidad. | Caps. 5.5, 7.2 | **Alta** |
| E.3.4 | **Ausencia de capítulo de metodología** pese a autodefinirse como «revisión documental» en tres apartados. Sin criterios de inclusión/exclusión, bases consultadas ni ecuaciones de búsqueda. | Caps. 4, 5, 8.1; estructura | **Crítica** |
| E.3.5 | **El Cap. 8.1 afirma hallazgos empíricos que el diseño no permite obtener.** «Los hallazgos del análisis del problema demostraron que estas situaciones están presentes en la región» — pero el Cap. 4 excluye expresamente intervenir empresas reales. Una revisión documental no «demuestra presencia» en campo. | Caps. 4, 8.1 | **Crítica** — colisión entre diseño declarado y conclusión afirmada. |
| E.3.6 | **El Cap. 8.1 afirma la existencia de una propuesta inexistente.** «La propuesta presentada en esta monografía demuestra que sí es posible aplicar un modelo» — no hay propuesta presentada en el texto. | Cap. 8.1 | **Crítica** |
| E.3.7 | **Inversión del orden expositivo:** el Desarrollo temático (Cap. 6) usa el aparato teórico antes de que el Marco Teórico (Cap. 7.2) lo establezca. | TDC; Caps. 6, 7 | Media |
| E.3.8 | **Redundancia sustantiva** entre Resumen, Cap. 6 y Cap. 7.2: los mismos cuatro autores y las mismas tesis se repiten en formulaciones casi idénticas. | Resumen; Caps. 6, 7.2 | Media |
| E.3.9 | **Conflicto de ODS:** el Cap. 3 invoca el ODS 8 y el Cap. 4 el ODS 9 para justificar el mismo estudio; el Cap. 6 cita «ONU, 2015» sin especificar objetivo. | Caps. 3, 4, 6 | Media |
| E.3.10 | **Ausencia de variables e hipótesis declaradas.** Aceptable en una revisión documental, pero incompatible con las afirmaciones causales que el texto sostiene (H1, H2). | Estructura | Alta |
| E.3.11 | **Salto conclusivo:** de «la literatura reporta beneficios en otros contextos» a «automatizar es viable y necesario para el Eje Cafetero» (Cap. 8.1), sin evidencia local que cierre la inferencia. | Cap. 8.1 | **Alta** — es el salto lógico central del documento. |
| E.3.12 | **Anomalía de numeración:** «5.5 Objetivos Específicos» bajo el apartado 5. | TDC | Baja |
| E.3.13 | **Ausencia de apartado de limitaciones**, obligatorio cuando las conclusiones se apoyan en fuentes de contextos ajenos. | Estructura | Alta |
| E.3.14 | **Horizonte temporal vencido:** todo el documento proyecta «hacia 2025» y está fechado el 27 de noviembre de 2025. | Transversal | **Alta** |
| E.3.15 | **Fusión de planteamiento y justificación** en un solo apartado (Cap. 4), mezclando diagnóstico del problema con argumentación de valor. | Cap. 4 | Baja |
| E.3.16 | **El marcador «Una elaboración personal»** introduce inferencias propias sin protocolo declarado que las distinga de los hallazgos de las fuentes. | Cap. 6 | Alta |

## E.4 Referencias que deben verificarse

> **Prioridad de verificación.** Ninguna de estas afirmaciones debe reutilizarse en COLBASOFT hasta ser confirmada contra la fuente original.

### Prioridad 1 — Fuentes ausentes que sostienen cifras (bloquean su reutilización)

| Fuente | Qué sostiene | Acción de verificación |
|---|---|---|
| DANE (2023) | 5–7 % del PIB manufacturero regional | Localizar la publicación exacta y confirmar la cifra y su alcance geográfico |
| Cámara de Comercio de Armenia (2022) | Pérdidas de «miles de millones» | Localizar el informe y obtener la cifra precisa |
| Cámara de Comercio de Armenia (2023) | +30 % de pérdidas por errores | Localizar el informe y confirmar el período de referencia |
| Universidad Tecnológica de Pereira (2022) | 60 % de PYMES sin sistemas digitales | Identificar el estudio, su muestra y su alcance |
| OIT (2021) | Reducción de errores del 40 % | Localizar la publicación y **resolver el conflicto de atribución con Hernández y Salazar (2021)** |
| Gobernación de Risaralda (2024) | Proyección 25–45 % de productividad | Localizar la fuente y confirmar la metodología de proyección |

### Prioridad 2 — Fuentes teóricas ausentes (bloquean objetivos específicos)

| Fuente | Qué sostiene | Acción de verificación |
|---|---|---|
| Rogers, E. (1962) — *Diffusion of Innovations* | Concepto formal de «Resistencia a la Automatización» (Cap. 7.1) y todo el OE-2 | Obtener la edición, confirmar autoría y año, corregir la transcripción del título |
| Brynjolfsson, E., y McAfee, A. (2014) — *The Second Machine Age* | Rezago de sectores tradicionales | Verificar la grafía del apellido y localizar el pasaje citado |
| Echeverry García, J. C. (2018) — *Colombia, una economía en transición* | Resistencia y falta de capital (Resumen) | Confirmar la existencia, el tipo de publicación y el año |
| ONU — ODS 8 / ODS 9 / «ONU 2015» | Alineación con desarrollo sostenible | **Definir cuál ODS aplica** y citar la fuente oficial |

### Prioridad 3 — Fuentes presentes cuyas cifras deben confirmarse en el original

| Fuente | Cifra | Riesgo |
|---|---|---|
| ANDI (2023) | 72 % sin herramientas tecnológicas | **Es la cifra ancla del proyecto.** Confirmar muestra y definición de «herramienta tecnológica». |
| Hernández y Salazar (2021) | −40 % errores / +55 % trazabilidad | **Cifras más reutilizadas del documento.** Confirmar población, método y contexto. |
| CEPAL (2022) | 25 % de eficiencia | **Resolver la contradicción con el 40 % del Cap. 3.** |
| López et al. (2020) | +30 % de productividad | Estudio mexicano: evaluar la transferibilidad (H5). |
| Martínez y Gómez (2019) | 67 % con errores | Estudio de Antioquia: evaluar la transferibilidad (H5). |
| Barreto y Ruiz (2022) | Pérdidas en textiles de Medellín | Evidencia sectorial más próxima: extraer sus datos específicos. |
| Cámara de Comercio de Pereira (2022) | Problemas de control de inventario | **Evidencia local más directa:** extraer todo dato aprovechable. |

### Prioridad 4 — Verificación formal de las 15 referencias del Cap. 9

Todas las entradas carecen de DOI y de URL de recuperación. Los cinco artículos de revista (Barreto y Ruiz; Hernández y Salazar; López et al.; Martínez y Gómez; Silva) requieren confirmación de existencia, volumen, número y paginación en bases indexadas.

---

# FASE F — PREGUNTAS PARA EL DIRECTOR DEL PROYECTO

> Banco completo de preguntas requeridas antes de iniciar el desarrollo.
> **🔴 = Bloqueante** (sin respuesta, el proyecto no puede avanzar) · **🟠 = Condicionante** (determina el rumbo) · **🟡 = Aclaratoria**

## F.1 Categoría: INVESTIGACIÓN

| # | Pregunta | Origen | Prioridad |
|---|---|---|---|
| I-01 | El Cap. 5 declara como método una **revisión documental**. ¿COLBASOFT mantiene ese diseño, migra a investigación aplicada / desarrollo tecnológico, o adopta un diseño mixto? | Caps. 4, 5 | 🔴 |
| I-02 | La monografía **no incluye capítulo de metodología** (E.3.4). ¿Debe construirse retroactivamente como documento anexo, o el proyecto profesional parte de una metodología nueva? | Estructura | 🔴 |
| I-03 | Nueve fuentes citadas **no aparecen en el Cap. 9** (E.1.1–E.1.9). ¿Se verifican y se incorporan a la bibliografía del nuevo documento, o se retiran las afirmaciones que sostienen? | Caps. 3, 4, 6, 8.1, 9 | 🔴 |
| I-04 | CEPAL (2022) aparece con **25 % (Cap. 7.2) y 40 % (Cap. 3)** de mejora de eficiencia. ¿Cuál es la cifra válida? | Caps. 3, 7.2 | 🔴 |
| I-05 | La reducción de errores del **40 % se atribuye a la OIT (Cap. 6) y a Hernández y Salazar (Cap. 7.2)**. ¿Cuál es la atribución correcta? | Caps. 6, 7.2 | 🔴 |
| I-06 | El **OE-3 compromete un modelo conceptual que el documento no presenta** (E.3.2). ¿Se construye ese modelo como primer entregable de COLBASOFT o se reformula el objetivo? | Caps. 5.5, 8.1 | 🔴 |
| I-07 | El **OE-2 solo nombra a Rogers (1962)** sin desarrollarlo (E.3.3). ¿Se profundiza en Rogers, se incorporan otros frameworks de adopción, o se ajusta el objetivo? | Caps. 5.5, 7.2 | 🟠 |
| I-08 | El Cap. 8.1 afirma que «los hallazgos demostraron que estas situaciones están presentes en la región», pero el Cap. 4 excluye intervenir empresas (E.3.5). ¿Cómo se resuelve esta colisión? | Caps. 4, 8.1 | 🔴 |
| I-09 | El horizonte «hacia 2025» está vencido (E.3.14). ¿Cuál es el nuevo horizonte y cómo se justifica la reproyección de las cifras citadas? | Transversal | 🔴 |
| I-10 | El Cap. 7.2 declara **15 antecedentes**, pero el cuerpo cita **24 fuentes** (E.2.15). ¿Se amplía la declaración o se acota el corpus? | Caps. 7.2, 9 | 🟠 |
| I-11 | La evidencia proviene de Antioquia, México, Medellín y LatAm (H5). ¿Se acepta su transferibilidad al Eje Cafetero o se exige evidencia local primaria? | Cap. 7.2 | 🟠 |
| I-12 | ¿Se invoca el **ODS 8 (Cap. 3) o el ODS 9 (Cap. 4)**? (E.3.9) | Caps. 3, 4 | 🟡 |
| I-13 | El Cap. 6 introduce cinco «elaboraciones personales» sin marco metodológico (E.1.13). ¿Cómo deben tratarse estas inferencias en el proyecto profesional? | Cap. 6 | 🟠 |
| I-14 | ¿Se requiere **aval de comité de ética** para el trabajo de campo de la Fase 3? | Fase D | 🟠 |
| I-15 | ¿Debe incluirse un apartado de **limitaciones** en el nuevo documento? (E.3.13) | Estructura | 🟡 |
| I-16 | Cinco referencias superan los diez años en un tema de obsolescencia rápida (E.1.12). ¿Se exige actualización bibliográfica? | Cap. 9 | 🟡 |

## F.2 Categoría: SOFTWARE

| # | Pregunta | Origen | Prioridad |
|---|---|---|---|
| S-01 | El Cap. 8.1 declara: «Más que desarrollar un sistema completo, buscamos plantear un modelo flexible». **¿Se autoriza formalmente construir el sistema?** | Cap. 8.1 | 🔴 |
| S-02 | El Cap. 4 excluye «proponer soluciones prácticas de implementación». **¿Se levanta esa restricción?** | Cap. 4 | 🔴 |
| S-03 | El nombre COLBASOFT declara una **«Plataforma inteligente»**, pero la IA se menciona una sola vez y de forma tangencial (Cap. 6). ¿Se autoriza el atributo «inteligente» y con qué anclaje? ¿O se ajusta el nombre? | Cap. 6 | 🔴 |
| S-04 | **«Trazabilidad» está en el título del proyecto y no tiene definición operativa** en el Cap. 7.1, a diferencia de los otros cinco conceptos. ¿Quién define su alcance: lote, referencia, movimiento, cadena completa? | Cap. 7.1 | 🔴 |
| S-05 | La descripción funcional más concreta del documento es «aplicativos o sistemas de registro digital que permitan estandarizar entradas, salidas y movimientos de inventario» (Cap. 8.2). **¿Es este el alcance funcional autorizado, o se amplía?** | Cap. 8.2 | 🔴 |
| S-06 | El Cap. 6 menciona **sensores** y **ERP** una sola vez cada uno. ¿Entran en el alcance? La Regla Innegociable 3 impide convertirlos en funcionalidad sin autorización. | Cap. 6 | 🟠 |
| S-07 | El Cap. 6 menciona **detección de fraudes**. ¿Se descarta explícitamente o se incorpora? | Cap. 6 | 🟠 |
| S-08 | El Cap. 6 menciona **coordinación con proveedores**. ¿Implica un módulo de compras? | Cap. 6 | 🟠 |
| S-09 | La R-08 (capacidad financiera limitada) exige bajo costo. **¿Cuál es el costo máximo aceptable** para la PYME objetivo? | Resumen; Caps. 3, 6 | 🟠 |
| S-10 | La R-11 señala infraestructura tecnológica deficiente. **¿Puede asumirse conectividad permanente**, o el sistema debe operar sin conexión? | Cap. 3 | 🟠 |
| S-11 | El Cap. 6 distingue automatización **parcial y total**. ¿En qué nivel se posiciona COLBASOFT? | Cap. 6 | 🟠 |
| S-12 | ¿Debe contemplarse cumplimiento de la **Ley 1581 de 2012** (protección de datos) y de requisitos DIAN? (C.2.11) | Ausente | 🟠 |
| S-13 | El Cap. 6 menciona **«monitoreo en tiempo real»** sin definir el umbral. ¿Qué latencia se considera aceptable? | Caps. 6, 7.1 | 🟡 |
| S-14 | ¿Se autoriza evaluar **soluciones existentes en el mercado** antes de construir, y documentar la justificación de construir? (C.2.6) | Cap. 6 | 🟠 |
| S-15 | ¿Cuál es el **entregable mínimo aprobatorio**: prototipo funcional, MVP en producción o sistema completo? | Fase D | 🔴 |
| S-16 | La marca «COLBASOFT» **no aparece en la monografía**. ¿Debe documentarse el origen y la justificación del nombre? | Ausencia total | 🟡 |

## F.3 Categoría: VALIDACIÓN

| # | Pregunta | Origen | Prioridad |
|---|---|---|---|
| V-01 | El Cap. 4 declara «sin intervenir empresas reales». **¿Se autoriza el contacto con empresas** para el levantamiento AS-IS y el piloto? | Cap. 4 | 🔴 |
| V-02 | El Cap. 8.2 propone tres indicadores —exactitud del inventario, tiempos de registro, frecuencia de errores— **sin fórmula, unidad ni umbral**. ¿Quién los operacionaliza y con qué criterio de éxito? | Cap. 8.2 | 🔴 |
| V-03 | **No existe línea base** de ninguna PYME concreta (C.2.4). Sin ella no puede demostrarse mejora. ¿Se autoriza levantarla? | Ausencia total | 🔴 |
| V-04 | ¿Cuántas empresas piloto se consideran suficientes y **quién gestiona el acceso**? | Fase D | 🟠 |
| V-05 | ¿Cuánto debe durar el piloto para que los indicadores del Cap. 8.2 arrojen resultados medibles? | Cap. 8.2 | 🟠 |
| V-06 | **¿Qué ocurre si el piloto no alcanza las cifras citadas** (−40 % errores, +55 % trazabilidad, +25–45 % productividad)? ¿Es causal de no aprobación o un hallazgo válido? | Caps. 7.2, 8.1 | 🔴 |
| V-07 | La R-09 (baja alfabetización digital) impone usabilidad extrema. **¿Qué método de evaluación de usabilidad** se exige? | Cap. 8.2 | 🟠 |
| V-08 | ¿Se requiere **grupo de control** o basta la comparación pre/post en la misma empresa? | Fase D | 🟠 |
| V-09 | El Cap. 8.2 recomienda capacitación práctica. **¿Forma parte del entregable evaluable?** | Cap. 8.2 | 🟠 |
| V-10 | ¿Cómo se gestiona la **confidencialidad de los datos comerciales** de las empresas participantes? | Fase D | 🟠 |
| V-11 | El Cap. 4 documenta resistencia cultural (P-16). **¿Qué se hace si el personal de la empresa piloto rechaza la herramienta?** | Caps. 4, 7.1 | 🟡 |
| V-12 | ¿Deben contrastarse formalmente las **hipótesis implícitas H1–H10** (A.5), o se mantienen como supuestos? | Fase A.5 | 🟠 |

## F.4 Categoría: ALCANCE

| # | Pregunta | Origen | Prioridad |
|---|---|---|---|
| A-01 | **¿Se autoriza formalmente que un trabajo de revisión documental evolucione a un proyecto de desarrollo de software?** Esta es la pregunta raíz: de su respuesta depende la existencia del roadmap completo. | Caps. 4, 8.1 | 🔴 |
| A-02 | La Regla Innegociable 1 establece que la monografía **no se modifica**. ¿Se confirma que COLBASOFT se documenta en un corpus nuevo que la preserva como anexo fundacional? | Regla 1 | 🔴 |
| A-03 | **¿Qué es una «PYME»** para este proyecto? ¿Qué criterio se adopta (empleados, activos, ingresos, Decreto 957 de 2019)? | Transversal | 🔴 |
| A-04 | **¿Qué comprende «sector textil»?** ¿Confección, tejeduría, comercialización, insumos, o un subconjunto? | Transversal | 🔴 |
| A-05 | **¿Qué municipios integran el «Eje Cafetero»** para este estudio? El texto menciona Pereira, Risaralda, Quindío y Armenia sin delimitar. | Transversal | 🔴 |
| A-06 | La Regla Innegociable 3 prohíbe inventar funcionalidades. **¿Todo requisito debe trazar a un apartado de la monografía**, o se admite incorporar hallazgos nuevos del levantamiento de campo? | Regla 3 | 🔴 |
| A-07 | ¿Cuál es el **plazo del proyecto** y qué fases del roadmap (D) caben en él? | Fase D | 🔴 |
| A-08 | Los problemas P-19 a P-22 (barreras regulatorias, falta de infraestructura, estacionalidad, baja resiliencia) **no son resolubles por software**. ¿Se confirma su exclusión del alcance funcional? | Caps. 3, 4 | 🟠 |
| A-09 | ¿El proyecto debe abarcar **todo el proceso logístico** (Cap. 6: flujo de materiales, trazabilidad, coordinación, inventarios) o solo la gestión de inventarios? | Caps. 5, 6 | 🔴 |
| A-10 | ¿El alcance incluye **una sola empresa como caso**, un modelo generalizable, o ambos? Depende de la validez de H9 (homogeneidad de procesos). | Caps. 5, 8.1 | 🟠 |
| A-11 | La R-13 (Cap. 8.2) recomienda adopción escalonada. **¿El entregable es la primera etapa de esa escalera** o el sistema completo? | Cap. 8.2 | 🟠 |
| A-12 | ¿Se mantiene el **equipo de tres autores** y cómo se distribuyen los roles en un proyecto de desarrollo? | Portada | 🟡 |
| A-13 | ¿El asesor continúa siendo el mismo, y se requiere un **asesor técnico adicional** para las fases de ingeniería? | Portada | 🟡 |
| A-14 | ¿Qué **normativa institucional del CIAF** aplica al formato de un proyecto de desarrollo, frente al de una monografía? | R-15, R-16 | 🟠 |
| A-15 | ¿Existe **propiedad intelectual** comprometida —de la institución, del equipo o de las empresas participantes— sobre el producto resultante? | Ausente | 🟠 |
| A-16 | La Regla Innegociable 6 prohíbe cambiar objetivos sin justificar. **¿Cuál es el procedimiento formal** para registrar y aprobar los cambios de objetivo que este documento identifica? | Regla 6 | 🔴 |

### Resumen del banco de preguntas

| Categoría | 🔴 Bloqueantes | 🟠 Condicionantes | 🟡 Aclaratorias | Total |
|---|---|---|---|---|
| Investigación | 6 | 6 | 4 | 16 |
| Software | 6 | 8 | 2 | 16 |
| Validación | 4 | 7 | 1 | 12 |
| Alcance | 8 | 6 | 2 | 16 |
| **Total** | **24** | **27** | **9** | **60** |

---

# CIERRE DE LA FASE 0

## Estado de cumplimiento de las Reglas Innegociables

| # | Regla | Estado |
|---|---|---|
| 1 | La monografía no se modifica | ✅ El archivo original permanece intacto. Esta auditoría es un documento externo. |
| 2 | No eliminar conceptos esenciales | ✅ Más de 90 conceptos inventariados en la Fase B; ninguno descartado. |
| 3 | No inventar funcionalidades | ✅ Cero funcionalidades propuestas. Los conceptos tangenciales (sensores, ERP, IA, detección de fraudes) se marcan como **pendientes de decisión**, no como requisitos. |
| 4 | No escribir código | ✅ Cero líneas de código. |
| 5 | No crear arquitectura | ✅ Ninguna decisión arquitectónica. La Fase 5 del roadmap la habilita, no antes. |
| 6 | No cambiar objetivos sin justificar | ✅ Los objetivos se transcriben literalmente. Las divergencias se elevan como preguntas al Director (I-01, I-06, I-07, A-01, A-16), no como cambios ejecutados. |
| 7 | Todo hallazgo cita el capítulo de origen | ✅ Cada entrada de las Fases A–F referencia su apartado en la monografía o declara explícitamente su ausencia. |

## Veredicto de la auditoría

La monografía constituye una **base conceptual válida y suficiente para fundamentar el dominio del problema** de COLBASOFT: identifica 24 problemas reales, 22 beneficios esperados, 5 conceptos formalmente definidos y 15 referencias que sostienen el argumento central.

Sin embargo, **no constituye una especificación de producto** y, más importante, **excluye explícitamente la construcción de software** en dos apartados distintos (Caps. 4 y 8.1). La existencia misma de COLBASOFT como plataforma depende de una decisión que solo el Director puede tomar.

Los tres hallazgos que gobiernan todo lo demás son:

1. **El modelo conceptual comprometido en el OE-3 no existe en el documento.** El puente entre la teoría y el software no está construido (C.1.2, E.3.2, E.3.6).
2. **Nueve de las veinticuatro fuentes citadas carecen de respaldo bibliográfico**, incluidas las que sostienen cuatro de las seis cifras cuantificadas del proyecto (E.1, E.2).
3. **La monografía excluye la implementación; COLBASOFT es implementación.** Esta contradicción es previa a cualquier trabajo de ingeniería (C.1.1, A-01).

**Recomendación de la auditoría:** no iniciar la Fase 2 ni ninguna posterior hasta cerrar la **Fase 1 (Resolución de Ambigüedades y Autorización de Alcance)** con acta firmada que responda, como mínimo, a las 24 preguntas bloqueantes de la Fase F.

---

*Documento de auditoría — Fase 0 · COLBASOFT · 1 de septiembre de 2026*
*La monografía original permanece sin modificaciones.*
