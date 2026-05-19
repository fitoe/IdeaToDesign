# Product Visual Design Task v1

Capability: `product_visual_design`

## Purpose

Create visual direction, information architecture, page/state matrix, and approval-ready design plan from product requirements.

## Envelope

Use `kanban-capability-task/v1` with `capability=product_visual_design`.

## Required Inputs

- `project_context`: business/product context.
- `target_pages`: pages or screens to design.
- `requirements`: user goals, conversion goals, product constraints.
- `acceptance_criteria`: what review should judge.

## Optional Inputs

- `brand_constraints`
- `reference_sites`
- `required_states`
- `implementation_constraints`
- `existing_artifacts`

## Blocker Conditions

Return `blocked=true` only when:
- project context is missing;
- target pages are missing;
- requirements contradict each other and cannot be resolved safely;
- required existing artifacts are referenced but inaccessible.

## Review Conditions

Return `review_required=true` when:
- visual direction needs approval;
- multiple viable directions require selection;
- design gate must happen before implementation.

## Example

```json
{
  "schema_version": "kanban-capability-task/v1",
  "task_id": "kb_design_001",
  "correlation_id": "site-home-design",
  "capability": "product_visual_design",
  "objective": "Create homepage visual direction for approval",
  "inputs": {
    "project_context": "International landing page for B2B service",
    "target_pages": ["home"],
    "requirements": ["formal", "low text density", "clear CTA"],
    "acceptance_criteria": ["design direction ready for user approval"]
  },
  "orchestration": {
    "origin": "kanban",
    "review_policy": "design_gate_required"
  }
}
```
