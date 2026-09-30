# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

This is **not a code repository** in the usual sense (no build system, no tests, no application source). Git is used only for version history and backup on GitHub. It is a document workspace for COLBASOFT, an academic degree project (Tecnólogo en Desarrollo de Software, CIAF, Pereira — per the monografía's cover page; the user's most recent presentation slide instead said «Ingeniería en Desarrollo de Software», unconfirmed). There are no build/lint/test commands. Working here means reading and writing documents, **in Spanish**.

COLBASOFT = *Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero*.

```
00_MONOGRAFIA_ORIGINAL/MONOGRAFÍA  COLBASOFT.docx         Source of truth, immutable (note the double space in the filename)
00_AUDITORIA_FASE_0/AUDITORIA_FUNDACIONAL_COLBASOFT.md    Audit (~980 lines)
01_SPEC_FASE_2/COLBASOFT_SPEC_v1.2.md                     Functional spec, CURRENT (~3650 lines); generated from v1.1 by 99_HERRAMIENTAS/spec/build_spec_v12.py
01_SPEC_FASE_2/COLBASOFT_SPEC_v1.1.md                     Previous version (v1.1 = v1.0 + CP-04 closure), kept untouched (historical)
01_SPEC_FASE_2/COLBASOFT_SPEC_v1.0.md                     Oldest version, kept untouched (historical)
02_SRS_FASE_3/SRS_COLBASOFT_v1.2.md                       SRS, CURRENT, ISO/IEC/IEEE 29148 adapted (~7520 lines, ~560 KB)
02_SRS_FASE_3/SRS_COLBASOFT_v1.1.md                       Previous version, kept untouched (historical)
02_SRS_FASE_3/SRS_COLBASOFT_v1.0.md                       Oldest version, kept untouched (historical)
03_DOMINIO_FASE_4/DOMAIN_MODEL.md                         Domain model v1.2 (~1960 lines; v1.0 is in git history, commit 79f823c; v1.1 must be committed before v1.2 replaces it)
03_DOMINIO_FASE_4/EVENT_CATALOG.md                        Domain events v1.2 (~1350 lines)
03_DOMINIO_FASE_4/GLOSSARY.md                             Official glossary v1.2 + Phase 4 internal audit (~2680 lines)
04_CP04_AUDITORIA/04_CP04_AUDITORIA.md                    CP-04 audit (as issued; ended "CON BLOQUEOS")
04_CP04_AUDITORIA/04_CP04_CIERRE.md                       CP-04 closure: decisions DF5-01..06, all changes, pending items, validation
04_CP04_AUDITORIA/04_CP04_DECISIONES_PENDIENTES.md         HD-25 alternatives A/B/C + DEC-01..09 one by one; revises DF5-06; CURRENT STATE
99_HERRAMIENTAS/                                          Generators + verifier for SPEC v1.1/v1.2, SRS and domain docs (not part of the product)
```

All documents except the Audit exceed a single Read: use `offset`/`limit`, or Grep for headings (`^# CAPÍTULO`, `^## `) or IDs. The monografía is a .docx; extract text with Python (`zipfile` + `word/document.xml`) to read it.

## Document hierarchy and project status

Hierarchy (never break it; each level extends the previous, never modifies it): **Monografía → Auditoría → SPEC → SRS → Modelo de dominio (DOMAIN_MODEL + EVENT_CATALOG + GLOSSARY)**.

| Checkpoint | Deliverable | Date | Status |
|---|---|---|---|
| CP-00 | Auditoría Fundacional | 2026-09-01 | Closed |
| CP-01 | Director's constitutional decisions DC-01…DC-08 (recorded in SPEC §0.1) | before 2026-09-05 | Closed (19 of 24 blocking questions) |
| CP-02 | COLBASOFT_SPEC v1.0 | 2026-09-05 | Treated as approved (file still says «Emitido para revisión») |
| CP-03 | SRS_COLBASOFT v1.0 | 2026-09-28 | Declared approved by Prompt #004; file still says «Emitido para revisión»; decisions DEC-01…DEC-09 unanswered |
| CP-04 | Domain model (3 docs) | 2026-09-28 | v1.0 emitted; audited 2026-09-29 (`04_CP04_AUDITORIA.md`) |
| DEC-01 audit | DEC-01 = A (Núcleo, 1 bodega) + piece/roll traceability (Q-11, F-1…F-6, Q-09, Q-10) → SPEC v1.2, SRS v1.2, domain v1.2 | 2026-09-30 | **Draft**: generated and cross-checked (`xref.py` clean); technical validation and functional/academic approval pending. HD-25 and HD-22 resolved; new HD-28, HD-29, HD-30, H-19, H-20 pending |
| CP-04 close | Decisions DF5-01..05 → SPEC v1.1, SRS v1.1, domain v1.1 | 2026-09-29 | **Technically validated** (`04_CP04_CIERRE.md`). DF5-06 revised (`04_CP04_DECISIONES_PENDIENTES.md`): the five v1.1 docs say «Validado técnicamente — aprobación funcional y académica pendiente». Current state: **«DECISIONES REQUERIDAS ANTES DE FASE 5»**. Nothing committed or pushed yet |

**Two phase numberings coexist.** Project phases (used by the user's prompts): Fase 0 Auditoría, 1 Constitución, 2 SPEC, 3 SRS, 4 Dominio, 5 Arquitectura… The audit's roadmap (Fase D) numbers differently (0 audit → 1 authorization → 2 theory cleanup → 3 AS-IS fieldwork → 4 requirements → 5 design → 6 build → 7 validation → 8 integration). The SRS and domain model were produced before the roadmap's AS-IS fieldwork and baseline, so they are **TO-BE** models (risk R-S01).

**Fase 5 (architecture / data model) is NOT started and still waits on decisions** (`04_CP04_DECISIONES_PENDIENTES.md`). Decisions already taken at the CP-04 close (never re-litigate them silently):
- **DF5-01:** the merchandise QR identifies **SKU + Lote** (not location, bodega or quantity). The Unidad de Inventario is still SKU + Lote + Ubicación (RN-INT-005 unchanged) and is resolved as merchandise QR + location (scanned or recorded selection); if the lot is in several locations and none is given, no operation.
- **DF5-02:** a confirmed entry leaves stock **En recepción** (RN-EXI-007); it becomes Disponible only when placed.
- **DF5-03:** the first placement is a **movimiento interno** in the kardex (RN-MOV-010); EV-INV-001 now designates that movement.
- **DF5-05:** offline records are re-validated on sync; if no longer valid they are not applied, the rejection is recorded (state «Rechazado en sincronización», EV-TRZ-007) and a Novedad is opened when they describe a physical fact (RN-INT-008).
- **DF5-06 (revised):** v1.1 docs are only **technically validated**; functional/academic approval pending. Do not write «Aprobado» until DEC-08's act exists and DEC-02…DEC-09 (and HD-28…HD-30, H-19, H-20) are answered or individually accepted in writing.

**v1.2 decisions of 2026-09-30 (owner, never re-litigate silently):** **DEC-01 = A** (approval threshold = Núcleo/H1, **1 bodega** pilot; transferencias, conteo general and the rest of H2 are outside the threshold but stay modeled); level **Ingeniería**; **Q-11** piece/roll traceability is inside the MVP; **F-1** pieza = rollo (metros/kilos) or paquete/bolsa (unidades); **F-2** quantity per piece recorded at reception; **F-3** partial cuts of rolls allowed; **F-4** after the scan the operator selects the pieza, the location filters/verifies; **F-5** count is manual, pieza by pieza; **F-6** contenedores/bolsas agrupadas inside the MVP; **Q-09** a reprint keeps the same QR (no new identity); **Q-10** the exit scan verifies and counts. DF5-01 still holds (QR = SKU + Lote); the new entity is **Pieza** (E-27, AG-22, CD-49, RN-LOT-006/007, RN-SAL-008/009, RN-MOV-011, RN-CNT-009). **HD-25 and HD-22 are resolved.** Pending (never invent answers): HD-28 (physical identity of a pieza without its own QR; mixed-lot containers; reasons to replace a QR now that reprint does not), HD-29 (remnant of a cut; partial move of a pieza), HD-30 (is every reference controlled by pieza?), SRS findings H-19 (HU-ENT-006 → HU-BOD-005 is H2) and H-20 (RF-REP-003 computes 24 KPI, KPI-02 needs H2 conteo general).

DEC-01 is answered (A, 1 bodega); DEC-02…DEC-09 are unanswered; none blocks architecture by itself, but DEC-04 (no structural rule parametrizable; before M-18/M-19 detail), DEC-06 (before the data model: KPI-05/KPI-12 capture) and DEC-07 (no money fields while DC-03 holds) impose design conditions; DEC-08 blocks formal approval. Also pending, non-blocking, need AS-IS data (mark «DECISIÓN PENDIENTE / INFORMACIÓN REQUERIDA», never invent values): HD-17 capacity with mixed units, HD-18 precision, HD-26 supplier barcode, HD-27 offline scope, number of bodegas. Mandatory inputs for the architecture once unblocked: indivisibility of the 11 operations in DOMAIN_MODEL §5.3, concurrency on one unit's availability, sync re-validation, historical reconstruction from the MVP (RNF-AUD-003, H1, even though the cut-off-date query RF-INV-006 is H2).

## How work is requested

The user drives each phase with a numbered «Prompt Maestro» and expects:
- A mandatory **Capítulo 0 «Auditoría de reanudación»** (documents, versions, constitutional decisions, closed phases, pending items) ending with `ESTADO: CONTEXTO RECONSTRUIDO`, before any content.
- Work **by chapters**, each closed with an «ESTADO DEL CAPÍTULO» block, and a final internal audit with totals.
- Absolute traceability; no lost elements; no invented numeric targets or functionality.
- Inconsistencies between documents are **recorded as findings and escalated**, never silently fixed.

The SPEC v1.1, the SRS and the three domain documents are **generated** by Python scripts in `99_HERRAMIENTAS/` (see its README). SPEC v1.1 = SPEC v1.0 + exact replacements in `spec/build_spec_v11.py`; SPEC v1.2 = SPEC v1.1 + exact replacements and insertions in `spec/build_spec_v12.py` (each must match once; `srs/parse_spec.py` now reads v1.2); to change the SPEC, add a replacement in the current builder, never edit the .md. Glossary IDs are stable: v1.0 terms keep their GL-nnn and terms added later carry `v11=True` or `v12=True` and continue the numbering. To change them, edit the data (`srs/*.md|*.txt|trace.py`, `dominio/*_data.py`) and regenerate — hand edits to generated `.md` files are lost on the next build unless also carried into the data. Generators take an optional output folder; without it they overwrite the official document, so build to a temp folder first and compare. Always finish with `python 99_HERRAMIENTAS/dominio/xref.py` (broken references, unpaired legacy IDs, malformed tables). On Windows run Python with `PYTHONIOENCODING=utf8`.

## Rules that govern any edit

From the audit's «Reglas Innegociables» and the Director's decisions:

1. **Never modify the monografía** (not even typos). Earlier documents are not edited by later phases either; new documents are derived.
2. Do not drop essential concepts.
3. **Do not invent functionality.** Every substantive element carries a provenance tag: `[MON §n]`, `[AUD x]`, `[DC-n]`, `[NUEVO]` (SPEC-level new contribution), `[SRS]` (derived in the SRS). Gap-closing proposals (PROP-* in SRS Annex C) are **not** baseline until the Director approves them.
4. **No code, architecture, technology choices, database design, C4/UML/ERD, endpoints/APIs, frameworks** until Fase 5 explicitly enables them.
5. Don't change objectives without justification; raise divergences as questions to the Director.
6. Every finding cites its source (monografía numbering follows its own table of contents, including the anomalous «5.5» Objetivos Específicos).

Constitutional decisions (SPEC §0.1, inmodificable):
- MVP scope closed: inventory/warehouse logistics, traceability, kardex, entries, exits, adjustments, counts, transfers, reports, alerts, operational dashboard.
- **Excluded absolutely:** sales, full purchasing, production, accounting, payroll, CRM, invoicing, and **any** AI (not only generative).
- **Exactly five roles:** Administrador, Jefe de Bodega, Coordinador de Bodega, Auxiliar de Bodega, Auditor. The Auditor never writes to inventory. «Sistema» is an actor for automatic actions, not a role.
- Responsive web + tablet, no native app. Power BI integration exists; analytical dashboards are not designed here.
- «Inteligente» = rule-based automation + KPI analytics. QR is the primary identifier; barcode only for lookups.
- The pilot company is never named («empresa de estudio» / «empresa piloto»).

## Identifier conventions

- **SPEC (legacy):** `DC-nn`, `PR-nn`, `PN-nn`, `CD-nn`, `M-nn`, `HU-nnn`, `RF-nnn`, `RNF-nnn`, `RN-nnn`, `KPI-nn`, `RG-nn`, `D-nn` (differentiators), `OP-nn`. PN, CD, M, KPI, RG, DC, PR keep these IDs everywhere.
- **SRS (permanent, cite these from Fase 3 on):** `HU-<DOM>-nnn`, `RF-<DOM>-nnn` (DOM = ACC USR CAT LOT BOD QRC ENT SAL MOV AJU CNT NOV INV KDX ALE REP DSH AUD PAR TAR, one per module M-01…M-20), `RNF-<CAT>-nnn` (SEG DSP REN ESC ACS AUD USA TAB NAV), `RN-<DOM>-nnn` (INT EXI MAE IDE LOT ENT SAL MOV AJU CNT NOV ALE AUD), `CU-nn`, `CA-nn` (MVP acceptance criteria). SRS Annex A maps legacy → permanent. Findings `H-01…H-18`, Director decisions `DEC-01…DEC-09` (not `D-nn`), SRS risks `R-S01…R-S10`. MoSCoW is a mechanical map of SPEC priority (P0 Must, P1 Should, P2 Could, P3 Won't); horizon H1/H2 comes from SPEC §12.3.
- **CP-04 audit/closure:** matrix rows `AC-nn`, audit findings `HA-nn`, Fase-5 blockers `B-nn`, pre-Fase-5 decisions `DF5-nn` (not DEC-nn).
- **Domain model (Fase 4):** subdomains `SD-nn`, entities `E-nn`, value objects `VO-nn`, aggregates `AG-nn`, invariants `IN-nn`, reactive policies `PO-nn`, state machines `SM-nn`, events `EV-<DOM>-nnn`, glossary `GL-nnn`, domain findings `HD-nn`, Fase-5 risks `RF5-nn`.
- IDs are **never reused or renumbered**; a retired element is marked «Retirado». When a legacy ID appears in a later document, it is paired with its permanent ID («RN-012 → RN-INT-002»).

## Vocabulary

**GLOSSARY.md is the only allowed definition of any term**; DOMAIN_MODEL Cap. 1 reuses its exact text. Controlled vocabulary (SPEC §0.5): *Ubicación, Movimiento, Ajuste, Conteo, Existencia, Documento de entrada, Referencia, Bitácora*; banned synonyms include posición/casilla/slot, transacción/registro (for movimiento), corrección/cuadre, toma física, stock/saldo, remisión/ingreso, modelo/estilo/artículo, log. Official entity names follow the SPEC, not Prompt #004 labels: Producto→Referencia, Variante→SKU, Área→Zona, Inventario→Unidad de inventario, Auditoría→Registro de bitácora + Observación de auditoría (HD-01). «Ruptura de stock» / «sobre stock» are kept as monografía terms of art only.

## Known facts that contradict headline numbers (do not «fix» without the Director)

- **Business rules:** the SPEC v1.0 says 68 (51 structural + 17 configurable); its tables contain **82** (60 + 22). v1.1 adds 3 structural rules kept separate in SPEC §9.15 (RN-081*…RN-083* → RN-EXI-007, RN-MOV-010, RN-INT-008) and v1.2 adds 6 more in §9.16 (RN-084*…RN-089* → RN-LOT-006, RN-LOT-007, RN-SAL-008, RN-MOV-011, RN-SAL-009, RN-CNT-009): **91** in SRS v1.2 and domain v1.2 (77 invariants + 14 policies cover 91/91). The 68/82 discrepancy is still declared, not fixed (DEC-03). Empty markers `RN-069*` and `RN-026b*` are not rules. The 10 rules of SPEC §9.1 are the core that must never be configurable; the SRS interprets **all** structural rules as non-configurable (DEC-04).
- **RF priorities** are 74/70/18 (P0/P1/P2), not the 72/69/21 in SPEC §7.1. SPEC §0.4 ranges (HU-001…096, RF-001…138) are wrong; there are 103 HU and 162 RF in v1.1 (110 HU, 171 RF and 498 Gherkin scenarios in v1.2; Núcleo/H1 = 91 HU / 152 RF).
- **Gaps:** PN-14 (cierre de jornada) is in the MVP backlog but has no HU/RF; 6 rules have no RF (RN-MOV-003, RN-MOV-006, RN-NOV-001, RN-NOV-002, RN-CNT-008, RN-SAL-005); 6 KPIs need data no RF captures (KPI-05, 07, 10, 12, 17, 24); «valorización» is a permission with no cost data in the MVP (DEC-07).
- Tag proportions differ between SPEC §0.3 and §13.3. Blocking open items for later phases: SPEC §13.6 (PYME definition, sector/municipality delimitation, authorization to contact companies, baseline, nine unverified sources, 2025 horizon reprojection).
