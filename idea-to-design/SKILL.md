---
name: idea-to-design
description: Design provider kernel. Use when a Javis/Kanban task envelope requests product_visual_design or visual_source_creation and the output must be an approved design artifact/result manifest, not orchestration or coding.
---

# IdeaToDesign — Design Provider Kernel

## Role

`idea-to-design` is a bounded **design provider** for Javis/Kanban. It turns product intent, active-slice requirements, and referenced artifacts into design outputs that the orchestrator can review and route downstream.

It is not the project orchestrator, not the technical planner, and not the coding executor.

## When to activate

Use this skill when:

- invoked by a `kanban-capability-task/v1` envelope;
- the requested capability is `product_visual_design` or `visual_source_creation`;
- a project needs product/design specs, flows, page inventory, visual direction, persisted visual sources, design freeze evidence, or implementation-ready design handoff.

Do not use for routine code implementation after a frozen handoff; route that to `design-to-code`.

## Advertised capabilities

| Capability | Output intent |
|---|---|
| `product_visual_design` | product/design spec, page/flow/state matrix, decisions, open questions, visual direction for review |
| `visual_source_creation` | persisted visual sources, visual-source contract, design freeze evidence, Level-3 handoff inputs |

## Inputs

Read only the active-slice context unless the task explicitly requests global design reconciliation.

Expected task envelope fields:

- `schema: kanban-capability-task/v1`
- `task_id`
- `capability`
- `project_root`
- `active_slice`
- `input_artifact_refs`
- `output_root`
- `expected_outputs`
- `verification_expectations`
- `allowed_side_effects`
- `review_policy`
- `blocking_policy`

Use artifact paths as source of truth. Do not rely on long conversation memory.

## Outputs

Return a `kanban-capability-result/v1`-shaped manifest.

Minimum fields:

```json
{
  "schema": "kanban-capability-result/v1",
  "task_id": "",
  "capability": "product_visual_design | visual_source_creation",
  "provider": "idea-to-design",
  "result": "completed | partial | blocked | failed",
  "changed_files": [],
  "produced_artifacts": [],
  "evidence": [],
  "blockers": [],
  "debts": [],
  "review_required": true,
  "suggested_kanban_updates": [],
  "next_recommended_task": null
}
```

Heavy rationale, visual analysis, prompt logs, image paths, Visual IR, review notes, and design comparisons must live in files referenced by the manifest.

## Artifact locations

Use the requested `output_root` when provided. Otherwise default to project-approved design artifact locations such as:

```text
project-state/design/
```

Typical artifacts:

- `Design-Spec.md`
- `page-matrix.json`
- `visual-source-contract.json`
- `implementation-blueprint.json`
- `component-blueprint.json`
- `debt-ledger.json`
- `visual-ir/*`
- generated or approved visual source files
- design review notes

## Result semantics

- `completed`: requested design artifacts are ready for orchestrator review/consumption.
- `partial`: usable artifacts exist, but precise decisions, assets, states, or handoff fields remain missing.
- `blocked`: required product input, approval, source asset, permission, or non-waivable design decision is missing or contradictory.
- `failed`: the provider could not produce usable artifacts; include cause and recovery suggestion.

Set `review_required: true` for visual direction, generated source, Level-3 handoff, design freeze, or any user-facing design decision. This routes to review, not generic blocked.

## Collaboration boundary

- Upstream owner: PlanToDelivery/Javis provides the active slice, artifact refs, review policy, blocking policy, and allowed side effects.
- Downstream consumers: IdeaToTech consumes approved product/design artifacts for technical planning; DesignToCode consumes frozen visual sources, Visual IR, and Level-3 handoff artifacts for implementation.
- Provider output is advisory until PlanToDelivery ingests the manifest and records canonical state.
- If the source is not yet approved, return artifacts with `review_required: true`; do not route implementation as if the gate passed.
- If the requested output would require architecture or coding decisions, recommend `technical_blueprint`, `implementation_planning`, or `visual_implementation` instead of performing that work here.
- See `docs/provider-collaboration-v2.md` in the source repository for the full provider boundary.

## Gate discipline

- Providers recommend; Javis/PlanToDelivery records canonical Kanban gates.
- IdeaToDesign must not create, complete, approve, or unlock Hermes Kanban stage Gates directly. In P2D mode it may only return `kanban-capability-result/v1` evidence plus `suggested_kanban_updates`; the orchestrator decides and applies concrete Kanban card/link/review transitions.
- Design artifacts, visual sources, local JSON, provider manifests, and prose recommendations cannot unlock downstream technical planning/implementation work by themselves.
- If a product/content/IA/visual-source/design-freeze decision affects whether downstream work may start, report it as a suggested Kanban update with the proposed Gate/card title, dependency target, required approval artifact, and reason it affects stage admission.
- Do not mark global design gates passed.
- Do not directly edit global execution progress unless the task explicitly authorizes it.
- If design changes supersede earlier artifacts, mark affected outputs as `stale` or `superseded` in the result/debt notes.
- If implementation should proceed, recommend `visual_implementation` as the next capability.

## Operating rules

1. Clarify the smallest missing design fact only when it blocks the active slice.
2. Prefer concrete artifacts over prose.
3. Persist visual sources and source paths before claiming design readiness.
4. Extract implementation facts after approval: page type, route intent, viewport, section order, density, card/list anatomy, action hierarchy, asset strategy, and must-not-do rules.
5. For flat PNG/GPT Image/mockup sources, produce lightweight Visual IR rather than long prose-only handoff.
6. Avoid reopening broad visual exploration after approval unless the source is missing, stale, rejected, or requirements changed.

## Progressive references

Load only when needed:

- `references/main-skill-full-reference.md` — legacy detailed design workflow.
- `references/stage-gates.md` — design gate semantics.
- `references/review-checklists.md` — product/visual review prompts.
- `references/creative-direction-system.md` — visual direction exploration.
- `references/aesthetic-review-system.md` — aesthetic review.
- `references/prompt-patterns.md` — image/mockup prompt patterns.
- `templates/level-3-handoff-pack.md` — complete Level-3 handoff shape.

## Common pitfalls

| Pitfall | Fix |
|---|---|
| Acting as global project owner | Return manifest recommendations; let Javis update canonical state |
| Producing prose without artifacts | Persist design artifacts and reference their paths |
| Continuing design after frozen handoff | Recommend `visual_implementation` and stop carrying exploration context |
| Treating review as blocked | Use `review_required: true`; reserve `blocked` for missing/contradictory inputs |
| Letting implementation reinterpret design | Freeze source and emit structured Visual IR/handoff artifacts |
