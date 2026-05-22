# Visual Source Creation Task v1

Capability: `visual_source_creation`

## Purpose

Turn approved design direction into implementation-ready visual source artifacts for downstream implementation providers.

## Envelope

Use `kanban-capability-task/v1` with `capability=visual_source_creation`.

IdeaToDesign must be admitted by PlanToDelivery/Javis before producing canonical visual sources for a P2D slice.

## Required Inputs

This contract is carried inside a `kanban-capability-task/v1` envelope admitted by PlanToDelivery. The envelope must include:

- `schema: kanban-capability-task/v1`
- `task_id`
- `capability: visual_source_creation`
- `project_root`: absolute path to target project
- `active_slice`: bounded page/screen/state scope
- `input_artifact_refs`: approved design direction, design spec, page matrix, or review decision refs
- `output_root`: provider artifact directory; result manifest path is always `output_root/result-manifest.json`
- `expected_outputs`: must include `result-manifest.json` and visual source/handoff artifacts
- `verification_expectations`: source-readiness and downstream handoff expectations
- `allowed_side_effects`: explicit file/image-generation/write side effects permitted for the slice
- `review_policy`: source freeze/review routing
- `blocking_policy`: missing approval/source handling
- `design_contract`: see below
- `kanban_constraints`: running card/gate/dependency constraints from PlanToDelivery

`design_contract` must include:

- `approved_design_direction`: text, file, board, or explicit approval reference
- `target_pages`: pages/screens and states to materialize
- `implementation_constraints`: platform, viewport, framework, asset constraints
- `acceptance_criteria`: readiness expectations for downstream implementation

## Expected Artifacts

- design spec
- page/state matrix
- component blueprint
- persisted visual source paths
- visual-source contract
- Visual IR or Level-3 handoff pack when implementation will follow
- asset notes
- design debt ledger
- `result-manifest.json`

## Blocker Conditions

Return `result=blocked` when approved design direction is missing, source artifacts cannot be accessed, page/state scope is contradictory, or the task does not permit required image-generation/file side effects.

## Review Conditions

Return `review_required=true` when the produced visual source needs approval before implementation.

## Example Next Task

```json
{
  "capability": "visual_implementation",
  "reason": "Approved visual source can be implemented by D2C"
}
```
