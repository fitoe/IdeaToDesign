---
name: idea-to-design
description: Use when user has a product idea, partial concept, rough page direction, or scattered design materials and needs them turned into a structured design plan, staged visual drafts, and a formal design document for implementation reference.
---

# Idea To Design

## Overview

Turn vague product ideas into a formal design document and staged design assets.

This skill is not a general-purpose product consultant. It is a design progression system.

Default outcome:
- one formal design doc: `Design-Spec.md`
- one design asset directory: `assets/`
- one machine-readable state file: `state.json`

Core rule:
- structured spec is source of truth
- images express decisions, not replace them

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

### stage-gated-progression
Do not jump forward without enough structure.

### selective-fidelity-escalation
Only elevate core pages to higher fidelity by default.

### designer-friendly-output
Final delivery must be easy to read. Process logs stay in background unless needed.

## Workflow

Follow five internal phases.

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

### 3. Visual Direction
Goal:
- establish one stable design direction before heavy image generation

Output:
- design direction
- key visual principles
- text wireframes for core pages

Rules:
- provide 2-3 candidate visual directions when needed
- choose one before high-fidelity work
- use text wireframes before image wireframes

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
- image-generated new features do not become official unless explicitly accepted

### 5. Finalize
Goal:
- produce a clean formal design document

Output:
- `Design-Spec.md`
- organized design assets
- updated `state.json`

Rules:
- final doc contains confirmed decisions only
- process traces stay outside main doc unless needed
- images first, text only for decisions, interactions, and constraints

## Default Deliverables

Always prefer minimal output.

Default deliverables:
- `Design-Spec.md`
- `assets/`
- `state.json`

Recommended default asset structure:

```text
assets/
  wireframes/
  mid-fi/
  hi-fi/
```

Only generate extra working files when project complexity justifies them.

## Token Efficiency

Prefer low-context operation by default.

Rules:
- keep one main doc, one asset directory, and one state file
- ask minimal questions, then draft assumptions
- expand only core flows and core pages by default
- keep process logs out of final output
- load supporting reference files only for current phase

Default scope:
- 1-2 core flows
- 3-5 core pages at higher fidelity
- supporting pages stay compressed

When continuing work:
- read `state.json` first
- avoid re-summarizing prior discussion unless needed
- update existing structure instead of re-generating it

When writing:
- prefer short fixed page sections
- avoid repeating design brief content on every page
- collapse repeated patterns instead of restating them
- move archival detail to optional working files only

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
- developers can implement from it with minimal confusion
