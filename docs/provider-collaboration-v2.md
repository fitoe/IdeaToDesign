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
  -> kanban-capability-task/v1(product_visual_design | visual_source_creation)
  -> IdeaToDesign
  -> kanban-capability-result/v1 + design artifacts
  -> PlanToDelivery review gate
  -> IdeaToTech and/or DesignToCode when approved
```

Expected upstream inputs:

- active slice and acceptance criteria from PlanToDelivery;
- product intent, route/page inventory, references, constraints, and prior artifact refs;
- explicit `allowed_side_effects`, `review_policy`, and `blocking_policy`.

Expected downstream outputs:

- `Design-Spec.md`, page/state matrix, decision log, or equivalent design artifact;
- `visual-source-contract.json` and persisted source paths when implementation will follow;
- Visual IR / Level-3 handoff fields sufficient for DesignToCode to implement without reinterpretation;
- result manifest with evidence, blockers, debts, and recommended next capability.

## Gate discipline

- IdeaToDesign may recommend `suggested_gate_updates`, but PlanToDelivery alone records canonical gates.
- Design approval, visual direction selection, source freeze, and Level-3 handoff review are `review_required: true`, not generic `blocked`.
- Use `blocked` only for missing/contradictory product facts, unavailable source assets, permission issues, or non-waivable design decisions.
- If a design artifact supersedes a previous one, mark stale/superseded artifacts in the result/debt notes instead of silently overwriting the delivery state.
- Do not send code tasks downstream until the approved source and implementation facts are persisted.

## Registry references

- Provider manifest: `contracts/provider-manifest.json`
- Task contracts: `contracts/product-visual-design-task-v1.md`, `contracts/visual-source-creation-task-v1.md`
- Result contract: `contracts/design-result-manifest-v1.md`
- Runtime skill: `idea-to-design/SKILL.md`
