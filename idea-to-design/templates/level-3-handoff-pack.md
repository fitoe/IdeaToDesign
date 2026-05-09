# Level 3 Implementation Handoff Pack

> 用途：正式 UI 样稿已确认且后续要进入代码实现时使用。保持短、可检查、可被下游 Agent 快速读取。

## 1. Required Files

```text
Design-Spec.md
DESIGN.md
tokens.json
visual-source-contract.json
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
design-debt.json
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

## 3. page-style-briefs/<page-id>.md

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

`implementation_gate.status` may be `open` only when Level 3 required files exist, design-to-code inputs exist for target pages, and `scripts/check-design-handoff.py` passes. If the user waives the gate, record the waiver explicitly in `implementation_gate.waivers`.
