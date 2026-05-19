---
name: idea-to-design
description: Use when turning product ideas, rough concepts, feature goals, or uncertain UI directions into approved visual sources and implementation-ready design handoff artifacts.
---

# Idea to Design

## Purpose

Move from idea to approved design source and handoff package. This skill owns product/visual exploration, design freeze, post-visual extraction, and implementation handoff readiness — not routine coding after handoff.

## Ownership Boundary

`idea-to-design` owns:
- idea clarification, product/design spec, task flows, page inventory
- visual direction, generated/staged mockups, design review
- Visual Freeze approval
- Post-Visual Extraction
- Level 3 implementation-ready handoff

After the user-approved visual source has Visual Freeze + Post-Visual Extraction + Level 3 handoff, routine implementation and parity repair move to `design-to-code`.

Return here after handoff only when the visual source is missing/stale, product state changed, requirements conflict with the design, the user asks for a design change, or handoff artifacts are too weak.

## Deliverable Levels

- **Level 1 — Product Design**: product/design spec, flows, pages, decisions, open questions.
- **Level 2 — Visual Source**: approved mockups/assets/tokens or equivalent persisted visual source.
- **Level 3 — Implementation Handoff**: Level 1+2 plus implementation-ready artifacts for downstream coding.

Level 3 should include or explicitly waive:
- `Design-Spec.md` or equivalent
- approved visual source paths
- `DESIGN.md` / `tokens.json` when applicable
- `visual-source-contract.json`
- `implementation-blueprint.json`
- `page-matrix.json`
- `component-blueprint.json`
- `debt-ledger.json`
- `design-to-code-inputs/manifest.json`
- page briefs or Visual IR for fidelity-critical PNG/GPT Image 2 sources

## Post-Visual Extraction

After design approval, extract implementation facts from the approved source before coding:
- page type, route intent, viewport
- section order and section names
- bbox / relative placement for key sections when fidelity matters
- first-screen density, card/list anatomy, action hierarchy
- asset strategy: CSS/SVG/Iconify/crop/defer
- must-preserve and must-not-do rules

For flat PNG/GPT Image 2 mockups, prefer lightweight Visual IR over long prose.

## Gate Rules

Before handing to implementation:
- visual source is persisted and user-approved
- design status is frozen or explicitly scoped as provisional
- open design questions are closed, waived, or listed as debt
- downstream artifacts identify routes/pages and maturity targets
- no secrets/tokens/private credentials are stored in design artifacts

## Kanban Provider Mode

Use this mode when invoked through a `kanban-capability-task/v1` envelope, a provider registry entry, or Javis/PlanToDelivery kanban dispatch. In this mode, `idea-to-design` is a provider, not the project orchestrator.

Advertised capabilities:
- `product_visual_design`: product/design spec, flows, page inventory, design decisions, open questions, and approval-ready visual direction;
- `visual_source_creation`: persisted visual sources, prompt/output records, visual-source contract, design freeze evidence, and implementation handoff inputs.

Provider rules:
- accept only the active slice and input artifact refs from the task envelope; do not reopen the whole project unless the task explicitly asks for global design reconciliation;
- produce artifacts under the requested output root when provided, otherwise under `project-state/design/` or the project-approved design artifact directory;
- return a `kanban-capability-result/v1`-shaped manifest instead of a prose-only handoff;
- include `capability`, `result`, `changed_files`, `produced_artifacts`, `evidence`, `blockers`, `debts`, `review_required`, and `next_recommended_task`;
- do not mark global design gates passed; recommend gate updates and let the orchestrator record them;
- set `review_required: true` when visual direction, generated source, Level 3 handoff, or design freeze needs human/orchestrator review. This is not a `blocked` result unless required inputs are missing or contradictory.

Result semantics:
- `completed`: requested design capability and artifacts are ready for orchestrator review/consumption;
- `partial`: usable artifacts exist but specific gaps/debts remain; list the missing artifacts or decisions precisely;
- `blocked`: required input, approval, source asset, permission, or non-waivable product decision is missing.

Prefer manifest artifact paths over long descriptions. Keep design rationale concise and put heavy visual analysis, prompts, image paths, Visual IR, and review notes in files.

## PlanToDelivery Project-State Collaboration

When routed by `PlanToDelivery`, treat project-root `project-state/` as the portable handoff layer. Do not directly modify global `execution-progress.json` or `artifact-manifest.json` unless explicitly authorized.

Produce or update design artifacts, usually under `project-state/design/` or the project-approved equivalent:
- `Design-Spec.md`
- `visual-source-contract.json`
- `implementation-blueprint.json`
- `page-matrix.json`
- `component-blueprint.json`
- `debt-ledger.json`
- `visual-ir/*` for fidelity-critical PNG/GPT Image 2 sources

Return compact delta handoff suggestions to `PlanToDelivery`:
- `result`: `completed`, `partial`, or `blocked`
- `changed_files` and `produced_artifacts` for design artifacts created or updated
- `suggested_manifest_entries` for each artifact with `id`, `kind`, `path`, `status`, `producer`, `consumer`, and summary
- `suggested_progress_updates` for design tasks, open decisions, user confirmation, and handoff readiness
- design gate recommendation, but do not mark the global gate passed yourself
- blockers/debts when visual source, approval, requirements, or extraction are missing
- evidence such as approved source paths, review notes, or user confirmation references
- `next_recommended_task`, usually routing to `design-to-code` after Visual Freeze and Post-Visual Extraction

After Visual Freeze and Post-Visual Extraction, recommend design artifacts as `ready` or `approved` for consumers `PlanToDelivery`, `IdeaToTech`, and `design-to-code`. If design changes later, report affected artifacts as `stale` or `superseded`.

## Low-Context Design Handoff Delta

When routed by `PlanToDelivery`, design work should stay scoped to the active page, route, section, or design decision named in the invocation brief.

Rules:
- do not reopen broad visual exploration after a visual source is approved unless the source is missing, stale, rejected, or requirements changed;
- read only the design/product artifacts referenced by `input_artifact_refs` plus the minimum source image/Figma/context needed for the active slice;
- persist heavy design analysis, Visual IR, review notes, prompt outputs, and handoff packs as files under `project-state/design/` or the project-approved design artifact directory;
- return artifact IDs/paths and a concise gate recommendation instead of long visual prose;
- mark superseded or stale design artifacts explicitly when a redesign occurs; do not leave conflicting sources active;
- after Level 3 handoff, recommend routing to `design-to-code` and stop carrying design exploration context forward.

Default delta response:

```json
{
  "result": "completed | partial | blocked",
  "changed_files": [],
  "produced_artifacts": [],
  "suggested_manifest_entries": [],
  "suggested_progress_updates": [],
  "suggested_blockers": [],
  "suggested_gate_updates": [],
  "evidence": [],
  "largest_remaining_gaps": [],
  "next_recommended_task": ""
}
```

## Progressive Loading

Load only when needed:
- `templates/level-3-handoff-pack.md` — full handoff package shape
- `references/stage-gates.md` — detailed gate semantics
- `references/review-checklists.md` — visual/product review prompts
- `references/session-recovery.md` — recovery state details
- `references/main-skill-full-reference.md` — full legacy detail if this compact guide is insufficient

## Common Pitfalls

| Pitfall | Fix |
|---|---|
| Letting coding reinterpret design from prose | Freeze source + extract structured handoff |
| Continuing design work after handoff | Route implementation/parity repair to `design-to-code` |
| Flat mockup only has a brief | Add Visual IR or explicit must-preserve/must-not-do |
| Treating tokens as full design | Also capture page anatomy and section density |
