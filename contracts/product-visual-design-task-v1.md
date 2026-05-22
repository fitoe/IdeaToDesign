# Product Visual Design Task v1

Capability: `product_visual_design`

## Purpose

Create visual direction, information architecture, page/state matrix, and approval-ready design plan from product requirements.

## Envelope

Use `kanban-capability-task/v1` with `capability=product_visual_design`.

IdeaToDesign must be admitted by PlanToDelivery/Javis before producing canonical design artifacts for a P2D slice. Chat history or an informal `继续` is not an execution envelope.

## Required Inputs

This contract is carried inside a `kanban-capability-task/v1` envelope admitted by PlanToDelivery. The envelope must include:

- `schema: kanban-capability-task/v1`
- `task_id`
- `capability: product_visual_design`
- `project_root`: absolute path to target project
- `active_slice`: bounded product/page/state scope
- `input_artifact_refs`: prior briefs, research, screenshots, references, or existing artifacts; may be empty only when `design_contract` contains sufficient product facts
- `output_root`: provider artifact directory; result manifest path is always `output_root/result-manifest.json`
- `expected_outputs`: must include `result-manifest.json` and design artifacts such as design spec or page matrix
- `verification_expectations`: review/evidence expectations
- `allowed_side_effects`: explicit file/image-generation/write side effects permitted for the slice
- `review_policy`: design review and approval routing
- `blocking_policy`: missing/contradictory fact handling
- `design_contract`: see below
- `kanban_constraints`: running card/gate/dependency constraints from PlanToDelivery

`design_contract` must include:

- `project_context`: business/product context
- `target_pages`: pages or screens to design
- `requirements`: user goals, conversion goals, product constraints
- `acceptance_criteria`: what review should judge

## Optional Inputs

- `brand_constraints`
- `reference_sites`
- `required_states`
- `implementation_constraints`
- `existing_artifacts`
- `content_inventory`
- `domain_risk_constraints`

## Blocker Conditions

Return `result=blocked` only when project context is missing, target pages are missing, requirements contradict each other and cannot be resolved safely, or required existing artifacts are referenced but inaccessible.

## Review Conditions

Return `review_required=true` when visual direction needs approval, multiple viable directions require selection, or design gate must happen before visual source creation/implementation.

## Example

```json
{
  "schema": "kanban-capability-task/v1",
  "task_id": "kb_design_001",
  "capability": "product_visual_design",
  "project_root": "/abs/project",
  "active_slice": {"id": "home-design", "pages": ["home"]},
  "input_artifact_refs": [],
  "output_root": "project-state/design/home-design",
  "expected_outputs": ["Design-Spec.md", "page-matrix.json", "result-manifest.json"],
  "verification_expectations": ["design direction ready for user approval"],
  "allowed_side_effects": ["write output_root design artifacts"],
  "review_policy": {"design_gate_required": true},
  "blocking_policy": {"missing_project_context": "blocked"},
  "design_contract": {
    "project_context": "International landing page for B2B service",
    "target_pages": ["home"],
    "requirements": ["formal", "low text density", "clear CTA"],
    "acceptance_criteria": ["design direction ready for user approval"]
  },
  "kanban_constraints": {"required": true, "design_card_id": "kb_design_001"}
}
```
