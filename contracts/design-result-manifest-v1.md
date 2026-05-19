# Design Result Manifest v1

IdeaToDesign returns `kanban-capability-result/v1` manifests.

## Required Fields

- `schema_version`: `kanban-capability-result/v1`
- `task_id`
- `correlation_id`
- `capability`
- `status`
- `summary`
- `artifacts`
- `evidence`
- `review_required`
- `blocked`
- `blockers`
- `debt`
- `next_tasks`

## Artifact Types

- `design_spec`
- `page_matrix`
- `component_blueprint`
- `visual_source`
- `asset_notes`
- `design_debt_ledger`

## Example

```json
{
  "schema_version": "kanban-capability-result/v1",
  "task_id": "kb_design_001",
  "correlation_id": "site-home-design",
  "capability": "product_visual_design",
  "status": "completed",
  "summary": "Homepage visual direction and page/state matrix are ready for review.",
  "artifacts": [
    {"type": "design_spec", "path": "project-state/design/design-spec.md"},
    {"type": "page_matrix", "path": "project-state/design/page-matrix.json"}
  ],
  "evidence": [],
  "review_required": true,
  "blocked": false,
  "blockers": [],
  "debt": [],
  "next_tasks": [
    {"capability": "visual_implementation", "reason": "After design gate approval"}
  ]
}
```

## Semantics

- Design approval is `review_required=true`, not `blocked=true`.
- Missing/contradictory required input is `blocked=true`.
- Downstream work is recommended by capability name, never by hard-coded provider internals.
