---
name: idea-to-design
description: Use when user has a product idea, partial concept, rough page direction, or scattered design materials and needs them turned into a structured design plan, staged visual drafts, and a formal design document for implementation reference.
---

# Idea To Design

## Overview

Turn vague product ideas into a formal design document and staged design assets.

This skill is not a general-purpose product consultant. It is a design progression system.

Default outcome:
- Level 1 lightweight design package: `Design-Spec.md`, `assets/`, `state.json`
- Level 3 implementation-ready UI package when formal UI mockups will be coded: design tokens, visual source contract, page briefs, parity checklist, and a checker-passing `implementation_gate`
- optional artifact and handoff manifests for orchestrated workflows
- optional recovery snapshots in `checkpoints/`

Standalone rule:
- this skill is standalone by default
- `PlanToDelivery` may consume its outputs, but `PlanToDelivery` is not required to run this skill
- outputs should stay useful for direct human review and for other orchestrators

Core rule:
- structured spec is source of truth
- images express decisions, not replace them
- approved mockups are visual sources, not implementation-ready specs by themselves
- formal UI work must be tokenized and page-briefed before coding
- `state.json` is session continuity and gate status source of truth
- all human-facing generated outputs must be in Chinese by default
- all human-facing UI copy should use formal product-ready wording, not explanatory placeholder labels

## When to Use

Use when user:
- has only a rough product idea and needs structure
- wants flows, pages, and interactions planned from limited input
- wants to use mature product patterns as references instead of specifying everything manually
- wants staged visual exploration with image generation
- wants existing design materials turned into a clean formal design document

Do not use when:
- task is purely technical architecture, API, or database design
- task is full brand system creation
- task is pixel-perfect final production design in professional design tools
- task is large multi-platform deep design for every screen at once

## Entry Modes

Choose one of three modes.

### 1. Start from idea
Use when input is vague, partial, or early-stage.

### 2. Continue current design
Use when `state.json`, draft docs, or image assets already exist.

### 3. Finalize design doc
Use when structure and visuals mostly exist and need formal consolidation.

## Core Principles

### task-flow-first
Define core user tasks first. Do not start from disconnected pages.

### spec-as-source-of-truth
`Design-Spec.md` and approved structure define product truth. Images must follow spec.

### reference-driven-hypothesis
When user input is incomplete, infer likely flows, pages, and visual directions from mature design patterns. Present them as editable hypotheses, not fixed truth.

### contextual-creative-direction
Visuals should fit product context, audience taste, and trust level. Do not force every project to look trendy, but do not accept generic AI-template output for core pages.

### stage-gated-progression
Do not jump forward without enough structure.

### selective-fidelity-escalation
Only elevate core pages to higher fidelity by default.

### designer-friendly-output
Final delivery must be easy to read. Process logs stay in background unless needed.

## Workflow

Follow five internal phases, plus Level 3 gates when implementation will follow.

### 1. Scope
Goal:
- define product purpose, target user, current scope, non-goals

Output:
- one-sentence product definition
- target user
- current scope
- non-goals
- candidate core task flows

Rules:
- ask as few questions as possible
- at most 1-3 critical questions before drafting
- if scope too large, cut to one core subproblem
- update `resume_packet` after scope changes
- keep `next_prompt_for_agent` executable by a fresh session

### 2. Structure
Goal:
- turn scope into product skeleton

Output:
- core task flows
- surface/page structure
- page inventory
- core vs supporting pages

Rules:
- flow before page
- structure references and visual references must stay separate
- default to 1-2 core flows
- default to 3-5 core pages for deep work
- checkpoint when structure becomes stable enough to continue in a new session

### 3. Visual Direction
Goal:
- establish one stable design direction before heavy image generation

Output:
- design direction
- `Creative Direction Summary`
- key visual principles
- text wireframes for core pages

Rules:
- provide 2-3 candidate visual directions when needed
- use `references/creative-direction-system.md` when visual direction feels generic, outdated, or high-impact
- default to a lightweight creative check: context fit, audience fit, one memorable move, anti-slop risk, and real content first
- choose one before high-fidelity work
- use text wireframes before image wireframes
- record chosen direction and rejected directions in `state.json`

### 4. Image Iteration
Goal:
- gradually refine visuals with image generation

Output:
- wireframes
- mid-fidelity visuals
- high-fidelity visuals for selected core pages

Rules:
- each round changes one main goal only
- record what to keep, what to change, what remains unresolved
- use `references/aesthetic-review-system.md` before accepting core-page high-fidelity visuals
- core pages should pass `Aesthetic Review` before final reference acceptance
- image-generated new features do not become official unless explicitly accepted
- update page-level fidelity and key asset refs after each accepted round

### 5. Finalize
Goal:
- produce a clean formal design document and, when needed, an implementation-ready handoff pack

Level 1 output:
- `Design-Spec.md`
- organized design assets
- updated `state.json`

Level 3 output for formal UI implementation:
- Level 1 output
- `DESIGN.md` and `tokens.json` generated or shaped with the `design-md` rules
- `visual-source-contract.json`
- compact page briefs under `page-style-briefs/`
- `implementation-parity-checklist.md`
- checker result recorded in `state.json`

Rules:
- final doc contains confirmed decisions only
- process traces stay outside main doc unless needed
- images first, text only for decisions, interactions, constraints, and implementation-critical style rules
- high-fidelity mockup approval does not open the implementation gate by itself
- write a fresh handoff summary before ending work
- refresh `next_prompt_for_agent` before pausing or ending work

## Deliverable Levels

Always prefer the lightest package that can safely support the next step.

### Level 1: concept/design package
Use for early ideas, internal exploration, and non-UI or non-implementation work.

Required:
- `Design-Spec.md`
- `assets/`
- `state.json`

### Level 2: visual source package
Use when visual mockups are reviewed but implementation is not yet starting.

Required:
- Level 1 output
- approved asset refs in `state.json`
- short visual source notes inside `Design-Spec.md` or `visual-source-contract.json`

### Level 3: implementation-ready UI package
Use automatically when formal UI mockups are approved and code implementation will follow.

Required:
- Level 2 output
- `DESIGN.md`
- `tokens.json`
- `visual-source-contract.json`
- `page-style-briefs/<page-id>.md` for each core implemented page
- `implementation-parity-checklist.md`
- `scripts/check-design-handoff.py` passes
- `state.json.implementation_gate.status = "open"`

Optional orchestration deliverables:
- `artifact-manifest.json`
- `approval-records.json`
- `handoff-manifest.json`
- `mockup-code-map.json` and `design-debt.json` only for long-lived implementation projects

Output gate:
- product/design document exists
- core flows and pages are defined or explicitly scoped
- design direction status is clear
- approved visual assets or equivalent visual source are recorded when implementation will follow
- Level 3 gate is open before coding starts
- resumable state is current
- any orchestrator-facing handoff manifest lists open questions and next action

Language rule:
- internal notes, state fields, and agent-only helper text may stay in English
- all final human-facing outputs, including design docs, page explanations, handoff text, and reviewable summaries, must be written in Chinese by default
- all final human-facing UI copy should read like real product content
- avoid labels such as "这里是详情", "这里展示数据", "按钮文案", "用户信息区域"
- for core pages, prefer near-production wording
- for supporting pages, wording may stay lighter but must not fall back to explanatory placeholders

Recommended default asset structure:

```text
assets/
  wireframes/
  mid-fi/
  hi-fi/
```

Only generate extra working files when project complexity justifies them.

Optional recovery structure:

```text
checkpoints/
  <timestamp>-<phase>-state.json
  <timestamp>-<phase>-spec.md
```

## Built-in Gate System

`design-process-gates` is absorbed into this skill. Do not treat gate control as an optional companion skill. `idea-to-design` owns the full path from idea to implementation-ready design handoff.

### Visual source gate
Track visual states separately: direction drafted, direction selected, wireframes drafted, mockups generated, local files verified, user reviewed, user accepted. Do not collapse these into a vague `visual_complete` status.

### Design token gate
When approved mockups will be implemented, generate or maintain `DESIGN.md` and `tokens.json`. Use `design-md` as the helper for syntax, linting, and exports; `idea-to-design` remains the owner of deciding that tokenization is required.

### Page brief gate
Every core implemented page needs a compact page brief. Keep each brief short: visual source, required regions, must-preserve rules, forbidden drift, and first-screen acceptance criteria. Avoid repeating global tokens in every brief.

### Implementation gate
`implementation_gate` stays `blocked` until Level 3 required files exist and the checker passes. If implementation starts without Level 3, label it as a user-waived exception in `state.json` and in the handoff notes.

### Parity gate
For UI implementation checkpoints, functional tests and builds are insufficient. The implementation consumer must identify the mockup/page brief, capture a mobile screenshot, compare structure/density/card anatomy/button hierarchy, and record differences as fixed, accepted deviation, user decision, or design debt.

### Change request rule
Development agents must not silently redesign approved mockups. If the design is impractical, create a design change request or design debt item instead of improvising the UI in code.

## Token Efficiency

Prefer low-context operation by default.

Rules:
- keep one main doc, one asset directory, and one state file
- ask minimal questions, then draft assumptions
- expand only core flows and core pages by default
- keep process logs out of final output
- load supporting reference files only for current phase
- use `checkpoints/` only at meaningful boundaries, not every tiny edit

Default scope:
- 1-2 core flows
- 3-5 core pages at higher fidelity
- supporting pages stay compressed

When continuing work:
- read `state.json` first
- avoid re-summarizing prior discussion unless needed
- update existing structure instead of re-generating it
- trust `resume_packet`, `current_focus`, and `handoff_notes` as first recovery source
- compare latest checkpoint only if current state is stale or contradictory
- if `next_prompt_for_agent` is valid, use it as the direct recovery instruction

When writing:
- prefer short fixed page sections
- avoid repeating design brief content on every page
- collapse repeated patterns instead of restating them
- move archival detail to optional working files only
- for Level 3, keep required files compact and link them instead of duplicating long visual descriptions

## Design-Spec Structure

Default `Design-Spec.md` structure:

1. Overview
2. Product Structure
3. Design Brief
4. Core Pages
5. Supporting Pages
6. Handoff Notes
7. Appendix

Guidelines:
- final document should stay concise
- core pages get detailed treatment
- supporting pages stay short
- edge pages may appear only in index/table form

## Reference-Driven Mode

When user input is incomplete:
- infer product type, core flows, page structures, interaction patterns, and visual directions
- use mature patterns to reduce user effort
- present outputs as editable hypotheses

Allowed:
- borrow patterns, structure ideas, interaction conventions, and visual inspiration

Not allowed:
- copy brand identity
- silently clone a specific product
- treat inferred references as final truth
- mix visual imitation with product definition without stating it

## Complexity Control

Default complexity limits:
- 1-2 core flows
- 3-5 core pages at high fidelity
- one main design document
- supporting pages kept short

If project grows too large:
- reduce scope
- choose one primary user journey
- postpone non-core screens
- avoid deep-designing everything at once

## Guardrails

Do not:
- force user to specify every detail up front
- let image outputs define product logic
- produce heavy multi-file output by default
- over-document non-core pages
- expand into full system design without clear need
- confuse work logs with final deliverables

Do:
- make assumptions explicit
- draft before over-questioning
- use mature patterns to reduce user effort
- keep final output readable for designers and developers
- preserve traceability through `state.json`
- keep `state.json` fresh enough that a crashed or new session can resume without replaying chat
- keep recovery quality high enough that a new session can continue within minutes from files only

## Escalation Rules

Only expand beyond default minimal package when:
- user asks for full archival detail
- project has many pages or multiple flows
- team handoff requires more structured records
- multiple design directions need retained history

Possible expanded files:
- iteration logs
- prompt logs
- rejected directions
- design debt notes

Main delivery remains `Design-Spec.md`.

## Success Criteria

This skill succeeds when:
- vague idea becomes clear product structure
- core flows and pages are defined without excessive user burden
- mature design patterns reduce clarification overhead
- visuals are produced in controlled stages
- final design document stays readable and not bloated
- designers can review it quickly
- Level 3 UI handoff has tokens, page briefs, visual contracts, and a passing checker
- developers can implement from it with minimal confusion and without silently drifting from approved mockups
