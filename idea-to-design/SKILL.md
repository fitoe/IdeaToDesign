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

### Mandatory P2D provider admission

When invoked by PlanToDelivery/Javis/P2D/Hermes Kanban, IdeaToDesign must not start from chat history, restored TODOs, or an informal `继续` instruction alone.

Before producing canonical design artifacts in P2D mode, verify:

1. `kanban-capability-task/v1` task envelope path;
2. `active-slice-digest/v1` path whose provenance matches the task envelope;
3. capability is `product_visual_design` or `visual_source_creation`;
4. current Hermes Kanban card is claimed/running for that task;
5. `output_root` is defined and result manifest path will be `output_root/result-manifest.json`;
6. `design_contract` contains target pages, acceptance criteria, and the capability-specific design input;
7. `visual_source_creation` includes approved design direction;
8. `expected_outputs`, `verification_expectations`, and `allowed_side_effects` are explicit.

Run the local admission guard when available:

```bash
python3 idea-to-design/scripts/check-provider-context.py \
  --task "$OUTPUT_ROOT/task-envelope.json" \
  --digest "$OUTPUT_ROOT/active-slice-digest.json" \
  --card-status "$OUTPUT_ROOT/card-status.json"
```

`--skip-running-check` is only for local contract tests or isolated dry-runs. In real PlanToDelivery/Hermes Kanban orchestration, missing running-card proof is a blocker.

If the guard cannot be run or any required item is missing, return a `blocked` result naming the missing artifact/check. Do not create or overwrite design artifacts first.

Immediately before any filesystem write in P2D mode, run the public pre-write guard with the exact files about to change:

```bash
PYTHONPATH=/home/imjzq/Projects/PlanToDelivery \
python3 /home/imjzq/Projects/PlanToDelivery/.agents/skills/plantodelivery/scripts/p2d_enforce.py \
  --project-root "$PROJECT_ROOT" \
  --board "$BOARD" \
  prewrite \
  --task-envelope "$OUTPUT_ROOT/task-envelope.json" \
  --active-slice-digest "$OUTPUT_ROOT/active-slice-digest.json" \
  --execution-permit "$OUTPUT_ROOT/execution-permit.json" \
  --expected-capability "$CAPABILITY" \
  --changed-file "relative/path/about-to-change"
```

Repeat `--changed-file` for every intended file. Run this before `write_file`, `patch`, design artifact writes, generated images copied into project state, evidence writes, or `result-manifest.json` writes. If `prewrite` exits non-zero, do not write; return a `blocked` result naming the guard error.

The Python API `assert_provider_write_allowed(ctx, changed_files, review_required=True)` is the equivalent in-process guard, but the CLI above is preferred for auditability. Evidence files and manifests are not allowed to bypass this check.

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
4. **Generated design source rule:** when producing any user-facing “设计图”, “视觉源”, “视觉板”, “设计稿”, “mockup”, or design draft, create it through the configured GPT Image2/image-generation workflow and save the raw generated image locally as the design source. Do not use local browser screenshots, coded HTML previews, implementation screenshots, or Playwright captures as design-source artifacts unless the user explicitly asks for screenshot evidence rather than a design image.
5. **High-quality visual prompt protocol:** before writing prompts for homepages, landing pages, brand-defining screens, key visual approval images, or any generated design source that must reach `distinctive` / `excellent` maturity, load `references/high-quality-visual-prompt-protocol.md`. Compile the image prompt from design decisions rather than a long wishlist, including Prompt Brief Card, Design DNA Card, Content Evidence Ledger, One Memorable Move, Page Narrative Map, Canvas Contract, Asset Strategy, Prompt Lint, and the final image prompt. For regulated, factual, or trust-sensitive domains such as healthcare, government, finance, education, manufacturing, SaaS, ecommerce, legal, nonprofit, and local services, also load `references/domain-visual-risk-packs.md` and add the relevant factual-safety constraints to the prompt.
6. **GPT Image2 quality-tier rule:** use `gpt-image-2-high` for homepage/landing-page hero and other final/key visual approval boards where visual quality drives the whole project direction. Use `gpt-image-2-medium` for ordinary secondary pages, non-final iteration boards, and most follow-up page batches. Avoid `gpt-image-2-low` for user-facing approval artifacts except rough private exploration explicitly marked as draft. If the configured default is medium, temporarily switch or route the homepage/key-page generation through the high tier, then return to medium for other pages.
7. **Generated-image delivery rule:** after `image_generate` succeeds, save/copy the raw generated image to the project artifact path and send it to the user immediately via `MEDIA:`. Do not run `vision_analyze` or other recognition/OCR checks on the generated image before sending unless the user explicitly asks for inspection, there is a tool/runtime error, the file is missing/empty, or the task is verification rather than design delivery. For routine design approval images, only perform cheap file-level checks such as existence, size, and dimensions if needed.
8. **Complete-page / flexible-board design rule:** generated design sources must show complete, decisionable page/screen states, but they do not have to be strictly one page per image. Choose the board layout by review usefulness and page type: homepages and key/complex pages usually deserve a single complete-page image; secondary desktop pages may be paired as two complete pages side-by-side; mobile/H5 flows may combine up to about three complete phone pages/states in one board when readability remains strong. Never use a board that squeezes 4–5 pages into one image with cropped/half-page previews as the approval artifact. If a multi-page board is used, every included page/state must be complete enough for approval and later implementation extraction; otherwise split into separate generated sources.
9. Clearly label artifact roles in manifests and review packets: `design_source` for GPT Image2/generated design files; `implementation_screenshot` / `verification_evidence` for local browser screenshots. Never present verification screenshots as design drawings.
10. Extract implementation facts after approval: page type, route intent, viewport, section order, density, card/list anatomy, action hierarchy, asset strategy, and must-not-do rules.
11. For flat PNG/GPT Image/mockup sources, produce lightweight Visual IR rather than long prose-only handoff.
12. Avoid reopening broad visual exploration after approval unless the source is missing, stale, rejected, or requirements changed.

## Progressive references

Load only when needed:

- `references/main-skill-full-reference.md` — legacy detailed design workflow.
- `references/stage-gates.md` — design gate semantics.
- `references/review-checklists.md` — product/visual review prompts.
- `references/creative-direction-system.md` — visual direction exploration.
- `references/aesthetic-review-system.md` — aesthetic review.
- `references/high-quality-visual-prompt-protocol.md` — compile homepage, landing-page, brand-defining, and key visual approval image prompts from design decisions instead of generic wishlists.
- `references/domain-visual-risk-packs.md` — factual-safety and domain-fit constraints for healthcare, government, finance, manufacturing, SaaS/AI, ecommerce, education, legal, nonprofit, and local-service visuals.
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
