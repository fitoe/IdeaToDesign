# Kanban-Capable IdeaToDesign Provider Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task after the PlanToDelivery capability envelope is accepted. IdeaToDesign is a provider, not the kanban orchestrator.

**Goal:** Adapt IdeaToDesign so it can serve kanban as a decoupled provider for product visual design and visual source creation.

**Architecture:** IdeaToDesign accepts a neutral capability task envelope and returns a neutral result manifest. It owns design exploration, page/state matrix, visual source generation, and design gate evidence. It does not own kanban task graph or provider selection.

**Tech Stack:** Markdown skill docs, JSON-schema-like contracts, design artifacts, visual-source contracts, PlanToDelivery-compatible result manifest.

---

## Capability Scope

IdeaToDesign should advertise these capabilities:

```json
{
  "capabilities": [
    "product_visual_design",
    "visual_source_creation"
  ]
}
```

### `product_visual_design`

Turns a product idea, page requirement, or stage objective into design strategy and visual direction.

Expected artifacts:
- positioning summary
- information architecture
- page/state matrix
- visual direction notes
- approval gate recommendation

### `visual_source_creation`

Turns approved design direction into implementation-ready visual sources.

Expected artifacts:
- design spec
- implementation blueprint
- page/state source list
- component blueprint
- asset notes
- design debt ledger

## Provider Boundaries

- IdeaToDesign must not manage kanban states directly.
- IdeaToDesign must not decide cross-provider task order.
- IdeaToDesign may return `review_required=true` when visual direction needs approval.
- IdeaToDesign may return `blocked=true` only when required input is missing or contradictory.
- IdeaToDesign should never label normal design review as `blocked`.

## Input Contract v1

```json
{
  "schema_version": "kanban-capability-task/v1",
  "capability": "product_visual_design",
  "objective": "Create approved visual direction for the homepage",
  "inputs": {
    "project_context": "...",
    "target_pages": [],
    "brand_constraints": [],
    "reference_sites": [],
    "required_states": [],
    "implementation_constraints": []
  },
  "orchestration": {
    "origin": "kanban",
    "task_id": "kb_design_001",
    "review_policy": "design_gate_required"
  }
}
```

## Result Manifest v1

```json
{
  "schema_version": "kanban-capability-result/v1",
  "capability": "product_visual_design",
  "status": "completed",
  "summary": "Visual direction and page/state matrix drafted for approval.",
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

## Task Breakdown

### Task 1: Add provider manifest

**Objective:** Declare IdeaToDesign capabilities without coupling to PlanToDelivery internals.

**Files:**
- Create: `contracts/provider-manifest.json`

**Required fields:**
- `schema_version: provider-manifest/v1`
- `provider_id: idea-to-design`
- `capabilities: product_visual_design, visual_source_creation`
- `input_schema_refs`
- `result_schema_ref`
- `review_policy_notes`

**Verification:**
```bash
python3 -m json.tool contracts/provider-manifest.json >/tmp/i2d-provider-manifest.json
python3 - <<'PY'
import json
m=json.load(open('contracts/provider-manifest.json'))
assert m['schema_version']=='provider-manifest/v1'
assert 'product_visual_design' in m['capabilities']
assert 'visual_source_creation' in m['capabilities']
PY
```

**Commit:**
```bash
git add contracts/provider-manifest.json
git commit -m "docs: add IdeaToDesign kanban provider manifest"
```

### Task 2: Add input contract documentation

**Objective:** Specify required/optional inputs for design provider tasks.

**Files:**
- Create: `contracts/product-visual-design-task-v1.md`
- Create: `contracts/visual-source-creation-task-v1.md`

**Verification:**
- Docs include required inputs, optional inputs, validation failures, and examples.
- Docs state missing approval/context may return `blocked=true`.

**Commit:**
```bash
git add contracts/*-task-v1.md
git commit -m "docs: define IdeaToDesign kanban task contracts"
```

### Task 3: Add result manifest documentation

**Objective:** Normalize design output for downstream D2C and P2D review gates.

**Files:**
- Create: `contracts/design-result-manifest-v1.md`

**Verification:**
- Manifest defines artifacts for design spec, page matrix, component blueprint, and debt ledger.
- Manifest defines `review_required` semantics.
- Manifest defines downstream `visual_implementation` next task recommendation.

**Commit:**
```bash
git add contracts/design-result-manifest-v1.md
git commit -m "docs: define IdeaToDesign result manifest"
```

### Task 4: Add kanban adapter notes to skill docs

**Objective:** Teach runtime skill how to respond when invoked through kanban envelope.

**Files:**
- Modify: skill source `SKILL.md` or equivalent runtime doc after locating actual source.

**Verification:**
- Existing standalone idea-to-design workflow remains intact.
- New section says kanban mode is contract I/O only, not orchestration ownership.

**Commit:**
```bash
git add SKILL.md contracts/
git commit -m "docs: document IdeaToDesign kanban provider mode"
```

---

## Acceptance Criteria

- IdeaToDesign can be selected by capability, not hard-coded name.
- It can produce design artifacts that D2C can consume later.
- Visual approval remains a review gate, not a blocker.
- Missing/contradictory inputs are the only normal design-time blockers.
- Tactical design references remain loadable but not kanban-aware.
