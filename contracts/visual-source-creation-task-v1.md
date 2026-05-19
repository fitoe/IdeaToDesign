# Visual Source Creation Task v1

Capability: `visual_source_creation`

## Purpose

Turn approved design direction into implementation-ready visual source artifacts for downstream implementation providers.

## Envelope

Use `kanban-capability-task/v1` with `capability=visual_source_creation`.

## Required Inputs

- `approved_design_direction`: text, file, board, or explicit approval reference.
- `target_pages`: pages/screens and states to materialize.
- `implementation_constraints`: platform, viewport, framework, asset constraints.
- `acceptance_criteria`: readiness expectations for downstream implementation.

## Expected Artifacts

- design spec;
- page/state matrix;
- component blueprint;
- visual source paths;
- asset notes;
- design debt ledger.

## Blocker Conditions

Return `blocked=true` when approved design direction is missing, source artifacts cannot be accessed, or page/state scope is contradictory.

## Review Conditions

Return `review_required=true` when the produced visual source needs approval before implementation.

## Example Next Task

```json
{
  "capability": "visual_implementation",
  "reason": "Approved visual source can be implemented by D2C"
}
```
