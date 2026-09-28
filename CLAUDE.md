# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

This is **not a code repository** in the usual sense (no build system, no tests, no application source). Git is used only for version history and backup on GitHub. It is a document workspace for COLBASOFT, an academic degree project (Tecnólogo en Desarrollo de Software, CIAF, Pereira — per the monografía's cover page; the user's most recent presentation slide instead said «Ingeniería en Desarrollo de Software», unconfirmed). There are no build/lint/test commands. Working here means reading and writing documents, **in Spanish**.

COLBASOFT = *Plataforma inteligente para la automatización y trazabilidad de inventarios en PYMES del sector textil del Eje Cafetero*.

```
00_MONOGRAFIA_ORIGINAL/MONOGRAFÍA  COLBASOFT.docx         Source of truth, immutable (note the double space in the filename)
00_AUDITORIA_FASE_0/AUDITORIA_FUNDACIONAL_COLBASOFT.md    Audit (~980 lines)
01_SPEC_FASE_2/COLBASOFT_SPEC_v1.0.md                     Functional spec (~3500 lines, ~300 KB)
02_SRS_FASE_3/SRS_COLBASOFT_v1.0.md                       SRS, ISO/IEC/IEEE 29148 adapted (~7100 lines, ~530 KB)
03_DOMINIO_FASE_4/DOMAIN_MODEL.md                         Domain model (~1900 lines)
03_DOMINIO_FASE_4/EVENT_CATALOG.md                        Domain events (~1300 lines)
03_DOMINIO_FASE_4/GLOSSARY.md                             Official glossary + Phase 4 internal audit (~2600 lines)
99_HERRAMIENTAS/                                          Generators + verifier for the SRS and domain docs (not part of the product)
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
| CP-04 | Domain model (3 docs) | 2026-09-28 | Emitted for Director review |

**Two phase numberings coexist.** Project phases (used by the user's prompts): Fase 0 Auditoría, 1 Constitución, 2 SPEC, 3 SRS, 4 Dominio, 5 Arquitectura… The audit's roadmap (Fase D) numbers differently (0 audit → 1 authorization → 2 theory cleanup → 3 AS-IS fieldwork → 4 requirements → 5 design → 6 build → 7 validation → 8 integration). The SRS and domain model were produced before the roadmap's AS-IS fieldwork and baseline, so they are **TO-BE** models (risk R-S01).

**Next phase (Fase 5: architecture / data model) is blocked on:** HD-04 (does a merchandise QR identify SKU+Lote or the unidad de inventario = SKU+Lote+Ubicación?), HD-07, HD-17, and Director answers to DEC-01, DEC-04, DEC-05. Ask whether these were resolved; never invent the answers.

## How work is requested

The user drives each phase with a numbered «Prompt Maestro» and expects:
- A mandatory **Capítulo 0 «Auditoría de reanudación»** (documents, versions, constitutional decisions, closed phases, pending items) ending with `ESTADO: CONTEXTO RECONSTRUIDO`, before any content.
- Work **by chapters**, each closed with an «ESTADO DEL CAPÍTULO» block, and a final internal audit with totals.
- Absolute traceability; no lost elements; no invented numeric targets or functionality.
- Inconsistencies between documents are **recorded as findings and escalated**, never silently fixed.

The SRS and the three domain documents are **generated** from structured data by Python scripts in `99_HERRAMIENTAS/` (see its README). To change them, edit the data (`srs/*.md|*.txt|trace.py`, `dominio/*_data.py`) and regenerate — hand edits to generated `.md` files are lost on the next build unless also carried into the data. Generators take an optional output folder; without it they overwrite the official document, so build to a temp folder first and compare. Always finish with `python 99_HERRAMIENTAS/dominio/xref.py` (broken references, unpaired legacy IDs, malformed tables). On Windows run Python with `PYTHONIOENCODING=utf8`.

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
- **Domain model (Fase 4):** subdomains `SD-nn`, entities `E-nn`, value objects `VO-nn`, aggregates `AG-nn`, invariants `IN-nn`, reactive policies `PO-nn`, state machines `SM-nn`, events `EV-<DOM>-nnn`, glossary `GL-nnn`, domain findings `HD-nn`, Fase-5 risks `RF5-nn`.
- IDs are **never reused or renumbered**; a retired element is marked «Retirado». When a legacy ID appears in a later document, it is paired with its permanent ID («RN-012 → RN-INT-002»).

## Vocabulary

**GLOSSARY.md is the only allowed definition of any term**; DOMAIN_MODEL Cap. 1 reuses its exact text. Controlled vocabulary (SPEC §0.5): *Ubicación, Movimiento, Ajuste, Conteo, Existencia, Documento de entrada, Referencia, Bitácora*; banned synonyms include posición/casilla/slot, transacción/registro (for movimiento), corrección/cuadre, toma física, stock/saldo, remisión/ingreso, modelo/estilo/artículo, log. Official entity names follow the SPEC, not Prompt #004 labels: Producto→Referencia, Variante→SKU, Área→Zona, Inventario→Unidad de inventario, Auditoría→Registro de bitácora + Observación de auditoría (HD-01). «Ruptura de stock» / «sobre stock» are kept as monografía terms of art only.

## Known facts that contradict headline numbers (do not «fix» without the Director)

- **Business rules:** the SPEC says 68 (51 structural + 17 configurable); its tables contain **82** (60 + 22). The SRS and domain model use 82. Empty markers `RN-069*` and `RN-026b*` are not rules. The 10 rules of SPEC §9.1 are the core that must never be configurable; the SRS interprets **all** structural rules as non-configurable (DEC-04).
- **RF priorities** are 74/70/18 (P0/P1/P2), not the 72/69/21 in SPEC §7.1. SPEC §0.4 ranges (HU-001…096, RF-001…138) are wrong; there are 103 HU and 162 RF.
- **Gaps:** PN-14 (cierre de jornada) is in the MVP backlog but has no HU/RF; 6 rules have no RF (RN-MOV-003, RN-MOV-006, RN-NOV-001, RN-NOV-002, RN-CNT-008, RN-SAL-005); 6 KPIs need data no RF captures (KPI-05, 07, 10, 12, 17, 24); «valorización» is a permission with no cost data in the MVP (DEC-07).
- Tag proportions differ between SPEC §0.3 and §13.3. Blocking open items for later phases: SPEC §13.6 (PYME definition, sector/municipality delimitation, authorization to contact companies, baseline, nine unverified sources, 2025 horizon reprojection).
