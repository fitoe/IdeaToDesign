---
name: idea-to-design
description: Use when a Javis/Kanban card needs product/design decisions, page/state inventory, visual direction, generated design sources, design review artifacts, or implementation-ready design handoff.
version: 3.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [design, visual-source, product-design, kanban-worker]
    related_skills: [PlanToDelivery, IdeaToTech, design-to-code]
---

# IdeaToDesign — Design Specialist Worker

## Overview

IdeaToDesign is a bounded design specialist for Javis/Kanban. It turns product intent and an active slice into design decisions, visual sources, page/state inventories, and handoff artifacts.

It does not own the project board, technical architecture, or implementation. It may suggest gates and downstream cards; Javis records them.

## When to Use

Use this skill when a card asks for product/design specs, page inventory, user flows, visual direction, generated design boards, visual-source confirmation, design freeze evidence, or implementation handoff.

Do not use it for coding from an already approved design source; route that to `design-to-code`.

## Input Contract

Expect a Kanban card or equivalent handoff with:

```yaml
goal:
scope:
inputs:
allowed_changes:
acceptance:
evidence_required:
execution_mode: fast | controlled | strict
```

If a strict P2D envelope/digest/permit is provided, obey it. Otherwise operate from the lightweight card contract and write only permitted artifacts.

## Outputs

Return concise evidence that Javis can ingest:

```json
{
  "provider": "idea-to-design",
  "result": "completed | partial | blocked | failed",
  "produced_artifacts": [],
  "design_decisions": [],
  "open_questions": [],
  "blockers": [],
  "suggested_kanban_updates": [],
  "review_required": true
}
```

Typical artifacts:

- `Design-Spec.md`
- `page-matrix.json`
- `visual-source-contract.json`
- `implementation-blueprint.json`
- `component-blueprint.json`
- `visual-ir/*`
- generated design images or boards
- design review notes

## Design Source Rules

1. User-facing “设计图 / 视觉源 / 视觉板 / 设计稿 / mockup” should be generated through the configured image-generation workflow and saved as raw design-source artifacts.
2. Browser screenshots, coded previews, and Playwright captures are verification evidence, not design drawings, unless the user explicitly approves them as the source.
3. Complete decisionable states are required. Avoid cropped half-page boards as approval artifacts.
4. Homepage/key visual direction usually needs a single complete high-quality design image. Secondary pages may be grouped only if each page/state remains readable and complete.
5. After generating an approval image, deliver it promptly. Do not run extra critique/vision analysis unless the user asks for inspection or the file/tool failed.

## Strong-Gate Visual Generation Guard

When the user asks to generate a visual draft, design mockup, visual board, homepage direction, or “视觉稿” inside a strong-gate Javis/Kanban project, treat it as a design-provider task, not as a free-standing image-generation action.

Required behavior:

1. Verify the active slice/card names released scope, page/state target, allowed changes, approval target, and downstream dependency impact.
2. If the user is restarting, shrinking, or replacing scope, require Javis to create or update the corresponding scope-change or visual-source gate before generation.
3. Do not generate visual drafts directly from the main conversation when the project requires Kanban gates, even if the request sounds small, such as “只做首页”, “只要 Hero”, or “先出个视觉稿”.
4. A generated draft is review evidence only. It does not unlock D2C or implementation until Javis records explicit user approval.
5. If older visual sources are rejected or superseded, mark them stale in the design artifacts/handoff and avoid reusing them as visual references unless the user explicitly restores them.

## Mode Behavior

| Mode | Behavior |
|---|---|
| `fast` | lightweight page/state decisions or quick visual source for a small slice |
| `controlled` | design-source contract, review packet, page matrix, implementation handoff |
| `strict` | follow P2D envelope/digest/permit/prewrite/audit requirements exactly |

Use `controlled` when the output unlocks D2C or another phase.

## Gate Suggestions

Suggest a Kanban gate when a design decision controls downstream start:

```yaml
title:
type: gate
decision: visual-source approval | product/content approval | scope freeze
released_scope:
required_evidence:
downstream_cards:
```

Do not mark gates complete yourself. Javis records approval and dependencies.

## Handoff to D2C

A D2C-ready handoff should include:

- approved visual source path;
- target page/routes/states;
- page/section order and density expectations;
- asset roles and must-not-substitute rules;
- responsive expectations;
- pass criteria and review requirement;
- known debts or allowed deviations.

If these are missing, return `partial` or suggest a follow-up design/handoff card instead of pretending implementation is ready.

## Common Pitfalls

| Pitfall | Fix |
|---|---|
| Acting as global project owner | Return artifacts and gate suggestions; let Javis update Kanban |
| Producing prose without durable artifacts | Save design sources/contracts and reference paths |
| Treating generated source as approved automatically | Route to review unless explicit approval exists |
| Sending local screenshots as design稿 | Label screenshots as implementation/verification evidence only |
| Reopening broad exploration after approval | Work only on missing/stale/rejected scope |

## Verification Checklist

- [ ] Active slice and released scope are explicit.
- [ ] Visual artifacts have stable file paths.
- [ ] Review-required outputs name the exact approval target.
- [ ] D2C handoff contains source, route/state, section, asset, responsive, and pass criteria facts.
- [ ] Suggested Kanban gates are advisory and dependency-ready.
