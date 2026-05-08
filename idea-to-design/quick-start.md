# Quick Start

Use `idea-to-design` in one of three modes:

1. `Start from idea`
2. `Continue current design`
3. `Finalize design doc`

## Default Output

- `Design-Spec.md`
- `assets/`
- `state.json`

## Standalone Rule

- usable without `PlanToDelivery`
- `PlanToDelivery` may consume the output, but is not required
- when orchestrated, optional manifests may summarize artifacts, approvals, and handoff status

## Language Rule

- internal agent-facing content may stay in English
- all human-facing outputs should default to Chinese
- all human-facing UI copy should use formal content, not explanatory placeholders

## Default Behavior

- ask minimal questions
- draft assumptions early
- use mature design patterns when user input is incomplete
- use contextual creative direction to avoid generic or outdated visuals
- focus on 1-2 core flows
- focus on 3-5 core pages
- keep final output light and readable

## Internal Phase Order

1. Scope
2. Structure
3. Visual Direction
4. Image Iteration
5. Finalize

## Hard Rules

- task flow before page
- spec before image
- text wireframe before image wireframe
- Creative Direction Summary before high-fidelity core visuals
- Aesthetic Review before accepting core-page high-fidelity assets
- only core pages go high fidelity by default
- final doc includes confirmed decisions only
- process logs stay outside main doc unless needed

## Continue Mode

When continuing work:
- read `state.json` first
- trust `resume_packet`, `current_focus`, and `handoff_notes` first
- compare latest checkpoint only if current state looks stale or inconsistent
- do not re-summarize prior discussion unless needed
- update existing structure instead of rebuilding it

## Complexity Limits

Default:
- 1-2 core flows
- 3-5 core pages at higher fidelity
- one main design doc

If project becomes too large:
- cut scope
- choose one primary journey
- postpone non-core pages

## Before Pausing

Before ending or pausing a session, update:
- `resume_packet.summary`
- `resume_packet.next_recommended_step`
- `resume_packet.next_prompt_for_agent`
- `handoff_notes.for_next_session`

## Main Goal

Turn vague ideas into a formal design document and staged design assets without making user specify everything manually.
