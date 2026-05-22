# Design Result Manifest v1

IdeaToDesign returns `kanban-capability-result/v1` manifests for `product_visual_design` and `visual_source_creation`. The manifest is written to `output_root/result-manifest.json` and is advisory until PlanToDelivery ingests it and updates canonical Kanban state.

## Required Result Manifest Fields

```json
{
  "schema": "kanban-capability-result/v1",
  "task_id": "",
  "capability": "product_visual_design | visual_source_creation",
  "provider": "idea-to-design",
  "result": "completed | partial | blocked | failed",
  "summary": "",
  "changed_files": [],
  "produced_artifacts": [],
  "evidence": [],
  "blockers": [],
  "debts": [],
  "review_required": true,
  "design_acceptance": {
    "design_ready": false,
    "accepted_by_user_or_orchestrator": false,
    "remaining_design_debt": [],
    "downstream_unblocked": false
  },
  "suggested_kanban_updates": [],
  "next_recommended_task": null
}
```

## Artifact Types

- `design_spec`
- `page_matrix`
- `component_blueprint`
- `visual_source`
- `visual_source_contract`
- `visual_ir`
- `level_3_handoff_pack`
- `asset_notes`
- `design_debt_ledger`
- `review_notes`

## Evidence Requirements

For `result=completed` or `result=partial`, include produced artifacts. For generated or approval-facing visual sources, include evidence referencing the persisted design source path or review packet.

When `review_required=true`, include `suggested_kanban_updates` so the orchestrator can create or move the proper design review/gate card. IdeaToDesign does not directly mark the design gate accepted.

## Example

```json
{
  "schema": "kanban-capability-result/v1",
  "task_id": "kb_design_001",
  "capability": "product_visual_design",
  "provider": "idea-to-design",
  "result": "completed",
  "summary": "Homepage visual direction and page/state matrix are ready for review.",
  "changed_files": [],
  "produced_artifacts": [
    "Design-Spec.md",
    "page-matrix.json"
  ],
  "evidence": [
    {"type": "design_spec", "path": "Design-Spec.md"},
    {"type": "page_matrix", "path": "page-matrix.json"}
  ],
  "blockers": [],
  "debts": [],
  "review_required": true,
  "design_acceptance": {
    "design_ready": true,
    "accepted_by_user_or_orchestrator": false,
    "remaining_design_debt": [],
    "downstream_unblocked": false
  },
  "suggested_kanban_updates": [
    {
      "type": "design_review",
      "title": "Review homepage design direction",
      "reason": "Design gate approval is required before visual source creation or implementation."
    }
  ],
  "next_recommended_task": {
    "capability": "visual_source_creation",
    "reason": "After design gate approval, materialize implementation-ready visual source."
  }
}
```

## Semantics

- `completed`: requested design artifacts are ready for orchestrator/user review or downstream consumption after approval.
- `partial`: usable artifacts exist, but precise decisions, assets, states, or handoff fields remain missing.
- `blocked`: required product input, target scope, approved direction, artifact access, permission, or non-waivable design decision is missing or contradictory.
- `failed`: the provider could not produce usable artifacts; include cause and recovery suggestion.

Design approval is `review_required=true`, not `blocked=true`. Missing/contradictory required input is `result=blocked`. Downstream work is recommended by capability name, never by hard-coded provider internals.
