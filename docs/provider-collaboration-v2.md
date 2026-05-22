# IdeaToDesign Provider Collaboration v2

IdeaToDesign is the bounded design provider in the Javis/PlanToDelivery V2 provider system. It owns design artifacts for the active slice, but it does not own project orchestration, canonical progress, or downstream code implementation.

## Capability boundary

| Capability | Owned by IdeaToDesign | Not owned by IdeaToDesign |
|---|---|---|
| `product_visual_design` | product/design spec, page/flow/state matrix, visual direction, design decisions and open questions | technical architecture, implementation sequencing, canonical gate mutation |
| `visual_source_creation` | persisted visual source, visual-source contract, design freeze evidence, Visual IR / Level-3 handoff inputs | coding, visual parity claims, global delivery progress |

## Upstream / downstream handoff

```text
PlanToDelivery/Javis
  -> Hermes Kanban card(status=running)
  -> kanban-capability-task/v1(product_visual_design | visual_source_creation)
  -> active-slice-digest/v1
  -> IdeaToDesign admission guard
  -> IdeaToDesign
  -> design artifacts / persisted visual sources
  -> output_root/result-manifest.json using kanban-capability-result/v1
  -> PlanToDelivery review/gate decision
  -> IdeaToTech and/or DesignToCode when approved
```

Expected upstream inputs:

- active slice and acceptance criteria from PlanToDelivery;
- product intent, route/page inventory, references, constraints, and prior artifact refs;
- `design_contract` containing project context/target pages/requirements for product design, or approved design direction for visual source creation;
- explicit `allowed_side_effects`, `review_policy`, and `blocking_policy`;
- output root and required artifact names;
- running Kanban card snapshot/proof from the orchestrator.

Expected downstream outputs:

- `Design-Spec.md`, page/state matrix, decision log, or equivalent design artifact;
- `visual-source-contract.json` and persisted source paths when implementation will follow;
- Visual IR / Level-3 handoff fields sufficient for DesignToCode to implement without reinterpretation;
- result manifest with evidence, blockers, debts, review requirement, and recommended next capability.

## Admission guard

Before provider work in P2D mode, run the local checker declared in the provider manifest:

```bash
python3 idea-to-design/scripts/check-provider-context.py \
  --task "$OUTPUT_ROOT/task-envelope.json" \
  --digest "$OUTPUT_ROOT/active-slice-digest.json" \
  --card-status "$OUTPUT_ROOT/card-status.json"
```

`--skip-running-check` is only for local contract tests or isolated dry-runs. In real Hermes Kanban orchestration, omitting the running card proof is a blocker.

The guard verifies:

- task and digest schemas;
- task_id and capability consistency;
- capability is `product_visual_design` or `visual_source_creation`;
- output root handoff writes `output_root/result-manifest.json`;
- expected design/visual-source outputs are declared;
- allowed side effects are explicit;
- design brief/page scope/acceptance criteria exist;
- `visual_source_creation` has approved design direction;
- result manifest schema and review handoff are valid when supplied.

## Gate discipline

- IdeaToDesign may recommend `suggested_kanban_updates`, but PlanToDelivery alone records canonical gates.
- Design approval, visual direction selection, source freeze, and Level-3 handoff review are `review_required: true`, not generic `blocked`.
- Use `result=blocked` only for missing/contradictory product facts, unavailable source assets, permission issues, or non-waivable design decisions.
- If a design artifact supersedes a previous one, mark stale/superseded artifacts in the result/debt notes instead of silently overwriting the delivery state.
- Do not send code tasks downstream until the approved source and implementation facts are persisted and accepted or explicitly waived by PlanToDelivery.

## Registry references

- Provider manifest: `contracts/provider-manifest.json`
- Task contracts: `contracts/product-visual-design-task-v1.md`, `contracts/visual-source-creation-task-v1.md`
- Result contract: `contracts/design-result-manifest-v1.md`
- Admission guard: `idea-to-design/scripts/check-provider-context.py`
- Runtime skill: `idea-to-design/SKILL.md`
