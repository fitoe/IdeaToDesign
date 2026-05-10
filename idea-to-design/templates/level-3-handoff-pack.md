# Level 3 Implementation Handoff Pack

> 用途：正式 UI 样稿已确认且后续要进入代码实现时使用。保持短、可检查、可被下游 Agent 快速读取。

## 1. Required Files

```text
Design-Spec.md
DESIGN.md
tokens.json
visual-source-contract.json
visual-proposals.json
visual-contracts/
  <page-id>.json
implementation-blueprint.json
page-matrix.json
component-blueprint.json
debt-ledger.json
page-style-briefs/
  <page-id>.md
implementation-parity-checklist.md
design-to-code-inputs/
  manifest.json
  <mockup-id>-<page-id>.png
pre-implementation-briefs/
  <page-id>.md
state.json
scripts/check-design-handoff.py
```

可选，仅长线项目使用：

```text
mockup-code-map.json
implementation-snapshots/
```

## 2. visual-source-contract.json

```json
{
  "version": "1.0",
  "mockups": [
    {
      "id": "mockup-001",
      "asset": "assets/hi-fi/mockup-001.png",
      "status": "approved",
      "covers": ["page-id"],
      "must_preserve": ["关键结构、信息层级、按钮主次"],
      "flexible": ["具体图标、非关键装饰、少量文案长度"],
      "not_allowed": ["未经记录的重设计", "PC 化布局", "偏离已确认视觉方向"]
    }
  ]
}
```

## 2. Visual Freeze and post-visual extraction

`implementation-blueprint.json` is valid only after the approved visual source is frozen and extracted. Pre-visual style hypotheses are useful for prompting, but they are not implementation constraints.

### state.json visual_freeze

```json
{
  "visual_freeze": {
    "status": "approved",
    "approved_at": "YYYY-MM-DDTHH:mm:ssZ",
    "source_version": "home-large-v2",
    "source_paths": ["assets/hi-fi/home-large-v2.png"],
    "covered_pages": ["home"],
    "visual_source_mode": "binding",
    "post_visual_extraction_status": "complete",
    "post_visual_extracted_at": "YYYY-MM-DDTHH:mm:ssZ"
  }
}
```

### extraction rules

After user approval:
- extract visual tokens, component anatomy, background system, typography hierarchy, spacing rhythm, card shapes, navigation style, first-screen proportions, and key visual anchors from the approved image
- update `DESIGN.md`, `tokens.json`, `visual-source-contract.json`, `visual-contracts/*`, page briefs, and compact blueprint files from the image
- if the approved image improves on pre-visual text without changing product rules, the image wins and text hypotheses are marked superseded
- if the image adds product-like elements, record them in `visual-proposals.json` rather than silently adding them to product scope

### visual-proposals.json

```json
{
  "proposals": [
    {
      "id": "home-extra-metric-card",
      "source_image": "assets/hi-fi/home-large-v2.png",
      "type": "image_generated_product_like_element",
      "decision": "defer",
      "note": "Generated metric card looks useful but was not part of approved product scope."
    }
  ]
}
```

## 3. Compact implementation blueprint package

`design-to-code` 默认先读这些文件。它们必须短、结构化、可按 pass 加载，避免实现阶段反复读完整设计文档和图片。

### implementation-blueprint.json

```json
{
  "version": "1.0",
  "mode": "blueprint_driven",
  "visual_freeze_ref": {
    "status": "approved",
    "source_version": "home-large-v2",
    "post_visual_extraction_status": "complete"
  },
  "source_priority": ["user_requirement", "product_spec", "approved_image", "engineering_constraint", "accepted_deviation"],
  "default_goal": "20% time for 80% visible coverage, then refine core fidelity",
  "read_order": ["implementation-blueprint.json", "page-matrix.json", "component-blueprint.json", "debt-ledger.json"],
  "pass_sequence": ["foundation", "coverage", "refinement", "fidelity"],
  "current_pass": "foundation",
  "reference_viewport": { "width": 390, "height": 844 },
  "routes": [{ "page_id": "home", "route": "/", "priority": "core", "target_maturity": "L4" }],
  "core_pages": ["home"],
  "foundation_components": ["AppShell", "BaseCard", "PrimaryButton"],
  "verification_policy": {
    "coverage": "all routes/pages/major sections",
    "system": "tokens, shell, component consistency",
    "fidelity": "core pages and first screens only unless user requests more"
  },
  "read_by_pass": {
    "foundation": ["tokens.json", "component-blueprint.json"],
    "coverage": ["page-matrix.json", "design-to-code-inputs/manifest.json"],
    "refinement": ["component-blueprint.json", "debt-ledger.json"],
    "fidelity": ["visual-contracts/<page-id>.json", "page-style-briefs/<page-id>.md"]
  }
}
```

### page-matrix.json

```json
{
  "version": "1.0",
  "maturity_levels": ["L0 route-ready", "L1 skeleton-ready", "L2 content-ready", "L3 system-styled", "L4 core-fidelity", "L5 functional-ready"],
  "pages": [
    {
      "page_id": "home",
      "route": "/",
      "priority": "core",
      "target_maturity": "L4",
      "current_maturity": "L0",
      "first_screen_priority": true,
      "sections": ["hero", "quick-actions", "recent-list"],
      "content_strategy": "near-production mock content",
      "asset_level": "A|B|C|D",
      "open_debt_ids": []
    }
  ]
}
```

### component-blueprint.json

```json
{
  "version": "1.0",
  "tiers": {
    "foundation_first": ["AppShell", "PageContainer", "BaseCard", "PrimaryButton"],
    "extract_after_repetition": ["StatsCard", "ListItem"],
    "page_local_first": ["HomeHero"],
    "deferred": ["RareModal"]
  },
  "rules": [
    "first pass may duplicate page-local structures for coverage speed",
    "extract repeated patterns after they appear 2-3 times",
    "do not let abstraction block visible coverage"
  ]
}
```

### debt-ledger.json

```json
{
  "version": "1.0",
  "items": [
    {
      "id": "asset-home-hero",
      "page": "home",
      "type": "asset_fallback|visual|content|mock|interaction|fidelity|engineering_deviation",
      "severity": "low|medium|high|blocker",
      "revisit_pass": "refinement|fidelity|functional-wiring",
      "status": "open|accepted|fixed",
      "note": ""
    }
  ]
}
```

## 4. page-style-briefs/<page-id>.md

```md
# <页面名> Page Style Brief

- page_id: <page-id>
- visual_source: <mockup-id>
- implementation_target: <route/file if known>

## Required Regions
- region: page-header
  - role:
  - style:
  - must_preserve:
- region: main-content
  - role:
  - style:
  - must_preserve:

## Must Preserve
-

## Forbidden Drift
-

## First-screen Acceptance
- viewport: mobile 390x844 unless project specifies otherwise
- must show:
- must not show:
```

## 4. implementation-parity-checklist.md

```md
# Implementation Parity Checklist

For each UI checkpoint:

## Design Input
- [ ] Mockup ID identified
- [ ] Page style brief read
- [ ] DESIGN.md / tokens.json read

## Implementation Check
- [ ] Navigation/header shape matches source
- [ ] First-screen density is comparable
- [ ] Card anatomy and button hierarchy match source
- [ ] Status colors and component roles follow tokens
- [ ] No silent redesign or PC-style fallback

## Verification
- [ ] Functional checks pass
- [ ] Mobile screenshot captured
- [ ] Difference recorded as fixed / accepted deviation / user decision / design debt
```

## 5. design-debt.json optional shape

```json
{
  "items": [
    {
      "page": "page-id",
      "mockup": "mockup-id",
      "issue": "",
      "severity": "low|medium|high",
      "status": "open|accepted|fixed",
      "accepted_by_user": false,
      "next_action": ""
    }
  ]
}
```

## 6. Design-to-code Inputs

`idea-to-design` prepares these; `design-to-code` consumes them for implementation.

```json
{
  "items": [
    {
      "page_id": "page-id",
      "mockup_id": "mockup-001",
      "source": "assets/hi-fi/mockup-board.png",
      "crop": "design-to-code-inputs/mockup-001-page-id.png",
      "crop_box": [0, 0, 390, 844],
      "size": [390, 844]
    }
  ]
}
```

Each implemented page also needs `pre-implementation-briefs/<page-id>.md` using the `design-to-code` Pre-Implementation Brief shape.

## 7. State Rule

`implementation_gate.status` may be `open` only when Level 3 required files exist, the compact implementation blueprint package exists, design-to-code inputs exist for target pages, and `scripts/check-design-handoff.py` passes. If the user waives the gate, record the waiver explicitly in `implementation_gate.waivers`.

Default downstream read path:
1. `state.json`
2. `implementation-blueprint.json`
3. only the current pass files listed in `implementation-blueprint.json.read_by_pass`

Do not require downstream agents to load full `Design-Spec.md`, all page briefs, all visual contracts, or source images unless the current pass or a blocker needs them.
