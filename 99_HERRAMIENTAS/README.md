# 99_HERRAMIENTAS — Generadores y verificadores de la documentación COLBASOFT

Estos scripts **no son parte del producto COLBASOFT**. Son las herramientas con las que se generaron y verificaron el SPEC v1.1, el SRS (Fase 3) y el Modelo de Dominio (Fase 4). Permiten regenerar esos documentos de forma consistente cuando cambie algo, por ejemplo cuando el Director resuelva las decisiones DEC-01…DEC-09 o los hallazgos HD-nn.

Requisito: Python 3.10 o superior, sin librerías externas. En Windows, ejecutar con `PYTHONIOENCODING=utf8` para que la consola muestre bien las tildes.

## Estructura

| Carpeta / archivo | Contenido |
|---|---|
| `spec/build_spec_v11.py` | Genera `01_SPEC_FASE_2/COLBASOFT_SPEC_v1.1.md` aplicando a la v1.0 (que no se toca) los reemplazos del cierre del CP-04; cada reemplazo debe aparecer una sola vez o el script falla |
| `srs/parse_spec.py` | Lee `01_SPEC_FASE_2/COLBASOFT_SPEC_v1.1.md` y extrae a `spec.json` las 103 HU, 162 RF, 47 RNF, reglas, 24 KPI, 14 PN, 48 CD y 42 RG |
| `srs/spec.json` | Extracción estructurada del SPEC (salida de `parse_spec.py`) |
| `srs/ids.py` | Asignación de IDs permanentes del SRS (`HU-<DOM>-nnn`, `RF-<DOM>-nnn`, `RNF-<CAT>-nnn`, `RN-<DOM>-nnn`) y equivalencias con los IDs del SPEC |
| `srs/trace.py` | Mapeos derivados en el SRS: HU↔RF, RF↔RN, KPI↔RF, RF↔concepto, objetivo por módulo, horizonte H1/H2, dependencias entre historias |
| `srs/g01.txt`…`g04.txt` | Escenarios Gherkin de las 103 historias (un escenario por criterio de aceptación del SPEC) |
| `srs/cap*.md`, `uc_*.md`, `annex_c.md` | Capítulos del SRS redactados a mano, con marcadores `@HU030`, `@RF052`, `@RN009`… que el generador convierte a IDs permanentes |
| `srs/build_srs.py` | Ensambla `SRS_COLBASOFT_v1.1.md` y genera los capítulos 5–9 y los anexos A y B |
| `dominio/export_ids.py` | Genera `srs_ids.json` (catálogo de IDs del SRS) a partir de `../srs` |
| `dominio/dm_data.py` | Subdominios, entidades, objetos de valor, agregados, invariantes, ciclos de vida, máquinas de estado y hallazgos del dominio |
| `dominio/ev_data.py` | Los 165 eventos y las líneas temporales de los 14 procesos |
| `dominio/gl_data.py` | Los 205 términos del glosario (fuente única también del lenguaje ubicuo). Los agregados después de la v1.0 llevan `v11=True` y continúan la numeración GL-nnn sin renumerar los anteriores |
| `dominio/build_f4.py` | Genera `DOMAIN_MODEL.md`, `EVENT_CATALOG.md` y `GLOSSARY.md` |
| `dominio/xref.py` | Verificador: referencias rotas en SRS v1.1, dominio, CLAUDE.md y `04_CP04_AUDITORIA/`; IDs del SPEC sin emparejar; tablas descuadradas |

## Uso

Cada generador acepta una carpeta de salida opcional. **Sin ese argumento sobrescribe el documento oficial del proyecto.** Conviene generar primero en una carpeta temporal y comparar.

```bash
cd 99_HERRAMIENTAS/spec
python build_spec_v11.py /tmp/prueba   # o sin argumento: 01_SPEC_FASE_2/COLBASOFT_SPEC_v1.1.md
```

```bash
cd 99_HERRAMIENTAS/srs
python parse_spec.py               # solo si cambió el SPEC
python build_srs.py /tmp/prueba    # o sin argumento: 02_SRS_FASE_3/
```

```bash
cd 99_HERRAMIENTAS/dominio
python export_ids.py               # solo si cambiaron los IDs del SRS
python build_f4.py /tmp/prueba     # o sin argumento: 03_DOMINIO_FASE_4/
python xref.py                     # verificar siempre al final
```

`xref.py` imprime una línea por cada problema encontrado; si solo imprime la línea final, no hay errores.

## Estado verificado

El 28 de septiembre de 2026 la cadena completa (extracción del SPEC → SRS → modelo de dominio) regeneró **byte a byte** los documentos v1.0, y `xref.py` terminó sin errores.

El 29 de septiembre de 2026, tras el cierre del CP-04, la cadena SPEC v1.1 → SRS v1.1 → modelo de dominio v1.1 se generó dos veces y dio archivos idénticos entre sí y con los oficiales; `xref.py` terminó sin errores (`04_CP04_AUDITORIA/04_CP04_CIERRE.md`, §15).

## Reglas al modificar

- **Los IDs nunca se renumeran.** Para agregar un elemento se agrega al final de su dominio; uno que se retire se marca «Retirado» y se conserva.
- **Editar los datos, no los documentos generados.** Si se edita a mano un `.md` generado, el siguiente regenerado borra el cambio. Para cambios puntuales sin regenerar se puede editar el `.md` directamente, pero entonces los datos y el documento dejan de coincidir: hay que llevar el mismo cambio a los datos.
- **No modificar la monografía, la Auditoría ni las versiones anteriores (SPEC v1.0, SRS v1.0).** Los scripts solo las leen. Un cambio al SPEC se hace agregando un reemplazo en `spec/build_spec_v11.py` (o en el generador de una versión posterior), nunca editando el `.md`.
- Después de cualquier cambio, ejecutar `xref.py`.
