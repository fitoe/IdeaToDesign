# IdeaToDesign

[![Skill](https://img.shields.io/badge/agent--skill-IdeaToDesign-7c3aed)](#)
[![Provider](https://img.shields.io/badge/Javis%20%2F%20PlanToDelivery-Kanban%20Provider-0ea5e9)](#)

**IdeaToDesign turns a rough product idea into a reviewable design package.**

It is built for agent workflows where you do not want another pile of vague prompts: you want flows, page structure, visual direction, design gates, and handoff artifacts that downstream technical planning and implementation agents can trust.

## Why it is useful

- Start from a sentence, end with a structured design direction.
- Convert fuzzy product intent into user flows, pages, and visual priorities.
- Keep creative direction contextual instead of generic “AI SaaS” styling.
- Produce practical artifacts: design specs, visual DNA, page briefs, and implementation handoff notes.
- Work as a standalone design skill or as a provider inside a larger delivery system.

## Kanban provider mode

IdeaToDesign is a **Javis / PlanToDelivery V2 design provider**.

Through `contracts/provider-manifest.json`, it exposes:

- `product_visual_design`
- `visual_source_creation`

When orchestrated by PlanToDelivery, work is routed through Hermes Kanban gates. PlanToDelivery owns provider routing, progress, review, and canonical board state; IdeaToDesign owns the active design slice and returns `kanban-capability-result/v1` artifacts.

```text
Idea -> IdeaToDesign -> visual/design handoff
              ^
              |
      PlanToDelivery Kanban gates
```

## What is inside

- `idea-to-design/SKILL.md` — the runtime skill kernel
- `contracts/` — provider and task contracts
- `docs/provider-collaboration-v2.md` — cross-provider boundaries
- `templates/` and `references/` — design specs, gates, prompt patterns, review checklists

## Quick start

Copy the skill directory into your agent skill path, or use this repository as the source project for your own skill runtime.

Start with a small scope:

- one core user flow
- 3–5 key pages
- a lightweight design spec
- one approved visual direction

## Design philosophy

IdeaToDesign is not a “generate a pretty mockup” shortcut. It is a design reasoning layer for agentic delivery: small enough to reuse, structured enough to review, and strict enough to prevent beautiful but unbuildable output.
